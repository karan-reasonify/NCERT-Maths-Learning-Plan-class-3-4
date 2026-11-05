# -*- coding: utf-8 -*-
"""Class 3/4 flow gate: the learning flow and the media / tool / question rules of the Class 3-4 pipeline.

It replaces the Class 6-8 `skeleton.py` (hook + idea topics + Questions topics + summary) because the Class 3-4 flow
is a different shape:

    OPENING TOPIC (source_type "framing")      hook video  ->  exploration tool (the first approved tool)
    IDEA TOPICS   ("instructional/exploration") concept video -> its matching tool (-> NCERT practice on the tool),
                                                repeated only where it adds value; a small concept may be one image
    REVIEW TOPIC  ("summary")                  short revision / assessment using concepts already covered

Concept roles (concept["source_segment_role"]):
    hook     the hook story video                       explore  the exploration tool, right after the hook
    story    one concept story video                    image    one real-life image (no video, no tool needed)
    tool     the concept tool (+ its NCERT practice)    review   revision of what was already taught

Everything is checked from the built plan plus the chapter config; nothing here needs the book. Messages are prefixed
"flow:" by gate_runner. Two stages (config["stage"]): "structure" checks the shape and the media decisions only (the
approval stop); "full" (default) also needs every story brief, image brief and tool spec complete.

    python -B flow_c34.py <plan.json> [chapter.config.json]
"""
from __future__ import annotations

import io
import json
import re
import sys

from .media_content import walk_topics

DEFAULTS = {
    "stage": "full",
    "video_max_seconds": {"hook": 90, "concept": 150},
    "idea_topic_concept_range": (1, 6),
    "max_tool_controls": 4,
    "max_tool_questions": 6,
    "max_notice_prompts": 3,
    "max_instruction_words": 15,
    "max_sentence_words": 16,
    "review_max_concepts": 2,
    "explore_tool_no": 1,
    "tool_map_required": True,
    "question_kinds": ("example", "exercise", "prompt"),
    "framing_source_type": "framing",
    "idea_source_type": "instructional/exploration",
    "summary_source_type": "summary",
}

ROLES = {"hook", "explore", "story", "image", "tool", "review"}
LECTURE = re.compile(
    r"\b(in this video|in today'?s (?:video|lesson)|today we (?:will|are going to) learn|let'?s learn|let us learn|"
    r"definition of|this lesson|lecture)\b", re.I)
HOOK_KEYS = ("characters", "setting", "situation", "open_question")
CONCEPT_KEYS = ("characters", "setting", "situation", "problem", "thread", "leads_to")
IMAGE_KEYS = ("real_life", "shows", "caption")
TOOL_KEYS = ("learning_objective", "screen", "controls", "instruction", "feedback", "done_when", "hint_ladder")


def _cfg(config, key):
    return (config or {}).get(key, DEFAULTS[key])


def _words(text):
    return len((text or "").split())


def _ws(text):
    return " ".join((text or "").split())


def _concepts(plan):
    """[(topic, concept)] in document order."""
    return [(t, c) for t in walk_topics(plan) for c in t.get("concepts") or []]


def _nodes(topic, concept, kind):
    cid = concept.get("concept_id")
    return [m for m in topic.get("media") or [] if m.get("type") == kind and m.get("concept_id") == cid]


def _all_nodes(plan, kind):
    return [(t, m) for t in walk_topics(plan) for m in t.get("media") or [] if m.get("type") == kind]


def _present(d, keys):
    """The keys of `keys` that are missing or empty in dict d."""
    d = d or {}
    return [k for k in keys if not d.get(k)]


# ------------------------------------------------------------------ the flow shape
def _check_shape(plan, topics, config, problems):
    if len(topics) < 3:
        problems.append("a chapter needs an opening topic, at least one idea topic and a review topic "
                        "(found %d topic(s))" % len(topics))
        return
    framing, idea, summary = (_cfg(config, k) for k in ("framing_source_type", "idea_source_type",
                                                          "summary_source_type"))
    opening, review = topics[0], topics[-1]
    lo, hi = _cfg(config, "idea_topic_concept_range")

    # ---- opening: hook video, then the exploration tool, nothing else ----
    if opening.get("source_type") != framing:
        problems.append("%s: the first topic must be the opening (source_type %r), it is %r"
                        % (opening.get("topic_id"), framing, opening.get("source_type")))
    roles = [c.get("source_segment_role") for c in opening.get("concepts") or []]
    if roles != ["hook", "explore"]:
        problems.append("%s: the opening topic must be exactly [hook video, exploration tool] with the tool right "
                        "after the hook, found roles %s" % (opening.get("topic_id"), roles))
    if opening.get("topic_objective"):
        problems.append("%s: the opening topic carries no topic_objective" % opening.get("topic_id"))
    for c in opening.get("concepts") or []:
        if not c.get("is_enrichment"):
            problems.append("%s: the %s concept of the opening must be enrichment (no objective)"
                            % (c.get("concept_id"), c.get("source_segment_role")))

    # ---- idea topics ----
    for t in topics[1:-1]:
        tid = t.get("topic_id")
        if t.get("source_type") != idea:
            problems.append("%s: a middle topic must be an idea topic (source_type %r), it is %r"
                            % (tid, idea, t.get("source_type")))
            continue
        if not t.get("topic_objective"):
            problems.append("%s: idea topic is missing its topic_objective" % tid)
        cs = t.get("concepts") or []
        if not lo <= len(cs) <= hi:
            problems.append("%s: %d concept(s) (keep %d to %d; each concept video is followed by at most one tool)"
                            % (tid, len(cs), lo, hi))
        for i, c in enumerate(cs):
            role, cid = c.get("source_segment_role"), c.get("concept_id")
            if role not in ("story", "image", "tool"):
                problems.append("%s: role %r is not allowed in an idea topic (story, image or tool)" % (cid, role))
                continue
            if i == 0 and role == "tool":
                problems.append("%s: a topic cannot open with a tool; the concept video (or image) comes first" % cid)
            if role == "tool":
                prev = cs[i - 1] if i else {}
                if prev.get("source_segment_role") not in ("story", "image") or c.get("applies_to") != prev.get("concept_id"):
                    problems.append("%s: a tool must come right after the concept it applies to and name it in "
                                    "applies_to (previous concept is %s, applies_to is %r)"
                                    % (cid, prev.get("concept_id"), c.get("applies_to")))
            n_v, n_i, n_t = (len(_nodes(t, c, k)) for k in ("video", "image", "2d_tool"))
            if role == "story" and (n_v != 1 or n_t):
                problems.append("%s: a concept video concept holds exactly 1 video and no tool (has %d video, %d tool)"
                                % (cid, n_v, n_t))
            if role == "image" and (n_i != 1 or n_v or n_t):
                problems.append("%s: an image concept holds exactly 1 image and no video or tool (%d image, %d video, "
                                "%d tool)" % (cid, n_i, n_v, n_t))
            if role == "tool" and (n_t != 1 or n_v):
                problems.append("%s: a tool concept holds exactly 1 tool and no video (%d tool, %d video)"
                                % (cid, n_t, n_v))

    # ---- review ----
    if review.get("source_type") != summary:
        problems.append("%s: the last topic must be the review (source_type %r), it is %r"
                        % (review.get("topic_id"), summary, review.get("source_type")))
    rcs = review.get("concepts") or []
    if not 1 <= len(rcs) <= _cfg(config, "review_max_concepts"):
        problems.append("%s: the review has %d concept(s) (keep 1 to %d: it is short)"
                        % (review.get("topic_id"), len(rcs), _cfg(config, "review_max_concepts")))
    if review.get("topic_objective"):
        problems.append("%s: the review topic carries no topic_objective" % review.get("topic_id"))
    if any(m.get("type") in ("2d_tool", "video") for m in review.get("media") or []):
        problems.append("%s: the review has no new video or tool; it revises what was already taught"
                        % review.get("topic_id"))
    _check_review(plan, topics, rcs, review, problems)


def _check_review(plan, topics, rcs, review, problems):
    earlier = [c for t in topics[:-1] for c in t.get("concepts") or []]
    earlier_ids = {c.get("concept_id") for c in earlier}
    earlier_terms = {k.lower() for c in earlier for k in c.get("key_terms") or []}
    covered = set()
    for c in rcs:
        cid = c.get("concept_id")
        if c.get("source_segment_role") != "review":
            problems.append("%s: every concept of the review topic has role 'review'" % cid)
        covers = c.get("review_covers") or []
        if not covers:
            problems.append("%s: a review concept lists the concepts it revises in review_covers" % cid)
        for r in covers:
            if r not in earlier_ids:
                problems.append("%s: review_covers names %s, which is not an earlier concept (the review adds no new "
                                "content)" % (cid, r))
        covered |= set(covers)
        new_terms = sorted(k for k in (c.get("key_terms") or []) if k.lower() not in earlier_terms)
        if new_terms:
            problems.append("%s: the review introduces key term(s) not taught earlier: %s" % (cid, new_terms))
        if c.get("ncert_refs"):
            problems.append("%s: the review reuses taught concepts; it carries no book item of its own (%s)"
                            % (cid, c["ncert_refs"][:3]))
    for t in topics[1:-1]:
        ids = {c.get("concept_id") for c in t.get("concepts") or [] if c.get("source_segment_role") in ("story", "image")}
        if ids and not (ids & covered):
            problems.append("%s: the review does not revise any concept of this topic" % t.get("topic_id"))


# ------------------------------------------------------------------ videos
def _check_videos(plan, config, problems):
    full = _cfg(config, "stage") == "full"
    vids = _all_nodes(plan, "video")
    seen_ideas = {}
    hooks = [m for _, m in vids if m.get("video_kind") == "hook"]
    if len(hooks) != 1:
        problems.append("the chapter needs exactly 1 hook video (found %d)" % len(hooks))
    max_s = _cfg(config, "video_max_seconds")
    for _, m in vids:
        vid, kind = m.get("id"), m.get("video_kind")
        if kind not in ("hook", "concept"):
            problems.append("%s: video_kind must be 'hook' or 'concept', it is %r" % (vid, kind))
            continue
        if not m.get("purpose"):
            problems.append("%s: no purpose (one sentence: what this video is for)" % vid)
        if kind == "hook":
            if m.get("new_idea"):
                problems.append("%s: the hook introduces the situation, not a concept (new_idea must be empty)" % vid)
        else:
            idea = _ws(m.get("new_idea")).lower()
            if not idea:
                problems.append("%s: a concept video explains one named concept (new_idea is empty)" % vid)
            elif idea in seen_ideas:
                problems.append("%s: repeats the concept of %s (%r): do not duplicate content"
                                % (vid, seen_ideas[idea], m.get("new_idea")))
            else:
                seen_ideas[idea] = vid
        if not full:
            continue
        brief = m.get("story_brief") or {}
        missing = _present(brief, HOOK_KEYS if kind == "hook" else CONCEPT_KEYS)
        if missing:
            problems.append("%s: story brief is incomplete, missing %s (a video is a story, not a plain explanation)"
                            % (vid, missing))
        if kind == "concept" and not isinstance(brief.get("characters"), list):
            problems.append("%s: story_brief.characters must be a list of the chapter's characters" % vid)
        cast = set(((plan.get("source_metadata") or {}).get("story") or {}).get("characters") or [])
        stray = sorted(set(brief.get("characters") or []) - cast) if cast else []
        if stray:
            problems.append("%s: characters %s are not in the chapter's story cast %s (same people as the book)"
                            % (vid, stray, sorted(cast)))
        text = json.dumps(brief, ensure_ascii=False)
        hit = LECTURE.search(text)
        if hit:
            problems.append("%s: teacher-style wording in the story brief (%r): tell a story instead" % (vid, hit.group(0)))
        secs = m.get("target_seconds")
        limit = max_s.get(kind)
        if not isinstance(secs, (int, float)) or secs <= 0:
            problems.append("%s: target_seconds is missing" % vid)
        elif limit and secs > limit:
            problems.append("%s: target_seconds %s is over the %s-second limit for a %s video"
                            % (vid, secs, limit, kind))


# ------------------------------------------------------------------ images
def _check_images(plan, topics, config, problems):
    full = _cfg(config, "stage") == "full"
    vkeys = set((plan.get("source_metadata") or {}).get("visual_key") or {})
    titles, shows = {}, {}
    for t in topics:
        for c in t.get("concepts") or []:
            imgs = _nodes(t, c, "image")
            if len(imgs) > 1:
                problems.append("%s: %d images (one clean image per concept at most)" % (c.get("concept_id"), len(imgs)))
            has_other = bool(_nodes(t, c, "video") or _nodes(t, c, "2d_tool")
                             or any(x.get("applies_to") == c.get("concept_id") for x in t.get("concepts") or []))
            for m in imgs:
                iid = m.get("id")
                pl = m.get("placement")
                if pl not in ("main", "pinned"):
                    problems.append("%s: placement must be 'main' or 'pinned', it is %r" % (iid, pl))
                if not m.get("adds"):
                    problems.append("%s: say what this image adds (a new real-life example or visual reference)" % iid)
                if c.get("source_segment_role") == "image" and pl != "main":
                    problems.append("%s: the image of an image-only concept sits in the main flow" % iid)
                if has_other and pl == "main" and not m.get("new_context"):
                    problems.append("%s: this concept is already taught by a video or tool; a main-flow image must "
                                    "bring a new real-life context (new_context true), otherwise pin it" % iid)
                for key, store in ((m.get("title", "").strip().lower(), titles), (_ws(m.get("shows")).lower(), shows)):
                    if key and key in store:
                        problems.append("%s: duplicates %s (same title or same thing shown)" % (iid, store[key]))
                    elif key:
                        store[key] = iid
                bad = sorted(set(m.get("visuals") or []) - vkeys)
                if bad:
                    problems.append("%s: visuals %s are not in the chapter's visual_key" % (iid, bad))
                if full:
                    missing = _present(m, IMAGE_KEYS)
                    if missing:
                        problems.append("%s: image brief is incomplete, missing %s" % (iid, missing))
                    if _words(m.get("caption")) > 15:
                        problems.append("%s: the caption/prompt is over 15 words" % iid)


# ------------------------------------------------------------------ tools
def _tool_concepts(topics):
    return [(t, c) for t in topics for c in t.get("concepts") or [] if c.get("source_segment_role") in ("explore", "tool")]


def _check_tools(plan, topics, config, problems):
    full = _cfg(config, "stage") == "full"
    approved = config.get("approved_tools") or []
    pairs = _tool_concepts(topics)
    tools = []
    for t, c in pairs:
        nodes = _nodes(t, c, "2d_tool")
        if nodes:
            tools.append((t, c, nodes[0]))
    if not approved:
        if _cfg(config, "tool_map_required"):
            problems.append("config has no approved_tools: the content team's approved tool table (names, purposes, "
                            "sequence) is the input of the tool map; do not invent tools")
    else:
        if len(tools) != len(approved):
            problems.append("the plan has %d tool(s), the approved tool map has %d: no tool may be added or dropped"
                            % (len(tools), len(approved)))
        for i, (t, c, n) in enumerate(tools):
            conf = n.get("tool_config") or {}
            want = approved[i] if i < len(approved) else None
            if conf.get("approved_no") != i + 1:
                problems.append("%s: tool is number %s in the plan but %d in the approved sequence"
                                % (n.get("id"), conf.get("approved_no"), i + 1))
            if want:
                if _ws(n.get("tool_name")) != _ws(want.get("name")):
                    problems.append("%s: tool name %r differs from the approved name %r"
                                    % (n.get("id"), n.get("tool_name"), want.get("name")))
                if _ws(conf.get("approved_purpose")) != _ws(want.get("purpose")):
                    problems.append("%s: the approved purpose was changed (must stay exactly as the content team "
                                    "wrote it)" % n.get("id"))
    cov = (plan.get("source_metadata") or {}).get("ncert_coverage") or {}
    kinds = config.get("book_item_kinds") or {}
    qkinds = set(_cfg(config, "question_kinds"))
    vkeys = set((plan.get("source_metadata") or {}).get("visual_key") or {})
    for t, c, n in tools:
        tid, conf, role = n.get("id"), n.get("tool_config") or {}, c.get("source_segment_role")
        if role == "explore" and conf.get("approved_no") != _cfg(config, "explore_tool_no"):
            problems.append("%s: the exploration tool must be approved tool %d" % (tid, _cfg(config, "explore_tool_no")))
        if full:
            missing = _present(conf, TOOL_KEYS)
            if missing:
                problems.append("%s: tool spec is incomplete, missing %s" % (tid, missing))
        if len(conf.get("hint_ladder") or []) not in (0, 4):
            problems.append("%s: the hint ladder has exactly 4 rungs" % tid)
        if len(conf.get("controls") or []) > _cfg(config, "max_tool_controls"):
            problems.append("%s: %d controls (simple controls: at most %d)"
                            % (tid, len(conf["controls"]), _cfg(config, "max_tool_controls")))
        if _words(conf.get("instruction")) > _cfg(config, "max_instruction_words"):
            problems.append("%s: the instruction is over %d words (minimal on-screen text)"
                            % (tid, _cfg(config, "max_instruction_words")))
        obj = conf.get("learning_objective") or ""
        if obj and (_words(obj) > 25 or ";" in obj):
            problems.append("%s: a tool has ONE learning objective in one short sentence" % tid)
        bad = sorted(set(conf.get("visuals") or []) - vkeys)
        if bad:
            problems.append("%s: visuals %s are not in the chapter's visual_key" % (tid, bad))
        qmap = conf.get("question_map") or []
        if [q.get("text") for q in qmap] != list(conf.get("tool_questions") or []):
            problems.append("%s: tool_questions and question_map disagree" % tid)
        if not qmap:
            problems.append("%s: the tool has no questions: tie it to the NCERT question(s) of its concept, or raise "
                            "this as a clash for the user" % tid)
        notice = [q for q in qmap if q.get("kind") == "notice"]
        ncert = [q for q in qmap if q.get("kind") == "ncert"]
        other = [q for q in qmap if q.get("kind") not in ("notice", "ncert")]
        if other:
            problems.append("%s: question kinds must be 'ncert' or 'notice'" % tid)
        if len(notice) > _cfg(config, "max_notice_prompts"):
            problems.append("%s: %d notice prompts (at most %d)" % (tid, len(notice), _cfg(config, "max_notice_prompts")))
        if len(ncert) > _cfg(config, "max_tool_questions"):
            problems.append("%s: %d NCERT questions on one tool (at most %d: a short interaction path); split the "
                            "set or ask the user" % (tid, len(ncert), _cfg(config, "max_tool_questions")))
        if role == "tool" and not ncert:
            problems.append("%s: a concept tool carries at least one NCERT question of its concept" % tid)
        for q in ncert:
            qid = q.get("ncert_id")
            if qid not in cov:
                problems.append("%s: tool question %r is not a book item of this chapter" % (tid, qid))
            elif cov[qid] != [c.get("concept_id")]:
                problems.append("%s: tool question %r is homed on %s, not on this tool's concept"
                                % (tid, qid, cov[qid]))
            if kinds and kinds.get(qid) not in qkinds:
                problems.append("%s: %r is a %r item, not an NCERT question" % (tid, qid, kinds.get(qid)))


# ------------------------------------------------------------------ questions
def _check_questions(plan, topics, config, problems):
    kinds = config.get("book_item_kinds") or {}
    qkinds = set(_cfg(config, "question_kinds"))
    book = set(config.get("book_items") or [])
    for t in topics:
        cs = t.get("concepts") or []
        tool_targets = {c.get("applies_to") for c in cs if c.get("source_segment_role") in ("tool", "explore")}
        for c in cs:
            cid, role = c.get("concept_id"), c.get("source_segment_role")
            refs = c.get("ncert_refs") or []
            outside = sorted(r for r in refs if book and r not in book)
            if outside:
                problems.append("%s: book item(s) %s are not in this chapter's NCERT_ITEMS (outside-chapter "
                                "questions are excluded)" % (cid, outside[:5]))
            qs = [r for r in refs if kinds.get(r) in qkinds]
            if qs and role in ("hook", "review"):
                problems.append("%s: a %s concept holds no NCERT questions (%s)" % (cid, role, qs[:3]))
            if qs and role in ("story", "image") and cid in tool_targets:
                problems.append("%s: its NCERT question(s) %s belong on the tool that follows it, not on the "
                                "concept itself" % (cid, qs[:3]))


# ------------------------------------------------------------------ language
def _check_language(plan, topics, config, problems):
    limit = _cfg(config, "max_sentence_words")
    for t in topics:
        for c in t.get("concepts") or []:
            for b in c.get("content") or []:
                if b.get("block_kind") not in ("teaching_plan", "recap"):
                    continue
                for line in b.get("steps") or b.get("text", "").split("\n"):
                    for s in re.split(r"(?<=[.!?])\s+", line):
                        if _words(s) > limit:
                            problems.append("%s: sentence is long (%d words, keep it to %d for this age): %r"
                                            % (c.get("concept_id"), _words(s), limit, s[:60]))


# ------------------------------------------------------------------ entry point
def check(plan, config=None):
    """Return a list of problem strings; empty means clean."""
    config = config or {}
    topics = list(walk_topics(plan))
    if not topics:
        return ["no topics at all"]
    problems = []
    for t, c in _concepts(plan):
        if c.get("source_segment_role") not in ROLES:
            problems.append("%s: source_segment_role %r is not one of %s"
                            % (c.get("concept_id"), c.get("source_segment_role"), sorted(ROLES)))
    _check_shape(plan, topics, config, problems)
    _check_videos(plan, config, problems)
    _check_images(plan, topics, config, problems)
    _check_tools(plan, topics, config, problems)
    _check_questions(plan, topics, config, problems)
    _check_language(plan, topics, config, problems)
    return problems


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    plan = json.load(io.open(sys.argv[1], encoding="utf-8"))
    cfg = json.load(io.open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else {}
    out = check(plan, cfg)
    print("%s: %d problem(s)" % (sys.argv[1], len(out)))
    for p in out:
        print("  -", p)

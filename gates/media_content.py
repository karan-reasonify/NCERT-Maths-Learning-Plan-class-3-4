# -*- coding: utf-8 -*-
"""Structural + media gate: the delivery breaks the API itself does not reject.

Ported from the upload skill's own preflight(),
since a plan can import clean and still hand the student a blank topic or a 404 tool. upload/upload_lp.py
imports `preflight` from here so the same check runs before build (via gate_runner) and right before upload
(belt and suspenders) off a single source of truth.

    python -B media_content.py <plan.json>      print the problems found, if any
"""
from __future__ import annotations

import json
import re
import sys

MEDIA_TYPES = {"2d_tool", "video", "image"}
DASHES = "—–"


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def walk_media(plan):
    for topic in walk_topics(plan):
        for node in topic.get("media") or []:
            yield node


def preflight(plan):
    """Return a list of problem strings; empty means clean."""
    problems = []

    for key in ("chapter_id", "chapter_master_id", "modules", "objectives"):
        if not plan.get(key):
            problems.append("no %s" % key)

    seen = set()
    for node in walk_media(plan):
        if node.get("id") in seen:
            problems.append("duplicate media id %r" % node.get("id"))
        seen.add(node.get("id"))

    bad = sorted(t for t in {n.get("type") for n in walk_media(plan)}
                 if t not in MEDIA_TYPES)
    if bad:
        problems.append("media types outside the enum: %r" % bad)

    text = json.dumps(plan, ensure_ascii=False)
    if "tool_2d" in text:
        problems.append("the retired spelling tool_2d appears %d time(s)"
                        % text.count("tool_2d"))
    dashes = sum(text.count(d) for d in DASHES)
    if dashes:
        problems.append("%d em or en dash(es) present" % dashes)

    seg_n, top_n, con_n = [], [], []
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            got = re.search(r"S(\d+)$", segment.get("segment_id") or "")
            seg_n.append(int(got.group(1)) if got else -1)
            for topic in segment.get("topics") or []:
                got = re.search(r"T(\d+)$", topic.get("topic_id") or "")
                top_n.append(int(got.group(1)) if got else -1)
                for concept in topic.get("concepts") or []:
                    got = re.search(r"C(\d+)$", concept.get("concept_id") or "")
                    con_n.append(int(got.group(1)) if got else -1)
    for label, nums in (("segment", seg_n), ("topic", top_n), ("concept", con_n)):
        if nums and nums != list(range(1, len(nums) + 1)):
            problems.append("%s ids are not contiguous in document order" % label)

    empty = [t.get("topic_id") for t in walk_topics(plan)
             if not t.get("available_content_types")]
    if empty:
        problems.append("%d topic(s) with no available_content_types: %s"
                        % (len(empty), empty[:5]))

    by_id = {n.get("id"): n for n in walk_media(plan)}
    for node in walk_media(plan):
        if node.get("type") != "2d_tool":
            continue
        conf = node.get("tool_config") or {}
        if not conf:
            problems.append("%s has no tool_config" % node.get("id"))
            continue
        same_as = conf.get("same_as")
        if same_as and same_as not in by_id:
            problems.append("%s references %s, which is not a media node"
                            % (node.get("id"), same_as))
        if not node.get("2d_tool_url"):
            problems.append("%s has an empty 2d_tool_url" % node.get("id"))
        head = by_id.get(same_as) if same_as else node
        if not ((head or {}).get("tool_config") or {}).get("tool_questions") \
                and not conf.get("tool_questions"):
            problems.append("%s carries no tool_questions" % node.get("id"))

    grade = plan.get("grade")
    if grade:
        wrong = [u for u in (n.get("2d_tool_url") for n in walk_media(plan))
                 if u and ("class_%s/" % grade) not in u]
        if wrong:
            problems.append("%d asset url(s) not under class_%s: %s"
                            % (len(wrong), grade, wrong[0]))

    # Whitelist, not a blacklist: asset urls and source_*_key fields legitimately contain
    # "cbse"/"ncert" as bucket-path segments (e.g. ".../V2/cbse/cbse/english/class_7/..."), and
    # "description"/"context"/"teaching_notes" are internal build notes, never shown to the
    # student - none of those should ever trip this. Only fields that either reach the student
    # directly or drive generation of something that does are scanned. "video_script" is a
    # dict (scanned via its own JSON so nested text is covered without tracking its shape here).
    BRANDING = re.compile(r"\bNCERT\b|\bCBSE\b|\btextbook\b|\bpage\s+\d+\b", re.IGNORECASE)
    STUDENT_FACING_FIELDS = {
        "title", "instructions_for_student", "generation_prompt", "video_script",
        "labels", "accuracy_constraints", "negative_prompt", "tool_name",
        # Class 3/4: the story brief and the image caption become what the child hears and reads
        "story_brief", "caption",
    }
    for node in walk_media(plan):
        for field in STUDENT_FACING_FIELDS:
            v = node.get(field)
            if v is None:
                continue
            text = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
            if BRANDING.search(text):
                problems.append("%s field %r carries textbook branding: %r"
                                % (node.get("id"), field, text[:120]))

    return problems


def summarise(plan):
    kinds = {}
    for node in walk_media(plan):
        kinds[node.get("type")] = kinds.get(node.get("type"), 0) + 1
    topics = list(walk_topics(plan))
    return {
        "modules": len(plan.get("modules") or []),
        "topics": len(topics),
        "concepts": sum(len(t.get("concepts") or []) for t in topics),
        "objectives": len(plan.get("objectives") or []),
        "media": sum(kinds.values()),
        "tools": kinds.get("2d_tool", 0),
    }


if __name__ == "__main__":
    import io
    for path in sys.argv[1:]:
        plan = json.load(io.open(path, encoding="utf-8"))
        problems = preflight(plan)
        print("%s: %d problem(s)" % (path, len(problems)))
        for p in problems:
            print("  -", p)

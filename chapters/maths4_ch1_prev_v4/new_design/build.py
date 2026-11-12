# -*- coding: utf-8 -*-
"""The per-chapter build script of the Class 3/4 pipeline. Copied unchanged into every chapter folder by
core/lp_start.py; everything chapter-specific lives in chapter.config.json, content.py, concept_plan.py (+ topics_*.py,
tools_*.py) next to it.

    python -B build.py --structure   STRUCTURE STAGE: build the plan with its media DECISIONS (which concept has a
                                     video, an image or a tool, which NCERT questions sit on which tool), run the
                                     gates that can pass now, write structure_report.md / .json and stop. This is the
                                     approval stop: show the report to the user and wait.
    python -B build.py --approve     record the user's approval of exactly that structure (structure_approved.json).
                                     Run it only after the user said yes. Any later change to the structure makes the
                                     approval stale.
    python -B build.py --briefs      (needs the approval) write briefs/videos.md, images.md, tools.md from the plan and
                                     list every brief that is still incomplete.
    python -B build.py               (needs the approval) build <chapter_id>.json and run every gate.
    python -B build.py --check       gates only, against the <chapter_id>.json already on disk.

The flow every chapter has (gates/flow_c34.py checks all of it):
    hook video -> exploration tool (first approved tool) -> [concept video -> its matching tool -> its NCERT practice]*
    -> chapter review. A small concept may be one image instead. The approved tools, their order and their purposes come
    from the content team (chapter.config.json "approved_tools") and are never changed here.

Phase-2-only, direct build: the output plan has "phase": 2 and the plain "chapter_id", no "_V3" file, no mirror step.
Required order afterwards (validation/STAMP_FORMAT.md):
    build.py -> core/set_version.py -> validation/validate_local.py -> upload/upload_lp.py --dry-run -> upload_lp.py
"""
from __future__ import annotations

import datetime
import hashlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_pipeline_root(start):
    """The directory above `start` that holds both gates/ and core/ (the pipeline root)."""
    d = os.path.abspath(start)
    for _ in range(12):
        if os.path.isdir(os.path.join(d, "gates")) and os.path.isdir(os.path.join(d, "core")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    raise SystemExit("could not find the pipeline root (a folder containing both gates/ and core/) above %r" % start)


ROOT = _find_pipeline_root(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from gates import gate_runner               # noqa: E402
from core import briefs as BR               # noqa: E402
from core import media_nodes as MN          # noqa: E402

import content as K          # noqa: E402  (the book's facts for this chapter)
import concept_plan as CP    # noqa: E402  (TOPICS and TOOLS)
from tools_spec.tool_node_builder import build_tool_node  # noqa: E402

CONFIG_PATH = os.path.join(HERE, "chapter.config.json")
REPORT_JSON = os.path.join(HERE, "structure_report.json")
REPORT_MD = os.path.join(HERE, "structure_report.md")
APPROVAL = os.path.join(HERE, "structure_approved.json")
BRIEF_DIR = os.path.join(HERE, "briefs")

SOURCE_TYPE = {"framing": "framing", "instructional": "instructional/exploration", "summary": "summary"}
A_ROLES = {"hook", "story", "image", "review"}
DOER_ROLES = {"explore", "tool"}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise SystemExit("no chapter.config.json next to build.py: run core/lp_start.py first")
    with io.open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = json.load(f)
    missing = [k for k in ("chapter_id", "chapter_master_id", "phase", "grade", "chapter_no", "chapter_name",
                           "media_tag", "asset_base_template") if not cfg.get(k) and cfg.get(k) != 0]
    if missing:
        raise SystemExit("chapter.config.json is missing: %s" % missing)
    if cfg["phase"] != 2:
        raise SystemExit("chapter.config.json phase must be 2: this pipeline is Phase 2 only")
    if "_v3" in cfg["chapter_id"].lower():
        raise SystemExit("chapter_id must not carry a _V3 suffix in this pipeline")
    return cfg


def out_path(cfg):
    return os.path.join(HERE, "%s.json" % cfg["chapter_id"])


def book_item_kinds():
    """{book id: kind} from content.NCERT_ITEMS. An entry is "id" (kind unknown), ("id", "kind") or {"id", "kind"};
    kind is example | exercise | prompt (an NCERT question), or talk | text (not a question)."""
    kinds = {}
    for entry in getattr(K, "NCERT_ITEMS", []) or []:
        if isinstance(entry, dict):
            kinds[entry["id"]] = entry.get("kind")
        elif isinstance(entry, (list, tuple)) and len(entry) == 2:
            kinds[entry[0]] = entry[1]
        else:
            kinds[entry] = None
    return kinds


def book_item_ids():
    return list(book_item_kinds())


# ---------------------------------------------------------------------------
# assembling modules -> segments -> topics -> concepts from concept_plan.TOPICS
# ---------------------------------------------------------------------------
def _content_block(kind, text, **extra):
    d = {"type": "paragraph", "block_kind": kind, "text": text, "publication_text": text}
    d.update(extra)
    return d


def _teach_blocks(concept):
    blocks = []
    if concept.get("textbook"):
        blocks.append(_content_block("textbook_text", "\n".join(concept["textbook"]), lines=concept["textbook"]))
    if concept.get("teach"):
        blocks.append(_content_block("teaching_plan", "\n".join(
            "%d. %s" % (i, s) for i, s in enumerate(concept["teach"], 1)), steps=concept["teach"]))
    for ex in concept.get("examples") or []:
        text = "\n".join(["Worked example: %s" % ex["q"]]
                         + ["%d. %s" % (i, s) for i, s in enumerate(ex["steps"], 1)]
                         + ["Answer: %s" % ex["answer"]])
        blocks.append(_content_block("worked_example", text, question=ex["q"], steps=ex["steps"],
                                     answer=ex["answer"], ncert_refs=ex.get("ncert") or []))
    if concept.get("recap"):
        blocks.append(_content_block("recap", "\n".join(concept["recap"])))
    for it in concept.get("items") or []:
        text = "\n".join(["%s: %s" % (it["book"], it["question"])]
                         + ["%d. %s" % (i, s) for i, s in enumerate(it["steps"], 1)]
                         + ["Answer: %s" % it["answer"]])
        blocks.append(_content_block("worked_example", text, item_kind="exercise", coverage_id=it["cov"],
                                     exercise_id=it["cov"], book_number=it["book"], question=it["question"],
                                     steps=it["steps"], answer=it["answer"], ncert_refs=[it["cov"]],
                                     book_kind=it.get("kind", "exercise")))
    return blocks


def _role(c):
    role = c.get("role") or ("tool" if c.get("kind") == "doer" else "story")
    allowed = DOER_ROLES if c.get("kind") == "doer" else A_ROLES
    if role not in allowed:
        raise SystemExit("concept %s: role %r is not allowed for a %s (use one of %s)"
                         % (c["key"], role, "tool concept" if c.get("kind") == "doer" else "teaching concept",
                            sorted(allowed)))
    return role


def _need(lookup, key, who, what):
    if key not in lookup:
        raise SystemExit("%s names %s %r, which is not an EARLIER concept of the plan" % (who, what, key))
    return lookup[key]["concept_id"]


def assemble(cfg):
    """-> (plan, concept_lookup, asset_base). concept_lookup: authored key "T2.C1" -> {concept, concept_id, topic}."""
    asset_base = cfg["asset_base_template"].format(grade=cfg["grade"], chapter_no=cfg["chapter_no"])
    tag = cfg["media_tag"]
    approved = cfg.get("approved_tools") or []

    modules_order, by_module = [], {}
    for t in CP.TOPICS:
        by_module.setdefault(t["module"], []).append(t)
        if t["module"] not in [m for m, _ in modules_order]:
            modules_order.append((t["module"], by_module[t["module"]]))

    modules_out, concept_lookup = [], {}
    objectives_out, ncert_coverage, s2o = [], {}, {}
    topic_n = concept_n = 0
    prev_video = None
    total_minutes = 0

    for module_id, topics in modules_order:
        module_name = next((n for mid, n, _ in K.MODULES if mid == module_id), module_id)
        module_summary = next((s for mid, _, s in K.MODULES if mid == module_id), "")
        segments_out = []
        for t in topics:
            topic_n += 1
            full_topic_id = "%s.S%d.T%d" % (module_id, topic_n, topic_n)
            concepts_out, media_out = [], []
            available_types = set()
            topic_objective_ids, topic_minutes = [], 0
            for c in t["concepts"]:
                concept_n += 1
                full_cid = "%s.C%d" % (full_topic_id, concept_n)
                concept_lookup[c["key"]] = {"concept": c, "concept_id": full_cid, "topic": t}
                role = _role(c)
                available_types.add("text")
                own_media = []      # nodes of this concept, in the order: image(s), video, tool
                pinned = []

                applies_to = None
                if c.get("kind") == "doer":
                    applies_to = _need(concept_lookup, c.get("applies_to"), "tool concept %s (applies_to)" % c["key"],
                                       "the concept it applies to")
                    if c["tool"] is None:
                        raise SystemExit("tool concept %s has no tool: a tool concept always carries its tool" % c["key"])
                    spec = CP.TOOLS.get(c["tool"])
                    if spec is None:
                        raise SystemExit("concept %s names tool %r, which is not in CP.TOOLS" % (c["key"], c["tool"]))
                    no = spec.get("approved_no")
                    want = approved[no - 1] if isinstance(no, int) and 1 <= no <= len(approved) else {}
                    qmap = ([{"kind": "notice", "text": p} for p in spec.get("notice") or []]
                            + [{"kind": "ncert", "text": it["question"], "ncert_id": it["cov"], "book": it["book"],
                                "answer": it["answer"]} for it in c.get("items") or []])
                    conf = dict(spec)
                    conf.pop("notice", None)
                    conf.update({"idea": spec.get("learning_objective", ""), "role": role, "applies_to": applies_to,
                                 "approved_name": want.get("name"), "approved_purpose": want.get("purpose"),
                                 "question_map": qmap, "misconceptions": list(c.get("misconceptions") or [])
                                 or list(spec.get("misconceptions") or [])})
                    node = build_tool_node(
                        media_id="%s.2D1" % full_cid, concept_id=full_cid, tool_name=spec["title"], tool_config=conf,
                        tool_questions=[q["text"] for q in qmap],
                        tool_2d_url="%s/tool_v3/%s/index.html" % (asset_base, spec["tool_id"]), grade=cfg["grade"],
                        instructions_for_student=spec.get("instruction") or spec.get("learning_objective", ""))
                    own_media.append(node)
                    available_types.add("2d_tool")

                if c.get("video"):
                    if role not in ("hook", "story"):
                        raise SystemExit("concept %s (role %s) cannot carry a video: only the hook and a concept "
                                         "video concept do" % (c["key"], role))
                    v = c["video"]
                    kind = "hook" if role == "hook" else "concept"
                    node = MN.video_node(
                        "%s.VID1" % full_cid, full_cid, kind, v["title"], v["purpose"], v.get("new_idea", ""),
                        v.get("story") or {}, v.get("seconds"), asset_base=asset_base,
                        source_key="%s.%s.%s" % (tag, c["key"], kind), chapter_label=cfg["chapter_name"],
                        previous_video_id=prev_video if kind == "concept" else None)
                    prev_video = node["id"]
                    own_media.append(node)
                    available_types.add("video")

                if c.get("image"):
                    im = c["image"]
                    node = MN.image_node(
                        "%s.IMG1" % full_cid, full_cid, im["title"], im["adds"], placement=im["placement"],
                        new_context=im["new_context"], real_life=im["real_life"], shows=im["shows"],
                        caption=im["caption"], style=im["style"], visuals=im["visuals"], asset_base=asset_base)
                    own_media.insert(0, node)
                    available_types.add("image")
                    if im["placement"] == "pinned":
                        pinned.append(node["id"])

                media_out += own_media
                ncert_refs = list(c.get("ncert") or [])
                for ex in c.get("examples") or []:
                    ncert_refs += ex.get("ncert") or []
                for it in c.get("items") or []:
                    ncert_refs.append(it["cov"])
                for cov_id in ncert_refs:
                    ncert_coverage.setdefault(cov_id, []).append(full_cid)

                review_covers = [_need(concept_lookup, k, "review concept %s (review_covers)" % c["key"],
                                       "a concept to revise") for k in c.get("review_covers") or []]
                is_enrichment_c = bool(c.get("enrichment"))
                objective_id = None
                if not is_enrichment_c and c.get("objective"):
                    objective_id = "%s.OBJ1" % full_cid
                    objectives_out.append({"objective_id": objective_id, "anchor": [full_cid],
                                           "home_topic_id": full_topic_id, "objective_text": c["objective"],
                                           "bloom_level": c.get("bloom")})
                    topic_objective_ids.append(objective_id)
                    s2o[c["key"]] = objective_id
                main_ids = [x["id"] for x in own_media if x["id"] not in pinned]
                vids = [x["id"] for x in own_media if x.get("type") == "video"]
                tool_node = next((x for x in own_media if x.get("type") == "2d_tool"), None)
                topic_minutes += c.get("minutes") or 0
                concepts_out.append({
                    "concept_id": full_cid,
                    "concept_name": c.get("name") or c.get("objective", "")[:60],
                    "content": _teach_blocks(c),
                    "bloom_level": c.get("bloom"),
                    "key_terms": c.get("key_terms") or [],
                    "misconceptions": c.get("misconceptions") or [],
                    "tool_media_id": tool_node["id"] if tool_node else None,
                    "ncert_refs": ncert_refs,
                    "is_enrichment": is_enrichment_c,
                    "source_segment_role": role,
                    "applies_to": applies_to,
                    "review_covers": review_covers,
                    "objective_id": objective_id,
                    "objective_ids": [objective_id] if objective_id else [],
                    "media_ids": main_ids,
                    "pinned_media_ids": pinned,
                    "video_media_ids": vids,
                    "walkthrough_video_id": vids[0] if vids else None,
                    "source_media": ("video" if vids else "2d_tool" if tool_node else "image" if main_ids else None),
                    "estimated_minutes": c.get("minutes") or 0,
                })
            total_minutes += topic_minutes
            is_enrichment_t = t["topic_type"] == "framing"
            topic_objective = None
            if t["topic_type"] == "instructional" and t.get("objective"):
                topic_objective = {"objective_id": "%s.TOBJ1" % full_topic_id, "objective_text": t["objective"],
                                   "home_topic_id": full_topic_id}
            summary_text = t.get("summary", "")
            segments_out.append({
                "segment_id": "%s.S%d" % (module_id, topic_n),
                "segment_objective_ids": list(topic_objective_ids),
                "topics": [{
                    "topic_id": full_topic_id,
                    "topic_name": t["name"],
                    "topic_type": t["topic_type"],
                    "source_type": SOURCE_TYPE[t["topic_type"]],
                    "is_enrichment": is_enrichment_t,
                    "topic_objective": topic_objective,
                    "topic_summary": summary_text,
                    "summary": summary_text,
                    "brief_summary": summary_text,
                    "detailed_summary": summary_text,
                    "ncert_sections": t.get("ncert_sections") or [],
                    "key_terms": t.get("key_terms") or [],
                    "concepts": concepts_out,
                    "media": media_out,
                    "available_content_types": sorted(available_types),
                    "depends_on": [],
                    "objective_ids": topic_objective_ids,
                    "learning_objectives": [o for o in objectives_out if o["objective_id"] in topic_objective_ids],
                    "estimated_minutes": topic_minutes,
                }],
            })
        modules_out.append({"module_id": module_id, "module_name": module_name, "module_summary": module_summary,
                            "segments": segments_out})

    plan = {
        "chapter_id": cfg["chapter_id"],
        "chapter_master_id": cfg["chapter_master_id"],
        "subject_ref_id": cfg.get("subject_ref_id"),
        "medium_id": cfg.get("medium_id", 1),
        "phase": 2,
        "grade": cfg["grade"],
        "chapter_no": cfg["chapter_no"],
        "chapter_name": cfg["chapter_name"],
        "pipeline": "class3_4_story_tool_flow",
        "chapter_approach": K.CHAPTER_APPROACH,
        "design_references": K.DESIGN_REFERENCES,
        "modules": modules_out,
        "objectives": objectives_out,
        "strand_to_objective_map": s2o,
        "estimated_time": round(total_minutes / 60.0, 2),
        "source_metadata": {
            "chapter": K.CHAPTER,
            "ncert_coverage": ncert_coverage,
            "visual_key": dict(getattr(K, "VISUAL_KEY", {}) or {}),
            "story": dict(getattr(K, "STORY", {}) or {}),
            "summary_stats": {},
        },
    }
    if cfg.get("publication_id"):
        # the LP2 upload endpoint requires a top-level publication_id (CBSE = 1) and a 2d_tool_json on every tool
        # node (empty until the tool is built), as the live chapters carry them
        plan["publication_id"] = cfg["publication_id"]
        for module in plan["modules"]:
            for segment in module["segments"]:
                for topic in segment["topics"]:
                    for nd in topic["media"]:
                        if nd.get("type") == "2d_tool":
                            nd.setdefault("2d_tool_json", "")
    return plan, concept_lookup, asset_base


# ---------------------------------------------------------------------------
# the structure report (the approval stop)
# ---------------------------------------------------------------------------
def _topics(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def structure_report(plan, cfg, concept_lookup):
    """The decisions the user approves: what each concept is, which media it has and which book items sit where.
    Briefs (story details, image and tool specs) are NOT in it, so writing them later does not void the approval."""
    key_of = {v["concept_id"]: k for k, v in concept_lookup.items()}
    kinds = book_item_kinds()
    qkinds = ("example", "exercise", "prompt")
    approved = cfg.get("approved_tools") or []
    topics_out, tool_map = [], []
    counts = {"hook_videos": 0, "concept_videos": 0, "images_main": 0, "images_pinned": 0, "tools": 0,
              "questions": {k: 0 for k in qkinds}}
    for t in _topics(plan):
        cs = []
        for c in t["concepts"]:
            media = []
            for n in t["media"]:
                if n.get("concept_id") != c["concept_id"]:
                    continue
                if n["type"] == "video":
                    media.append("video:%s: %s" % (n["video_kind"], n.get("new_idea") or n.get("purpose")))
                    counts["hook_videos" if n["video_kind"] == "hook" else "concept_videos"] += 1
                elif n["type"] == "image":
                    media.append("image:%s: %s" % (n["placement"], n["adds"]))
                    counts["images_" + n["placement"]] += 1
                elif n["type"] == "2d_tool":
                    conf = n["tool_config"]
                    media.append("tool %s: %s" % (conf.get("approved_no"), n["tool_name"]))
                    counts["tools"] += 1
                    tool_map.append({"no": conf.get("approved_no"), "name": n["tool_name"],
                                     "approved_name": conf.get("approved_name"),
                                     "purpose": conf.get("approved_purpose"), "concept_id": c["concept_id"],
                                     "concept_key": key_of[c["concept_id"]], "applies_to": c.get("applies_to"),
                                     "objective": conf.get("learning_objective")})
            qs = [r for r in c["ncert_refs"] if kinds.get(r) in qkinds]
            for r in qs:
                counts["questions"][kinds[r]] += 1
            cs.append({"key": key_of[c["concept_id"]], "concept_id": c["concept_id"], "name": c["concept_name"],
                       "role": c["source_segment_role"], "media": media, "applies_to": c.get("applies_to"),
                       "questions": qs, "other_items": [r for r in c["ncert_refs"] if r not in qs],
                       "review_covers": c.get("review_covers") or []})
        topics_out.append({"topic_id": t["topic_id"], "name": t["topic_name"], "source_type": t["source_type"],
                           "concepts": cs})
    n_concepts = sum(len(t["concepts"]) for t in topics_out)
    return {
        "chapter": {"chapter_id": cfg["chapter_id"], "name": cfg["chapter_name"], "grade": cfg["grade"],
                    "chapter_no": cfg["chapter_no"], "chapter_master_id": cfg["chapter_master_id"],
                    "subject_ref_id": cfg.get("subject_ref_id")},
        "counts": dict(counts, modules=len(plan["modules"]), topics=len(topics_out), concepts=n_concepts,
                       book_items=len(kinds), approved_tools=len(approved)),
        "topics": topics_out,
        "tool_map": tool_map,
        "clashes": list(getattr(K, "CLASHES", []) or []),
        "book_errors": [dict(x) for x in getattr(K, "SOLUTION_NOTES", []) or []],
    }


def report_hash(report):
    """What the user approves: the flow, the tool map, the counts and the open clashes. The ids are left out so that
    entering the issued chapter_master_id later does not void the approval."""
    core = {k: report[k] for k in ("topics", "tool_map", "counts", "clashes")}
    return hashlib.sha256(json.dumps(core, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def report_markdown(r):
    c, k = r["chapter"], r["counts"]
    q = k["questions"]
    L = ["# Structure for approval: Class %s, %s" % (c["grade"], c["name"]), "",
         "chapter_id `%s`, chapter_master_id %s, subject_ref_id %s" % (c["chapter_id"], c["chapter_master_id"],
                                                                     c["subject_ref_id"]), "",
         "## Counts", "",
         "- %d topics, %d concepts, %d NCERT book items in all" % (k["topics"], k["concepts"], k["book_items"]),
         "- videos: %d hook + %d concept (each a story)" % (k["hook_videos"], k["concept_videos"]),
         "- images: %d in the main flow + %d pinned" % (k["images_main"], k["images_pinned"]),
         "- tools: %d of %d approved (names, purposes and order exactly as the content team gave them)"
         % (k["tools"], k["approved_tools"]),
         "- NCERT questions placed on tools / concepts: %d solved examples, %d exercises, %d prompts"
         % (q["example"], q["exercise"], q["prompt"]), "",
         "## The learning flow", ""]
    for t in r["topics"]:
        L.append("### %s  %s  (%s)" % (t["topic_id"], t["name"], t["source_type"]))
        for cc in t["concepts"]:
            L.append("- **%s** `%s` [%s] %s" % (cc["concept_id"], cc["key"], cc["role"], cc["name"]))
            for m in cc["media"]:
                L.append("  - %s" % m)
            if cc["questions"]:
                L.append("  - NCERT questions: %s" % ", ".join(cc["questions"]))
            if cc["review_covers"]:
                L.append("  - revises: %s" % ", ".join(cc["review_covers"]))
        L.append("")
    L += ["## Tool map (locked)", "", "| # | Tool | Concept | Applies to | One learning objective |", "|---|---|---|---|---|"]
    for x in r["tool_map"]:
        L.append("| %s | %s | %s (`%s`) | %s | %s |" % (x["no"], x["name"], x["concept_id"], x["concept_key"],
                                                       x["applies_to"], x["objective"]))
    L += ["", "## Clashes and judgement calls (decide these)", ""]
    L += ["- " + s for s in r["clashes"]] or ["- none"]
    L += ["", "## Printed-book errors found", ""]
    L += ["- %s: %s" % (e.get("item"), e.get("correct") or e.get("printed_solution")) for e in r["book_errors"]] or ["- none"]
    L += ["", "Nothing below this line is written until you approve: story briefs, image briefs, tool specs.", ""]
    return "\n".join(L)


def check_approval(report):
    """(ok, message): the approval on disk must hash the structure as it is now."""
    if not os.path.exists(APPROVAL):
        return False, "the structure has not been approved: run build.py --structure, show structure_report.md to the user, then build.py --approve after they say yes"
    with io.open(APPROVAL, encoding="utf-8") as f:
        ap = json.load(f)
    if ap.get("structure_sha256") != report_hash(report):
        return False, "the structure changed after it was approved (structure_approved.json is stale): show the new structure_report.md to the user and approve again"
    return True, "structure approved %s" % ap.get("approved_at", "")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def run_gates(plan, cfg, stage):
    gate_cfg = dict(cfg, book_items=book_item_ids(), book_item_kinds=book_item_kinds(), stage=stage)
    errors, counts = gate_runner.run(plan, gate_cfg)
    warnings = counts.pop("warnings", [])
    print("counts:", counts)
    if warnings:
        print("%d ADVISORY WARNING(S) (non-blocking):" % len(warnings))
        for w in warnings:
            print("  ~", w)
    return errors


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    argv = sys.argv[1:]
    cfg = load_config()

    if "--check" in argv:
        if not os.path.exists(out_path(cfg)):
            raise SystemExit("%s does not exist yet: run build.py once without --check first" % out_path(cfg))
        with io.open(out_path(cfg), encoding="utf-8") as f:
            plan = json.load(f)
        errors = run_gates(plan, cfg, "full")
        return _finish(errors, "all gates passed (blocking)")

    plan, concept_lookup, asset_base = assemble(cfg)
    report = structure_report(plan, cfg, concept_lookup)

    if "--structure" in argv:
        with io.open(REPORT_JSON, "w", encoding="utf-8", newline="\n") as f:
            json.dump(report, f, ensure_ascii=False, indent=1, sort_keys=True)
        with io.open(REPORT_MD, "w", encoding="utf-8", newline="\n") as f:
            f.write(report_markdown(report))
        print("wrote %s and %s" % (REPORT_MD, REPORT_JSON))
        errors = run_gates(plan, cfg, "structure")
        if errors:
            return _finish(errors, "")
        print("structure stage OK: %d topics, %d concepts, %d tools of %d approved. Show structure_report.md to the "
              "user and WAIT. Briefs, tool specs and the final build are not allowed before they approve it."
              % (report["counts"]["topics"], report["counts"]["concepts"], report["counts"]["tools"],
                 report["counts"]["approved_tools"]))
        return 0

    if "--approve" in argv:
        if not os.path.exists(REPORT_JSON):
            raise SystemExit("run build.py --structure first and show the report to the user")
        errors = run_gates(plan, cfg, "structure")
        if errors:
            return _finish(errors, "")
        with io.open(APPROVAL, "w", encoding="utf-8", newline="\n") as f:
            json.dump({"structure_sha256": report_hash(report), "chapter_id": cfg["chapter_id"],
                       "approved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                       "note": "recorded after the user approved structure_report.md"}, f, indent=1)
        print("approval recorded in %s (valid for exactly this structure)" % APPROVAL)
        return 0

    ok, msg = check_approval(report)
    if not ok:
        print("REFUSED: " + msg)
        return 2
    print(msg)

    if "--briefs" in argv:
        made = BR.write_briefs(plan, BRIEF_DIR)
        print("wrote briefs/: %d video, %d image, %d tool brief(s)" % (made["videos"], made["images"], made["tools"]))
        errors = run_gates(plan, cfg, "full")
        todo = [e for e in errors if "incomplete" in e or "target_seconds" in e or "caption" in e]
        for e in todo:
            print("  TO DO:", e)
        print("%d brief item(s) still to do; %d other gate message(s)" % (len(todo), len(errors) - len(todo)))
        return 0

    errors = run_gates(plan, cfg, "full")
    if errors:
        return _finish(errors, "")
    with io.open(out_path(cfg), "w", encoding="utf-8", newline="\n") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    print("wrote %s" % out_path(cfg))
    return _finish([], "all gates passed (blocking)")


def _finish(errors, ok_message):
    if errors:
        print("%d GATE FAILURE(S):" % len(errors))
        for e in errors:
            print("  -", e)
        return 1
    if ok_message:
        print(ok_message)
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""End-to-end smoke test of the Class 3/4 pipeline on the made-up chapter in smoke/toy_ch99.

    python3 -B -X utf8 smoke/run_smoke.py

Copies the toy chapter into smoke/_run/new_design/ next to a fresh copy of the template files, then runs, in order:
tool_map lock, build.py (must REFUSE before approval), --structure, --approve, --briefs, build.py, validate_local,
upload_lp --dry-run. Then it breaks the built plan in a dozen ways and checks that the right gate says so.
No network, no database. Exit 0 only if every check passes. smoke/_run/ is deleted at the end (--keep leaves it).
"""
from __future__ import annotations

import copy
import io
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RUN = os.path.join(HERE, "_run", "new_design")
sys.path.insert(0, ROOT)

PY = [sys.executable, "-B", "-X", "utf8"]
FAILS = []


def check(name, ok, detail=""):
    print("%s  %s%s" % ("PASS" if ok else "FAIL", name, ("   [" + detail + "]") if (detail and not ok) else ""))
    if not ok:
        FAILS.append(name)


def run(args, cwd=RUN):
    p = subprocess.run(PY + args, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    return p.returncode, p.stdout + p.stderr


def prepare():
    shutil.rmtree(os.path.join(HERE, "_run"), ignore_errors=True)
    os.makedirs(RUN)
    for n in os.listdir(os.path.join(HERE, "toy_ch99")):
        if n.endswith((".py", ".md")):
            shutil.copy(os.path.join(HERE, "toy_ch99", n), RUN)
    T = os.path.join(ROOT, "chapter_template")
    shutil.copy(os.path.join(T, "build.py"), RUN)
    shutil.copy(os.path.join(T, "topics_common.py.template"), os.path.join(RUN, "topics_common.py"))
    shutil.copy(os.path.join(T, "concept_plan.py.template"), os.path.join(RUN, "concept_plan.py"))
    with io.open(os.path.join(T, "chapter.config.json.sample"), encoding="utf-8") as f:
        cfg = json.load(f)
    cfg.update({"chapter_id": "cbse_eng_maths3_ch99", "chapter_master_id": 999, "subject_ref_id": 80, "grade": 3,
                "chapter_no": 99, "chapter_name": "Kite Day Toy", "media_tag": "c3z"})
    with io.open(os.path.join(RUN, "chapter.config.json"), "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


def mutated(plan, fn):
    p = copy.deepcopy(plan)
    fn(p)
    return p


def topics(p):
    return [t for m in p["modules"] for s in m["segments"] for t in s["topics"]]


def concept(p, key_suffix):
    for t in topics(p):
        for c in t["concepts"]:
            if c["concept_id"].endswith(key_suffix):
                return t, c
    raise KeyError(key_suffix)


def node(p, nid):
    for t in topics(p):
        for m in t["media"]:
            if m["id"] == nid:
                return m
    raise KeyError(nid)


def negative_tests(plan, cfg):
    from gates import gate_runner
    gate_cfg = dict(cfg, stage="full")
    import importlib.util
    spec = importlib.util.spec_from_file_location("toy_build", os.path.join(RUN, "build.py"))
    sys.path.insert(0, RUN)
    toy = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(toy)
    gate_cfg.update(book_items=toy.book_item_ids(), book_item_kinds=toy.book_item_kinds())

    def errors(p, c=None):
        errs, _ = gate_runner.run(p, c or gate_cfg)
        return errs

    check("the untouched plan has no gate error", errors(plan) == [], str(errors(plan)[:3]))

    cases = [
        ("a renamed tool is caught", "differs from the approved name",
         lambda p: p.update() or node(p, "M1.S1.T1.C2.2D1").__setitem__("tool_name", "Kite Finder")),
        ("a changed approved purpose is caught", "approved purpose was changed",
         lambda p: node(p, "M1.S2.T2.C4.2D1")["tool_config"].__setitem__("approved_purpose", "Something else.")),
        ("a dropped tool is caught", "no tool may be added or dropped",
         lambda p: p.update(modules=p["modules"]) or _drop_tool(p, "M1.S2.T2.C4.2D1")),
        ("a swapped tool order is caught", "approved sequence",
         lambda p: (node(p, "M1.S1.T1.C2.2D1")["tool_config"].__setitem__("approved_no", 2),
                    node(p, "M1.S2.T2.C4.2D1")["tool_config"].__setitem__("approved_no", 1))),
        ("a hook that teaches a concept is caught", "introduces the situation",
         lambda p: node(p, "M1.S1.T1.C1.VID1").__setitem__("new_idea", "ten ones make one ten")),
        ("a repeated concept video is caught", "do not duplicate content",
         lambda p: _dup_idea(p)),
        ("a lecture-style brief is caught", "teacher-style wording",
         lambda p: node(p, "M1.S2.T2.C3.VID1")["story_brief"].__setitem__("situation", "In this video we will learn tens.")),
        ("a character outside the book's cast is caught", "not in the chapter's story cast",
         lambda p: node(p, "M1.S2.T2.C3.VID1")["story_brief"].__setitem__("characters", ["Meera", "Zorg"])),
        ("a too-long video is caught", "over the 150-second limit",
         lambda p: node(p, "M1.S2.T2.C3.VID1").__setitem__("target_seconds", 400)),
        ("a duplicate image on a taught concept is caught", "new real-life context",
         lambda p: _image_on_video_concept(p)),
        ("a tool question that is not NCERT is caught", "is not a book item of this chapter",
         lambda p: node(p, "M1.S2.T2.C4.2D1")["tool_config"]["question_map"][0].__setitem__("ncert_id", "invented.q")),
        ("too many controls are caught", "controls (simple controls",
         lambda p: node(p, "M1.S2.T2.C4.2D1")["tool_config"].__setitem__("controls", ["a", "b", "c", "d", "e"])),
        ("a long on-screen instruction is caught", "minimal on-screen text",
         lambda p: node(p, "M1.S2.T2.C4.2D1")["tool_config"].__setitem__("instruction", "word " * 20)),
        ("a tool that is not right after its concept is caught", "right after the concept it applies to",
         lambda p: concept(p, "C4")[1].__setitem__("applies_to", "M1.S1.T1.C1")),
        ("new content in the review is caught", "not taught earlier",
         lambda p: concept(p, "C6")[1].__setitem__("key_terms", ["ten", "fraction"])),
        ("a review that revises nothing is caught", "review_covers",
         lambda p: concept(p, "C6")[1].__setitem__("review_covers", [])),
        ("an outside-chapter book item is caught", "outside-chapter",
         lambda p: _outside_item(p)),
        ("a question left on a concept whose tool follows is caught", "belong on the tool that follows it",
         lambda p: _question_on_story(p)),
        ("an em dash is caught", "dash",
         lambda p: concept(p, "C3")[1]["content"][0].__setitem__("text", "ten — ones")),
        ("a false sum is caught", "false equation",
         lambda p: concept(p, "C3")[1]["content"][1].__setitem__("text", "1. 10 + 10 = 30")),
    ]
    for name, needle, fn in cases:
        errs = errors(mutated(plan, fn))
        check(name, any(needle in e for e in errs), "wanted %r in %s" % (needle, errs[:4]))

    errs = errors(plan, dict(gate_cfg, approved_tools=[]))
    check("a missing approved tool map is caught", any("no approved_tools" in e for e in errs), str(errs[:3]))


def _drop_tool(p, nid):
    for t in topics(p):
        t["media"] = [m for m in t["media"] if m["id"] != nid]
        for c in t["concepts"]:
            if c.get("tool_media_id") == nid:
                c["tool_media_id"] = None
                c["media_ids"] = [x for x in c["media_ids"] if x != nid]


def _dup_idea(p):
    node(p, "M1.S2.T2.C3.VID1")["new_idea"] = "ten ones make one ten"
    t, c = concept(p, "C6")
    extra = copy.deepcopy(node(p, "M1.S2.T2.C3.VID1"))
    extra["id"] = "M1.S3.T3.C5.VID1"
    extra["concept_id"] = c["concept_id"]
    for tt in topics(p):
        if tt["topic_id"] == "M1.S3.T3":
            tt["media"].append(extra)


def _image_on_video_concept(p):
    t, c = concept(p, "C3")
    img = copy.deepcopy(node(p, "M1.S3.T3.C5.IMG1"))
    img.update(id="M1.S2.T2.C3.IMG1", concept_id=c["concept_id"], home_concept_id=c["concept_id"],
               placement="main", new_context=False, title="Another board", shows="another thing")
    t["media"].append(img)


def _outside_item(p):
    t, c = concept(p, "C4")
    c["ncert_refs"].append("ch7.q9")


def _question_on_story(p):
    t, c = concept(p, "C3")
    c["ncert_refs"].append("kf.q2")


def main():
    prepare()
    code, out = run([os.path.join(ROOT, "core", "tool_map.py"), "lock", "tool_map.md"])
    check("tool_map lock reads the content team's table", code == 0 and "locked 2 approved tool" in out, out)
    with io.open(os.path.join(RUN, "chapter.config.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    check("approved_tools hold name and the row's purpose",
          [t["name"] for t in cfg["approved_tools"]] == ["Kite Spotter", "Ten Bundles"]
          and cfg["approved_tools"][1]["purpose"].startswith("Tie loose sticks"), str(cfg["approved_tools"]))
    code, out = run([os.path.join(ROOT, "core", "tool_map.py"), "verify", "tool_map.md"])
    check("tool_map verify agrees with the config", code == 0, out)

    code, out = run(["build.py"])
    check("a build before approval is refused", code == 2 and "REFUSED" in out, out)
    code, out = run(["build.py", "--structure"])
    check("--structure passes and stops", code == 0 and "structure stage OK" in out, out)
    check("structure_report.md is written", os.path.exists(os.path.join(RUN, "structure_report.md")))
    code, out = run(["build.py", "--briefs"])
    check("--briefs is refused before approval", code == 2 and "REFUSED" in out, out)
    code, out = run(["build.py", "--approve"])
    check("--approve records the approval", code == 0 and os.path.exists(os.path.join(RUN, "structure_approved.json")), out)
    code, out = run(["build.py", "--briefs"])
    check("--briefs writes the briefs and none is left to do", code == 0 and "0 brief item(s) still to do" in out, out)
    for n in ("videos.md", "images.md", "tools.md"):
        check("briefs/%s exists" % n, os.path.exists(os.path.join(RUN, "briefs", n)))
    code, out = run(["build.py"])
    check("the full build passes every gate", code == 0 and "all gates passed" in out, out)
    plan_path = os.path.join(RUN, "cbse_eng_maths3_ch99.json")
    check("the plan JSON is written", os.path.exists(plan_path))

    with io.open(plan_path, encoding="utf-8") as f:
        plan = json.load(f)
    roles = [c["source_segment_role"] for t in topics(plan) for c in t["concepts"]]
    check("the flow is hook, explore, story, tool, image, review",
          roles == ["hook", "explore", "story", "tool", "image", "review"], str(roles))
    check("the plan carries publication_id and an empty 2d_tool_json on every tool",
          plan.get("publication_id") == 1 and all("2d_tool_json" in m for t in topics(plan) for m in t["media"]
                                                  if m["type"] == "2d_tool"))
    check("tool_questions are exactly the NCERT questions plus the notice prompts",
          [len(node(plan, i)["tool_config"]["tool_questions"]) for i in ("M1.S1.T1.C2.2D1", "M1.S2.T2.C4.2D1")] == [2, 2])
    check("the second video continues from the hook", node(plan, "M1.S2.T2.C3.VID1").get("continues_from")
          == "M1.S1.T1.C1.VID1")

    code, out = run(["build.py", "--check"])
    check("build.py --check (the validator's read-only command) passes on the built plan",
          code == 0 and "all gates passed" in out, out)

    code, out = run([os.path.join(ROOT, "validation", "validate_local.py"), plan_path])
    check("validate_local writes the stamp", code == 0 and os.path.exists(plan_path + ".stamp.json"), out)
    code, out = run([os.path.join(ROOT, "upload", "upload_lp.py"), plan_path, "--dry-run"])
    check("upload_lp --dry-run accepts the stamped plan", code == 0, out[-600:])

    # an edit to the structure after approval voids the approval
    p = os.path.join(RUN, "topics_1.py")
    with io.open(p, encoding="utf-8") as f:
        src = f.read()
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(src.replace('"Making a Ten"', '"Making a Ten Again"'))
    code, out = run(["build.py"])
    check("changing the structure after approval makes the approval stale", code == 2 and "stale" in out, out)
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(src)

    negative_tests(plan, cfg)

    if "--keep" not in sys.argv:
        shutil.rmtree(os.path.join(HERE, "_run"), ignore_errors=True)
    print()
    if FAILS:
        print("%d CHECK(S) FAILED: %s" % (len(FAILS), FAILS))
        return 1
    print("smoke test passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

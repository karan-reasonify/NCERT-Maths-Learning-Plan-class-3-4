# -*- coding: utf-8 -*-
"""Build a single 2d_tool media node dict, "spec + placeholder" style.

"Spec + placeholder" means: tool_config carries the FULL teaching spec (idea, screen, controls,
challenges, hints) so a tool builder can implement it later, but nothing is rendered yet - 2d_tool_url
points at a reserved, not-yet-live path, and build_status is "placeholder". This is the shape used by
maths7_ch10 and maths8_ch9's own build.py (their `tool_node()` function), NOT the maths6_ch3 Tools/_core
system, which builds and ships real standalone HTML/tsx per tool before the plan ever references it.

See TOOL_SPEC_GUIDE.md (same folder) for the tool_config/tool_questions shape and a worked example.

    python -B tool_node_builder.py          self-test: build one node, check it against
                                             gates.media_content.preflight() for a minimal plan.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from gates import media_content  # noqa: E402


def build_tool_node(media_id, concept_id, tool_name, tool_config, tool_questions, *,
                     tool_2d_url, grade=None, subtype="interactive", same_as=None,
                     instructions_for_student=None, title=None, **kwargs):
    """Return a 2d_tool media node dict.

    media_id                   this node's own "id" (e.g. "M1.S1.T2.C2.2D1")
    concept_id                 the concept this tool is homed on ("home_concept_id" too, unless
                                a different `kwargs["home_concept_id"]` is passed for a shared tool)
    tool_name                  shown to the student as the tool's name (STUDENT_FACING - no
                                NCERT/CBSE/textbook/page wording; gates/media_content.py bans it there)
    tool_config                the full spec dict (idea/screen/student_does/challenges/feedback/
                                done_when/shared_state/misconceptions/hint_ladder - see
                                chapter_template/concept_plan.py.template's T() builder). Must not
                                be empty - gates/media_content.py's preflight() rejects a node whose
                                tool_config is falsy.
    tool_questions              the list of challenges/questions this tool poses; required on this
                                node OR on the node `same_as` points at (preflight() checks either).
    tool_2d_url                 the reserved asset url (never reconstructed - read it straight off
                                config/ASSET_BASE the way every build.py in this pipeline does;
                                see TOOL_SPEC_GUIDE.md's "asset-upload-side rule").
    grade                       if given, asserted to appear in tool_2d_url as "class_<grade>/" -
                                the same check gates/media_content.py's preflight() runs; catches a
                                wrong ASSET_BASE substitution immediately instead of at validate time.
    same_as                     another node's id, when this tool reuses that node's tool_questions
                                instead of carrying its own (two concepts sharing one manipulative).
    instructions_for_student    one sentence of plain instructions; defaults to tool_config["idea"].
    title                       STUDENT_FACING display title; defaults to tool_name.

    Any extra keyword is merged onto the returned dict (e.g. home_concept_id= to override, or
    build_status= to mark a tool as "live" once its .tsx actually ships).
    """
    if not tool_config:
        raise ValueError("tool_config must not be empty (gates/media_content.py's preflight() "
                         "rejects a 2d_tool node with no tool_config)")
    if grade is not None and ("class_%s/" % grade) not in tool_2d_url:
        raise ValueError("tool_2d_url %r does not contain class_%s/ - build it from the chapter's "
                         "own asset_base_template, never by hand" % (tool_2d_url, grade))

    conf = dict(tool_config)
    if not same_as:
        conf["tool_questions"] = list(tool_questions)
    conf.setdefault("same_as", same_as)

    node = {
        "id": media_id,
        "type": "2d_tool",
        "subtype": subtype,
        "title": title or tool_name,
        "tool_name": tool_name,
        "concept_id": concept_id,
        "home_concept_id": concept_id,
        "2d_tool_url": tool_2d_url,
        "tool_config": conf,
        "instructions_for_student": instructions_for_student or tool_config.get("idea", ""),
        "build_status": "placeholder",
    }
    node.update(kwargs)
    return node


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------
def _minimal_plan_with_one_tool():
    tool_config = {
        "tool_id": "tool_selftest", "idea": "Drag a counter onto a number line to find its value.",
        "screen": "A number line from -10 to 10 and one draggable counter.",
        "student_does": ["Drag the counter to the number asked for."],
        "challenges": ["Place the counter at 3.", "Place the counter at -4.",
                       "Place the counter at 0.", "Place the counter at -10.",
                       "Place the counter at 10."],
        "feedback": ["A wrong placement snaps back with a gentle shake."],
        "done_when": "all 5 challenges are placed correctly.",
        "shared_state": ["counterPosition"], "misconceptions": ["M_SELFTEST_1"],
        "hint_ladder": [{"rung": "orienting", "text": "Which number does the challenge name?"},
                        {"rung": "strategic", "text": "Count from 0 in the sign the number has."},
                        {"rung": "specific", "text": "Move the counter one step at a time."},
                        {"rung": "bottom-out", "text": "The counter belongs on -4; place it there."}],
    }
    node = build_tool_node(
        media_id="M1.S1.T1.C1.2D1", concept_id="M1.S1.T1.C1", tool_name="Number Line Counter",
        tool_config=tool_config, tool_questions=tool_config["challenges"], grade=9,
        tool_2d_url="https://media.singularity-learn.com/learning_plan_assets/V2/cbse/cbse/"
                    "english/class_9/mathematics/ch_1/tool_v3/tool_selftest/index.html")
    plan = {
        "chapter_id": "cbse_eng_mathsN_selftest", "chapter_master_id": 1, "grade": 9,
        "objectives": [{"objective_id": "OBJ1", "objective_text": "Place integers on a number line."}],
        "modules": [{
            "module_id": "M1", "segments": [{
                "segment_id": "M1.S1", "topics": [{
                    "topic_id": "M1.S1.T1", "available_content_types": ["2d_tool"],
                    "concepts": [{"concept_id": "M1.S1.T1.C1"}],
                    "media": [node],
                }],
            }],
        }],
    }
    return plan


if __name__ == "__main__":
    plan = _minimal_plan_with_one_tool()
    problems = media_content.preflight(plan)
    if problems:
        print("SELF-TEST FAILED - build_tool_node() produced a node preflight() rejects:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("self-test OK: build_tool_node() output passes gates.media_content.preflight()")

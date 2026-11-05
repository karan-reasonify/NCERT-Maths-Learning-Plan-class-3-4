# -*- coding: utf-8 -*-
"""Run every gate family that applies to a built Class 3/4 plan, chosen off its chapter.config.json.

    errors, counts = run(plan, config)

`plan` is the built plan dict (Phase 2 shape, no _V3). `config` is the chapter.config.json dict, plus (added by
build.py, never by hand) `book_items` / `book_item_kinds` from content.NCERT_ITEMS.

Gate families, in the order they run:
  media_content   the structural / delivery checks the upload API itself does not make (media types, ids, dashes,
                  textbook branding in student-facing fields, tool urls under class_<grade>, tool_questions present)
  eqcheck_*       arithmetic truth in every authored string; `config["eqcheck"]` picks plain / signed / powers
                  (Class 3-4 chapters use "plain": no negatives, no powers)
  coverage        every NCERT item of the chapter maps to a concept, consistently, in both directions
  objectives      wording and anchoring of the topic and concept objectives
  flow            gates/flow_c34.py: hook -> exploration tool -> (concept video -> concept tool)* -> review, the
                  approved tool map, story-based videos, minimal images, NCERT-only tool questions

This replaces the Class 6-8 runner, which also ran the question-layout, solution-card, video-script and
skeleton / theorem gates; none of those exist here.

Blocking errors vs advisory warnings: `errors` is what validation/validate_local.py gates the stamp on.
`counts["warnings"]` is non-blocking. A message is advisory only if it contains one of ADVISORY_MARKERS:
  - "shares no key term with its own concept" (objectives.py, a shallow word-overlap check)
  - "mapped to more than one concept" (coverage.py, informational: a human judges it)
  - "sentence is long" (flow_c34.py, a reading-level heuristic for a Class 3-4 child)
Every other message from every gate blocks.

    python -B gate_runner.py <plan.json> <chapter.config.json>
"""
from __future__ import annotations

import io
import json
import sys

from . import coverage, flow_c34, media_content, objectives

EQCHECK_MODULES = {}

ADVISORY_MARKERS = (
    "shares no key term with its own concept",
    "mapped to more than one concept",
    "sentence is long",
)


def _is_advisory(message):
    return any(marker in message for marker in ADVISORY_MARKERS)


def _eqcheck_module(name):
    if name not in EQCHECK_MODULES:
        if name == "plain":
            from . import eqcheck_plain as mod
        elif name == "signed":
            from . import eqcheck_signed as mod
        elif name == "powers":
            from . import eqcheck_powers as mod
        else:
            raise ValueError("unknown eqcheck variant %r (expected plain/signed/powers)" % name)
        EQCHECK_MODULES[name] = mod
    return EQCHECK_MODULES[name]


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def _topic_tools(topic):
    return [x for x in topic.get("media") or [] if x.get("type") == "2d_tool"] \
        + [c["tool_spec"] for c in topic.get("concepts") or [] if c.get("tool_spec")]


def _authored_texts(plan):
    """Every string the gate scans for false arithmetic: content blocks, objectives, tool specs."""
    texts = []
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            for block in concept.get("content") or []:
                for field in ("text", "question", "answer"):
                    v = block.get(field)
                    if isinstance(v, str):
                        texts.append(v)
                for step in block.get("steps") or []:
                    if isinstance(step, str):
                        texts.append(step)
        if topic.get("topic_objective"):
            texts.append(topic["topic_objective"].get("objective_text", ""))
        for tool in _topic_tools(topic):
            if tool.get("tool_config"):
                texts.append(json.dumps(tool["tool_config"], ensure_ascii=False))
    for obj in plan.get("objectives") or []:
        texts.append(obj.get("objective_text", ""))
    return texts


def run_eqcheck(plan, variant, errata=None):
    """errata: exact chain strings to skip, a known printed-book error kept on purpose, never a way to silence a real
    failure. Each one must be used by the plan; an entry that matches nothing is itself an error."""
    mod = _eqcheck_module(variant)
    errata = set(errata or [])
    used = set()
    errors, n = [], 0
    for text in _authored_texts(plan):
        if variant == "plain":
            fails, checked = mod.arithmetic_in_text(text)
        else:
            fails, checked = mod.false_equations(text), mod.count_checked(text)
        n += checked
        for s in fails:
            hit = next((e for e in errata if s == e or s.startswith(e + "  ->")), None)
            if hit:
                used.add(hit)
                continue
            errors.append("false equation: %s" % s)
    errors += ["errata entry never matched (remove it from config): %s" % s for s in errata - used]
    return errors, n


def run(plan, config):
    """(errors, counts): errors is a flat list of blocking strings; counts is a dict of per-gate tallies plus
    counts["warnings"] (the non-blocking, advisory strings)."""
    errors, warnings, counts = [], [], {}

    structure_problems = media_content.preflight(plan)
    errors += ["structure: %s" % p for p in structure_problems]
    counts["structure_problems"] = len(structure_problems)

    eq_errors, n_eq = run_eqcheck(plan, config.get("eqcheck", "plain"), config.get("eqcheck_errata"))
    errors += eq_errors
    counts["equations_checked"] = n_eq
    counts["equations_failed"] = len(eq_errors)

    for name, mod in (("coverage", coverage), ("objectives", objectives), ("flow", flow_c34)):
        messages = ["%s: %s" % (name, e) for e in mod.check(plan, config)]
        blocking = [m for m in messages if not _is_advisory(m)]
        advisory = [m for m in messages if _is_advisory(m)]
        errors += blocking
        warnings += advisory
        counts["%s_problems" % name] = len(blocking)
        if advisory:
            counts["%s_warnings" % name] = len(advisory)

    counts["warnings"] = warnings
    return errors, counts


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    config = json.load(open(sys.argv[2], encoding="utf-8"))
    errors, counts = run(plan, config)
    warnings = counts.pop("warnings", [])
    print("counts:", counts)
    if warnings:
        print("%d ADVISORY WARNING(S) (non-blocking):" % len(warnings))
        for w in warnings:
            print("  ~", w)
    if errors:
        print("%d GATE FAILURE(S):" % len(errors))
        for e in errors:
            print("  -", e)
        return 1
    print("all gates passed (blocking)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

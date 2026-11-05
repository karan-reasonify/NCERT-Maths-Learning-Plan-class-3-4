# -*- coding: utf-8 -*-
"""NCERT coverage gate: every book item (example/FiO/exercise) maps to a concept, consistently, in both
directions the plan itself carries.

A built Phase 2 plan carries the book-item <-> concept map twice, independently authored by build.py from
two different places:
  - forward:  each concept's own `ncert_refs` list      (concept_id -> [book_item, ...])
  - reverse:  `source_metadata.ncert_coverage`           (book_item -> [concept_id, ...])
This was verified against the three reference phase2 JSONs (maths6_ch3, maths7_ch10, maths8_ch9): both keys
are present and populated in all three, so a plan-JSON-only cross-check of the two directions is real, not a
check that happens to find nothing because the data isn't there.

What this gate CAN verify from `plan` alone:
  - `source_metadata.ncert_coverage` exists and no book item in it maps to zero concepts (an orphaned item).
  - every concept id inside `ncert_coverage`'s values is a real, currently-numbered concept in the plan (a
    stale id left behind by a renumber - see docs/27's renumber-and-asset-pinning trap - would show up here).
  - every item inside a concept's own `ncert_refs` is a key of `ncert_coverage` (no ref the reverse map never
    heard of).
  - the two directions agree: if concept C lists item R in its `ncert_refs`, R's entry in `ncert_coverage`
    must include C, and vice versa. A one-way mismatch is a real authoring slip, not a formatting quibble -
    it means one of the two maps was hand-edited (e.g. after a renumber) and the other wasn't.
  - "exactly once": flagged as `coverage_count` info when a book item's reverse-map list holds other than
    exactly one concept (0 is already caught above as orphaned; >1 is reported so a human can decide whether
    a question genuinely gets touched by two concepts or whether it is a stray duplicate).

What this gate CANNOT verify from `plan` alone (explicit limitations):
  - The *master* list of book items. `ncert_coverage`'s keys ARE the only JSON-resident list of "every book
    item" - they are themselves written by build.py from a chapter-specific constant (e.g. K.NCERT_ITEMS)
    that is NOT reproduced anywhere else in the plan. So this gate can tell you a listed item is orphaned or
    inconsistent, but it can never tell you a printed example/FiO/exercise question was left off the list
    entirely - that would need the chapter's own content.py/exercises.py, which gate_runner never hands to a
    gate (it only ever receives `plan` + `config`). If a caller wants that check, `config["book_items"]` may
    carry an independently authored master list to compare against; without it, this limitation stands.
  - "Independent `domain_facts()`-style fact recomputation." Reading maths6_ch3/new_design/build.py's own
    `domain_facts()` (lines ~489-640) shows this is NOT a generic, JSON-derivable check: it hand-recomputes
    chapter-specific numeric trivia (Kaprekar-constant round counts, Collatz peak/step counts, palindromic
    time counts, reverse-and-add rounds, ...) that only exists as Python logic in that one chapter's build
    script. There is nothing in the plan JSON that identifies which numbers are "Kaprekar of 6382" versus an
    ordinary authored number, so a generic gate cannot re-derive or check these without re-implementing each
    chapter's bespoke maths - which is not a coverage check, it's a new per-chapter test suite. The closest
    JSON-only generic analogue already exists and is wired in: `gates/eqcheck_plain.py` / `_signed.py` /
    `_powers.py` (run by `gate_runner.run()`), which re-evaluate every literal "a op b = c" chain in authored
    text. This gate deliberately does not duplicate that.

    python -B coverage.py <plan.json>      print the problems found, if any
"""
from __future__ import annotations

import json
import sys


def walk_topics(plan):
    for module in plan.get("modules") or []:
        for segment in module.get("segments") or []:
            for topic in segment.get("topics") or []:
                yield topic


def walk_concepts(plan):
    for topic in walk_topics(plan):
        for concept in topic.get("concepts") or []:
            yield concept


def check(plan, config=None):
    """Return a list of problem strings; empty means clean. `config` may carry an optional
    `book_items` list (an independently authored master list) to additionally check `ncert_coverage`'s
    keys against - see the "CANNOT verify" note above; without it, that one check is skipped."""
    config = config or {}
    problems = []

    concepts = list(walk_concepts(plan))
    concept_ids = {c.get("concept_id") for c in concepts}

    sm = plan.get("source_metadata") or {}
    cov = sm.get("ncert_coverage")
    if not isinstance(cov, dict) or not cov:
        problems.append("source_metadata.ncert_coverage is missing or empty; "
                         "no reverse book-item -> concept map to check")
        cov = {}

    # forward map, built fresh from the concepts themselves (never trust a cached copy)
    forward = {}
    for c in concepts:
        cid = c.get("concept_id")
        for item in c.get("ncert_refs") or []:
            forward.setdefault(item, set()).add(cid)

    # 1. orphaned book items: listed in the reverse map but mapped to zero concepts
    orphaned = sorted(item for item, cids in cov.items() if not cids)
    if orphaned:
        problems.append("%d book item(s) in ncert_coverage with no concept at all: %s"
                         % (len(orphaned), orphaned[:10]))

    # 2. stale concept ids: ncert_coverage points at a concept that no longer exists in the plan
    for item, cids in cov.items():
        if not isinstance(cids, list):
            problems.append("ncert_coverage[%r] is not a list: %r" % (item, cids))
            continue
        stale = sorted(set(cids) - concept_ids)
        if stale:
            problems.append("ncert_coverage[%r] names concept(s) not in this plan (stale after a renumber?): %s"
                             % (item, stale))

    # 3. unknown refs: a concept's own ncert_refs names a book item the reverse map never heard of
    unknown_refs = sorted(set(forward) - set(cov))
    if unknown_refs:
        problems.append("%d book item(s) named in a concept's ncert_refs but absent from ncert_coverage: %s"
                         % (len(unknown_refs), unknown_refs[:10]))

    # 4. bidirectional mismatch: the two directions disagree about which concept(s) own an item
    mismatched = []
    for item in sorted(set(forward) | set(cov)):
        fwd_cids = forward.get(item, set())
        rev_cids = set(cov.get(item) or [])
        if fwd_cids != rev_cids:
            mismatched.append((item, sorted(fwd_cids), sorted(rev_cids)))
    for item, fwd_cids, rev_cids in mismatched[:15]:
        problems.append("ncert_coverage and concept.ncert_refs disagree on %r: "
                         "ncert_refs says %s, ncert_coverage says %s" % (item, fwd_cids, rev_cids))
    if len(mismatched) > 15:
        problems.append("... %d more forward/reverse mismatch(es) not shown" % (len(mismatched) - 15))

    # 5. "exactly once": informational count of items covered by other than exactly one concept
    # (0 is already reported above as orphaned; this reports the >1 case so a human can judge it)
    multi = sorted((item, cids) for item, cids in cov.items() if isinstance(cids, list) and len(cids) > 1)
    if multi:
        problems.append("%d book item(s) mapped to more than one concept (expected exactly one unless "
                         "deliberately touched twice): %s"
                         % (len(multi), [(i, c) for i, c in multi[:10]]))

    # 6. optional: an independently authored master list of book items, if the caller supplies one
    master = config.get("book_items")
    if master:
        missing_from_cov = sorted(set(master) - set(cov))
        if missing_from_cov:
            problems.append("%d book item(s) in config.book_items but missing from ncert_coverage entirely: %s"
                             % (len(missing_from_cov), missing_from_cov[:10]))

    return problems


def summarise(plan):
    sm = plan.get("source_metadata") or {}
    cov = sm.get("ncert_coverage") or {}
    concepts = list(walk_concepts(plan))
    with_refs = sum(1 for c in concepts if c.get("ncert_refs"))
    return {
        "book_items": len(cov),
        "concepts": len(concepts),
        "concepts_with_ncert_refs": with_refs,
    }


if __name__ == "__main__":
    import io
    for path in sys.argv[1:]:
        plan = json.load(io.open(path, encoding="utf-8"))
        problems = check(plan)
        print("%s: %d problem(s)" % (path, len(problems)))
        for p in problems:
            print("  -", p)
        print("  summary:", summarise(plan))

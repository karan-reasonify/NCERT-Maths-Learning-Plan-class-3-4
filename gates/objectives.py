# -*- coding: utf-8 -*-
"""Objectives gate: wording and anchoring rules for every concept/topic objective in a plan.

Generalized from the objectives section of the same three build.py's check() functions
(maths6_ch3, maths7_ch10, maths8_ch9). Ground truth taken from the live phase2 JSONs:

  * Concept objectives live in the flat plan["objectives"] list, one per non-enrichment concept,
    each anchored back with anchor == [that concept's concept_id]. Enrichment concepts (the
    intro's hook/try_it, and - per maths6_ch3/maths7_ch10's data - a stray enrichment-flagged
    idea concept here and there) carry no objective_id and no entry in plan["objectives"].
  * Topic objectives are NOT in plan["objectives"] - each lives inline as topic["topic_objective"],
    its own id namespace ("TOn" vs the concept objectives' "On"). Every idea topic has exactly
    one; the intro, the summary and every question topic have none. This gate classifies a topic
    the same way skeleton.py does - by topic["source_type"], not topic["is_enrichment"] - because
    is_enrichment turns out NOT to agree across the three reference chapters: maths7_ch10 flags
    every question topic is_enrichment True, maths6_ch3 does not (its question topics are
    is_enrichment False even though they correctly carry no topic_objective). source_type is the
    one field that spells "this is a question topic" consistently enough to build a rule on
    (modulo the configurable spelling difference also handled in skeleton.py).
  * Word limits: maths7_ch10/maths8_ch9 enforce 15-40 words for a concept objective and 30-55 for
    a topic objective; maths6_ch3 enforces only the upper bound (<=40 / <=55) with no floor. This
    gate takes the task's literal spec - 15-40 for a concept objective, <=55 for a topic
    objective (no floor) - as the default, which means it will NOT flag maths6_ch3's unusually
    short topic objectives (ch6 has none under 30 in practice) but also won't demand a floor the
    task never asked for; a chapter that wants ch7/ch8's stricter 30-word floor can set
    `topic_objective_min_words` in its config.
  * "References the concept's own content, not generic" (concept objective) and "collectively
    covers every concept in that topic" (topic objective) are both left deliberately shallow,
    matching this project's eqcheck_* style: a real but partial signal, not a semantic check.
    See `_concept_terms` / the coverage check below for exactly what is and isn't caught -
    a topic objective that covers its concepts with synonyms rather than their own vocabulary
    passes clean, and that is a known, accepted gap, not a bug.

    python -B objectives.py <plan.json> [chapter.config.json]
"""
from __future__ import annotations

import io
import json
import re
import sys

from .media_content import walk_topics

BANNED = re.compile(r"\b(learn\w*|know\w*|understand\w*|familiar\w*)\b", re.I)
_STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "into", "onto", "its", "their",
    "pull", "together", "doit", "practice", "pull it together and do it", "a", "an", "of",
    "to", "in", "on", "is", "are", "it", "do", "we", "how", "what", "why", "when", "then",
}

DEFAULTS = {
    "concept_objective_word_range": (15, 40),
    "topic_objective_min_words": 0,
    "topic_objective_max_words": 55,
    "topic_objective_coverage_min": 0.5,
    "coverage_exclude_doer_role": "doer",
    # Same spelling knobs as skeleton.py's DEFAULTS, kept duplicated rather than imported: this
    # module must give a correct answer even when run standalone with a config that only sets
    # the objectives-specific keys above, and gate_runner.py will pass one shared config dict to
    # both anyway.
    "framing_source_type": "framing",
    "summary_source_type": "summary",
    "idea_source_type": "instructional/exploration",
    "qt_source_types": ("question_topic", "exercise"),
}


def _cfg(config, key):
    return (config or {}).get(key, DEFAULTS[key])


def _words(text):
    return (text or "").split()


def _tool_names(plan):
    """Every tool title/id the student could recognise, so an objective is never caught naming
    one (the task's "no objective may name a tool" rule)."""
    names = set()
    for t in walk_topics(plan):
        for m in t.get("media") or []:
            if m.get("type") != "2d_tool":
                continue
            if m.get("title"):
                names.add(m["title"].strip().lower())
            if m.get("tool_name"):
                names.add(m["tool_name"].strip().lower())
            if m.get("tool_id"):
                names.add(str(m["tool_id"]).strip().lower())
            if m.get("id"):
                names.add(str(m["id"]).strip().lower())
    return {n for n in names if n}


def _stem(word):
    """Fold the one mismatch that would otherwise swamp this heuristic in false positives:
    plain plurals ("neighbours" vs "neighbour"). Nothing fancier - a real stemmer would also
    quietly start forgiving genuine paraphrases, which is exactly the over-engineering the task
    asked this check to avoid."""
    return word[:-1] if word.endswith("s") and len(word) > 4 else word


def _significant_words(text):
    return {_stem(w.lower()) for w in re.findall(r"[A-Za-z]+", text or "")
            if len(w) >= 4 and w.lower() not in _STOPWORDS}


def _concept_terms(concept):
    """A shallow bag of words this concept is 'about', used only for the topic-objective
    coverage heuristic and the concept-objective own-content check. key_terms is the authored
    source when present, but it is frequently empty in the reference plans, and even when
    present is often an un-tokenized phrase ("taller neighbours") that can never literally
    appear inside an objective sentence - so this mines individual words out of key_terms the
    same way it mines the concept_name, stripped of the doer/practice banner prefix, which
    names the topic's recap, not its own content."""
    terms = set()
    for phrase in concept.get("key_terms") or []:
        terms |= _significant_words(phrase)
    name = concept.get("concept_name") or ""
    name = re.split(r":\s*", name, maxsplit=1)[-1]  # drop "Pull it together and do it: " / "Practice: "
    terms |= _significant_words(name)
    return terms


def check(plan, config=None):
    """Return a list of problem strings; empty means clean."""
    problems = []
    topics = list(walk_topics(plan))
    by_oid = {o.get("objective_id"): o for o in plan.get("objectives") or []}
    if len(by_oid) != len(plan.get("objectives") or []):
        problems.append("duplicate objective ids in plan.objectives")

    concept_lo, concept_hi = _cfg(config, "concept_objective_word_range")
    topic_lo = _cfg(config, "topic_objective_min_words")
    topic_hi = _cfg(config, "topic_objective_max_words")
    coverage_min = _cfg(config, "topic_objective_coverage_min")
    doer_role = _cfg(config, "coverage_exclude_doer_role")
    tool_names = _tool_names(plan)

    anchored_to = {}  # concept_id -> objective_id, to catch a concept anchored twice
    for t in topics:
        for c in t.get("concepts") or []:
            cid = c.get("concept_id")
            oid = c.get("objective_id")
            if c.get("is_enrichment"):
                if oid:
                    problems.append("%s: an enrichment concept must carry no objective (has %s)" % (cid, oid))
                continue
            # ---- exactly one concept objective, anchored to this concept ----
            if not oid:
                problems.append("%s: no concept objective" % cid)
                continue
            obj = by_oid.get(oid)
            if not obj:
                problems.append("%s: objective_id %s is not in plan.objectives" % (cid, oid))
                continue
            if obj.get("anchor") != [cid]:
                problems.append("%s: objective %s is anchored to %r, not [%r]"
                                % (cid, oid, obj.get("anchor"), cid))
            if oid in anchored_to and anchored_to[oid] != cid:
                problems.append("objective %s is used by two concepts (%s and %s)" % (oid, anchored_to[oid], cid))
            anchored_to[oid] = cid

            text = obj.get("objective_text") or ""
            n = len(_words(text))
            if not concept_lo <= n <= concept_hi:
                problems.append("%s: objective %s is %d word(s) (keep %d to %d)"
                                % (cid, oid, n, concept_lo, concept_hi))
            hit = BANNED.search(text)
            if hit:
                problems.append("%s: objective %s uses the unobservable verb %r" % (cid, oid, hit.group(0)))
            low = text.lower()
            for tn in tool_names:
                if tn and tn in low:
                    problems.append("%s: objective %s names a tool (%r)" % (cid, oid, tn))

            # ---- anchored to its OWN content, not generic: catch an objective that is just a
            # restatement of the banner words with nothing of this concept in it ----
            own_terms = _concept_terms(c)
            if own_terms and not (own_terms & _significant_words(text)):
                problems.append("%s: objective %s shares no key term with its own concept (%r)"
                                % (cid, oid, sorted(own_terms)[:6]))

        # ---- exactly one topic objective per idea topic; none on framing/summary/question
        # topics. Classified by source_type, like skeleton.py - see the module docstring for
        # why is_enrichment can't be trusted for this. ----
        to = t.get("topic_objective")
        tid = t.get("topic_id")
        exempt_types = {_cfg(config, "framing_source_type"), _cfg(config, "summary_source_type")} \
            | set(_cfg(config, "qt_source_types"))
        if t.get("source_type") in exempt_types:
            if to:
                problems.append("%s: a %s topic must carry no topic_objective" % (tid, t.get("source_type")))
            continue
        if not to:
            problems.append("%s: missing topic_objective" % tid)
            continue
        ttext = to.get("objective_text") or ""
        n = len(_words(ttext))
        if not topic_lo <= n <= topic_hi:
            problems.append("%s: topic objective %s is %d word(s) (keep %d to %d)"
                            % (tid, to.get("objective_id"), n, topic_lo, topic_hi))
        hit = BANNED.search(ttext)
        if hit:
            problems.append("%s: topic objective %s uses the unobservable verb %r"
                            % (tid, to.get("objective_id"), hit.group(0)))
        low = ttext.lower()
        for tn in tool_names:
            if tn and tn in low:
                problems.append("%s: topic objective %s names a tool (%r)" % (tid, to.get("objective_id"), tn))

        # ---- coverage: does the topic objective touch enough of its concepts' own vocabulary?
        # Shallow heuristic, documented limitation in the module docstring. The doer/practice
        # concept is excluded on purpose: it recaps the others rather than introducing content
        # of its own, so demanding its banner words show up in the topic objective would just
        # reward restating "pull it together" instead of the actual ideas. ----
        concepts = [c for c in (t.get("concepts") or [])
                    if not c.get("is_enrichment") and c.get("source_segment_role") != doer_role]
        if concepts:
            text_words = _significant_words(ttext)
            hit_n = sum(1 for c in concepts if _concept_terms(c) & text_words)
            ratio = hit_n / len(concepts)
            if ratio < coverage_min:
                problems.append("%s: topic objective covers %d/%d concepts' own vocabulary "
                                "(want at least %.0f%%)" % (tid, hit_n, len(concepts), coverage_min * 100))

    return problems


# ------------------------------------------------------------------ self-test
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    plan = json.load(io.open(sys.argv[1], encoding="utf-8"))
    cfg = json.load(io.open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else {}
    problems = check(plan, cfg)
    print("%s: %d problem(s)" % (sys.argv[1], len(problems)))
    for p in problems:
        print("  -", p)

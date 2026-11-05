---
name: lp34
description: >-
  Build a Phase 2 learning plan for ONE NCERT Maths Mela chapter of Class 3 or Class 4 - story hook video,
  exploration tool, concept video then matching tool, NCERT practice on the tool, short review - by running the
  c34 agents in order. Use as `/lp34 <chapter>[, <book pdf>][, <teacher instruction>]`, e.g. "/lp34 class 3 ch
  2, use the kite story". Needs the content team's approved tool table. Stops at an approval point and at a
  validated local plan. Never uploads.
argument-hint: "<chapter>[, <book pdf>][, <teacher instruction>]"
---

# /lp34: one Class 3 or 4 chapter, start to finish

<!-- PIPELINE_ROOT -->
Pipeline root: the folder holding `core/`, `gates/`, `chapter_template/` (this repo). When this skill is installed in another
workspace (`core/install_claude.py`) the installer writes the absolute path on the line above: `cd` there before every command.
Chapter folder: `chapters/maths<G>_ch<N>/new_design/`. Run `core/` scripts as `python -I -X utf8`, `build.py` (from the chapter
folder) as `python3 -B -X utf8`.
**Local only: never upload, never push, never write to the database. `set_version.py` and `check_master_id.py` only read.**
Read first: `docs/02_flow_rules.md` (the rules), `docs/01_runbook.md` (the steps), `docs/03_checklist_and_gates.md`.

You orchestrate. Each step below is done by its own agent (`Agent` tool, `subagent_type` = its name). Give every agent: the
chapter folder path, the teacher instruction verbatim, and which files earlier steps wrote. Read what comes back yourself; an
agent's "done" is not evidence, its command output is. **Run the agents one after the other, never in parallel: they all edit
the same chapter files.**

## 0. Arguments and inputs

`$ARGUMENTS` is `<chapter>[, <book pdf>][, <teacher instruction>]`. Chapter forms: `class 3 ch 2`, `3.2`, `maths3_ch2`. The
instruction is free text ("use the kite story", "keep it short"); it is the teacher's wish, not a licence to break a rule.

Before scaffolding, make sure you have, and ask the user for what is missing (one message, all of it):
1. **the approved tool table** from the curriculum / content team (names, purposes, sequence). Save it verbatim to a file in the
   scratchpad. No table, no plan: do not invent tools.
2. **the ids.** `upload/chapter_ids.local.json` (git-ignored) already holds `chapter_master_id` and `subject_ref_id` for all 14
   chapters of Class 3 and of Class 4; `core/lp_start.py` reads them. Ask only if the chapter is not in that file.

## 1. Scaffold

```bash
python -I -X utf8 core/lp_start.py --raw "$ARGUMENTS" --tool-map <the table file>
```

Exit 2 = it needs something from the user: relay the message and stop. Needs PyMuPDF in the interpreter (`pip install pymupdf`). Open
`book/page_001.png`: confirm the chapter title and number. Settle every FLAG in `lp_brief.md`. If `chapters/maths<G>_ch<N>`
already exists, ask before `--force`.

## 2. `c34-chapter-analyst` then 3. `c34-tool-mapper` then 4. `c34-journey-designer`

Check each one's output before the next: `analysis.md` complete and every question has an id and a kind; the tool map verified
unchanged (`core/tool_map.py verify`); the journey is hook, exploration tool, then concept video -> tool units in the approved
order, then a review.

## 5. `c34-media-minimiser`, then `c34-question-mapper`

Then run `python3 -B -X utf8 build.py --structure` yourself. It must print `structure stage OK`; if not, send the failures back
to the right agent.

## 6. HARD STOP: show the structure, wait for approval

Show the user `structure_report.md`: the chapter and ids; topics, concepts; the number of hook and concept videos, images
(main / pinned) and tools of the approved tools; NCERT questions by kind and how many sit on each tool; the tool map; how the
teacher instruction was applied; **every clash and judgement call** (`content.CLASHES`, anything the agents flagged: a tool with
no matching concept, a concept with no NCERT question, a book order that disagrees with the tool order, a teacher instruction that
clashes with a rule); every printed-book error. **Do not decide a clash silently. Do not write briefs before approval.**

Wait for the user. On a yes: `python3 -B -X utf8 build.py --approve`. If they change anything, redo the affected steps and show
the structure again (the approval is void after any change).

## 7. `c34-brief-writer`

Writes story briefs, image briefs, tool specs, teach lines. It must end with `build.py --briefs` showing `0 brief item(s) still to
do` and `build.py` printing `all gates passed (blocking)`. Read `briefs/videos.md` yourself: each video is a story with a problem,
not a lesson.

## 8. `c34-checklist-validator`

An independent, read-only review against the ten-item checklist. If it says NOT READY, send the FAILs back to the step it names and
repeat from there. If it says READY WITH CONCERNS, put the concerns in your report.

## 9. Version, validate, dry-run (stop here)

```bash
python -I -X utf8 core/finalize_ids.py <plan.json>         # objectives O1..On, modules M1..Mn: the upload endpoint rejects the builder's ids (idempotent; run again after any build.py)
python -I -X utf8 core/check_master_id.py <plan.json>      # read-only: id, subject, medium against the live row
python -I -X utf8 core/set_version.py <plan.json>          # reads the live max version, then writes version/plan_id
python -I -X utf8 validation/validate_local.py <plan.json> # zero errors -> <plan>.stamp.json
python -I -X utf8 upload/upload_lp.py <plan.json> --dry-run
```

If `.env` / `DATABASE_URL` is missing the first two cannot run: say so and stop rather than implying they passed.

## 10. Report

Say plainly what exists and what does not: files written, the gate result, the stamp status; counts (topics, concepts, hook and
concept videos, images main / pinned, tools of approved, NCERT questions by kind); that **every video, image and tool is still a
placeholder**; every clash and judgement call and how it was decided; how the teacher instruction was handled; the validator's
verdict. **Upload only if the user then asks** (use `upload/SKILL.md`; staging first; ask before anything else). **Standing rule from
the user (5 Nov 2026) for every Class 3 and Class 4 chapter: when a new plan is built on top of versions that already exist, the
new, latest version is uploaded ACTIVE (the default: no `--no-activate`), so it becomes the chapter's active version; if that
version number already sits on the server as a draft, send the same file again with `--force`. Staging only; any other host needs
an explicit ask.** In the report say what the new version replaces (media the old active version has that the new plan lacks) and
run `upload/verify_uploaded.py`. Never claim a check passed that did not run.

## If something is not available in this session

- **`/lp34` is not offered.** Claude Code loads project skills only from the `.claude/` of the folder it was opened in. Open Claude
  Code in the pipeline folder, or run `python3 core/install_claude.py --workspace <the folder you opened>` and restart the session.
  Or skip the slash command: say `Follow <pipeline root>/.claude/skills/lp34/SKILL.md for: class 3 ch 2, <instruction>`. This file is
  plain instructions and works that way in any session.
- **The `c34-*` agent types are not offered** (same reason). Do the step with a `general-purpose` agent instead: give it the full text of
  `.claude/agents/<name>.md` as its instructions, plus the pipeline root and the chapter folder. One agent at a time, in the same order.

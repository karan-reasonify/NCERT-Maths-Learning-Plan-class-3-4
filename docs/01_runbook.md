# 01. Runbook: one chapter, start to finish

In Claude Code, from this folder: `/lp34 <chapter>[, <book pdf>][, <teacher instruction>]`, for example
`/lp34 class 3 ch 2, use the kite story`. The skill (`.claude/skills/lp34/SKILL.md`) runs the steps below with the
agents. By hand, the steps are the same. Run Python as `python3 -B -X utf8` (build) or `python -I -X utf8` (the `core/`
scripts). **Local only: nothing here uploads. `set_version.py` and `check_master_id.py` only read.**

Work in `chapters/maths<G>_ch<N>/new_design/` (Class 3 ch 2 is `chapters/maths3_ch2/new_design/`).

## 0. Inputs

Ask the user, before anything is built, for what is missing:

1. the **approved tool table** (the content team's names, purposes and sequence). No table, no build: tools are never invented.
2. the ids: `upload/chapter_ids.local.json` (git-ignored) holds `chapter_master_id` and `subject_ref_id` for all 28 chapters; ask
   only for a chapter that is not in it (a wrong id uploads good content to the wrong chapter and still says success).
3. optional: a teacher instruction.

## 1. Scaffold (deterministic)

```bash
python -I -X utf8 core/lp_start.py --raw "class 3 ch 2" --tool-map <the table file>
```

It finds the NCERT chapter PDF by itself, copies `chapter_template/`, fills `chapter.config.json`, cuts the chapter into
`book/` (`chapter.pdf`, `pages.json`, `chapter_text.md`, `outline.json`, `page_NNN.png`), locks the tool table into
`approved_tools`, and writes `lp_brief.md` + `lp_state.json`. Exit 2 means it needs something from the user: relay the
message and stop. Needs PyMuPDF (`pip install pymupdf`) in the interpreter that runs it. **Always open `book/page_001.png`**
and confirm the title and pages. Primary-class pages are pictures, boxes and activities: read every page PNG.

## 2. Analyse the chapter: `c34-chapter-analyst`

Writes `analysis.md`: learning objectives, candidate concepts, every example / activity / question with its id and kind,
the book's characters, setting and recurring objects, printed-book errors. Fills `content.py` (identity, `NCERT_ITEMS`,
`STORY`, `VISUAL_KEY`, `MISCONCEPTIONS`).

## 3. Lock the tool map: `c34-tool-mapper`

Checks `core/tool_map.py verify`, then maps each approved tool to exactly one concept and one learning objective, in the
approved order. Writes `tool_map.locked.md` and the tool entries of `tools_N.py` (title, number, objective only). Anything
that does not fit (a tool with no matching concept, a concept the tools do not cover) goes into `content.CLASHES`; it is
never fixed by renaming, reordering, adding or dropping a tool.

## 4. Design the journey: `c34-journey-designer`

Writes the topic skeleton in `topics_N.py`: the opening (hook + exploration tool), the idea topics (concept video, tool),
the review. Keys are final from here on.

## 5. Minimum media, then NCERT questions: `c34-media-minimiser`, then `c34-question-mapper`

Run one after the other (both edit `topics_N.py`). The media agent decides, concept by concept, video / image / tool /
only one, and why; the question agent homes every NCERT question on the tool (or concept) it practises and leaves out
anything from outside the chapter.

## HARD STOP: show the structure, wait for approval

```bash
python3 -B -X utf8 build.py --structure      # writes structure_report.md, runs the gates that can pass now
```

Show `structure_report.md` to the user: counts, the flow topic by topic, the tool map, every clash and judgement call,
every book error found, how the teacher instruction was applied. **Wait for approval.** Then:

```bash
python3 -B -X utf8 build.py --approve        # records the approval of exactly this structure
```

Any later change to the structure voids the approval; show it again.

## 6. Briefs: `c34-brief-writer`

Fills the story briefs (VID `story=`), image briefs (IMG fields), tool specs (T), teach lines and recaps, in language for
the age. `python3 -B -X utf8 build.py --briefs` writes `briefs/*.md` and lists every brief still incomplete.

## 7. Build and gate

```bash
python3 -B -X utf8 build.py
```

Writes `cbse_eng_maths<G>_ch<N>.json` and runs every gate. Fix the content, never the gate, until it prints zero errors.
A gate that seems wrong is a question for the user.

## 8. Final checklist: `c34-checklist-validator`

An independent read of the built plan against the ten-item checklist (`docs/02_flow_rules.md`), with evidence for every
item. It changes nothing.

## 9. Version, validate, dry-run (stop here)

```bash
python -I -X utf8 core/finalize_ids.py <plan.json>         # objectives O1..On, modules M1..Mn: the upload endpoint rejects the builder's ids (idempotent; run again after any build.py)
python -I -X utf8 core/check_master_id.py <plan.json>      # read-only: id, subject, medium against the live row
python -I -X utf8 core/set_version.py <plan.json>          # reads the live max version, writes version/plan_id
python -I -X utf8 validation/validate_local.py <plan.json> # zero errors -> <plan>.stamp.json
python -I -X utf8 upload/upload_lp.py <plan.json> --dry-run
```

If `.env` / `DATABASE_URL` is missing the first two cannot run: say so and stop. **Upload only if the user then asks**
(staging first; ask before anything else; see `upload/SKILL.md`). Standing rule from the user (5 Nov 2026), Class 3 and 4: a new
version built on top of existing ones is uploaded ACTIVE (the default; `--force` only to re-send a draft of the same version), so the
latest version becomes the chapter's active one; report what it replaces and run `upload/verify_uploaded.py`.

## 10. Report

Say plainly what exists and what does not: files written, gate result, stamp status, counts (topics, concepts, hook and
concept videos, images main / pinned, tools of approved, NCERT questions), what is still placeholder (every video, image
and tool), every clash and judgement call, how the teacher instruction was handled. Never claim a check passed that did
not run.

## If `/lp34` is not offered

Claude Code loads project skills and agents only from the `.claude/` of the folder it was opened in. Open it in this folder; or run
`python3 core/install_claude.py --workspace <the folder you opened>` and restart the session; or, in any session, say
`Follow <pipeline root>/.claude/skills/lp34/SKILL.md for: class 3 ch 2, <instruction>` (the skill is plain instructions; it
falls back to `general-purpose` agents given the text of `.claude/agents/<name>.md` when the `c34-*` agent types are missing).

## Test the pipeline itself

`python3 -B -X utf8 smoke/run_smoke.py` builds a made-up chapter end to end and breaks it 21 ways; exit 0 means the
pipeline, the approval stop and the gates all work. No network, no database.

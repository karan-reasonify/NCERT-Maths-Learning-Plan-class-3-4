# Class 3 and 4 learning plans (NCERT / CBSE)

This folder builds one Phase 2 learning-plan JSON per Class 3 or Class 4 maths chapter. Start with `/lp34 <chapter>`; the
steps are in `docs/01_runbook.md`, the rules in `docs/02_flow_rules.md`. The folder `../Learning-Plan-Maths/` is the Class 6 to 10
pipeline this was taken from: read it if you must, never change it from here.

## Always
- **The flow is fixed:** hook video -> exploration tool (the first approved tool) -> [concept video -> its matching tool -> that
  concept's NCERT questions on the tool]* -> short review. A small concept may be one image. Videos are stories, never lectures.
  Images are clean real-life context that adds something. Tools are small: one objective, simple controls, minimal text.
- **The approved tools are the content team's.** Same names, same purposes, same order. Never invent, rename, reorder, add or
  drop one; a mismatch is a clash for the user, not something to fix quietly.
- **Questions are the book's.** Only NCERT questions of the concept, on the tool of that concept. Nothing from outside the
  chapter, nothing extra or advanced.
- **Stop for approval** after `build.py --structure`. No briefs, no final build before the user says yes (`build.py --approve`).
  Do not decide a clash or a judgement call silently: list it.
- **Local only.** Never upload, never push, never write to the database unless the user asks; staging first, ask before anything else.
  **Standing rule (user, 5 Nov 2026), Class 3 and Class 4:** when the user asks for an upload and the chapter already has versions,
  the new, latest version goes up ACTIVE (no `--no-activate`; `--force` only to re-send a draft of the same version number), so it
  becomes the active version. Staging only. Say in the report what it replaces, and read it back with `upload/verify_uploaded.py`.
- **Upload needs final ids.** Run `core/finalize_ids.py <plan.json>` after every `build.py` and before `set_version.py`: the
  endpoint rejects the builder's objective ids and the `MLAST` module id.
- **Gates are not edited to make a chapter pass.** Fix the content. A gate that seems wrong is a question for the user.
- Every media item is a placeholder. Say so in every report; never say "done" for something that is only briefed.

## Text rules (anything a child reads)
Short plain sentences (Class 3 about 8 to 9 years: at most 14 words; Class 4: at most 16). No em dash, no en dash (comma,
colon or "to"); minus is U+2212; `×` and `÷`. Never "NCERT", "textbook", "page N" or "Fig." (say "your maths book"). Every
number comes from the book or is plainly the plan's own practice number; every sum must be true. Book characters and objects only.

## Ids
`upload/chapter_ids.local.json` (git-ignored, never commit or print it into tracked files) holds `chapter_master_id` and
`subject_ref_id` for all 14 chapters of Class 3 and Class 4; `core/lp_start.py` fills them in. Confirm live with
`core/check_master_id.py` before any upload.

## Commands
```
python -I -X utf8 core/lp_start.py --raw "class 3 ch 2" --tool-map <table>
python3 core/install_claude.py --workspace <folder Claude Code is opened in>      # if /lp34 is not offered
python3 -B -X utf8 build.py --structure | --approve | --briefs | (none) | --check     # from the chapter folder
python3 -B -X utf8 smoke/run_smoke.py                                                  # test the pipeline itself
```
Use `python3 -B -X utf8` for anything that imports chapter modules (`python -I` cannot).
Agents: `.claude/agents/c34-*.md`. Skill: `.claude/skills/lp34/SKILL.md`.

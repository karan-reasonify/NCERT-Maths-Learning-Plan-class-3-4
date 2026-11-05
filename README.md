# Learning-Plan-Maths-Class3-4

Builds, validates and (only when asked) uploads a CBSE **Class 3 or Class 4** maths learning plan from one NCERT Maths
Mela chapter: a story hook video, an exploration tool, then concept video -> matching tool -> that concept's NCERT
questions, concept by concept, and a short review. One Phase 2 plan JSON per chapter, checked by a shared gate library
before anything reaches the database. Media (videos, images, tools) are **placeholders** with briefs; they are made in
other folders.

It is the Class 3/4 sibling of `../Learning-Plan-Maths/` (Class 6 to 10), which it only reads from. It keeps that
pipeline's plan shape, structural / arithmetic / coverage / objective gates, validation stamp and upload scripts, and
replaces the question / answer / image / video machinery with the flow in `docs/02_flow_rules.md`.

## Quickstart

In Claude Code, from this folder:

```
/lp34 class 3 ch 2, use the kite story
```

Have ready: the content team's **approved tool table** (names, purposes, sequence). The chapter's `chapter_master_id` and
`subject_ref_id` are already in `upload/chapter_ids.local.json` (all 28 chapters; git-ignored, never committed). The skill (`.claude/skills/lp34/SKILL.md`) scaffolds the chapter, runs the agents, **stops for your approval of the
structure**, then writes the briefs, builds, gates and validates. It never uploads.

| Agent (`.claude/agents/`) | Step |
|---|---|
| `c34-chapter-analyst` | 1 analyse the NCERT chapter |
| `c34-tool-mapper` | 2 lock the tool map |
| `c34-journey-designer` | 3 design the learning journey |
| `c34-media-minimiser` | 4 decide the minimum media |
| `c34-question-mapper` | 5 map NCERT questions |
| (approval stop) | you read `structure_report.md` and say yes |
| `c34-brief-writer` | 6 create content briefs |
| `c34-checklist-validator` | final checklist, read-only |

### If `/lp34` is not offered

Claude Code only loads project skills and agents from the `.claude/` of the folder it was **opened in**.

1. Open Claude Code in this folder (`Learning-Plan-Maths-Class3-4`), **or**
2. keep working from a parent folder and install a copy there, then restart the session:
   `python3 core/install_claude.py --workspace /root/maths-learning-plan` (also `--user` for every project, `--uninstall`, `--status`), **or**
3. skip the slash command, in any session: say
   `Follow /root/maths-learning-plan/Learning-Plan-Maths-Class3-4/.claude/skills/lp34/SKILL.md for: class 3 ch 2, <instruction>`.
   If the `c34-*` agent types are not offered either, the skill tells Claude to use `general-purpose` agents with the text of
   `.claude/agents/<name>.md` as their instructions.

## The one hard rule

**No upload without a passing `validation/validate_local.py` run.** `upload/upload_lp.py` refuses to POST a plan unless a
fresh `<plan>.stamp.json` sits next to it, with a sha256 that matches the plan's current bytes. Phase 2 only: no `_V3`.

## Folder layout

| Folder | Holds |
|---|---|
| `core/` | `lp_start.py` (scaffold + cut the chapter + lock the tool table), `tool_map.py`, `install_claude.py` (make `/lp34` visible from another folder), `media_nodes.py` (placeholder story-video and image nodes), `briefs.py`, `config.py`, `set_version.py`, `check_master_id.py`, `published_media.py` |
| `gates/` | `gate_runner.py`, `flow_c34.py` (the flow gate), `media_content.py`, `eqcheck_*.py`, `coverage.py`, `objectives.py` |
| `chapter_template/` | what `lp_start.py` copies into a chapter: `build.py`, `topics_common.py`, `content.py`, `topics_1.py`, `tools_1.py`, `tool_map.md`, `chapter.config.json` |
| `tools_spec/` | `tool_node_builder.py`, `TOOL_SPEC_GUIDE.md` |
| `validation/`, `upload/` | the stamp gate and the upload scripts (`upload/SKILL.md`); `upload/chapter_ids.local.json` holds the issued ids (git-ignored) |
| `docs/` | `00_overview`, `01_runbook`, `02_flow_rules` (the rules), `03_checklist_and_gates`, `04_provenance` |
| `textbooks/` | NCERT Maths Mela: `class3/cemm1NN.pdf`, `class4/demm1NN.pdf` |
| `chapters/` | one `maths<G>_ch<N>/new_design/` per chapter |
| `smoke/` | `run_smoke.py`: builds a made-up chapter end to end and breaks it 21 ways |

## Check that the pipeline works

```
python3 -B -X utf8 smoke/run_smoke.py        # exit 0 = it works; no network, no database
```

Needs only the Python standard library; cutting a chapter out of its PDF (`core/lp_start.py`) also needs `pymupdf`.
`docs/04_provenance.md` says exactly what was taken from where, what was left out, and what was decided without asking.

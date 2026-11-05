# 04. Provenance: what was taken, what was left, what was decided

Built 4 Nov 2026 as a new folder beside `Learning-Plan-Maths/` (which was only read, never changed). The request: take
everything from the Class 6 to 10 learning-plan pipeline **except the question, answer, image and video parts**, build the
Class 3 / 4 flow from the curriculum owner's rules (`docs/02_flow_rules.md`), take things from the Class 5 chapter only
as the user ticks them, and create agents for the chapter steps.

## Taken from Learning-Plan-Maths (copied, then trimmed)

| Part | Here |
|---|---|
| `core/config.py`, `check_master_id.py`, `set_version.py`, `published_media.py` | copied; the image-generation helpers (manim, Gemini key) removed from `config.py` and `.env.example` |
| `gates/media_content.py`, `eqcheck_plain/signed/powers.py`, `coverage.py`, `objectives.py` | copied; `media_content` also scans `story_brief` and `caption` for textbook branding |
| `gates/gate_runner.py` | rewritten: runs media_content, eqcheck, coverage, objectives and the new `flow` gate |
| `validation/`, `upload/`, `tools_spec/tool_node_builder.py` | copied |
| `chapter_template/build.py` | rewritten for the Class 3/4 flow (same plan shape, same assembly of modules / topics / concepts / objectives, approval stop added) |
| `core/lp_start.py` | rewritten for Class 3 and 4: finds the NCERT chapter PDF itself, locks the tool table |
| `textbooks/class3`, `textbooks/class4` | copied (NCERT Maths Mela; the `udgam` folders were not taken, as chosen) |

## Left out, as asked (the question, answer, image and video parts)

`core/qt.py` and the "Questions: <topic>" layout (`gates/question_layout.py`, `core/question_layout_*`); question and
solution cards (`core/solutions/`, `math_solutions/`, `gates/solution_content.py`); the video-script contract and
checker (`core/video_script/`, `gates/video_script_rules.py`); image specs and the image editor (`chapter_template/
media_specs.py.template`, `MEDIA_BRIEF.md.template`, `core/image_editor/`); the Class 6-8 skeleton gate
(`gates/skeleton.py`) and the Class 9/10 theorem gate; Manim.

Their jobs are replaced by: `core/media_nodes.py` (placeholder story-video and real-life-image nodes), `core/briefs.py`
(video / image / tool briefs), and `gates/flow_c34.py`.

## Taken from the Class 5 chapter (the user's ticks)

Ticked and carried over: **primary-class scaffolding** (`lp_start.py` for Class 3 and 4, `photo_rule_band` "default");
**the content team's tool table as input** (`tool_map.md` + `core/tool_map.py`, the way Class 5 used `priority_doc.md`);
**placeholder media mode** (media are placeholders with reserved ids and urls); **upload-ready tool nodes**
(`publication_id` and an empty `2d_tool_json`); **authoring helpers** (`topics_common.py` with A, WE, FIO, DOER, TOPIC, T,
the `topics_N.py` / `tools_N.py` split, with the video and solution fields dropped and VID / IMG added); **child writing
rules** (short plain sentences, no dashes, "maths book", retuned to age 8 to 10); **the approval stop after structure**
(made mechanical: `--structure`, `--approve`).

Not ticked, so not taken: the finished Class 5 Ch1 chapter as a sample.

## Decisions made without asking (change them if wrong)

- Folder name `Learning-Plan-Maths-Class3-4`, one folder for both classes, chapters under `chapters/maths3_ch<N>` and `maths4_ch<N>`.
- The output is the same Phase 2 plan JSON as the other classes, with media as placeholders; briefs are generated from it.
- Numeric limits the rules leave open (see `docs/02_flow_rules.md`, "Notes"): video lengths, control counts, words per sentence.
- A chapter's NCERT questions sit on the tool of their concept (`tool_questions`) and on the concept, not in separate
  "Questions" topics with a video each. An exploration tool may add up to 3 "what do you notice?" prompts; they are
  not questions to answer.
- Pinned images: `placement: "pinned"` + `pinned_media_ids`. Unverified against the platform.
- `eqcheck` defaults to `plain` (no negatives, no powers in Class 3 to 4).

## Open items

- The ids (4 Nov 2026) are in `upload/chapter_ids.local.json`, git-ignored: `chapterId` = `chapter_master_id`, `subjectId` =
  `subject_ref_id` (an inference from the `chapterMaster` table's `ChapterId` / `SubjectId`; `core/check_master_id.py` proves it
  against the live row, which has NOT been run: no `DATABASE_URL` here). Ids fall as the chapter number rises, as issued.
- `core/lp_start.py` was run against real NCERT PDFs (Class 3 ch 1, 2, 5, 14; Class 4 ch 1, 3) in a scratch virtual
  environment with PyMuPDF: the chapter is cut, the title and the printed chapter number are read correctly, the tool table
  is locked. It needs PyMuPDF (`pip install pymupdf`) in whichever interpreter runs it. No real chapter has been authored
  yet: the agents have not been run on a real chapter (the tool table is the content team's input), only the pipeline
  they drive has been tested (`smoke/run_smoke.py`).
- The `c34-*` agents and `/lp34` register only when Claude Code is opened in this folder, or from a copy made by
  `core/install_claude.py` (done once for `/root/maths-learning-plan`; restart the session). The first version of the agent
  files had a YAML error (an unquoted colon in `c34-chapter-analyst`'s description), so that agent could not register; fixed.
- The original checklist item 4 was cut off in the request; its wording is a reconstruction.

# 00. Overview

## What this is

A pipeline that turns one NCERT Class 3 or Class 4 maths chapter (Maths Mela) into one **Phase 2 learning-plan JSON**,
checked by a shared gate library before anything reaches the database. It is the Class 3/4 sibling of
`Learning-Plan-Maths` (Class 6 to 10): the plan shape, the gates for structure / arithmetic / coverage / objectives, the
validation stamp and the upload scripts are the same machinery. What is different is the **learning flow** and the
**media**: see `docs/02_flow_rules.md`.

## The flow every chapter has

```
OPENING TOPIC     hook video (a story)  ->  exploration tool (the first approved tool)
IDEA TOPIC(S)     concept video (a story) -> its matching tool -> that concept's NCERT questions (on the tool)
                  ...repeated only where it adds value; a small concept may be one image instead
REVIEW TOPIC      a short revision of concepts already taught, nothing new
```

Concept roles in the plan (`concept["source_segment_role"]`): `hook`, `explore`, `story`, `image`, `tool`, `review`.
Topic types: `framing` (the opening), `instructional` (idea topics), `summary` (the review).

## Inputs and outputs

| In | |
|---|---|
| the chapter | `textbooks/class3/cemm1NN.pdf` or `textbooks/class4/demm1NN.pdf` (NCERT Maths Mela), found by `core/lp_start.py` |
| the approved tool table | from the curriculum / content team, pasted into `tool_map.md` (names, purposes, sequence). Never invented here. |
| ids | `chapter_master_id`, `subject_ref_id`: `upload/chapter_ids.local.json` (git-ignored; all 28 chapters), read by `core/lp_start.py` |
| optional | a teacher instruction |

| Out (in `chapters/maths<G>_ch<N>/new_design/`) | |
|---|---|
| `cbse_eng_maths<G>_ch<N>.json` | the Phase 2 plan, media as **placeholders** (`build_status: "placeholder"`) |
| `structure_report.md` | the structure the user approves |
| `briefs/videos.md`, `images.md`, `tools.md` | what the media team builds from |
| `analysis.md`, `tool_map.md` | the working record of steps 1 and 2 |

## What the plan carries for media

Media are made in other folders. The plan holds one placeholder node per planned item, with a reserved id and url:

- **video** (`core/media_nodes.py`): `video_kind` `hook` or `concept`, a `story_brief` (characters, setting, situation,
  problem, thread, what it leads into), the `new_idea` it explains, a target length;
- **image**: `placement` `main` or `pinned`, what it `adds`, the real-life subject, what the child should notice, a short
  caption, the shared `visuals` it draws;
- **tool** (`tools_spec/tool_node_builder.py`): the approved name and purpose (copied, never edited), ONE learning
  objective, the simple controls, a short instruction, feedback, hints, and `question_map`: the NCERT questions of its
  concept (plus up to 3 "what do you notice?" prompts on the exploration tool).

## The gates (`gates/gate_runner.py`)

| Gate | Checks |
|---|---|
| `media_content` | media types, ids, dashes, textbook branding in student-facing fields, tool urls under `class_<grade>`, tool_questions present |
| `eqcheck_*` | every `a op b = c` in authored text is true (Class 3/4 use `plain`) |
| `coverage` | every NCERT item of the chapter is attached to a concept, in both directions |
| `objectives` | wording and anchoring of topic and concept objectives |
| `flow` (`flow_c34.py`) | the flow, the approved tool map, story-based videos, minimal images, NCERT-only tool questions, age-suitable text |

`docs/03_checklist_and_gates.md` maps each item of the final checklist to the gate message that proves it.

## The approval stop

`build.py --structure` builds the plan with the media **decisions** only and writes `structure_report.md`. The user reads
it. Only after a yes does `build.py --approve` record the approval (a hash of the structure). `--briefs` and the final
build refuse without it, and refuse again if the structure changes afterwards.

## What is deliberately not here

The Class 6 to 10 "Questions: <topic>" layout, question and solution image cards, Manim rendering, the Keeko video-script
contract and its checker, the media-spec image pipeline and the image editor. See `docs/04_provenance.md`.

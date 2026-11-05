# 03. The final checklist and the gate that proves each item

`gates/flow_c34.py` messages appear as `flow: ...` in `build.py` and `validation/validate_local.py`. Items marked
"judgement" cannot be proven by a script; `c34-checklist-validator` answers them with evidence from the plan and the
briefs, and the user has the last word.

| # | Checklist item | Mechanical proof (gate message) | Judgement |
|---|---|---|---|
| 1 | Begins with a short, engaging hook video | `the chapter needs exactly 1 hook video`; `the opening topic must be exactly [hook video, exploration tool]`; `target_seconds ... over the 90-second limit`; `the hook introduces the situation, not a concept` | Is it engaging? Does the open question create curiosity? |
| 2 | First exploration tool right after the hook | `the opening topic must be exactly [hook video, exploration tool] with the tool right after the hook`; `the exploration tool must be approved tool 1` | Is it the right first tool? |
| 3 | Every concept video follows the relevant exploration and leads into its matching tool | `a tool must come right after the concept it applies to and name it in applies_to`; `a topic cannot open with a tool`; `a concept video concept holds exactly 1 video and no tool` | Does the video really lead into this tool? |
| 4 | Approved tools used in the approved order, unchanged in purpose | `the plan has N tool(s), the approved tool map has M: no tool may be added or dropped`; `tool is number X in the plan but Y in the approved sequence`; `tool name ... differs from the approved name`; `the approved purpose was changed`; `core/tool_map.py verify` | none |
| 5 | Every video uses a story / theme, not a plain explanation | `story brief is incomplete, missing [...]`; `teacher-style wording in the story brief`; `characters ... are not in the chapter's story cast`; `... is a concept video: new_idea is empty` | Is it a real story with a meaningful event or problem? |
| 6 | Images clean, minimal, genuinely useful | `N images (one clean image per concept at most)`; `say what this image adds`; `image brief is incomplete`; `the caption/prompt is over 15 words`; `visuals ... are not in the chapter's visual_key` | Does it make the concept easier to notice? |
| 7 | No unnecessary repetition across video, image and tool | `repeats the concept of ...: do not duplicate content`; `a main-flow image must bring a new real-life context ... otherwise pin it`; `duplicates ... (same title or same thing shown)` | Is the same explanation given twice in different media? |
| 8 | Tool interactions short, clear, suitable for the class | `N controls (simple controls: at most 4)`; `the instruction is over 15 words`; `a tool has ONE learning objective in one short sentence`; `N NCERT questions on one tool (at most 6...)`; `the hint ladder has exactly 4 rungs`; `sentence is long` (advisory) | Would an 8 or 9 year old know what to do without help? |
| 9 | Tool questions limited to relevant NCERT chapter questions | `tool question ... is not a book item of this chapter`; `... is homed on ..., not on this tool's concept`; `book item(s) ... are not in this chapter's NCERT_ITEMS (outside-chapter questions are excluded)`; `its NCERT question(s) ... belong on the tool that follows it`; `a concept tool carries at least one NCERT question of its concept` | Does each question really belong to its concept? |
| 10 | All NCERT concepts and required questions covered, nothing unrelated added | `coverage: N book item(s) ... missing from ncert_coverage`; `ncert_coverage and concept.ncert_refs disagree`; `the review introduces key term(s) not taught earlier`; `the review reuses taught concepts` | Is every concept of the book chapter taught, not only every question? |

Also always on: arithmetic is true (`false equation`), no em or en dash, no `NCERT` / `textbook` / `page N` in anything
the child reads (`structure:` messages), contiguous ids, tool urls under `class_<grade>/`.

Two stages: `build.py --structure` checks the shape and the media **decisions** (everything above except the brief
completeness messages); `build.py` (after approval) checks everything.

# chapter.config.json: every key

`core/lp_start.py` fills this file; the keys marked **ask** need an answer from the user. Edit by hand only with a reason.

## Identity (ids: ask the user)

| key | meaning |
|---|---|
| `chapter_id` | `cbse_eng_maths<G>_ch<N>`; never a `_V3` suffix (Phase 2 only) |
| `phase` | always `2` |
| `chapter_master_id` | **ask**: the issued id. A wrong id uploads good content to the wrong chapter and still says success. `core/check_master_id.py` compares it with the live row. |
| `subject_ref_id`, `medium_id`, `publication_id` | **ask** (subject); medium 1 = English; publication 1 = CBSE (the upload endpoint needs `publication_id`) |
| `grade`, `chapter_no`, `chapter_name` | Class 3 or 4; the chapter number as the book prints it; the title (check against `book/page_001.png`) |
| `media_tag` | short prefix for media keys (`c3x`, `c4x` ...), unique per chapter |
| `asset_base_template` | where the media will live: `.../class_{grade}/mathematics/ch_{chapter_no}`; the subject folder is always `mathematics` |

## The approved tools (the content team's, never invented)

| key | meaning |
|---|---|
| `approved_tools` | `[{"no", "name", "purpose", "flow_row"}]`, written by `core/tool_map.py lock` from `tool_map.md`. The plan must carry exactly these tools, in this order, with these names and purposes. |
| `tool_map_required` | `true`. Set `false` only when the user says this chapter has no approved tools. |

## Checks

| key | default | meaning |
|---|---|---|
| `eqcheck` | `plain` | arithmetic-truth gate: `plain` (no negatives, no powers), `signed`, `powers` |
| `eqcheck_errata` | `[]` | exact false-equation chains kept verbatim from the book; an entry that never matches is an error |
| `concept_objective_word_range` | `[5, 30]` | words in a concept objective |
| `topic_objective_max_words` | `40` | words in a topic objective |
| `coverage_exclude_doer_role` | `tool` | the role left out of the "topic objective covers its concepts" heuristic |
| `idea_topic_concept_range` | `[1, 6]` | concepts in an idea topic (a concept video and its tool are 2) |
| `max_tool_controls` | `4` | simple controls per tool |
| `max_tool_questions` | `6` | NCERT questions on one tool (a short interaction path) |
| `max_instruction_words` | `15` | words in a tool's on-screen instruction |
| `max_sentence_words` | `14` (Class 3), `16` (Class 4) | longest sentence in teach lines and recaps (advisory) |
| `video_max_seconds` | `{"hook": 90, "concept": 150}` | target length limits |
| `allow_words`, `photo_rule_band` | `[]`, `default` | carried from the other classes; `default` is the primary-class rule |

Limits that the curriculum rules leave open are defaults, not curriculum rules: change them only with the user's say-so
and write the reason in `content.CLASHES`.

## Added by build.py, never by hand

`book_items`, `book_item_kinds` (from `content.NCERT_ITEMS`) and `stage` (`structure` or `full`) are passed to the gates
at run time.

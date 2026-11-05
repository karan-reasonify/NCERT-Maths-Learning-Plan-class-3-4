# Tool spec guide (Class 3 and 4)

## Spec + placeholder

A tool here is a **spec and a placeholder**: `tool_config` on the plan's `2d_tool` node carries the whole description
(learning objective, screen, controls, instruction, feedback, hints, and the questions it asks), the `.tsx` / HTML is
built later in another folder, `2d_tool_url` is a reserved path and `build_status` is `"placeholder"`.
`tool_node_builder.build_tool_node()` makes the node; `chapter_template/build.py` calls it for every tool concept.

## Which tools exist: the content team decides

The approved tool names, purposes and sequence come from the curriculum / content team (`tool_map.md`, locked into
`chapter.config.json` as `approved_tools` by `core/tool_map.py`). A spec never renames a tool, never changes its purpose,
and never adds or drops a tool; `gates/flow_c34.py` fails the plan if it does. Tool 1 is the **exploration tool** and comes
right after the hook video. Every other tool comes right after the concept video it applies to.

## Writing a spec: `T(...)` in `tools_N.py`

```python
from topics_common import T
TOOLS = {
    "ten_bundles": T(
        "tool_ten_bundles",                 # tool_id (used in the asset path)
        "Ten Bundles",                      # title: EXACTLY the approved name
        2,                                  # approved_no: its place in the approved sequence
        "Students tie sticks into tens and read the tens and ones.",   # ONE learning objective, one short sentence
        screen="A heap of loose sticks, a blue string, a tens box and a ones box.",
        controls=["Drag sticks", "Tie a bundle", "Reset"],              # at most 4, obvious
        instruction="Drag ten sticks together and tie them.",           # at most 15 words
        feedback=["Ten sticks tie into one bundle and the tens box shows 1.",
                  "Fewer than ten sticks cannot be tied; they wait in the ones box."],   # explains the result
        done_when="Every possible bundle of ten is tied.",
        shared_state=["tens", "ones"], misconceptions=["M_TOY_1"],
        visuals=["bundle"],                 # keys of content.VISUAL_KEY: the same shape looks the same all chapter
        hints=["How many sticks make a bundle?", "Count ten sticks.",
               "Drag ten sticks to the string.", "Take 10 sticks and tie them: 10 ones make 1 ten."]),
}
```

- **One learning objective, a short interaction path.** If a tool needs more than 4 controls or more than 6 questions it is
  doing too much: raise it as a clash, do not stretch it.
- **Large visuals, minimal text.** The picture is the lesson. No menus, no scoring screens, no decoration.
- **Hints:** exactly 4 rungs: orienting, strategic, specific, bottom-out (they may be left out until the briefs stage).
- **The tool's questions are not written here.** They are the NCERT items (`FIO`) of its concept: `build.py` puts them in
  `tool_config.question_map` (`kind: "ncert"`) and in `tool_questions`. An exploration tool may add up to 3 `notice`
  prompts ("What do you notice?"); a concept tool needs at least one NCERT question. A tool never carries an unrelated,
  extra or advanced question.
- **No outside concepts.** A tool covers the concept assigned to it, not later topics.

## The asset-upload-side rule

- The subject folder in every asset path is always `mathematics`, never `maths`.
- The `2d_tool_url` an upload uses is always read off the plan's own field, never rebuilt from grade and chapter at
  upload time. `build_tool_node()` takes `tool_2d_url` as an explicit argument for that reason.
- A tool node carries `2d_tool_json: ""` until the tool is built, and the plan carries a top-level `publication_id`; the
  upload endpoint rejects a plan without them (`build.py` adds both).

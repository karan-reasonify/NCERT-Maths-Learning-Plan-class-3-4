# 02. The Class 3 and 4 flow rules (the source of truth)

These are the rules for the Class 3 and Class 4 learning plan pipeline (NCERT / CBSE), as the curriculum owner wrote
them. Every agent, the `/lp34` skill and the gates follow them. Where a rule can be checked mechanically it is a
message of `gates/flow_c34.py` (see `docs/03_checklist_and_gates.md`); the rest is judged by the
`c34-checklist-validator` agent and the user.

**Purpose.** Build a consistent pipeline for Class 3 and 4 learning plans that introduces each chapter through an
engaging story, uses the already-approved interactive tools in their intended sequence, and adds only the minimum
supporting videos and images needed to make concepts clear.

## 1. Core learning flow

1. **Hook video.** Open the chapter with a short story-based video using the chapter theme. Create curiosity and
   introduce the situation, not the full lesson.
2. **Exploration tool.** Place the first relevant exploration tool immediately after the hook. Let students observe,
   try, notice and make simple discoveries before formal explanation.
3. **Concept video.** After exploration, use a short story-led video to explain the specific concept students have just
   encountered. Continue the chapter's story / theme; do not present a plain lecture.
4. **Concept tool.** Place the matching approved tool after the concept video. The tool should let students apply or
   investigate that exact concept.
5. **Continue concept by concept.** Repeat the concept video, then the relevant tool, only where it adds value. Keep the
   approved tool sequence unchanged.
6. **NCERT practice.** Place only the NCERT questions that belong to the concept just taught. Do not add unrelated,
   extra or advanced questions to a tool.
7. **Chapter review.** End with a short revision or assessment using concepts already covered in the chapter. Avoid
   introducing new content here.

## 2. Rules for videos, images and tools

- **Videos must tell a story.** Use the chapter's characters, setting or situation as a thread. Show a meaningful event
  or problem that naturally leads to the concept. Avoid generic teacher-style explanation videos.
- **Images must show real-life context.** Use clean, relevant photographs or illustrations of familiar objects and
  situations. An image should make the concept easier to notice, not decorate the page.
- **Do not duplicate content.** If a concept is already clearly taught in a video or explored in a tool, do not add
  another image that repeats the same explanation. Add an image only when it contributes a new real-life example or
  visual reference.
- **Use an image when no video / tool is needed.** If a small concept does not need a video or an interactive tool, show
  one relevant image directly in the learning flow with a short prompt or caption.
- **Pin supporting visuals when appropriate.** If an image is only a reference or recap for a concept already taught in a
  video / tool, keep it pinned or available as supporting material instead of inserting it again in the main sequence.
- **Keep tools small and purposeful.** Each tool has one clear learning objective, simple controls, strong visuals and a
  short interaction path. Do not turn a tool into a long lesson or a collection of unrelated activities.

## 3. Tool design requirements

- Use the approved tool names, purposes and sequence exactly as provided by the curriculum / content team.
- A tool focuses on the concept assigned to it. Do not add concepts from later topics or outside the chapter.
- Use large, clear visuals and minimal on-screen text suitable for Class 3 students (about 8 to 9 years old; Class 4 is
  about 9 to 10).
- Use simple instructions and obvious controls. Students understand what to do without lengthy guidance.
- Use consistent visual representation and colours for the same shapes / objects across the chapter.
- Give feedback that helps the child understand the result. Avoid unnecessary scoring, menus or decorative elements.

## 4. Recommended content pattern for each concept

Use this only when the concept needs it. Do not force every content type into every topic.

- **Story / video:** introduces or explains one concept without repeating the hook or another video.
- **Image:** one clean real-life visual only if it adds context not already shown.
- **Tool:** one focused interaction that lets the student explore or apply the concept.

## 5. Pipeline for the development team (the agents)

| Step | What | Agent |
|---|---|---|
| 1 | **Analyse the NCERT chapter:** extract learning objectives, concepts, examples, activities. | `c34-chapter-analyst` |
| 2 | **Lock the tool map:** use the approved tool list and sequence; map each tool to its exact concept and learning objective. | `c34-tool-mapper` |
| 3 | **Design the learning journey:** hook video first, then the exploration tool, then concept videos / tools in the approved sequence. | `c34-journey-designer` |
| 4 | **Decide the minimum media:** for every concept, a story video, a real-life image, a tool, or only one of these. Avoid duplicate explanations. | `c34-media-minimiser` |
| 5 | **Map NCERT questions:** tag every relevant question to its concept and tool. Exclude outside-chapter questions. | `c34-question-mapper` |
| | **HARD STOP:** show the structure, wait for the user's approval. | `/lp34` |
| 6 | **Create content briefs:** concise video story briefs, image briefs and tool briefs in age-appropriate language and visuals. | `c34-brief-writer` |
| 7 | **Final validation checklist** (below). | `c34-checklist-validator` |

## 6. Final validation checklist

- [ ] Does the chapter begin with a short, engaging hook video?
- [ ] Does the first exploration tool come immediately after the hook?
- [ ] Does every concept video follow the relevant exploration and lead into its matching tool?
- [ ] Are the approved tools used in the approved order and unchanged in purpose? *(The original text of this item is
      cut off after "approved order and unchanged in purpose?"; this wording is the reconstruction agreed with the
      user.)*
- [ ] Does every video use a story / theme instead of a plain explanation?
- [ ] Are images clean, minimal and genuinely useful for understanding the concept?
- [ ] Is any concept being repeated unnecessarily across video, image and tool?
- [ ] Are tool interactions short, clear and suitable for Class 3?
- [ ] Are tool questions limited to relevant NCERT chapter questions for that concept?
- [ ] Are all NCERT concepts and required questions covered without adding unrelated content?

## Notes on the wording

- The original text numbers its sections 1, 2, 3, 6, 7, 8 (no 4 or 5). Nothing is known to be missing; this file groups
  the same rules under 1 to 6.
- "Pinned" is implemented as `placement: "pinned"` on the image node and a `pinned_media_ids` list on its concept, kept
  out of `media_ids` (the main sequence). Whether the learning platform already understands `pinned_media_ids` is NOT
  verified: confirm with the platform team before the first upload.
- Numeric limits that the text leaves open are config defaults, not rules the curriculum owner gave: hook video up to
  90 s, concept video up to 150 s, tool controls up to 4, instruction up to 15 words, NCERT questions per tool up to 6,
  sentences up to 14 words (Class 3) or 16 (Class 4). Change them in `chapter.config.json` with the user's say-so.

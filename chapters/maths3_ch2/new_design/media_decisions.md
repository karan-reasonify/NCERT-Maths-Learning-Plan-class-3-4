# Media decisions: Class 3, Chapter 2, "Toy Joy"

Step 4 (c34-media-minimiser), REVISED on 5 Nov 2026 after the user's decisions on the structure. Every video, image and
tool below is a PLACEHOLDER: story briefs, image briefs and tool specs come after the user approves the structure. The
approved tool map is untouched (`core/tool_map.py verify` matches). Clash numbers refer to `content.CLASHES` (1 to 14 from
the first steps, 15 to 21 from the first media pass, 22 to 25 from the question mapper, 26 and 27 new in this revision).
The questions (FIO items, SOLUTION_NOTES, `ncert` homes) were not touched: the question mapper runs next.

## The user's general principle (5 Nov 2026), in the user's own words

> We don't need to restrict all visuals and examples to objects explicitly shown in NCERT. We can use additional
> real-life examples like birthday caps, footballs, shoeboxes, bottles, dice, etc., as long as they correctly represent
> and support the concept being taught.
> 1. NCERT concepts and learning objectives must be fully aligned.
> 2. Additional examples and visuals are absolutely fine if they help children understand the same concept.
> 3. Don't introduce unrelated concepts or activities that go beyond the intended learning objective.
> 4. Don't misrepresent an object or its geometrical properties.
> 5. Use textbook examples as the foundation, not as a restriction on visual creativity.
> Please apply this principle while resolving all clashes. We want conceptually accurate, child-friendly and engaging
> learning experiences, not a textbook-only presentation.

How it was applied here: real objects are allowed wherever they are a correct example of the solid (point 2) and are shown as
the plain solid they stand for (point 4); the book's rocket, house and engine stay the foundation of the T4 unit (point 5);
nothing was added that is outside the chapter's objectives (points 1 and 3), which is why the flat circle is only a secondary
extra and the hidden-cube counting is gone.

## The user's decisions that reached the media

| # | the user said | what changed in the plan |
|---|---|---|
| 1 | Tool 1: keep the football, birthday cap, shoebox, dice and bottles. Rolling, sliding and standing may stay if shown accurately. Not only textbook illustrations. | New VISUAL_KEY keys `football`, `birthday_cap`, `shoebox`, `bottle` (`die` kept and sharpened). Tool 1 visuals are these five objects; its three notice prompts name no solid. The hook and the T2 video use the same objects. CLASH 1 decided. |
| 2 | A sphere is always a proper shaded 3D solid, never a flat disc. A flat circle drawing only if it genuinely helps, not compulsory. Cube against cuboid is suitable. | VISUAL_KEY `sphere` rewritten (shaded ball everywhere). The book's flat discs (chart, Q2, Q6, round parts of two shop toys) are not copied. New key `flat_circle` (T7 photo only). The flat circle leaves every T7 objective and key term. CLASH 2 decided. |
| 3 | Add a simple visual lead-in before Tool 8: a die with three visible faces and a setup that creates curiosity about the hidden opposite faces, without giving the answer. | T8.C1 stays ONE image concept with a fixed setup (below), now an illustration. CLASH 3, 10 and 19. |
| 6 (touches media) | Do not force explanations the context does not support. Balls as corners and sticks as edges may be an extra if accurate; otherwise keep Tool 6 on constructing. Remove hidden-cube counting unless it is part of the learning objective. | The T6 video shows the joining only. The balls and sticks link is optional, in Tool 6's feedback after the cuboid frame. M_TOY_9 and M_TOY_5 are no longer tagged on the T6 video. CLASH 6 and 17. |

## The decision in one paragraph

Every medium the content team's note names is kept; none is dropped and none is added. The note already asks for the
minimum: a hook, three concept videos (rows 3, 5, 9), one optional demo (row 11), two main images (rows 7, 13) and the
eight tools. The only medium not in the note is the lead-in image of a die before Tool 8, put there by the journey
designer (CLASH 3, CLASH 10) and now asked for by the user. The revision changes WHAT the media show, not how many there are.

**Counts: 1 hook video + 4 concept videos = 5 videos; 3 images in the main flow (T4, T7, T8), 0 pinned; 8 tools.**
Unchanged by the revision. No concept was turned into an image concept or back, because no concept lost its video or tool
and none gained one.

## The table (one row per concept)

| concept key | name | story video (new_idea) | image (placement, adds) | tool | why | duplicate check |
|---|---|---|---|---|---|---|
| T1.C1 | The Mystery of Toys | HOOK video. No new_idea (the hook explains no concept). Jaya opens a toy box and finds a football, a die, a shoebox, a bottle and a birthday cap; some roll and some stand; ends on the open question why. Names NO solid shape. | none | (Tool 1 follows) | The note and the flow rule ask for a hook. A story only. | The hook asks the question and leaves the answer to Tool 1, so the answer is given once. It names the objects, never cube, cuboid, cylinder, cone or sphere. |
| T1.C2 | Explore Shapes Around Us | none | none | Tool 1, approved. Visuals: `football`, `die`, `shoebox`, `bottle`, `birthday_cap` (real objects). Notice prompts name no solid. | Discovery before naming: the child turns the objects, groups those that look alike and pushes each to see if it rolls, slides or stands. | A picture of the same objects would repeat the tool. Tool 1 names no shape (CLASH 1). |
| T2.C1 | Meet the Solid Shapes | concept video: the five solid shapes and their names (cube, cuboid, cylinder, cone, sphere). Jaya and Devika line up the same football, die, shoebox, bottle and birthday cap from the toy box and the children name each kind. | none | (Tool 2 follows) | A big new idea (five names) with misconceptions M_TOY_6 and M_TOY_1, so a story video is right. It names what the child just handled in Tool 1. | No chart image: the video shows the objects and Tool 2 shows and names each solid. The sphere is a shaded ball only, never a flat disc (CLASH 2). The flat circle appears once, in T7. |
| T2.C2 | Meet the 3D Shapes | none | none | Tool 2, approved. Visuals: the five abstract solids and `craft_faces`, plus the real objects (`die`, `shoebox`, `bottle`, `birthday_cap`, `football`) for matching. | Rotate, name and match is the manipulation. | The video names, the tool has the child name and match: apply, not repeat. |
| T3.C1 | The Secret Parts of Shapes | concept video: the parts of a solid, faces, edges and corners, and a face is flat or curved | none (no pinned cube figure, CLASH 21) | (Tool 3 follows) | A big new idea with three misconceptions (M_TOY_3, 4, 5). The note's close-up visuals are inside the video. | The book's labelled cube is shown in the video and labelled again by the tool on tap, so a separate picture would be a third showing. |
| T3.C2 | Explore Faces, Edges and Corners | none | none | Tool 3, approved | Select, trace and identify is the manipulation. | Standard video then tool. |
| T4.C1 | Shapes in Real Constructions | none (the note asks for none; a video would repeat the image) | **main**, `new_context=True`, illustration. ONE composite of three panels: Jaya's rocket, Jaya's two-storey house, Devika's toy engine. Unlabelled. Adds: the first look at real models, each holding several solids, before Tool 4 names and counts them. | (Tool 4 follows) | The note's image set (CLASH 8: one composite, because an image concept holds one image). It is the only teaching before Tool 4, so it is main, not pinned. The book's models stay the foundation (the user's point 5), so no extra real-life example was added (CLASH 15). | Same pictures as Tool 4 on purpose (the note: "reuse the same construction visuals"): the image is a LOOK, the tool is NAME, COUNT, WHERE. Shop toys kept for the tool only, their round parts drawn as shaded balls (CLASH 16). |
| T4.C2 | Identify Shapes in Constructions | none | none | Tool 4, approved | Select, name, count and place words is the manipulation. | Uses the image's models plus the shop toys, which the image does not show. |
| T5.C1 | Let's Build Something! | concept video: making a model by arranging solid shapes and telling where each shape is placed | none | (Tool 5 follows) | The idea of telling a friend how to build, so that they build the same, is new and has misconception M_TOY_8. A story (Jaya and Devika) suits it. | The finished models were shown in T4; the video shows building in order, not naming or counting shapes. The position words are used, not taught again (CLASH 12 (a)). |
| T5.C2 | Build and Describe | none | none | Tool 5, approved | Arrange, describe and recreate is the manipulation. | Reuses the houses, rocket and tower as models to rebuild: a different act from T4. |
| T6.C1 | Building with Clay, Sticks and Cubes | concept video (short demo as a story, CLASH 9): a solid shape can be made by joining parts: balls and sticks make a frame, cubes make a bigger solid. It shows the JOINING ONLY. | none | (Tool 6 follows) | The note says "only if needed to show the process"; a tool cannot open a topic and one image cannot show joining. | No count, none of the book's figures, no tour of controls, no meaning given to balls and sticks, no hidden or visible cubes (the user's decision on CLASH 6). The optional link "8 balls are the 8 corners, 12 sticks are the 12 edges of the cuboid frame" is NOT in the video and NOT in `new_idea`: it is a line in Tool 6's feedback after the child builds the cuboid frame (briefs stage). Misconception tags removed from the video. |
| T6.C2 | Build with Clay, Sticks and Cubes | none | none | Tool 6, approved (purpose unchanged; its optional feedback line is above) | Join, build and count is the manipulation. | See T6.C1. The tool never shows the link for the 4 ball, 6 stick figure (it is drawn flat in the book, not a solid frame). |
| T7.C1 | How Are Shapes Different? | none (the note: "no video needed") | **main**, `new_context=True`, **photo**. ONE photo of real objects that shows and does not tell. CORE: a die (or a plain cube-shaped box) beside a closed shoebox, a cube beside a cuboid. SECONDARY, smaller and optional: a real ball beside a flat paper circle. Adds: real objects (Tool 7 draws solids in chart colours). | (Tool 7 follows) | The note's comparison image (CLASH 8: one image). The only teaching before Tool 7, so main. | The image shows the pairs; Tool 7 and Q6 ask the child to say the differences, so the image carries no text on the differences and does not repeat Q6's question (CLASH 18). The cube-cuboid pair is in both on purpose. The flat circle is in no objective and no key term, and Tool 7 does not need it (CLASH 2). |
| T7.C2 | Compare and Discover | none | none | Tool 7, approved | Compare and explain is the manipulation. | Q6's round shape is drawn as a shaded ball (CLASH 2), so the question mapper re-reads its sample answer. |
| T8.C1 | Opposite Faces of a Die | none | **main**, `new_context=True`, **illustration** (changed from photo). ONE picture of a plain die tucked into the corner of two upright books on a desk: three faces show, the other three are out of sight against the books and the desk. Adds: the wonder about the hidden faces, what "opposite face" means; no answer. | (Tool 8 follows) | Not in the note. Asked for by the user (decision 3): a lead-in that prepares the activity without giving the answer (CLASH 3, 10, 19). | Overlaps the die in Tool 8 and in Q7's picture. It must not show a face with its opposite, a sum of 7, a pattern or arrows, or it would answer Q7. |
| T8.C2 | Shape Challenges and Games | none | none | Tool 8, approved. Its board uses only clean examples of the five solids (CLASH 26). | Application and revision. | The image taught the idea only; the pattern and the game are the tool. |
| T9.C1 | Name the Shape and Its Parts | none (review) | none of its own; shows earlier pictures by reference | none | A review holds no new video or tool. | CLASH 20. |
| T9.C2 | Shapes in Models and Dice | none (review) | none of its own; shows earlier pictures by reference | none | Same. | CLASH 20. |

## The real objects (clean examples) and how each behaves

Each object is a correct example of its solid only when shown as the plain solid (the user's point 4). The VISUAL_KEY entry
of each says exactly how it is drawn. "Stated accurately" for Tool 1 and for the feedback of later tools:

| object (key) | solid | how it is shown | on a flat surface it behaves like this |
|---|---|---|---|
| football (`football`) | sphere | a round soccer ball with black and white patches, light and shadow, never a flat disc | rolls in every direction; it has no flat face, so it does not slide or stand |
| shoebox (`shoebox`) | cuboid | a closed box, lid on, six flat faces, square corners, no handle | slides on any flat face and stands on any flat face (big face or end); does not roll |
| die (`die`) | cube | a plain die, square corners, exact dots | slides and stands on any of its six flat faces; it tips over rather than rolls smoothly |
| bottle (`bottle`) | cylinder | a plain straight-sided bottle with a flat bottom and flat lid, NO narrow neck (a neck would make it not a cylinder) | lying down it rolls one way (sideways, not endways); upright it stands on its flat bottom or lid |
| birthday cap (`birthday_cap`) | cone | upright, pointed tip, one curved side, round rim, plain colour, no pom-pom or strap | lying down it rolls round in a circle; upright it stands on its flat round base. A real cap is hollow underneath (CLASH 27). |

Not used as clean examples (only roughly a solid, or fits none of the five): a clay pot, a watermelon, an orange, a ball of
wool, a globe on a stand, a roti stack, a cake slice, and any flat disc standing for a sphere (CLASH 26).

Tool 1 note for the brief writer: the five objects give one look-alike pair by looks (the die and the shoebox are both
boxes). The child can also group by behaviour: rolls every way, rolls one way, rolls in a circle, only slides and stands.
If the grouping needs more look-alikes, the brief writer adds them (for example a tin can, a matchbox, an ice-cream cone, a
marble), each a clean example with its own VISUAL_KEY entry; none was added here beyond the user's list.

## Against the teacher's note, row by row

| note row | medium the note names | kept? | detail decided here |
|---|---|---|---|
| 1 | hook video, story only | yes | Jaya (a book character) opens the toy box with the five objects. No solid is named and the question is not answered. |
| 2 | Tool 1 | fixed | real objects (decision 1); no media |
| 3 | concept video | yes | one idea: the five names, on the same objects. |
| 4 | Tool 2 | fixed | no media; may match with the real objects |
| 5 | concept video | yes | one idea: parts of a solid. |
| 6 | Tool 3 | fixed | no media |
| 7 | image set, main, before Tool 4 | yes, as ONE composite image | three panels, one model each, unlabelled; main (CLASH 8, 15, 16). |
| 8 | Tool 4 | fixed | reuses the image's models plus the shop toys (round parts shaded balls). |
| 9 | concept video | yes | one idea: arranging shapes and telling where each goes. |
| 10 | Tool 5 | fixed | no media |
| 11 | concept video or demo, only if needed | yes, as a short story video | one idea; shows the joining only (CLASH 9, 17); no hidden cubes. |
| 12 | Tool 6 | fixed | no media; optional balls and corners link in its feedback |
| 13 | comparison image, main, no video | yes, ONE image | photo of real objects; cube beside cuboid is the core, ball beside flat paper circle secondary (CLASH 8, 18). |
| 14 | Tool 7 | fixed | no media |
| 15 | Tool 8 only | yes, plus the lead-in image the user asked for | one illustration, die with hidden faces (CLASH 3, 10, 19). |
| 16 | question topics | no media | questions sit on the tools (CLASH 13). |
| 17 | assessment | no media of its own | the review reuses earlier pictures by reference (CLASH 14, 20). |

## What each image must show and must not show (for the brief writer)

| image | must show | must NOT show | style, placement |
|---|---|---|---|
| T4.C1 Shapes in Real Constructions | Jaya's rocket (pink cone, lavender cube, cyan cube, large orange cylinder, standing cuboids at the foot), Jaya's two-storey teal house (cubes, cones, cylinder pillars, boards), Devika's toy engine (cylinder, two cones, cab, base slab, wheels, string); the book's colours from VISUAL_KEY; same scale, plain background. | Shape names, labels, arrows, counts, outlines of parts, position words in the caption, the shop toys, the other three houses. Nothing that answers do3 to do6 or do9. | illustration (the book's own models, so Tool 4 matches), main. |
| T7.C1 How Are Shapes Different? | MAIN pair at the same angle: a die (or a plain cube-shaped box) beside a closed shoebox, real, familiar, clean. SECONDARY pair, clearly smaller or to one side: a real shaded ball (VISUAL_KEY `football`) beside a flat paper circle (`flat_circle`). | Any sentence on how they differ, Q6's question as the caption, a printed "special cuboid" explanation on the picture, a drawn flat disc STANDING FOR the ball (the circle appears only as itself, beside the ball, never in place of it). | photo, main. If the photo looks crowded the secondary pair is dropped; nothing else changes. |
| T8.C1 Opposite Faces of a Die | SETUP: a plain white die with black dots tucked into the corner where two upright maths books meet on a desk, seen from the open side. The top and two side faces show with EXACT dot counts. The underside (on the desk), the back and one side (against the books) are out of sight, so a child wonders what is on them. The three visible numbers meet at one corner of a usual die and are not 6, 5, 3 (Q7's own picture) nor 1, 2, 3 (a child would guess 4, 5, 6 behind them, which feeds M_TOY_10); for example 1, 4 and 5. | Two views, a mirror, a face together with its opposite, a sum of 7, any pattern text, arrows, a hidden face drawn in, a question mark on a face. | illustration, main. |

## Decisions recorded (the note left open, or the user's decisions left to me)

1. **The T4 image holds all three models the note names.** The house in the image is Jaya's two-storey house, the richest of
   her four. The book's models stay the foundation (the user's point 5); no real-life extra was added (CLASH 15).
2. **`shop_toys` is KEPT FOR TOOL 4 ONLY**, and its round parts are drawn as shaded balls (toy 2's red round shape and the
   head of the yellow cat in toy 3, which the book draws flat). The other three houses stay for Tool 5.
3. **T4 caption without the position words** (CLASH 12 option b is not taken).
4. **T7 keeps the secondary pair (ball beside a flat paper circle) in the ONE photo.** This is my judgement, for the user to
   overrule. Why keep: the content team's note asks for it; the user allows it when it helps; the book's own flat discs keep
   M_TOY_1 a live risk, and one flat paper circle costs no extra medium. Why only secondary: the book never teaches a flat
   circle, and the user's point 3 says not to go beyond the learning objective. So it is removed from the T7 topic
   objective, the T7.C1 objective, the key terms of T7.C1 and T7.C2 and the misconception tag of Tool 7's concept; Tool 7
   does not require it; if the picture is crowded it is dropped and nothing else changes. M_TOY_1 stays on T7.C1 (the image).
5. **T8 lead-in is ONE illustration, not a photo.** My judgement, for the user to overrule. Why: the dot counts must be
   exact (a wrong count planted just before Q7 would be a false fact, and generated photos of dice often miscount), and the
   hidden-face setup must be controlled. Setup chosen: the die in the corner of two upright books. Setups rejected:
   (a) a see-through "ghost" die with blank hidden faces: abstract, not real-life, and it draws the opposite pairs as a
   diagram; (b) a mirror under or behind the die: it shows a hidden face and answers the question; (c) fingers covering
   faces: random and unclear which faces are hidden; (d) arrows or question marks on the hidden faces: arrows are not allowed
   and question marks tell the child what to think instead of letting the setup do it. The books work because the hidden
   faces are plainly the ones touching the desk and the books, with no numbers shown.
6. **T6 video worded as ONE idea** (making a solid by joining parts), shows the joining only. Balls = corners and sticks =
   edges is an optional extra in Tool 6's feedback after the cuboid frame (8 balls, 12 sticks: exactly the 8 corners and 12
   edges Tool 3 taught). It is not used for the 4 ball, 6 stick figure. The brief writer writes it only if it is accurately
   demonstrated on screen (the user's decision 6).
7. **No pinned images** (CLASH 21 re-checked): the real objects are already in Tool 1, the T2 video, Tool 2 and the T7 photo.
8. **The hook and the T2 video use the toy box objects of Tool 1**, so the names in T2 attach to what the child just handled.
   The hook names the objects, never a solid.
9. **Tool 2's `visuals` got the five real-object keys.** This is a visuals-only edit that decision C needed (matching to
   familiar objects). Nothing else in `tools_1.py` changed besides Tool 1's `visuals` and `notice` (and one comment line).

## Considered and not added

- A chart of the five solids with real examples, pinned: Tool 2 and the T2 video already show them (CLASH 21).
- The book's labelled cube, pinned beside Tool 3: the video and the tool carry it (CLASH 21).
- A video for T4, T7 or T8: the note asks for none and a video would repeat the image.
- An image for T2, T3, T5 or T6: the video or the tool already shows it.
- An image of the real objects for Tool 1 (a "toy box" photo): Tool 1 shows the same objects at once.
- Real-life models (a photo of a real house or toy rocket) in the T4 image: the note says to reuse the construction visuals,
  and the book's models are the foundation (CLASH 15 option c stays unchosen).
- New pictures in the review: new content or duplicates (CLASH 20).

## Clashes in `content.CLASHES` touched by this revision

- DECIDED BY THE USER lines appended to: 1, 2, 3, 6, 10, 16, 18, 19 (each keeps its original text).
- Following from those decisions: 17 (T6 video), 20 (the T8 picture is an illustration).
- Re-checked, no change: 8, 15, 21.
- New: 26 (book pictures the plan does not reproduce: flat discs, roughly-round and rough objects; the flat-disc part is the
  user's, the game-border part is applied from the user's principle), 27 (a real object is only an approximate solid: the
  open hollow cap, the bottle neck, the lid, the seams, the rounded corners).

## Left to the next steps (not done here)

- **Question mapper:** the answers of ch2.q2, ch2.q6, ch2.disc1 and the sample answer of ch2.q1 ("globe") speak of the
  book's flat disc or of objects the plan treats as rough; say2's wording and the M_TOY_9 tag on T6.C2; q1c and say3 under the
  new cap of 7. I did not touch FIO items, SOLUTION_NOTES or `ncert` homes.
- **Brief writer:** the T8 caption (a curiosity prompt, not Q7's question), the real_life, shows and caption of every image,
  the optional balls-and-corners feedback line in Tool 6, Tool 8's board, look-alike objects for Tool 1 if the grouping needs
  them, and the rule that every tool says only what is true about the real objects (CLASH 27).
- **Content team (only they can change an approved purpose):** Tool 6's purpose still says "explore what they represent" and
  "count visible/hidden cubes where relevant"; the plan does not teach hidden cubes, which the user asked for.

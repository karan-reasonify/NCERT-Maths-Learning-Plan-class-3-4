# Question map: Class 3, Chapter 2, "Toy Joy"

Step 5 (c34-question-mapper), REVISED on 5 Nov 2026 after the user's decisions. Every book item of the chapter is tagged
question -> concept -> tool. The homes are written as `FIO(...)` in `topics_1.py` (`items` of the tool concept) and as
`ncert=[...]` for text and talk items. Clash numbers refer to `content.CLASHES`. Every video, image and tool is a placeholder.
Page = pdf page (printed page), as in `analysis.md`.

Result: 35 book items = 31 questions (19 exercise, 11 prompt, 1 example) + 4 not questions (3 text, 1 talk). Each item has ONE
home. Nothing is excluded: every item is from this chapter (checked against the 7 page PNGs). The user raised the cap to 7
questions per tool for THIS chapter only (`chapter.config.json` "max_tool_questions": 7, CLASH 4 and 22 option a), so the two
provisional moves of the first pass are undone: ch2.q1c is back on Tool 4 (last) and ch2.say3 is its own item on Tool 6 (right
after q9, asked on q9's screen). Nothing is PROVISIONAL any more.

## The map

Columns: id | kind | page | concept (plan key, analysis code) | tool (plan key, approved number and name) | label shown |
status. "stretch" means the home is a judgement call that the user CONFIRMED on 5 Nov 2026 (CLASH 5, 23); "activity" means a
real-world activity kept as an on-screen version on its tool (CLASH 25).

| id | kind | page | concept | tool | label | status |
|---|---|---|---|---|---|---|
| opening | text | 1 (9) | T1.C1 The Mystery of Toys (C1, C2) | none: teaching text (`ncert` of the hook) | | in (text) |
| ch2.do1 | exercise | 1 (9) | T2.C1 Meet the Solid Shapes (C1) | T2.C2, Tool 2 Meet the 3D Shapes | Let us Do, craft | in (stretch, activity, CLASH 5, 25) |
| ch2.do2 | prompt | 1 (9) | T2.C1 (C1) | T2.C2, Tool 2 | Let us Do, craft faces | in (stretch, CLASH 5) |
| ch2.do3 | prompt | 1 (9) | T4.C1 Shapes in Real Constructions (C7) | T4.C2, Tool 4 Identify Shapes in Constructions | Let us Do, rocket count | in |
| ch2.do4 | prompt | 1 (9) | T4.C1 (C8 position words, on C7) | T4.C2, Tool 4 | Let us Do, rocket between | in |
| ch2.do5 | prompt | 1 (9) | T4.C1 (C8) | T4.C2, Tool 4 | Let us Do, rocket on top | in |
| ch2.do6 | prompt | 1 (9) | T4.C1 (C8) | T4.C2, Tool 4 | Let us Do, rocket under | in |
| ch2.fig1 | text | 1 (9) | T3.C1 The Secret Parts of Shapes (C4) | none: teaching text (`ncert` of the concept video) | | in (text) |
| ch2.do7 | exercise | 2 (10) | T5.C1 Let's Build Something! (C9, also C4, C5) | T5.C2, Tool 5 Build and Describe | Let us Do, house | in (stretch, activity, CLASH 23, 25) |
| ch2.do8 | prompt | 2 (10) | T3.C1 (C5, printed-book error 8) | T3.C2, Tool 3 Explore Faces, Edges and Corners | Let us Do, from a distance | in (stretch, CLASH 5; the plan's clearer wording, below) |
| ch2.do9 | prompt | 2 (10) | T4.C1 (C7) | T4.C2, Tool 4 | Let us Do, toy engine | in |
| ch2.disc1 | prompt | 2 (10) | T4.C1 (C7) | T4.C2, Tool 4 | Let us Discuss | in (round toy parts are balls, spheres) |
| ch2.disc2 | exercise | 2 (10) | T5.C1 (C9) | T5.C2, Tool 5 | Let us Discuss, build | in (activity, CLASH 25) |
| ch2.fact1 | text | 2 (10) | T7.C1 How Are Shapes Different? (C6) | none: teaching text (`ncert` of the comparison image) | | in (text) |
| ch2.play1 | exercise | 3 (11) | T5.C1 (C9, C8) | T5.C2, Tool 5 | Let us Play, Construct and Describe | in (activity, CLASH 25) |
| ch2.play1ex | example | 3 (11) | T5.C1 (C8, C9) | T5.C2, Tool 5 | Let us Play, Example | in (missing word fixed, SOLUTION_NOTES) |
| ch2.q1 | exercise | 3 (11) | T2.C1 (C3, C2) | T2.C2, Tool 2 | Let us Do, Q1 | in (activity, CLASH 25; sample uses real clean objects, CLASH 26) |
| ch2.q1a | exercise | 3 (11) | T2.C1 (C3) | T2.C2, Tool 2 | Let us Do, Q1(a) | in (stretch, CLASH 5) |
| ch2.q1b | exercise | 3 (11) | T2.C1 (C3) | T2.C2, Tool 2 | Let us Do, Q1(b) | in (stretch, CLASH 5) |
| ch2.q1c | exercise | 3 (11) | T4.C1 (C7) | T4.C2, Tool 4, last in its list | Let us Do, Q1(c) | in (back on Tool 4 since the cap is 7, CLASH 22 option a) |
| ch2.note1 | talk | 4 (12) | T2.C1 (C3, C13, C2) | none: teaching text (`ncert` of the concept video) | | in (talk) |
| ch2.q2 | exercise | 4 (12) | T2.C1 (C2) | T2.C2, Tool 2 | Let us Do, Q2 | in (the sphere is a ball and gets no mark) |
| ch2.q3 | exercise | 4 (12) | T3.C1 (C5, C4) | T3.C2, Tool 3 | Let us Do, Q3 | in (fourth bullet: none of the five, Sample answer, SOLUTION_NOTES) |
| ch2.q4 | exercise | 5 (13) | T6.C1 Building with Clay, Sticks and Cubes (C11) | T6.C2, Tool 6 Build with Clay, Sticks and Cubes | Let us Do, Q4 | in (activity, CLASH 6, 25) |
| ch2.q5 | exercise | 5 (13) | T6.C1 (C12) | T6.C2, Tool 6 | Let us Do, Q5 | in (activity, CLASH 25) |
| ch2.play2 | exercise | 5 (13) | T8.C1 Opposite Faces of a Die (C14, C13) | T8.C2, Tool 8 Shape Challenges and Games | Let us Play, board game | in (activity, CLASH 23, 25, 26; the board has real clean objects only) |
| ch2.q6 | exercise | 6 (14) | T7.C1 (C10) | T7.C2, Tool 7 Compare and Discover | Let us Do, Q6 | in (CLASH 2; the round shape is a ball, five solids) |
| ch2.q7 | exercise | 6 (14) | T8.C1 (C13) | T8.C2, Tool 8 | Let us Do, Q7 | in (CLASH 3; picture shows 6, 5, 3 only, Sample answer, SOLUTION_NOTES) |
| ch2.q8 | exercise | 6 (14) | T5.C1 (C9) | T5.C2, Tool 5 | Let us Do, Q8 | in |
| ch2.say1 | prompt | 7 (15) | T6.C1 (C12) | T6.C2, Tool 6 | Let us Do, bubble (cube and cuboid) | in (stretch, CLASH 23) |
| ch2.say2 | prompt | 7 (15) | T6.C1 (C12) | T6.C2, Tool 6 | Let us Do, bubble (how many cubes) | in (plan's own countable stack, no hidden cubes, CLASH 6, 28) |
| ch2.q9 | exercise | 7 (15) | T6.C1 (C12) | T6.C2, Tool 6 | Let us Do, Q9 | in (stretch, activity, CLASH 5, 25; "ways" against "shapes", SOLUTION_NOTES) |
| ch2.say3 | prompt | 7 (15) | T6.C1 (C12) | T6.C2, Tool 6, right after q9, asked on q9's screen | Let us Do, Q9 bubble | in (stretch, CLASH 5; its own item since the cap is 7, CLASH 22) |
| ch2.q10 | exercise | 7 (15) | T5.C1 (C7, C9) | T5.C2, Tool 5 | Let us Do, Q10 | in (stretch, CLASH 23) |
| ch2.q11 | exercise | 7 (15) | T6.C1 (C12) | T6.C2, Tool 6 | Let us Do, Q11 | in (activity, CLASH 25) |

## Per tool

| Tool | tool concept | book questions on the tool | count | against the cap of 7 |
|---|---|---|---|---|
| 1 Explore Shapes Around Us | T1.C2 (explore) | none (its 3 notice prompts are the plan's own; CLASH 1) | 0 | ok |
| 2 Meet the 3D Shapes | T2.C2 | do1, do2, q1, q1a, q1b, q2 | 6 | ok |
| 3 Explore Faces, Edges and Corners | T3.C2 | q3, do8 | 2 | ok |
| 4 Identify Shapes in Constructions | T4.C2 | do3, do4, do5, do6, do9, disc1, q1c | 7 | at the cap |
| 5 Build and Describe | T5.C2 | do7, disc2, play1, play1ex, q8, q10 | 6 | ok |
| 6 Build with Clay, Sticks and Cubes | T6.C2 | q4, q5, say1, say2, q9, say3, q11 | 7 | at the cap |
| 7 Compare and Discover | T7.C2 | q6 | 1 | ok |
| 8 Shape Challenges and Games | T8.C2 | q7, play2 | 2 | ok |

31 questions = 0 + 6 + 2 + 7 + 6 + 7 + 1 + 2. The hook (T1.C1) and the review (T9) hold no book item of their own.

Stretches (homes confirmed by the user, CLASH 5 and 23): do1, do2, q1a, q1b on Tool 2; do8 on Tool 3; do7 and q10 on Tool 5;
say1, q9 and say3 on Tool 6. Nothing was moved from the tool mapper's proposal.

## do8: the plan's clearer wording (CLASH 5, 23, SOLUTION_NOTES)

In the book, do8 is the LAST SENTENCE of the house activity on the second page: "Collect objects to make a house. Name the
shapes, and talk about their faces and edges. Which are straight and which are curved? Also, describe how the shapes have been
arranged. What part of the shapes can you see from a distance?" It is about the child's house of shapes seen from far away, and
"part" means the faces, edges and corners of Tool 3. The book's own wording stays in `NCERT_ITEMS` and `analysis.md`; the FIO
question on Tool 3 is the plan's clearer wording of it:

- Question: "Here is a house made of solid shapes. Imagine you stand far away from it. What parts of the shapes can you still
  see? The parts are faces, edges and corners."
- Steps: "Look at the house from far away." / "Say which parts you can still see."
- Answer: "Sample answer: the faces. From far away, the big faces are the easiest to see. Your maths book gives no answer, so
  this is our own reading. Your answer may differ."
- House picture on Tool 3: the plan's own simple house, a yellow cuboid for the walls and a lavender cone for the roof, drawn
  like Tool 3's solids (VISUAL_KEY cuboid and cone, both already in Tool 3's visuals), seen first small from far away and then
  close up. It is NOT Jaya's two-storey house (reserved for the T4 image) and not one of Jaya's other three houses (kept for
  Tool 5).

## Teaching text (not questions)

`opening` on T1.C1 (hook), `note1` on T2.C1, `fig1` on T3.C1, `fact1` on T7.C1. They sit in `ncert` of the teaching concept, not
on a tool. (`ch2.say3` is no longer listed under `ncert`: it is a tool question.)

## Excluded (outside this chapter, or extra and advanced)

None. All 35 items in `content.NCERT_ITEMS` are printed in this chapter's 7 pages, and nothing else is on a tool. Looked at and
not added, because the book does not set it here:
- the note's "roll, slide or stand" exploring, a "different view" challenge, a sphere against a flat circle and hidden against
  visible cubes: they are not book questions (CLASH 1, 2, 6, 7); they live in the tools' own prompts, not in this list;
- a question for "balls are corners, sticks are edges" on Tool 6: not a book question; the link, if shown at all, is Tool 6's
  feedback at the briefs stage (CLASH 6);
- the game border pictures, Q4 and Q5 figures and the page-7 stack: they are pictures of questions already mapped, not
  questions;
- no question was written for Tool 1, no "extra" or "advanced" question was added anywhere.

## Answers (CLASH 24, user decision of 5 Nov 2026)

Official answer key: NONE FOUND (searched textbooks/, docs/, upload/, this chapter's book folder and text layer, and the
sibling folders Learning-Plan-Maths and Image-Pipeline-Maths: the only solution material there is for other classes). So
every plan-made answer begins exactly "From the picture" (counts, positions, what a picture shows) or "Sample answer" (open
tasks, games and geometry the book does not print), open tasks end "Your answer may differ", and none reads as an official
textbook answer. Q3's fourth bullet is "none of the five", labelled Sample answer. Q7 reads "Sample answer: on a usual die, ...".
Printed-book errors that touch a question are in `content.SOLUTION_NOTES`: Q3's fourth bullet, Q7's picture, the Example's
missing word, the engine blanks, Q9 against its bubble, say2's stack, the page numbers in the game sentence, do8, and the flat
sphere.

## Notes for the user

- Wording: question text is the book's, with these changes: the Example's missing word is put back (on top of); the game
  sentence says "the pages in your maths book" instead of the printed page numbers and adds "You can play it on the screen"; for
  Q1 the table's five column names are added after the book's sentence; do8 is the plan's clearer wording (above); Q9 and its
  bubble are now two items (the bubble's sentence is its own question).
- The sphere is always a shaded ball (CLASH 2): Q2's yellow ball gets no mark because no instruction in Q2 applies to a sphere;
  Q6 compares five solids; disc1's round toy parts are spheres; Q1's sample answer uses a football and a marble, never a globe,
  a clay pot, a watermelon, a cake slice or a roti stack (CLASH 26).
- say2: the book's words, asked on the plan's own stack in which every cube can be seen or counted by turning it; the words
  "hidden" and "visible" are not used with the child. The tag M_TOY_9 is removed from Tool 6 (CLASH 6, 28). For the user to
  confirm: that a plan-made stack may stand in for the book's picture for this one bubble (CLASH 28).
- The ten real-world activities (do1, do7, disc2, play1, q1, q4, q5, q9, q11, play2) are on-screen versions on their tools, each
  with a one- or two-line task in its steps (CLASH 25).

# Question map: Class 4, Chapter 1, "Shapes Around Us"

Step 5 (c34-question-mapper). Every book item of the chapter is tagged question -> concept -> tool. The homes are written as
`FIO(...)` in `topics_1.py` (`items` of the tool concept, or of the image concept T2.C1 that no tool follows) and as
`ncert=[...]` for text and talk items. Clash numbers refer to `content.CLASHES`. Every video, image and tool is a placeholder.
Page = pdf page = printed page, as in `analysis.md`. The 22 tools and their order are the pipeline's PROPOSAL (CLASH 1).

Result: 131 book items = 109 questions (1 example, 59 exercises, 49 prompts) + 22 not questions (17 text, 5 talk). Each item has
ONE home. Nothing is excluded: every item is printed in this chapter's 23 pages (checked against the 23 page images), and
`NCERT_ITEMS` matches `analysis.md` section 5 exactly (131 ids, same kinds). The cap is 6 per tool (`chapter.config.json`
"max_tool_questions": 6, untouched). The proposal had Tools 2, 13 and 14 at 7; three questions sit one tool away from the
proposal ONLY because of the cap (PROVISIONAL, CLASH 30): cube_prism, straw_rect_angles, straw_compare. Option (b), cap 7, puts
them back with three small edits.

## The map

Columns: id | kind | page | concept (plan key, name, analysis code) | tool (tool concept, approved number and name) | label shown |
status. "in" = homed once; "PROVISIONAL" = moved only because of the cap (CLASH 30).

| id | kind | page | concept | tool | label | status |
|---|---|---|---|---|---|---|
| opening | text | 1 | T1.C1 Diksha's Trip to Delhi (C1) | none: teaching text (`ncert` of the hook) | | in (text) |
| ch1.model1 | exercise | 1 | T1.C2 Blocks for Buildings (C1) | T1.C2, Tool 1 Blocks for Buildings | Opening, Task | in (activity, CLASH 9, 16) |
| ch1.model_q1 | prompt | 1 | T1.C2 (C1) | T1.C2, Tool 1 | Opening, Q1 | in (CLASH 9) |
| ch1.model_q2 | prompt | 1 | T1.C2 (C1) | T1.C2, Tool 1 | Opening, Q2 | in (CLASH 9) |
| ch1.model_q3 | prompt | 1 | T1.C2 (C1) | T1.C2, Tool 1 | Opening, Q3 | in (CLASH 9; answer in everyday words, no solid named) |
| ch1.model_q4 | prompt | 1 | T1.C2 (C1) | T1.C2, Tool 1 | Opening, Q4 | in (CLASH 9) |
| ch1.model_q5 | prompt | 1 | T1.C2 (C1) | T1.C2, Tool 1 | Opening, Q5 | in (CLASH 9) |
| ch1.model_talk | talk | 1 | T1.C2 (C1) | none: teaching text (`ncert` of T1.C2) | | in (talk) |
| ch1.project1 | exercise | 2 | T2.C1 Bricks and the Qutub Minar (C1) | none: image concept, no tool follows (`items` of T2.C1) | Project Work | in (offline, CLASH 8, 16; teacher line dropped, CLASH 13, 32) |
| ch1.qutub_say | text | 2 | T2.C1 (C1) | none: teaching text (`ncert` of T2.C1) | | in (text) |
| ch1.qutub_q1 | prompt | 2 | T2.C1 (C1) | none: image concept (`items` of T2.C1) | Qutub Minar, Q1 | in (CLASH 8, 29) |
| ch1.qutub_q2 | prompt | 2 | T2.C1 (C1) | none: image concept | Qutub Minar, Q2 | in (CLASH 8, 29) |
| ch1.qutub_q3 | prompt | 2 | T2.C1 (C1) | none: image concept | Qutub Minar, Q3 | in (CLASH 8, 29; uses the book's 5 storeys) |
| ch1.qutub_fact | text | 2 | T2.C1 (C1) | none: teaching text (`ncert` of T2.C1) | | in (text) |
| ch1.bricks_text | text | 2 | T2.C1 (C1) | none: teaching text (`ncert` of T2.C1) | | in (text) |
| ch1.bricks_q | prompt | 2 | T2.C1 (C1) | none: image concept | Bricks | in (CLASH 8, 29) |
| ch1.note_boxes | text | 2 | T2.C1 (C1) | none: teaching text (`ncert` of T2.C1) | | in (text; teacher note, CLASH 13) |
| ch1.craft1 | exercise | 3 | T2.C1 (C2) | none: image concept | Craft, Q1 | in (offline, CLASH 8, 16) |
| ch1.net_text | text | 3 | T7.C1 Nets of Solids (C2) | none: teaching text (`ncert` of T7.C1) | | in (text; moved with the nets, CLASH 5) |
| ch1.craft2 | exercise | 3 | T7.C2 Fold the Net (C2) | T7.C2, Tool 9 Fold the Net | Craft, Q2 | in (activity, CLASH 5, 10, 16; E24) |
| ch1.prism_q1 | prompt | 3 | T2.C3 Prism or Pyramid (C2) | T2.C3, Tool 2 Prism or Pyramid | Prisms, Q1 | in |
| ch1.prism_q2 | prompt | 3 | T2.C3 (C2) | T2.C3, Tool 2 | Prisms, Q2 | in |
| ch1.prism_q3 | prompt | 3 | T2.C3 (C2) | T2.C3, Tool 2 | Prisms, Q3 | in ("such faces" has two readings, CLASH 33) |
| ch1.pyr_q1 | prompt | 3 | T2.C3 (C2) | T2.C3, Tool 2 | Pyramids, Q1 | in |
| ch1.pyr_q2 | prompt | 3 | T2.C3 (C2) | T2.C3, Tool 2 | Pyramids, Q2 | in |
| ch1.pyr_q3 | prompt | 3 | T2.C3 (C2) | T2.C3, Tool 2 | Pyramids, Q3 | in (the triangular pyramid's other shape is its triangle base) |
| ch1.cube_prism | prompt | 3 | T3.C2 Faces, Corners and Edges (C2) | T3.C2, Tool 3 Faces, Corners and Edges | Craft, cube and prism | in, PROVISIONAL (proposal: Tool 2; moved only because of the cap, CLASH 3, 30) |
| ch1.prism_pyr_talk | talk | 3 | T2.C2 Prisms and Pyramids (C2) | none: teaching text (`ncert` of T2.C2) | | in (talk) |
| ch1.craft3 | exercise | 4 | T3.C2 Faces, Corners and Edges (C3) | T3.C2, Tool 3 | Craft, Q3 | in (activity, CLASH 16) |
| ch1.fve | prompt | 4 | T3.C2 (C3) | T3.C2, Tool 3 | Craft, F+V−E | in (en dash shown as minus, CLASH 32) |
| ch1.sort_faces | exercise | 4 | T3.C2 (C3) | T3.C2, Tool 3 | Sorting by flat faces | in (E3) |
| ch1.three_faces | prompt | 4 | T3.C2 (C3) | T3.C2, Tool 3 | Sorting by flat faces, 3 faces | in (E2: both readings given) |
| ch1.sort_edges | exercise | 4 | T3.C2 (C3) | T3.C2, Tool 3 | Sorting by straight edges | in (E3) |
| ch1.observe1 | prompt | 5 | T3.C4 Opposite Faces (C4) | T3.C4, Tool 4 Opposite Faces | Let Us Observe, Q1 | in (E6: "on a usual die") |
| ch1.observe2 | prompt | 5 | T3.C4 (C4) | T3.C4, Tool 4 | Let Us Observe, Q2 | in |
| ch1.observe3 | prompt | 5 | T3.C4 (C4) | T3.C4, Tool 4 | Let Us Observe, Q3 | in (the three views fit one cube only: red with purple, yellow with orange) |
| ch1.border1 | exercise | 5 | T4.C2 Spot the Faces (C5) | T4.C2, Tool 5 Spot the Faces | Border, Q1 | in (E7; "for example", CLASH 12, 31) |
| ch1.border2 | exercise | 5 | T4.C2 (C5) | T4.C2, Tool 5 | Border, Q2 | in (E7; "for example", CLASH 31) |
| ch1.border3 | exercise | 5 | T4.C2 (C5) | T4.C2, Tool 5 | Border, Q3 | in (E7) |
| ch1.border4 | exercise | 5 | T4.C2 (C5) | T4.C2, Tool 5 | Border, Q4 | in (E7) |
| ch1.border5 | exercise | 5 | T4.C2 (C5) | T4.C2, Tool 5 | Border, Q5 | in (E7; waits for the user's reading, CLASH 12) |
| ch1.sort1 | exercise | 6 | T4.C4 Sort the Solids (C5) | T4.C4, Tool 6 Sort the Solids | Sorting 3D Shapes, (1) | in |
| ch1.sort2 | exercise | 6 | T4.C4 (C5) | T4.C4, Tool 6 | Sorting 3D Shapes, (2) | in (the sphere has no edges) |
| ch1.sort3 | exercise | 6 | T4.C4 (C5) | T4.C4, Tool 6 | Sorting 3D Shapes, (3) | in |
| ch1.sort3_q | prompt | 7 | T4.C4 (C5) | T4.C4, Tool 6 | Sorting 3D Shapes, circles | in (E4) |
| ch1.sort4 | exercise | 7 | T4.C4 (C5) | T4.C4, Tool 6 | Sorting 3D Shapes, curved and flat | in ("previous page" reworded, CLASH 32) |
| ch1.note_venn | text | 7 | T4.C3 Two Circles That Overlap (C5) | none: teaching text (`ncert` of T4.C3) | | in (text; teacher note, CLASH 13) |
| ch1.build1 | exercise | 7 | T5.C2 Build and Draw Cubes (C6) | T5.C2, Tool 7 Build and Draw Cubes | Build with Cubes | in (activity, CLASH 16) |
| ch1.towers | prompt | 7 | T5.C2 (C6) | T5.C2, Tool 7 | Cube Towers | in (CLASH 18: first tower 30, second tower NO number) |
| ch1.dotcubes | exercise | 8 | T5.C2 (C7) | T5.C2, Tool 7 | Drawing Cubes on a Triangular Dot Paper | in (CLASH 4) |
| ch1.solids_q1 | exercise | 8 | T6.C2 Solid Riddles (C8) | T6.C2, Tool 8 Solid Riddles | Solids, Q1 | in (E5) |
| ch1.solids_q2 | talk | 8 | T6.C1 Guess My Solid (C8) | none: teaching text (`ncert` of T6.C1) | | in (talk) |
| ch1.solids_q3 | exercise | 9 | T7.C2 Fold the Net (C9) | T7.C2, Tool 9 Fold the Net | Solids and nets, Q3 | in |
| ch1.solids_q4 | exercise | 9 | T7.C2 (C9) | T7.C2, Tool 9 | Solids and nets, Q4 | in (E1) |
| ch1.solids_q5 | exercise | 9 | T7.C2 (C9) | T7.C2, Tool 9 | Solids and nets, Q5 | in |
| ch1.angle_text | text | 10 | T8.C1 Where Two Lines Meet (C10) | none: teaching text (`ncert` of T8.C1) | | in (text) |
| ch1.yoga_text | text | 10 | T8.C1 (C10) | none: teaching text (`ncert` of T8.C1) | | in (text) |
| ch1.house_ex | example | 10 | T8.C2 When Lines Meet (C10) | T8.C2, Tool 10 When Lines Meet | Example | in (the solved example: 7 angles) |
| ch1.boat_q | prompt | 10 | T8.C2 (C10) | T8.C2, Tool 10 | When Lines Meet | in (E8: 10 marks) |
| ch1.angles_do1 | exercise | 10 | T8.C2 (C10) | T8.C2, Tool 10 | Let Us Do, Q1 | in |
| ch1.angles_do2 | prompt | 11 | T8.C2 (C10) | T8.C2, Tool 10 | Let Us Do, Q2 | in (classroom picture, CLASH 16) |
| ch1.right_make | exercise | 11 | T9.C2 Right Angle Checker (C11) | T9.C2, Tool 11 Right Angle Checker | Right Angles | in (activity, CLASH 16) |
| ch1.right_circle | exercise | 11 | T9.C2 (C11) | T9.C2, Tool 11 | Right Angles, dot grid | in (E9) |
| ch1.right_objects | exercise | 11 | T9.C2 (C11) | T9.C2, Tool 11 | Right Angles, objects | in (classroom picture, CLASH 16) |
| ch1.right_do1 | exercise | 12 | T9.C2 (C11) | T9.C2, Tool 11 | Let Us Do, Q1 | in |
| ch1.acute_text | text | 12 | T9.C3 Acute and Obtuse Angles (C12) | none: teaching text (`ncert` of T9.C3) | | in (text) |
| ch1.acute_obj | prompt | 12 | T9.C4 Acute or Obtuse (C12) | T9.C4, Tool 12 Acute or Obtuse | Acute and Obtuse Angles, acute | in (classroom picture, CLASH 16) |
| ch1.obtuse_obj | prompt | 12 | T9.C4 (C12) | T9.C4, Tool 12 | Acute and Obtuse Angles, obtuse | in (classroom picture, CLASH 16) |
| ch1.letters | exercise | 12 | T9.C4 (C12) | T9.C4, Tool 12 | Acute and Obtuse Angles, letters | in (E10: no count for A) |
| ch1.ao_do1a | exercise | 13 | T9.C4 (C12) | T9.C4, Tool 12 | Let Us Do, Q1 (acute) | in |
| ch1.ao_do1b | exercise | 13 | T9.C4 (C12) | T9.C4, Tool 12 | Let Us Do, Q1 (obtuse) | in |
| ch1.ao_do2 | exercise | 13 | T9.C4 (C12) | T9.C4, Tool 12 | Let Us Do, Q2 | in (E10: method, no count) |
| ch1.straw_tri_make | exercise | 14 | T10.C2 Push the Straw Shapes (C13) | T10.C2, Tool 13 Push the Straw Shapes | Shapes with Straws, triangle | in (activity, CLASH 16) |
| ch1.straw_tri_push | prompt | 14 | T10.C2 (C13) | T10.C2, Tool 13 | Shapes with Straws, triangle push | in (E11) |
| ch1.straw_tri_trace | exercise | 14 | T10.C2 (C13) | T10.C2, Tool 13 | Shapes with Straws, trace | in (offline notebook task, CLASH 16) |
| ch1.straw_tri_angles | prompt | 14 | T10.C2 (C13) | T10.C2, Tool 13 | Shapes with Straws, triangle angles | in (E11) |
| ch1.straw_rect_make | exercise | 14 | T10.C2 (C13) | T10.C2, Tool 13 | Shapes with Straws, rectangle | in (activity, CLASH 16) |
| ch1.straw_rect_angles | prompt | 14 | T9.C2 Right Angle Checker (C13) | T9.C2, Tool 11 Right Angle Checker | Shapes with Straws, rectangle angles | in, PROVISIONAL (proposal: Tool 13; moved only because of the cap, CLASH 3, 30) |
| ch1.straw_rect_push | prompt | 14 | T10.C2 (C13) | T10.C2, Tool 13 | Shapes with Straws, rectangle push | in (E11) |
| ch1.straw_rect_after | prompt | 14 | T10.C4 Angles After the Push (C13) | T10.C4, Tool 14 Angles After the Push | Shapes with Straws, after the push | in (E11) |
| ch1.straw_square | prompt | 14 | T10.C4 (C13) | T10.C4, Tool 14 | Shapes with Straws, square | in (E11) |
| ch1.straw_compare | prompt | 14 | T14.C2 Sides and Angles (C13) | T14.C2, Tool 19 Sides and Angles | Shapes with Straws, compare | in, PROVISIONAL (proposal: Tool 14; moved only because of the cap, CLASH 3, 30) |
| ch1.note_rigid | text | 14 | T10.C1 Rigid Shapes (C13) | none: teaching text (`ncert` of T10.C1) | | in (text; teacher note, CLASH 13) |
| ch1.dotshapes | exercise | 15 | T11.C2 Angles in Shapes (C14) | T11.C2, Tool 15 Angles in Shapes | Shapes on a dot grid | in |
| ch1.dotshapes_q | prompt | 15 | T11.C2 (C14) | T11.C2, Tool 15 | Shapes on a dot grid, Discuss | in (headed "Discuss" but counts shapes: a prompt; "3 right angles: none") |
| ch1.fourside_q | prompt | 15 | T11.C2 (C14) | T11.C2, Tool 15 | Four-sided shapes | in (E12: the three shapes are not named) |
| ch1.note_square | text | 15 | T11.C1 Right Angles in Shapes (C14) | none: teaching text (`ncert` of T11.C1) | | in (text; teacher note, CLASH 13) |
| ch1.pentagon_make | exercise | 16 | T10.C4 Angles After the Push (C15) | T10.C4, Tool 14 | Shapes with Straws, pentagon | in (CLASH 4, 6, 19, 23) |
| ch1.pentagon_q1 | prompt | 16 | T10.C4 (C15) | T10.C4, Tool 14 | Shapes with Straws, pentagon angles | in (CLASH 4, 6) |
| ch1.pentagon_q2 | prompt | 16 | T10.C4 (C15) | T10.C4, Tool 14 | Shapes with Straws, pentagon push | in (question mark put in, CLASH 32) |
| ch1.pentagon_q3 | prompt | 16 | T10.C4 (C15) | T10.C4, Tool 14 | Shapes with Straws, pentagon change | in (CLASH 4, 6) |
| ch1.circle_straws | exercise | 16 | T12.C2 Make a Circle (C16) | T12.C2, Tool 16 Make a Circle | Straws and a circle | in (activity, CLASH 16) |
| ch1.circle_straws_q1 | prompt | 16 | T12.C2 (C16) | T12.C2, Tool 16 | Straws and a circle, Q1 | in |
| ch1.circle_straws_q2 | prompt | 16 | T12.C2 (C16) | T12.C2, Tool 16 | Straws and a circle, Q2 | in |
| ch1.make_circle | exercise | 16 | T12.C2 (C16) | T12.C2, Tool 16 | Let Us Make | in (scale, no units, CLASH 16) |
| ch1.make_circle_q | prompt | 16 | T12.C2 (C16) | T12.C2, Tool 16 | Let Us Make, Q | in |
| ch1.centre_text | text | 16 | T12.C1 The Circle (C16) | none: teaching text (`ncert` of T12.C1) | | in (text) |
| ch1.amazing1 | exercise | 17 | T13.C2 Fold the Circle (C17) | T13.C2, Tool 17 Fold the Circle | Amazing Circles | in (activity, CLASH 16) |
| ch1.amazing_q1 | prompt | 17 | T13.C2 (C17) | T13.C2, Tool 17 | Amazing Circles, Q1 | in |
| ch1.amazing_t2 | text | 17 | T13.C1 Folding a Circle (C17) | none: teaching text (`ncert` of T13.C1) | | in (text) |
| ch1.amazing_t3 | talk | 17 | T13.C1 (C17) | none: teaching text (`ncert` of T13.C1) | | in (talk) |
| ch1.amazing_q4 | exercise | 17 | T13.C2 (C17) | T13.C2, Tool 17 | Amazing Circles, Q4 | in ("center" written "centre", CLASH 32) |
| ch1.amazing_t5 | talk | 17 | T13.C1 (C17) | none: teaching text (`ncert` of T13.C1) | | in (talk) |
| ch1.note_measure | text | 17 | T13.C1 (C17) | none: teaching text (`ncert` of T13.C1) | | in (text; teacher note, CLASH 13) |
| ch1.circ_do1 | exercise | 18 | T13.C2 Fold the Circle (C18) | T13.C2, Tool 17 | Let Us Do, folds | in (C18 on C17's tool, CLASH 4, 6) |
| ch1.compass | exercise | 18 | T13.C4 Find Radius and Diameter (C18) | T13.C4, Tool 18 Find Radius and Diameter | Let Us Do, compass | in (teacher sentence dropped, CLASH 13, 32; E15) |
| ch1.carpet | exercise | 18 | T13.C4 (C18) | T13.C4, Tool 18 | Let Us Do, carpet | in |
| ch1.note_compass | text | 18 | T13.C3 Wheels and Carpets (C18) | none: teaching text (`ncert` of T13.C3) | | in (text; teacher note, CLASH 13) |
| ch1.wheels_q0 | prompt | 19 | T13.C4 (C18) | T13.C4, Tool 18 | Wheels | in (CLASH 6) |
| ch1.wheels_q1 | prompt | 19 | T13.C4 (C18) | T13.C4, Tool 18 | Wheels, radius and diameter | in (CLASH 6; E16) |
| ch1.puzzle1 | exercise | 19 | T15.C2 Divide the Shapes (C19) | T15.C2, Tool 20 Divide the Shapes | Puzzling Shapes, Q1 | in (E17; one square and one rectangle, CLASH 31) |
| ch1.puzzle2 | exercise | 19 | T15.C2 (C19) | T15.C2, Tool 20 | Puzzling Shapes, Q2 | in |
| ch1.puzzle3 | exercise | 19 | T15.C2 (C19) | T15.C2, Tool 20 | Puzzling Shapes, Q3 | in |
| ch1.puzzle4 | exercise | 20 | T15.C2 (C19) | T15.C2, Tool 20 | Puzzling Shapes, Q4 | in (cuts not unique: Sample answer) |
| ch1.cards | exercise | 20 | T14.C2 Sides and Angles (C20) | T14.C2, Tool 19 Sides and Angles | Card Game | in (CLASH 6, 10; E18) |
| ch1.try1_text | text | 21 | T16.C1 Squiggly and Wiggly's Webs (C21) | none: teaching text (`ncert` of T16.C1) | | in (text) |
| ch1.try1a | prompt | 21 | T16.C2 Spider Web Puzzles (C21) | T16.C2, Tool 21 Spider Web Puzzles | Let Us Try, Q1 (triangles) | in (10) |
| ch1.try1b | exercise | 21 | T16.C2 (C21) | T16.C2, Tool 21 | Let Us Try, Q1 (Squiggly's path) | in (yes; a path through all 12 walls) |
| ch1.try1c | prompt | 21 | T16.C2 (C21) | T16.C2, Tool 21 | Let Us Try, Q1 (rectangles) | in (12) |
| ch1.try1d | exercise | 21 | T16.C2 (C21) | T16.C2, Tool 21 | Let Us Try, Q1 (Wiggly's path) | in (no, on the "every wall" reading, CLASH 33) |
| ch1.try2 | exercise | 21 | T17.C2 Matchstick Moves (C22) | T17.C2, Tool 22 Matchstick Moves | Let Us Try, Q2 | in (solved) |
| ch1.try3 | exercise | 22 | T17.C2 (C22) | T17.C2, Tool 22 | Let Us Try, Q3 | in (NO solution given, CLASH 18) |
| ch1.try4 | exercise | 22 | T17.C2 (C22) | T17.C2, Tool 22 | Let Us Try, Q4 | in (NO solution given, CLASH 18) |
| ch1.try5 | exercise | 22 | T6.C2 Solid Riddles (C23) | T6.C2, Tool 8 Solid Riddles | Model challenge | in (CLASH 4, 6; E21: part c not named) |
| ch1.try6 | exercise | 22 | T14.C2 Sides and Angles (C24) | T14.C2, Tool 19 | Let Us Try, Q6 | in (CLASH 4, 6) |
| ch1.try6_q | prompt | 22 | T14.C2 (C24) | T14.C2, Tool 19 | Let Us Try, Q6, sides and angles | in (CLASH 4, 6) |
| ch1.try7a | exercise | 23 | T14.C2 (C24) | T14.C2, Tool 19 | Let Us Try, Q7 | in (CLASH 4, 6) |
| ch1.try7b | exercise | 23 | T14.C2 (C24) | T14.C2, Tool 19 | Let Us Try, Q7 (more) | in (CLASH 4, 6) |
| ch1.try8 | exercise | 23 | T11.C2 Angles in Shapes (C24) | T11.C2, Tool 15 | Let Us Try, Q8 | in (CLASH 6; E23) |
| ch1.try8_q | prompt | 23 | T11.C2 (C24) | T11.C2, Tool 15 | Let Us Try, Q8, only right angles | in (CLASH 6; the red figure is a tilted rectangle, CLASH 31) |
| ch1.try9 | exercise | 23 | T11.C2 (C24) | T11.C2, Tool 15 | Let Us Try, Q9 | in (CLASH 6; E22: every shape that fits) |

## Per tool

| Tool | tool concept | book questions on the tool | count | against the cap of 6 |
|---|---|---|---|---|
| 1 Blocks for Buildings | T1.C2 (explore) | model1, model_q1, model_q2, model_q3, model_q4, model_q5 (plus 3 notice prompts of the plan, not book questions) | 6 | at the cap |
| image after Tool 1 (no tool) | T2.C1 (`items` of the image concept) | qutub_q1, qutub_q2, qutub_q3, bricks_q, project1, craft1 | 6 | not a tool; the gate allows it (CLASH 8) |
| 2 Prism or Pyramid | T2.C3 | prism_q1, prism_q2, prism_q3, pyr_q1, pyr_q2, pyr_q3 | 6 | at the cap (7 in the proposal) |
| 3 Faces, Corners and Edges | T3.C2 | craft3, fve, sort_faces, three_faces, sort_edges, cube_prism | 6 | at the cap (cube_prism from Tool 2, PROVISIONAL) |
| 4 Opposite Faces | T3.C4 | observe1, observe2, observe3 | 3 | ok |
| 5 Spot the Faces | T4.C2 | border1, border2, border3, border4, border5 | 5 | ok |
| 6 Sort the Solids | T4.C4 | sort1, sort2, sort3, sort3_q, sort4 | 5 | ok |
| 7 Build and Draw Cubes | T5.C2 | build1, towers, dotcubes | 3 | ok |
| 8 Solid Riddles | T6.C2 | solids_q1, try5 | 2 | ok |
| 9 Fold the Net | T7.C2 | craft2, solids_q3, solids_q4, solids_q5 | 4 | ok |
| 10 When Lines Meet | T8.C2 | house_ex, boat_q, angles_do1, angles_do2 | 4 | ok |
| 11 Right Angle Checker | T9.C2 | right_make, right_circle, right_objects, right_do1, straw_rect_angles | 5 | ok (straw_rect_angles from Tool 13, PROVISIONAL) |
| 12 Acute or Obtuse | T9.C4 | acute_obj, obtuse_obj, letters, ao_do1a, ao_do1b, ao_do2 | 6 | at the cap |
| 13 Push the Straw Shapes | T10.C2 | straw_tri_make, straw_tri_push, straw_tri_trace, straw_tri_angles, straw_rect_make, straw_rect_push | 6 | at the cap (7 in the proposal) |
| 14 Angles After the Push | T10.C4 | straw_rect_after, straw_square, pentagon_make, pentagon_q1, pentagon_q2, pentagon_q3 | 6 | at the cap (7 in the proposal) |
| 15 Angles in Shapes | T11.C2 | dotshapes, dotshapes_q, fourside_q, try8, try8_q, try9 | 6 | at the cap |
| 16 Make a Circle | T12.C2 | circle_straws, circle_straws_q1, circle_straws_q2, make_circle, make_circle_q | 5 | ok |
| 17 Fold the Circle | T13.C2 | amazing1, amazing_q1, amazing_q4, circ_do1 | 4 | ok |
| 18 Find Radius and Diameter | T13.C4 | compass, carpet, wheels_q0, wheels_q1 | 4 | ok |
| 19 Sides and Angles | T14.C2 | cards, try6, try6_q, try7a, try7b, straw_compare | 6 | at the cap (straw_compare from Tool 14, PROVISIONAL) |
| 20 Divide the Shapes | T15.C2 | puzzle1, puzzle2, puzzle3, puzzle4 | 4 | ok |
| 21 Spider Web Puzzles | T16.C2 | try1a, try1b, try1c, try1d | 4 | ok |
| 22 Matchstick Moves | T17.C2 | try2, try3, try4 | 3 | ok |

109 questions = 6 + 6 + 6 + 6 + 3 + 5 + 5 + 3 + 2 + 4 + 4 + 5 + 6 + 6 + 6 + 6 + 5 + 4 + 4 + 6 + 4 + 4 + 3. The hook (T1.C1), the
review (T18) and the concept videos hold no book question. Every one of the 22 tools carries at least one book question of the
concept it serves (no tool is empty).

## Stretches (a home that is a judgement call)

- Tool 1: the six questions of the opener on an exploration tool (CLASH 9); model_q3 is asked before any solid is named.
- Image T2.C1 (no tool): qutub_q1 to qutub_q3 and bricks_q (one picture, three subjects, CLASH 29), and the two offline tasks
  project1 and craft1 (CLASH 8). craft1 is a sphere craft on a bricks picture, the weakest fit; its nearest other home would be
  Tool 9 (CLASH 8 option c). The gate allows all six here: it bars book questions on an image concept only when a tool applies to it.
- Tool 3: cube_prism (PROVISIONAL, cap). Tool 11: straw_rect_angles (PROVISIONAL, cap). Tool 19: straw_compare (PROVISIONAL, cap).
- Tool 8: try5 moved up from page 22 (CLASH 6). Tool 9: craft2 moved from page 3 with the net text (CLASH 5, 10).
- Tool 14: the pentagon (analysis C15, CLASH 4, 19, 23). Tool 15: try8, try8_q, try9 moved up from page 23 (CLASH 6).
- Tool 17: circ_do1 (analysis C18, printed on the next page, CLASH 4, 6). Tool 18: wheels_q0 and wheels_q1 (page 19, CLASH 6).
- Tool 19: cards, try6, try6_q, try7a, try7b placed before the puzzles (CLASH 4, 6, 10).
- Tools 10, 11, 12: angles_do2, right_objects, acute_obj and obtuse_obj ask for classroom objects; they sit on the classroom picture
  of their tool (CLASH 16).

## Teaching text (not questions): 17 text + 5 talk = 22

Each is in `ncert` of the teaching concept that carries it, never on a hook, a review or a tool as a question: opening (T1.C1 hook);
model_talk (T1.C2); qutub_say, qutub_fact, bricks_text, note_boxes (T2.C1); prism_pyr_talk (T2.C2); note_venn (T4.C3); solids_q2
(T6.C1); net_text (T7.C1); angle_text, yoga_text (T8.C1); acute_text (T9.C3); note_rigid (T10.C1); note_square (T11.C1);
centre_text (T12.C1); amazing_t2, amazing_t3, amazing_t5, note_measure (T13.C1); note_compass (T13.C3); try1_text (T16.C1). The six
teacher notes (note_boxes, note_venn, note_rigid, note_square, note_measure, note_compass) stay as teaching text; no question,
step or answer gives a teacher a role (CLASH 13).

## Excluded (outside this chapter, or extra and advanced)

None. All 131 items in `content.NCERT_ITEMS` are printed in this chapter's 23 pages. Looked at and not added:
- the nets and the six 2D cards at the end of the book: supporting material of Craft 2 and the Card Game, not book items; the
  steps say they are on the screen (CLASH 10);
- the 3 notice prompts of Tool 1 (in `tools_1.py`): the plan's own, not book questions;
- the QR code on the opener, the "Do you know" figures and the pictures themselves: not questions;
- nothing from another chapter, the prelims or an "extra" section was added anywhere; no question was written for any tool.

## Answers (CLASH 11, 18, 31, 33)

The book prints no answers and no key is part of this chapter's files. Every answer begins exactly "From the picture" (counts,
positions, what a picture shows) or "Sample answer" (open tasks, geometry the book does not print); open tasks end "Your answer
may differ"; none reads as an official textbook answer. No answer gives a number or solution that could not be confirmed:
ch1.try3 and ch1.try4 give no solution, and the second tower of ch1.towers gets no number; each says how to find it. Checked again
on the page images by the question mapper: F+V−E = 2 for all five solids; the house has 7 and the boat 10 marked angles; the first
cube tower is 4 layers of 16, 9, 4 and 1 (30); the colour-cube opposites (red with purple, yellow with orange); 10 triangles and
12 rectangles in the webs, and a path through all 12 numbered walls of Squiggly's web; the right-angle counts 4, 0, 1, 0, 0, 4;
the shapes of Q9. Two readings of `analysis.md` were corrected (two squares among the hidden shapes: one square and one rectangle;
the red tilted figure of Q8: a rectangle). Printed-book errors and ambiguities that touch a question are in `content.SOLUTION_NOTES`
(25 entries); `content.ERRATA` stays empty because the book prints no false sum. The gate checked 44 sums on the screen, none false.

## Notes for the user: what needs a decision (new clashes)

- CLASH 30: the three provisional moves because of the cap of 6 (option b, cap 7, undoes them).
- CLASH 31: three figure readings differ from analysis.md and VISUAL_KEY (hidden shapes, the red tilted figure, the cheese pieces).
- CLASH 32: the words on screen of six questions differ from the print (compass and project1 teacher lines, en dash, a question mark,
  "center", "previous page"). The compass line follows CLASH 13 option (a) and needs the user's yes.
- CLASH 33: two questions with two readings (prism_q3 "such faces", Wiggly's walk "every wall").
- Lines "QUESTION MAPPER (step 5)" were appended to CLASH 3, 8, 9, 10, 11, 12, 13, 16 and 18.

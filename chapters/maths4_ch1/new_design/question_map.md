# Question map: Class 4, Chapter 1, "Shapes Around Us" (rebuild on the 9-lesson plan, amended 12 Nov 2026)

Step 5 (c34-question-mapper), 6 Nov 2026, AMENDED on 12 Nov 2026 for the content team's validator report (CLASH 54 to 59). Every book item of the chapter is tagged question -> concept -> tool. The homes are `FIO(...)` in `items` of the tool concept in `topics_1.py`; the 22 items that are not questions are `ncert=[...]` of the teaching concept that carries them. Clash numbers refer to `content.CLASHES` (59 clashes: 1 to 49 are earlier steps', 50 to 52 the mapper's of 6 Nov, 54 to 58 the user's answers of 12 Nov, 59 this amendment's; 1 to 53 and the old rows below use the OLD tool numbers only where the text says so: every `Tool n` in the table is the NEW number). Page = pdf page = printed page. Every video, image and tool is a placeholder. The book prints no answers: every answer on a tool begins "From the picture" or "Sample answer", and none is presented as an official answer.

## Result

131 book items = 109 questions (1 example, 59 exercises, 49 prompts) + 22 not questions (17 text, 5 talk). Each question has ONE home, on the tool concept (DOER) of the concept it practises; none is on a hook, a video or image concept, or the review. **Nothing is excluded**: every item is printed on the 23 pages of this chapter. Checked by program against the 6 Nov structure report: 131 ids, the same set, 109 questions homed, none missing, none twice; every FIO kind equals its `NCERT_ITEMS` kind; the 22 text and talk items are each in `ncert` of exactly one concept (the same concept as before, except note_venn, which follows its tool from T3.C4 to T3.C6 because the old Tool 3 is now Tool 5).

**Eleven questions moved on 12 Nov 2026**, each to the new tool whose activity it plainly is (CLASH 59; listed below with the reason). The lesson plan's 23 activities are now 23 tools (1 to 23), and Lesson 9's three tools (24 to 26) carry no book question: the user chose not to repeat book questions there (CLASH 58). Eight tools carry no book question (config `no_book_question_tools`: 3, 4, 17, 19, 23, 24, 25, 26). The cap of 13 holds on every tool.

| Tool | questions | kinds |
|---|---|---|
| Tool 1 Shape Detective | 11 | 3 exercise, 8 prompt |
| Tool 2 Guess the Shape | 9 | 8 exercise, 1 prompt |
| Tool 3 Match the 3D Shape | 0 | none |
| Tool 4 Build Your Own 3D Shape | 0 | none |
| Tool 5 Prisms and Pyramids | 12 | 4 exercise, 8 prompt |
| Tool 6 Nets of 3D Shapes | 1 | 1 exercise |
| Tool 7 Which Net Makes Which Shape | 2 | 2 exercise |
| Tool 8 Find the Wrong Net | 1 | 1 exercise |
| Tool 9 Faces Edges and Corners | 6 | 5 exercise, 1 prompt |
| Tool 10 Count and Win | 2 | 1 exercise, 1 prompt |
| Tool 11 Spin the Shape | 4 | 1 exercise, 3 prompt |
| Tool 12 Cube Towers and Drawings | 1 | 1 exercise |
| Tool 13 Look Carefully | 1 | 1 prompt |
| Tool 14 Copy the Cube Structure | 1 | 1 exercise |
| Tool 15 Angle Builder | 10 | 1 example, 6 exercise, 3 prompt |
| Tool 16 Angle Sorting | 10 | 6 exercise, 4 prompt |
| Tool 17 Beat the Clock | 0 | none |
| Tool 18 Circle Detective | 13 | 7 exercise, 6 prompt |
| Tool 19 Radius or Diameter | 0 | none |
| Tool 20 Build a Pentagon | 8 | 4 exercise, 4 prompt |
| Tool 21 Triangle vs Rectangle | 10 | 3 exercise, 7 prompt |
| Tool 22 Build a Strong Structure | 7 | 5 exercise, 2 prompt |
| Tool 23 True or False | 0 | none |
| Tool 24 Shape Identification Quiz | 0 | none |
| Tool 25 Digital Worksheet | 0 | none |
| Tool 26 Sample Online Assessment | 0 | none |
| **Total** | **109** | 1 example, 59 exercise, 49 prompt |

Tool 18 is AT the cap (13); Tool 5 is one under (12): nothing may be added to them. Tool 1 is the exploration tool and holds 11 questions (plus the tool's own 3 notice prompts, CLASH 25). The gate `flow_c34._check_questions` allows a book question on a tool concept (explore or tool), bars it on a hook, on a review and on a story or image concept that a tool applies to. The eight tools with no book question each carry ONE `notice` prompt, because the structure gate (media_content, "carries no tool_questions") refuses a tool with no question at all (CLASH 59); the brief writer may reword them.

The stage interactions of the plan (the three clues, Match, Label, Count the parts, Spin the shape, Strong or wobbly, Identify the Angle, the build stages) are NOT book questions: they are the tools' interaction, unscored, and the new tools 3, 4, 10, 11, 13, 14, 17, 19, 23 carry them (SPLIT NOTES, `media_decisions.md` section 10). They are not in this map and not in the cap.

## The moves of 12 Nov 2026 (CLASH 59; the user's yes is needed for each)

| id | from | to | why |
|---|---|---|---|
| ch1.solids_q3 | Tool 6 Nets of 3D Shapes | Tool 7 Which Net Makes Which Shape | "Match the following nets to the appropriate solids": a net matched to its solid |
| ch1.solids_q5 | Tool 6 | Tool 7 | Nitesh's pieces (1 pentagon and 5 triangles): which solid has them in its net, the same action (net to solid) |
| ch1.solids_q4 | Tool 6 | Tool 8 Find the Wrong Net | "Which of these nets can be folded": two nets fold and two do not, so it is finding the net that will not fold |
| ch1.craft3 | Tool 9 Faces Edges and Corners | Tool 10 Count and Win | counting F, V and E of five solids and filling the table: counting faces, edges and corners |
| ch1.fve | Tool 9 | Tool 10 | F+V−E is worked on the table of craft3, so it goes with it |
| ch1.observe1 | Tool 9 | Tool 11 Spin the Shape | the face opposite another face on a die |
| ch1.observe2 | Tool 9 | Tool 11 | the faces that touch a face, and the one that does not |
| ch1.observe3 | Tool 9 | Tool 11 | three views of one cube: opposite colours |
| ch1.border5 | Tool 9 | Tool 11 | "circle the shapes that have the same opposite faces": opposite faces |
| ch1.towers | Tool 12 Cube Towers and Drawings | Tool 13 Look Carefully | count the cubes of two towers, hidden ones too |
| ch1.dotcubes | Tool 12 | Tool 14 Copy the Cube Structure | complete the cubes on triangular dot paper: copying a cube structure on dot paper |

Considered and NOT moved: ch1.circ_do1 (the diameter is double the radius, by folding the paper) stays on Tool 18, because Tool 18's purpose names that fold and the book prints no radius or diameter number for Tool 19; ch1.solids_q1 (descriptions by counts, name the shape) stays on Tool 9, because on Tool 3 it would use face, edge and corner counts before they are taught, and on Tool 10 it reads the counts the other way round; ch1.build1 stays on Tool 12; the yes or no push questions stay on Tool 21. Tool 9 keeps the sorts (sort_faces, three_faces, sort_edges, sort2), solids_q1 and try5: counting and naming work its narrowed purpose does not mention (CLASH 59, option b would move them to Tool 10).

## The map

Columns: id | kind | page | concept (plan key, name, analysis code and name) | tool (approved number and name, NEW numbering) | label shown to the child (the book's own, never a page) | status. "in" = homed once; the bracket names the stretch (the item is on a tool whose lead concept is not its own analysis concept) and the clashes it touches. Statuses written on 6 Nov have their tool numbers changed to the new ones; the moves of 12 Nov say so.

| id | kind | page | concept | tool | label | in / excluded (why) |
|---|---|---|---|---|---|---|
| opening | text | 1 | T1.C1 Diksha's Trip to Delhi (analysis C1 Shapes in buildings) | none: teaching text, `ncert` of T1.C1 |  | in (text: the hook video's situation) |
| ch1.model1 | exercise | 1 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Opening, Task | in (opening task; blocks on screen (CLASH 36)) |
| ch1.model_q1 | prompt | 1 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Opening, Q1 | in |
| ch1.model_q2 | prompt | 1 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Opening, Q2 | in |
| ch1.model_q3 | prompt | 1 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Opening, Q3 | in |
| ch1.model_q4 | prompt | 1 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Opening, Q4 | in (needs the child's own model (CLASH 25)) |
| ch1.model_q5 | prompt | 1 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Opening, Q5 | in (needs the child's own model (CLASH 25)) |
| ch1.model_talk | talk | 1 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | none: teaching text, `ncert` of T1.C2 |  | in (talk: discussion prompt for the child, in the tool's feedback) |
| ch1.project1 | exercise | 2 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Project Work | in (offline project; teacher line dropped (CLASH 36, 50)) |
| ch1.qutub_say | text | 2 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | none: teaching text, `ncert` of T1.C2 |  | in (text: the boy's speech, a line of the tool) |
| ch1.qutub_q1 | prompt | 2 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Qutub Minar, Q1 | in (look-and-think (CLASH 25)) |
| ch1.qutub_q2 | prompt | 2 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Qutub Minar, Q2 | in (look-and-think; no block fits the tapering tower (CLASH 25, 32)) |
| ch1.qutub_q3 | prompt | 2 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | Tool 1 Shape Detective | Qutub Minar, Q3 | in (look-and-think (CLASH 25)) |
| ch1.qutub_fact | text | 2 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | none: teaching text, `ncert` of T1.C2 |  | in (text: the book's own fact, a line of the tool) |
| ch1.bricks_text | text | 2 | T2.C2 Guess the Shape (analysis C1 Shapes in buildings) | none: teaching text, `ncert` of T2.C2 |  | in (text: fact) |
| ch1.bricks_q | prompt | 2 | T2.C2 Guess the Shape (analysis C1 Shapes in buildings) | Tool 2 Guess the Shape | Bricks | in (C1 on Tool 2 (CLASH 21)) |
| ch1.note_boxes | text | 2 | T1.C2 Shape Detective (analysis C1 Shapes in buildings) | none: teaching text, `ncert` of T1.C2 |  | in (text: Note for Teachers: coverage id only, no task for a teacher (CLASH 30)) |
| ch1.craft1 | exercise | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Craft, Q1 | in (curved solid on a prism tool; paper strips on screen (CLASH 15, 36)) |
| ch1.net_text | text | 3 | T4.C1 What Is a Net? (analysis C2 Prisms, pyramids and nets) | none: teaching text, `ncert` of T4.C1 |  | in (text: the idea of the net video) |
| ch1.craft2 | exercise | 3 | T4.C2 Nets of 3D Shapes (analysis C2 Prisms, pyramids and nets) | Tool 6 Nets of 3D Shapes | Craft, Q2 | in (C2 net half on Tool 6, nets on the end pages (CLASH 35; E24)) |
| ch1.prism_q1 | prompt | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Prisms, Q1 | in |
| ch1.prism_q2 | prompt | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Prisms, Q2 | in |
| ch1.prism_q3 | prompt | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Prisms, Q3 | in |
| ch1.pyr_q1 | prompt | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Pyramids, Q1 | in |
| ch1.pyr_q2 | prompt | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Pyramids, Q2 | in |
| ch1.pyr_q3 | prompt | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Pyramids, Q3 | in |
| ch1.cube_prism | prompt | 3 | T3.C6 Prisms and Pyramids (analysis C2 Prisms, pyramids and nets) | Tool 5 Prisms and Pyramids | Prisms and Pyramids, cube | in (answered as a square prism (CLASH 47)) |
| ch1.prism_pyr_talk | talk | 3 | T3.C3 Prism or Pyramid? (analysis C2 Prisms, pyramids and nets) | none: teaching text, `ncert` of T3.C3 |  | in (talk: the book's talk prompt, carried by the comparison image) |
| ch1.craft3 | exercise | 4 | T5.C3 Count and Win (analysis C3 Faces, corners, edges) | Tool 10 Count and Win | Craft, Q3 | in (moved from Tool 9 to Tool 10: count F, V and E and fill the table; CLASH 59) |
| ch1.fve | prompt | 4 | T5.C3 Count and Win (analysis C3 Faces, corners, edges) | Tool 10 Count and Win | Craft, F+V−E | in (moved from Tool 9 to Tool 10: worked on the table of craft3; F+V−E, wording (CLASH 50, 59)) |
| ch1.sort_faces | exercise | 4 | T5.C2 Faces Edges and Corners (analysis C3 Faces, corners, edges) | Tool 9 Faces Edges and Corners | Sorting by flat faces | in (C3 stage (E3, CLASH 52)) |
| ch1.three_faces | prompt | 4 | T5.C2 Faces Edges and Corners (analysis C3 Faces, corners, edges) | Tool 9 Faces Edges and Corners | Sorting by flat faces, 3 faces | in (C3 stage (E2)) |
| ch1.sort_edges | exercise | 4 | T5.C2 Faces Edges and Corners (analysis C3 Faces, corners, edges) | Tool 9 Faces Edges and Corners | Sorting by straight edges | in (C3 stage (E3, CLASH 52)) |
| ch1.observe1 | prompt | 5 | T5.C4 Spin the Shape (analysis C4 Opposite and adjacent faces) | Tool 11 Spin the Shape | Let Us Observe, Q1 | in (moved from Tool 9 to Tool 11: opposite faces of a die; C4 stage (E6); CLASH 59) |
| ch1.observe2 | prompt | 5 | T5.C4 Spin the Shape (analysis C4 Opposite and adjacent faces) | Tool 11 Spin the Shape | Let Us Observe, Q2 | in (moved from Tool 9 to Tool 11: faces that touch; C4 stage; CLASH 59) |
| ch1.observe3 | prompt | 5 | T5.C4 Spin the Shape (analysis C4 Opposite and adjacent faces) | Tool 11 Spin the Shape | Let Us Observe, Q3 | in (moved from Tool 9 to Tool 11: opposite colours of a cube; C4 stage; CLASH 59) |
| ch1.border1 | exercise | 5 | T2.C2 Guess the Shape (analysis C5 Sorting solids by parts) | Tool 2 Guess the Shape | Border, Q1 | in (C5 on Tool 2 (CLASH 21, 51; E7)) |
| ch1.border2 | exercise | 5 | T2.C2 Guess the Shape (analysis C5 Sorting solids by parts) | Tool 2 Guess the Shape | Border, Q2 | in (C5 on Tool 2 (E7)) |
| ch1.border3 | exercise | 5 | T2.C2 Guess the Shape (analysis C5 Sorting solids by parts) | Tool 2 Guess the Shape | Border, Q3 | in (C5 on Tool 2 (E7)) |
| ch1.border4 | exercise | 5 | T2.C2 Guess the Shape (analysis C5 Sorting solids by parts) | Tool 2 Guess the Shape | Border, Q4 | in (C5 on Tool 2 (E7)) |
| ch1.border5 | exercise | 5 | T5.C4 Spin the Shape (analysis C5 Sorting solids by parts) | Tool 11 Spin the Shape | Border, Q5 | in (moved from Tool 9 to Tool 11: opposite faces; C5 on Tool 11 (E7, CLASH 51, 59)) |
| ch1.sort1 | exercise | 6 | T3.C6 Prisms and Pyramids (analysis C5 Sorting solids by parts) | Tool 5 Prisms and Pyramids | Sorting 3D Shapes, (1) | in (C5 on Tool 5; curved solids (CLASH 15, 52; E3)) |
| ch1.sort2 | exercise | 6 | T5.C2 Faces Edges and Corners (analysis C5 Sorting solids by parts) | Tool 9 Faces Edges and Corners | Sorting 3D Shapes, (2) | in (C5 on Tool 9 (CLASH 52)) |
| ch1.sort3 | exercise | 6 | T3.C6 Prisms and Pyramids (analysis C5 Sorting solids by parts) | Tool 5 Prisms and Pyramids | Sorting 3D Shapes, (3) | in (C5 on Tool 5 (CLASH 51, 52; E3)) |
| ch1.sort3_q | prompt | 7 | T3.C6 Prisms and Pyramids (analysis C5 Sorting solids by parts) | Tool 5 Prisms and Pyramids | Sorting 3D Shapes, circles | in (C5 on Tool 5 (CLASH 51; E4)) |
| ch1.sort4 | exercise | 7 | T3.C6 Prisms and Pyramids (analysis C5 Sorting solids by parts) | Tool 5 Prisms and Pyramids | Sorting 3D Shapes, curved and flat | in (C5 on Tool 5; wording (CLASH 15, 50)) |
| ch1.note_venn | text | 7 | T3.C6 Prisms and Pyramids (analysis C5 Sorting solids by parts) | none: teaching text, `ncert` of T3.C6 |  | in (text: Note for Teachers: coverage id only (CLASH 30)) |
| ch1.build1 | exercise | 7 | T6.C2 Cube Towers and Drawings (analysis C6 Building and counting cubes) | Tool 12 Cube Towers and Drawings | Build with Cubes | in |
| ch1.towers | prompt | 7 | T6.C3 Look Carefully (analysis C6 Building and counting cubes) | Tool 13 Look Carefully | Cube Towers | in (moved from Tool 12 to Tool 13: count every cube, hidden ones too; CLASH 59) |
| ch1.dotcubes | exercise | 8 | T6.C4 Copy the Cube Structure (analysis C7 Cube on dot paper) | Tool 14 Copy the Cube Structure | Drawing Cubes on a Triangular Dot Paper | in (moved from Tool 12 to Tool 14: cubes on dot paper; C7 (CLASH 20, 59)) |
| ch1.solids_q1 | exercise | 8 | T5.C2 Faces Edges and Corners (analysis C8 Naming a solid) | Tool 9 Faces Edges and Corners | Solids, Q1 | in (C8 on Tool 9 (E5)) |
| ch1.solids_q2 | talk | 8 | T5.C2 Faces Edges and Corners (analysis C8 Naming a solid) | none: teaching text, `ncert` of T5.C2 |  | in (talk: discussion prompt, in the tool's feedback) |
| ch1.solids_q3 | exercise | 9 | T4.C3 Which Net Makes Which Shape (analysis C9 Nets of solids) | Tool 7 Which Net Makes Which Shape | Solids and nets, Q3 | in (moved from Tool 6 to Tool 7 on 12 Nov 2026: a net matched to its solid; CLASH 59) |
| ch1.solids_q4 | exercise | 9 | T4.C4 Find the Wrong Net (analysis C9 Nets of solids) | Tool 8 Find the Wrong Net | Solids and nets, Q4 | in (moved from Tool 6 to Tool 8: which nets fold and which do not; E1: A and C do not fold; CLASH 59) |
| ch1.solids_q5 | exercise | 9 | T4.C3 Which Net Makes Which Shape (analysis C9 Nets of solids) | Tool 7 Which Net Makes Which Shape | Solids and nets, Q5 | in (moved from Tool 6 to Tool 7: a net's pieces matched to a solid; CLASH 59) |
| ch1.angle_text | text | 10 | T7.C1 Angles and the Right Angle (analysis C10 Angles) | none: teaching text, `ncert` of T7.C1 |  | in (text: the idea of the angle video) |
| ch1.yoga_text | text | 10 | T7.C1 Angles and the Right Angle (analysis C10 Angles) | none: teaching text, `ncert` of T7.C1 |  | in (text: the angle video's fact) |
| ch1.house_ex | example | 10 | T7.C2 Angle Builder (analysis C10 Angles) | Tool 15 Angle Builder | Example | in (the only example (CLASH 38; E8)) |
| ch1.boat_q | prompt | 10 | T7.C2 Angle Builder (analysis C10 Angles) | Tool 15 Angle Builder | When Lines Meet | in (E8) |
| ch1.angles_do1 | exercise | 10 | T7.C2 Angle Builder (analysis C10 Angles) | Tool 15 Angle Builder | Let Us Do (angles), Q1 | in |
| ch1.angles_do2 | prompt | 11 | T7.C2 Angle Builder (analysis C10 Angles) | Tool 15 Angle Builder | Let Us Do (angles), Q2 | in |
| ch1.right_make | exercise | 11 | T7.C2 Angle Builder (analysis C11 Right angles) | Tool 15 Angle Builder | Right Angles, make | in (paper fold on screen (CLASH 36)) |
| ch1.right_circle | exercise | 11 | T7.C2 Angle Builder (analysis C11 Right angles) | Tool 15 Angle Builder | Right Angles, dot grid | in (E9) |
| ch1.right_objects | exercise | 11 | T7.C2 Angle Builder (analysis C11 Right angles) | Tool 15 Angle Builder | Right Angles, objects | in |
| ch1.right_do1 | exercise | 12 | T7.C2 Angle Builder (analysis C11 Right angles) | Tool 15 Angle Builder | Let Us Do (right angles), Q1 | in |
| ch1.acute_text | text | 12 | T7.C3 Acute and Obtuse Angles (analysis C12 Acute and obtuse) | none: teaching text, `ncert` of T7.C3 |  | in (text: the rule of the acute and obtuse video) |
| ch1.acute_obj | prompt | 12 | T7.C4 Angle Sorting (analysis C12 Acute and obtuse) | Tool 16 Angle Sorting | Acute and Obtuse Angles, objects (acute) | in |
| ch1.obtuse_obj | prompt | 12 | T7.C4 Angle Sorting (analysis C12 Acute and obtuse) | Tool 16 Angle Sorting | Acute and Obtuse Angles, objects (obtuse) | in |
| ch1.letters | exercise | 12 | T7.C4 Angle Sorting (analysis C12 Acute and obtuse) | Tool 16 Angle Sorting | Acute and Obtuse Angles, letters | in (E10) |
| ch1.ao_do1a | exercise | 13 | T7.C4 Angle Sorting (analysis C12 Acute and obtuse) | Tool 16 Angle Sorting | Let Us Do (acute and obtuse), Q1 (acute) | in |
| ch1.ao_do1b | exercise | 13 | T7.C4 Angle Sorting (analysis C12 Acute and obtuse) | Tool 16 Angle Sorting | Let Us Do (acute and obtuse), Q1 (obtuse) | in (E28) |
| ch1.ao_do2 | exercise | 13 | T7.C4 Angle Sorting (analysis C12 Acute and obtuse) | Tool 16 Angle Sorting | Let Us Do (acute and obtuse), Q2 | in (E10) |
| ch1.straw_tri_make | exercise | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, triangle | in |
| ch1.straw_tri_push | prompt | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, push the triangle | in |
| ch1.straw_tri_trace | exercise | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, trace | in (notebook tracing on screen (CLASH 36, 50)) |
| ch1.straw_tri_angles | prompt | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, angles of a triangle | in (reads the tool's triangle (CLASH 28; E11)) |
| ch1.straw_rect_make | exercise | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, rectangle | in |
| ch1.straw_rect_angles | prompt | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, angles of a rectangle | in |
| ch1.straw_rect_push | prompt | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, push the rectangle | in |
| ch1.straw_rect_after | prompt | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, the new shape | in |
| ch1.straw_square | prompt | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, square | in |
| ch1.straw_compare | prompt | 14 | T9.C2 Triangle vs Rectangle (analysis C13 Rigid shapes) | Tool 21 Triangle vs Rectangle | Shapes with Straws, compare | in |
| ch1.note_rigid | text | 14 | T9.C1 A Rigid Shape (analysis C13 Rigid shapes) | none: teaching text, `ncert` of T9.C1 |  | in (text: Note for Teachers: coverage id only; its fact is a line of Tool 21's feedback after the push (CLASH 30, 46)) |
| ch1.dotshapes | exercise | 15 | T7.C4 Angle Sorting (analysis C14 Dot-grid shapes) | Tool 16 Angle Sorting | Shapes on a dot grid | in (C14 stage on Tool 16) |
| ch1.dotshapes_q | prompt | 15 | T7.C4 Angle Sorting (analysis C14 Dot-grid shapes) | Tool 16 Angle Sorting | Shapes on a dot grid, Discuss | in (C14 stage, a prompt (CLASH 38)) |
| ch1.fourside_q | prompt | 15 | T7.C4 Angle Sorting (analysis C14 Dot-grid shapes) | Tool 16 Angle Sorting | Four-sided shapes | in (C14 stage (E12, CLASH 51)) |
| ch1.note_square | text | 15 | T7.C4 Angle Sorting (analysis C14 Dot-grid shapes) | none: teaching text, `ncert` of T7.C4 |  | in (text: Note for Teachers: coverage id only; its fact is for the tool's feedback (CLASH 30, 51)) |
| ch1.pentagon_make | exercise | 16 | T8.C4 Build a Pentagon (analysis C15 The pentagon) | Tool 20 Build a Pentagon | Pentagon, make | in |
| ch1.pentagon_q1 | prompt | 16 | T8.C4 Build a Pentagon (analysis C15 The pentagon) | Tool 20 Build a Pentagon | Pentagon, Q1 | in |
| ch1.pentagon_q2 | prompt | 16 | T8.C4 Build a Pentagon (analysis C15 The pentagon) | Tool 20 Build a Pentagon | Pentagon, Q2 | in (wording (CLASH 50; E13)) |
| ch1.pentagon_q3 | prompt | 16 | T8.C4 Build a Pentagon (analysis C15 The pentagon) | Tool 20 Build a Pentagon | Pentagon, Q3 | in |
| ch1.circle_straws | exercise | 16 | T8.C2 Circle Detective (analysis C16 Making a circle) | Tool 18 Circle Detective | Circle with straws | in (C16 leads Tool 18 (CLASH 20)) |
| ch1.circle_straws_q1 | prompt | 16 | T8.C2 Circle Detective (analysis C16 Making a circle) | Tool 18 Circle Detective | Circle with straws, Q1 | in |
| ch1.circle_straws_q2 | prompt | 16 | T8.C2 Circle Detective (analysis C16 Making a circle) | Tool 18 Circle Detective | Circle with straws, Q2 | in |
| ch1.make_circle | exercise | 16 | T8.C2 Circle Detective (analysis C16 Making a circle) | Tool 18 Circle Detective | Let Us Make | in |
| ch1.make_circle_q | prompt | 16 | T8.C2 Circle Detective (analysis C16 Making a circle) | Tool 18 Circle Detective | Let Us Make, What do you get? | in |
| ch1.centre_text | text | 16 | T8.C1 Parts of a Circle (analysis C16 Making a circle) | none: teaching text, `ncert` of T8.C1 |  | in (text: the circle video's words) |
| ch1.amazing1 | exercise | 17 | T8.C2 Circle Detective (analysis C17 Diameter by folding) | Tool 18 Circle Detective | Amazing Circles | in (C17 stage; fold and thread on screen (CLASH 20, 36)) |
| ch1.amazing_q1 | prompt | 17 | T8.C2 Circle Detective (analysis C17 Diameter by folding) | Tool 18 Circle Detective | Amazing Circles, Q1 | in |
| ch1.amazing_t2 | text | 17 | T8.C1 Parts of a Circle (analysis C17 Diameter by folding) | none: teaching text, `ncert` of T8.C1 |  | in (text: the circle video's words) |
| ch1.amazing_t3 | talk | 17 | T8.C2 Circle Detective (analysis C17 Diameter by folding) | none: teaching text, `ncert` of T8.C2 |  | in (talk: discussion prompt, in the tool's feedback) |
| ch1.amazing_q4 | exercise | 17 | T8.C2 Circle Detective (analysis C17 Diameter by folding) | Tool 18 Circle Detective | Amazing Circles, Q4 | in (C17 stage; wording (CLASH 50; E14)) |
| ch1.amazing_t5 | talk | 17 | T8.C2 Circle Detective (analysis C17 Diameter by folding) | none: teaching text, `ncert` of T8.C2 |  | in (talk: discussion prompt; answered by circ_do1) |
| ch1.note_measure | text | 17 | T8.C2 Circle Detective (analysis C17 Diameter by folding) | none: teaching text, `ncert` of T8.C2 |  | in (text: Note for Teachers: coverage id only (CLASH 30)) |
| ch1.circ_do1 | exercise | 18 | T8.C2 Circle Detective (analysis C18 Radius and diameter) | Tool 18 Circle Detective | Let Us Do (circles) | in (C18 stage (CLASH 2: half or double, no cm)) |
| ch1.compass | exercise | 18 | T8.C2 Circle Detective (analysis C18 Radius and diameter) | Tool 18 Circle Detective | Compass design | in (C18 stage; teacher sentence dropped (CLASH 30, 50; E15)) |
| ch1.carpet | exercise | 18 | T8.C2 Circle Detective (analysis C18 Radius and diameter) | Tool 18 Circle Detective | Carpet design | in (C18 stage) |
| ch1.note_compass | text | 18 | T8.C2 Circle Detective (analysis C18 Radius and diameter) | none: teaching text, `ncert` of T8.C2 |  | in (text: Note for Teachers: coverage id only (CLASH 30)) |
| ch1.wheels_q0 | prompt | 19 | T8.C2 Circle Detective (analysis C18 Radius and diameter) | Tool 18 Circle Detective | Wheels, Q1 | in (C18 stage) |
| ch1.wheels_q1 | prompt | 19 | T8.C2 Circle Detective (analysis C18 Radius and diameter) | Tool 18 Circle Detective | Wheels, Q2 | in (C18 stage (E16)) |
| ch1.puzzle1 | exercise | 19 | T1.C2 Shape Detective (analysis C19 Puzzling shapes) | Tool 1 Shape Detective | Puzzling Shapes, Q1 | in (stage 2 Hidden shapes, C19 on the exploration tool (CLASH 20, 25; E31)) |
| ch1.puzzle2 | exercise | 19 | T2.C2 Guess the Shape (analysis C19 Puzzling shapes) | Tool 2 Guess the Shape | Puzzling Shapes, Q2 | in (cuts, a misfit (CLASH 16)) |
| ch1.puzzle3 | exercise | 19 | T2.C2 Guess the Shape (analysis C19 Puzzling shapes) | Tool 2 Guess the Shape | Puzzling Shapes, Q3 | in (cuts, a misfit (CLASH 16)) |
| ch1.puzzle4 | exercise | 20 | T2.C2 Guess the Shape (analysis C19 Puzzling shapes) | Tool 2 Guess the Shape | Puzzling Shapes, Q4 | in (cuts, a misfit (CLASH 16; E17)) |
| ch1.cards | exercise | 20 | T2.C2 Guess the Shape (analysis C20 Card game) | Tool 2 Guess the Shape | Card Game | in (C20 leads Tool 2; cards on the end pages (CLASH 21, 35; E18)) |
| ch1.try1_text | text | 21 | T9.C3 A Stick Across a Frame (analysis C21 Spider webs) | none: teaching text, `ncert` of T9.C3 |  | in (text: the strong-frames story) |
| ch1.try1a | prompt | 21 | T9.C4 Build a Strong Structure (analysis C21 Spider webs) | Tool 22 Build a Strong Structure | Let Us Try, Q1, triangles | in (C21 on Tool 22 (CLASH 22)) |
| ch1.try1b | exercise | 21 | T9.C4 Build a Strong Structure (analysis C21 Spider webs) | Tool 22 Build a Strong Structure | Let Us Try, Q1, Squiggly's walk | in (walk, a misfit (CLASH 12, 17; E19)) |
| ch1.try1c | prompt | 21 | T9.C4 Build a Strong Structure (analysis C21 Spider webs) | Tool 22 Build a Strong Structure | Let Us Try, Q1, rectangles | in (C21 on Tool 22 (CLASH 22)) |
| ch1.try1d | exercise | 21 | T9.C4 Build a Strong Structure (analysis C21 Spider webs) | Tool 22 Build a Strong Structure | Let Us Try, Q1, Wiggly's walk | in (walk, a misfit; two readings (CLASH 12, 17; E19)) |
| ch1.try2 | exercise | 21 | T9.C4 Build a Strong Structure (analysis C22 Matchstick puzzles) | Tool 22 Build a Strong Structure | Let Us Try, Q2 | in (C22 on Tool 22 (CLASH 22)) |
| ch1.try3 | exercise | 22 | T9.C4 Build a Strong Structure (analysis C22 Matchstick puzzles) | Tool 22 Build a Strong Structure | Let Us Try, Q3 | in (C22; the triangles touch at their base corners (CLASH 12; E20)) |
| ch1.try4 | exercise | 22 | T9.C4 Build a Strong Structure (analysis C22 Matchstick puzzles) | Tool 22 Build a Strong Structure | Let Us Try, Q4 | in (C22 (CLASH 12; E20)) |
| ch1.try5 | exercise | 22 | T5.C2 Faces Edges and Corners (analysis C23 Model challenge) | Tool 9 Faces Edges and Corners | Model challenge | in (C23 on Tool 9; (c) a prism the chapter never shows (CLASH 19; E21)) |
| ch1.try6 | exercise | 22 | T8.C4 Build a Pentagon (analysis C24 Classifying by angles) | Tool 20 Build a Pentagon | Let Us Try, Q6 | in (C24 on Tool 20 (CLASH 18)) |
| ch1.try6_q | prompt | 22 | T8.C4 Build a Pentagon (analysis C24 Classifying by angles) | Tool 20 Build a Pentagon | Let Us Try, Q6, sides and angles | in (C24 on Tool 20 (CLASH 18; E25)) |
| ch1.try7a | exercise | 23 | T8.C4 Build a Pentagon (analysis C24 Classifying by angles) | Tool 20 Build a Pentagon | Let Us Try, Q7 (fewer angles) | in (C24 on Tool 20 (CLASH 18)) |
| ch1.try7b | exercise | 23 | T8.C4 Build a Pentagon (analysis C24 Classifying by angles) | Tool 20 Build a Pentagon | Let Us Try, Q7 (more angles) | in (C24 on Tool 20 (CLASH 18)) |
| ch1.try8 | exercise | 23 | T7.C2 Angle Builder (analysis C24 Classifying by angles) | Tool 15 Angle Builder | Let Us Try, Q8 | in (C24 closes Tool 15 (E23)) |
| ch1.try8_q | prompt | 23 | T7.C2 Angle Builder (analysis C24 Classifying by angles) | Tool 15 Angle Builder | Let Us Try, Q8, only right angles | in (C24 closes Tool 15 (E23)) |
| ch1.try9 | exercise | 23 | T7.C4 Angle Sorting (analysis C24 Classifying by angles) | Tool 16 Angle Sorting | Let Us Try, Q9 | in (C24 stage (E22)) |

## Excluded

None. No item is from another chapter, the prelims, or extra or advanced material. The two pieces at the end of the book (the nets of Craft 2 and
the six 2D cards of the Card Game) are supporting material of ch1.craft2 and ch1.cards, not items of their own (CLASH 35). The plan's 8
assessment questions, the true or false statements, the three-clue guess and every other plan-made stage are not book items and are on no tool.

## Where the printed wording is edited (CLASH 50; the user's yes is needed)

ch1.compass drops "Ask your teacher to help you use a compass." (CLASH 30 option a, as recommended). ch1.project1 reads "Observe a street ..." (the printed
"Encourage learners to" is a teacher line). ch1.fve writes F+V−E with the minus sign (the book has an en dash). ch1.pentagon_q2 gets its question
mark. ch1.amazing_q4 reads "centre". ch1.sort4 reads "circles like the ones you just used". Everything else is copied; dotted blanks are drawn as short lines.

## Answers: how they are labelled and checked

Every answer begins exactly "From the picture" (counts, positions, what a picture or the screen shows) or "Sample answer" (open tasks and geometry the
book does not print); open tasks end "Your answer may differ". No answer uses degrees, cm, "vertex", "diagonal", "regular", "polygon" or "NCERT".
Sums are checked by the gate (52 equations, none false). The results of `analysis.md` Appendix A were re-checked: both cube towers (30 and 66, solid
layers and no gap assumed, E27), nets A to D (B and D fold, A and C do not, E1), the matchstick solutions (by program on the triangular grid: Q3
4 triangles after moving 2 sticks if the three triangles touch at their base corners; Q4 128 of the 715 ways to remove 4 sticks leave exactly 3
triangles), the boat (10 marked angles, E8), the coloured cube (red opposite purple, yellow opposite orange), the dot-grid right angles (E9), the
p23 shapes (E22, E23, measured), the wheels (B, C, A, D by measure), the webs (10 triangles, 12 rectangles; Squiggly's numbers 1 to 12 trace one
closed walk). How each was checked is in `content.SOLUTION_NOTES` (31 entries; `content.ERRATA` stays empty: the book prints no false sum).
Answers with NO total on purpose: letters (the angles of A), ao_do2 (the stick figures), border1 to border5, cards, puzzle4, try9 (several shapes fit,
shape 1 fits none), straw_tri_angles (reads the tool's triangle).

## Decisions this step leaves to the user (clashes 50 to 52, 59, and two answers)

1. CLASH 50: the six edits of printed question wording (above). Recommended: yes.
2. CLASH 51: a square face counts as a rectangular face in Tools 2, 5 and 11 (the old Tools 2, 3 and 5), before Tool 16 carries the note "a square is a special rectangle". Recommended: keep, say it once.
3. CLASH 52: one set of ten solids for every sorting stage (E3). Recommended: yes.
4. CLASH 12 (existing): the walk answer of ch1.try1d is written on the "every wall" reading (no), with the other reading in one line; the user's choice changes only that answer.
5. CLASH 12 and 28 (existing): sign-off of Appendix A and of the answers with no total.
6. CLASH 59: the eleven moves above, the questions kept where they were, and the one `notice` prompt on each tool without a book question. Recommended: yes.

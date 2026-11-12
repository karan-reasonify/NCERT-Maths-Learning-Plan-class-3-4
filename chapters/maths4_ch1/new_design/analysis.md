# Analysis: Class 4, Chapter 1, "Shapes Around Us" (rebuild on the 9-lesson plan; working file, step 1)

Written by the chapter analyst. Nothing is designed here: no flow, no media, no tools. This re-verifies and reuses the analysis of the previous build (`chapters/maths4_ch1_prev_v4/new_design/analysis.md`); item ids are kept so the two can be compared. All 23 `book/page_NNN.png` were opened; hard figures (both cube towers, the matchstick figures, the nets, hidden shapes, dot grids, webs, shapes of p22 and p23) were re-rendered from `book/chapter.pdf` at 300 to 600 dpi, measured in pixels and checked. The text layer was used only as a typing aid. Rows or sentences marked "(mine)" are my reading or check of a printed figure: **the book prints no answers**, so they need the content team's or the user's sign-off before any plan uses them.

**What changed against the previous analysis** (details in section 6 and Appendix A): E17 corrected (hidden shapes are ONE square and ONE tilted rectangle, not two squares); E23 corrected (the last figure of p23 Q8 is a tilted rectangle, not a square); tower 2 on p7 is now counted (66) and tower 1 re-confirmed (30); the matchstick figures are counted and solved (Q3: 9 sticks, Q4: 13 sticks); E19 widened (two readings of the walk questions; Squiggly's numbers already trace a walk); new E26 to E31.

## 1. Chapter facts

| | |
|---|---|
| Book | NCERT "Maths Mela", Textbook of Mathematics for Grade 4, First Edition March 2025, "Reprint 2026-27" (printed at the foot of every page). |
| Chapter | 1, "Shapes Around Us" (read from `page_001.png`). Chapter = printed pages 1 to 23; the contents list puts Chapter 2 at page 24. |
| Pages | 23 pdf pages = printed pages 1 to 23: **pdf page n is printed page n**. The opener (p1) shows no number. Every page carries a diagonal "not to be republished" watermark. |
| Class and age | Class 4, learners about 9 to 10 years old. |
| Extras on the opener | A QR code labelled "0433CH01" (not decoded). |
| Outside the 23 pages | Two tasks send the child to the end of the book (`textbooks/class4/demm114.pdf`, looked at again this run): Craft 2 "Use the nets given at the end of the book" (nets on three pages titled "Nets of a Triangular Prism and Rectangular Prism / Cuboid", "Nets of a Triangular Pyramid and Hexagonal Prism", "Nets of a Square Pyramid and Pentagonal Pyramid", each with "Cut along the dotted lines and fold along the dark lines") and the Card Game "2D-shape cards" (a page titled "2D Shapes", "Use the shapes given below in Chapter 1": orange square, green oval, dark-brown quarter circle, light-green semicircle, cyan triangle, pink circle). Supporting material of this chapter, not part of the 23 pages, not listed as items. There is **no cube net** among them. |
| Chapter id | `chapter_master_id` 526 (from `lp_state.json`; not confirmed live). |
| The new source | `lp_brief.md`: a 9-lesson teaching plan (8 lessons with 2 or 3 activities each = 23 activities, Lesson 9 revision) and a 10-mark assessment. The user's decisions (6 Nov 2026): ONE TOOL PER LESSON (Lessons 1 to 8); plan items that break the pipeline rules are adjusted (no degrees; no timer or points; the pentagon is the book's "five sides, all equal"; the assessment becomes an unscored recap in the review); book parts the plan does not mention are folded into the nearest lesson's tool as extra stages and questions. |

## 2. Learning objectives (what the book is aiming at)

After this chapter a child can:

1. **build** a model of a building from blocks, boxes and cans, and **say** which shape stands for which part and how the model is like and unlike the real building (p1, p2);
2. **name** prisms and pyramids, **find** the face shape common to all prisms (rectangle) and to all pyramids (triangle), and **explain** what a net is (p3);
3. **count** the faces (F), corners (V) and edges (E) of solids, **record** them in a table, **calculate** F+V−E and **explain** what they notice (p4);
4. **sort** solids by number of flat faces, number of straight edges, curved or flat faces, and with Venn circles (p4 to p7);
5. **find** the face opposite a face of a die or cube, and the faces that share an edge with a face (p5);
6. **build** cube models, **count** the cubes in a tower and **draw** a cube on triangular dot paper (p7, p8);
7. **match** a description (faces, corners, edges) to a solid and **name** it; **match** nets to solids; **decide** which nets fold into a solid (p8, p9);
8. **identify** an angle as two lines that meet at a point, **mark** and **count** angles in pictures and objects (p10, p11);
9. **make** a right-angle checker from paper, **find** and **draw** right angles; **tell** acute (less than a right angle) from obtuse (more than a right angle); **draw** and **mark** them (p11 to p13);
10. **test** with straws and clay whether a triangle, rectangle, square and pentagon keep their shape when pushed, and **describe** what happens to the angles (p14, p16);
11. **draw** three- and four-sided shapes on a dot grid, **count** their right angles, **compare** a rectangle and a square with other four-sided shapes (p15);
12. **make** a circle (equal straws; points at an equal distance from A), **name** centre, radius and diameter, **fold** paper to show that all diameters are equal and pass through the centre, **state** that the diameter is double the radius (p16 to p18);
13. **use** a compass for a circle design, **mark** centre, radius and diameter on a design, **compare** radii and diameters of wheels (p18, p19);
14. **solve** shape puzzles: hidden shapes, dividing shapes with lines or cuts, counting triangles and rectangles in a web, tracing a path that uses no wall twice, matchstick puzzles (p19 to p22);
15. **sort** 2D shapes by their sides, **classify** shapes by number of angles, **relate** sides to angles, **identify** shapes by their kinds of angles (p20, p22, p23);
16. **find** which solid has a given number of straws (edges) and clay balls (corners) (p22).

(The plan's own eight objectives, in `lp_brief.md`: identify shapes; understand 2D versus 3D; recognise prisms and pyramids; faces, edges, vertices; acute, right, obtuse; parts of a circle; geometrical patterns in everyday objects; logical thinking. See section 8B for what the book does with each.)

## 3. Concepts in the book's order

Tags: **BIG** big new idea; **FACT** small fact or vocabulary; **SKILL** hands-on skill; **PUZZLE** reasoning with a puzzle; **LINK** consolidates earlier ideas. Pages are pdf = printed.

| # | Concept | One plain line | Pages | Needs from earlier | Tag |
|---|---|---|---|---|---|
| C1 | Shapes in the buildings around us | Buildings (India Gate, Qutub Minar, a gateway, a hut, a street) can be modelled by putting simple solid shapes together; choose a shape for each part. | 1 to 2 | nothing | SKILL (context) |
| C2 | Prisms, pyramids and nets | What the prisms share (rectangular side faces, two end faces) and what the pyramids share (triangular faces meeting at one point); a net is a box opened out flat; is a cube a prism? | 3 | C1 | BIG (prism vs pyramid) + FACT (net) + SKILL (craft) |
| C3 | Faces, corners and edges of solids | Count F, V, E of five straw-and-clay solids; sort solids by flat faces and straight edges; notice F+V−E. | 4 | C2 | BIG |
| C4 | Opposite and adjacent faces | On a die and on a coloured cube, find the face opposite a face and the faces that touch it along an edge. | 5 | C3 | SKILL |
| C5 | Sorting solids by their parts | All faces alike or not; curved or straight edges; rectangular, triangular or both faces (Venn circles); curved or flat faces; the pencil sketches along the border. | 5 to 7 | C2, C3 | BIG (classification) |
| C6 | Building with cubes and counting cubes | Build four cube models; count the cubes in two cube towers. | 7 | counting | SKILL |
| C7 | Drawing a cube on triangular dot paper | Complete cube outlines on a triangular dot grid. | 8 | C6 | SKILL |
| C8 | Naming a solid from its description | Match six descriptions of faces, corners, edges to solids and name them; say how they differ. | 8 | C3, C5 | LINK |
| C9 | Nets of solids | Match four nets to solids; decide which of four nets fold into the solid below; find the solid from the cut-up pieces of a net. | 9 | C2, C3 | SKILL |
| C10 | Angles: when two lines meet | Two straws meeting at a point make an angle; angles in yoga postures; count angles in a house and a boat; mark angles in pictures; angles in the classroom. | 10, 11 | nothing | BIG |
| C11 | Right angles | Fold paper into a right-angle checker; check a book, a window and a dot grid; draw right angles. | 11, 12 | C10 | BIG + SKILL |
| C12 | Acute and obtuse angles | Acute is less than a right angle, obtuse is more; draw them on a dot grid from a given line; mark red, green, blue on stick figures; angles in V, A, Z. | 12, 13 | C11 | BIG |
| C13 | Rigid shapes: pushing a triangle, a rectangle, a square | Straw shapes pushed on a side: the triangle keeps its shape, the rectangle does not and its right angles change. | 14 | C10 to C12 | BIG (investigation) |
| C14 | Three- and four-sided shapes on a dot grid | Draw them, circle those with right angles, count shapes by number of right angles; how a rectangle and a square differ from other 4-sided shapes. | 15 | C11 to C13 | SKILL + LINK |
| C15 | The pentagon | A 5-sided shape with all sides equal; push it; see what happens to its angles. | 16 | C13 | FACT + SKILL |
| C16 | Making a circle: centre and radius | Equal straws round a point make a circle, unequal straws do not; points at an equal distance from A joined freehand make a circle; centre and radius named. | 16 | nothing | BIG |
| C17 | Diameter: folding circles | Fold circular paper in half in different ways: the creases are equal, all pass through the centre; they are diameters; centre to border is the radius. | 17 | C16 | BIG + SKILL |
| C18 | Radius and diameter: double, compass, wheels | The diameter is double the radius; a compass design; mark centre, radius, diameter on a carpet design; compare wheels. | 18, 19 | C16, C17 | BIG (relationship) + SKILL |
| C19 | Puzzling shapes | Name hidden shapes; divide a triangle into 1 square and 2 triangles; a square into 3 triangles; cuts that turn one shape into smaller shapes. | 19, 20 | C14, C15 | PUZZLE |
| C20 | Card game: sorting 2D shapes by their sides | Sort the six 2D-shape cards (end of the book) into three groups by sides; explain why. | 20 | C14 to C16 | SKILL + LINK |
| C21 | Spider webs: counting and paths | Count triangles in Squiggly's web and rectangles in Wiggly's; trace a walk that uses no wall twice. | 21 | C19 | PUZZLE |
| C22 | Matchstick puzzles | 5 sticks for 2 triangles; move 2 sticks to make 4 triangles; remove 4 sticks to leave 3 triangles. | 21, 22 | C21 | PUZZLE |
| C23 | Model challenge: straws and clay balls | Which solid has 12 straws and 8 balls? 9 and 6? 15 and 10? 10 and 6? | 22 | C3 | PUZZLE + LINK |
| C24 | Classifying shapes by angles | Sort 7 shapes by 3, 4 or 5 angles; relate sides to angles; draw shapes with fewer or more than 5 angles; count right angles; find a shape from its kinds of angles. | 22, 23 | C10 to C14 | LINK |

Themes: **A solid shapes** (C1 to C9), **B angles** (C10 to C14), **C circles and other 2D shapes** (C15 to C18, C20), **D puzzles and reasoning** (C19, C21 to C24). Big new ideas: C2, C3, C5, C10, C11, C12, C13, C16, C17 (plus C18 as a relationship). C15 is mainly a small fact with one hands-on step.

## 4. The book's story

**Characters (exact names)**

| Name | Where | What the book says |
|---|---|---|
| Diksha | p1, p3 (and, probably, the girl in the "Do you know" bubble on p2, not named there) | "Diksha wanted to go to a big city during her summer holidays. Her father took her to Delhi ..." She builds a model of India Gate with wooden blocks (p1). "Diksha has folded open and flattened a box to see what an open box looks like. This is called the net of the box." (p3). Drawn as a girl with a ponytail, yellow top, pink skirt. |
| Diksha's father | p1 | "Her father took her to Delhi". Not named, not drawn. |
| Isha | p10 | "Isha made different corners with straws." Only her hands and straws are drawn. |
| Nitesh | p9 (Q5) | "Nitesh cuts up a net on the folds. Here are its pieces." A boy with dark hair, light blue t-shirt, orange scissors. |
| Squiggly | p21 | "Squiggly, the spider, likes to make webs in different shapes." Black fuzzy spider; triangular webs; walks "each morning". |
| Wiggly | p21 | "Her brother, Wiggly made a web using rectangles." Walks "at the end of each day". |

Unnamed people in pictures (must not be named): a boy with dark hair holding a stepped green "Qutub Minar" model (p2: "I have made something. Look at my Qutub Minar."); a girl in a pink top making a straw triangle on a purple rug (p14); a girl with a red bow, purple pinafore, thinking (p19). The new plan names no character; it is written as a teacher showing pictures, videos and activities.

**Setting.** A summer-holiday trip to Delhi (named in the opener: India Gate, Qutub Minar, Safdarjung Tomb, Akshardham, the National Museum, Jantar Mantar, Sansad Bhawan; only India Gate and Qutub Minar are drawn). Diksha builds on a floor mat with a drawing of India Gate propped behind her. The opener also shows two more buildings "shown here" to model, neither named: a sandy-brown gateway with two tall minarets, and a round thatched hut. Then a classroom and craft table (straws, clay, paper, matchsticks, a compass), the children's models, a model street, two spider webs.

**Thread.** Diksha's wish to model what she saw in Delhi opens the chapter; later pages carry on with solids, nets, angles, circles and puzzles; the spiders Squiggly and Wiggly are the only recurring story pair inside the chapter.

**Recurring objects and how the book draws them**
- wooden blocks (p1): light brown cuboids, a cylinder, a cube, two half-round blocks;
- bricks (p2): red-brown clay brick, grey stone block, brown wooden block;
- prisms (p3): blue solids with dashed hidden edges (Triangular, Square [drawn long like a box with square ends], Hexagonal); pyramids (p3): pink-magenta (Triangular, Square, Pentagonal);
- the box net (p1, p3): a pink paper box opened flat, dotted folds;
- straws and clay balls (p10, p14, p16, p22; photos in the p4 table): thin straws joined by round clay balls;
- the die and the colour cube (p5): a grey-white die showing numerals 5, 1, 3; a cube in three views with faces red, orange, green, purple, dark blue, yellow;
- cube models (p7): A red, B purple, C yellow, D blue base with teal, pink, green layers and a green top cube; two towers (see Appendix A);
- solids on p8: shaded beige sphere, green square pyramid, purple cone, red cuboid, pink-purple cylinder, teal cube, a small orange triangular prism (read); and a red sphere, gold cone, blue triangular pyramid, green cube, purple cuboid. **The book draws one kind of solid in different colours in different places** (a cube is teal on one line and green on the next);
- angle marks (p10): small red arc, or red square for a right angle; the right-angle checker (p11): pale orange paper folded twice;
- dot grids: black dots on white or on pale blue, yellow, peach, pink panels; the triangular dot paper (p8) with one finished dark-purple cube;
- circular paper (p17): orange-brown with dashed creases; the compass design; the carpet (orange circle, green and yellow petals, brown border);
- wheels (p19): A grey car wheel with four oval holes, B large brown wooden spoked wheel, C bicycle wheel with blue spokes, D small dark tyre with silver rim;
- matchsticks (p21, p22): wooden stick with a red head; webs: purple threads;
- the 2D cards (end of the book): see section 1.

## 5. Every book item

One row per numbered question, per activity step-group, per fact. Sub-parts (a, b, c) that share a stem stay in one row. Kinds: `example` a solved example; `exercise` a task to do (draw, build, mark, match, sort, fold, measure); `prompt` an answerable in-text question or blank; `talk` a discussion prompt; `text` a rule, fact, figure or note. **Counts: 131 items = 1 example + 59 exercise + 49 prompt (= 109 questions) + 5 talk + 17 text.** The book has no numbered end exercise and prints no answers. Activity boxes and headings: 20 (Project Work, Craft, Let Us Observe, Sorting 3D Shapes, Build with Cubes, Cube Towers, Drawing Cubes on a Triangular Dot Paper, When Lines Meet, Let Us Do x4 [p10, p12, p13, p18], Right Angles, Acute and Obtuse Angles, Shapes with Straws, Let Us Make, Amazing Circles, Puzzling Shapes, Card Game, Let Us Try). Six "Note for Teachers" boxes (p2, p7, p14, p15, p17, p18) are `text`. Wording re-read against each page image this run; the page number is the pdf page = printed page.

| id | kind | p | the book's wording (copied) | concept |
|---|---|---|---|---|
| opening | text | 1 | Diksha wanted to go to a big city during her summer holidays. Her father took her to Delhi and they visited many old and new interesting monuments like the India Gate, Qutub Minar, Safdarjung Tomb, Akshardham, the National Museum, Jantar Mantar and Sansad Bhawan. Now she is trying to make a model of India Gate using her wooden blocks. | C1 |
| ch1.model1 | exercise | 1 | Try to make a model of the buildings shown here using blocks. | C1 |
| ch1.model_q1 | prompt | 1 | 1. What parts of the building have you shown in your model (for example, roof, pillars, base, etc.)? | C1 |
| ch1.model_q2 | prompt | 1 | 2. Why did you select these parts? | C1 |
| ch1.model_q3 | prompt | 1 | 3. What shapes will model these parts well? ______________ | C1 |
| ch1.model_q4 | prompt | 1 | 4. How is your model similar to the picture of the real building? __________________ | C1 |
| ch1.model_q5 | prompt | 1 | 5. How is it different from the real building? ______________ | C1 |
| ch1.model_talk | talk | 1 | Discussion: What would happen if you removed one piece of your model? • Would the model still look like the original building? • In what ways could you make the model even better? | C1 |
| ch1.project1 | exercise | 2 | Project Work: Encourage learners to observe a street carefully and make a model showing the main buildings on the street. | C1 |
| ch1.qutub_say | text | 2 | (boy's speech bubble) I have made something. Look at my Qutub Minar. | C1 |
| ch1.qutub_q1 | prompt | 2 | Do you think it looks like the Qutub Minar?................... | C1 |
| ch1.qutub_q2 | prompt | 2 | What shape would you use if you made a model of the Qutub Minar? Why?............... | C1 |
| ch1.qutub_q3 | prompt | 2 | How many such shapes will you use? ............................ | C1 |
| ch1.qutub_fact | text | 2 | Do you know: The Qutub Minar is a World Heritage site and the tallest building made up of bricks. It has 5 storeys and 379 stairs. | C1 |
| ch1.bricks_text | text | 2 | Earlier, people made buildings with clay bricks, stone blocks or wood. Today we also use concrete blocks, hollow blocks, etc. | C1 |
| ch1.bricks_q | prompt | 2 | What is common to all of these bricks? ……….. | C1 |
| ch1.note_boxes | text | 2 | Note for Teachers: Ask learners to collect different boxes, bottles, cans, coconut shells, etc., to model the given buildings. | C1 |
| ch1.craft1 | exercise | 3 | Craft. 1. Make a sphere-like shape with paper strips. | C2 |
| ch1.net_text | text | 3 | Diksha has folded open and flattened a box to see what an open box looks like. This is called the net of the box. If you fold along the dotted lines, you will get the box back. | C2 |
| ch1.craft2 | exercise | 3 | 2. Use the nets given at the end of the book to make the models shown below. [Prisms: Triangular Prism, Square Prism, Hexagonal Prism. Pyramids: Triangular Pyramid, Square Pyramid, Pentagonal Pyramid] | C2 |
| ch1.prism_q1 | prompt | 3 | What shape of face is common to all the prisms? _________________ | C2 |
| ch1.prism_q2 | prompt | 3 | What other shapes do these prisms have? _________________ | C2 |
| ch1.prism_q3 | prompt | 3 | How many such faces each? _________________ | C2 |
| ch1.pyr_q1 | prompt | 3 | What shape of face is common to all the pyramids? _______________ | C2 |
| ch1.pyr_q2 | prompt | 3 | All the triangular faces meet at _________________ point. | C2 |
| ch1.pyr_q3 | prompt | 3 | Identify any other shape in each of the pyramids _________________ | C2 |
| ch1.cube_prism | prompt | 3 | Is a cube also a prism? | C2 |
| ch1.prism_pyr_talk | talk | 3 | What is the difference between a prism and a pyramid? Discuss. | C2 |
| ch1.craft3 | exercise | 4 | 3. Now try to make the above shapes using straws and plasticine/thread and fill in the table. [table: Shapes / Number of faces (F) / Number of corners (V) / Number of edges (E); rows Cube/Square Prism, Cuboid/Rectangular Prism, Triangular Pyramid, Square Pyramid, Triangular Prism] | C3 |
| ch1.fve | prompt | 4 | Identify any relationship that you may find between the number of faces (F), edges (E), and corners (V). Calculate F+V–E in each case. What do you notice? | C3 |
| ch1.sort_faces | exercise | 4 | Sort 3D shapes by the number of flat faces. Write their names here. [columns: 1 flat face, 2 flat faces, 4 flat faces, 5 flat faces, 6 flat faces, 8 flat faces] | C3 |
| ch1.three_faces | prompt | 4 | Can you construct a 3D shape with 3 flat faces? | C3 |
| ch1.sort_edges | exercise | 4 | Now sort 3D shapes by the number of straight edges. Write their names here. [columns: 6 straight edges, 8 straight edges, 9 straight edges, 12 straight edges] | C3 |
| ch1.observe1 | prompt | 5 | Let Us Observe. 1. Take a die. Look at the face that has number 1. The face numbered 6 is opposite to the face numbered 1. What is the face opposite to the a) face numbered 2? …….. b) face numbered 3? …….. c) face numbered 4? …….. | C4 |
| ch1.observe2 | prompt | 5 | 2. a) Which faces have common edges with the face numbered 1? ............................ b) Which face has no common edge with the face numbered 1? .......................... | C4 |
| ch1.observe3 | prompt | 5 | 3. Look at three different views of the same cube. a) What colour is the face that is opposite to the red face? ............................ b) What colour is the face that is opposite to the yellow face? ..................................... | C4 |
| ch1.border1 | exercise | 5 | Follow these instructions for the shapes along the border. 1. Colour all shapes with a rectangular face in red. | C5 |
| ch1.border2 | exercise | 5 | 2. Draw a smiley on shapes with a triangular face. | C5 |
| ch1.border3 | exercise | 5 | 3. Draw a star on shapes with a curved face. | C5 |
| ch1.border4 | exercise | 5 | 4. Colour all shapes with no corner in blue. | C5 |
| ch1.border5 | exercise | 5 | 5. Circle the shapes that have the same opposite faces. | C5 |
| ch1.sort1 | exercise | 6 | Sorting 3D Shapes. Write the names of 3D shapes in the correct places. (1) A: All faces look the same. B: All faces do not look the same. | C5 |
| ch1.sort2 | exercise | 6 | (2) A: Shapes with curved edges. B: Shapes with straight edges. | C5 |
| ch1.sort3 | exercise | 6 | (3) A: Shapes with rectangular faces. B: Shapes with triangular faces. Overlap: Shapes with both rectangular and triangular faces. | C5 |
| ch1.sort3_q | prompt | 7 | In which circle did you write triangular prism and rectangular pyramid? | C5 |
| ch1.sort4 | exercise | 7 | Let us sort shapes in another way. Using circles like those on the previous page, can you sort shapes into the categories "Shapes with curved faces" and "Shapes with flat faces"? | C5 |
| ch1.note_venn | text | 7 | Note for Teachers: Use the available wooden, paper, and straw models. Discuss adjacent and opposite faces. Discuss shapes that fall into two sets. Let them make Venn diagrams (using circles like above) and write the names of these shapes. | C5 |
| ch1.build1 | exercise | 7 | Build with Cubes. Build these models with the cubes from the Jaadui Pitara Kit or any other similar material. A. B. C. D. | C6 |
| ch1.towers | prompt | 7 | Cube Towers. How many cubes are there in each of these cube towers? | C6 |
| ch1.dotcubes | exercise | 8 | Drawing Cubes on a Triangular Dot Paper. Can you complete the following cubes? | C7 |
| ch1.solids_q1 | exercise | 8 | 1. Match the pictures to the descriptions and name the shapes. a) I have 5 faces and 5 corners. I have 8 edges. 1 of my faces is a square and 4 of my faces are triangles.............. b) I have 1 flat face, 1 curved face, and 1 edge.............. c) I have 1 curved face. I have no edges or corners........ d) I have 2 flat faces, 1 curved face, and 2 edges. I have no corners.............. e) I have 5 faces, 6 corners, and 9 edges, and 2 of my faces are triangles.............. f) I have 6 faces, 12 edges, and 8 corners.............. | C8 |
| ch1.solids_q2 | talk | 8 | 2. Each one is different. How? Discuss. | C8 |
| ch1.solids_q3 | exercise | 9 | 3. Match the following nets to the appropriate solids given below. [nets (1) to (4); solids (a) to (d)] | C9 |
| ch1.solids_q4 | exercise | 9 | 4. Which of these nets can be folded to make a solid of the kind given below? [nets A to D, each with a solid below it] | C9 |
| ch1.solids_q5 | exercise | 9 | 5. Nitesh cuts up a net on the folds. Here are its pieces. [one pentagon, five triangles] Which solid has the above pieces in its net? [solids a. b. c. d.] | C9 |
| ch1.angle_text | text | 10 | Isha made different corners with straws. We can say that the two straws are like two lines that meet at a point. When two lines meet they create an angle. | C10 |
| ch1.yoga_text | text | 10 | We see many angles in yoga postures. [five yoga figures with angles marked] | C10 |
| ch1.house_ex | example | 10 | There are 7 angles in this house drawing. | C10 |
| ch1.boat_q | prompt | 10 | How many angles are there in this boat drawing? | C10 |
| ch1.angles_do1 | exercise | 10 | Let Us Do. 1. Mark the angles in the following pictures. a) b) c) d) e) [scissors, hanger, a hand making a V sign, a seesaw, a slide] | C10 |
| ch1.angles_do2 | prompt | 11 | 2. Where do you see angles in the classroom? Give a few examples. | C10 |
| ch1.right_make | exercise | 11 | Right Angles. Let's make a right angle with a piece of paper as shown. | C11 |
| ch1.right_circle | exercise | 11 | Identify the angles that you think are right angles and circle them in the dot grid given below. Check using your right angle checker. | C11 |
| ch1.right_objects | exercise | 11 | Check for right angles in a book, window, and any other object. Write the names of objects where you find right angles. | C11 |
| ch1.right_do1 | exercise | 12 | Let Us Do. 1. Draw some right angles on the dot grid. | C11 |
| ch1.acute_text | text | 12 | Acute and Obtuse Angles. Acute angles are less than a right angle. Obtuse angles are more than a right angle. | C12 |
| ch1.acute_obj | prompt | 12 | Name some objects from your classroom which have an acute angle. | C12 |
| ch1.obtuse_obj | prompt | 12 | Name some objects from your classroom which have an obtuse angle. | C12 |
| ch1.letters | exercise | 12 | Identify all angles in the following letters. [V, A, Z] | C12 |
| ch1.ao_do1a | exercise | 13 | Let Us Do. 1. Draw some acute angles on the top grid. Draw a line to make an acute angle using each given line in the bottom grid. | C12 |
| ch1.ao_do1b | exercise | 13 | Draw some obtuse angles on the top grid. Draw a line to make an obtuse angle using each given line in the bottom grid. | C12 |
| ch1.ao_do2 | exercise | 13 | 2. In the figures given below, mark the acute angles in red, right angles in green, and obtuse angles in blue. [four stick figures] | C12 |
| ch1.straw_tri_make | exercise | 14 | Shapes with Straws. Make a triangle with straws of different sizes and clay/plasticine. | C13 |
| ch1.straw_tri_push | prompt | 14 | Does the shape of the triangle change if we gently push one of its sides? Yes/No | C13 |
| ch1.straw_tri_trace | exercise | 14 | Trace the triangles you made with the straws in your notebook. | C13 |
| ch1.straw_tri_angles | prompt | 14 | What kinds of angles does a triangle have? | C13 |
| ch1.straw_rect_make | exercise | 14 | Make a rectangular shape with straws and clay. | C13 |
| ch1.straw_rect_angles | prompt | 14 | What kinds of angles do you see in the rectangle?.................. | C13 |
| ch1.straw_rect_push | prompt | 14 | Does the shape of the rectangle change if we gently push one of its sides? Yes/No | C13 |
| ch1.straw_rect_after | prompt | 14 | What has happened to the angles of the new shape? Are they still right angles? What types of angles have been formed? | C13 |
| ch1.straw_square | prompt | 14 | Similarly, push one side of a square. Are they still right angles? What types of angles have been formed? | C13 |
| ch1.straw_compare | prompt | 14 | How are the angles of triangles and rectangles similar or different? | C13 |
| ch1.note_rigid | text | 14 | Note for Teachers: Help children to understand the rigidity of different shapes. The triangle is the most rigid shape, as it does not change its shape when pushed. | C13 |
| ch1.dotshapes | exercise | 15 | Use the dot grid given below to draw several three- and four-sided shapes. Circle the shapes that have one or more right angles. | C14 |
| ch1.dotshapes_q | prompt | 15 | Discuss: What shapes did you make? How many shapes have you made with a) 1 right angle b) 2 right angles c) 3 right angles d) all right angles | C14 |
| ch1.fourside_q | prompt | 15 | Here are some 4-sided shapes. In what ways are rectangle and square different from these shapes? [a green trapezium-like shape, a pink parallelogram, an orange diamond] | C14 |
| ch1.note_square | text | 15 | Note for Teachers: Discuss similarities and differences between a square and a rectangle. Provide experiences to observe squares as a special case of rectangles. Teachers can also provide more dot grids, if required. | C14 |
| ch1.pentagon_make | exercise | 16 | Try to make this 5-sided shape with all sides equal (Pentagon) | C15 |
| ch1.pentagon_q1 | prompt | 16 | Are these right angles? | C15 |
| ch1.pentagon_q2 | prompt | 16 | Does the shape of the pentagon change if we gently push one of its sides. Yes/No | C15 |
| ch1.pentagon_q3 | prompt | 16 | How does this change the angles? | C15 |
| ch1.circle_straws | exercise | 16 | Can you make a circle using straws? | C16 |
| ch1.circle_straws_q1 | prompt | 16 | Look at the picture. The lengths of the straws in this picture are ................. (Equal/Unequal) | C16 |
| ch1.circle_straws_q2 | prompt | 16 | What will happen if we take straws of unequal lengths? | C16 |
| ch1.make_circle | exercise | 16 | Let Us Make. Can you use a scale to draw a circular shape? Let us see. Mark a point A. Draw many points that are at an equal distance from point A. Connect the dots freehand. | C16 |
| ch1.make_circle_q | prompt | 16 | What do you get? ................ | C16 |
| ch1.centre_text | text | 16 | The point A is the centre and the line from the centre to the border of the circle is the radius. | C16 |
| ch1.amazing1 | exercise | 17 | Amazing Circles. a) Take a piece of circular paper. b) Fold your paper in half and crease it well. c) Open the fold and measure the length of the crease using a thread. d) Fold your paper in half in a different way and crease it well. e) Open the fold and measure the length of the crease again. f) Fold it again in half in a different way and crease it well. g) Open the fold, measure the length of the crease. | C17 |
| ch1.amazing_q1 | prompt | 17 | 1. The length of all the creases are __________. (Equal/Unequal) | C17 |
| ch1.amazing_t2 | text | 17 | 2. These creases are called diameters of the circle. | C17 |
| ch1.amazing_t3 | talk | 17 | 3. Discuss where the centre is. Do you notice that all the diameters pass through the centre? | C17 |
| ch1.amazing_q4 | exercise | 17 | 4. Measure the length of the creases from the center to the border of the circle. This is called the radius of the circle. | C17 |
| ch1.amazing_t5 | talk | 17 | 5. Discuss if there is any relationship between the radius and the diameter of a circle. | C17 |
| ch1.note_measure | text | 17 | Note for Teachers: Children can measure the length using a paper strip or thread or scale. | C17 |
| ch1.circ_do1 | exercise | 18 | Let Us Do. Fold the circular paper in half. Fold this half again in half. The length of the diameter is ___________ (half/double) of the length of radius. | C18 |
| ch1.compass | exercise | 18 | A circle can be made easily using a compass. Ask your teacher to help you use a compass. Make the following design. [Step. 1, Step. 2, Step. 3] | C18 |
| ch1.carpet | exercise | 18 | Look at the carpet design. A beautiful circle, right? Mark the centre, radius, and the diameter of the circular design with any colour of your choice. | C18 |
| ch1.note_compass | text | 18 | Note for Teachers: Help children to draw circles using a compass. Encourage learners to draw different-sized circles. | C18 |
| ch1.wheels_q0 | prompt | 19 | Look at the wheels. All wheels look like …………… | C18 |
| ch1.wheels_q1 | prompt | 19 | Name the wheel with the 1. longest radius ……................ 2. shortest radius ……................ 3. longest diameter ……................ 4. shortest diameter ……................ | C18 |
| ch1.puzzle1 | exercise | 19 | Puzzling Shapes. 1. Identify the hidden shapes and write their names. | C19 |
| ch1.puzzle2 | exercise | 19 | 2. Draw 2 lines to divide the triangle into 1 square and 2 triangles. | C19 |
| ch1.puzzle3 | exercise | 19 | 3. Draw 2 lines to divide the square into 3 triangles. | C19 |
| ch1.puzzle4 | exercise | 20 | 4. Draw lines to show the cuts needed on the shapes in the left column to get the smaller shapes on the right. [(A), (B), (C)] | C19 |
| ch1.cards | exercise | 20 | Card Game. Sort the 2D-shape cards given at the end of the book into three groups according to their sides. Draw the sorted shapes in the space given below. Explain why you sorted your shapes in this way. | C20 |
| ch1.try1_text | text | 21 | Let Us Try. 1. Squiggly spiders. Squiggly, the spider, likes to make webs in different shapes. One day she begins to make triangular webs. [...] Her brother, Wiggly made a web using rectangles. [...] She likes to take a walk each morning and check if the walls of her web are strong. [...] He likes to take a walk at the end of each day and check if the walls of his web are strong. | C21 |
| ch1.try1a | prompt | 21 | How many triangles are in her web? | C21 |
| ch1.try1b | exercise | 21 | Can she begin at point A and reach back to the same point without walking on any wall more than once? Trace and show Squiggly's path. | C21 |
| ch1.try1c | prompt | 21 | How many rectangles can you see in his web? | C21 |
| ch1.try1d | exercise | 21 | Can he begin at point A and leave from point B without walking on any wall more than once? Trace and show Wiggly's path. | C21 |
| ch1.try2 | exercise | 21 | 2. Use 5 matchsticks to make 2 triangles. Then draw it in the space provided. | C22 |
| ch1.try3 | exercise | 22 | 3. Move two of these matchsticks to form 4 triangles. | C22 |
| ch1.try4 | exercise | 22 | 4. Remove 4 of these matchsticks to leave only 3 triangles. | C22 |
| ch1.try5 | exercise | 22 | 5. Model challenge. Can you make a model of solid shapes which has a) 12 straws and 8 clay balls? b) 9 straws and 6 clay balls? c) 15 straws and 10 clay balls? d) 10 straws and 6 clay balls? | C23 |
| ch1.try6 | exercise | 22 | 6. Classify these shapes based on the number of angles. [shapes a to g; boxes: 3 angles, 4 angles, 5 angles] | C24 |
| ch1.try6_q | prompt | 22 | What relation do you notice between the number of sides and the number of angles? | C24 |
| ch1.try7a | exercise | 23 | 7. Draw a 2D shape that has less than 5 angles. | C24 |
| ch1.try7b | exercise | 23 | Draw a 2D shape with more than 5 angles. | C24 |
| ch1.try8 | exercise | 23 | 8. Mark the right angles and write the number of right angles in each figure. [six figures] | C24 |
| ch1.try8_q | prompt | 23 | Which of the above shapes have only right angles? | C24 |
| ch1.try9 | exercise | 23 | 9. Observe the following shapes. [shapes 1 to 14] Identify the shape that has: ● 2 right angles, 1 acute, and 1 obtuse angle ____ ● 1 right, 2 obtuse, and 1 acute angle ____ ● 2 obtuse, and 2 acute angles ____ ● 4 right angles ____ | C24 |

Notes on the kinds (same as the previous build; confirm in section 7): `ch1.house_ex` is the only solved example (7 angles in the house, then the boat is asked); `ch1.dotshapes_q` is headed "Discuss:" but asks the child to count shapes, so it is a `prompt`; `talk` is kept for open discussion with no short answer (model_talk, prism_pyr_talk, solids_q2, amazing_t3, amazing_t5). Physical tasks (Craft 1, 2, 3, Project Work, Build with Cubes, folding, compass, Trace in the notebook) are `exercise` so none is dropped; whether and how they appear on a screen is for later steps.

## 6. Printed-book errors and ambiguities

No arithmetic error found: the house has 7 marked angles; the Qutub Minar facts are the book's own; every description in p8 Q1 and every count in p22 Q5 is a true solid; F+V−E is 2 for all five table solids. What follows are figures that do not match their text, missing answers and unclear wording. "(mine)" = my reading of the figure, re-measured this run.

| # | Where | What | Effect |
|---|---|---|---|
| E1 | p9 Q4 (`ch1.solids_q4`) | Net A is a column of four rectangles with one flap on the right of the top row and one on the right of the bottom row: both flaps are on the **same side**, so the flaps cover the same end and the other end stays open; it cannot make the yellow box (mine, re-checked). Net A is made of **six rectangles** that do NOT fold into a cuboid. Net C has the square and only **2 of the 4** triangles the red pyramid needs. Nets B (cylinder) and D (flat box: end faces on opposite sides) are fine. | The question is meant to have "no" answers, but no key is printed. Do not reuse A or C as a "this folds" picture. Also: any plan sentence "six rectangles make a cuboid" is contradicted by the book's own net A. |
| E2 | p4 | "Can you construct a 3D shape with 3 flat faces?" does not say whether curved faces are allowed. Only-flat solids need at least 4 faces; a half-cylinder has exactly 3 flat faces (two semicircles and a rectangle) plus 1 curved face. | Answer depends on the reading. |
| E3 | p4 sorting tables | The set of shapes to sort is not stated. The straight-edge table (6, 8, 9, 12) has no column for the pentagonal pyramid (10 edges) or hexagonal prism (18); the flat-face table has no column for 0 (sphere), 3 or 7. (mine) Fit: 1 flat face cone; 2 cylinder; 4 triangular pyramid; 5 square pyramid, triangular prism; 6 cube, cuboid, pentagonal pyramid; 8 hexagonal prism. 6 edges triangular pyramid; 8 square pyramid; 9 triangular prism; 12 cube, cuboid. | Not an error; the child cannot place every p3 shape. The "8 flat faces" column is the book's only hint about the hexagonal prism. |
| E4 | p7 | "In which circle did you write triangular prism and rectangular pyramid?" A **rectangular pyramid** is never named (the pyramids named are triangular, square, pentagonal); the red solid in p9 Q4 is a pyramid on a rectangle. The question points to the three-part Venn of p6 (3); both belong in the overlap if a square base counts as a rectangle (the p15 note says a square is a special rectangle). | Wording gap. |
| E5 | p8 Q1 | Seven pictures beside six descriptions a) to f): sphere, square pyramid, cone, cuboid, cylinder, cube, and a small orange solid (re-read at 4x: a triangular prism lying on a rectangle, triangle end visible). Description f) "6 faces, 12 edges, 8 corners" fits **both** the red cuboid and the teal cube. Pictures are not lettered. | The child picks one or accepts two. |
| E6 | p5 Let Us Observe 1 | "The face numbered 6 is opposite to the face numbered 1", then asks for the faces opposite 2, 3, 4. Answers depend on the die in hand (most dice: 5, 4, 3); the picture shows only 5, 1, 3. | Not printed. |
| E7 | p5 border | About 20 pencil sketches (re-counted: 2 dice, 2 erasers, 3 balls incl. a football, 3 cans or bottles, an ice-cream cone, a party hat, 2 cheese pieces, a Rubik's cube, a gift box, a wooden wedge, a cake slice, a pyramid drawn with a triangle grid, a double pyramid). Instruction 5 "Circle the shapes that have the same opposite faces" is unclear. No numbering, no key. | Ambiguous to turn into questions as printed. |
| E8 | p10 | The house "has 7 angles" (3 in the roof, 4 right-angle marks: confirmed). For the boat (mine, re-counted) **10 marks** are drawn (2 at the sail top split by the mast, 2 at the sail's bottom corners, 2 right-angle squares where the mast meets the sail, 4 in the hull). | The boat answer is the count of printed marks. |
| E9 | p11 dot grid | Eight angle figures, no key. (mine, measured) Right angles: top row 2nd and 3rd; bottom row 1st ("<", 90°) and 4th (">", 90°). Others: top row 1st and 4th are obtuse (about 116°, 117°); bottom row 2nd about 53° and 3rd about 27° (acute). | Reading by measurement. |
| E10 | p12 letters, p13 stick figures | "Identify all angles" in V, A, Z: only one angle per letter is pre-marked, the number of angles in A is not stated. The four stick figures do not say how many to mark. | Counts open. |
| E11 | p14 | Several questions have an answer the book never prints (triangle does not change; rectangle does; new angles are no longer right angles). The teacher note says only "The triangle is the most rigid shape". | Answers must come from the content team. |
| E12 | p15 | The three "4-sided shapes" (trapezium-like, parallelogram, diamond) are not named. | Do not introduce names without a decision. |
| E13 | p16 | "Does the shape of the pentagon change if we gently push one of its sides. Yes/No" has no question mark. "all sides equal (Pentagon)" is an equilateral pentagon, not necessarily with equal angles: pushing changes the angles, which is the point. | Typo; wording. |
| E14 | p17 | "centre" (items 3, p16) and "center" (item 4). Item 5 is answered only on p18 ("half/double"). | Spelling; order. |
| E15 | p18 | "Ask your teacher to help you use a compass." Steps 1 to 3 are pictures only. | Teacher-role wording; steps read from the picture. |
| E16 | p19 wheels | Longest and shortest radius and diameter are asked but no units or measures are printed. (mine, measured outer diameters in one scale) B 458, C 417, A 355, D 305: **B longest, D shortest** (order B > C > A > D). | Reading by measurement. |
| E17 | p19 to p20 | **CORRECTED.** Hidden shapes: number to find not stated. (mine, measured) the outline picture holds **6**: one circle, one cylinder, ONE upright square (303 by 302), ONE tilted rectangle (539 by 237, about 2.3 times as long as wide) and two triangles. The previous analysis said "two squares": wrong. Q2 and Q3 have solutions on the dot grid (Appendix A), none printed. Q4: (A) long hexagon into a rectangle and 2 triangles (2 cuts, one at each pointed end); (B) square into 4 right triangles (3 cuts); (C) triangle into 4 pieces: 3 corner triangles of different sizes and a hexagon (3 corner cuts). Cut lines are not unique. | Open answers. |
| E18 | p20 | The six cards are only at the end of the book (see section 1). "according to their sides" does not say what the three groups are. | Cards not in the 23-page file; the rule is open. |
| E19 | p21 | **Widened.** Squiggly's web (re-drawn: corners T, UL, UR, centre X, LL, LR, A; 12 walls). Triangles (mine) **10**: 1 top, 1 bottom, 4 small inner, 4 large inner. Every corner has an even number of walls, so a closed walk over every wall exists; **her printed wall numbers 1 to 12 already trace one valid closed walk from A back to A** (consecutive numbers share a corner): the figure gives the answer away. Wiggly's web: rectangles (mine) **12** (1 top box, top box plus the box under it, 6 in the first row of three cells counting pairs and the triple, 2 in the second row, 2 two-row ones). Corners with an odd number of walls: the two row-2 end corners (left and right edge) only; A and B each have 2 walls. So a walk over **every** wall from A to B does **not** exist. But the questions never say "every wall": read as "any walk from A to B without repeating a wall" both walks are trivially yes (A, down, left to the middle line, down to B). | The intended reading must be decided. |
| E20 | p21, p22 | **Resolved this run (mine).** Q2: 5 sticks, 2 triangles sharing a stick (a four-sided diamond with one diagonal). Q3: 9 sticks (three triangles of 3 sticks). It is solvable only if the three triangles touch at their base corners (the print draws small gaps between them). Q4: 13 sticks, 6 small triangles plus one big triangle of side 2 (7 triangles). Solutions in Appendix A. | The book prints none. |
| E21 | p22 Q5 | (c) 15 straws and 10 balls is a **pentagonal prism**, a solid the chapter never shows. (a) cube or cuboid, (b) triangular prism, (d) pentagonal pyramid are in the chapter. The picture beside Q5 is a square pyramid of blue straws and orange balls (8 straws, 5 balls), not one of the four answers. | The child builds a solid not shown earlier. |
| E22 | p23 Q9 | (mine, measured) several shapes fit each line: 2 right, 1 acute, 1 obtuse: **2 and 7**; 1 right, 2 obtuse, 1 acute: **10**; 2 obtuse and 2 acute: **3, 5, 8, 9, 11, 13**; 4 right angles: **4, 6, 12, 14**. Shape 1 is a dart: 3 acute corners and one corner bigger than a straight line (a kind of angle the chapter never names). | Ambiguous; one short blank per line. |
| E23 | p23 Q8 | **CORRECTED.** Right-angle counts left to right (mine): 4, 0, 1, 0, 0, 4. Only the first (blue rectangle) and last have only right angles. The last figure is a **tilted rectangle** (about 190 by 157, a little longer than wide), not a square as the previous analysis said. The purple triangle has one right angle (90.8° measured). | Reading by measurement. |
| E24 | p3 and the end pages | Craft 2 shows a "Square Prism"; the end-of-book net page is named "Rectangular Prism / Cuboid" and there is no net named "Square Prism". The p4 table row is "Cube/Square Prism". | Names do not line up. |
| E25 | text layer | `chapter_text.md` puts "What relation do you notice between the number of sides and the number of angles?" after Q5; the page prints it under Q6. | Use the page. |
| E26 | p7 tower 2 | Colours are not consistent: the side faces of the back-left arm are green where the same faces elsewhere are light cyan. The cube structure is unaffected. | Do not copy the colouring. |
| E27 | p7 both towers | Only the outside is drawn: both counts (30, 66) assume solid layers with no gaps and no extra hidden cubes. The book never says "hidden" but the answer needs inferring the hidden cubes. | State the assumption. |
| E28 | p12 | "Obtuse angles are more than a right angle" has no upper limit: a corner bigger than a straight line is also "more than a right angle" (p23 shape 1 has one). | Definition incomplete. |
| E29 | p14 | The only rule about rigidity is a teacher note ("the triangle is the most rigid shape, as it does not change its shape when pushed"). The words "rigid" and "rigidity" appear nowhere in the child's text. | The word is for the teacher. |
| E30 | p16 | The straw pentagon is drawn as a regular-looking pentagon of five equal blue straws; the text never says "regular". | See section 8B. |
| E31 | p19 Q1 | The hidden shapes are all one red; one is a cylinder (3D) among 2D outlines. | Note for the figure. |

## 7. Open questions for the user

1. **Tool table.** `tool_map.md` is still the empty template: names, purposes and order of the 8 tools (one per lesson) are not yet written. Lesson 9 has no tool (confirm).
2. **Load per tool.** With 8 tools and 109 questions the average is 13.6 per tool (the cap is 6, a config default). My suggested folding (section 8A) gives 20, 13, 4, 11, 3, 24, 17, 17. Raise the cap for this chapter, group sub-parts, or send the dot-grid and classify-by-angles questions (10) to the Lesson 9 worksheet?
3. **Words.** The book says "corner" (V for corners) and never "vertex", "apex", "base" (of a solid), "polygon", "2D/3D" definitions. The plan's Lesson 4 uses "Vertex" as a label and asks "What is a vertex?". Use "corner (also called vertex)", or "corner" only? Keep "apex" for the point where the pyramid's faces meet?
4. **"Face".** The plan says a face is a flat surface; the book counts curved faces (cone, cylinder, sphere, p8). Keep the book's meaning when the folded book items (sorting, p8 Q1) reach the tool?
5. **Plan's own numbers and statements** (hexagonal prism 8, 18, 12; "a cube is a special square prism"; the cm sums; the 8 assessment questions; the true/false statements) are not in the book. All are mathematically true; the assessment questions are not book items. May the unscored recap use them, or must it reuse book items?
6. **Cube net.** The book draws no cube net; the plan's Fold It and "six connected squares" need one. May a cube net be drawn (and the wording changed to "squares joined in a cross", not "any six joined squares")?
7. **"Build a cube using smaller unit cubes"** (Lesson 2): the size (8 or 27 cubes) is not in the book.
8. **Answers.** The book prints none. Who signs off Appendix A?
9. **Walk questions** (E19): "every wall once" or "any path"?
10. **Matchstick Q3** (E20): draw the triangles touching?
11. **Physical-only tasks** (Craft 1, 2, 3, Project Work, paper folding, compass, collect boxes, notebook tracing): on-screen version, one image, or a story step?
12. **End-of-book pages** (nets, cards): may later steps use them?
13. **Teacher-role wording.** The plan is itself teacher-voiced ("I will..."); the book has six teacher notes. Re-word for the child?
14. **Pentagonal prism** (p22 Q5 c): accept a solid the chapter never shows?
15. **Kinds** (section 5 notes): confirm `house_ex` as the only example, `dotshapes_q` as a prompt, and the five talk items.
16. **Unnamed pictured people** (p2 boy, p14 girl, p19 girl): "a child" in briefs, or leave out?
17. **Solid colours.** The book draws one solid in several colours. The previous build's decision (one colour per solid, every solid a shaded 3D solid, a sphere always a shaded ball) is not decided for this rebuild.

## 8. Book vs the new plan

The plan (lp_brief.md): Lesson 1 Introduction to Shapes Around Us (activities: Shape Detective, Guess the Shape); Lesson 2 Prisms and Pyramids (Match the 3D Shape, Build Your Own 3D Shape, Prism or Pyramid); Lesson 3 Nets (Fold It, Which Net Makes Which Shape, Find the Wrong Net); Lesson 4 Faces, Edges and Corners (Label the Cube, Count and Win, Spin the Shape); Lesson 5 Cube Towers and Drawings (Build a Cube Tower, Look Carefully, Copy the Cube Structure); Lesson 6 Angles (Angle Builder, Angle Sorting, Beat the Clock); Lesson 7 Circles and Pentagons (Circle Detective, Radius or Diameter, Build a Pentagon); Lesson 8 Rigidity with Straws (Triangle vs Rectangle, Build a Strong Structure, True or False); Lesson 9 Revision and assessment. Codes used below: L2A1 = Lesson 2, Activity 1, and so on.

### 8A. Coverage matrix

**Status codes.** Y = the plan teaches or asks the same thing; P = same topic, a different task or wording (for example degrees instead of "right angle"); N = NOT IN THE PLAN.

**A1. By book concept.** Items are counted from the 131 items of section 5 (kinds text and talk included).

| Concept | Items Y / P / N | What the plan covers | Verdict | Where to fold the rest |
|---|---|---|---|---|
| C1 Shapes in buildings | 1 / 4 / 12 | L1 intro: monuments (India Gate, Qutub Minar), "what shapes can you identify". | PARTLY | L1: block model of a building, street project, Qutub Minar shape and number of pieces, bricks |
| C2 Prisms, pyramids, nets | 9 / 1 / 1 | L2 slides (prisms, pyramids, "a cube is a special square prism"); L3 (net) | COVERED | craft1 (paper-strip sphere) to L2 |
| C3 Faces, corners, edges | 0 / 1 / 4 | L4 counts (cube, cuboid, triangular prism, square pyramid) | PARTLY | F+V−E, sort by flat faces, sort by straight edges, 3 flat faces to L4 |
| C4 Opposite and adjacent faces | 0 / 1 / 2 | L4A3 uses a die, asks visible faces | PARTLY | opposite and adjacent faces, three views of the coloured cube to L4A3 |
| C5 Sorting solids by their parts | 0 / 2 / 9 | L2A3 two baskets (Prism, Pyramid) | PARTLY | Venn circles, curved or flat, rectangular or triangular faces to L2A3; border objects to L1 (4) and L4 (1) |
| C6 Building and counting cubes | 1 / 1 / 0 | L5A1, L5A2, L5A3 | COVERED | none |
| C7 Cube on triangular dot paper | 0 / 1 / 0 | L5 video script mentions an isometric grid, no activity | PARTLY | L5 |
| C8 Naming a solid from a description | 0 / 1 / 1 | L4A2 counts; L2A1 names | PARTLY | the "I have..." riddle form to L4A2 (or L1A2); the curved solids (sphere, cone, cylinder) are not in the plan |
| C9 Nets of solids | 2 / 0 / 1 | L3A1, L3A2, L3A3 | COVERED | solids_q5 (pieces of a cut-up net) to L3 |
| C10 Angles: when lines meet | 1 / 0 / 5 | L6 intro (two rays at a point), L6A1 | PARTLY | yoga, house and boat counts, mark angles in pictures, angles in the classroom to L6 |
| C11 Right angles | 0 / 2 / 2 | L6 right angle = corner of a square; L6A1 | PARTLY | paper right-angle checker, right angles in objects to L6 |
| C12 Acute and obtuse | 0 / 4 / 3 | L6 acute, obtuse (with degrees); L6A1, L6A2 | PARTLY | objects, letters V A Z, dot-grid drawing; book form is "less than / more than a right angle" (no degrees) |
| C13 Rigid shapes | 6 / 3 / 2 | L8A1 triangle vs rectangle | COVERED | tracing and "what angles does a triangle have" to L8 |
| C14 Dot-grid 3- and 4-sided shapes | 0 / 0 / 4 | none | NOT IN THE PLAN | L6 (right angles in shapes; rectangle vs other 4-sided shapes), or L9 worksheet |
| C15 The pentagon | 1 / 1 / 2 | L7A3 | PARTLY | push test and "how does this change the angles" to L7 (or L8) |
| C16 Making a circle: centre, radius | 1 / 0 / 5 | L7 centre and radius; L7A1 | PARTLY | equal-straws circle, points at equal distance from A to L7 |
| C17 Diameter: folding circles | 2 / 2 / 3 | L7 diameter definition | PARTLY | folding creases, all equal, through the centre to L7 |
| C18 Radius, diameter, compass, wheels | 1 / 2 / 3 | L7A2 (cm sums), L7A1 (carpet is like Circle Detective) | PARTLY | compass design, "all wheels look like circles", wheels by radius and diameter to L7 |
| C19 Puzzling shapes | 1 / 0 / 3 | L1A1 Shape Detective (hidden shapes) | PARTLY | the three cut puzzles to L1 (2D shapes) or L8 (triangles) |
| C20 Card game of 2D shapes | 0 / 0 / 1 | none | NOT IN THE PLAN | L1 (2D shapes) |
| C21 Spider webs | 0 / 0 / 5 | none | NOT IN THE PLAN | L8 (triangles and rectangles of threads), or L1A1 |
| C22 Matchstick puzzles | 0 / 0 / 3 | none | NOT IN THE PLAN | L8 |
| C23 Model challenge: straws and balls | 0 / 0 / 1 | none | NOT IN THE PLAN | L4A2 (straws = edges, balls = corners); (c) is a pentagonal prism |
| C24 Classifying shapes by angles | 0 / 3 / 4 | L6A2 sorts angles, not shapes | PARTLY | classify, relate sides to angles, draw, count right angles, find the shape to L6 (or L9) |

Totals: **Y 26, P 29, N 76** of 131 items. COVERED 4 concepts (C2, C6, C9, C13), PARTLY 15, NOT IN THE PLAN 5 (C14, C20, C21, C22, C23).

**A2. The specific parts you asked about.**
- Opposite and adjacent faces of a die: NOT IN THE PLAN (L4A3 spins a die but asks visible faces) to L4A3.
- Sorting solids by parts, overlapping circles: NOT IN THE PLAN to L2A3.
- Paper right-angle checker and dot-grid angles: NOT IN THE PLAN to L6.
- Equal-straws circle: NOT IN THE PLAN to L7.
- Folding circles: NOT IN THE PLAN (the plan has the definitions only) to L7.
- Compass design: NOT IN THE PLAN to L7.
- Wheels and carpet: carpet is close to L7A1 (PARTLY); wheels are NOT IN THE PLAN to L7A2.
- Spider webs: NOT IN THE PLAN to L8 (or L1A1).
- Matchstick puzzles: NOT IN THE PLAN to L8.
- Straw-and-clay model challenge: NOT IN THE PLAN to L4A2.
- Card game of 2D shapes: NOT IN THE PLAN to L1.
- Classifying shapes by angles: NOT IN THE PLAN (L6A2 sorts angles) to L6.
- Hidden shapes: puzzle1 is covered by L1A1; cuts (puzzle2 to 4) are NOT IN THE PLAN to L1 or L8.
- Also not in the plan: F+V−E and the sorts by flat faces and straight edges; the curved solids (sphere, cone, cylinder); Craft 1 (paper-strip ball); Project Work and the bricks; the Qutub Minar facts; every `talk` prompt (model_talk, solids_q2, amazing_t3, amazing_t5; prism_pyr_talk is covered by L2).

**A3. Items by status, per concept** (every item id appears once; ids without the "ch1." prefix; `opening` is the item "opening").

| C | Y | P | N |
|---|---|---|---|
| C1 | model_q3 | opening, model1, model_q1, model_q2 | model_q4, model_q5, model_talk, project1, qutub_say, qutub_q1, qutub_q2, qutub_q3, qutub_fact, bricks_text, bricks_q, note_boxes |
| C2 | net_text, prism_q1, prism_q2, prism_q3, pyr_q1, pyr_q2, pyr_q3, cube_prism, prism_pyr_talk | craft2 | craft1 |
| C3 | | craft3 | fve, sort_faces, three_faces, sort_edges |
| C4 | | observe1 | observe2, observe3 |
| C5 | | border1, border2 | border3, border4, border5, sort1, sort2, sort3, sort3_q, sort4, note_venn |
| C6 | towers | build1 | |
| C7 | | dotcubes | |
| C8 | | solids_q1 | solids_q2 |
| C9 | solids_q3, solids_q4 | | solids_q5 |
| C10 | angle_text | | yoga_text, house_ex, boat_q, angles_do1, angles_do2 |
| C11 | | right_circle, right_do1 | right_make, right_objects |
| C12 | | acute_text, ao_do1a, ao_do1b, ao_do2 | acute_obj, obtuse_obj, letters |
| C13 | straw_tri_make, straw_tri_push, straw_rect_make, straw_rect_push, straw_rect_after, note_rigid | straw_rect_angles, straw_square, straw_compare | straw_tri_trace, straw_tri_angles |
| C14 | | | dotshapes, dotshapes_q, fourside_q, note_square |
| C15 | pentagon_make | pentagon_q1 | pentagon_q2, pentagon_q3 |
| C16 | centre_text | | circle_straws, circle_straws_q1, circle_straws_q2, make_circle, make_circle_q |
| C17 | amazing_t2, amazing_t5 | amazing_t3, amazing_q4 | amazing1, amazing_q1, note_measure |
| C18 | carpet | circ_do1, wheels_q1 | compass, note_compass, wheels_q0 |
| C19 | puzzle1 | | puzzle2, puzzle3, puzzle4 |
| C20 | | | cards |
| C21 | | | try1_text, try1a, try1b, try1c, try1d |
| C22 | | | try2, try3, try4 |
| C23 | | | try5 |
| C24 | | try6, try8, try9 | try6_q, try7a, try7b, try8_q |

**A4. Per-lesson load of book QUESTIONS (example, exercise, prompt) if the unmentioned parts are folded into the nearest of the 8 tools. A suggestion, not a decision.** Ids are listed so you can move any. `*` marks the non-question items (text or talk) that go with the tool.

| Lesson | Q | Status of the Q (Y / P / N) | Questions | Text and talk (not counted) |
|---|---|---|---|---|
| L1 | **20** | 2 / 5 / 13 | model1, model_q1 to q5, project1, qutub_q1 to q3, bricks_q, border1 to border4, puzzle1 to puzzle4, cards | opening, model_talk, qutub_say, qutub_fact, bricks_text, note_boxes |
| L2 | **13** | 7 / 0 / 6 | craft1, prism_q1 to q3, pyr_q1 to q3, cube_prism, sort1, sort2, sort3, sort3_q, sort4 | prism_pyr_talk, note_venn |
| L3 | **4** | 2 / 1 / 1 | craft2, solids_q3, solids_q4, solids_q5 | net_text |
| L4 | **11** | 0 / 3 / 8 | craft3, fve, sort_faces, three_faces, sort_edges, observe1 to observe3, border5, solids_q1, try5 | solids_q2 |
| L5 | **3** | 1 / 2 / 0 | build1, towers, dotcubes | none |
| L6 | **24** | 0 / 8 / 16 | house_ex, boat_q, angles_do1, angles_do2, right_make, right_circle, right_objects, right_do1, acute_obj, obtuse_obj, letters, ao_do1a, ao_do1b, ao_do2, dotshapes, dotshapes_q, fourside_q, try6, try6_q, try7a, try7b, try8, try8_q, try9 | angle_text, yoga_text, acute_text, note_square |
| L7 | **17** | 2 / 4 / 11 | pentagon_make, pentagon_q1 to q3, circle_straws, circle_straws_q1, q2, make_circle, make_circle_q, amazing1, amazing_q1, amazing_q4, circ_do1, compass, carpet, wheels_q0, wheels_q1 | centre_text, amazing_t2, amazing_t3, amazing_t5, note_measure, note_compass |
| L8 | **17** | 5 / 3 / 9 | straw_tri_make, straw_tri_push, straw_tri_trace, straw_tri_angles, straw_rect_make, straw_rect_angles, straw_rect_push, straw_rect_after, straw_square, straw_compare, try1a to try1d, try2, try3, try4 | note_rigid, try1_text |
| **Total** | **109** | 19 / 26 / 64 | | 22 (5 talk + 17 text) |

**Arithmetic, said plainly.** 109 questions over 8 tools is about 13.6 per tool; the pipeline's default cap is 6 per tool, so **only L3 (4) and L5 (3) are under it and six of the eight tools are over**. Even a perfect spread would need 109/8 = 13.6 per tool. 8 tools × 6 = 48 questions fit under the cap; **61 do not**, however they are spread. The other ways to cut the load are: (a) raise `max_tool_questions` in chapter.config.json (needs your say-so); (b) count each multi-part box as one stage and use fewer, longer stages (the config counts questions, so this needs a rule); (c) **Option B:** send C14 and C24 (10 questions: dotshapes, dotshapes_q, fourside_q, try6, try6_q, try7a, try7b, try8, try8_q, try9) to the Lesson 9 worksheet, which gives L6 = 14 and L9 = 10; (d) also send the cut and path puzzles (puzzle2 to 4, try1a to d, try2 to 4: 10 questions) to Lesson 9, which gives L1 = 17, L8 = 10, L9 = 20.

### 8B. What the plan has that the book does not

| In the plan | In the book (checked) |
|---|---|
| **Degrees** (45°, 90°, 120°, 30°, 110°, 150°, "smaller than 180°", "show the angle measurement", the assessment's "smaller than 90°") | **None.** 0 occurrences of "°" or "degree". Acute and obtuse are defined only against a right angle (p12). (The user removed degrees.) |
| **"Vertex"** (Label the Cube, "Corner (Vertex)", assessment Q4) | **Never printed.** The book says "corner(s)" and uses the letter V ("Number of corners (V)", p4). |
| **"Regular / irregular pentagon", "equal angles"** | Not printed. The book has only "5-sided shape with all sides equal (Pentagon)" and then asks what happens to the angles when pushed (p16). |
| **Hexagonal prism 8-18-12; pentagonal pyramid** | Both are **drawn** (p3 pictures; the end-of-book net pages; the pentagonal pyramid also in p9 Q5 option d) but **no counts are given** for either. The "8 flat faces" column on p4 is the only hint. |
| **Triangular prism 5-9-6; square pyramid 5-8-5; triangular pyramid 4-6-4; cube and cuboid 6-12-8** | Counts appear only in descriptions (p8 Q1 a, e, f) and in the blank table (p4) and the straw model challenge (p22 Q5). The triangular pyramid's 4-6-4 is asked (table row) but not stated. |
| **"A cube is a special type of square prism"** | **Implied, not stated:** p3 asks "Is a cube also a prism?" (no answer) and the p4 table row reads "Cube/Square Prism" (and "Cuboid/Rectangular Prism"). |
| **"Base" and "apex"** | "base" appears only for a building ("roof, pillars, base", p1). "apex" never. p3 asks "All the triangular faces meet at ___ point." and "What other shapes do these prisms have?". |
| **2D vs 3D wording** | "3D shape(s)" appears 5 times (p4, p6) and "2D shape(s)" 3 times (p20, p23). **Neither is defined.** The plan's objective 2 has no lesson of its own. |
| **Partly hidden cubes** ("count all the cubes, including the partially hidden ones", four multiple-choice answers) | The book's towers (p7) need hidden cubes to be counted (tower 1: 30; tower 2: 66; see Appendix A) but it never says so. No multiple-choice. |
| **Timer, five seconds, points, a score** | None. |
| **True or False statements** (4) | None. Statement 3 is plainly false. Statement 4 mentions a **diagonal**: the word "diagonal" appears nowhere in the book. |
| **Radius and diameter sums in cm** (3, 10, 7, 6 cm) | **None.** No units anywhere (0 occurrences of "cm"); no sums. The book states only "half/double" (p18) and "Discuss the relationship" (p17). |
| **Assessment: 8 questions, 10 marks, 20 minutes** | None of the 8 is a book question. |
| **Monuments** ("India Gate, Qutub Minar and other buildings") | The book names India Gate, Qutub Minar, Safdarjung Tomb, Akshardham, the National Museum, Jantar Mantar, Sansad Bhawan (opener), and draws India Gate (drawing behind Diksha) and Qutub Minar (p2). The two other buildings drawn on p1 are unnamed. |
| **Hidden-shape picture of a city / playground** ("Shape City"), **30 seconds** | The book's nearest are the hidden-shapes outline picture (p19) and the border sketches (p5). No city picture; no time. |
| **Guess the Shape: three clues; chessboard** | No chessboard. The "I have ... faces" riddles of p8 Q1 and the angle-clue lines of p23 Q9 are the book's clue form. |
| **A net of a cube, "Six connected squares", "Six rectangles → Cuboid", "One square and four triangles → Square pyramid"** | **No cube net** in the 23 pages or the end pages. Cuboid nets appear (p9 Q3 (3), Q4 D); a square pyramid net is on the end pages. |
| **Build a cube from smaller unit cubes** | The book builds models A to D (none is a cube). |
| **Rigidity: "a diagonal", "two triangles", "more rigid"** | Rigidity appears only as a teacher note (p14). No diagonal task. The book asks the pushes (triangle, rectangle, square, pentagon). |
| **Sphere, cone, cylinder are absent** (the plan's solids are prisms, pyramids, cube, cuboid) | The book uses them (p5 to p9). |

### 8C. Errors or risks in the plan (checked for mathematical truth)

All checked against the plan's text, 6 Nov 2026.
1. **Counts: all TRUE.** Triangular prism 5, 9, 6 (5+6−9 = 2); hexagonal prism 8, 18, 12 (8+12−18 = 2); triangular pyramid 4, 6, 4 (2); square pyramid 5, 8, 5 (2); cube and cuboid 6, 12, 8 (2). (The pentagonal pyramid, not given in the plan, is 6, 10, 6, also 2.) Euler's rule F+V−E = 2 is **not in the plan**; the book asks for it (p4).
2. **FALSE or MISLEADING wording:** Lesson 2, triangular pyramid: "4 vertices meeting at the top apex". There are 4 vertices in all; only **one** is the apex, where the 3 side faces meet. Say "4 vertices; 3 edges meet at the apex".
3. **FALSE as a bare statement:** Lesson 3 "Six connected squares → Cube". Only certain 11 arrangements fold into a cube (a row of six or a 2×3 block does not). "Six rectangles → Cuboid" is also false in general (the book's own net A in p9 Q4 is six rectangles and does not fold, E1). "One square and four triangles → Square pyramid" is true only when the four triangles are joined to the four sides of the square. Show figures, not the sentences.
4. **Find the Wrong Net:** "Two nets will fold into the given solid, one will not" needs the wrong net to be truly invalid and the right ones valid; the book supplies no such set (E1: its nets A and C do not fold, B and D do). A cube has 11 nets, so a "wrong" net must be checked.
5. **"Face: a flat surface of a 3D shape"** conflicts with the book's "1 curved face" for a cone or cylinder (p8). Fine for prisms and pyramids; wrong for the solids the book folds in. Also "Edge: the line where two faces meet" fits the book's cone (1 edge: the circle). "Corner: where edges meet" does not describe the cone's apex (no edges meet there).
6. **Lesson 4 Spin the Shape "How many faces can you see now?"**: for an opaque cube or cuboid the answer is 1, 2 or 3, never more. TRUE and checkable; do not offer 4 or more.
7. **Lesson 6 definitions:** acute "smaller than a right angle, example 45°", right "equal to 90°, example: the corner of a square", obtuse "greater than 90° but smaller than 180°, example 120°": all TRUE. Angle Sorting set 30, 45, 90, 110, 120, 150: 30 and 45 acute, 90 right, 110, 120, 150 obtuse: TRUE. The book's own obtuse definition has no upper limit (E28). Degrees are removed by the user.
8. **Lesson 7 pentagon:** "a regular pentagon has five equal sides and five equal angles": TRUE. The user's decision (the book's "five sides, all equal") is an **equilateral** pentagon, and equal sides do NOT make equal angles: the book's own push test (p16) shows the angles change. "Irregular pentagon" is undefined in the plan (equal sides with unequal angles, or unequal sides?). Define it if it stays.
9. **Lesson 7 sums:** Radius 3 cm → diameter 6 cm; diameter 10 cm → radius 5 cm; radius 7 cm → diameter 14 cm; the assessment's radius 6 cm → diameter 12 cm: all TRUE. Units cm are new (the book has none); the numbers are the plan's own practice numbers.
10. **Lesson 8 statements:** "A triangle is a rigid shape" TRUE; "A rectangle can change its shape when pushed" TRUE; "A triangle has four sides" FALSE (correct answer False): TRUE as an answer key; "Adding a diagonal to a rectangular frame creates two triangles" TRUE, and the frame then cannot change shape. **Soft wording:** "a triangle's shape does not easily change if its side lengths remain fixed": with fixed sides a triangle cannot change at all. Say "cannot change". Also "rigid" is a word for the teacher only in the book (E29).
11. **Lesson 1 Guess the Shape:** "I have four equal sides. I have four corners." also fits a **rhombus** (four equal sides, four corners). The third clue ("A chessboard has many of my smaller forms": a chessboard is made of squares) decides it, so the answer Square is true but only with all three clues. The book does not name a rhombus (E12).
12. **Lesson 2 Challenge 3 "Build a cube using smaller unit cubes":** size unstated (8 or 27).
13. **Lesson 2 triangular pyramid "all faces are triangles":** TRUE. Prism: "two identical and parallel bases facing each other... side faces connect": TRUE. Square prism "four rectangular side faces": TRUE (a cube's are squares).
14. **Lesson 5:** "a structure with two cubes at the bottom and one on top" is 3 cubes (not 2+1 = 3 wrongly). TRUE; "a tower with three cubes" and "a structure with six cubes" are consistent. The four multiple-choice answers are plan-made.
15. **Assessment (10 marks):** Section A 1×3 = 3, Section B 1×3 = 3, Section C 2×2 = 4, total 10: TRUE. Answer key: Two; Acute; Pentagon; "A point where edges meet"; "A flat pattern that can be folded to form a 3D shape"; Diameter = 2 × Radius; 2 × 6 = 12 cm; 90° right; 120° obtuse: all TRUE. Q1 "two" fits any prism. Q3 uses "polygon" (not in the book). Q4 uses "vertex" (not in the book). Q2 and Q8 use degrees (user removed).
16. **Missing from the plan:** objective 2 (2D versus 3D) has no lesson; sphere, cone, cylinder; F+V−E; opposite and adjacent faces; sorting solids by faces and edges; the circle-making activities (see 8A).
17. **Wording that mixes 2D and 3D in Lesson 1:** "Which object looks like a triangle?" (2D word for an object); "an object with a pyramid-like structure" (3D). Fine for a picture hunt but unclear for a child.
18. The third-party image links in the plan are references only; none is copied.

### 8D. A first mapping of the plan's activities onto book items (not a decision)

| Plan activity | Book items that look like it |
|---|---|
| L1 questions ("shapes in India Gate", "why different shapes", "shapes in the picture") | model_q3, model_q2, model1; the border and hidden-shape pictures |
| L1A1 Shape Detective | border1 to border4 (objects with rectangular, triangular, curved faces, no corners); puzzle1 (hidden shapes); try1a, try1c (count triangles, rectangles in a figure) |
| L1A2 Guess the Shape (clues) | solids_q1 (clues "I have 5 faces..."), try9 (shape from clues), fourside_q, cards |
| L2 Prisms and Pyramids slides | prism_q1 to q3, pyr_q1 to q3, cube_prism, prism_pyr_talk |
| L2A1 Match the 3D Shape | craft2 (labelled solids), solids_q1 |
| L2A2 Build Your Own 3D Shape | craft2, craft1, build1, model1 (blocks) |
| L2A3 Prism or Pyramid | sort3, sort3_q, sort1, sort2, sort4, prism_pyr_talk |
| L3 intro and L3A1 Fold It | net_text, craft2, solids_q5 (pieces of a net) |
| L3A2 Which Net Makes Which Shape | solids_q3 |
| L3A3 Find the Wrong Net | solids_q4 (nets A and C do not fold; B and D do) |
| L4 intro, L4A1 Label the Cube | craft3 (columns F, V, E); the book has no printed definitions |
| L4A2 Count and Win | craft3, sort_faces, sort_edges, fve, solids_q1, try5 |
| L4A3 Spin the Shape (die) | observe1, observe2, observe3 |
| L5A1 Build a Cube Tower | build1 (models A to D) |
| L5A2 Look Carefully | towers (30 and 66) |
| L5A3 Copy the Cube Structure | build1, dotcubes |
| L6 intro and L6A1 Angle Builder | angle_text, right_make, right_do1, ao_do1a, ao_do1b |
| L6A2 Angle Sorting | right_circle, ao_do2, try6, try8, try9 |
| L6A3 Beat the Clock | none in the book (the timer is the plan's; the identifying is ao_do2, try8, try9) |
| L7 intro and L7A1 Circle Detective | make_circle, centre_text, amazing_t2, amazing_q4, carpet |
| L7A2 Radius or Diameter | circ_do1, amazing_t5, wheels_q1 |
| L7A3 Build a Pentagon | pentagon_make, pentagon_q1 to q3 |
| L8 intro and L8A1 Triangle vs Rectangle | straw_tri_make, straw_tri_push, straw_rect_make, straw_rect_push, straw_rect_after, straw_compare, note_rigid |
| L8A2 Build a Strong Structure | straw_square; matchsticks try2, try3, try4 (triangles from sticks); the book has no diagonal |
| L8A3 True or False | statements are the plan's; book basis: note_rigid, straw_tri_push, straw_rect_push |
| L9 revision, worksheet, assessment | no book items; the assessment questions are the plan's own |

## Appendix A. Checks of the printed figures (mine; the book prints no answers)

Needs the content team's or the user's sign-off before any plan uses them. "Measured" = pixel measurements on 300 to 600 dpi renders.

- **p7 tower 1 = 30.** Four layers: base 4 by 4 (4 cubes visible along the front and 4 along the side), 3 by 3, 2 by 2, 1 cube: 16+9+4+1. Same shape as model D (p7), different colours. Assumes solid layers.
- **p7 tower 2 = 66.** Two crossing staircase walls through one centre column of 6. Each of the four arms has columns of 5, 4, 3, 2, 1 cubes going out: 6 + 4×15 = 66. Evidence: the front-left and front-right arms show 1, 2, 3, 4, 5 stacked long faces (counted), one step outward moves the top by the same step in every arm, the back row of 11 tops is flat only if each back step drops by one cube, and a rendered voxel model of this shape matches the printed silhouette, all 21 top faces (1 centre + 20) and all stair positions. Assumes no gaps and no extra hidden cubes. (E26, E27)
- **p9 Q3:** (1) with (b), (2) with (d), (3) with (a), (4) with (c). (1) is a big triangle with the dotted middle triangle (a triangular pyramid net); (2) a rectangle with two circles (cylinder); (3) a strip of 4 rectangles with a flap on each side (cuboid); (4) 3 rectangles with a triangle on each end of the middle one (triangular prism). Solids: (a) purple cuboid, (b) blue triangular pyramid, (c) teal triangular prism, (d) green cylinder.
- **p9 Q4:** B and D fold into the solid below them; A and C do not (E1).
- **p9 Q5:** one pentagon and five triangles make a **pentagonal pyramid**, option d. Option c is a hexagonal pyramid (six-sided base); a is a square pyramid; b a triangular pyramid.
- **p8 Q1:** a) square pyramid; b) cone; c) sphere; d) cylinder; e) triangular prism; f) cube or cuboid (E5).
- **p5 Q1:** faces opposite to 2, 3, 4 are not given; the book's die shows only 5, 1, 3. **Q2:** a) faces 2, 3, 4 and 5; b) face 6 (opposite to 1). **Q3:** red is opposite **purple**; yellow is opposite **orange** (blue is opposite green); I checked every colouring of the cube against the three printed views, only this fits.
- **p4 F, V, E:** cube and cuboid 6, 8, 12; triangular pyramid 4, 4, 6; square pyramid 5, 5, 8; triangular prism 5, 6, 9. F+V−E = 2 in all five.
- **p10 boat:** 10 marks (E8); house 7.
- **p11 dot grid:** right angles are the top row 2nd and 3rd, and the bottom row 1st and 4th (E9).
- **p19 wheels:** longest radius and diameter B; shortest D (E16).
- **p19 Q1 hidden shapes:** circle, cylinder, one square, one tilted rectangle, two triangles (E17).
- **p19 Q2 (4 by 4 right triangle on the dot grid):** draw a line from the middle of the top leg straight down to the slanted side, and a line from the middle of the left leg straight across to the slanted side; they meet on the slanted side and make a 2-by-2 square in the right-angle corner and 2 small right triangles.
- **p19 Q3 (3 by 3 square):** pick a dot E on one side and join E to the two corners of the opposite side: 3 triangles.
- **p21 Q1:** a) 10 triangles; b) yes (all corners even; her printed numbers 1 to 12 trace one walk); c) 12 rectangles; d) a walk over every wall from A to B does not exist; if only "any walk" is asked, yes (E19).
- **p21 Q2:** a four-sided diamond of 4 sticks with one diagonal stick: 5 sticks, 2 triangles.
- **p22 Q3:** the 3 triangles touching at their base corners; call the base corners P0, P1, P2, P3 and the apexes a1, a2, a3. Move the base stick P2P3 and the right slanting stick a3P3 of the third triangle to lie along the top, one from a1 to a2 and one from a2 to a3. The 9 sticks then make 4 triangles (two upright, two upside-down), no more.
- **p22 Q4:** the figure has 13 sticks and 6 small triangles (upper left inverted, upper right upright, two upright below, one inverted between them, one inverted at the right) plus one big triangle of side 2. Remove the 4 sticks: the right slanting stick of the upper upright triangle, the horizontal stick under it, the left slanting stick of the lower-right upright triangle and its bottom stick. Exactly 3 triangles stay (upper-left, lower-left and right inverted), using the other 9 sticks. Other solutions exist (for example remove the same first two and the two sticks of the right-hand inverted triangle that are not shared).
- **p22 Q5:** a) cube or cuboid (12 edges, 8 corners); b) triangular prism (9, 6); c) pentagonal prism (15, 10; E21); d) pentagonal pyramid (10, 6). Straws are edges and clay balls are corners; F+V−E is 2 for each.
- **p22 Q6:** 3 angles: b, d, f; 4 angles: a, c, g; 5 angles: e. The number of sides equals the number of angles.
- **p23 Q8:** 4, 0, 1, 0, 0, 4; only the first and last have only right angles (E23).
- **p23 Q9:** E22 (shapes 2 and 7; 10; 3, 5, 8, 9, 11, 13; 4, 6, 12, 14).
- **End-of-book cards:** orange square, green oval, dark-brown quarter circle, light-green semicircle, cyan triangle, pink circle. The grouping "according to their sides" is open (for example 4 straight sides, 3 straight sides, curved or mixed).

## What I could not read or settle

- The QR code on the opener (not decoded).
- The straw-model photos beside the p4 table (too small to count edges from).
- The hidden-cube assumption behind 30 and 66 (the figures show only the outside).
- The unlettered pictures of p8 Q1 (which of the cube or cuboid f) means).
- Whether the author meant "same opposite faces" as I read it (E7).
- The plan's third-party images (references only; not opened or copied).


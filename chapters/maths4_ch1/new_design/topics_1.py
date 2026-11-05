# -*- coding: utf-8 -*-
"""Class 4, Chapter 1 "Shapes Around Us": the topic skeleton (step 3, the journey designer). Keys are final from here.

The flow follows tool_map.md row by row (46 rows): hook, Tool 1, then [concept video or image -> its tool] units in the order
of the table, then the review. The 22 tools are LOCKED exactly as proposed (tools_1.py); nothing here adds, drops, renames or
reorders one. QUESTION MAPPER (step 5): the 109 book questions are homed here as FIO(...) in `items` of the tool
concept (or of the image concept T2.C1, which no tool follows), each once; the 22 text and talk items stay in `ncert` of
the teaching concept that carries them. Three questions sit one tool away from the proposal ONLY because of the cap of 6
(PROVISIONAL, CLASH 30): cube_prism (Tool 2 to Tool 3), straw_rect_angles (Tool 13 to Tool 11), straw_compare (Tool 14
to Tool 19). Question map: question_map.md.

PROVISIONAL, CLASH 1: the whole table (22 tools, their order and the flow built on it) is the pipeline's PROPOSAL; the user
approves it at the structure stop. Every "PROVISIONAL, CLASH n" comment below marks a choice that follows the proposal's
recommended option of a clash that is still open. They are not decided.

PROVISIONAL, CLASH 2: 22 tools, 16 concept videos, 6 images, 4 modules, 46 rows (the size of the chapter).

MEDIA STEP (step 4, the media minimiser; the full table and the must-show / must-not-show lines are in media_decisions.md):
  No medium was added, dropped or moved: 1 hook + 16 concept videos, 6 main images, 0 pinned, 22 tools. Every tool after
  Tool 1 needs one video or image right before it (the flow gate), so the media count is already at its floor. What this
  step decided is the DETAIL inside each choice: each image shows real objects that are NOT the ones its tool uses (CLASH 20,
  21, 22, 29), seven video purposes were reworded so a video poses the question and the tool finds the answer (CLASH 25),
  and the open judgement calls are CLASH 20 to 29. No new_idea was changed.

Journey, by topic (module, then topic: units in order):
  M1 Solid Shapes
    T1  Diksha's Blocks in Delhi       hook video -> Tool 1
    T2  Bricks, Prisms and Pyramids    image (bricks and towers) ; video prisms and pyramids -> Tool 2
    T3  Parts of a Solid               video faces, corners, edges -> Tool 3 ; image die -> Tool 4
    T4  Sorting Solids                 image everyday objects -> Tool 5 ; video overlap -> Tool 6
    T5  Building with Cubes            image cube tower -> Tool 7
    T6  Naming a Solid from Clues      video guessing game -> Tool 8
    T7  Nets                           video nets -> Tool 9
  M2 Angles and Rigid Shapes
    T8  Angles                         video angles -> Tool 10
    T9  Right, Acute and Obtuse Angles video right angles -> Tool 11 ; video acute and obtuse -> Tool 12
    T10 Rigid Shapes                   video rigid shapes -> Tool 13 ; image folding gate -> Tool 14
    T11 Right Angles in Shapes         video shapes on a dot grid -> Tool 15
  M3 Circles and Flat Shapes
    T12 Making a Circle                video circle -> Tool 16
    T13 Diameter and Radius            video diameter -> Tool 17 ; image carpet and wheels -> Tool 18
    T14 Sides and Angles of Flat Shapes  video sides and angles -> Tool 19
  M4 Shape Puzzles
    T15 Puzzling Shapes                video hidden shapes -> Tool 20
    T16 Spider Webs                    video webs -> Tool 21
    T17 Matchstick Puzzles             video matchsticks -> Tool 22
  MLAST
    T18 Chapter Review                 two review concepts, nothing new

Why topics are grouped as they are: one idea per topic. A topic holds a second unit only when it builds on the first
(right angle, then acute and obtuse against it; faces, then opposite faces; the push test, then what it does to the angles;
a diameter, then radius and diameter in real things; a sorting rule, then the overlap). Where the ideas differ the units are
separate topics (cubes and riddles, the three puzzles). No topic has more than 4 concepts.

Rules for every string here: short plain sentences (Class 4: at most 16 words), no em or en dash, never "NCERT", "textbook",
"page N" or "Fig." (say "your maths book"), book characters and objects only (content.STORY). Teach lines, recaps, story
briefs, image briefs and tool specs are left to the brief writer.
"""
from __future__ import annotations

from topics_common import A, DOER, FIO, IMG, TOPIC, VID, WE  # noqa: F401

TOPICS = []

# ======================================================================================================================
# MODULE M1  SOLID SHAPES  (Tools 1 to 9)
# ======================================================================================================================

# ---- T1: the opening (hook video -> Tool 1, the exploration tool) -----------------------------------------------------
# PROVISIONAL, CLASH 9: Tool 1 carries six book questions (homed by the question mapper, step 5).
TOPICS.append(TOPIC(
    "T1", "M1", "Diksha's Blocks in Delhi", ["Chapter opener"], "Understand",
    "",   # the opening carries NO topic objective
    "Diksha returns from Delhi and starts to build India Gate. You pick blocks for the roof, pillars and base.",
    [A("T1.C1", "Diksha's Trip to Delhi", "Understand", "", role="hook",
       textbook=["Diksha wanted to go to a big city during her summer holidays. Her father took her to Delhi and they "
                 "visited many old and new interesting monuments like the India Gate, Qutub Minar, Safdarjung Tomb, "
                 "Akshardham, the National Museum, Jantar Mantar and Sansad Bhawan. Now she is trying to make a model of "
                 "India Gate using her wooden blocks."],
       ncert=["opening"], key_terms=[], minutes=4,
       video=VID("Diksha's Trip to Delhi",
                 "Diksha and her father visit the old and new buildings of Delhi, and she starts to model India Gate "
                 "with her wooden blocks. It shows the situation only and names no shape.")),
     DOER("T1.C2", "Blocks for Buildings", "blocks", "Understand", "",
          applies_to="T1.C1", role="explore",
          textbook=["Discussion: What would happen if you removed one piece of your model? Would the model still look "
                    "like the original building? In what ways could you make the model even better?"],
          ncert=["ch1.model_talk"], minutes=8,
          # QUESTION MAPPER (step 5), CLASH 9: the six book questions of the opener, exactly the cap. The answers are in
          # everyday words (no solid is named yet) and every one is a Sample answer (the book prints none).
          items=[
              FIO("ch1.model1", "Opening, Task",
                  "Try to make a model of the buildings shown here using blocks.",
                  ["Look at the buildings on the screen.",
                   "Pick blocks for the roof, the pillars and the base.",
                   "Place the blocks to build your model."],
                  "Sample answer: a wide base, tall blocks for the pillars and a flat block on top. "
                  "Your answer may differ.", kind="exercise"),
              FIO("ch1.model_q1", "Opening, Q1",
                  "What parts of the building have you shown in your model (for example, roof, pillars, base, etc.)?",
                  ["Look at your model.", "Name each part you built."],
                  "Sample answer: the base, two pillars and the roof. Your answer may differ.", kind="prompt"),
              FIO("ch1.model_q2", "Opening, Q2",
                  "Why did you select these parts?",
                  ["Think about the parts you notice first in the building."],
                  "Sample answer: the base, pillars and roof are the parts you see first. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.model_q3", "Opening, Q3",
                  "What shapes will model these parts well?",
                  ["Look at the blocks you picked for each part."],
                  "Sample answer: a long flat block for the base. Tall blocks for the pillars. "
                  "A flat block for the roof. Your answer may differ.", kind="prompt"),
              FIO("ch1.model_q4", "Opening, Q4",
                  "How is your model similar to the picture of the real building?",
                  ["Put your model beside the picture and compare."],
                  "Sample answer: it has a base, pillars and a roof, just like the real building. "
                  "Your answer may differ.", kind="prompt"),
              FIO("ch1.model_q5", "Opening, Q5",
                  "How is it different from the real building?",
                  ["Look for what your model leaves out."],
                  "Sample answer: my model is smaller and its blocks have no windows or colours. "
                  "Your answer may differ.", kind="prompt"),
          ])],
    topic_type="framing"))

# ---- T2: bricks, prisms and pyramids (image -> video -> Tool 2) -----------------------------------------------------
# The image is the second half of C1. The opening topic must be exactly [hook, Tool 1], so the image opens this topic.
# PROVISIONAL, CLASH 8: the image holds six look-and-think or offline book items (homed by the question mapper, step 5).
# PROVISIONAL, CLASH 15: the image is a new real-life picture, not a redraw of the book's.
# PROVISIONAL, CLASH 13 (a): note_boxes (a teacher note) stays as a coverage ref only; the brief writer drops it.
# PROVISIONAL, CLASH 3 and CLASH 30: the proposal gave Tool 2 7 book questions against the cap of 6; ch1.cube_prism now sits
# on Tool 3 only because of the cap.
TOPICS.append(TOPIC(
    "T2", "M1", "Bricks, Prisms and Pyramids", ["Project Work", "Craft"], "Understand",
    "Students say what bricks have in common and name the face shapes that all prisms and all pyramids share.",
    "Look at the bricks of a tall tower. Then sort blocks into prisms and pyramids by their faces.",
    [A("T2.C1", "Bricks and the Qutub Minar", "Understand",
       "Students say what all bricks have in common and pick shapes to stack for a model of a tall tower.",
       role="image",
       textbook=["I have made something. Look at my Qutub Minar.",
                 "Do you know: The Qutub Minar is a World Heritage site and the tallest building made up of bricks. "
                 "It has 5 storeys and 379 stairs.",
                 "Earlier, people made buildings with clay bricks, stone blocks or wood. Today we also use concrete "
                 "blocks, hollow blocks, etc."],
       ncert=["ch1.qutub_say", "ch1.qutub_fact", "ch1.bricks_text", "ch1.note_boxes"],
       # QUESTION MAPPER (step 5), CLASH 8: no tool follows this image concept, so the gate allows its book items here
       # (flow_c34 _check_questions only bars them when a tool applies to the concept). Four look-and-think prompts and
       # two offline tasks. project1 is worded for the child (the printed "Encourage learners" is a teacher line,
       # CLASH 13 and CLASH 32).
       items=[
           FIO("ch1.qutub_q1", "Qutub Minar, Q1",
               "Do you think it looks like the Qutub Minar?",
               ["Look at the stack of boxes beside the tower."],
               "Sample answer: a little. Both get smaller towards the top. Your answer may differ.", kind="prompt"),
           FIO("ch1.qutub_q2", "Qutub Minar, Q2",
               "What shape would you use if you made a model of the Qutub Minar? Why?",
               ["Look at the tower in the picture."],
               "Sample answer: round shapes like cans, because the tower is round. Your answer may differ.",
               kind="prompt"),
           FIO("ch1.qutub_q3", "Qutub Minar, Q3",
               "How many such shapes will you use?",
               ["Think about the 5 storeys of the tower."],
               "Sample answer: 5, one for each storey. The tower has 5 storeys. Your answer may differ.",
               kind="prompt"),
           FIO("ch1.bricks_q", "Bricks",
               "What is common to all of these bricks?",
               ["Look at the clay brick, the stone block and the wooden block."],
               "From the picture: all of them are blocks with flat faces and straight edges. "
               "They have the same shape.", kind="prompt"),
           FIO("ch1.project1", "Project Work",
               "Observe a street carefully and make a model showing the main buildings on the street.",
               ["Look at a street, or at a picture of one.",
                "Note the main buildings.",
                "Make them with boxes, cans and blocks."],
               "Sample answer: a road with boxes for houses and round shapes for huts. Your answer may differ.",
               kind="exercise"),
           FIO("ch1.craft1", "Craft, Q1",
               "Make a sphere-like shape with paper strips.",
               ["Take paper strips of the same length.",
                "Join their ends at the top and at the bottom.",
                "Bend the strips outwards to make a ball."],
               "Sample answer: a ball of curved strips. They join at the top and at the bottom. "
               "Your answer may differ.", kind="exercise"),
       ],
       key_terms=["brick", "tower"], minutes=4,
       # MEDIA STEP, CLASH 29: one picture, three subjects (the tower, the stepped box model, the three blocks), because the
       # book's questions ask about all three. No label, no number, no count of storeys or boxes, no child, no hand.
       image=IMG("The Qutub Minar and Its Bricks",
                 "A real picture of the Qutub Minar, a small stepped stack of boxes beside it, and a clay brick, a "
                 "stone block and a wooden block, so the child can answer the look-and-think questions. It carries no "
                 "label, number or count.",
                 placement="main", new_context=False, style="photo",
                 visuals=["qutub_minar", "qutub_model", "bricks"])),
     A("T2.C2", "Prisms and Pyramids", "Understand",
       "Students say that solids can be sorted by the shapes of their faces into prisms and pyramids.",
       role="story",
       textbook=["What is the difference between a prism and a pyramid? Discuss."],
       ncert=["ch1.prism_pyr_talk"],
       key_terms=["prism", "pyramid", "face"], misconceptions=["M_SH_1", "M_SH_2"], minutes=5,
       video=VID("Diksha Sorts Her Blocks",
                 "Diksha sorts her blocks and boxes by their faces and meets the words prism and pyramid.",
                 new_idea="Solids can be sorted by their faces into two families, prisms and pyramids.")),
     DOER("T2.C3", "Prism or Pyramid", "prism_pyramid", "Apply",
          "Students name the face shape that all prisms share and the face shape that all pyramids share, and say if a "
          "cube is a prism.",
          applies_to="T2.C2", key_terms=["prism", "pyramid", "cube"], misconceptions=["M_SH_1", "M_SH_2"], minutes=8,
          # QUESTION MAPPER (step 5). PROVISIONAL, CLASH 30: the proposal homed 7 questions here against the cap of 6.
          # ch1.cube_prism ("Is a cube also a prism?") sits on Tool 3 ONLY because of the cap (CLASH 3, 30); under
          # option (b), cap 7, it comes back here as the last item of this list.
          items=[
              FIO("ch1.prism_q1", "Prisms, Q1",
                  "What shape of face is common to all the prisms?",
                  ["Tap the faces of the triangular, square and hexagonal prisms.",
                   "Look for the shape that every prism has."],
                  "From the picture: a rectangle. Every prism has rectangle faces.", kind="prompt"),
              FIO("ch1.prism_q2", "Prisms, Q2",
                  "What other shapes do these prisms have?",
                  ["Tap the faces that are not rectangles."],
                  "From the picture: the triangular prism has triangles. The square prism has squares. "
                  "The hexagonal prism has hexagons.", kind="prompt"),
              FIO("ch1.prism_q3", "Prisms, Q3",
                  "How many such faces each?",
                  ["Count the faces of the other shape on each prism.",
                   "Count the rectangle faces on each prism too."],
                  "From the picture: 2 of the other shape on each prism. The rectangle faces are 3, 4 and 6.",
                  kind="prompt"),
              FIO("ch1.pyr_q1", "Pyramids, Q1",
                  "What shape of face is common to all the pyramids?",
                  ["Tap the faces of the triangular, square and pentagonal pyramids.",
                   "Look for the shape that every pyramid has."],
                  "From the picture: a triangle. Every pyramid has triangle faces.", kind="prompt"),
              FIO("ch1.pyr_q2", "Pyramids, Q2",
                  "All the triangular faces meet at _________________ point.",
                  ["Look at where the triangle faces of a pyramid join."],
                  "From the picture: one point. The triangle faces meet at the top of the pyramid.", kind="prompt"),
              FIO("ch1.pyr_q3", "Pyramids, Q3",
                  "Identify any other shape in each of the pyramids",
                  ["Look at the face the pyramid stands on."],
                  "From the picture: the base. The triangular pyramid's base is a triangle. "
                  "The square pyramid's is a square. The pentagonal pyramid's is a pentagon.", kind="prompt"),
          ])],
    topic_type="instructional"))

# ---- T3: parts of a solid (video -> Tool 3, image -> Tool 4) --------------------------------------------------------
# PROVISIONAL, CLASH 7: Tool 4 follows an image, not a concept video.  PROVISIONAL, CLASH 15: the die picture is new.
# PROVISIONAL, CLASH 11: the book prints no answers (F+V-E, die opposites, colour cube): sign-off is open.
TOPICS.append(TOPIC(
    "T3", "M1", "Parts of a Solid", ["Craft", "Let Us Observe"], "Analyze",
    "Students count the faces, edges and corners of solids and find the face opposite a given face.",
    "Count the faces, corners and edges of solids. Then find the face opposite another face.",
    [A("T3.C1", "Counting the Parts of Solids", "Understand",
       "Students name and count the faces, edges and corners of a solid.",
       role="story",
       key_terms=["face", "corner", "edge"], misconceptions=["M_SH_3", "M_SH_4"], minutes=5,
       video=VID("Diksha Counts Straws and Clay",
                 "Diksha builds solids from straws and clay balls and counts their faces, corners and edges.",
                 new_idea="A solid has faces, corners and edges that can be counted.")),
     DOER("T3.C2", "Faces, Corners and Edges", "faces_edges", "Analyze",
          "Students count the parts of straw and clay solids, work out F+V−E for each and sort solids by flat faces "
          "and straight edges.",
          applies_to="T3.C1", key_terms=["flat face", "straight edge"], misconceptions=["M_SH_3", "M_SH_4"], minutes=7,
          # QUESTION MAPPER (step 5). The five proposed items plus ch1.cube_prism, last, which comes from Tool 2 ONLY
          # because of the cap of 6 (PROVISIONAL, CLASH 30). Why here: the table of craft3 has the row
          # "Cube/Square Prism". Under option (b), cap 7, cube_prism goes back to Tool 2 and this tool has 5.
          # E2, E3 (CLASH 11): the sorts of sort_faces and sort_edges do not fit every solid; the answers say so.
          items=[
              FIO("ch1.craft3", "Craft, Q3",
                  "Now try to make the above shapes using straws and plasticine/thread and fill in the table.",
                  ["Build each solid. Straws are the edges and clay balls are the corners.",
                   "Count the faces F, the corners V and the edges E of each solid.",
                   "Write the three counts in the table."],
                  "From the picture (F, V, E): cube 6, 8, 12. Cuboid 6, 8, 12. Triangular pyramid 4, 4, 6. "
                  "Square pyramid 5, 5, 8. Triangular prism 5, 6, 9.", kind="exercise"),
              FIO("ch1.fve", "Craft, F+V−E",
                  "Identify any relationship that you may find between the number of faces (F), edges (E), and "
                  "corners (V). Calculate F+V−E in each case. What do you notice?",
                  ["Cube: 6 + 8 − 12 = 2",
                   "Cuboid: 6 + 8 − 12 = 2",
                   "Triangular pyramid: 4 + 4 − 6 = 2",
                   "Square pyramid: 5 + 5 − 8 = 2",
                   "Triangular prism: 5 + 6 − 9 = 2"],
                  "From the picture: F+V−E is 2 for all five solids. So F + V is 2 more than E.", kind="prompt"),
              FIO("ch1.sort_faces", "Sorting by flat faces",
                  "Sort 3D shapes by the number of flat faces. Write their names here.",
                  ["Count the flat faces of each solid.",
                   "Drag the solid to its column."],
                  "Sample answer: 1: cone. 2: cylinder. 4: triangular pyramid. 5: square pyramid, triangular prism. "
                  "6: cube, cuboid, pentagonal pyramid. 8: hexagonal prism.", kind="exercise"),
              FIO("ch1.three_faces", "Sorting by flat faces, 3 faces",
                  "Can you construct a 3D shape with 3 flat faces?",
                  ["Try to build one on the screen."],
                  "Sample answer: a solid with only flat faces needs at least 4. A cylinder cut in half along its "
                  "length has 3 flat faces and 1 curved face.", kind="prompt"),
              FIO("ch1.sort_edges", "Sorting by straight edges",
                  "Now sort 3D shapes by the number of straight edges. Write their names here.",
                  ["Count the straight edges of each solid.",
                   "Drag the solid to its column."],
                  "Sample answer: 6: triangular pyramid. 8: square pyramid. 9: triangular prism. 12: cube and "
                  "cuboid. The pentagonal pyramid has 10 and the hexagonal prism 18, so they fit no column.",
                  kind="exercise"),
              FIO("ch1.cube_prism", "Craft, cube and prism",
                  "Is a cube also a prism?",
                  ["Look at the first row of the table."],
                  "Sample answer: yes. The table lists the cube as a square prism.", kind="prompt"),
          ]),
     A("T3.C3", "Faces of a Die", "Understand",
       "Students say that two faces of a die can be opposite each other or can meet at an edge.",
       role="image",
       key_terms=["opposite face", "die"], misconceptions=["M_SH_5"], minutes=4,
       # MEDIA STEP, CLASH 21: a real standard die with dots, faces 6, 4 and 5 in view (not the 1, 5, 3 of the book and the
       # tool), so the picture does not answer Let Us Observe 2. No label, no arrow, no second die, no hidden face shown.
       image=IMG("A Die on a Table",
                 "A real picture of a die at rest on a table with three faces in view, so the child meets the words "
                 "opposite and meets at an edge on a real object before turning the tool's die. Faces 6, 4 and 5 show, "
                 "so no answer of the tool is given away.",
                 placement="main", new_context=True, style="photo", visuals=["die"])),
     DOER("T3.C4", "Opposite Faces", "opposite", "Apply",
          "Students find the face opposite a given face and the faces that share an edge with it, on a die and a "
          "coloured cube.",
          applies_to="T3.C3", key_terms=["opposite face", "edge"], misconceptions=["M_SH_5"], minutes=5,
          # QUESTION MAPPER (step 5). E6 (CLASH 11): the die answers depend on the die; the tool's die is a usual die
          # (opposite faces add up to 7, VISUAL_KEY die), so the answer says "on a usual die".
          items=[
              FIO("ch1.observe1", "Let Us Observe, Q1",
                  "Take a die. Look at the face that has number 1. The face numbered 6 is opposite to the face "
                  "numbered 1. What is the face opposite to the a) face numbered 2? b) face numbered 3? "
                  "c) face numbered 4?",
                  ["Turn the die on the screen.",
                   "Find the face on the other side of 2, then of 3, then of 4.",
                   "2 + 5 = 7",
                   "3 + 4 = 7",
                   "4 + 3 = 7"],
                  "Sample answer: on a usual die, a) 5, b) 4, c) 3. Opposite faces add up to 7.", kind="prompt"),
              FIO("ch1.observe2", "Let Us Observe, Q2",
                  "a) Which faces have common edges with the face numbered 1? "
                  "b) Which face has no common edge with the face numbered 1?",
                  ["Turn the die so that 1 is on top.",
                   "Tap the faces that touch 1 along an edge."],
                  "From the picture: a) 2, 3, 4 and 5. b) 6, the face opposite 1.", kind="prompt"),
              FIO("ch1.observe3", "Let Us Observe, Q3",
                  "Look at three different views of the same cube. a) What colour is the face that is opposite to "
                  "the red face? b) What colour is the face that is opposite to the yellow face?",
                  ["Colours seen together in one view touch each other.",
                   "A face and the face opposite it are never seen together."],
                  "From the picture: a) purple. b) orange.", kind="prompt"),
          ])],
    topic_type="instructional"))

# ---- T4: sorting solids (image -> Tool 5, video -> Tool 6) ----------------------------------------------------------
# PROVISIONAL, CLASH 7 and CLASH 15: Tool 5 follows a new image of everyday objects.
# PROVISIONAL, CLASH 4: C5 is split between Tools 5 and 6.  PROVISIONAL, CLASH 12: E7, "same opposite faces" is unclear.
# PROVISIONAL, CLASH 13 (a): note_venn is a teacher note; the brief writer re-words its fact, no verbatim line here.
TOPICS.append(TOPIC(
    "T4", "M1", "Sorting Solids", ["Let Us Observe", "Sorting 3D Shapes"], "Analyze",
    "Students sort solids by their faces and edges, and place solids that fit two rules in the overlap of two circles.",
    "Mark faces on everyday objects. Then sort solids into circles and find solids that fit two rules.",
    [A("T4.C1", "Solids in Everyday Things", "Understand",
       "Students spot rectangular, triangular and curved faces on everyday objects.",
       role="image",
       key_terms=["rectangular face", "triangular face", "curved face"], misconceptions=["M_SH_3"], minutes=4,
       # MEDIA STEP, CLASH 20: the objects must NOT be the border objects the tool marks (die, eraser, ball, can, ice-cream
       # cone, party hat, cheese wedge, gift box). Different objects of the same kinds, no grouping, no mark, no label.
       image=IMG("Everyday Solids",
                 "A real picture of four to eight familiar objects that are not on the tool, for example a matchbox, a "
                 "round tin, a marble and a toy tent, so the child sees solids at home before marking the tool's "
                 "objects. They stand apart, with no group, mark or label.",
                 placement="main", new_context=True, style="photo", visuals=["everyday_objects"])),
     DOER("T4.C2", "Spot the Faces", "spot_faces", "Apply",
          "Students mark everyday objects that have a rectangular, triangular or curved face, or no corner.",
          applies_to="T4.C1", key_terms=["curved face", "corner"], misconceptions=["M_SH_3"], minutes=6,
          # QUESTION MAPPER (step 5). E7, CLASH 12 and CLASH 31: the book's border sketches are not numbered and no key
          # is printed. The answers name only the objects whose solid is certain (die, eraser, Rubik's cube, gift box,
          # wooden wedge, cake slice, balls, cans and bottles, cone, party hat). The two cheese pieces and the two
          # pyramid sketches are left out of the answers until the user decides what the screen draws (CLASH 31).
          # border5 waits for the user's reading of "same opposite faces" (CLASH 12).
          items=[
              FIO("ch1.border1", "Border, Q1",
                  "Follow these instructions for the shapes along the border. "
                  "Colour all shapes with a rectangular face in red.",
                  ["Look at each shape.",
                   "Colour it red if it has a rectangular face."],
                  "From the picture, for example: the dice, erasers and Rubik's cube. "
                  "The gift box, wooden wedge and cake slice too.", kind="exercise"),
              FIO("ch1.border2", "Border, Q2",
                  "Draw a smiley on shapes with a triangular face.",
                  ["Look at each shape.",
                   "Draw a smiley if it has a triangular face."],
                  "From the picture: for example the wooden wedge and the cake slice.", kind="exercise"),
              FIO("ch1.border3", "Border, Q3",
                  "Draw a star on shapes with a curved face.",
                  ["Look at each shape.",
                   "Draw a star if it has a curved face."],
                  "From the picture: the balls and the football. The cans and bottles. "
                  "The ice-cream cone and the party hat.", kind="exercise"),
              FIO("ch1.border4", "Border, Q4",
                  "Colour all shapes with no corner in blue.",
                  ["Look at each shape.",
                   "Colour it blue if it has no corner."],
                  "From the picture: the balls, the football, the cans and the bottles.", kind="exercise"),
              FIO("ch1.border5", "Border, Q5",
                  "Circle the shapes that have the same opposite faces.",
                  ["Look at each pair of opposite faces of a shape.",
                   "Circle the shape if the two faces of a pair look the same."],
                  "Sample answer: for example the dice, the erasers, the gift box and the Rubik's cube. "
                  "Your answer may differ.", kind="exercise"),
          ]),
     A("T4.C3", "Two Circles That Overlap", "Understand",
       "Students say why a solid that fits two rules belongs in the part where two circles overlap.",
       role="story",
       ncert=["ch1.note_venn"],
       key_terms=["overlap", "sort"], misconceptions=["M_SH_2"], minutes=5,
       video=VID("Diksha's Two Circles",
                 "Diksha sorts her blocks into two circles on her mat by a rule and finds a block that belongs in both.",
                 new_idea="A solid that fits both rules goes where the two circles overlap.")),
     DOER("T4.C4", "Sort the Solids", "sort_solids", "Analyze",
          "Students sort solids into two circles by a rule and place a solid that fits both rules in the overlap.",
          applies_to="T4.C3", key_terms=["overlap", "curved edge", "straight edge"], misconceptions=["M_SH_2"],
          minutes=6,
          # QUESTION MAPPER (step 5). E4, CLASH 11: "rectangular pyramid" is printed in sort3_q but never taught; the
          # sample answers name only taught solids. A sphere is a shaded ball; it has no edges (sort2).
          items=[
              FIO("ch1.sort1", "Sorting 3D Shapes, (1)",
                  "Write the names of 3D shapes in the correct places. A: All faces look the same. "
                  "B: All faces do not look the same.",
                  ["Look at the faces of each solid.",
                   "Drag the solid to circle A or circle B."],
                  "Sample answer: A: cube. B: cuboid, cylinder, cone, square pyramid, triangular prism. "
                  "Your answer may differ.", kind="exercise"),
              FIO("ch1.sort2", "Sorting 3D Shapes, (2)",
                  "A: Shapes with curved edges. B: Shapes with straight edges.",
                  ["Look at the edges of each solid.",
                   "Drag the solid to circle A or circle B."],
                  "Sample answer: A: cone, cylinder. B: cube, cuboid, square pyramid, triangular prism. "
                  "The sphere has no edges.", kind="exercise"),
              FIO("ch1.sort3", "Sorting 3D Shapes, (3)",
                  "A: Shapes with rectangular faces. B: Shapes with triangular faces. "
                  "The overlap: Shapes with both rectangular and triangular faces.",
                  ["Look at the faces of each solid.",
                   "Drag the solid to A, to B or to the overlap."],
                  "Sample answer: A: cube, cuboid, hexagonal prism. B: triangular pyramid. "
                  "Overlap: triangular prism, and a pyramid with a rectangle base. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.sort3_q", "Sorting 3D Shapes, circles",
                  "In which circle did you write triangular prism and rectangular pyramid?",
                  ["Look at the faces of both solids."],
                  "Sample answer: in the overlap of the two circles. Both solids have rectangle faces and "
                  "triangle faces.", kind="prompt"),
              FIO("ch1.sort4", "Sorting 3D Shapes, curved and flat",
                  "Let us sort shapes in another way. Using circles like the ones you just used, can you sort "
                  "shapes into the categories “Shapes with curved faces” and “Shapes with flat faces”?",
                  ["Look at the faces of each solid.",
                   "Drag it to curved, to flat or to the overlap."],
                  "Sample answer: curved only: sphere. Flat only: cube, cuboid, prisms, pyramids. "
                  "Both, in the overlap: cone, cylinder.", kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T5: building with cubes (image -> Tool 7) ----------------------------------------------------------------------
# PROVISIONAL, CLASH 7 and CLASH 15: Tool 7 follows a new image of a tower of toy cubes.
# PROVISIONAL, CLASH 4: Tool 7 carries C6 and C7.  PROVISIONAL, CLASH 18: the second tower of the book cannot be counted.
TOPICS.append(TOPIC(
    "T5", "M1", "Building with Cubes", ["Build with Cubes", "Cube Towers", "Drawing Cubes on a Triangular Dot Paper"],
    "Apply",
    "Students build cube models, count the cubes in a tower including hidden ones and draw cubes on triangular dot paper.",
    "Build models from cubes and count the cubes in a tower. Then draw cubes on dot paper.",
    [A("T5.C1", "A Tower of Cubes", "Understand",
       "Students say that a tower of cubes is built in layers and that some of its cubes are hidden from view.",
       role="image",
       key_terms=["cube", "layer"], misconceptions=["M_SH_6"], minutes=4,
       # MEDIA STEP, CLASH 20: a different tower from the book's two (the tool counts those), drawn clean so every cube has
       # clear edges, hence style illustration. No number, no layer line, no see-through or pulled-apart view.
       image=IMG("A Tower of Toy Cubes",
                 "A clean picture of a small tower of plain toy cubes stacked in layers, a different tower from the "
                 "two the tool counts, so the child meets cubes in layers before counting any. It does not show or "
                 "count the hidden cubes.",
                 placement="main", new_context=True, style="illustration", visuals=["toy_cube_tower"])),
     DOER("T5.C2", "Build and Draw Cubes", "cubes", "Apply",
          "Students build cube models, count the cubes in a tower including the hidden ones and complete cube "
          "drawings on triangular dot paper.",
          applies_to="T5.C1", key_terms=["cube", "layer", "hidden cube"], misconceptions=["M_SH_6"], minutes=6,
          # QUESTION MAPPER (step 5), CLASH 18: the first tower is 4 layers of 1, 4, 9 and 16 cubes (checked on the page
          # at 14x; 1 + 4 + 9 + 16 = 30). The second tower (the large X) cannot be counted from print, so the answer
          # gives it NO number and says how to find it.
          items=[
              FIO("ch1.build1", "Build with Cubes",
                  "Build these models with the cubes from the Jaadui Pitara Kit or any other similar material.",
                  ["Look at the models A, B, C and D.",
                   "Place cubes on the screen to copy each model.",
                   "Turn the model round to check it."],
                  "From the picture: each model you build looks like its picture when you turn it round.",
                  kind="exercise"),
              FIO("ch1.towers", "Cube Towers",
                  "How many cubes are there in each of these cube towers?",
                  ["Count layer by layer from the top. Count the hidden cubes too.",
                   "First tower, top layer: 1 cube",
                   "First tower, second layer: 2 + 2 = 4 cubes",
                   "First tower, third layer: 3 + 3 + 3 = 9 cubes",
                   "First tower, bottom layer: 4 + 4 + 4 + 4 = 16 cubes",
                   "1 + 4 + 9 + 16 = 30"],
                  "From the picture: the first tower has 30 cubes. Count the second tower layer by layer "
                  "on the screen.", kind="prompt"),
              FIO("ch1.dotcubes", "Drawing Cubes on a Triangular Dot Paper",
                  "Can you complete the following cubes?",
                  ["Look at the finished cube.",
                   "Join the dots with straight lines to finish each cube like it."],
                  "From the picture: each finished cube looks like the first one. "
                  "It has 3 diamond faces that meet at one corner.", kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T6: naming a solid from clues (puzzle story video -> Tool 8) ---------------------------------------------------
# PROVISIONAL, CLASH 4 and CLASH 6: Tool 8 carries C8 and C23 (the model challenge moved up from the end of the chapter).
# PROVISIONAL, CLASH 14: a puzzle told as a story, solved on the tool.  PROVISIONAL, CLASH 12: E5 and E21 (clue f fits two
# solids; part c is a pentagonal prism the chapter never shows).
TOPICS.append(TOPIC(
    "T6", "M1", "Naming a Solid from Clues", ["Name the solid", "Model challenge"], "Apply",
    "Students name a solid from clues about its faces, edges and corners, or from the straws and clay balls it needs.",
    "Diksha and her father give clues about a solid. You work out which solid it is.",
    [A("T6.C1", "Guess My Solid", "Understand",
       "Students use the numbers of faces, edges and corners of a solid to say which solid it is.",
       role="story",
       textbook=["Each one is different. How? Discuss."],
       ncert=["ch1.solids_q2"],
       key_terms=["face", "edge", "corner"], misconceptions=["M_SH_4"], minutes=5,
       video=VID("Guess My Solid",
                 "Diksha and her father play a guessing game with clues about faces, corners and edges, and about "
                 "straws and clay balls.",
                 new_idea="The numbers of faces, edges and corners of a solid can tell you which solid it is.")),
     DOER("T6.C2", "Solid Riddles", "riddles", "Apply",
          "Students pick or build the solid that fits clues about its faces, edges and corners, or about its straws "
          "and clay balls.",
          applies_to="T6.C1", key_terms=["face", "edge", "corner"], misconceptions=["M_SH_4"], minutes=6,
          # QUESTION MAPPER (step 5), CLASH 6 (try5 moved up from the end of the chapter) and CLASH 12: E5 (clue f fits a
          # cube and a cuboid) and E21 (part c is a solid the chapter never shows: the answer describes it by its parts
          # and does not give it a name).
          items=[
              FIO("ch1.solids_q1", "Solids, Q1",
                  "Match the pictures to the descriptions and name the shapes. "
                  "a) I have 5 faces and 5 corners. I have 8 edges. 1 of my faces is a square and 4 of my faces "
                  "are triangles. "
                  "b) I have 1 flat face, 1 curved face, and 1 edge. "
                  "c) I have 1 curved face. I have no edges or corners. "
                  "d) I have 2 flat faces, 1 curved face, and 2 edges. I have no corners. "
                  "e) I have 5 faces, 6 corners, and 9 edges, and 2 of my faces are triangles. "
                  "f) I have 6 faces, 12 edges, and 8 corners.",
                  ["Read one clue at a time.",
                   "Match it with a solid on the screen.",
                   "Name the solid."],
                  "From the picture: a) square pyramid. b) cone. c) sphere. d) cylinder. e) triangular prism. "
                  "f) cube or cuboid, because both fit.", kind="exercise"),
              FIO("ch1.try5", "Model challenge",
                  "Can you make a model of solid shapes which has a) 12 straws and 8 clay balls? "
                  "b) 9 straws and 6 clay balls? c) 15 straws and 10 clay balls? d) 10 straws and 6 clay balls?",
                  ["Straws are the edges and clay balls are the corners.",
                   "Build a solid for each count and check it.",
                   "c) Two 5-sided ends use 5 + 5 = 10 straws. 5 more straws join them: 10 + 5 = 15.",
                   "c) Each end has 5 corners: 5 + 5 = 10 balls.",
                   "d) A base of 5 straws and 5 slanting straws: 5 + 5 = 10. Balls: 5 + 1 = 6."],
                  "Sample answer: a) a cube or a cuboid. b) a triangular prism. c) a solid with two 5-sided ends. "
                  "d) a pentagonal pyramid.", kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T7: nets (video -> Tool 9) -------------------------------------------------------------------------------------
# PROVISIONAL, CLASH 5: nets are taught here, not next to the prisms and pyramids where the book first shows one.
# PROVISIONAL, CLASH 4 and CLASH 10: Tool 9 also takes Craft 2, which uses the nets at the end of the book.
# PROVISIONAL, CLASH 12: E1, nets A and C of the book's question do not fold.
TOPICS.append(TOPIC(
    "T7", "M1", "Nets", ["Craft"], "Apply",
    "Students match nets to solids and decide which nets fold into a given solid.",
    "Open a box flat to see its net. Then fold nets to find which ones make solids.",
    [A("T7.C1", "Nets of Solids", "Understand",
       "Students explain that a net is a solid opened out flat and that it folds back into the solid.",
       role="story",
       textbook=["Diksha has folded open and flattened a box to see what an open box looks like. This is called the "
                 "net of the box. If you fold along the dotted lines, you will get the box back."],
       ncert=["ch1.net_text"],
       key_terms=["net", "fold"], misconceptions=["M_SH_7"], minutes=5,
       video=VID("Diksha Opens a Box",
                 "Diksha opens a box flat to see its net, and Nitesh cuts a net on its folds.",
                 new_idea="A net is a solid opened out flat, and it folds back into the solid.")),
     DOER("T7.C2", "Fold the Net", "fold_net", "Apply",
          "Students match nets to solids, test which nets fold into a given solid and find the solid from the pieces "
          "of its net.",
          applies_to="T7.C1", key_terms=["net", "fold"], misconceptions=["M_SH_7"], minutes=6,
          # QUESTION MAPPER (step 5), CLASH 5 and CLASH 10: craft2 (printed before the prisms' questions) is homed here with
          # the nets; the nets are on the screen. E1 (CLASH 12): nets A and C of solids_q4 do not fold; the answer says so
          # and lets the child test it. E24: the end-of-book net page has no net named "Square Prism".
          items=[
              FIO("ch1.craft2", "Craft, Q2",
                  "Use the nets given at the end of the book to make the models shown below.",
                  ["The nets are on the screen.",
                   "Fold each net along its dotted lines.",
                   "Match each net to its solid: three prisms and three pyramids."],
                  "Sample answer: each net folds into the solid shown beside it. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.solids_q3", "Solids and nets, Q3",
                  "Match the following nets to the appropriate solids given below.",
                  ["Look at the faces of each net.",
                   "Drag each net to the solid it folds into."],
                  "From the picture: (1) with (b), (2) with (d), (3) with (a), (4) with (c).", kind="exercise"),
              FIO("ch1.solids_q4", "Solids and nets, Q4",
                  "Which of these nets can be folded to make a solid of the kind given below?",
                  ["Fold each net on the screen.",
                   "See if it closes into the solid below it."],
                  "From the picture: B and D fold into the solid below. A and C do not. Fold each one to check.",
                  kind="exercise"),
              FIO("ch1.solids_q5", "Solids and nets, Q5",
                  "Nitesh cuts up a net on the folds. Here are its pieces. "
                  "Which solid has the above pieces in its net?",
                  ["Count the pieces: 1 pentagon and 5 triangles.",
                   "Find the solid with a pentagon and 5 triangles."],
                  "From the picture: d, the pentagonal pyramid. It has 1 pentagon and 5 triangles.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ======================================================================================================================
# MODULE M2  ANGLES AND RIGID SHAPES  (Tools 10 to 15)
# ======================================================================================================================

# ---- T8: angles (video -> Tool 10) ----------------------------------------------------------------------------------
TOPICS.append(TOPIC(
    "T8", "M2", "Angles", ["When Lines Meet"], "Understand",
    "Students make an angle from two lines that meet at a point, and mark and count angles in pictures.",
    "Two lines that meet at a point make an angle. You find angles in pictures.",
    [A("T8.C1", "Where Two Lines Meet", "Understand",
       "Students say that two lines meeting at a point make an angle and find angles in everyday pictures.",
       role="story",
       textbook=["Isha made different corners with straws. We can say that the two straws are like two lines that meet "
                 "at a point. When two lines meet they create an angle.",
                 "We see many angles in yoga postures."],
       ncert=["ch1.angle_text", "ch1.yoga_text"],
       key_terms=["angle", "line"], misconceptions=["M_AN_1", "M_AN_2"], minutes=5,
       # MEDIA STEP, CLASH 25: no house and no boat here (Tool 10 holds that example and that question).
       video=VID("Isha's Straw Corners",
                 "Isha meets two straws at a point and sees angles in yoga postures. The house and the boat are left "
                 "to the tool.",
                 new_idea="Two lines that meet at a point make an angle.")),
     DOER("T8.C2", "When Lines Meet", "lines_meet", "Apply",
          "Students make an angle by meeting two straws at a point, then mark and count the angles in pictures.",
          applies_to="T8.C1", key_terms=["angle"], misconceptions=["M_AN_1", "M_AN_2"], minutes=6,
          # QUESTION MAPPER (step 5). E8 (CLASH 11): the boat count is the number of printed marks, 10. angles_do2 asks
          # for angles in the classroom; it sits on the classroom picture of this tool (CLASH 16).
          items=[
              FIO("ch1.house_ex", "Example",
                  "There are 7 angles in this house drawing.",
                  ["1 angle at the top of the roof.",
                   "2 angles at the lower corners of the roof.",
                   "2 right angles at the top of the walls.",
                   "2 right angles at the bottom of the walls.",
                   "1 + 2 + 2 + 2 = 7"],
                  "From the picture: 7 angles.", kind="example"),
              FIO("ch1.boat_q", "When Lines Meet",
                  "How many angles are there in this boat drawing?",
                  ["4 angles in the body of the boat.",
                   "2 angles at the top of the sail, one on each side of the mast.",
                   "2 angles at the lower corners of the sail.",
                   "2 right angles where the mast meets the sail.",
                   "4 + 2 + 2 + 2 = 10"],
                  "From the picture: 10 marked angles.", kind="prompt"),
              FIO("ch1.angles_do1", "Let Us Do, Q1",
                  "Mark the angles in the following pictures. a) b) c) d) e)",
                  ["Look at each picture.",
                   "Tap the places where two lines meet."],
                  "Sample answer: scissors, where the two blades meet. Hanger, at its lower corners. "
                  "Hand, where the two fingers meet. Seesaw, where the plank meets the stand. "
                  "Slide, where it meets the ground. Your answer may differ.", kind="exercise"),
              FIO("ch1.angles_do2", "Let Us Do, Q2",
                  "Where do you see angles in the classroom? Give a few examples.",
                  ["Look at the classroom on the screen.",
                   "Find places where two lines meet."],
                  "Sample answer: the corner of the desk and of the blackboard. The hands of the clock. "
                  "The door. Your answer may differ.", kind="prompt"),
          ])],
    topic_type="instructional"))

# ---- T9: right, acute and obtuse angles (video -> Tool 11, video -> Tool 12) ----------------------------------------
# PROVISIONAL, CLASH 16: the paper folding is shown on the screen.  PROVISIONAL, CLASH 12: E9, E10 (figures read by
# measure, no key).
TOPICS.append(TOPIC(
    "T9", "M2", "Right, Acute and Obtuse Angles", ["Right Angles", "Acute and Obtuse Angles"], "Apply",
    "Students make a right angle from folded paper and use it to tell right, acute and obtuse angles apart.",
    "Fold paper to make a right angle. Then use it to tell right, acute and obtuse angles apart.",
    [A("T9.C1", "Right Angles", "Understand",
       "Students make a right angle by folding paper twice and use it to find right angles in objects and drawings.",
       role="story",
       key_terms=["right angle", "right angle checker"], misconceptions=["M_AN_3"], minutes=5,
       video=VID("Diksha Folds a Paper Corner",
                 "Diksha folds a paper twice to make a right angle checker and tests corners with it.",
                 new_idea="A right angle can be made by folding paper twice and used to check other corners.")),
     DOER("T9.C2", "Right Angle Checker", "right_checker", "Apply",
          "Students test the corners of shapes and objects with a paper right angle and draw right angles on a dot grid.",
          applies_to="T9.C1", key_terms=["right angle"], misconceptions=["M_AN_3"], minutes=6,
          # QUESTION MAPPER (step 5). E9 (CLASH 12): the right angles of the dot grid are read by measure; no key is printed.
          # ch1.straw_rect_angles comes from Tool 13 ONLY because of the cap of 6 (PROVISIONAL, CLASH 30): "What kinds of
          # angles do you see in the rectangle?" is answered by testing the rectangle's corners with the checker. Under
          # option (b), cap 7, it goes back to Tool 13 and this tool has 4.
          items=[
              FIO("ch1.right_make", "Right Angles",
                  "Let's make a right angle with a piece of paper as shown.",
                  ["Fold the paper in half.",
                   "Fold it in half again, so the first fold lies on itself.",
                   "The corner where the folds meet is a right angle."],
                  "From the picture: the corner where the folds meet is a right angle. A red square marks it.",
                  kind="exercise"),
              FIO("ch1.right_circle", "Right Angles, dot grid",
                  "Identify the angles that you think are right angles and circle them in the dot grid given below. "
                  "Check using your right angle checker.",
                  ["Look at the eight angles on the dot grid.",
                   "Circle the ones you think are right angles.",
                   "Lay your right angle checker on each corner to check."],
                  "From the picture: the 2nd and 3rd angles in the top row. The 1st and 4th in the bottom row. "
                  "Check each with your checker.", kind="exercise"),
              FIO("ch1.right_objects", "Right Angles, objects",
                  "Check for right angles in a book, window, and any other object. "
                  "Write the names of objects where you find right angles.",
                  ["Lay your right angle checker on a corner of the book.",
                   "Do the same for the window and other objects."],
                  "Sample answer: the corner of a book, a window frame, a door and a desk top. "
                  "Your answer may differ.", kind="exercise"),
              FIO("ch1.right_do1", "Let Us Do, Q1",
                  "Draw some right angles on the dot grid.",
                  ["Draw a line across the dots.",
                   "Draw a second line from its end, straight up or down."],
                  "Sample answer: a line across and a line straight up from its end. "
                  "A turned square corner works too. Your answer may differ.", kind="exercise"),
              FIO("ch1.straw_rect_angles", "Shapes with Straws, rectangle angles",
                  "What kinds of angles do you see in the rectangle?",
                  ["Lay your right angle checker on each corner of the straw rectangle."],
                  "From the picture: all four angles are right angles.", kind="prompt"),
          ]),
     A("T9.C3", "Acute and Obtuse Angles", "Understand",
       "Students compare an angle with a right angle and say whether it is acute, right or obtuse.",
       role="story",
       textbook=["Acute angles are less than a right angle. Obtuse angles are more than a right angle."],
       ncert=["ch1.acute_text"],
       key_terms=["acute angle", "obtuse angle"], misconceptions=["M_AN_4"], minutes=5,
       video=VID("Isha Checks More Corners",
                 "Isha puts the right angle checker on corners and finds some smaller and some bigger.",
                 new_idea="An acute angle is less than a right angle and an obtuse angle is more than a right angle.")),
     DOER("T9.C4", "Acute or Obtuse", "acute_obtuse", "Apply",
          "Students swing a line against a right angle to tell acute angles from obtuse angles, then draw and mark "
          "both kinds.",
          applies_to="T9.C3", key_terms=["acute angle", "obtuse angle"], misconceptions=["M_AN_4"], minutes=7,
          # QUESTION MAPPER (step 5). E10 (CLASH 11): how many angles to mark in V, A, Z and in the stick figures is not
          # stated, so those two answers give the method and no count. acute_obj and obtuse_obj sit on the classroom picture.
          items=[
              FIO("ch1.acute_obj", "Acute and Obtuse Angles, acute",
                  "Name some objects from your classroom which have an acute angle.",
                  ["Look at the classroom on the screen.",
                   "Compare each corner with a right angle."],
                  "Sample answer: the hands of a clock at 2 o'clock. A door opened a little. "
                  "The tip of a pencil. Your answer may differ.", kind="prompt"),
              FIO("ch1.obtuse_obj", "Acute and Obtuse Angles, obtuse",
                  "Name some objects from your classroom which have an obtuse angle.",
                  ["Look at the classroom on the screen.",
                   "Compare each corner with a right angle."],
                  "Sample answer: the hands of a clock at 4 o'clock and a door opened wide. "
                  "Your answer may differ.", kind="prompt"),
              FIO("ch1.letters", "Acute and Obtuse Angles, letters",
                  "Identify all angles in the following letters.",
                  ["Look at the letters V, A and Z.",
                   "Find each place where two strokes meet."],
                  "Sample answer: V has 1 acute angle. Z has 2 acute angles. A has an acute angle at the top. "
                  "It has angles where the bar meets the legs. Your answer may differ.", kind="exercise"),
              FIO("ch1.ao_do1a", "Let Us Do, Q1 (acute)",
                  "Draw some acute angles on the top grid. Draw a line to make an acute angle using each given "
                  "line in the bottom grid.",
                  ["Start from one end of a line.",
                   "Draw a second line that leans in, closer than a right angle."],
                  "Sample answer: from one end of the line, draw a slanting line. "
                  "Make the angle less than a right angle. Your answer may differ.", kind="exercise"),
              FIO("ch1.ao_do1b", "Let Us Do, Q1 (obtuse)",
                  "Draw some obtuse angles on the top grid. Draw a line to make an obtuse angle using each given "
                  "line in the bottom grid.",
                  ["Start from one end of a line.",
                   "Draw a second line that leans out, wider than a right angle."],
                  "Sample answer: from one end of the line, draw a slanting line. "
                  "Make the angle more than a right angle. Your answer may differ.", kind="exercise"),
              FIO("ch1.ao_do2", "Let Us Do, Q2",
                  "In the figures given below, mark the acute angles in red, right angles in green, and obtuse "
                  "angles in blue.",
                  ["Find each place where two lines of a figure meet.",
                   "Compare the angle with a right angle."],
                  "Sample answer: red if smaller than a right angle. Green if the same. Blue if bigger. "
                  "Your answer may differ.", kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T10: rigid shapes (video -> Tool 13, image -> Tool 14) ---------------------------------------------------------
# PROVISIONAL, CLASH 3 and CLASH 30: the proposal gave Tools 13 and 14 7 book questions each against the cap of 6; ch1.straw_rect_angles
# (to Tool 11) and ch1.straw_compare (to Tool 19) sit elsewhere only because of the cap.
# PROVISIONAL, CLASH 4 and CLASH 6: Tool 14 carries the second half of C13 and the pentagon (C15, printed before C14).
# PROVISIONAL, CLASH 7 and CLASH 15: Tool 14 follows a new image of a folding steel gate.
# PROVISIONAL, CLASH 13 (a): the only fact quoted from the teacher note is the rigid-shape sentence. It gives away what
# the push shows, so the brief writer uses it as the reveal after the push, not before.
# PROVISIONAL, CLASH 19: the word pentagon first appears on Tool 14 (no video or image of its own); option (a), keep.
# MEDIA STEP, CLASH 23: the media step also picks (a): no medium is added for the pentagon (the user may still choose c).
TOPICS.append(TOPIC(
    "T10", "M2", "Rigid Shapes", ["Shapes with Straws"], "Analyze",
    "Students say which straw shapes keep their shape when pushed and how the angles of a pushed rectangle, square and "
    "pentagon change.",
    "Push straw shapes and see which ones keep their shape. Then see how the angles change.",
    [A("T10.C1", "Rigid Shapes", "Understand",
       "Students say that a shape which keeps its shape when one side is pushed is called rigid.",
       role="story",
       textbook=["The triangle is the most rigid shape, as it does not change its shape when pushed."],
       ncert=["ch1.note_rigid"],
       key_terms=["rigid shape"], misconceptions=["M_AN_5"], minutes=5,
       # MEDIA STEP, CLASH 25: the video poses the question; the push and its result belong to Tool 13.
       video=VID("Isha Pushes Her Straw Shapes",
                 "Isha makes a triangle and a rectangle from straws and clay and wonders what happens if she gently "
                 "pushes one side of each. The push and its result are left to the tool.",
                 new_idea="A shape that keeps its shape when one side is pushed is called rigid.")),
     DOER("T10.C2", "Push the Straw Shapes", "push_straws", "Apply",
          "Students push one side of a straw triangle and a straw rectangle and say which one keeps its shape.",
          applies_to="T10.C1", key_terms=["rigid shape"], misconceptions=["M_AN_5"], minutes=8,
          # QUESTION MAPPER (step 5). PROVISIONAL, CLASH 30: the proposal homed 7 questions here against the cap of 6.
          # ch1.straw_rect_angles sits on Tool 11 ONLY because of the cap (CLASH 3, 30); under option (b), cap 7, it comes
          # back here between straw_rect_make and straw_rect_push. E11 (CLASH 11): the book prints no answer for the
          # push test; every answer is a Sample answer the child can test on the screen.
          items=[
              FIO("ch1.straw_tri_make", "Shapes with Straws, triangle",
                  "Make a triangle with straws of different sizes and clay/plasticine.",
                  ["Pick 3 straws of different lengths.",
                   "Join their ends with 3 clay balls."],
                  "Sample answer: 3 straws of different lengths joined at their ends make a triangle. "
                  "Your answer may differ.", kind="exercise"),
              FIO("ch1.straw_tri_push", "Shapes with Straws, triangle push",
                  "Does the shape of the triangle change if we gently push one of its sides? Yes/No",
                  ["Push one side of your triangle on the screen.",
                   "Watch if the shape changes."],
                  "Sample answer: No. The triangle keeps its shape.", kind="prompt"),
              FIO("ch1.straw_tri_trace", "Shapes with Straws, trace",
                  "Trace the triangles you made with the straws in your notebook.",
                  ["Draw round the triangle in your notebook.",
                   "Draw its three straight sides."],
                  "Sample answer: a triangle with 3 straight sides drawn in the notebook. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.straw_tri_angles", "Shapes with Straws, triangle angles",
                  "What kinds of angles does a triangle have?",
                  ["Compare each corner with a right angle."],
                  "Sample answer: every triangle has acute angles. One angle can be a right angle or an obtuse "
                  "angle. Your answer may differ.", kind="prompt"),
              FIO("ch1.straw_rect_make", "Shapes with Straws, rectangle",
                  "Make a rectangular shape with straws and clay.",
                  ["Pick 2 long straws and 2 short straws.",
                   "Join their ends with 4 clay balls."],
                  "Sample answer: 2 long and 2 short straws joined at 4 clay balls make a rectangle. "
                  "Your answer may differ.", kind="exercise"),
              FIO("ch1.straw_rect_push", "Shapes with Straws, rectangle push",
                  "Does the shape of the rectangle change if we gently push one of its sides? Yes/No",
                  ["Push one side of your rectangle on the screen.",
                   "Watch if the shape changes."],
                  "Sample answer: Yes. The rectangle leans over and changes its shape.", kind="prompt"),
          ]),
     A("T10.C3", "A Folding Gate", "Understand",
       "Students notice that the four-sided shapes of a folding gate lean over when it is pushed.",
       role="image",
       key_terms=["rigid shape"], misconceptions=["M_AN_5"], minutes=4,
       # MEDIA STEP, CLASH 22: shown half closed so the cells lean. A real gate's cells are pushed squares, so the picture
       # carries no angle mark, no label, no hand, no before and after pair, and never a five-sided frame (CLASH 23).
       image=IMG("A Folding Steel Gate",
                 "A real picture of a folding steel gate, half closed, whose four-sided cells lean over. It gives a "
                 "real use of a shape that does not hold its shape, and it carries no angle mark or label.",
                 placement="main", new_context=True, style="photo", visuals=["folding_gate"])),
     DOER("T10.C4", "Angles After the Push", "push_angles", "Analyze",
          "Students push a rectangle, a square and a pentagon and say how their angles change.",
          applies_to="T10.C3", key_terms=["pentagon", "angle"], misconceptions=["M_AN_5"], minutes=8,
          # QUESTION MAPPER (step 5). PROVISIONAL, CLASH 30: the proposal homed 7 questions here against the cap of 6.
          # ch1.straw_compare sits on Tool 19 ONLY because of the cap (CLASH 3, 30); under option (b), cap 7, it comes back
          # here as the third item, after straw_square. CLASH 19 and 23: the pentagon is named in pentagon_make.
          # E13: the missing question mark of pentagon_q2 is put in (CLASH 32).
          items=[
              FIO("ch1.straw_rect_after", "Shapes with Straws, after the push",
                  "What has happened to the angles of the new shape? Are they still right angles? "
                  "What types of angles have been formed?",
                  ["Look at the pushed rectangle.",
                   "Compare each corner with a right angle."],
                  "Sample answer: the angles have changed. They are not right angles now. "
                  "Two are acute and two are obtuse.", kind="prompt"),
              FIO("ch1.straw_square", "Shapes with Straws, square",
                  "Similarly, push one side of a square. Are they still right angles? "
                  "What types of angles have been formed?",
                  ["Push one side of the square on the screen.",
                   "Compare each corner with a right angle."],
                  "Sample answer: no. The pushed square leans over. Two angles are acute and two are obtuse.",
                  kind="prompt"),
              FIO("ch1.pentagon_make", "Shapes with Straws, pentagon",
                  "Try to make this 5-sided shape with all sides equal (Pentagon)",
                  ["Pick 5 straws of the same length.",
                   "Join their ends with 5 clay balls."],
                  "Sample answer: 5 equal straws joined at 5 clay balls make a pentagon. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.pentagon_q1", "Shapes with Straws, pentagon angles",
                  "Are these right angles?",
                  ["Lay a right angle checker on each corner of the pentagon."],
                  "From the picture: no. Each angle is bigger than a right angle.", kind="prompt"),
              FIO("ch1.pentagon_q2", "Shapes with Straws, pentagon push",
                  "Does the shape of the pentagon change if we gently push one of its sides? Yes/No",
                  ["Push one side of the pentagon on the screen.",
                   "Watch if the shape changes."],
                  "Sample answer: Yes. The pentagon leans over and changes its shape.", kind="prompt"),
              FIO("ch1.pentagon_q3", "Shapes with Straws, pentagon change",
                  "How does this change the angles?",
                  ["Compare the angles before and after the push."],
                  "Sample answer: some angles get smaller and some get bigger. Your answer may differ.",
                  kind="prompt"),
          ])],
    topic_type="instructional"))

# ---- T11: right angles in shapes (video -> Tool 15) -----------------------------------------------------------------
# PROVISIONAL, CLASH 4 and CLASH 6: Tool 15 carries C14 and the second part of C24 (printed on the last page).
# PROVISIONAL, CLASH 12: E12, E22, E23 (the four-sided shapes are unnamed, several shapes fit one clue).
# PROVISIONAL, CLASH 13 (a): note_square is a teacher note; the brief writer re-words its fact, no verbatim line here.
TOPICS.append(TOPIC(
    "T11", "M2", "Right Angles in Shapes", ["Shapes on a dot grid"], "Apply",
    "Students draw three- and four-sided shapes on a dot grid and count the right angles in each.",
    "Draw shapes with three or four sides on a dot grid and count their right angles.",
    [A("T11.C1", "Right Angles in Shapes", "Understand",
       "Students count the right angles in three- and four-sided shapes drawn on a dot grid.",
       role="story",
       ncert=["ch1.note_square"],
       key_terms=["rectangle", "square"], misconceptions=["M_AN_6"], minutes=5,
       # MEDIA STEP, CLASH 25: the counting of right angles belongs to Tool 15.
       video=VID("Nitesh Draws Shapes on Dots",
                 "Nitesh draws a three-sided and a four-sided shape on a dot grid and wonders how many of their angles "
                 "are right angles. The counting is left to the tool.",
                 new_idea="Three- and four-sided shapes can have none, some or all of their angles right angles.")),
     DOER("T11.C2", "Angles in Shapes", "shape_angles", "Apply",
          "Students draw three- and four-sided shapes on a dot grid, count their right angles and tell shapes apart by "
          "their kinds of angles.",
          applies_to="T11.C1", key_terms=["rectangle", "square", "right angle"], misconceptions=["M_AN_6", "M_AN_7"],
          minutes=7,
          # QUESTION MAPPER (step 5), CLASH 6: try8, try8_q and try9 moved up from the end of the chapter. E12: the three
          # four-sided shapes are not named. E22: several shapes fit each clue of try9, so the answer lists them all and
          # says so; shape 1 (a dart, with an angle past a straight line) fits no clue and is not mentioned.
          # E23: the right-angle counts are read by measure; the red tilted figure is called "the red tilted shape".
          items=[
              FIO("ch1.dotshapes", "Shapes on a dot grid",
                  "Use the dot grid given below to draw several three- and four-sided shapes. "
                  "Circle the shapes that have one or more right angles.",
                  ["Draw shapes with 3 sides and with 4 sides on the dots.",
                   "Lay your right angle checker on each corner.",
                   "Circle the shapes with a right angle."],
                  "Sample answer: a right triangle, a rectangle, a square and a slanted four-sided shape. "
                  "Circle the first three. Your answer may differ.", kind="exercise"),
              FIO("ch1.dotshapes_q", "Shapes on a dot grid, Discuss",
                  "Discuss: What shapes did you make? How many shapes have you made with a) 1 right angle "
                  "b) 2 right angles c) 3 right angles d) all right angles",
                  ["Count the right angles of each shape you drew.",
                   "Count the shapes in each group."],
                  "Sample answer: 1 right angle: a right triangle. 2: a shape with one slanted side. 3: none. "
                  "All: a rectangle and a square. Your answer may differ.", kind="prompt"),
              FIO("ch1.fourside_q", "Four-sided shapes",
                  "Here are some 4-sided shapes. In what ways are rectangle and square different from these shapes?",
                  ["Check the corners of each shape with your right angle checker."],
                  "Sample answer: a rectangle and a square have 4 right angles. The three shapes shown have none. "
                  "Your answer may differ.", kind="prompt"),
              FIO("ch1.try8", "Let Us Try, Q8",
                  "Mark the right angles and write the number of right angles in each figure.",
                  ["Lay your right angle checker on each corner.",
                   "Mark the right angles and count them."],
                  "From the picture: 4, 0, 1, 0, 0, 4, from left to right.", kind="exercise"),
              FIO("ch1.try8_q", "Let Us Try, Q8, only right angles",
                  "Which of the above shapes have only right angles?",
                  ["Look for the figures where every corner is marked."],
                  "From the picture: the blue rectangle and the red tilted shape.", kind="prompt"),
              FIO("ch1.try9", "Let Us Try, Q9",
                  "Observe the following shapes. Identify the shape that has: "
                  "2 right angles, 1 acute, and 1 obtuse angle; "
                  "1 right, 2 obtuse, and 1 acute angle; "
                  "2 obtuse, and 2 acute angles; "
                  "4 right angles.",
                  ["Compare each corner with a right angle.",
                   "Count the right, acute and obtuse angles of each shape."],
                  "From the picture: 2 right, 1 acute, 1 obtuse: shapes 2 and 7. 1 right, 2 obtuse, 1 acute: "
                  "shape 10. 2 obtuse, 2 acute: 3, 5, 8, 9, 11, 13. 4 right: 4, 6, 12, 14. More than one fits.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ======================================================================================================================
# MODULE M3  CIRCLES AND FLAT SHAPES  (Tools 16 to 19)
# ======================================================================================================================

# ---- T12: making a circle (video -> Tool 16) ------------------------------------------------------------------------
TOPICS.append(TOPIC(
    "T12", "M3", "Making a Circle", ["Let Us Make"], "Understand",
    "Students form a circle from points at the same distance from a centre and name its centre and radius.",
    "Lay equal straws around a centre and a circle appears. You meet the centre and the radius.",
    [A("T12.C1", "The Circle", "Understand",
       "Students name the centre of a circle and the radius, a line from the centre to the border.",
       role="story",
       textbook=["The point A is the centre and the line from the centre to the border of the circle is the radius."],
       ncert=["ch1.centre_text"],
       key_terms=["circle", "centre", "radius"], misconceptions=["M_CI_1"], minutes=5,
       # MEDIA STEP, CLASH 25: a given round paper, one radius, no ring of equal straws (that is what Tool 16 finds).
       video=VID("Diksha's Circle of Straws",
                 "Diksha holds a round paper circle, names its middle point the centre and a line from it to the edge "
                 "a radius, and wonders how to make a perfect circle.",
                 new_idea="In a circle the point in the middle is the centre, and a line from the centre to the border "
                          "is a radius.")),
     DOER("T12.C2", "Make a Circle", "circle_make", "Apply",
          "Students form a circle from equal straws and from points marked at the same distance from a centre.",
          applies_to="T12.C1", key_terms=["circle", "centre"], misconceptions=["M_CI_1"], minutes=6,
          # QUESTION MAPPER (step 5). No units anywhere: the scale only shows equal distances (CLASH 16).
          items=[
              FIO("ch1.circle_straws", "Straws and a circle",
                  "Can you make a circle using straws?",
                  ["Pick straws of the same length.",
                   "Lay them round one middle point, like spokes."],
                  "Sample answer: yes. Straws of the same length laid round a middle point have ends that make "
                  "a circle.", kind="exercise"),
              FIO("ch1.circle_straws_q1", "Straws and a circle, Q1",
                  "Look at the picture. The lengths of the straws in this picture are ................. "
                  "(Equal/Unequal)",
                  ["Look at the straws in the picture."],
                  "From the picture: equal.", kind="prompt"),
              FIO("ch1.circle_straws_q2", "Straws and a circle, Q2",
                  "What will happen if we take straws of unequal lengths?",
                  ["Try straws of different lengths on the screen."],
                  "Sample answer: the ends do not make a circle. The shape looks uneven.", kind="prompt"),
              FIO("ch1.make_circle", "Let Us Make",
                  "Can you use a scale to draw a circular shape? Let us see. Mark a point A. Draw many points that "
                  "are at an equal distance from point A. Connect the dots freehand.",
                  ["Mark a point A.",
                   "Use the scale to mark many points at the same distance from A.",
                   "Join the points by hand."],
                  "Sample answer: many points at the same distance from A, joined by hand. "
                  "They make a round shape. Your answer may differ.", kind="exercise"),
              FIO("ch1.make_circle_q", "Let Us Make, Q",
                  "What do you get?",
                  ["Look at the shape you joined."],
                  "From the picture: a circle.", kind="prompt"),
          ])],
    topic_type="instructional"))

# ---- T13: diameter and radius (video -> Tool 17, image -> Tool 18) --------------------------------------------------
# PROVISIONAL, CLASH 4 and CLASH 6: Tool 17 carries C17 and the "double" step of C18 (circ_do1).
# PROVISIONAL, CLASH 7 and CLASH 15: Tool 18 follows a new image of a carpet beside four wheels.
# PROVISIONAL, CLASH 13 (a): note_measure and note_compass are teacher notes; the brief writer re-words their facts.
TOPICS.append(TOPIC(
    "T13", "M3", "Diameter and Radius", ["Amazing Circles", "Let Us Do"], "Analyze",
    "Students show that the diameters of a circle are equal, pass through the centre and are double the radius, and find "
    "them in wheels and carpets.",
    "Fold a circle in half in different ways to find its diameters. Then find them in wheels and carpets.",
    [A("T13.C1", "Folding a Circle", "Understand",
       "Students say that a crease that folds a circle in half is called a diameter.",
       role="story",
       textbook=["These creases are called diameters of the circle.",
                 "Discuss where the centre is. Do you notice that all the diameters pass through the centre?",
                 "Discuss if there is any relationship between the radius and the diameter of a circle."],
       ncert=["ch1.amazing_t2", "ch1.amazing_t3", "ch1.amazing_t5", "ch1.note_measure"],
       key_terms=["diameter", "centre", "radius"], misconceptions=["M_CI_2", "M_CI_3"], minutes=5,
       # MEDIA STEP, CLASH 25: one fold only; equal creases, the centre and "double" are what Tool 17 finds.
       video=VID("Diksha Folds a Round Paper",
                 "Diksha folds a round paper in half once, calls the crease a diameter, and wonders if every fold in "
                 "half gives the same crease.",
                 new_idea="A crease that folds a circle in half is called a diameter.")),
     DOER("T13.C2", "Fold the Circle", "circle_fold", "Analyze",
          "Students show that the folds of a circle are equal diameters through the centre and that a diameter is "
          "double the radius.",
          applies_to="T13.C1", key_terms=["diameter", "radius"], misconceptions=["M_CI_2", "M_CI_3"], minutes=6,
          # QUESTION MAPPER (step 5), CLASH 4 and CLASH 6: circ_do1 (analysis C18, printed on the next page) is homed here with
          # the folds; its answer is the "double" step. E14: "center" of the printed amazing_q4 is spelt "centre"
          # (CLASH 32). The thread is a virtual thread; no units.
          items=[
              FIO("ch1.amazing1", "Amazing Circles",
                  "a) Take a piece of circular paper. b) Fold your paper in half and crease it well. "
                  "c) Open the fold and measure the length of the crease using a thread. "
                  "d) Fold your paper in half in a different way and crease it well. "
                  "e) Open the fold and measure the length of the crease again. "
                  "f) Fold it again in half in a different way and crease it well. "
                  "g) Open the fold, measure the length of the crease.",
                  ["Fold the round paper in half. Open it and measure the crease.",
                   "Fold it in half a different way. Measure the new crease.",
                   "Fold it a third way. Measure that crease."],
                  "From the picture: the three creases have the same length.", kind="exercise"),
              FIO("ch1.amazing_q1", "Amazing Circles, Q1",
                  "The length of all the creases are __________. (Equal/Unequal)",
                  ["Compare the three creases you measured."],
                  "From the picture: equal.", kind="prompt"),
              FIO("ch1.amazing_q4", "Amazing Circles, Q4",
                  "Measure the length of the creases from the centre to the border of the circle. "
                  "This is called the radius of the circle.",
                  ["Measure from the centre to the border along a crease.",
                   "Do it for each crease."],
                  "From the picture: every length from the centre to the border is the same. Each one is a radius.",
                  kind="exercise"),
              FIO("ch1.circ_do1", "Let Us Do, folds",
                  "Fold the circular paper in half. Fold this half again in half. "
                  "The length of the diameter is ___________ (half/double) of the length of radius.",
                  ["Fold the paper in half. The crease is a diameter.",
                   "Fold it in half again. A half of that crease is a radius.",
                   "Compare the diameter with the radius."],
                  "From the picture: double. The diameter is double the radius.", kind="exercise"),
          ]),
     A("T13.C3", "Wheels and Carpets", "Understand",
       "Students point out the centre, radius and diameter of a round carpet design and of wheels.",
       role="image",
       ncert=["ch1.note_compass"],
       key_terms=["radius", "diameter"], misconceptions=["M_CI_4"], minutes=4,
       # MEDIA STEP, CLASH 20: NOT the book's carpet or its wheels A to D (the tool marks and compares those), and one wheel
       # only, so the picture does not pre-empt the comparison. Each round object seen straight on, a true circle.
       image=IMG("A Round Rug and a Wheel",
                 "A real picture of a round rug and one bicycle wheel that are not the tool's carpet and wheels, each "
                 "seen straight on, so the child sees round things at home before marking the tool's. It carries no "
                 "mark, label or ruler.",
                 placement="main", new_context=True, style="photo", visuals=["round_rug_and_wheel"])),
     DOER("T13.C4", "Find Radius and Diameter", "radius_diameter", "Apply",
          "Students draw a circle design, mark its centre, radius and diameter and compare wheels by radius and "
          "diameter.",
          applies_to="T13.C3", key_terms=["radius", "diameter", "compass"], misconceptions=["M_CI_4"], minutes=6,
          # QUESTION MAPPER (step 5), CLASH 13 (a), CLASH 32: the printed sentence "Ask your teacher to help you use a
          # compass." is dropped from the compass question (the compass is on the screen); it edits one book question and
          # needs the user's yes; the printed wording is restored by putting the sentence back. E15: Step 1 to Step 3 are
          # pictures only in the book, so the steps below are read from the pictures. E16: wheels B and D by measure.
          items=[
              FIO("ch1.compass", "Let Us Do, compass",
                  "A circle can be made easily using a compass. Make the following design.",
                  ["Step 1: draw one circle with the compass.",
                   "Step 2: keep the same opening. Draw more circles, each with its point on the first circle.",
                   "Step 3: colour the petals as in the picture."],
                  "Sample answer: a flower of six petals. Use the same compass opening. "
                  "Colour it blue, green, red and yellow. Your answer may differ.", kind="exercise"),
              FIO("ch1.carpet", "Let Us Do, carpet",
                  "Look at the carpet design. A beautiful circle, right? Mark the centre, radius, and the diameter "
                  "of the circular design with any colour of your choice.",
                  ["Mark the centre with a dot.",
                   "Draw a radius from the centre to the edge.",
                   "Draw a diameter through the centre from edge to edge."],
                  "Sample answer: the centre is the small dot in the middle. A radius runs from it to the edge. "
                  "A diameter goes through it from edge to edge. Your answer may differ.", kind="exercise"),
              FIO("ch1.wheels_q0", "Wheels",
                  "Look at the wheels. All wheels look like ...............",
                  ["Look at the four wheels A, B, C and D."],
                  "From the picture: circles.", kind="prompt"),
              FIO("ch1.wheels_q1", "Wheels, radius and diameter",
                  "Name the wheel with the 1. longest radius 2. shortest radius 3. longest diameter "
                  "4. shortest diameter",
                  ["Measure the radius and the diameter of each wheel.",
                   "Compare the four wheels."],
                  "From the picture: 1. B. 2. D. 3. B. 4. D. The wheel with the longest radius also has the "
                  "longest diameter.", kind="prompt"),
          ])],
    topic_type="instructional"))

# ---- T14: sides and angles of flat shapes (video -> Tool 19) --------------------------------------------------------
# PROVISIONAL, CLASH 4 and CLASH 6: Tool 19 carries C20 and the first part of C24, placed before the puzzles of the book.
# PROVISIONAL, CLASH 10: the six 2D shape cards are at the end of the book, outside the chapter's pages.
TOPICS.append(TOPIC(
    "T14", "M3", "Sides and Angles of Flat Shapes", ["Card Game", "Let Us Try"], "Analyze",
    "Students sort flat shapes by their sides and find that a straight-sided shape has as many angles as sides.",
    "Sort flat shapes by their sides. Then count their angles and see what you notice.",
    [A("T14.C1", "Counting Sides and Angles", "Understand",
       "Students sort flat shapes by the number of their sides and count the angles of each.",
       role="story",
       key_terms=["side", "angle"], misconceptions=["M_AN_7"], minutes=5,
       # MEDIA STEP, CLASH 25: the angle counts (and that they match the sides) belong to Tool 19; other shapes than its cards.
       video=VID("Nitesh Sorts Flat Shape Cards",
                 "Nitesh sorts flat shape cards into groups by their number of sides and wonders what else he can "
                 "count on a shape.",
                 new_idea="A flat shape can be sorted by the number of its sides, and its angles can be counted too.")),
     DOER("T14.C2", "Sides and Angles", "sides_angles", "Analyze",
          "Students sort flat shapes by their sides and by their angles and find that a straight-sided shape has as "
          "many angles as sides.",
          applies_to="T14.C1", key_terms=["side", "angle"], misconceptions=["M_AN_7"], minutes=6,
          # QUESTION MAPPER (step 5), CLASH 6 and CLASH 10: cards, try6, try6_q, try7a, try7b are the proposal's five; the six
          # cards are on the screen. E18 (CLASH 11): the book does not say what the three groups are; the answer is one
          # reading. ch1.straw_compare comes from Tool 14 ONLY because of the cap of 6 (PROVISIONAL, CLASH 30): "How are
          # the angles of triangles and rectangles similar or different?" is answered with the numbers of angles and the
          # right angles, which this tool compares. Under option (b), cap 7, it goes back to Tool 14 and this tool has 5.
          items=[
              FIO("ch1.cards", "Card Game",
                  "Sort the 2D-shape cards given at the end of the book into three groups according to their "
                  "sides. Draw the sorted shapes in the space given below. Explain why you sorted your shapes "
                  "in this way.",
                  ["The six cards are on the screen.",
                   "Drag the cards into three groups by their sides.",
                   "Say why you made each group."],
                  "Sample answer: only straight sides: square, triangle. Only curved sides: oval, circle. "
                  "Both: quarter circle, semicircle. Your answer may differ.", kind="exercise"),
              FIO("ch1.try6", "Let Us Try, Q6",
                  "Classify these shapes based on the number of angles.",
                  ["Count the angles of each shape a to g.",
                   "Drag it to 3 angles, 4 angles or 5 angles."],
                  "From the picture: 3 angles: b, d, f. 4 angles: a, c, g. 5 angles: e.", kind="exercise"),
              FIO("ch1.try6_q", "Let Us Try, Q6, sides and angles",
                  "What relation do you notice between the number of sides and the number of angles?",
                  ["Count the sides of each shape.",
                   "Compare with its number of angles."],
                  "From the picture: each shape has as many angles as it has sides.", kind="prompt"),
              FIO("ch1.try7a", "Let Us Try, Q7",
                  "Draw a 2D shape that has less than 5 angles.",
                  ["Draw a shape on the dots.",
                   "Count its angles."],
                  "Sample answer: a triangle has 3 angles and a rectangle has 4. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.try7b", "Let Us Try, Q7 (more)",
                  "Draw a 2D shape with more than 5 angles.",
                  ["Draw a shape on the dots.",
                   "Count its angles."],
                  "Sample answer: a hexagon has 6 angles. Your answer may differ.", kind="exercise"),
              FIO("ch1.straw_compare", "Shapes with Straws, compare",
                  "How are the angles of triangles and rectangles similar or different?",
                  ["Count the angles of a triangle and of a rectangle.",
                   "Compare their kinds of angles."],
                  "Sample answer: both have angles at their corners. A triangle has 3 angles and a rectangle has 4, "
                  "all right angles. Your answer may differ.", kind="prompt"),
          ])],
    topic_type="instructional"))

# ======================================================================================================================
# MODULE M4  SHAPE PUZZLES  (Tools 20 to 22)
# ======================================================================================================================

# ---- T15: puzzling shapes (puzzle story video -> Tool 20) -----------------------------------------------------------
# PROVISIONAL, CLASH 14: a puzzle told as a story, solved on the tool.
# PROVISIONAL, CLASH 17: Diksha tells the story, for the unnamed girl of the book's picture.
# PROVISIONAL, CLASH 6: C19 (printed before the card game) comes after Tool 19 here.
TOPICS.append(TOPIC(
    "T15", "M4", "Puzzling Shapes", ["Puzzling Shapes"], "Apply",
    "Students find hidden shapes in a drawing and draw lines that cut a shape into smaller shapes.",
    "Find shapes hidden in a drawing. Then draw lines to cut a shape into smaller shapes.",
    [A("T15.C1", "Hidden Shapes and Cuts", "Understand",
       "Students find shapes hidden in a drawing and say how lines cut a shape into smaller shapes.",
       role="story",
       key_terms=["hidden shape"], minutes=5,
       # MEDIA STEP, CLASH 25: a simple drawing of the story's own, not the book's puzzles; one cut, no solution.
       video=VID("Diksha's Hidden Shapes",
                 "Diksha finds a shape hidden in a simple drawing and cuts a paper shape into two smaller shapes with "
                 "one line, then wonders what else she can find or cut.",
                 new_idea="Shapes can hide inside a drawing, and lines can cut one shape into smaller shapes.")),
     DOER("T15.C2", "Divide the Shapes", "divide", "Apply",
          "Students find the hidden shapes in a drawing and draw lines that divide a shape into smaller shapes.",
          applies_to="T15.C1", key_terms=["hidden shape"], minutes=6,
          # QUESTION MAPPER (step 5), CLASH 11 and CLASH 31: E17. Reading the figure at 7x, the hidden shapes are a circle, a
          # cylinder, ONE square, ONE tilted rectangle and two triangles (analysis.md said two squares: the tilted one is
          # about 2.2 times as long as it is wide). The cut lines of the puzzles are not unique, so they are Sample answers.
          items=[
              FIO("ch1.puzzle1", "Puzzling Shapes, Q1",
                  "Identify the hidden shapes and write their names.",
                  ["Trace each outline with your finger.",
                   "Name the shape you find."],
                  "From the picture: a circle, a cylinder, a square, a rectangle and two triangles.", kind="exercise"),
              FIO("ch1.puzzle2", "Puzzling Shapes, Q2",
                  "Draw 2 lines to divide the triangle into 1 square and 2 triangles.",
                  ["Draw a line from the middle of the top side straight down to the slanted side.",
                   "Draw a line from the middle of the left side straight across to the slanted side."],
                  "Sample answer: the two lines meet on the slanted side. They make 1 square in the corner and "
                  "2 triangles. Your answer may differ.", kind="exercise"),
              FIO("ch1.puzzle3", "Puzzling Shapes, Q3",
                  "Draw 2 lines to divide the square into 3 triangles.",
                  ["Pick a dot on the top side, between the two top corners.",
                   "Draw a line from it to each bottom corner."],
                  "Sample answer: the two lines make 3 triangles. Your answer may differ.", kind="exercise"),
              FIO("ch1.puzzle4", "Puzzling Shapes, Q4",
                  "Draw lines to show the cuts needed on the shapes in the left column to get the smaller shapes "
                  "on the right.",
                  ["Look at the pieces on the right.",
                   "Draw the cut lines on the shape on the left."],
                  "Sample answer: A: cut straight across near each pointed end. "
                  "B: cut from each top corner to the middle of the bottom. Then cut straight down the middle. "
                  "C: cut off the 3 corners. Your answer may differ.", kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T16: spider webs (puzzle story video -> Tool 21) ---------------------------------------------------------------
# PROVISIONAL, CLASH 14 and CLASH 11: a puzzle story; the answers 10, yes, 12, no are the analyst's reading.
TOPICS.append(TOPIC(
    "T16", "M4", "Spider Webs", ["Let Us Try"], "Analyze",
    "Students count shapes in two webs and decide which walks use no wall twice.",
    "Squiggly and Wiggly check their webs. You count shapes and trace walks that use no wall twice.",
    [A("T16.C1", "Squiggly and Wiggly's Webs", "Understand",
       "Students count the shapes in a web, big and small, and say what a walk that uses no wall twice means.",
       role="story",
       textbook=["Squiggly, the spider, likes to make webs in different shapes. One day she begins to make triangular "
                 "webs.",
                 "She likes to take a walk each morning and check if the walls of her web are strong.",
                 "Her brother, Wiggly made a web using rectangles.",
                 "He likes to take a walk at the end of each day and check if the walls of his web are strong."],
       ncert=["ch1.try1_text"],
       key_terms=["web", "wall", "path"], misconceptions=["M_PU_1", "M_PU_2"], minutes=5,
       video=VID("Squiggly and Wiggly Check Their Webs",
                 "The spiders Squiggly and Wiggly check the walls of their webs and wonder how many shapes each web "
                 "holds and whether a walk can use every wall once.",
                 new_idea="Shapes in a web can be counted, big and small, and a walk that uses no wall twice can be "
                          "tested.")),
     DOER("T16.C2", "Spider Web Puzzles", "webs", "Analyze",
          "Students count the triangles and rectangles in two webs and decide which walks can be made without using a "
          "wall twice.",
          applies_to="T16.C1", key_terms=["web", "wall", "path"], misconceptions=["M_PU_1", "M_PU_2"], minutes=6,
          # QUESTION MAPPER (step 5). The four answers (10, yes, 12, no) were re-checked on the page (10 triangles, 12
          # rectangles, and the path below uses all 12 numbered walls once). E19 and CLASH 31: the book does not say
          # "every wall"; the plan reads Wiggly's walk as one that uses every wall once (the story says he checks his
          # walls); without that reading the answer to try1d would be yes. No rule about corners is given to the child.
          items=[
              FIO("ch1.try1a", "Let Us Try, Q1 (triangles)",
                  "How many triangles are in her web?",
                  ["Top and bottom triangles: 1 + 1 = 2.",
                   "Count the 4 small triangles in the middle: 2 + 4 = 6.",
                   "Count the 4 big triangles made of 2 small ones: 6 + 4 = 10."],
                  "From the picture: 10 triangles.", kind="prompt"),
              FIO("ch1.try1b", "Let Us Try, Q1 (Squiggly's path)",
                  "Can she begin at point A and reach back to the same point without walking on any wall more than "
                  "once? Trace and show Squiggly's path.",
                  ["Start at A. Trace one wall at a time.",
                   "The walls are numbered 1 to 12 in the picture.",
                   "Do not use a wall twice."],
                  "Sample answer: yes. One path: 12, 6, 9, 3, 4, 7, 10, 2, 8, 5, 11, 1. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.try1c", "Let Us Try, Q1 (rectangles)",
                  "How many rectangles can you see in his web?",
                  ["Count the small rectangles.",
                   "Count the bigger ones made of 2 or 3 small ones."],
                  "From the picture: 12 rectangles, big and small.", kind="prompt"),
              FIO("ch1.try1d", "Let Us Try, Q1 (Wiggly's path)",
                  "Can he begin at point A and leave from point B without walking on any wall more than once? "
                  "Trace and show Wiggly's path.",
                  ["Start at A. Trace one wall at a time.",
                   "Try to use every wall once and end at B."],
                  "Sample answer: no. Try to use every wall once. Every walk from A gets stuck first.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T17: matchstick puzzles (puzzle story video -> Tool 22) --------------------------------------------------------
# PROVISIONAL, CLASH 14: a puzzle story.  PROVISIONAL, CLASH 18: Tool 22's part 4 (remove 4 sticks to leave 3 triangles)
# is not solved yet, and part 3 only on one reading of the figure.
TOPICS.append(TOPIC(
    "T17", "M4", "Matchstick Puzzles", ["Let Us Try"], "Apply",
    "Students make triangles from matchsticks and move or remove sticks to form a given number of triangles.",
    "Wiggly makes triangles with matchsticks. You make, move and remove sticks to form triangles.",
    [A("T17.C1", "Wiggly's Matchsticks", "Understand",
       "Students count the triangles made from matchsticks and say how moving or taking away sticks changes the count.",
       role="story",
       key_terms=["matchstick", "triangle"], misconceptions=["M_PU_3"], minutes=5,
       video=VID("Wiggly's Matchstick Triangles",
                 "Wiggly makes triangles with matchsticks and wonders how few sticks he needs.",
                 new_idea="Triangles made of matchsticks can be counted, and moving or removing sticks changes the count.")),
     DOER("T17.C2", "Matchstick Moves", "matchsticks", "Apply",
          "Students make, move and remove matchsticks to form a given number of triangles.",
          applies_to="T17.C1", key_terms=["matchstick", "triangle"], misconceptions=["M_PU_3"], minutes=5,
          # QUESTION MAPPER (step 5), CLASH 18 and CLASH 11: E20. try3 is solved only on a reading of the figure and try4 is
          # not solved, so their answers give NO solution and say how to find one. try2 (5 sticks, 2 triangles) is solved.
          items=[
              FIO("ch1.try2", "Let Us Try, Q2",
                  "Use 5 matchsticks to make 2 triangles. Then draw it in the space provided.",
                  ["Make a diamond with 4 sticks.",
                   "Lay the 5th stick across the middle of the diamond.",
                   "Draw what you made."],
                  "Sample answer: a diamond with one stick across its middle. The 2 triangles share that stick. "
                  "Your answer may differ.", kind="exercise"),
              FIO("ch1.try3", "Let Us Try, Q3",
                  "Move two of these matchsticks to form 4 triangles.",
                  ["Move two sticks on the screen.",
                   "Count the triangles after each move."],
                  "Sample answer: keep moving two sticks on the screen until you can count 4 triangles. "
                  "Your answer may differ.", kind="exercise"),
              FIO("ch1.try4", "Let Us Try, Q4",
                  "Remove 4 of these matchsticks to leave only 3 triangles.",
                  ["Take away 4 sticks on the screen, one at a time.",
                   "Count the triangles that are left."],
                  "Sample answer: keep taking away sticks on the screen until only 3 triangles are left. "
                  "Your answer may differ.", kind="exercise"),
          ])],
    topic_type="instructional"))

# ======================================================================================================================
# THE REVIEW  (MLAST)
# ======================================================================================================================
# PROVISIONAL, CLASH 14: the review only recaps; it has no checked question (the book has no end exercise).
# Two review concepts (the gate allows at most 2). Between them they revise the main idea of every topic; the two
# image-only concepts that only set the scene (T2.C1 bricks, T4.C1 everyday objects) are not revised on their own.
# Key terms below are all taken from the concepts above (the gate rejects a new term).
# MEDIA STEP, CLASH 28: the review has no video, no image and no tool of its own; its recap may show an earlier picture
# only by its VISUAL_KEY key (the same drawing), never a new image node.
TOPICS.append(TOPIC(
    "T18", "MLAST", "Chapter Review", ["Summary"], "Understand",
    "",   # the review carries NO topic objective
    "Look back at solids, angles, circles and puzzles. You use only what you have already met.",
    [A("T18.C1", "Look Back at Solids", "Understand",
       "Students recall the faces of prisms and pyramids, the parts of a solid and which nets fold into solids.",
       role="review",
       review_covers=["T2.C2", "T3.C1", "T3.C3", "T4.C3", "T5.C1", "T6.C1", "T7.C1"],
       key_terms=["prism", "pyramid", "face", "edge", "corner", "net"], minutes=5),
     A("T18.C2", "Look Back at Angles, Circles and Puzzles", "Understand",
       "Students recall right, acute and obtuse angles, the parts of a circle and how to solve the shape puzzles.",
       role="review",
       review_covers=["T8.C1", "T9.C1", "T9.C3", "T10.C1", "T10.C3", "T11.C1", "T12.C1", "T13.C1", "T13.C3", "T14.C1",
                      "T15.C1", "T16.C1", "T17.C1"],
       key_terms=["angle", "right angle", "acute angle", "obtuse angle", "circle", "radius", "diameter"],
       minutes=5)],
    topic_type="summary"))

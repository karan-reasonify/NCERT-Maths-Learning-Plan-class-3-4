# -*- coding: utf-8 -*-
"""Toy Joy (Class 3, chapter 2): the chapter's topic skeleton. STRUCTURE STAGE (c34-journey-designer, step 3).

Keys are FINAL from here on: topic "T1", concept "T1.C1". The order follows the teacher's note row by row and the eight
approved tools exactly as the content team gave them (tool_map.locked.md); nothing is reordered, added or dropped.

    T1  opening       note rows 1, 2      hook video -> Tool 1
    T2  idea topic    note rows 3, 4      concept video -> Tool 2
    T3  idea topic    note rows 5, 6      concept video -> Tool 3
    T4  idea topic    note rows 7, 8      image concept -> Tool 4        (PROVISIONAL, CLASH 8)
    T5  idea topic    note rows 9, 10     concept video -> Tool 5
    T6  idea topic    note rows 11, 12    demo video    -> Tool 6        (PROVISIONAL, CLASH 9)
    T7  idea topic    note rows 13, 14    image concept -> Tool 7        (PROVISIONAL, CLASH 8)
    T8  idea topic    note row 15         image concept -> Tool 8        (PROVISIONAL, CLASH 10 and CLASH 3)
    T9  review        note row 17         two look-back concepts, nothing new (CLASH 14)

Note row 16 (NCERT practice) is met by the questions on the tools (CLASH 13). QUESTIONS (step 5, c34-question-mapper,
revised after the user's decisions of 5 Nov 2026): every one of the 31 book questions is homed once, as FIO(...) in `items`
of the tool concept of the concept it practises (the map is in question_map.md). Tool 1 holds none (CLASH 1). The user
raised the cap to 7 for this chapter only (CLASH 4 and 22, option a): ch2.q1c is back on Tool 4 (last) and ch2.say3 is its
own item on Tool 6 (right after q9, asked on q9's screen). Tool 4 and Tool 6 hold 7 each. Every answer is the plan's own
reading and begins "From the picture" or "Sample answer" (no official key exists, CLASH 24). Every video, image and tool
here is a PLACEHOLDER: the story briefs, image briefs and tool specs come after the user approves the structure.

MEDIA DECISIONS (step 4, c34-media-minimiser, revised after the user's decisions of 5 Nov 2026; the reasons are in
media_decisions.md, the overlaps in CLASH 15 to 21, 26 and 27): every media choice the content team's note names is kept,
none is dropped or added. The minimum is 5 story videos (the hook and four concept videos), 3 main images, 0 pinned
images, 8 tools. The user's general principle: extra real-life examples (a football, a birthday cap, a shoebox, a bottle,
a die) are fine when they correctly represent the concept, and a sphere is ALWAYS a shaded 3D ball, never a flat disc.
Details decided inside the note's choices: Tool 1, the hook and the T2 video use those real objects; the T4 image is one
unlabelled composite (rocket, one house, engine) and the shop toys stay on the tool only; the T6 demo is one short story
video that shows the joining only (no hidden cubes, no meaning for balls and sticks); the T7 comparison image is ONE photo
of real objects that shows and does not tell, with the cube beside the cuboid as its core and a ball beside a flat paper
circle only as a smaller secondary pair; the T8 lead-in is ONE illustration of a die with three faces in view and the
other three out of sight; the review (T9) adds no media of its own.

One idea topic per unit (concept video or image, then its tool): each unit is one idea with its own tool, objective and
questions, so a later change to one unit leaves the others alone. No two units explain the same concept: T4 reads where a
shape is in a finished model, T5 uses the same words to tell someone how to build one (CLASH 12).
"""
from __future__ import annotations

from topics_common import A, DOER, FIO, IMG, TOPIC, VID, WE  # noqa: F401

TOPICS = []

# ---- T1: the opening (note rows 1 and 2) -----------------------------------------------------------------------
# The hook is a story only and names no solid. Tool 1 follows at once and names no shape either: discovery first.
# CLASH 1 is DECIDED BY THE USER (5 Nov 2026): the toy box, the football, the birthday cap, the shoebox, the bottle, the die
# and "roll, slide or stand" are kept as real-life examples, stated accurately. Tool 1 and the hook name no solid shape.
TOPICS.append(TOPIC(
    "T1", "M1", "The Mystery of Toys", ["Let us Do"], "Understand",
    "",   # the opening carries NO topic objective
    "Jaya opens a toy box. Some toys roll and some stand. Try them yourself.",
    [A("T1.C1", "The Mystery of Toys", "Understand", "", role="hook",
       textbook=["Some children are making animal and bird faces on old boxes, cans and paper."],
       teach=["Predict first: which toys will roll away and which will stay?"],
       ncert=["opening"], key_terms=[], minutes=4,
       # MEDIA: hook video kept (the note and the flow rule). No image: Tool 1 shows the same objects at once. The hook
       # asks the question and leaves the answer to Tool 1, so nothing is explained twice. The toy box holds the objects
       # Tool 1 uses (VISUAL_KEY football, die, shoebox, bottle, birthday_cap); the hook names no solid shape.
       video=VID("The Mystery of Toys",
                 "Jaya opens a toy box and finds a football, a die, a shoebox, a bottle and a birthday cap. Some roll "
                 "and some stand. The story ends on the open question why, names no solid shape and leaves the answer "
                 "to Tool 1.",
                 story={"characters": ["Jaya", "Devika", "the children"],
                        "setting": "the classroom craft corner: a long table and a big toy box",
                        "situation": "It is the day before the toy show. Jaya opens the toy box. She takes out a football, a die "
                                     "and a shoebox. Then she takes out a bottle and a birthday cap. Devika lines them up on the "
                                     "long table. Jaya gives each toy a gentle push. The football rolls off the edge and the "
                                     "children chase it. The bottle, lying down, rolls a little way. The cap, on its side, rolls "
                                     "round and round. The die and the shoebox only slide a short way and stop. Then the "
                                     "children try to stand each toy up. The bottle, the die, the shoebox and the cap all stand. "
                                     "The football will not stay on one spot, however hard Jaya tries. Nobody says what any toy is "
                                     "called or why it moves that way.",
                        "open_question": "Why does the football roll away, while the shoebox stays where it is?"},
                 seconds=75)),
     DOER("T1.C2", "Explore Shapes Around Us", "explore_shapes", "Understand", "",
          applies_to="T1.C1", role="explore", minutes=6,
          recap=["Some things roll. Some slide. Some stand.",
                 "A football rolls every way. A shoebox slides and stands on its flat sides.",
                 "Things that look alike move in the same way."])],
    topic_type="framing"))

# ---- T2: Meet the Solid Shapes (note rows 3 and 4) -> Tool 2 ----------------------------------------------------
# The concept video is the first place the five solids are named (cube, cuboid, cylinder, cone, sphere), through the
# toys and objects the children already handled in Tool 1. It explains only these five and nothing about their parts.
TOPICS.append(TOPIC(
    "T2", "M1", "Meet the Solid Shapes", ["Let us Do", "Teacher's Note"], "Apply",
    "Students name a cube, a cuboid, a cylinder, a cone and a sphere, even when turned, and match each to an "
    "everyday object.",
    "You meet five solid shapes. You give each one its name.",
    [A("T2.C1", "Meet the Solid Shapes", "Remember",
       "Students name the cube, cuboid, cylinder, cone and sphere, whichever way the shape is turned.", role="story",
       textbook=["Look at my bottle (cylinder). I made a puppy face on it. It has wide ears.",
                 "I made a cat face on the cuboid. It has long whiskers.",
                 "I made a pig face on the box (cube). It has narrow eyes.",
                 "I made a bird face on the cone. Look at its pointed beak!",
                 "They can turn the shapes and observe them in different orientations."],
       teach=["Predict first: what name would you give a football, a die and a shoebox?",
              "A football is a sphere. A die is a cube. A shoebox is a cuboid.",
              "A bottle is a cylinder. A birthday cap is a cone.",
              "A shape keeps its name when you turn it or lay it down."],
       ncert=["ch2.note1"],
       key_terms=["solid", "cube", "cuboid", "cylinder", "cone", "sphere"],
       misconceptions=["M_TOY_6", "M_TOY_1"], minutes=5,
       # MEDIA: concept video kept (the note; a big new idea, the five names, with known misconceptions). No image: the
       # video shows the toys and Tool 2 shows and names each solid, so a chart would repeat both. The video reuses the
       # real objects of Tool 1 (die, shoebox, bottle, birthday cap, football). The sphere is shown as a shaded ball only,
       # never a flat disc (CLASH 2); the flat-circle contrast belongs to the T7 image (CLASH 18), not here.
       video=VID("Meet the Solid Shapes",
                 "Jaya and Devika line up the football, die, shoebox, bottle and birthday cap from the toy box, and the "
                 "children give each kind of solid shape its name.",
                 new_idea="the five solid shapes and their names: cube, cuboid, cylinder, cone and sphere",
                 story={"characters": ["Jaya", "Devika", "the children"],
                        "setting": "the craft corner, with a shelf and blank name cards for the toy show",
                        "situation": "The toy show opens tomorrow. Jaya and Devika must put a name card on each shelf. All "
                                     "the cards are blank. The children show the craft they made. A puppy face is on a bottle. A "
                                     "cat face is on the shoebox. A pig face is on a box like the die. A bird face is on the "
                                     "birthday cap. Jaya holds up the toys one at a time.",
                        "problem": "Devika cannot tell which name goes with which toy. The cards stay blank until the children "
                                   "name each kind. So the children name each kind. Devika writes each name on a card. A ball is "
                                   "a sphere. A die is a cube. A shoebox is a cuboid. A bottle is a cylinder. A birthday cap is "
                                   "a cone. The football is drawn as a full, shaded ball. Then Devika lays the bottle on its "
                                   "side. She says it is a new kind of toy and needs a new card. Jaya stands the bottle up and "
                                   "lays it down again. Then Jaya holds the cap with its tip down. She lays it on its side. It "
                                   "is the same bottle and the same cap. So each keeps its one name.",
                        "thread": "The toys from the hook are on the shelf. The children have pushed them, turned them and "
                                  "stood them up. Now they need names for them.",
                        "leads_to": "Tool 2, Meet the 3D Shapes. The child turns each solid and names it. Then the child matches "
                                    "it to an everyday object."},
                 seconds=120)),
     # QUESTIONS (6, under the cap of 7): the recognition and matching questions of C2 and C3. do1, do2, q1a, q1b are
     # stretches whose home the user confirmed (CLASH 5, 5 Nov 2026): the craft names cube, cuboid and cylinder (so not
     # Tool 1), and the most / least count is the last step of the classroom match in q1. do1 and q1 are real-world
     # activities kept as ON-SCREEN versions (CLASH 25): do1, the child picks an animal or bird face for each solid; q1,
     # the child sorts real objects into the five columns, then looks round the classroom. The q1 sample answer uses only
     # objects that really are the solid (a football, a die, a shoebox, a bottle, a birthday cap and the like), never a
     # globe, a clay pot, a watermelon, a cake slice or a roti stack (CLASH 26). The sphere is a shaded ball here.
     DOER("T2.C2", "Meet the 3D Shapes", "meet_3d_shapes", "Apply",
          "Students name the five solids, even when turned, and match each to an everyday object.",
          applies_to="T2.C1", minutes=7, misconceptions=["M_TOY_6", "M_TOY_1"],
          key_terms=["solid", "cube", "cuboid", "cylinder", "cone", "sphere"],
          recap=["A solid keeps its name when you turn it.",
                 "A die is a cube. A shoebox is a cuboid.",
                 "A bottle is a cylinder. A birthday cap is a cone.",
                 "A football is a sphere. A sphere is a solid ball."],
          items=[
              FIO("ch2.do1", "Let us Do, craft",
                  "Use old boxes (cubes and cuboids) and bottles (cylinders) to do craft work. Draw faces on them.",
                  ["Pick a box or a bottle on the screen.", "Choose an animal or bird face and put it on."],
                  "Sample answer: a puppy face on a bottle. A cat face on a cuboid box. Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.do2", "Let us Do, craft faces",
                  "What did you draw on their faces?",
                  [],
                  "Sample answer: a puppy, a cat, a pig and a bird. Your answer may differ.",
                  kind="prompt"),
              FIO("ch2.q1", "Let us Do, Q1",
                  "Find the shapes in the classroom that look like the following shapes. And fill in the table with "
                  "their names. The table has five columns: Cylinder, Sphere, Cube, Cuboid, Cone.",
                  ["Look at the real objects on the screen. Put each one in the column with its shape name.",
                   "Then look around your classroom for more."],
                  "Sample answer: Cylinder: bottle, chalk. Sphere: football, marble. Cube: die, cube-shaped box. "
                  "Cuboid: shoebox, eraser, book. Cone: birthday cap. Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.q1a", "Let us Do, Q1(a)",
                  "Name the shape that you find the most.",
                  ["Count the names in each column.", "Pick the column with the most names."],
                  "Sample answer: cuboid. Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.q1b", "Let us Do, Q1(b)",
                  "Name the shape that you find the least.",
                  ["Count the names in each column.", "Pick the column with the fewest names."],
                  "Sample answer: cone. Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.q2", "Let us Do, Q2",
                  "Look at these shapes and follow the instructions below. Circle the cubes. Put a tick against the "
                  "shapes that are cones. Put a cross against the shapes that are cylinders. Draw a box around the "
                  "cuboids.",
                  ["Look at each shape, even when it is turned or lying down.", "Mark it by its name."],
                  "From the picture: circle the 3 cubes. Tick the 3 cones. Cross the 3 cylinders. Box the 3 cuboids. "
                  "The yellow ball is a sphere. No instruction is for a sphere, so it gets no mark.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T3: The Secret Parts of Shapes (note rows 5 and 6) -> Tool 3 -----------------------------------------------
TOPICS.append(TOPIC(
    "T3", "M1", "The Secret Parts of Shapes", ["Let us Do"], "Apply",
    "Students point to the faces, edges and corners of a solid and say which faces are flat and which are curved.",
    "Every solid has faces, edges and corners. You find them on each shape.",
    [A("T3.C1", "The Secret Parts of Shapes", "Understand",
       "Students point to the face, edge and corner of a solid and tell a flat face from a curved face.", role="story",
       textbook=["face", "edge", "corner"],   # the three labels on the book's cube picture (fig1)
       teach=["Predict first: how many flat sides does a die have?",
              "A die has 6 flat sides. Each flat side is a face.",
              "Where two faces meet is a line. The line is an edge.",
              "A pointed place on a solid is a corner.",
              "A football has one curved face. It has no edges and no corners.",
              "A face can be flat or curved."],
       examples=[WE("How many faces, edges and corners does a shoebox have?",
                    ["The top is 1 face. The bottom is 1 face. The 4 sides are 4 faces.",
                     "1 + 1 + 4 = 6 faces.",
                     "4 edges go round the top. 4 edges go round the bottom. 4 edges go up the sides.",
                     "4 + 4 + 4 = 12 edges.",
                     "4 corners are on the top. 4 corners are on the bottom.",
                     "4 + 4 = 8 corners."],
                    "Example: a shoebox has 6 faces, 12 edges and 8 corners.")],
       ncert=["ch2.fig1"],
       key_terms=["face", "edge", "corner", "flat face", "curved face"],
       misconceptions=["M_TOY_3", "M_TOY_4", "M_TOY_5"], minutes=5,
       # MEDIA: concept video kept (the note; a big new idea with three known misconceptions). The close-up visuals the
       # note asks for are inside the video, so no image. No pinned cube figure (CLASH 21): Tool 3 labels the parts on tap.
       video=VID("The Secret Parts of Shapes",
                 "Jaya looks closely at the toy solids and finds the faces, edges and corners of each.",
                 new_idea="the parts of a solid: faces, edges and corners, and a face is flat or curved",
                 story={"characters": ["Jaya", "Devika"],
                        "setting": "the craft corner, with a gift box being decorated for the toy show",
                        "situation": "Devika decorates a gift box shaped like the die. She wants a ribbon on the lines where two "
                                     "sides meet. She wants a star on each pointed place. She wants paint on each flat side. But "
                                     "she only says that bit and points. Jaya cannot tell which bit she means. Jaya "
                                     "fetches a big magnifying glass and looks closely at the box. Close-ups show a flat side "
                                     "lighting up. A line where two sides meet glows. A pointed place sparkles. Together they find "
                                     "the names. A flat side is a face. The line is an edge. The pointed place is a corner. Then "
                                     "Jaya looks at the bottle. Its top and bottom are flat. Its side bends all the way round. "
                                     "That side is a curved face. The rim, where the flat top meets the side, is an edge too. It is a "
                                     "curved edge. The football is one curved face all over. It has no lines and no pointed "
                                     "places.",
                        "problem": "The friends have no words for the parts of a solid. So the ribbon, the stars and the paint "
                                   "go to the wrong places. Devika also wonders if a curved side counts, because it is not flat.",
                        "thread": "The five solids now have names on the shelf cards. The die is a cube. Now the children need "
                                  "names for its parts.",
                        "leads_to": "Tool 3, Explore Faces, Edges and Corners. The child taps a face, traces an edge and finds a "
                                    "corner."},
                 seconds=130)),
     # QUESTIONS (2): q3 sorts the five solids by flat and curved faces and straight and curved edges. Its bullet "with
     # both straight and curved edges" has no answer among the five solids (printed-book error, SOLUTION_NOTES), so the
     # answer says none, is labelled "Sample answer" and repeats no printed answer. do8 is a stretch whose home the user
     # confirmed (CLASH 5, 5 Nov 2026) and whose wording the user asked to make clearer from the book's own context: the
     # book's last sentence of the house activity ("What part of the shapes can you see from a distance?") follows
     # "Collect objects to make a house", so the FIO question is the PLAN'S clearer wording (a house made of solid shapes,
     # seen from far away; the parts are the faces, edges and corners of this tool). The book's own wording stays in
     # NCERT_ITEMS and analysis.md. HOUSE PICTURE ON TOOL 3: the plan's own simple house, a yellow cuboid for the walls
     # and a lavender cone for the roof, drawn like this tool's solids (VISUAL_KEY cuboid and cone), seen first small
     # from far away and then close up. It is NOT Jaya's two-storey house (reserved for the T4 image) and NOT one of
     # Jaya's other three houses (kept for Tool 5). No answer is printed in the book: the answer is a Sample answer.
     DOER("T3.C2", "Explore Faces, Edges and Corners", "faces_edges_corners", "Apply",
          "Students find the faces, edges and corners of solids and use flat and curved parts to tell solids apart.",
          applies_to="T3.C1", minutes=7, misconceptions=["M_TOY_3", "M_TOY_4", "M_TOY_5"],
          key_terms=["face", "edge", "corner", "flat face", "curved face"],
          recap=["A face is a side of a solid. It can be flat or curved.",
                 "An edge is where two faces meet. An edge can be straight or curved.",
                 "A corner is a pointed place on a solid.",
                 "Flat and curved parts help you tell solids apart."],
          items=[
              FIO("ch2.q3", "Let us Do, Q3",
                  "Name the shapes:\n"
                  "• with no edges.\n"
                  "• with only flat faces.\n"
                  "• with only curved faces.\n"
                  "• with both straight and curved edges.\n"
                  "• with both flat and curved faces.",
                  ["Think of the five solids: cube, cuboid, cylinder, cone and sphere.",
                   "Check the faces and the edges of each one."],
                  "Sample answer: No edges: sphere. Only flat faces: cube and cuboid. Only curved faces: sphere. "
                  "Both straight and curved edges: none of the five. Both flat and curved faces: cylinder and cone.",
                  kind="exercise"),
              FIO("ch2.do8", "Let us Do, from a distance",
                  "Here is a house made of solid shapes. Imagine you stand far away from it. "
                  "What parts of the shapes can you still see? The parts are faces, edges and corners.",
                  ["Look at the house from far away.", "Say which parts you can still see."],
                  "Sample answer: the faces. From far away, the big faces are the easiest to see. "
                  "Your maths book gives no answer, so this is our own reading. Your answer may differ.",
                  kind="prompt"),
          ])],
    topic_type="instructional"))

# ---- T4: Shapes in Real Constructions (note rows 7 and 8) -> Tool 4 ---------------------------------------------
# PROVISIONAL, CLASH 8: the note's IMAGE SET (house, rocket, toy engine) is made ONE image concept holding one composite
# picture, because an image concept holds exactly one image. No video (the note asks for none). Tool 4 reuses this picture.
# new_context is True because a tool follows the image and the image is the only teaching before it (the flow gate asks
# for it); the picture brings the real constructions the tool then works on.
# MEDIA DECISION (CLASH 15, 16): placement main (the only teaching before Tool 4, so it cannot be pinned). The picture
# is a LOOK, the tool is the NAME, COUNT and WHERE: so the picture has no labels, no shape names, no counts and no
# position words, and it shows nothing that answers do3 to do6 or do9. It holds three panels, one model each: Jaya's
# rocket, Jaya's two-storey house (the richest of her four), Devika's toy engine. The shop toys (disc1) stay on the
# tool only; the other three houses stay for Tool 5. Style: illustration, the book's own models, so the tool matches.
# The round parts of the shop toys on the tool are shaded balls, not the book's flat discs (the user, CLASH 2 and 16).
TOPICS.append(TOPIC(
    "T4", "M2", "Shapes in Real Constructions", ["Let us Do", "Let us Discuss"], "Apply",
    "Students name and count the solid shapes in a construction and say where one shape is placed.",
    "A rocket, a house and a toy engine are made of many shapes. You name and count them.",
    [A("T4.C1", "Shapes in Real Constructions", "Understand",
       "Students notice that a rocket, a house and a toy engine are each built from several solid shapes.",
       role="image",
       textbook=["Jaya is building a rocket with different shapes.",
                 "Devika went to a shop and bought a toy engine.",
                 "Here is Devika's toy engine. It has many parts."],
       teach=["Predict first: is Jaya's rocket made of one shape or many shapes?",
              "Look closely at each model. Many separate pieces make it.",
              "One model can hold many different solid shapes."],
       key_terms=["construction"], misconceptions=["M_TOY_7"], minutes=4,
       image=IMG("Shapes in Real Constructions",
                 "One unlabelled picture of Jaya's rocket, Jaya's two-storey house and Devika's toy engine, so the "
                 "child sees that each model holds several solid shapes before Tool 4 asks for names and counts.",
                 placement="main", new_context=True, style="illustration",
                 real_life="a craft table with three toy models in three panels: Jaya's rocket, Jaya's two-storey "
                           "house and Devika's toy engine, each built from separate solid pieces",
                 shows="that each model has many separate solid pieces, not all alike. All four cuboids of the rocket "
                       "are in full view. The picture has no labels, numbers or words",
                 caption="Look at the rocket, the house and the engine. What are they made of?",
                 visuals=["jaya_rocket", "jaya_houses", "devika_toy_engine"])),
     # QUESTIONS (7, at the cap of 7; CLASH 4 and 22 are SETTLED by the user, 5 Nov 2026): the rocket (count, between, on
     # top, under), the engine, the shop toys and, last, ch2.q1c (objects made of more than one shape, a classroom search
     # with no picture; its own concept is this one, C7). The user raised the cap from 6 to 7 for this chapter only, so q1c is
     # back here. The answers are the plan's readings of the pictures (the book prints none): each begins "From the
     # picture" or "Sample answer". The round parts of the shop toys are shaded balls (CLASH 2 and 16), so disc1 names them
     # as spheres.
     DOER("T4.C2", "Identify Shapes in Constructions", "shapes_in_constructions", "Apply",
          "Students name and count the solids in a construction and say where one is using on top, under or between.",
          applies_to="T4.C1", minutes=7, misconceptions=["M_TOY_7", "M_TOY_8"],
          key_terms=["construction", "on top", "under", "between"],
          recap=["A model can be made of many solid shapes.",
                 "Name each piece. Then count each kind once.",
                 "On top, under and between tell where a piece is.",
                 "Between needs a piece on each side."],
          items=[
              FIO("ch2.do3", "Let us Do, rocket count",
                  "Jaya is building a rocket with different shapes. What shapes has she used? How many of each? "
                  "Cube: ____ Cuboid: ____ Cone: ____ Cylinder: ____",
                  ["Find the cubes and count them.", "Find the cuboids and count them.",
                   "Find the cone and the cylinder."],
                  "From the picture: cube 2, cuboid 4, cone 1, cylinder 1.",
                  kind="prompt"),
              FIO("ch2.do4", "Let us Do, rocket between",
                  "Which shape is between the red cuboid and yellow cuboid?",
                  ["Find the red cuboid and the yellow cuboid.", "Look at what stands in the middle of them."],
                  "From the picture: the orange cylinder.",
                  kind="prompt"),
              FIO("ch2.do5", "Let us Do, rocket on top",
                  "Which shape is on the top of the orange cylinder?",
                  ["Find the orange cylinder.", "Look at what sits on its top."],
                  "From the picture: the cyan cube.",
                  kind="prompt"),
              FIO("ch2.do6", "Let us Do, rocket under",
                  "Which shape is under the pink cone?",
                  ["Find the pink cone.", "Look at what is just below it."],
                  "From the picture: the lavender cube.",
                  kind="prompt"),
              FIO("ch2.do9", "Let us Do, toy engine",
                  "Devika went to a shop and bought a toy engine. Here is Devika's toy engine. It has many parts. "
                  "Count and fill. ____ red cylinder(s) ____ yellow cone(s) ____ grey cuboid(s) ____ blue cube(s)",
                  ["Count the cylinders.", "Count the cones.", "Count the cuboids.", "Count the cubes."],
                  "From the picture: 1 red cylinder and 2 yellow cones. 1 grey cuboid and 1 blue cube.",
                  kind="prompt"),
              FIO("ch2.disc1", "Let us Discuss",
                  "Here are some more toys from the toy shop. They are made up of different shapes. What shapes are "
                  "used in these toys?",
                  ["Look at each toy, from left to right.", "Name the shapes it is made of."],
                  "From the picture: toy 1: cone and cylinder. Toy 2: sphere (the red ball) and cylinder (the stick). "
                  "Toy 3: sphere (the head) and cylinder (the body). Toy 4: cube and cuboid.",
                  kind="prompt"),
              FIO("ch2.q1c", "Let us Do, Q1(c)",
                  "Name the objects that are made up of more than one shape.",
                  ["Look around the classroom.", "Find things built from two or more shapes."],
                  "Sample answer: a table with a flat top and legs, and a toy rocket. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T5: Let's Build Something! (note rows 9 and 10) -> Tool 5 --------------------------------------------------
# Position words: T4 reads where a shape is in a finished model; this video uses them to tell someone how to build one.
TOPICS.append(TOPIC(
    "T5", "M2", "Let's Build Something!", ["Let us Discuss", "Let us Play", "Let us Do"], "Apply",
    "Students build a model from solid shapes and say where each shape goes so a friend can build the same model.",
    "You build a house, a rocket or a tower. You tell a friend where each shape goes.",
    [A("T5.C1", "Let's Build Something!", "Understand",
       "Students say that a model is made by arranging solid shapes and use position words to tell where each one goes.",
       role="story",
       textbook=["Jaya made some houses using different shapes.",
                 "Try to build such houses, towers, rockets, etc., using different shapes available around you."],
       teach=["Predict first: can a friend build your model from shape names alone?",
              "Not always. A friend also needs to know where each shape goes.",
              "Start at the bottom. Say what goes next.",
              "On top of means above. Under means below.",
              "Between means one shape on each side.",
              "Say the order and the place of each shape."],
       key_terms=["model", "arrange", "on top", "under", "between"], misconceptions=["M_TOY_8"], minutes=5,
       # MEDIA: concept video kept (the note; the idea of telling a friend how to build is new and has a known
       # misconception). No image: the finished models were shown in T4 and Tool 5 holds the models to rebuild. The story
       # builds in order and does not name or count the shapes of a finished model (that was Tool 4) (CLASH 15).
       video=VID("Let's Build Something!",
                 "Jaya wants to build a house, a rocket or a tower and tells Devika where each shape goes.",
                 new_idea="making a model by arranging solid shapes and telling where each shape is placed",
                 story={"characters": ["Jaya", "Devika", "the children"],
                        "setting": "two tables in the craft corner, with a cardboard screen standing between them",
                        "situation": "For the toy show, Jaya builds a little house on her table. The dice stand side by side, with "
                                     "a gap between them. The shoebox lies on top of the dice. The birthday cap stands on its "
                                     "round base. It sits on top of the shoebox as the roof. The show needs the same house on "
                                     "Devika's table. Devika must build it "
                                     "without seeing Jaya's. Jaya first just names the pieces: the dice, the shoebox and the cap. "
                                     "Devika's house comes out wrong. Her shoebox is at the bottom, and the dice sit on top of "
                                     "it. The cap lies on its side beside the shoebox. So Jaya "
                                     "starts again from the bottom. She says where each piece goes, one piece at a time. She uses "
                                     "the words on top of, under and between. Now the two houses match. The children roll a marble "
                                     "through the gap under the shoebox. The story builds in order and never counts the pieces of "
                                     "a finished model.",
                        "problem": "Saying only what the pieces are is not enough. Devika's house comes out wrong. Jaya needs "
                                   "words for the order and the place of each piece.",
                        "thread": "The children know the names and the parts of the solids. They have looked closely at the "
                                  "rocket, the house and the engine. Now they build a model of their own and tell a friend how.",
                        "leads_to": "Tool 5, Build and Describe. The child builds a model and says where each shape goes. Then "
                                    "the child builds one from a friend's words."},
                 seconds=120)),
     # QUESTIONS (6, under the cap of 7): build, say where each shape goes, rebuild from a description (C9). do7 also asks
     # about faces and edges (the Tool 3 idea) and q10 also names shapes (the Tool 4 idea), but the main task of both is
     # the arrangement, so both stay here (CLASH 23; the user confirmed these homes on 5 Nov 2026). play1ex has a missing
     # word in the book: the printed sentence is corrected from the picture and the fix is recorded in SOLUTION_NOTES.
     # do7, disc2 and play1 are real-world activities kept as ON-SCREEN versions (CLASH 25): the child builds from shapes
     # on the screen, says the names, the straight or curved parts and where each shape sits; for play1, three shapes are
     # joined, the order is told and the friends rebuild the same model.
     DOER("T5.C2", "Build and Describe", "build_and_describe", "Apply",
          "Students arrange solid shapes into a model and describe where each shape is so others can build it.",
          applies_to="T5.C1", minutes=8, misconceptions=["M_TOY_8"], key_terms=["model", "arrange"],
          recap=["Build from the bottom. Say each shape and where it goes.",
                 "Use on top of, under and between.",
                 "A friend can build the same model from your words."],
          items=[
              FIO("ch2.do7", "Let us Do, house",
                  "Collect objects to make a house. Name the shapes, and talk about their faces and edges. Which are "
                  "straight and which are curved? Also, describe how the shapes have been arranged.",
                  ["Pick shapes on the screen and build a house.",
                   "Name each shape. Say if its faces and edges are straight or curved. Say where it sits."],
                  "Sample answer: a cube with a cone on top. The cube has flat faces and straight edges. "
                  "The cone has one flat face, one curved face and a curved edge. Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.disc2", "Let us Discuss, build",
                  "Jaya made some houses using different shapes. Try to build such houses, towers, rockets, etc., "
                  "using different shapes available around you.",
                  ["Pick some shapes.", "Put one shape on another.", "Check that your model stands."],
                  "Sample answer: a tower. A cuboid is at the bottom. A cylinder is on it. A cone is on top. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.play1", "Let us Play, Construct and Describe",
                  "Construct and Describe. Ask students to sit in groups of four or five. In each group, one student "
                  "selects any three shapes and puts them together. The student, then describes the sequence of "
                  "construction and the other students have to build the same without seeing the original one. Let "
                  "children take turns and play the game in the group.",
                  ["Pick three shapes and join them. Tell your friends the order you built them in.",
                   "Your friends build the same model without seeing yours. Take turns."],
                  "Sample answer: there is no fixed answer. The game works when your friends build the same model.",
                  kind="exercise"),
              FIO("ch2.play1ex", "Let us Play, Example",
                  "Example: The cylinder is on top of the cuboid. The cone is on the cylinder.",
                  ["Put the cuboid down first.", "Put the cylinder on top of the cuboid.",
                   "Put the cone on the cylinder."],
                  "From the picture: the cuboid is at the bottom. The cylinder is on it. The cone is on top.",
                  kind="example"),
              FIO("ch2.q8", "Let us Do, Q8",
                  "In what order is this model built?",
                  ["Put the wooden blocks and the pink cuboids at the bottom.", "Put the lower board on them.",
                   "Stand the four cylinders on the lower board.", "Put the upper board on the cylinders.",
                   "Put the four cones on the upper board."],
                  "Sample answer: blocks and pink cuboids, lower board, cylinders, upper board, cones. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.q10", "Let us Do, Q10",
                  "Name the shapes used in these models. Describe how the shapes are arranged.",
                  ["Look at models (a), (b), (c) and (d) one by one.", "Name the shapes in each model.",
                   "Say which shape is on top and which is below."],
                  "Sample answer: all four models use cuboids. In (b) a wide green cuboid sits on a stack of five. "
                  "In (d) three cuboids are stacked like steps. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T6: Building with Clay, Sticks and Cubes (note rows 11 and 12) -> Tool 6 -----------------------------------
# PROVISIONAL, CLASH 9: the note's demo ("only if needed") is made as a SHORT story video, because a tool cannot open a
# topic and one image cannot show the joining. The children join clay balls and sticks into a frame, then join cubes.
# MEDIA DECISION (CLASH 17): the video is kept as the note's optional demo, SHORT, and shows the joining only. It is a
# story, not a how-to for the tool: it ends before any count, it does not show the book's figures (q4, q5, q9, q11) and
# it says nothing about what balls and sticks stand for and teaches no hidden or visible cubes (the user's decision on
# CLASH 6, 5 Nov 2026). The optional link "8 balls are the 8 corners, 12 sticks are the 12 edges of the cuboid frame" is NOT
# in the video and NOT in new_idea: it belongs to Tool 6's feedback after the child builds the cuboid frame (briefs stage).
# new_idea is worded as ONE idea (making a solid by joining parts), because the approved Tool 6 pairs the two (CLASH 11).
TOPICS.append(TOPIC(
    "T6", "M2", "Clay, Sticks and Cubes", ["Let us Do"], "Apply",
    "Students join clay balls and sticks, and cubes, to make solid shapes and say how many cubes a shape uses.",
    "You join clay balls and sticks into a frame. You join cubes into bigger shapes.",
    [A("T6.C1", "Building with Clay, Sticks and Cubes", "Understand",
       "Students describe how clay balls and sticks make a frame and how cubes join to make a bigger shape.",
       role="story",
       textbook=["Look what I made with clay and sticks! You can also try to make such shapes."],
       teach=["Predict first: can small parts join to make a bigger shape?",
              "Yes. Clay balls and sticks join to make a frame.",
              "A frame is a shape you can see through.",
              "Small cubes join face to face to make a bigger solid.",
              "Join small parts to make a bigger shape."],
       key_terms=["clay ball", "stick", "frame", "cube"], misconceptions=[], minutes=5,
       video=VID("Building with Clay, Sticks and Cubes",
                 "The children join clay balls with sticks to make a frame, then join cubes to make a bigger shape, "
                 "showing the joining only, with no count, no hidden cubes and no meaning given to balls and sticks.",
                 new_idea="a solid shape can be made by joining parts: balls and sticks make a frame, cubes make a bigger solid",
                 story={"characters": ["Jaya", "Devika", "the children"],
                        "setting": "the craft corner at the end of a busy day",
                        "situation": "The toy show shelf is full. The old boxes are all used up. The children still want a big toy "
                                     "for the middle of the table. Jaya finds clay, a bundle of thin sticks and a pile of "
                                     "small cubes. She rolls clay into balls. She presses a stick into two balls to join them. She "
                                     "keeps joining until she has a see-through frame. The frame stands on the table. Devika joins "
                                     "small cubes face to face to make a longer block. Then she makes a bigger shape that stands "
                                     "by itself. The children set the frame and the cube shape in the middle. The story shows the "
                                     "joining only. It counts nothing and gives no meaning to the balls or the sticks.",
                        "problem": "There are no old boxes left. The children need a big shape for the middle of the table. They "
                                   "find that small parts can be joined to make one.",
                        "thread": "In the last story the children built models by stacking toys. Now the toys have run out. So "
                                  "they make new shapes by joining small parts.",
                        "leads_to": "Tool 6, Build with Clay, Sticks and Cubes. The child joins clay balls and sticks, then joins "
                                    "cubes."},
                 seconds=100)),
     # QUESTIONS (7, at the cap of 7; CLASH 4 and 22 are SETTLED by the user, 5 Nov 2026): clay and sticks (q4), cubes (q5,
     # say1, say2, q9, say3, q11). The user raised the cap to 7 for this chapter only, so the speech bubble ch2.say3 ("What
     # possible shapes do you get if you join 3 cubes?") is its OWN item again, right after q9, asked on q9's screen (the
     # same picture of 3 joined cubes); it is no longer only listed under `ncert`. q9 and say3 are stretches whose home the
     # user confirmed (CLASH 5), and "ways" against "shapes" is a printed-book difference (SOLUTION_NOTES).
     # CLASH 6 is DECIDED (5 Nov 2026): no hidden-cube teaching, and the words "hidden" and "visible" are never used with the
     # child. ch2.say2 stays as the book's question, but the on-screen stack is the PLAN'S OWN stack of cubes in which every
     # cube can be seen or counted by turning it (no cube is behind another), so the child never has to work out a cube they
     # cannot see; the briefs stage fixes that stack and its total. The tag M_TOY_9 (hidden cubes) is REMOVED from this tool:
     # no question needs it. The balls = corners, sticks = edges link is NOT a question: it stays in this tool's feedback
     # (briefs stage) and no question was added for it. q4, q5, q9 and q11 are real-world activities kept as ON-SCREEN
     # versions (CLASH 25): the child places clay balls and sticks, or joins cubes or dice, on the screen.
     DOER("T6.C2", "Build with Clay, Sticks and Cubes", "clay_sticks_cubes", "Apply",
          "Students make solid shapes from clay balls and sticks and from cubes, and count the cubes used.",
          applies_to="T6.C1", minutes=8, misconceptions=["M_TOY_5"],
          key_terms=["clay ball", "stick", "frame", "cube"],
          recap=["Joined parts make a shape.",
                 "Cubes join face to face.",
                 "Turning a shape does not change it.",
                 "Count each cube once."],
          items=[
              FIO("ch2.q4", "Let us Do, Q4",
                  "Which shapes can you build? Look what I made with clay and sticks! You can also try to make such "
                  "shapes.",
                  ["Look at the two shapes.", "Put a clay ball on each dot, then join the balls with sticks."],
                  "From the picture: one shape has 4 clay balls and 6 sticks. The other is a cuboid frame with "
                  "8 clay balls and 12 sticks.",
                  kind="exercise"),
              FIO("ch2.q5", "Let us Do, Q5",
                  "Try to make these shapes using cubes.",
                  ["Look at each picture.", "Join cubes on the screen until your shape matches it."],
                  "From the picture: the green shape has three arms. The pink shape looks like a plus sign. "
                  "Check your model against each picture.",
                  kind="exercise"),
              FIO("ch2.say1", "Let us Do, bubble (cube and cuboid)",
                  "What shape do you get if you join a cube and a cuboid?",
                  ["Join a cube to a cuboid.", "Look at the new shape."],
                  "Sample answer: a longer cuboid, when the cube joins the end of the cuboid. Your answer may differ.",
                  kind="prompt"),
              FIO("ch2.say2", "Let us Do, bubble (how many cubes)",
                  "How many cubes are used to make this shape?",
                  ["Count the cubes, one at a time.", "Turn the shape and count again to check."],
                  "From the picture: the stack has 10 cubes. There are 4 cubes in the tallest column, then 3, 2 "
                  "and 1. 4 + 3 + 2 + 1 = 10. Your two counts should match.",
                  kind="prompt"),
              FIO("ch2.q9", "Let us Do, Q9",
                  "In how many different ways can you join 3 cubes? Try and see.",
                  ["Join 3 cubes face to face.", "Turn the shape and look at it.", "Try a different way to join them."],
                  "Sample answer: 3 cubes in a straight row, or bent like an L. Your answer may differ.",
                  kind="exercise"),
              FIO("ch2.say3", "Let us Do, Q9 bubble",
                  "What possible shapes do you get if you join 3 cubes?",
                  ["Look at the shapes you made with 3 cubes.", "Say what each shape looks like."],
                  "Sample answer: a long cuboid, or an L shape. Your answer may differ.",
                  kind="prompt"),
              FIO("ch2.q11", "Let us Do, Q11",
                  "Use six dice to make the following shapes: (a) a cuboid (b) a tower (c) any other shape of your "
                  "choice",
                  ["Join 6 dice on the screen to make each shape."],
                  "Sample answer: (a) 6 dice in one row, or 2 rows of 3. (b) 6 dice stacked one on top of another. "
                  "(c) steps made of 3, 2 and 1 dice. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T7: How Are Shapes Different? (note rows 13 and 14) -> Tool 7 ----------------------------------------------
# PROVISIONAL, CLASH 8: the note's COMPARISON IMAGE in the main flow, no video. One image concept, one picture.
# CLASH 2 is DECIDED BY THE USER (5 Nov 2026): the cube beside the cuboid is the core of the image and of the topic; a
# sphere is only ever a shaded real ball; a flat circle is optional and not compulsory. So the topic and concept
# objectives, the key terms and Tool 7 speak of the cube and the cuboid (and the solids of Q6) only. The ball beside a flat
# paper circle stays in the photo ONLY as a smaller, clearly secondary pair (the media minimiser's judgement, for the user
# to overrule): if the photo looks crowded it is dropped and nothing else changes.
# MEDIA DECISION (CLASH 18): placement main (no video, the only teaching before Tool 7). The picture SHOWS and does not
# TELL: the pairs side by side at the same angle, with no sentence on the differences and not the question of Q6,
# because Tool 7 is where the child says them. Style PHOTO of real objects: Tool 7 draws the solids in the chart colours,
# so real objects are the new context, and a real ball shows the thickness that a drawn disc cannot (M_TOY_1).
TOPICS.append(TOPIC(
    "T7", "M3", "How Are Shapes Different?", ["Let us Do"], "Analyze",
    "Students compare a cube with a cuboid and other solids and say how they are alike and different.",
    "You compare shapes and say how they are alike and how they are different.",
    [A("T7.C1", "How Are Shapes Different?", "Understand",
       "Students say how a cube and a cuboid are alike and different, and that a cube is a special cuboid.",
       role="image",
       textbook=["Note that a cube is a special type of cuboid."],
       ncert=["ch2.fact1"],
       teach=["Predict first: can a die also be called a cuboid?",
              "Yes. A cube is a special cuboid.",
              "All the faces of a cube are the same size. The faces of a cuboid can be different sizes.",
              "Every cube is a cuboid, but not every cuboid is a cube."],
       key_terms=["cube", "cuboid", "same", "different"], misconceptions=["M_TOY_2", "M_TOY_1"], minutes=4,
       image=IMG("How Are Shapes Different?",
                 "One photo of real objects, so the child sees a cube and a cuboid side by side before Tool 7 asks them "
                 "to say the differences. Main pair: a die (or a plain cube-shaped box) beside a closed shoebox. "
                 "Secondary pair, smaller and optional: a real ball beside a flat paper circle, which Tool 7 does not "
                 "need. Real objects are the new context: Tool 7 draws the solids in chart colours.",
                 placement="main", new_context=True, style="photo",
                 real_life="two real pairs on a plain table in even light, shot from one angle: a large die with "
                           "clear dots beside a closed shoebox of the same height, and a smaller football beside a "
                           "flat paper circle in one corner",
                 shows="a cube and a cuboid side by side, at the same angle and in the same light. A smaller round "
                       "ball sits beside a flat paper circle. The photo has no words, labels or arrows",
                 caption="Look at the two big objects side by side. What do you notice?",
                 visuals=["die", "shoebox", "football", "flat_circle"])),
     # QUESTIONS (1): q6, the book's only compare question. Its green round shape is a flat disc in the book; the user
     # decided (CLASH 2) that the plan draws it as a shaded ball, so the child compares FIVE solids: a cylinder, a cube, a
     # cone, a cuboid and a ball (sphere). The sample answer is re-read for that and says nothing of a flat disc.
     DOER("T7.C2", "Compare and Discover", "compare_and_discover", "Analyze",
          "Students compare solids and say in what ways they are the same and in what ways they are different.",
          applies_to="T7.C1", minutes=7, misconceptions=["M_TOY_2"],
          key_terms=["cube", "cuboid", "same", "different"],
          recap=["Look at the faces, the edges and the corners to compare two solids.",
                 "Two solids can be the same in some ways and different in others.",
                 "A cube is a special cuboid."],
          items=[
              FIO("ch2.q6", "Let us Do, Q6",
                  "In what ways are these shapes the same? In what ways are they different?",
                  ["Look at the faces of each shape.", "Look at the edges of each shape."],
                  "Sample answer: all five are solid shapes. The cube and the cuboid have only flat faces. "
                  "The cylinder and the cone have flat and curved faces. The sphere is a ball. It has only a curved "
                  "face and no edges. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T8: Shape Challenges and Games (note row 15) -> Tool 8 -----------------------------------------------------
# CLASH 10 and CLASH 3 are DECIDED BY THE USER (5 Nov 2026): the note puts nothing before Tool 8, but a tool cannot open a
# topic, so the lead-in is ONE image concept: a die with three visible faces and a visual setup that creates curiosity
# about the hidden opposite faces, without giving the answer. Tool 8 stays application with no new concept. The picture
# must NOT print the pattern: the book's question on the tool (what is opposite 1, 2, 3, and what pattern) is still the
# child's to answer.
# MEDIA DECISION (CLASH 19): placement main. ONE illustration. SETUP: a plain white die with black dots tucked into the
# corner where two upright maths books meet on a desk, seen from the open side. The top and two side faces show, with
# exact dot counts; the underside (on the desk), the back and one side (against the books) are out of sight, so the child
# wonders what is on them. The visible numbers meet at one corner of a usual die and are not 6, 5, 3 (Q7's picture) nor
# 1, 2, 3 (it would hint at 4, 5, 6 behind them); for example 1, 4 and 5. Never two views, a mirror, a face together
# with its opposite, a sum of 7, a pattern or arrows. It teaches only that every face has an opposite out of sight.
# Style illustration (not photo): the dot counts must be exact and the setup controlled.
TOPICS.append(TOPIC(
    "T8", "M3", "Shape Challenges and Games", ["Let us Play", "Let us Do"], "Apply",
    "Students find the face opposite a given face on a die and use the shapes they have met to solve shape "
    "challenges.",
    "You find the face opposite another on a die. Then you take the shape challenges.",
    [A("T8.C1", "Opposite Faces of a Die", "Understand",
       "Students point to the face opposite a given face on a die.", role="image",
       textbook=["Talk about opposite faces in cubes, cuboids and cylinders."],
       teach=["Predict first: what is on the faces of the die that you cannot see?",
              "A die has 6 faces. Here you can see only 3.",
              "Every face has one face straight across from it.",
              "That face is its opposite face."],
       key_terms=["die", "opposite face"], misconceptions=["M_TOY_10"], minutes=4,
       image=IMG("Opposite Faces of a Die",
                 "One illustration of a plain die tucked into the corner of two upright books on a desk: three faces show "
                 "and the other three are out of sight against the books and the desk, so the child wonders what is "
                 "on them. No pair of opposite faces, no sum of 7, no pattern and no arrows: Tool 8 leaves them to find.",
                 placement="main", new_context=True, style="illustration",
                 real_life="a plain white die with black dots in the corner where two upright maths books meet on "
                           "a desk, seen from the open side. The book covers are plain, with no title or writing",
                 shows="three faces of the die in view: 1 dot on top, 5 dots on the left and 4 dots on the right, as "
                       "on a standard die. The other three faces are out of sight against the books and the desk. "
                       "There is no other dot, number, mirror, second view or arrow",
                 caption="You can see three faces. What could be on the faces you cannot see?",
                 visuals=["die"])),
     # QUESTIONS (2, under the cap of 7; CLASH 22 is SETTLED by the user, 5 Nov 2026): q7 (opposite faces, CLASH 3) and play2
     # (the board game). ch2.q1c is back on Tool 4, its own concept (the cap is now 7), so Tool 8 holds q7 and play2.
     # Q7's picture shows only the faces 6, 5 and 3 and cannot answer its own question (printed-book error): the answer is the
     # plan's reading from a usual die, labelled "Sample answer", and is recorded in SOLUTION_NOTES. play2 is a real-world
     # activity kept as an ON-SCREEN version (CLASH 25): the game board on the screen is the plan's own and every picture
     # on it is a real object that really is one of the five solids (a football, a die, a shoebox, a bottle, a birthday
     # cap and the like), never the book's cake slice, clay pot, watermelon or roti stack (CLASH 26). The book's border has
     # no key for which picture belongs to which number (printed-book error 9), so the brief writer defines the board.
     DOER("T8.C2", "Shape Challenges and Games", "shape_challenges", "Apply",
          "Students recognise solid shapes, even when turned, and read the opposite faces of a die.",
          applies_to="T8.C1", minutes=8, misconceptions=["M_TOY_10", "M_TOY_6"],
          key_terms=["die", "opposite face"],
          recap=["A turned solid is still the same solid.",
                 "Every face of a die has an opposite face.",
                 "Look for the shape first, then move on the board."],
          items=[
              FIO("ch2.q7", "Let us Do, Q7",
                  "Look at a die. The faces have 1 to 6 dots. What number is on: the face opposite number 1? "
                  "the face opposite number 2? the face opposite number 3? What pattern do you notice?",
                  ["Look at a real die.", "Find the face opposite 1, then 2, then 3."],
                  "Sample answer: on a usual die, 1 is opposite 6. 2 is opposite 5. 3 is opposite 4. "
                  "The pattern: each pair adds up to 7. 1 + 6 = 7. 2 + 5 = 7. 3 + 4 = 7.",
                  kind="exercise"),
              FIO("ch2.play2", "Let us Play, board game",
                  "There is a game along the border of the pages in your maths book. You can play it on the screen. "
                  "Roll the die and move the counter to the next picture associated with the number on the die "
                  "(if possible without crossing the 'Finish' square) and play the game with your friends. The one "
                  "who reaches the finish mark first wins the game. 1 dot: Cylinder. 2 dots: Sphere. 3 dots: Cone. "
                  "4 dots: Cube. 5 dots: Cuboid. 6 dots: Move 2 steps forward if possible.",
                  ["Roll the die. Find the shape for your number.",
                   "Move to the next picture of that shape. If that would cross Finish, stay."],
                  "Sample answer: there is no fixed answer. The first player to reach the Finish square wins.",
                  kind="exercise"),
          ])],
    topic_type="instructional"))

# ---- T9: the review (note row 17, Chapter Check) ----------------------------------------------------------------
# A short look back with pictures already used, nothing new: no new video, tool, book item or key term (CLASH 14).
# C1 covers recognition and properties, C2 covers constructions and reasoning. Together they revise every idea topic.
# MEDIA DECISION (CLASH 20): the review holds no video, image or tool node of its own. The Chapter Check is "visual" by
# showing again the pictures already made for T4, T7 and T8 (and the tool models), by reference; a second copy would be
# flagged as a duplicate and a new picture would be new content.
TOPICS.append(TOPIC(
    "T9", "MLAST", "Chapter Check", ["Review"], "Understand", "",
    "A short look back at the shapes, their parts and the models you made.",
    [A("T9.C1", "Name the Shape and Its Parts", "Understand",
       "Students name a solid shape, point to its faces, edges and corners and tell how two shapes are alike and "
       "different.",
       role="review", key_terms=["cube", "cuboid", "cylinder", "cone", "sphere", "face", "edge", "corner", "same",
                                 "different"],
       teach=["Look at the die and the shoebox in the photo. Name each solid.",
              "A die is a cube. A shoebox is a cuboid.",
              "Point to a face, an edge and a corner on the shoebox.",
              "Think of a football. Does it have an edge or a corner?",
              "A football has one curved face. It has no edges and no corners.",
              "Say one way a cube and a cuboid are the same. Say one way they differ."],
       review_covers=["T2.C1", "T3.C1", "T7.C1"], minutes=4),
     A("T9.C2", "Shapes in Models and Dice", "Understand",
       "Students name and count the shapes in a model, say where each one is and find the face opposite another on "
       "a die.",
       role="review", key_terms=["construction", "model", "on top", "under", "between", "cube", "die",
                                 "opposite face"],
       teach=["Look again at Jaya's rocket, the house and the engine.",
              "Is each model made of one shape or of many shapes?",
              "Pick one piece and say where it is. Use on top of, under or between.",
              "Say how you build a model. Start at the bottom and go up.",
              "Think of the clay frame and the joined cubes. Small parts can join to make a bigger shape.",
              "Look at the die in the corner of the books. Every face has an opposite face."],
       review_covers=["T4.C1", "T5.C1", "T6.C1", "T8.C1"], minutes=4)],
    topic_type="summary"))

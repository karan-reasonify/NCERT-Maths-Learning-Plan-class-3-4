# -*- coding: utf-8 -*-
"""Class 4, Chapter 1 "Shapes Around Us": the tool entries, one per approved tool, in the approved order.

STRUCTURE (steps 2 to 5, locked and approved on 6 Nov 2026): tool_id, title (EXACTLY the approved name), approved_no, ONE
learning objective, and for Tool 1 its 3 `notice` prompts. BRIEFS (step 6, the brief writer): screen, controls, instruction,
feedback, done_when, shared_state, the four hints and the full `visuals` list. Nothing structural was changed here.

The 22 tools are the pipeline's PROPOSAL, approved by the user (CLASH 1 and 34 in content.py). The concept each tool serves and
the book items homed on it are in tool_map.locked.md and question_map.md. The tool's questions are NOT written here: they are
the book's items (FIO in topics_1.py), placed once each.

How every spec is written (the user's brief, three phases in every tool):
  PHASE 1, get ready      a simple picture from the story or picture just before; one line of what to do; no score.
  PHASE 2, play           the child acts on the objects (drag, tap, turn, fold, draw, push, count, measure) and gets
                          immediate feedback that explains the result; hints, retry and Reset are always there.
  PHASE 3, the book's questions   the book's own questions, one at a time, each answered by doing it on the same screen.
  The frame is the same in every tool (progress dots, Back, Next, Hint; Reset is a control), so the child learns it once.

Rules every tool follows:
- one colour per solid (prisms blue, pyramids magenta, cube teal, cuboid red, sphere a lighter coral red, cone yellow,
  cylinder soft orchid); every solid a shaded 3D solid, a sphere a shaded ball; real objects, the die, the colour cube, nets,
  the border sketches and the hidden-shapes outlines keep their own look (VISUAL_KEY says which);
- every answer the tool shows begins exactly From the picture or Sample answer (open tasks end Your answer may differ);
- nothing in a tool gives a teacher a role, and no text repeats a printed-book error (content.SOLUTION_NOTES);
- anything the plan itself made up on a screen (a helper tray, a rule, a reading) is labelled as the plan's own.

Every tool is a spec and a placeholder: nothing below is built yet.
"""
from __future__ import annotations

from topics_common import T  # noqa: F401

# The frame is the same in every tool, so it is written once.
FRAME = ("Frame as in every tool: progress dots on top, Back and Next at the sides, a Hint button. Book questions come "
         "one at a time, each in a small panel with its answer choices, such as cards, numbers or Yes and No. Every answer "
         "the tool shows starts with From the picture or Sample answer. ")

TOOLS = {
    # ---- Module 1: solid shapes (Tools 1 to 9)
    "blocks": T(
        "tool_blocks_for_buildings", "Blocks for Buildings", 1,
        "Students pick solid shapes for the roof, pillars and base of a building and compare the model with the real building.",
        notice=["Which blocks stand firm on the floor, and which ones roll?",
                "Which block could you use more than once?",
                "What changes when you swap one block for another?"],
        screen=FRAME +
        "PHASE 1, get ready: Diksha's mat from the story. Her wooden blocks lie in front of the India Gate drawing. One line "
        "says, Help Diksha build a model. Nothing is scored. "
        "PHASE 2, play: three buildings sit on top: India Gate, the sandy-brown gateway with tall minarets and the round "
        "thatched hut. Pick one. Drag blocks from the tray to a base pad, pillar pads and a roof pad. Every block in the tray "
        "can be used again and again. A block that cannot rest where it is put rolls or slides away, so you see which blocks "
        "stand firm. Tap Compare to put your model beside the real building. No block has a shape name written on it. "
        "PHASE 3, the six questions of your maths book: build the model, tap the parts you used (roof, pillars, base), pick "
        "why you chose them, pick a block for each part, then pick what is alike and what is different when the model sits "
        "beside the picture.",
        controls=["Drag a block", "Tap a block to turn it", "Tap Compare", "Reset"],
        instruction="Pick blocks for the roof, the pillars and the base. Build the model.",
        feedback=["A block on a flat pad stays. The pad names its part: base, pillars or roof.",
                  "A block that cannot rest rolls or slides off. It says, This block rolls on its curved side.",
                  "Compare puts your model beside the real building. Matching parts glow. Missing parts show, such as windows and colours.",
                  "No try is wrong here. A different set of blocks makes a different model. Your answer may differ."],
        done_when="A model stands with a base, pillars and a roof, Compare has been opened, and the six book questions are answered.",
        shared_state=["chosenBuilding", "placedBlocks", "partsUsed", "compareOpen"],
        hints=["Look at the picture of the building. Find its top, its tall sides and its bottom.",
               "Pick a block for each part. Ask: will it stand firm, or will it roll?",
               "Try a long flat block for the base. Stand a tall block on each side for the pillars.",
               "Lay a flat block across the top of the pillars for the roof. Then tap Compare."],
        visuals=["wooden_blocks", "india_gate_drawing", "other_buildings", "diksha"]),
    "prism_pyramid": T(
        "tool_prism_or_pyramid", "Prism or Pyramid", 2,
        "Students name the face shape all prisms share and the faces all pyramids share, and decide whether a cube is also a prism.",
        screen=FRAME +
        "PHASE 1, get ready: Diksha's father's two sets from the story stand on two shelves. The shelf of prisms holds three "
        "blue solids: triangular, square and hexagonal. The shelf of pyramids holds three magenta solids: triangular, square "
        "and pentagonal. A teal cube stands on its own stand in the middle, with no family named. "
        "PHASE 2, play: turn any solid. Tap a face: it lights up and its flat shape is drawn beside the solid. A tally keeps "
        "the shapes found on each shelf. "
        "PHASE 3, the seven questions of your maths book: pick the shape card common to all prisms; name the other faces of "
        "each prism and count them; pick the shape common to all pyramids; fill in the point where the triangle faces meet; "
        "name the other shape of each pyramid, its base; then put the cube beside the square prism and say if a cube is also "
        "a prism. A line on the screen says that colour only tells the solids apart. The faces decide the family.",
        controls=["Tap a face", "Turn the solid", "Tap a shape card", "Reset"],
        instruction="Tap the faces of each solid. Which shapes do you find?",
        feedback=["A tapped face lights up and shows its shape. The tally adds one.",
                  "Right shape card: it turns green and says why. Every prism has rectangle faces. Every pyramid has triangle faces.",
                  "Wrong shape card: it shakes and shows a solid without that face. The square prism has no triangle face.",
                  "Counts: each prism has 2 faces of its other shape. The rectangle faces are 3, 4 and 6.",
                  "Cube beside the square prism: tap their faces. Both have 2 square ends. The cube's 4 sides are squares too. Colour does not decide the family. The faces do."],
        done_when="Every solid is turned and its faces are tapped, the seven book questions are answered and the cube is compared with the square prism.",
        shared_state=["selectedSolid", "tappedFaces", "tally", "chosenCards"],
        hints=["Turn one solid. Look at each flat face and name its shape.",
               "Tap the faces of the three blue solids. Which shape shows on all three?",
               "Tap the long side faces of each blue solid. Then tap the slanting faces of each magenta solid.",
               "Every prism has rectangle faces. Every pyramid has triangle faces that meet at one point."],
        visuals=["prisms", "pyramids", "solid_pictures"]),
    "faces_edges": T(
        "tool_faces_corners_and_edges", "Faces, Corners and Edges", 3,
        "Students count the faces, edges and corners of solids, find F+V−E for each and sort solids by flat faces and straight edges.",
        screen=FRAME +
        "PHASE 1, get ready: Diksha's straws and clay balls from the story lie on a table. Tap a straw: it is an edge. Tap a "
        "clay ball: it is a corner. Tap a see-through colour sheet on a side: it is a face. "
        "PHASE 2, play: the skeleton of one solid stands on a turntable: cube, cuboid, triangular pyramid, square pyramid or "
        "triangular prism. Its straws take the colour of the solid (cube teal, cuboid red, prisms blue, pyramids magenta). "
        "Every clay ball is one plain clay colour. Tap parts to count them. Three counters show faces F, corners V and edges E. "
        "PHASE 3, the five questions of your maths book: build each of the five solids from straws and clay balls and fill "
        "in the table of F, V and E; work out F+V−E in each row and say what you notice; sort nine solids by their flat "
        "faces; try to build a solid with 3 flat faces; sort seven solids by their straight edges. A grey tray, added by "
        "this plan and labelled so, catches solids that fit no column of your maths book.",
        controls=["Tap a face, corner or edge", "Drag straws and balls to build", "Drag a solid to a column", "Reset"],
        instruction="Build each solid. Tap its faces, corners and edges, then fill the table.",
        feedback=["A tapped part lights up and its counter adds one. A part counted before cannot count again.",
                  "A skeleton that closes fills with its colour. A missing straw leaves a gap.",
                  "Table row right: the row turns green. Wrong number: it shakes and the part to recount blinks.",
                  "F+V−E: each row shows its sum, such as 6 + 8 − 12 = 2. All five rows give 2. So for these five solids, F + V is 2 more than E.",
                  "Sort right: the solid stays and says why. The cone has 1 flat face and 1 curved face. Wrong column: the solid slides back and shows its count.",
                  "The pentagonal pyramid has 10 straight edges. The hexagonal prism has 18. They slide to the grey tray, because no column in your maths book fits them.",
                  "3 flat faces: flat panels alone cannot close a solid. A cylinder cut in half along its length has 3 flat faces and 1 curved face."],
        done_when="All five solids are built and counted, the table and F+V−E are filled, both sorts are done and the 3 flat faces try is made.",
        shared_state=["builtSolids", "counts", "tableRows", "sortColumns"],
        hints=["Look at one solid. A face is a side, a corner is a point and an edge is a line.",
               "Count one kind of part at a time. Tap each part once so you do not count it twice.",
               "Tap every straw of the cube one by one. Tap every clay ball too. Then tap the faces.",
               "A cube has 6 faces, 8 corners and 12 edges. Count the next solid in the same way."],
        visuals=["straws_and_clay", "prisms", "pyramids", "solid_pictures"]),
    "opposite": T(
        "tool_opposite_faces", "Opposite Faces", 4,
        "Students find the face opposite a given face and the faces that share an edge with it, on a die and a coloured cube.",
        screen=FRAME +
        "PHASE 1, get ready: the real die from the picture rests on a table. It has dots, and it is the same die as in the "
        "picture. Turn it with your finger. "
        "PHASE 2, play: tap a face, then tap another face. The tool says whether the two faces meet at an edge or are "
        "opposite and never touch. A strip writes down each opposite pair you find. A tapped face shows its number in a small "
        "chip, so you can say the face numbered 2. "
        "PHASE 3, the three questions of your maths book: find the face opposite 2, then opposite 3, then opposite 4; turn "
        "the die so 1 is on top, tap the faces that share an edge with 1, then the face that does not; then look at three "
        "views of one coloured cube and name the colour opposite red and the colour opposite yellow. A rule shows on the "
        "screen: colours seen together in one view touch each other. A face and the face opposite it are never seen together.",
        controls=["Drag to turn the die or cube", "Tap a face", "Tap a colour", "Reset"],
        instruction="Turn the die. Tap a face, then tap the face opposite it.",
        feedback=["Two faces that touch glow orange. The die turns to show the edge they share.",
                  "An opposite pair glows green. The die turns to show they never touch. The strip writes the pair, such as 2 + 5 = 7.",
                  "After 2, 3 and 4 are found, a line shows the sums. On a usual die, opposite faces add up to 7.",
                  "The faces that share an edge with 1 are 2, 3, 4 and 5. Face 6 is opposite 1. It has no common edge with 1.",
                  "Colour cube, right: the two colours are never seen in one view. Red is opposite purple. Yellow is opposite orange.",
                  "Colour cube, wrong: the two colours appear together in one view, so they touch. Try another colour."],
        done_when="The faces opposite 2, 3 and 4 are found, the faces that touch 1 are tapped, and both colour pairs are named.",
        shared_state=["dieTurn", "tappedFaces", "pairStrip", "cubeView"],
        hints=["Turn the die slowly. Look at one face and the faces next to it.",
               "Faces that touch share an edge. Opposite faces are on opposite sides.",
               "Turn the die so face 2 is on top. Look at the face on the bottom.",
               "On a usual die, opposite faces add up to 7. So the face opposite 2 is 5."],
        visuals=["die", "colour_cube"]),
    "spot_faces": T(
        "tool_spot_the_faces", "Spot the Faces", 5,
        "Students mark everyday objects by their faces and corners: rectangular, triangular or curved faces, and no corners.",
        screen=FRAME +
        "PHASE 1, get ready: a new shelf of everyday things, none of them in the picture before: a toothpaste box, a "
        "candle and a chocolate box shaped like a triangular prism. Five marks wait in a tray: a red crayon for a "
        "rectangular face, a smiley for a triangular face, a star for a curved face, a blue crayon for no corner and a "
        "pencil circle for opposite faces that look the same. One line says, Mark what you see. Nothing is scored. "
        "PHASE 2, play: you pick a mark and tap an object to put it there. You decide which marks fit each thing. A right "
        "mark stays. A wrong mark slides off and gives a short reason. The pencil circle is never marked right or wrong. "
        "It is a Sample answer, as in the fifth question. "
        "PHASE 3, the five questions of your maths book, on the pencil sketches along the border (about twenty objects), "
        "with the same tray: colour every shape with a rectangular face red; draw a smiley on shapes with a triangular "
        "face; draw a star on shapes with a curved face; colour shapes with no corner blue; circle the shapes that have "
        "the same opposite faces, using the pencil circle. "
        "Only objects whose solid is certain are checked. Where a base is out of view, the screen says so and does not mark "
        "you wrong. The fifth question can be read in more than one way. The screen shows a Sample answer under one reading, "
        "that each pair of opposite faces looks the same, with the words Your answer may differ. This reading is the "
        "plan's own.",
        controls=["Pick a mark from the tray", "Tap an object to mark it", "Tap a mark on an object to clear it", "Reset"],
        instruction="Pick a mark. Tap every object that fits it.",
        feedback=["Right mark: it stays. A line says why: the toothpaste box has flat faces with four straight sides.",
                  "Wrong mark: it slides off and says why. The flat ends of the candle are round, not rectangular.",
                  "The candle takes the star, because its side is curved. It has no corner, so it takes blue too.",
                  "The chocolate box takes the smiley for its 2 triangle ends. Its 3 long faces are rectangles, so it takes red too.",
                  "Out of view: a cheese piece or a pyramid drawing shows no base. A rectangular face is then neither right nor wrong.",
                  "Fifth question: each circle you draw is a Sample answer. Your answer may differ."],
        done_when="The shelf things are marked, the first four border instructions are done, and the circle question shows a Sample answer.",
        shared_state=["pickedMark", "markedObjects", "borderTab"],
        hints=["Look at one object. Which flat or curved faces can you see?",
               "Pick one mark. Then look for the face or the corner that mark is about.",
               "A rectangular face is flat, like a book cover. A curved face is not flat. A corner is a pointed place.",
               "Colour the die, the eraser and the gift box red. They have rectangular faces."],
        visuals=["border_objects", "everyday_objects"]),
    "sort_solids": T(
        "tool_sort_the_solids", "Sort the Solids", 6,
        "Students sort solids into two circles by a rule and place a solid that fits both rules in the overlap of two circles.",
        screen=FRAME +
        "PHASE 1, get ready: Diksha's two rope circles from the story lie on a pale green panel. They cross, and the part "
        "where they cross is the overlap. "
        "PHASE 2, play: pick any two rules from a short list: all faces look the same, has a curved face, has a triangular "
        "face, has a rectangular face. Drag the solids into the circles. A solid that fits both rules goes in the overlap, "
        "and both rule labels glow. "
        "PHASE 3, the five questions of your maths book, on four panels: (1) A, all faces look the same, and B, all faces do "
        "not look the same; (2) A, curved edges, and B, straight edges; (3) A, rectangular faces, B, triangular faces, and "
        "the overlap for both, then the question of which circle holds the triangular prism and the rectangular pyramid; "
        "(4) curved faces and flat faces, with an overlap. The rectangular pyramid is the pyramid on a rectangle base, shown "
        "with both names. Solids are shaded 3D pictures in their own colours: sphere coral red, cone yellow, cylinder "
        "orchid, cube teal, cuboid red, prisms blue, pyramids magenta. A solid that fits no rule waits outside the circles, "
        "such as the sphere on panel 2.",
        controls=["Drag a solid", "Pick a rule", "Reset"],
        instruction="Drag each solid into the circle where it belongs.",
        feedback=["Right circle: the solid stays and the rule lights up. A cone has a curved edge.",
                  "Wrong circle: the solid slides back and shows what does not fit. A cube has no curved face.",
                  "Right overlap: both rules light up together. The triangular prism has rectangular and triangular faces.",
                  "The sphere has no edges, so it stays outside both circles on panel 2.",
                  "Panel 4: the sphere has curved faces only. The cone and the cylinder are in the overlap. The cube, cuboid, prisms and pyramids have flat faces only."],
        done_when="Every solid is placed on all four panels, the overlap is used, and the question about the triangular prism and the rectangular pyramid is answered.",
        shared_state=["panel", "placements", "chosenRules"],
        hints=["Read the rule on each circle. Look at one solid and its faces or edges.",
               "Ask three things: does it fit A? Does it fit B? Does it fit both?",
               "Turn the solid. Look for flat or curved faces and straight or curved edges.",
               "A solid that fits both rules goes in the middle part, where the circles overlap."],
        visuals=["sorting_circles", "solid_pictures", "sphere", "prisms", "pyramids"]),
    "cubes": T(
        "tool_build_and_draw_cubes", "Build and Draw Cubes", 7,
        "Students build cube models, count the cubes in a tower including the hidden ones and complete cube drawings on triangular dot paper.",
        screen=FRAME +
        "PHASE 1, get ready: the small staircase of toy cubes from the picture stands on a table. Drag the model to turn it "
        "round and see its back. "
        "PHASE 2, play: drag the top layer up. It floats up with its cubes counted, then drag the next layer up. Cubes you "
        "could not see before now show. The total is the layers added: 2 + 4 + 6 = 12 for this tower. "
        "PHASE 3, the three questions of your maths book: build models A, B, C and D with unit cubes and turn each model to "
        "check it against its picture; count the cubes in the two cube towers, hidden cubes too; finish the cube drawings on "
        "triangular dot paper. Every cube is teal and has clear edges, so each one can be counted.",
        controls=["Drag cubes to move them", "Drag the model to turn it", "Drag from dot to dot to draw a line", "Reset"],
        instruction="Build the model. Drag layers up to count cubes. Join dots to draw cubes.",
        feedback=["Build right: turn the model and it matches its picture. Wrong: the cubes that differ blink.",
                  "Drag a layer up: it floats up with its count, and hidden cubes show. Toy tower: 2 + 4 + 6 = 12.",
                  "First tower: add the layers, 1 + 4 + 9 + 16 = 30. A wrong count shows the layers again, one at a time.",
                  "Second tower: the middle column has 6. Each of four stairs has 5 + 4 + 3 + 2 + 1 = 15. So 6 + 4 × 15 = 66.",
                  "Dot paper right: a line through two dots stays. The cube grows 3 diamond faces that meet at one corner. A line off the dots does not stay."],
        done_when="Models A to D are built, both towers are counted layer by layer, and both cube drawings are finished.",
        shared_state=["placedCubes", "liftedLayers", "layerCounts", "drawnLines"],
        hints=["Look at the model or tower from the front. Some cubes are behind others.",
               "Count one layer at a time. Add the layers at the end.",
               "Drag the top layer up and count its cubes. Drag the next layer up and count again.",
               "On the dot paper, join dots with straight lines to match the finished cube."],
        visuals=["cube_models", "cube_towers", "triangular_dot_paper", "toy_cube_tower"]),
    "riddles": T(
        "tool_solid_riddles", "Solid Riddles", 8,
        "Students pick or build the solid that fits clues about its faces, edges and corners, or about its straws and clay balls.",
        screen=FRAME +
        "PHASE 1, get ready: a cloth bag and a clue card from the story. The card reads, 4 faces, 4 corners, 6 edges. Tap the "
        "bag: a triangular pyramid comes out and its parts glow, so the clue and the solid fit. "
        "PHASE 2, play: pick any solid on the shelf and tap its parts. A clue card writes itself: I have some faces, some "
        "corners and some edges. Clear it and write clues for another solid. "
        "PHASE 3, the two questions of your maths book: match the six descriptions a to f to seven solid pictures and name "
        "each solid; then build solids from straws and clay balls, 12 and 8, 9 and 6, 15 and 10, 10 and 6. Straws are edges "
        "and clay balls are corners. Solids are shaded in their own colours. A few ready rings of straws and balls are the "
        "plan's own helper, labelled so. For 15 straws and 10 clay balls the tool shows the solid by its parts, two "
        "5-sided ends, and does not name it.",
        controls=["Drag a description to a solid", "Drag straws and balls to build", "Tap the bag or Check", "Reset"],
        instruction="Match each clue to a solid. Then build solids from straws and clay balls.",
        feedback=["Right match: the solid glows and its name shows. Every part of the clue ticks.",
                  "Wrong match: the card slides back. It shows a clue part that does not fit. For example, the clue says 5 faces. A cone has 2.",
                  "Clue f: the cube and the cuboid both have 6 faces, 12 edges and 8 corners. So both fit.",
                  "Build right: the counters match and the skeleton closes. It fills with the colour of its solid, and its name shows.",
                  "Build wrong: the counters show too many or too few straws or balls. A gap shows where a part is missing."],
        done_when="All six descriptions are matched and named, and the four straw and clay builds are made.",
        shared_state=["clueMatches", "strawCount", "ballCount", "builtSkeleton"],
        hints=["Read one clue at a time. Count the parts of each solid on the shelf.",
               "Cross out the solids that do not fit the first clue. Then use the next clue.",
               "For a build, remember: straws are edges and clay balls are corners.",
               "A solid with 5 faces, 5 corners and 8 edges is the square pyramid. Try the next clue in the same way."],
        visuals=["solid_pictures", "sphere", "straws_and_clay", "pyramids"]),
    "fold_net": T(
        "tool_fold_the_net", "Fold the Net", 9,
        "Students match nets to solids, test which nets fold into a given solid and find the solid from its net pieces.",
        screen=FRAME +
        "PHASE 1, get ready: Diksha's pink box net from the story lies flat with its dotted fold lines. Tap Fold: it closes "
        "into the box. Tap Open: it lies flat again. "
        "PHASE 2, play: tap Fold on any net. If every face lands on a side and the shape closes, the net works. If flaps "
        "overlap or a gap is left, the fold stops and says the net does not close. Nets are line drawings with dotted folds. "
        "A net is never coloured like its solid. "
        "PHASE 3, the four questions of your maths book: the six nets from the end of the book wait on the screen. Fold each "
        "net and drag it to the solid it makes, three prisms and three pyramids. Match four nets to four solids. Fold four "
        "nets to see which close into the solid below them. Lay out the pieces Nitesh cut, 1 pentagon and 5 triangles, and "
        "pick the solid they make from four solids a to d.",
        controls=["Drag a net or a piece", "Tap Fold or Open", "Tap a solid", "Reset"],
        instruction="Fold the net. Does it close into the solid? Match it to its solid.",
        feedback=["A net that closes folds up face by face. The solid appears in its own colour, and the net glows green.",
                  "A net that does not close stops folding. It says, This net does not close into the solid. Fold it again to check.",
                  "Right match: the net slides to its solid and both glow. Wrong match: the net slides back.",
                  "Nitesh's pieces fly together and close up. They make the pentagonal pyramid, with one 5-sided base and 5 triangle faces.",
                  "Pieces and a solid: the right solid has the same faces as the pieces."],
        done_when="All six nets are folded and matched, the four nets are matched and tested, and Nitesh's pieces are matched to a solid.",
        shared_state=["netPositions", "foldState", "matches", "pieceTable"],
        hints=["Look at the faces of the net. Count them and name their shapes.",
               "Tap Fold and watch. Does each face land on a side without covering another?",
               "Count the pieces of Nitesh's net: 1 pentagon and 5 triangles. Find the solid with those faces.",
               "A net closes into a solid when its faces match the solid's faces."],
        visuals=["box_net", "nets_and_solids", "nitesh"]),
    # ---- Module 2: angles and rigid shapes (Tools 10 to 15)
    "lines_meet": T(
        "tool_when_lines_meet", "When Lines Meet", 10,
        "Students make an angle by meeting two lines at a point, and mark and count the angles in pictures.",
        screen=FRAME +
        "PHASE 1, get ready: Isha's two straws from the story lie on a table, apart. "
        "PHASE 2, play: drag the ends of the straws until they meet at a clay ball. A red arc shows the angle. Swing one "
        "straw: the arc grows or shrinks. Stretch a straw longer: the angle stays the same. Then tap the place where two "
        "limbs meet on five yoga figures: an arc appears. "
        "PHASE 3, the four questions of your maths book: tap each angle of the house until the count reaches 7; tap each "
        "marked angle of the boat and count them; tap the angles in five pictures, scissors, hanger, hand, seesaw and slide; "
        "then tap places where two lines meet in a classroom picture with a desk, a blackboard, a door, a window and a clock.",
        controls=["Drag a straw end to swing or stretch it", "Tap where two lines meet", "Reset"],
        instruction="Meet two straws at a point. Then tap each angle you find.",
        feedback=["Straws that meet show a red arc, the angle. Straws that do not touch show no angle.",
                  "Swing a straw: the arc changes size. Stretch a straw: the arc stays the same. A longer line does not make a bigger angle.",
                  "Right tap: a red arc appears where two lines meet. The count adds one.",
                  "Wrong tap: only one line is here, or none. An angle needs two lines that meet at a point.",
                  "House: 1 + 2 + 2 + 2 = 7 angles. Boat: 4 + 2 + 2 + 2 = 10 marked angles."],
        done_when="Two straws are met at a point, the house shows 7 and the boat 10, five pictures are marked and three angles are found in the classroom picture.",
        shared_state=["strawPositions", "markedAngles", "angleCount", "sceneTaps"],
        hints=["Look for two lines that meet at one point.",
               "Find the point where the two lines touch. The angle is there.",
               "In the scissors, tap the point where the two blades meet.",
               "On the boat, tap each red mark once. The count goes up by one each time."],
        visuals=["straws_angle", "angle_mark", "yoga_figures", "house_and_boat", "angle_pictures", "classroom_scene"]),
    "right_checker": T(
        "tool_right_angle_checker", "Right Angle Checker", 11,
        "Students make a paper right angle, use it to test the corners of shapes and objects, and draw right angles on a dot grid.",
        screen=FRAME +
        "PHASE 1, get ready: the paper checker from the story lies on a desk, with a red square on its folded corner. "
        "PHASE 2, play: lay the checker on three test corners: a postcard corner, the same postcard turned on its side, and "
        "a pointed paper corner. A corner that fits exactly lights up as a right angle. Turn the checker round: it still "
        "fits a right angle. "
        "PHASE 3, the four questions of your maths book: fold a new sheet twice to make your own checker; look at eight "
        "angles on a dot grid, lay the checker on each and circle the right angles; lay the checker on corners in a "
        "classroom picture, a book, a window, a door and a desk, and list where right angles are; draw right angles on a dot grid.",
        controls=["Fold the paper", "Drag and turn the checker", "Tap or draw on the grid", "Reset"],
        instruction="Fold your checker. Lay it on a corner. Does it fit exactly?",
        feedback=["Fold right: the second fold lies on the first. A red square marks the corner where the folds meet.",
                  "A corner fits: it lights up and says, right angle. A turned corner that fits is still a right angle.",
                  "A corner does not fit: a gap or an overhang shows. It is not a right angle.",
                  "Circle right: the angle stays circled. Wrong circle: the checker shows the gap, and the circle rubs out.",
                  "Draw right: a red square appears when the checker fits your corner. A line across the dots and a line straight up from its end work. A turned square corner works too."],
        done_when="A checker is folded, the eight dot-grid angles are checked, objects with right angles are listed and some right angles are drawn.",
        shared_state=["foldStep", "checkerPose", "circledAngles", "drawnLines"],
        hints=["Fold the paper in half. Then fold it in half again.",
               "Lay the corner of the checker on the angle. Put one arm of the checker on one line.",
               "Does the other arm lie on the other line? If it does, the angle is a right angle.",
               "On the dot grid, draw a line across the dots. Then draw a line straight up from its end."],
        visuals=["right_angle_checker", "dot_grid", "angle_mark", "classroom_scene"]),
    "acute_obtuse": T(
        "tool_acute_or_obtuse", "Acute or Obtuse", 12,
        "Students tell an acute angle from an obtuse angle by comparing it with a right angle, and draw and mark both kinds.",
        screen=FRAME +
        "PHASE 1, get ready: a dashed upright line shows a right angle against a flat bottom line. A paper checker lies "
        "beside it. "
        "PHASE 2, play: swing a second line out from the bottom line. In this tool only, an angle smaller than a right angle "
        "shows red and says acute, the same size shows green and says right, and a bigger one shows blue and says obtuse. "
        "These are the colours your maths book asks for. "
        "PHASE 3, the six questions of your maths book: tap objects with acute angles, then objects with obtuse angles, in a "
        "classroom picture where you drag the door or a clock hand to swing it; tap the places where two strokes meet in the "
        "letters V, A and Z; draw acute angles on a dot grid and add a line to make an acute angle from each given line; do "
        "the same for obtuse angles; colour the angles of four stick figures red, green or blue.",
        controls=["Drag a line, a door or a clock hand to swing it", "Draw on the dots", "Tap an angle to colour it", "Reset"],
        instruction="Swing the line. Is the angle smaller, the same or bigger than a right angle?",
        feedback=["Smaller than the dashed right angle: red, acute. The same: green, right. Bigger: blue, obtuse.",
                  "Drag the door open a little: red, acute. Drag it wide: blue, obtuse. Drag a clock hand to 2 o'clock: red, acute. Drag it to 4 o'clock: blue, obtuse.",
                  "V has 1 acute angle. Z has 2 acute angles. In A, tap each place where strokes meet. The tool names each angle and gives no count.",
                  "Your drawn line is checked against the right angle. Less gives acute. More gives obtuse. A line on the right angle makes a right angle. The question asks for another kind.",
                  "Stick figures: the right colour stays. A wrong colour shows the angle beside the right angle, so you can compare."],
        done_when="The classroom objects are tapped, the letters are marked, acute and obtuse angles are drawn, and the four stick figures are coloured.",
        shared_state=["swingAngle", "doorOpening", "clockTime", "drawnAngles", "angleColours"],
        hints=["Look at the dashed line. It shows a right angle.",
               "Compare your angle with the dashed line. Is it inside it or outside it?",
               "Swing the line until it lies on the dashed line. Then swing it back.",
               "Smaller than the dashed line is acute. Bigger is obtuse. The same is a right angle."],
        visuals=["dot_grid", "angle_mark", "right_angle_checker", "stick_figures", "classroom_scene", "angle_letters"]),
    "push_straws": T(
        "tool_push_the_straw_shapes", "Push the Straw Shapes", 13,
        "Students push one side of a straw triangle and a straw rectangle and say which one keeps its shape.",
        screen=FRAME +
        "PHASE 1, get ready: Isha's triangle and rectangle of straws and clay lie on a table, as in the story. "
        "PHASE 2, play: drag a side or a clay ball to push it. Each clay ball turns like a joint. Watch what each shape does. "
        "PHASE 3, the seven questions of your maths book: build a triangle from 3 straws of different lengths; push one side "
        "and answer Yes or No; trace the triangle in your notebook, an offline step answered with the card I did it; drag "
        "the right angle checker onto its corners and say what kinds of angles a triangle has; build a rectangle from 2 "
        "long and 2 short straws; check "
        "its angles; push one side and answer Yes or No. After both pushes a line says that the triangle is the most rigid shape.",
        controls=["Drag a straw to a clay ball", "Drag a side or a ball to push", "Drag the checker onto a corner", "Reset"],
        instruction="Build the shape. Push one side gently. Does the shape change?",
        feedback=["Right join: the straws snap to a clay ball. A shape closes when every end is joined.",
                  "Push the triangle: it turns or slides, but its shape stays. Answer: No, it does not change.",
                  "Push the rectangle: it leans over and its corners change. Answer: Yes, it changes.",
                  "A wrong Yes or No: the shape is pushed again, so you can look once more.",
                  "The checker on a corner shows right, acute or obtuse. Every triangle has acute angles. One corner can be a right angle or an obtuse angle. Every corner of the rectangle fits the checker, so it has four right angles.",
                  "Trace step: the screen shows the triangle large. It says, Draw round it in your notebook. Its panel has one card, I did it. The tool cannot check a notebook.",
                  "After both pushes: a shape that keeps its shape when pushed is rigid. The triangle is the most rigid shape, as it does not change its shape when pushed."],
        done_when="A triangle and a rectangle are built and pushed, their angles are checked with the checker, and the seven book questions are answered.",
        shared_state=["strawLengths", "jointPositions", "pushResult", "cornerKinds"],
        hints=["Look at the clay balls. They let the straws turn like joints.",
               "Push one side gently. Watch the corners, not only the sides.",
               "If the corners and the sides keep their places, the shape did not change.",
               "The triangle does not change when pushed. The rectangle leans over and changes."],
        visuals=["rigid_shapes", "straws_and_clay", "right_angle_checker", "angle_mark"]),
    "push_angles": T(
        "tool_angles_after_the_push", "Angles After the Push", 14,
        "Students push a rectangle, a square and a pentagon and say how their angles change.",
        screen=FRAME +
        "PHASE 1, get ready: a small folding gate, the one from the picture and with no marks on it, stands beside a straw "
        "rectangle. Drag a clay ball of the rectangle: it slants, like a slanted diamond cell of the gate. "
        "PHASE 2, play: a straw rectangle, a straw square and a pentagon of five equal straws lie on a mat. The word "
        "pentagon is written beside the five-straw shape. Push one side of any shape. Lay the right angle checker on any "
        "corner. Each corner is then tagged right, acute or obtuse. "
        "PHASE 3, the seven questions of your maths book: push the rectangle and say what has happened to its angles; push "
        "the square and say the same; say how the angles of triangles and rectangles are alike or different; build the "
        "pentagon from 5 equal straws; check its angles with the checker; push it and answer Yes or No; say how the push "
        "changes its angles.",
        controls=["Drag a clay ball to push", "Lay the checker on a corner", "Pick a word for the corner", "Reset"],
        instruction="Push one side. Check every corner with the checker. What changed?",
        feedback=["Pushed rectangle: it leans. No corner fits the checker now. Two corners are acute and two are obtuse.",
                  "Pushed square: it leans in the same way. Two corners are acute and two are obtuse.",
                  "Pentagon before the push: every corner is bigger than a right angle. None is a right angle.",
                  "Pushed pentagon: it leans and changes its shape. Some corners get smaller and some get bigger.",
                  "Alike and different: a triangle and a rectangle both have angles at their corners. A triangle has 3 angles. A rectangle has 4 right angles. Pushed, the angles of the rectangle change, but those of the triangle do not.",
                  "A wrong word on a corner shakes. The checker shows beside that corner."],
        done_when="A rectangle, a square and a pentagon are pushed, their corners are tagged, and the seven book questions are answered.",
        shared_state=["shapeInPlay", "jointPositions", "cornerTags", "compareChoices"],
        hints=["Lay the checker on a corner before you push. Then push, and lay it on again.",
               "A corner smaller than the checker is acute. A bigger corner is obtuse.",
               "Push the rectangle. Look at the top left corner and the bottom left corner.",
               "A pushed rectangle has two acute corners and two obtuse corners. A pushed square is the same."],
        visuals=["rigid_shapes", "straws_and_clay", "angle_mark", "right_angle_checker", "folding_gate"]),
    "shape_angles": T(
        "tool_angles_in_shapes", "Angles in Shapes", 15,
        "Students draw three- and four-sided shapes on a dot grid, count their right angles and tell shapes apart by their kinds of angles.",
        screen=FRAME +
        "PHASE 1, get ready: Nitesh's dot grid from the story, with his three-sided shape, his four-sided shape and the paper "
        "checker. "
        "PHASE 2, play: draw a three-sided or four-sided shape by joining dots. Lay the checker on each corner. A corner "
        "that fits gets a red square, and a counter shows how many right angles the shape has. "
        "PHASE 3, the six questions of your maths book: draw several three- and four-sided shapes and circle those with a "
        "right angle; sort your shapes by 1, 2, 3 or all right angles; test three other four-sided shapes against a rectangle "
        "and a square; mark the right angles in six figures and write each count; say which figures have only right angles; "
        "then find shapes from four clues among 14 numbered shapes.",
        controls=["Draw on the dots", "Lay the checker on a corner", "Tap a shape to pick it", "Reset"],
        instruction="Draw or pick a shape. Lay the checker on each corner and count.",
        feedback=["The checker fits: a red square marks the corner, and the counter adds one.",
                  "The checker does not fit: a small gap shows and no square is drawn.",
                  "Six figures: the counts are 4, 0, 1, 0, 0 and 4, from left to right. Only the blue rectangle and the red tilted shape have only right angles.",
                  "Clue cards: tap every shape that fits. More than one shape can fit a clue. A shape that does not fit says so.",
                  "Rectangle and square: each has 4 right angles. A square is a special kind of rectangle. The three other four-sided shapes have none.",
                  "Your own shapes: a right triangle has 1 right angle. A shape with one slanted side has 2. A rectangle and a square have all 4. Your answer may differ."],
        done_when="Shapes are drawn and checked, the six figures are counted, the clue cards are answered and the book's questions are done.",
        shared_state=["drawnShapes", "checkerPose", "rightAngleCount", "clueAnswers"],
        hints=["Lay the checker on one corner at a time. Does it fit exactly?",
               "Count only the corners where the checker fits. Mark each with a red square.",
               "For a clue, count the right angles first. Then look at the other corners.",
               "A rectangle and a square have 4 right angles. The three other four-sided shapes have none."],
        visuals=["dot_grid", "four_sided_shapes", "angle_shapes", "angle_mark", "right_angle_figures", "shape_gallery",
                 "right_angle_checker"]),
    # ---- Module 3: circles and flat shapes (Tools 16 to 19)
    "circle_make": T(
        "tool_make_a_circle", "Make a Circle", 16,
        "Students form a circle from equal straws and from marked points at the same distance from a centre.",
        screen=FRAME +
        "PHASE 1, get ready: Diksha's round paper from the story, with its centre dot and one radius. "
        "PHASE 2, play: a clay ball sits on the centre. Lay straws round it like spokes. Pick a straw length and lay many "
        "straws of that length: their ends make a round line. Swap in a longer or a shorter straw and watch the ends. "
        "PHASE 3, the five questions of your maths book: make a circle with straws; say whether the straws in the picture "
        "are equal or unequal; say what happens with straws of unequal lengths; mark a point A and use the ruler to mark "
        "many points at the same distance from A, then join the dots freehand; say what you get. The ruler only shows equal "
        "distances. It has no units.",
        controls=["Lay a straw or mark a point", "Pick a straw length", "Drag to join the dots", "Reset"],
        instruction="Lay straws round the centre. Do their ends make a circle?",
        feedback=["Equal straws: the ends sit on one round line. The tool draws it. This is a circle.",
                  "Unequal straws: some ends are far and some are near. The line looks uneven. It is not a circle.",
                  "Equal distance: each dot at the same ruler mark from A joins the round line. Join the dots freehand and a circle shows.",
                  "A dot at a different ruler mark sits off the round line and blinks.",
                  "What do you get? The question is answered when the joined dots show a circle."],
        done_when="A ring of equal straws and a ring of unequal straws are laid, many points at the same distance from A are marked and joined, and the five book questions are answered.",
        shared_state=["strawLengths", "laidStraws", "markedPoints", "joinedCurve"],
        hints=["Put the clay ball in the middle. Every straw starts there.",
               "Lay straws that are all the same length. Look at where their ends are.",
               "Use the same mark on the ruler every time you mark a dot from A.",
               "Straws of the same length laid round one middle point have ends that make a circle."],
        visuals=["equal_straws_circle", "ruler_and_thread"]),
    "circle_fold": T(
        "tool_fold_the_circle", "Fold the Circle", 17,
        "Students show that the folds of a circle are equal diameters through the centre and that a diameter is double the radius.",
        screen=FRAME +
        "PHASE 1, get ready: the round paper from the story, with its one crease. "
        "PHASE 2, play: drag the fold line to fold the paper in half a different way. Tap Open to see the crease. Drag the "
        "virtual thread along the crease to measure it. The thread has no units. It only compares lengths. After three folds "
        "the creases cross at one point. A dot marks it, and the screen names it the centre. "
        "PHASE 3, the four questions of your maths book: fold and measure three creases, as the seven steps of the activity "
        "say; say if the creases are equal or unequal; measure from the centre to the border along a crease, a radius; fold "
        "the paper in half, fold the half in half again, and say if the diameter is half or double the radius.",
        controls=["Drag the fold line", "Tap Open", "Drag the thread along a crease", "Reset"],
        instruction="Fold the paper in half. Open it. Measure the crease with the thread.",
        feedback=["Fold in half: the edges meet and a crease is made. Open shows the dashed crease.",
                  "Measure: the thread stretches along the crease. Three creases give three threads of the same length. The creases are equal.",
                  "All the creases cross at one point. A dot marks it, and the screen names it the centre.",
                  "Radius: the thread from the centre to the border is the same for every crease.",
                  "Half or double: two radius threads fit exactly along one diameter thread. The diameter is double the radius. Half is not right.",
                  "A wrong choice slides back. The thread is shown against the other one."],
        done_when="Three creases are made and measured, the radius is measured, and the half fold and the quarter fold show that the diameter is double the radius.",
        shared_state=["foldLines", "creaseLengths", "centrePoint", "radiusThread"],
        hints=["Fold the circle so the edge meets itself all the way round.",
               "Fold it a different way each time. Open it and measure each crease.",
               "Lay the threads side by side. Do their ends line up?",
               "Two radius threads end to end are as long as one diameter thread."],
        visuals=["circle_paper", "ruler_and_thread"]),
    "radius_diameter": T(
        "tool_find_radius_and_diameter", "Find Radius and Diameter", 18,
        "Students draw a circle design, mark its centre, radius and diameter and compare wheels by radius and diameter.",
        screen=FRAME +
        "PHASE 1, get ready: a round steel plate and a coin lie side by side, each seen straight on. Tap the middle of each. "
        "A dot in the middle stays. A dot off the middle slides to the middle. "
        "PHASE 2, play: a compass lies on a page. Drag its pencil arm to set an opening. Fix the point and swing the pencil: "
        "a circle is drawn. A wider opening draws a bigger circle. "
        "PHASE 3, the four questions of your maths book: make the flower design in three steps, one circle, then more "
        "circles of the same opening with their points on the first circle, then colour the petals blue, green, red and "
        "yellow; mark the centre, a radius and a diameter on the carpet design with any colour; say what all four wheels "
        "look like; name the wheel with the longest radius, the shortest radius, the longest diameter and the shortest "
        "diameter, using the thread on wheels A to D. Six faint dots on the first circle, shown after it is drawn, are the "
        "plan's own aid, labelled so.",
        controls=["Drag the compass", "Pick a colour, then tap or draw", "Drag the thread to measure", "Reset"],
        instruction="Draw with the compass. Mark centre, radius and diameter. Measure the wheels.",
        feedback=["Compass: the point stays fixed and the pencil swings round. The same opening draws the same size of circle.",
                  "Carpet, right: the dot sits in the middle. A radius from the centre to the edge stays. A line through the centre from edge to edge is a diameter.",
                  "Carpet, wrong: a line across that misses the centre does not stay. It is not a diameter.",
                  "Wheels: the thread shows each radius and diameter. B is longest in both. D is shortest in both. The wheel with the longest radius has the longest diameter too.",
                  "All four wheels are round. They look like circles.",
                  "Flower: a circle with a different opening does not match. The tool shows the first opening again."],
        done_when="The flower is drawn and coloured, the carpet is marked, the wheels are measured and the four book questions are answered.",
        shared_state=["compassOpening", "drawnCircles", "carpetMarks", "wheelMeasures"],
        hints=["A compass has a fixed point and a pencil. Fix the point first.",
               "For the flower, keep the same opening. Put the point on the first circle.",
               "On the carpet, start every line at the middle dot. A diameter goes right across.",
               "Measure each wheel with the thread. The biggest wheel has the longest radius and the longest diameter."],
        visuals=["compass_design", "carpet_design", "wheels", "compass", "ruler_and_thread", "plate_and_coin"]),
    "sides_angles": T(
        "tool_sides_and_angles", "Sides and Angles", 19,
        "Students sort flat shapes by their sides and their angles and find that a straight-sided shape has as many angles as sides.",
        screen=FRAME +
        "PHASE 1, get ready: Nitesh's own paper shapes from the story lie in a row. Count the sides of each. "
        "PHASE 2, play: drag Nitesh's shapes into groups by their sides. Tap a corner to count it. Each tapped corner is an angle. "
        "PHASE 3, the five questions of your maths book: sort the six shape cards from the end of the book into three groups "
        "by their sides and say why; drag seven shapes a to g into 3 angles, 4 angles and 5 angles; say what relation you "
        "notice between sides and angles; draw a shape with fewer than 5 angles on dots; draw a shape with more than 5 angles "
        "on dots. The three groups of the card game are one reading, the plan's own: only straight sides, only curved sides, both.",
        controls=["Drag a card or shape", "Tap a corner to count it", "Draw on the dots", "Reset"],
        instruction="Sort the cards by their sides. Then count the angles of each shape.",
        feedback=["Right group: the card stays and a line says why. The square has only straight sides.",
                  "Wrong group: the card slides back. A line shows the side that does not fit.",
                  "Cards: the square and the triangle have only straight sides. The oval and the circle have only curved sides. The quarter circle and the semicircle have both.",
                  "Count angles: each tapped corner adds one. Shapes b, d and f have 3 angles. Shapes a, c and g have 4. Shape e has 5.",
                  "Relation: each straight-sided shape has as many angles as it has sides.",
                  "Drawing: the tool counts the angles of your shape. A triangle has 3 and a rectangle has 4, fewer than 5. A hexagon has 6, more than 5.",
                  "The circle has no corners. The rule about sides and angles is for straight-sided shapes."],
        done_when="The cards are sorted into three groups, the seven shapes are sorted by angles, the relation is stated and two shapes are drawn.",
        shared_state=["cardGroups", "cornerCounts", "angleBoxes", "drawnShapes"],
        hints=["Look at the edges of a card. Are they straight, curved or both?",
               "Count the sides of a shape. Then tap each corner and count the angles.",
               "Put each shape with 3 sides in 3 angles. Do the same for 4 and for 5.",
               "Each straight-sided shape has as many angles as it has sides."],
        visuals=["shape_cards", "angle_shapes", "dot_grid"]),
    # ---- Module 4: shape puzzles (Tools 20 to 22)
    "divide": T(
        "tool_divide_the_shapes", "Divide the Shapes", 20,
        "Students find the hidden shapes in a drawing and draw lines that divide a shape into smaller shapes.",
        screen=FRAME +
        "PHASE 1, get ready: Diksha's drawing from the story shows its one hidden shape in colour. A paper rectangle shows "
        "one cut. "
        "PHASE 2, play: trace any outline with a finger and the shape glows. Draw one line across a paper shape and tap Cut "
        "to see the pieces slide apart. "
        "PHASE 3, the four questions of your maths book: find the hidden shapes in the red drawing and pick a name card for "
        "each; draw 2 lines to divide a triangle on a dot grid into 1 square and 2 triangles; draw 2 lines to divide a "
        "square into 3 triangles; draw the cut lines that turn each of the shapes A, B and C into the pieces shown beside it. "
        "On a dot grid a line runs from dot to dot. Shapes A, B and C have no dots, so their lines go straight across where "
        "your finger goes. The red outlines are one colour on purpose, so the shapes hide one another.",
        controls=["Trace an outline", "Drag to draw a straight line", "Tap Cut", "Reset"],
        instruction="Find the hidden shapes. Then draw lines to cut a shape into pieces.",
        feedback=["Right shape traced: it glows and asks for its name. Pick a name card. A right name stays.",
                  "Right cut: the pieces slide apart. They are counted and named, and they match the shapes wanted.",
                  "Not the pieces wanted: the pieces slide back together. The pieces you made are shown, so you can try another cut.",
                  "Cut lines can go in many ways. Any cut that gives the right pieces is right. Your answer may differ."],
        done_when="The hidden shapes are named, both dot-grid puzzles are solved, and the cuts for shapes A, B and C give the pieces shown.",
        shared_state=["tracedShapes", "drawnLines", "pieces", "shapeNames"],
        hints=["Trace each outline slowly with your finger. Look for a shape that closes.",
               "Look at the pieces you want. Count them and name their shapes.",
               "On a dot grid, draw a line from dot to dot across the shape.",
               "For the triangle, draw a line from the middle of the top side straight down. Then draw one from the middle of the left side straight across."],
        visuals=["hidden_shapes", "dissection_shapes", "dot_grid"]),
    "webs": T(
        "tool_spider_web_puzzles", "Spider Web Puzzles", 21,
        "Students count the triangles and rectangles in two webs and decide which walks can be made without using a wall twice.",
        screen=FRAME +
        "PHASE 1, get ready: Squiggly and Wiggly sit at the tops of their webs. Squiggly's web is made of triangles and "
        "Wiggly's of rectangles. "
        "PHASE 2, play: tap any shape in a web to see it glow. Drag along the walls to take a walk. Each wall you use turns "
        "thick. A wall used twice stops the walk and says, You used this wall already. "
        "PHASE 3, the four questions of your maths book: tap each triangle in Squiggly's web and count them; trace "
        "Squiggly's path from A back to A without using a wall twice, on the walls numbered 1 to 12; tap each rectangle in "
        "Wiggly's web and count them; try Wiggly's path from A to B without using a wall twice. One rule shows on the "
        "screen for both walks: use every wall once. This rule is added by this plan. Your maths book does not say every.",
        controls=["Tap a shape to count it", "Drag along walls to walk", "Tap Undo wall", "Reset"],
        instruction="Count the shapes. Then walk along each wall once, never twice.",
        feedback=["A shape tapped glows, and the count adds one. A shape counted before does not count again.",
                  "Triangles: 2 + 4 + 4 = 10. That is 2 at the top and bottom, 4 small ones and 4 big ones. Rectangles: 12, big and small.",
                  "Squiggly's walk is right when it uses all 12 walls once and ends back at A. One such walk is 12, 6, 9, 3, 4, 7, 10, 2, 8, 5, 11, 1.",
                  "Wiggly's walk: try as many walks as you like. Every walk from A gets stuck before every wall is used.",
                  "Stuck: the walk stops. It says, No new wall is left here. Tap Undo wall and try another way.",
                  "A wall used twice does not count as a walk. The wall blinks."],
        done_when="Both counts are found, Squiggly's walk is traced, and Wiggly's walk is tried in at least three different ways.",
        shared_state=["countedShapes", "walkWalls", "usedWalls", "triedWalks"],
        hints=["Look at the web. Find the small shapes first and tap each one.",
               "Then look for bigger shapes made of small ones. Tap those too.",
               "For a walk, start at A. Tap one wall at a time. Do not use a wall twice.",
               "If you get stuck, go back one wall with Undo wall and try a different wall."],
        visuals=["spider_webs", "squiggly_and_wiggly"]),
    "matchsticks": T(
        "tool_matchstick_moves", "Matchstick Moves", 22,
        "Students make, move and remove matchsticks to form a given number of triangles.",
        screen=FRAME +
        "PHASE 1, get ready: Wiggly's sticks from the story lie on a flat stone. Three sticks make one triangle. Take one "
        "stick away and the count of triangles drops to 0. Put it back and it is 1. "
        "PHASE 2, play: drag sticks onto a grid of dots. A stick snaps end to end. A counter shows how many triangles are on "
        "the grid, small and big. Move a stick or take one away and watch the counter change. "
        "PHASE 3, the three questions of your maths book: use 5 sticks to make 2 triangles, then tap Draw it to copy what you "
        "made into the drawing box; move 2 "
        "sticks of a row of 3 triangles made of 9 sticks to make 4 triangles; take away 4 sticks of a figure of 13 sticks, "
        "with 7 triangles in all, to leave 3 triangles. In the row, the three triangles touch at their corners. This is "
        "the plan's own reading and the screen says so.",
        controls=["Drag a stick to move it", "Tap a stick to take it away", "Tap Draw it", "Reset"],
        instruction="Move or take away sticks to get the number of triangles asked for.",
        feedback=["Sticks that meet end to end snap together. The counter counts every triangle, small or big.",
                  "5 sticks: a diamond of 4 sticks with the fifth across the middle makes 2 triangles. They share the middle stick.",
                  "Move 2 sticks: take the left side and bottom stick of the first triangle. Lay them end to end across the three tops. The counter shows 4 triangles in a row.",
                  "Take away 4 sticks: one way is to remove 2 sticks of the top right triangle. These are its right side and its bottom stick. Then remove 2 sticks of the far right triangle. These are its top stick and its right side. The counter shows 3. Other ways work too.",
                  "Not yet: the counter shows how many triangles you have now. It also shows how many sticks you moved or took away. Tap Reset to start again."],
        done_when="Two triangles are made from 5 sticks, 4 triangles are made by moving 2 sticks, and 3 triangles are left after taking away 4 sticks.",
        shared_state=["stickPositions", "triangleCount", "movedCount", "removedCount"],
        hints=["Count the triangles now. Then think about which sticks are shared.",
               "A stick can be the side of two triangles. Look for sticks that two triangles share.",
               "Try one move and look at the counter. Tap Reset if the count goes down.",
               "Five sticks can make two triangles: a diamond with one stick across its middle."],
        visuals=["matchsticks"]),
}

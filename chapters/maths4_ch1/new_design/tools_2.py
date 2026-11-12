# -*- coding: utf-8 -*-
"""Class 4 Ch 1, Shapes Around Us: the tool specs of the 11 new activity tools (Tools 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 23).

Loaded by concept_plan.py next to tools_1.py (every tools_N.py defines a dict TOOLS). The shared FRAME is in tools_1.py.

Written on 12 Nov 2026, after the user approved the structure. Each tool is written in plain order, First, Then and
(where the tool has book questions) Last. Each tool carries only its own activity of the lesson plan and the book
questions homed on it. Until 12 Nov these activities were stages of older, bigger tools: their text and fixes are reused here.
Every media item of every tool is a placeholder.
"""
from __future__ import annotations

from topics_common import T  # noqa: F401
from tools_1 import FRAME  # noqa: F401

# One `notice` prompt for each tool that carries no book question (the structure gate wants every tool to carry at least one
# question or prompt). Short plain sentences. A notice prompt is read as a thought bubble and never answered.
NOTICE_TOOL3 = ["What do you notice about the faces of the prisms and the pyramids?"]
NOTICE_TOOL4 = ["What do you notice about the faces of the solids you built?"]
NOTICE_TOOL17 = ["What do you notice when you compare each angle with a right angle?"]
NOTICE_TOOL19 = ["What do you notice about each radius and its diameter?"]
NOTICE_TOOL23 = ["What do you notice about the shapes that keep their form when pushed?"]

# The number pad is ONE control wherever a child types a number (a count, a total, a radius or a diameter).
NUMBER_PAD = ("A number pad sits beside the box. It has digits 0 to 9, a Back key and OK, for up to two digits. ")

TOOLS = {
    # ------------------------------------------------------------------------------------------------------------------
    # Tool 3: Lesson 2, Activity 1. Concept C2 (name the solids). Follows the Two Tents image with Tools 4 and 5: it does not replay it.
    "match_3d_shape": T(
        "tool_match_the_3d_shape", "Match the 3D Shape", 3,
        "Students match the name of each solid, such as a triangular prism, a cube or a square pyramid, to its picture.",
        notice=NOTICE_TOOL3,
        screen=FRAME +
        "First, a shelf holds five solids. They are a triangular prism, a square pyramid and a cube. "
        "The other two are a hexagonal prism and a triangular pyramid. "
        "Every solid is a shaded 3D solid in the one neutral stone-grey tint. "
        "Below the shelf lie five name tiles in a mixed order. Each solid has an empty slot under it. "
        "Drag a name tile into the slot under its solid. Tap an arrow to turn a solid and look at its faces. "
        "A name that fits snaps in, and the faces that decide glow. A name that does not fit slides back with a clue. "
        "No solid is blue, pink or any other colour of the chapter's colour code. So colour never gives a name away. "
        "Then, a thought bubble reads the notice prompt. It is read, not answered.",
        controls=["Drag a name tile under a solid", "Tap an arrow to turn a solid", "Reset"],
        instruction="Drag each name under the solid it belongs to.",
        feedback=["A right name snaps in and the faces that explain it glow. "
                  "Two matching triangle ends and three rectangles make a triangular prism.",
                  "A wrong name slides back and says what to check. This solid has one bottom face, "
                  "so look for triangles that meet at a point.",
                  "A triangular prism and a triangular pyramid both have triangle faces. "
                  "A prism has two matching ends. A pyramid has one bottom face.",
                  "A cube has six equal square faces. A square pyramid has one square bottom and four triangles.",
                  "A hexagonal prism has two matching six-sided ends joined by rectangles.",
                  "Every solid has the same stone-grey tint. Only its faces tell its name, never its colour."],
        done_when="All five names sit under the right solid and the thought bubble has been read.",
        shared_state=["turnedSolid", "nameTiles", "placedNames"],
        misconceptions=["M_SH_1", "M_SH_2"],
        hints=["Turn the solid. Look at its flat faces and name their shapes.",
               "Are there two matching end faces? Or one bottom face with triangles that meet at a point?",
               "Tap the end faces. Do they match? Look at the other faces. Are they rectangles or triangles?",
               "Two matching ends joined by rectangles make a prism. One bottom face and triangles that meet at "
               "one point make a pyramid."],
        visuals=["prisms", "pyramids", "solid_pictures", "solid_colours"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 4: Lesson 2, Activity 2. Concept C2 (build a solid). The three challenges of the lesson plan.
    # BUILDER NOTE: the block set is a real toy set, so it keeps its own colours (the user's decision of 12 Nov 2026): one colour for
    # every square tile and one for every triangle tile, so the colour tells a face shape and never the name of a solid.
    "build_3d_shape": T(
        "tool_build_your_own_3d_shape", "Build Your Own 3D Shape", 4,
        "Students build a triangular prism, a square pyramid and a cube from blocks, then name each solid they built.",
        notice=NOTICE_TOOL4,
        screen=FRAME +
        "First, a tray holds a toy block set. It has flat square tiles, long rectangle tiles, triangle tiles and small cubes. "
        "It is a real set, so it keeps its own bright colours. "
        "All square tiles share one colour and all triangle tiles share another. "
        "None is the prism blue, the pyramid pink or the cube teal. "
        "A building pad stands beside the tray. Three challenge cards come one at a time. "
        "They ask for a triangular prism, a square pyramid, and a cube from eight small cubes. "
        "For the prism and the pyramid, the tray holds the tiles needed and two extra ones. "
        "Drag tiles onto the pad. Each tile snaps edge to edge to the tile beside it. "
        "When the tiles close up, the pad folds them into a solid. "
        "A tile that does not fit leaves a gap. The screen names the face that is missing. "
        "For the cube, the pad shows a 2 by 2 floor. The tray holds ten small cubes. "
        "Drag small cubes onto it. Four cover the floor and four more sit on top. "
        "A cube cannot hang in the air. It falls onto the floor or onto a cube below. "
        "Tap a tile or the solid, then tap an arrow to turn it. Look at the solid from every side. "
        "When a solid closes, ten name cards appear. Five are sphere, cone, cylinder, cube and cuboid. "
        "Five are triangular prism, hexagonal prism, triangular pyramid, square pyramid and pentagonal pyramid. "
        "Tap the name of the solid you built. "
        "The faces glow and the screen says if the name fits, and why. "
        "Then, after the cube, a thought bubble reads the notice prompt. It is read, not answered.",
        controls=["Drag a tile or a cube onto the pad", "Tap an arrow to turn a tile or the solid", "Tap a name card", "Reset"],
        instruction="Build the solid on the card. Then tap its name.",
        feedback=["A tile that fits clicks into place edge to edge. A tile that does not fit leaves a gap.",
                  "When the solid closes, its faces glow and the screen names their shapes.",
                  "A right name gets a tick and a reason. "
                  "Two matching triangle ends joined by three rectangles make a triangular prism.",
                  "One square base and four triangles that meet at one point make a square pyramid.",
                  "A wrong name slides back. The faces that decide glow, and the screen says what to check.",
                  "Eight small cubes make a 2 by 2 by 2 block. 2 × 2 × 2 = 8. The block is a cube.",
                  "More or fewer than eight cubes leave steps or gaps. That block is not a cube.",
                  "The tiles keep the block set's own colours. Colour never gives a name away."],
        done_when="All three solids are built and named, and the thought bubble has been read.",
        shared_state=["challenge", "placedTiles", "placedCubes", "closedSolid", "chosenName"],
        misconceptions=["M_SH_1", "M_SH_2"],
        hints=["Read the card. Think about the flat faces this solid needs.",
               "Pick the faces first. Then place them edge to edge on the pad.",
               "Look at the pad. A gap shows that a face is still missing.",
               "A prism has two matching end faces with rectangles between them. A pyramid has one bottom face "
               "and triangles. For the cube, build the floor first, then the top."],
        visuals=["prisms", "pyramids", "solid_colours"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 7: Lesson 3, Activity 2. Concept C9 (net to solid). Carries solids_q3 and solids_q5.
    "which_net": T(
        "tool_which_net_makes_which_shape", "Which Net Makes Which Shape", 7,
        "Students match each net to the solid it folds into, such as a cube, a cuboid or a square pyramid.",
        screen=FRAME +
        "First, three nets lie on the left. Each is flat and pale with dotted fold lines, and none is in a solid's colour. "
        "The first net is a staircase of six squares. It has three pairs of squares. "
        "Each new pair starts under the right square of the pair before. "
        "The second net is a strip of four tall rectangles. Two are wide and two are narrow, in turn. "
        "A rectangle sits above one wide rectangle and a rectangle below the same one. It has six rectangles in all. "
        "The third net is one square with a triangle on each of its four sides. "
        "Three solids stand on the right in the one neutral stone-grey tint. "
        "They stand in a mixed order: a square pyramid, a cube and a cuboid. "
        "Drag each net onto its solid. When a net lands on its solid, it folds up and closes into that solid. "
        "The screen says why. Six squares fold into a cube. "
        "Six rectangles, four in a ring and one at each end, fold into a cuboid. "
        "One square and four triangles fold into a square pyramid. "
        "A wrong match slides back. It says to check the shapes of the faces and how many there are. "
        "Last, your maths book's two questions come one at a time. "
        "Solids and nets, Q3: four nets are numbered 1 to 4. Four solids below are marked a to d. "
        "Net 1 has 4 triangles. Net 2 has a rectangle and 2 circles. Net 3 has 6 rectangles. "
        "Net 4 has 3 rectangles and 2 triangles. "
        "Solids a to d are a cuboid, a triangular pyramid, a triangular prism and a cylinder. "
        "All are in the one neutral tint. "
        "Drag each net onto one of the solids a to d. A net on its own solid folds up into it. "
        "A wrong one slides back. When all four are placed, the screen shows the book's answer. "
        "Solids and nets, Q5: Nitesh's six pieces lie loose in pale orange. They are one pentagon and five triangles. "
        "Four pyramids marked a to d stand below, as the book draws them. They are in the one neutral tint. "
        "Tap each piece once. It turns green and a counter adds one for pentagons or for triangles. "
        "Then tap one of the solids a to d. The screen shows the book's answer.",
        controls=["Drag a net onto a solid", "Tap a piece to count it", "Tap a solid to answer", "Reset"],
        instruction="Drag each net to the solid it folds into.",
        feedback=["A net that lands on the right solid folds up and closes with no gap.",
                  "The screen says why. Six squares fold into a cube. Six rectangles fold into a cuboid. "
                  "One square and four triangles fold into a square pyramid.",
                  "A wrong match slides back. The screen counts the faces of the net. Check them against the solid.",
                  "Solids are in one neutral tint and nets are never in a solid's colour. Colour never gives the match away.",
                  "Solids and nets, Q3. From the picture: (1) with (b), (2) with (d), (3) with (a), (4) with (c).",
                  "Solids and nets, Q5. Count the pieces first: 1 pentagon and 5 triangles. "
                  "A wrong solid shows its own faces beside the pieces. They do not match, so try another solid.",
                  "Solids and nets, Q5. From the picture: d, the pentagonal pyramid. It has 1 pentagon and 5 triangles."],
        done_when="All three nets are matched, and the two book questions are answered.",
        shared_state=["netPositions", "foldResult", "pieceCounts", "answers"],
        misconceptions=["M_SH_7"],
        hints=["Look at the faces of the net. What shapes are they?",
               "Count the faces of the net. The solid needs the same faces.",
               "Count each kind of face. Which solid has exactly those faces?",
               "A net folds into a solid when every face lands once. Match the faces of the net to the faces of the solid."],
        visuals=["nets_and_solids", "box_net", "prisms", "pyramids", "solid_colours"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 8: Lesson 3, Activity 3. Concept C9 (the net that will not fold). Carries solids_q4.
    # Every net here was checked by folding a cube over it (12 Nov 2026): nets 1 and 3 fold into a cube. Net 2, the block of two rows of
    # three squares, does NOT fold: four squares meet at one corner and a cube has only three faces at a corner. The right answer is
    # Net 2 (the middle net, never the last). The verified cut is along the top row, down, then back along the bottom row: the two
    # middle squares land on one face and one face of the cube stays open.
    "wrong_net": T(
        "tool_find_the_wrong_net", "Find the Wrong Net", 8,
        "Students find the one net that will not fold into a given solid and say why it will not.",
        screen=FRAME +
        "First, a cube stands on the right in the one neutral stone-grey tint. Three nets lie on the left, each flat and pale. "
        "Net 1 is a strip of four squares. It has one square above its left end and one square below its right end. "
        "Net 2 is a block of two rows of three squares. "
        "Net 3 is a row of three squares. A second row of three starts under its last square and goes right. "
        "Two of the nets fold into the cube. One does not. "
        "Tap the net that you think will not fold. The net you tap folds first. "
        "If it is Net 1 or Net 3, it closes into the cube with no gap. The screen says so, and you tap another net. "
        "If it is Net 2, it folds and two of its squares land on the same place. They are the two in the middle. One face of the cube stays open. "
        "Then Net 1 and Net 3 fold too, and both close into the cube with no gap. "
        "Then, three reason cards appear, in this order: It has too many squares. Four squares meet at one corner. It has too few squares. "
        "Tap the card that says why Net 2 did not fold. "
        "Last, your maths book's question comes. "
        "Solids and nets, Q4: nets A to D are drawn as the book prints them. Each has a solid below it. "
        "Below A is a cuboid. Below B is a cylinder. Below C is a pyramid. Below D is a flat box. "
        "All four solids are in the one neutral tint. "
        "Tap the fold lines of a net to fold it. See if the solid below closes. "
        "Then tap Folds or Does not fold. The screen shows the book's answer.",
        controls=["Tap a net to choose it", "Tap a fold line to fold the net", "Tap a card to answer", "Reset"],
        instruction="Which net will not fold into the solid? Tap it.",
        feedback=["A net that folds closes edge to edge. No gap shows and no face lands on another.",
                  "Net 2 will not fold. Two squares land on the same place, and one face stays open.",
                  "If you tap Net 1 or Net 3, it closes into the cube. The screen says so, and you can try another net.",
                  "The right card, Four squares meet at one corner, turns green. "
                  "A cube has only three faces at a corner, so four squares cannot fit round it.",
                  "A wrong card shakes gently, then can be tried again. "
                  "Too many squares? No. Net 2 has six squares, and a cube has six faces.",
                  "Too few squares? No. Net 2 has six squares too. Look at the squares round one corner.",
                  "Net A has both end flaps on the same side, so one end stays open. "
                  "Net C has only 2 of the 4 triangles its pyramid needs.",
                  "Solids and nets, Q4. From the picture: B and D fold into the solid below. A and C do not."],
        done_when="Net 2 is tapped as the net that will not fold and its reason card is chosen. All four nets of the book question are answered.",
        shared_state=["chosenNet", "foldResult", "reasonCard", "answers"],
        misconceptions=["M_SH_7"],
        hints=["Look at the faces of each net. Do they look like the faces of the solid?",
               "Imagine folding along the dotted lines. Where does each face go?",
               "Tap the fold lines. Watch for a face that lands on another face, or a gap.",
               "Every face must land once. Count the faces that meet at one corner of the solid. "
               "Then look in the net for a corner where more meet."],
        visuals=["nets_and_solids", "solid_colours"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 10: Lesson 4, Activity 2. Concept C3 (count the parts). Carries craft3 and fve.
    # Nothing is scored and there is no win screen: the child counts, types, and sees at once whether it is right.
    "count_and_win": T(
        "tool_count_and_win", "Count and Win", 10,
        "Students count the faces, edges and corners of a cube, a cuboid, a triangular prism and a square pyramid.",
        screen=FRAME +
        "First, four solids come one at a time. They are a cube, a cuboid, a triangular prism and a square pyramid. "
        "Each is a model of straws and clay balls. It is drawn see-through so every part can be counted. "
        "Straws are the edges and balls are the corners. "
        "The straws take the colour of the solid. Cube teal, cuboid red, triangular prism blue, square pyramid pink. "
        "Every clay ball is one plain clay colour. "
        "Three answer boxes sit beside the model: Faces, Edges and Corners. "
        "Tap a part to mark it. A marked part turns green and a small counter beside its box adds one. "
        "A part marked once does not count twice. "
        "To mark a face, tap the space inside a ring of straws. A see-through panel fills it and stays. "
        "Then tap a box and type the count. " + NUMBER_PAD +
        "The screen checks the box at once. The next solid comes when all three boxes are right. "
        "Nothing is scored, and no win screen appears. "
        "Last, your maths book's two questions come one at a time. "
        "Craft, Q3: the book's table is on screen. It has five rows and three columns. "
        "The rows are a cube or square prism and a cuboid or rectangular prism. "
        "They also hold a triangular pyramid, a square pyramid and a triangular prism. "
        "The columns are faces (F), corners (V) and edges (E). "
        "A pile of straws and clay balls waits beside a build pad. "
        "Drag straws and balls onto the pad to make the solid of a row. "
        "Tap its parts to count them. Then tap a cell of the row and type the count on the number pad. "
        "A right cell turns green and a wrong cell shakes. The screen then shows the book's answer. "
        "Craft, F+V−E: a fourth column joins the table. "
        "For each row, tap its cell and type the result on the number pad. The row shows its sum at once. "
        "Then tap a card for what you notice. Three cards offer answers. "
        "One says the result is the same for all five solids. "
        "One says it is bigger when a solid has more faces. "
        "One says it is different for every solid. "
        "The screen shows the book's answer.",
        controls=["Tap a part or a card", "Tap a box, then type a count on the number pad",
                  "Drag straws and clay balls onto the pad", "Reset"],
        instruction="Count the faces, edges and corners. Type each count.",
        feedback=["A tapped part turns green and a counter adds one. A part marked once does not count twice.",
                  "A face is one side of a solid, flat or curved. An edge is a line where two faces meet. A corner is a point where edges meet.",
                  "A right box turns green and shows how the count was made. A cube has 4 side faces, a top and a bottom. 4 + 1 + 1 = 6.",
                  "A wrong box shakes. The parts to count again blink. The right number is not shown.",
                  "Craft, Q3. A right cell turns green. A wrong cell shakes and the model to count again blinks.",
                  "Craft, Q3. From the picture (F, V, E): cube 6, 8, 12. Cuboid 6, 8, 12. Triangular pyramid 4, 4, 6. "
                  "Square pyramid 5, 5, 8. Triangular prism 5, 6, 9.",
                  "Craft, F+V−E. Each row shows its sum. The cube gives 6 + 8 − 12 = 2. The cuboid gives 6 + 8 − 12 = 2. "
                  "The triangular pyramid gives 4 + 4 − 6 = 2. The square pyramid gives 5 + 5 − 8 = 2. "
                  "The triangular prism gives 5 + 6 − 9 = 2.",
                  "Craft, F+V−E. From the picture: F+V−E is 2 for all five solids. So F+V is 2 more than E in each one."],
        done_when="The four solids are counted right. The book's table and the F + V − E question are answered.",
        shared_state=["markedParts", "counters", "boxValues", "tableCells", "noticeCard"],
        misconceptions=["M_SH_3", "M_SH_4"],
        hints=["Look at one solid. A face is a side, an edge is a line, a corner is a point.",
               "Count one kind of part at a time. Tap each part once so it turns green.",
               "Count the green parts and type that number. Do the next kind the same way.",
               "Tap every part once, then count the green ones. For F + V − E, add F and V, then take away E."],
        visuals=["prisms", "pyramids", "solid_colours", "straws_and_clay"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 11: Lesson 4, Activity 3. Concept C4 (die, opposite faces). Carries observe1 to observe3 and border5.
    # BUILDER NOTE: the first step turns a die and counts the faces that show; the opposite faces and the touching faces are found on a plain
    # cuboid, so the practice never shows a pair of opposite die numbers before the book questions.
    "spin_shape": T(
        "tool_spin_the_shape", "Spin the Shape", 11,
        "Students turn a die or a cuboid to find which faces are opposite and which faces touch.",
        screen=FRAME +
        "First, a die stands on a turntable. Tap an arrow to turn it left, right, up or down, or drag the die to turn it. "
        "The arrows and the drag are one Turn control, and it works the same on every shape in this tool. "
        "After each turn the screen asks, How many faces can you see now? Tap 1, 2 or 3. "
        "A right tap lights the faces you can see. The others are at the back or the bottom. "
        "After three turns the screen asks, Can you turn the die so that 4 faces show? "
        "Turn it any way you like. The count never goes above 3. "
        "A line then says why. The faces at the back and the bottom are hidden. "
        "Then, a plain red cuboid stands on the turntable. It is like a closed box with nothing printed on it. "
        "Tap any face of the cuboid. The face opposite it glows orange and a line joins the two. "
        "The four faces that touch it along an edge glow pale. "
        "A line says a face and its opposite are never seen together. Faces that touch share an edge. "
        "Last, your maths book's four questions come one at a time, in the book's order. "
        "Let Us Observe, Q1: a die stands on the turntable. A line says that 6 is opposite 1. "
        "Turn the die with the arrows or by dragging it. Take the faces 2, 3 and 4 one by one. "
        "Tap the number tile, 1 to 6, for the face opposite it. "
        "Let Us Observe, Q2: turn the die so that 1 is on top. "
        "In part a, tap the number tiles of the faces that touch 1 along an edge. "
        "In part b, tap the number tile of the face that does not touch 1. "
        "Let Us Observe, Q3: three views of one coloured cube stand side by side. "
        "Six colour tiles lie below: red, orange, green, purple, dark blue and yellow. "
        "Tap a colour tile for the face opposite the red face. Then tap a colour tile for the face opposite the yellow face. "
        "A fourth copy of the cube can be turned with the arrows or by dragging it, to check. "
        "Border, Q5: the pencil sketches round the border are on screen. "
        "They include two dice, two erasers, a Rubik's cube and a gift box. "
        "They also include balls, cans, a cone and a party hat. "
        "The rest are cheese pieces and a pyramid made of small triangles. "
        "The last are a double pyramid, a wooden wedge and a cake slice. "
        "Tap each sketch whose opposite faces look the same. A tapped sketch gets a circle. Tap it again to remove the circle. "
        "The screen shows the book's answer after each question.",
        controls=["Turn the shape: tap an arrow or drag it", "Tap a face, a number or a colour",
                  "Tap a sketch to circle it", "Reset"],
        instruction="Turn the shape. Find the faces that are opposite and the faces that touch.",
        feedback=["A right count lights the faces you can see. The rest are at the back or the bottom.",
                  "A wrong count shakes and the faces you can see light up. Count again.",
                  "No turn shows 4 faces of a die or a box. The faces at the back and the bottom are hidden.",
                  "Tap a face and the face opposite it glows. A face and its opposite are never seen together.",
                  "Faces that touch share an edge. You can see them together.",
                  "Let Us Observe, Q1. A right tile shows the pair, such as 6 and 1. "
                  "A wrong tile turns the die. It shows that face touching the one you were asked about.",
                  "Let Us Observe, Q1. Sample answer: on a usual die, a) 5, b) 4, c) 3. Opposite faces add up to 7.",
                  "Let Us Observe, Q2. A wrong tile shakes. Turn the die to see if that face touches 1.",
                  "Let Us Observe, Q2. From the picture: a) 2, 3, 4 and 5. b) 6, the face opposite 1.",
                  "Let Us Observe, Q3. Colours seen together in one view touch each other. "
                  "A face and its opposite are never seen together. A wrong colour shakes and the views stay on screen.",
                  "Let Us Observe, Q3. From the picture: a) purple. b) orange.",
                  "Border, Q5. No circle is marked wrong. Sample answer: for example the dice, the erasers, the gift box "
                  "and the Rubik's cube. Your answer may differ."],
        done_when="Both practice steps are done and the four book questions are answered.",
        shared_state=["turnedShape", "visibleCount", "tappedFace", "tappedNumbers", "tappedColours", "circledSketches"],
        misconceptions=["M_SH_5", "M_SH_9"],
        hints=["Turn the shape slowly. Notice which faces you can see together.",
               "Faces you see together touch. A face and its opposite are never seen together.",
               "Turn the shape until your face is on top. Look at the face on the bottom.",
               "The face on the other side from your face is its opposite. The four faces round it touch it."],
        visuals=["die", "colour_cube", "border_objects", "solid_colours"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 13: Lesson 5, Activity 2. Concept C6 (count every cube). Carries towers.
    # BUILDER NOTE: the first stack is a small step of 15 cubes, not the story's tower (14 cubes), not Tool 12's challenges and
    # not the book's two towers.
    "look_carefully": T(
        "tool_look_carefully", "Look Carefully", 13,
        "Students count all the cubes in a stack, the partly hidden ones too.",
        screen=FRAME +
        "First, a stack of teal cubes stands on a pad. It has two layers. "
        "The bottom layer is 3 rows of 3 cubes. The top layer is 2 rows of 3 cubes and sits on the back two rows. "
        "Some cubes are hidden behind others. "
        "Four answer tiles lie below the stack: 9, 12, 15 and 18. "
        "Tap a layer to lift it off and see its rows and columns. "
        "Then tap one answer tile. "
        "Last, your maths book's question comes. "
        "Cube Towers: two towers stand side by side, and every cube is a teal cube. "
        "The first is a stepped tower of 4 layers. "
        "The second is a plus-shaped tower with a middle column and four stairs. "
        "Tap a layer or a stair to lift it off and see its columns. "
        "Then tap the answer box of a tower and type its total. " + NUMBER_PAD +
        "The screen shows the book's answer.",
        controls=["Tap a layer or a stair to lift it off", "Tap an answer tile", "Type a total on the number pad", "Reset"],
        instruction="Count every cube, the hidden ones too. Tap your answer.",
        feedback=["A tapped layer lifts off and shows its rows and columns. For example, 3 rows of 3 is 3 × 3 = 9 cubes.",
                  "Hidden cubes count. A cube you cannot see is still in its layer.",
                  "A right tile shows the two layers added up: 9 + 6 = 15.",
                  "A wrong tile does not show the number. The layers lift off again so you can recount. "
                  "The tile 9 counts only the cubes you can see.",
                  "Cube Towers. A right total shows the layers added up. 1 + 4 + 9 + 16 = 30.",
                  "Cube Towers, second tower. Each stair has 5 + 4 + 3 + 2 + 1 = 15 cubes. "
                  "Four stairs make 4 × 15 = 60. With the middle column, 6 + 60 = 66.",
                  "Cube Towers. From the picture: the first tower has 30 cubes. The second tower has 66 cubes. "
                  "Both counts include the hidden cubes and assume no gaps.",
                  "A wrong total does not show the number. The layers or stairs lift off again so you can recount."],
        done_when="The stack is counted right and both towers of the book question have their total.",
        shared_state=["liftedLayers", "chosenTile", "typedTotals", "answers"],
        misconceptions=["M_SH_6"],
        hints=["Look at the stack from the side. How many layers does it have?",
               "Count one layer at a time. Then add the layers.",
               "Tap a layer to lift it off. Count its rows and columns.",
               "Multiply the rows by the columns to get the cubes in a layer. Then add the layers."],
        visuals=["cube_towers", "cube_models"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 14: Lesson 5, Activity 3. Concept C7 (copy a cube structure). Carries dotcubes.
    # The sample (5 cubes) is a plain practice number: a row of three, one cube behind its left end and one on top of its right end.
    "copy_cube_structure": T(
        "tool_copy_the_cube_structure", "Copy the Cube Structure", 14,
        "Students recreate a cube structure on a grid and copy cube structures on dot paper.",
        screen=FRAME +
        "First, a small structure of 5 teal cubes stands on the left. "
        "It has a row of three cubes along the front. One cube sits behind the left end. One cube sits on top of the right end. "
        "An empty grid of squares, 4 by 4, lies on the right. A tray of spare cubes sits beside it. "
        "Drag cubes onto the grid to copy the structure. "
        "A cube cannot hang in the air. It sits on the grid or on a cube below. "
        "Then tap Check. The two structures stand side by side and turn together slowly. "
        "A cube that is missing or in the wrong place glows. "
        "When the copy matches from every side, both stay still. The screen says they are the same. "
        "Last, your maths book's question comes. "
        "Drawing Cubes on a Triangular Dot Paper: the dot paper is on screen. "
        "It shows one finished teal cube at the top left. Two more cubes are drawn only in dotted lines through the dots. "
        "Drag from dot to dot to draw the missing lines of each cube. "
        "A line that runs through the dots stays. A line that misses the dots slides back. "
        "When all the lines of a cube are drawn, it turns teal like the first one. "
        "The screen shows the book's answer.",
        controls=["Drag a cube onto the grid", "Drag from dot to dot to draw a line", "Tap Check", "Reset"],
        instruction="Copy the model with cubes. Tap Check to compare.",
        feedback=["Check lays the sample and your copy side by side. A cube that is missing or misplaced glows.",
                  "A cube cannot hang in the air. It falls onto the grid or onto a cube below.",
                  "When the copy matches from every side, both models stay still. The screen says they are the same.",
                  "On the dot paper a line that runs through the dots stays. A line that misses the dots slides back.",
                  "A finished cube shows three faces that meet at one corner.",
                  "Drawing Cubes on a Triangular Dot Paper. From the picture: each cube you finish looks like the first one. "
                  "It shows 3 diamond faces that meet at one corner."],
        done_when="The copy matches the sample. Both cubes on the dot paper are finished.",
        shared_state=["gridCubes", "checkResult", "drawnLines"],
        misconceptions=["M_SH_6"],
        hints=["Look at the finished model or cube. What do you see first?",
               "Copy one part at a time. Start from the bottom or from one corner.",
               "On the grid, build the bottom layer first. On the dot paper, follow the lines from dot to dot.",
               "Tap Check to lay your copy beside the original. Fix what does not match."],
        visuals=["cube_models", "triangular_dot_paper"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 17: Lesson 6, Activity 3. Concept C12 (name one angle). One angle at a time, three answers, the answer shown at once,
    # nothing timed and nothing scored.
    "beat_the_clock": T(
        "tool_beat_the_clock", "Beat the Clock", 17,
        "Students name one angle at a time as acute, right or obtuse by comparing it with a right angle.",
        notice=NOTICE_TOOL17,
        screen=FRAME +
        "First, one angle is shown at a time. It is two straws, one green and one orange, that meet at one end. "
        "A small red arc marks the corner of every angle. The arc is the same for all, so it gives nothing away. "
        "Six angles come in a fixed mixed order. "
        "One is narrow and one is wide. One is a right angle that leans, so it is not an upright L. "
        "One is a little narrower than a right angle, and one is a little wider. The last is very wide. "
        "No angle is so close to a right angle that the paper corner cannot tell it. "
        "Every wide angle is smaller than a straight line. "
        "Three answer cards sit below: Acute, Right and Obtuse. "
        "A paper corner, a pale orange paper folded to a right angle, waits at the side. "
        "Drag it onto the angle to compare. Then tap one card. "
        "A right card turns green and the paper corner lies on the angle to show why. "
        "The small red square of a right angle appears only after the answer. "
        "A wrong card shakes gently, then can be tried again. The paper corner lies on the angle and the screen says what it shows. "
        "Then tap the right card to go on. "
        "Nothing is timed or scored, and there is no countdown. Take as long as you need. "
        "Then, after the sixth angle, a thought bubble reads the notice prompt. It is read, not answered.",
        controls=["Tap a card: Acute, Right or Obtuse", "Drag the paper corner onto the angle", "Reset"],
        instruction="Look at the angle. Tap acute, right or obtuse.",
        feedback=["A right card turns green and the paper corner lies on the angle to show why.",
                  "A wrong card shakes gently, then can be tried again. The paper corner lies on the angle and the screen says what it shows.",
                  "Inside the paper corner is acute. On the paper corner is right. Outside the paper corner is obtuse.",
                  "A right angle can lean or turn. It is still a right angle if it fits the paper corner.",
                  "The paper corner decides, not how big the angle looks.",
                  "Every angle is answered the same way. Nothing is timed or counted."],
        done_when="All six angles are named right. The thought bubble has been read.",
        shared_state=["angleIndex", "paperCornerPlaced", "chosenCard", "answered"],
        misconceptions=["M_AN_4"],
        hints=["Look at where the two straws meet. That is the angle.",
               "Compare the angle with a right angle. Is it smaller, equal or bigger?",
               "Drag the paper corner onto it. Is the second straw inside, on or outside the paper corner?",
               "Inside the paper corner is acute. On it is right. Outside it is obtuse."],
        visuals=["angle_mark", "straws_angle", "right_angle_checker"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 19: Lesson 7, Activity 2. Concept C18 (the diameter is double the radius). The lesson plan's three challenges, plain
    # numbers and no units: radius 3, diameter 10, radius 7.
    "radius_or_diameter": T(
        "tool_radius_or_diameter", "Radius or Diameter", 19,
        "Students use the fact that the diameter is double the radius to find one when given the other.",
        notice=NOTICE_TOOL19,
        screen=FRAME +
        "First, three circle challenges come one at a time on a round sheet of orange-brown paper. "
        "Each circle shows its centre as a dot. "
        "One line is drawn and marked with its number. The other line has a question mark. "
        "There are no units anywhere. "
        "Challenge 1 says, Radius 3. Find the diameter. The radius runs from the centre to the rim. "
        "The diameter is a dashed line across through the centre. "
        "Challenge 2 says, Diameter 10. Find the radius. "
        "Challenge 3 says, Radius 7. Find the diameter. "
        "Tap the answer box and type the number. " + NUMBER_PAD +
        "The screen checks it at once. "
        "A right answer shows the picture. For a diameter, the radius is laid twice along it. "
        "For a radius, the diameter folds in half at the centre. "
        "After the third answer the screen says, The diameter is double the radius. "
        "The radius is half the diameter. "
        "Then, a thought bubble reads the notice prompt. It is read, not answered.",
        controls=["Type the answer on the number pad", "Reset"],
        instruction="Find the missing radius or diameter. Type your answer.",
        feedback=["A right answer turns green. The diameter is double the radius, so 3 + 3 = 6 for challenge 1.",
                  "For challenge 2 the radius is half the diameter, so 10 ÷ 2 = 5.",
                  "For challenge 3 the diameter is double the radius, so 7 + 7 = 14.",
                  "A wrong answer shakes. The circle shows both lines again and the screen says what to check.",
                  "You may type the number you were given. The screen says you already know that line. "
                  "The other line is not the same length.",
                  "If the answer is too small for a diameter, the screen says why. "
                  "The diameter goes right across, so it is longer than the radius.",
                  "The diameter is double the radius. The radius is half the diameter."],
        done_when="All three challenges are answered right and the thought bubble has been read.",
        shared_state=["challenge", "typedDigits", "answered"],
        misconceptions=["M_CI_3", "M_CI_4"],
        hints=["Look at the circle. Which line do you know, and which line must you find?",
               "The diameter goes across through the centre. It is longer than the radius.",
               "To find the diameter, double the radius. To find the radius, halve the diameter.",
               "Double a number by adding it to itself. Halve it by splitting it into two equal parts."],
        visuals=["circle_paper"]),

    # ------------------------------------------------------------------------------------------------------------------
    # Tool 23: Lesson 8, Activity 3. Concept C13 (rigid shapes), true or false. The lesson plan's four statements, one at a time.
    # The lesson plan uses a longer word for a stick across the corners in statement 4; the child words are used here. The book's questions about pushing
    # frames stay on Tool 21.
    "true_or_false": T(
        "tool_true_or_false", "True or False", 23,
        "Students decide if each statement about rigid shapes is right or wrong and say why.",
        notice=NOTICE_TOOL23,
        screen=FRAME +
        "First, four statements come one at a time on a card, with straw shapes beside it. "
        "The straw shapes have red or pink clay joints that let a shape turn. "
        "Statement 1: A triangle is a rigid shape. "
        "Statement 2: A rectangle can change its shape when pushed. "
        "Statement 3: A triangle has four sides. "
        "Statement 4: Adding a stick across a rectangular frame, from corner to corner, makes two triangles. "
        "Two buttons sit below the card: True and False. Tap one. "
        "A right button turns green. A wrong button shakes gently, then can be tried again. "
        "Either way, the screen then shows the reason in one short sentence. "
        "It may also show the frame being pushed. "
        "A wrong try shows the reason too, and the other button waits to be tapped. "
        "For statement 1 the reason says a triangle keeps its shape when it is pushed. "
        "For statement 2 the pushed rectangle leans over into a slanting shape. "
        "For statement 3 the three sides of a triangle light up, one, two, three. "
        "For statement 4 the stick cuts the frame into two triangles. "
        "Then, after statement 4, a thought bubble reads the notice prompt. It is read, not answered.",
        controls=["Tap True or False", "Reset"],
        instruction="Read the statement. Tap True or False.",
        feedback=["A right button turns green and the reason shows in one short sentence.",
                  "A wrong button shakes gently, then can be tried again. The reason shows too, and the other button waits.",
                  "Statement 1 is true. A triangle keeps its shape when it is pushed, so it is rigid.",
                  "Statement 2 is true. A pushed rectangle leans over into a slanting shape.",
                  "Statement 3 is false. A triangle has three sides, not four.",
                  "Statement 4 is true. The stick cuts the frame into two triangles, and triangles keep their shape."],
        done_when="All four statements are answered right and the thought bubble has been read.",
        shared_state=["statementIndex", "chosenButton", "reasonShown"],
        misconceptions=["M_AN_5", "M_AN_9"],
        hints=["Read the statement slowly. Think of a straw shape you pushed.",
               "Picture the shape pushed at one corner. Does it change?",
               "Count the sides or the corners. Does the count match the statement?",
               "A rigid shape keeps its shape when it is pushed. Check the statement against that."],
        visuals=["rigid_shapes"]),

}

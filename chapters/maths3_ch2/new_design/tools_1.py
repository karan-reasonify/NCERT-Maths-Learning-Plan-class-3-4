# -*- coding: utf-8 -*-
"""Toy Joy (Class 3, chapter 2): the chapter's tool specs, one entry per APPROVED tool.

STRUCTURE STAGE (c34-tool-mapper): each entry carries tool_id, title (EXACTLY the approved name), approved_no, the ONE
learning objective and, for Tool 1, the `notice` prompts. BRIEFS STAGE (c34-brief-writer, after the user approved the
structure on 5 Nov 2026): screen, controls, instruction, feedback, done_when, shared_state and the four hints are now
written. The tool's questions are the book items (FIO in topics_N.py), never written here.

The approved list is the content team's (tool_map.md -> chapter.config.json "approved_tools"): same names, same
purposes, same order. tool_map.locked.md has the concept, the place in the flow and the proposed book items of each.

A tool here is a spec + placeholder (tools_spec/TOOL_SPEC_GUIDE.md): the tool itself is built elsewhere. Nothing below is
made yet.

Rules every tool follows (the user's decisions of 5 Nov 2026):
- a sphere is always a shaded 3D ball, never a flat disc;
- every real object is shown as its plain solid (CLASH 27): a closed shoebox, a plain bottle, an upright birthday cap, a
  plain football and a die with exact dots; the tool says only what is true of it (a ball rolls every way, a box slides and
  stands on its flat sides, a bottle rolls one way and stands on a flat end, a cap rolls round and round on its side
  and stands on its round base, a die tips over instead of rolling smoothly);
- Tool 1 names no solid; "face" in the geometric sense is first used in Tool 3 (Tool 2 uses it only for animal faces);
- the words hidden and visible are never used with the child.
"""
from __future__ import annotations

from topics_common import T  # noqa: F401

TOOLS = {
    # Tool 1: the exploration tool, right after the hook. Concept: C1 (the opening situation).
    "explore_shapes": T(
        "tool_explore_shapes_around_us", "Explore Shapes Around Us", 1,
        "Students group everyday objects that look alike and notice which ones roll, slide or stand.",
        notice=["Turn each object around. What do you notice from every side?",
                "Which objects look alike? Why do you put them together?",
                "Push each one. Which roll, slide or stand? Do the rolling ones all move the same way?"],
        screen="A bright table seen from the front. The five toys from the story stand on it, large and shaded. "
               "They are a football, a die, a shoebox, a bottle and a birthday cap. A tray under the table holds five "
               "look-alike partners. They are a marble, a cube-shaped box, an eraser, a chalk stick and a wooden cone. "
               "These object names are for the builder only. Every toy and every partner is shown as an UNLABELLED "
               "picture tile: no word is written on or under any tile, so no solid name reaches the child. No shape "
               "name is written anywhere. Only the words rolls, slides and stands appear, after a push or a "
               "try. A push shows what the object does the way it lies now. A football or a marble rolls every way. A "
               "bottle or a chalk stick lying down rolls one way. A cap or a wooden cone lying down rolls round and "
               "round. A die, a cube-shaped box, a shoebox and an eraser slide. Any object standing upright just "
               "slides when nudged.",
        controls=["Drag to turn an object", "Tap Push", "Tap Stand it up", "Drag a partner next to its toy"],
        instruction="Turn, push and stand each toy. Put the ones that look alike together.",
        feedback=["Alike pair: the partner glows beside its toy. Push both and they move the same way.",
                  "Not alike: the partner slides back to the tray. Turn both and look at every side again.",
                  "Push result: rolls every way, rolls one way, rolls round and round, or slides.",
                  "Stand result is one of these. Stands on a flat side. Stands on a flat end. Stands on its round "
                  "base. Will not stand."],
        done_when="Each toy is turned, pushed and stood up, and each partner is matched.",
        shared_state=["objectPose", "pushResult", "standResult", "partnerPairs"], misconceptions=[],
        hints=["Turn each object. Look at it from every side.",
               "Find two objects that look alike. Push them both.",
               "Push the football and the marble. Do they move in the same way?",
               "The marble looks like the football. Drag the marble next to the football."],
        # the user's decision of 5 Nov 2026 (CLASH 1): real objects, not the abstract solids, so no shape is named.
        # The five partners are look-alike objects that really are the same solid (a second clean example each).
        visuals=["football", "die", "shoebox", "bottle", "birthday_cap",
                 "marble", "cube_box", "eraser", "chalk", "wooden_cone"]),

    # Tool 2: after the concept video that names the five solids. Concept: C2 (with matching to everyday objects).
    "meet_3d_shapes": T(
        "tool_meet_the_3d_shapes", "Meet the 3D Shapes", 2,
        "Students name the five solids, even when turned, and match each to an everyday object.",
        screen="A big turntable stands in the middle. One solid sits on it at a time. The five solids wait on a "
               "shelf in the chart colours. They are a mint green cube, a yellow cuboid, a lime green cylinder, a "
               "lavender cone and a shaded red ball, the sphere. Five name cards run along the bottom. The same stage "
               "later shows three more things. First, a craft table with old boxes, bottles and a row of animal and "
               "bird faces. Second, ten real objects and a table with five columns headed Cylinder, Sphere, Cube, "
               "Cuboid and Cone. The objects are a football, a marble, a die, a cube-shaped box, a shoebox, an "
               "eraser, a book, a bottle, a chalk stick and a birthday cap. Third, a mixed picture of 13 solids with "
               "four marks: circle, tick, cross and box. It has 3 cubes, 3 cones, 3 cylinders, 3 cuboids and 1 ball. "
               "Several are tilted or lying down. The four marks wait in a tray. The word face is used here only "
               "for animal faces.",
        controls=["Drag a solid to turn it", "Tap a name card", "Drag a picture to its place",
                  "Drag a mark onto a shape"],
        instruction="Turn the solid, then tap its name. Name it even when it lies down.",
        feedback=["Right name: the card glows and the toy it looks like joins the solid. A turned solid keeps its name.",
                  "Wrong name: the card shakes and shows a clue. Cube: all sides the same. Cuboid: a box with flat sides "
                  "that can be different sizes. "
                  "Cylinder: two round flat ends. Cone: a pointed tip. Sphere: round all over.",
                  "Right column: the object stays and the count goes up by one. Wrong column: it slides back with its "
                  "clue.",
                  "Right mark: it stays, even on a tilted or lying shape. Wrong mark: it fades with a clue. The ball "
                  "needs no mark, because no mark is for a sphere.",
                  "A face put on a box or a bottle sticks. The tool names the object: a bottle is a cylinder."],
        done_when="Each solid is named, each object is sorted and the picture is marked.",
        shared_state=["selectedSolid", "turnAngle", "columns", "marks", "craftFaces"],
        misconceptions=["M_TOY_6", "M_TOY_1"],
        hints=["Turn the solid and look at all of it.",
               "Which toy does it look like? A die, a shoebox, a bottle, a cap or a football?",
               "Find the name card that goes with that toy.",
               "A die is a cube. A shoebox is a cuboid. A bottle is a cylinder. A cap is a cone. "
               "A football is a sphere."],
        visuals=["cube", "cuboid", "cylinder", "cone", "sphere", "craft_faces",
                 "die", "shoebox", "bottle", "birthday_cap", "football",
                 "marble", "cube_box", "eraser", "chalk", "book"]),

    # Tool 3: after the concept video on the parts of a solid. Concept: C4 (with C5, flat and curved).
    "faces_edges_corners": T(
        "tool_explore_faces_edges_and_corners", "Explore Faces, Edges and Corners", 3,
        "Students find the faces, edges and corners of solids and use flat and curved parts to tell solids apart.",
        screen="One big solid stands on a turntable in the chart colours. It is a cube, a cuboid, a cylinder, a cone "
               "or a shaded ball. The other four wait on a shelf. Three buttons sit below: Face, Edge and Corner. "
               "Three small counters beside the solid show how many faces, edges and corners the child has found. "
               "Each counter shows the total for that solid: cube and cuboid 6, 12 and 8; cylinder 3, 2 and 0; cone "
               "2, 1 and 1; ball 1, 0 and 0. For question 3 there are five rows with empty slots, and a card that "
               "says None of the five. For the house question the screen shows the plan's own simple house. It is a "
               "yellow cuboid for the walls and a lavender cone for the roof. It is small and far away first. After "
               "the child has tapped the parts that can be seen, it moves close up by itself. It is not Jaya's "
               "house.",
        controls=["Drag to turn the solid", "Pick Face, Edge or Corner", "Tap or trace the part on the solid",
                  "Drag a solid or a card to a row"],
        instruction="Pick Face, Edge or Corner. Then tap or trace it on the solid.",
        feedback=["Right part: it glows and says its name, such as curved edge.",
                  "Not that part: it stays dim and says what it is. A corner is a pointed place, not a whole side.",
                  "Right solid for a row: it stays in the row and says why. The cone has a flat face and a curved "
                  "face.",
                  "Wrong solid: it hops back and shows the part that does not fit. The cone has a curved edge, so "
                  "it is not in No edges.",
                  "House seen from far away: the big faces are easy to see. Then it comes close, and the edges and "
                  "corners show too."],
        done_when="Every solid is explored, the rows are full and the house is answered.",
        shared_state=["selectedSolid", "foundParts", "rowAnswers", "houseDistance"],
        misconceptions=["M_TOY_3", "M_TOY_4", "M_TOY_5"],
        hints=["Turn the solid. Look at its sides, its lines and its points.",
               "A face is a side. An edge is a line. A corner is a point.",
               "Pick Edge. Trace the line where two faces meet.",
               "Tap the glowing part. The tool tells you what it is."],
        visuals=["face_edge_corner_figure", "cube", "cuboid", "cylinder", "cone", "sphere", "simple_house"]),

    # Tool 4: after the construction image set (no video in the note). Concept: C7 (with the position words of C8).
    "shapes_in_constructions": T(
        "tool_identify_shapes_in_constructions", "Identify Shapes in Constructions", 4,
        "Students name and count the solids in a construction and say where one is using on top, under or between.",
        screen="One big picture of a model shows at a time. Each piece is a separate solid that can be tapped. First "
               "comes Jaya's rocket. It has 2 cubes, 4 cuboids, 1 cone and 1 cylinder, and all four cuboids are fully "
               "in view. The orange cylinder stands clearly between the red cuboid and the yellow cuboid. The cyan "
               "cube sits on top of the cylinder. The lavender cube is under the pink cone. Next comes Devika's toy engine. It has 1 red cylinder, 2 yellow cones, 1 grey cuboid, 1 blue "
               "cube and black wheels. Last come the four shop toys. They are a cone and a cylinder, a shaded ball on "
               "a stick, a cylinder body with a shaded ball head and no legs or ears, and a board with cubes and "
               "cuboids. Five name cards run along the bottom. Four count boxes with plus and minus sit beside the "
               "model. For the last question there are six small pictures: a table, Jaya's rocket, a football, a "
               "die, a bottle and a shoebox. The hints follow the question on screen.",
        controls=["Tap a piece or a toy", "Tap a name card", "Tap + or − to set a count", "Tap Next model"],
        instruction="Tap a piece, then tap its name. Then count each kind.",
        feedback=["Right name: the piece glows and its kind is added to the list. Each piece is counted once.",
                  "Wrong name: the piece shakes. Look at the whole piece, not only its colour, and try again.",
                  "Right count: the box turns green. Too few or too many: the pieces not yet counted glow softly.",
                  "Right position: the sentence lights up. It says: The orange cylinder is between the red cuboid "
                  "and the yellow cuboid.",
                  "Wrong position: the tool says why. Between needs a piece on each side. On top and under do not "
                  "change when you walk round.",
                  "The black wheels of the engine are not in this count."],
        done_when="The models are named and counted, and every question on screen is answered.",
        shared_state=["selectedPiece", "namedPieces", "counts", "positionAnswers"],
        misconceptions=["M_TOY_7", "M_TOY_8"],
        hints=["Look at the whole model first. Find the piece the question asks about.",
               "Go piece by piece. Say each name and count the ones with the same name.",
               "Look at the pieces next to it, above it and below it.",
               "The glowing piece is the answer. The tool names it for you."],
        visuals=["jaya_rocket", "devika_toy_engine", "shop_toys", "table", "football", "die", "bottle", "shoebox"]),

    # Tool 5: after the concept video "Let's Build Something!". Concept: C9.
    "build_and_describe": T(
        "tool_build_and_describe", "Build and Describe", 5,
        "Students arrange solid shapes into a model and describe where each shape is so others can build it.",
        screen="A building table with a wooden board. A shelf holds the five solids in the chart colours, several of "
               "each, and wooden boards. Under the table sits a sentence strip with word cards in three groups. "
               "One group is the five shape names. One group is the place words: first, then, on top of, under and "
               "between. One group is the part words: flat faces, curved faces, straight edges and curved edges. A "
               "cardboard screen can slide in "
               "front of the model. The same table also shows the boy's tower. It shows the book's question 8 model "
               "as step cards: blocks and pink cuboids, lower board, cylinders, upper board, cones. It shows the "
               "four stacked models (a) to (d) too. Friend builds puts a friend model together from the child's word "
               "cards behind the screen.",
        controls=["Drag a shape or a step card", "Tap word cards to say where it goes", "Tap Friend builds",
                  "Tap Reset"],
        instruction="Build a model. Tell your friend where each shape goes, using the word cards.",
        feedback=["A shape on a flat face stays put and clicks in. A shape that cannot rest on the one below slips off.",
                  "Same model: the friend's model and yours glow together. Your words were clear.",
                  "Different model: the tool shows the first place they differ. Check the order and the words on top "
                  "of, under and between.",
                  "Step cards in the right order click into place. A card in the wrong place slides back.",
                  "Part words: the tool checks them against the shape. A cube has flat faces and straight edges. A "
                  "cone has a flat face, a curved face and a curved edge."],
        done_when="A model stands and a friend builds the same model from the child's words.",
        shared_state=["modelPieces", "buildOrder", "wordCards", "friendModel"],
        misconceptions=["M_TOY_8"],
        hints=["Start at the bottom. Which shape goes down first?",
               "Say each shape and where it goes: first, then, on top of.",
               "Use on top of, under or between with a shape name.",
               "Say it like this: the shoebox is at the bottom. The bottle is on top of the shoebox."],
        visuals=["boy_tower", "jaya_houses", "jaya_rocket", "stacked_models",
                 "cube", "cuboid", "cylinder", "cone", "sphere"]),

    # Tool 6: after the clay, sticks and cubes demo (optional in the note). Concept: C11 and C12 (see CLASHES).
    "clay_sticks_cubes": T(
        "tool_build_with_clay_sticks_and_cubes", "Build with Clay, Sticks and Cubes", 6,
        "Students make solid shapes from clay balls and sticks and from cubes, and count the cubes used.",
        screen="Two work areas. In the clay area, beige clay balls and striped sticks sit on a shelf. Dots on the "
               "table show where the balls go for the two shapes in your maths book. In the cube area, a heap of "
               "equal cubes sits on a shelf and an empty table waits where cubes snap face to face. A tray under the "
               "table keeps each new shape made. Beside the table sit the picture to match, a row of 3 teal cubes, a "
               "cube with a long cuboid, and six white dice. The cuboid has square ends the size of the cube's "
               "face. The plan's own stack of 10 cubes sits there too, in one row, "
               "in columns of 4, 3, 2 and 1 cubes, with a count box. Every cube and ball is a separate piece that "
               "can be turned.",
        controls=["Drag a clay ball or a stick", "Drag a cube to join it", "Drag to turn what you made", "Tap Clear"],
        instruction="Join the clay balls with sticks. Then join cubes to make new shapes.",
        feedback=["Shape of 4 balls and 6 sticks done. The tool says: Your shape has 4 balls and 6 sticks. It says "
                  "nothing more about the balls or the sticks.",
                  "Cuboid frame done (only this frame). The tool says: Your frame has 8 balls and 12 sticks. A "
                  "cuboid has 8 corners and 12 edges. The balls are the corners. The sticks are the edges.",
                  "A stick with no ball at one end falls. Every stick needs a ball at each end.",
                  "Cube shape matches the picture: it glows and says Same shape, even when turned. If it does not "
                  "match, the tool shows the first cube that is different. Cubes join face to face. A cube that "
                  "touches only an edge does not stay.",
                  "Cube joined to the end of the cuboid. The tool says: You made a longer cuboid. Cube joined to the "
                  "side. It says: This shape has a step. Slide the cube to the end.",
                  "Joining 3 cubes: each new shape goes into your tray. A shape you only turned is not added again.",
                  "Count: the count box turns green when it matches the stack. Turn the stack and count again.",
                  "Six dice joined. The tool names what you made: a cuboid, a tower or steps."],
        done_when="Both clay shapes are built and every cube question is answered.",
        shared_state=["clayBalls", "sticks", "cubePlacements", "shapeTray", "countBox"],
        misconceptions=["M_TOY_5"],
        hints=["Look at the picture. Which pieces do you need?",
               "Add one piece at a time. Cubes join face to face.",
               "Put a ball on each dot. Then join two balls with a stick.",
               "The tool glows on the next piece to add. Add it, then look again."],
        visuals=["clay_and_sticks", "cube_shapes", "die", "cube", "cuboid"]),

    # Tool 7: after the comparison image (no video in the note). Concept: C10 (with the fact C6).
    "compare_and_discover": T(
        "tool_compare_and_discover", "Compare and Discover", 7,
        "Students compare solids and say in what ways they are the same and in what ways they are different.",
        screen="Five solids stand in a row in the chart colours. They are a mint green cube, a yellow cuboid, a lime "
               "green cylinder, a lavender cone and a shaded red ball. Two big circles at the top hold the two solids "
               "the child taps. The two solids turn together. Under them sit two boxes called Same and Different. A "
               "row of clue chips sits below: flat face, curved face, straight edge, curved edge, corner and all "
               "faces the same size.",
        controls=["Tap two solids", "Drag a clue to Same or Different", "Drag to turn both solids"],
        instruction="Tap two solids. Drag the clues to Same or Different.",
        feedback=["Right box: the clue clicks in. A line says why, such as Both have flat faces.",
                  "Wrong box: the clue slides back. A line says why, such as The ball has no corners.",
                  "A clue that neither solid has stays in the row. It says: Neither has this.",
                  "Cube and cuboid together: the cube's faces are all the same size."],
        done_when="Each solid is compared and every clue is placed right.",
        shared_state=["pickedSolids", "clueBoxes"],
        misconceptions=["M_TOY_2"],
        hints=["Turn both solids. Look at the flat parts, the lines and the points.",
               "Take one clue. Does the first solid have it? Does the second?",
               "If both have it, the clue goes in Same. If only one has it, it goes in Different.",
               "The cube and the cuboid both have flat faces, straight edges and corners."],
        visuals=["cube", "cuboid", "cylinder", "cone", "sphere"]),

    # Tool 8: application and revision. Concept: C14 (with the dice pattern C13, see CLASHES).
    "shape_challenges": T(
        "tool_shape_challenges_and_games", "Shape Challenges and Games", 8,
        "Students recognise solid shapes, even when turned, and read the opposite faces of a die.",
        screen="Two parts. Part one is the die. A big white die with black dots sits on a desk. It opens as in the "
               "picture before this tool: 1 dot on top, 5 dots on the left and 4 dots on the right. The child turns "
               "it with a finger. Six number buttons sit under each question. After the three answers the three sums "
               "show, and the child taps what they notice from three cards. Part two is the game, on the plan's own "
               "board. A green frame holds 24 white picture squares in a row from Start to Finish. In order they "
               "are: birthday cap, shoebox, football, die, bottle, book, wooden cone, marble, eraser, cube-shaped "
               "box, chalk, football, shoebox, birthday cap, die, bottle, book, marble, wooden cone, cube-shaped "
               "box, eraser, chalk, football, die. Some pictures are turned or lying down. Every picture is a real "
               "object that really is one of the five solids. The key sits under the board: 1 dot cylinder, 2 dots "
               "sphere, 3 dots cone, 4 dots cube, 5 dots cuboid, 6 dots move 2 steps forward if possible. The Finish "
               "mark is on the last square, the die. A counter moves to the next picture of the rolled shape, but "
               "only if that does not cross Finish. If no picture of that shape is left before Finish, the counter "
               "stays where it is. A 6 works the same way: if 2 steps would cross Finish, the counter stays. Two "
               "counters start at Start: the child's and Devika's. The tool moves Devika's counter by the same rules.",
        controls=["Drag to turn the die", "Tap a number", "Tap Roll", "Tap the picture to move to"],
        instruction="Guess the opposite face. Turn the die to check. Then play the game.",
        feedback=["Right face: both faces glow. The die turns to show they are straight across.",
                  "Wrong face: both faces glow. The die turns to show they touch. Opposite faces are on opposite "
                  "sides of the die.",
                  "After the three answers, the tool shows each pair on a usual die. One line each: 1 + 6 = 7. "
                  "2 + 5 = 7. 3 + 4 = 7.",
                  "A wrong pattern card sends the child back to one pair to add again.",
                  "Right picture in the game: the counter hops there and the shape name shows.",
                  "Wrong picture in the game: the tool names the shape in that picture. It asks for the next picture "
                  "of the rolled shape.",
                  "Roll 1 to 5: the counter moves to the next picture of that shape. If none is left before "
                  "Finish, the counter stays.",
                  "Roll 6: the counter moves 2 squares forward if it can. If that would cross Finish, the counter "
                  "stays."],
        done_when="The faces opposite 1, 2 and 3 are found and one counter reaches Finish.",
        shared_state=["dieView", "oppositeAnswers", "counterPositions", "lastRoll"],
        misconceptions=["M_TOY_10", "M_TOY_6"],
        hints=["Turn the die. Look at all six sides.",
               "The opposite face is straight across, on the other side of the die.",
               "Turn the die until the 1 is on top. Look at the bottom.",
               "On a usual die, the face opposite 1 has 6 dots."],
        visuals=["game_border", "die", "cube", "cuboid", "cylinder", "cone", "sphere",
                 "football", "shoebox", "bottle", "birthday_cap", "marble", "cube_box", "eraser", "chalk", "book",
                 "wooden_cone"]),
}

# -*- coding: utf-8 -*-
"""Shapes Around Us (Class 4, chapter 1): the chapter's tool specs, one entry per tool.

There are 26 tools. Every activity of the user's lesson plan is its own tool. This file holds the twelve tools that existed
first (Tools 1, 2, 5, 6, 9, 12, 15, 16, 18, 20, 21 and 22) and the shared FRAME; tools_2.py and tools_3.py hold the other fourteen
(Tools 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 23, 24, 25 and 26) and import FRAME from here. A tool that used to carry several activities
now holds only the one its approved purpose names; the activities that became tools of their own are listed in the SPLIT NOTES of
media_decisions.md (section 10).

STRUCTURE (steps 2 to 5, approved by the user): tool_id, title (EXACTLY the approved name), approved_no, the ONE learning objective,
and for Tool 1 its 3 `notice` prompts. BRIEFS (step 6, the brief writer): screen, controls, instruction, feedback, done_when,
shared_state, misconceptions, the four hints and the full `visuals` list.

The 26 tools are the content team's (derived from the user's lesson plan): names, purposes and order are locked in
chapter.config.json "approved_tools" (tool_map.md; core/tool_map.py verify prints a match). tool_map.locked.md holds the
concept, the place in the flow and the book items of each; content.CLASHES holds every place where the plan and the book do not fit.

Which concept each tool serves (concepts C1 to C24 are the analyst's, analysis.md section 3). The LEAD concept names the tool, the
others are book parts folded into it (the user's decisions, listed in content.CLASHES):
  Tool 1  C1 leads (buildings and block shapes), C19 hidden shapes (puzzle1) is a stage
  Tool 2  telling shapes apart by sides, corners and faces: C20 leads, with C5 border questions, C1 bricks, C19 cuts
  Tool 3  C2: name a solid and match it to its picture (new)                  Tool 4  C2: build a solid from blocks (new)
  Tool 5  C2 leads (prisms and pyramids), C5 sorting by faces follows (the Prism or Pyramid sorting)
  Tool 6  C9 (nets): fold a net, craft2 of C2 follows                         Tool 7  C9: match a net to its solid (new)
  Tool 8  C9: find the net that will not fold (new)
  Tool 9  C3 leads (label the cube), C5 sorts, C8 riddles and C23 model challenge follow
  Tool 10 C3: count the faces, edges and corners (new)                        Tool 11 C4: spin a die, opposite faces (new)
  Tool 12 C6 (build cube towers), paired with C7                              Tool 13 C6: count every cube, hidden ones too (new)
  Tool 14 C7: copy a cube structure, cubes on dot paper (new)
  Tool 15 C10 and C11 (an angle and the right angle), C10 leads, C24 right-angle counts close it
  Tool 16 C12 leads (acute and obtuse), C14 dot-grid shapes and C24 (try9) follow
  Tool 17 C12: name one angle at a time, no clock, no points (new)
  Tool 18 C16, C17, C18 as one circle tool (centre and radius, diameter, double), C16 leads
  Tool 19 C18: find the radius from the diameter and the other way, plain numbers (new)
  Tool 20 C15 leads (the pentagon, met inside the tool from the straws, no picture before it), C24 counting angles follows
  Tool 21 C13 only (rigid shapes: pushing a triangle, a rectangle, a square)
  Tool 22 a stick across a frame makes it firm (a step on from C13), C21 webs and C22 matchsticks follow
  Tool 23 C13: true or false on rigid shapes (new)
  Tools 24, 25, 26  Lesson 9: the shape identification quiz, the digital worksheet and the sample online assessment (new, no book
                    question)

HOW EVERY SPEC IS WRITTEN (one stage on screen at a time; the page frame shows only progress dots):
  The tool keeps its order, written in plain words. FIRST, one line recalls the video's idea, then a small action on OTHER objects than
  the story or picture just before. THEN, the stages that are practice, each tagged Practice: the child acts, gets immediate feedback
  that explains the result, hints, retry and Reset. Unscored, untimed. LAST, your maths book's questions of that tool, one at a time,
  in the book's order; each has a defined input (drag, tap, draw or type) and shows the book's own answer, which starts From the
  picture or Sample answer (open ones end Your answer may differ).
Controls (at most 4, each ONE plain action) are shared by all stages of a tool. Back, Next, the Hint lamp and the progress dots are
the page frame, the same in every tool, and are not tool controls.
Colour rules: prisms blue, pyramids pink, cube teal, cuboid red, sphere coral, cone yellow, cylinder orchid, every solid a shaded 3D
solid; in the sorting, matching and riddle stages (Tools 3, 5, 7 and 9) every solid has ONE neutral stone-grey tint so colour never
gives the answer; nets are never in the colour of their solid; one set of ten solids for every sorting stage (sphere, cone,
cylinder, cube, cuboid, triangular prism, hexagonal prism, triangular pyramid, square pyramid, pentagonal pyramid).
Words: always corner, and always "a stick across the corners"; a face may be flat or curved; no angle measures, no length units, no
timer, no score; angles are smaller than, equal to or bigger than a right angle (acute, right and obtuse only from Tool 16 on).
"Diamond" has ONE meaning in this chapter: a leaning four-sided shape with four equal sides and no right angle (a rhombus, as the
orange shape of the book's Four-sided shapes). A square turned so that a corner points up is called "a square tile turned on its
corner", never a diamond.
Builder notes kept out of every child-facing field: the grey tray of Tool 9 and the "every wall once" reading of the walks in Tool 22
are this chapter's own choices (question_map.md, E19 and E2); a child reads them only as "only for practice" and "in this puzzle".

A tool here is a spec + placeholder (tools_spec/TOOL_SPEC_GUIDE.md): the tool itself is built elsewhere.
"""
from __future__ import annotations

from topics_common import T  # noqa: F401

# The frame is the same in every tool, so it is written once.
FRAME = ("Frame, the same in every tool: progress dots on top; "
         "one stage on screen at a time; Back and Next at the sides and a Hint lamp that gives the four hints one at a time; "
         "a wrong try can be tried again and Reset starts the stage over; nothing is timed, scored or counted as a win. "
         "Stages that are not questions from your maths book carry a small tag, Practice. Your maths book's questions carry the book's own label, and "
         "after each try the screen shows the book's answer, which starts From the picture or Sample answer "
         "(open ones end Your answer may differ). ")


TOOLS = {
    # ---------------------------------------------------------------------------------------------------------------
    # Tool 1: the exploration tool, right after the hook video. Concept C1, with the hidden shapes of C19 (puzzle1).
    "shape_detective": T(
        "tool_shape_detective", "Shape Detective", 1,
        "Students choose the block shape that models each part of a building and spot shapes hidden in a picture.",
        notice=["What do you notice about the parts of India Gate?",
                "Which parts of the buildings can use the same block shape?",
                "What do you notice about the shapes hidden in the picture?"],
        screen=FRAME +
        "First, Practice: one line says, Diksha wants a block for every part of a building. "
        "A floor mat holds light brown wooden blocks. There are a long flat block, a tall block and a cube. "
        "There are also a can-shaped block and two half-round blocks. No picture of a building stands behind them. "
        "Tap a block to pick it up and turn it. A block resting on a curved side rolls. A block on a flat side stays still. "
        "No block has a name on it. "
        "Then, Practice: Tap the parts. Three pictures come in turn: India Gate, the Qutub Minar and a model street. "
        "Tap a part of the picture. For India Gate that is the top, a pillar or the steps. "
        "For the street it is a house, a hut or the road. "
        "A strip of block cards opens. Tap a card and the block appears beside the part as a see-through ghost. "
        "A block that fits glows green and the screen says why. "
        "A block that does not fit leaves a gap or sticks out, and the screen says which. Then the child tries another card. "
        "India Gate is an arch and the Qutub Minar tapers, so no single block fits them exactly. "
        "The screen says so and lets the child stack blocks to come close. "
        "The tool's three notice prompts come as thought bubbles after this stage. They are read, not answered. "
        "Then, Practice: Hidden shapes. A plain street scene (the model street) holds hidden shapes. "
        "The child taps something round, then something with four straight sides. "
        "Then comes something with three straight sides and a solid with a point on top. "
        "Only objects that truly show the shape are accepted. "
        "Last, your maths book's questions, 11 in all, one at a time, in the book's order. "
        "Opening, Task: drag blocks onto a build pad to model the gateway with two tall towers and the round hut. "
        "Opening, Q1: tap the part words you used (base, pillars or towers, roof). Q2: tap a reason card. "
        "Q3: tap a block picture for each part. Q4 and Q5: Compare sets the model beside the real picture, "
        "then tap the cards that fit (alike, different). "
        "A thought bubble then reads, What would happen if you removed one piece of your model? "
        "Would it still look like the building? How could you make it better? "
        "Project Work: drag shapes along the road of the model street. "
        "Qutub Minar: a child holds a stack of three green boxes and says, I have made something. Look at my Qutub Minar. "
        "Q1: tap Yes, A little or No. Q2: tap a shape card and a reason card. Q3: tap a number tile, 1 to 9. "
        "A Do you know line reads, The Qutub Minar is a World Heritage site and the tallest building made up of bricks. "
        "It has 5 storeys and 379 stairs. "
        "Puzzling Shapes, Q1: the red outlines lie over one another. Tap each outline, then tap its name card "
        "(circle, square, rectangle, triangle, cylinder). "
        "A last line says, You can also model buildings with boxes, bottles, cans and coconut shells.",
        controls=["Drag a block or a shape onto the picture", "Tap a part, a card or a number", "Tap Compare", "Reset"],
        instruction="Tap a part of the building. Pick a block that fits it.",
        feedback=["A block that fits glows green and the screen says why. A tall straight block fits a straight pillar.",
                  "A block that does not fit leaves a gap or sticks out. The screen says which. Try another block.",
                  "No single block fits India Gate's arch or the Qutub Minar's slope. The screen shows a stack that comes close.",
                  "Compare sets the model beside the real picture. Parts that match glow. Parts the model leaves out show, "
                  "such as windows and colour.",
                  "In Hidden shapes a right tap fills the outline and locks its name. A wrong tap says how many sides that "
                  "outline has.",
                  "No try is marked wrong in the open questions. Each one ends with Sample answer, and Your answer may differ."],
        done_when="Both practice stages are done, Compare was opened and the 11 questions of your maths book are answered.",
        shared_state=["chosenBuilding", "placedBlocks", "partsTapped", "compareOpen", "foundOutlines", "answers"],
        hints=["Look at the building. Find its top, its tall sides and its bottom.",
               "Ask which block would stand firm in this part. Would it leave a gap?",
               "For a tall straight part try a tall block. For a flat top try a flat block.",
               "Match the part's sides to the block's sides. A round part needs a block that can roll."],
        visuals=["india_gate_drawing", "wooden_blocks", "other_buildings", "qutub_minar", "qutub_model", "street_model",
                 "hidden_shapes"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 2: after the hidden block story. Telling shapes apart by sides, corners and faces.
    "guess_shape": T(
        "tool_guess_the_shape", "Guess the Shape", 2,
        "Students name a shape from clues about its sides, corners and faces and sort objects and flat shapes by them.",
        screen=FRAME +
        "First, Practice: one line says, Sides, corners and flat or curved parts tell shapes apart. "
        "Two real things lie on a desk, a book and a clay water pot. "
        "Tap a straight side, a corner or a curved part of either: it lights up softly and its word shows. "
        "Nothing is counted. "
        "Then, Practice: Three clues. A mystery shape sits behind a cloth. Three clue cards come one at a time. "
        "After each clue a tray shows which shapes still fit, and the others turn grey with a reason. "
        "The child taps a guess after each clue and may change it. After clue 3 the cloth lifts. "
        "Round 1: I have four equal sides. I have four corners. A chessboard has many of my smaller forms. "
        "The tray holds a square, a diamond, a long rectangle, a triangle and a circle. "
        "A diamond is a leaning shape with four equal sides and no square corner. "
        "After clue 2 the square and the diamond both fit, so clue 3 decides. "
        "Round 2: I can roll. I have no corner. I have no flat face. The tray holds a ball, a can, a cube and a box. "
        "Round 3: I have straight sides. I have three corners. The end of a tent looks like me. "
        "The tray holds a triangle, a square, a circle and a slanting four-sided shape. "
        "Last, your maths book's questions, 9 in all, one at a time, in the book's order. They come in three groups. "
        "Objects: Bricks (tap the cards that fit: box shape, flat faces, square corners, curved sides). "
        "Border Q1 to Q4: the pencil sketches of the book's border are on screen. Tap a sketch to mark it as the task says. "
        "Q1 marks a rectangular face red. Q2 marks a triangular face with a smiley. "
        "Q3 marks a curved face with a star. Q4 marks no corner blue. Tap again to undo. "
        "Flat cards: Card Game (the six cards from the end of the book are on screen). "
        "Drag them into three groups, then tap a reason card such as Only straight sides. "
        "Cuts: Puzzling Shapes Q2 and Q3. On the dot grid, drag from dot to dot to draw two lines. "
        "Q4: drag along the cut lines for shapes A, B and C. "
        "Every shape drawn as a solid is a shaded 3D solid.",
        controls=["Tap a clue, a shape, a card or a sketch", "Drag a card to its group", "Drag from dot to dot to cut",
                  "Reset"],
        instruction="Read the clues one by one. Tap the shape that fits all of them.",
        feedback=["After each clue, shapes that cannot fit turn grey and say why. The long rectangle does not have four equal sides.",
                  "After clues one and two, two shapes may still fit. A diamond has four equal sides and four corners too. "
                  "Clue three decides.",
                  "A right guess lifts the cloth and says how it fits all three clues. A wrong guess says which clue it breaks. "
                  "Try again.",
                  "A right mark on a sketch stays and says why. A die has square faces, and a square face counts as a "
                  "rectangular face.",
                  "A wrong mark shakes and says what that shape has instead. A ball has a curved face, not a triangular one.",
                  "A card dropped in the wrong group slides back and says what sides it has.",
                  "Cuts: the screen colours the pieces and counts them. Right: 1 square and 2 triangles. Wrong: it names the "
                  "pieces it found.",
                  "Cut lines are not unique. Each cut answer ends with Sample answer, and Your answer may differ."],
        done_when="Three rounds are guessed and the 9 questions of your maths book are answered.",
        shared_state=["round", "clueNumber", "guess", "markedSketches", "cardGroups", "cutLines"],
        misconceptions=["M_SH_3"],
        hints=["Read the clue again. What does it say about sides, corners or curved parts?",
               "Cross out every shape that does not fit the clue.",
               "Two shapes may still fit after two clues. The third clue must split them.",
               "Compare the two shapes left. Find the one that fits all three clues."],
        visuals=["bricks", "border_objects", "shape_cards", "dissection_shapes", "dot_grid", "sphere", "solid_pictures"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 5: Lesson 2, Activity 3, the Prism or Pyramid sorting (baskets, answer at once) and the book questions it holds.
    # Match the solids to their names is Tool 3 and building a solid from faces is Tool 4. Concept C2, with the sorting of C5.
    "prisms_pyramids": T(
        "tool_prisms_and_pyramids", "Prisms and Pyramids", 5,
        "Students sort solids one by one as prism or pyramid by looking at their faces.",
        screen=FRAME +
        "First, Practice: one line recalls both ideas. A prism has two matching end faces joined by rectangles. "
        "A pyramid has one bottom face and triangular faces that meet at one point. "
        "Two real things lie on a desk. One is a new six-sided pencil with both ends flat. "
        "The other is a wooden toy pyramid from a shape-sorter set. "
        "Tap the two ends of the pencil: they light up and match. "
        "Tap the top of the toy pyramid: the triangle faces that meet there light up. "
        "Then, Practice: Prism or pyramid? The ten solids come one at a time in a mixed order. "
        "They are the sphere, cone, cylinder, cube, cuboid, triangular prism, hexagonal prism, "
        "triangular pyramid, square pyramid and pentagonal pyramid. "
        "Every solid has the same stone-grey tint, so colour gives nothing away. "
        "The child turns each solid with the arrows and looks at its faces. "
        "Three baskets wait: Prism, Pyramid and Neither. Drag the solid into a basket. The answer shows at once. "
        "A right solid stays in its basket and the faces that explain it glow. A wrong solid slides back with a clue. "
        "Last, your maths book's questions, 12 in all, one at a time, in the book's order. "
        "Craft Q1: make a sphere-like shape with paper strips. Drag the ends of the strips to a top pin and a bottom pin. "
        "Then drag the middle of each strip outwards to make a ball. The answer starts Sample answer. "
        "Prisms Q1: three blue prisms stand side by side, as the book draws them: triangular, square and hexagonal. "
        "Tap their faces, then tap a shape card. The answer starts From the picture. "
        "Prisms Q2: tap the faces that are not rectangles, then tap a shape card under each prism. "
        "The cards are Triangle, Square and Hexagon. "
        "Prisms Q3: tap two number tiles under each prism, 1 to 8. One is for the faces of the other shape. "
        "One is for the rectangle faces. "
        "Pyramids Q1: three pink pyramids stand side by side: triangular, square and pentagonal. "
        "Tap their faces, then tap a shape card. "
        "Pyramids Q2: tap the word card one to fill the blank. All the triangular faces meet at one point. "
        "Pyramids Q3: tap the bottom face of each pyramid, then tap a shape card for it. The cards include Only triangles. "
        "In these six questions the solids keep the book's blue and pink, because each question names the family. "
        "Cube question, Is a cube also a prism?: a cube stands beside the square prism, both in the stone-grey tint. "
        "Tap their faces, then tap Yes or No. "
        "Sorting (1): two circles. A is, All faces look the same. B is, All faces do not look the same. Drag solids in. "
        "Sorting (3): two overlapping circles, rectangular faces and triangular faces, with an overlap. Drag solids in. "
        "A square face counts as a rectangular face. A solid that fits neither circle waits outside them. "
        "Sorting circles question: tap the part where the triangular prism and a pyramid with a rectangle at the bottom belong. "
        "Curved and flat: circles like the ones you just used, for curved faces and flat faces. They have an overlap. "
        "Drag the ten solids in. "
        "In every sorting question the same ten solids have the same stone-grey tint. "
        "The four sorting answers start Sample answer, for example, and end Your answer may differ. "
        "Any solid that fits the circle's rule is kept. Another fitting solid is right too.",
        controls=["Drag a solid or a strip", "Tap a face, a card or a number", "Tap an arrow to turn the solid", "Reset"],
        instruction="Turn each solid and look at its faces. Prism, pyramid or neither?",
        feedback=["A right basket keeps the solid and lights the faces that explain it. "
                  "Two matching triangle ends and three rectangles make a triangular prism.",
                  "A wrong basket slides the solid back and says what to check. "
                  "For a prism, look for two matching end faces. For a pyramid, look for triangles that meet at one point.",
                  "The cube goes in Prism. Two matching square ends joined by four squares make a square prism.",
                  "A cone has a point like a pyramid. Its side is curved, not triangles, so it goes in Neither.",
                  "All ten solids share one stone-grey tint. Only the faces decide, never the colour.",
                  "In the circles, a solid that fits two rules goes in the overlap. A square face counts as a rectangular face.",
                  "The sphere, cone and cylinder are not prisms or pyramids. "
                  "The sphere has only a curved face. The cone has one flat face and a curved face.",
                  "The cylinder has two flat faces and a curved face. The cone and the cylinder go in the overlap of "
                  "curved and flat.",
                  "Prisms and pyramids: a tapped face lights up. From the picture: every prism has rectangle faces and "
                  "every pyramid has triangle faces."],
        done_when="All ten solids are sorted into baskets and the 12 questions of your maths book are answered.",
        shared_state=["selectedSolid", "tappedFaces", "baskets", "stripBall", "circlePlacements", "answers"],
        misconceptions=["M_SH_1", "M_SH_2", "M_SH_8"],
        hints=["Turn the solid. Look at its flat faces and name their shapes.",
               "Ask: are there two matching end faces? Or one bottom face and triangles that meet at a point?",
               "Tap the end faces. Do they match? Tap the other faces. Are they rectangles or triangles?",
               "Two matching ends with rectangles between them make a prism. "
               "One bottom face and triangles meeting at one point make a pyramid."],
        visuals=["prisms", "pyramids", "solid_pictures", "paper_strip_ball", "sorting_circles", "sphere", "solid_colours"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 6: Lesson 3, Activity 1, Fold It (a cube net first, then a cuboid or a pyramid net) and the one book question it holds
    # (craft2). Which net makes which shape is Tool 7 and the wrong net is Tool 8. Concept C9 (nets), with craft2 of C2.
    "nets": T(
        "tool_nets_of_3d_shapes", "Nets of 3D Shapes", 6,
        "Students fold the net of a cube, then of a cuboid or a pyramid, into a solid.",
        screen=FRAME +
        "First, Practice: one line recalls the idea. A net is a solid opened out flat. Folding it brings the solid back. "
        "A plain brown cardboard carton lies flat on a table with dotted fold lines. It is not Diksha's pink gift box. "
        "Tap a fold line and its flap folds up. Fold every flap and the carton stands up again. "
        "Then, Practice: Fold it. A flat net sits on the table with dotted fold lines. "
        "The first net is a cross of six squares, a net for a cube. "
        "Tap a fold line to fold that face up, one face at a time. "
        "The faces close into a solid in one stone-grey tint. "
        "Then the child taps a card to choose a second net, a cuboid or a square pyramid. "
        "The cuboid net is a strip of four tall rectangles. A square sits above one and a square below the same one. "
        "The pyramid net is a square with four triangles joined to its sides. "
        "Fold it the same way. Every net here was checked by folding. "
        "Nets are flat, pale and never in the colour of a solid. "
        "Last, your maths book's question, 1 in all. "
        "Craft Q2: use the nets from the end of the book to make the models shown. "
        "The six nets are on screen: a triangular prism, a cuboid and a triangular pyramid. "
        "Then a hexagonal prism, a square pyramid and a pentagonal pyramid. "
        "Tap the fold lines of a net to fold it. Then drag the net to the model it makes. "
        "Three prisms and three pyramids stand beside the nets in one stone-grey tint. "
        "The cuboid net has square ends, so it goes with the square prism. "
        "The answer starts Sample answer and ends Your answer may differ.",
        controls=["Tap a fold line to fold the net", "Drag a net to its model", "Tap a card to choose a net", "Reset"],
        instruction="Tap a fold line to fold the net. Does it close into the solid?",
        feedback=["A net that folds closes edge to edge. No gap shows and nothing is left over. The solid appears.",
                  "The cross of six squares folds into a cube. The square with four triangles folds into a pyramid. "
                  "The strip of four tall rectangles with squares above and below one folds into a cuboid.",
                  "A face left flat keeps the solid open. A gap shows and the screen says which face is still flat.",
                  "A right match snaps in and shows the folded solid. A wrong match slides back with a hint. "
                  "This net has two hexagons, so which solid has hexagons at both ends?",
                  "Nets are drawn pale and never in the colour of a solid. The solids beside them share one stone-grey tint. "
                  "Colour never gives the match away.",
                  "Sample answer: each net folds into the solid shown beside it. Your answer may differ."],
        done_when="Both nets are folded into solids and the question of your maths book is answered.",
        shared_state=["foldedFaces", "chosenNet", "netPlacements", "answers"],
        misconceptions=["M_SH_7"],
        hints=["Look at the faces of the net. What shapes are they?",
               "Count the faces of the net. The solid must have the same faces.",
               "Tap a dotted line. Watch where each face goes when it folds.",
               "Tap each dotted line once, face by face. When no face is left flat, the solid is closed."],
        visuals=["box_net", "prisms", "pyramids", "solid_colours"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 9: Lesson 4, Activity 1, Label the Cube, and the six book questions it holds (the sorts by flat faces and straight
    # edges, the riddles and the model challenge). Count the parts is Tool 10 and Spin the shape (the die) is Tool 11.
    # Concept C3 with the sorts, the riddles and the straw model.
    # BUILDER NOTE: the grey "Only for practice" tray is this chapter's own addition for solids that fit no column of the book's sorts
    # (E2, E3 of question_map.md); the label a child reads is "Only for practice", never a word about who added it.
    "faces_edges_corners": T(
        "tool_faces_edges_and_corners", "Faces Edges and Corners", 9,
        "Students point to the faces, edges and corners of a cube and name each one.",
        screen=FRAME +
        "First, Practice: one line recalls the idea: a solid has faces, edges and corners. "
        "A real matchbox lies on a table. Tap a flat side: it lights up as a face. "
        "Tap a line where two sides meet: an edge. Tap a point where edges meet: a corner. "
        "Nothing is counted yet. "
        "Then, Practice: Label the cube. A large teal cube stands on a turntable and turns slowly. "
        "Three labels, Face, Edge and Corner, sit beside it. Drag each label to a matching part. "
        "A label that fits snaps in. Tapping a part lights it up. "
        "Last, your maths book's questions, 6 in all, one at a time, in the book's order. "
        "Sorting by flat faces: the ten solids wait in a tray in one stone-grey tint. "
        "Tap a solid to turn it. Tap its flat faces: each one lights up and a small count shows beside the solid. "
        "Drag each solid to a column headed 1, 2, 4, 5, 6 or 8 flat faces. "
        "A grey tray labelled Only for practice catches a solid that fits no column. The answer starts Sample answer. "
        "Sorting by flat faces, 3 faces: the child tries to build a solid with 3 flat faces. "
        "Flat panels, including two half circles, and one curved panel wait on the side. "
        "Drag panels to the build pad and see whether they close into a solid. Then tap Yes or No. "
        "Either tap is accepted. The answer shows both readings. It starts Sample answer. "
        "Sorting by straight edges: the same ten solids. Tap a straight edge to light it. "
        "Drag each solid to a column headed 6, 8, 9 or 12 straight edges. "
        "The same grey tray, Only for practice, catches a solid that fits no column. The answer starts Sample answer. "
        "Sorting 3D Shapes (2): two circles, A for curved edges and B for straight edges. Drag solids in. "
        "A solid with no edges goes in the grey tray. The answer starts Sample answer. "
        "Solids Q1: seven solids stand in one stone-grey tint. They are a square pyramid, a cone and a sphere. "
        "They are also a cuboid, a cylinder, a cube and a triangular prism. Six clue cards, a to f, wait beside them. "
        "Drag each clue card onto a solid, then tap that solid's name card. "
        "A thought bubble then reads, Each one is different. How? The answer starts From the picture. "
        "Model challenge: four cards, a to d, each give a count of straws and clay balls. "
        "Card a gives 12 straws and 8 balls. Card b gives 9 and 6. Card c gives 15 and 10. Card d gives 10 and 6. "
        "Straws are the edges and clay balls are the corners. "
        "Drag that many straws and balls to the pad and join them into a solid that closes. Then tap a name card. "
        "The name cards are the ten solid names. One more card reads, Not one of the solids so far. "
        "A cube and a cuboid both fit 12 straws and 8 balls, so either card is right. "
        "A model that closes but matches none of the ten names takes that last card. "
        "The answer starts Sample answer. "
        "In every sorting and riddle question the solids have one stone-grey tint.",
        controls=["Drag a label, a solid, a straw, a ball or a panel", "Tap a part, a face or a card",
                  "Tap an arrow to turn the solid", "Reset"],
        instruction="Drag each label to its part of the cube. Tap a part to light it.",
        feedback=["A tapped part lights up. A label that fits snaps in. A wrong label slides back and says what to look at.",
                  "A flat side is a face. A line where faces meet is an edge. A point where edges meet is a corner.",
                  "A face can be flat or curved. A cone has one flat face and a curved face. "
                  "A cylinder has two flat faces and a curved face.",
                  "Sorting: a solid in the right column stays and says why. A wrong one slides back and shows its count.",
                  "The grey tray is only for practice. It holds solids that fit no column of your maths book.",
                  "Sample answer: the sphere has no flat face. A pentagonal pyramid has 10 straight edges and a hexagonal "
                  "prism has 18.",
                  "Sample answer: a solid with only flat faces needs at least 4 faces. "
                  "A cylinder cut in half along its length has 3 flat faces and 1 curved face. Your answer may differ.",
                  "A riddle card that fits keeps its solid and says which clue decides. "
                  "Clue f fits a cube and a cuboid, so both are right.",
                  "A model that closes but is none of the ten solids gets a special card. "
                  "The card reads, Not one of the solids so far.",
                  "In the sorting and riddle stages every solid has the same stone-grey tint. Colour never gives the answer."],
        done_when="The cube is labelled and the 6 questions of your maths book are answered.",
        shared_state=["labelsPlaced", "tappedParts", "sortColumns", "circlePlacements", "riddleMatches", "builtModel"],
        misconceptions=["M_SH_3", "M_SH_4", "M_SH_5", "M_SH_9"],
        hints=["Look at one solid. A face is a side, an edge is a line, a corner is a point.",
               "Count one kind of part at a time. Tap each part once.",
               "Turn the solid with the arrows. Tap each flat face, or each straight edge, once.",
               "Tap the parts one by one and watch the count. The last number shows where the solid goes."],
        visuals=["straws_and_clay", "solid_pictures", "prisms", "pyramids", "sphere", "sorting_circles", "solid_colours"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 12: Lesson 5, Activity 1, Build a cube tower (three cubes; two at the bottom and one on top; six cubes; count the cubes
    # used) and the one book question it holds (build1). Look carefully is Tool 13 and Copy the cube structure and the dot paper
    # are Tool 14. Concepts C6 and C7, paired; C6 leads.
    "cube_towers": T(
        "tool_cube_towers_and_drawings", "Cube Towers and Drawings", 12,
        "Students build cube towers from small cubes and count the cubes they used.",
        screen=FRAME +
        "First, Practice: one line recalls the idea: count a tower layer by layer, and count the hidden cubes too. "
        "A little step of cubes stands on a tray: a bottom layer of 2 by 2 and one cube on top. "
        "Tap the top layer to lift it off: 1 cube. Tap the bottom layer: 4 cubes. 1 + 4 = 5. "
        "Then, Practice: Build a cube tower. Challenge cards come one at a time. "
        "The first asks for a tower with three cubes. The second asks for a step with two cubes at the bottom and one on top. "
        "The third asks for a structure with six cubes. "
        "A box of small cubes waits beside an empty pad. Drag cubes from the box onto the pad. "
        "A cube cannot hang in the air: it falls onto the pad or onto a cube below. "
        "After each build, tap a number tile, 1 to 9, for all the cubes you used. "
        "The right number lifts the layers one by one and adds them. "
        "Every cube is a shaded teal cube with clear edges. Layers are told apart by their steps, not by colour. "
        "Last, your maths book's question, 1 in all. "
        "Build with Cubes: models A, B, C and D come one at a time. "
        "Drag cubes onto the pad to copy the model. You may drag a whole row of cubes at once. "
        "Tap a turn arrow to turn your model round. Tap Check to set it beside the picture. "
        "The answer starts From the picture.",
        controls=["Drag a cube onto the pad", "Tap an arrow to turn the model", "Tap a layer, Check or a number", "Reset"],
        instruction="Build the tower with cubes. Count every cube, the hidden ones too.",
        feedback=["A cube cannot hang in the air. It falls onto the pad or onto a cube below.",
                  "A right total lifts the layers and adds them. For the step, 2 + 1 = 3 cubes.",
                  "A wrong total does not show the number. The layers lift off again so you can recount.",
                  "Too many or too few cubes: the card says how many more or fewer it needs.",
                  "Hidden cubes count. A cube you cannot see is still in its layer.",
                  "Six cubes can be built in many ways. Every build of six cubes with none in the air is right.",
                  "A model is right when it looks like the picture from every side. Turn it round to check.",
                  "From the picture: each model you build looks like its picture when you turn it round."],
        done_when="The three towers are built and counted and models A to D of your maths book are copied.",
        shared_state=["placedCubes", "liftedLayers", "chosenTotal", "modelTurn", "answers"],
        misconceptions=["M_SH_6"],
        hints=["Look at the card. How many cubes does it ask for?",
               "Build the bottom layer first. Then place cubes on top of it.",
               "Count one layer at a time. Then add the layers.",
               "Tap the top layer to lift it off. Count its cubes. Then lift the next layer."],
        visuals=["cube_models", "cube_towers"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 15: after the straws and paper corner story. Concepts C10 and C11, paired; C24 right-angle counts close it.
    "angle_builder": T(
        "tool_angle_builder", "Angle Builder", 15,
        "Students make angles smaller than, equal to and bigger than a right angle, and find right angles with a paper corner.",
        screen=FRAME +
        "First, Practice: one line recalls the idea. Two lines that meet at a point make an angle. "
        "The corner of a paper fold is a right angle. "
        "A laptop stands open on a table. Drag its lid: the lid and the keyboard are two lines that meet at the hinge, "
        "and the angle opens and closes. "
        "Then, Practice: Make an angle. Two arms meet at a point on a board. "
        "The paper corner lies fixed on the lower arm. It is pale orange paper with a small red square. "
        "Drag the other arm. "
        "Three challenge cards ask for an angle smaller than, equal to and bigger than a right angle. "
        "The screen shows the arm inside the paper corner, on it or outside it. No numbers show. "
        "The lower arm is long and the upper arm is short, and both keep their length. "
        "The upper arm swings from the lower arm up to a straight line and stops there. "
        "No angle is bigger than a straight line. "
        "Then, Practice: Check a turned square. A square tile turned on its corner and a slanting four-sided shape "
        "lie on the board. Drag the paper corner onto each corner and tap whether it fits. "
        "Last, your maths book's questions, 10 in all, one at a time, in the book's order. "
        "Example, the house: tap each red mark to count to 7. "
        "When Lines Meet, the boat: tap each angle, then tap a number tile. "
        "Let Us Do Q1: five pictures (scissors, hanger, hand, seesaw, slide). "
        "Tap the places where two lines meet and a red arc appears. "
        "Q2: object cards of a classroom (a desk, a door, a clock, a window, a ball and a round plate). "
        "Tap the cards that show angles. The ball and the plate show none. "
        "Right Angles, make: tap the fold lines to fold the paper in half, then in half again. Then tap the paper to open it. "
        "Right Angles, dot grid: eight angles. Tap the ones you think are right angles, "
        "then drag the paper corner onto each to check. "
        "Right Angles, objects: drag the paper corner onto a corner of a book, a window and one more object. "
        "Then tap Right angle or Not a right angle. "
        "Let Us Do (right angles) Q1: on the dot grid, drag from a dot to draw a line across. "
        "Then draw a line up from the same dot. Check it with the paper corner. "
        "Let Us Try Q8: six figures. Drag the paper corner onto each corner, tap the right angles, "
        "then tap a number tile for each figure. Then tap the figures that have only right angles.",
        controls=["Drag an arm, the paper corner or a line", "Tap a place, a card or a number",
                  "Tap a fold line to fold the paper", "Reset"],
        instruction="Drag the arm to open the angle. Compare it with the paper corner.",
        feedback=["Arm inside the paper corner: the angle is smaller than a right angle. Arm on it: the red square lights up, "
                  "a right angle. Arm outside it: bigger than a right angle.",
                  "No numbers show. The paper corner decides.",
                  "A longer arm does not make a bigger angle. Only swinging the arm changes it. The arm stops at a straight line.",
                  "A turned corner can still be a right angle. The paper corner fits a square tile turned on its corner.",
                  "The paper corner fits: a right angle, with the red square. It does not fit: the screen says smaller or "
                  "bigger than the paper corner.",
                  "Counting marks: a counter adds one for each angle tapped. From the picture: the house has 1 + 2 + 2 + 2 = 7. "
                  "The boat has 2 + 2 + 2 + 4 = 10.",
                  "A right answer card turns green and says why. A wrong one shakes and shows the part to look at again."],
        done_when="Three angles are made, the turned square is checked and the 10 questions of your maths book are answered.",
        shared_state=["armPosition", "paperCornerPlaced", "markedAngles", "foldedPaper", "drawnLines", "answers"],
        hints=["Drag the arm. Watch how the angle changes.",
               "Lay the paper corner on the angle. Is the arm inside it, on it or outside it?",
               "Open the arm until its edge lines up with the edge of the paper corner.",
               "Inside the paper corner is smaller. On it is a right angle. Outside it is bigger."],
        visuals=["angle_mark", "straws_angle", "yoga_figures", "house_and_boat", "angle_pictures", "right_angle_checker",
                 "angle_figures_grid", "dot_grid", "right_angle_figures"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 16: after the narrow and wide corners story. Concept C12: the sorting of angles into acute, right and obtuse, in pictures
    # and in shapes; C14 dot-grid shapes and try9 of C24 follow. The one-angle-at-a-time naming is Tool 17.
    "angle_sorting": T(
        "tool_angle_sorting", "Angle Sorting", 16,
        "Students sort angles as acute, right or obtuse by comparing each with a right angle, in pictures and in shapes.",
        screen=FRAME +
        "First, Practice: one line recalls the idea: an acute angle is less than a right angle, and an obtuse angle is more. "
        "A paper hand fan lies on a table. Drag its last stick to open it: a little, to a right angle "
        "(a small red square), then wide. "
        "Each time the screen says smaller than, equal to or bigger than the paper corner. "
        "Then, Practice: Sort the angles. Six angles sit in a row: two smaller than a right angle, one right angle "
        "and three bigger. They are shown without numbers and all are smaller than a straight line. "
        "Three boxes wait: Acute, Right and Obtuse. Drag the paper corner onto an angle to compare. "
        "Then drag the angle into a box. The answer shows at once. "
        "Last, your maths book's questions, 10 in all, one at a time, in the book's order. "
        "Acute and Obtuse Angles, objects (acute): picture cards of classroom objects lie in a row. "
        "The cards show a sharp pencil tip, scissors opened a little and a set square's pointed corner. "
        "They also show a door opened wide, a laptop lid leaned back and a book's corner. "
        "Tap the cards that show an acute angle. "
        "Objects (obtuse): tap the cards that show an obtuse angle. "
        "Letters: the letters V, A and Z. Tap each place where two strokes meet, then tap Acute, Right or Obtuse. "
        "Let Us Do Q1 (acute): on the dot grids, drag from the end of each given line to draw a second line. "
        "It must make an acute angle. The paper corner checks each one. "
        "Q1 (obtuse): do the same to make an obtuse angle. "
        "Q2: four stick figures. Tap an angle, then tap a colour: red for acute, green for right, blue for obtuse. "
        "Shapes on a dot grid: drag from dot to dot to draw three- and four-sided shapes. "
        "Check the corners with the paper corner, and tap the shapes that have a right angle. "
        "Discuss: tap number tiles for how many shapes you made with 1, 2, 3 or all right angles. "
        "Four-sided shapes: three four-sided shapes stand beside a rectangle and a square. "
        "Drag the paper corner onto their corners, then tap the cards that say how they differ. "
        "Let Us Try Q9: fourteen shapes numbered 1 to 14. Tap the shapes that fit each of the four clues. "
        "More than one shape may fit a clue. "
        "Every answer starts Sample answer, except Q9, which starts From the picture.",
        controls=["Drag an angle, the paper corner or a line", "Tap an angle, a card or a number",
                  "Tap a colour to mark an angle", "Reset"],
        instruction="Lay the paper corner on each angle. Sort it: acute, right or obtuse.",
        feedback=["Inside the paper corner is acute. On it is a right angle. Outside it is obtuse.",
                  "The paper corner decides, not how big an angle looks.",
                  "A correct sort stays in its box and says why. For example: it is wider than the paper corner, so it is obtuse.",
                  "A wrong sort slides back and shows the paper corner laid on the angle.",
                  "On a dot grid the paper corner reads each angle you draw. A wrong kind says it is too narrow or too wide.",
                  "Every obtuse angle in the practice stage is smaller than a straight line.",
                  "Sample answer: a rectangle and a square have 4 right angles. The three shapes shown have none. "
                  "A square is a special kind of rectangle.",
                  "Sample answer: no 3-sided or 4-sided shape has exactly 3 right angles. "
                  "A 4-sided shape with 3 right angles has a fourth right angle too.",
                  "In the last question more than one shape can fit a clue. Every fitting shape lights up."],
        done_when="The six angles are sorted and the 10 questions of your maths book are answered.",
        shared_state=["checkerPlaced", "sortedAngles", "chosenKind", "drawnAngles", "colouredAngles", "answers"],
        misconceptions=["M_AN_4"],
        hints=["Put the paper corner on the angle, with its corner on the angle's corner.",
               "Look at the second arm. Is it inside, on or outside the paper corner?",
               "Inside is acute. On it is a right angle. Outside is obtuse.",
               "Acute: less than a right angle. Right: equal to it. Obtuse: more than a right angle."],
        visuals=["angle_mark", "angle_letters", "stick_figures", "dot_grid", "four_sided_shapes", "shape_gallery",
                 "right_angle_checker"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 18: after the circle on the ground story. Concepts C16, C17 and C18 as one circle tool. 13 book questions: the cap.
    "circle_detective": T(
        "tool_circle_detective", "Circle Detective", 18,
        "Students make a circle, name its centre, radius and diameter, and show that the diameter is double the radius.",
        screen=FRAME +
        "First, Practice: one line recalls the idea: a circle has a centre, a radius and a diameter. "
        "A round steel plate lies on a table with a dot in its middle. "
        "Tap the plate: it spins, and the dot stays still while the rim goes round it. "
        "Nothing is named and nothing is measured. "
        "Then, Practice: Label the parts. A large circle shows its centre, one radius and one diameter, marked but "
        "not labelled. Three labels, Centre, Radius and Diameter, wait beside it. Drag each label to its place. "
        "When all three are placed the screen shows the right answers. "
        "Then, Practice: Radius, diameter or neither? Three lines are drawn on a circle. "
        "One goes from the centre to the rim. One goes across through the centre. "
        "One goes across and misses the centre. "
        "Tap a card for each: Radius, Diameter or Neither. "
        "Last, your maths book's questions, 13 in all, one at a time, in the book's order. "
        "Circle with straws: drag straws of the same length round a middle clay ball like spokes. "
        "Q1: tap Equal or Unequal. "
        "Q2: swap some straws for longer or shorter ones by dragging, then tap a card for what happens. "
        "Let Us Make: drag the scale from point A and tap to mark many points the same distance from A. "
        "Then drag a line by hand through the points, and tap the name card for what you get. "
        "Amazing Circles: a dotted guide line lies across the paper circle. It always passes through the middle. "
        "Drag an end of the guide line to turn it to a new direction. "
        "Then tap Fold: the paper folds in half along the guide line. Open the fold and the crease stays. "
        "Do this three times. Each time the guide line points a new way. It cannot sit on a crease already made. "
        "Drag the thread along each crease. "
        "Q1: tap Equal or Unequal. Q4: drag the thread from the centre to the border along a crease. "
        "Let Us Do: tap Fold and the circle folds in half along a diameter. "
        "Tap Fold again: the half folds in half, and its crease from the centre to the border is a radius. "
        "Drag the radius thread along the diameter, then tap Half or Double. "
        "Compass design: drag the compass point to a place and drag its pencil round. "
        "Then follow Step 1 to Step 3 and tap colours for the petals. "
        "Carpet design: tap the centre. Drag a line from the centre to the edge, a radius. "
        "Drag a line across through the centre, a diameter. Pick any colour. "
        "Wheels Q1: tap the word card, circles. "
        "Q2: four wheels, A to D, hang straight on hooks on a plain wall, so each is a true circle. "
        "Drag the thread across each to compare. Then tap the wheel for the longest radius, the shortest radius, "
        "the longest diameter and the shortest diameter. "
        "Lengths are shown with the thread and never with numbers. "
        "A line reads, You can measure with a paper strip or a thread, and another, Try circles of different sizes.",
        controls=["Drag a straw, a label, the scale, the thread, the compass or a line", "Tap a card, a wheel or a place",
                  "Tap Fold to fold the paper in half", "Reset"],
        instruction="Find the centre, radius and diameter of a circle. Then make circles.",
        feedback=["A label that fits snaps in. A wrong label slides back and says what to check. The radius touches the centre "
                  "and the border.",
                  "A line across a circle that misses the centre is not a diameter. Every diameter passes through the centre.",
                  "Straws of the same length make a circle. Their ends all sit the same distance from the middle.",
                  "Straws of different lengths do not make a circle. Their ends make an uneven shape.",
                  "Each fold in half makes a crease that crosses the others at the centre. The thread shows every crease is "
                  "the same length.",
                  "Fold the half in half again. The diameter is double the radius, and the radius is half the diameter.",
                  "Lengths are shown with the thread, never with numbers. You can also measure with a paper strip or a thread.",
                  "The compass point stays on the centre and the pencil draws the circle. Try circles of different sizes.",
                  "From the picture: wheel B is the biggest and wheel D the smallest. A wheel with a longer radius has a longer diameter."],
        done_when="Both practice stages are done and the 13 questions of your maths book are answered.",
        shared_state=["placedLabels", "strawCircle", "creases", "threadLengths", "compassCircles", "wheelAnswers"],
        hints=["Look at the circle. Find its middle point first.",
               "The radius touches the centre. The diameter goes across through the centre.",
               "Fold the paper in half. The crease is a diameter. Fold again to find a radius.",
               "Drag the radius thread along the diameter. See how many radius threads fit."],
        visuals=["equal_straws_circle", "circle_paper", "compass_design", "carpet_design", "wheels", "compass"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 20: Lesson 7, Activity 3, right after Radius or Diameter (Tool 19). The pentagon is met inside the tool, from the
    # straws themselves, with no picture before it. Concept C15, with the angle counting of C24 as the
    # last questions.
    "build_pentagon": T(
        "tool_build_a_pentagon", "Build a Pentagon", 20,
        "Students make a pentagon from five equal sides, say it has five sides and five corners, and see its angles change when "
        "pushed.",
        screen=FRAME +
        "First, Practice: one line says, Straws and clay balls make shapes. A straw is a side and a ball is a corner. "
        "The tool opens with the straws and no picture. A tray holds straws and clay balls. "
        "Drag three straws and three balls to make a triangle. Then drag four straws and four balls to make a four-sided shape. "
        "Tap each ball to count the corners: 3, then 4. "
        "A card then asks, What shape will five equal straws make? "
        "A second tray holds eight straws and six clay balls. Five straws are long and all the same length. "
        "Three straws are shorter and each of the three is a different length (short, shorter, shortest). "
        "Pick five straws of the same length. Drag them end to end with a ball at each joint to close a ring. "
        "The closed ring settles into a neat five-sided shape. The screen then says, "
        "This ring has 5 sides and 5 corners. It is called a pentagon. "
        "Then, Practice: Try other rings and push. The child may also try five straws of unequal lengths, "
        "for example the three shorter straws and two long ones. "
        "That ring closes too, with five sides and five corners, but its sides are not equal. "
        "It does not settle into the neat shape. The screen says, "
        "This ring has 5 sides, so it is a pentagon too. Its sides are not equal. "
        "Four or six straws do not make a pentagon. "
        "Tap each ball and count the corners. Tap each straw and count the sides. "
        "Then drag one side of the pentagon to push it. The ring leans over. "
        "A red mark at each corner shows how its angle changed. "
        "The starting ring stays as a faint ghost, so before and after can be compared. "
        "The straws and balls lie flat on a board. "
        "Last, your maths book's questions, 8 in all, one at a time, in the book's order. "
        "Pentagon, make: build the same ring from five equal straws. A tick shows when five equal straws close it. "
        "Q1: are these right angles? Drag the paper corner onto each corner, then tap Yes or No. "
        "Q2: push one side, then tap Yes or No. "
        "Q3: compare before and after, then tap the cards, for example Some angles get smaller and some get bigger. "
        "Let Us Try Q6: seven flat shapes, a to g. Drag each to the box 3 angles, 4 angles or 5 angles. "
        "What relation do you notice: tap the card for the number of sides and the number of angles. "
        "Q7: on the dot grid, drag from dot to dot to draw a shape with fewer than 5 angles. "
        "Then draw a shape with more than 5 angles. The screen counts the corners. "
        "Pentagon, make and Q3 start Sample answer. Q1 and Q2 start From the picture. "
        "Let Us Try Q6 and its relation start From the picture. Q7 starts Sample answer.",
        controls=["Drag a straw, a ball, a side, a shape or the paper corner", "Tap a corner, a card or a number",
                  "Drag from dot to dot to draw", "Reset"],
        instruction="Join five equal straws into a ring. Count the corners. Then push.",
        feedback=["A ball marks one corner and a straw is one side. A triangle has 3 sides and 3 corners. "
                  "A four-sided shape has 4 sides and 4 corners.",
                  "Five straws of the same length close into a ring with five joints. The pentagon has 5 sides and 5 corners.",
                  "Five straws of unequal lengths also close into a ring with 5 sides. It is a pentagon too, but its sides "
                  "are not equal.",
                  "Four or six straws do not make a pentagon. The screen says how many sides the ring has.",
                  "Push a side and the ring leans over. Its shape changes even though every straw keeps its length.",
                  "Some angles get smaller and some get bigger when you push. Each angle of the first ring is bigger than a "
                  "right angle.",
                  "From the picture: a shape with 3 sides has 3 angles. 4 sides give 4 angles and 5 sides give 5 angles.",
                  "A right box keeps its shape and says how many corners it has. A wrong box slides back and shows the count.",
                  "Drawn shapes: the screen counts the corners. 3 or 4 corners is fewer than 5 angles. 6 or more is more than 5."],
        done_when="The pentagon is built, counted and pushed, and the 8 questions of your maths book are answered.",
        shared_state=["chosenStraws", "ringClosed", "countedCorners", "pushedRing", "boxes", "drawnShapes"],
        misconceptions=["M_AN_7", "M_AN_8"],
        hints=["Look at the shapes you made. A triangle has 3 sides and 3 corners.",
               "Join the straws end to end with a ball at each joint. Close the ring.",
               "Count the balls. Count the straws. Compare the two numbers.",
               "Pick five straws of the same length and join them in a ring. Then tap each ball to count."],
        visuals=["rigid_shapes", "angle_shapes", "dot_grid", "angle_mark", "right_angle_checker"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 21: after the push the straw shapes story. Concept C13.
    "triangle_rectangle": T(
        "tool_triangle_vs_rectangle", "Triangle vs Rectangle", 21,
        "Students show that a triangle keeps its shape when pushed and that a rectangle's angles change.",
        screen=FRAME +
        "First, Practice: one line recalls the idea: a rigid shape keeps its shape when it is pushed. "
        "Before any push, the child guesses. "
        "Two frames from home are shown and not pushed: a window frame with four sides and a shelf bracket with three sides. "
        "Tap the frame you think will keep its shape when pushed. The guess is kept. "
        "Then, Practice: Push the frames. A board holds a straw triangle and a straw rectangle joined by clay balls. "
        "They lie flat and are pinned to the board along their bottom sides. "
        "Drag the top corner of each frame to push it. The rectangle leans into a slanting shape. The triangle does not change. "
        "Then tap the frame you think is more rigid. The first guess is shown beside the result. "
        "Last, your maths book's questions, 10 in all, one at a time, in the book's order. "
        "Shapes with Straws, triangle: drag three straws of different lengths and three clay balls to join a triangle. "
        "Push the triangle: push one side, then tap Yes or No. "
        "Trace: drag a pencil along the three sides on paper. "
        "Angles of a triangle: drag the paper corner onto each corner, then tap Acute, Right or Obtuse for each. "
        "Rectangle: drag two long and two short straws and four balls, and push until every corner fits the paper corner. "
        "Angles of a rectangle: drag the paper corner onto each corner, then tap a card. "
        "Push the rectangle: push one side, then tap Yes or No. "
        "The new shape: tap Compare to see before and after. Drag the paper corner onto each corner. "
        "Then tap the cards: still right angles, and which kinds. "
        "Square: push one side of a square, check the corners, then tap the cards. "
        "Compare: tap the cards for how the angles of triangles and rectangles are alike or different.",
        controls=["Drag a straw, a corner, the paper corner or a pencil", "Tap a card, Yes or No",
                  "Tap Compare to see before and after", "Reset"],
        instruction="Push a corner of each frame. Which one keeps its shape?",
        feedback=["Push the triangle: it does not change. Its three straws cannot change length, so its corners cannot change.",
                  "Push the rectangle: it leans over into a slanting shape. The straws keep their length, but the corners turn.",
                  "From the picture: before the push the rectangle has 4 right angles. After it, two angles are acute and two are obtuse.",
                  "A pushed square does the same: two acute angles and two obtuse angles.",
                  "A triangle keeps its shape when it is pushed. It is the most rigid shape.",
                  "Sample answer: this triangle has three acute angles. Another triangle can have a right angle or an obtuse angle.",
                  "The paper corner decides every angle. Smaller than a right angle is acute. Equal is right. Bigger is obtuse.",
                  "A right answer card turns green and says why. A wrong one shakes and shows the corner to check again."],
        done_when="The guess is made, both frames are pushed and the 10 questions of your maths book are answered.",
        shared_state=["guess", "framePositions", "paperCornerPlaced", "beforeAfter", "answers"],
        hints=["Look at each frame. Which corners can turn when you push?",
               "Push a corner slowly. Watch the sides and the angles.",
               "Lay the paper corner on a corner of the frame before the push and after it.",
               "Push both frames the same way. Compare each frame with its shape before the push."],
        visuals=["rigid_shapes", "angle_mark", "right_angle_checker"]),

    # ---------------------------------------------------------------------------------------------------------------
    # Tool 22: after the two webs story. A stick across a four-sided frame makes it firm; the book items are webs and matchsticks.
    # "Strong or wobbly" as true or false statements is Tool 23.
    # BUILDER NOTE: "every wall once" is the chapter's chosen reading of the two walk questions (question_map.md E19);
    # a child reads only "In this puzzle we walk every wall once."
    "strong_structure": T(
        "tool_build_a_strong_structure", "Build a Strong Structure", 22,
        "Students add a stick across a four-sided frame to make triangles and see that the frame becomes firm.",
        screen=FRAME +
        "First, Practice: one line recalls Squiggly's idea: a stick across a four-sided frame makes triangles. "
        "Before building, the child guesses. "
        "A wooden garden gate frame with four sides is shown without any brace. "
        "Tap the spot where one stick could go to stop it leaning. The guess is kept. "
        "Then, Practice: Build a square frame. Drag four sticks and four joints to make a square on a board. "
        "Then push a corner and watch it lean into a slanting shape. "
        "Add one stick across the corners, from one corner to the opposite corner: the square splits into 2 triangles. "
        "Push again: the frame keeps its shape. "
        "Tap Check to set before and after side by side, then tap a reason card such as Triangles cannot change. "
        "Last, your maths book's questions, 7 in all, one at a time, in the book's order. "
        "Let Us Try Q1, triangles: tap each triangle in Squiggly's web to count it, then tap digit tiles to type the total. "
        "Squiggly's walk: drag a pencil along the walls from A. Each wall gets its number. "
        "A wall cannot be used twice. The walk is checked when it returns to A. "
        "Rectangles: tap each rectangle in Wiggly's web to count it, then tap digit tiles to type the total. "
        "Wiggly's walk: drag a pencil from A along the walls to B without using a wall twice. "
        "In this puzzle every wall is walked once. "
        "The four answers about the webs start From the picture. "
        "Q2: drag five matchsticks to make 2 triangles in the drawing box. "
        "Q3: drag two of the nine matchsticks to new places to make 4 triangles. "
        "Q4: tap 4 of the 13 matchsticks to remove them so that only 3 triangles stay, then tap Check. "
        "The three matchstick answers start Sample answer and end Your answer may differ. "
        "The sticks lie flat on the table. The spider webs keep the book's purple threads, "
        "and the matchsticks have red heads.",
        controls=["Drag a stick, a corner or a pencil", "Tap a card, a frame, a stick or a digit",
                  "Tap Check to count or compare", "Reset"],
        instruction="Build a square frame. Add a stick across the corners. Push it.",
        feedback=["Push the plain square frame and it leans into a slanting shape.",
                  "Add a stick across the corners. The frame splits into 2 triangles and keeps its shape when pushed.",
                  "A frame made only of triangles keeps its shape. A frame with a four-sided cell can lean over.",
                  "Squiggly's web is all triangles, so it keeps its shape. Wiggly's web has four-sided cells, so it can lean.",
                  "Counting: every tap lights one triangle or rectangle. Big and small ones both count.",
                  "From the picture: 1 + 1 + 4 + 4 = 10 triangles. 1 + 6 + 2 + 2 + 1 = 12 rectangles.",
                  "From the picture: Squiggly's walk uses every wall once and ends at A. The numbers 1 to 12 show it. "
                  "In this puzzle we walk every wall once.",
                  "From the picture, with every wall walked once: no walk goes from A to B. Two corners have 3 walls each.",
                  "If he may skip walls, a walk from A to B without a repeat exists.",
                  "Sample answer: two triangles that share one stick use 5 sticks. 3 + 3 − 1 = 5.",
                  "Sample answer: move two sticks to make 4 triangles. Remove 4 sticks to leave 3 triangles with no stray "
                  "stick. Other answers can be right too.",
                  "The checker counts triangles and stray sticks. Open answers end with Sample answer, and Your answer may differ."],
        done_when="The square frame is built, pushed, braced and pushed again, and the 7 questions of your maths book are answered.",
        shared_state=["frameSticks", "pushedFrame", "walkPath", "countedShapes", "matchsticks", "answers"],
        misconceptions=["M_PU_1", "M_PU_2", "M_PU_3"],
        hints=["Look at the frame. Does it lean when you push it?",
               "Put a stick across from one corner to the opposite corner. How many triangles does it make?",
               "Push the frame again. Compare it with before.",
               "A stick across the corners makes triangles, and a frame of triangles keeps its shape."],
        visuals=["spider_webs", "matchsticks", "squiggly_and_wiggly", "rigid_shapes"]),
}

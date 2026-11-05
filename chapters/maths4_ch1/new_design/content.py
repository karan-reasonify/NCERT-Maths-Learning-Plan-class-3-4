# -*- coding: utf-8 -*-
"""TEMPLATE - chapter-level authored content: the one place the book's own facts live. Fill in every TODO.

The topics themselves (modules -> topics -> concepts) belong in topics_N.py; this module holds chapter-wide data that
every topic refers to by key: the identity, the modules, the chapter's story (characters, setting), the visual key,
every NCERT item, the misconceptions, the open clashes.

No em dash and no en dash anywhere in any string (gates/media_content.py scans the whole built plan). Minus is U+2212.
Never "NCERT", "textbook" or "page N" in anything a child reads.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# chapter identity (also in chapter.config.json: keep the two in sync by hand)
# ---------------------------------------------------------------------------
CHAPTER = {
    "grade": 4,                      # same as chapter.config.json "grade"
    "label": "Class 4",
    "chapter_no": 1,                 # same as chapter.config.json "chapter_no"
    "name": "Shapes Around Us",      # same as chapter.config.json "chapter_name"
    "book": "NCERT Maths Mela",      # Grade 4, First Edition March 2025, Reprint 2026-27; chapter = printed pages 1 to 23
    "source_pdf": "textbooks/class4/demm101.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

# ---------------------------------------------------------------------------
# modules: (module_id, module_name, summary), the top level of the hierarchy. Short; the child sees them.
# ---------------------------------------------------------------------------
MODULES = [
    # Four themes from analysis.md section 3 and the tool proposal, plus the review. Tools 1 to 9, 10 to 15, 16 to 19, 20 to 22.
    ("M1", "Solid Shapes",
     "Start with Diksha's blocks. Meet prisms and pyramids, count their parts, sort them, build with cubes and fold nets."),
    ("M2", "Angles and Rigid Shapes",
     "Find angles where two lines meet. Tell right, acute and obtuse angles apart. Push straw shapes to see which keep their shape."),
    ("M3", "Circles and Flat Shapes",
     "Make circles from straws and points. Fold circles to find the diameter. Sort flat shapes by their sides and angles."),
    ("M4", "Shape Puzzles",
     "Find hidden shapes, count shapes in spider webs and make triangles from matchsticks."),
    ("MLAST", "Chapter Review",
     "Look back at solids, angles, circles and puzzles. Nothing new comes in here."),
]

# ---------------------------------------------------------------------------
# the chapter's story: ONE thread that the hook starts and every concept video continues. Characters, setting and
# objects are the BOOK's own (same people, same colours). A video's story brief may only use these characters.
# ---------------------------------------------------------------------------
STORY = {
    "thread": "Diksha visits Delhi with her father, sees its old and new monuments and tries to build a model of India "
              "Gate from her wooden blocks; the children and the spiders Squiggly and Wiggly then meet solid shapes, "
              "nets, angles, circles and shape puzzles.",
    "setting": "a floor mat where Diksha builds with wooden blocks after her summer trip to Delhi (India Gate, Qutub "
               "Minar and other monuments); a classroom and craft table with straws, clay, paper, matchsticks and a "
               "compass; two spider webs",
    # Only these are named or described as people or creatures in the book. Unnamed children in pictures (a boy with a
    # stepped Qutub Minar model, a girl making a straw triangle, a girl with a red bow) are not listed: the book gives
    # them no names. Diksha's father is "Her father" in the book (not named, not drawn).
    "characters": [
        "Diksha",
        "Diksha's father",
        "Isha",
        "Nitesh",
        "Squiggly",
        "Wiggly",
    ],
}

# ---------------------------------------------------------------------------
# VISUAL_KEY: how each recurring shape or object is drawn, so it looks the same in every tool and image of the chapter.
# Tool specs and image briefs name these keys in `visuals`. Example: "ten_rod": "a tall blue bar, 10 squares".
# ---------------------------------------------------------------------------
#
# These describe how the BOOK draws each recurring object, so one shape looks the same everywhere. The book is not
# consistent about one colour per solid (the prisms are blue and the pyramids pink on one spread, but the same solids
# are other colours elsewhere), so the colours below are the book's colour for that figure (one colour per solid for the
# whole chapter is CLASH 27, not decided). Standing user rule for this pipeline: a sphere is always a proper shaded 3D
# ball, never a flat disc; every solid is a shaded 3D solid, and every straw, clay ball, cube and dot can be counted.
# Media step (step 4): keys added for the real-life images (everyday_objects, toy_cube_tower, folding_gate,
# round_rug_and_wheel), for things the tools' questions use that had no key (compass, ruler_and_thread, classroom_scene,
# angle_pictures, angle_letters, right_angle_figures, shape_gallery) and for people the videos need (isha, dikshas_father,
# delhi_monuments). tools_1.py is locked, so the brief writer wires these into each tool's `visuals` list at the briefs
# stage (the list is in media_decisions.md).
VISUAL_KEY = {
    "wooden_blocks": "light brown wooden blocks: cuboids of different sizes, a cylinder, a cube and two half-round blocks, lying on a floor mat in front of a drawing of India Gate",
    "india_gate_drawing": "a drawing of the India Gate arch in sandy brown on a white sheet that stands up behind Diksha",
    "other_buildings": "two small buildings drawn beside the first task: a sandy-brown gateway with tall minarets and arches, and a round hut with a thatched straw-coloured roof and pale walls (the book does not name them)",
    "street_model": "a small model street on a green base: a grey road, small houses with red, orange and blue roofs, two round brown huts, a lamp post",
    "qutub_minar": "a tall tapering reddish-brown tower with balconies that narrow towards the top, shown with a few bushes at its foot",
    "qutub_model": "a small stepped stack of three green boxes, each smaller than the one below (the book shows a boy holding it; in the image it stands on a table, with no child)",
    "bricks": "three solid blocks side by side: a red-brown clay brick, a grey stone block and a brown wooden block, all true cuboids with flat faces and square corners, shown from one angle so three faces of each can be seen",
    "diksha": "a girl with a ponytail, a yellow top and a pink skirt (as the book draws her)",
    "nitesh": "a boy with dark hair and a light blue t-shirt, cutting a net out of paper with orange scissors",
    "squiggly_and_wiggly": "two black fuzzy spiders with large round eyes and a thin hanging thread; Squiggly makes the triangular web, her brother Wiggly the web of rectangles",
    "box_net": "a pink paper box opened out flat with dotted fold lines, which folds back into the box",
    "paper_strip_ball": "a ball made of curved orange paper strips joined at the top and bottom, with a small green leaf on top",
    "prisms": "solid shapes drawn in blue with dashed hidden edges: a triangular prism, a square prism and a hexagonal prism",
    "pyramids": "solid shapes drawn in magenta pink with dashed hidden edges: a triangular pyramid, a square pyramid and a pentagonal pyramid",
    "straws_and_clay": "thin straws in green, yellow, blue or orange joined at their ends by small round clay balls to make a skeleton of a shape (red or pink balls on the triangle and the rectangle, grey-pink balls on the pentagon, orange balls on a blue-straw pyramid); every straw is its own straight line and every ball its own dot, drawn see-through so no edge hides another and all can be counted: straws are the edges and balls the corners (cube and cuboid 12 and 8, triangular pyramid 6 and 4, square pyramid 8 and 5, triangular prism 9 and 6)",
    "die": "a standard grey-white die with dots in the usual patterns; opposite faces always add up to 7 (1 and 6, 2 and 5, 3 and 4), so two faces that add up to 7 are never in view together; the book's picture shows 5 on top, 1 in front and 3 on the right (it writes numerals, the plan draws the same faces with dots, the same on the image and on the tool: CLASH 21)",
    "colour_cube": "one cube with six differently coloured faces (red, orange, green, purple, dark blue, yellow), shown in three views side by side; the three views are drawn as in the book and must all fit one single cube with one colouring",
    "border_objects": "about twenty pencil sketches of everyday objects around a page: dice, erasers, balls and a football, cans and bottles, an ice-cream cone, a party hat, cheese wedges, a Rubik's cube, a gift box, a wooden wedge, a cake slice; in the plan each is drawn as the solid it really is: the ice-cream cone is a plain cone with no scoop, every ball is a shaded ball, a can is a cylinder, a cheese wedge or cake slice is a triangular prism",
    "sorting_circles": "round outlines in dark purple-blue on a pale green panel with green italic labels; one panel has two separate circles, another has two circles that overlap",
    "cube_models": "four models of unit cubes: A red, B purple, C yellow, D with a blue base and teal, pink and green layers above it; every unit cube drawn with its own edges so the cubes can be counted",
    "cube_towers": "two stacks of unit cubes: a stepped tower with red, pink, green and blue layers, and a large green and cyan X-shaped tower; the plan draws every cube with clear edges so layers can be counted (the printed X tower cannot be counted reliably: CLASH 18)",
    "triangular_dot_paper": "grey dots in a slanting triangular grid (evenly spaced rows, each row shifted half a step, so any three neighbouring dots make an equal triangle) with one finished cube outline in dark purple and two cubes drawn only in dotted lines that run exactly through dots",
    "sphere": "a proper shaded 3D ball with a soft highlight, round from every side (the book draws a beige one and a red one this way); never a flat disc",
    "solid_pictures": "shaded 3D pictures, each a true solid: a beige sphere, a green square pyramid, a purple cone, a red cuboid, a pink-purple cylinder, a teal cube and a small orange triangular prism lying on a rectangle face with its two triangle ends clear (the book's small orange solid, read as a triangular prism: E5); and a red sphere, a yellow cone, a blue triangular pyramid, a green cube and a purple cuboid; every sphere is a shaded ball, a cone has one round flat base and one point, a cylinder has two round flat faces and a curved side",
    "nets_and_solids": "line drawings of nets with dotted fold lines (violet in one question, dark green in another) with a coloured solid beside or below each; the pieces of Nitesh's net are pale orange (one pentagon and five triangles); every face of a net is its own flat shape joined to the next along a dotted fold line, so the faces can be counted; the nets of the book's question 4 are drawn as printed (A and C do not fold: CLASH 12)",
    "angle_mark": "a small red arc at the corner of an angle, or a small red square for a right angle",
    "straws_angle": "two straws, one green and one orange, meeting at one end to show an angle, with a red arc or red square at the corner",
    "yoga_figures": "five simple yoga figures with round heads in blue and orange, each with a red arc where two limbs meet",
    "house_and_boat": "a blue house with a darker blue roof and a boat with a brown hull and a cream sail on a thick brown mast, with red angle marks at the corners",
    "right_angle_checker": "a piece of pale orange paper folded twice so the folded corner is a right angle, marked with a red square",
    "dot_grid": "rows of black dots on a white page, or on a pale blue, yellow, peach or pink rounded panel",
    "stick_figures": "four simple stick people with round faces, whose arms and legs meet at angles",
    "rigid_shapes": "straw shapes joined by red or pink clay balls: a triangle, a rectangle, a square of four equal straws (both lean over when pushed) and a pentagon of five equal blue straws; each clay ball is a joint that lets the shape turn, so a push tilts a four-sided or five-sided shape but never a triangle",
    "four_sided_shapes": "three flat 4-sided shapes: a green shape with a slanted side, a pink slanting shape and an orange diamond",
    "equal_straws_circle": "many straws in different colours, all the same length, laid like spokes round a central clay ball so their ends make a circle; and the same straws with unequal lengths, whose ends do not make a circle",
    "circle_paper": "a round sheet of orange-brown paper with dashed fold lines through the middle (creases); a red circle for the radius and diameter picture",
    "compass_design": "a yellow circle, then overlapping dotted circles, then a six-petal flower made of overlapping circles coloured blue, green, red and yellow",
    "carpet_design": "a brown carpet with a fringe, a paisley border and an orange circle in the middle holding green and yellow petals around a small blue centre",
    "wheels": "four wheels labelled A to D: a grey car wheel with four oval holes, a large brown wooden spoked wheel, a bicycle wheel with blue spokes and a thin black tyre, and a small dark tyre with a silver rim; each seen straight on so it is a true circle with its centre showing, in the printed sizes (B the largest, then C, then A, and D the smallest: E16)",
    "hidden_shapes": "red outlines drawn over one another: a circle, a cylinder, one square, one tilted rectangle (about twice as long as wide) and two triangles (corrected by the question mapper, CLASH 31)",
    "dissection_shapes": "flat coloured shapes: an orange long hexagon, a green square and a pink triangle on the left, and the smaller pieces they are cut into on the right",
    "shape_cards": "six flat cut-out cards from the end of the book: an orange square, a green oval, a brown quarter circle, a light-green semicircle, a blue triangle and a pink circle",
    "spider_webs": "purple threads on white: Squiggly's web is a long shape with 12 walls numbered 1 to 12 in dark red and point A at the bottom; Wiggly's web is a set of rectangles with a short bar at the top, point A at its upper right end and point B at the bottom of the middle-left line",
    "matchsticks": "a thin wooden stick with a red-orange head at one end; all sticks the same length; shown singly, in three separate triangles, and in a group of small triangles, with every stick drawn whole so the sticks can be counted",
    "angle_shapes": "flat coloured 2D shapes: a blue square, a red triangle, a green slanting 4-sided shape, a purple right triangle, a purple pentagon, a thin green triangle and a red rectangle",
    # ---- added by the media step (step 4)
    "everyday_objects": "four to eight familiar objects, each a clean solid shape and none of them from the border sketches: for example a matchbox, a round tin, a marble and a toy tent, standing apart on a plain shelf in even light with nothing printed on them",
    "toy_cube_tower": "a small tower of identical plain toy cubes with no letters or pictures, stacked in layers on a table so the layers show; not the book's two towers; every cube the same size with clear edges",
    "folding_gate": "a steel folding gate across a doorway: slim straight steel strips of equal length crossing in a diamond lattice, pinned at every crossing and at the ends, shown half closed so every four-sided cell leans over",
    "round_rug_and_wheel": "a plain round woven rug and one bicycle wheel, each seen straight on so each is a true circle; not the book's carpet and not its wheels A to D",
    "compass": "a school compass: two arms joined at the top, a sharp metal point on one arm and a pencil on the other; the point stays fixed on the centre and the pencil draws the circle",
    "ruler_and_thread": "a plain school ruler with equal tick marks and no unit written on it, and a loose thread, used only to compare lengths",
    "classroom_scene": "a simple classroom: a desk and bench, a blackboard, a door, a window, a wall clock, and a book and a ruler on the desk; every corner drawn true so right, acute and obtuse angles can be found",
    "angle_pictures": "five plain pictures: an open pair of scissors, a clothes hanger, a hand making a V sign, a seesaw and a slide; in each the two arms that meet are drawn clearly",
    "angle_letters": "the capital letters V, A and Z in large plain strokes",
    "right_angle_figures": "six flat coloured figures in a row: a blue rectangle, a green slanted four-sided shape, a purple triangle, an orange four-sided shape wider at the top, a purple slanted diamond and a red tilted rectangle (a little longer than wide, as the book draws it: CLASH 31); every corner drawn true",
    "shape_gallery": "fourteen flat coloured shapes numbered 1 to 14 in three rows, mostly four-sided (squares, rectangles and slanted shapes) with one dart-shaped number 1; every corner drawn true so right, acute and obtuse angles can be told apart",
    "isha": "a girl of Diksha's age in simple clothes, drawn in the book's style; the book shows only her hands and straws, so the plan gives her one plain look and keeps it the same in every video",
    "dikshas_father": "Diksha's father: a grown man in simple clothes, drawn in the book's style; the book names him in words only, so the plan gives him one plain look and keeps it the same in every video",
    "delhi_monuments": "the real places named in the opener, drawn as they truly look with no invented building: India Gate, Qutub Minar, Safdarjung Tomb, Akshardham, the National Museum, Jantar Mantar and Sansad Bhawan",
}

# ---------------------------------------------------------------------------
# how this chapter is taught (shown once with the plan)
# ---------------------------------------------------------------------------
CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "TODO 2 to 4 short sentences: the arc (a story hook, then try it, then a story that names the idea, then "
             "a tool to apply it, then the book's questions on that tool, then a short review).",
    "points": [
        {"title": "TODO design decision", "text": "TODO what it is and why."},
    ],
}

# ---------------------------------------------------------------------------
# NCERT_ITEMS: every item of this chapter the plan must cover, as ("id", kind). Nothing from outside the chapter.
#   "example"   a solved example printed in the book      \
#   "exercise"  an exercise question                       }  NCERT questions: each sits on the tool of its concept
#   "prompt"    an answerable in-text question             /   (or on the concept itself when no tool follows)
#   "talk"      a discussion prompt (not a question)       \  stay in the teaching text
#   "text"      a fact, rule, figure or summary line       /
# Use the book's own section numbering as the id prefix, e.g. "2.1.example1", "end.Q4".
# ---------------------------------------------------------------------------
#
# 131 items, one per numbered question or per activity step-group (sub-parts a, b, c that share a stem stay together).
# 1 example + 59 exercise + 49 prompt = 109 NCERT questions; 5 talk; 17 text. The book prints no answers. The printed
# page number equals the pdf page number for every page of this chapter (the opener, page 1, carries no printed number).
NCERT_ITEMS = [
    # ---- printed page 1 (the chapter opener)
    ("opening", "text"),
    ("ch1.model1", "exercise"),
    ("ch1.model_q1", "prompt"),
    ("ch1.model_q2", "prompt"),
    ("ch1.model_q3", "prompt"),
    ("ch1.model_q4", "prompt"),
    ("ch1.model_q5", "prompt"),
    ("ch1.model_talk", "talk"),
    # ---- printed page 2
    ("ch1.project1", "exercise"),
    ("ch1.qutub_say", "text"),
    ("ch1.qutub_q1", "prompt"),
    ("ch1.qutub_q2", "prompt"),
    ("ch1.qutub_q3", "prompt"),
    ("ch1.qutub_fact", "text"),
    ("ch1.bricks_text", "text"),
    ("ch1.bricks_q", "prompt"),
    ("ch1.note_boxes", "text"),
    # ---- printed page 3
    ("ch1.craft1", "exercise"),
    ("ch1.net_text", "text"),
    ("ch1.craft2", "exercise"),
    ("ch1.prism_q1", "prompt"),
    ("ch1.prism_q2", "prompt"),
    ("ch1.prism_q3", "prompt"),
    ("ch1.pyr_q1", "prompt"),
    ("ch1.pyr_q2", "prompt"),
    ("ch1.pyr_q3", "prompt"),
    ("ch1.cube_prism", "prompt"),
    ("ch1.prism_pyr_talk", "talk"),
    # ---- printed page 4
    ("ch1.craft3", "exercise"),
    ("ch1.fve", "prompt"),
    ("ch1.sort_faces", "exercise"),
    ("ch1.three_faces", "prompt"),
    ("ch1.sort_edges", "exercise"),
    # ---- printed page 5
    ("ch1.observe1", "prompt"),
    ("ch1.observe2", "prompt"),
    ("ch1.observe3", "prompt"),
    ("ch1.border1", "exercise"),
    ("ch1.border2", "exercise"),
    ("ch1.border3", "exercise"),
    ("ch1.border4", "exercise"),
    ("ch1.border5", "exercise"),
    # ---- printed page 6
    ("ch1.sort1", "exercise"),
    ("ch1.sort2", "exercise"),
    ("ch1.sort3", "exercise"),
    # ---- printed page 7
    ("ch1.sort3_q", "prompt"),
    ("ch1.sort4", "exercise"),
    ("ch1.note_venn", "text"),
    ("ch1.build1", "exercise"),
    ("ch1.towers", "prompt"),
    # ---- printed page 8
    ("ch1.dotcubes", "exercise"),
    ("ch1.solids_q1", "exercise"),
    ("ch1.solids_q2", "talk"),
    # ---- printed page 9
    ("ch1.solids_q3", "exercise"),
    ("ch1.solids_q4", "exercise"),
    ("ch1.solids_q5", "exercise"),
    # ---- printed page 10
    ("ch1.angle_text", "text"),
    ("ch1.yoga_text", "text"),
    ("ch1.house_ex", "example"),
    ("ch1.boat_q", "prompt"),
    ("ch1.angles_do1", "exercise"),
    # ---- printed page 11
    ("ch1.angles_do2", "prompt"),
    ("ch1.right_make", "exercise"),
    ("ch1.right_circle", "exercise"),
    ("ch1.right_objects", "exercise"),
    # ---- printed page 12
    ("ch1.right_do1", "exercise"),
    ("ch1.acute_text", "text"),
    ("ch1.acute_obj", "prompt"),
    ("ch1.obtuse_obj", "prompt"),
    ("ch1.letters", "exercise"),
    # ---- printed page 13
    ("ch1.ao_do1a", "exercise"),
    ("ch1.ao_do1b", "exercise"),
    ("ch1.ao_do2", "exercise"),
    # ---- printed page 14
    ("ch1.straw_tri_make", "exercise"),
    ("ch1.straw_tri_push", "prompt"),
    ("ch1.straw_tri_trace", "exercise"),
    ("ch1.straw_tri_angles", "prompt"),
    ("ch1.straw_rect_make", "exercise"),
    ("ch1.straw_rect_angles", "prompt"),
    ("ch1.straw_rect_push", "prompt"),
    ("ch1.straw_rect_after", "prompt"),
    ("ch1.straw_square", "prompt"),
    ("ch1.straw_compare", "prompt"),
    ("ch1.note_rigid", "text"),
    # ---- printed page 15
    ("ch1.dotshapes", "exercise"),
    ("ch1.dotshapes_q", "prompt"),
    ("ch1.fourside_q", "prompt"),
    ("ch1.note_square", "text"),
    # ---- printed page 16
    ("ch1.pentagon_make", "exercise"),
    ("ch1.pentagon_q1", "prompt"),
    ("ch1.pentagon_q2", "prompt"),
    ("ch1.pentagon_q3", "prompt"),
    ("ch1.circle_straws", "exercise"),
    ("ch1.circle_straws_q1", "prompt"),
    ("ch1.circle_straws_q2", "prompt"),
    ("ch1.make_circle", "exercise"),
    ("ch1.make_circle_q", "prompt"),
    ("ch1.centre_text", "text"),
    # ---- printed page 17
    ("ch1.amazing1", "exercise"),
    ("ch1.amazing_q1", "prompt"),
    ("ch1.amazing_t2", "text"),
    ("ch1.amazing_t3", "talk"),
    ("ch1.amazing_q4", "exercise"),
    ("ch1.amazing_t5", "talk"),
    ("ch1.note_measure", "text"),
    # ---- printed page 18
    ("ch1.circ_do1", "exercise"),
    ("ch1.compass", "exercise"),
    ("ch1.carpet", "exercise"),
    ("ch1.note_compass", "text"),
    # ---- printed page 19
    ("ch1.wheels_q0", "prompt"),
    ("ch1.wheels_q1", "prompt"),
    ("ch1.puzzle1", "exercise"),
    ("ch1.puzzle2", "exercise"),
    ("ch1.puzzle3", "exercise"),
    # ---- printed page 20
    ("ch1.puzzle4", "exercise"),
    ("ch1.cards", "exercise"),
    # ---- printed page 21
    ("ch1.try1_text", "text"),
    ("ch1.try1a", "prompt"),
    ("ch1.try1b", "exercise"),
    ("ch1.try1c", "prompt"),
    ("ch1.try1d", "exercise"),
    ("ch1.try2", "exercise"),
    # ---- printed page 22
    ("ch1.try3", "exercise"),
    ("ch1.try4", "exercise"),
    ("ch1.try5", "exercise"),
    ("ch1.try6", "exercise"),
    ("ch1.try6_q", "prompt"),
    # ---- printed page 23
    ("ch1.try7a", "exercise"),
    ("ch1.try7b", "exercise"),
    ("ch1.try8", "exercise"),
    ("ch1.try8_q", "prompt"),
    ("ch1.try9", "exercise"),
]

# ---------------------------------------------------------------------------
# misconceptions this chapter targets: (id, one-sentence description of the wrong idea).
# ---------------------------------------------------------------------------
MISCONCEPTIONS = [
    ("M_SH_1", "A cube is not a prism, because a prism must be a long shape with a triangle or a rectangle at its ends."),
    ("M_SH_2", "Any solid with a triangular face is a pyramid, so a triangular prism is a pyramid."),
    ("M_SH_3", "A face is only a flat side, so a cone, a cylinder or a sphere has no face at all."),
    ("M_SH_4", "A corner and an edge are the same thing, or a curved line cannot be an edge."),
    ("M_SH_5", "The face opposite a face is any face next to it, so opposite faces and faces that touch are mixed up."),
    ("M_SH_6", "The number of cubes in a tower is the number of cubes you can see, so hidden cubes do not count."),
    ("M_SH_7", "Any flat pattern of faces is a net, so any six joined squares will fold into a box."),
    ("M_AN_1", "An angle is only a corner of a drawn shape, so scissors, a seesaw or a yoga pose has no angle."),
    ("M_AN_2", "A bigger angle is one with longer arms, so making the lines longer makes the angle larger."),
    ("M_AN_3", "A right angle must look like an upright L, so a tilted corner, such as a turned square, is not a right angle."),
    ("M_AN_4", "An obtuse angle is any angle that looks big and an acute angle is any that looks small, with no check against a right angle."),
    ("M_AN_5", "A rectangle keeps its shape and its right angles when it is pushed, just as a triangle does."),
    ("M_AN_6", "A square is not a rectangle, because the two look different."),
    ("M_AN_7", "The number of angles of a shape can be different from its number of sides."),
    ("M_CI_1", "A round-looking drawing is a circle even when its points are at different distances from the centre."),
    ("M_CI_2", "Any line across a circle is a diameter, even one that does not pass through the centre."),
    ("M_CI_3", "The radius and the diameter of a circle are the same length, or the diameter is half the radius."),
    ("M_CI_4", "The wheel with the longest radius need not be the wheel with the longest diameter."),
    ("M_PU_1", "Only the small triangles count when you count the triangles in a web, and a triangle made of several pieces does not count."),
    ("M_PU_2", "A walk over every wall of a web without using a wall twice can always be found if you keep trying."),
    ("M_PU_3", "Two triangles always need six matchsticks, so two triangles cannot be made with five."),
]

# ---------------------------------------------------------------------------
# CLASHES: judgement calls and conflicts the user must decide, one string each (shown in the structure report):
# a tool with no matching concept, a concept with no NCERT question, an approved tool the book does not support,
# a teacher instruction against a hard rule. Empty means none. Never settle one silently.
# ---------------------------------------------------------------------------
CLASHES = [
    (
        "CLASH 1: The 22 tools are the pipeline's PROPOSAL, not the content team's table.\n"
        "  NOTE SAYS: No content-team table exists for this chapter. The brief says \"If no approved tool sequence exists, propose one based on the textbook's natural learning progression\", and the user chose \"propose fresh from the book\". So the 22 tools below (names, purposes, order) were proposed by the pipeline (tool_proposal.md), locked unchanged from tool_map.md, and mapped to concepts and objectives. The pipeline's rule is that approved tools are the content team's, so the user must approve this table at this stop.\n"
        "  THE 22 TOOLS (number, name, purpose; names are 2 to 5 plain words, and the proposal checked them against the 13 tool names of the older live plan: none repeats):\n"
        "      1. Blocks for Buildings: The child picks wooden blocks for the roof, pillars and base of the buildings in the opening picture, builds the model and finds how it is like and unlike the real building.\n"
        "      2. Prism or Pyramid: The child taps the faces of prisms and pyramids to find the rectangle faces all prisms share and the triangle faces that meet at one point in every pyramid, and decides if a cube is also a prism.\n"
        "      3. Faces, Corners and Edges: The child counts the faces, corners and edges of straw and clay solids, fills the F, V and E table, works out F+V−E and sorts the solids by flat faces and straight edges.\n"
        "      4. Opposite Faces: The child turns a die and a coloured cube to find the face opposite a face and the faces that share an edge with it.\n"
        "      5. Spot the Faces: The child marks everyday objects by their faces and corners: rectangular face, triangular face, curved face, no corner and the same opposite faces.\n"
        "      6. Sort the Solids: The child drags solids into two circles by a rule, such as curved or straight edges, and into overlapping circles to find the solids that belong to both sets.\n"
        "      7. Build and Draw Cubes: The child copies cube models from unit cubes, counts the cubes in a tower layer by layer including the hidden ones, and completes cube drawings on triangular dot paper.\n"
        "      8. Solid Riddles: The child reads clues about faces, corners and edges, and about straws and clay balls, and picks or builds the solid that fits each clue.\n"
        "      9. Fold the Net: The child folds nets into solids, matches nets to solids, tests which nets fold into a given solid and finds the solid whose net has the given pieces.\n"
        "      10. When Lines Meet: The child makes an angle by meeting two straws at a point, then marks and counts the angles in pictures and in a classroom scene.\n"
        "      11. Right Angle Checker: The child folds paper into a right angle checker, uses it to test corners of shapes and objects, and draws right angles on a dot grid.\n"
        "      12. Acute or Obtuse: The child swings a line against a right angle to see if an angle is acute or obtuse, draws both kinds on a dot grid and colours angles red, green and blue.\n"
        "      13. Push the Straw Shapes: The child builds a triangle and a rectangle from straws and clay, pushes one side and sees that the triangle keeps its shape while the rectangle does not.\n"
        "      14. Angles After the Push: The child pushes a rectangle, a square and a pentagon and reads how the angles change: the right angles of the rectangle and square become acute and obtuse.\n"
        "      15. Angles in Shapes: The child draws three- and four-sided shapes on a dot grid, counts their right angles, compares rectangle and square with other four-sided shapes and finds a shape from its kinds of angles.\n"
        "      16. Make a Circle: The child places equal straws around a centre and marks points at an equal distance from a point A to see that every point of a circle is the same distance from its centre.\n"
        "      17. Fold the Circle: The child folds a circle in half in different ways, sees that the creases are equal and meet at the centre, and finds that the diameter is double the radius.\n"
        "      18. Find Radius and Diameter: The child draws a compass flower, marks the centre, radius and diameter on a carpet design and compares four wheels by radius and diameter.\n"
        "      19. Sides and Angles: The child sorts flat shape cards by their sides and shapes by their number of angles, sees that the two counts match and draws shapes with fewer and more than five angles.\n"
        "      20. Divide the Shapes: The child spots hidden shapes and draws lines to divide a triangle, a square and other shapes into smaller shapes.\n"
        "      21. Spider Web Puzzles: The child counts the triangles and rectangles in the two webs and traces walks that use no wall twice to find which walks are possible.\n"
        "      22. Matchstick Moves: The child makes, moves and removes matchsticks to form 2, 4 and 3 triangles.\n"
        "  OPTIONS: (a) approve the table as proposed; (b) change names, purposes or order (say which: the table is rewritten and locked again, and the concepts, objectives and every later step are redone for the change); (c) send the content team's table, which replaces this one.\n"
        "  RECOMMENDATION: (a) approve. Each purpose is one action on one idea of the book, the book supports each tool (analysis.md section 8), and no tool repeats another (tool_proposal.md section 4). The size of the table is CLASH 2."
    ),
    (
        "CLASH 2: The chapter is large: 22 tools, 16 concept videos, 6 images, 4 modules, 46 rows.\n"
        "  NOTE SAYS: The brief says \"Do not use a fixed number of videos or tools\" and \"Avoid creating unnecessary tools simply to increase the tool count\". The flow rules say to repeat video and tool \"only where it adds value\".\n"
        "  BOOK SAYS: 24 concepts, 20 activity boxes and 109 questions on 23 pages. At 6 questions a tool, 109 questions need at least 19 tools even if every question sat on a tool (109 / 6 = 18.2).\n"
        "  THE PLAN: 1 hook, 22 tools, 16 concept videos (4 of them puzzle stories), 6 images (5 before a tool, 1 with no tool) and 1 review = 46 rows. Modules: M1 solid shapes (Tools 1 to 9), M2 angles and rigid shapes (10 to 15), M3 circles and flat shapes (16 to 19), M4 shape puzzles (20 to 22), then the review. Every tool after Tool 1 needs a concept video or an image before it, so 21 media items come before tools. Four tools are small by nature (Tool 4: 3 questions, Tool 7: 3, Tool 8: 2, Tool 22: 3). 103 questions sit on tools (about 4.7 each) and 6 on an image.\n"
        "  OPTIONS: (a) keep 22 tools; (b) a leaner plan of 21 tools: Tool 18 becomes an image of the carpet and the wheels holding its 4 questions (the compass flower, the marking and the measuring are then not done on a tool; the table changes); (c) a leaner plan of 19 tools: also merge Tools 5 and 6 (needs a cap of 10) and Tools 13 and 14 (needs a cap of 14), each making a tool that does two things; (d) another cut: say which tools to drop (each drop changes the table and re-homes its questions).\n"
        "  RECOMMENDATION: (a). The chapter is long in the book itself, the tools follow its activities one for one and none repeats another. If the user wants fewer, (b) is the cheapest cut."
    ),
    (
        "CLASH 3: Tools 2, 13 and 14 hold 7 book questions each; the cap is 6.\n"
        "  NOTE SAYS: The question cap per tool is 6 (chapter.config.json \"max_tool_questions\": a config default, not a curriculum rule; only the user may raise it). The build gate fails a tool with more than 6 book questions.\n"
        "  BOOK SAYS: Tool 2 holds prism_q1, prism_q2, prism_q3, pyr_q1, pyr_q2, pyr_q3, cube_prism. Tool 13 holds straw_tri_make, straw_tri_push, straw_tri_trace, straw_tri_angles, straw_rect_make, straw_rect_angles, straw_rect_push. Tool 14 holds straw_rect_after, straw_square, straw_compare, pentagon_make, pentagon_q1, pentagon_q2, pentagon_q3. Tools 1, 12 and 15 sit exactly at 6; no other tool is over.\n"
        "  OPTIONS: (a) keep the cap at 6 and make 23 tools: cube_prism moves to Tool 3 (6) and the push test becomes three tools (triangle: 4 questions; rectangle and square: 6; pentagon: 4). This ADDS a tool, so the table changes, and the third push tool repeats the first two only to fit the cap. (b) raise the cap to 7 for this chapter only (needs the user's say-so; one number in chapter.config.json; 22 tools; nothing else changes). (c) keep the cap at 6 and call two items teaching text instead of questions: straw_tri_trace (a notebook task) and straw_compare (an open discussion) become talk items, and cube_prism moves to Tool 3; 22 tools, but those two items then have no answer on a tool, cube_prism sits on a tool about counting parts (it is in Tool 2's purpose: \"decides if a cube is also a prism\"), and the analyst and the user must change the item kinds.\n"
        "  RECOMMENDATION: (b). Until the user decides, the build gate will report 3 errors (Tools 2, 13 and 14: 7 against 6). The tool mapper has not edited the config or the gate."
        "\n  QUESTION MAPPER (step 5): the cap stays at 6 and the structure stage is clean. To get there the single item whose move does least harm left each of Tools 2, 13 and 14, provisionally: cube_prism to Tool 3, straw_rect_angles to Tool 11, straw_compare to Tool 19. The details and the way back are in CLASH 30. Option (b) here (cap 7) puts all three back with three small edits."
    ),
    (
        "CLASH 4: Seven tools carry two of the analyst's concepts; five concepts are split over two places.\n"
        "  NOTE SAYS: Flow rule 3: \"A tool focuses on the concept assigned to it.\" The mapper rule is one concept per tool, or the pair the book itself puts side by side.\n"
        "  BOOK SAYS: analysis.md has 24 concepts for 22 tools. Pairs on one tool: Tool 7 (C6 build and count cubes + C7 cube on triangular dots), Tool 8 (C8 name a solid from its description + C23 model challenge), Tool 9 (C9 nets + the net text and Craft 2 of C2), Tool 14 (second half of C13 + C15 pentagon), Tool 15 (C14 + the second half of C24), Tool 17 (C17 + the \"double\" step of C18, circ_do1) and Tool 19 (C20 + the first half of C24). Concepts split over two places: C1 (Tool 1 and the image), C5 (Tools 5 and 6), C13 (Tools 13 and 14), C18 (Tools 17 and 18), C24 (Tools 15 and 19). Each pairing is written in the tool's own flow row, so the approved purpose already says it.\n"
        "  OPTIONS: (a) accept: in the plan each tool is one topic concept with one objective, and each pair is two ways to practise one idea; (b) give a paired part its own tool (adds up to 7 tools and changes the table); (c) leave the paired parts out (drops book questions, which the brief does not allow).\n"
        "  RECOMMENDATION: (a). The locked map names, for each tool, the concept it serves and the part of a neighbouring concept it takes."
    ),
    (
        "CLASH 5: Nets are taught at Tool 9, not next to the prisms and pyramids where the book first shows a net.\n"
        "  NOTE SAYS: Tool 9 (Fold the Net) is the ninth tool, after the solids module's cube and riddle tools.\n"
        "  BOOK SAYS: Page 3, under the prisms and pyramids, shows Diksha opening a box flat (\"This is called the net of the box\") and Craft 2 asks the child to use the nets at the end of the book to make the six prisms and pyramids. The three net questions (match nets to solids, which nets fold, Nitesh's pieces) are on page 9.\n"
        "  THE PLAN: net_text and craft2 of page 3 move to Tool 9, so the net word, Craft 2 and the three page-9 questions are one unit. The book's objective \"explain what a net is\" (analysis.md section 2, item 2) is therefore met at Tool 9, six tools after the prisms and pyramids.\n"
        "  OPTIONS: (a) as proposed (nets at Tool 9); (b) nets right after prisms and pyramids, the book's page-3 order: Tool 9 would move to position 3, which reorders the approved tools; (c) keep Tool 9 where it is and add one pinned image of the opened box beside Tool 2 so the word comes at page 3 (one more image; the C9 video then continues from it).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 6: The tool order differs from the book's printed order in six places.\n"
        "  NOTE SAYS: The brief says \"Follow the sequence and mathematical methods of the textbook\" and \"Do not introduce concepts assigned to later tools prematurely\"; the flow rules say to keep the approved tool sequence.\n"
        "  BOOK SAYS: The concepts run C1 to C24 in page order. The tools differ from it here (all moves are in tool_proposal.md section 8): (1) try5 (C23, page 22) is on Tool 8, at the page-8 position. (2) try8, try8_q and try9 (C24, page 23) are on Tool 15, at the page-15 position; cards (C20, page 20) and try6, try6_q, try7a, try7b (C24, pages 22 to 23) are on Tool 19, after the circles and before the puzzles of pages 19 to 22. (3) C15, the pentagon (page 16), is taught on Tool 14, before C14 (page 15) on Tool 15. (4) C20, the card game (page 20), comes before C19, Puzzling Shapes (pages 19 to 20, Tool 20). (5) circ_do1 (page 18, C18) is on Tool 17 with the folds of page 17, and wheels_q0 and wheels_q1 (page 19) join Tool 18 (page 18). (6) craft1 (page 3) and project1 (page 2) sit on the C1 image, and net_text and craft2 (page 3) on Tool 9 (CLASH 5).\n"
        "  CHECK: No tool uses an idea that a later tool teaches (the words acute and obtuse come before Tools 14, 15 and 19; prisms, pyramids, corners and edges before Tool 8; the right angle before Tools 15 and 19; the radius before Tool 18).\n"
        "  OPTIONS: (a) accept the moves; (b) restore the printed order for C23 and C24: Tool 8 would hold 1 question and Tool 15 would lose 3, and Tool 19 would have to move to the end of the chapter, which reorders the approved tools; (c) restore only C19 before C20: Tools 19 and 20 swap places, which also reorders the tools.\n"
        "  RECOMMENDATION: (a). Each move puts a question beside the tool whose action answers it."
    ),
    (
        "CLASH 7: Five tools follow an image, not a concept video.\n"
        "  NOTE SAYS: Flow rules 3 and 4: \"Concept video\" then \"Concept tool\", the matching tool after the concept video. The gate (gates/flow_c34.py) accepts a concept video or an image right before a tool, and CLAUDE.md says \"A small concept may be one image\".\n"
        "  BOOK SAYS / THE PLAN: Tool 1 follows the hook video. Sixteen tools follow a concept video (Tools 2, 3, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22). Five follow a real-life image: Tool 4 (a die), Tool 5 (everyday objects), Tool 7 (a tower of toy cubes), Tool 14 (a folding gate) and Tool 18 (a carpet and wheels). Each is a small idea next to a neighbour whose video would only repeat it (flow rule 2: do not duplicate content; an image only when it adds a real-life example). Flow rule 2 also says an image is for the case \"when no video / tool is needed\", and here a tool does follow: the doc and the gate do not fully agree.\n"
        "  OPTIONS: (a) keep the five images; (b) make each of the five a short story video (21 concept videos, 5 more, a longer chapter); (c) mix: say which of the five become videos (Tools 7 and 14 are the biggest ideas).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 8: The image after Tool 1 holds six look-and-think or offline book items.\n"
        "  NOTE SAYS: After Tool 1 comes one image (a real picture of the Qutub Minar beside a clay brick, a stone block and a wooden block) with no video and no tool, because the second half of C1 repeats the placing of solids that Tool 1 has just done (flow rule 2: use one image when a small concept needs no video or tool).\n"
        "  BOOK SAYS: Six items are homed on it: qutub_q1, qutub_q2, qutub_q3 and bricks_q (look-and-think prompts of page 2), project1 (Project Work: make a model of a street, offline) and craft1 (page 3, Craft 1: make a sphere-like shape with paper strips, offline and not about towers or bricks; it is C2 in analysis.md, moved here so Tool 2 stays lower).\n"
        "  GATE CHECK (gates/flow_c34.py): this is allowed. The gate rejects book questions on an image or video concept only when a tool follows and applies to that concept (the questions then belong on the tool), and on the hook and the review. No tool applies to this image, and the cap of 6 is checked on tools only, so six items on the image pass. Not checked by any gate: build.py turns concept items into worked-example blocks (the question, short working and the answer, which the plan labels \"From the picture\" or \"Sample answer\"), so, as built, the child reads them and no answer box is made; whether the platform would show one is not verified.\n"
        "  OPTIONS: (a) as proposed; (b) project1 on Tool 1 (Tool 1 would hold 7, needs cap 7); (c) craft1 on Tool 9 (both are paper crafts; Tool 9 would hold 5); (d) both (b) and (c) (the image keeps the four look-and-think prompts); (e) a tool for the tower with qutub_q1 to qutub_q3 and bricks_q (23 tools, changes the table).\n"
        "  RECOMMENDATION: (a) for now. craft1 is the weakest fit (a sphere craft on a bricks picture); (c) is its nearest home."
        "\n  QUESTION MAPPER (step 5): homed as recommended, option (a). The six items are FIO items in `items` of the image concept T2.C1. The gate allows it because no tool applies to T2.C1 (flow_c34 _check_questions bars book questions on an image concept only when a tool follows and applies to it, and the cap of 6 is checked on tools only). Answers: qutub_q1 to qutub_q3, project1 and craft1 are Sample answers, bricks_q is From the picture. project1 is worded for the child (CLASH 13, CLASH 32). qutub_q3 uses the book's own 5 storeys (the Do you know bubble, a teaching text on this concept); the image itself shows no number (CLASH 29)."
    ),
    (
        "CLASH 9: Tool 1, the exploration tool, carries six book questions.\n"
        "  NOTE SAYS: Tool 1 follows the hook video and the child tries blocks before any video names a solid. The gate allows up to 3 \"what do you notice\" prompts on it; its Phase 1 reconnects with the hook (Diksha's blocks), not a concept.\n"
        "  BOOK SAYS: Page 1 asks six things about the child's model: model1 (make a model of the buildings with blocks) and model_q1 to model_q5 (which parts, why, what shapes, how it is similar, how it is different). That is exactly the cap, and the 3 notice prompts come on top, so this exploration tool is heavier than most. model_q3 (\"What shapes will model these parts well?\") is asked before any video has named a solid, so the child answers in everyday words.\n"
        "  OPTIONS: (a) keep the six on Tool 1; (b) keep model1 and the notice prompts on Tool 1 and put model_q1 to model_q5 on the C1 image (it would hold 11; they are about \"your model\", so they fit poorly there).\n"
        "  RECOMMENDATION: (a)."
        "\n  QUESTION MAPPER (step 5): option (a) kept. model1 and model_q1 to model_q5 are the six FIO items of Tool 1 (T1.C2), exactly the cap; the 3 notice prompts of tools_1.py come on top. The sample answer of model_q3 uses everyday words (a long flat block, tall blocks) and names no solid. model_talk stays teaching text on T1.C2."
    ),
    (
        "CLASH 10: Tools 9 and 19 use pages from the end of the book, outside the chapter's 23 pages.\n"
        "  NOTE SAYS: The chapter file is printed pages 1 to 23. Nothing outside the chapter may be used.\n"
        "  BOOK SAYS: Craft 2 (page 3, Tool 9) says \"Use the nets given at the end of the book\" and the Card Game (page 20, Tool 19) says \"Sort the 2D-shape cards given at the end of the book\". The end pages (demm114.pdf) show nets of a triangular prism, a rectangular prism or cuboid, a triangular pyramid, a hexagonal prism, a square pyramid and a pentagonal pyramid, and six cards: an orange square, a green oval, a brown quarter circle, a light-green semicircle, a blue triangle and a pink circle. The net page has no \"Square Prism\" though Craft 2 shows one (E24), and the book does not say what the three groups of the card game are (E18).\n"
        "  OPTIONS: (a) use these pages as supporting material of this chapter (the book's own, and the two activities cannot be done without them); (b) use only the 23 pages and leave Craft 2 and the Card Game out (the brief says do not skip any activity).\n"
        "  RECOMMENDATION: (a), with the figures redrawn from the book's shapes."
        "\n  QUESTION MAPPER (step 5): craft2 (Tool 9) and cards (Tool 19) keep the book's own words ('given at the end of the book'); the first step of each says the nets or the six cards are on the screen. The answer of cards is one reading of the groups (E18): only straight sides, only curved sides, both."
    ),
    (
        "CLASH 11: The book prints no answers: who signs off the analyst's readings?\n"
        "  NOTE SAYS: The brief says \"Preserve exact NCERT questions\" and \"Never invent mathematical rules or textbook activities\". Every answer the plan makes is labelled \"From the picture\" or \"Sample answer\".\n"
        "  BOOK SAYS: There is no answer key. Every answer is the analyst's reading of a figure (analysis.md, Appendix A, rows marked \"mine\") or a sample answer. On tools: F+V-E is 2 for the five solids, and the sort columns do not fit every solid (E2, E3: Tool 3); the die opposites 5, 4, 3 depend on the die (E6) and the colour cube reading (Tool 4); \"rectangular pyramid\" is never named (E4: Tool 6); the boat has 10 marked angles (E8: Tool 10); the dot-grid angles (E9: Tool 11); how many angles to mark in V, A, Z and the stick figures (E10: Tool 12); the push test (E11: Tools 13 and 14); right-angle counts 4, 0, 1, 0, 0, 4 (E23: Tool 15); wheel B longest and D shortest (E16: Tool 18); the card groups (E18: Tool 19); the hidden shapes and the cuts (E17: Tool 20); the web answers 10, yes, 12, no (E19: Tool 21).\n"
        "  OPTIONS: (a) the user or the content team signs off Appendix A before the briefs stage; (b) the plan keeps each reading labelled \"From the picture\" or \"Sample answer\" with no sign-off; (c) an item whose answer cannot be confirmed is held back (see CLASH 18).\n"
        "  RECOMMENDATION: (a). The briefs and the question cards would otherwise rest on one reader's measuring of printed figures."
        "\n  QUESTION MAPPER (step 5): every answer begins exactly 'From the picture' (counts, positions, what a picture shows) or 'Sample answer' (open tasks and geometry the book does not print); open tasks end 'Your answer may differ'; none reads as an official textbook answer. Three items give NO number and NO solution because the analyst could not confirm one: ch1.try3, ch1.try4 and the second tower of ch1.towers; each answer says how to find it. Re-checked on the page images by the question mapper: F+V−E is 2 for the five solids, the boat has 10 marked angles and the house 7, the first cube tower has layers of 16, 9, 4 and 1 (30), the colour-cube opposites (red and purple, yellow and orange), the right-angle counts 4, 0, 1, 0, 0, 4, the shapes of Q9, 10 triangles and 12 rectangles in the webs, and a path through all 12 numbered walls of Squiggly's web. The gate checks every sum on the screen (none false). Two readings of analysis.md were corrected (CLASH 31) and two questions have two readings (CLASH 33). Each printed-book difference is in content.SOLUTION_NOTES; content.ERRATA stays empty (the book prints no false sum)."
    ),
    (
        "CLASH 12: Six printed-book errors or ambiguities reach a tool (E1, E5, E7, E9, E21, E22).\n"
        "  NOTE SAYS: The brief says \"Preserve exact NCERT questions, diagrams, values and conditions\" and the user said to keep the book as printed.\n"
        "  BOOK SAYS: E1 (Tool 9, page 9 Q4): net A has both flaps on the same side and net C has the rectangle and only 2 of the 4 triangles its pyramid needs, so neither folds into the solid below it; B and D fold; no key is printed. E5 (Tool 8, page 8 Q1 f): \"6 faces, 12 edges, 8 corners\" fits both the cube and the cuboid. E7 (Tool 5, page 5 border 5): \"Circle the shapes that have the same opposite faces\" is unclear and the sketches are not numbered. E9 (Tool 11, page 11 dot grid): no key; the right angles are read by measuring the figure. E21 (Tool 8, page 22 Q5 c): 15 straws and 10 clay balls is a pentagonal prism, a solid the chapter never shows. E22 (Tool 15, page 23 Q9): several shapes fit each clue (2 right, 1 acute, 1 obtuse: shapes 2 and 7; 2 obtuse and 2 acute: six shapes; 4 right angles: four shapes), and shape 1 is a dart with an angle larger than a straight line, a kind of angle the chapter never names.\n"
        "  OPTIONS: (a) keep each figure and wording as printed, and let the tool test the child's answer against the figure (the fold test for E1, either solid for E5, every shape that fits for E22, the checker for E9), with no new term taught; for E21 part c the child builds a solid from the counts without being given the name pentagonal prism. (b) fix the figure for the child (redraw nets A and C; choose one answer for E5 and E22). (c) hold back the part (E21 part c, E7 border5).\n"
        "  RECOMMENDATION: (a) for E1, E5, E9, E21 and E22. For E7 the user's reading of \"same opposite faces\" is needed (does it mean each pair of opposite faces looks alike?) before the briefs."
        "\n  QUESTION MAPPER (step 5): option (a) used for E1, E5, E9, E21 and E22. E1: solids_q4 answers 'B and D fold, A and C do not' and says to fold each net to check. E5: solids_q1 f) answers 'cube or cuboid, because both fit'. E9: right_circle lists the four angles read by measure and says to check each with the checker. E21: try5 c) is shown by its parts (two 5-sided ends, 15 straws, 10 balls) and is not named. E22: try9 lists every shape that fits each clue and says more than one fits; shape 1 is not mentioned. E7: border3 and border4 are answered; border1 and border2 name only the objects whose solid is certain, with 'for example' (the cheese pieces are drawn as pyramids in the book: CLASH 31); border5 is a Sample answer under one reading and still needs the user's reading of 'same opposite faces'."
    ),
    (
        "CLASH 13: Six Teacher's Notes and \"Ask your teacher to help you use a compass\" against the brief's rule.\n"
        "  BRIEF SAYS: \"Do not assign a teaching role to a classroom teacher.\"\n"
        "  BOOK SAYS: Six \"Note for Teachers\" boxes: page 2 note_boxes (collect boxes, bottles, cans), page 7 note_venn (use models, discuss opposite faces, make Venn diagrams), page 14 note_rigid (the triangle is the most rigid shape), page 15 note_square (a square is a special rectangle), page 17 note_measure (measure with a paper strip, thread or scale) and page 18 note_compass (help children draw circles with a compass). And the compass question the child reads (compass, Tool 18) says \"Ask your teacher to help you use a compass.\" Three notes carry a fact the plan needs (note_rigid for Tool 13, note_square for Tool 15, note_measure for Tool 17); the others only direct a teacher.\n"
        "  OPTIONS: (a) keep the facts as plain statements for the child with no teacher in them, drop the notes that only direct a teacher, and drop the one sentence \"Ask your teacher to help you use a compass\" from the compass question (the compass is on the screen, so no helper is needed); (b) keep the book's words exactly, including the teacher (breaks the brief's rule); (c) drop all six notes.\n"
        "  RECOMMENDATION: (a). It edits one book question by one sentence, so it needs the user's yes."
        "\n  QUESTION MAPPER (step 5): option (a) is followed, as recommended, so it needs the user's yes. (1) The compass question reads 'A circle can be made easily using a compass. Make the following design.' (the sentence 'Ask your teacher to help you use a compass.' is dropped; put it back to restore the printed words). (2) The same rule is applied to project1: 'Encourage learners to observe a street carefully and make a model showing the main buildings on the street.' reads 'Observe a street carefully and make a model showing the main buildings on the street.' It is a teacher line inside a question, not one of the six notes; put 'Encourage learners to' back to restore it. (3) The six notes stay `ncert` teaching text on their concepts (note_boxes, note_venn, note_rigid, note_square, note_measure, note_compass); no question, step or answer gives a teacher a role. See CLASH 32."
    ),
    (
        "CLASH 14: The brief's puzzle videos and revision with concept checks have no separate slot.\n"
        "  BRIEF SAYS: D, \"Puzzle / activity videos\", and E, \"Chapter revision\" with \"short concept checks and application questions\".\n"
        "  FLOW RULES SAY: only a hook video, concept videos, tools and a review. The gate says the review has no video, no tool and no book item of its own, and adds no new content. The book has no end exercise and no summary page.\n"
        "  THE PLAN: four concept videos are told as puzzle stories (Diksha's guessing game before Tool 8, her hidden shapes before Tool 20, Squiggly and Wiggly before Tool 21, Wiggly's matchsticks before Tool 22); the puzzle itself is solved on the tool. The review recaps solids, angles, circles and puzzles with only what was taught, and has no checked question.\n"
        "  OPTIONS: (a) as proposed; (b) a review with concept checks that re-ask questions already on tools (the gate and the rule \"each question once\" stop that); (c) a review with new questions written by the plan (breaks \"never invent textbook activities\" and the gate).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 15: Six real-life images are new to the book.\n"
        "  NOTE SAYS: Flow rule 2: images are clean real-life context that adds something. The user's principle: extra real-life examples are fine when they represent the concept correctly; a solid is drawn as a solid; a sphere is a shaded 3D ball; plan-made answers are labelled.\n"
        "  BOOK SAYS: The book has drawings of the Qutub Minar and bricks (page 2), a die (page 5), a border of pencil sketches (page 5), cube towers (page 7), a carpet (page 18) and wheels (page 19). It has no folding gate. The six images are: the Qutub Minar beside a brick, a stone block and a wooden block (after Tool 1); a die on a table (before Tool 4); everyday objects (a die, an eraser, a ball, a can, an ice-cream cone, a party hat, a cheese wedge, a gift box; before Tool 5); a tower of toy cubes (before Tool 7); a folding steel gate (before Tool 14); a carpet with a round design beside four wheels (before Tool 18).\n"
        "  CARE FOR THE BRIEFS: the ice-cream cone must show the cone solid (no scoop on top); the folding gate must really lean over when pushed; the die must match the numbers the tool uses; the toy-cube tower must be countable layer by layer.\n"
        "  OPTIONS: (a) accept all six; (b) use only redrawn versions of the book's own pictures; (c) accept all but the folding gate.\n"
        "  RECOMMENDATION: (a), each image checked for accuracy at the briefs stage."
    ),
    (
        "CLASH 16: Physical tasks become on-screen versions inside the tools.\n"
        "  BRIEF SAYS: \"Do not skip any important textbook concept or activity\", and children must act, not only watch.\n"
        "  BOOK SAYS: Many activities need real material: straws and clay (Craft 3; Tools 13, 14 and 16), a block kit, cubes (Tool 7), paper folding (the right angle checker, the circle), the end-of-book nets and cards, a thread to measure a crease, a compass, matchsticks (Tool 22), Craft 1 and Project Work.\n"
        "  THE PLAN: each becomes an on-screen version that keeps the book's rules (Tools 3, 7, 9, 11, 13, 14, 16, 17, 18, 22). Not on a tool: craft1 and project1 (on the C1 image), and straw_tri_trace (a notebook task, Tool 13). angles_do2, right_objects, acute_obj and obtuse_obj ask for objects in the classroom; they sit on a classroom scene inside Tools 10, 11 and 12.\n"
        "  OPTIONS: (a) on-screen versions; (b) show a physical task as a story step or an image and keep the tool to the screen part; (c) leave the physical tasks out.\n"
        "  RECOMMENDATION: (a)."
        "\n  QUESTION MAPPER (step 5): each physical task is a FIO item with one to three short steps that say what the child does on the screen (fold, build, join, move, lay the checker on a corner). Offline items keep Sample answers: craft1 and project1 (image T2.C1) and straw_tri_trace (Tool 13). The sphere craft and the street model are shown by their figures only."
    ),
    (
        "CLASH 17: The puzzle story for Tool 20 uses Diksha for a girl the book does not name.\n"
        "  NOTE SAYS: Flow row 40 (the story before Tool 20): \"Diksha finds shapes hidden in a drawing and cuts shapes into smaller ones.\" Pipeline rule: book characters and objects only.\n"
        "  BOOK SAYS: Six characters have names: Diksha, her father, Isha, Nitesh, Squiggly, Wiggly. The picture beside the page-19 puzzles shows an unnamed girl with a red bow; the boy with the Qutub model (page 2) and the girl with a straw triangle (page 14) are unnamed too.\n"
        "  OPTIONS: (a) Diksha tells the story (she is the chapter's main child); (b) \"a child\" with no name; (c) no person in the puzzle stories.\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 18: Two book items have no confirmed answer: page 22 Q4 (Tool 22) and the second cube tower (Tool 7).\n"
        "  NOTE SAYS: Tool 22's purpose is \"to form 2, 4 and 3 triangles\" and Tool 7's is to count \"the cubes in a tower layer by layer including the hidden ones\". A tool the book cannot support is a clash, never a change.\n"
        "  BOOK SAYS: Tool 22: Q2 (5 sticks, 2 triangles) is solved. Q3 (move 2 sticks to make 4 triangles) is solved only if the three triangles are read as touching at their base corners, though the figure draws small gaps. Q4 (remove 4 sticks to leave 3 triangles) is NOT solved in analysis.md (E20: the sticks were not counted exactly). Tool 7: the second tower on page 7 (a large green and cyan X shape) cannot be counted reliably from print; the first looks like layers of 16, 9, 4 and 1 = 30, uncertain.\n"
        "  OPTIONS: (a) the analyst or the content team solves Q3 and Q4 and counts both towers before the briefs; (b) the tools keep the items and show an answer only once it is confirmed; (c) hold the unconfirmed parts back (Tool 22 would form only the 2 and 4 triangles; its approved purpose would then change, which needs the user).\n"
        "  RECOMMENDATION: (a)."
        "\n  QUESTION MAPPER (step 5): option (b). ch1.towers: the first tower is checked on the page at 14x, with front rows 4, 3, 2 and 1 and matching left faces, so layers of 16, 9, 4 and 1 make 30 (the answer shows 1 + 4 + 9 + 16 = 30 in its steps). The second tower gets NO number; the answer says to count it layer by layer on the screen. ch1.try3 and ch1.try4 give NO solution and no stick count; each answer says to move or take away sticks on the screen and count (Sample answer). ch1.try2 is solved (a diamond of 4 sticks with the 5th across it). Tool 22 therefore has only try2 confirmed, and the user's choice among options (a), (b) and (c) is still open."
    ),
    (
        "CLASH 19: The word pentagon first reaches the child on Tool 14, with no video or image of its own before it.\n"
        "  NOTE SAYS: Tool 14 (Angles After the Push) follows the image of the folding gate (flow rows 28 and 29, topic T10), and its approved purpose is \"The child pushes a rectangle, a square and a pentagon and reads how the angles change\". The flow rules say a tool applies a concept the child has just met, and the brief says \"Do not introduce concepts assigned to later tools prematurely\".\n"
        "  BOOK SAYS: C15, the pentagon (printed page 16), is a small fact plus one hands-on step: \"Try to make this 5-sided shape with all sides equal (Pentagon)\". The book names the shape inside the task, with its picture, and then asks whether the angles are right angles and what happens when a side is pushed. No sentence teaches the word before the task. The proposal gives C15 no concept video and no image (tool_proposal.md section 2: \"inside Tool 14\"). The only media before Tool 14 are the push-test video (a triangle and a rectangle) and the folding-gate image (four-sided shapes), so the word pentagon and the idea of a 5-sided shape are new on the tool itself. The review (T18) does not revise the pentagon on its own either.\n"
        "  OPTIONS: (a) keep it as the book does: the tool names the pentagon with the shape beside the word, and no media is added; (b) the folding-gate image (T10.C3) also shows a five-sided frame and its caption names it (no new media item, but that image then carries two ideas and the media step must keep it clean); (c) add one pinned image of a pentagon beside Tool 14 (one more image, 7 in all; a new real-life example, checked at the briefs stage; no tool changes); (d) end the rigid-shapes video (T10.C1) with Isha making a five-sided shape and naming it (that video then carries a second idea, which breaks one concept per video).\n"
        "  RECOMMENDATION: (a). The book itself names the pentagon inside the task, and the media step can still choose (b) or (c)."
    ),
    # ---- CLASH 20 to 29: added by the media step (step 4, the media minimiser)
    (
        "CLASH 20: Three images would repeat the pictures of the tool that follows them (everyday objects, cube tower, carpet and wheels).\n"
        "  NOTE SAYS: Flow rule 2: \"Do not duplicate content\", and an image only \"when it contributes a new real-life example or visual reference\". The user's principle: several tools discover something on their own, so an image must not give the finding away.\n"
        "  BOOK SAYS: The proposal's images show the same things the tools use. Tool 5 marks the book's border sketches (a die, an eraser, a ball, a can, an ice-cream cone, a party hat, a cheese wedge, a gift box and more), and the image before it listed exactly those objects. Tool 7 counts the book's two cube towers, and the image before it was a tower in layers with cubes that cannot be seen. Tool 18 marks the book's carpet and compares the book's wheels A to D, and the image before it was a carpet beside four wheels of different sizes, which would show the comparison (B largest, D smallest) before the tool does.\n"
        "  THE PLAN (media step): each image shows different real objects of the same kind, so each adds a new real-life example and none shows a finding. Tool 5's image: four to eight objects that are not on the border (for example a matchbox, a round tin, a marble and a toy tent), standing apart, with no group, mark or label. Tool 7's image: a different small tower of plain toy cubes, drawn as a clean illustration so every cube can be counted (a photo cannot promise an exact count), with no number, no layer line and no see-through view. Tool 18's image: a round rug and ONE bicycle wheel, each seen straight on, not the book's carpet and not four wheels. Three new VISUAL_KEY keys (everyday_objects, toy_cube_tower, round_rug_and_wheel); one image title changed (\"A Round Rug and a Wheel\"); Tool 7's image style is now illustration.\n"
        "  OPTIONS: (a) as decided; (b) keep the proposal's objects (each image then shows the tool's own objects, and the wheel sizes and the layers are shown before the tool); (c) drop the image and let the tool follow a short video (a video replaces an image, so the count of media does not fall).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 21: The die image would answer part of Tool 4 if it shows the faces 1, 5 and 3.\n"
        "  NOTE SAYS: CLASH 15 asks that the die match the numbers the tool uses. The user's principle: an image must not give a finding away.\n"
        "  BOOK SAYS: Page 5 draws a die with 5 on top, 1 in front and 3 on the right, then asks which faces are opposite 2, 3 and 4 and which faces share an edge with the face numbered 1. A picture with 1 beside 5 and 3 shows that 5 and 3 touch 1, which is part of Let Us Observe 2 (a). A real die can never show two faces that add up to 7 together (1 and 6, 2 and 5, 3 and 4), so a generated picture must be checked for that. The book writes numerals; a real die has dots. The opposite pairs (E6) are the analyst's reading and still open (CLASH 11).\n"
        "  THE PLAN (media step): the image is a real standard die with dots, at rest, with the faces 6, 4 and 5 in view (none of the faces the questions ask about, and no pair that adds up to 7), with no label, arrow, second die or hidden face. The tool's die is drawn with dots too, with opposite faces adding up to 7, so one die looks the same everywhere (VISUAL_KEY die).\n"
        "  OPTIONS: (a) as decided; (b) the proposal's faces 1, 5 and 3 (they match the book's picture and the tool, and show that 5 and 3 touch 1); (c) numerals on both die pictures (the image is then not a real die).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 22: A real folding gate shows leaning cells, which are what a pushed square looks like.\n"
        "  NOTE SAYS: CLASH 15: \"the folding gate must really lean over when pushed\". Tool 14, which comes right after the image, is where the child finds that the right angles of a pushed rectangle and square become acute and obtuse.\n"
        "  BOOK SAYS: The book has no gate. A real scissor gate is a lattice of equal strips; each cell has four equal sides and, half closed, shows acute and obtuse angles. A still picture cannot show a push.\n"
        "  THE PLAN (media step): one picture of a gate half closed so the cells lean, a photo of a real gate (if no true photo is available, a clean illustration with straight strips of equal length and a pin at every crossing). It carries no angle mark, no label, none of the words acute, obtuse or right angle in its caption, no hand, no before and after pair and no five-sided frame. It gives a real use of the idea of Tool 13 (a four-sided frame does not hold its shape), not the finding of Tool 14.\n"
        "  OPTIONS: (a) as decided; (b) a before and after pair of the same gate (it shows the push and gives away Tool 14's finding); (c) drop the gate and let Tool 14 follow a short video (a second push story, repeating the one before Tool 13).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 23: The media step's answer to CLASH 19 (the pentagon).\n"
        "  NOTE SAYS: CLASH 19 left the choice of (a), (b) or (c) to the media step, to be recorded for the user to decide.\n"
        "  BOOK SAYS: Page 16 names the pentagon inside the task, with its picture: \"Try to make this 5-sided shape with all sides equal (Pentagon)\". The shape is one more straw added to shapes the child has just pushed.\n"
        "  THE PLAN (media step): picks (a), no medium added. The fewest-media rule says a fact the tool already shows, with the word beside its picture, needs no image or video. (b) is rejected: the gate image would carry two ideas, and a real folding gate has no five-sided cell, so it would misrepresent the object. (c) is possible but adds a seventh image, and it would have to be pinned: whether the platform shows a pinned image is not verified (docs/02, notes on the wording). (d) of CLASH 19 breaks one concept per video.\n"
        "  OPTIONS: (a) no new medium; Tool 14's first screen shows the five-straw shape and the word pentagon; (b) a five-sided frame in the gate image (not recommended); (c) one pinned picture of one real five-sided object next to Tool 14, chosen at the briefs stage, with five straight sides and no label (7 images); (d) end the rigid-shapes video with a pentagon (not recommended).\n"
        "  RECOMMENDATION: (a). The user decides."
    ),
    (
        "CLASH 24: Would a short video teach better than the image before Tools 4, 5, 7, 14 and 18? (the media step's view of CLASH 7)\n"
        "  NOTE SAYS: CLASH 7 keeps the five images. This step was asked to say, tool by tool, whether a video would teach the idea better, and not to change it.\n"
        "  THE PLAN (media step): Tool 4 (opposite faces): no. The idea is two words and the tool is the turning die; a video of a turning die would do what the tool does and hand over the opposite pairs. Tool 5 (spot the faces): no. The words rectangular, triangular and curved face come from the videos on faces; a video would repeat them. Tool 7 (cubes): yes, it is the one of the five where a video would teach better, because a still picture cannot show a cube that is hidden and the hidden cube (M_SH_6) is the idea; but a story that builds the tower in layers would also give away the counting method the tool finds, and the tool's own layer view shows the same. Tool 14 (angles after the push): no. A second push story would repeat the push video before Tool 13, and the real gate adds a real-life use. Tool 18 (radius and diameter in things): no, the idea is applied, not new; only the three steps of the compass flower (E15: pictures only in the book) would gain from motion, and the tool can show them step by step.\n"
        "  OPTIONS: (a) keep the five images; (b) change one of them to a short story video (Tool 7 is the case for it: 17 concept videos and 5 images); (c) change more than one (say which).\n"
        "  RECOMMENDATION: (a); (b) for Tool 7 only if the user wants a video there."
    ),
    (
        "CLASH 25: Seven video purposes showed what the tool is meant to find, so they were reworded as questions.\n"
        "  NOTE SAYS: The journey designer wrote several videos to frame the idea and leave the finding to the tool, and flow rule 2 says do not give the same explanation twice. Rows 20, 26, 30, 32, 34, 38 and 40 of tool_map.md (and tool_map.locked.md) describe the stories before the tools.\n"
        "  BOOK SAYS / THE PLAN: As those rows read, a story would do the tool's work or show its result. Row 20 (angles) shows the house and the boat, which are Tool 10's solved example and its question. Row 26 (rigid shapes) has Isha push a triangle and a rectangle, which is Tool 13's whole test. Row 30 (angles in shapes) has Nitesh count the right angles of each shape, which is Tool 15's task. Row 32 (the circle) has equal straws make a circle, which is Tool 16's finding. Row 34 (diameter) has several folds give equal creases, which is Tool 17's finding. Row 38 (sides and angles) has Nitesh count the angles of each shape, which is Tool 19's finding. Row 40 (puzzling shapes) solves hidden shapes and cuts, which are Tool 20's puzzles. The VID purposes in topics_1.py now pose the question and stop: Isha meets two straws and sees yoga angles only; Isha wonders what a push does; Nitesh wonders how many angles are right angles; Diksha names the centre and one radius of a given round paper and wonders how to make a perfect circle; Diksha folds once and wonders if every fold is the same; Nitesh sorts by sides and wonders what else to count; Diksha finds one hidden shape and makes one cut. No new_idea changed. The rows of the locked table still carry the older wording (the table is not edited).\n"
        "  OPTIONS: (a) the reworded purposes (the tool finds the answer); (b) the rows' wording (the video shows the result and the tool then repeats it).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 26: Six videos have a thin case for being a video: three link concepts and three puzzle stories.\n"
        "  NOTE SAYS: The media test is a video for the hook, a big new idea or a known misconception, and a small concept may be one image. But every tool after Tool 1 needs one video or one image right before it (the flow gate), so 21 media items before 21 tools is the floor: fewer media would mean fewer tools (CLASH 2). The media step can only choose video or image for each tool; it cannot lower the count.\n"
        "  BOOK SAYS / THE PLAN: Clear cases (a big idea or a misconception each): prisms and pyramids, faces corners and edges, the overlap, nets, angles, right angles, acute and obtuse, rigid shapes, the circle and the diameter. Thin cases: the guessing game (T6.C1, a link concept, and Tool 8 is the same game), right angles in shapes (T11.C1, a link, and Tool 15 does the counting) and sides and angles (T14.C1, a link, and Tool 19 finds the pattern); and the three puzzle stories on hidden shapes, webs and matchsticks (T15.C1, T16.C1, T17.C1), which the user's brief asks for (\"Puzzle / activity videos\") and which carry the misconceptions M_PU_1 to M_PU_3. Each of the six is kept to one frame the tool does not give.\n"
        "  OPTIONS: (a) keep all 16 concept videos (the proposal); (b) change the three link videos to images (same count; each would need a real-life picture that its tool then partly repeats); (c) fewer tools (CLASH 2, option b or c).\n"
        "  RECOMMENDATION: (a)."
    ),
    (
        "CLASH 27: One colour per solid across the chapter, and every solid drawn as a shaded 3D solid.\n"
        "  NOTE SAYS: Flow rule 3: \"Use consistent visual representation and colours for the same shapes / objects across the chapter.\" The user's principle: a sphere is always a shaded 3D ball; never misrepresent an object.\n"
        "  BOOK SAYS: The book colours the same solid differently on different pages: prisms are blue and pyramids magenta on page 3, but the square pyramid is green and the triangular pyramid blue on page 8; the cuboid is red on page 8 and purple on page 9; the cone is purple in one row and yellow in the next. The small beige \"sphere\" of page 8 reads like a flat disc.\n"
        "  THE PLAN (media step): every solid is drawn as a shaded 3D solid in every picture and tool (VISUAL_KEY updated: a sphere is a shaded ball, a cone has one round base and one point, a cylinder two round flat faces, a cube six equal squares, a cuboid rectangle faces, the small orange solid of page 8 a triangular prism). The colours are NOT decided: VISUAL_KEY keeps the book's colour for each figure.\n"
        "  OPTIONS: (a) one colour per solid for the whole chapter: prisms blue and pyramids magenta (as on page 3), cube teal, cuboid red, sphere red, cone yellow, cylinder pink-purple; (b) the book's colour for each figure (as VISUAL_KEY now says).\n"
        "  RECOMMENDATION: (a), because the flow rule asks for it; VISUAL_KEY is edited only after the user's answer."
    ),
    (
        "CLASH 28: The review and the earlier pictures.\n"
        "  NOTE SAYS: Flow rule 1.7: the review uses concepts already covered and adds no new content. The gate: no video or tool in the review, no new key term, no book item. The brief asks for \"a visual recap\".\n"
        "  THE PLAN (media step): the review (T18) has no video, no image node and no tool. Between its two concepts it revises the idea of every topic; the two scene-setting images (T2.C1 bricks and T4.C1 everyday objects) are not revised on their own. A recap may show an earlier picture only as the same VISUAL_KEY drawing (the die, the cube tower, the gate, the carpet and wheels, the solids, the straw shapes, the circle), never as a new picture.\n"
        "  OPTIONS: (a) recap lines only, no pictures; (b) recap lines with earlier drawings re-shown by their key, with no new image node; (c) one new recap image (a new medium and a risk of new content).\n"
        "  RECOMMENDATION: (b), which meets the brief's \"visual recap\" with no new medium."
    ),
    (
        "CLASH 29: The image after Tool 1 holds three subjects.\n"
        "  NOTE SAYS: CLASH 8 and CLASH 15: one clean real-life image on the concept; images are clean and minimal.\n"
        "  BOOK SAYS: Page 2 asks about three different pictures: whether the boy's stepped box model looks like the Qutub Minar (qutub_q1), what shape to use and how many for a model of the tower (qutub_q2, qutub_q3), and what the clay brick, the stone block and the wooden block share (bricks_q). Without the model qutub_q1 cannot be asked; without the blocks bricks_q cannot.\n"
        "  THE PLAN (media step): one picture with the real tower, the small stepped stack of three boxes beside it (no child: it stands on a table) and the three blocks in front, well spaced. No label, no number, no \"5 storeys\", no count of boxes or storeys, no hand. The blocks are true cuboids. The tower must be the real monument (a real photograph, or a faithful drawing checked against the book), never an invented tower. The book's figures for the street model (project1) and the paper strip ball (craft1) are not in this picture: they are the figures of those two question cards (VISUAL_KEY street_model and paper_strip_ball).\n"
        "  OPTIONS: (a) one picture, three subjects; (b) tower and blocks only, and qutub_q1 reworded (changes a book question); (c) two images (a second medium on one concept, which breaks one image per concept).\n"
        "  RECOMMENDATION: (a)."
    ),

    # ---- CLASH 30 to 33: added by the question mapper (step 5)
    (
        "CLASH 30: Three book questions sit one tool away from the proposal ONLY because of the cap of 6 (PROVISIONAL).\n"
        "  NOTE SAYS: The cap is 6 book questions per tool (chapter.config.json 'max_tool_questions': 6, a config default that only the user may raise; the structure stage fails a tool with 7). CLASH 3 left Tools 2, 13 and 14 at 7 each. The user's instruction for step 5: keep the cap at 6, home at most 6 on every tool provisionally, move for each of the three tools the single item whose move does least harm, and delete nothing.\n"
        "  BOOK SAYS: The proposal gave Tool 2 prism_q1, prism_q2, prism_q3, pyr_q1, pyr_q2, pyr_q3 and cube_prism; Tool 13 straw_tri_make, straw_tri_push, straw_tri_trace, straw_tri_angles, straw_rect_make, straw_rect_angles and straw_rect_push; Tool 14 straw_rect_after, straw_square, straw_compare, pentagon_make, pentagon_q1, pentagon_q2 and pentagon_q3.\n"
        "  MOVED, AND WHERE THEY SIT NOW: (1) ch1.cube_prism ('Is a cube also a prism?') from Tool 2 to Tool 3, Faces, Corners and Edges (now 6): the table that Tool 3 fills has the row 'Cube/Square Prism', and it is the proposal's own fallback (options (a) and (c) of CLASH 3). Harm: Tool 2's approved purpose ends 'and decides if a cube is also a prism', and its one book question for that now comes one tool later. (2) ch1.straw_rect_angles ('What kinds of angles do you see in the rectangle?') from Tool 13 to Tool 11, Right Angle Checker (now 5): the answer, all four are right angles, is found by laying the checker on the corners, which is Tool 11's action. Harm: it is asked two tools before the child pushes the rectangle (Tool 13), on a straw rectangle shown on Tool 11's screen. (3) ch1.straw_compare ('How are the angles of triangles and rectangles similar or different?') from Tool 14 to Tool 19, Sides and Angles (now 6): Tool 19 compares the numbers of angles and sides of shapes, and a triangle and a rectangle are among them. Harm: the closing question of the push test is asked five tools after it. Tools 2, 13 and 14 now hold 6, 6 and 6; Tools 3, 11 and 19 hold 6, 5 and 6. Nothing was deleted, no item kind was changed, no other question moved from the proposal.\n"
        "  OPTIONS: (a) keep the three provisional moves (cap 6, 22 tools, no new tool); (b) raise the cap to 7 for this chapter (CLASH 3 option b): the three items go back, cube_prism to Tool 2 (last in its list), straw_rect_angles to Tool 13 (between straw_rect_make and straw_rect_push) and straw_compare to Tool 14 (after straw_square), three small edits in topics_1.py; Tools 2, 13 and 14 then hold 7 and Tools 3, 11 and 19 hold 5, 4 and 5; (c) keep the cap and call straw_tri_trace and straw_compare talk items (CLASH 3 option c; this changes content.NCERT_ITEMS, the analyst's work, and is the user's call); (d) the 23-tool plan of CLASH 3 option (a).\n"
        "  RECOMMENDATION: (b), as CLASH 3 recommends. Until the user decides, the three moves keep the structure stage clean."
    ),
    (
        "CLASH 31: Three readings of the printed figures by the question mapper differ from analysis.md or from VISUAL_KEY.\n"
        "  NOTE SAYS: The user's rule: never misrepresent an object; check every number against the page; no answer is invented. analysis.md (E17, E23) and VISUAL_KEY were written from the page at lower zoom.\n"
        "  BOOK SAYS: (1) Hidden shapes (page 19, ch1.puzzle1): read at 7x, the outlines are a circle, a cylinder, ONE square (the one on the right, 420 by 420 units), ONE tilted rectangle (756 by 337, about 2.2 times as long as wide) and two triangles; analysis.md says two squares. (2) The red tilted figure of Q8 (page 23, ch1.try8, ch1.try8_q) measures 213 by 259 units at 6x (a rectangle, about 5 to 6), not a square; analysis.md and VISUAL_KEY right_angle_figures say 'red tilted square'. Its 4 right angles stand either way. (3) The border sketches (page 5, ch1.border1, border2, border5): the two cheese pieces are drawn as PYRAMIDS (an apex over a base with holes), and the border also has a pyramid drawn with a triangle grid and a double-pyramid sketch; VISUAL_KEY border_objects says a cheese wedge or cake slice is a triangular prism and does not list the two pyramid sketches.\n"
        "  THE PLAN (question mapper): (1) answer 'a circle, a cylinder, a square, a rectangle and two triangles'; VISUAL_KEY hidden_shapes is corrected. (2) answer 'the blue rectangle and the red tilted shape'; VISUAL_KEY right_angle_figures is corrected to a tilted rectangle. (3) the answers of border1, border2 and border5 name only the objects whose solid is certain (dice, erasers, Rubik's cube, gift box, wooden wedge, cake slice) with 'for example'; VISUAL_KEY border_objects is NOT edited.\n"
        "  OPTIONS: (a) keep the two VISUAL_KEY corrections and decide the cheese pieces (as pyramids like the book, or as the triangular prisms VISUAL_KEY says) before the briefs; then the border answers are completed; (b) undo the corrections and keep analysis.md's reading (two squares, a red square); (c) the content team settles all three.\n"
        "  RECOMMENDATION: (a). The page shows a rectangle in both places, and the two corrections are one phrase each. The cheese pieces are a user decision because a pyramid has triangular faces and a base, a triangular prism has rectangular faces too."
    ),
    (
        "CLASH 32: The words on screen of six questions differ from the print in small ways.\n"
        "  NOTE SAYS: The question mapper copies the book's wording exactly (agent rule 5). The user's rules: no teacher role (brief), minus is U+2212, no page pointer that fails on a screen, no wrong printed statement repeated.\n"
        "  BOOK SAYS / DONE: (1) ch1.compass: 'Ask your teacher to help you use a compass.' is dropped (CLASH 13 option a, as recommended; it edits one book question and needs the user's yes). (2) ch1.project1: 'Encourage learners to observe a street carefully...' reads 'Observe a street carefully...' (a teacher line inside a question; CLASH 13). (3) ch1.fve: 'F+V' then an en dash then 'E' is printed; the screen shows F+V−E with the minus sign. (4) ch1.pentagon_q2: the missing question mark of '...push one of its sides. Yes/No' is put in. (5) ch1.amazing_q4: 'center' is written 'centre', as in the rest of the chapter. (6) ch1.sort4: 'circles like those on the previous page' reads 'circles like the ones you just used', because a screen has no pages. The book's pointers 'at the end of the book' (craft2, cards) and 'given below' stay as printed, with a first step that says the nets and the cards are on the screen. Each change is in content.SOLUTION_NOTES and is one phrase.\n"
        "  OPTIONS: (a) as done; (b) keep every printed word, including the teacher sentences, the en dash and 'previous page' (breaks the brief's rule on teachers and the dash rule); (c) keep the printed words and add a short note under each question.\n"
        "  RECOMMENDATION: (a). Each change can be undone with one edit of topics_1.py."
    ),
    (
        "CLASH 33: Two printed questions have two readings, and the plan shows both or says which one it took.\n"
        "  NOTE SAYS: The user's rule: no invented answer; no child-facing text repeats a wrong printed statement.\n"
        "  BOOK SAYS: (1) ch1.prism_q3, 'How many such faces each?' (page 3): 'such' can mean the other shapes of Q2, which are 2 on every prism, or the rectangle faces of Q1, which are 3, 4 and 6 on the triangular, square and hexagonal prisms. (2) ch1.try1d, 'Can he begin at point A and leave from point B without walking on any wall more than once?' (page 21): the question does not say that every wall must be used. Read as it stands, the answer is yes (a short walk from A to B uses a few walls once each). The story says he walks to check that his walls are strong, so the plan reads it as a walk that uses EVERY wall once; then no walk from A can be completed, because A and B have 2 walls each and only the two corners with 3 walls can start and end such a walk (analysis.md E19; the rule about corners is not shown to the child). Squiggly's walk (ch1.try1b) is yes on either reading.\n"
        "  THE PLAN (question mapper): the answer of prism_q3 gives both counts; the answer of try1d says 'No. Try to use every wall once. Every walk from A gets stuck first.' and asks the child to try it on the screen.\n"
        "  OPTIONS: (a) as done; (b) prism_q3 answers only the other shapes (2 each) and try1d answers yes with a short walk (the plain reading); (c) the content team says what the author meant.\n"
        "  RECOMMENDATION: (a), and (c) if the content team can be asked."
    ),
]

# ---------------------------------------------------------------------------
# printed-book errors this plan corrects: {"item", "printed_solution", "correct"}; and ERRATA, exact false-equation
# chains kept verbatim from the book (copy each into chapter.config.json "eqcheck_errata" too).
# ---------------------------------------------------------------------------
SOLUTION_NOTES = [
    {"item": "all 109 questions",
     "printed_solution": "The chapter prints no answer, solution or key.",
     "correct": "No content-team key is part of this chapter's files (CLASH 11). Every answer is the plan's own reading "
                "and begins exactly 'From the picture' (counts, positions, what a picture shows) or 'Sample answer' "
                "(open tasks and geometry the book does not print); open tasks end 'Your answer may differ'. None is "
                "presented as an official textbook answer. Where no answer could be confirmed (ch1.try3, ch1.try4 and "
                "the second tower of ch1.towers) the answer gives no number and no solution and says how to find it. "
                "The content team may replace the answers with a key."},
    {"item": "ch1.solids_q4 (E1)",
     "printed_solution": "No key. Net A is a column of four rectangles with one flap at the top right and one at the "
                         "bottom right, both on the SAME side; net C has the rectangle and only 2 of the 4 triangles its "
                         "pyramid needs. B (cylinder) and D (flat box, flaps on opposite sides) are fine.",
     "correct": "The figure and the question stay as printed. The answer says 'B and D fold into the solid below. A and "
                "C do not. Fold each one to check' (From the picture), so the child tests it by folding on the screen. "
                "The reason is not told, and the plan does not draw a 'this folds' picture of A or C."},
    {"item": "ch1.three_faces (E2)",
     "printed_solution": "'Can you construct a 3D shape with 3 flat faces?' does not say whether curved faces are allowed.",
     "correct": "Sample answer: a solid with only flat faces needs at least 4, and a cylinder cut in half along its "
                "length has 3 flat faces and 1 curved face. The answer gives both readings."},
    {"item": "ch1.sort_faces and ch1.sort_edges (E3)",
     "printed_solution": "The set of shapes to sort is not stated. The columns are 1, 2, 4, 5, 6 and 8 flat faces and "
                         "6, 8, 9 and 12 straight edges, so the pentagonal pyramid (10 edges) and the hexagonal prism "
                         "(18 edges) have no edge column, and there is no column for 0, 3 or 7 flat faces.",
     "correct": "Sample answers: flat faces 1 cone, 2 cylinder, 4 triangular pyramid, 5 square pyramid and triangular "
                "prism, 6 cube, cuboid and pentagonal pyramid, 8 hexagonal prism. Straight edges 6 triangular pyramid, "
                "8 square pyramid, 9 triangular prism, 12 cube and cuboid; the answer says the pentagonal pyramid (10) "
                "and the hexagonal prism (18) fit no column."},
    {"item": "ch1.sort3_q and ch1.sort4 (E4)",
     "printed_solution": "'rectangular pyramid' is printed but never named in the chapter. sort4 says 'circles like "
                         "those on the previous page', which points to a page of the book.",
     "correct": "The answer says both solids go in the overlap because both have rectangle faces and triangle faces, "
                "and describes the pyramid as 'a pyramid with a rectangle base' in ch1.sort3. In ch1.sort4 the words "
                "'on the previous page' read 'you just used' (CLASH 32)."},
    {"item": "ch1.solids_q1 (E5)",
     "printed_solution": "Seven pictures stand beside six descriptions, not lettered. Description f) '6 faces, 12 edges, "
                         "8 corners' fits both the cuboid and the cube. No key.",
     "correct": "From the picture: a) square pyramid, b) cone, c) sphere, d) cylinder, e) triangular prism, f) 'cube or "
                "cuboid, because both fit'. The sphere is a shaded ball."},
    {"item": "ch1.observe1 (E6)",
     "printed_solution": "'Take a die.' The answers depend on the die in hand; the picture shows only 5, 1 and 3. No key.",
     "correct": "Sample answer: on a usual die, a) 5, b) 4, c) 3, because opposite faces add up to 7 (2 + 5, 3 + 4, "
                "4 + 3). The tool's die is a usual die (VISUAL_KEY die)."},
    {"item": "ch1.border1 to ch1.border5 (E7)",
     "printed_solution": "The shapes along the border are about 20 pencil sketches, not numbered, with no key. 'Circle the "
                         "shapes that have the same opposite faces' is unclear. The two cheese pieces are drawn as "
                         "pyramids, not as wedges.",
     "correct": "From the picture: border3 (curved face) the balls, the football, the cans and bottles, the ice-cream "
                "cone and the party hat; border4 (no corner) the balls, the football, the cans and the bottles. "
                "border1 and border2 name only the unambiguous objects, with 'for example'. border5 is a Sample answer "
                "under one reading (each pair of opposite faces looks the same). The cheese pieces and the two pyramid "
                "sketches are left out of the answers until the user decides (CLASH 31, CLASH 12)."},
    {"item": "ch1.boat_q (E8)",
     "printed_solution": "'How many angles are there in this boat drawing?' The book does not say that the mast splits the "
                         "sail into two angles. No key.",
     "correct": "From the picture: 10 marked angles: 4 in the body, 2 at the top of the sail, 2 at the lower corners of "
                "the sail and 2 right angles where the mast meets the sail (4 + 2 + 2 + 2 = 10). The house has 7 "
                "(1 + 2 + 2 + 2 = 7), as the book says."},
    {"item": "ch1.right_circle (E9)",
     "printed_solution": "Eight angle figures on a dot grid and no key.",
     "correct": "From the picture, read by measure: the 2nd and 3rd angles in the top row and the 1st and 4th in the "
                "bottom row are right angles. The answer says to check each with the checker."},
    {"item": "ch1.letters and ch1.ao_do2 (E10)",
     "printed_solution": "'Identify all angles' in V, A and Z marks only one angle in each letter and does not say how many "
                         "there are in A. The four stick figures do not say how many angles to mark.",
     "correct": "Sample answers with no count of the angles of A or of the figures: V has 1 acute angle, Z has 2 acute "
                "angles, A has an acute angle at the top and angles where the bar meets the legs. For the stick figures "
                "the answer gives the method: red if smaller than a right angle, green if the same, blue if bigger."},
    {"item": "ch1.straw_tri_push to ch1.pentagon_q3 (E11)",
     "printed_solution": "The push test has no printed answer; the teacher note says only that the triangle is the most "
                         "rigid shape.",
     "correct": "Sample answers the child can test on the screen: the triangle does not change; the rectangle, the "
                "square and the pentagon do; a pushed rectangle or square has two acute and two obtuse angles; a pushed "
                "pentagon has some angles smaller and some bigger. The pentagon's angles are all bigger than a right "
                "angle (From the picture)."},
    {"item": "ch1.fourside_q (E12)",
     "printed_solution": "The three 4-sided shapes are not named.",
     "correct": "The answer says 'the three shapes shown' and gives no name for them: a rectangle and a square have 4 "
                "right angles, and the three shapes shown have none."},
    {"item": "ch1.pentagon_q2, ch1.amazing_q4 and ch1.fve (E13, E14)",
     "printed_solution": "pentagon_q2 has no question mark ('... push one of its sides. Yes/No'). amazing_q4 spells 'center' "
                         "while the chapter says 'centre'. fve prints 'F+V' and 'E' joined by an en dash.",
     "correct": "The screen shows 'sides? Yes/No', 'centre' and 'F+V−E' with the minus sign (CLASH 32). Nothing else is changed."},
    {"item": "ch1.compass and ch1.project1 (E15 and the teacher wording)",
     "printed_solution": "'Ask your teacher to help you use a compass.' and 'Encourage learners to observe a street "
                         "carefully...' give a teacher a role. Step 1 to Step 3 of the compass design are pictures only.",
     "correct": "The compass question reads 'A circle can be made easily using a compass. Make the following design.' and "
                "project1 reads 'Observe a street carefully and make a model showing the main buildings on the street.' "
                "(CLASH 13, CLASH 32; the user's yes is needed). The steps of the design are read from the three pictures "
                "(same opening, circles with their points on the first circle, then colour the petals)."},
    {"item": "ch1.wheels_q1 (E16)",
     "printed_solution": "Radius and diameter are asked four ways but only two wheels can answer; no units; no key.",
     "correct": "From the picture, read by measure: longest radius and longest diameter B; shortest radius and shortest "
                "diameter D. Radius and diameter are the same wheel in each pair."},
    {"item": "ch1.puzzle1 to ch1.puzzle4 (E17)",
     "printed_solution": "The number of hidden shapes is not stated, and no solution to puzzles 2 to 4 is printed; the cuts "
                         "are not unique. analysis.md reads two squares among the hidden shapes.",
     "correct": "Read again at 7x: the hidden shapes are a circle, a cylinder, ONE square (the one on the right), ONE tilted "
                "rectangle (about 2.2 times as long as wide) and two triangles (From the picture; CLASH 31). Puzzle 2 on "
                "the 4 by 4 right triangle: a line from the middle of the top side straight down to the slanted side, and "
                "a line from the middle of the left side straight across to it; they make 1 square and 2 triangles. "
                "Puzzle 3: a dot on the top side joined to the two bottom corners makes 3 triangles. Puzzle 4: Sample answer."},
    {"item": "ch1.cards (E18)",
     "printed_solution": "The six cards are at the end of the book, and the book does not say what the three groups are.",
     "correct": "The six cards are on the screen. Sample answer: only straight sides (square, triangle), only curved sides "
                "(oval, circle), both (quarter circle, semicircle)."},
    {"item": "ch1.try1a to ch1.try1d (E19)",
     "printed_solution": "No key. Neither walking question says that every wall must be used.",
     "correct": "From the picture: 10 triangles (1 at the top, 1 at the bottom, 4 small and 4 big in the middle: 1 + 1 + 4 + 4 "
                "= 10) and 12 rectangles. Squiggly's walk is possible: the walls in the order 12, 6, 9, 3, 4, 7, 10, 2, 8, "
                "5, 11, 1 use all 12 once and return to A. Wiggly's walk is read as one that uses every wall once, and then "
                "no walk from A can be completed (CLASH 33); the answer gives no rule about corners."},
    {"item": "ch1.try3 and ch1.try4 (E20)",
     "printed_solution": "No answer. Q3 is solvable only if the three triangles are read as touching at their base corners "
                         "(the figure draws small gaps); Q4 was not solved.",
     "correct": "The answers give no solution and no stick count. They say to move two sticks (Q3) or take away sticks "
                "(Q4) on the screen and count the triangles, as a Sample answer (CLASH 18)."},
    {"item": "ch1.towers",
     "printed_solution": "'How many cubes are there in each of these cube towers?' No key. The second tower (the large X) "
                         "cannot be counted reliably from print.",
     "correct": "The first tower has 4 layers of 1, 4, 9 and 16 cubes (checked on the page at 14x): 1 + 4 + 9 + 16 = 30. "
                "The answer gives NO number for the second tower and says to count it layer by layer on the screen "
                "(CLASH 18)."},
    {"item": "ch1.try5 (E21)",
     "printed_solution": "c) 15 straws and 10 clay balls is a solid the chapter never shows.",
     "correct": "The working shows it from its parts: two 5-sided ends (5 + 5 = 10 straws) and 5 more straws (10 + 5 = 15), "
                "with 5 + 5 = 10 balls. The answer says 'a solid with two 5-sided ends' and does not name it. a) cube or "
                "cuboid, b) triangular prism, d) pentagonal pyramid (5 + 5 = 10 straws, 5 + 1 = 6 balls)."},
    {"item": "ch1.try8, ch1.try8_q and ch1.try9 (E22, E23)",
     "printed_solution": "try9 asks to 'identify the shape' but several shapes fit each clue; shape 1 is a dart with an angle "
                         "larger than a straight line. try8 has no key, and its red tilted figure is drawn as a rectangle, "
                         "not a square.",
     "correct": "From the picture, read by measure: try8 4, 0, 1, 0, 0, 4 and 'the blue rectangle and the red tilted shape'. "
                "try9: 2 right, 1 acute, 1 obtuse: shapes 2 and 7; 1 right, 2 obtuse, 1 acute: shape 10; 2 obtuse, 2 "
                "acute: shapes 3, 5, 8, 9, 11, 13; 4 right angles: shapes 4, 6, 12, 14. The answer says that more than "
                "one shape fits. Shape 1 fits no clue and is not mentioned."},
    {"item": "ch1.craft2 (E24)",
     "printed_solution": "Craft 2 shows a 'Square Prism', but the net page at the end of the book has no net of that name "
                         "(it has a 'Rectangular Prism / Cuboid').",
     "correct": "The answer does not name which net makes which prism. It says each net folds into the solid shown beside "
                "it, a Sample answer. The nets are on the screen."},
    {"item": "ch1.prism_q3",
     "printed_solution": "'How many such faces each?' does not say which faces: the other shapes of Q2 (2 each) or the "
                         "rectangle faces of Q1 (3, 4 and 6). No key.",
     "correct": "From the picture: the answer gives both, '2 of the other shape on each prism. The rectangle faces are 3, "
                "4 and 6' (CLASH 33)."},
]
# The book prints no equation and no false sum, so there is no false-equation chain to keep: ERRATA stays empty and
# chapter.config.json "eqcheck_errata" stays empty. Every sum the plan writes is true (F+V−E = 2 for the five solids,
# 1 + 4 + 9 + 16 = 30, 4 + 2 + 2 + 2 = 10, 1 + 2 + 2 + 2 = 7, 1 + 1 + 4 + 4 = 10, 5 + 5 + 5 = 15, 5 + 5 = 10, 5 + 1 = 6).
ERRATA = [
]

DESIGN_REFERENCES = [
    {"text": "Class 3/4 story and tool flow: docs/00_overview.md. The approved tool map comes from the content team.",
     "url": ""},
]

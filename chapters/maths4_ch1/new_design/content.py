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
# Five modules (step 3, the journey designer; amended on 12 Nov 2026, CLASH 58). M1 is Lesson 1 and holds its two topics (T1 and T2:
# the gate fixes the opening topic as exactly [hook, Tool 1], so Lesson 1 needs two topics, CLASH 6); M2 is the solids
# (Lessons 2 to 5, T3 to T6); M3 is the angles (Lesson 6, T7); M4 is circles, the pentagon and rigid shapes (Lessons 7 and 8,
# T8 and T9). M5 holds Lesson 9 (T10, the recap story and the three practice tools) and the closing look back (T11, the review,
# which the pipeline wants as the last topic). There is no separate MLAST module any more: M5 is the last module, so
# core/finalize_ids.py has nothing to rename.
MODULES = [
    ("M1", "Spotting Shapes", "Find shapes in buildings. Guess a hidden shape from its clues."),
    ("M2", "Solid Shapes", "Meet prisms and pyramids and fold nets. Count faces, edges and corners, then cube towers."),
    ("M3", "Angles", "Make angles with straws and paper. Sort them as acute, right or obtuse."),
    ("M4", "Circles and Firm Shapes", "Draw a circle, make a pentagon and test which straw shapes stay firm."),
    ("M5", "Revision and Review", "Name the shapes of the chapter, try a worksheet and a short assessment, then look back."),
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
    # them no names. Diksha's father is "Her father" in the book (not named, not drawn). The new lesson plan (lp_brief.md)
    # names no character of its own: it is written as a teacher showing pictures, videos and activities.
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
# These describe how the BOOK draws each recurring object (step 1, written from a fresh reading of all 23 page images), as
# CORRECTED BY THE MEDIA STEP (step 4) to the recommended option of CLASH 34 (still open: provisional until the user decides):
# every drawn solid is a shaded 3D solid with ONE colour per kind of solid (prisms blue, pyramids pink as on the book's first
# solid spread, cube teal, cuboid red, sphere coral, cone yellow, cylinder orchid); a net is never in the colour of its solid;
# real objects (wooden blocks, bricks, a die, a football, tents, paper boxes) keep their own colours; sticks, clay balls, nets,
# dot paper, the compass and the cube towers are drawn so every part can be counted. Added by the media step: `isha`,
# `dikshas_father`, `sphere`, `solid_colours`, `compass` (objects the questions and videos need) and `prism_tent`,
# `pyramid_tent` (the one image). The book prints neither tent; they are the plan's own real-life examples (CLASH 32, 43). The
# football patch of the second image was removed on 12 Nov 2026 (CLASH 57), and so was its key. All visuals are made new: the
# third-party pictures in the plan are references only (CLASH 31).
VISUAL_KEY = {
    "wooden_blocks": "light brown wooden blocks: cuboids of different sizes, a cylinder, a cube and two half-round blocks, lying on a floor mat in front of a drawing of India Gate (real wood, so the blocks keep the light brown of wood as in the book and are not in the solid colours; in the hook video none is placed on a part of the model, so nothing shows which block fits where)",
    "india_gate_drawing": "a drawing of India Gate in sandy brown on a white sheet that stands up behind Diksha: a tall arch with a round-topped opening between two thick pillars, a flat top above it and steps below (it is an arch, so no single block of the set fits it)",
    "other_buildings": "two small buildings drawn beside the first task: a sandy-brown gateway with two tall minarets and arches, and a round hut with a thatched straw-coloured roof and pale walls (the book does not name them)",
    "delhi_monuments": "the places the book names in its opener: India Gate, Qutub Minar, Safdarjung Tomb, Akshardham, the National Museum, Jantar Mantar and Sansad Bhawan, drawn as they truly look with no invented building (the book draws only India Gate and Qutub Minar)",
    "street_model": "a small model street on a green base: a grey road, small houses with red, orange and blue roofs, two round brown huts, a lamp post",
    "qutub_minar": "a tall tapering reddish-brown tower with balconies that narrow towards the top, with a few bushes at its foot (it tapers, so no single block fits it exactly)",
    "qutub_model": "a small stepped stack of three green boxes, each smaller than the one below, held by an unnamed boy with dark hair and a light blue top (real boxes keep their own green; the boy has no name in the book, so he is just a child)",
    "bricks": "three solid blocks side by side: a red-brown clay brick, a grey stone block and a brown wooden block (three real materials, so they keep their own colours), all true cuboids with flat faces and square corners, shown from one angle so three faces of each can be seen",
    "diksha": "a girl with a ponytail, a yellow top and a pink skirt (as the book draws her)",
    "isha": "a girl of Diksha's age in simple clothes, drawn in the book's style; the book shows only her hands and straws, so she is given one plain look that stays the same in every video",
    "dikshas_father": "Diksha's father: a grown man in simple clothes, drawn in the book's style; the book names him in words only, so he is given one plain look that stays the same in every video",
    "nitesh": "a boy with dark hair and a light blue t-shirt, cutting a net out of paper with orange scissors",
    "squiggly_and_wiggly": "two black fuzzy spiders with large round eyes and a thin hanging thread; Squiggly makes the triangular web, her brother Wiggly the web of rectangles",
    "box_net": "a pink paper box opened out flat with dotted fold lines, and a line drawing 'Net of a box' with dotted folds; it folds back into the box (a real paper box, kept pink as in the book; a flat net is never in the colour of a solid)",
    "paper_strip_ball": "a ball made of curved orange paper strips joined at the top and bottom, with a small green leaf on top (the craft ball of the first Craft task, a paper craft kept orange as in the book; it is not the sphere of the solids)",
    "solid_colours": "the colour code of the maths solids, one colour per kind of solid in the teaching pictures: prisms blue, pyramids pink, cube teal, cuboid red, sphere coral, cone yellow, cylinder orchid; every solid a shaded 3D solid, with dashed hidden edges where an edge is hidden; in the sorting, matching and riddle stages of the tools every solid is drawn in ONE neutral stone-grey tint (still shaded 3D, so faces and edges show), so that colour never gives the answer; flat shapes in flat colours; a net is never in the colour of its solid; real objects (wooden blocks, bricks, a die, a football, tents, paper boxes) keep their own colours",
    "prisms": "shaded 3D solids, ALL in the one prism blue (as the book draws them), with dashed hidden edges, labelled Triangular Prism, Square Prism (drawn long, like a box with square ends) and Hexagonal Prism; every other prism of the chapter (a pentagonal prism if one is ever drawn) is this same blue; in the sorting stages the same solids use the one neutral tint instead",
    "pyramids": "shaded 3D solids, ALL in the one pyramid pink (the book's pink-magenta), with dashed hidden edges, labelled Triangular Pyramid, Square Pyramid and Pentagonal Pyramid; every other pyramid of the chapter is this same pink; in the sorting stages the same solids use the one neutral tint instead",
    "sphere": "a proper shaded 3D ball with a soft highlight, round from every side, always in the one sphere colour, a coral (a lighter tint of red than the cuboid's deep red, so a sphere and a cuboid on one screen are never alike); never a flat disc; a real ball (a football) keeps its own colours",
    "straws_and_clay": "thin straws joined at their ends by small round clay balls to make the skeleton of a shape; every straw is its own straight line and every ball its own dot, drawn see-through so no edge hides another and every one can be counted: straws are the edges and balls are the corners (cube and cuboid 12 and 8, triangular pyramid 6 and 4, square pyramid 8 and 5, triangular prism 9 and 6; the model-challenge square pyramid beside the last task is 8 straws and 5 balls). In a SOLID skeleton the straws are in the colour of the solid they make (cube teal, cuboid red, every prism blue, every pyramid pink) and every clay ball is one plain clay colour (a warm grey-brown); in a FLAT straw shape (the triangle, rectangle, square and pentagon of the push tools) the straws stay green, yellow, blue or orange as in the book and the balls red or pink, because a flat shape is not one of the solids",
    "die": "a standard grey-white die (a real die, so it keeps its own colour and is not the teal cube): opposite faces always add up to 7 (1 and 6, 2 and 5, 3 and 4), so two faces that add up to 7 are never in view together; the book's picture shows 5, 1 and 3 on its three visible faces and writes numerals, the same die on every screen",
    "colour_cube": "one cube with six differently coloured faces, red, orange, green, purple, dark blue and yellow, shown in three views side by side: (top orange, left red, right green), (top purple, left orange, right green), (top red, left dark blue, right yellow); the six face colours are the question's own data, so this cube is NOT teal; the three views must fit one single cube (red opposite purple, yellow opposite orange, dark blue opposite green)",
    "border_objects": "about twenty pencil sketches round the edge of the Let Us Observe task, in plain pencil outline with grey pencil shading and no colour, so the child's red, blue, smiley and star marks show: 2 dice, 2 erasers, a Rubik's cube, a gift box, 3 balls (one a football), 3 cans or bottles, an ice-cream cone, a party hat, 2 cheese pieces, a pyramid made of small triangles, a double pyramid, a wooden wedge and a cake slice; each is drawn as the book draws it and as itself: every ball a shaded ball, the cone a plain cone with no scoop, a can a cylinder, the wooden wedge and the cake slice triangular prisms, and each cheese piece a pyramid with small holes (never a wedge)",
    "sorting_circles": "round outlines in dark purple-blue on a pale green panel with green italic labels; two panels have two separate circles, one panel has two overlapping circles with a labelled overlap",
    "cube_models": "four models of unit cubes in the book's shapes, A, B, C and D (A a block with one step, B a long L-shape, C a stepped pile, D a stepped model of layers 4 by 4, 3 by 3, 2 by 2 and 1 cube); every unit cube is a shaded teal cube, as every cube of the chapter, so the four models differ in shape only (the book prints them red, purple, yellow and blue with teal, pink and green); every unit cube is drawn with its own edges so the cubes can be counted",
    "cube_towers": "two stacks of unit cubes, every cube a shaded teal cube with clear edges (a light top, a teal left face, a darker right face), the layers told apart by their steps and not by colour: a stepped tower of 4 layers (4 by 4, 3 by 3, 2 by 2 and 1 cube: 16 + 9 + 4 + 1 = 30 cubes, the same shape as model D) and a large plus-shaped tower: a middle column of 6 cubes and four stairs going out from it, each stair with columns of 5, 4, 3, 2 and 1 cubes (6 + 4 × 15 = 66 cubes); the figures show only the outside, so the hidden cubes are counted by reading the layers and columns, with solid layers and no gaps (the book's counts of 30 and 66 assume this); the tower of the cube tower video is a different, smaller tower",
    "triangular_dot_paper": "grey dots in a slanting triangular grid (evenly spaced rows, each row shifted half a step, so any three neighbouring dots make an equal triangle), with one finished cube outline in teal (the cube colour) and two cubes drawn only in dotted lines that run exactly through the dots",
    "solid_pictures": "shaded 3D pictures, each a true solid in the colour of its kind: beside Q1 a coral sphere with a dashed ring, a pink square pyramid with a hidden corner dashed, a yellow cone, a red cuboid, an orchid cylinder, a teal cube and a small blue triangular prism lying on a rectangle face with its two triangle ends clear (the book's small orange solid, read as a triangular prism); beside Q2 a coral sphere, a yellow cone, a pink triangular pyramid, a teal cube and a red cuboid; a sphere is a shaded ball, a cone has one round flat base and one point, a cylinder has two round flat faces and a curved side; when these solids are the riddle cards of the faces, edges and corners tool they are drawn in the one neutral tint so colour cannot give the answer",
    "nets_and_solids": "line drawings of nets with dotted fold lines (violet in Q3: a triangle net, a cylinder net, a cuboid net, a triangular prism net; dark green in Q4: four nets) with a solid beside or below each (in a teaching picture in the colour of its kind: cylinder orchid, cube teal, cuboid red, prisms blue, pyramids pink; in the matching stages of the nets tool every solid is drawn in the one neutral tint); a net is flat and is NEVER in the colour of the solid it folds into, so the colour cannot give the match away; every face of a net is its own flat shape joined to the next along a dotted fold line, so the faces can be counted; Nitesh's pieces are pale orange (one pentagon and five triangles) with four solids a to d below; the nets of Q4 are drawn as printed (A and C do not fold)",
    "angle_mark": "a small red arc at the corner of an angle, or a small red square for a right angle",
    "straws_angle": "two straws, one green and one orange, meeting at one end to show an angle, with a red arc or red square at the corner",
    "yoga_figures": "five simple yoga figures with round heads in blue and orange, each with a red arc where two limbs meet",
    "house_and_boat": "a blue house with a darker blue triangular roof (7 red angle marks) and a boat with a brown hull and a cream sail split by a brown mast into two triangles (10 red angle marks)",
    "right_angle_checker": "a piece of pale orange paper folded twice so the folded corner is a right angle, marked with a red square",
    "dot_grid": "rows of black dots on a white page, or on a pale blue, yellow, peach or pink rounded panel",
    "angle_figures_grid": "eight blue angles drawn on a dot grid in two rows of four; each is two lines meeting at a point",
    "angle_pictures": "five plain pictures: an open pair of scissors, a clothes hanger, a hand making a V sign, a seesaw and a slide; in each the two arms that meet are drawn clearly",
    "angle_letters": "the capital letters V, A and Z in large plain strokes, one angle of each marked in red",
    "stick_figures": "four simple stick people with round faces, whose arms and legs meet at angles",
    "rigid_shapes": "straw shapes joined by red or pink clay balls: a triangle (made by a girl in a pink top on a purple rug), a rectangle of blue straws with a second drawing of it pushed over into a slanted shape, a square, and a pentagon of five equal blue straws with grey-pink clay balls; each clay ball is a joint that lets a shape turn, so a push tilts a four-sided or five-sided shape but never a triangle",
    "four_sided_shapes": "three flat 4-sided shapes: a green shape with a slanted side, a pink slanting shape and an orange diamond (in this chapter a diamond always means one thing: a leaning shape with four equal sides and no right angle; a square turned on its corner is called a square turned on its corner)",
    "equal_straws_circle": "many straws in different colours, all the same length, laid like spokes round a central clay ball so that their ends make a circle; and the same straws with unequal lengths, whose ends do not make a circle",
    "circle_paper": "a round sheet of orange-brown paper with dashed fold lines through the middle (creases); a red circle with the labels Diameter and Radius on a half and a quarter fold",
    "compass_design": "a yellow circle (Step 1), overlapping dotted circles (Step 2), then a six-petal flower made of overlapping circles in blue, green, red and yellow (Step 3)",
    "compass": "a school compass: two arms joined at the top, a sharp metal point on one arm and a pencil on the other; the point stays fixed on the centre and the pencil draws the circle",
    "carpet_design": "a brown carpet with a fringe, a paisley border and an orange circle in the middle holding green and yellow petals around a small blue centre",
    "wheels": "four wheels labelled A to D: a grey car wheel with four oval holes, a large brown wooden spoked wheel, a bicycle wheel with blue spokes and a thin black tyre, and a small dark tyre with a silver rim; each seen straight on so it is a true circle with its centre showing, in the printed sizes (B the largest, then C, then A, and D the smallest)",
    "hidden_shapes": "red outlines drawn over one another: a circle, a cylinder, one upright square, one tilted rectangle (about 2.2 times as long as wide) and two triangles (six shapes); all one red on purpose, so they hide one another; the cylinder here is a line drawing in that red, not the orchid solid",
    "dissection_shapes": "flat coloured shapes: an orange long hexagon, a green square and a pink triangle on the left, and the smaller pieces they are cut into on the right",
    "shape_cards": "six flat cut-out cards from the end of the book: an orange square, a green oval, a brown quarter circle, a light-green semicircle, a blue triangle and a pink circle",
    "spider_webs": "purple threads on white: Squiggly's web is a long shape with 12 walls numbered 1 to 12 in dark red and point A at the bottom tip (the numbers follow one walk from A round to A); Wiggly's web is a set of rectangles with a short bar at the top, point A at the bar's upper right end and point B at the bottom of the second line from the left; these are the figures of the strong structure tool, and the two webs story draws two simple webs of its own instead",
    "matchsticks": "a thin wooden stick with a red head at one end, all the same length, every stick drawn whole so the sticks can be counted: Q2 five loose sticks and a dashed drawing box; Q3 nine sticks as three small triangles in a row that touch at the base corners (the book draws small gaps; here the corners touch, because only then can the puzzle be solved); Q4 thirteen sticks making six small triangles (a big triangle of side 2 with one small triangle on its upper left side and one on its lower right side); all corners meet on one triangular grid",
    "angle_shapes": "flat coloured 2D shapes in Q6: a blue square, a red triangle, a green slanting 4-sided shape, a purple right triangle, a purple pentagon, a thin green triangle and a red rectangle",
    "right_angle_figures": "six flat coloured figures in Q8 in a row: a blue rectangle, a green slanting 4-sided shape, a purple triangle, an orange 4-sided shape wider at the top, a purple slanting 4-sided shape and a red tilted rectangle (a little longer than wide, as the book draws it: a rectangle, not a square); every corner drawn true",
    "shape_gallery": "fourteen flat coloured shapes numbered 1 to 14 in Q9 in three rows, mostly 4-sided (squares, rectangles and slanting shapes) with one dart-shaped number 1; every corner drawn true so right, acute and obtuse angles can be told apart",
    # ---- the image (added by the media step, CLASH 43): the plan's own real-life examples, not in the book
    "prism_tent": "a real camping tent with two matching triangle ends and three rectangle faces (two slanting sides and the floor), straight edges, as a clean shaded illustration standing on grass; one plain tent colour, the same as the pyramid tent, so colour is no clue (not the prism blue); the face shapes are marked with light outlines, never counted or named",
    "pyramid_tent": "a real tent with a square floor and four triangle faces that meet at one point at the top, straight edges, as a clean shaded illustration standing on grass beside the prism tent; the same plain tent colour as the prism tent (not the pyramid pink); the face shapes are marked with light outlines, one marking for triangles on both tents, never counted or named",
}

# ---------------------------------------------------------------------------
# how this chapter is taught (shown once with the plan)
# ---------------------------------------------------------------------------
CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "Each lesson has a story or a picture, then small tools you use yourself. "
             "Lesson 9 revises the chapter with a quiz, a worksheet and a sample assessment. "
             "A closing look back ends the chapter.",
    "points": [
        {"title": "Stories with a problem",
         "text": "Diksha, her father, Isha, Nitesh, Squiggly and Wiggly meet a real problem. A story names the idea, "
                 "but it never gives away what you find out yourself."},
        {"title": "You do it first",
         "text": "In the tools you build, fold, push, count and draw. Most tools show at once whether your try is right. "
                 "The sample assessment shows its answers when you finish each section."},
        {"title": "Questions from your maths book",
         "text": "Your maths book's questions sit inside the tool they belong to. "
                 "Other tools have practice made for this chapter."},
        {"title": "No timer, no score",
         "text": "Nothing is timed, scored or counted as a win. You get hints, you can try again and you can start over."},
        {"title": "Clear, true pictures",
         "text": "A solid always looks like a solid. Each kind of solid keeps one colour. In sorting and matching games "
                 "every solid is the same grey, so colour gives no clue."},
        {"title": "Shapes in real life",
         "text": "Buildings, tents, wheels and spider webs show where shapes hide around us."},
        {"title": "Revision and a look back",
         "text": "Lesson 9 has a recap story, a picture quiz, a worksheet and a sample assessment. "
                 "Then a short look back shows earlier ideas again. Nothing new is taught there."},
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
# 1 example + 59 exercise + 49 prompt = 109 NCERT questions; 5 talk; 17 text. Ids are the SAME as in the previous build
# (maths4_ch1_prev_v4) so the two can be compared; every item was re-read against its page image for this rebuild. The
# book prints no answers. The printed page number equals the pdf page number for every page of this chapter (the opener,
# page 1, carries no printed number). The nets (Craft 2) and the six 2D cards (Card Game) are at the end of the book and
# are not items of their own.
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
#
# The first 21 ids are the same as in the previous build; M_SH_8, M_SH_9, M_AN_8 and M_AN_9 are new for the rebuild (they
# come from the new lesson plan's wording: the apex, spinning a die, the regular pentagon, the rigid triangle).
MISCONCEPTIONS = [
    ("M_SH_1", "A cube is not a prism, because a prism must be a long shape with a triangle or a rectangle at its ends."),
    ("M_SH_2", "Any solid with a triangular face is a pyramid, so a triangular prism is a pyramid."),
    ("M_SH_3", "A face is only a flat side, so a cone, a cylinder or a sphere has no face at all."),
    ("M_SH_4", "A corner and an edge are the same thing, or a curved line cannot be an edge."),
    ("M_SH_5", "The face opposite a face is any face next to it, so opposite faces and faces that touch are mixed up."),
    ("M_SH_6", "The number of cubes in a tower is the number of cubes you can see, so hidden cubes do not count."),
    ("M_SH_7", "Any flat pattern of faces is a net, so any six joined squares will fold into a box."),
    ("M_SH_8", "All the corners of a pyramid meet at its top point, so every corner of a pyramid is the apex."),
    ("M_SH_9", "You can see all six faces of a cube at the same time if you turn it the right way."),
    ("M_AN_1", "An angle is only a corner of a drawn shape, so scissors, a seesaw or a yoga pose has no angle."),
    ("M_AN_2", "A bigger angle is one with longer arms, so making the lines longer makes the angle larger."),
    ("M_AN_3", "A right angle must look like an upright L, so a tilted corner, such as a turned square, is not a right angle."),
    ("M_AN_4", "An obtuse angle is any angle that looks big and an acute angle is any that looks small, with no check against a right angle."),
    ("M_AN_5", "A rectangle keeps its shape and its right angles when it is pushed, just as a triangle does."),
    ("M_AN_6", "A square is not a rectangle, because the two look different."),
    ("M_AN_7", "The number of angles of a shape can be different from its number of sides."),
    ("M_AN_8", "A pentagon with all sides equal must also have all its angles equal, so it cannot change when it is pushed."),
    ("M_AN_9", "A triangle of straws leans over when you push a side, just as a rectangle does."),
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
    # --- written by the tool mapper (step 2), rebuild from zero on the user's 9-lesson plan, 6 Nov 2026. ---
    # The twelve tools (names, purposes, order) are the content team's table and are NOT changed by any clash below:
    # every clash is a question for the user. Clashes 1 to 4 carry the user's own decisions of 6 Nov 2026 ("DECIDED BY
    # THE USER"). Clashes 5 to 14 are the proposer's ten open questions (tool_proposal.md section 8), 15 to 19 its
    # misfits (section 4), 20 to 38 are the mapper's checks. Numbers follow that order.

    "CLASH 1, the tool structure. "
    "DECIDED BY THE USER (6 Nov 2026): the lesson plan becomes tools, with the plan's activities as the tool's stages "
    "(first one tool per lesson); because the book questions overload that, 'about 11 tools, cap 13': Lessons 2, 3, 4 "
    "and 5 get one tool each (Tools 3, 4, 5, 6) and Lessons 1, 6, 7 and 8 get two each (Tools 1 and 2, 7 and 8, 9 and "
    "10, 11 and 12). That came to 12 tools, and max_tool_questions is 13 for this chapter (the default is 6). "
    "Lesson 9 has no tool: it is the review (rows 27 and 28). "
    "PLAN SAYS: 8 lessons with 23 activities, a 9th lesson of revision and a 10-mark assessment. "
    "BOOK SAYS: 109 questions and 22 text or talk items on 23 pages, no end exercise. "
    "OPTIONS: none, decided. RECOMMENDATION: none. The open question about 12 against 'about 11' is CLASH 5. "
    "core/tool_map.py verify printed a match, so the table is unchanged.",

    "CLASH 2, plan items that break the pipeline rules. "
    "DECIDED BY THE USER (6 Nov 2026): they are ADJUSTED, not kept. (1) Degrees (45, 90, 120, 30, 110, 150, 'smaller than "
    "180', 'show the angle measurement', assessment Q2 and Q8) become 'smaller than, equal to, bigger than a right angle'; "
    "the arm of Tool 7 shows a right-angle corner and no number. (2) Beat the Clock (5 seconds, a point per answer, a "
    "final score) becomes 'Identify the Angle' (Tool 8, stage 2): no timer, no points, three options, feedback after "
    "each answer. (3) The regular pentagon with equal angles and the regular or irregular comparison become the book's "
    "'5-sided shape with all sides equal'; the comparison is the push test, the angles change (Tool 10). (4) The "
    "10-mark, 20-minute assessment becomes an unscored recap inside the two review concepts, with no book question "
    "(CLASH 11). (5) The radius and diameter sums in cm (3, 10, 7, 6 cm) become the book's relation: fold a circle in "
    "half and in half again, the diameter is double the radius; wheels are compared without numbers (Tool 9). (6) The "
    "True or False quiz becomes 'Strong or wobbly' picture practice with the book's own frames (Tool 12); the false "
    "statement 'a triangle has four sides' is dropped. (7) Words outside the book: vertex becomes corner, polygon "
    "becomes n-sided shape, slanted quadrilateral becomes slanted four-sided shape, diagonal becomes 'a stick across "
    "the corners', 'regular' is dropped (CLASH 9). (8) Teacher voice ('I will explain') and slide-style videos become "
    "short stories (CLASH 4). (9) Third-party image links are references only (CLASH 31). "
    "ALSO ADJUSTED BY THE PROPOSER, FOR CONFIRMATION: Shape Detective's 30 seconds is dropped (same rule as the clock); "
    "'Count and Win' is the stage 'Count the parts' (win is a score word); 'arrange blocks to create a square-based "
    "pyramid' is built from its five faces, because cubes only make a stepped pile; 'build a cube from smaller unit "
    "cubes' is 8 unit cubes (CLASH 8); Find the Wrong Net is built on the book's four nets and four solids, and any new "
    "net is checked by folding. "
    "RECOMMENDATION: confirm the proposer's four extra adjustments; the nine above need nothing.",

    "CLASH 3, the book parts the plan does not mention. "
    "DECIDED BY THE USER (6 Nov 2026): they are FOLDED into the nearest lesson's tool as extra stages and questions. "
    "Where they went (tool: items, ids without 'ch1.'): Tool 1: model1, model_q1 to q5, project1, qutub_q1 to q3, "
    "puzzle1. Tool 2: bricks_q, border1 to border4, cards, puzzle2 to puzzle4. Tool 3: craft1, prism_q1 to q3, pyr_q1 to "
    "q3, cube_prism, sort1, sort3, sort3_q, sort4. Tool 4: craft2, solids_q3 to q5. Tool 5: craft3, fve, sort_faces, "
    "three_faces, sort_edges, sort2, observe1 to observe3, border5, solids_q1, try5. Tool 6: build1, towers, dotcubes. "
    "Tool 7: house_ex, boat_q, angles_do1, angles_do2, right_make, right_circle, right_objects, right_do1, try8, "
    "try8_q. Tool 8: acute_obj, obtuse_obj, letters, ao_do1a, ao_do1b, ao_do2, dotshapes, dotshapes_q, fourside_q, "
    "try9. Tool 9: circle_straws, circle_straws_q1, q2, make_circle, make_circle_q, amazing1, amazing_q1, amazing_q4, "
    "circ_do1, compass, carpet, wheels_q0, wheels_q1. Tool 10: pentagon_make, pentagon_q1 to q3, try6, try6_q, try7a, "
    "try7b. Tool 11: straw_tri_make to straw_compare (10). Tool 12: try1a to try1d, try2, try3, try4. Counts 11, 9, 12, "
    "4, 12, 3, 10, 10, 13, 8, 10, 7 = 109, each question on exactly one tool, none missing (checked by script against "
    "NCERT_ITEMS). The 22 text and talk items ride with the media of their concept (tool_proposal.md section 3). "
    "Items that moved away from the analyst's concept (so the question mapper homes them on the tool's one concept): "
    "bricks_q (C1) to Tool 2; border1 to border4, sort1 to sort4 (C5) across Tools 2, 3 and 5; craft2 (C2) to Tool 4; "
    "solids_q1 (C8), try5 (C23) and border5 to Tool 5; cards (C20) and puzzle2 to puzzle4 (C19) to Tool 2; try8 and "
    "try8_q (C24) to Tool 7; try9 (C24) and dotshapes, dotshapes_q, fourside_q (C14) to Tool 8; try6, try6_q, try7a, "
    "try7b (C24) to Tool 10; try1a to try1d (C21) and try2 to try4 (C22) to Tool 12. "
    "OPTIONS: none, decided. RECOMMENDATION: none; the strain it causes is CLASHES 7, 13, 15 to 19, 20 and 23."
    " QUESTION MAPPER (step 5): every home listed here was checked item by item against the 23 page images and is KEPT: 109 "
    "questions (1 example, 59 exercises, 49 prompts), each on exactly one tool concept (checked by program against "
    "NCERT_ITEMS: none missing, none twice, every kind matches), per tool 11, 9, 12, 4, 12, 3, 10, 10, 13, 8, 10, 7. "
    "Nothing is excluded, because every item is printed in this chapter, and nothing was moved to stay within the cap. The "
    "22 text and talk items are each in `ncert` of one teaching concept (checked by program).",

    "CLASH 4, how the videos are written. "
    "DECIDED BY THE USER (6 Nov 2026): videos are stories with a problem, not slide lectures. "
    "PLAN SAYS: 'Video Format: Animated Slide Presentation', 'I will explain', 'Create a video-style script ...'. "
    "BOOK SAYS: Diksha, her father, Isha, Nitesh, Squiggly and Wiggly are the only story cast. "
    "So the hook and the 11 concept videos (rows 3, 5, 6, 9, 11, 13, 15, 17, 19, 23, 25) are short stories of that cast "
    "(a hidden block with clues, a gift box opened out, a cube tower counted by layers, straws and a paper corner, a peg "
    "and string circle, Squiggly's and Wiggly's webs). Each has ONE new_idea and ends in the tool; the plan's lists of "
    "facts (counts, definitions) are carried by the story's problem and by the tool's feedback. "
    "OPTIONS: none, decided. RECOMMENDATION: none. Open points about the stories: the claim in the row 25 video "
    "(CLASH 22) and the cast (CLASH 37).",

    "CLASH 5, the number of tools: 12, not 'about 11' (proposer's open question 1). "
    "PLAN SAYS: the user said 'about 11 tools, cap 13'. The rule 'Lessons 2 to 5 one tool each, Lessons 1, 6, 7, 8 two "
    "each' gives 12 (4 + 8). BOOK SAYS: nothing about tools. "
    "OPTIONS: (a) 12 as built; (b) 11 by joining two tools, for example Tools 11 and 12 (Lesson 8), which changes both "
    "approved purposes and would put 17 questions on one tool, over the cap; (c) 13 by adding a third Lesson 7 tool "
    "(Tool 9 would drop to 8 questions). "
    "RECOMMENDATION: (a). Joining or adding a tool changes the approved table, so it is the user's call and not "
    "the mapper's.",

    "CLASH 6, Lesson 1 needs two topics (proposer's open question 2). "
    "PLAN SAYS: one topic per lesson. BOOK SAYS: nothing. GATE SAYS: the opening topic must be exactly [hook video, "
    "exploration tool] (flow_c34 _check_shape). Lesson 1 has the hook, Tool 1 and a second activity with its own video "
    "and Tool 2, so Topic 1 holds [hook, Tool 1] and Topic 2 (Guess the Shape) holds [concept video, Tool 2]. This is the "
    "only place where 'one topic per lesson' bends: 10 topics for 9 lessons. "
    "OPTIONS: (a) two topics as in the table; (b) put the row 3 video and Tool 2 inside the opening (the gate forbids); "
    "(c) move Guess the Shape into Lesson 2's topic (that topic would then hold two lessons' content). "
    "RECOMMENDATION: (a).",

    "CLASH 7, how many book questions each tool holds (proposer's open question 3). "
    "PLAN SAYS: cap 13 for this chapter. BOOK SAYS: 109 questions. TOOL_SPEC_GUIDE says a tool with more than 6 "
    "questions is doing too much and must be raised as a clash. The counts are Tool 1: 11, Tool 2: 9, Tool 3: 12, Tool "
    "4: 4, Tool 5: 12, Tool 6: 3, Tool 7: 10, Tool 8: 10, Tool 9: 13 (exactly the cap), Tool 10: 8, Tool 11: 10, Tool 12: "
    "7. Ten of the twelve tools are over the default of 6. Even a perfect spread of 109 over 12 tools is 9 per tool. "
    "Tools 3 and 5 are one question under the cap, so no later step may add a question to Tools 3, 5 or 9. "
    "OPTIONS: (a) accept the cap of 13 as decided; (b) move items (sort1 and sort4 to Tool 5 makes it 14, over; the "
    "dot-grid and angle-count items to the review, which the gate forbids); (c) a third Lesson 7 tool (CLASH 5). "
    "RECOMMENDATION: (a). Each tool shows its book questions as the last stage, a few at a time."
    " QUESTION MAPPER: the counts are confirmed. No tool is over 13; Tool 9 is at 13 and Tools 3 and 5 at 12, so nothing may "
    "be added to them. The exploration tool T1.C2 holds 11 book questions (CLASH 25). The gate (flow_c34 _check_questions) "
    "bars book questions only on a hook, on a review, and on a story or image concept that a tool applies to; every "
    "question sits on a tool concept, so none needed to move and no new clash comes from the cap.",

    "CLASH 8, the cube net and the cube of unit cubes (proposer's open question 4). "
    "PLAN SAYS: Fold It starts from 'the net of a cube' and Which Net says 'six connected squares make a cube'; "
    "Lesson 2 challenge 3 is 'build a cube using smaller unit cubes' with no size. BOOK SAYS: no cube net anywhere, "
    "neither in the 23 pages nor on the end pages (those hold the nets of a triangular prism, a rectangular prism or "
    "cuboid, a triangular pyramid, a hexagonal prism, a square pyramid and a pentagonal pyramid); the cuboid net "
    "appears on p9 Q3 (3) and Q4 D. The book builds models A to D, none a cube. A cube has 11 nets, and most arrangements "
    "of six squares (a row of six, a block of 2 by 3) do not fold. "
    "OPTIONS: (a) draw one cube net, the cross of six squares, as a figure, never the bare sentence 'six squares make "
    "a cube'; build the cube as 2 by 2 by 2 (8 unit cubes); (b) use only the book's nets and no cube net; (c) a 3 by 3 "
    "by 3 cube of 27. "
    "RECOMMENDATION: (a) with 8 unit cubes. Any new wrong net for Find the Wrong Net is checked by folding.",

    "CLASH 9, words the book does not use (proposer's open question 5). "
    "PLAN SAYS: vertex, 'corner (vertex)', apex, polygon, regular, diagonal, rigid, quadrilateral, base, 'face is a flat "
    "surface'. BOOK SAYS: corner(s) and the letter V ('Number of corners (V)', p4); apex never; polygon never; diagonal "
    "never; 'rigid' and 'rigidity' only in a teacher's note (E29); 'base' only for a building; 'face' from p3 on, "
    "undefined, and with curved faces (p8: a cone has 1 flat and 1 curved face). "
    "OPTIONS: (a) 'corner' only, and no apex; (b) 'corner' with 'vertex' as a second name once, keep apex and rigid; (c) "
    "the plan's words everywhere. "
    "RECOMMENDATION: (b) in this form: corner is the word; vertex at most once as a second name (never in a tool "
    "label); keep apex (the book asks 'all the triangular faces meet at ___ point') and rigid (the lesson's name); "
    "'a stick across the corners', not diagonal; n-sided shape, not polygon; 'face' is a flat or curved side of a solid, "
    "not 'a flat surface only'; for a prism say 'the two end faces', for a pyramid 'the bottom face (base)'.",

    "CLASH 10, 2D versus 3D has no lesson (proposer's open question 6). "
    "PLAN SAYS: objective 2, 'understand the difference between 2D and 3D shapes', but no lesson teaches it. BOOK SAYS: "
    "'3D shapes' five times (p4, p6) and '2D shapes' three times (p20, p23), never defined. "
    "OPTIONS: (a) one light line in the row 3 story (a flat shape has sides and corners, a solid has faces); Tool 2 "
    "already sorts real objects (solids) and flat shape cards, which shows it; (b) leave it to the pictures; (c) a "
    "video of its own (not in the approved table). "
    "RECOMMENDATION: (a), as a story line and not a definition.",

    "CLASH 11, the review (proposer's open question 7). "
    "PLAN SAYS: Lesson 9 is revision slides, a shape-identification visual quiz, a digital worksheet and a 10-mark "
    "assessment of 8 questions. TABLE SAYS: two review rows (rows 27 and 28), unscored, reusing earlier visuals, no new "
    "tool, no book question. GATE SAYS (flow_c34 _check_review): at most 2 review concepts; each lists the earlier "
    "concepts it revises (review_covers); no new key term; no book item; no new video or tool; every idea topic must "
    "have at least one concept revised (so the Topic 2 concept, Guess the Shape, must appear in row 27 or row 28). "
    "The 8 assessment questions are the plan's own, not book questions. "
    "OPTIONS: (a) reuse the plan's assessment ideas reworded as recap lines with picture feedback (no degrees, cm, "
    "polygon or vertex); (b) recap lines made only from teaching already given; (c) no recap lines. "
    "RECOMMENDATION: (a). The digital worksheet has no slot (CLASH 33).",

    "CLASH 12, the answers the book does not print (proposer's open question 8). "
    "BOOK SAYS: no answers at all. The analyst's readings of the printed figures (analysis.md Appendix A, 'mine') need "
    "the content team's or the user's sign-off: tower 1 = 30 and tower 2 = 66 (both assume solid layers with no extra "
    "hidden cube, E27); the house 7 and the boat 10 marks (E8); the matchstick figures (Q3: 9 sticks, only solvable if "
    "the three triangles touch at their base corners, E20; Q4: 13 sticks); nets A and C do not fold and B and D do "
    "(E1); p9 Q3 matches (1)-b, (2)-d, (3)-a, (4)-c and Q5 is a pentagonal pyramid; p8 Q1 a to f (f is a cube or a "
    "cuboid, E5); the coloured cube (red opposite purple, yellow opposite orange, blue opposite green); F, V, E of the "
    "five solids; the right angles of the p11 dot grid (E9); the wheels (B longest, D shortest, E16); the six hidden "
    "shapes (E17); the web counts (10 triangles, 12 rectangles); p22 Q5, Q6 and p23 Q8, Q9 (E22, E23). Every plan-made "
    "answer is labelled 'From the picture' or 'Sample answer'. "
    "THE WALK QUESTIONS (E19) HAVE TWO READINGS. 'Every wall': Squiggly's printed numbers 1 to 12 already trace a closed "
    "walk over all 12 walls (yes), and no walk over every wall of Wiggly's web exists from A to B (no, two corners have "
    "an odd number of walls). 'Any path without using a wall twice': both are trivially yes. "
    "OPTIONS: (a) the 'every wall' reading, because the story says each spider walks to check its walls; (b) 'any "
    "path'. RECOMMENDATION: (a); the user or content team signs off Appendix A before the briefs."
    " QUESTION MAPPER: the solved results of Appendix A are written as answers, each beginning 'From the picture' or 'Sample "
    "answer', and each re-checked by me: towers 30 and 66 (both with the no-gap assumption, E27); nets A to D (B and D "
    "fold, A and C do not); the matchstick solutions of p22 Q3 and Q4 (re-checked by program: Q3 gives 4 triangles after "
    "moving 2 sticks only if the three triangles touch at their base corners; of the 715 ways to remove 4 sticks from Q4, "
    "128 leave exactly 3 triangles, and the answer gives one that leaves no stray stick); the boat (10 marked angles); the "
    "coloured cube (red opposite purple, yellow opposite orange, derived again from the three views including the way the "
    "faces turn round a corner); the right angles of the dot grid; the shapes of p23 Q8 and Q9 (re-measured); the wheels "
    "(B, C, A, D, outer sizes 665, 604, 515 and 440 on a 6x render); the webs (10 triangles, 12 rectangles, and Squiggly's "
    "printed numbers 1 to 12 trace one closed walk). THE WALKS: ch1.try1b says yes (both readings agree). ch1.try1d is "
    "written on the recommended 'every wall' reading: no, because two corners of Wiggly's web have 3 walls each; one more "
    "line gives the other reading (if he may skip walls he can go from A to B). So the user's choice (a) or (b) changes "
    "only that one answer. Where the book allows many answers (the letter A, the four stick figures, the cuts, the cards, "
    "the border sketches, the clues of p23 Q9) the answer gives no total or lists every fit and says so. SOLUTION_NOTES has "
    "how each result was checked.",

    "CLASH 13, Tools 2 and 12 each run four short stages (proposer's open question 9). "
    "PLAN SAYS: Tool 2 (Lesson 1, Activity 2) is one three-clue guess, and Tool 12 (Lesson 8, Activities 2 and 3) a stick "
    "across a frame and a quiz. BOOK SAYS: Tool 2 also gets the objects and bricks (bricks_q, border1 to border4), the "
    "flat cards (cards) and the cuts (puzzle2 to puzzle4); Tool 12 gets the webs (try1a to try1d) and the matchsticks "
    "(try2 to try4). So Tool 2 = three clues, sort objects, sort flat cards, cut shapes; Tool 12 = a stick across the "
    "frame, strong or wobbly, webs, matchsticks. "
    "OPTIONS: (a) accept, one stage on screen at a time; (b) move the cuts (Tool 2) to Tool 1 (14 questions, over the cap) "
    "or to Tool 12 (10), and the webs (Tool 12) to Tool 11 (14, over the cap), which changes the approved purposes. "
    "RECOMMENDATION: (a)."
    " QUESTION MAPPER: Tool 2's nine questions are listed in the tool's stage order (bricks, border objects, flat cards, "
    "cuts), so ch1.cards comes before ch1.puzzle2 to ch1.puzzle4, which the book prints the other way round; the child "
    "meets the flat cards before the cuts.",

    "CLASH 14, the pentagon is pushed before the rigidity lesson (proposer's open question 10; an order clash). "
    "PLAN SAYS: Lesson 7 builds a pentagon and pushes it (Tool 10); Lesson 8 teaches rigidity (Tools 11 and 12). BOOK "
    "SAYS: the push of the triangle, the rectangle and the square (p14) comes first, the pentagon's push question "
    "(p16, 'does the shape of the pentagon change if we gently push one of its sides') builds on it. "
    "OPTIONS: (a) accept: the pentagon image and Tool 10 teach the push on the pentagon first (its angles change), "
    "and the row 23 rigid video recalls it; (b) move Tool 10 after Tool 11 (reorders the approved tools: not allowed "
    "here); (c) keep only 'count the sides and corners' in Tool 10 and move the push to Tool 11 (changes both "
    "approved purposes). "
    "RECOMMENDATION: (a).",

    "CLASH 15, curved solids in the prisms and pyramids tool (Tool 3; a misfit). "
    "PLAN SAYS: Lesson 2 is prisms and pyramids and the cube only. BOOK SAYS: craft1 (a ball from paper strips), sort1 "
    "(all faces look the same or not) and sort4 (curved or flat faces) use the sphere, cone and cylinder, which are "
    "neither prisms nor pyramids. "
    "OPTIONS: (a) keep them in Tool 3 as 'not every solid is a prism or a pyramid'; (b) move them to Tool 5, which "
    "already holds 12 and would reach 15 (over the cap). "
    "RECOMMENDATION: (a). The solids are drawn as shaded 3D solids (CLASH 34)."
    " QUESTION MAPPER: craft1, sort1 and sort4 stay on Tool 3. Their answers name the curved solids and say that the cone "
    "and the cylinder have both flat and curved faces (the overlap of sort4), which is the 'not every solid is a prism or a "
    "pyramid' idea. The set of solids to sort is CLASH 52.",

    "CLASH 16, the cuts in the shape-guessing tool (Tool 2; a misfit). "
    "PLAN SAYS: Tool 2's approved purpose includes 'cuts shapes into smaller shapes'. BOOK SAYS: puzzle2 (divide a "
    "triangle into 1 square and 2 triangles with 2 lines), puzzle3 (a square into 3 triangles with 2 lines) and puzzle4 "
    "(cuts A, B, C) are about shapes inside shapes, not clues about sides, corners and faces. The cut lines are not "
    "unique (E17). "
    "OPTIONS: (a) keep them in Tool 2 as its last stage (the approved purpose names them); (b) Tool 1 (hidden shapes, "
    "but 14 questions, over the cap); (c) Tool 12 (triangles, 10 questions). "
    "RECOMMENDATION: (a). Every cut answer is a 'Sample answer'."
    " QUESTION MAPPER: puzzle2 and puzzle3 give the dot-grid cuts of Appendix A as Sample answers. puzzle4 gives one cut for "
    "each of A (two cuts), B (three cuts) and C (three corner cuts), all Sample answers ending 'Your answer may differ', "
    "because the cut lines are not unique (E17).",

    "CLASH 17, the walk puzzles in the strong-structure tool (Tool 12; a misfit). "
    "BOOK SAYS: try1b (can Squiggly start at A and come back to A without using a wall twice) and try1d (can Wiggly go "
    "from A to B) are about paths, not rigidity. They are tied to the same story as try1a and try1c (the number of "
    "triangles and rectangles in the webs) and to 'checking if the walls are strong'. "
    "OPTIONS: (a) keep them in Tool 12 as part of the webs stage; (b) no better home: the review may carry no book "
    "item and the other tools are full or unrelated; (c) drop them (leaves two book questions uncovered). "
    "RECOMMENDATION: (a). The reading of the question is CLASH 12."
    " QUESTION MAPPER: try1b (yes) and try1d (no on the 'every wall' reading, with the other reading in one line) are "
    "written as in CLASH 12. They stay on Tool 12 with try1a and try1c.",

    "CLASH 18, angle-counting items in the pentagon tool (Tool 10; a misfit). "
    "PLAN SAYS: Tool 10's approved purpose ends 'compares shapes with three, four and five angles'. BOOK SAYS: try6 "
    "(classify seven shapes by 3, 4 or 5 angles), try6_q (sides against angles), try7a and try7b (draw a shape with "
    "fewer or more than 5 angles) are about the number of angles of any shape, not the pentagon's push. "
    "OPTIONS: (a) keep them in Tool 10, the pentagon being the five-angle case; (b) Tool 8 (14, over the cap); (c) "
    "Tool 7 (14, over the cap). RECOMMENDATION: (a)."
    " QUESTION MAPPER: try6 and try6_q are answered from the picture (3 angles: b, d, f; 4 angles: a, c, g; 5 angles: e; the "
    "number of angles is the number of sides). try7a and try7b are Sample answers (a triangle or a square; a 6-sided "
    "shape). No answer says 'regular' or 'equal angles' (CLASH 2).",

    "CLASH 19, try5 (c) is a solid the chapter never shows (Tool 5; a misfit, E21). "
    "BOOK SAYS: 'a model of a solid with 15 straws and 10 clay balls' is a pentagonal prism, which the chapter never "
    "draws (it shows triangular, square and hexagonal prisms and a pentagonal pyramid). Parts (a) 12 and 8 (cube or "
    "cuboid), (b) 9 and 6 (triangular prism) and (d) 10 and 6 (pentagonal pyramid) are solids of the chapter. "
    "OPTIONS: (a) keep it: the child builds it from the counts, a prism with pentagon ends, and the answer is "
    "a 'Sample answer'; (b) show (c) as a hint-only extra; (c) leave (c) out (one book part uncovered). "
    "RECOMMENDATION: (a)."
    " QUESTION MAPPER: the answer to try5 c) says 'a prism with two 5-sided ends' and does not name it a pentagonal prism, "
    "as in the previous build; its working shows 5 + 5 = 10 and 10 + 5 = 15 straws and 5 + 5 = 10 balls. Parts a), b) and "
    "d) are the cube or cuboid, the triangular prism and the pentagonal pyramid.",

    "CLASH 20, tools that carry more than one analysis concept (which leads, which follow). "
    "TABLE SAYS: each tool has one purpose. BOOK SAYS: the analyst's 24 concepts are finer than the 12 tools. The lead "
    "names the tool and its objective; the others are stages, and the question mapper homes all of a tool's items on "
    "the tool's one concept. Tool 1: C1 leads, C19 hidden shapes (puzzle1) is stage 2. Tool 2: CLASH 21. Tool 3: C2 "
    "(prisms and pyramids) leads, C5 sorting by faces follows; the net half of C2 goes to Tool 4. Tool 4: C9 leads, C2 "
    "(craft2) is stage 1. Tool 5: C3 leads; C4 (die, coloured cube), C5 (sort2, border5), C8 (riddles) and C23 (straw "
    "model) follow. Tool 6: C6 and C7, the plan's own pair (Lesson 5 is 'Cube Towers and Geometrical Drawings'), C6 "
    "leads. Tool 7: C10 and C11, the plan's own pair (one video teaches the angle and the right angle), C10 leads, "
    "C24 (try8, try8_q) closes it. Tool 8: C12 leads, C14 and C24 (try9) follow. Tool 9: C16, C17 and C18, three circle "
    "concepts in one tool (the plan has one circle video and two activities): C16 (make a circle, centre, radius) leads, "
    "C17 (diameter by folding) and C18 (double, compass, carpet, wheels) follow. Tool 10: C15 leads, C24 follows. Tool "
    "11: C13 only. Tool 12: CLASH 22. "
    "OPTIONS: (a) accept; (b) one tool per analysis concept (24 tools, not the approved table). "
    "RECOMMENDATION: (a).",

    "CLASH 21, Tool 2 (Guess the Shape) has no one book concept. "
    "PLAN SAYS: Lesson 1, Activity 2, three clues and the answer Square (four equal sides, four corners, a chessboard "
    "has many of my smaller forms); the approved purpose adds sorting objects and flat cards by sides, corners and "
    "faces, and cuts. BOOK SAYS: no concept is 'telling shapes apart by their sides, corners and faces'. The nearest are "
    "C20 (sort the six 2D cards by their sides), the border questions of C5 (colour shapes with a rectangular face, a "
    "triangular face, a curved face or no corner), bricks_q of C1 (what is common to the bricks) and the book's clue "
    "form ('I have 5 faces and 5 corners', p8 Q1; p23 Q9). The three-clue guess has no book question of its own. The "
    "first two clues also fit a diamond (a shape of p15), so the answer opens only after clue 3. "
    "OPTIONS: (a) name the concept 'telling shapes apart by their sides, corners and faces', C20 leading, the rest "
    "stages; (b) let C5 (the border questions, 4 of 9) lead. RECOMMENDATION: (a).",

    "CLASH 22, Tool 12 (Build a Strong Structure): its concept is the plan's, its book items are puzzles. "
    "PLAN SAYS: Lesson 8, Activity 2, build a square frame, add a diagonal, compare the stability. BOOK SAYS: no task adds "
    "a stick across a frame; 'strong' appears only in try1_text ('check if the walls of her web are strong') and a "
    "teacher's note. All seven items (try1a to try1d, try2 to try4) are puzzles (C21 webs, C22 matchsticks); try2 "
    "(5 sticks, 2 triangles) is a four-sided frame with a stick across, the one place where plan and book meet. The row "
    "25 story says Squiggly's triangle web holds firm and Wiggly's rectangle web wobbles until a thread goes across: "
    "geometrically true (a frame of triangles cannot change shape, a rectangle frame can) but the wobble is the "
    "table's invention, not the book's. "
    "OPTIONS: (a) the concept is the plan's 'a stick across a frame makes it firm', a step on from C13, with C21 and C22 "
    "as stages; (b) the concept is the book's puzzle pair and the stick is a stage. "
    "RECOMMENDATION: (a); the user confirms the row 25 story claim.",

    "CLASH 23, 'one tool, one purpose' under three or four stages. "
    "FLOW RULE SAYS: each tool has one clear learning objective, simple controls, a short interaction path, and is not "
    "'a collection of unrelated activities'. GATES CHECK (flow_c34 _check_tools): at most 4 controls per tool (not per "
    "stage), an instruction of at most 15 words, an objective of at most 25 words with no ';', 1 to 13 book questions "
    "and at most 3 notice prompts, a hint ladder of 0 or 4 rungs, one tool and no video in a tool concept. NOTHING "
    "counts stages or judges 'one purpose'; that is for the checklist validator and the user. Stages per tool: Tool 1: "
    "2; Tool 2: 4; Tool 3: 3; Tool 4: 3; Tool 5: 3; Tool 6: 3; Tool 7: 3; Tool 8: 3; Tool 9: 3; Tool 10: 1 with 4 steps; "
    "Tool 11: 2; Tool 12: 4. "
    "OPTIONS: (a) accept: one stage on screen at a time, the same four controls shared across stages (drag, tap, "
    "Next, Reset), the NCERT Challenge always last; (b) split a tool (changes the approved table). "
    "RECOMMENDATION: (a).",

    "CLASH 24, stage interactions the plan makes up against 'questions are the book's'. "
    "CLAUDE.MD AND TOOL_SPEC_GUIDE SAY: a tool carries only the book's questions of its concept (plus up to 3 notice "
    "prompts on the exploration tool). The user's decision (CLASH 1) turns the plan's activities into stages, and some "
    "ask the child things with plan-made answers: Tool 2 'Three clues'; Tool 3 'Match' and 'Prism or Pyramid'; Tool 4 "
    "'Fold the net' and 'Find the wrong net'; Tool 5 'Label' and 'Count the parts'; Tool 6 'Build a cube tower' (three "
    "cubes, two at the bottom and one on top, six cubes) and 'Look carefully' (four answer options); Tool 7 and Tool 8 "
    "(make an angle, sort six angles, 'Identify the Angle' with three options); Tool 9 'Label the parts'; Tool 12 'Strong "
    "or wobbly'. flow_c34 counts only 'notice' and 'ncert' items in a tool's question_map, so the plan passes. "
    "OPTIONS: (a) treat the stages as the tool's interaction, like the notice prompts: not book questions, not in the "
    "cap, no score, every answer labelled 'From the picture' or 'Sample answer', the book questions last; (b) drop the "
    "plan-made stages (against the user's decision). RECOMMENDATION: (a)."
    " QUESTION MAPPER: none of the plan's own stage interactions is written as a FIO. Three clues, Match, Label, Count the "
    "parts, Spin the shape, Strong or wobbly, Identify the Angle and the build stages are the tool's interaction (unscored, "
    "labelled the plan's own). They are not in `items`, not among the 109 questions of question_map.md and not in the cap.",

    "CLASH 25, Tool 1 as the exploration tool holds 11 book questions and 3 notice prompts. "
    "FLOW RULE SAYS: the exploration tool lets the child observe, try and notice before any formal explanation. BOOK "
    "SAYS: model1, model_q1 to q5, project1, qutub_q1 to q3 and puzzle1 are mostly open prompts ('what shapes will model "
    "these parts', 'how is your model similar to the real building', 'how many such shapes'); model_q4 and model_q5 "
    "need a model the child has built. Tool 1 is also the first contact with the hidden-shapes picture, which holds a "
    "cylinder among flat outlines (E31). "
    "OPTIONS: (a) keep 11 + 3: the notice prompts come first and are read, not answered, and name no new term; the book "
    "questions come last as sample-answer prompts; (b) move project1 and model_q4 and model_q5 to Tool 2 (12); (c) "
    "2 notice prompts. RECOMMENDATION: (a)."
    " QUESTION MAPPER: Tool 1's 11 questions are in the book's order (model1, model_q1 to q5, project1, qutub_q1 to q3, "
    "puzzle1). Every sample answer uses everyday words (a flat block, a tall block, a round block, a can, a box) and names "
    "no solid, so the exploration tool names no concept; qutub_q1 and qutub_q2 say that the real tower slopes smoothly and "
    "the stepped boxes do not, and qutub_q3 uses the 5 storeys of the book's own 'Do you know'.",

    "CLASH 26, 'concept video, then its tool' and 'never two tools in a row'. "
    "FLOW RULE SAYS: hook, exploration tool, then [concept video, matching tool]; images only for a small concept. "
    "HOW EACH TOOL MEETS IT (row numbers of tool_map.md): Tool 1 follows the hook (row 1), the exploration tool; "
    "Tool 2 follows the row 3 video; Tool 3 follows the row 7 image after the row 5 and row 6 videos; Tool 4 the row 9 "
    "video; Tool 5 the row 11 video; Tool 6 the row 13 video; Tool 7 the row 15 video; Tool 8 the row 17 video; Tool 9 "
    "the row 19 video; Tool 10 the row 21 image (the pentagon has an image and no video); Tool 11 the row 23 video; Tool "
    "12 the row 25 video. No two tools touch: Tools 7 and 8, 9 and 10, 11 and 12 are separated by a video or an image, "
    "and every topic opens with a video or the hook. Tools 3 and 10 follow an IMAGE, not a video, and that is the "
    "only place the rule is bent; the gate allows it (the previous concept is story or image and applies_to names it). "
    "A main-flow image whose concept has a tool must bring a new real-life context (new_context true) or be pinned "
    "(flow_c34 _check_images), so rows 7 and 21 must each show a real-life example the tool does not. "
    "OPTIONS: (a) accept; (b) a short video for the pentagon (adds a row to the approved table). "
    "RECOMMENDATION: (a).",

    "CLASH 27, the book's printed order against the tool order. "
    "BOOK SAYS (concepts by page): C1 p1-2, C2 p3, C3 p4, C4 p5, C5 p5-7, C6 p7, C7-C8 p8, C9 p9, C10-C12 p10-13, C13 "
    "p14, C14 p15, C15 and C16 p16 (pentagon first), C17-C18 p17-19, C19-C20 p19-20, C21-C22 p21-22, C23 p22, C24 "
    "p22-23. The tool order follows the user's lessons and agrees in broad sweep (buildings, solids, nets, parts, "
    "cubes, angles, circle and pentagon, rigidity) but disagrees in five places: (1) nets (Tool 4, C9) come before "
    "faces, edges and corners (Tool 5, C3), and the analysis says C9 needs C3; (2) the sorting questions of C5 "
    "(border1 to border4 in Tool 2; sort1, sort3, sort3_q, sort4 in Tool 3) come before the lesson that counts faces "
    "(Tool 5), while the book sorts after counting (sort2 was moved to Tool 5 for that reason); (3) the pentagon "
    "(Tool 10, C15) and the dot-grid shapes with a rectangle against slanted four-sided shapes (Tool 8, C14) come "
    "before the push tests (Tool 11, C13), CLASH 14; (4) on p16 the book makes the pentagon first and the circle "
    "second, the plan the circle (Tool 9) first and the pentagon (Tool 10) second; (5) the puzzles of p19 to p22 (hidden "
    "shapes, cards, cuts, model challenge) are spread over Tools 1, 2 and 5, far earlier than the book. Inside a tool "
    "the items keep the book's order. "
    "OPTIONS: (a) accept the lesson order and make each item answerable with words the child already has (the border "
    "pictures are everyday objects; net questions need only pictures of faces); (b) reorder tools (not allowed here). "
    "RECOMMENDATION: (a).",

    "CLASH 28, printed-book errors that touch the tools (analysis.md section 6; the book prints no solutions, so "
    "SOLUTION_NOTES, filled at step 5, holds the plan's own answers and how each was checked). "
    "Tool 1: E31 (hidden shapes are all one red and include a cylinder), E17. Tool 2: E7 (border sketches unnumbered), "
    "E17 (cut lines not unique), E18 (the cards are on the end pages and the three groups are not said). Tool 3: E3 "
    "(the set to sort is not stated), E4 (p7 names a 'rectangular pyramid', never drawn or named). Tool 4: E1 (nets A "
    "and C do not fold; never reuse A or C as a net that folds; net A is six rectangles that do NOT make a cuboid), E24 "
    "(Square Prism has no net on the end pages). Tool 5: E2 (3 flat faces, flat only?), E3, E5 (f fits a cube and a "
    "cuboid; seven pictures, six descriptions), E6 (opposite of 2, 3, 4 depends on the die), E7 (border5), E21 "
    "(CLASH 19). Tool 6: E26 (tower 2 colours inconsistent), E27 (hidden cubes). Tool 7: E8 (boat 10), E9 (dot grid "
    "measured), E10 (angles of V, A, Z), E23 (try8 counts 4, 0, 1, 0, 0, 4). Tool 8: E10 (stick figures), E12 (the "
    "4-sided shapes are not named), E22 (try9 has several fits; shape 1 is a dart), E28 (obtuse has no upper limit). "
    "Tool 9: E14 (centre and center; item 5 answered on p18), E15 ('ask your teacher' for the compass), E16 (wheels not "
    "measured). Tool 10: E13 (no question mark), E30 (drawn regular-looking). Tool 11: E11 (no answers), E29 (rigid is a "
    "teacher's word). Tool 12: E19 (walks), E20 (matchsticks). E25 only concerns the text layer. "
    "OPTIONS: (a) handle each as the locked map says: the figure decides, the plan labels its answer; (b) ask the "
    "content team about each. RECOMMENDATION: (a), with CLASH 12 for the answers."
    " QUESTION MAPPER: every E that touches a question is in SOLUTION_NOTES with how its answer was checked, and "
    "SOLUTION_NOTES is no longer empty. The answers that give no total on purpose: ch1.letters (the angles of A), "
    "ch1.ao_do2 (the stick figures), ch1.border1 to ch1.border5 ('for example'), ch1.cards, ch1.puzzle4, ch1.try9 (several "
    "shapes fit each clue and shape 1 fits none, E22) and ch1.straw_tri_angles (it reads the tool's triangle, which the "
    "brief writer draws with three angles narrower than a right angle). ch1.dotshapes_q c) says 'none', because a 3- or "
    "4-sided shape with 3 right angles has 4.",

    "CLASH 29, errors in the plan that the proposal corrected (analysis.md 8C; for the user to confirm). "
    "(1) Triangular pyramid '4 vertices meeting at the top apex': it has 4 corners in all and the 3 side faces meet at "
    "one of them, the apex. (2) 'Six connected squares = cube', 'six rectangles = cuboid' (the book's own net A is six "
    "rectangles and does not fold) and 'a square and four triangles = square pyramid' (true only when the triangles "
    "join the four sides): never said as bare sentences, only valid nets as figures. (3) 'Face is a flat surface': a "
    "face can be flat or curved (the cone and cylinder). (4) Spin the Shape 'how many faces can you see now': only 1, 2 "
    "or 3 for a solid cube or cuboid, never 4 or more. (5) The 'regular' pentagon: equal sides do not give equal "
    "angles, as the push test shows. (6) 'A triangle's shape does not easily change if its sides stay fixed': it cannot "
    "change at all. (7) Guess the Shape: clues 1 and 2 also fit a diamond; clue 3 decides. (8) Lesson 1 mixed flat and "
    "solid words ('looks like a triangle', 'pyramid-like'): a flat shape and a solid are named separately. (9) Obtuse "
    "'smaller than 180': 'more than a right angle', no number (the book gives no upper limit, E28; the dart of p23 shape "
    "1 is the one larger angle, E22). All the plan's counts are true (triangular prism 5, 9, 6; hexagonal prism 8, 18, "
    "12; triangular pyramid 4, 6, 4; square pyramid 5, 8, 5; cube and cuboid 6, 12, 8; F+V−E = 2). "
    "OPTIONS: (a) the corrections as listed; (b) keep the plan's wording. RECOMMENDATION: (a).",

    "CLASH 30, the six Teacher's Notes against 'no teaching role for a classroom teacher'. "
    "USER'S STANDING RULE (also in the Class 5 plans): videos explain, tools let the child explore, apply and get "
    "feedback, and no classroom teacher is given a teaching role. BOOK SAYS: six notes to the teacher: note_boxes (p2, "
    "'ask learners to collect boxes, bottles, cans'), note_venn (p7, 'discuss adjacent and opposite faces, shapes in two "
    "sets, make Venn diagrams'), note_rigid (p14, 'help children to understand rigidity; the triangle is the most rigid "
    "shape'), note_square (p15, 'discuss a square and a rectangle; a square is a special case of a rectangle; provide more "
    "dot grids'), note_measure (p17, 'measure with a paper strip, thread or scale'), note_compass (p18, 'help children to "
    "draw circles with a compass'); and p18 says 'ask your teacher to help you use a compass' (E15). "
    "OPTIONS: (a) keep each as a coverage id only; a note that holds a fact (the triangle does not change when pushed, "
    "a square is a special rectangle, adjacent and opposite faces) becomes a line of a story or of a tool's feedback; "
    "each instruction to the teacher is dropped; (b) rewrite the notes as instructions to the child. "
    "RECOMMENDATION: (a)."
    " QUESTION MAPPER: the compass sentence of ch1.compass ('Ask your teacher to help you use a compass.') is DROPPED, as "
    "option (a) recommends, and the teacher line 'Encourage learners to' of ch1.project1 is dropped with it (CLASH 50, "
    "which needs the user's yes). The six notes stay coverage ids only (note_boxes and note_measure and note_compass on "
    "Tool 1 and Tool 9, note_venn on Tool 3, note_square on Tool 8, note_rigid on the row 23 story); none is a task for a "
    "teacher and none is a FIO. The facts a note holds (a square is a special rectangle, adjacent and opposite faces, the "
    "triangle does not change when pushed) are for the brief writer to place as a line of a story or of a tool's feedback; "
    "the answers of Tools 2, 3 and 5 already treat a square face as a rectangular face (CLASH 51).",

    "CLASH 31, the third-party images in the plan. "
    "PLAN SAYS: about 20 image links under the activities (a Teachers Pay Teachers 'Shape City', blog and shop pictures, "
    "BBC Bitesize, Cuemath, GeoGebra, PaintingValley, Workybooks, RevisionDojo, the Exploratorium). BOOK SAYS: nothing; "
    "none was opened or copied. "
    "OPTIONS: (a) references only, every picture new and drawn from the book's own buildings and objects (VISUAL_KEY); "
    "(b) reuse the third-party pictures (licence unknown). RECOMMENDATION: (a).",

    "CLASH 32, the new real-life images. "
    "TABLE SAYS: two main images (row 7, a prism and a pyramid side by side with their face shapes marked; row 21, a "
    "five-sided shape with all sides equal) and the Tool 1 pictures (India Gate, the Qutub Minar, a street). BOOK SAYS: "
    "only India Gate and the Qutub Minar are drawn (and a model street). USER'S PRINCIPLES: accurate real-life examples "
    "are welcome when they represent the concept correctly; solids are shaded 3D solids; never misrepresent an object "
    "or its geometry. RISKS: row 7 must show a real prism and a real pyramid (a triangular tent or a chocolate box; a "
    "pyramid roof) with matching face marks; row 21 must not claim 'regular', because equal sides do not give equal "
    "angles; India Gate is an arch (cuboids and half-round blocks) and the Qutub Minar tapers, so no block of the "
    "book's set fits exactly and the book's own stack of three smaller boxes is the model (qutub_q2 is a 'Sample "
    "answer'). "
    "OPTIONS: (a) illustrations in the book's style that draw each real object truly; (b) photographs (licence needed). "
    "RECOMMENDATION: (a).",

    "CLASH 33, the brief's puzzle videos and the revision with concept checks have no separate slot. "
    "PLAN SAYS: Lesson 9 is revision slides, a shape-identification visual quiz, a digital worksheet and a short "
    "assessment. lp_brief.md as I have it contains no 'puzzle video' and no 'concept check' under those names. "
    "TABLE SAYS: 11 concept videos, 2 images, 2 review rows and no row for puzzles, concept checks or a worksheet. "
    "BOOK SAYS: the puzzles (C19 hidden shapes and cuts, C21 webs, C22 matchsticks, C23 model challenge) ride inside "
    "Tools 1, 2, 5 and 12 as stages with no video of their own; the review may hold no book item or new tool. "
    "OPTIONS: (a) accept: the puzzles stay stages, the visual quiz is the unscored picture recap in the review rows; "
    "(b) add a puzzle video (a new row, not in the approved table); (c) a worksheet outside the plan. "
    "RECOMMENDATION: (a). If the user means other videos, the user names them.",

    "CLASH 34, one colour and one drawing for each solid. "
    "FLOW RULE SAYS: the same shapes and colours look the same all through the chapter. BOOK SAYS: it is not "
    "consistent (prisms blue and pyramids pink on p3, but a cube is teal in one line and green in the next on p8; "
    "towers and models use other colours). USER'S PRINCIPLES: solids are shaded 3D solids, a sphere always a shaded "
    "ball. VISUAL_KEY lists the book's colours as printed (analysis.md open question 17). "
    "OPTIONS: (a) one colour per kind of solid across Tools 3, 4, 5 and 6 (prisms blue, pyramids pink as on p3, the "
    "other solids as on p8), every solid shaded 3D with dashed hidden edges, flat shapes in flat colours; (b) the "
    "book's colours wherever the book prints them. RECOMMENDATION: (a); the brief writer fixes the colour list.",

    "CLASH 35, material at the end of the book. "
    "BOOK SAYS: craft2 ('use the nets given at the end of the book') and cards ('2D-shape cards given at the end of "
    "the book') send the child to pages outside the 23 chapter pages (the nets of six solids; an orange square, green "
    "oval, dark-brown quarter circle, light-green semicircle, cyan triangle and pink circle). The analyst does not list "
    "them as items of their own. craft2 sits on Tool 4 and cards on Tool 2. "
    "OPTIONS: (a) use them: the end pages belong to this chapter and say 'use the shapes given below in Chapter 1'; "
    "(b) redraw the nets and cards from the book's descriptions. RECOMMENDATION: (a), drawn fresh from those pages."
    " QUESTION MAPPER: ch1.craft2 and ch1.cards keep the printed 'at the end of the book'; their first step says that the "
    "nets and the six cards are on the screen (CLASH 50).",

    "CLASH 36, physical tasks on a screen. "
    "BOOK SAYS: model1 (blocks), project1 (a model street), craft1 (paper strips), craft2 (cut and fold nets), craft3 "
    "(straws and plasticine), build1 (cubes from a kit), right_make (fold a paper corner), amazing1 (fold and measure "
    "with thread), compass, the straw shapes and their notebook tracing, the matchsticks. All are hands-on. "
    "OPTIONS: (a) a virtual version of the same task on the tool (build, fold, drag, push), with one line that the child "
    "can also try it with real straws or paper, never as a teacher's job; (b) drop them (leaves book items uncovered). "
    "RECOMMENDATION: (a). Measuring with thread becomes an overlay on screen, with no centimetres."
    " QUESTION MAPPER: each hands-on question keeps its printed wording and gets steps for the screen version (build on "
    "screen, fold on screen, measure with the thread overlay, push the frame). The answers describe the result the screen "
    "shows and no measured number; open ones end 'Your answer may differ'. No answer uses cm.",

    "CLASH 37, the unnamed children in the book's pictures. "
    "BOOK SAYS: a boy with a stepped Qutub Minar model (p2), a girl making a straw triangle (p14) and a girl with a red "
    "bow (p19) have no names. The boy's clothes (dark hair, light blue top) look like Nitesh's, but the book names "
    "Nitesh only on p9. "
    "OPTIONS: (a) 'a child' in the briefs; (b) let Diksha, Isha or Nitesh stand in. RECOMMENDATION: (a).",

    "CLASH 38, the kinds of three items decide the counts. "
    "BOOK SAYS: house_ex is the only solved example; dotshapes_q is headed 'Discuss:' but asks the child to count "
    "shapes; five items are talk (model_talk, prism_pyr_talk, solids_q2, amazing_t3, amazing_t5). The question counts "
    "(109, Tool 8 = 10) follow that reading (analysis.md section 5 notes). "
    "OPTIONS: (a) keep it (dotshapes_q is a question on Tool 8); (b) make dotshapes_q a talk item (Tool 8 = 9, total "
    "108). RECOMMENDATION: (a)."
    " QUESTION MAPPER: confirmed. ch1.dotshapes_q is a prompt on Tool 8 (10 questions); with option (b) Tool 8 would hold 9 "
    "and the total 108. Its answer is a Sample answer.",

    # --- written by the journey designer (step 3). ---
    "CLASH 39, Topic 3 puts three media before one tool (found while placing rows 5 to 8). "
    "NOTE: in Topic 3 (Prisms and Pyramids) the prism video (row 5) is followed by the pyramid video (row 6), the pyramid "
    "video by the comparison image (row 7), and only then comes Tool 3 (row 8, applies_to the image). So the prism video "
    "does not lead straight into a tool, and three media explain one tool. The gate allows it (a story concept holds one "
    "video and no tool; a tool may follow an image), so no gate message appears, but checklist item 3 (every concept video "
    "leads into its matching tool) and item 7 (no repeated explanation across video, image and tool) are judged by the "
    "checklist validator and by you. CLASH 26 covers only the image before a tool. "
    "PLAN SAYS: Lesson 2 has a prisms slide set, a pyramids slide set and a comparison image ('I will explain the difference "
    "between these two concepts'), then Activities 1 to 3 as one tool (table rows 5 to 8). "
    "BOOK SAYS: page 3 shows the prisms and the pyramids on one spread, asks about each, then 'What is the difference "
    "between a prism and a pyramid? Discuss.'; no part of it is a tool. "
    "OPTIONS: (a) keep rows 5 to 8 as the table has them: two stories, one comparison image (new_context true, a real tent "
    "and a real pyramid roof, not the solids Tool 3 draws), then Tool 3; the row 6 story opens by recalling the row 5 blocks "
    "so the two stories read as one sorting scene; (b) join rows 5 and 6 into one video with two ideas (breaks one "
    "new_idea per video); (c) drop the comparison image (row 7) so Tool 3 follows the pyramid video (removes a row of the "
    "approved table; the face shapes would be marked inside the stories). "
    "RECOMMENDATION: (a); choose (c) only if three media before one tool feels long.",

    # --- written by the media minimiser (step 4). No medium was added, dropped or moved: 1 hook + 11 concept videos, 2 image
    # concepts, 0 pinned images, 12 tools. Each clash below is a place where one medium overlaps another or gives away a
    # tool's finding; the recommendation is already applied as a PROVISIONAL choice in topics_1.py and media_decisions.md. ---
    "CLASH 40, the row 3 video and Tool 2 play the same game (three clues). "
    "NOTE SAYS (table rows 3 and 4): the row 3 story is a hidden block with three clues, the first two fitting two shapes and "
    "the third deciding; Tool 2's first stage is 'the child guesses a shape from three clues' (the plan's example is a square: "
    "four equal sides, four corners, a chessboard). BOOK SAYS: no such game; the nearest are the clue riddles of p8 Q1 (Tool 5) "
    "and p23 Q9 (Tool 8). RISK: the video plays round one of the tool, so the child meets the same activity twice. "
    "THE PLAN (media step): the video's hidden block is one block of Diksha's wooden set that is none of Tool 2's own rounds, "
    "and it stops once the third clue names the block: it sorts no object, cuts no shape and does not use the plan's square; "
    "Tool 2's rounds are written after the video and use other shapes. "
    "OPTIONS: (a) different shapes in the video and in the tool; (b) the video stops before the third clue and the child gives "
    "it in Tool 2 (then the video is only a question). RECOMMENDATION: (a).",

    "CLASH 41, face, corner and edge are used before row 11 teaches them. "
    "NOTE SAYS: Tool 2's approved purpose says 'sides, corners and faces' (Topic 2); the row 3 story carries one line 'a solid "
    "has faces' (CLASH 10); rows 5 to 7 say 'end faces', 'bottom face (base)' and 'triangular faces' and name a hexagonal and a "
    "pentagonal solid; row 11 then teaches 'a solid has faces, edges and corners'. BOOK SAYS: p5 already asks for 'a "
    "rectangular face', 'a triangular face', 'a curved face' and 'no corner'; p3 names the pentagonal pyramid and the hexagonal "
    "prism; no word is ever defined. RISK: row 11 repeats what rows 3 to 7 already said. "
    "THE PLAN (media step): in rows 3, 5, 6 and 7 the words are everyday words (a flat or curved side, a corner, an end face), "
    "never defined and never counted; row 11 is the only video that defines face, edge and corner, and it points to all three "
    "on ONE block and counts nothing; 'pentagonal' and 'hexagonal' are names only (the pentagon is counted in row 21). "
    "OPTIONS: (a) as planned; (b) move the first formal use to row 3 (breaks the table's order). RECOMMENDATION: (a).",

    "CLASH 42, Topic 3: three media explain the prism and pyramid contrast (a closer look at CLASH 39). "
    "NOTE SAYS (rows 5 to 8): two stories, one comparison image, then Tool 3. FINDING: the three media overlap in subject, and "
    "they answer first the blanks that Tool 3 then asks (prism_q1 to prism_q3: the common face, the other shapes, how many; "
    "pyr_q1 to pyr_q3; cube_prism); the image holds the book's own talk prompt prism_pyr_talk. That is the pipeline's order "
    "(concept media first, then the tool applies), but it is the longest run before any tool in the chapter (about 22 minutes "
    "with the tool). DIVISION OF LABOUR (decided so no explanation is given twice): row 5 teaches the prism alone (no pyramid, no "
    "cube, no count of faces, no answer to 'is a cube also a prism?'); row 6 teaches the pyramid alone (no prism beside it; it "
    "may open by recalling the blocks Diksha sorted); the row 7 image is the only place the two stand side by side, on real tents "
    "(CLASH 43), with the book's question 'what is the difference?' as its prompt and no answer on the picture; Tool 3 names, "
    "builds and sorts. Recommended length: 60 to 90 seconds for each of the two videos (the ceiling is 150). "
    "OPTIONS: (a) as the table has it, with this division of labour; (b) pin the image beside the pyramid concept so the flow is "
    "video, video, tool (row 7 and the key T3.C3 leave the main sequence: a change to the table, for the user); (c) join rows 5 "
    "and 6 (CLASH 39 b); (d) drop the image (CLASH 39 c). RECOMMENDATION: (a).",

    "CLASH 43, the real objects of the two images, and whether a video would teach Tools 3 and 10 better. "
    "NOTE SAYS (CLASH 32 and 39, topics note): row 7 'a real tent and a pyramid roof side by side'; row 21 'a pentagon tile or a "
    "football patch'; both must bring a real-life example the tool does not show (new_context true). FINDING: (1) the pyramid "
    "roof is already the example of the row 6 video (Diksha's roofs of triangle cards), so the image would repeat it. THE PLAN: "
    "the image is TWO TENTS: a camping tent (two matching triangle ends, three rectangle faces) and a tent with a square floor "
    "and four triangles meeting at one point. Both have triangle faces, so the pair shows that a triangle face alone does not make "
    "a pyramid (M_SH_2). Both are one plain tent colour, not the prism blue and pyramid pink, so colour gives no clue before "
    "Tool 3's sort (CLASH 47); they are clean illustrations with the face shapes marked by light outlines, no counts, no names "
    "'triangular prism' or 'square pyramid' (Tool 3's match stage) and no drawn solid of Tool 3. The title is 'Two Tents'. "
    "(2) Row 21: a FOOTBALL with black five-sided patches, one patch facing the child so its five sides and five corners can be "
    "counted; the title is 'A Football Patch' (the old title 'Five Equal Sides' gave the count away); it shows no number, never "
    "the word 'regular', no equal-angle mark, no straw or clay shape and no push. The patch has equal sides, as the book says, and "
    "its angles look equal too; the image says nothing about angles, and Tool 10's push shows that equal sides do not fix the "
    "angles (M_AN_8). A real pentagon is what Tool 10 does not show (it draws straws and flat shapes). "
    "TOOLS AFTER AN IMAGE, would a short video teach better? Tool 3: no, it already follows two videos (CLASH 42). Tool 10: no; "
    "the pentagon's fact is a name and two counts (a small concept, so an image); a story would either show the push (Tool 10's "
    "finding) or count aloud (the image's job), and motion belongs to the push, which is the tool. Recorded only; nothing changed. "
    "OPTIONS: (a) tents and a football patch; (b) a pyramid roof and a pentagon floor tile; (c) photographs (licence needed, "
    "CLASH 32 b). RECOMMENDATION: (a).",

    "CLASH 44, rows 15 and 19 carry two ideas each, and the tool then repeats part of them (CLASH 20). "
    "NOTE SAYS: row 15 teaches 'two lines that meet at a point make an angle' and 'the corner of a paper fold is a right angle' "
    "in one video; row 19 the centre, the radius and the diameter. BOOK SAYS: p10 the angle, p11 the right angle (its own "
    "task, the paper checker), p16 centre and radius, p17 the diameter by folding, p18 the double. RISK: 'two concepts never share "
    "a video', and Tool 7 (right_make: fold a paper corner; right_objects) and Tool 9 (make_circle, amazing1) then do what the "
    "video showed. THE PLAN: the two new_idea lines are NOT changed (the table's pairs); only the edges are fixed. Row 15: the "
    "angle first (two straws opened), then ONE right angle (a paper fold that fits one of Isha's angles); the fold is shown once "
    "and checks only the straw angle, never a book, a window, a dot grid or a yoga figure (Tool 7's questions), and acute and "
    "obtuse are not named. Row 19: the three names on ONE circle on the ground (the peg is the centre, the string the radius, "
    "one line through the peg the diameter); no second diameter, no fold, no 'all equal', no 'double' (Tool 9's finding), no "
    "unequal string, no straws, no compass, no wheels or carpet. "
    "OPTIONS: (a) as the table, with these edges; (b) split each into two videos (adds rows: not allowed here); (c) cut the "
    "second idea of each (the right angle to Tool 7's feedback, the diameter to Tool 9's), so the tool teaches it. "
    "RECOMMENDATION: (a).",

    "CLASH 45, row 15, Tool 7 and row 17 stage one situation (straws and a paper corner) three times. "
    "NOTE SAYS (rows 15 to 18): row 15 Isha's straws and Nitesh's paper corner; Tool 7 an arm moved against a right-angle corner "
    "(smaller, equal, bigger); row 17 'Nitesh and Isha test straw corners against the paper corner, some narrower and some "
    "wider'; Tool 8 sorts. So the same test appears in a video, a tool, a second video and a second tool. WHAT ROW 17 ADDS: only "
    "the two names, acute and obtuse (CLASH 2: Tool 7 says 'smaller than, equal to, bigger than'). RISK: row 17 is thin and "
    "re-runs Tool 7. THE PLAN: row 17 shows TWO corners only, one narrower and one wider, in one quick check, and its story is the "
    "giving of the two names by the book's rule ('acute is less than a right angle, obtuse is more'); it never re-runs 'make an "
    "angle', sorts no set (Tool 8's six angles), shows no V, A or Z and no stick figure, no classroom object (acute_obj and "
    "obtuse_obj ask for those), no corner bigger than a straight line (E28) and no degrees. Row 15 and Tool 7 never use the two "
    "names. OPTIONS: (a) as the table, with these edges; (b) make row 17 an image concept (the rule as a picture, no story), which "
    "drops a video of the table; (c) pin a 'three angles' reference beside Tool 8 (placement pinned), the cheapest addition if the "
    "user wants one to keep on screen. RECOMMENDATION: (a).",

    "CLASH 46, rows 23 and 25 would hand over the findings of Tools 11 and 12. "
    "NOTE SAYS (rows 23 to 26): row 23 'Isha and Nitesh push a corner of a straw triangle and of a straw rectangle; the rectangle "
    "slants and the triangle stays', idea 'a triangle is a rigid shape'; Tool 11 'the child pushes a corner of a triangle frame "
    "and of a rectangle frame and sees that the triangle keeps its shape while the rectangle's angles change'. Row 25 'Squiggly's "
    "triangle web holds firm while Wiggly's rectangle web wobbles, until a thread is added from corner to corner'; Tool 12 'adds a "
    "stick across the corners to make triangles' and compares before and after. BOOK SAYS: p14 asks 'does the shape of the "
    "triangle change if we gently push one of its sides? Yes/No' and prints no answer (E11); 'rigid' is only in a teacher's note "
    "(E29). FINDING: as the table words them, both videos show the very result the tool lets the child find, so the tool would "
    "only repeat. THE PLAN (the discovery rule: a video names the idea and may pose the test, the tool shows the result): row 23 "
    "stops BEFORE the push: the two children hold a straw triangle and a straw rectangle, recall the pentagon of Tool 10 that "
    "changed when pushed (CLASH 14), say what 'rigid' means and ask which shape will stay; its new_idea is now 'A rigid shape "
    "keeps its shape when it is pushed', and the finding 'a triangle is rigid, a rectangle is not' is Tool 11's. The fact of "
    "note_rigid (CLASH 30) therefore becomes a line of Tool 11's feedback after the push, not of the row 23 story. Row 25 stops "
    "BEFORE the thread: the triangle web holds, the rectangle web wobbles (a recall of Tool 11 in a new setting) and Squiggly says "
    "a thread from corner to corner would make triangles; the video does not show the thread added or the web firm (Tool 12's "
    "first stage does), no count of triangles or rectangles, no walk and no matchstick (Tool 12's webs and puzzles), and it draws "
    "two simple webs of its own, not the book's two. "
    "OPTIONS: (a) both stop before the result (recommended); (b) as the table (the videos show the result and the tools confirm "
    "it); (c) row 23 stops, row 25 as the table. RECOMMENDATION: (a). It changes the story text of rows 23 and 25 and the "
    "new_idea of row 23: the user decides. CLASH 22 (the row 25 claim) stays open.",

    "CLASH 47, the one-colour-per-solid code can give the answer. "
    "NOTE SAYS (CLASH 34, option a, applied to VISUAL_KEY as a provisional choice): prisms blue, pyramids pink, cube teal, cuboid "
    "red, sphere coral, cone yellow, cylinder orchid, every solid shaded 3D, a net never in the colour of its solid. FINDING: (1) a "
    "colour that always means 'prism' or 'pyramid' lets the child sort by colour in Tool 3's sorting stage and name a solid by "
    "colour in Tool 5's riddles and Tool 4's match; (2) the teal cube and the red cuboid sit apart from the blue prisms, although "
    "the book's own table names them 'Cube/Square Prism' and 'Cuboid/Rectangular Prism' (p4) and Tool 3 asks 'is a cube also a "
    "prism?' (cube_prism): a teal cube beside blue prisms would answer 'no'. Real objects (wooden blocks, bricks, a die, a "
    "football, the two tents, paper boxes) keep their own colours, so the code governs only the maths solids. "
    "OPTIONS: (a) the code everywhere, the sorting and guessing stages included; (b) the code in the teaching pictures, and one "
    "neutral tint for every solid in the stages where colour could answer (Tool 3's sort and cube question, Tool 4's match, Tool "
    "5's riddles); (c) no code. RECOMMENDATION: (b); the brief writer fixes the stages. Until the user answers, VISUAL_KEY keeps "
    "(a) and the cube is never shown beside the prisms as a different family.",

    "CLASH 48, the thin concept videos (rows 3, 9 and 17). "
    "NOTE SAYS: the table fixes 11 concept videos. FINDING: three are thin. Row 3's idea is the tool's own game (CLASH 40). Row 9's "
    "idea is one sentence ('a net is a solid opened out flat; folding brings it back'), but its content is motion (the box opened, "
    "laid flat and folded back), which a still picture cannot show, so a video earns its place. Row 17's idea is two names for "
    "what Tool 7 just did (CLASH 45). The other eight each carry a big idea or a known misconception (rows 5 and 6: M_SH_1, "
    "M_SH_2, M_SH_8; row 11: M_SH_3, 4, 5, 9; row 13: M_SH_6; row 15: M_AN_1 to 3; row 19: M_CI_1 to 4; rows 23 and 25: M_AN_5, "
    "M_AN_6, M_AN_9). THE PLAN: all eleven are kept as the table has them. "
    "OPTIONS: (a) keep all; (b) rows 9 and 17 become image concepts (the book's own picture of the opened box; the rule of "
    "acute and obtuse as a picture), which drops two videos of the table; (c) row 3 pinned as a hint beside Tool 2. "
    "RECOMMENDATION: (a).",

    "CLASH 49, the review has no medium of its own and reuses earlier pictures only. "
    "NOTE SAYS (rows 27 and 28): 'reuses earlier visuals; no new tool and no book question'; GATE: the review may not hold a new "
    "video or tool. THE PLAN (media step): no video, no image node and no tool in the review. A recap or picture-quiz may show "
    "an earlier picture only as the same VISUAL_KEY drawing, never as a new one: row 27 from prisms, pyramids, prism_tent, "
    "pyramid_tent, box_net, nets_and_solids, cube_models; row 28 from straws_angle, right_angle_checker, angle_figures_grid, "
    "circle_paper, football_patch, rigid_shapes. It never shows a figure of a book question together with its answer (the review "
    "carries no book item), so the two cube towers, the wheels, the carpet and the nets of Q3 and Q4 are not reused. "
    "OPTIONS: (a) as above; (b) a new picture per recap line (new media: not allowed here). RECOMMENDATION: (a).",

    # --- written by the question mapper (step 5). No question was moved, added or excluded; every clash below is a question for the user. ---
    "CLASH 50, the printed wording of six questions is edited on the screen (question mapper, step 5). NOTE SAYS: questions "
    "are the book's and the wording is copied exactly. BOOK SAYS: (1) ch1.compass: 'A circle can be made easily using a "
    "compass. Ask your teacher to help you use a compass.' gives a teacher a role (E15, CLASH 30). (2) ch1.project1: "
    "'Encourage learners to observe a street carefully ...' is a line to the teacher inside the question. (3) ch1.fve "
    "prints 'F+V' and 'E' joined by an en dash. (4) ch1.pentagon_q2 has no question mark after 'one of its sides' (E13). "
    "(5) ch1.amazing_q4 spells 'center' where the chapter writes 'centre' (E14). (6) ch1.sort4 says 'circles like those on "
    "the previous page', which points to a page. DONE, as CLASH 30 option (a) recommends for the compass sentence: (1) the "
    "compass question reads 'A circle can be made easily using a compass. Make the following design.'; (2) project1 reads "
    "'Observe a street carefully and make a model showing the main buildings on the street.'; (3) the screen writes F+V−E "
    "with the minus sign; (4) the question mark is put in; (5) 'centre'; (6) 'circles like the ones you just used'. Dotted "
    "blanks are drawn as short lines. NOT CHANGED: pointers that a screen cannot follow but a child understands stay as "
    "printed: 'at the end of the book' (craft2, cards: the first step says that the nets and the cards are on the screen, "
    "CLASH 35), 'given below', 'in your notebook' (straw_tri_trace), 'thread' and 'plasticine' (craft3, amazing1; CLASH "
    "36), 'the Jaadui Pitara Kit' (build1) and 'Discuss:' (dotshapes_q). OPTIONS: (a) the six edits above; (b) copy every "
    "printed word, teacher sentences included (against CLASH 30); (c) also reword the pointers. RECOMMENDATION: (a). The "
    "user's yes is needed because each edit changes a printed question.",

    "CLASH 51, a square face counts as a rectangular face in the answers of Tools 2, 3 and 5. NOTE SAYS: ch1.border1 (Tool "
    "2: shapes with a rectangular face), ch1.sort3 and ch1.sort3_q (Tool 3: rectangular and triangular faces, 'rectangular "
    "pyramid'), ch1.border5 (Tool 5) and ch1.bricks_q (Tool 2) are answered with the dice, the Rubik's cube and the square "
    "pyramid, whose faces are squares. BOOK SAYS: the p15 note for teachers (note_square, carried on Tool 8) says that a "
    "square is a special case of a rectangle, but that note comes AFTER Tools 2, 3 and 5; M_AN_6 lists 'a square is not a "
    "rectangle' as a wrong idea; E4: a 'rectangular pyramid' is never drawn, so sort3_q is read with the square pyramid. "
    "THE PLAN (question mapper): sort3 carries one step line 'A square face counts as a rectangular face', and the answers "
    "put the square pyramid in the overlap with the triangular prism. OPTIONS: (a) keep it, say it once in that step and "
    "teach the fact in Tool 8's feedback (note_square); (b) leave the dice, the Rubik's cube and the square pyramid out of "
    "the answers (the child may circle them and be told 'not listed'); (c) bring the square-is-a-rectangle line into an "
    "earlier story (changes a video). RECOMMENDATION: (a).",

    "CLASH 52, the solids to sort are not stated by the book, and Tools 3 and 5 sort different sets (E3). NOTE SAYS: Tool "
    "3's Match stage uses 'the book's six solids plus the cube' (tool_proposal.md) and its sorts use the sphere, the cone "
    "and the cylinder (CLASH 15); Tool 5's sorts need the hexagonal prism (8 flat faces), the pentagonal pyramid (10 "
    "straight edges), the cuboid and the cone. BOOK SAYS: the p4 columns (1, 2, 4, 5, 6 and 8 flat faces; 6, 8, 9 and 12 "
    "straight edges) and the p6 and p7 sorts give no list of shapes. The sample answers of ch1.sort1, sort3, sort3_q, sort4 "
    "(Tool 3) and ch1.sort_faces, sort_edges, sort2 (Tool 5) assume ONE set of ten solids: sphere, cone, cylinder, cube, "
    "cuboid (the square prism of p3, drawn long), triangular prism, hexagonal prism, triangular pyramid, square pyramid and "
    "pentagonal pyramid; each says 'for example' and 'Your answer may differ'. OPTIONS: (a) one set of these ten for every "
    "sorting stage and for Tool 3's Match stage (the brief writer fixes the drawings and the colours, CLASH 34 and 47); (b) "
    "Tool 3 sorts only the solids it names and Tool 5 all ten; (c) leave the set to the brief writer. RECOMMENDATION: (a).",
    "CLASH 53, record of approval: on 6 Nov 2026 the user replied 'continue' to the structure report and its request "
    "'approve both as recommended'; this is read as approval of the structure with every recommendation of CLASH 1 to 52 "
    "as written. This includes: the tool table derived from the user's 9-lesson plan (12 tools, now approved); the cap of 13 "
    "questions per tool for this chapter; Lesson 1 as two topics; one cross net and a 2 by 2 by 2 cube drawn as figures; "
    "the words of CLASH 9; the rigid videos of rows 23 and 25 stopping before the push and before the thread (CLASH 46); "
    "a neutral tint instead of the solids' colour code in the sorting, matching and riddle stages (CLASH 47, so the colour "
    "never answers 'is a cube a prism'); the six question wordings of CLASH 50; one set of ten solids for every sorting "
    "stage (CLASH 52); the 'every wall once' reading of Wiggly's walk. The sign-off of the plan-made answers is still "
    "open, so every answer stays labelled 'From the picture' or 'Sample answer'. No upload was asked for. Nothing else changed.",

    # --- written on 12 Nov 2026 for the content team's validator report (lp_changes_11nov.md). CLASH 54 to 58 record the user's answers
    # (DECIDED BY THE USER); CLASH 59 is the amendment's own judgement calls, for the user to confirm. The user's yes of 6 Nov 2026
    # (CLASH 53) is VOID for the structure: the new structure must be approved again. ---
    "CLASH 54, the content team's validator report and the tool count: 26 tools, not 12. "
    "PLAN SAYS (lp_brief.md): 8 lessons with 23 activities (2 in Lesson 1, then 3 in each of Lessons 2 to 8), a 9th lesson of "
    "revision and a 10-mark sample assessment. REPORT SAYS (11 Nov 2026, lp_changes_11nov.md): 11 activities are missing as "
    "activities (Lesson 2 Activities 1 and 2, Lesson 3 Activities 2 and 3, Lesson 4 Activities 2 and 3, Lesson 5 Activities 2 and 3, "
    "Lesson 6 Activity 3, Lesson 7 Activity 2 'Radius or Diameter' and Lesson 8 Activity 3); Lesson 9 'Revision and Chapter "
    "Practice' and a Sample Online Assessment are missing; the Football Patch Tool is to be removed. TABLE SAYS (until 12 Nov): 12 "
    "tools, each carrying the lesson's activities as stages (CLASH 1 and 5). OPTIONS: (a) every missing activity becomes its own "
    "tool: 23 tools for Lessons 1 to 8 plus three for Lesson 9 = 26; (b) keep the 12 tools and list the missing activities as "
    "stages (the 6 Nov design; the report says the content team does not see them); (c) merge some of them into fewer tools. "
    "RECOMMENDATION: (a). DECIDED BY THE USER (12 Nov 2026): (a). The plan had 12 tools; the user's plan has 23 activities in "
    "Lessons 1 to 8, so each missing activity becomes its own tool. The tool table is now tool_map.md and config approved_tools "
    "(26 tools; core/tool_map.py verify prints a match). New tools: 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 23 (Lessons 2 to 8) and 24, "
    "25, 26 (Lesson 9). The twelve tools that stay (1, 2, 5, 6, 9, 12, 15, 16, 18, 20, 21, 22) keep their concept and their book "
    "questions, except the eleven moves of CLASH 59. Four have a narrower approved purpose now (Tool 5 is only the Prism or Pyramid "
    "sorting, Tool 6 only Fold It, Tool 9 only the labels of a cube, Tool 12 only the cube towers); two lost a stage to a new tool "
    "without a change of purpose (Tool 16 to Tool 17, Tool 22 to Tool 23); Tool 20's purpose gained the sentence that the pentagon "
    "is met inside the tool. Where a stage moved to a new tool, media_decisions.md section 10 (SPLIT NOTES) says which. OLD AND "
    "NEW NUMBERS: CLASH 1 to 53 and SOLUTION_NOTES still use the old numbers 1 to 12. Old 1 = 1, old 2 = 2, old 3 = "
    "5 (its Match and Build stages are now Tools 3 and 4), old 4 = 6 (Match and Find the wrong net are Tools 7 and 8), old 5 = 9 "
    "(Count the parts and Spin the shape are Tools 10 and 11), old 6 = 12 (Look carefully and Copy the cube structure are Tools 13 "
    "and 14), old 7 = 15, old 8 = 16 (Identify the Angle is Tool 17), old 9 = 18 (Radius or Diameter is Tool 19), old 10 = 20, old "
    "11 = 21, old 12 = 22 (Strong or wobbly is Tool 23). Row numbers of the table changed too (42 rows now). CLASH 1 and CLASH 5 "
    "(12 tools) are superseded; so are the parts of CLASH 24, 26 and 39 that say 'no two tools touch' (see CLASH 55).",

    "CLASH 55, where the new tools sit: back to back, after the lesson's video or image. "
    "PLAN SAYS: after a lesson's slides or video come its activities, one after another, in the plan's order. TABLE SAYS (until 12 "
    "Nov): one tool per concept video, no two tools touching (CLASH 26). GATE: flow_c34 lets a tool follow another tool of the same "
    "topic only when config `tools_in_a_row` is true; each such tool still names, in applies_to, the video or image concept it "
    "follows. OPTIONS: (a) the new tools run back to back inside their lesson, after the lesson's video or image, in the plan's "
    "order; the videos stay at about 12 (plus the Lesson 9 recap); (b) a short story video before each new tool (11 more videos: "
    "against 'minimal media'); (c) split a lesson into several topics so that every tool opens its own unit (more topics, the same "
    "videos repeated). RECOMMENDATION: (a). DECIDED BY THE USER (12 Nov 2026): (a), config `tools_in_a_row` is true. Consequences: "
    "Topic 3 has six concepts (video, video, image, Tools 3, 4, 5): the most the range [1, 6] allows, so `idea_topic_concept_range` "
    "is unchanged; Tools 3, 4 and 5 all name the Two Tents image T3.C3 in applies_to, Tools 6, 7 and 8 the net video, Tools 9, 10 "
    "and 11 the parts video, Tools 12, 13 and 14 the cube tower video, Tool 16 and Tool 17 the acute and obtuse video (Tool 15 the "
    "angle video), Tools 18, 19 and 20 the circle video, Tool 22 and Tool 23 the strong-frames video (Tool 21 the rigid video), and "
    "Tools 24, 25 and 26 the Lesson 9 recap video. That is how the gate reads 'a tool applies to the concept before it'; it does not "
    "mean that, for example, Tool 4 is about the image. The runs are long (three tools after one video in Lessons 2 to 5, 7 and 9): "
    "CLASH 39 and 42 (Topic 3) now cover three tools too.",

    "CLASH 56, clock, points, degrees and cm in the plan's new activities. "
    "PLAN SAYS: Activity 3 'Beat the Clock' (5 seconds, a point for each right answer, a final score); 'Count and Win'; 'Radius = 3 "
    "cm, 10 cm, 7 cm' and 'A circle has a radius of 6 cm'; angles of 30, 45, 90, 110, 120 and 150 degrees; the 10-mark, 20-minute "
    "assessment (1 x 3, 1 x 3 and 2 x 2 marks, with degrees and cm in it). TABLE SAYS: the same adjustments as CLASH 2: no timer, no "
    "points or score, no degrees, no cm. OPTIONS: (a) keep the earlier adjustments and use the plan's activity names; (b) keep the "
    "plan's own clock, points and marks (against the pipeline's 'no unnecessary scoring'); (c) rename the activities too. "
    "RECOMMENDATION: (a). DECIDED BY THE USER (12 Nov 2026): (a). Beat the Clock (Tool 17) has no clock and no points; Count and Win "
    "(Tool 10) has no points; the Sample Online Assessment (Tool 26) is unscored, 8 questions in 3 sections, no marks shown; Radius "
    "or Diameter (Tool 19) uses plain numbers, no units; no degrees and no cm anywhere. The names are the plan's. The book prints no "
    "radius or diameter number, so the numbers of Tool 19 are practice numbers, and each one must be a true double.",

    "CLASH 57, the football picture is removed, and Build a Pentagon introduces the pentagon itself. "
    "PLAN SAYS: Lesson 7 Activity 3 'Build a Pentagon' (five segments, five points, regular and irregular); no football item. REPORT "
    "SAYS: remove the Football Patch Tool. TABLE SAYS (until 12 Nov): there was no Football Patch TOOL; the only football item was "
    "the IMAGE 'A Football Patch' (concept T8.C3 'The Pentagon', row 21), shown before Build a Pentagon, and recalled by the review "
    "through the visual `football_patch` (CLASH 26, 32, 43 and 49). OPTIONS: (a) remove the picture, nothing in its place; Build a "
    "Pentagon follows Radius or Diameter directly and introduces the pentagon itself; (b) another real pentagon (a floor tile) in "
    "its place; (c) keep the football picture. RECOMMENDATION: (a). DECIDED BY THE USER (12 Nov 2026): (a). The image, the image "
    "concept T8.C3 and the visual key `football_patch` are removed, and the review's look-back no longer recalls a football patch "
    "(it asks about 'the shape you built from equal straws'). The pentagon concept is now the role 'tool' concept of Tool 20 "
    "(T8.C4) and its applies_to is the circle video T8.C1, as the gate requires; its idea stays the book's, five sides and five "
    "corners, and the child meets the pentagon for the first time inside the tool (no picture, no video before it). The book's own "
    "football stays in the answers of ch1.border3 ('From the picture: the 3 balls, one of them a football'): that is the book's "
    "picture, not ours. M_AN_7 and M_AN_8 stay on Tool 20. CORRECTED on 12 Nov 2026 after the validator pass: the word 'pentagon' is NOT first said in the tool. It first appears in the "
    "name cards of Tool 3 and Tool 4 (pentagonal pyramid) and in the book's own questions of Tool 5 and Tool 7 (pyr_q3, solids_q5), "
    "which cannot move; what Tool 20 introduces is the idea, a flat shape with five equal sides and five corners, and the review is "
    "the only later place that says it again.",

    "CLASH 58, Lesson 9 and the sample assessment. "
    "PLAN SAYS: Lesson 9 'Revision and Chapter Practice' (revisit the concepts with slides, a shape-identification visual quiz, a "
    "digital worksheet, a short online assessment) and a 'Sample Online Assessment, 10 Marks'. REPORT SAYS: the whole section and the "
    "assessment are missing and must be added, 'available as an online activity'. TABLE SAYS (until 12 Nov): Lesson 9 had no tool; it "
    "was the two look-back review concepts, with the assessment reworded as an unscored recap (CLASH 2 (4) and CLASH 11). GATE: the "
    "last topic must be a review with 1 to 2 concepts and no video, image or tool. OPTIONS: (a) Lesson 9 is a new idea topic made of "
    "the plan's own revision and worksheet: Topic 10 'Revision and Chapter Practice' with one recap story video, then Tool 24 Shape "
    "Identification Quiz, Tool 25 Digital Worksheet and Tool 26 Sample Online Assessment, and the two existing review concepts stay "
    "as Topic 11 'Looking Back' (unscored, no media, no book item); (b) the tools inside the review (the gate forbids it); (c) the "
    "worksheet and the assessment repeat book questions. RECOMMENDATION: (a). DECIDED BY THE USER (12 Nov 2026): plan-made revision and "
    "worksheet, no repeated book questions: (a). The recap is a story video (role 'story'): it adds no new idea, and its own "
    "new_idea line reads 'Each shape of the chapter can be named by its parts', so the gate sees no duplicate. The quiz, the "
    "worksheet and the assessment carry no book question (config no_book_question_tools); the assessment is unscored, 8 questions "
    "in 3 sections. M5 holds Topic 10 and Topic 11 (there is no MLAST module any more). FLAGGED FOR THE USER: because the pipeline "
    "wants a review last, the assessment is the last TOOL but NOT the very last topic: Topic 11 'Looking Back' follows it. If the user "
    "wants the assessment as the very last item, the gate would have to change (a question for the user; nothing was changed). Also: "
    "the locked purpose of Tool 26 says 'the plan's sample assessment'; it is copied word for word into the tool's configuration "
    "(approved_purpose) and a gate compares it, so it was not changed: if the user wants it reworded, tool_map.md and the config change.",

    "CLASH 59, the amendment's own judgement calls (question mapper, 12 Nov 2026): for the user to confirm. "
    "NOTE SAYS: keep every book question where it is, except where it plainly belongs to a new activity. DONE: 11 questions moved, "
    "each to the new tool whose activity it is. (1) ch1.solids_q3 (match four nets to four solids), from Tool 6 to Tool 7: it is "
    "'which net makes which shape'. (2) ch1.solids_q5 (which solid has Nitesh's pieces in its net), from Tool 6 to Tool 7: the same "
    "action, a net to its solid. (3) ch1.solids_q4 (which of the nets A to D can be folded), from Tool 6 to Tool 8: it is 'find the "
    "net that will not fold'. (4) ch1.craft3 (count F, V and E of five solids and fill the table), from Tool 9 to Tool 10: it is "
    "counting faces, edges and corners. (5) ch1.fve (the relation F+V-E, worked on that table), from Tool 9 to Tool 10: it must stay "
    "with the table it uses. (6) ch1.observe1, (7) ch1.observe2 and (8) ch1.observe3 (die and coloured cube: opposite faces and faces "
    "that touch), from Tool 9 to Tool 11, and (9) ch1.border5 ('circle the shapes that have the same opposite faces'), from Tool 9 to "
    "Tool 11: opposite faces. (10) ch1.towers (count the cubes of two towers, hidden ones too), from Tool 12 to Tool 13. (11) "
    "ch1.dotcubes (complete the cubes on triangular dot paper), from Tool 12 to Tool 14: copying a cube structure on dot paper. "
    "The questions per tool are now 11, 9, 0, 0, 12, 1, 2, 1, 6, 2, 4, 1, 1, 1, 10, 10, 0, 13, 0, 8, 10, 7, 0, 0, 0, 0 (Tools 1 to 26; "
    "109 in all, each once, none dropped, none added, none from outside the chapter). `no_book_question_tools` is now 3, 4, 17, 19, "
    "23, 24, 25, 26 (Tools 7, 8, 10, 11, 13 and 14 each received a book question and left the list). KEPT WHERE THEY WERE, "
    "considered and not moved: (a) ch1.circ_do1 (the diameter is double the radius, by folding the paper) stays on Tool 18, not on "
    "Tool 19: Tool 18's purpose names that fold, the book prints no radius or diameter number, and Tool 19 works with plain numbers "
    "that are not a book question; (b) ch1.solids_q1 (match pictures to descriptions that give counts, and name the shapes) stays "
    "on Tool 9: on Tool 3 it would use face, edge and corner counts two lessons before they are taught; on Tool 10 it works the "
    "other way round (counts to the solid); (c) ch1.build1 stays on Tool 12 (build models with cubes), not on Tool 14; (d) "
    "ch1.straw_tri_push and ch1.straw_rect_push (Yes or No) stay on Tool 21, not on Tool 23 (True or False reads statements). LEFT "
    "TO THE USER: Tool 9 (the labels of a cube) still holds the sorts by flat faces and straight edges (sort_faces, sort_edges, "
    "sort2, three_faces), the riddles solids_q1 and the model challenge try5, which are counting and naming work that its narrowed "
    "purpose does not mention. OPTIONS: (a) leave them (recommended: they are the lesson's own questions, and moving more than the "
    "plain ones decides the lesson's design for the user); (b) move the sorts and the model challenge to Tool 10 (Tool 9 would then "
    "carry only solids_q1 or none). TOOL 23, TRUE OR FALSE: CLASH 2 (6) dropped the plan's false statement ('a triangle has four "
    "sides') and CLASH 56 kept the earlier adjustments, but a true-or-false tool needs some false statements: the brief writer "
    "proposes false ones from the book's own facts (for example 'a rectangle keeps its shape when it is pushed') and the user "
    "confirms them at the briefs. NO BOOK QUESTION on a tool means one `notice` prompt only because the structure gate "
    "(media_content, 'carries no tool_questions') refuses a tool with no question at all: Tools 3, 4, 17, 19, 23, 24, 25 and 26 each "
    "hold one prompt ('What do you notice about ...?'); the brief writer may reword it. DONE LATER (12 Nov 2026): CHAPTER_APPROACH was rewritten in the brief stage and no longer describes three parts. RECOMMENDATION: (a). The user's yes is needed for every move.",

    "CLASH 60, record of approval: on 12 Nov 2026 the user replied 'approve' to the amended structure report (26 tools, 11 topics, "
    "42 concepts) after four open points were put with a recommendation each; this is read as approval of the structure with every "
    "recommendation of CLASH 54 to 59 as written. This includes: the 11 new activity tools back to back after their lesson's video "
    "or image (CLASH 55); the plan's names, with no clock, no points, no degrees and no cm (CLASH 56); the football picture removed "
    "with nothing instead (CLASH 57); Lesson 9 as Topic 10 (a recap story video, Tool 24 Shape Identification Quiz, Tool 25 Digital "
    "Worksheet, Tool 26 Sample Online Assessment) with the two look-back cards kept as Topic 11 after it, so the assessment is the "
    "last tool and not the very last topic (CLASH 58); the 11 moved book questions and the 8 tools without a book question, each "
    "with one notice prompt (CLASH 59); the pentagon met inside Tool 20 with no picture before it (CLASH 57); and three tools after "
    "one video in Lessons 2, 3, 4, 5, 7, 8 and 9. TOOL 23, TRUE OR FALSE (the user's yes to the recommendation put on 12 Nov 2026): "
    "the plan's own four statements are used as the plan wrote them, including the false one: (1) A triangle is a rigid shape, "
    "True. (2) A rectangle can change its shape when pushed, True. (3) A triangle has four sides, False. (4) Adding a diagonal to a "
    "rectangular frame creates two triangles, True. This replaces the brief writer's proposal in CLASH 59. The sign-off of the "
    "answers the plan made is still open, so every such answer stays labelled 'From the picture' or 'Sample answer'. No upload "
    "was asked for. Nothing else changed.",

    "CLASH 61, fixes after the validator pass, approval recorded again (12 Nov 2026). The validator found four failures in the brief "
    "text and some concerns; they were fixed in the specs, not in the structure: Tool 8's nets and reason cards now agree (Net 2, "
    "the block of two rows of three, is the net that will not fold, and every net of Tools 6, 7 and 8 was folded by a script); the "
    "thought-bubble prompt is placed in Tools 24, 25 and 26; no tool says a face is flat only (a face can be flat or curved); Tool 2 "
    "no longer says 'right angle' in Lesson 1. Also: Tool 3 shows the five solids of its approved purpose only; Tool 25 has one "
    "rule for Check; Tool 20's tray holds six clay balls; the phase wording was removed from the frame. Two inaccurate notes of "
    "this record were corrected (CLASH 57: the word 'pentagon' is first met in the name cards of Tools 3 and 4 and in the book's "
    "own questions, not in Tool 20; CLASH 59: the approach text no longer describes three parts). DECISION RECORDED: Tool 4 Build Your "
    "Own 3D Shape builds with a real toy block set in its own colours, one colour for each kind of face and never a prism, pyramid "
    "or cube colour, so colour never names the solid the child builds; the approach text now says the grey tint is for sorting and "
    "matching games. Nothing else changed: no tool, no purpose, no question home. This is a repeat of the structure approval for "
    "the corrected records; the user was told.",
]

# ---------------------------------------------------------------------------
# printed-book errors this plan corrects: {"item", "printed_solution", "correct"}; and ERRATA, exact false-equation
# chains kept verbatim from the book (copy each into chapter.config.json "eqcheck_errata" too).
# ---------------------------------------------------------------------------
SOLUTION_NOTES = [
    {"item": "all 109 questions",
     "printed_solution": "The chapter prints no answer, solution or key.",
     "correct": "No content-team key is part of this chapter's files (CLASH 12). Every answer is the plan's own reading and begins exactly 'From the picture' (counts, positions, what a picture or the screen shows) or 'Sample answer' (open tasks and geometry the book does not print); open tasks end 'Your answer may differ'. None is presented as an official answer, and none is a number the analysis could not confirm. The results of analysis.md Appendix A (towers 30 and 66, the matchstick solutions of p22 Q3 and Q4, nets A to D, the boat, the coloured cube) were checked again by the question mapper on 6 Nov 2026; each is explained in its own entry below. The content team may replace the answers with a key."},
    {"item": "ch1.solids_q4 (E1)",
     "printed_solution": "No key. Net A is a column of four rectangles with one flap at the top right and one at the bottom right, both on the SAME side, so both flaps cover the same end; net C has the base and only 2 of the 4 triangles its pyramid needs. B (cylinder) and D (a flat box whose two end flaps are on opposite ends) are fine.",
     "correct": "From the picture: B and D fold into the solid below, A and C do not. Checked by counting the faces of each net and folding it on a 6x render of the page: A has 6 rectangles but its two end flaps close the same end; C has 3 faces of the 6 a pyramid on a 4-sided base needs; D is a strip of 4 rectangles (two long, two short) with an end flap on each opposite end. The steps say why A and C fail. A and C are never shown as nets that fold, and the plan never says 'six rectangles make a cuboid'."},
    {"item": "ch1.solids_q3",
     "printed_solution": "No key.",
     "correct": "From the picture: (1) with (b), (2) with (d), (3) with (a), (4) with (c). (1) is 4 triangles (a triangular pyramid), (2) a rectangle and 2 circles (a cylinder), (3) a strip of 4 rectangles with a flap on each of two opposite sides (a cuboid), (4) 3 rectangles and 2 triangles (a triangular prism)."},
    {"item": "ch1.solids_q5",
     "printed_solution": "No key.",
     "correct": "From the picture: d, the pentagonal pyramid. 1 pentagon and 5 triangles fit only a pentagonal pyramid. Option c has a 6-sided bottom face, a is a square pyramid and b a triangular pyramid."},
    {"item": "ch1.three_faces (E2)",
     "printed_solution": "'Can you construct a 3D shape with 3 flat faces?' does not say whether curved faces are allowed.",
     "correct": "Sample answer: a solid with only flat faces needs at least 4. A cylinder cut in half along its length has 3 flat faces (two half circles and a rectangle) and 1 curved face. The answer gives both readings and ends 'Your answer may differ'."},
    {"item": "ch1.sort_faces and ch1.sort_edges (E3)",
     "printed_solution": "The set of shapes to sort is not stated. The columns are 1, 2, 4, 5, 6 and 8 flat faces and 6, 8, 9 and 12 straight edges, so the pentagonal pyramid (10 edges) and the hexagonal prism (18 edges) have no edge column, and there is no column for 0, 3 or 7 flat faces.",
     "correct": "Sample answers over the ten solids of CLASH 52: flat faces 1 cone, 2 cylinder, 4 triangular pyramid, 5 square pyramid and triangular prism, 6 cube, cuboid and pentagonal pyramid, 8 hexagonal prism (the sphere has none). Straight edges 6 triangular pyramid, 8 square pyramid, 9 triangular prism, 12 cube and cuboid; the answer says that the pentagonal pyramid (10) and the hexagonal prism (18) fit no column."},
    {"item": "ch1.sort1, ch1.sort2, ch1.sort3, ch1.sort3_q and ch1.sort4 (E3, E4)",
     "printed_solution": "'rectangular pyramid' is printed but never drawn or named in the chapter. The set to sort is not stated. sort4 says 'circles like those on the previous page', which points to a page of the book.",
     "correct": "Sample answers over the ten solids of CLASH 52, each 'for example'. A square face counts as a rectangular face (CLASH 51), so the square pyramid is in the overlap of sort3 with the triangular prism, and sort3_q answers 'the overlap' for the triangular prism and a pyramid with a rectangle at the bottom. In sort4 'on the previous page' reads 'you just used' (CLASH 50). sort2: the cone and the cylinder have curved edges, the sphere has no edges."},
    {"item": "ch1.solids_q1 (E5)",
     "printed_solution": "Seven pictures stand beside six descriptions that are not lettered. Description f) '6 faces, 12 edges, 8 corners' fits both the cuboid and the cube. No key.",
     "correct": "From the picture: a) square pyramid, b) cone, c) sphere, d) cylinder, e) triangular prism, f) cube or cuboid, because both fit. Checked: 5 + 5 − 8 = 2 and 5 + 6 − 9 = 2 and 6 + 8 − 12 = 2 for a, e and f. The sphere is a shaded ball."},
    {"item": "ch1.observe1 and ch1.observe2 (E6)",
     "printed_solution": "'Take a die.' The answers depend on the die in hand; the picture shows only 5, 1 and 3. No key.",
     "correct": "Sample answer: on a usual die, a) 5, b) 4, c) 3, because opposite faces add up to 7 (2 + 5, 3 + 4, 4 + 3). The tool's die is a usual die (VISUAL_KEY die). observe2 is true for any die on which 6 is opposite 1: the faces 2, 3, 4 and 5 touch 1 and 6 does not."},
    {"item": "ch1.observe3",
     "printed_solution": "Three views of one cube, no key.",
     "correct": "From the picture: a) purple, b) orange. Checked by trying every colouring of the six faces against the three printed views, including the way the faces turn round a corner (top, left, right read as one turn): only red opposite purple, yellow opposite orange and dark blue opposite green fit all three views."},
    {"item": "ch1.border1 to ch1.border5 (E7)",
     "printed_solution": "The shapes along the border are about 20 pencil sketches, not numbered, with no key. 'Circle the shapes that have the same opposite faces' is unclear.",
     "correct": "From the picture, 'for example' (counted on the page: 2 dice, 2 erasers, a Rubik's cube, a gift box, 3 balls one of them a football, 3 cans or bottles, an ice-cream cone, a party hat, 2 cheese pieces, 2 pyramid drawings, a wooden wedge and a cake slice). border3 (curved face): the balls, the cans or bottles, the cone, the hat. border4 (no corner): the balls and the cans or bottles. border1 and border2 list only certain shapes. The two cheese pieces are drawn as pyramids with small holes, never as wedges, so border1 does not list them and border5 does not either. border5 is a Sample answer under one reading (each pair of opposite faces looks the same) and needs the user's reading (CLASH 28)."},
    {"item": "ch1.house_ex and ch1.boat_q (E8)",
     "printed_solution": "'There are 7 angles in this house drawing.' and 'How many angles are there in this boat drawing?' The book does not say that the mast splits the sail into two angles. No key for the boat.",
     "correct": "From the picture: the house has 7 marks (1 + 2 + 2 + 2 = 7, as the book says) and the boat has 10 marked angles (2 + 2 + 2 + 4 = 10): 2 at the top of the sail, one on each side of the mast, 2 at the lower corners of the sail, 2 right angles where the mast meets the sail and 4 in the body of the boat (counted on a 6x render)."},
    {"item": "ch1.right_circle (E9)",
     "printed_solution": "Eight angle figures on a dot grid and no key.",
     "correct": "From the picture, read by measure on the page: the 2nd and 3rd angles in the top row and the 1st and 4th in the bottom row are right angles. The top row 1st and 4th and the bottom row 2nd and 3rd are not (the first two are wider than a right angle, the last two narrower). The answer says to check each with the checker."},
    {"item": "ch1.letters and ch1.ao_do2 (E10, E28)",
     "printed_solution": "'Identify all angles' in V, A and Z marks only one angle in each letter and does not say how many there are in A. The four stick figures do not say how many angles to mark. 'Obtuse angles are more than a right angle' has no upper limit.",
     "correct": "Sample answers with no count for A or for the figures: V has 1 acute angle, Z has 2 acute angles, A has an acute angle at the top and angles where the bar meets the legs. For the stick figures the answer gives the method: red if it is narrower than a right angle, green if the same, blue if wider. Tool 8 shows only obtuse angles narrower than a straight line, except the book's dart (CLASH 28)."},
    {"item": "ch1.straw_tri_push to ch1.straw_compare (E11, E29)",
     "printed_solution": "The push test has no printed answer; the teacher note says only that the triangle is the most rigid shape, and the word rigid is never in the child's text.",
     "correct": "From the picture (what the push on the screen shows): the triangle does not change; the rectangle and the square lean over into two acute and two obtuse angles; the rectangle has 4 right angles before the push. A triangle of three fixed straws cannot change at all. straw_tri_angles reads the tool's triangle (three angles narrower than a right angle, like the book's straw triangle) and adds that another triangle can have a right angle or a wider one."},
    {"item": "ch1.fourside_q and ch1.dotshapes_q (E12)",
     "printed_solution": "The three 4-sided shapes are not named. dotshapes_q asks for the shapes with 1, 2, 3 and all right angles.",
     "correct": "The answer says 'the three shapes shown' and gives no name for them: a rectangle and a square have 4 right angles, and the three shapes shown have none (measured: none has a corner near a right angle). For dotshapes_q: 1 right angle a right triangle, 2 a shape with one slanting side, 3 none (a 4-sided shape with 3 right angles has 4), all a rectangle and a square."},
    {"item": "ch1.pentagon_q2, ch1.amazing_q4 and ch1.fve (E13, E14)",
     "printed_solution": "pentagon_q2 has no question mark ('... push one of its sides. Yes/No'). amazing_q4 spells 'center' while the chapter says 'centre'. fve prints 'F+V' and 'E' joined by an en dash. amazing_t5 (the relation of radius and diameter) is answered only on p18.",
     "correct": "The screen shows 'sides? Yes/No', 'centre' and 'F+V−E' with the minus sign (CLASH 50). The relation is answered in circ_do1: double."},
    {"item": "ch1.pentagon_make and ch1.pentagon_q1 (E30)",
     "printed_solution": "The straw pentagon is drawn as a regular-looking pentagon; the text never says 'regular'.",
     "correct": "The task says only '5-sided shape with all sides equal'. pentagon_q1 answers 'no, each angle is bigger than a right angle' (From the picture of that pentagon); equal sides do not fix the angles, and pentagon_q3 shows some angles get smaller and some bigger when it is pushed."},
    {"item": "ch1.compass and ch1.project1 (E15 and the teacher wording)",
     "printed_solution": "'Ask your teacher to help you use a compass.' and 'Encourage learners to observe a street carefully...' give a teacher a role. Step 1 to Step 3 of the compass design are pictures only.",
     "correct": "The compass question reads 'A circle can be made easily using a compass. Make the following design.' and project1 reads 'Observe a street carefully and make a model showing the main buildings on the street.' (CLASH 30 option (a), CLASH 50; the user's yes is needed). The steps are read from the three pictures: Step 1 a circle, Step 2 more circles of the same opening that start on the first circle and pass through its centre, Step 3 the petals coloured."},
    {"item": "ch1.wheels_q1 (E16)",
     "printed_solution": "Radius and diameter are asked four ways but only two wheels can answer; no units; no key.",
     "correct": "From the picture, read by measure on a 6x render (outer sizes 665, 604, 515 and 440 for B, C, A and D): longest radius and longest diameter B; shortest radius and shortest diameter D. Radius and diameter are the same wheel in each pair."},
    {"item": "ch1.puzzle1 to ch1.puzzle4 (E17, E31)",
     "printed_solution": "The number of hidden shapes is not stated, and no solution to puzzles 2 to 4 is printed; the cuts are not unique. The hidden shapes are all one red and one of them is a cylinder among flat outlines.",
     "correct": "Read at 6x and measured: the hidden shapes are a circle, a cylinder, ONE upright square (as wide as it is tall), ONE tilted rectangle (about 2.3 times as long as wide) and two triangles; the answer says the cylinder is a solid and the others are flat. Puzzle 2 on the 4 by 4 right triangle: a line from the middle of the top side straight down to the slanted side, and a line from the middle of the left side straight across to it; they make a 2 by 2 square and 2 small right triangles. Puzzle 3 on the 3 by 3 square: a dot on the top side joined to the two bottom corners makes 3 triangles. Puzzle 4, Sample answers: A two cuts at the pointed ends, B three cuts from the bottom middle to the two top corners and straight up the middle (four right triangles with legs in the ratio 2 to 1, as printed), C three corner cuts (3 triangles and a 6-sided piece)."},
    {"item": "ch1.cards (E18)",
     "printed_solution": "The six cards are at the end of the book, and the book does not say what the three groups are.",
     "correct": "The six cards are on the screen. Sample answer: only straight sides (square, triangle), only curved sides (oval, circle), both (quarter circle, semicircle). Another grouping, for example by the number of straight sides, is also right."},
    {"item": "ch1.try1a to ch1.try1d (E19)",
     "printed_solution": "No key. Neither walking question says that every wall must be used. Squiggly's printed numbers 1 to 12 already trace one closed walk.",
     "correct": "From the picture: 10 triangles (1 at the top, 1 at the bottom, 4 small and 4 big in the middle: 1 + 1 + 4 + 4 = 10) and 12 rectangles (1 + 6 + 2 + 2 + 1 = 12). Squiggly's walk: the numbers 1 to 12 go A, then each next wall starts where the last ended, and they use all 12 walls once and end at A (checked wall by wall; every corner has an even number of walls). Wiggly: two corners (the left and right ends of the long middle line) have 3 walls each and every other corner an even number, so a walk over every wall must start and end at those two corners, never at A and B (no, on the 'every wall' reading); if he may skip walls, A, down the long line, along the middle line and down to B uses no wall twice (yes). CLASH 12 and 17."},
    {"item": "ch1.try2, ch1.try3 and ch1.try4 (E20)",
     "printed_solution": "No answer. The book draws the three triangles of Q3 with small gaps at their base corners and does not say how Q4's 13 sticks are to be read.",
     "correct": "Sample answers, each checked by program on the triangular grid. Q2: two triangles that share one stick use 3 + 3 − 1 = 5 sticks. Q3: the figure has 9 sticks (9 red heads) in three triangles that touch at their base corners; the bottom stick and the right slanting stick of the third triangle, laid along the tops between the first and second and between the second and third top corners, make 4 triangles (2 up, 2 down); with truly separate triangles there is no solution, so the touching reading is the only one in which the question can be answered (CLASH 12). Q4: the figure has 13 sticks and 7 triangles (6 small, 1 of side 2); of the 715 ways to remove 4 sticks, 128 leave exactly 3 triangles; the answer gives one that leaves no stray stick (the right side and bottom of the top right triangle, the top and right side of the far right triangle). Other answers are right too."},
    {"item": "ch1.towers (E26, E27)",
     "printed_solution": "'How many cubes are there in each of these cube towers?' No key. Only the outside of each tower is drawn, and the colours of tower 2 are not consistent.",
     "correct": "From the picture: 30 and 66, with the stated assumption of solid layers, no gap and no extra hidden cube. The first tower has 4 layers of 1, 4, 9 and 16 cubes (1 + 4 + 9 + 16 = 30, the same shape as model D). The second tower is a middle column of 6 and four stairs going out from it, each with columns of 5, 4, 3, 2 and 1 cubes: 5 + 4 + 3 + 2 + 1 = 15, 4 × 15 = 60 and 6 + 60 = 66 (counted from the 21 visible top faces and the stair steps; analysis.md Appendix A). The tool draws every cube teal, so the colour mix is not copied."},
    {"item": "ch1.try5 (E21)",
     "printed_solution": "c) 15 straws and 10 clay balls is a solid the chapter never shows. The picture beside it is a square pyramid of 8 straws and 5 balls, none of the four answers.",
     "correct": "The working shows it from its parts: two 5-sided ends (5 + 5 = 10 straws), 5 more straws (10 + 5 = 15) and 5 + 5 = 10 balls. The answer says 'a prism with two 5-sided ends' and does not name it. a) cube or cuboid, b) triangular prism, d) pentagonal pyramid (5 + 5 = 10 straws, 5 + 1 = 6 balls)."},
    {"item": "ch1.try6 and ch1.try6_q (E25)",
     "printed_solution": "The text layer puts 'What relation do you notice...' after Q5; the page prints it under Q6.",
     "correct": "The page is used: try6_q follows try6. From the picture: 3 angles b, d, f; 4 angles a, c, g; 5 angles e; the number of sides is the number of angles."},
    {"item": "ch1.try8, ch1.try8_q and ch1.try9 (E22, E23)",
     "printed_solution": "try9 asks to 'identify the shape' but several shapes fit each clue; shape 1 is a dart with an angle larger than a straight line. try8 has no key, and its red tilted figure is drawn as a rectangle, not a square.",
     "correct": "From the picture, re-measured on the page: try8 4, 0, 1, 0, 0, 4 and 'the first and the last shape' (both rectangles; the purple triangle has one right angle). try9: 2 right, 1 acute, 1 obtuse: shapes 2 and 7; 1 right, 2 obtuse, 1 acute: shape 10; 2 obtuse, 2 acute: shapes 3, 5, 8, 9, 11, 13; 4 right angles: shapes 4, 6, 12, 14. The answer says that more than one shape fits. Shape 1 fits no clue and is not mentioned."},
    {"item": "ch1.craft2 and ch1.craft3 (E24)",
     "printed_solution": "Craft 2 shows a 'Square Prism', but the net page at the end of the book has no net of that name (it has a 'Rectangular Prism / Cuboid'). The p4 table row is 'Cube/Square Prism'.",
     "correct": "The answer does not say which net makes which prism: each net folds into the solid shown beside it, a Sample answer. The nets are on the screen. craft3 uses the table's own row names."},
    {"item": "ch1.prism_q3",
     "printed_solution": "'How many such faces each?' does not say which faces: the other shapes of Q2 (2 each) or the rectangle faces of Q1 (3, 4 and 6). No key.",
     "correct": "From the picture: the answer gives both, '2 of the other shape on each prism. The rectangle faces are 3, 4 and 6'."},
    {"item": "ch1.pyr_q3",
     "printed_solution": "'Identify any other shape in each of the pyramids' has no answer for the triangular pyramid, whose faces are all triangles.",
     "correct": "From the picture: the bottom face; the square pyramid has a square, the pentagonal pyramid a pentagon, and the triangular pyramid has only triangles."},
]
# The book prints no equation and no false sum, so there is no false-equation chain to keep: ERRATA stays empty and
# chapter.config.json "eqcheck_errata" stays empty. Every sum the plan writes is true (F+V−E = 2 for the five solids,
# 1 + 4 + 9 + 16 = 30, 5 + 4 + 3 + 2 + 1 = 15, 4 × 15 = 60, 6 + 60 = 66, 2 + 2 + 2 + 4 = 10, 1 + 2 + 2 + 2 = 7, 1 + 1 + 4 + 4 = 10,
# 3 + 2 + 1 = 6, 1 + 6 + 2 + 2 + 1 = 12, 3 + 3 − 1 = 5, 5 + 5 = 10, 10 + 5 = 15, 5 + 1 = 6).
ERRATA = [
]

DESIGN_REFERENCES = [
    {"text": "Class 3/4 story and tool flow: docs/00_overview.md. The tool map follows the user's 9-lesson teaching plan, with every activity its own tool.",
     "url": ""},
]

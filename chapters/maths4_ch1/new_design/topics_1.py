# -*- coding: utf-8 -*-
"""Shapes Around Us (Class 4, chapter 1): the topic skeleton. STEP 3, c34-journey-designer, rebuilt from zero on the user's
9-lesson plan (6 Nov 2026) and AMENDED on 12 Nov 2026 for the content validator's report (lp_changes_11nov.md, CLASH 54 to 58).
Keys are FINAL from here on once approved: topic "T1", concept "T1.C1".

The flow follows tool_map.md ROW BY ROW (42 rows): hook (row 1), Tool 1 (row 2), then ten units of [concept video(s) or image, then
the lesson's tools back to back], then the two review rows (41, 42). The 26 tools are LOCKED (tools_1.py, chapter.config.json
approved_tools); nothing here adds, drops, renames, reorders, merges or splits one. No tool opens a topic. The tools of one lesson run
back to back (config `tools_in_a_row`, CLASH 55); every one of them applies_to the lesson's last video or image concept.

    M1 Spotting Shapes            (Lesson 1, two topics because the gate fixes the opening topic: CLASH 6)
      T1  Shapes Around Us        row 1  hook video                  -> row 2  Tool 1  Shape Detective
      T2  Guess the Shape         row 3  concept video               -> row 4  Tool 2  Guess the Shape
    M2 Solid Shapes
      T3  Prisms and Pyramids     rows 5 and 6 videos, row 7 comparison image -> rows 8, 9, 10  Tools 3, 4, 5
      T4  Nets of 3D Shapes       row 11 concept video               -> rows 12, 13, 14  Tools 6, 7, 8
      T5  Faces, Edges and Corners row 15 concept video              -> rows 16, 17, 18  Tools 9, 10, 11
      T6  Cube Towers and Drawings row 19 concept video              -> rows 20, 21, 22  Tools 12, 13, 14
    M3 Angles
      T7  Understanding Angles    row 23 video -> row 24 Tool 15 ; row 25 video -> rows 26, 27  Tools 16, 17
    M4 Circles and Firm Shapes
      T8  Circles and Pentagons   row 28 video -> rows 29, 30, 31  Tools 18, 19, 20 (the pentagon is met inside Tool 20; no picture)
      T9  Shapes with Straws, Rigidity  row 32 video -> row 33 Tool 21 ; row 34 video -> rows 35, 36  Tools 22, 23
    M5 Revision and Review        (Lesson 9, then the closing look back)
      T10 Revision and Chapter Practice  row 37 recap story video -> rows 38, 39, 40  Tools 24, 25, 26
      T11 Looking Back            rows 41 and 42: two look-back concepts, nothing new (the last topic: the gate wants a review last)

Counts: 11 topics, 5 modules; 1 hook video, 12 concept videos (rows 3, 5, 6, 11, 15, 19, 23, 25, 28, 32, 34, 37; row 37 is the recap
story of Lesson 9), 1 image concept (row 7, Two Tents), 26 tools, 2 review concepts = 42 concepts, one per table row. Concept keys:
T1.C1..C2, T2.C1..C2, T3.C1..C6, T4.C1..C4, T5.C1..C4, T6.C1..C4, T7.C1..C5, T8.C1..C4, T9.C1..C5, T10.C1..C4, T11.C1..C2
(2+2+6+4+4+4+5+4+5+4+2 = 42).

STEP 4, THE MINIMUM MEDIA (c34-media-minimiser; the table and the reasons are in media_decisions.md, the open points are
CLASH 40 to 49 and 54 to 58): the 12 videos and the Two Tents image of the earlier plan are kept. Changed on 12 Nov 2026: the
football image (row 21) is removed with nothing in its place (CLASH 57), and one recap story video is added for Lesson 9 (row 37,
CLASH 58). Count: 1 hook video + 12 concept videos, 1 image concept (main, new_context true), 0 pinned images, 26 tools. Rule for
every video: it names the idea and may pose the test, but never shows the result a tool lets the child find; the recap names no
picture of the quiz and no answer of the worksheet or the assessment.

DECIDED EARLIER AND KEPT (the user's yes of 6 Nov 2026, CLASH 53), as amended by CLASH 54 to 58:
  CLASH 6   Lesson 1 is T1 + T2 (11 topics for 9 lessons: Lesson 1 takes two, Lesson 9 takes two).
  CLASH 9   the word is "corner"; apex and rigid kept; "vertex" is not a key term here (the brief writer may use it once).
  CLASH 10  one light line in the row 3 story tells a flat shape (sides, corners) from a solid (faces).
  CLASH 11  the review is an unscored look-back; the Topic 2 concept T2.C1 is named in review row 41 (T11.C1).
  CLASH 14  the pentagon is pushed (Tool 20) before the rigidity lesson (Tools 21, 22, 23); the row 32 video may recall it.
  CLASH 20  a tool's concept is its LEAD concept; the other analysis concepts are stages (row 23 teaches the angle and the
            right angle in one video; row 28 the three parts of a circle).
  CLASH 21  Tool 2's concept is "telling shapes apart by their sides, corners and faces".
  CLASH 22  Tool 22's concept is the plan's "a stick across a frame makes it firm"; the user confirms the row 34 story claim.
  CLASH 26  Tools 3, 4 and 5 follow an IMAGE (row 7), so that image has new_context=True; with the lesson's tools back to back they
            all name that image in applies_to (CLASH 55).
  CLASH 30  the six teacher notes are coverage ids only; a fact in a note becomes a line of its story (note_rigid).
  CLASH 32  the new image (row 7) draws real objects truly, in the book's style.
  CLASH 39  Topic 3 puts three media before its tools.
  CLASH 40  row 3 video and Tool 2 both play "three clues": the video's block is not one of Tool 2's rounds.
  CLASH 41  face, corner and edge are used before row 15 teaches them: everyday words in rows 3 to 7, defined only in row 15.
  CLASH 42  Topic 3: division of labour between rows 5, 6, 7 and the three tools (prism alone, pyramid alone, contrast on real tents).
  CLASH 43  the image's real objects (two tents); the football patch of row 21 is gone (CLASH 57).
  CLASH 44  rows 23 and 28 carry two ideas each; the tools then repeat part of them.
  CLASH 45  row 23, Tool 15 and row 25 stage one situation (straws and a paper corner) three times.
  CLASH 46  rows 32 and 34 stop before the push and before the thread, so Tools 21 and 22 keep their finding.
  CLASH 47  the one-colour-per-solid code can give the answer in sorting stages; real objects keep their own colours.
  CLASH 48  the thin videos (rows 3, 11, 25): kept, alternatives recorded.
  CLASH 49  the review has no medium of its own and reuses earlier pictures only.
  CLASH 54 to 58 (12 Nov 2026, the user's answers to the validator's report): every missing activity is its own tool (26 tools);
            the lesson's tools run back to back; no clock, no points, no degrees, no cm; the football picture is removed and
            Build a Pentagon introduces the pentagon itself; Lesson 9 is a recap video plus three tools, then the review.

QUESTIONS (step 5, c34-question-mapper): every book question is a FIO(...) in `items` of its tool concept: 109 questions
(1 example, 59 exercise, 49 prompt), each once, per tool 11, 9, 0, 0, 12, 1, 2, 1, 6, 2, 4, 1, 1, 1, 10, 10, 0, 13, 0, 8, 10, 7, 0, 0, 0, 0
(Tools 1 to 26); none is on a hook, a video or image concept or the review, and none is excluded (every item is printed on the 23
pages). On 12 Nov 2026 eleven questions moved from the old tool of their lesson to a new tool whose activity they plainly are (CLASH
59 lists each move and why). The 22 book items that are not questions (5 talk, 17 text) stay in `ncert=[...]` of the teaching
concept that holds them. The hook carries "opening" only. Tools 3, 4, 17, 19, 23, 24, 25 and 26 carry no book question
(config `no_book_question_tools`). question_map.md has the whole chain (question, concept, tool). Every answer is "From the picture"
or "Sample answer" (the book prints none); CLASH 50 to 52 are the mapper's.

Rules for every string: short plain sentences (Class 4: at most 16 words), no em or en dash, never "NCERT", "textbook",
"page N" or "Fig." (say "your maths book"), book characters and objects only (content.STORY). Teach lines, recaps, story
briefs, image briefs and tool specs are the brief writer's (step 6), except the hook's prediction and the two look-back
reviews, which are plain recap lines made only of ideas already taught. The recap video (T10.C1) and the new tools (3, 4, 7, 8, 10,
11, 13, 14, 17, 19, 23, 24, 25, 26) get their story brief and spec after the user approves the structure.
"""

from __future__ import annotations

from topics_common import A, DOER, FIO, IMG, TOPIC, VID, WE  # noqa: F401

TOPICS = []

# ----------------------------------------------------------------------------------------------------------------------
# STORY BRIEFS (step 6, the brief writer): one dict per video, in plan order. Cast only from content.STORY["characters"].
# Each concept video continues the thread of the one before and leaves its tool's finding to the tool.
# ----------------------------------------------------------------------------------------------------------------------
_S_HOOK = {
    "characters": ["Diksha", "Diksha's father"],
    "setting": "A floor mat at home in the evening, after the summer trip to Delhi. Diksha's wooden blocks lie spread out. "
               "A drawing of India Gate stands up behind her.",
    "situation": "Diksha and her father remember the trip. They name India Gate, the Qutub Minar and other buildings. "
                 "Diksha says she will build India Gate from her blocks. She spreads the blocks out and studies the drawing. "
                 "She picks up one block after another, turns it and puts it down again. No block is placed on the model.",
    "open_question": "Which block could Diksha use for the top of India Gate, and which for the rest?",
}
_S_CLUES = {
    "characters": ["Diksha", "Diksha's father"],
    "setting": "The same floor mat. Two of Diksha's wooden blocks lie on it, a long block and a half-round block. "
               "Her father sits beside her.",
    "situation": "Diksha's father starts a guessing game. He hides one of the two blocks behind his back and gives three clues. "
                 "His first clue is, I have flat faces. Both blocks fit. His second clue is, I have corners. Both still fit. "
                 "His third clue is, I have a curved side. Now only one block fits. "
                 "Diksha picks the half-round block, and her father shows it to her. "
                 "He adds that a flat shape has sides and corners, and a block has faces.",
    "problem": "The first two clues fit both blocks. Diksha must use clues about sides, corners and flat or curved parts together.",
    "thread": "Continues from the hook. Diksha is still on her mat with her blocks. Her father now asks her to look at "
              "them closely.",
    "leads_to": "The Guess the Shape tool, where the child guesses shapes from three clues.",
}
_S_PRISM = {
    "characters": ["Diksha", "Diksha's father"],
    "setting": "The floor mat. A new box of wooden blocks from her father stands open beside the old set.",
    "situation": "Diksha wants tall pillars for her India Gate model. Her father gives her a new box of blocks. "
                 "Some have three-sided ends, some square ends and some six-sided ends. "
                 "She piles blocks of different shapes and the pillar topples. She stands one block on its end. She sets a "
                 "matching block on top, and the pillar stays straight. She looks at both ends of each block and sees that "
                 "they match. The sides between the ends are all rectangles. Her father says a block like this is called a prism.",
    "problem": "Diksha's pillar topples when she piles odd blocks on each other. She needs to see what the blocks that "
               "stack straight have in common.",
    "thread": "Continues from the hidden block game. Diksha now looks at the faces of her blocks.",
    "leads_to": "The next story, about pyramids. Then a picture of two tents, then three tools: match the solids, build them and sort them.",
}
_S_PYRAMID = {
    "characters": ["Diksha", "Diksha's father"],
    "setting": "The floor mat. The prism blocks are packed away in their box. Cream paper cards, a square one and some "
               "triangles, lie beside the model house.",
    "situation": "Diksha remembers the blocks she sorted. Her pillars are done, but her model house needs a roof. "
                 "Her father suggests triangle cards. Diksha leans triangle cards together over a square card. "
                 "Their tops meet at one point. Her father calls that point the apex and the square card the base. "
                 "She tries a three-sided card and a five-sided card as the bottom card too. "
                 "Each roof has one bottom card and triangles that meet at the apex.",
    "problem": "The roof cards slide apart. Diksha has to find how to lean them so they hold each other up.",
    "thread": "Continues from the prism story: the same mat, with the sorted blocks put away.",
    "leads_to": "A picture of two tents, then three tools: match the solids, build them and sort them.",
}
_S_NET = {
    "characters": ["Diksha", "Diksha's father"],
    "setting": "A craft table at home. On it lie a pink gift box, scissors, a pencil and a sheet of card.",
    "situation": "Diksha's father gives her a pink gift box with a small present inside. Diksha takes the present out. She wants "
                 "to make a second box just like it for her friend. She carefully opens the box out and presses it flat on the table. "
                 "She traces the flat shape on card and cuts it out. She draws dotted lines where the folds were. "
                 "She folds along the dotted lines, and the box comes back. Her father says the flat shape is called the net of the box.",
    "problem": "Diksha has no pattern for the box. How can she make an exact copy of it?",
    "thread": "Continues from the roofs story. Diksha and her father are now at a craft table, cutting and folding paper.",
    "leads_to": "Three tools: fold nets into solids, match nets to solids, and find the net that will not fold.",
}
_S_PARTS = {
    "characters": ["Diksha", "Isha", "Nitesh"],
    "setting": "A craft room at school. A cardboard screen stands on the table between Nitesh and the girls. "
               "Each child has a box of wooden blocks.",
    "situation": "Nitesh cannot see through the screen. Diksha holds up one box-shaped block. She and Isha must describe it "
                 "so that Nitesh can pick the same block. Saying that it has flat sides is not enough. Nitesh cannot tell which sides. "
                 "So they give the parts names. Isha taps one flat side and calls it a face. She runs a finger along a line "
                 "where two faces meet and calls it an edge. Diksha taps a point where edges meet and calls it a corner. "
                 "Isha says some people call a corner a vertex. Nitesh picks the same block from his box. "
                 "Diksha adds that a face can also be curved, like the side of a clay pot.",
    "problem": "Nitesh cannot see the block. Diksha and Isha need exact words for its parts.",
    "thread": "Continues from the gift box story. Diksha is at school now, with Isha and Nitesh.",
    "leads_to": "Three tools: label the parts of a cube, count them, and spin a die.",
}
_S_TOWER = {
    "characters": ["Isha", "Nitesh"],
    "setting": "A craft table with a box of small wooden cubes.",
    "situation": "Nitesh builds a small tower of cubes. The bottom layer is 3 rows of 3. On it sits a smaller layer of 2 rows of 2. "
                 "One cube is on top. He challenges Isha to say how many cubes he used without taking the tower apart. "
                 "Isha counts layer by layer. The bottom layer has 3 × 3 = 9 cubes. The middle layer has 2 × 2 = 4 cubes. "
                 "The top layer has 1 cube. She says the cubes she cannot see still count. 9 + 4 + 1 = 14. "
                 "Nitesh lifts the layers off one at a time, and they count 14 together.",
    "problem": "Isha cannot see every cube in the tower. How can she find the total without taking it apart?",
    "thread": "Continues from the parts story: Isha and Nitesh now use wooden cubes to build.",
    "leads_to": "Three tools: build cube towers, count every cube, and copy a cube structure.",
}
_S_ANGLE = {
    "characters": ["Isha", "Nitesh"],
    "setting": "The same craft table, now with straws, a lump of clay and a sheet of paper.",
    "situation": "Isha joins two straws at one end with clay. She opens them like two arms. "
                 "She says that two lines that meet at a point make an angle. Nitesh is making a picture frame from sticks. "
                 "Every corner of the frame must be exactly alike. He has no tool to check a corner. "
                 "He folds a sheet of paper in half and in half again. Isha opens her straws slowly until they fit the folded "
                 "corner exactly. They call that angle a right angle. "
                 "Nitesh lays the folded corner on one corner of his frame. It fits exactly, so that corner is a right "
                 "angle too. He checks the other corners the same way. One corner leans, so he turns its stick until the "
                 "folded corner fits. Now every corner of his frame is exactly alike.",
    "problem": "Nitesh needs every corner of his frame exactly alike. He has no tool to check one. "
               "How can they check a corner?",
    "thread": "Continues from the cube tower story. Isha and Nitesh put away the cubes and take out straws and paper.",
    "leads_to": "The Angle Builder tool.",
}
_S_ACUTE = {
    "characters": ["Isha", "Nitesh"],
    "setting": "The craft table. Two straw corners lie beside the folded paper corner.",
    "situation": "Isha made two straw corners for two corners of a model frame. She wants to tell Nitesh which one goes where. "
                 "Nitesh lays the paper corner on the first one. It fits inside the paper corner, so it is narrower. "
                 "He lays it on the second. It sticks out past the paper corner, so it is wider. "
                 "They want names to write on their plan. The first is called an acute angle: less than a right angle. "
                 "The second is called an obtuse angle: more than a right angle.",
    "problem": "Isha and Nitesh need names to tell the two corners apart when they write their plan.",
    "thread": "Continues from the straws and paper corner story: the paper corner and the straw angles return.",
    "leads_to": "Two tools: sort angles, and name one angle at a time.",
}
_S_CIRCLE = {
    "characters": ["Diksha", "Diksha's father"],
    "setting": "An open patch of ground near Diksha's house in the late afternoon. A wooden peg, a long string and a stick "
               "lie on the ground.",
    "situation": "Diksha's father wants a big round ring on the ground for a game. He hammers a peg into the ground. "
                 "He ties one end of a string to the peg and the other to a stick. "
                 "Diksha pulls the string tight and walks round the peg, scratching a line with the stick. "
                 "The line closes into a ring. Her father gives the parts names. The spot of the peg is the centre. "
                 "The string from the centre to the ring is the radius. A line across the ring through the peg is a diameter.",
    "problem": "Diksha and her father need a big round ring. They have only a peg, a string and a stick.",
    "thread": "Continues from the angle stories. Diksha is outside now, with her father, on open ground.",
    "leads_to": "Three tools: label a circle, find the radius or the diameter, and build a pentagon.",
}
_S_RIGID = {
    "characters": ["Isha", "Nitesh"],
    "setting": "The craft table with a straw triangle, a straw rectangle and clay joints.",
    "situation": "Isha and Nitesh want to build a small stand for a toy signboard. Nitesh holds up a straw triangle and Isha "
                 "a straw rectangle. Isha remembers the straw pentagon that leaned over when it was pushed. "
                 "A good stand must keep its shape when someone pushes it. Nitesh says a shape like that is called rigid. "
                 "They look at the triangle and the rectangle and wonder which one is rigid. "
                 "The story ends with their hands over the two shapes, before anyone pushes.",
    "problem": "They need a frame that keeps its shape when pushed. They do not know which shape to choose.",
    "thread": "Continues from the pentagon. Isha remembers in one line how it leaned over when pushed.",
    "leads_to": "The Triangle vs Rectangle tool, where the child pushes the two shapes.",
}
_S_WEBS = {
    "characters": ["Squiggly", "Wiggly"],
    "setting": "Two spider webs on a garden fence at dusk. Squiggly's web is made of triangles and Wiggly's of rectangles.",
    "situation": "Squiggly makes triangular webs and her brother Wiggly makes rectangular ones. "
                 "Every morning Squiggly checks that the walls of her web are strong. "
                 "One windy evening a gust blows. Squiggly's web hardly moves. Wiggly's web leans over into a slanting shape and sways. "
                 "Wiggly worries that a fly will escape. Squiggly looks at his rectangles. She says a thread from one corner "
                 "to the opposite corner would make triangles. Wiggly holds a thread, unsure. The story ends before the thread goes across.",
    "problem": "Wiggly's web wobbles in the wind. How can he stop its walls from leaning?",
    "thread": "Continues from the push story. The idea of a triangle that keeps its shape returns, now with two spiders.",
    "leads_to": "Two tools: add a stick across a frame, and decide if statements about rigid shapes are right or wrong.",
}

# ======================================================================================================================
# MODULE M1  SPOTTING SHAPES  (Lesson 1: Tools 1 and 2)
# ======================================================================================================================

# ---- T1: the opening (row 1 hook video, row 2 Tool 1) -----------------------------------------------------------------
# The gate fixes the opening topic as exactly [hook video, exploration tool]. The hook is a story only: it names no shape
# formally and teaches nothing. Tool 1 names no solid formally either: the child picks a block by its picture.
# PROVISIONAL, CLASH 25: Tool 1 will hold the book's 11 questions and 3 notice prompts (the question mapper homes them).
# PROVISIONAL, CLASH 37: the boy with the stepped Qutub Minar model has no name in the book, so he stays "a child".
TOPICS.append(TOPIC(
    "T1", "M1", "Shapes Around Us", ["Opener", "Qutub Minar", "Project Work"], "Understand",
    "",   # the opening carries NO topic objective
    "Diksha tries to build India Gate from her blocks. You pick a block shape for each part of a building.",
    [A("T1.C1", "Diksha's Trip to Delhi", "Understand", "", role="hook",
       textbook=["Diksha wanted to go to a big city during her summer holidays. Her father took her to Delhi and they "
                 "visited many old and new interesting monuments like the India Gate, Qutub Minar, Safdarjung Tomb, "
                 "Akshardham, the National Museum, Jantar Mantar and Sansad Bhawan. Now she is trying to make a model of "
                 "India Gate using her wooden blocks."],
       teach=["Predict first: which block could Diksha use for the top of India Gate?"],
       ncert=["opening"], key_terms=[], minutes=4,
       video=VID("Diksha's Trip to Delhi",
                 "Diksha and her father visit Delhi. She tries to build India Gate from her wooden blocks. "
                 "She wonders which block shape fits each part. It ends on that question, with no answer, "
                 "no finished model, no block placed on a part and no shape name.",
                 story=_S_HOOK, seconds=75)),
     DOER("T1.C2", "Shape Detective", "shape_detective", "Understand", "",
          applies_to="T1.C1", role="explore",
          recap=["Diksha wants a block for every part of a building.",
                 "Look at each part and pick the block that is most like it."],
          textbook=["What would happen if you removed one piece of your model?",
                    "Would the model still look like the original building?",
                    "In what ways could you make the model even better?",
                    "I have made something. Look at my Qutub Minar.",
                    "The Qutub Minar is a World Heritage site and the tallest building made up of bricks. "
                    "It has 5 storeys and 379 stairs."],
          # note_boxes is a Note for Teachers: a coverage id only (CLASH 30); nothing of it is shown to the child.
          ncert=["ch1.model_talk", "ch1.qutub_say", "ch1.qutub_fact", "ch1.note_boxes"],
          key_terms=[], minutes=8,
          # QUESTION MAPPER (step 5), CLASH 25: the 11 book questions of Tool 1 in the book's order (the 3 notice prompts are the
          # tool's own, tools_1.py). The exploration tool names no solid, so every answer uses everyday words (a flat block, a tall
          # block, a round block, a can). The book prints no answer: each one is a "Sample answer" or "From the picture".
          # project1 reads "Observe a street ..." (the printed "Encourage learners" is a teacher line, CLASH 50).
          items=[
              FIO("ch1.model1", "Opening, Task",
                  "Try to make a model of the buildings shown here using blocks.",
                  ["Look at the two buildings on the screen.",
                   "Pick a block for each part you see.",
                   "Place the blocks to build your model."],
                  "Sample answer: for the gateway, a wide block with two tall blocks beside it. "
                  "For the hut, a round block with a half-round block on top. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.model_q1", "Opening, Q1",
                  "What parts of the building have you shown in your model (for example, roof, pillars, base, etc.)?",
                  ["Look at the model you built.",
                   "Name each part of it."],
                  "Sample answer: the base, the pillars or towers, and the roof. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.model_q2", "Opening, Q2",
                  "Why did you select these parts?",
                  ["Think about the parts you notice first in the building."],
                  "Sample answer: they are the parts you notice first. "
                  "Without them the building would not look the same. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.model_q3", "Opening, Q3",
                  "What shapes will model these parts well?",
                  ["Look at the blocks you chose for each part."],
                  "Sample answer: a long flat block for the base. Tall blocks for the pillars. "
                  "A flat block for the roof. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.model_q4", "Opening, Q4",
                  "How is your model similar to the picture of the real building?",
                  ["Put your model beside the picture.",
                   "Look for the parts that match."],
                  "Sample answer: it has a base, pillars and a roof, like the real building. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.model_q5", "Opening, Q5",
                  "How is it different from the real building?",
                  ["Look for what your model leaves out."],
                  "Sample answer: my model is smaller. Its blocks have no windows, no carvings and no colour. "
                  "Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.project1", "Project Work",
                  "Observe a street carefully and make a model showing the main buildings on the street.",
                  ["Look at the street picture on the screen.",
                   "Pick a shape for each building.",
                   "Place the shapes along the road."],
                  "Sample answer: boxes for the houses and round shapes for the huts. A long flat box makes the road. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.qutub_q1", "Qutub Minar, Q1",
                  "Do you think it looks like the Qutub Minar?",
                  ["Look at the stack of boxes and at the tower."],
                  "Sample answer: a little. Both get narrower towards the top. "
                  "The tower slopes smoothly and the boxes are stepped. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.qutub_q2", "Qutub Minar, Q2",
                  "What shape would you use if you made a model of the Qutub Minar? Why?",
                  ["Look at the tower from its bottom to its top."],
                  "Sample answer: round cans, one on top of another, each smaller than the one below. "
                  "The tower looks round and gets narrower. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.qutub_q3", "Qutub Minar, Q3",
                  "How many such shapes will you use?",
                  ["Think about the 5 storeys of the tower.",
                   "Use one shape for each storey."],
                  "Sample answer: 5, one for each storey. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.puzzle1", "Puzzling Shapes, Q1",
                  "Identify the hidden shapes and write their names.",
                  ["Look at the red outlines.",
                   "Trace each outline with your finger.",
                   "Find one shape at a time."],
                  "From the picture: 6 shapes. A circle, a square, a rectangle, 2 triangles and a cylinder. "
                  "The cylinder is a solid shape and the others are flat.",
                  kind="exercise"),
          ])],
    topic_type="framing"))

# ---- T2: Guess the Shape (row 3 concept video, row 4 Tool 2) -----------------------------------------------------------
# PROVISIONAL, CLASH 6: Lesson 1 spans T1 and T2 because the opening topic must be exactly [hook, Tool 1].
# PROVISIONAL, CLASH 21: no one book concept; the concept is "telling shapes apart by their sides, corners and faces".
# PROVISIONAL, CLASH 10: one light line in the story separates a flat shape (sides, corners) from a solid (faces).
# PROVISIONAL, CLASH 13: Tool 2 runs four short stages (three clues, sort objects, sort flat cards, cut shapes).
# PROVISIONAL, CLASH 16: the cuts (puzzle2 to puzzle4) ride on Tool 2 because its approved purpose names them.
# PROVISIONAL, CLASH 40: the row 3 hidden block is none of Tool 2's own rounds. CLASH 41: face and corner are everyday words here;
#   row 11 is the only video that defines face, edge and corner.
TOPICS.append(TOPIC(
    "T2", "M1", "Guess the Shape", ["Bricks", "Shapes Along the Border", "Card Game", "Puzzling Shapes"], "Apply",
    "Students tell shapes apart by their sides, corners and faces, and name a shape from three clues.",
    "Diksha's father hides a block and gives clues. You guess the shape and sort shapes by their parts.",
    [A("T2.C1", "Telling Shapes Apart", "Understand",
       "Students use clues about sides, corners and flat or curved parts to tell one shape from another.",
       role="story", key_terms=["clue", "side", "corner", "face"], minutes=5,
       teach=["Predict first: a long block and a half-round block both have flat faces and corners. What clue could tell them apart?",
              "Diksha's father says, I have a curved side. Only the half-round block has one.",
              "The long block has flat faces only. The half-round block has a curved side too.",
              "Sides, corners and flat or curved parts tell one shape from another.",
              "A flat shape has sides and corners. A solid has faces."],
       video=VID("The Hidden Block",
                 "Diksha's father hides a block from her wooden set and gives three clues. The first two clues fit "
                 "two different shapes and the third decides. One light line tells a flat shape from a solid. The "
                 "block is none of Tool 2's own rounds, and the video sorts and cuts nothing.",
                 new_idea="Sides, corners and flat or curved parts tell one shape from another.",
                 story=_S_CLUES, seconds=80)),
     DOER("T2.C2", "Guess the Shape", "guess_shape", "Apply",
          "Students name a shape from three clues, then sort objects and flat shapes by their sides, corners and faces.",
          applies_to="T2.C1", key_terms=["clue", "side", "corner", "face"], minutes=7,
          recap=["Sides, corners and flat or curved parts tell one shape from another."],
          textbook=["Earlier, people made buildings with clay bricks, stone blocks or wood. Today we also use concrete "
                    "blocks, hollow blocks, etc."],
          ncert=["ch1.bricks_text"],
          # QUESTION MAPPER (step 5): 9 book questions, in the tool's stage order (the bricks, the border objects, the flat cards,
          # then the cuts, CLASH 13), so cards come before puzzle2 to puzzle4 although the book prints the cuts first. The three
          # clues are the tool's own interaction (CLASH 24), not a book question.
          # E7: the border sketches are not numbered and no key is printed, so the border answers are "for example". The two cheese
          # pieces are pyramids with small holes, as the book draws them. A square face counts as a rectangular face (CLASH 51).
          # The cut lines are not unique (E17), so every cut answer is a Sample answer.
          items=[
              FIO("ch1.bricks_q", "Bricks",
                  "What is common to all of these bricks?",
                  ["Look at the clay brick, the stone block and the wooden block.",
                   "Look at their faces and corners."],
                  "From the picture: all three have a box shape. They have flat faces and square corners.",
                  kind="prompt"),
              FIO("ch1.border1", "Border, Q1",
                  "Follow these instructions for the shapes along the border. "
                  "Colour all shapes with a rectangular face in red.",
                  ["Look at each shape.",
                   "Colour it red if it has a rectangular face."],
                  "From the picture, for example: the dice, the erasers, the Rubik's cube and the gift box. "
                  "The wooden wedge and the cake slice too.",
                  kind="exercise"),
              FIO("ch1.border2", "Border, Q2",
                  "Draw a smiley on shapes with a triangular face.",
                  ["Look at each shape.",
                   "Draw a smiley if it has a triangular face."],
                  "From the picture, for example: the wooden wedge and the cake slice. "
                  "The two cheese pieces and the two pyramid drawings too.",
                  kind="exercise"),
              FIO("ch1.border3", "Border, Q3",
                  "Draw a star on shapes with a curved face.",
                  ["Look at each shape.",
                   "Draw a star if it has a curved face."],
                  "From the picture: the 3 balls, one of them a football. The 3 cans or bottles. "
                  "The ice-cream cone and the party hat.",
                  kind="exercise"),
              FIO("ch1.border4", "Border, Q4",
                  "Colour all shapes with no corner in blue.",
                  ["Look at each shape.",
                   "Colour it blue if it has no corner."],
                  "From the picture: the 3 balls and the 3 cans or bottles.",
                  kind="exercise"),
              FIO("ch1.cards", "Card Game",
                  "Sort the 2D-shape cards given at the end of the book into three groups according to their sides. "
                  "Draw the sorted shapes in the space given below. Explain why you sorted your shapes in this way.",
                  ["The six shape cards are on the screen.",
                   "Look at the sides of each card: straight, curved or both.",
                   "Drag each card to its group.",
                   "Say why you put the cards together."],
                  "Sample answer: only straight sides: the square and the triangle. Only a curved side: the oval and the circle. "
                  "Straight and curved sides: the quarter circle and the semicircle. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.puzzle2", "Puzzling Shapes, Q2",
                  "Draw 2 lines to divide the triangle into 1 square and 2 triangles.",
                  ["Look at the big triangle on the dot grid.",
                   "Draw a line from the middle of the top side straight down to the slanted side.",
                   "Draw a line from the middle of the left side straight across to the slanted side."],
                  "Sample answer: the two lines meet on the slanted side. They make 1 square and 2 small triangles. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.puzzle3", "Puzzling Shapes, Q3",
                  "Draw 2 lines to divide the square into 3 triangles.",
                  ["Look at the square on the dot grid.",
                   "Pick a dot on the top side.",
                   "Join it to the two bottom corners."],
                  "Sample answer: the two lines make 3 triangles. One is on the left, one in the middle and one on the right. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.puzzle4", "Puzzling Shapes, Q4",
                  "Draw lines to show the cuts needed on the shapes in the left column to get the smaller shapes on the right.",
                  ["Look at each shape on the left and at the pieces on the right.",
                   "Draw the lines where the shape must be cut.",
                   "Count the pieces to check."],
                  "Sample answer: A: cut straight down at each pointed end. You get a rectangle and 2 triangles. "
                  "B: cut from the bottom middle to the two top corners. Then cut straight up the middle. You get 4 triangles. "
                  "C: cut across each corner with a straight line. You get 3 small triangles and a 6-sided piece. "
                  "Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["clue", "side", "corner", "face"]))

# ======================================================================================================================
# MODULE M2  SOLID SHAPES  (Lessons 2 to 5: Tools 3 to 14)
# ======================================================================================================================

# ---- T3: Prisms and Pyramids (rows 5, 6 videos, row 7 image, rows 8 to 10 Tools 3, 4, 5) ---------------------------------------
# Two concept videos and one comparison image, then THREE tools back to back (Lesson 2's three activities: Match the 3D Shape,
# Build Your Own 3D Shape, Prisms and Pyramids; config tools_in_a_row, CLASH 55). All three apply to the image concept T3.C3, the
# last medium before them, as the gate requires.
# PROVISIONAL, CLASH 26: the tools follow the row 7 IMAGE; the image brings a new real-life example (new_context=True).
# PROVISIONAL, CLASH 32: the row 7 image draws a real prism and a real pyramid truly, with their face shapes marked.
# PROVISIONAL, CLASH 39 and 42: three media before the tools. Division of labour: row 5 the prism alone, row 6 the pyramid alone,
#   row 7 the only place the two stand side by side (two real tents, not the roofs of row 6), then Tool 3 names, Tool 4 builds,
#   Tool 5 sorts.
# PROVISIONAL, CLASH 43: the row 7 image is two tents (a camping tent and a tent with a square floor), in one plain tent colour.
# PROVISIONAL, CLASH 15: the curved solids of craft1, sort1 and sort4 ride on Tool 5 as "not every solid is a prism or a pyramid".
# PROVISIONAL, CLASH 9: for a pyramid the word is "the bottom face (base)" and "apex" is kept; for a prism "the two end faces".
# PROVISIONAL, CLASH 34: one colour per kind of solid (prisms blue, pyramids pink, as the book's first spread).
TOPICS.append(TOPIC(
    "T3", "M2", "Prisms and Pyramids", ["Craft", "Prisms and Pyramids", "Sorting 3D Shapes"], "Analyze",
    "Students pick out a prism and a pyramid by their faces and tell the two kinds of solid apart.",
    "Diksha sorts her blocks and makes roofs. You find prisms and pyramids and tell them apart.",
    [A("T3.C1", "What Is a Prism?", "Understand",
       "Students pick out a prism by its two matching end faces joined by rectangles.",
       role="story", key_terms=["prism", "end face", "rectangle"], misconceptions=["M_SH_1", "M_SH_2"], minutes=5,
       teach=["Predict first: what do the blocks that make a straight pillar have in common?",
              "Look at both ends of each block. The two end faces match.",
              "The sides between the two ends are rectangles.",
              "A prism has two matching end faces joined by rectangles."],
       video=VID("Diksha's Prism Blocks",
                 "Diksha sorts her blocks and finds some with two matching end faces joined by rectangles. "
                 "Examples are triangular, square and hexagonal. It shows no pyramid, no cube and no count of faces.",
                 new_idea="A prism has two matching end faces joined by rectangles.",
                 story=_S_PRISM, seconds=70)),
     A("T3.C2", "What Is a Pyramid?", "Understand",
       "Students pick out a pyramid by its one bottom face and triangular faces that meet at one point.",
       role="story", key_terms=["pyramid", "apex", "base"], misconceptions=["M_SH_2", "M_SH_8"], minutes=5,
       teach=["Predict first: Diksha leans triangle cards over a square card. Where do their tops meet?",
              "All the triangle tops meet at one point. That point is the apex.",
              "The square card at the bottom is the base.",
              "A pyramid has one bottom face and triangular faces that meet at the apex."],
       video=VID("Diksha's Roofs",
                 "Diksha makes roofs from triangle cards that all meet at one point. She finds that a pyramid has "
                 "one bottom face and triangular faces meeting at the apex. Examples are triangular, square and "
                 "pentagonal. It shows no prism beside them.",
                 new_idea="A pyramid has one bottom face and triangular faces that meet at one point, the apex.",
                 story=_S_PYRAMID, seconds=70)),
     A("T3.C3", "Prism or Pyramid?", "Analyze",
       "Students say how a prism differs from a pyramid by looking at their faces.",
       role="image", key_terms=["prism", "pyramid"], misconceptions=["M_SH_2"], minutes=4,
       teach=["Predict first: both tents have triangle faces. Are they the same kind of solid?",
              "The camping tent has two matching triangle ends. Rectangles join them.",
              "The other tent has a square floor. Its triangles meet at one point at the top.",
              "Look again. Do the triangles of each tent meet at one point?",
              "A triangle face alone does not make a pyramid."],
       textbook=["What is the difference between a prism and a pyramid? Discuss."],
       ncert=["ch1.prism_pyr_talk"],
       image=IMG("Two Tents",
                 "Two real tents side by side: one with two matching triangle ends and rectangle faces, one with a "
                 "square floor and triangles that meet at one point. Their face shapes are marked, with no counts "
                 "and no solid names. The videos use blocks and card roofs and the three tools draw solids, so "
                 "none of them shows a real object. Both tents have triangle faces, which shows that a triangle "
                 "alone does not make a pyramid.",
                 placement="main", new_context=True, style="illustration",
                 real_life="two tents standing side by side on plain green grass, with a gap between them",
                 shows="a camping tent with two matching triangle ends and rectangle sides, beside a second tent. "
                       "The second tent has a square floor. Its four triangle sides meet at one point at the top. "
                       "Both tents are the same plain colour. The face shapes are marked with light outlines. "
                       "Triangles get the same marking on both tents.",
                 caption="Look at the faces of the two tents. How are they different?",
                 visuals=["prism_tent", "pyramid_tent"])),
     # Tool 3 (new, CLASH 54): Lesson 2, Activity 1. No book question homes here (config no_book_question_tools); the name-matching
     # stage was Stage 1, Match, of the old single tool (SPLIT NOTES in media_decisions.md). The follow-on of the book's
     # solids_q1 (name a solid from its description) was considered and kept on Tool 9 (CLASH 59).
     DOER("T3.C4", "Match the 3D Shape", "match_3d_shape", "Remember",
          "Students match the name of each solid, such as a triangular prism, a cube or a square pyramid, to its picture.",
          applies_to="T3.C3", key_terms=["prism", "pyramid", "cube"],
          misconceptions=["M_SH_1", "M_SH_2"], minutes=5),
     # Tool 4 (new, CLASH 54): Lesson 2, Activity 2. No book question homes here; it was Stage 2, Build from faces, of the old tool.
     DOER("T3.C5", "Build Your Own 3D Shape", "build_3d_shape", "Apply",
          "Students build a triangular prism, a square pyramid and a cube from blocks, then name each solid they built.",
          applies_to="T3.C3", key_terms=["prism", "pyramid", "cube", "face"],
          misconceptions=["M_SH_1", "M_SH_2"], minutes=6),
     # Tool 5 (the old Tool 3, narrowed: Lesson 2, Activity 3, the Prism or Pyramid sorting only).
     DOER("T3.C6", "Prisms and Pyramids", "prisms_pyramids", "Apply",
          "Students sort solids one by one as prism or pyramid by looking at their faces.",
          applies_to="T3.C3", key_terms=["prism", "pyramid", "face"],
          recap=["A prism has two matching end faces joined by rectangles.",
                 "A pyramid has one bottom face and triangular faces that meet at one point."],
          misconceptions=["M_SH_1", "M_SH_2", "M_SH_8"], minutes=8,
          # note_venn is a Note for Teachers: a coverage id only (CLASH 30).
          ncert=["ch1.note_venn"],
          # QUESTION MAPPER (step 5): 12 book questions, one under the cap of 13: add nothing (CLASH 7). The Match and Build stages
          # of the old tool are now Tools 3 and 4 (CLASH 54). The sorting stage is the three-circle sort of the book. E3: the set
          # of solids to sort is not stated, so the answers say "for example" and use the ten solids of CLASH 52. E4: a rectangular
          # pyramid is never drawn, so sort3_q reads it as a pyramid with a rectangle base (a square pyramid); a square face counts
          # as a rectangular face (CLASH 51). The cube is answered as a square prism, not left beside the blue prisms as another
          # family (CLASH 47). The answers about the prisms and pyramids read the book's own pictures.
          items=[
              FIO("ch1.craft1", "Craft, Q1",
                  "Make a sphere-like shape with paper strips.",
                  ["Take paper strips of the same length.",
                   "Join their ends at the top and at the bottom.",
                   "Bend the strips outwards to make a ball."],
                  "Sample answer: a ball of curved strips that meet at the top and at the bottom. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.prism_q1", "Prisms, Q1",
                  "What shape of face is common to all the prisms?",
                  ["Tap the faces of the triangular, square and hexagonal prisms.",
                   "Look for the shape that every prism has."],
                  "From the picture: a rectangle. Every prism has rectangle faces.",
                  kind="prompt"),
              FIO("ch1.prism_q2", "Prisms, Q2",
                  "What other shapes do these prisms have?",
                  ["Tap the faces that are not rectangles."],
                  "From the picture: the triangular prism has triangles. The square prism has squares. "
                  "The hexagonal prism has hexagons.",
                  kind="prompt"),
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
                  "From the picture: a triangle. Every pyramid has triangle faces.",
                  kind="prompt"),
              FIO("ch1.pyr_q2", "Pyramids, Q2",
                  "All the triangular faces meet at _________________ point.",
                  ["Look at where the triangle faces of a pyramid join."],
                  "From the picture: one point, at the top. It is called the apex.",
                  kind="prompt"),
              FIO("ch1.pyr_q3", "Pyramids, Q3",
                  "Identify any other shape in each of the pyramids",
                  ["Look at the face the pyramid stands on."],
                  "From the picture: the bottom face. The square pyramid has a square. "
                  "The pentagonal pyramid has a pentagon. The triangular pyramid has only triangles.",
                  kind="prompt"),
              FIO("ch1.cube_prism", "Prisms and Pyramids, cube",
                  "Is a cube also a prism?",
                  ["Look at the square prism and at a cube.",
                   "Look at their end faces and their side faces."],
                  "From the picture: yes. A cube has 2 square ends joined by 4 squares, so it is a square prism.",
                  kind="prompt"),
              FIO("ch1.sort1", "Sorting 3D Shapes, (1)",
                  "Write the names of 3D shapes in the correct places. "
                  "A: All faces look the same. B: All faces do not look the same.",
                  ["Look at the faces of each solid.",
                   "Drag the solid to circle A or circle B."],
                  "Sample answer, for example: A: cube. B: cuboid, cylinder, cone, square pyramid, triangular prism. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.sort3", "Sorting 3D Shapes, (3)",
                  "Write the names of 3D shapes in the correct places. A: Shapes with rectangular faces. "
                  "B: Shapes with triangular faces. The overlap: Shapes with both rectangular and triangular faces.",
                  ["Look at the faces of each solid.",
                   "A square face counts as a rectangular face.",
                   "Drag the solid to A, to B or to the overlap."],
                  "Sample answer, for example: A: cube, cuboid, hexagonal prism. B: triangular pyramid, pentagonal pyramid. "
                  "Overlap: triangular prism, square pyramid. The sphere, cone and cylinder fit neither circle. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.sort3_q", "Sorting 3D Shapes, circles",
                  "In which circle did you write triangular prism and rectangular pyramid?",
                  ["Look at the faces of both solids.",
                   "A rectangular pyramid has a rectangle at the bottom. A square pyramid is like it."],
                  "Sample answer: in the part where the two circles overlap. "
                  "Both have rectangle faces and triangle faces.",
                  kind="prompt"),
              FIO("ch1.sort4", "Sorting 3D Shapes, curved and flat",
                  "Let us sort shapes in another way. Using circles like the ones you just used, can you sort shapes "
                  "into the categories “Shapes with curved faces” and “Shapes with flat faces”?",
                  ["Look at the faces of each solid.",
                   "Drag it to curved, to flat or to the overlap."],
                  "Sample answer: only curved: sphere. Only flat: cube, cuboid, prisms and pyramids. "
                  "Both, in the overlap: cone and cylinder. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["prism", "pyramid", "apex", "base"]))

# ---- T4: Nets of 3D Shapes (row 11 concept video, rows 12 to 14 Tools 6, 7, 8) ------------------------------------------
# One concept video, then THREE tools back to back (Lesson 3's activities: Nets of 3D Shapes = Fold It, Which Net Makes Which Shape,
# Find the Wrong Net; CLASH 54, 55). All three apply to the net video T4.C1.
# PROVISIONAL, CLASH 27: nets come before faces, edges and corners although the book teaches C3 first; the story needs only
#   the picture of a box opened out flat and folded back.
# PROVISIONAL, CLASH 8: no bare "six squares make a cube"; valid nets are shown as figures only.
TOPICS.append(TOPIC(
    "T4", "M2", "Nets of 3D Shapes", ["Craft", "Nets"], "Apply",
    "Students describe a net as a solid opened out flat and match nets to the solids they fold into.",
    "Diksha opens a gift box out flat and folds it back. You fold nets into solids and find a net that will not fold.",
    [A("T4.C1", "What Is a Net?", "Understand",
       "Students describe a net as a solid opened out flat that folds back into the same solid.",
       role="story", key_terms=["net", "fold"], misconceptions=["M_SH_7"], minutes=5,
       teach=["Predict first: Diksha opens a gift box and lays it flat. Can she fold it back?",
              "She folds along the dotted lines, and the box comes back.",
              "The flat shape is called a net.",
              "A net is a solid opened out flat. Folding it brings the solid back."],
       textbook=["Diksha has folded open and flattened a box to see what an open box looks like. This is called the net "
                 "of the box. If you fold along the dotted lines, you will get the box back."],
       ncert=["ch1.net_text"],
       video=VID("Diksha's Gift Box",
                 "Diksha opens out a gift box, lays it flat and folds it back into the box. It shows this one net "
                 "only: never a net that fails and never a cube net.",
                 new_idea="A net is a solid opened out flat, and folding it brings the solid back.",
                 story=_S_NET, seconds=65)),
     # Tool 6 (the old Tool 4, narrowed: Lesson 3, Activity 1, Fold It only).
     DOER("T4.C2", "Nets of 3D Shapes", "nets", "Apply",
          "Students fold the net of a cube, then of a cuboid or a pyramid, into a solid.",
          applies_to="T4.C1", key_terms=["net", "fold"], misconceptions=["M_SH_7"], minutes=5,
          recap=["A net is a solid opened out flat. Folding it brings the solid back."],
          # QUESTION MAPPER (step 5), changed 12 Nov 2026 (CLASH 59): 1 book question stays here, craft2 (fold the nets of the end
          # pages into the solids). The three questions that are 'which net makes which shape' or 'which net does not fold' moved:
          # solids_q3 and solids_q5 to Tool 7, solids_q4 to Tool 8. E1 (on Tool 8): of the printed nets A to D only B and D fold; A has
          # both end flaps on the same side and C has only 2 of the 4 triangles its pyramid needs, so A and C are never shown as nets
          # that fold. Every answer is checked by counting the faces and folding each net (SOLUTION_NOTES). The nets of craft2 are on
          # the end pages of the book (CLASH 35).
          items=[
              FIO("ch1.craft2", "Craft, Q2",
                  "Use the nets given at the end of the book to make the models shown below.",
                  ["The nets are on the screen.",
                   "Fold each net along its dotted lines.",
                   "Match each net to its solid: three prisms and three pyramids."],
                  "Sample answer: each net folds into the solid shown beside it. Your answer may differ.",
                  kind="exercise"),
          ]),
     # Tool 7 (new, CLASH 54): Lesson 3, Activity 2. Homes the two book questions that match a net to its solid (CLASH 59).
     DOER("T4.C3", "Which Net Makes Which Shape", "which_net", "Apply",
          "Students match each net to the solid it folds into, such as a cube, a cuboid or a square pyramid.",
          applies_to="T4.C1", key_terms=["net", "fold", "cube"], misconceptions=["M_SH_7"], minutes=6,
          recap=["A net is a solid opened out flat. Folding it brings the solid back."],
          # Re-homed from the old net tool on 12 Nov 2026 (CLASH 59): solids_q3 (match four nets to four solids) and solids_q5
          # (which solid has these pieces in its net). Both answers are checked by counting the faces of each net (SOLUTION_NOTES).
          items=[
              FIO("ch1.solids_q3", "Solids and nets, Q3",
                  "Match the following nets to the appropriate solids given below.",
                  ["Count the faces of each net.",
                   "Net (1) has 4 triangles. Net (2) has a rectangle and 2 circles.",
                   "Net (3) has 6 rectangles. Net (4) has 3 rectangles and 2 triangles.",
                   "Drag each net to the solid it folds into."],
                  "From the picture: (1) with (b), (2) with (d), (3) with (a), (4) with (c).",
                  kind="exercise"),
              FIO("ch1.solids_q5", "Solids and nets, Q5",
                  "Nitesh cuts up a net on the folds. Here are its pieces. "
                  "Which solid has the above pieces in its net?",
                  ["Count the pieces: 1 pentagon and 5 triangles.",
                   "Find the solid with a pentagon and 5 triangles."],
                  "From the picture: d, the pentagonal pyramid. It has 1 pentagon and 5 triangles.",
                  kind="exercise"),
          ]),
     # Tool 8 (new, CLASH 54): Lesson 3, Activity 3. Homes the book question that asks which nets fold and which do not (CLASH 59).
     DOER("T4.C4", "Find the Wrong Net", "wrong_net", "Analyze",
          "Students find the one net that will not fold into a given solid and say why it will not.",
          applies_to="T4.C1", key_terms=["net", "fold"], misconceptions=["M_SH_7"], minutes=6,
          recap=["A net folds into a solid only when every face lands once, with no gap."],
          # Re-homed from the old net tool on 12 Nov 2026 (CLASH 59): solids_q4. E1: of the printed nets A to D only B and D fold; A has
          # both end flaps on the same side and C has only 2 of the 4 triangles its pyramid needs, so A and C are never shown as nets
          # that fold.
          items=[
              FIO("ch1.solids_q4", "Solids and nets, Q4",
                  "Which of these nets can be folded to make a solid of the kind given below?",
                  ["Fold each net on the screen.",
                   "See if it closes into the solid below it.",
                   "A: both end flaps are on the same side. One end stays open.",
                   "C: the pyramid needs 4 triangles, but C has only 2."],
                  "From the picture: B and D fold into the solid below. A and C do not.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["net", "fold"]))

# ---- T5: Faces, Edges and Corners (row 15 concept video, rows 16 to 18 Tools 9, 10, 11) ----------------------------------------
# One concept video, then THREE tools back to back (Lesson 4's activities: Faces Edges and Corners = Label the Cube, Count and
# Win, Spin the Shape; CLASH 54, 55). All three apply to the parts video T5.C1.
# PROVISIONAL, CLASH 9: the word is "corner"; "vertex" is not a key term (at most once as a second name, in the story).
# PROVISIONAL, CLASH 19: try5 (c), a pentagonal prism the chapter never shows, rides on Tool 9.
# PROVISIONAL, CLASH 41: the row 15 video points to the three parts on ONE block and counts nothing (no F, V, E, no F+V-E).
TOPICS.append(TOPIC(
    "T5", "M2", "Faces, Edges and Corners", ["Faces, Corners and Edges", "Let Us Observe", "Model Challenge"], "Apply",
    "Students name, count and compare the faces, edges and corners of solids.",
    "Diksha and Isha describe a block by its parts. You count faces, edges and corners.",
    [A("T5.C1", "Parts of a Solid", "Remember",
       "Students point to the faces, edges and corners of a solid and say what each one is.",
       role="story", key_terms=["face", "edge", "corner"],
       teach=["Predict first: Isha taps a flat side and calls it a face. What might she call a line where two faces meet?",
              "A line where two faces meet is an edge. A point where edges meet is a corner.",
              "A face can be flat or curved, like the side of a clay pot.",
              "A solid has faces, edges and corners."],
       misconceptions=["M_SH_3", "M_SH_4", "M_SH_5", "M_SH_9"], minutes=5,
       video=VID("Describe the Block",
                 "Diksha and Isha describe a block to Nitesh. They use its flat faces, edges and corners. It counts "
                 "nothing and states no rule about the counts.",
                 new_idea="A solid has faces, edges and corners.",
                 story=_S_PARTS, seconds=85)),
     # Tool 9 (the old Tool 5, narrowed: Lesson 4, Activity 1, Label the Cube only).
     DOER("T5.C2", "Faces Edges and Corners", "faces_edges_corners", "Apply",
          "Students point to the faces, edges and corners of a cube and name each one.",
          applies_to="T5.C1", key_terms=["face", "edge", "corner"],
          recap=["A solid has faces, edges and corners."],
          misconceptions=["M_SH_3", "M_SH_4", "M_SH_5", "M_SH_9"], minutes=6,
          textbook=["Each one is different. How? Discuss."],
          ncert=["ch1.solids_q2"],
          # QUESTION MAPPER (step 5), changed 12 Nov 2026 (CLASH 59): 6 book questions stay here (the sorts by flat faces and straight
          # edges, the riddles solids_q1 and the model challenge try5). craft3 and fve moved to Tool 10 (counting), observe1 to observe3
          # and border5 to Tool 11 (die, opposite faces). E2, E3: the sorts do not fit every solid, so the answers say so;
          # the set is the ten solids of CLASH 52. E5: f) fits a cube and a cuboid. E21: try5 c) is a solid
          # the chapter never shows (CLASH 19): the answer says "a prism with two 5-sided ends". Every sum on this tool is true.
          items=[
              FIO("ch1.sort_faces", "Sorting by flat faces",
                  "Sort 3D shapes by the number of flat faces. Write their names here.",
                  ["Count the flat faces of each solid.",
                   "Drag the solid to its column."],
                  "Sample answer: 1: cone. 2: cylinder. 4: triangular pyramid. 5: square pyramid, triangular prism. "
                  "6: cube, cuboid, pentagonal pyramid. 8: hexagonal prism. The sphere has no flat face. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.three_faces", "Sorting by flat faces, 3 faces",
                  "Can you construct a 3D shape with 3 flat faces?",
                  ["Try to build one on the screen."],
                  "Sample answer: a solid with only flat faces needs at least 4 faces. "
                  "A cylinder cut in half along its length has 3 flat faces and 1 curved face. "
                  "Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.sort_edges", "Sorting by straight edges",
                  "Now sort 3D shapes by the number of straight edges. Write their names here.",
                  ["Count the straight edges of each solid.",
                   "Drag the solid to its column."],
                  "Sample answer: 6: triangular pyramid. 8: square pyramid. 9: triangular prism. 12: cube and cuboid. "
                  "The pentagonal pyramid has 10 and the hexagonal prism has 18, so they fit no column. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.sort2", "Sorting 3D Shapes, (2)",
                  "Write the names of 3D shapes in the correct places. "
                  "A: Shapes with curved edges. B: Shapes with straight edges.",
                  ["Look at the edges of each solid.",
                   "Drag the solid to circle A or circle B."],
                  "Sample answer: A: cone, cylinder. B: cube, cuboid, prisms and pyramids. The sphere has no edges. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.solids_q1", "Solids, Q1",
                  "Match the pictures to the descriptions and name the shapes. "
                  "a) I have 5 faces and 5 corners. I have 8 edges. 1 of my faces is a square and 4 of my faces are "
                  "triangles. b) I have 1 flat face, 1 curved face, and 1 edge. "
                  "c) I have 1 curved face. I have no edges or corners. "
                  "d) I have 2 flat faces, 1 curved face, and 2 edges. I have no corners. "
                  "e) I have 5 faces, 6 corners, and 9 edges, and 2 of my faces are triangles. "
                  "f) I have 6 faces, 12 edges, and 8 corners.",
                  ["Read one clue at a time.",
                   "Match it with a solid on the screen.",
                   "Name the solid."],
                  "From the picture: a) square pyramid. b) cone. c) sphere. d) cylinder. e) triangular prism. "
                  "f) cube or cuboid, because both fit.",
                  kind="exercise"),
              FIO("ch1.try5", "Model challenge",
                  "Model challenge. Can you make a model of solid shapes which has a) 12 straws and 8 clay balls? "
                  "b) 9 straws and 6 clay balls? c) 15 straws and 10 clay balls? d) 10 straws and 6 clay balls?",
                  ["Straws are the edges and clay balls are the corners.",
                   "Build a solid for each count and check it.",
                   "c) Try two matching flat ends joined by straws.",
                   "d) Try one flat base with straws that meet at one top ball."],
                  "Sample answer: a) a cube or a cuboid. b) a triangular prism. "
                  "c) a prism with two 5-sided ends. d) a pentagonal pyramid. Your answer may differ.",
                  kind="exercise"),
          ]),
     # Tool 10 (new, CLASH 54): Lesson 4, Activity 2. Homes the book's table of counts and its F+V−E question (CLASH 59).
     DOER("T5.C3", "Count and Win", "count_and_win", "Apply",
          "Students count the faces, edges and corners of a cube, a cuboid, a triangular prism and a square pyramid.",
          applies_to="T5.C1", key_terms=["face", "edge", "corner"],
          recap=["A solid has faces, edges and corners."],
          misconceptions=["M_SH_3", "M_SH_4"], minutes=6,
          # Re-homed from the old tool on 12 Nov 2026 (CLASH 59): craft3 (count F, V and E of five solids and fill the table) and fve
          # (the relation F+V−E, worked on that table). Every sum on this tool is true (F+V−E is 2 for the five solids).
          items=[
              FIO("ch1.craft3", "Craft, Q3",
                  "Now try to make the above shapes using straws and plasticine/thread and fill in the table.",
                  ["Build each solid. Straws are the edges and clay balls are the corners.",
                   "Count the faces F, the corners V and the edges E of each solid.",
                   "Write the three counts in the table."],
                  "From the picture (F, V, E): cube 6, 8, 12. Cuboid 6, 8, 12. Triangular pyramid 4, 4, 6. "
                  "Square pyramid 5, 5, 8. Triangular prism 5, 6, 9.",
                  kind="exercise"),
              FIO("ch1.fve", "Craft, F+V−E",
                  "Identify any relationship that you may find between the number of faces (F), edges (E), and corners (V). "
                  "Calculate F+V−E in each case. What do you notice?",
                  ["Cube: 6 + 8 − 12 = 2",
                   "Cuboid: 6 + 8 − 12 = 2",
                   "Triangular pyramid: 4 + 4 − 6 = 2",
                   "Square pyramid: 5 + 5 − 8 = 2",
                   "Triangular prism: 5 + 6 − 9 = 2"],
                  "From the picture: F+V−E is 2 for all five solids. So F+V is 2 more than E in each one.",
                  kind="prompt"),
          ]),
     # Tool 11 (new, CLASH 54): Lesson 4, Activity 3. Homes the four book questions on a die, a coloured cube and opposite faces.
     DOER("T5.C4", "Spin the Shape", "spin_shape", "Understand",
          "Students turn a die or a cuboid to find which faces are opposite and which faces touch.",
          applies_to="T5.C1", key_terms=["face", "opposite face"],
          recap=["A solid has faces, edges and corners."],
          misconceptions=["M_SH_5", "M_SH_9"], minutes=6,
          # Re-homed from the old tool on 12 Nov 2026 (CLASH 59): observe1 to observe3 (die and coloured cube) and border5 (circle the
          # shapes whose opposite faces look the same). E6: the die answers are for a usual die (the tool's die; VISUAL_KEY die).
          # E7: border5 is unclear, so its answer is "for example" (CLASH 28). Only 1, 2 or 3 faces of a die or a cube can be seen at once.
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
                  "Sample answer: on a usual die, a) 5, b) 4, c) 3. Opposite faces add up to 7.",
                  kind="prompt"),
              FIO("ch1.observe2", "Let Us Observe, Q2",
                  "a) Which faces have common edges with the face numbered 1? "
                  "b) Which face has no common edge with the face numbered 1?",
                  ["Turn the die so that 1 is on top.",
                   "Tap the faces that touch 1 along an edge."],
                  "From the picture: a) 2, 3, 4 and 5. b) 6, the face opposite 1.",
                  kind="prompt"),
              FIO("ch1.observe3", "Let Us Observe, Q3",
                  "Look at three different views of the same cube. a) What colour is the face that is opposite to "
                  "the red face? b) What colour is the face that is opposite to the yellow face?",
                  ["Colours seen together in one view touch each other.",
                   "A face and the face opposite it are never seen together.",
                   "Red touches orange, green, dark blue and yellow. The colour left over is purple.",
                   "Turn the cube on the screen to see which colour is opposite yellow."],
                  "From the picture: a) purple. b) orange.",
                  kind="prompt"),
              FIO("ch1.border5", "Border, Q5",
                  "Follow these instructions for the shapes along the border. "
                  "Circle the shapes that have the same opposite faces.",
                  ["Look at each pair of opposite faces of a shape.",
                   "Circle the shape if the two faces of a pair look the same."],
                  "Sample answer: for example the dice, the erasers, the gift box and the Rubik's cube. "
                  "Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["face", "edge", "corner"]))

# ---- T6: Cube Towers and Drawings (row 19 concept video, rows 20 to 22 Tools 12, 13, 14) ----------------------------------------
# One concept video, then THREE tools back to back (Lesson 5's activities: Cube Towers and Drawings = Build a Cube Tower, Look
# Carefully, Copy the Cube Structure; CLASH 54, 55). All three apply to the cube tower video T6.C1.
# PROVISIONAL, CLASH 20: the plan's own pair, cube towers and drawings, is one tool; counting leads, drawing follows.
TOPICS.append(TOPIC(
    "T6", "M2", "Cube Towers and Drawings", ["Build with Cubes", "Cube Towers", "Drawing Cubes on a Triangular Dot Paper"],
    "Apply",
    "Students count the cubes in a tower layer by layer, hidden cubes too, and copy a cube structure on dot paper.",
    "Nitesh builds a cube tower and Isha counts it. You count cubes and copy a tower on dot paper.",
    [A("T6.C1", "Counting Cubes in a Tower", "Understand",
       "Students count the cubes in a tower layer by layer, including the hidden ones.",
       role="story", key_terms=["cube tower", "layer", "hidden cube"], misconceptions=["M_SH_6"], minutes=5,
       teach=["Predict first: Nitesh's tower has three layers. How many cubes are in its bottom layer, 3 by 3?",
              "The bottom layer has 3 × 3 = 9 cubes. The middle layer has 2 × 2 = 4 cubes. The top layer has 1 cube.",
              "9 + 4 + 1 = 14 cubes. Some of them are hidden under others.",
              "Count the cubes of a tower row by row and layer by layer, hidden cubes too."],
       video=VID("The Cube Tower",
                 "Nitesh builds a small cube tower of its own. Isha counts it layer by layer, including the cubes she "
                 "cannot see. It is none of the book's towers or models.",
                 new_idea="Count the cubes of a tower row by row and layer by layer, hidden cubes too.",
                 story=_S_TOWER, seconds=80)),
     # Tool 12 (the old Tool 6, narrowed: Lesson 5, Activity 1, Build a Cube Tower only).
     DOER("T6.C2", "Cube Towers and Drawings", "cube_towers", "Apply",
          "Students build cube towers from small cubes and count the cubes they used.",
          applies_to="T6.C1", key_terms=["cube tower", "layer"], misconceptions=["M_SH_6"], minutes=5,
          recap=["Count the cubes of a tower layer by layer. Count the hidden cubes too."],
          # QUESTION MAPPER (step 5), changed 12 Nov 2026 (CLASH 59): 1 book question stays here, build1 (build the models A to D with
          # cubes). towers moved to Tool 13 (count the cubes, hidden ones too) and dotcubes to Tool 14 (cubes on dot paper).
          items=[
              FIO("ch1.build1", "Build with Cubes",
                  "Build these models with the cubes from the Jaadui Pitara Kit or any other similar material.",
                  ["Look at the models A, B, C and D.",
                   "Place cubes on the screen to copy each model.",
                   "Turn the model round to check it."],
                  "From the picture: each model you build looks like its picture when you turn it round.",
                  kind="exercise"),
          ]),
     # Tool 13 (new, CLASH 54): Lesson 5, Activity 2. Homes the book's count of the two cube towers (CLASH 59).
     DOER("T6.C3", "Look Carefully", "look_carefully", "Understand",
          "Students count all the cubes in a stack, the partly hidden ones too.",
          applies_to="T6.C1", key_terms=["cube tower", "layer", "hidden cube"], misconceptions=["M_SH_6"], minutes=6,
          recap=["Count the cubes of a tower layer by layer. Count the hidden cubes too."],
          # Re-homed from the old tool on 12 Nov 2026 (CLASH 59): towers. Both tower counts assume solid layers with no gap and no
          # hidden extra cube (E27), and the colours of tower 2 are not copied (E26); the answer says so. 30 and 66 were counted on
          # the page (CLASH 12).
          items=[
              FIO("ch1.towers", "Cube Towers",
                  "How many cubes are there in each of these cube towers?",
                  ["Count each tower. Count the hidden cubes too.",
                   "First tower, top layer: 1 cube",
                   "First tower, second layer: 2 × 2 = 4 cubes",
                   "First tower, third layer: 3 × 3 = 9 cubes",
                   "First tower, bottom layer: 4 × 4 = 16 cubes",
                   "1 + 4 + 9 + 16 = 30",
                   "Second tower: a tall middle column of 6 cubes.",
                   "Four stairs go out from it. Each stair has columns of 5, 4, 3, 2 and 1 cubes.",
                   "5 + 4 + 3 + 2 + 1 = 15",
                   "4 × 15 = 60",
                   "6 + 60 = 66"],
                  "From the picture: the first tower has 30 cubes. The second tower has 66 cubes. "
                  "Both counts include the hidden cubes and assume no gaps.",
                  kind="prompt"),
          ]),
     # Tool 14 (new, CLASH 54): Lesson 5, Activity 3. Homes the book's cubes on triangular dot paper (CLASH 59).
     DOER("T6.C4", "Copy the Cube Structure", "copy_cube_structure", "Apply",
          "Students recreate a cube structure on a grid and copy cube structures on dot paper.",
          applies_to="T6.C1", key_terms=["cube tower", "layer"], misconceptions=[], minutes=6,
          recap=["Count the cubes of a tower layer by layer. Count the hidden cubes too."],
          # Re-homed from the old tool on 12 Nov 2026 (CLASH 59): dotcubes (complete the cubes on the triangular dot paper).
          items=[
              FIO("ch1.dotcubes", "Drawing Cubes on a Triangular Dot Paper",
                  "Can you complete the following cubes?",
                  ["Look at the finished cube.",
                   "Join the dots with straight lines to finish each cube like it."],
                  "From the picture: each cube you finish looks like the first one. "
                  "It shows 3 diamond faces that meet at one corner.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["cube tower", "layer", "hidden cube"]))

# ======================================================================================================================
# MODULE M3  ANGLES  (Lesson 6: Tools 15, 16 and 17)
# ======================================================================================================================

# ---- T7: Understanding Angles (row 23 video, row 24 Tool 15, row 25 video, rows 26, 27 Tools 16, 17) ------------------------
# Two units: [video, Tool 15] and [video, Tool 16, Tool 17 back to back] (CLASH 55). Tool 17 applies to the acute and obtuse video.
# PROVISIONAL, CLASH 20: row 23 teaches the angle and the right angle in one video (the plan's own pair); the names acute and
#   obtuse come only in row 25, so Tool 15 does not use them.
# PROVISIONAL, CLASH 2 (decided): no degrees; a right angle is a corner (a small red square). CLASH 56: Beat the Clock (Tool 17)
#   has no clock and no points; the user kept the earlier adjustments and the plan's activity names.
# PROVISIONAL, CLASH 44 and 45: the row 23 paper fold is shown once and checks only the straw angle; row 25 shows two corners only
#   (one narrower, one wider) and is the only video that names acute and obtuse; Tool 15 never uses the two names.
TOPICS.append(TOPIC(
    "T7", "M3", "Understanding Angles", ["When Lines Meet", "Right Angles", "Acute and Obtuse Angles", "Shapes on a Dot Grid"],
    "Apply",
    "Students make and check angles against a right angle and sort them as acute, right or obtuse.",
    "Isha and Nitesh make angles with straws and a paper corner. You make, check and sort angles.",
    [A("T7.C1", "Angles and the Right Angle", "Understand",
       "Students make an angle with two lines that meet at a point and find a right angle with a paper corner.",
       role="story", key_terms=["angle", "right angle"],
       teach=["Predict first: Isha opens two straws joined at one end. What do the two straws make?",
              "Two lines that meet at a point make an angle.",
              "Nitesh folds a paper in half and in half again. The folded corner fits one of her angles exactly.",
              "The corner of a paper fold is a right angle."],
       misconceptions=["M_AN_1", "M_AN_2", "M_AN_3"], minutes=5,
       textbook=["Isha made different corners with straws.",
                 "We can say that the two straws are like two lines that meet at a point.",
                 "When two lines meet they create an angle.",
                 "We see many angles in yoga postures."],
       ncert=["ch1.angle_text", "ch1.yoga_text"],
       video=VID("Straws and a Paper Corner",
                 "Isha joins two straws at one end and opens them. Nitesh folds a paper corner that fits one of her "
                 "angles exactly. Nitesh then checks the corners of his own straw frame with it. It names neither "
                 "acute nor obtuse and checks no other object.",
                 new_idea="Two lines that meet at a point make an angle. The corner of a paper fold is a right angle.",
                 story=_S_ANGLE, seconds=80)),
     DOER("T7.C2", "Angle Builder", "angle_builder", "Apply",
          "Students make angles smaller than, equal to and bigger than a right angle, and check right angles with a paper corner.",
          applies_to="T7.C1", key_terms=["angle", "right angle"],
          recap=["Two lines that meet at a point make an angle.",
                 "The corner of a paper fold is a right angle."],
          misconceptions=["M_AN_1", "M_AN_2", "M_AN_3"], minutes=8,
          # QUESTION MAPPER (step 5): 10 book questions. The names acute and obtuse come only in row 17, so no answer here uses them:
          # an angle is "narrower" or "wider" than the checker. E8: the boat has 10 marked angles, the house 7. E9: right angles of
          # the dot grid read by measure (top row 2nd and 3rd, bottom row 1st and 4th). E23: try8 counts 4, 0, 1, 0, 0, 4 (the last
          # figure is a tilted rectangle). The paper fold is shown on the screen (CLASH 36).
          items=[
              FIO("ch1.house_ex", "Example",
                  "There are 7 angles in this house drawing.",
                  ["1 angle at the top of the roof.",
                   "2 angles at the lower corners of the roof.",
                   "2 right angles at the top of the walls.",
                   "2 right angles at the bottom of the walls.",
                   "1 + 2 + 2 + 2 = 7"],
                  "From the picture: 7 angles, as your maths book says.",
                  kind="example"),
              FIO("ch1.boat_q", "When Lines Meet",
                  "How many angles are there in this boat drawing?",
                  ["2 angles at the top of the sail, one on each side of the mast.",
                   "2 angles at the lower corners of the sail.",
                   "2 right angles where the mast meets the sail.",
                   "4 angles in the body of the boat.",
                   "2 + 2 + 2 + 4 = 10"],
                  "From the picture: 10 marked angles.",
                  kind="prompt"),
              FIO("ch1.angles_do1", "Let Us Do (angles), Q1",
                  "Mark the angles in the following pictures.",
                  ["Look at each picture: scissors, hanger, hand, seesaw and slide.",
                   "Tap the places where two lines meet."],
                  "Sample answer: scissors, where the two blades meet. Hanger, at the top and at the lower corners. "
                  "Hand, where the two fingers meet. Seesaw, where the plank meets the stand. "
                  "Slide, where the slope meets the ladder. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.angles_do2", "Let Us Do (angles), Q2",
                  "Where do you see angles in the classroom? Give a few examples.",
                  ["Look at the object cards. Tap the ones where two lines meet."],
                  "Sample answer: a desk corner, a door corner and the two hands of a clock. "
                  "Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.right_make", "Right Angles, make",
                  "Let's make a right angle with a piece of paper as shown.",
                  ["Fold the paper in half.",
                   "Fold it in half again.",
                   "Open it a little. The corner made by the folds is a right angle."],
                  "From the picture: the corner made by the two folds is a right angle. "
                  "It is your right angle checker.",
                  kind="exercise"),
              FIO("ch1.right_circle", "Right Angles, dot grid",
                  "Identify the angles that you think are right angles and circle them in the dot grid given below. "
                  "Check using your right angle checker.",
                  ["Look at the 8 angles on the dot grid.",
                   "Circle the ones you think are right angles.",
                   "Lay your right angle checker on each one to check."],
                  "From the picture: 4 of the 8 angles are right angles. In the top row, they are the 2nd and 3rd. "
                  "In the bottom row, they are the 1st and 4th.",
                  kind="exercise"),
              FIO("ch1.right_objects", "Right Angles, objects",
                  "Check for right angles in a book, window, and any other object. "
                  "Write the names of objects where you find right angles.",
                  ["Hold your right angle checker in a corner of the book.",
                   "Do the same for the window and one more object."],
                  "Sample answer: a book, a window, the corner of a desk and a door. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.right_do1", "Let Us Do (right angles), Q1",
                  "Draw some right angles on the dot grid.",
                  ["Pick a dot.",
                   "Draw a line straight across from it.",
                   "Draw a line straight up from the same dot.",
                   "Check the corner with your right angle checker."],
                  "Sample answer: one line goes straight across and one goes straight up from the same dot. "
                  "They make a right angle. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.try8", "Let Us Try, Q8",
                  "Mark the right angles and write the number of right angles in each figure.",
                  ["Lay your right angle checker on each corner.",
                   "Mark each right angle and count them.",
                   "Blue rectangle 4, green slanting shape 0, purple triangle 1.",
                   "Orange shape 0, purple slanting shape 0, red tilted rectangle 4."],
                  "From the picture: 4, 0, 1, 0, 0, 4, from left to right.",
                  kind="exercise"),
              FIO("ch1.try8_q", "Let Us Try, Q8, only right angles",
                  "Which of the above shapes have only right angles?",
                  ["Look for the figures where every corner is a right angle."],
                  "From the picture: the first shape and the last shape. Both are rectangles.",
                  kind="prompt"),
          ]),
     A("T7.C3", "Acute and Obtuse Angles", "Understand",
       "Students tell an acute angle from an obtuse angle by comparing each with a right angle.",
       role="story", key_terms=["acute angle", "obtuse angle"], misconceptions=["M_AN_4"], minutes=5,
       teach=["Predict first: is Isha's first straw corner narrower or wider than the paper corner?",
              "It is narrower. An angle narrower than a right angle is called acute.",
              "Her second corner is wider. An angle wider than a right angle is called obtuse.",
              "An acute angle is less than a right angle. An obtuse angle is more than a right angle."],
       textbook=["Acute angles are less than a right angle.",
                 "Obtuse angles are more than a right angle."],
       ncert=["ch1.acute_text"],
       video=VID("Narrow and Wide Corners",
                 "Nitesh and Isha test two straw corners against the paper corner. One is narrower and one is wider, "
                 "and they get their names here. It sorts no set of angles.",
                 new_idea="An acute angle is less than a right angle. An obtuse angle is more than a right angle.",
                 story=_S_ACUTE, seconds=55)),
     DOER("T7.C4", "Angle Sorting", "angle_sorting", "Apply",
          "Students sort angles as acute, right or obtuse by comparing each with a right angle.",
          applies_to="T7.C3", key_terms=["acute angle", "obtuse angle", "right angle"],
          recap=["An acute angle is less than a right angle.",
                 "An obtuse angle is more than a right angle."],
          misconceptions=["M_AN_4"], minutes=8,
          # note_square is a Note for Teachers: a coverage id only (CLASH 30); its fact (a square is a special rectangle)
          # may become a line of the Tool 16 feedback.
          ncert=["ch1.note_square"],
          # QUESTION MAPPER (step 5): 10 book questions. The one-angle-at-a-time stage is now Tool 17 (CLASH 54, 56). E10: the
          # letters A and the four stick figures give no count, so those answers give the method and no total. E12:
          # the three 4-sided shapes are not named. E22: several shapes of try9 fit each clue, so the answer lists them all.
          # dotshapes_q (c): no 3- or 4-sided shape can have exactly 3 right angles, so the answer is "none" (CLASH 38).
          items=[
              FIO("ch1.acute_obj", "Acute and Obtuse Angles, objects (acute)",
                  "Name some objects from your classroom which have an acute angle.",
                  ["Look for a corner that is narrower than your right angle checker."],
                  "Sample answer: a sharp pencil point, scissors opened a little, a set square's pointed corner. "
                  "Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.obtuse_obj", "Acute and Obtuse Angles, objects (obtuse)",
                  "Name some objects from your classroom which have an obtuse angle.",
                  ["Look for a corner that is wider than your right angle checker."],
                  "Sample answer: a door opened wide and the clock hands at 4 o'clock. "
                  "Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.letters", "Acute and Obtuse Angles, letters",
                  "Identify all angles in the following letters.",
                  ["Look at the letters V, A and Z.",
                   "Find each place where two strokes meet.",
                   "Compare each angle with a right angle."],
                  "Sample answer: V has 1 acute angle. Z has 2 acute angles. "
                  "A has an acute angle at the top and angles where the bar meets the legs. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.ao_do1a", "Let Us Do (acute and obtuse), Q1 (acute)",
                  "Draw some acute angles on the top grid. Draw a line to make an acute angle using each given "
                  "line in the bottom grid.",
                  ["Pick one end of a given line.",
                   "Draw a second line from that end.",
                   "Make the angle narrower than a right angle."],
                  "Sample answer: draw a second line from one end of each given line. Make it narrower than a right angle. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.ao_do1b", "Let Us Do (acute and obtuse), Q1 (obtuse)",
                  "Draw some obtuse angles on the top grid. Draw a line to make an obtuse angle using each given "
                  "line in the bottom grid.",
                  ["Pick one end of a given line.",
                   "Draw a second line from that end.",
                   "Make the angle wider than a right angle."],
                  "Sample answer: draw a second line from one end of each given line. Make it wider than a right angle. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.ao_do2", "Let Us Do (acute and obtuse), Q2",
                  "In the figures given below, mark the acute angles in red, right angles in green, and obtuse "
                  "angles in blue.",
                  ["Find each place where two lines of a figure meet.",
                   "Compare the angle with a right angle."],
                  "Sample answer: red if it is narrower than a right angle. Green if it is the same. "
                  "Blue if it is wider. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.dotshapes", "Shapes on a dot grid",
                  "Use the dot grid given below to draw several three- and four-sided shapes. "
                  "Circle the shapes that have one or more right angles.",
                  ["Draw shapes with 3 sides and with 4 sides on the dots.",
                   "Lay your right angle checker on each corner.",
                   "Circle the shapes with a right angle."],
                  "Sample answer: a right triangle, a rectangle, a square and a slanting four-sided shape. "
                  "Circle the first three. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.dotshapes_q", "Shapes on a dot grid, Discuss",
                  "Discuss: What shapes did you make? How many shapes have you made with "
                  "a) 1 right angle b) 2 right angles c) 3 right angles d) all right angles",
                  ["Count the right angles of each shape you drew.",
                   "Count the shapes in each group."],
                  "Sample answer: 1 right angle: a right triangle. 2: a shape with one slanting side. "
                  "3: none, because a 4-sided shape with 3 right angles has 4. All: a rectangle and a square. "
                  "Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.fourside_q", "Four-sided shapes",
                  "Here are some 4-sided shapes. In what ways are rectangle and square different from these shapes?",
                  ["Lay your right angle checker on the corners of each shape."],
                  "Sample answer: a rectangle and a square have 4 right angles. The three shapes shown have none. "
                  "Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.try9", "Let Us Try, Q9",
                  "Observe the following shapes. Identify the shape that has: "
                  "2 right angles, 1 acute, and 1 obtuse angle; 1 right, 2 obtuse, and 1 acute angle; "
                  "2 obtuse, and 2 acute angles; 4 right angles.",
                  ["Compare each corner with a right angle.",
                   "Count the right, acute and obtuse angles of each shape."],
                  "From the picture: 2 right, 1 acute, 1 obtuse: shapes 2 and 7. 1 right, 2 obtuse, 1 acute: shape 10. "
                  "2 obtuse, 2 acute: shapes 3, 5, 8, 9, 11 and 13. 4 right: shapes 4, 6, 12 and 14. "
                  "More than one shape fits.",
                  kind="exercise"),
          ]),
     # Tool 17 (new, CLASH 54): Lesson 6, Activity 3. No book question homes here (config no_book_question_tools). It was the stage
     # Identify the Angle of the old Angle Sorting tool (SPLIT NOTES in media_decisions.md). No clock and no points (CLASH 56).
     DOER("T7.C5", "Beat the Clock", "beat_the_clock", "Apply",
          "Students name one angle at a time as acute, right or obtuse by comparing it with a right angle.",
          applies_to="T7.C3", key_terms=["acute angle", "obtuse angle", "right angle"],
          recap=["An acute angle is less than a right angle.",
                 "An obtuse angle is more than a right angle."],
          misconceptions=["M_AN_4"], minutes=5)],
    topic_type="instructional", key_terms=["angle", "right angle", "acute angle", "obtuse angle"]))

# ======================================================================================================================
# MODULE M4  CIRCLES AND FIRM SHAPES  (Lessons 7 and 8: Tools 18 to 23)
# ======================================================================================================================

# ---- T8: Circles and Pentagons (row 28 video, rows 29, 30, 31 Tools 18, 19, 20) ------------------------------------------------
# One concept video (the circle), then THREE tools back to back (Lesson 7's activities: Circle Detective, Radius or Diameter,
# Build a Pentagon; CLASH 54, 55). All three apply to the circle video T8.C1.
# CLASH 57 (the user's decision): the football picture (the image concept "The Pentagon", row 21) is REMOVED and nothing takes its
#   place. Build a Pentagon now follows Radius or Diameter directly and introduces the pentagon itself: its concept T8.C4 is a role
#   'tool' concept that applies_to the circle video, and the book's idea stays (five sides and five corners).
# PROVISIONAL, CLASH 20: one circle tool carries the centre and radius, the diameter by folding, and the double.
# PROVISIONAL, CLASH 14: the pentagon is pushed here (Tool 20), before the rigidity lesson (T9); the row 32 video may recall it.
# PROVISIONAL, CLASH 18: the angle-counting items (try6, try6_q, try7a, try7b) ride on Tool 20 as its last stage.
# PROVISIONAL, CLASH 44: row 28 names centre, radius and ONE diameter; "all equal" and "double" are Tool 18's finding.
TOPICS.append(TOPIC(
    "T8", "M4", "Circles and Pentagons", ["Let Us Make", "Amazing Circles", "Compass and Wheels", "Pentagon"], "Apply",
    "Students name the centre, radius and diameter of a circle, find one from the other, and count the sides and corners "
    "of a pentagon.",
    "Diksha and her father draw a big circle on the ground. You find its parts, use the double and make a pentagon.",
    [A("T8.C1", "Parts of a Circle", "Remember",
       "Students name the centre, the radius and the diameter of a circle.",
       role="story", key_terms=["circle", "centre", "radius", "diameter"],
       teach=["Predict first: the peg stays still and the string is pulled tight. What does the stick draw?",
              "It draws a circle. The spot of the peg is the centre.",
              "The string from the centre to the circle is the radius.",
              "A line across the circle through the centre is a diameter.",
              "A circle has a centre, a radius and a diameter."],
       misconceptions=["M_CI_1", "M_CI_2", "M_CI_3", "M_CI_4"], minutes=5,
       textbook=["The point A is the centre and the line from the centre to the border of the circle is the radius.",
                 "These creases are called diameters of the circle."],
       ncert=["ch1.centre_text", "ch1.amazing_t2"],
       video=VID("A Circle on the Ground",
                 "Diksha and her father draw a big circle on the ground. They use a peg and a string, and name the "
                 "centre, the radius and one diameter. It never says all diameters are equal or that the diameter "
                 "is double the radius.",
                 new_idea="A circle has a centre, a radius and a diameter.",
                 story=_S_CIRCLE, seconds=80)),
     DOER("T8.C2", "Circle Detective", "circle_detective", "Apply",
          "Students make a circle, name its centre, radius and diameter, and show that the diameter is double the radius.",
          applies_to="T8.C1", key_terms=["circle", "centre", "radius", "diameter"],
          recap=["A circle has a centre, a radius and a diameter."],
          misconceptions=["M_CI_1", "M_CI_2", "M_CI_3", "M_CI_4"], minutes=8,
          textbook=["Discuss where the centre is. Do you notice that all the diameters pass through the centre?",
                    "Discuss if there is any relationship between the radius and the diameter of a circle."],
          # note_measure and note_compass are Notes for Teachers: coverage ids only (CLASH 30).
          ncert=["ch1.amazing_t3", "ch1.amazing_t5", "ch1.note_measure", "ch1.note_compass"],
          # QUESTION MAPPER (step 5), CLASH 7: 13 book questions, exactly the cap: add nothing. The plan's own Label the parts stage
          # is the tool's interaction (CLASH 24). No cm anywhere (CLASH 2): measuring is the thread overlay on screen (CLASH 36) and
          # the relation is the book's half or double. The compass sentence "Ask your teacher to help you use a compass." is dropped,
          # CLASH 30 option (a), CLASH 50. E16: wheels B longest and D shortest, read by measure (outer sizes in the ratio
          # 665 : 604 : 515 : 440 for B, C, A, D). Radius and diameter are the same wheel in each pair.
          items=[
              FIO("ch1.circle_straws", "Circle with straws",
                  "Can you make a circle using straws?",
                  ["Put one clay ball in the middle.",
                   "Lay straws of the same length round it, like spokes.",
                   "Look at the ends of the straws."],
                  "Sample answer: yes. Straws of the same length round a middle ball have their ends on a circle. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.circle_straws_q1", "Circle with straws, Q1",
                  "Look at the picture. The lengths of the straws in this picture are _______ (Equal/Unequal)",
                  ["Look at how long each straw is."],
                  "From the picture: equal.",
                  kind="prompt"),
              FIO("ch1.circle_straws_q2", "Circle with straws, Q2",
                  "What will happen if we take straws of unequal lengths?",
                  ["Swap some straws for longer or shorter ones.",
                   "Look at the ends of the straws."],
                  "Sample answer: the ends do not make a circle. The shape comes out uneven. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.make_circle", "Let Us Make",
                  "Can you use a scale to draw a circular shape? Let us see. Mark a point A. "
                  "Draw many points that are at an equal distance from point A. Connect the dots freehand.",
                  ["Mark a point A.",
                   "Use the scale to mark many points the same distance from A.",
                   "Join the dots by hand."],
                  "Sample answer: the points lie all round A and join into a round shape. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.make_circle_q", "Let Us Make, What do you get?",
                  "What do you get?",
                  ["Look at the shape you drew."],
                  "From the picture: a circle.",
                  kind="prompt"),
              FIO("ch1.amazing1", "Amazing Circles",
                  "Take a piece of circular paper. Fold your paper in half and crease it well. "
                  "Open the fold and measure the length of the crease using a thread. "
                  "Fold your paper in half in a different way and crease it well. "
                  "Open the fold and measure the length of the crease again. "
                  "Fold it again in half in a different way and crease it well. "
                  "Open the fold, measure the length of the crease.",
                  ["Fold the circle in half and crease it.",
                   "Open it and lay the thread along the crease.",
                   "Fold it in half in a different way and measure again.",
                   "Do it a third time and compare the three creases."],
                  "Sample answer: you get 3 creases that cross at one point. Each one measures the same. "
                  "Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.amazing_q1", "Amazing Circles, Q1",
                  "The length of all the creases are __________. (Equal/Unequal)",
                  ["Compare the three creases you measured."],
                  "From the picture: equal.",
                  kind="prompt"),
              FIO("ch1.amazing_q4", "Amazing Circles, Q4",
                  "Measure the length of the creases from the centre to the border of the circle. "
                  "This is called the radius of the circle.",
                  ["Find the centre where the creases cross.",
                   "Lay the thread from the centre to the border along a crease.",
                   "Do it for each crease."],
                  "From the picture: from the centre to the border every crease measures the same. That length is the radius.",
                  kind="exercise"),
              FIO("ch1.circ_do1", "Let Us Do (circles)",
                  "Fold the circular paper in half. Fold this half again in half. "
                  "The length of the diameter is ___________ (half/double) of the length of radius.",
                  ["Fold the circle in half. The crease is a diameter.",
                   "Fold the half in half again. The crease from the centre to the border is a radius.",
                   "Lay the radius along the diameter and compare."],
                  "From the picture: double. The diameter is double the radius.",
                  kind="exercise"),
              FIO("ch1.compass", "Compass design",
                  "A circle can be made easily using a compass. Make the following design.",
                  ["Step 1: draw a circle with the compass.",
                   "Step 2: keep the same opening. Put the point on the circle and draw another circle.",
                   "Do this at other points of the first circle.",
                   "Step 3: colour the petals."],
                  "Sample answer: a flower of overlapping circles, like Step 3 of the picture. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.carpet", "Carpet design",
                  "Look at the carpet design. A beautiful circle, right? Mark the centre, radius, and the diameter "
                  "of the circular design with any colour of your choice.",
                  ["Find the small blue dot in the middle: that is the centre.",
                   "Draw a line from the centre to the edge of the circle: a radius.",
                   "Draw a line across the circle through the centre: a diameter."],
                  "Sample answer: the centre is the blue dot in the middle. A radius runs from the dot to the edge. "
                  "A diameter runs across through the dot. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.wheels_q0", "Wheels, Q1",
                  "Look at the wheels. All wheels look like _______",
                  ["Look at the shape of each wheel."],
                  "From the picture: circles.",
                  kind="prompt"),
              FIO("ch1.wheels_q1", "Wheels, Q2",
                  "Name the wheel with the 1. longest radius 2. shortest radius 3. longest diameter "
                  "4. shortest diameter",
                  ["Find the centre of each wheel.",
                   "Compare how far the edge is from the centre.",
                   "A wheel with a longer radius has a longer diameter."],
                  "From the picture: 1. B. 2. D. 3. B. 4. D. The wheel with the longest radius also has the longest diameter.",
                  kind="prompt"),
          ]),
     # Tool 19 (new, CLASH 54): Lesson 7, Activity 2. No book question homes here (config no_book_question_tools): the book prints no
     # radius or diameter number (no cm, CLASH 56), and its one doubling question, circ_do1, is the paper fold of Tool 18 (CLASH 59).
     DOER("T8.C3", "Radius or Diameter", "radius_or_diameter", "Apply",
          "Students use the fact that the diameter is double the radius to find one when given the other.",
          applies_to="T8.C1", key_terms=["radius", "diameter"],
          recap=["The diameter is double the radius."],
          misconceptions=["M_CI_3", "M_CI_4"], minutes=5),
     # Tool 20 (Lesson 7, Activity 3). It introduces the pentagon itself (CLASH 57): its concept is the book's idea, five sides and
     # five corners, met inside the tool with no picture before it. applies_to is the circle video (the gate wants the lesson's
     # last video or image concept).
     DOER("T8.C4", "Build a Pentagon", "build_pentagon", "Apply",
          "Students make a pentagon from five equal sides, say it has five sides and five corners, and see its angles change when "
          "pushed.",
          applies_to="T8.C1", key_terms=["pentagon", "angle"],
          recap=["A pentagon has five sides and five corners."], misconceptions=["M_AN_7", "M_AN_8"], minutes=8,
          # QUESTION MAPPER (step 5): 8 book questions. The pentagon is "5 sides, all equal": never "regular", never "equal angles"
          # (CLASH 2; equal sides do not fix the angles, the push shows it). pentagon_q2 reads with its question mark (CLASH 50, E13).
          # try6 to try7b are the angle-counting items (CLASH 18): shapes of try6 read from the picture (3 angles b, d, f; 4 angles
          # a, c, g; 5 angles e); the number of angles is the number of sides.
          items=[
              FIO("ch1.pentagon_make", "Pentagon, make",
                  "Try to make this 5-sided shape with all sides equal (Pentagon)",
                  ["Pick 5 straws of the same length.",
                   "Join their ends with 5 clay balls."],
                  "Sample answer: 5 equal straws joined by 5 clay balls make a pentagon. "
                  "It has 5 sides and 5 corners. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.pentagon_q1", "Pentagon, Q1",
                  "Are these right angles?",
                  ["Lay your right angle checker on each corner of the pentagon."],
                  "From the picture: no. Each angle is bigger than a right angle.",
                  kind="prompt"),
              FIO("ch1.pentagon_q2", "Pentagon, Q2",
                  "Does the shape of the pentagon change if we gently push one of its sides? Yes/No",
                  ["Push one side of the pentagon on the screen.",
                   "Watch if the shape changes."],
                  "From the picture: yes. The pentagon leans over and its shape changes.",
                  kind="prompt"),
              FIO("ch1.pentagon_q3", "Pentagon, Q3",
                  "How does this change the angles?",
                  ["Compare the angles before and after the push."],
                  "Sample answer: some angles get smaller and some get bigger. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.try6", "Let Us Try, Q6",
                  "Classify these shapes based on the number of angles.",
                  ["Count the corners of each shape.",
                   "Blue square 4, red triangle 3, green slanting shape 4, purple right triangle 3.",
                   "Purple pentagon 5, thin green triangle 3, red rectangle 4.",
                   "Drag each shape to its box: 3 angles, 4 angles or 5 angles."],
                  "From the picture: 3 angles: b, d and f. 4 angles: a, c and g. 5 angles: e.",
                  kind="exercise"),
              FIO("ch1.try6_q", "Let Us Try, Q6, sides and angles",
                  "What relation do you notice between the number of sides and the number of angles?",
                  ["Count the sides of each shape.",
                   "Compare with the number of angles."],
                  "From the picture: they are the same. 3 sides have 3 angles, 4 sides have 4 angles and 5 sides have 5 angles.",
                  kind="prompt"),
              FIO("ch1.try7a", "Let Us Try, Q7 (fewer angles)",
                  "Draw a 2D shape that has less than 5 angles.",
                  ["Draw a shape on the dots with 3 or 4 sides.",
                   "Count its angles."],
                  "Sample answer: a triangle has 3 angles. A square has 4 angles. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.try7b", "Let Us Try, Q7 (more angles)",
                  "Draw a 2D shape with more than 5 angles.",
                  ["Draw a shape on the dots with 6 or more sides.",
                   "Count its angles."],
                  "Sample answer: a shape with 6 sides has 6 angles. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["circle", "centre", "radius", "diameter", "pentagon"]))

# ---- T9: Shapes with Straws, Rigidity (row 32 video, row 33 Tool 21, row 34 video, rows 35, 36 Tools 22, 23) --------------------
# Two units: [video, Tool 21] and [video, Tool 22, Tool 23 back to back] (CLASH 55). Tool 23 applies to the strong-frames video.
# PROVISIONAL, CLASH 9: "rigid" is the plan's word (a teacher's word in the book) and is kept; a stick across the corners, not "diagonal".
# PROVISIONAL, CLASH 30 (changed by the media step, CLASH 46): note_rigid is a fact (the triangle does not change when pushed).
#   The row 32 video stops BEFORE the push, so the fact becomes a line of the Tool 21 feedback after the push, not of the story.
# PROVISIONAL, CLASH 46: rows 32 and 34 stop before the result (the push; the thread) so Tools 21 and 22 keep their finding;
#   the row 32 new_idea is now the meaning of "rigid", the finding "a triangle is rigid" is Tool 21's.
# PROVISIONAL, CLASH 22: Tool 22's concept is the plan's "a stick across a frame makes it firm"; the row 34 story (Squiggly's
#   triangle web firm, Wiggly's rectangle web wobbly until a thread goes across) is the content team's table, and the user
#   confirms the claim.
# PROVISIONAL, CLASH 13 and 17: Tool 22 carries the walk puzzles (try1b, try1d). The Strong or wobbly stage of the old tool is now
#   Tool 23, True or False (CLASH 54).
TOPICS.append(TOPIC(
    "T9", "M4", "Shapes with Straws, Rigidity", ["Shapes with Straws", "Let Us Try"], "Apply",
    "Students show that a triangle keeps its shape when pushed and that a stick across a frame makes it firm.",
    "Isha and Nitesh push straw shapes. Squiggly and Wiggly show which webs stay firm.",
    [A("T9.C1", "A Rigid Shape", "Understand",
       "Students say that a triangle is a rigid shape because it keeps its shape when pushed.",
       role="story", key_terms=["rigid shape", "triangle"],
       teach=["Predict first: Isha and Nitesh will push a corner of each straw shape. Which one will keep its shape?",
              "A rigid shape keeps its shape when it is pushed.",
              "Push the straw shapes in the next tool to find out which one is rigid."],
       misconceptions=["M_AN_5", "M_AN_6", "M_AN_9"], minutes=5,
       # CLASH 46, approved by the user: the book's sentence "The triangle is the most rigid shape, as it does not
       # change its shape when pushed" is Tool 21's finding, so it is NOT quoted before the tool. ch1.note_rigid stays
       # homed through ncert=; the fact is given in Tool 21's feedback after the push.
       textbook=[],
       ncert=["ch1.note_rigid"],
       video=VID("Push the Straw Shapes",
                 "Isha and Nitesh hold a straw triangle and a straw rectangle and recall the pentagon that changed "
                 "when pushed. They ask which shape will keep its shape when pushed. The video stops before the "
                 "push, so Tool 21 shows the result.",
                 new_idea="A rigid shape keeps its shape when it is pushed.",
                 story=_S_RIGID, seconds=60)),
     DOER("T9.C2", "Triangle vs Rectangle", "triangle_rectangle", "Analyze",
          "Students push the corners of a triangle frame and a rectangle frame and tell which one keeps its shape.",
          applies_to="T9.C1", key_terms=["rigid shape", "triangle"],
          recap=["A rigid shape keeps its shape when it is pushed."],
          misconceptions=["M_AN_5", "M_AN_6", "M_AN_9"], minutes=7,
          # QUESTION MAPPER (step 5): 10 book questions. E11: the book prints no answers; each is what the push on the screen shows
          # (a triangle of three fixed straws cannot change, a rectangle or a square leans into two acute and two obtuse angles).
          # The fact of note_rigid (the triangle does not change when pushed) is a line of this tool's feedback after the push,
          # not of the story (CLASH 30, 46). The names acute and obtuse are known from Tool 16. The straws and clay are on screen
          # (CLASH 36); "in your notebook" stays as printed (CLASH 50). The answer to straw_tri_angles reads the tool's triangle,
          # so the brief writer draws it with three angles narrower than a right angle, as the book's straw triangle looks.
          items=[
              FIO("ch1.straw_tri_make", "Shapes with Straws, triangle",
                  "Make a triangle with straws of different sizes and clay/plasticine.",
                  ["Pick 3 straws of different lengths.",
                   "Join their ends with 3 clay balls."],
                  "Sample answer: 3 straws joined by 3 clay balls make a triangle. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.straw_tri_push", "Shapes with Straws, push the triangle",
                  "Does the shape of the triangle change if we gently push one of its sides? Yes/No",
                  ["Push one side of the triangle on the screen.",
                   "Watch if the shape changes."],
                  "From the picture: no. The triangle keeps its shape.",
                  kind="prompt"),
              FIO("ch1.straw_tri_trace", "Shapes with Straws, trace",
                  "Trace the triangles you made with the straws in your notebook.",
                  ["Place the straw triangle on the paper.",
                   "Draw along its three sides."],
                  "Sample answer: the outline has 3 straight sides and 3 corners. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.straw_tri_angles", "Shapes with Straws, angles of a triangle",
                  "What kinds of angles does a triangle have?",
                  ["Lay your right angle checker on each corner of your triangle.",
                   "Say if each angle is narrower, the same or wider."],
                  "Sample answer: all 3 angles of my triangle are acute. "
                  "Another triangle can have a right angle or a wider angle. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.straw_rect_make", "Shapes with Straws, rectangle",
                  "Make a rectangular shape with straws and clay.",
                  ["Pick 2 long straws and 2 short straws.",
                   "Join their ends with 4 clay balls so every corner is a right angle."],
                  "Sample answer: 2 long and 2 short straws joined by 4 clay balls. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.straw_rect_angles", "Shapes with Straws, angles of a rectangle",
                  "What kinds of angles do you see in the rectangle?",
                  ["Lay your right angle checker on each corner."],
                  "From the picture: all 4 angles are right angles.",
                  kind="prompt"),
              FIO("ch1.straw_rect_push", "Shapes with Straws, push the rectangle",
                  "Does the shape of the rectangle change if we gently push one of its sides? Yes/No",
                  ["Push one side of the rectangle on the screen.",
                   "Watch if the shape changes."],
                  "From the picture: yes. The rectangle leans over into a slanting shape.",
                  kind="prompt"),
              FIO("ch1.straw_rect_after", "Shapes with Straws, the new shape",
                  "What has happened to the angles of the new shape? Are they still right angles? "
                  "What types of angles have been formed?",
                  ["Lay your right angle checker on each corner of the new shape."],
                  "From the picture: the angles have changed. They are not right angles now. "
                  "Two are acute and two are obtuse.",
                  kind="prompt"),
              FIO("ch1.straw_square", "Shapes with Straws, square",
                  "Similarly, push one side of a square. Are they still right angles? What types of angles have been formed?",
                  ["Push one side of the square on the screen.",
                   "Lay your right angle checker on each corner."],
                  "From the picture: no. Two angles become acute and two become obtuse.",
                  kind="prompt"),
              FIO("ch1.straw_compare", "Shapes with Straws, compare",
                  "How are the angles of triangles and rectangles similar or different?",
                  ["Think about what the push did to each shape."],
                  "Sample answer: both have angles at their corners. When pushed, the triangle's angles stay the same. "
                  "The rectangle's angles change. Your answer may differ.",
                  kind="prompt"),
          ]),
     A("T9.C3", "A Stick Across a Frame", "Understand",
       "Students say that a stick across a four-sided frame makes triangles and keeps the frame firm.",
       role="story", key_terms=["frame", "rigid shape"], misconceptions=["M_AN_5"], minutes=5,
       teach=["Predict first: Wiggly's four-sided web wobbles. Where could one thread go to help?",
              "Squiggly says: stretch a thread from one corner straight across to the opposite corner.",
              "The thread cuts the four-sided frame into two triangles.",
              "A stick across a four-sided frame makes triangles. Does that keep the frame firm? Test it in the next tool."],
       textbook=["Squiggly, the spider, likes to make webs in different shapes. One day she begins to make triangular webs.",
                 "Her brother, Wiggly made a web using rectangles.",
                 "She likes to take a walk each morning and check if the walls of her web are strong.",
                 "He likes to take a walk at the end of each day and check if the walls of his web are strong."],
       ncert=["ch1.try1_text"],
       video=VID("The Two Webs",
                 "Squiggly's triangle web holds firm and Wiggly's rectangle web wobbles. Squiggly says a thread from "
                 "corner to corner would make triangles. The video stops before the thread is added, so Tool 22 "
                 "shows the result.",
                 new_idea="A stick across a four-sided frame makes triangles and keeps the frame firm.",
                 story=_S_WEBS, seconds=75)),
     DOER("T9.C4", "Build a Strong Structure", "strong_structure", "Apply",
          "Students add a stick across the corners of a square frame and tell strong frames from wobbly ones.",
          applies_to="T9.C3", key_terms=["frame", "web"],
          recap=["Squiggly's idea: a stick across a four-sided frame makes triangles."], misconceptions=["M_PU_1", "M_PU_2", "M_PU_3"], minutes=8,
          # QUESTION MAPPER (step 5): 7 book questions. The plan's own square frame with a stick across it and Strong or wobbly
          # are the tool's interaction, unscored (CLASH 2, 24). The web and matchstick answers are the solved results of analysis
          # Appendix A (CLASH 12); how each was checked is in SOLUTION_NOTES. E19: both walks are answered on the "every wall"
          # reading (CLASH 12, 17): Squiggly's printed numbers 1 to 12 trace one closed walk; no walk over every wall of Wiggly's
          # web goes from A to B, and the answer adds the other reading in one line. E20: the three triangles of try3 touch at their
          # base corners (the book draws small gaps). Every answer is "From the picture" or "Sample answer".
          items=[
              FIO("ch1.try1a", "Let Us Try, Q1, triangles",
                  "How many triangles are in her web?",
                  ["Count the triangles one kind at a time.",
                   "The top triangle: 1. The bottom triangle: 1.",
                   "The small triangles in the middle: 4.",
                   "The big triangles in the middle, each made of 2 small ones: 4.",
                   "1 + 1 + 4 + 4 = 10"],
                  "From the picture: 10 triangles.",
                  kind="prompt"),
              FIO("ch1.try1b", "Let Us Try, Q1, Squiggly's walk",
                  "Can she begin at point A and reach back to the same point without walking on any wall more than once? "
                  "Trace and show Squiggly's path.",
                  ["Start at A.",
                   "Follow the walls in the order of the numbers 1, 2, 3 up to 12.",
                   "Each number starts where the last one ended."],
                  "From the picture: yes. The numbers 1 to 12 show a way. She uses every wall once and comes back to A.",
                  kind="exercise"),
              FIO("ch1.try1c", "Let Us Try, Q1, rectangles",
                  "How many rectangles can you see in his web?",
                  ["Count the rectangles one kind at a time.",
                   "The small box at the top: 1.",
                   "The upper row of 3 cells: 3 single cells, 2 pairs and 1 triple. 3 + 2 + 1 = 6",
                   "The lower row: the left and right cells are closed. 2",
                   "An upper cell with the closed cell under it: 2",
                   "The top box with the upper cell under it: 1",
                   "1 + 6 + 2 + 2 + 1 = 12"],
                  "From the picture: 12 rectangles.",
                  kind="prompt"),
              FIO("ch1.try1d", "Let Us Try, Q1, Wiggly's walk",
                  "Can he begin at point A and leave from point B without walking on any wall more than once? "
                  "Trace and show Wiggly's path.",
                  ["Start at A.",
                   "Walk along the walls and try to end at B.",
                   "Do not use any wall twice."],
                  "From the picture: no, if he must walk on every wall. Two corners have 3 walls each, so such a walk "
                  "has to start and end there. If he may skip some walls, he can walk from A to B.",
                  kind="exercise"),
              FIO("ch1.try2", "Let Us Try, Q2",
                  "Use 5 matchsticks to make 2 triangles. Then draw it in the space provided.",
                  ["A triangle needs 3 matchsticks.",
                   "Two triangles that share one stick need 3 + 3 − 1 = 5 matchsticks.",
                   "Lay the 5 sticks and draw what you made."],
                  "Sample answer: 2 triangles that share one stick. They use 5 sticks. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.try3", "Let Us Try, Q3",
                  "Move two of these matchsticks to form 4 triangles.",
                  ["The figure has 9 sticks and 3 triangles that touch at their base corners.",
                   "Take the bottom stick and the right slanting stick of the third triangle.",
                   "Lay them end to end along the tops of the three triangles."],
                  "Sample answer: one stick joins the first and second top corners. The other joins the second and third. "
                  "You get 4 triangles, 2 pointing up and 2 pointing down. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.try4", "Let Us Try, Q4",
                  "Remove 4 of these matchsticks to leave only 3 triangles.",
                  ["The figure has 13 sticks and 7 triangles: 6 small ones and 1 big one.",
                   "Take away 4 sticks so that only 3 triangles stay.",
                   "No stray stick should be left."],
                  "Sample answer: take away the right side and the bottom stick of the top right triangle. "
                  "Take away the top stick and the right side of the far right triangle. 3 triangles stay. "
                  "Other answers are right too.",
                  kind="exercise"),
          ]),
     # Tool 23 (new, CLASH 54): Lesson 8, Activity 3. No book question homes here (config no_book_question_tools). It was the stage
     # Strong or wobbly of the old strong-structure tool (SPLIT NOTES in media_decisions.md).
     DOER("T9.C5", "True or False", "true_or_false", "Understand",
          "Students decide if each statement about rigid shapes is right or wrong and say why.",
          applies_to="T9.C3", key_terms=["rigid shape", "triangle", "frame"],
          recap=["A rigid shape keeps its shape when it is pushed."],
          misconceptions=["M_AN_5", "M_AN_9"], minutes=4)],
    topic_type="instructional", key_terms=["rigid shape", "triangle", "frame"]))

# ======================================================================================================================
# MODULE M5  REVISION AND REVIEW  (rows 37 to 42 of the table; Lesson 9, then the closing look back)
# ======================================================================================================================

# ---- T10: Revision and Chapter Practice (row 37 recap story video, rows 38, 39, 40 Tools 24, 25, 26) --------------------------
# CLASH 58 (the user's decision): Lesson 9 is an idea topic made by the lesson plan itself: one recap STORY video (it adds no new idea,
# but it has its own new_idea line so that the gate sees no duplicate: each shape of the chapter can be named by its parts), then
# three tools back to back: Shape Identification Quiz, Digital Worksheet, Sample Online Assessment (all apply to the recap video).
# No book question is repeated here: the three tools and the recap carry none (config no_book_question_tools: 24, 25, 26). The
# assessment is unscored, 8 questions in 3 sections, no clock, no marks shown, no degrees, no cm (CLASH 56).
# The pipeline wants the LAST topic to be a review with no media, so the two look-back concepts stay as Topic 11 (below): the assessment
# is the last TOOL but not the very last topic (CLASH 58 says so; the user decided).
# The recap story: Diksha and her friends lay out the blocks, nets, angles, circles and straw frames of the trip and name each one by
# its parts. It shows none of the pictures of the quiz and gives no answer of the worksheet or the assessment (media_decisions.md).
TOPICS.append(TOPIC(
    "T10", "M5", "Revision and Chapter Practice", ["Chapter Practice"], "Apply",
    "Students name each shape of the chapter from a picture and answer mixed questions on solids, angles, circles and "
    "rigid frames.",
    "Diksha and her friends name the shapes of her trip. You try a picture quiz, a worksheet and a short assessment.",
    [A("T10.C1", "Naming the Shapes of the Trip", "Understand",
       "Students name each kind of shape of the chapter by pointing to its parts.",
       role="story", key_terms=["prism", "pyramid", "net", "angle", "circle", "pentagon", "rigid shape"], minutes=5,
       teach=["Predict first: the wind has blown the labels off Diksha's boxes. How can she tell the models apart?",
              "Look at the parts of each model, not at its colour or size.",
              "Try the picture quiz in the next tool."],
       video=VID("Diksha's Shape Show",
                 "The wind blows the paper labels off the model boxes of Diksha's trip, and her father, Isha and Nitesh "
                 "help her pick each label again by looking at the parts of each model. It adds no new idea. It shows none "
                 "of the pictures of the quiz and gives no answer of the worksheet or the assessment.",
                 new_idea="Each shape of the chapter can be named by its parts.",
                 # BRIEF WRITER (12 Nov 2026): a story, not a lecture. Diksha re-labels her model boxes after the wind blows the
                 # labels off, and each helper names a model by looking at its parts. The names spoken are only the families
                 # (the label words); no key of Tool 24, 25 or 26 is said: no count, no "acute", "obtuse" or "right angle", no
                 # "five sides", no radius and diameter link, no "two matching ends", and it never says which frame keeps its shape.
                 # It shows none of the quiz pictures: the quiz uses stone-grey solids, a prism net, a drawn circle, a triangle frame
                 # and a rectangle frame; this story uses Diksha's wooden pillar and roof cards, the pink gift box card, straws on a
                 # paper corner, a round paper sheet, a square and a pentagon frame, and the two webs.
                 story={
                     "characters": ["Diksha", "Diksha's father", "Isha", "Nitesh", "Squiggly", "Wiggly"],
                     "setting": "Diksha's room on the evening before the school shape show. Open boxes of her models stand on "
                                "the floor mat. They hold wooden pillar blocks and roof cards. They hold the pink gift box and "
                                "its flat card. They hold straws with a folded paper corner, and a round sheet of paper. "
                                "The last box holds straw frames, a square and a pentagon. "
                                "A heap of paper labels lies beside them. Squiggly and Wiggly hang in their webs in the "
                                "open window.",
                     "situation": "Diksha has packed the models of her whole trip into boxes for the school shape show. Each "
                                  "box had a paper label. Her father, Isha and Nitesh are helping. A gust of wind blows through "
                                  "the window. Every label flutters off and lands in a heap. Now nobody knows which label "
                                  "belongs on which box. Her father says, Do not go by colour or size. Look at the parts. "
                                  "He lifts out a wooden pillar and turns it. Both ends and the sides between show. Diksha "
                                  "picks its label. Next he lifts out the roof cards. They lean together, and all the "
                                  "triangles meet at one point on top. Diksha picks that label too. "
                                  "Nitesh lifts out the flat card cut from the pink gift box. He folds it along the dotted "
                                  "lines, and the box comes back. Diksha picks its label. "
                                  "Isha joins two straws at one end and lays the folded paper corner against them. They fit "
                                  "it exactly. Diksha picks the label for the straws. "
                                  "Diksha folds a round sheet of paper in half. She points to the middle point and to the "
                                  "fold across the sheet. Then she picks its label. "
                                  "A second gust shakes the window. Diksha looks at the straw frames in the last box and at the "
                                  "two webs. She looks at how each one is built. Then she picks the last label, and every box "
                                  "is named again. Her father says that tomorrow the visitors will point at pictures and ask "
                                  "for names. Nitesh holds up a card, face down. It is the first picture for the show. "
                                  "Can Diksha name any shape she is shown, just by looking at its parts?",
                     "problem": "The wind has mixed up every label. Colour and size do not tell Diksha where a label goes. "
                                "She needs a way to name each model that does not depend on colour or size.",
                     "thread": "Continues from the two webs story. Wiggly's web now has the thread across its corners. The "
                               "same wind that rocked his web blows the labels off Diksha's boxes.",
                     "leads_to": "The Shape Identification Quiz, where the child names shapes from pictures, one at a time. "
                                 "The video ends before the first card turns over.",
                 },
                 seconds=115)),
     # Tool 24 (new, CLASH 54): Lesson 9, the visual quiz. No book question.
     DOER("T10.C2", "Shape Identification Quiz", "shape_quiz", "Remember",
          "Students name each shape in a picture from the chapter, whether a solid, a net, an angle, a circle or a frame.",
          applies_to="T10.C1", key_terms=["prism", "pyramid", "net", "angle", "circle", "pentagon", "rigid shape"], minutes=6),
     # Tool 25 (new, CLASH 54): Lesson 9, the digital worksheet. No book question.
     DOER("T10.C3", "Digital Worksheet", "digital_worksheet", "Apply",
          "Students answer mixed questions on solids, angles, circles and rigid shapes: fill in the blanks, match, count and sort.",
          applies_to="T10.C1", key_terms=["prism", "pyramid", "net", "angle", "circle", "pentagon", "rigid shape"], minutes=8),
     # Tool 26 (new, CLASH 54, 56, 58): Lesson 9, the sample online assessment. Unscored: 8 questions in 3 sections, no clock, no marks
     # shown, no degrees, no cm. No book question.
     DOER("T10.C4", "Sample Online Assessment", "sample_assessment", "Apply",
          "Students answer a short assessment of eight questions on the whole chapter and check each answer.",
          applies_to="T10.C1", key_terms=["prism", "pyramid", "net", "angle", "circle", "pentagon", "rigid shape"], minutes=10)],
    topic_type="instructional", key_terms=["prism", "pyramid", "net", "angle", "circle", "pentagon", "rigid shape"]))

# ---- T11: the review (rows 41, 42) -------------------------------------------------------------------------------------------
# PROVISIONAL, CLASH 11 (option a): the review is an unscored look-back. The plan's assessment ideas are reworded as
# look-back prompts with a plain recap line after each: a prism has two matching end faces; an angle less than a right angle
# is acute; a pentagon has five sides; a corner is where edges meet (taught in T5); a net is a solid opened out flat; the
# diameter is double the radius (no cm sums); a right angle and an obtuse angle. No degrees, no polygon, no vertex, no marks.
# The recap lines restate rules taught earlier, so they are not plan-made answers to book questions. Every key term is one
# already taught; no book item, no new video or tool. The Topic 2 concept T2.C1 is named in review row 41 (T11.C1) so the review
# revises every idea topic (the gate checks it). T11.C2 covers the angle, circle, pentagon and rigidity topics and the recap
# concept of Topic 10 (T10.C1), so the review revises Lesson 9 too.
# The brief writer may trim or add look-back lines, but only ideas already taught.
# CLASH 49 (media step): the review has no video, no image node and no tool, so it carries NO picture. The child-facing steps are plain
# look-back questions ("Think of ...") answered from memory; no step names a picture or a VISUAL_KEY id.
# CLASH 58: this is the last topic because the pipeline wants a review last, with 1 to 2 concepts and no media; the Lesson 9 tools
# (Topic 10) come before it.
# BUILDER NOTE (never shown to the child): the earlier pictures each look-back recalls, in case a pinned recap picture is wanted later
# (pinned support is not verified): T11.C1 (row 41) recalls prisms, pyramids, prism_tent, pyramid_tent, box_net, nets_and_solids,
# cube_models; T11.C2 (row 42) recalls straws_angle, right_angle_checker, angle_figures_grid, circle_paper, rigid_shapes.
# The same list is in media_decisions.md section 6.
# Row 42, the straws: video row 23 makes Isha's straws fit the paper corner EXACTLY, so the look-back asks what kind of angle that was
# (a right angle), and then asks for the names of the narrow and the wide corner of video row 25.
TOPICS.append(TOPIC(
    "T11", "M5", "Looking Back", ["Summary"], "Understand",
    "",   # the review carries NO topic objective
    "You look back at solid shapes, angles, circles and firm shapes. Nothing is new and nothing is marked.",
    [A("T11.C1", "Look Back: Solid Shapes", "Understand",
       "Students name prisms, pyramids and nets, tell solids apart by their parts, and count the cubes in a tower.",
       role="review",
       key_terms=["clue", "side", "corner", "face", "edge", "prism", "pyramid", "net", "cube tower", "layer"],
       teach=["Look back at the hidden block game. Which clues helped you guess the shape?",
              "Sides, corners and flat or curved parts help tell one shape from another.",
              "Think of Diksha's pillar blocks. How many matching end faces does a prism have?",
              "Two matching end faces, joined by rectangles.",
              "Think of the two tents. How is a pyramid different from a prism?",
              "A pyramid has one bottom face. Its triangle faces meet at one point.",
              "Think of Diksha's gift box. What is a net?",
              "A net is a solid opened out flat. Folding it brings the solid back.",
              "Think of the block Diksha described to Nitesh. Where do edges meet?",
              "Edges meet at a corner. A solid has faces, edges and corners.",
              "Think of Nitesh's tower of cubes. How did Isha count every cube?",
              "Count layer by layer, and count the hidden cubes too."],
       review_covers=["T2.C1", "T3.C1", "T3.C2", "T3.C3", "T4.C1", "T5.C1", "T6.C1"], minutes=4),
     A("T11.C2", "Look Back: Angles, Circles and Firm Shapes", "Understand",
       "Students sort angles as acute, right or obtuse, name the parts of a circle, and tell which frames stay firm.",
       role="review",
       key_terms=["angle", "right angle", "acute angle", "obtuse angle", "circle", "centre", "radius", "diameter",
                  "pentagon", "rigid shape", "frame"],
       teach=["Think of Isha's straws joined at one end. What do two lines that meet at a point make?",
              "They make an angle.",
              "Isha opened her straws until they fitted the paper corner exactly. What kind of angle was that?",
              "A right angle. The corner of a paper fold is a right angle.",
              "Think of the narrow straw corner and the wide one. What are they called?",
              "The narrow one is acute: less than a right angle. The wide one is obtuse: more than a right angle.",
              "Think of the round paper you folded. Name the centre, the radius and the diameter.",
              "The centre is the middle. The radius goes from the centre to the border. The diameter goes across through the centre.",
              "Which is longer, the radius or the diameter?",
              "The diameter is double the radius.",
              "Think of the shape you built from equal straws. How many sides and corners does it have?",
              "Five sides and five corners. A shape with five sides is a pentagon.",
              "Think of the straw triangle and the straw rectangle. Which one keeps its shape when you push it?",
              "The triangle does. A stick across a four-sided frame makes triangles, so the frame stays firm."],
       review_covers=["T7.C1", "T7.C3", "T8.C1", "T8.C4", "T9.C1", "T9.C3", "T10.C1"], minutes=4)],
    topic_type="summary"))

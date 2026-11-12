# -*- coding: utf-8 -*-
"""Class 4 Ch 1, Shapes Around Us: the tool specs of Lesson 9 (Tool 24 Shape Identification Quiz, Tool 25 Digital Worksheet, Tool 26 Sample Online Assessment).

Loaded by concept_plan.py next to tools_1.py (every tools_N.py defines a dict TOOLS). The shared FRAME is in tools_1.py.

BRIEF WRITER, 12 Nov 2026. These three tools carry no book question (config no_book_question_tools). Every question in them is made for
this chapter: each is tagged Practice and its answer starts From the picture or Sample answer. Tool 26's answers are the lesson plan's
own key (Sample answer). No clock, no points, no marks shown, no degrees, no length units; nothing is scored. Tool 24 checks a tapped card at once and a
typed number at Check; Tool 25 checks the sorts and matches at once and the blanks and counts at Check; Tool 26 checks at the end of
each section and shows the key.

Every picture, number and sum below was made for this chapter and checked:
  Tool 24, picture 5: bottom layer 4 × 2 = 8 cubes, top layer 2 × 2 = 4 cubes, 8 + 4 = 12.
  Tool 25, item 5: one row 4 + 3 + 2 + 1 = 10 cubes, the row behind is the same, 10 + 10 = 20. Item 4: a triangular pyramid has
  3 edges round the bottom and 3 up to the top point, 3 + 3 = 6. Item 7: diameter 14, radius 14 ÷ 2 = 7, and 7 × 2 = 14.
  Tool 26: question 7, radius 6, diameter 2 × 6 = 12.
The recap story (T10.C1) shows none of these pictures and says none of these answers.
"""
from __future__ import annotations

from topics_common import T  # noqa: F401
from tools_1 import FRAME  # noqa: F401

# One `notice` prompt for each tool that carries no book question (the structure gate wants every tool to carry at least one
# question or prompt). Short plain sentences, no marks, no clock.
NOTICE_TOOL24 = ["What do you notice about the parts that help you name a shape?"]
NOTICE_TOOL25 = ["What do you notice when you count the parts of a shape?"]
NOTICE_TOOL26 = ["What do you notice about the parts of the shapes in each question?"]

# ----------------------------------------------------------------------------------------------------------------------
# Tool 24, the Shape Identification Quiz: ten pictures, one at a time, named from three cards or by a typed number.
# ----------------------------------------------------------------------------------------------------------------------
SCREEN24 = FRAME + (
    "First, one picture fills the screen, with three name cards under it. "
    "The cube tower picture has a number pad and a Check key instead of cards. "
    "Each question carries the small tag Practice, and its answer starts From the picture. "
    "No picture carries a name, a label or a number that gives the answer away. "
    "Every solid is one plain stone-grey tint, shaded and 3D, so colour gives no clue. "
    "Then, the child taps the card that names the picture. On the tower picture the child types a number and taps Check. "
    "A right answer turns green. The part its reason names lights up, and one reason line shows. "
    "A wrong card shakes gently and says what that shape has instead. Then it can be tried again. "
    "After the fourth hint, the hint itself greys out one wrong card. "
    "After the tenth picture, all ten show again as small tiles. Each tile has its answer line. "
    "The ten pictures follow the chapter in this order. The cards stay in the order listed. "
    "Picture 1, a solid: a pentagonal pyramid with its hidden edges dashed. Its bottom has five sides. "
    "Its five triangle faces meet at one point on top. "
    "Question: What is this solid? Cards: Square pyramid, Pentagonal pyramid, Hexagonal prism. "
    "Picture 2, a solid: a cylinder standing up. It has two flat round faces and one curved face. "
    "Question: What is this solid? Cards: Cylinder, Cone, Sphere. "
    "Picture 3, a net: a flat pattern in pale paper with violet dotted fold lines. Three rectangles lie in a row. "
    "One triangle joins the top of the middle rectangle. Another joins its bottom. "
    "Question: Which solid does this net fold into? Cards: Cube, Square pyramid, Triangular prism. "
    "Picture 4, a part of a solid: a cube with one edge lit in amber. Nothing else is marked. "
    "Question: What is the lit part? Cards: Edge, Face, Corner. "
    "Picture 5, a cube tower of teal cubes with clear edges. The bottom layer is 4 cubes long and 2 wide. "
    "A smaller layer of 2 by 2 cubes sits on it. "
    "Question: How many cubes are in this tower? The hidden ones count too. Number pad, one or two digits. "
    "Picture 6, an angle: a green straw and an orange straw joined by a clay ball. A red arc marks the corner. "
    "A folded paper corner lies beside it. The angle is clearly narrower than the paper corner. "
    "Question: What kind of angle is this? Cards: Right angle, Obtuse angle, Acute angle. "
    "Picture 7, a circle: a plain circle on pale paper with its centre dot showing. "
    "One bold line runs across it through the centre dot. Both ends of the line touch the circle. "
    "No word is on the picture. "
    "Question: What is the bold line? Cards: Radius, Diameter, Centre. "
    "Picture 8, a flat shape: a flat purple pentagon, turned a little. No side lies along the bottom. "
    "Question: What is this shape? Cards: Hexagon, Square, Pentagon. "
    "Picture 9, a frame: three green straws joined at their ends by red clay balls. "
    "Question: What is this frame? Cards: Triangle frame, Square frame, Pentagon frame. "
    "Picture 10, a frame: four blue straws joined by red clay balls. "
    "Two long straws sit opposite each other. Two short straws sit opposite each other. Every corner is square. "
    "Question: What is this frame? Cards: Square frame, Rectangle frame, Pentagon frame. "
    "Then, after the tenth picture and its tiles, a thought bubble reads the notice prompt. It is read, not answered."
)

# ----------------------------------------------------------------------------------------------------------------------
# Tool 25, the Digital Worksheet: nine mixed items, one lesson idea each; fill in the blank, match, count and sort.
# ----------------------------------------------------------------------------------------------------------------------
SCREEN25 = FRAME + (
    "First, a short worksheet of nine items opens, one item at a time. "
    "Each item has a small heading in plain words that names the idea it practises. "
    "Each item carries the small tag Practice. Each answer line starts From the picture. "
    "Items 2 and 7 are fill in the blank items. Their answer lines start Sample answer. "
    "Then, the child taps a card, drags a card or a shape, or types a number. "
    "There is one rule. The sort and match items (1, 3, 6, 8 and 9) show right or wrong at once, and they have no Check. "
    "A dragged card that fits stays, turns green and shows one reason line. "
    "A dragged card that does not fit shakes gently, slides back and says what to look at, and can be tried again. "
    "Only the fill in the blank and count items (2, 4, 5 and 7) use Check. The child taps a card or types a number, then taps Check. "
    "A right answer turns green and one reason line shows. "
    "A wrong answer shakes gently, says why it does not fit, and can be tried again. "
    "The Hint lamp never gives the answer. It says where to look and what to try. "
    "After the ninth item, all nine show again as small tiles. Each tile has its answer line. "
    "Every solid is one plain stone-grey tint, shaded and 3D. "
    "A net is pale paper with violet dotted fold lines, never the colour of a solid. "
    "The nine items follow the lessons in this order. "
    "Item 1, Curved or flat: sort by dragging. Six solids lie in a tray. "
    "They are a sphere, a cube, a cone, a cuboid, a cylinder and a triangular prism. "
    "Two boxes wait: Has a curved part, and All parts flat. Drag each solid into its box. "
    "Item 2, Prism or pyramid: fill in the blank by tapping a card. "
    "Sentence: A solid with two matching triangle ends and three rectangle sides is a triangular ____. "
    "Cards: pyramid, prism, cone. "
    "Item 3, Nets and solids: match by dragging. Three nets in pale paper lie on the left. "
    "One is six squares joined in a cross. One is a rectangle with a circle at each end. "
    "One is a square with a triangle on each side. "
    "Three solids stand on the right: a cylinder, a square pyramid and a cube. "
    "Drag each net onto the solid it folds into. "
    "Item 4, Counting edges: count by typing. A triangular pyramid is shown with its hidden edges dashed. "
    "Question: How many edges does this solid have? The dashed edges count too. Number pad, one digit. "
    "Item 5, Cube towers: count by typing. A stair of teal cubes, two cubes deep. "
    "From the front and above, the columns are 4, 3, 2 and 1 cubes tall. "
    "The top of each column shows both cubes of its depth. "
    "Question: How many cubes make this stair? Number pad, one or two digits. "
    "Item 6, Angles: sort by dragging. Six angle cards lie in a tray. "
    "Each is two straws joined at one end, with a red arc at the corner. "
    "A small folded paper corner is drawn beside each one. "
    "Two angles are narrower than the paper corner. Two fit it exactly, and one of those is turned. "
    "Two are wider than it. "
    "Three boxes wait: Acute angle, Right angle and Obtuse angle. Drag each angle card into its box. "
    "Item 7, Radius and diameter: fill in the blank by typing. "
    "A plain circle shows a bold line across it through the centre dot. The line is marked 14. "
    "Sentence: The line across through the centre is 14 long. The line from the centre to the circle is ____ long. "
    "Number pad, one digit, no unit. "
    "Item 8, Sides of flat shapes: match by dragging. Three flat shapes in flat colours lie in a row. "
    "They are a blue triangle, a red rectangle and a purple pentagon. The pentagon is turned a little. "
    "Three cards wait: 3 sides, 4 sides and 5 sides. Drag each card onto its shape. "
    "Item 9, Firm frames: sort by dragging. Six straw frames lie in a tray. "
    "They are a triangle, a rectangle, a square and a pentagon. "
    "Two more are a square and a rectangle with a stick across the corners. "
    "Two boxes wait: Keeps its shape when pushed, and Leans when pushed. Drag each frame into its box. "
    "Then, after the ninth item and its tiles, a thought bubble reads the notice prompt. It is read, not answered."
)

# ----------------------------------------------------------------------------------------------------------------------
# Tool 26, the Sample Online Assessment: the lesson plan's eight questions in three sections, checked at the end of each section.
# ----------------------------------------------------------------------------------------------------------------------
SCREEN26 = FRAME + (
    "First, a short assessment opens with three sections, one at a time. "
    "They are Fill in the blanks, Short answers and Solve. "
    "No clock runs. No marks and no total show. "
    "Each question carries the small tag Practice. "
    "Then, the child answers every question of the section. The child taps a card or types a number. "
    "A tapped card can be changed until the section is checked. "
    "Next, the child taps Check this section. "
    "Every answer is checked now, not before. A right answer turns green. "
    "A wrong answer stays as it was. The key shows under it with a reason. "
    "Every key line starts Sample answer. "
    "After the check the answers are locked. Reset clears the section so it can be tried again. "
    "The key hides until the next check. "
    "The Hint lamp gives a reminder and never the answer. "
    "Section A, Fill in the blanks, three questions. "
    "Question 1: A prism has ____ matching end faces. Number pad, one digit. "
    "Question 2: An angle smaller than a right angle is called ____. "
    "Cards: an obtuse angle, a right angle, an acute angle. "
    "Question 3: A shape with five sides is called a ____. Cards: square, pentagon, hexagon. "
    "Section B, Short answers, three questions. The child taps the sentence that is right, from three sentences. "
    "Question 4: What is a corner of a solid? "
    "Sentences: A point where edges meet. A flat side of the solid. A line where two faces meet. "
    "Question 5: What is a net of a solid? "
    "Sentences: A model of the solid made from straws. A picture of the solid from the front. "
    "A flat pattern that folds to make the solid. "
    "Question 6: How are the diameter and the radius of a circle linked? "
    "Sentences: The diameter is half the radius. The diameter is double the radius. "
    "The diameter and the radius are the same. "
    "Section C, Solve, two questions. "
    "Question 7: A circle has a radius of 6. What is its diameter? Number pad, one or two digits, no unit. "
    "Question 8: Two angle pictures, a and b. "
    "Each is two straws joined at one end, with a red arc at the corner. "
    "A folded paper corner lies beside each one. "
    "Picture a is a right angle. It is turned a little, so it does not look like an upright L. "
    "Picture b is wider than the paper corner. "
    "The child names each one. Cards under each picture: acute angle, right angle, obtuse angle. "
    "Then, after the last section is checked, a thought bubble reads the notice prompt. It is read, not answered."
)

TOOLS = {
    # Tool 24: Lesson 9, the shape identification quiz. Covers the whole chapter; no book question.
    "shape_quiz": T(
        "tool_shape_identification_quiz", "Shape Identification Quiz", 24,
        "Students name each shape in a picture from the chapter, whether a solid, a net, an angle, a circle or a frame.",
        notice=NOTICE_TOOL24,
        screen=SCREEN24,
        controls=["Tap a name card or a digit", "Tap Check", "Reset"],
        instruction="Look at the picture. Tap the name that fits it, or type the number.",
        feedback=[
            "Picture 1. Right: The bottom has five sides and the triangles meet at one point. It is a pentagonal pyramid. "
            "Wrong card, Square pyramid: A square pyramid has a four-sided bottom. Count the sides of this bottom. "
            "Wrong card, Hexagonal prism: A prism has matching ends and no point on top. This solid has a point.",
            "Picture 2. Right: Two flat round faces and one curved face make a cylinder. "
            "Wrong card, Cone: A cone has one flat round face and a point. This solid has two flat faces. "
            "Wrong card, Sphere: A sphere has no flat face. This solid has flat round ends.",
            "Picture 3. Right: Two triangles and three rectangles fold into a triangular prism. "
            "Wrong card, Cube: A cube's net has six squares. This net has triangles. "
            "Wrong card, Square pyramid: Its net has one square and four triangles. Count the triangles here.",
            "Picture 4. Right: An edge is a line where two faces meet. "
            "Wrong card, Face: A face is one side of a solid, flat or curved. The lit part is only a line. "
            "Wrong card, Corner: A corner is a point. The lit part is a line between two corners.",
            "Picture 5. Right: The bottom layer is 4 × 2 = 8 cubes. The top layer is 2 × 2 = 4 cubes. 8 + 4 = 12. "
            "A number below 12: Some cubes are hidden under the top layer. Count layer by layer. "
            "A number above 12: Count each layer once. Then add the layers.",
            "Picture 6. Right: The angle fits inside the paper corner. It is smaller than a right angle, so it is acute. "
            "Wrong card, Right angle: A right angle fits the paper corner exactly. This one leaves room. "
            "Wrong card, Obtuse angle: An obtuse angle sticks out past the paper corner. This one is narrower.",
            "Picture 7. Right: The line goes across the circle through the centre. It is a diameter. "
            "Wrong card, Radius: A radius goes only from the centre to the circle. This line goes right across. "
            "Wrong card, Centre: The centre is one point in the middle. The bold part is a line.",
            "Picture 8. Right: Five straight sides make a pentagon. "
            "Wrong card, Hexagon: A hexagon has six sides. Count the sides again. "
            "Wrong card, Square: A square has four sides. Count the sides of this shape.",
            "Picture 9. Right: Three straws and three joints make a triangle frame. It keeps its shape when pushed. "
            "Wrong card, Square frame: A square frame has four straws. Count the straws here. "
            "Wrong card, Pentagon frame: A pentagon frame has five straws. Count the straws here.",
            "Picture 10. Right: Two long straws and two short straws make a rectangle frame. It leans over when pushed. "
            "Wrong card, Square frame: A square frame has four equal straws. Compare the long and the short straws. "
            "Wrong card, Pentagon frame: A pentagon frame has five straws. Count the straws here.",
        ],
        done_when="All ten pictures are named right, the reason of each one has been shown, and the thought bubble has been read.",
        shared_state=["currentPicture", "chosenCard", "typedNumber", "greyedCards", "namedRight"],
        misconceptions=["M_SH_2", "M_SH_3", "M_SH_4", "M_SH_6", "M_SH_7", "M_AN_4", "M_CI_2", "M_AN_5", "M_AN_9"],
        hints=["Look at the whole picture first. Is it a solid, a flat pattern, an angle, a circle or a frame?",
               "Look for parts you can count: faces, edges, corners, sides or layers. Dashed lines are hidden edges, and they count.",
               "Think of the shape you built, folded or pushed in the tools. Which card has the same parts?",
               "Test one card at a time against the parts you counted. Keep the card that fits all of them."],
        visuals=["solid_colours", "pyramids", "solid_pictures", "nets_and_solids", "cube_towers", "angle_mark",
                 "straws_angle", "right_angle_checker", "circle_paper", "angle_shapes", "rigid_shapes"]),

    # Tool 25: Lesson 9, the digital worksheet. Covers the eight lessons; no book question.
    "digital_worksheet": T(
        "tool_digital_worksheet", "Digital Worksheet", 25,
        "Students answer mixed questions on solids, angles, circles and rigid shapes: fill in the blanks, match, count and sort.",
        notice=NOTICE_TOOL25,
        screen=SCREEN25,
        controls=["Tap a card or a digit", "Drag a card or a shape into place", "Tap Check", "Reset"],
        instruction="Do each item in turn. Tap Check for blanks and counts.",
        feedback=[
            "Item 1, Curved or flat. Right: The sphere, the cone and the cylinder have a curved part. "
            "The cube, the cuboid and the triangular prism have only flat faces. "
            "A solid in the wrong box slides back. It says whether that solid has a curved part.",
            "Item 2, Prism or pyramid. Right: Matching ends with rectangles between them make a prism. "
            "Wrong card, pyramid: A pyramid has one bottom face and triangles that meet at a point. "
            "Wrong card, cone: A cone has a curved side. This solid has flat sides.",
            "Item 3, Nets and solids. Right: Six squares fold into a cube. "
            "Two circles and a rectangle fold into a cylinder. One square and four triangles fold into a square pyramid. "
            "A net on the wrong solid slides back. It says what flat shapes that net has.",
            "Item 4, Counting edges. Right: There are 3 edges round the bottom and 3 up to the top point. 3 + 3 = 6. "
            "A different number: Count every line where two faces meet. The dashed ones count too.",
            "Item 5, Cube towers. Right: One row has 4 + 3 + 2 + 1 = 10 cubes. The row behind is the same, so 10 + 10 = 20. "
            "A different number: Count one row first. Then think about the row behind it.",
            "Item 6, Angles. Right: The narrow angles fit inside the paper corner, so they are acute. "
            "The angles that fit it exactly are right angles. The wide ones stick out past it, so they are obtuse. "
            "A card in the wrong box slides back. It says to lay the paper corner on it.",
            "Item 7, Radius and diameter. Right: The diameter is double the radius. So the radius is 14 ÷ 2 = 7. "
            "A different number: Double the radius gives the diameter. Which number doubled makes 14?",
            "Item 8, Sides of flat shapes. Right: A triangle has 3 sides. A rectangle has 4 sides. A pentagon has 5 sides. "
            "A card on the wrong shape slides back. It says to count the straight sides.",
            "Item 9, Firm frames. Right: The triangle keeps its shape. So do the two frames with a stick across the corners. "
            "The rectangle, the square and the pentagon lean when pushed. "
            "A frame in the wrong box slides back. It says to look for triangles inside it.",
            "Sorts and matches show right or wrong at once. Blanks and counts show it after Check.",
        ],
        done_when="All nine items are answered right, the reason of each one has been shown, and the thought bubble has been read. "
                  "Sorts and matches are right at once. Blanks and counts are right after Check.",
        shared_state=["currentItem", "chosenCard", "typedNumber", "placedCards", "greyedAnswers", "itemsDone"],
        misconceptions=["M_SH_2", "M_SH_3", "M_SH_4", "M_SH_6", "M_SH_7", "M_AN_3", "M_AN_5", "M_AN_9", "M_CI_3"],
        hints=["Read the heading. It names the idea this item practises.",
               "Look at the picture or the cards slowly. Which parts matter here?",
               "Think of the tool where you met this idea. What did you do there?",
               "Test one card, or one count, at a time. Say what you checked. Keep what fits."],
        visuals=["solid_colours", "solid_pictures", "sphere", "prisms", "pyramids", "nets_and_solids", "cube_towers",
                 "angle_mark", "straws_angle", "right_angle_checker", "circle_paper", "angle_shapes", "rigid_shapes",
                 "straws_and_clay"]),

    # Tool 26: Lesson 9, the sample online assessment: 8 questions in 3 sections, unscored (CLASH 56, 58); no book question.
    "sample_assessment": T(
        "tool_sample_online_assessment", "Sample Online Assessment", 26,
        "Students answer a short assessment of eight questions on the whole chapter and check each answer.",
        notice=NOTICE_TOOL26,
        screen=SCREEN26,
        controls=["Tap a card or a digit", "Tap Check this section", "Reset"],
        instruction="Answer each question. Tap Check this section when you finish it.",
        feedback=[
            "Check this section turns every right answer green and shows its key line under it.",
            "A wrong answer stays as it was, and the key shows under it with a reason. Nothing is marked and nothing is added up.",
            "Question 1. Sample answer: two. A prism has two end faces that match, with rectangles between them.",
            "Question 2. Sample answer: an acute angle. It is smaller than a right angle, so it fits inside a paper corner.",
            "Question 3. Sample answer: pentagon. A shape with five sides is a pentagon.",
            "Question 4. Sample answer: a point where edges meet. An edge is a line where two faces meet.",
            "Question 5. Sample answer: a flat pattern that folds to make the solid. Folding it brings the solid back.",
            "Question 6. Sample answer: the diameter is double the radius, so diameter = 2 × radius.",
            "Question 7. Sample answer: 12. The diameter is double the radius, and 2 × 6 = 12.",
            "Question 8. Sample answer: a is a right angle, and b is an obtuse angle. "
            "Picture a fits the paper corner exactly, and picture b is wider than it.",
        ],
        done_when="All three sections are checked, the key of every question has been shown, and the thought bubble has been read.",
        shared_state=["currentSection", "answers", "sectionChecked", "keyShown"],
        misconceptions=["M_SH_1", "M_SH_4", "M_SH_7", "M_AN_3", "M_AN_4", "M_CI_3"],
        hints=["Read the question slowly. What does it ask you to name or find?",
               "Think of the tool where you met this idea in the chapter.",
               "Say what you remember about it in your own words.",
               "Choose the answer you can explain. The key shows after you check the section."],
        visuals=["angle_mark", "straws_angle", "right_angle_checker"]),

}

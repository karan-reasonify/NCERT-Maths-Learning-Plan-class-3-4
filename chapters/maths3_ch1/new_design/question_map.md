# Question map: Class 3, Chapter 1, "What's in a Name?" (rebuild from zero)

Step 5 (c34-question-mapper). Every book item of the chapter is tagged question -> concept -> tool. The homes are written as
`FIO(...)` in `topics_1.py` (`items` of the tool concept, or of the image concept T7.C3 for ch1.letus10) and as `ncert=[...]` for
text and talk items. Clash numbers refer to `content.CLASHES`. Every video, image and tool is a placeholder. Page = pdf page
(printed page), as in `analysis.md`.

Result: 43 book items = 29 questions (20 exercise, 7 prompt, 2 example) + 14 not questions (9 text, 5 talk). Each item has ONE home.
Nothing is excluded: every item is printed in this chapter's 8 pages, checked against the 8 page PNGs (the 47 marks on the stone slab
were counted again on a zoomed crop: rows of 4, 4 and 1 groups of five, then 2 extra). The homes are exactly the ones
`tool_map.locked.md` proposed; no question was moved. The cap is 6 questions per tool (`chapter.config.json` max_tool_questions, not
changed): the largest tool, Tool 7, holds exactly 6. The two notebook tasks (ch1.letus4b, ch1.letus7) are the book's questions, shown
as short optional instruction cards on their tool, as the note asks. ch1.letus10 sits on the image concept T7.C3 because no tool
follows it (the flow gate allows a book question on an image concept when no tool follows it; CLASH 24).

## The map

Columns: id | kind | page | concept (plan key, analysis code) | tool | label shown | in / excluded (why). "stretch" = a home that is a
judgement call the user can reverse (the clash is named).

| id | kind | page | concept | tool | label | status |
|---|---|---|---|---|---|---|
| opening | text | 1 | T1.C1 The Cows of Tarakeshwar, hook (C1) | none: teaching text (`ncert` of the hook) | | in (text) |
| ch1.story1 | talk | 1 | T1.C1 (C1) | none: teaching text (`ncert` of the hook) | | in (talk) |
| ch1.rule1 | text | 1 | T1.C2 Marks at the Gate (C1) | none: task text of Tool 1 (`ncert` of T1.C2) | | in (text; the friend's rule is Tool 1's task) |
| ch1.story2 | prompt | 1 | T1.C2 (C1) | T1.C2, Tool 1 Marks at the Gate | Story, cows back home | in (stretch, CLASH 1: a book question on the exploration tool; no number in it) |
| ch1.wall1 | text | 2 | T2.C1 Reading the Marks, video (C2) | none: teaching text (`ncert` of the row 3 video) | | in (text; its second sentence is copied into the question ch1.fill1, CLASH 39) |
| ch1.fill1 | prompt | 2 | T2.C2 Count the Big Herd (C2) | T2.C2, Tool 2 Count the Big Herd | Story, how many cows | in (47 = 9 groups of 5 and 2 extra, read from the picture, CLASH 3, 39) |
| ch1.story3 | text | 2 | T2.C2 (C2) | none: teaching text (`ncert` of Tool 2's concept) | | in (text) |
| ch1.story4 | prompt | 2 | T2.C2 (C2) | T2.C2, Tool 2 | Story, why worried | in (the 2 cows still out are said in the answer, CLASH 3) |
| ch1.fill2 | prompt | 2 | T2.C2 (C2) | T2.C2, Tool 2 | Story, cows reached home | in (47 − 2 = 45) |
| ch1.found1 | text | 2 | T2.C2 (C2) | none: teaching text (`ncert` of Tool 2's concept) | | in (text; shown after the child's answers) |
| ch1.hemant1 | exercise | 2 | T2.C4 Hemant's Cows and Sheep (C3) | T2.C4, Tool 3 Hemant's Cows and Sheep | Story, Hemant's herd | in (36 and 23 kept apart; the sum 59 is never shown, CLASH 5) |
| ch1.tnote1 | talk | 2 | T2.C4 (C1, C2, C3) | none: teaching text (`ncert` of Tool 3's concept) | | in (talk; no teacher role, its idea is a line for the child) |
| ch1.letus1 | exercise | 3 | T3.C2 Longest and Shortest Names (C4) | T3.C2, Tool 4 Longest and Shortest Names | Let us Do, Q1 | in ("animals and birds" not repeated, CLASH 10; elephant 8, ox 2) |
| ch1.longer1 | prompt | 3 | T3.C2 (C4) | T3.C2, Tool 4 | Let us Do, Q1 note | in (open: the child types an animal, Sample answer crocodile, 9 letters, CLASH 10) |
| ch1.letus2 | exercise | 3 | T3.C2 (C4) | T3.C2, Tool 4 | Let us Do, Q2 | in (Mahesh 6, Kartik 6: neither is longer, CLASH 9) |
| ch1.letus3 | exercise | 4 | T3.C2 (C4; analysis C5) | T3.C2, Tool 4 | Let us Do, Q3 | in (stretch, CLASH 6: moved from C5 to keep Tool 5 at 5; typed names, CLASH 8) |
| ch1.letus3a | exercise | 4 | T3.C2 (C4; analysis C5 uses C4) | T3.C2, Tool 4 | Let us Do, Q3(a) | in (stretch, CLASH 6; the eight book names: tick Hemant, Mahesh, Kartik; cross Deba, Deep, Teji, Jojo, Mala) |
| ch1.letus3b | exercise | 4 | T4.C2 Starting and Ending Letters (C5) | T4.C2, Tool 5 Starting and Ending Letters | Let us Do, Q3(b) | in (own name typed; Mala as the example, CLASH 7, 8) |
| ch1.letus3c | exercise | 4 | T4.C2 (C5) | T4.C2, Tool 5 | Let us Do, Q3(c) | in (own name; 0 matches when the letter is outside D, H, J, K, M, T) |
| ch1.letus3d | exercise | 4 | T4.C2 (C5) | T4.C2, Tool 5 | Let us Do, Q3(d) | in (D and M tie, 2 each, decided CLASH 7; "From the picture") |
| ch1.letus3e | exercise | 4 | T4.C2 (C5) | T4.C2, Tool 5 | Let us Do, Q3(e) | in (read as the same ending letter as your own name, CLASH 6; a 2) |
| ch1.letus3f | exercise | 4 | T4.C2 (C5) | T4.C2, Tool 5 | Let us Do, Q3(f) | in (20 letters on the alphabet strip, CLASH 7; "From the picture") |
| ch1.tnote2 | talk | 4 | T4.C2 (C5) | none: teaching text (`ncert` of Tool 5's concept) | | in (talk) |
| ch1.cards1 | text | 5 | T5.C2 Build a Number Name (C6) | none: teaching text (`ncert` of Tool 6's concept) | | in (text; the 27 cards are Tool 6's scene) |
| ch1.example1 | example | 5 | T5.C2 (C6) | T5.C2, Tool 6 Build a Number Name | Let us Do, Q4, Teji's number | in (43: Forty 5 + Three 5 = 10, printed in the book) |
| ch1.fill3 | prompt | 5 | T5.C2 (C6) | T5.C2, Tool 6 | Let us Do, Q4, Jojo's number | in (17: Seventeen, 9 letters) |
| ch1.letus4a | exercise | 5 | T5.C2 (C6) | T5.C2, Tool 6 | Let us Do, Q4(a) | in (roll number 1 to 99 typed on a number pad, CLASH 8, 14; "end of the book" not repeated; sample 91) |
| ch1.letus4b | exercise | 5 | T5.C2 (C6) | T5.C2, Tool 6 | Let us Do, Q4(b) | in (the notebook task, a short optional instruction card, not a separate tool) |
| ch1.example2 | example | 5 | T6.C2 Number Name Puzzles (C7) | T6.C2, Tool 7 Number Name Puzzles | Let us Think, 56 | in (stretch, CLASH 15: a solved example on a tool; Fifty 5 + Six 3 = 8, printed in the book) |
| ch1.think1 | exercise | 5 | T6.C2 (C7) | T6.C2, Tool 7 | Let us Think | in (the 13 numbers with 8 letters, computed by program) |
| ch1.tnote3 | talk | 5 | T6.C2 (C7) | none: teaching text (`ncert` of Tool 7's concept) | | in (talk) |
| ch1.letus5 | exercise | 6 | T6.C2 (C8, inside Tool 7) | T6.C2, Tool 7 | Let us Do, Q1 | in (73, 77, 78: 12 letters each, CLASH 15) |
| ch1.letus6a | exercise | 6 | T6.C2 (C8) | T6.C2, Tool 7 | Let us Do, Q2, first Find out | in (copied Q2 stem not shown, CLASH 16; 93, 97 and 98 accepted) |
| ch1.letus6b | exercise | 6 | T6.C2 (C8) | T6.C2, Tool 7 | Let us Do, Q2, second Find out | in ("smallest" read as fewest letters: 70, CLASH 17) |
| ch1.letus7 | exercise | 6 | T6.C2 (C8) | T6.C2, Tool 7 | Let us Do, Q3 | in (the notebook task, a short optional instruction card; Tool 7 is at the cap of 6 with it) |
| ch1.place1 | text | 6 | T6.C3 Longest and Shortest Place Names (C9) | none: teaching text (`ncert` of the image) | | in (text; the book asks nothing here, CLASH 18) |
| ch1.place2 | text | 6 | T6.C3 (C9) | none: teaching text (`ncert` of the image) | | in (text) |
| ch1.group1 | text | 6, 7 | T7.C1 Grouping by a Rule, video (C10) | none: teaching text (`ncert` of the row 16 video) | | in (text) |
| ch1.jojo1 | prompt | 7 | T7.C2 Group the Cards Two Ways (C11) | T7.C2, Tool 8 Group the Cards Two Ways | Story, Jojo's groups | in ("each groups" not repeated, CLASH 20; things that fly and do not fly) |
| ch1.letus8 | exercise | 7 | T7.C2 (C10) | T7.C2, Tool 8 | Let us Do, Q4 | in (four and four; lamp and clock read as electric, CLASH 21) |
| ch1.letus9 | exercise | 8 | T7.C2 (C11) | T7.C2, Tool 8 | Let us Do, group differently | in ("the given objects" not repeated, CLASH 22; any valid grouping accepted) |
| ch1.tnote4 | talk | 8 | T7.C2 (C10, C11) | none: teaching text (`ncert` of Tool 8's concept) | | in (talk) |
| ch1.letus10 | exercise | 8 | T7.C3 Hair Styles in a Class (C12) | none: the question sits on the image concept T7.C3 (no tool follows it) | Let us Do, Hair Styles | in (stretch, CLASH 24: the one question on an image; the plan's class of 12, counts 3, 2, 2, 1, 3, 1, CLASH 23) |

## Per tool

| Tool | tool concept | book questions on the tool, in the book's order | count | against the cap of 6 |
|---|---|---|---|---|
| 1 Marks at the Gate | T1.C2 (explore) | story2 (the tool's 3 notice prompts are the plan's own, not book questions) | 1 | ok |
| 2 Count the Big Herd | T2.C2 | fill1, story4, fill2 | 3 | ok |
| 3 Hemant's Cows and Sheep | T2.C4 | hemant1 | 1 | ok |
| 4 Longest and Shortest Names | T3.C2 | letus1, longer1, letus2, letus3, letus3a | 5 | ok (CLASH 6) |
| 5 Starting and Ending Letters | T4.C2 | letus3b, letus3c, letus3d, letus3e, letus3f | 5 | ok |
| 6 Build a Number Name | T5.C2 | example1, fill3, letus4a, letus4b (optional notebook card) | 4 | ok |
| 7 Number Name Puzzles | T6.C2 | example2, think1, letus5, letus6a, letus6b, letus7 (optional notebook card) | 6 | at the cap (CLASH 15) |
| 8 Group the Cards Two Ways | T7.C2 | jojo1, letus8, letus9 | 3 | ok |
| (no tool) image Hair Styles in a Class | T7.C3 | letus10 | 1 | not a tool (CLASH 24) |

29 questions = 1 + 3 + 1 + 5 + 5 + 4 + 6 + 3 + 1. The hook (T1.C1), the other image concepts (T4.C1 Name Tags, T6.C3 Place Names), the
bridge and the six concept videos' own concepts (T2.C1, T2.C3, T3.C1, T5.C1, T6.C1, T7.C1) and the review (T8.C1, T8.C2) hold no book
question.

By kind: 20 exercise (hemant1, letus1, letus2, letus3, letus3a to letus3f, letus4a, letus4b, think1, letus5, letus6a, letus6b, letus7,
letus8, letus9, letus10), 7 prompt (story2, fill1, story4, fill2, longer1, fill3, jojo1), 2 example (example1, example2). Not
questions, 14: 9 text (opening, rule1, wall1, story3, found1, cards1, place1, place2, group1) and 5 talk (story1, tnote1, tnote2, tnote3,
tnote4).

## Excluded

Nothing. All 43 items are printed on pdf pages 1 to 8 of this chapter. Nothing from another chapter, the prelims, or "extra" or
"advanced" material was found in the chapter file, and none was added. The pieces of the content team's table that are NOT book
questions, and so are not mapped here, are the plan's own steps inside a tool: the "2 cows still out" step (Tool 2), the Name Tags
picture and its orange and blue letters (Tool 5), the notice prompts of Tool 1, the stages and rule cards of Tool 8, and the six hair
style counts (an answer block).

## Answer labels (the book prints no answer anywhere)

Every plan-made answer begins exactly "From the picture" (13) or "Sample answer" (16). Total 29.
- "From the picture": story2, fill1 (47), story4, fill2 (45), letus1 (elephant 8, ox 2), letus3d (D and M tie), letus3f (20 letters),
  example1 (10), fill3 (9), example2 (8), jojo1 (fly / do not fly), letus8 (the electricity split), letus10 (3, 2, 2, 1, 3, 1).
- "Sample answer ... Your answer may differ" (12): hemant1, longer1, letus3, letus3a, letus3b, letus3c, letus3e, letus4a, letus4b,
  think1, letus7, letus9.
- "Sample answer" (4, closed counts worked out by program, no "may differ"): letus2 (6 and 6), letus5 (73, 77, 78), letus6a (93, 97, 98),
  letus6b (70). The user decides whether these four keep "Sample answer" (CLASH 9, 16, 17).

## Checks of numbers (by program, then by eye on the page images)

Animal names: tiger 5, dog 3, snake 5, goat 4, lion 4, elephant 8, deer 4, ox 2, rat 3, monkey 6. The eight names: Deba 4, Deep 4,
Hemant 6, Mahesh 6, Kartik 6, Teji 4, Jojo 4, Mala 4. Starting letters D 2, H 1, J 1, K 1, M 2, T 1 (8 names); ending letters a 2, h 1,
i 1, k 1, o 1, p 1, t 1 (8 names); 26 − 6 = 20 letters start no name. 47 marks = 9 × 5 + 2 = 45 + 2; 47 − 2 = 45. Hemant: 36 = 7 × 5 + 1,
23 = 4 × 5 + 3, together 36 + 23 = 59 marks (only a check, never shown to the child). Number names: 43 = Forty 5 + Three 5 = 10; 17 =
Seventeen 9; 56 = Fifty 5 + Six 3 = 8; 42 = 8; seventy 7; sixty-three 10; twenty-three 11; 73, 77, 78 = 12; 91 = Ninety 6 + One 3 = 9.
Eight-letter numbers (13): 13, 14, 18, 19, 41, 42, 46, 51, 52, 56, 61, 62, 66. Two words of 6 + 5 letters (12): 23, 27, 28, 33, 37, 38,
83, 87, 88, 93, 97, 98. From 63 to 78 the fewest letters is 70 (7); the next fewest is 66 (8). Hair styles: 3 + 2 + 2 + 1 + 3 + 1 = 12.

## New clash from this step

CLASH 39 (judgement call): ch1.wall1 stays on the row 3 video and its second sentence is copied into the question ch1.fill1 on Tool 2;
the printed "their wall" against the stone slab figure. Recommendation: keep as done. QUESTION MAPPER notes were also added to CLASH 1, 3,
5, 6, 7, 8, 9, 10, 14, 15, 16, 17, 20, 21, 22, 23 and 24. No cap clash: every tool is at or under 6.

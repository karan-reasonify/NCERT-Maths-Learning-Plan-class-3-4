# Question map: Class 3, Chapter 1, "What's in a Name?"

Step 5 (c34-question-mapper). Every book item of the chapter is tagged question -> concept -> tool. The homes are written as
`FIO(...)` in `topics_1.py` (`items` of the tool concept, or of the image concept T7.C3 for ch1.letus10) and as `ncert=[...]`
for text and talk items. Clash numbers refer to `content.CLASHES`. Every video, image and tool is a placeholder. Page = pdf
page (printed page), as in `analysis.md`.

Result: 43 book items = 29 questions (20 exercise, 7 prompt, 2 example) + 14 not questions (9 text, 5 talk). Each item has ONE
home. Nothing is excluded: every item is printed in this chapter's 8 pages (checked against the 8 page PNGs; the 47 marks on the
stone slab were counted again on a zoomed crop). Nothing was moved from the tool mapper's proposal in `tool_map.locked.md`.
The cap is 6 questions per tool (`chapter.config.json` max_tool_questions, not changed): the largest tool holds exactly 6.

## The map

Columns: id | kind | page | concept (plan key, analysis code) | tool (plan key, approved number and name) | label shown | status.
"stretch" = a home that is a judgement call the user can reverse (the clash is named).

| id | kind | page | concept | tool | label | status |
|---|---|---|---|---|---|---|
| opening | text | 1 (1) | T1.C1 The Cows of Tarakeshwar, the hook (C1) | none: teaching text (`ncert` of the hook) | | in (text) |
| ch1.story1 | talk | 1 (1) | T1.C1 (C1) | none: teaching text (`ncert` of the hook) | | in (talk) |
| ch1.rule1 | text | 1 (1) | T1.C2 Marks at the Gate (C1) | none: the task text of Tool 1 (`ncert` of T1.C2) | | in (text; the friend's rule is Tool 1's task) |
| ch1.story2 | prompt | 1 (1) | T1.C2 (C1) | T1.C2, Tool 1 Marks at the Gate | Story, cows back home | in (stretch, CLASH 2: a book question on the exploration tool) |
| ch1.wall1 | text | 2 (2) | T2.C1 The Marks Left on the Wall (C2) | none: teaching text (`ncert` of video 1) | | in (text, CLASH 32) |
| ch1.fill1 | prompt | 2 (2) | T2.C1 (C2) | T2.C2, Tool 2 Marks for a Big Herd | Story, how many cows | in (47 read from the picture, CLASH 11 a) |
| ch1.story3 | text | 2 (2) | T2.C1 (C2) | none: teaching text (`ncert` of video 1) | | in (text, CLASH 32) |
| ch1.story4 | prompt | 2 (2) | T2.C1 (C2) | T2.C2, Tool 2 | Story, why worried | in |
| ch1.fill2 | prompt | 2 (2) | T2.C1 (C2) | T2.C2, Tool 2 | Story, cows reached home | in (47 minus 2 = 45) |
| ch1.found1 | text | 2 (2) | T2.C1 (C2) | none: teaching text (`ncert` of video 1) | | in (text) |
| ch1.hemant1 | exercise | 2 (2) | T2.C1 (C3, inside Tool 2) | T2.C2, Tool 2 | Story, Hemant's herd | in (stretch, CLASH 4: C3 has no concept of its own; the approved purpose of Tool 2 names it) |
| ch1.tnote1 | talk | 2 (2) | T2.C1 (C1, C2, C3) | none: teaching text (`ncert` of video 1) | | in (talk, CLASH 16) |
| ch1.letus1 | exercise | 3 (3) | T3.C1 How Long Is a Name? (C4) | T3.C2, Tool 3 Longest and Shortest Name | Let us Do, Q1 | in ("animals and birds" not repeated, CLASH 29) |
| ch1.longer1 | prompt | 3 (3) | T3.C1 (C4) | T3.C2, Tool 3 | Let us Do, Q1 note | in (open: Sample answer, CLASH 30) |
| ch1.letus2 | exercise | 3 (3) | T3.C1 (C4) | T3.C2, Tool 3 | Let us Do, Q2 | in (6 letters each, CLASH 6) |
| ch1.letus3 | exercise | 4 (4) | T3.C1 (C4; analysis C5) | T3.C2, Tool 3 | Let us Do, Q3 | in (stretch, CLASH 5, 14: moved from C5 for the cap) |
| ch1.letus3a | exercise | 4 (4) | T3.C1 (C4; analysis C5 uses C4) | T3.C2, Tool 3 | Let us Do, Q3(a) | in (stretch, CLASH 5) |
| ch1.letus3b | exercise | 4 (4) | T4.C1 Name Tags in a Row (C5) | T4.C2, Tool 4 Starting and Ending Letters | Let us Do, Q3(b) | in (own name = Mala, CLASH 14) |
| ch1.letus3c | exercise | 4 (4) | T4.C1 (C5) | T4.C2, Tool 4 | Let us Do, Q3(c) | in |
| ch1.letus3d | exercise | 4 (4) | T4.C1 (C5) | T4.C2, Tool 4 | Let us Do, Q3(d) | in (D and M tie, CLASH 14) |
| ch1.letus3e | exercise | 4 (4) | T4.C1 (C5) | T4.C2, Tool 4 | Let us Do, Q3(e) | in (same ending letter as your own, CLASH 11 c) |
| ch1.letus3f | exercise | 4 (4) | T4.C1 (C5) | T4.C2, Tool 4 | Let us Do, Q3(f) | in (20 letters) |
| ch1.tnote2 | talk | 4 (4) | T4.C1 (C5) | none: teaching text (`ncert` of the image) | | in (talk, CLASH 16) |
| ch1.cards1 | text | 5 (5) | T5.C1 Number Names (C6) | none: teaching text (`ncert` of video 3) | | in (text) |
| ch1.example1 | example | 5 (5) | T5.C1 (C6) | T5.C2, Tool 5 Build a Number Name | Let us Do, Q4, Teji's number | in |
| ch1.fill3 | prompt | 5 (5) | T5.C1 (C6) | T5.C2, Tool 5 | Let us Do, Q4, Jojo's number | in (9 letters) |
| ch1.letus4a | exercise | 5 (5) | T5.C1 (C6) | T5.C2, Tool 5 | Let us Do, Q4(a) | in ("end of the book" not repeated, CLASH 11 d, 29; roll number 29, CLASH 14) |
| ch1.letus4b | exercise | 5 (5) | T5.C1 (C6) | T5.C2, Tool 5 | Let us Do, Q4(b) | in |
| ch1.example2 | example | 5 (5) | T6.C1 Same Letters, Different Numbers (C7) | T6.C2, Tool 6 Number Name Puzzles | Let us Think, 56 | in (stretch, CLASH 24: its cards also show C6's building; the book prints it with ch1.think1 in one box) |
| ch1.think1 | exercise | 5 (5) | T6.C1 (C7) | T6.C2, Tool 6 | Let us Think | in (13 numbers of 8 letters, CLASH 9 d) |
| ch1.tnote3 | talk | 5 (5) | T6.C1 (C7) | none: teaching text (`ncert` of video 4) | | in (talk, CLASH 16) |
| ch1.letus5 | exercise | 6 (6) | T6.C1 (C8, inside Tool 6) | T6.C2, Tool 6 | Let us Do, Q1 | in (73, 77, 78) |
| ch1.letus6a | exercise | 6 (6) | T6.C1 (C8) | T6.C2, Tool 6 | Let us Do, Q2, first Find out | in (stem not repeated, CLASH 9 a, 29; 93, 97 and 98 fit, CLASH 9 b) |
| ch1.letus6b | exercise | 6 (6) | T6.C1 (C8) | T6.C2, Tool 6 | Let us Do, Q2, second Find out | in ("smallest" = fewest letters, 70, CLASH 9 c) |
| ch1.letus7 | exercise | 6 (6) | T6.C1 (C8) | T6.C2, Tool 6 | Let us Do, Q3 | in (stretch, CLASH 8, 14: a notebook task for classmates, on screen "make a clue and test it") |
| ch1.place1 | text | 6 (6) | T6.C3 Longest and Shortest Place Names (C9) | none: teaching text (`ncert` of the image) | | in (text; the book asks nothing here, CLASH 12) |
| ch1.place2 | text | 6 (6) | T6.C3 (C9) | none: teaching text (`ncert` of the image) | | in (text) |
| ch1.group1 | text | 6, 7 (6, 7) | T7.C1 Group Things by a Rule (C10) | none: teaching text (`ncert` of video 5) | | in (text) |
| ch1.jojo1 | prompt | 7 (7) | T7.C1 (C11) | T7.C2, Tool 7 Group the Cards Two Ways | Story, Jojo's groups | in ("each groups" not repeated, CLASH 10, 29) |
| ch1.letus8 | exercise | 7 (7) | T7.C1 (C10) | T7.C2, Tool 7 | Let us Do, Q4 | in (four and four; lamp and clock read as electric, CLASH 10) |
| ch1.letus9 | exercise | 8 (8) | T7.C1 (C11) | T7.C2, Tool 7 | Let us Do, group differently | in ("the given objects" = the eight household objects, CLASH 10, 29) |
| ch1.tnote4 | talk | 8 (8) | T7.C1 (C10, C11) | none: teaching text (`ncert` of video 5) | | in (talk, CLASH 16) |
| ch1.letus10 | exercise | 8 (8) | T7.C3 Hair Styles (C12) | none: the question sits on the image concept T7.C3 (no tool follows it) | Let us Do, Hair Styles | in (stretch, CLASH 13: the one question on an image; answer has no counts yet, CLASH 31) |

## Per tool

| Tool | tool concept | book questions on the tool, in order | count | against the cap of 6 |
|---|---|---|---|---|
| 1 Marks at the Gate | T1.C2 (explore) | story2 (plus the tool's 3 notice prompts, which are the plan's own, not book questions) | 1 | ok |
| 2 Marks for a Big Herd | T2.C2 | fill1, story4, fill2, hemant1 | 4 | ok |
| 3 Longest and Shortest Name | T3.C2 | letus1, longer1, letus2, letus3, letus3a | 5 | ok |
| 4 Starting and Ending Letters | T4.C2 | letus3b, letus3c, letus3d, letus3e, letus3f | 5 | ok |
| 5 Build a Number Name | T5.C2 | example1, fill3, letus4a, letus4b | 4 | ok |
| 6 Number Name Puzzles | T6.C2 | example2, think1, letus5, letus6a, letus6b, letus7 | 6 | at the cap (CLASH 8) |
| 7 Group the Cards Two Ways | T7.C2 | jojo1, letus8, letus9 | 3 | ok |
| (no tool) image Hair Styles | T7.C3 | letus10 | 1 | not a tool (CLASH 13) |

29 questions = 1 + 4 + 5 + 5 + 4 + 6 + 3 + 1. The hook (T1.C1), the other image concepts (T4.C1 name tags, T6.C3 place signboards)
and the review (T8.C1, T8.C2) hold no book question.

By kind: 20 exercise (hemant1, letus1, letus2, letus3, letus3a to letus3f, letus4a, letus4b, think1, letus5, letus6a, letus6b,
letus7, letus8, letus9, letus10), 7 prompt (story2, fill1, story4, fill2, longer1, fill3, jojo1), 2 example (example1, example2).
The `FIO` kinds are the same as the kinds in `content.NCERT_ITEMS` (the structure stage checks this).

Stretches (homes that are judgement calls, none decided silently): story2 (CLASH 2), hemant1 (CLASH 4), letus3 and letus3a
(CLASH 5), example2 (CLASH 24), letus7 (CLASH 8, 14), letus10 Stretches (homes that are judgement calls, none decided silently): story2 (CLASH 2), hemant1 (CLASH 4), letus3 and letus3a
(CLASH 5), example2 (CLASH 24), letus7 (CLASH 8, 14), letus10 (CLASH 13). All seven are the proposal's own homes in
`tool_map.locked.md`, followed as recommended. Nothing was moved.

## ch1.letus10: the one question on an image

No tool follows the hair styles image (T7.C3), so the book question sits on the image concept itself. The flow gate allows this
(a question on a story or image concept is reported only when a tool follows it), and `build.py --structure` prints
`structure stage OK` with it there. If a tool is ever added after this image, the question moves to that tool. The picture
shows a practice class (CLASH 21), and its six counts are not written yet (CLASH 31).

## Teaching text (not questions)

14 items, in `ncert` of the teaching concept that carries them, never on a hook (except the hook's own story) and never on the
review: `opening`, `ch1.story1` on T1.C1 (hook); `ch1.rule1` on T1.C2 (the task text of Tool 1); `ch1.wall1`, `ch1.story3`,
`ch1.found1`, `ch1.tnote1` on T2.C1; `ch1.tnote2` on T4.C1 (image); `ch1.cards1` on T5.C1; `ch1.tnote3` on T6.C1; `ch1.place1`,
`ch1.place2` on T6.C3 (image); `ch1.group1`, `ch1.tnote4` on T7.C1. The four Teacher's Notes are talk items for the child, never
a task for a teacher (CLASH 16). CLASH 32 asks whether T2.C1's quoted lines may sit before Tool 2.

## Wording on screen that differs from the print (CLASH 29, SOLUTION_NOTES)

| question | printed | on screen | why |
|---|---|---|---|
| ch1.letus1 | "Some animals and birds got together" | "Some animals got together" | no bird is among the ten cards |
| ch1.jojo1 | "each groups" | "each group" | a grammar slip |
| ch1.letus9 | "Group the given objects differently" | "Group the eight household objects differently" | the book does not say which objects |
| ch1.letus4a | "Number cards are given at the end of the book" | "The number cards are on the screen." | the cards are not in this chapter; the screen has them |
| ch1.letus6a | stem of Q1 printed over the riddles | only the Find out box | the stem repeats Q1 and the riddles do not ask it |

All other questions use the book's words. Where the book's real-world task needs the child's own data (friends' names, own name,
roll number, notebook, class), the plan shows its own practice data and labels the answer (CLASH 14): the eight names of the
chapter, "Mala" as my name, roll number 29, a practice class.

## Excluded (outside this chapter, or extra and advanced)

None. All 43 items in `content.NCERT_ITEMS` are printed in this chapter's 8 pages (pdf 1 to 8; the next chapter starts on the
next printed page), and nothing else is on a tool. Looked at and not added, because the book does not set it here:
- the three notice prompts of Tool 1 in `tools_1.py`: they are the plan's own and not book questions; no book question was
  written for them;
- the thought bubble "1..2.. 3..." (pdf 6): it belongs to ch1.letus7, it is not a question;
- the pictures themselves (the stone slab, the ten animal cards, the 27 number cards, the signboards, the picture cards, the
  household cards, Mala's mother combing her hair): they are the data of questions already mapped;
- the cut-out number cards "at the end of the book": not in this chapter file (CLASH 11 d), nothing is mapped for them;
- the class tasks of the Teacher's Notes (children entering and leaving the classroom, boys and girls, "suggest more things"):
  not book questions, on no tool (CLASH 16);
- the QR code on the opener (0333CH01): not a question.
No "extra" or "advanced" question was added anywhere, and no question was written to fill a tool.

## Answers (CLASH 30)

The book prints no answer and no official key was found (searched `textbooks/class3/cemm1ps.pdf`, `docs/`, `upload/` and this
chapter's book folder). Every plan-made answer begins exactly "From the picture" (12) or "Sample answer" (17: 14 open tasks that
end "Your answer may differ" and 3 closed counts without it). None reads as an official book answer. Every number was checked by
program (letter counts of all 99 number names, the 13 numbers of 8 letters, 73, 77 and 78 with 12 letters, 43 with 10, 17 with 9,
70 with 7, the eight names, the 20 letters that start no name, the three riddle answers) and every sum in a step or answer is true
(34 equations checked by the gate, none false).

| id | answer the plan gives |
|---|---|
| ch1.story2 | From the picture: yes, all marks struck out, no cow missing |
| ch1.fill1 | From the picture: 47 (20 + 20 + 5 + 2) |
| ch1.story4 | From the picture: two marks were left, no cows outside, so two cows had not come back |
| ch1.fill2 | From the picture: 45 (47 minus 2) |
| ch1.hemant1 | Sample answer: 36 marks and 23 marks in two rows, 59 in all |
| ch1.letus1 | From the picture: elephant, 8 letters; ox, 2 letters |
| ch1.longer1 | Sample answer: crocodile, 9 letters (the book names no animal) |
| ch1.letus2 | From the picture: Mahesh 6, Kartik 6, the same, neither is longer |
| ch1.letus3 | Sample answer: Deba, Deep, Hemant, Mahesh, Kartik, Teji, Jojo, Mala |
| ch1.letus3a | Sample answer: tick Hemant, Mahesh, Kartik (6); cross Deba, Deep, Teji, Jojo, Mala (4) |
| ch1.letus3b | Sample answer: M (my name is Mala) |
| ch1.letus3c | Sample answer: 2 names, Mahesh and Mala |
| ch1.letus3d | Sample answer: D and M, 2 names each |
| ch1.letus3e | Sample answer: 2 names end with a, Deba and Mala |
| ch1.letus3f | Sample answer: the 20 letters A, B, C, E, F, G, I, L, N, O, P, Q, R, S, U, V, W, X, Y, Z |
| ch1.example1 | From the picture: Forty 5 + Three 5 = 10 letters |
| ch1.fill3 | From the picture: 9 letters (Seventeen) |
| ch1.letus4a | Sample answer: roll number 29, Twenty 6 + Nine 4 = 10 letters |
| ch1.letus4b | Sample answer: 12 twelve 6, 31 thirty-one 9, 90 ninety 6 |
| ch1.example2 | From the picture: Fifty 5 + Six 3 = 8 letters |
| ch1.think1 | Sample answer: five of the 13 (13, 14, 18, 19, 41, 42, 46, 51, 52, 56, 61, 62, 66) and what is common |
| ch1.letus5 | Sample answer: 73, 77, 78 (12 letters each) |
| ch1.letus6a | Sample answer: 93, 97 or 98 (each fits) |
| ch1.letus6b | Sample answer: 70, seventy, 7 letters (63 has 10) |
| ch1.letus7 | Sample answer: a puzzle of the plan's own, numbers 20 to 25, the longest name, answer 23 |
| ch1.jojo1 | From the picture: things that fly against things that do not fly |
| ch1.letus8 | From the picture: TV, Lamp, Clock, Fan against Chair, Bed, Pillow, Blanket |
| ch1.letus9 | Sample answer: sleeping (Bed, Pillow, Blanket) against the rest |
| ch1.letus10 | From the picture: how to read the six counts; no count yet (CLASH 31) |

## Printed-book errors that touch a question

All 17 entries are in `content.SOLUTION_NOTES`: the Q2 stem repeated from Q1; "very near to 100" (93, 97, 98); "the smallest"
(70 or 63); "animals and birds" with no bird; no animal named in the longer-name note; Mahesh and Kartik at 6 letters each; the 47
read from a picture; the friends' names and the ending-letter reading; the cards "at the end of the book"; the dash in a number
name; the notebook task for classmates; "each groups"; the battery clock and the oil lamp; "the given objects"; "your class"; the two
sets numbered 1 to 4; and the missing answer key. `content.ERRATA` stays empty: the book prints no false sum (analysis.md,
section 6b item 17).

## For the brief writer (not decided here)

- ch1.letus10: replace the answer with the six true counts once the class picture is fixed (CLASH 31).
- T2.C1 quotes two sentences that answer Tool 2's questions: CLASH 32 asks the user.
- Tool 7 holds jojo1, letus8, letus9 in the book's order; the play phase may use the two rounds of CLASH 10.
- Tool 1 shows the 3 notice prompts and then ch1.story2; the friend's rule (ch1.rule1) is the task line.
- Tool 6's first line is the solved 56 (ch1.example2): a recall of video 4's opener, not a second explanation (CLASH 24).

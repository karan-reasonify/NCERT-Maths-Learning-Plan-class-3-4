# -*- coding: utf-8 -*-
"""What's in a Name? (Class 3, chapter 1): the chapter's topic skeleton. STRUCTURE STAGE (c34-journey-designer, step 3),
rebuild from zero on the content team's note of 6 Nov 2026.

Keys are FINAL from here on: topic "T1", concept "T1.C1". THE NOTE FIXES THE SHAPE: four modules, eight topics, the 20
rows of tool_map.md in their order, the eight tools exactly as locked (tool_map.locked.md, `core/tool_map.py verify`
prints a match). Nothing is reordered, added, merged or dropped.

    module  topic  note rows        flow (concept keys)
    M1      T1     rows 1, 2        hook video T1.C1 -> Tool 1 T1.C2 (exploration)
    M1      T2     rows 3, 4, 5, 6  concept video T2.C1 -> Tool 2 T2.C2 -> Hemant bridge video T2.C3 -> Tool 3 T2.C4
    M2      T3     rows 7, 8        concept video T3.C1 -> Tool 4 T3.C2
    M2      T4     rows 9, 10       concept image T4.C1 (Name Tags in a Row) -> Tool 5 T4.C2
    M2      T5     rows 11, 12      concept video T5.C1 -> Tool 6 T5.C2
    M2      T6     rows 13, 14, 15  concept video T6.C1 -> Tool 7 T6.C2 -> concept image T6.C3 (Place Names)
    M3      T7     rows 16, 17, 18  story video T7.C1 -> Tool 8 T7.C2 -> concept image T7.C3 (Hair Styles)
    MLAST   T8     rows 19, 20      review concept T8.C1 (Marks and Names) + T8.C2 (Number Names and Groups)

Why this order: it is the note's order, and the note's order is the book's order (tool_map.locked.md, "Order check").
The tool order C1, C2, C3, C4, C5, C6, C7 with C8, C9 image, C10 with C11, C12 image has no place where the book and the
tool order disagree, so no tool is moved and no clash on order is needed.

Never two tools in a row: Tool 1 -> (topic 2 opens with a video); Tool 2 -> bridge video -> Tool 3; Tool 3 -> (topic 3
opens with a video); Tool 4 -> (topic 4 opens with the Name Tags image); Tool 5 -> (topic 5 opens with a video); Tool 6 ->
(topic 6 opens with a video); Tool 7 -> place names image -> (topic 7 opens with a video); Tool 8 -> Hair Styles image.

Videos: 7 (the hook, rows 3, 5, 7, 11, 13, 16). Each concept video has ONE new_idea. Target seconds are the middle of the
note's ranges (CLASH 26 option b): hook 50, row 3 40, bridge 25, row 7 40, row 11 45, row 13 40, row 16 45.

Images: 3 main concept images the note asks for (rows 9, 15, 18) and 2 pinned recap pictures on the two review concepts
(rows 19 and 20, PROVISIONAL, CLASH 25). Tools: 8 of 8.

STEP 4, THE MINIMUM MEDIA (c34-media-minimiser; the table is media_decisions.md, the open points are CLASH 29 to 38):
the content team's note fixes the media, so none is added and none is dropped. What this step decided is the DETAIL.
- The 8 tool concepts get no other medium: a tool's main scene is its visual (the note's rule).
- Each of the 7 videos keeps ONE new_idea and holds back what the tool after it asks (see each VID purpose).
- Every image is an ILLUSTRATION, not a photo: exact letters, dots and counts must be right, which a photo cannot promise.
- The 3 main images sit in the main flow (the gate wants an image-only concept's image there); the 2 review pictures are
  pinned recaps (CLASH 32 says what happens if the platform cannot pin).
- New VISUAL_KEY keys: wall_marks, tally_group, sheep, hemant, name_tag, place_signboard, class_children,
  number_name_row. number_card, household_card and picture_card already exist and are unchanged.

HOMES OF THE BOOK'S NON-QUESTION ITEMS (`ncert=`, 14 items, each once; the 29 book questions are the question mapper's,
step 5, as FIO on the tool of the concept):
  opening, story1 -> T1.C1 hook          rule1 -> T1.C2 Tool 1             wall1 -> T2.C1 video
  story3, found1 -> T2.C2 Tool 2         tnote1 -> T2.C4 Tool 3            tnote2 -> T4.C2 Tool 5
  cards1 -> T5.C2 Tool 6                 tnote3 -> T6.C2 Tool 7           place1, place2 -> T6.C3 image
  group1 -> T7.C1 video                  tnote4 -> T7.C2 Tool 8
The one place this differs from the "Teaching text" column of tool_map.locked.md: ch1.wall1 sits on the row 3 video
(T2.C1), not on Tool 2, because its first sentence opens that video's story and its second sentence is the stem of
ch1.fill1, which Tool 2 asks. The question mapper may move it.

STEP 5, HOMES OF THE 29 BOOK QUESTIONS (`items=[FIO(...)]`, each once; tool_map.locked.md's proposal kept as it was,
nothing moved; CLASH 39 is the one new judgement call):
  Tool 1 T1.C2  ch1.story2                                                       1
  Tool 2 T2.C2  ch1.fill1, ch1.story4, ch1.fill2                                 3
  Tool 3 T2.C4  ch1.hemant1                                                      1
  Tool 4 T3.C2  ch1.letus1, ch1.longer1, ch1.letus2, ch1.letus3, ch1.letus3a     5
  Tool 5 T4.C2  ch1.letus3b, ch1.letus3c, ch1.letus3d, ch1.letus3e, ch1.letus3f  5
  Tool 6 T5.C2  ch1.example1, ch1.fill3, ch1.letus4a, ch1.letus4b (notebook card) 4
  Tool 7 T6.C2  ch1.example2, ch1.think1, ch1.letus5, ch1.letus6a, ch1.letus6b,
                ch1.letus7 (notebook card)                                        6 (the cap)
  Tool 8 T7.C2  ch1.jojo1, ch1.letus8, ch1.letus9                                3
  image  T7.C3  ch1.letus10 (no tool follows it: the gate allows it, CLASH 24)   1
                                                                          total 29
The four Teacher's Notes are homed but NOT quoted in `textbook`: they give a teacher a role, which the user's rule does
not allow; their ideas are lines for the child, written at the briefs stage.

WHAT THE BRIEF WRITER MUST KEEP APART (hand-off, see also CLASH 28):
- hook and Tool 1 name no number and no idea; Tool 1 uses no number words and not the words "standing mark" or
  "struck-out mark" (the row 3 video gives them).
- video T2.C1 does not count the slab and does not say how many cows are out or home (Tool 2: ch1.fill1, ch1.story4,
  ch1.fill2); the bridge T2.C3 does not hand over the finished records of 36 and 23 and does not add them (Tool 3).
- video T3.C1 counts only animal names that are neither the longest nor the shortest, names no captain, and leaves
  Mahesh and Kartik to Tool 4 (ch1.letus1, ch1.letus2).
- the Name Tags image T4.C1 shows no pile, no count and no pair of names with the same starting or ending letter.
- video T5.C1 does not solve 43 or 17 (Tool 6: ch1.example1, ch1.fill3); video T6.C1 does not solve the eight-letter
  hunt (Tool 7); video T7.C1 does not say Jojo's rule (Tool 8: ch1.jojo1).
- nothing that is a child's answer is stated by a video or an image.

EVERY video, image and tool in this plan is a PLACEHOLDER: briefs come after the user approves the structure.
"""
from __future__ import annotations

from topics_common import A, DOER, FIO, IMG, TOPIC, VID, WE  # noqa: F401

TOPICS = []

# ---- T1: The Cows of Tarakeshwar (rows 1 and 2) ------------------------------------------------------------------
# The hook is a story only: Deba and Deep, the cows, the question. It teaches nothing, names no number and no idea, and
# ends on the problem (the book's own banner: "What could Deba and Deep do?"). Tool 1 follows at once: the child does
# the friend's idea (one mark for each cow that leaves, one struck out for each that returns) before any video names it.
# PROVISIONAL, CLASH 1 (a): the friend's rule is Tool 1's task; the last sentence of ch1.rule1 ("all the marks were
# struck out when they came back home") is NOT quoted, because it answers ch1.story2 ("Did all the cows come back
# home?") which the question mapper puts on Tool 1; the child finds the answer by marking a small herd of the plan's own.
TOPICS.append(TOPIC(
    "T1", "M1", "The Cows of Tarakeshwar", ["Opening story"], "Understand",
    "",   # the opening carries NO topic objective
    "Deba and Deep take their cows out each day. Then you make marks at the gate.",
    [A("T1.C1", "The Cows of Tarakeshwar", "Understand", "", role="hook",
       textbook=["A long long time ago, there was a cowherd family in Tarakeshwar.",
                 "Every day Deba and Deep took the cows out for grazing.",
                 "They used to return in the late evening together with all the cows.",
                 'One day, Deba asked, "How do we know that we have not lost any cows?"',
                 "They did not know how to count.",
                 "What could Deba and Deep do?"],
       ncert=["opening", "ch1.story1"], key_terms=[], minutes=4,
       teach=['Predict first: how can Deba and Deep tell that no cow is lost?'],
       video=VID("The Cows of Tarakeshwar",
                 "Deba and Deep take their cows out and home, but cannot count. The story ends on "
                 "one problem: how can they tell a cow is lost? It gives no answer, no number, no mark and "
                 "no idea.",
                 story={'characters': ['Deba', 'Deep', 'their friend'],
                        'setting': 'The village of Tarakeshwar, a long time ago: a low cow shed with a red-brown tiled roof, a '
                                   'rough wooden gate, green grazing fields and soft late evening light. The cowherds, their '
                                   'friend, the shed and the cows look as in the visual key (deba_and_deep, their_friend, '
                                   'cow_shed, cows).',
                        'situation': 'In the morning Deba and Deep walk their cows out through the gate to the fields, sticks in '
                                     'hand. In the late evening the cows come back together. They crowd through the gate, push, '
                                     "stop to drink and mix into one moving crowd. Deba watches the crowd and asks, 'How do we "
                                     "know that we have not lost any cows?' Deep looks at the crowd, then at the gate, and has no "
                                     'answer. Neither of them knows how to count. Their friend stands by the fence, listens and '
                                     'says nothing. The story shows no number, no mark on the wall, no idea and no answer. Nobody '
                                     'counts the cows, and nobody says that all of them are home.',
                        'open_question': 'How can Deba and Deep know that no cow is lost, when they do not know how to count?'},
                 seconds=50)),     # row 1: 45 to 55 s, the middle (CLASH 26)
       # STEP 4: the hook is the only video of this concept and Tool 1 is its only tool; no image (the wall and the cows are
       # Tool 1's own scene). The hook shows no mark on the wall and not the friend's idea (Tool 1's task); the friend may
       # stand at the gate and say nothing. It does not show the cows coming home as a count or as "all of them".
     DOER("T1.C2", "Marks at the Gate", "marks_gate", "Understand", "",
          applies_to="T1.C1", role="explore", minutes=6, misconceptions=["M_MARK_1"],
          recap=['Make one mark for each cow that goes out.',
                 'Strike out one mark for each cow that comes back.',
                 'A mark with no line is a cow that is not home yet.'],
          textbook=["Their friend gave them an idea.",
                    "When you go out, make a mark on the wall for each cow that leaves the gate.",
                    "Then when you come back, strike out one mark from the wall each time a cow re-enters the gate."],
          ncert=["ch1.rule1"],
          # STEP 5 (question mapper): the one book question of C1, on the exploration tool (the gate allows a book question
          # on role "explore"). The herd is the plan's own small herd (CLASH 1 a), so no number is written here and no
          # number word is used (M_MARK_1); the answer is what the child's own marks show, and the book says the same
          # ("all the marks were struck out when they came back home").
          items=[
              FIO("ch1.story2", "Story, cows back home",
                  "Did all the cows come back home?",
                  ["Make one mark for each cow that leaves the gate.",
                   "Strike out one mark for each cow that comes back.",
                   "Look at the wall. Does any mark have no line across it?"],
                  "From the picture: yes, all the cows came back home. Step 3: no mark was left without a line. "
                  "So no cow was missing.",
                  kind="prompt"),
          ])],
    topic_type="framing"))

# ---- T2: Marks Left on the Wall (rows 3, 4, 5, 6) ----------------------------------------------------------------
# Four concepts, two units: [concept video -> Tool 2] and [Hemant bridge video -> Tool 3]; the bridge is the "video between
# two tools" that the note asks for. PROVISIONAL, CLASH 2 (a): C1 has no concept video of its own; the row 3 video names
# the two kinds of mark (the child met them on Tool 1) and adds the groups of five, with ONE new_idea; it is the concept
# video that Tool 2 applies to. CLASH 28 (a): it uses a short row of marks of the plan's own, not the slab of 47.
# DECIDED BY THE USER (CLASH 4): the bridge is a short story VIDEO (20 to 30 s), the concept video of C3.
# CLASH 3 (a): Tool 2's 47 and its "still out (2)" are read from the picture (the question mapper labels the answers);
# CLASH 5 (a): Tool 3 has two fixed rows, real sheep and a quick way to make marks (the brief writer).
# ch1.story3 is quoted only as far as it gives no answer: "Two marks were still left on the wall but they didn't see any
# cows outside. They were worried." is the scene that ch1.story4 asks about, so the tool shows it and it is not quoted.
# ch1.found1 is homed on Tool 2 and shown after the child's answers (it says the two cows were found). ch1.tnote1 is
# homed on Tool 3 and not quoted (teacher role); its idea, other ways to count without numbers, is a line for the child.
# STEP 4 (media): two units, [video T2.C1 -> Tool 2] and [bridge T2.C3 -> Tool 3]; no image in this topic (the slab, the
# wall, the cows and the sheep are the tools' own scenes). CLASH 34: groups of five are drawn as the book's slab draws them
# (a gap, no slanting line), because a slanting line means "struck out" here. CLASH 33: the bridge says WHY there are two
# rows once; Tool 3 only checks that the child keeps them apart. Hemant and the sheep are new VISUAL_KEY keys.
TOPICS.append(TOPIC(
    "T2", "M1", "Marks Left on the Wall", ["Opening story", "Hemant"], "Apply",
    "Students read a long row of marks in groups of five, tell how many cows are still out and how many are home, "
    "and keep separate marks for cows and sheep.",
    "Marks stay on the wall and you read them. Then you make marks for cows and sheep.",
    [A("T2.C1", "Reading the Marks", "Understand",
       "Students say that a standing mark is a cow still out, a struck-out mark is a cow back, and groups of five "
       "make marks easy to read.",
       role="story",
       textbook=["After a few years, they had many more cows."],
       ncert=["ch1.wall1"],
       teach=['Predict first: a long row of marks is hard to read. What can help?',
              'Leave a small gap after every five marks. Read one group at a time.',
              'A standing mark is a cow still out. A struck-out mark is a cow that is back.',
              'Rule: read marks in groups of five. Standing means out. Struck out means back.'],
       key_terms=["standing mark", "struck-out mark", "groups of five"], misconceptions=["M_MARK_2"], minutes=5,
       video=VID("Marks on the Wall",
                 "Deba and Deep have many more cows now. The marks are hard to read. The story shows what a "
                 "standing mark and a struck-out mark mean. It shows why groups of five help, on a short row "
                 "of the plan's own. It counts no cows and gives no total.",
                 new_idea="reading marks: a standing mark is a cow still out, a struck-out mark is a cow back, and "
                          "groups of five make a long row of marks easy to read",
                 story={'characters': ['Deba', 'Deep', 'their friend'],
                        'setting': 'Tarakeshwar, a few years later: the shed gate at evening and the wall beside it, with rows of '
                                   'dark brown marks on it (wall_marks, tally_mark, struck_mark, tally_group, cow_shed, cows, '
                                   'deba_and_deep, their_friend). The herd is much bigger now. The stone slab is not shown.',
                        'situation': "It opens with one line from Deba: they still use their friend's marks, and now they have "
                                     'many more cows. The wall is full of marks. One evening the cows come in through the gate '
                                     'and Deep puts a thin line across one mark for each cow that comes in. The marks run in one '
                                     'long row and Deba loses his place. He cannot tell the marks that have a line from the marks '
                                     'that do not. Their friend shows them a way: leave a small gap after every five marks. They '
                                     'draw the marks again that way. Now the marks stand in groups of five, and no line slants across a group. Deba reads the wall '
                                     'one group at a time. A few cows are still on the path, and their marks have no line yet. '
                                     "Deba points at one: 'A standing mark is a cow still out.' Deep points at a mark with a line "
                                     "across it: 'A struck-out mark is a cow that is back.' The last cows walk in, and every mark "
                                     'gets its line. The story counts no cows, says no total of marks and shows no slab.',
                        'problem': 'The herd has grown, so the wall holds a long row of marks. Deba and Deep lose their place and '
                                   'cannot tell which cows are still out and which are back. How can they read a long row '
                                   'quickly?',
                        'thread': "Opens with one line that picks up the opening story and the child's try at the gate: Deba and "
                                  "Deep still use their friend's marks, now for many more cows. The marks idea is recalled, not "
                                  'taught again.',
                        'leads_to': 'Tool 2, Count the Big Herd: the child reads a big row of marks in groups of five and finds '
                                    'how many cows are still out and how many are home.'},
                 seconds=40)),     # row 3: 35 to 45 s, the middle
     DOER("T2.C2", "Count the Big Herd", "big_herd", "Apply",
          "Students count marks drawn in groups of five and tell how many cows are still out and how many came home.",
          applies_to="T2.C1", minutes=6, misconceptions=["M_MARK_2"], key_terms=["marks left", "still out"],
          recap=['Count marks in groups of five. It is quicker.',
                 'A standing mark is a cow still out.',
                 'Cows at home are all the cows minus the cows still out.'],
          textbook=["The next day, they returned with the cows.",
                    "They struck out one mark as each cow re-entered the gate."],
          ncert=["ch1.story3", "ch1.found1"],
          # STEP 5: the three book questions of C2 (CLASH 3 a: the 47, the groups of five and the 2 still out are read from
          # the picture and labelled "From the picture"). 47 = 9 groups of 5 and 2 extra marks (4 + 4 + 1 groups; the slab
          # has two full rows of 4 groups and a last row of one group of 5 and one group of 2), counted again on a zoomed
          # crop of the page. "Two cows still out" is a step of the plan, not a book question. ch1.wall1 stays on the
          # video T2.C1; its second sentence is the stem of ch1.fill1 and is copied into that question.
          items=[
              FIO("ch1.fill1", "Story, how many cows",
                  "One day, their wall had this many marks when they left home. So, they had ________ cows.",
                  ["One mark stands for one cow.",
                   "The marks are in groups of 5.",
                   "Count the groups: 4 + 4 + 1 = 9 groups.",
                   "9 groups of 5 is 9 × 5 = 45 marks.",
                   "There are 2 extra marks: 45 + 2 = 47."],
                  "From the picture: 47 cows. That is 9 groups of 5 and 2 extra marks.",
                  kind="prompt"),
              FIO("ch1.story4", "Story, why worried",
                  "Why were Deba and Deep worried?",
                  ["Strike out one mark for each cow that comes back.",
                   "Look at the wall. Some marks are still there.",
                   "Can they see any cows outside?"],
                  "From the picture: 2 marks were still left on the wall. So 2 cows were not home yet. "
                  "Deba and Deep saw no cows outside the gate. That is why they were worried.",
                  kind="prompt"),
              FIO("ch1.fill2", "Story, cows reached home",
                  "How many cows had reached home?",
                  ["The wall had 47 marks when the cows left.",
                   "2 marks were still left when the cows came back.",
                   "Cows home: 47 − 2 = 45."],
                  "From the picture: 45 cows had reached home.",
                  kind="prompt"),
          ]),
     A("T2.C3", "Hemant's Two Rows", "Understand",
       "Students say that cows and sheep go in two separate rows of marks, so each kind can be counted on its own.",
       role="story",
       key_terms=["two rows", "record"], misconceptions=["M_MARK_3"], minutes=4,
       teach=['Predict first: Hemant has cows and sheep. Should he use one row of marks or two?',
              "In one row, a cow's mark and a sheep's mark look the same.",
              'So Hemant keeps one row for the cows and one row for the sheep.',
              'Rule: one kind of animal, one row of marks.'],
       video=VID("Hemant's Two Rows",
                 "Their friend Hemant has cows and sheep. The story shows why he keeps two rows of marks, "
                 "one for each kind. It names no number of cows or sheep and shows no finished row.",
                 new_idea="cows and sheep go in two separate rows of marks",
                 story={'characters': ['Hemant', 'Deba', 'Deep'],
                        'setting': "Hemant's shed and yard beside the fields of Tarakeshwar, with his cows and real sheep (cows, "
                                   'sheep, hemant, wall_marks, tally_mark, deba_and_deep). Hemant wears his green shirt.',
                        'situation': 'It opens with one line: the cows that were missing are found and home, and Deba and Deep '
                                     'are happy. Then their friend Hemant comes by. Hemant has many cows and many sheep, and he '
                                     'wants to keep marks like Deba and Deep. He makes one row of marks for all his animals. In '
                                     'the evening one animal has not come back, and one mark in the row has no line. Hemant looks '
                                     "at the mark and asks, 'Is it a cow or a sheep?' A cow's mark and a sheep's mark look the "
                                     "same, so nobody can say. Deba says, 'Make one row for the cows and one row for the sheep.' "
                                     'Hemant draws a small cow at the head of one row and a small sheep at the head of the other. '
                                     'A mark left in the sheep row now says that a sheep is still out. The story says no number '
                                     "of Hemant's animals, shows no finished row and adds nothing together.",
                        'problem': 'In one mixed row, a mark that is left cannot say whether a cow or a sheep is still out.',
                        'thread': 'Opens with one line that picks up the story of the missing cows: Deba and Deep have found '
                                  'their cows. Their friend Hemant, named once in the book, is drawn here for the first time and '
                                  'visits them with his cows and sheep. The story does not say he is the friend of the first '
                                  'story.',
                        'leads_to': "Tool 3, Hemant's Cows and Sheep: the child makes Hemant's marks, one row for his cows and a "
                                    'separate row for his sheep.'},
                 seconds=25)),     # row 5: 20 to 30 s, the middle
     DOER("T2.C4", "Hemant's Cows and Sheep", "hemant_herd", "Apply",
          "Students make one row of marks for 36 cows and a separate row for 23 sheep, and keep the two rows apart.",
          applies_to="T2.C3", minutes=6, misconceptions=["M_MARK_3"], key_terms=["two rows", "record"],
          recap=['One kind of animal, one row of marks.',
                 'A group of five is a quick way to make marks.',
                 'Never mix the two rows.',
                 'Marks can also keep count of children who come in and go out.'],
          ncert=["ch1.tnote1"],
          # STEP 5: the one book question of C3. The answer is the child's own marks (open), so "Sample answer". The two
          # totals are NOT added: the note says do not combine them and CLASH 5 (a) says the tool never shows the sum.
          # Quick way, in the plan's own steps: 36 = 7 groups of 5 and 1 extra (35 + 1), 23 = 4 groups of 5 and 3 extra.
          items=[
              FIO("ch1.hemant1", "Story, Hemant's herd",
                  "Their friend Hemant had 36 cows and 23 sheep. Help Hemant keep track of his cows and sheep by "
                  "making marks like Deba and Deep.",
                  ["Make one mark for each cow: 36 marks.",
                   "Make one mark for each sheep: 23 marks.",
                   "Keep the cow marks and the sheep marks in two rows.",
                   "Groups of 5 are quick: 36 is 7 groups of 5 and 1 extra.",
                   "23 is 4 groups of 5 and 3 extra."],
                  "Sample answer: 36 marks in one row for the cows. 23 marks in another row for the sheep. "
                  "Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["standing mark", "struck-out mark", "groups of five", "two rows"]))

# ---- T3: How Long Is a Name? (rows 7 and 8) ----------------------------------------------------------------------
# PROVISIONAL, CLASH 9 (a): the video defines the length of a name with the book's animal names and shows "not how wide
# it looks" with an equal-count animal pair in the plan's own font (otherwise option c: width left out, and then the
# media stage tells the user, because the objective and the new_idea below name the width). Mahesh and Kartik stay for
# Tool 4's second stage. CLASH 28 (a): the video counts only two or three animal names that are neither the longest nor
# the shortest and names no captain. STEP 4, CLASH 35 answers the open point of CLASH 9 by measurement: at one letter size
# no pair of the book's animal names has FEWER letters but is wider (dog 3 against lion 4 is only 3 to 4 percent wider),
# so the video shows width the other way, by writing dog big and tiger small (dog takes more room, tiger has 5 letters
# against 3). That keeps Mahesh and Kartik (equal count, unequal width) a true discovery on Tool 4. The equal-count pairs
# snake and tiger (5 each) and dog and rat (3 each) are the fallback. No image in this topic: the animal cards and the
# names are Tool 4's own scene. CLASH 6 (a): Tool 4 will hold ch1.letus1, ch1.longer1, ch1.letus2, ch1.letus3 and
# ch1.letus3a (the question mapper); CLASH 10 (b) and (i): "Some animals" and a typed animal name; CLASH 8: the friends'
# names are typed. The two phrases quoted below are the book's own definition inside ch1.letus1 (the question stays on
# Tool 4).
TOPICS.append(TOPIC(
    "T3", "M2", "How Long Is a Name?", ["Let us Do 1 to 3"], "Apply",
    "Students count the letters in names to tell how long a name is, find the longest name and the shortest name, "
    "and see that two names can be equally long.",
    "You count the letters in names to find the longest and the shortest.",
    [A("T3.C1", "Counting the Letters", "Understand",
       "Students say that the length of a name is the number of its letters, not how wide the written name looks.",
       role="story",
       textbook=["The one with the longest name, i.e., the one with the most letters.",
                 "The one with the shortest name, i.e., the one with the fewest letters."],
       key_terms=["name length", "letter count"], misconceptions=["M_NAME_1"], minutes=5,
       teach=['Predict first: dog is written big and tiger is written small. Which name is longer?',
              'Example: count the letters. Dog has 3 letters. Tiger has 5 letters.',
              'Tiger is longer, even though dog looks bigger.',
              'Rule: the length of a name is its number of letters.'],
       video=VID("Counting the Letters",
                 "Names of animals have different numbers of letters. The story shows that name length "
                 "is the letter count. It is not how wide the name looks. It counts only dog and tiger and "
                 "names no captain. Dog is written big and takes more room, but tiger has more letters.",
                 new_idea="the length of a name is its number of letters, not how wide the name looks",
                 story={'characters': ['the children', 'Deba', 'Deep'],
                        'setting': 'The shady yard in front of the village school, a few days later: the children play a game '
                                   'with animal names, and Deba and Deep stand at the edge with their sticks. Names are written '
                                   'on the ground with a stick.',
                        'situation': 'It opens with one line: Deba tells the children how marks kept count of cows and sheep, and '
                                     'the children ask what else they can count. Then they start a game: the child with the '
                                     'longest animal name goes first. One child writes DOG in huge letters on the ground. Another '
                                     "child writes tiger in small letters next to it. 'Dog is longer! Look how much room it "
                                     "takes,' says the first child. A girl taps each letter of dog: d, o, g, three letters. Then "
                                     "she taps each letter of tiger: t, i, g, e, r, five letters. 'Tiger has more letters,' she "
                                     'says. The children look from the big word to the small word, and they see it. The girl says '
                                     'the length of a name is how many letters it has, not how wide it looks. The story counts no '
                                     'other name, names no team captain and never says that two names can be equally long.',
                        'problem': 'Two children disagree about whose animal name is longer: one name looks wider, the other has '
                                   'more letters. How can the children decide fairly which name is longer?',
                        'thread': 'Opens with one line that picks up the marks stories: Deba tells the children how marks kept '
                                  'count of cows and sheep, and the children ask what else they can count. The children are '
                                  'friends of Deba and Deep in the same village, now in the school yard.',
                        'leads_to': 'Tool 4, Longest and Shortest Names: the child counts letters in animal names, in the names '
                                    'of two boys and in the names of friends, to find the longest and the shortest.'},
                 seconds=40)),     # row 7: 35 to 45 s, the middle
     DOER("T3.C2", "Longest and Shortest Names", "longest_shortest", "Apply",
          "Students count the letters in names to find the longest name and the shortest name, and see when two "
          "names are equally long.",
          applies_to="T3.C1", minutes=7, misconceptions=["M_NAME_1", "M_NAME_2"],
          recap=['The length of a name is its number of letters.',
                 'The longest name has the most letters. The shortest has the fewest.',
                 'Two names can have the same number of letters.'],
          key_terms=["longest name", "shortest name"],
          # STEP 5: five book questions in the book's order, one per stage step: stage 1 the animal captains (ch1.letus1,
          # ch1.longer1), stage 2 Mahesh and Kartik (ch1.letus2), stage 3 the names the child enters (ch1.letus3 and
          # ch1.letus3a, moved here from C5 for the cap of 6: CLASH 6 a). CLASH 10 (b) and (i): the stem says "Some
          # animals" (the book's "animals and birds" has no bird card) and the child types an animal name for
          # ch1.longer1. CLASH 8: the friends' names are typed (the eight book names are quick-pick tiles); the answers to
          # ch1.longer1, ch1.letus3 and ch1.letus3a depend on what is typed, so they are "Sample answer ... Your answer may
          # differ". ch1.letus2 is a "Discuss" question: the plan's reading is 6 and 6, labelled "Sample answer" (CLASH 9).
          items=[
              FIO("ch1.letus1", "Let us Do, Q1",
                  "Some animals got together to play a game. They wanted to make 2 teams. They decided that the "
                  "captain of the first team will be the one with the longest name, i.e., the one with the most "
                  "letters. The captain of the second team will be the one with the shortest name, i.e., the one "
                  "with the fewest letters. Find out the captains of the 2 teams.",
                  ["Count the letters in each name.",
                   "tiger 5, dog 3, snake 5, goat 4, lion 4.",
                   "elephant 8, deer 4, ox 2, rat 3, monkey 6.",
                   "The most letters is 8, so the first team captain is elephant.",
                   "The fewest letters is 2, so the second team captain is ox."],
                  "From the picture: first team captain is elephant, letter count 8. "
                  "Second team captain is ox, letter count 2.",
                  kind="exercise"),
              FIO("ch1.longer1", "Let us Do, Q1 note",
                  "Do you know any animal having a longer name than the first team's captain?",
                  ["The first team's captain is elephant. It has 8 letters.",
                   "Type an animal whose name has more than 8 letters."],
                  "Sample answer: crocodile has 9 letters, and 9 is more than 8. Your answer may differ.",
                  kind="prompt"),
              FIO("ch1.letus2", "Let us Do, Q2",
                  "Who has a longer name? Discuss. The names are Mahesh and Kartik. The two boys say, "
                  "\"My name is longer.\"",
                  ["Mahesh: M, a, h, e, s, h. That is 6 letters.",
                   "Kartik: K, a, r, t, i, k. That is 6 letters.",
                   "6 and 6 are the same, so neither name is longer.",
                   "A name that looks wider is not a longer name."],
                  "Sample answer: Mahesh has 6 letters and Kartik has 6 letters. The names are the same "
                  "length, so neither is longer. Mahesh only takes more room.",
                  kind="exercise"),
              FIO("ch1.letus3", "Let us Do, Q3",
                  "Write down the names of some of your friends in the spaces given below and then, answer the "
                  "questions from a to f.",
                  ["Type the name of a friend on each line.",
                   "Or tap a name from your maths book.",
                   "You can write up to 8 names."],
                  "Sample answer: Deba, Deep, Hemant, Mahesh, Kartik, Teji, Jojo and Mala. These are names "
                  "from your maths book. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3a", "Let us Do, Q3(a)",
                  "Tick the longest name(s) and cross the shortest name(s).",
                  ["Count the letters in each name.",
                   "The most letters make the longest name.",
                   "The fewest letters make the shortest name.",
                   "Names can tie. Tick or cross every one that ties."],
                  "Sample answer: for the eight book names, tick Hemant, Mahesh and Kartik. They have 6 letters "
                  "each. Cross Deba, Deep, Teji, Jojo and Mala. They have 4 letters each. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["name length", "letter count", "longest name", "shortest name"]))

# ---- T4: Starting and Ending Letters (rows 9 and 10) -------------------------------------------------------------
# PROVISIONAL, CLASH 12 (a): Tool 5 follows an IMAGE concept, not a concept video; the note asks for it and the flow gate
# accepts it. PROVISIONAL, CLASH 11 (a): the Name Tags image and the orange (first letter) and blue (last letter) are the
# note's; the image sits on a concept that Tool 5 applies to, so the flow gate needs new_context True (the new real-life
# context is the name tag itself, which the book does not have). Style is an illustration because the two colours are the
# plan's own convention. The names on the tags must not give away Tool 5's counts. CLASH 7 (decided): Tool 5 sorts the
# book's eight names; CLASH 6 (a): Tool 5 will hold ch1.letus3b to ch1.letus3f; CLASH 8 (decided): the child types their
# own name. ch1.tnote2 is homed on Tool 5 and not quoted (teacher role).
TOPICS.append(TOPIC(
    "T4", "M2", "Starting and Ending Letters", ["Let us Do 3"], "Analyze",
    "Students name the starting letter and the ending letter of a name, count the names that share a letter, "
    "and find the most used starting letter.",
    "You look at the first and the last letter of names. Then you sort names by them.",
    [A("T4.C1", "Name Tags in a Row", "Understand",
       "Students point to the starting letter and the ending letter of a name.",
       role="image", key_terms=["starting letter", "ending letter"], minutes=4,
       teach=['Predict first: which letter of Teji is orange? Which letter is blue?',
              'The first letter is orange. It is the starting letter.',
              'The last letter is blue. It is the ending letter.',
              'Rule: every name has a starting letter and an ending letter.'],
       # STEP 4 (CLASH 29): three tags only, the names Teji, Hemant and Jojo (book names that Tool 5's counts do not turn
       # on); no two tags share a starting or an ending letter; no pile, no count, no sorting, no label words on the
       # picture (the caption says which colour is which). Illustration: the two colours are the plan's own convention.
       image=IMG("Name Tags in a Row",
                 "A real-life row of name tags, one above each school bag hook. The first letter of each name "
                 "is orange and the last is blue. It gives the words starting letter and ending letter before "
                 "the sorting. The book has no name tags. It shows three tags only, with no pile, no count "
                 "and no pair of names that share a letter. Tool 5 does the sorting.",
                 placement="main", new_context=True, style="illustration",
                 real_life="a row of school bag hooks on a classroom wall, with a plain white name tag hanging above "
                           "each hook",
                 shows="three name tags in a row, one above each bag hook: Teji, Hemant and Jojo, written in a thin "
                       "handwriting font with every letter the same size. In each name the first letter is orange and "
                       "the last letter is blue; all the other letters are dark grey. No two tags share a first letter "
                       "or a last letter (T, H, J and i, t, o). No pile of tags, no count, no other name, no ring, no "
                       "label words and no green. If the picture maker cannot spell the three names exactly, the names "
                       "are typeset on blank tags afterwards",
                 caption="Orange is the starting letter. Blue is the ending letter.",
                 visuals=["name_tag", "first_last_letter_colours"])),
     DOER("T4.C2", "Starting and Ending Letters", "start_end_letters", "Analyze",
          "Students sort names by their starting letter and by their ending letter, count each group, and find the "
          "most used starting letter.",
          applies_to="T4.C1", minutes=6, misconceptions=["M_NAME_3"],
          recap=['The starting letter is the first letter of a name.',
                 'The ending letter is the last letter of a name.',
                 'Many names can share a starting letter or an ending letter.',
                 'Two letters can tie for the most used.',
                 "Try it later with the boys' names and the girls' names in your class."],
          key_terms=["starting letter", "ending letter", "most used letter"],
          ncert=["ch1.tnote2"],
          # STEP 5: five book questions (ch1.letus3b to ch1.letus3f). CLASH 7 (decided): the practice set is the book's
          # eight names Deba, Deep, Hemant, Mahesh, Kartik, Teji, Jojo, Mala. Starting letters D 2, H 1, J 1, K 1, M 2,
          # T 1 (8 names); ending letters a 2, then h, i, k, o, p, t 1 each (8 names); the 6 starting letters leave
          # 26 - 6 = 20 letters unused. CLASH 8 (decided): the child types an own name, so 3b, 3c and 3e depend on it:
          # "Sample answer" with Mala as the example (Mala is in the set; a typed name outside the set gives 0 matches).
          # 3d and 3f are fixed by the eight names: "From the picture" (CLASH 7). CLASH 6: (e) is read as the same ending
          # letter as the child's own name, like (c); the other reading (the biggest group with one ending letter) gives
          # the same 2 names here (Deba and Mala).
          items=[
              FIO("ch1.letus3b", "Let us Do, Q3(b)",
                  "Write the starting letter of your name.",
                  ["Type your name.",
                   "Look at the first letter of your name."],
                  "Sample answer: if my name is Mala, the starting letter is M. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3c", "Let us Do, Q3(c)",
                  "Count all the name(s) that have the same starting letter as yours.",
                  ["Say your name is Mala. Its starting letter is M.",
                   "Find every name that starts with M. Count Mala too.",
                   "Mahesh and Mala start with M.",
                   "If no name starts with your letter, the count is 0."],
                  "Sample answer: 2 names start with M, Mahesh and Mala. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3d", "Let us Do, Q3(d)",
                  "Which starting letter is the most used? Count the names that begin with it.",
                  ["Sort the names by their starting letter.",
                   "Count each group.",
                   "D 2, H 1, J 1, K 1, M 2, T 1.",
                   "The most is 2, for D and for M. They tie."],
                  "From the picture: D and M are used the most, and they tie. D starts 2 names, Deba and "
                  "Deep. M starts 2 names, Mahesh and Mala.",
                  kind="exercise"),
              FIO("ch1.letus3e", "Let us Do, Q3(e)",
                  "Count the names with the same ending letter.",
                  ["Sort the eight names by their ending letter.",
                   "Count each group.",
                   "a 2, h 1, i 1, k 1, o 1, p 1, t 1.",
                   "Use the ending letter of your name, like in part (c).",
                   "Mala ends with a. Deba and Mala end with a."],
                  "Sample answer: 2 names end with a, Deba and Mala. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3f", "Let us Do, Q3(f)",
                  "Write the letters that are not the starting letter of any name.",
                  ["The starting letters are D, H, J, K, M and T.",
                   "That is 6 of the 26 letters of the alphabet.",
                   "26 − 6 = 20 letters are left."],
                  "From the picture: 20 letters are not a starting letter. "
                  "They are A, B, C, E, F, G, I, L, N, O, P, Q, R, S, U, V, W, X, Y and Z.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["starting letter", "ending letter", "most used letter"]))

# ---- T5: Number Names (rows 11 and 12) ---------------------------------------------------------------------------
# PROVISIONAL, CLASH 13 (a): "tens card", "ones card" and "a hyphen is not a letter" are the note's words, said by the
# plan as its own; the cards on screen carry no hyphen. The video holds ONE new_idea (how a number name is built from
# cards and counted) and must not solve 43 or 17: Tool 6 holds ch1.example1, ch1.fill3, ch1.letus4a and ch1.letus4b (the
# notebook card), CLASH 14 (a): roll numbers 1 to 99 only, CLASH 8: typed on a number pad. ch1.cards1 is homed on Tool 6
# (its scene shows the 27 cards). STEP 4, CLASH 36: the video builds 15 (Fifteen, one card, 7 letters) and 86 (Eighty then
# Six, 9 letters, the hyphen not counted); both are outside every Tool 6 and Tool 7 answer set and avoid the cards Twenty,
# Thirty, Forty, Fifty and Seventy (the next video, Tool 6 and Tool 7 need those fresh). No image: the cards are the
# video's and Tool 6's own scene (new VISUAL_KEY number_name_row).
TOPICS.append(TOPIC(
    "T5", "M2", "Number Names", ["Let us Do 4"], "Apply",
    "Students make number names from number cards, tens card first, and count the letters in each number name.",
    "You make number names with number cards. Then you count their letters.",
    [A("T5.C1", "Making Number Names", "Understand",
       "Students say that a number name uses the tens card first, then the ones card, and that a hyphen is not a "
       "letter.",
       role="story",
       key_terms=["number name", "tens card", "ones card", "hyphen"],
       misconceptions=["M_NUM_2", "M_NUM_4", "M_NUM_5"], minutes=5,
       teach=['Predict first: which card goes first, the tens card or the ones card?',
              'Example: lay the tens card first, then the ones card. Eighty, then Six, makes 86.',
              'Count the letters: Eighty has 6 and Six has 3. 6 + 3 = 9 letters.',
              'Example: Fifteen is one card with 7 letters. Numbers from 1 to 19 use one card.',
              'A hyphen is not a letter. Do not count it.',
              'Rule: tens card first, then the ones card. Count only letters.'],
       video=VID("Teji and Jojo Make Numbers",
                 "Teji and Jojo make number names with number cards. The story shows the tens card first, then "
                 "the ones card. It shows one card for 1 to 19. It says a hyphen is not a letter. It builds "
                 "15 and 86, never 43 or 17.",
                 new_idea="a number name is built from cards: the tens card first, then the ones card, one card for "
                          "1 to 19, and a hyphen is not a letter",
                 story={'characters': ['Teji', 'Jojo'],
                        'setting': 'A corner of the school classroom: a mat on the floor and a box of number cards spilled out, '
                                   'peach, light blue and light green (number_card, number_name_row, teji, jojo).',
                        'situation': 'It opens with one line: the children have counted the letters in names, and Teji asks if '
                                     'numbers have names with letters too. Jojo says yes and asks how many letters the name of 15 '
                                     'has. Teji lays one card, Fifteen: for the numbers 1 to 19 one card is enough. They tap its '
                                     'letters, f, i, f, t, e, e, n: seven letters. Next Teji lays 86. She puts the tens card '
                                     'first, Eighty, and the ones card after it, Six. Jojo copies her but lays Six first and '
                                     'Eighty after it. It reads wrong, and Teji slides the cards: the tens card goes first. They '
                                     'count the letters of each card: Eighty has six letters and Six has three, so nine letters '
                                     'in all. Then Jojo writes the name as eighty-six with a hyphen and counts the hyphen too. He '
                                     'gets ten. Teji shows him that a hyphen is not a letter, so it is not counted. Nine letters. '
                                     'The story builds only 15 and 86. It never builds 43 or 17 and does not use the cards '
                                     'Twenty, Thirty, Forty, Fifty or Seventy.',
                        'problem': 'Jojo wants to know how many letters a number name has, but the name is made of cards. He does '
                                   'not know which card goes first or what to count.',
                        'thread': 'Opens with one line that picks up the name stories: the children counted letters in names, and '
                                  'Teji asks whether numbers have names with letters too. Teji and Jojo are friends of Deba and '
                                  'Deep from the same village school.',
                        'leads_to': 'Tool 6, Build a Number Name: the child lays a tens card and a ones card and counts the '
                                    "letters, for Teji's number, Jojo's number and the child's own roll number."},
                 seconds=45)),     # row 11: 40 to 50 s, the middle
     DOER("T5.C2", "Build a Number Name", "number_name", "Apply",
          "Students make a number name from one or two number cards, tens card first, and count its letters.",
          applies_to="T5.C1", minutes=6, misconceptions=["M_NUM_2", "M_NUM_3", "M_NUM_4", "M_NUM_5"],
          recap=['Lay the tens card first, then the ones card.',
                 'A number from 1 to 19 is one card.',
                 'Count the letters on every card. A hyphen is not a letter.'],
          key_terms=["number name", "tens card", "ones card"],
          textbook=["Teji and Jojo are making numbers using these cards."],
          ncert=["ch1.cards1"],
          # STEP 5: four book questions (ch1.letus4b is the book's notebook task, shown as a short OPTIONAL instruction card
          # on the tool, as the note says). Letter counts checked by program: Forty 5 + Three 5 = 10 (printed in the
          # book), Seventeen 9, Ninety 6 + One 3 = 9, twelve 6, thirty 6 + one 3 = 9, ninety 6. CLASH 14 (a): the roll
          # number is 1 to 99, typed on the number pad (CLASH 8); the printed "at the end of the book" is not repeated, the
          # 27 cards are on the screen. The sample roll number 91 avoids the cards and numbers that rows 11 and 13 keep
          # for the videos and for Tool 7 (CLASH 36).
          items=[
              FIO("ch1.example1", "Let us Do, Q4, Teji's number",
                  "Teji makes her roll number 43 like this: Forty, Three. Its number name has 10 letters.",
                  ["Lay the tens card first: Forty.",
                   "Then lay the ones card: Three.",
                   "Forty has 5 letters. Three has 5 letters.",
                   "5 + 5 = 10 letters."],
                  "From the picture: 43 is Forty and Three. Its number name has 5 + 5 = 10 letters.",
                  kind="example"),
              FIO("ch1.fill3", "Let us Do, Q4, Jojo's number",
                  "Jojo makes his roll number 17 like this: Seventeen. Its number name has ________ letters.",
                  ["17 is one card, Seventeen. It is not two cards.",
                   "Count the letters: S, e, v, e, n, t, e, e, n.",
                   "That is 9 letters."],
                  "From the picture: 9 letters.",
                  kind="prompt"),
              FIO("ch1.letus4a", "Let us Do, Q4(a)",
                  "Write your roll number using number cards as shown above. The number cards are on the screen. "
                  "My roll number is ________. Its number name has ________ letters.",
                  ["Type your roll number, from 1 to 99.",
                   "Lay the tens card first, then the ones card.",
                   "Count the letters on the cards."],
                  "Sample answer: my roll number is 91. Its cards are Ninety and One. Its number name has "
                  "6 + 3 = 9 letters. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus4b", "Let us Do, Q4(b)",
                  "Write some numbers and their number names in your notebook. How many letters does each have?",
                  ["Pick a number and write its number name in your notebook.",
                   "Count the letters. A hyphen is not a letter."],
                  "Sample answer: 12 is twelve, 6 letters. 31 is thirty-one, 9 letters. 90 is ninety, "
                  "6 letters. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["number name", "tens card", "ones card", "hyphen"]))

# ---- T6: Number Puzzles and Place Names (rows 13, 14, 15) --------------------------------------------------------
# PROVISIONAL, CLASH 15 (a): Tool 7 serves C7 and C8 as one concept (finding numbers from the letter count of their
# names), at the cap of 6 questions: ch1.example2, ch1.think1, ch1.letus5, ch1.letus6a, ch1.letus6b, ch1.letus7 (the
# question mapper); CLASH 16 and 17 (a) are about its answers. The video holds ONE new_idea (different numbers can have
# the same letter count, Twenty and Thirty) and ends on the eight-letter puzzle without solving it. PROVISIONAL, CLASH 18
# (a): the place names image is an image-only concept (C9, no tool, no question) drawn with typeset boards, so style is
# illustration; it sits after Tool 7 as the note says, and no tool follows it. ch1.tnote3 is homed on Tool 7 and not
# quoted (teacher role). One topic holds both the puzzles and the place names because the note puts them in one topic;
# the topic objective names both. STEP 4, CLASH 36: the video poses the eight-letter question in general and gives no
# example: 56 is Tool 7's first item (ch1.example2) and every eight-letter number is Tool 7's answer. It names no
# longest name, no riddle and does not say what the eight-letter numbers have in common (ch1.tnote3 is Tool 7's).
TOPICS.append(TOPIC(
    "T6", "M2", "Number Puzzles and Place Names", ["Let us Think", "Let us Do", "Find out", "Place names"], "Analyze",
    "Students use the letter counts of number names to find numbers that fit a clue, and say which place names are "
    "the longest and the shortest.",
    "You solve number puzzles with letter counts. Then you meet the longest and the shortest place names.",
    [A("T6.C1", "Same Letters, Different Numbers", "Understand",
       "Students say that different numbers can have number names with the same number of letters, such as Twenty "
       "and Thirty.",
       role="story",
       key_terms=["letter count", "same letter count"], misconceptions=["M_NUM_6"], minutes=5,
       teach=['Predict first: can two different numbers have names with the same number of letters?',
              'Example: Twenty has 6 letters. Thirty has 6 letters. The numbers are different.',
              'Rule: different numbers can have names with the same number of letters.'],
       video=VID("Twenty and Thirty",
                 "Teji and Jojo see that Twenty and Thirty have the same number of letters. Jojo asks if other "
                 "numbers do too, and the eight-letter puzzle begins. It names no number with 8 letters and "
                 "solves nothing.",
                 new_idea="different numbers can have number names with the same number of letters",
                 story={'characters': ['Teji', 'Jojo'],
                        'setting': 'The same corner of the school classroom, a little later: the mat with the number cards and a '
                                   'speech bubble for each child (number_card, teji, jojo, speech_bubble).',
                        'situation': 'It opens with one line: Teji and Jojo can now count the letters of a number name, and Jojo '
                                     "wants a puzzle. Jojo says, 'Two different numbers must have different numbers of letters.' "
                                     'Teji lays the card Twenty and the card Thirty side by side on the mat. They tap the letters '
                                     "of Twenty: six. They tap the letters of Thirty: six. 'Two different numbers, the same "
                                     "number of letters,' says Teji. Jojo is surprised and grins. Then Jojo has an idea. He asks "
                                     'which numbers have names with eight letters. Teji grins, and the story ends on that '
                                     'question. It names no number with eight letters, no longest name and no riddle, and nobody '
                                     'says what such numbers have in common.',
                        'problem': 'Jojo thinks two different numbers must have names with different numbers of letters. Is he '
                                   'right?',
                        'thread': 'Opens with one line that picks up the video before it: Teji and Jojo, in the same classroom '
                                  'corner with the same cards, can now count the letters of a number name.',
                        'leads_to': 'Tool 7, Number Name Puzzles: the child hunts for numbers with eight letters, the longest '
                                    'number names and the two Find out boxes.'},
                 seconds=40)),     # row 13: 35 to 45 s, the middle
     DOER("T6.C2", "Number Name Puzzles", "number_puzzles", "Analyze",
          "Students use the letter counts of number names to find the numbers between 1 and 99 that fit a clue.",
          applies_to="T6.C1", minutes=7,
          recap=['Try a number and count the letters of its name.',
                 'Keep the numbers that fit the clue.',
                 'More than one number can fit one clue.',
                 'A bigger number does not mean a longer name.',
                 'Look at the numbers with the same letter count. What is common in them?'],
          misconceptions=["M_NUM_1", "M_NUM_6", "M_PUZ_1", "M_PUZ_2"],
          key_terms=["letter count", "number name"],
          ncert=["ch1.tnote3"],
          # STEP 5: exactly 6 book questions, the cap (CLASH 15): ch1.example2 and ch1.think1 (the eight-letter hunt),
          # ch1.letus5 (the longest names), ch1.letus6a and ch1.letus6b (the two Find out boxes) and ch1.letus7 (the
          # notebook task, shown as a short OPTIONAL instruction card for a similar puzzle). Every list below was computed
          # by program over 1 to 99, never typed from memory: 8 letters 13, 14, 18, 19, 41, 42, 46, 51, 52, 56, 61, 62, 66
          # (13 numbers); 12 letters 73, 77, 78; two words of 6 and 5 letters 23, 27, 28, 33, 37, 38, 83, 87, 88, 93, 97,
          # 98, of which 93, 97, 98 are near 100; 63 to 78 fewest letters is 70 (7 letters; 66 has 8). CLASH 16 (b): the
          # copied Q2 stem is not shown, only the two Find out boxes. CLASH 17 (a): "smallest" is read as fewest letters.
          # The closed answers are worked out, not read from a picture, so they are "Sample answer".
          items=[
              FIO("ch1.example2", "Let us Think, 56",
                  "Teji and Jojo made the number 56 (fifty-six). It has 8 letters.",
                  ["Lay the tens card first: Fifty.",
                   "Then lay the ones card: Six.",
                   "Fifty has 5 letters. Six has 3 letters.",
                   "5 + 3 = 8 letters."],
                  "From the picture: 56 is Fifty and Six. Its number name has 5 + 3 = 8 letters.",
                  kind="example"),
              FIO("ch1.think1", "Let us Think",
                  "Write other numbers between 1 and 99 that have 8 letters.",
                  ["Try a number. Say its name and count the letters.",
                   "Keep the numbers whose names have 8 letters.",
                   "Forty, fifty and sixty have 5 letters each.",
                   "One, two and six have 3 letters each: 5 + 3 = 8."],
                  "Sample answer: forty-two (42) has 8 letters. Every number with 8 letters fits. "
                  "They are 13, 14, 18, 19, 41, 42, 46, 51, 52, 56, 61, 62 and 66. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus5", "Let us Do, Q1",
                  "Write the number(s) between 1 and 99 that have the longest name.",
                  ["A number name is longest when both of its words are long.",
                   "Seventy has 7 letters, the longest tens word.",
                   "Three, seven and eight have 5 letters each, the longest ones words.",
                   "7 + 5 = 12 letters. Ninety-nine has only 6 + 4 = 10 letters."],
                  "Sample answer: 73, 77 and 78. Seventy-three, seventy-seven and seventy-eight have 12 letters "
                  "each.",
                  kind="exercise"),
              FIO("ch1.letus6a", "Let us Do, Q2, first Find out",
                  "Find out. My number name has two words. The first word has 6 letters. The second word has 5 "
                  "letters. I am very near to 100. Who am I?",
                  ["The first word has 6 letters: twenty, thirty, eighty or ninety.",
                   "The second word has 5 letters: three, seven or eight.",
                   "These 12 numbers fit the letters.",
                   "23, 27, 28, 33, 37, 38, 83, 87, 88, 93, 97, 98.",
                   "Very near to 100 means the nineties: 93, 97 and 98."],
                  "Sample answer: ninety-three (93), ninety-seven (97) or ninety-eight (98). Each one fits.",
                  kind="exercise"),
              FIO("ch1.letus6b", "Let us Do, Q2, second Find out",
                  "Find out. My friends and I are the numbers from 63 to 78. My number name is the smallest among "
                  "all my friends. Who am I?",
                  ["Count the letters in each name from 63 to 78.",
                   "Seventy has 7 letters. Every other name has 8 or more.",
                   "Here, smallest means the name with the fewest letters."],
                  "Sample answer: 70, seventy. It has 7 letters, the fewest from 63 to 78. Sixty-three, the "
                  "smallest number, has 10 letters.",
                  kind="exercise"),
              FIO("ch1.letus7", "Let us Do, Q3",
                  "Make similar puzzles of your own in your notebook and ask your classmates.",
                  ["Pick a few numbers and count the letters in their names.",
                   "Write a clue about the letters, like the Find out boxes.",
                   "Check that your number fits the clue."],
                  "Sample answer: My friends and I are the numbers from 20 to 25. My number name is the longest "
                  "among all my friends. Who am I? Answer: 23, twenty-three, with 11 letters. Your answer may "
                  "differ.",
                  kind="exercise"),
          ]),
     A("T6.C3", "Longest and Shortest Place Names", "Understand",
       "Students compare place names by letter count and say which place has the longest name and which places "
       "have the shortest names.",
       role="image",
       textbook=["Venkatanarasimharajuvaripeta is a place in India with the longest name.",
                 "It is located in Andhra Pradesh, close to the border of Tamil Nadu.",
                 "Ib in Odisha and Od in Gujarat are the places in India with the shortest names."],
       ncert=["ch1.place1", "ch1.place2"],
       key_terms=["place name", "longest name", "shortest name"], minutes=4,
       teach=['Predict first: which place has the longest name? Which places have the shortest names?',
              'The longest is Venkatanarasimharajuvaripeta. The shortest are Ib and Od.',
              'Rule: the longest name has the most letters. The shortest has the fewest.'],
       # STEP 4 (CLASH 30): the picture holds NO generated text. The three board texts VENKATANARASIMHARAJUVARIPETA, IB and
       # OD (28, 2 and 2 letters) are added afterwards as typeset capitals, spelled exactly, in one font at one letter
       # height, so the long board is as long as its name. No letter count, no other script, no person pointing.
       image=IMG("Longest and Shortest Place Names",
                 "A new real-life example of the longest and the shortest names, from places and not from "
                 "animals or friends: three yellow signboards, the first far longer than the other two. "
                 "The picture holds NO generated text: the three board texts are added afterwards as "
                 "typeset capitals and must be spelled exactly VENKATANARASIMHARAJUVARIPETA, IB and OD. "
                 "It shows no letter count and no other script.",
                 placement="main", new_context=False, style="illustration",
                 real_life="three yellow place name signboards on short posts by a quiet road in India: one very long "
                           "board and two very short boards",
                 shows="three BLANK yellow boards on short posts. The first board is far longer than the other two, "
                       "about fourteen times as long; the other two are small and about the same size. The picture "
                       "maker draws NO text at all: no letters, no digits and no other script, and every board face "
                       "stays plain yellow and empty. No letter count and no person pointing",
                 caption="Venkatanarasimharajuvaripeta is the longest place name. Ib and Od are the shortest.",
                 visuals=["place_signboard"]))],
    topic_type="instructional", key_terms=["letter count", "number name", "place name"]))

# ---- T7: Grouping Things (rows 16, 17, 18) -----------------------------------------------------------------------
# PROVISIONAL, CLASH 19 (a): Tool 8 serves C10 and C11 as one concept (group the same things by a rule, in more than
# one way); its questions are ch1.jojo1, ch1.letus8, ch1.letus9 (the question mapper). CLASH 20 (a), 21 (a), 22 (a) are
# about its stages and answers. The story video shows Teji's rule (the book prints it) and Jojo's different grouping of
# the same cards, and does NOT say Jojo's rule: the child finds it in Tool 8's first stage. One new_idea: things are
# grouped by a rule and the same things can be grouped another way. PROVISIONAL, CLASH 23 (decided by the user) and 24
# (a): Hair Styles in a Class is an image-only concept (C12) holding the book's one question ch1.letus10 (the question
# mapper puts it on this concept: no tool follows it, and the flow gate allows it); the picture is the plan's own
# practice class of exactly 12 children with the book's six hair styles, so style is illustration. ch1.tnote4 is homed
# on Tool 8 and not quoted (teacher role). ch1.group1 is quoted on the video up to Teji's rule; Jojo's rule is not
# printed in the book either. STEP 4, CLASH 37: the video shows Jojo's two groups of five with no label, no caption and no
# word that hints at the rule (no fly, air, wings, sky, move, up); Tool 8 stage 1 asks for the rule. The video does not
# use the eight household objects (Tool 8 stage 2) and not the hair styles (the image after Tool 8).
TOPICS.append(TOPIC(
    "T7", "M3", "Grouping Things", ["Grouping", "Let us Do", "Hair Styles"], "Apply",
    "Students group things by a rule, find the rule behind a grouping, regroup the same things another way, and "
    "count the children in each hair style group.",
    "You group things by a rule, then in another way. Then you group children by hair style.",
    [A("T7.C1", "Grouping by a Rule", "Understand",
       "Students say that a rule decides which group a thing goes in, and that the same things can be grouped by a "
       "different rule.",
       role="story",
       textbook=["Teji and Jojo have some picture cards.",
                 "She has grouped the cards into 'those that eat food' and 'those that don't eat food'.",
                 "Jojo has arranged the same cards differently."],
       ncert=["ch1.group1"],
       key_terms=["group", "rule"], misconceptions=["M_GRP_1"], minutes=5,
       teach=['Predict first: can the same cards be grouped in more than one way?',
              'Teji uses this rule: those that eat food, and those that do not.',
              'Jojo groups the same cards in a different way.',
              'Rule: a rule decides each group. The same things can be grouped another way.'],
       video=VID("Teji and Jojo Sort the Cards",
                 "Teji puts picture cards into two groups by a rule. Jojo puts the same cards into different "
                 "groups and does not say his rule. It gives no hint of his rule.",
                 new_idea="things are put into groups by a rule, and the same things can be grouped another way",
                 story={'characters': ['Teji', 'Jojo'],
                        'setting': 'The same corner of the school classroom: a table with ten picture cards and two dotted group '
                                   'boxes (picture_card, group_box, teji, jojo). The picture cards have no names written on them.',
                        'situation': 'It opens with one line: after the number puzzle, Jojo takes out a bag of ten picture cards. '
                                     'They show a yellow bird, a black insect, a brown rat, a striped fish, a blue drone, a white '
                                     'aeroplane, a blue mobile phone, a yellow light bulb, an orange book and a red and green '
                                     "kite. Teji puts the cards into two groups by a rule that she says in her own words: 'those "
                                     "that eat food' and 'those that don't eat food'. Four cards go in the first group and six in "
                                     'the second, as in the book: the bird, the insect, the rat and the fish; then the drone, the '
                                     'aeroplane, the phone, the bulb, the book and the kite. Jojo watches. Then he gathers the same ten cards and sets them out in two '
                                     'different groups, five cards in each, without a word, as in the book: the kite, the aeroplane, '
                                     'the bird, the insect and the drone in the first group; the fish, the light bulb, the phone, '
                                     'the book and the rat in the second. His cards lie still in two dotted '
                                     'boxes with no label and no caption. Teji checks that every card is in one group. She says, '
                                     "'Your groups are different from mine, and they work too.' Jojo smiles. The story ends "
                                     "there. Nobody says Jojo's rule. The voice never names Jojo's cards and uses no word that "
                                     'hints at his rule.',
                        'problem': "Jojo has grouped the same ten cards in a way that looks nothing like Teji's groups. Teji "
                                   'wonders if there is only one right way to group cards, or if both ways can be right.',
                        'thread': 'Opens with one line that picks up the number puzzle video: after the puzzle, Jojo takes out a '
                                  'bag of picture cards. The same two friends in the same classroom corner.',
                        'leads_to': "Tool 8, Group the Cards Two Ways: the child finds the rule behind Jojo's groups, groups "
                                    'eight household objects by electricity and then groups the same eight objects in another '
                                    'way.'},
                 seconds=45)),     # row 16: 40 to 50 s, the middle
     DOER("T7.C2", "Group the Cards Two Ways", "group_two_ways", "Apply",
          "Students group things by a rule, find the rule behind a grouping, and regroup the same things by another "
          "rule.",
          applies_to="T7.C1", minutes=7, misconceptions=["M_GRP_1", "M_GRP_2", "M_GRP_3"],
          recap=['A rule tells which things go in which group.',
                 'The same things can be grouped in more than one way.',
                 'Every thing goes in one group.',
                 'Can you add one more thing to each group?'],
          key_terms=["group", "rule"],
          ncert=["ch1.tnote4"],
          # STEP 5: three book questions, one per stage in the book's order (CLASH 19 a): ch1.jojo1 (stage 1, Jojo's
          # rule), ch1.letus8 (stage 2, the electricity split) and ch1.letus9 (stage 3, regroup). Printed slips not
          # repeated: "each groups" reads "each group" (CLASH 20 a); "the given objects" reads "these eight household
          # objects" (CLASH 22). The electricity split is fixed (CLASH 21 a); the final stage accepts any grouping that puts
          # every object in exactly one of two groups, both non-empty, that differs from the electricity split (CLASH 22 a).
          # The sample rule "give light or show pictures" (Lamp, TV) was chosen because every one of the eight objects has a
          # certain place under it; "things for sleeping" was left out because a fan is used when sleeping in many homes.
          items=[
              FIO("ch1.jojo1", "Story, Jojo's groups",
                  "What is common in each group Jojo has made?",
                  ["Look at the cards in the first group.",
                   "Ask: what can all of these do?",
                   "Now look at the second group. Can any of them do it?"],
                  "From the picture: the first group has things that fly. They are the kite, aeroplane, bird, "
                  "fly and drone. The second group has things that do not fly. They are the fish, light bulb, "
                  "mobile phone, book and rat.",
                  kind="prompt"),
              FIO("ch1.letus8", "Let us Do, Q4",
                  "Given below are pictures of some household objects: TV, Chair, Lamp, Bed, Clock, Fan, Pillow, "
                  "Blanket. Write the names of the above objects in the two groups given below: Things that need "
                  "electricity, Things that don't need electricity.",
                  ["Look at each object. Does it need electricity to work?",
                   "TV, Lamp, Clock and Fan do.",
                   "Chair, Bed, Pillow and Blanket do not.",
                   "Every object goes in one group."],
                  "From the picture: Things that need electricity: TV, Lamp, Clock, Fan. Things that don't need "
                  "electricity: Chair, Bed, Pillow, Blanket. The lamp has a pull cord, so it is an electric lamp. "
                  "A clock runs on electricity from a cell or from the plug.",
                  kind="exercise"),
              FIO("ch1.letus9", "Let us Do, group differently",
                  "Group these eight household objects differently. Write them down in the space below.",
                  ["Think of a new rule for the same eight objects.",
                   "Put every object in one of the two groups.",
                   "Pick a rule card to name your rule."],
                  "Sample answer: Things that give light or show pictures: Lamp, TV. Things that do not: Chair, "
                  "Bed, Clock, Fan, Pillow, Blanket. Your answer may differ.",
                  kind="exercise"),
          ]),
     A("T7.C3", "Hair Styles in a Class", "Apply",
       "Students sort the children of a class picture by hair style and count how many children are in each group.",
       role="image",
       key_terms=["hair style", "group"], minutes=5,
       teach=['Predict first: which hair style has the most children? Look before you count.',
              "Look at each child's hair. Find its style in the row.",
              'Count the children in each style group.',
              'Rule: group the children by hair style, then count each group.'],
       # STEP 5: the book's one question on this image concept (CLASH 24 a: no tool follows it, so the gate allows it
       # here; build.py shows it as an answer block, there is no input for the six counts). The six counts are the plan's
       # own practice class, in the order of the book's table (media_decisions.md): 3 + 2 + 2 + 1 + 3 + 1 = 12.
       items=[
           FIO("ch1.letus10", "Let us Do, Hair Styles",
               "Hair Styles. Mala is going to school. Her mother has combed her hair. Mala has two ponytails. Look at "
               "the children in your class. All children comb their hair in different ways. Look and write down.",
               ["The picture shows a practice class, not your own class.",
                "Look at the hair of each child.",
                "Find the hair style of the table that matches it.",
                "Count the children for each hair style and write the number."],
               "From the picture: 3 children have a high ponytail. 2 have two long plaits. 2 have short curly "
               "hair. 1 has wavy hair with a clip. 3 have short straight hair. 1 has two low ponytails. "
               "In all: 3 + 2 + 2 + 1 + 3 + 1 = 12 children. This is the practice class of this plan. "
               "Your own class may give other numbers.",
               kind="exercise"),
       ],
       # STEP 4 (CLASH 31): the 12 children, one by one, and the six TRUE counts are fixed in media_decisions.md (front row
       # left to right: high ponytail, short straight swept to one side, two plaits, short curly, two low ponytails, wavy with
       # clip; back row: short straight swept to one side, high ponytail, short curly, two plaits, high ponytail, short
       # straight swept to one side). In the table's order the
       # counts are 3, 2, 2, 1, 3, 1 and they add to 12. The picture shows no number, ring or tally; the answer block of
       # ch1.letus10 gives the counts, labelled "From the picture". This image asks only for counts of six styles, never a
       # new rule (that is Tool 8's final stage).
       image=IMG("Hair Styles in a Class",
                 "A plan-made practice class of exactly 12 unnamed children, in two rows of six, in the six "
                 "hair styles of the book's table, each style at least once. Each child is whole from the chest "
                 "up with the hair clear, so the child can group by looking and count each group. The six style "
                 "heads sit in a strip below, as the table row, with no numbers. The book has no such picture.",
                 placement="main", new_context=False, style="illustration",
                 real_life="a class of twelve children in school clothes, in two rows of six; the back row stands on a low "
                           "bench, so each back-row child shows from the chest up above the heads of the front row",
                 shows="twelve unnamed children of a practice class, in two rows of six, each whole from the chest up in "
                       "three-quarter view with the hair clear, one of six hair styles each. The back row stands on a low "
                       "bench, high enough that each back-row child shows from the chest up above the heads of the front "
                       "row, and no head or hair is hidden. Children of one style have identical hair. Front row, left to "
                       "right: 1 high ponytail; 2 short straight black hair swept to one side; 3 two long plaits with blue "
                       "ribbons; 4 short curly hair; 5 two low ponytails; 6 wavy hair with a blue hair clip. Back row, left "
                       "to right: 7 short straight black hair swept to one side; 8 high ponytail; 9 short curly hair; 10 "
                       "two long plaits with blue ribbons; 11 high ponytail; 12 short straight black hair swept to one "
                       "side. Boys and girls, shirt colours that do not follow the style, no child hidden, no Mala and no "
                       "mother. Below the class sits a strip of the six style heads of the table, in this order: high "
                       "ponytail, two long plaits, short curly, wavy with a clip, short straight black hair swept to one "
                       "side, two low ponytails, with no numbers. Draw no number, ring, tick or tally",
                 caption="A practice class. Match each child's hair to a style, then count.",
                 visuals=["class_children", "hair_style_pictures"]))],
    topic_type="instructional", key_terms=["group", "rule", "hair style"]))

# ---- T8: Chapter Review (rows 19 and 20) -------------------------------------------------------------------------
# Two review concepts, nothing new: no video, no tool, no book item, no key term that was not taught (every key term
# below is one of an earlier concept). PROVISIONAL, CLASH 25 (a): each review concept is ONE pinned recap picture
# assembled from the chapter's earlier tool scenes and images (a pinned image, kept beside what was already taught, as
# the flow rules say); the media minimiser confirms it. The recap uses "standing mark", "tens card" and "hyphen" only as
# the plan taught them (CLASH 13), and "hair style groups" means the plan-made practice class (CLASH 23). Together the
# two concepts revise every idea topic (T2 to T7): visual 1 revises T2, T3, T4 and T6 (the place names image); visual 2
# revises T5, T6 (the same letter count) and T7. Hemant's two rows (T2.C3) are not in the note's recap lines and are not
# revised here. STEP 4, CLASH 32: the two pictures are kept (the note asks for a visual per review concept), PINNED, and
# built only from pictures the chapter already has (the crop or the re-use of an earlier file, never a new scene). A recap
# shows IDEAS with the chapter's own examples, never the answer of a tool or image question: no 47, 45 or 2, no elephant
# or ox, no D and M tie, no 43 or 17, no puzzle answer, no hair-style counts, no Jojo rule. Pinned media are unverified
# on the platform: if it cannot show them, CLASH 32 gives the fallback.
TOPICS.append(TOPIC(
    "T8", "MLAST", "Chapter Review", ["Review"], "Understand", "",
    "A short look back at marks, names, number names and groups.",
    [A("T8.C1", "Marks and Names", "Understand",
       "Students recall what standing and struck-out marks mean, find the longest name and the shortest name, and "
       "name the starting letter and the ending letter of a name.",
       role="review",
       key_terms=["standing mark", "struck-out mark", "longest name", "shortest name", "starting letter",
                  "ending letter", "place name"],
       review_covers=["T2.C1", "T3.C1", "T4.C1", "T6.C3"], minutes=4,
       teach=['Look back at the marks. A standing mark is a cow still out.',
              'A struck-out mark is a cow that is back. Groups of five are easy to read.',
              'Look back at the name tags. The orange letter starts a name. The blue letter ends it.',
              'The longest name has the most letters. The shortest name has the fewest.',
              'Look back at the place boards. One name is very long. The other names are very short.'],
       image=IMG("Marks and Names: a look back",
                 "Recap only, one picture assembled from the chapter's own pictures: a short row of standing "
                 "and struck-out marks in groups of five, the three name tags, and the long and the short "
                 "place boards. No new example and no answer of a tool question.",
                 placement="pinned", style="illustration",
                 real_life="a classroom wall display that puts together pictures from this chapter",
                 shows="one recap picture that is a COMPOSITION of finished pictures the chapter already has, cut and set "
                       "together, nothing new drawn and no text generated: a short row of marks in groups of five with a "
                       "gap, some marks with a thin line across them and some standing, no slanting line across a group "
                       "(from the Marks at the Gate scene); the three name tags exactly as in the Name Tags picture; and "
                       "the long place board and one short place board exactly as in the Place Names picture. No "
                       "number, no count, no answer of any tool question and no new example",
                 caption="Look back at marks, name tags and place names.",
                 visuals=["tally_group", "struck_mark", "name_tag", "first_last_letter_colours",
                          "place_signboard"])),
     A("T8.C2", "Number Names and Groups", "Understand",
       "Students recall how a number name is made with cards, that different numbers can share a letter count, and "
       "how things are grouped by a rule.",
       role="review",
       key_terms=["number name", "tens card", "ones card", "same letter count", "group", "rule", "hair style"],
       review_covers=["T5.C1", "T6.C1", "T7.C1", "T7.C3"], minutes=4,
       teach=['Look back at the number cards. The tens card goes first, then the ones card.',
              'Twenty and Thirty have the same number of letters. Different numbers can match.',
              "Look back at Teji's groups. A rule says which things go together.",
              'The same things can be grouped another way.',
              'Look back at the class. Each child has one hair style. The children in a style group can be counted.'],
       image=IMG("Number Names and Groups: a look back",
                 "Recap only, one picture assembled from the chapter's own pictures: number cards laid tens "
                 "card first, Twenty and Thirty side by side, Teji's two groups of picture cards, and the "
                 "class sorted by hair style. No new example and no answer of a tool question.",
                 placement="pinned", style="illustration",
                 real_life="a classroom wall display that puts together pictures from this chapter",
                 shows="one recap picture that is a COMPOSITION of finished pictures the chapter already has, cut and set "
                       "together, nothing new drawn and no text generated: number cards laid tens card first, Eighty "
                       "then Six, with no hyphen (from the story of the cards); the cards Twenty and Thirty side by side; "
                       "Teji's two "
                       "groups of picture cards only, never Jojo's groups; and the practice class cut from the Hair "
                       "Styles picture, with its children set in small clusters by hair style. No number, ring or tally "
                       "on the class, no count, no puzzle answer, no rule of Jojo and no new example",
                 caption="Look back at number cards, groups and hair styles.",
                 visuals=["number_card", "number_name_row", "picture_card", "class_children",
                          "hair_style_pictures"]))],
    topic_type="summary"))

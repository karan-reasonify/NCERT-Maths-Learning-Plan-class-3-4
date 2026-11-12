# -*- coding: utf-8 -*-
"""What's in a Name? (Class 3, chapter 1): the chapter's topic skeleton. STRUCTURE STAGE (c34-journey-designer, step 3).

Keys are FINAL from here on: topic "T1", concept "T1.C1". The order follows tool_map.md row by row and the seven tools
exactly as locked (tool_map.locked.md); nothing is reordered, added or dropped. The tool table is the pipeline's PROPOSAL
(CLASH 1, PROVISIONAL): the user approves it only at the structure stop.

    module  topic  tool_map rows   flow
    M1      T1     rows 1, 2       hook video -> Tool 1 (exploration)
    M1      T2     rows 3, 4       concept video 1 -> Tool 2
    M2      T3     rows 5, 6       concept video 2 -> Tool 3
    M2      T4     rows 7, 8       image (name tags) -> Tool 4             (PROVISIONAL, CLASH 7)
    M2      T5     rows 9, 10      concept video 3 -> Tool 5
    M2      T6     rows 11, 12, 13 puzzle story video -> Tool 6 -> image (place names)   (PROVISIONAL, CLASH 12, 15, 17)
    M3      T7     rows 14, 15, 16 concept video 5 -> Tool 7 -> image (hair styles)       (PROVISIONAL, CLASH 13, 17)
    MLAST   T8     row 17          two look-back concepts, nothing new      (CLASH 15)

Why the topics are grouped like this (the gates accept it; CLASH 17 asks the user): one idea topic per unit (concept video
or image, then its tool), so a later change to one unit leaves the others alone. The two image-only concepts are NOT topics
of their own: C9 (place names) is the last concept of T6, straight after the number puzzles, as on the book's page, because
the longest and the shortest place names follow "the number with the longest name"; C12 (hair styles) is the last concept of
T7, because sorting children by hair style and counting each group is grouping again. Neither opens a topic about another
idea, neither needs a topic objective of its own, and no tool follows either (the gate lets an image concept sit anywhere
in an idea topic). Modules: M1 marks, M2 letters in names (animal, friend, number and place names), M3 groups, then MLAST.

KEYS OF THE SEVEN TOOLS (tools_1.py): marks_gate, marks_herd, longest_shortest, start_end_letters, build_number_name,
number_puzzles, group_two_ways.

QUESTIONS (step 5, c34-question-mapper): the book's 29 questions are homed here as FIO in `items`, each once: Tool 1 holds 1
(ch1.story2), Tool 2 holds 4, Tool 3 holds 5, Tool 4 holds 5, Tool 5 holds 4, Tool 6 holds 6 (the cap), Tool 7 holds 3, and
the hair styles IMAGE concept T7.C3 holds 1 (ch1.letus10: no tool follows that image, so the question sits on the image
itself, which the flow gate allows, CLASH 13). The 14 text and talk items are homed through `ncert=`. The full chain
question -> concept -> tool is in question_map.md. Items are in the book's order on each tool. Every answer is the plan's
own (the book prints none) and begins "From the picture" or "Sample answer" (CLASH 30). Five questions (ch1.letus1,
ch1.letus4a, ch1.letus6a, ch1.jojo1, ch1.letus9) do not repeat a printed error on screen (CLASH 29, SOLUTION_NOTES).

BRIEFS STAGE (step 6, c34-brief-writer, after the user approved the structure): the `teach` and `recap` lines, the story
briefs and `seconds` of the six videos, the real_life / shows / caption of the three images, the tool specs (tools_1.py)
and the answer of ch1.letus10 (the six true counts of the 12-child practice class, CLASH 31) are written. Nothing of the
structure changed. Every video, image and tool is still a PLACEHOLDER.

WHAT THE BRIEF WRITER MUST KEEP APART (hand-off notes, the book's questions sit on the tools):
- video 1 (T2.C1) must not state the count of marks, nor how many cows reached home: Tool 2 asks both (ch1.fill1, ch1.fill2).
- video 2 (T3.C1) poses the Mahesh and Kartik argument but leaves its answer to Tool 3 (ch1.letus2).
- video 3 (T5.C1) and Tool 5 share Teji's 43 and Jojo's 17 (ch1.example1, ch1.fill3): the video may use other numbers.
- video 4 (T6.C1) poses the puzzles and leaves every answer to Tool 6; video 5 (T7.C1) does not give away Jojo's rule
  (ch1.jojo1).
- the hook and Tool 1 name no number and no shape; Tool 1 needs no number names (M_MARK_1).

MEDIA DECISIONS (step 4, c34-media-minimiser; the full table and reasons are in media_decisions.md, the open points are
CLASH 19 to 28 in content.py). Every medium of the proposal is KEPT; no concept changed its role and no key moved:
  hook video 1; concept videos 5 (T2.C1, T3.C1, T5.C1, T6.C1, T7.C1); images 3, all main, none pinned (T4.C1 name tags,
  T6.C3 place signboards, T7.C3 hair styles); tools 7; the review holds no new medium. What changed is inside the media:
  - video 1 recalls the friend's idea in one line and says no count, so its title no longer names a number;
  - video 2 counts only a name that Tool 3 does not ask;
  - video 3 makes "numbers" with the cards (the book's own words), not Teji's and Jojo's roll numbers (43 and 17 are
    Tool 5's), and uses 15, 25 or 36;
  - video 4 holds ONE new_idea (the same letter count); the longest name is only a question it leaves to Tool 6;
  - video 5 shows no label for Jojo's groups;
  - each image says what it must not show (name tags: no piles and no counts; signboards: no letter count; hair
    styles: no number) and names its visuals.
"""
from __future__ import annotations

from topics_common import A, DOER, FIO, IMG, TOPIC, VID, WE  # noqa: F401

TOPICS = []

# ---- T1: the opening (rows 1 and 2) ---------------------------------------------------------------------------------
# The hook is a story only: Deba and Deep, the cows, the question. It teaches nothing and names no idea. Tool 1 follows at
# once: the child does the friend's idea (one mark for each cow that leaves, one struck out for each that returns) before
# any video names it. PROVISIONAL, CLASH 2: ch1.story2 sits on Tool 1 (its one book question) with the tool's three notice
# prompts, and the friend's rule (ch1.rule1) is the task instruction, so it is homed on Tool 1.
TOPICS.append(TOPIC(
    "T1", "M1", "The Cows of Tarakeshwar", ["Opening story"], "Understand",
    "",   # the opening carries NO topic objective
    "Deba and Deep take their cows out. Then you make marks at the gate.",
    [A("T1.C1", "The Cows of Tarakeshwar", "Understand", "", role="hook",
       textbook=["A long long time ago, there was a cowherd family in Tarakeshwar.",
                 "Every day Deba and Deep took the cows out for grazing.",
                 "They used to return in the late evening together with all the cows.",
                 'One day, Deba asked, "How do we know that we have not lost any cows?"',
                 "They did not know how to count.",
                 "What could Deba and Deep do?"],
       teach=["Predict first: how can Deba and Deep tell that no cow is lost?"],
       ncert=["opening", "ch1.story1"], key_terms=[], minutes=4,
       video=VID("The Cows of Tarakeshwar",
                 "Deba and Deep take the cows out every day and cannot count. How can they tell that no cow is "
                 "lost? The story ends on that question: no idea, no number and no mark on the wall yet.",
                 story={"characters": ["Deba", "Deep", "their friend"],
                        "setting": "Tarakeshwar, a long time ago: the cow shed with its tiled roof and rough wooden "
                                   "gate, the green grazing fields, late evening light. Look of the cowherds, the "
                                   "friend, the shed and the cows as in the visual key (deba_and_deep, their_friend, "
                                   "cow_shed, cows).",
                        "situation": "At sunset Deba and Deep bring the cows home. The cows crowd through the gate, "
                                     "push, stop to drink and mix together, so the herd looks like a moving crowd. "
                                     "Deba watches and cannot tell whether every cow has come home, and asks, 'How do "
                                     "we know that we have not lost any cows?' Deep looks at the crowd, then at the "
                                     "gate, and has no answer. Neither of them knows how to count. Their friend "
                                     "stands by the fence and listens, and says nothing yet. The story names no "
                                     "number and no solution, and no wall is shown.",
                        "open_question": "How can Deba and Deep tell that no cow is lost, when they do not know how "
                                         "to count?"},
                 seconds=75)),
     DOER("T1.C2", "Marks at the Gate", "marks_gate", "Understand", "",
          applies_to="T1.C1", role="explore", minutes=6, misconceptions=["M_MARK_1"],
          recap=["Make one mark for each cow that goes out.",
                 "Strike out one mark for each cow that comes back.",
                 "No mark left means no cow is missing."],
          textbook=["Their friend gave them an idea.",
                    "When you go out, make a mark on the wall for each cow that leaves the gate.",
                    "Then when you come back, strike out one mark from the wall each time a cow re-enters the gate.",
                    "The next day they followed their friend's idea, and all the marks were struck out when they came "
                    "back home."],
          ncert=["ch1.rule1"],
          items=[
              FIO("ch1.story2", "Story, cows back home",
                  "Did all the cows come back home?",
                  ["Strike out one mark for each cow that comes back.",
                   "Look at the wall. Is any mark left?"],
                  "From the picture: yes. All the marks were struck out, so no cow was missing.",
                  kind="prompt"),
          ])],
    topic_type="framing"))

# ---- T2: the marks left on the wall (rows 3 and 4) -> Tool 2 --------------------------------------------------------
# PROVISIONAL, CLASH 3: C1 has no concept video of its own. Video 1 names the friend's idea in its opening lines (the child
# did it on Tool 1) and carries ONE new idea, C2: the marks left are the cows still out. PROVISIONAL, CLASH 4: Tool 2 holds
# C2 (read the marks) and C3 (separate marks for cows and sheep, Hemant's task) as one unit. PROVISIONAL, CLASH 16: the idea
# of ch1.tnote1 (other ways to count large groups without numbers) is a closing LINE for the child, never a task for a teacher;
# it is homed here and not quoted. CLASH 11 (a): the 47 is read from the picture.
TOPICS.append(TOPIC(
    "T2", "M1", "Marks Left on the Wall", ["Opening story", "Teacher's Note"], "Understand",
    "Students read the marks left on a wall to tell how many cows are still out and how many came back, and keep "
    "separate marks for two kinds of animals.",
    "Marks stay on the wall. You find out which cows are still out.",
    [A("T2.C1", "The Marks Left on the Wall", "Understand",
       "Students say that each mark left on the wall is one cow still out and each struck out mark is one cow back.",
       role="story",
       # CLASH 32 (b), approved by the user 6 Nov 2026: the two book sentences that state the marks and the worry
       # ("this many marks", "Two marks were still left ... They were worried") are NOT quoted here: they are the
       # story that ch1.fill1, ch1.story4 and ch1.fill2 on Tool 2 ask about. ch1.wall1 and ch1.story3 stay homed
       # through ncert=.
       textbook=["After a few years, they had many more cows.",
                 "The next day, they returned with the cows. They struck out one mark as each cow re-entered the gate.",
                 "Deba and Deep quickly went to search for the missing cows and found them in a nearby field. They "
                 "all happily returned home together!"],
       ncert=["ch1.wall1", "ch1.story3", "ch1.found1", "ch1.tnote1"],
       teach=["Predict first: the cows are back, but a mark is not struck out. Is that cow home?",
              "No. A mark that is not struck out is a cow still out.",
              "A struck out mark is a cow that came back.",
              "Rule: marks left are cows still out. Struck out marks are cows home.",
              "Think: how else could you count many cows without numbers?"],
       key_terms=["mark", "strike out", "marks left"], misconceptions=["M_MARK_2"], minutes=5,
       video=VID("Marks Still on the Wall",
                 "Years later the herd is large. The friend's idea is only recalled in one line, as the child did it "
                 "on Tool 1. The cows come home, marks are still left, and the story shows that a mark left is a cow "
                 "still out. No count is said: the marks, the cows out and the cows back are for Tool 2.",
                 new_idea="the marks left on the wall are the cows still out, and the cows that came back are the "
                          "rest",
                 story={"characters": ["Deba", "Deep", "their friend"],
                        "setting": "Tarakeshwar, years later: the cow shed gate at evening and the big stone slab "
                                   "beside it, where the marks are kept in groups of five. The herd is much larger "
                                   "now (visual keys: stone_slab, tally_mark, struck_mark, cow_shed, cows, "
                                   "deba_and_deep).",
                        "situation": "Years later the herd has grown. In one line, Deba reminds Deep of their "
                                     "friend's idea: a mark for each cow that goes out, and one struck out for each "
                                     "cow that comes back (the friend shows only in this quick memory). That evening "
                                     "the cows file in through the gate and Deep strikes out a mark for each one. "
                                     "The last cow walks in and the shed is full and quiet. But some marks on the "
                                     "slab are still standing, not struck out. Deba and Deep look at the slab and "
                                     "do not count the marks. Deba says a mark still standing is a cow still out, "
                                     "and they hurry out together to look for the cows. They find the cows in a "
                                     "nearby field, and all walk home together. The last marks are struck out. Deba "
                                     "ends with a thought: marks are one way to count without numbers, so is there "
                                     "another way? The story never says how many marks stand or how many cows are "
                                     "out, and shows no numeral anywhere.",
                        "problem": "Every cow that came in has had its mark struck out, yet some marks are still "
                                   "standing. Deep thinks the marks left must be the cows that came home. Deba "
                                   "points at the gate: a cow that came home had its mark struck out. So what do the "
                                   "marks left stand for?",
                        "thread": "Continues the hook and the child's try at the gate on Tool 1: Deba and Deep still "
                                  "use their friend's idea. It is recalled in one line only and is not taught again.",
                        "leads_to": "Tool 2, Marks for a Big Herd: the child reads the marks on the slab, strikes "
                                    "them out and finds the cows still out and the cows home."},
                 seconds=115)),
     DOER("T2.C2", "Marks for a Big Herd", "marks_herd", "Apply",
          "Students find the cows still out and the cows back from the marks left, then make separate marks for cows "
          "and sheep.",
          applies_to="T2.C1", minutes=7, misconceptions=["M_MARK_2"], key_terms=["mark", "strike out", "marks left"],
          recap=["Count marks in groups of five. It is quicker.",
                 "Marks left are cows still out.",
                 "Cows home: all the marks, minus the marks left.",
                 "Keep cow marks and sheep marks in separate rows."],
          items=[
              # The 47 is read from the stone slab (CLASH 11 a): 4 groups of 5 in each of 2 full rows, then 5 and 2.
              FIO("ch1.fill1", "Story, how many cows",
                  "One day, their wall had this many marks when they left home. So, they had ________ cows.",
                  ["Count the marks in groups of 5.",
                   "A full row is 5 + 5 + 5 + 5 = 20.",
                   "Two full rows: 20 + 20 = 40.",
                   "The last row has a group of 5 and a group of 2.",
                   "5 + 2 = 7.",
                   "40 + 7 = 47."],
                  "From the picture: 47 cows. One mark stands for one cow.",
                  kind="prompt"),
              FIO("ch1.story4", "Story, why worried",
                  "Why were Deba and Deep worried?",
                  ["Strike out one mark for each cow that comes back.",
                   "Look at the wall. Some marks are still there.",
                   "Can they see any cows outside?"],
                  "From the picture: two marks were still left, but they saw no cows outside. So two cows had "
                  "not come back.",
                  kind="prompt"),
              FIO("ch1.fill2", "Story, cows reached home",
                  "How many cows had reached home?",
                  ["The wall had 47 marks when the cows left.",
                   "2 marks were still left when the cows came back.",
                   "47 − 2 = 45."],
                  "From the picture: 45 cows had reached home.",
                  kind="prompt"),
              # No sheep and no Hemant are drawn in the book (CLASH 4, 28): the answer is the plan's own, "Sample answer".
              FIO("ch1.hemant1", "Story, Hemant's herd",
                  "Their friend Hemant had 36 cows and 23 sheep. Help Hemant keep track of his cows and sheep by "
                  "making marks like Deba and Deep.",
                  ["Make one mark for each cow: 36 marks.",
                   "Make one mark for each sheep: 23 marks.",
                   "Keep the cow marks and the sheep marks apart."],
                  "Sample answer: 36 marks in one row for the cows. 23 marks in another row for the sheep. "
                  "That is 36 + 23 = 59 marks. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["mark", "strike out", "marks left"]))

# ---- T3: how long is a name? (rows 5 and 6) -> Tool 3 ---------------------------------------------------------------
# Video 2 poses the Mahesh and Kartik argument and the animal captains; Tool 3 settles both. PROVISIONAL, CLASH 6: on
# Tool 3 the two names are counted and the plan states that they have the same number of letters (6 and 6), labelled "From
# the picture". PROVISIONAL, CLASH 5: ch1.letus3 and ch1.letus3a are homed on Tool 3 (question mapper). CLASH 11 (b):
# "animals and birds" is kept as printed. CLASH 14: the friends' names are the book's eight names (sample data, labelled).
TOPICS.append(TOPIC(
    "T3", "M2", "How Long Is a Name?", ["Let us Do"], "Apply",
    "Students count the letters in a name and use the letter count to find the longest name and the shortest name.",
    "Names have letters. You count the letters to find the longest name and the shortest.",
    [A("T3.C1", "How Long Is a Name?", "Understand",
       "Students count the letters in a name and say that the longest name has the most letters.", role="story",
       textbook=["They decided that the captain of the first team will be the one with the longest name, i.e., the "
                 "one with the most letters.",
                 "The captain of the second team will be the one with the shortest name, i.e., the one with the fewest "
                 "letters."],
       teach=["Predict first: which name is longer, cow or sheep?",
              "Cow has 3 letters: c, o, w. Sheep has 5 letters: s, h, e, e, p.",
              "5 is more than 3, so sheep is the longer name.",
              "Rule: the longest name has the most letters. The shortest name has the fewest letters."],
       key_terms=["letter count", "longest name", "shortest name"], misconceptions=["M_NAME_1", "M_NAME_2"], minutes=5,
       video=VID("Whose Name Is Longer?",
                 "Mahesh and Kartik each say that their name is longer. Animals pick team captains by the letters in "
                 "their names. The story shows that the length of a name is its letter count. It counts only a name "
                 "that Tool 3 does not ask, and leaves both answers to the tool: the captains and the two boys.",
                 new_idea="the length of a name is its number of letters: the longest name has the most letters and "
                          "the shortest name the fewest",
                 story={"characters": ["Mahesh", "Kartik", "Deba", "Deep", "the children"],
                        "setting": "The shady yard in front of the village school, a few days after the cow story: "
                                   "children play, and Deba and Deep stand at the edge of the scene with their "
                                   "sticks. A cow and a sheep stand by the fence. They are just two animals the "
                                   "children point at and name: they belong to no one in the story, and neither is "
                                   "one of the ten animals of Tool 3 (visual keys: mahesh_kartik_boys, "
                                   "deba_and_deep, cows, sheep).",
                        "situation": "Deba tells the children in one line how marks helped them keep count of the "
                                     "cows, and the children wonder what else can be counted. Just then Mahesh and "
                                     "Kartik face each other, pointing at one speech bubble: 'My name is longer.' "
                                     "Both say it at once. Nearby, some animals are choosing captains for a game in "
                                     "the same way: the longest name for the first team and the shortest name for the "
                                     "second (told only in words, no animal name is shown or counted). Nobody can "
                                     "agree how to tell a long name from a short one. A child points at the cow by "
                                     "the fence, writes the word cow in the sand and taps each letter, and a small "
                                     "mark appears under it for each "
                                     "letter, like a mark on Deba and Deep's wall: c, o, w, three letters. Then the "
                                     "child points at the sheep and writes sheep: s, h, e, e, p, five letters. The "
                                     "marks under sheep make a longer "
                                     "row than the marks under cow. The children say: the longest name has the most "
                                     "letters and the shortest has the fewest. Mahesh and Kartik turn to their own "
                                     "names and start to count, and the story stops there. It never counts Mahesh or "
                                     "Kartik and never says whether the two names are equal.",
                        "problem": "Two friends each say 'My name is longer', and the game needs a captain with the "
                                   "longest name and a captain with the shortest. How can anyone decide whose name is "
                                   "longer?",
                        "thread": "Opens with one line that picks up the video before it: Deba tells how marks kept "
                                  "count of the cows, and the children ask what else can be counted. The children are "
                                  "friends of Deba and Deep in the same village, now at the school yard.",
                        "leads_to": "Tool 3, Longest and Shortest Name: the child counts the letters of the animal "
                                    "names, of Mahesh and Kartik, and of eight practice friends."},
                 seconds=115)),
     DOER("T3.C2", "Longest and Shortest Name", "longest_shortest", "Apply",
          "Students count the letters in each name and pick the name with the most letters and the name with the "
          "fewest.",
          applies_to="T3.C1", minutes=6, misconceptions=["M_NAME_1", "M_NAME_2"],
          key_terms=["letter count", "longest name", "shortest name"],
          recap=["Count the letters in a name. That is its length.",
                 "The most letters make the longest name.",
                 "The fewest letters make the shortest name.",
                 "A name that looks wider is not a longer name.",
                 "Two names can have the same number of letters."],
          items=[
              # CLASH 29: the book says "animals and birds" but no bird is among the ten cards; the screen says "animals".
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
                   "Think of an animal whose name has more than 8 letters."],
                  "Sample answer: crocodile has 9 letters, and 9 is more than 8. Your answer may differ.",
                  kind="prompt"),
              # CLASH 6: Mahesh and Kartik both have 6 letters; the plan states the tie, labelled "From the picture".
              FIO("ch1.letus2", "Let us Do, Q2",
                  "Who has a longer name? Discuss. The names are Mahesh and Kartik. The boys say, "
                  "\"My name is longer.\"",
                  ["Mahesh: M, a, h, e, s, h. That is 6 letters.",
                   "Kartik: K, a, r, t, i, k. That is 6 letters.",
                   "6 and 6 are the same, so neither name is longer.",
                   "A name that looks wider is not a longer name."],
                  "From the picture: Mahesh has 6 letters and Kartik has 6 letters. "
                  "The two names are the same length. Neither is longer.",
                  kind="exercise"),
              # CLASH 5 and 14: letus3 and letus3a sit here, not on Tool 4. The eight names of the book are the practice friends.
              FIO("ch1.letus3", "Let us Do, Q3",
                  "Write down the names of some of your friends in the spaces given below and then, answer the "
                  "questions from a to f.",
                  ["Use the eight names of this chapter as practice friends.",
                   "Write one name on each line."],
                  "Sample answer: Deba, Deep, Hemant, Mahesh, Kartik, Teji, Jojo and Mala. These are practice "
                  "names from this chapter. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3a", "Let us Do, Q3(a)",
                  "Tick the longest name(s) and cross the shortest name(s).",
                  ["Count the letters in each name.",
                   "Deba 4, Deep 4, Hemant 6, Mahesh 6.",
                   "Kartik 6, Teji 4, Jojo 4, Mala 4.",
                   "The most letters is 6. The fewest letters is 4."],
                  "Sample answer: tick Hemant, Mahesh and Kartik (6 letters each). Cross Deba, Deep, Teji, Jojo "
                  "and Mala (4 letters each). Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["letter count", "longest name", "shortest name"]))

# ---- T4: starting and ending letters (rows 7 and 8) -> Tool 4 -------------------------------------------------------
# PROVISIONAL, CLASH 7: Tool 4 follows an IMAGE concept (name tags in a row), not a video, as the table puts it. The image is
# the only teaching before the tool, so it cannot be pinned: new_context is True (the flow gate asks for it when a tool
# follows a main image), the new real-life context being the name tags. The book has no name tags and prints no teaching
# for this idea; the real_life / shows / caption of the image are for the brief writer. PROVISIONAL, CLASH 16: the idea of
# ch1.tnote2 (longest and shortest names in a group) is a line for the child, homed here, not a task for a teacher.
# CLASH 14: the names on the tags are the book's eight names (sample data).
TOPICS.append(TOPIC(
    "T4", "M2", "Starting and Ending Letters", ["Let us Do", "Teacher's Note"], "Apply",
    "Students find the starting letter and the ending letter of a name and sort names by them to find the letter "
    "used most.",
    "Every name starts and ends with a letter. You sort names by those letters.",
    [A("T4.C1", "Name Tags in a Row", "Understand",
       "Students point to the starting letter and the ending letter of a name.", role="image",
       teach=["Predict first: which letter comes first in Teji? Which comes last?",
              "The first letter is T. The last letter is i.",
              "Rule: the first letter is the starting letter. The last letter is the ending letter.",
              "Orange ring: starting letter. Blue ring: ending letter.",
              "Think: which of your friends has the longest name? Which has the shortest?"],
       ncert=["ch1.tnote2"], key_terms=["starting letter", "ending letter"], minutes=4,
       image=IMG("Name Tags in a Row",
                 "Real name tags in a row, for example on school bag hooks, with the starting letter and the ending "
                 "letter of each name marked: the two words the tool uses and the book never shows. Three or four "
                 "names only, no piles and no counts, because the tool does the sorting.",
                 placement="main", new_context=True, style="illustration",
                 real_life="a row of school bag hooks on a classroom wall, with a name tag hanging from each hook",
                 shows="three name tags in a row: Teji, Jojo and Hemant, one on each hook. Each name is written in a "
                       "thin dark grey handwriting font with a capital first letter, large enough to read every "
                       "letter. The starting letter has a soft orange ring and the ending letter has a soft blue "
                       "ring, and no middle letter has a ring. No two tags share a starting letter or an ending "
                       "letter. No piles, no counts, no other names and no green ring are drawn",
                 caption="Orange ring: the starting letter. Blue ring: the ending letter.",
                 visuals=["name_tag", "start_end_marker"])),
     DOER("T4.C2", "Starting and Ending Letters", "start_end_letters", "Apply",
          "Students sort names into piles by starting letter or by ending letter and count each pile to find the "
          "letter used most.",
          applies_to="T4.C1", minutes=6, key_terms=["starting letter", "ending letter", "most used letter"],
          recap=["The starting letter is the first letter of a name.",
                 "The ending letter is the last letter.",
                 "Names with the same letter make one pile. Count each pile.",
                 "The tallest pile shows the letter used most. Two piles can tie."],
          items=[
              # CLASH 14: the child taps one of the eight practice names as "my name"; the sample answers use Mala for
              # parts b, c and e. With these eight names D and M tie for the most used starting letter.
              FIO("ch1.letus3b", "Let us Do, Q3(b)",
                  "Write the starting letter of your name.",
                  ["Tap one of the eight names as your name.",
                   "Look at the first letter of that name."],
                  "Sample answer: if my name is Mala, the starting letter is M. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3c", "Let us Do, Q3(c)",
                  "Count all the name(s) that have the same starting letter as yours.",
                  ["Say your name is Mala. Its starting letter is M.",
                   "Find every name that starts with M. Count Mala too.",
                   "Mahesh and Mala start with M."],
                  "Sample answer: 2 names start with M, Mahesh and Mala. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3d", "Let us Do, Q3(d)",
                  "Which starting letter is the most used? Count the names that begin with it.",
                  ["Count the names for each starting letter.",
                   "D 2, H 1, J 1, K 1, M 2, T 1.",
                   "The most is 2, for D and for M. They tie."],
                  "Sample answer: D and M are used the most. D starts 2 names, Deba and Deep. M starts 2 names, "
                  "Mahesh and Mala. Your answer may differ.",
                  kind="exercise"),
              # CLASH 11 (c): read as the same ending letter as your own name, like part c. The other reading (the biggest
              # group with one ending letter) gives the same 2 names here, because only Deba and Mala share one.
              FIO("ch1.letus3e", "Let us Do, Q3(e)",
                  "Count the names with the same ending letter.",
                  ["Use the ending letter of your name, like in part (c).",
                   "Mala ends with a.",
                   "Deba and Mala end with a."],
                  "Sample answer: 2 names end with a, Deba and Mala. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus3f", "Let us Do, Q3(f)",
                  "Write the letters that are not the starting letter of any name.",
                  ["The starting letters are D, H, J, K, M and T.",
                   "That is 6 of the 26 letters of the alphabet.",
                   "26 − 6 = 20 letters are left. Write them."],
                  "Sample answer: A, B, C, E, F, G, I, L, N, O, P, Q, R, S, U, V, W, X, Y, Z. Your answer may "
                  "differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["starting letter", "ending letter", "most used letter"]))

# ---- T5: number names (rows 9 and 10) -> Tool 5 ---------------------------------------------------------------------
# Video 3: Teji and Jojo lay number cards to make numbers of their own (a tens card then a ones card; one card for 1 to 19)
# and count the letters of the number name; their roll numbers 43 and 17 are for Tool 5 (CLASH 23). Misconceptions M_NUM_2 to M_NUM_5 (the dash, forty, the teens, the order of the
# cards) are met here and on Tool 5. CLASH 11 (d): the 27 cards of the picture stand for the cards "at the end of the book".
# CLASH 14: the roll number is a number the child picks.
TOPICS.append(TOPIC(
    "T5", "M2", "Number Names", ["Let us Do"], "Apply",
    "Students make a number name from number cards, a tens card first and then a ones card, and count its letters.",
    "Numbers have names too. You build a number name and count its letters.",
    [A("T5.C1", "Number Names", "Understand",
       "Students say how a number name is made from number cards and count the letters in it.", role="story",
       textbook=["Teji and Jojo are making numbers using these cards."],
       ncert=["ch1.cards1"],
       teach=["Predict first: how can number cards make the number 25?",
              "Lay the tens card first: Twenty. Then lay the ones card: Five.",
              "Count the letters: Twenty has 6, Five has 4. 6 + 4 = 10 letters.",
              "Rule: the tens card goes first. Numbers 1 to 19 are one card. The dash is not a letter."],
       examples=[WE("Example: Make 36 with number cards. How many letters does its number name have?",
                    ["Lay the tens card first: Thirty.",
                     "Then lay the ones card: Six.",
                     "Thirty has 6 letters. Six has 3 letters.",
                     "6 + 3 = 9."],
                    "Thirty and Six make 36. Its number name has 9 letters.")],
       key_terms=["number name", "number cards", "letter count"],
       misconceptions=["M_NUM_2", "M_NUM_3", "M_NUM_4", "M_NUM_5"], minutes=5,
       video=VID("Making Numbers with Cards",
                 "Teji and Jojo make numbers with number cards. A number name is laid out with a tens card then a "
                 "ones card (one card for 1 to 19), and its letters can be counted. The story uses its own numbers "
                 "(15, 25, 36), never 43 or 17: those roll numbers are for Tool 5.",
                 new_idea="a number name is made with number cards, and it has a letter count of its own",
                 story={"characters": ["Teji", "Jojo"],
                        "setting": "A corner of the school classroom: a mat on the floor and a box of number cards "
                                   "spilled out, in three colours, peach, light blue and light green (visual keys: "
                                   "number_card, number_name_row, teji, jojo).",
                        "situation": "Teji and Jojo spill a box of number cards on the mat. Teji says numbers have "
                                     "names too, and the names can be made from the cards. She makes 25: the tens "
                                     "card Twenty first, then the ones card Five. Jojo copies her but lays Five "
                                     "first and Twenty after it. It reads wrong, and Teji slides the cards: the tens "
                                     "card goes first. They count the letters of Teji's number name, Twenty and "
                                     "Five, ten letters in all. Then Jojo makes 15 with one card, Fifteen, and Teji "
                                     "shows that for 1 to 19 one card is enough, so Fifteen has seven letters. "
                                     "Last, Jojo makes 36, Thirty and Six, and writes it as thirty-six with a dash. "
                                     "He counts the dash as a letter and gets one too many. Teji shows him that the "
                                     "dash is not a letter, so thirty-six has nine letters. The story uses only "
                                     "these numbers and never says roll number.",
                        "problem": "Jojo wants to know how many letters his number name has, but the name is made "
                                   "of cards. He does not know which card goes first or what to count.",
                        "thread": "Opens with one line that picks up the name puzzle: Mahesh and Kartik counted the "
                                  "letters of their names, and Teji asks whether numbers have names with letters "
                                  "too. Teji and Jojo are friends of Deba and Deep in the same village school.",
                        "leads_to": "Tool 5, Build a Number Name: the child lays a tens card and a ones card and "
                                    "counts the letters."},
                 seconds=105)),
     DOER("T5.C2", "Build a Number Name", "build_number_name", "Apply",
          "Students make a number name from a tens card and a ones card and count the letters in it.",
          applies_to="T5.C1", minutes=6, misconceptions=["M_NUM_2", "M_NUM_3", "M_NUM_4", "M_NUM_5"],
          key_terms=["number name", "number cards", "letter count"],
          recap=["Lay the tens card first, then the ones card.",
                 "Count the letters on both cards and add them.",
                 "Forty is spelled f, o, r, t, y. It has 5 letters.",
                 "Seventeen is one card with 9 letters.",
                 "The dash is not a letter."],
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
              # CLASH 11 (d): the book says the cards are "at the end of the book"; the screen has them (CLASH 29).
              # CLASH 14: the roll number is a practice number from 1 to 99 that the child picks.
              FIO("ch1.letus4a", "Let us Do, Q4(a)",
                  "Write your roll number using number cards as shown above. The number cards are on the screen. "
                  "My roll number is ________. Its number name has ________ letters.",
                  ["Pick a practice roll number from 1 to 99.",
                   "Lay the tens card first, then the ones card.",
                   "Count the letters in the cards."],
                  "Sample answer: my roll number is 29. Its cards are Twenty and Nine. Its number name has "
                  "6 + 4 = 10 letters. Your answer may differ.",
                  kind="exercise"),
              FIO("ch1.letus4b", "Let us Do, Q4(b)",
                  "Write some numbers and their number names in your notebook. How many letters does each have?",
                  ["Pick a number and write its number name.",
                   "Count the letters. The dash is not a letter."],
                  "Sample answer: 12 is twelve, 6 letters. 31 is thirty-one, 9 letters. 90 is ninety, "
                  "6 letters. Your answer may differ.",
                  kind="exercise"),
          ])],
    topic_type="instructional", key_terms=["number name", "number cards", "letter count"]))

# ---- T6: number puzzles and place names (rows 11, 12, 13) -> Tool 6, then the place names image ---------------------------
# PROVISIONAL, CLASH 15: the brief's "puzzle video" is the concept video of this topic, told as a story (Teji and Jojo
# challenge each other); the puzzles are solved on Tool 6. PROVISIONAL, CLASH 8 and 9: C7 and C8 are one unit with Tool 6
# (at the cap of 6 questions); the open clues (Q2 stem, 93/97/98, "smallest") are for the question mapper and the brief
# writer. PROVISIONAL, CLASH 16: the idea of ch1.tnote3 (what is common in names with the same letter count) is a line for
# the child, homed on the video concept. PROVISIONAL, CLASH 12 and 17: C9 (place names) is ONE image, no video, no tool,
# the last concept of this topic; the book asks nothing about it, so it holds no question. It is not a repeat of C4: it
# shows real signboards, the longest and the shortest place names of India. M_NUM_1 (a bigger number has a longer name) is
# met by the puzzles, M_PUZ_1 and M_PUZ_2 by the riddles on Tool 6.
TOPICS.append(TOPIC(
    "T6", "M2", "Number Puzzles and Place Names", ["Let us Think", "Let us Do", "Teacher's Note"], "Analyze",
    "Students use the letters in number names to find numbers between 1 and 99, and tell which place names in India "
    "are the longest and the shortest.",
    "Some number names have the same letters. You solve puzzles. Then you read about the longest and shortest "
    "place names.",
    [A("T6.C1", "Same Letters, Different Numbers", "Understand",
       "Students find numbers between 1 and 99 whose names have the same number of letters, using the letter count as "
       "a clue.", role="story",
       ncert=["ch1.tnote3"],
       teach=["Predict first: can two numbers have names with the same letter count?",
              "Yes. Twenty has 6 letters. Thirty has 6 letters too.",
              "Fifty-six has 8 letters. Other numbers may have 8 letters too.",
              "Rule: different numbers can have names with the same letter count."],
       key_terms=["letter count", "number name"], misconceptions=["M_NUM_1", "M_PUZ_1", "M_PUZ_2"], minutes=5,
       video=VID("Teji and Jojo's Number Puzzle",
                 "Teji and Jojo challenge each other with puzzles about the letters in number names. They start "
                 "from 56, which has 8 letters, and ask which other numbers have 8 letters. They may end by asking "
                 "which number has the longest name. It does not rebuild a number name and it answers nothing: "
                 "every answer is found on the tool.",
                 new_idea="different numbers can have names with the same number of letters",
                 story={"characters": ["Teji", "Jojo"],
                        "setting": "The same corner of the school classroom, a little later: the mat with the "
                                   "number cards, with a speech bubble for each child (visual keys: number_card, "
                                   "teji, jojo, speech_bubble).",
                        "situation": "Teji and Jojo have laid out the number fifty-six on the mat. Teji tells Jojo "
                                     "that fifty-six has 8 letters, as the book's own opening puzzle says (the "
                                     "cards are already laid, so no number name is built again). Jojo thinks that "
                                     "only fifty-six can have a name with 8 letters. Teji says no, and shows him "
                                     "two single cards: Twenty has 6 letters and Thirty has 6 letters too. Two "
                                     "different numbers with the same number of letters. Jojo is surprised and "
                                     "grins. Teji sets a challenge: find the other numbers between 1 and 99 whose "
                                     "names have 8 letters. Jojo adds his own: and which number between 1 and 99 "
                                     "has the longest name? They shake on it. The story ends there. It names no "
                                     "other number with 8 letters, no longest name and no answer to any riddle, and "
                                     "nobody says what such numbers have in common.",
                        "problem": "Jojo thinks only fifty-six can have a name with 8 letters. Teji says other "
                                   "numbers between 1 and 99 share that count. Which ones are they?",
                        "thread": "Opens with one line that picks up the video before it: Teji and Jojo can now "
                                  "count the letters of a number name, and Jojo wants a puzzle. The same two "
                                  "friends, the same mat and cards.",
                        "leads_to": "Tool 6, Number Name Puzzles: the child hunts for numbers with 8 letters, the "
                                    "longest names and the riddles."},
                 seconds=100)),
     DOER("T6.C2", "Number Name Puzzles", "number_puzzles", "Analyze",
          "Students use clues about the letters in number names to find numbers between 1 and 99 and say what "
          "same-count names share.",
          applies_to="T6.C1", minutes=8, misconceptions=["M_NUM_1", "M_PUZ_1", "M_PUZ_2"],
          key_terms=["letter count", "number name"],
          recap=["Forty, fifty and sixty have 5 letters. One, two and six have 3 letters.",
                 "Add the letters of the two words: 5 + 3 = 8 letters.",
                 "A bigger number can have a shorter name. Ninety-nine has 10 letters.",
                 "To make a puzzle, write a clue and check that a number fits it."],
          items=[
              # The box "Teji and Jojo made the number 56..." (Let us Think) is two items: the solved 56 first, then the hunt.
              FIO("ch1.example2", "Let us Think, 56",
                  "Teji and Jojo made the number 56 (fifty-six). It has 8 letters.",
                  ["Lay the tens card first: Fifty.",
                   "Then lay the ones card: Six.",
                   "Fifty has 5 letters. Six has 3 letters.",
                   "5 + 3 = 8 letters."],
                  "From the picture: 56 is Fifty and Six. Its number name has 5 + 3 = 8 letters.",
                  kind="example"),
              # CLASH 9 (d): any of the 13 numbers fits; the "what is common" is in the last two steps (Sample answer).
              FIO("ch1.think1", "Let us Think",
                  "Write other numbers between 1 and 99 that have 8 letters.",
                  ["Try a number. Say its name and count the letters.",
                   "Keep the numbers whose names have 8 letters.",
                   "Forty, fifty and sixty have 5 letters each.",
                   "One, two and six have 3 letters each: 5 + 3 = 8."],
                  "Sample answer: forty-six (46), fifty-one (51), sixty-two (62), thirteen (13) and eighteen "
                  "(18). The 13 numbers with 8 letters are 13, 14, 18, 19, 41, 42, 46, 51, 52, 56, 61, 62 and "
                  "66. Your answer may differ.",
                  kind="exercise"),
              # The longest names are 73, 77 and 78 (12 letters each): three lines, three numbers.
              FIO("ch1.letus5", "Let us Do, Q1",
                  "Write the number(s) between 1 and 99 that have the longest name.",
                  ["A number name is longest when both of its words are long.",
                   "Seventy has 7 letters, the longest tens word.",
                   "Three, seven and eight have 5 letters each, the longest ones words.",
                   "7 + 5 = 12 letters. Ninety-nine has only 6 + 4 = 10 letters."],
                  "Sample answer: 73, 77 and 78. Seventy-three, seventy-seven and seventy-eight have 12 letters "
                  "each.",
                  kind="exercise"),
              # CLASH 9 (a) and CLASH 29: the printed stem of Q2 repeats Q1's, so only the Find out box is shown.
              # CLASH 9 (b): 93, 97 and 98 all fit; "very near to 100" does not choose one.
              FIO("ch1.letus6a", "Let us Do, Q2, first Find out",
                  "Find out. My number name has two words. The first word has 6 letters. The second word has 5 "
                  "letters. I am very near to 100. Who am I?",
                  ["The first word is a tens word with 6 letters: twenty, thirty, eighty, ninety.",
                   "The second word is a ones word with 5 letters: three, seven, eight.",
                   "Very near to 100 means ninety. More than one number may fit."],
                  "Sample answer: ninety-three (93), ninety-seven (97) or ninety-eight (98). Each one fits.",
                  kind="exercise"),
              # CLASH 9 (c): "smallest" is read as the fewest letters, as the steps say; 63 is not the answer.
              FIO("ch1.letus6b", "Let us Do, Q2, second Find out",
                  "Find out. My friends and I are the numbers from 63 to 78. My number name is the smallest among "
                  "all my friends. Who am I?",
                  ["Count the letters in each name from 63 to 78.",
                   "Seventy has 7 letters. Every other name has 8 or more.",
                   "Here, smallest means the name with the fewest letters."],
                  "Sample answer: 70, seventy. It has 7 letters, the fewest from 63 to 78. Sixty-three, the "
                  "smallest number, has 10 letters.",
                  kind="exercise"),
              # CLASH 8 and 14: a notebook task for classmates; the screen version is "make a clue and test it".
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
     A("T6.C3", "Longest and Shortest Place Names", "Remember",
       "Students tell which place names in India are the longest and which are the shortest.", role="image",
       textbook=["Venkatanarasimharajuvaripeta is a place in India with the longest name. It is located in Andhra "
                 "Pradesh, close to the border of Tamil Nadu.",
                 "Ib in Odisha and Od in Gujarat are the places in India with the shortest names."],
       teach=["Predict first: how long can the name of a place be?",
              "The long board says Venkatanarasimharajuvaripeta. It is the longest place name in India.",
              "Ib and Od are very short. They are the shortest place names in India.",
              "Rule: the longest name has the most letters, for places too."],
       ncert=["ch1.place1", "ch1.place2"], key_terms=["longest name", "shortest name"], minutes=4,
       image=IMG("Place Name Signboards",
                 "Real signboards of the longest and the shortest place names in India: a new real-life example of "
                 "the longest and the shortest name, taken from places and not from animals or friends. Every name "
                 "spelled exactly, and no letter count shown.",
                 placement="main", new_context=False, style="photo",
                 real_life="yellow place name boards at railway stations in India: one with a very long name and "
                           "two with very short names",
                 shows="three yellow boards with black letters in English capitals, spelled exactly letter by "
                       "letter as written here: VENKATANARASIMHARAJUVARIPETA on one very long board, and IB and OD "
                       "on two small boards, so the long board is much longer than the two short ones. A local "
                       "script is drawn above the English only if it is a real script, otherwise it is left out. "
                       "No letter count, no numbers, no invented letters and no person pointing",
                 caption="Venkatanarasimharajuvaripeta, the longest place name in India. Ib and Od, the shortest.",
                 visuals=["place_sign"]))],
    topic_type="instructional", key_terms=["letter count", "number name", "longest name", "shortest name"]))

# ---- T7: grouping things (rows 14, 15, 16) -> Tool 7, then the hair styles image ----------------------------------------------
# Video 5 shows Teji's two groups by a rule and Jojo's different grouping of the same cards; it does not say Jojo's rule
# (ch1.jojo1 asks it on Tool 7). PROVISIONAL, CLASH 10: C10 and C11 are one unit with Tool 7. PROVISIONAL, CLASH 16: the idea
# of ch1.tnote4 (other ways to group; every object belongs to one group) is a line for the child, homed on the video
# concept. PROVISIONAL, CLASH 13 and 17: C12 (hair styles) is ONE image, no video, no tool, the last concept of this topic;
# the book's question ch1.letus10 sits on it (the question mapper homed it there: the gate lets an image concept hold a
# question when no tool follows it, and no tool may be added after it, CLASH 13). It is the ONE book question of this plan
# that sits on an image concept. The class is the plan's own practice class, labelled as such (CLASH 14, 21). M_GRP_1 to
# M_GRP_3 are met on Tool 7. Tool 7 holds jojo1, letus8 and letus9, in the book's order.
TOPICS.append(TOPIC(
    "T7", "M3", "Grouping Things", ["Let us Do", "Teacher's Note"], "Apply",
    "Students put things into two groups by a rule, say what is common in a group, regroup the same things another "
    "way, and sort children by hair style and count each group.",
    "You put things into two groups by a rule. Then you group them another way. You also group children by hair "
    "style.",
    [A("T7.C1", "Group Things by a Rule", "Understand",
       "Students put things into two groups by a rule and say that the same things can be grouped another way.",
       role="story",
       textbook=["Teji and Jojo have some picture cards. Teji has put these into two groups like this:",
                 "She has grouped the cards into 'those that eat food' and 'those that don't eat food'.",
                 "Jojo has arranged the same cards differently."],
       ncert=["ch1.group1", "ch1.tnote4"],
       teach=["Predict first: can the same cards be grouped in more than one way?",
              "Teji's groups: those that eat food, those that don't eat food.",
              "Jojo groups the same cards in another way.",
              "Rule: things can be grouped by a rule. The same things can be grouped another way.",
              "Think: what more things could you add to each group? Every thing goes in one group."],
       key_terms=["group", "rule", "common"], misconceptions=["M_GRP_1", "M_GRP_2", "M_GRP_3"], minutes=5,
       video=VID("Teji's Two Groups",
                 "Teji puts her picture cards into two groups by a rule. Jojo groups the same cards another way. "
                 "The story shows that the same things can be grouped in more than one way, and ends before anyone "
                 "says Jojo's rule: the tool asks for it.",
                 new_idea="things can be grouped by a rule, and the same things can be grouped another way",
                 story={"characters": ["Teji", "Jojo"],
                        "setting": "The same corner of the school classroom: a table with ten picture cards and "
                                   "two dotted boxes beside them (visual keys: picture_card, group_box, teji, "
                                   "jojo). The picture cards have no names written on them.",
                        "situation": "After the number puzzle, Jojo takes out a bag of ten picture cards: a yellow "
                                     "bird, a black insect, a brown rat, a striped fish, a blue drone, a white "
                                     "aeroplane, a blue mobile phone, a yellow light bulb, an orange book and a red "
                                     "kite. Teji puts the cards into two groups with a rule she says in her own "
                                     "words: those that eat food, and those that don't eat food. Jojo watches, "
                                     "then gathers the same ten cards and sets them out as two different groups, "
                                     "without a word. His cards lie still in two dotted boxes, with no label, no "
                                     "caption and nothing that moves or flutters. Teji checks that every card is in "
                                     "one of Jojo's two groups and says, 'Your groups are different from mine, and "
                                     "they work too.' She looks at them for a long time and smiles. The story ends "
                                     "there: nobody asks or says what Jojo's rule is. The voice never names the "
                                     "cards and never uses a word that hints at his rule.",
                        "problem": "Jojo says, 'I grouped the same cards, but my groups are not like yours.' Teji "
                                   "wonders whether there is only one right way to group a set of cards, or "
                                   "whether both ways can be right.",
                        "thread": "Opens with one line that picks up the video before it: after the number "
                                  "puzzle, Jojo takes out a bag of picture cards. The same two friends in the same "
                                  "classroom corner.",
                        "leads_to": "Tool 7, Group the Cards Two Ways: the child groups the cards by Teji's rule, "
                                    "then finds the rule of Jojo's groups."},
                 seconds=100)),
     DOER("T7.C2", "Group the Cards Two Ways", "group_two_ways", "Apply",
          "Students drag cards into two groups by a rule, find the rule of a group, and regroup the same cards another "
          "way.",
          applies_to="T7.C1", minutes=7, misconceptions=["M_GRP_1", "M_GRP_2", "M_GRP_3"],
          key_terms=["group", "rule", "common"],
          recap=["A rule tells which things go together.",
                 "Things that fit the rule go in one group. The rest go in the other.",
                 "The same things can be grouped another way.",
                 "Every thing goes in one group.",
                 "Think of more things and put them in groups."],
          items=[
              # CLASH 29: the book prints "each groups"; the screen says "each group". The rule is read from the picture.
              FIO("ch1.jojo1", "Story, Jojo's groups",
                  "What is common in each group Jojo has made?",
                  ["Look at the cards in the first group.",
                   "Ask: what can all of these do?",
                   "Now look at the cards in the second group. Can any of them do it?"],
                  "From the picture: the first group has things that fly. They are the kite, aeroplane, bird, "
                  "drone and the fly. The second group has things that do not fly. They are the mobile phone, "
                  "fish, light bulb, book and rat.",
                  kind="prompt"),
              # CLASH 10: four and four, as the lines of the book show. The lamp and the clock are read as electric ones.
              FIO("ch1.letus8", "Let us Do, Q4",
                  "Given below are pictures of some household objects: TV, Chair, Lamp, Bed, Clock, Fan, Pillow, "
                  "Blanket. Write the names of the above objects in the two groups given below: Things that need "
                  "electricity, Things that don't need electricity.",
                  ["Look at each object. Does it need electricity to work?",
                   "TV, Lamp, Clock and Fan do.",
                   "Chair, Bed, Pillow and Blanket do not.",
                   "Every object goes in one group."],
                  "From the picture: Things that need electricity: TV, Lamp, Clock, Fan. Things that don't need "
                  "electricity: Chair, Bed, Pillow, Blanket. The lamp is an electric table lamp. The clock runs on "
                  "electricity, from a battery or the plug.",
                  kind="exercise"),
              # CLASH 10 and 29: "the given objects" is read as these eight household objects. A different rule is the
              # child's own; the sample answer groups by sleeping.
              FIO("ch1.letus9", "Let us Do, group differently",
                  "Group the eight household objects differently. Write them down in the space below.",
                  ["Think of a new rule for the same eight objects.",
                   "Put every object in one of the two groups.",
                   "Say your rule."],
                  "Sample answer: Things we use for sleeping: Bed, Pillow, Blanket. Things we do not use for "
                  "sleeping: TV, Chair, Lamp, Clock, Fan. Your answer may differ.",
                  kind="exercise"),
          ]),
     A("T7.C3", "Hair Styles", "Apply",
       "Students sort the children of a class by hair style and count the children in each group.", role="image",
       teach=["Predict first: which hair style do most children in the picture have?",
              "Look at the hair of each child. Find its style in the row.",
              "Count the children for each style.",
              "Rule: sort the children by hair style, then count each group. The groups together make all the "
              "children."],
       key_terms=["hair style"], minutes=5,
       # The book's question sits on the image because no tool follows it (CLASH 13). CLASH 31, settled at the briefs
       # stage: the picture is fixed as a practice class of 12 children (the image brief below lists them one by one), so
       # the answer now holds the six true counts, which add up to 12.
       items=[
           FIO("ch1.letus10", "Let us Do, Hair Styles",
               "Hair Styles. Mala is going to school. Her mother has combed her hair. Mala has two ponytails. Look at "
               "the children in your class. All children comb their hair in different ways. Look and write down.",
               ["The picture shows a practice class, not your own class.",
                "Look at the hair of each child.",
                "Find the hair style of the table that matches it.",
                "Count the children for each hair style and write the number."],
               "From the picture: 2 children have a high ponytail. 3 have two long plaits. 2 have short curly hair. "
               "1 has wavy hair with a clip. 3 have short straight hair. 1 has two low ponytails. "
               "2 + 3 + 2 + 1 + 3 + 1 = 12 children in all. Your own class may give other numbers.",
               kind="exercise"),
       ],
       image=IMG("Hair Styles in a Class",
                 "A real-life picture of a class of children with the six hair styles of the table, each child clear "
                 "and countable, which the child groups and counts to fill the table. No number is shown: the counts "
                 "are the child's answer.",
                 placement="main", new_context=False, style="illustration",
                 real_life="a class of twelve children in school clothes, sitting in two rows of six and facing the "
                           "front",
                 shows="twelve children, the plan's own practice class, each drawn from the chest up facing the "
                       "viewer with the hair fully visible and a small gap between neighbours; the back row sits on a "
                       "low bench so no child is hidden. Each child has exactly one of the six hair styles, as "
                       "follows. Back row, left to right: a boy with short curly hair; a boy with short straight "
                       "black hair; a girl with two long plaits tied with blue ribbons; a girl with one high "
                       "ponytail; a boy with short straight black hair; a girl with wavy hair and a blue hair clip. "
                       "Front row, left to right: a girl with short curly hair; a girl with two long plaits tied "
                       "with blue ribbons; Mala, with brown hair in two low ponytails; a girl with one high "
                       "ponytail; a boy with short straight black hair; a girl with two long plaits tied with blue "
                       "ribbons. So the six styles hold two, three, two, one, three and one children, twelve in "
                       "all. Under the picture sits a strip of the six hair-style pictures of the table, in the "
                       "order one high ponytail, two long plaits, short curly hair, wavy hair with a clip, short "
                       "straight hair, two low ponytails, each with an empty box below it. No number, tally, tick "
                       "or ring is drawn, and Mala's mother and the combing scene are left out",
                 caption="Match each child's hair to a style in the row. Then count.",
                 visuals=["hair_style_pictures", "mala", "class_children"]))],
    topic_type="instructional", key_terms=["group", "rule", "common", "hair style"]))

# ---- T8: the review (row 17) -------------------------------------------------------------------------------------------------
# Two look-back concepts, nothing new: no video, no tool, no book item, no new key term (every key term below is one of an
# earlier concept). PROVISIONAL, CLASH 15: no separate "concept checks" are added (the book has none); the brief writer
# recaps with the plan's own lines and may show earlier pictures by reference. Together the two concepts revise every
# idea topic (T2 to T7), the image concepts included.
TOPICS.append(TOPIC(
    "T8", "MLAST", "Chapter Review", ["Review"], "Understand", "",
    "A short look back at marks, names, number names and groups.",
    [A("T8.C1", "Look Back: Marks and Names", "Understand",
       "Students use marks to tell which cows are still out, and use letter counts to find the longest and the "
       "shortest name.", role="review",
       # The review holds no picture of its own (CLASH 27): each look-back line below points at a picture shown before
       # (the wall with marks, the name tags image, the place signboards image) and shows it again by reference.
       teach=["Look back at the wall with marks. A mark is left. Is that cow home or still out?",
              "It is still out. A struck out mark is a cow that came home.",
              "Look back at two names. Which has more letters? That one is the longer name.",
              "The longest name has the most letters. The shortest name has the fewest letters.",
              "Look back at the name tags. Orange ring: starting letter. Blue ring: ending letter.",
              "Look back at the signboards. Which place name has the most letters?"],
       key_terms=["mark", "marks left", "letter count", "longest name", "shortest name", "starting letter",
                  "ending letter"],
       review_covers=["T2.C1", "T3.C1", "T4.C1", "T6.C3"], minutes=4),
     A("T8.C2", "Look Back: Number Names and Groups", "Understand",
       "Students make a number name from number cards, count its letters, and put things into two groups by a rule.",
       role="review",
       # No picture of its own (CLASH 27): the number cards, the cards in two groups and the hair styles picture are
       # shown again by reference to the pictures already made.
       teach=["Look back at the number cards. Which card goes first in a number name?",
              "The tens card goes first, then the ones card. Numbers 1 to 19 are one card.",
              "Different numbers can have names with the same letter count.",
              "Look back at the cards in two groups. A rule tells which things go together.",
              "The same things can be grouped another way. Every thing goes in one group.",
              "Look back at the children. Group them by hair style, then count each group."],
       key_terms=["number name", "number cards", "letter count", "group", "rule", "hair style"],
       review_covers=["T5.C1", "T6.C1", "T7.C1", "T7.C3"], minutes=4)],
    topic_type="summary"))

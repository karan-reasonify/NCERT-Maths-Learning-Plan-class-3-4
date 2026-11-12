# -*- coding: utf-8 -*-
"""What's in a Name? (Class 3, chapter 1): the chapter's tool specs, one entry per tool of the locked table.

STRUCTURE STAGE (c34-tool-mapper): each entry carries tool_id, title (EXACTLY the name in the table), approved_no, the ONE
learning objective, the VISUAL_KEY keys it draws and, for Tool 1, the `notice` prompts.
BRIEFS STAGE (c34-brief-writer): the rest of each spec (screen, controls, instruction, feedback, done_when, shared_state,
hints) is written here. The screen text describes the three phases of every tool in the same order: PHASE 1 get ready (a
simple situation that reconnects with the video or picture before it), PHASE 2 play (drag, tap, count or compare, with
feedback, hints, retry and Reset), PHASE 3 the book's own questions, exactly as the book words them (they are the FIO items
of the concept, never written here). The tool's questions are the book items (FIO in topics_N.py), never written here.

The seven tools are the pipeline's PROPOSAL, not the content team's (CLASH 1 in content.py): no content-team table existed
and the user chose "propose fresh from the book". tool_map.md -> chapter.config.json "approved_tools" holds the same names,
purposes and order; tool_map.locked.md has the concept, the place in the flow and the proposed book items of each.

A tool here is a spec + placeholder (tools_spec/TOOL_SPEC_GUIDE.md): the tool itself is built elsewhere. Nothing below is
made yet.

Notes for the builders:
- Tools 3, 4 and 5 and the hair styles image use sample data (CLASH 14): the book's eight names are the practice friends
  and the sample roll number is 29. Anything the plan makes up (practice numbers, practice names, Hemant's rows) is labelled
  Practice or Sample on screen.
- No tool needs number names before Tool 5 (Tool 1 is for children who "do not know how to count": one mark, one cow).
- Every tool has the same frame: step dots, Hint, Reset, Back and Next in the same place; no score and no timer; the same
  colours (orange ring: starting letter, blue ring: ending letter; the rings are never green; a round green badge is a
  tick or a cross; the green of the tens cards and of the number circle is plain card and outline colour, not a badge).
- Answer entry (fix pass of 6 Nov 2026): every book question has a defined input within the 4 controls of its tool. Tool 1:
  Yes and No tiles. Tool 2: a number pad (47, 45) and three answer cards (why worried); marks made with the 1 and 5
  buttons of a row. Tool 3: drag a card, a name or an answer tile into a box; tick or cross badge on a name. Tool 4: tap a
  card, a letter, a pile or a number tile; drag a card into a pile. Tool 5: drag a card to the board; a number pad for the
  roll number and the letter counts. Tool 6: drag a card or a laid number into a row; pick a clue. Tool 7: drag a card
  into a group; tap a rule card; Check my groups. The notice prompts of Tool 1 are read and thought about: no input.
"""
from __future__ import annotations

from topics_common import T  # noqa: F401

TOOLS = {
    # Tool 1: the exploration tool, right after the hook. Concept: C1 (the opening situation).
    "marks_gate": T(
        "tool_marks_at_the_gate", "Marks at the Gate", 1,
        "Students make one mark for each cow that leaves, strike one out for each that returns, "
        "and notice whether any cow is missing.",
        screen="Same frame as every tool (step dots, Hint, Reset, Back, Next; no score, no timer). One big picture: "
               "the cow shed gate with Deba and Deep beside it, and a plain wall for the marks. Eight cows (the "
               "plan's own practice herd, with a small label Practice) wait in the shed. No number is shown on screen. "
               "PHASE 1, get ready: one line, 'Deba and Deep want to know that no cow is lost.' "
               "PHASE 2, play. Morning: a cow walks to the gate and waits. The child taps Make a mark, one upright bar "
               "appears on the wall and the cow walks out. This repeats for every cow. When the last cow is out, the "
               "first notice prompt shows. "
               "Evening: the line changes to 'Strike out one mark for each cow that comes back.' A cow walks to the "
               "gate and waits. The child taps Strike out a mark, a slanting line crosses the top upright bar and the "
               "cow walks in. This repeats for every cow, and the second notice prompt shows after the first cow "
               "is in. "
               "PHASE 3, the book's question: when the last cow is in, the question 'Did all the cows come back "
               "home?' shows under the wall with two big answer tiles, Yes and No. The child looks at the wall and "
               "taps one tile. The third notice prompt shows last. The three notice prompts are read and thought "
               "about: no answer is entered, the child taps Next.",
        controls=["Make a mark", "Strike out a mark", "Tap the Yes tile or the No tile", "Reset"],
        instruction="Make a mark when a cow goes out. Strike one out when it comes back.",
        notice=["What do you see on the wall when a cow goes out?",
                "What happens to the marks when the cows come back?",
                "How can you tell that no cow is missing?"],
        feedback=["Right try: One cow goes out, so one mark appears on the wall.",
                  "Right try: One cow comes in, so one mark is struck out.",
                  "Right try: Yes. Every mark is struck out, so no cow is missing.",
                  "Wrong try: Look at the wall. Is any mark left? Every mark is struck out, so no cow is missing.",
                  "Wrong try: No cow is at the gate. Wait for the next cow.",
                  "Wrong try: This cow has its mark already. One mark for each cow.",
                  "Wrong try: Wrong button. A cow going out gets a mark. A cow coming in gets a strike out.",
                  "Tone: a soft chime and 'Well done.' before each right reason. 'Not yet, try again.' before each wrong "
                  "reason. No buzzer, no red cross, no score."],
        done_when="Every cow has gone out with one mark made and has come back with one mark struck out, and the "
                  "child has tapped Yes or No for the book's question.",
        shared_state=["marks_made", "marks_struck_out"],
        hints=["Look at the gate. Is the cow going out or coming in?",
               "One cow, one mark. Going out: make a mark. Coming in: strike one out.",
               "A cow is waiting at the gate. Tap the button that matches what it is doing.",
               "Going out: tap Make a mark. Coming in: tap Strike out a mark."],
        visuals=["tally_mark", "struck_mark", "wall_marks", "cow_shed", "cows", "deba_and_deep"]),

    # Tool 2: C2 (reading the marks) with C3 (marks for two kinds), the book's own pair.
    "marks_herd": T(
        "tool_marks_for_a_big_herd", "Marks for a Big Herd", 2,
        "Students read the marks to find the cows still out and the cows back, "
        "then make separate marks for cows and sheep.",
        screen="Same frame as every tool (step dots, Hint, Reset, Back, Next; no score, no timer). The picture is the "
               "stone slab from the story, its marks standing in groups of five, with the shed gate beside it. "
               "PHASE 1, get ready: a small slab labelled Practice (the plan's own) holds 13 marks: two groups of "
               "five and one group of three. One line: 'The herd is big. Marks stand in groups of five.' "
               "PHASE 2, play: the child taps each group and a running total shows 5, 10, 13. Then ten cows walk in "
               "with the line 'Ten cows come home. Strike out their marks.' and the child taps a group of five "
               "twice to strike out ten marks. Three marks stay standing, and the line 'Which marks are the cows "
               "still out?' asks the child to tap them. "
               "PHASE 3, the book's questions on the real slab, one after another. (1) Count the marks: nine groups of "
               "five and one group of two. Each tap shows only that group's own count and no running total; the "
               "child adds them and types the number of cows on the number pad (digits 0 to 9 and an OK tile), "
               "to fill the blank 'they had ___ cows'. (2) The next day the cows walk in, and each time five cows "
               "enter the child taps a group of five to strike it out, nine times. The last group of two stays "
               "standing and the gate stays empty. Then three answer cards show for why Deba and Deep were worried: "
               "'Two marks were still left, but no cows were outside.' and two wrong cards, 'Every mark was struck "
               "out and every cow was home.' and 'The wall had too many marks to count.' The child taps one card. "
               "Last, the child types on the number pad how many cows had reached home. (3) Hemant's herd: a cow row "
               "and a sheep row, each headed by a picture of a cow or a real sheep, with '36 cows' and '23 sheep' in "
               "words. Each row has its own Make 1 mark and Make 5 marks buttons, so the row is chosen by the button "
               "the child taps. The child makes marks for his cows and his sheep, kept in separate rows. A tap on a "
               "mark takes it back.",
        controls=["Tap a group of marks", "Tap Make 1 mark or Make 5 marks on a row",
                  "Tap the number pad or an answer card", "Reset"],
        instruction="Count marks in fives. Marks left are cows still out. Keep cows and sheep apart.",
        feedback=["Right try: Ten cows came in, so ten marks are struck out.",
                  "Right try: The marks left are the cows still out.",
                  "Right try: Marks were left, but no cow was outside. Some cows had not come back.",
                  "Right try: 47 − 2 = 45, so 45 cows reached home.",
                  "Right try: 36 marks in the cow row and 23 marks in the sheep row. One mark for each animal.",
                  "Wrong try: That number is not right. Count each group again. A full group has five marks.",
                  "Wrong try: Cows home are all the marks minus the marks left. Take away again.",
                  "Wrong try: If every mark were struck out, they would not worry. Look at the marks left.",
                  "Wrong try: Counting is not the worry. A mark left stands for a cow still out.",
                  "Wrong try: Struck out marks are cows that came home. Look at the marks left.",
                  "Wrong try: Cows and sheep need separate rows. Make cow marks in the cow row.",
                  "Wrong try: This row has more marks than animals. Tap a mark to take it back.",
                  "Tone: a soft chime and 'Well done.' before each right reason. 'Not yet, try again.' before each wrong "
                  "reason. No buzzer, no red cross, no score."],
        done_when="The child has counted the practice slab and the real slab, struck out the marks of the cows that "
                  "came home, typed the cows on the slab and the cows home, tapped why Deba and Deep were worried, "
                  "and made separate marks for Hemant's cows and sheep.",
        shared_state=["marks_on_slab", "marks_struck_out", "cow_marks", "sheep_marks"],
        hints=["Look at the marks. They stand in groups. Each mark is one cow.",
               "Work group by group. A full group is five cows.",
               "Count in fives: 5, 10, 15. The Make 5 marks button adds one group.",
               "Tap each group once and add them. Marks left are the cows still out."],
        visuals=["tally_mark", "struck_mark", "stone_slab", "sheep", "cows", "deba_and_deep"]),

    # Tool 3: C4 (the length of a name is its letter count).
    "longest_shortest": T(
        "tool_longest_and_shortest_name", "Longest and Shortest Name", 3,
        "Students count the letters in each name and compare them to find the longest and the shortest name.",
        screen="Same frame as every tool (step dots, Hint, Reset, Back, Next; no score, no timer). Names sit on large "
               "cards, one letter in each box, all boxes the same size, so a name that only looks wider is not "
               "mistaken for a longer one. "
               "PHASE 1, get ready: two names labelled Practice (the plan's own, cat and horse), with their letters "
               "counted and one line, 'Horse has more letters than cat.' "
               "PHASE 2, play: three names labelled Practice (hen, camel and buffalo, the plan's own). The child taps the "
               "letters of each name to count them, then follows the line 'Tick the longest name. Cross the "
               "shortest.' "
               "PHASE 3, the book's questions, one after another. (1) The ten animal cards, each with letter boxes. "
               "The child taps the letters to count each card, then drags one card into First team captain and one "
               "into Second team captain; the letter count shows on the card and travels with it into the box. "
               "(2) A strip of four animal names the plan adds (bat, "
               "giraffe, crocodile, rhinoceros, labelled Sample animals); the child drags one that has more letters "
               "than the first team's captain into a box. (3) Mahesh and Kartik in equal letter boxes beside the two "
               "boys; the child counts both names and drags the answer tile: Mahesh, Kartik or The same. (4) The "
               "eight friends of the book (Deba, Deep, Hemant, Mahesh, Kartik, Teji, Jojo, Mala), labelled Practice "
               "with the book's friends, are dragged onto eight lines. (5) The child taps the green tick badge on the "
               "longest names and the green cross badge on the shortest; names that tie all get the same mark.",
        controls=["Tap a letter to count it", "Drag a name or an answer into a box",
                  "Tap the tick or the cross on a name", "Reset"],
        instruction="Count the letters of each name. Most make the longest. Fewest make the shortest.",
        feedback=["Right try: The count goes up by one for each letter you tap.",
                  "Right try: That name has the most letters, so it is the longest.",
                  "Right try: That name has the fewest letters, so it is the shortest.",
                  "Right try: Both names have 6 letters. They are the same length. Neither is longer.",
                  "Right try: Names that tie for the most letters all get a tick.",
                  "Wrong try: Count the letters again. More letters make a longer name.",
                  "Wrong try: That name looks wider, but wider is not longer. Count the letters.",
                  "Wrong try: That name does not have more than 8 letters. Try another name.",
                  "Tone: a soft chime and 'Well done.' before each right reason. 'Not yet, try again.' before each wrong "
                  "reason. No buzzer, no red cross, no score."],
        done_when="The child has counted the letters of the practice names and the ten animal cards, named both team "
                  "captains, compared Mahesh and Kartik, filled the eight friends' names, and ticked the longest and "
                  "crossed the shortest names.",
        shared_state=["letter_counts", "friend_names"],
        hints=["Look at one name. Tap its letters, one tap for each letter.",
               "Count every name. Then compare the counts, not how wide the names look.",
               "The most letters make the longest name. The fewest make the shortest.",
               "Tap every letter and read each count. Pick the biggest and the smallest."],
        visuals=["animal_card", "name_big", "mahesh_kartik_boys", "tick_and_cross"]),

    # Tool 4: C5 (starting letters and ending letters). The weakest tool of the table (CLASH 7).
    # Fix pass 6 Nov 2026: the tool no longer replays the name tags image (its three tags Teji, Jojo and Hemant, its bag
    # hooks, its drawn rings, its caption line). Name cards on a table, other names in the get-ready and play phases, and
    # the two rings appear only as the child taps (the tool's own device).
    "start_end_letters": T(
        "tool_starting_and_ending_letters", "Starting and Ending Letters", 4,
        "Students sort names by their starting letter or ending letter and count each group to find the letter used most.",
        screen="Same frame as every tool (step dots, Hint, Reset, Back, Next; no score, no timer). Name cards lie flat "
               "on a table (the name_tag card, string tucked under; no hooks, no row on a wall). No card has a ring "
               "at the start. A ring appears only when the child taps a letter, and its meaning shows beside it: an "
               "orange ring for a starting letter with the words 'starting letter', a blue ring for an ending "
               "letter with the words 'ending letter'. No middle letter is ever ringed. "
               "PHASE 1, get ready: one card, Mala, lies alone on the table, no ring, with one line, 'A name has a "
               "first letter and a last letter. Find them.' "
               "PHASE 2, play: three practice cards, Kartik, Mahesh and Deba, come one at a time with the line 'Tap "
               "the first letter. Then tap the last letter.' The child taps the first letter and an orange ring "
               "appears with the words 'starting letter'. The child taps the last letter and a blue ring appears with "
               "the words 'ending letter'. A tap on a middle letter gives a gentle shake. "
               "PHASE 3, the book's questions, one after another, with the eight friends of the book (Deba, Deep, "
               "Hemant, Mahesh, Kartik, Teji, Jojo, Mala) as name cards on the table, labelled Practice with the "
               "book's friends. Each card now shows its orange ring and its blue ring, and a row of number tiles "
               "from 1 to 8 sits under the table. (1) 'My name' is Mala (the child may tap another card); the child "
               "taps the card, then taps its starting letter. (2) With the switch on Starting letter, the child "
               "drags cards into piles: a card goes onto a pile with the same orange-ring letter or starts a new "
               "pile. The child counts the pile of their own letter and taps the number tile with that count. (3) "
               "The child taps the tallest pile or piles, a tie is allowed, and taps the number tile for the count "
               "in it. (4) The switch is turned to Ending letter and the cards are sorted by their blue-ring "
               "letter; the child counts the names that end like their own and taps the number tile with that "
               "count. (5) An alphabet strip from A to Z: the child taps every letter that starts no name, and a "
               "tap on a starting letter gives a gentle shake.",
        controls=["Drag a card into a pile", "Switch: starting letter or ending letter",
                  "Tap a card, a letter, a pile or a number tile", "Reset"],
        instruction="Tap the first and last letter. Drag names with the same letter together.",
        feedback=["Right try: The first letter gets an orange ring. The last letter gets a blue ring.",
                  "Right try: Deba and Deep both start with D, so they share a pile.",
                  "Right try: The pile has 2 cards, so the tile 2 is right.",
                  "Right try: Two piles are the tallest. Two letters are used the most.",
                  "Right try: Deba and Mala both end with a, so they share a pile.",
                  "Wrong try: That is a middle letter. Tap the first or the last letter.",
                  "Wrong try: Kartik starts with K, not D. Start a new pile for K.",
                  "Wrong try: Count the cards in the pile again. Tap the tile with that number.",
                  "Wrong try: H starts Hemant. It is a starting letter, so leave it out.",
                  "Tone: a soft chime and 'Well done.' before each right reason. 'Not yet, try again.' before each wrong "
                  "reason. No buzzer, no red cross, no score."],
        done_when="The child has tapped the starting and ending letters of the practice name cards, sorted the eight "
                  "names into piles by starting letter and by ending letter, tapped the number tiles for the counts, "
                  "and tapped the letters that start no name.",
        shared_state=["friend_names", "my_name", "piles"],
        hints=["Look at one name card. Which letter comes first? Which comes last?",
               "Names with the same letter go in one pile. Then count the cards in each pile.",
               "Check the switch. It says starting letter or ending letter.",
               "Drag a card onto a pile with the same letter. If there is none, start a new pile."],
        visuals=["name_big", "name_tag", "start_end_marker", "group_box", "answer_blank"]),

    # Tool 5: C6 (number names and their letter count).
    "build_number_name": T(
        "tool_build_a_number_name", "Build a Number Name", 5,
        "Students make a number name from a tens card and a ones card and count the letters in it.",
        screen="Same frame as every tool (step dots, Hint, Reset, Back, Next; no score, no timer). All 27 number cards "
               "sit at the bottom in their three colours: peach ones, light blue teens, light green tens. Above them "
               "is a laying board where cards go side by side, the tens card first and then the ones card, with no "
               "dash and no plus sign between them. Teji and Jojo stand at the two sides. A green-outlined circle "
               "shows the number, a letter strip shows the letters of each card, and a number pad (digits 0 to 9 "
               "and an OK tile) sits under the board for every number the child types. "
               "PHASE 1, get ready: the story's 25 is laid out (Twenty, Five) with one line, 'Tens card first. Then "
               "the ones card.' "
               "PHASE 2, play: with the line 'Make 24. Tens card first.' the child makes the practice number 24 (the "
               "plan's own, labelled Practice) from cards, taps the letters to count them and types the count on the "
               "pad, and then makes 16 with one card in the same way. The written name beside the "
               "circle, twenty-four, has a dash; a tap on the dash gives a gentle shake, because the dash is not a "
               "letter. "
               "PHASE 3, the book's questions, one after another. (1) Teji's number 43: the child lays Forty and "
               "Three, counts the letters and types the count on the pad. (2) Jojo's number 17: the child lays "
               "Seventeen, counts its letters and types the count on the pad, to fill the blank 'its number name has "
               "___ letters'. (3) The child types a roll number from 1 to 99 on the pad, labelled Practice roll "
               "number (the sample is 29), lays its cards, counts, and types the letter count. (4) The child types "
               "another number, lays its cards, counts and types the count, and repeats this to make a list of at "
               "least three numbers, each with its count.",
        controls=["Drag a card to the board or back to the row", "Tap each letter to count it",
                  "Tap the number pad", "Reset"],
        instruction="Lay the tens card first, then the ones card. Count the letters.",
        feedback=["Right try: Twenty has 6 letters and Four has 4. 6 + 4 = 10 letters.",
                  "Right try: Sixteen is one card. It has 7 letters.",
                  "Right try: Forty has 5 letters and Three has 5. 5 + 5 = 10 letters.",
                  "Wrong try: The tens card goes first. Then the ones card.",
                  "Wrong try: Numbers 1 to 19 are one card. Do not join two cards.",
                  "Wrong try: The dash is not a letter. Count only the letters.",
                  "Wrong try: Forty is spelled f, o, r, t, y. It has 5 letters, not 6.",
                  "Wrong try: That count is not right. Tap each letter once, then add the letters of both cards.",
                  "Tone: a soft chime and 'Well done.' before each right reason. 'Not yet, try again.' before each wrong "
                  "reason. No buzzer, no red cross, no score."],
        done_when="The child has made the practice numbers, laid Forty and Three and Seventeen, made a number for "
                  "the practice roll number and at least three more numbers, and typed the letter count each time.",
        shared_state=["card_row", "letter_count", "my_roll_number"],
        hints=["Look at the cards. Which card is the tens card?",
               "Lay the tens card first. Then lay the ones card.",
               "Numbers 1 to 19 use one card. Count the letters on every card.",
               "Tap each letter once. Then add the letters of both cards."],
        visuals=["number_card", "number_name_row", "teji", "jojo", "answer_blank"]),

    # Tool 6: C7 (numbers whose names have the same letter count) with C8 (longest names, riddles, own puzzles).
    "number_puzzles": T(
        "tool_number_name_puzzles", "Number Name Puzzles", 6,
        "Students use the letter counts of number names to find numbers between 1 and 99 "
        "and notice what same-count names share.",
        screen="Same frame as every tool (step dots, Hint, Reset, Back, Next; no score, no timer). One board for every "
               "puzzle. The 27 number cards are always in view, so every name can be read and counted. The child lays "
               "one or two cards on the board; a letter strip shows the letters and the count, and a pink name bar "
               "and a green-outlined circle show the number. Teji and Jojo hold the clue in a speech bubble that "
               "changes with each puzzle. "
               "PHASE 1, get ready: the book's own first line, 'Teji and Jojo made the number 56 (fifty-six). It has 8 "
               "letters.' Fifty and Six sit on the board and the letter strip shows 5 + 3 = 8. "
               "PHASE 2, play: a practice clue of the plan's own, labelled Practice: 'Make a number with 9 "
               "letters.' The child lays cards until the count shows 9. "
               "PHASE 3, the book's puzzles, one after another. Every answer is a number the child lays on the "
               "board and drags, as one laid number, into an answer row or box. (1) Other numbers between 1 and 99 "
               "with 8 letters: five empty rows below the book's own first row (42); the child lays cards and, when "
               "the count shows 8, drags the laid number into an empty row. At the end the cards of the numbers "
               "found sit side by side so the child can see what is the same. (2) The numbers with the longest "
               "name: three rows, filled the same way. (3) The first Find out riddle: two words, the first of 6 "
               "letters, the second of 5, very near to 100; the child drags the laid number into the answer box. "
               "(4) The second Find out riddle: a strip of the numbers 63 to 78; the child taps a number to count "
               "its letters, then drags the number with the fewest letters into the answer box. (5) The child "
               "makes a puzzle of their own: they pick two numbers for 'from' and 'to' and the word longest or "
               "shortest with Pick a clue, and the tool shows the answer so the child can check that a number "
               "fits.",
        controls=["Drag a card or a laid number", "Tap a number to count its letters", "Pick a clue", "Reset"],
        instruction="Lay cards to make a number. Count its letters. Check the clue.",
        feedback=["Right try: Fifty has 5 letters and Six has 3. 5 + 3 = 8 letters.",
                  "Right try: These cards have 8 letters, so the number fits the clue.",
                  "Right try: Ninety-three, ninety-seven and ninety-eight each fit. More than one number can fit.",
                  "Right try: Seventy has 7 letters, the fewest from 63 to 78.",
                  "Wrong try: Ninety-nine has 6 + 4 = 10 letters. A bigger number can have a shorter name.",
                  "Wrong try: Twenty-three has the right letters, but it is not near to 100.",
                  "Wrong try: Sixty-three is the smallest number, but it has 10 letters. Smallest here means the "
                  "fewest letters.",
                  "Wrong try: That name has more or fewer letters than the clue. Count again.",
                  "Tone: a soft chime and 'Well done.' before each right reason. 'Not yet, try again.' before each wrong "
                  "reason. No buzzer, no red cross, no score."],
        done_when="The child has made a number with 9 letters, found other numbers with 8 letters and the numbers "
                  "with the longest name, answered both riddles, and made a puzzle of their own that checks.",
        shared_state=["card_row", "letter_count", "found_numbers"],
        hints=["Read the clue first. What does it say about the letters?",
               "Try a number. Lay its cards and count the letters.",
               "Count the letters on each card, then add them. The dash is not a letter.",
               "Lay the tens card first, then the ones card. Keep numbers whose count fits the clue."],
        visuals=["number_card", "number_name_row", "answer_blank", "teji", "jojo", "speech_bubble"]),

    # Tool 7: C10 (group things by a rule) with C11 (another way to group the same things), the book's own pair.
    "group_two_ways": T(
        "tool_group_the_cards_two_ways", "Group the Cards Two Ways", 7,
        "Students put things into two groups by a rule, say what is common in a group, and regroup them another way.",
        screen="Same frame as every tool (step dots, Hint, Reset, Back, Next; no score, no timer). Large cards and two "
               "big dotted boxes. Two rounds, one for each set of cards. "
               "PHASE 1, get ready: Teji stands beside a heap of ten picture cards with no names on them, and her "
               "two boxes, labelled 'Those that eat food' and 'Those that don't eat food', the words of the story. "
               "PHASE 2, play, round 1: with the line 'Put each card in Teji's group.' the child drags each of the "
               "ten picture cards into the box of Teji's rule where it fits. A card in the wrong box slides back with a reason, and a card in the right box "
               "settles in. When all ten are placed, the same cards move into two other boxes with no labels: Jojo's "
               "groups. "
               "PHASE 3, the book's questions, one after another. (1) Jojo's groups: for each group the child taps "
               "what is common from four rule cards (Things that fly, Things that do not fly, Things that eat food, "
               "Things with wings). Round 2: (2) the eight household cards (TV, Chair, Lamp, Bed, Clock, Fan, "
               "Pillow, Blanket) go into two note-pad panels labelled 'Things that need electricity' and 'Things "
               "that don't need electricity'. (3) The same eight cards go into two panels with no labels, grouped "
               "another way. Then four rule cards show (Things we use for sleeping, Things that need electricity, "
               "Things that fly, Things that eat food) and the child taps the rule card that tells why the two "
               "groups differ. Check my groups passes only when every card is in one group, the groups are not "
               "the electricity groups, and the tapped rule card fits the two groups (the plan's rule: Bed, "
               "Pillow and Blanket against the other five).",
        controls=["Drag a card into a group", "Tap the rule that fits", "Check my groups", "Reset"],
        instruction="Use the rule to put each card in a group. Every card goes in one.",
        feedback=["Right try: A fish eats food, so it goes with those that eat food.",
                  "Right try: The first group has things that fly. The second group has things that do not.",
                  "Right try: A TV needs electricity, so it goes in that group.",
                  "Right try: The lamp is an electric table lamp. The clock runs on electricity, from a battery "
                  "or the plug.",
                  "Right try: Same cards, new groups. Both ways are fine.",
                  "Right try: Things we use for sleeping fits Bed, Pillow and Blanket. The other five are not for sleeping.",
                  "Wrong try: A book does not eat food. Try the other group.",
                  "Wrong try: A kite does not eat food, so that is not the rule. Look at what all five do.",
                  "Wrong try: A kite has no wings, so wings is not the rule. Look at what all five do.",
                  "Wrong try: One card is still outside. Every card goes in one group.",
                  "Wrong try: These are the same groups as before. Pick a new rule.",
                  "Wrong try: Things that need electricity gives the same groups as before. Pick a new rule.",
                  "Wrong try: No household card flies or eats food. That rule does not fit.",
                  "Wrong try: That rule does not fit your two groups. Look at what the cards in one group share.",
                  "Tone: a soft chime and 'Well done.' before each right reason. 'Not yet, try again.' before each wrong "
                  "reason. No buzzer, no red cross, no score."],
        done_when="The child has grouped the ten picture cards by Teji's rule, tapped the rule of Jojo's groups, "
                  "grouped the eight household cards by electricity, and grouped them a second way with every card "
                  "in one group and the matching rule card tapped.",
        shared_state=["picture_groups", "household_groups"],
        hints=["Look at the card. What is it? What can it do?",
               "A rule tells which cards belong together. Check the card against the rule.",
               "Does this card fit the rule? If yes, use that group. If no, use the other group.",
               "Drag the card into the group where it fits. Every card goes in one group."],
        visuals=["picture_card", "household_card", "group_box", "teji", "jojo"]),
}

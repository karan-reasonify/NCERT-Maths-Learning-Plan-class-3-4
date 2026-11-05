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
    "grade": 3,                      # same as chapter.config.json "grade"
    "label": "Class 3",
    "chapter_no": 1,                 # same as chapter.config.json "chapter_no"
    "name": "What's in a Name?",     # same as chapter.config.json "chapter_name"
    "book": "NCERT Maths Mela",
    "source_pdf": "textbooks/class3/cemm101.pdf",
}
CHAPTER_NAME = CHAPTER["name"]

# ---------------------------------------------------------------------------
# modules: (module_id, module_name, summary), the top level of the hierarchy. Short; the child sees them.
# ---------------------------------------------------------------------------
MODULES = [
    ("M1", "Keeping Count with Marks", "Deba and Deep keep track of their cows with marks. You try it too."),
    ("M2", "Names and Their Letters", "Count the letters in names of animals, friends, numbers and places."),
    ("M3", "Grouping Things", "Put things into two groups by a rule. Then group them another way."),
    ("MLAST", "Chapter Review", "A short look back at marks, names and groups."),
]

# ---------------------------------------------------------------------------
# the chapter's story: ONE thread that the hook starts and every concept video continues. Characters, setting and
# objects are the BOOK's own (same people, same colours). A video's story brief may only use these characters.
# ---------------------------------------------------------------------------
STORY = {
    "thread": "Deba and Deep, two cowherds of Tarakeshwar who do not know how to count, keep track of their cows with one "
              "mark on the wall for each cow that leaves and one strike-out for each cow that comes back; then Teji, Jojo "
              "and their friends count the letters in names and in number names, and sort things into groups by a rule.",
    "setting": "the village of Tarakeshwar: a cow shed with a tiled roof and a gate, a wall and a stone slab with marks, "
               "the grazing fields; then a classroom and home: name cards, number cards, picture cards, household "
               "objects, and the hair styles of children going to school",
    # Only these are named or described as people in the book. Deba and Deep are never told apart in the pictures or the
    # text ("their friend" who gives the idea is unnamed; Hemant is named once, as "their friend Hemant", and is not drawn).
    # The unnamed children of the last page are the book's own "children in your class".
    "characters": [
        "Deba",
        "Deep",
        "their friend",
        "Hemant",
        "Mahesh",
        "Kartik",
        "Teji",
        "Jojo",
        "Mala",
        "Mala's mother",
        "the children",
    ],
}

# ---------------------------------------------------------------------------
# VISUAL_KEY: how each recurring shape or object is drawn, so it looks the same in every tool and image of the chapter.
# Tool specs and image briefs name these keys in `visuals`. Example: "ten_rod": "a tall blue bar, 10 squares".
# ---------------------------------------------------------------------------
VISUAL_KEY = {
    "tally_mark": "one short upright black bar drawn with a thick stroke on a wall or stone, one bar for each animal; on the stone slab the bars stand in groups of five side by side with no slash, four groups to a row, and the last row holds one group of five and one group of two",
    "struck_mark": "a tally bar with a slanting black line drawn across it; in the cow story picture the struck-out bars are at the top and the bars not yet struck out stand upright below them",
    "stone_slab": "a rough reddish-brown stone slab with small grey specks and one thin crack, standing on yellow sand; it carries the marks for the many cows",
    "cow_shed": "a low stone and mud shed with a red-brown tiled roof, a fence of rough wooden poles at the gate and a green bush beside it; the cows leave and re-enter through the gate",
    "cows": "cows and bullocks in white, cream, orange, red-brown and one pink-purple, with short horns and pink noses; a white cow wears a small bell on a blue strap",
    "deba_and_deep": "two cowherds with long dark curly hair, each with a tall wooden stick: one in a purple-brown robe with a dark belt and a cross strap, one in a plain ochre tunic with a brown sash and a cross strap; the book never says which is Deba and which is Deep",
    "their_friend": "a young cowherd seen from behind in a light blue shirt with a bag strap and short dark curly hair, holding a stick; the book does not name him",
    "animal_card": "a tilted white square card with a thick colour frame (red, light green, yellow, cyan, blue, magenta, lilac, pink); the animal is drawn inside and its name is written in a handwriting font along the bottom edge; the ten cards are tiger, dog, snake, goat, lion, elephant, deer, ox, rat and monkey",
    "name_big": "a child's name written large in a thin handwriting font in dark grey on white, one name under the other: Mahesh, then Kartik",
    "mahesh_kartik_boys": "two boys pointing at one white speech bubble that says 'My name is longer.': one with black curly hair in a yellow shirt with red dots, one with short black hair in an aqua shirt with a green collar; the book does not say which boy has which name",
    "number_card": "a rounded tag-shaped card with the number word in a serif font: One to Nine on peach tags, Ten to Nineteen on light blue tags, Twenty, Thirty, Forty, Fifty, Sixty, Seventy, Eighty, Ninety on light green tags (27 cards in all); a number name is made by laying the tens card first and the ones card after it, for example Forty, Three; Seventeen is one card",
    "teji": "a girl with black hair in two plaits tied with red bows, in a red dress with white dots",
    "jojo": "a boy with black curly hair in a yellow T-shirt with a blue-green band across the middle",
    "picture_card": "a tilted white square card with a thick colour frame and a plain picture with no name, used for sorting: a yellow bird, a black fly, a brown rat and a striped fish, and a blue drone, a white aeroplane, a blue mobile phone, a yellow light bulb, an orange book and a red kite",
    "household_card": "the same card style with the name in handwriting under the picture: TV (red frame), Chair (light green), Lamp (yellow), Bed (cyan), Clock (light blue), Fan (magenta), Pillow (lilac), Blanket (pink)",
    "group_box": "a rounded box with a dotted outline that holds the cards of one group; a writing group is a note-pad panel with spiral rings down its left edge and a coloured tab on top: lilac with the labels Things that need electricity and Things that don't need electricity, or pale green with blue tabs and no labels",
    "answer_blank": "a dotted line or a pale yellow rounded box for the child's answer; on the number hunt, a pink bar for the number name and a green-outlined circle for the numeral",
    "tick_and_cross": "a round green badge with a white tick, and a round green badge with a white cross",
    "place_sign": "a yellow signboard with black letters in more than one script and in English capitals: VENKATANARASIMHARAJUVARIPETA, IB and OD",
    "mala": "a schoolgirl with brown hair in two ponytails, in a blue pinafore with a yellow satchel on her way to school",
    "mala_mother": "a woman in a green sari with a red bindi, seated, combing the hair of a small girl who sits in front of her",
    "hair_style_pictures": "six head-and-shoulder pictures in pale green table cells: one high ponytail; two long plaits with blue ribbons; short curly hair; wavy hair with a blue hair clip; short straight black hair; two low ponytails",
    "speech_bubble": "a white rounded bubble with a thin black outline and a pointed tail, serif text; the thought bubble is a pale blue cloud with 1..2.. 3...",
    # --- added by the media minimiser (step 4, CLASH 28): objects the media need and the book does not give a key for ---
    "wall_marks": "a plain mud-plastered wall beside the cow shed gate, with one short block of black upright tally bars, one bar for each cow that has gone out; a bar that has been struck out has a slanting line across it, the struck out bars at the top of the block and the upright bars below, so that each kind can be counted and told apart at a glance",
    "sheep": "a real sheep: a woolly cream-white fleece, a small dark brown face and dark legs, small ears, no horns and a short tail; clearly smaller than a cow and never drawn with a cow's smooth coat, horns or bell; in the same flat colour style as the cows, using the same shed and gate",
    "name_tag": "a plain white rectangular tag with rounded corners, a small hole and a loop of string at the top and one thin coloured edge (a different colour for each name); the name is in the same thin dark grey handwriting font as the animal cards, with a capital first letter, large enough to read each letter; not the tilted square animal card, which has a thick frame and a picture",
    "start_end_marker": "a soft orange ring round the starting letter of a name and a soft blue ring round the ending letter; the same two colours on every tag, in the name tag image and on Tool 4; no ring on a letter in the middle; not green, which belongs to the tick and cross",
    "number_name_row": "a number name laid out as in the book: the tens card first and the ones card after it, side by side with a small gap and no dash or plus sign between them (Forty, Three); a number from 1 to 19 is one card by itself (Seventeen); the cards keep their own colours (peach ones, light blue teens, light green tens) so the tens card and the ones card can be told apart",
    "class_children": "children of one class in school clothes, ten to fifteen of them, each drawn from the chest up facing the viewer with the hair fully visible, none hidden behind another and spaced so that each child can be counted; every child has exactly one of the six hair styles of hair_style_pictures, in the same drawing style; the plan's own class, not the child's own class",
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
NCERT_ITEMS = [
    ("opening", "text"),
    # first page: the cowherds and the marks on the wall
    ("ch1.story1", "talk"),
    ("ch1.rule1", "text"),
    ("ch1.story2", "prompt"),
    # second page: many more cows, the missing cows, Hemant
    ("ch1.wall1", "text"),
    ("ch1.fill1", "prompt"),
    ("ch1.story3", "text"),
    ("ch1.story4", "prompt"),
    ("ch1.fill2", "prompt"),
    ("ch1.found1", "text"),
    ("ch1.hemant1", "exercise"),
    ("ch1.tnote1", "talk"),
    # third page: Let us Do 1 and 2 (animal captains, Mahesh and Kartik)
    ("ch1.letus1", "exercise"),
    ("ch1.longer1", "prompt"),
    ("ch1.letus2", "exercise"),
    # fourth page: Let us Do 3 (friends' names), parts a to f
    ("ch1.letus3", "exercise"),
    ("ch1.letus3a", "exercise"),
    ("ch1.letus3b", "exercise"),
    ("ch1.letus3c", "exercise"),
    ("ch1.letus3d", "exercise"),
    ("ch1.letus3e", "exercise"),
    ("ch1.letus3f", "exercise"),
    ("ch1.tnote2", "talk"),
    # fifth page: Let us Do 4 (number cards), Let us Think (8 letters)
    ("ch1.cards1", "text"),
    ("ch1.example1", "example"),
    ("ch1.fill3", "prompt"),
    ("ch1.letus4a", "exercise"),
    ("ch1.letus4b", "exercise"),
    ("ch1.example2", "example"),
    ("ch1.think1", "exercise"),
    ("ch1.tnote3", "talk"),
    # sixth page: the second Let us Do (numbered 1 to 4 again): longest number names, Find out riddles, place names
    ("ch1.letus5", "exercise"),
    ("ch1.letus6a", "exercise"),
    ("ch1.letus6b", "exercise"),
    ("ch1.letus7", "exercise"),
    ("ch1.place1", "text"),
    ("ch1.place2", "text"),
    ("ch1.group1", "text"),
    # seventh page: Jojo's groups, household objects
    ("ch1.jojo1", "prompt"),
    ("ch1.letus8", "exercise"),
    # eighth page: group differently, Hair Styles
    ("ch1.letus9", "exercise"),
    ("ch1.tnote4", "talk"),
    ("ch1.letus10", "exercise"),
]

# ---------------------------------------------------------------------------
# misconceptions this chapter targets: (id, one-sentence description of the wrong idea).
# ---------------------------------------------------------------------------
MISCONCEPTIONS = [
    ("M_MARK_1", "You must know number names before you can tell whether any animal is missing."),
    ("M_MARK_2", "The marks still left on the wall are the animals that came back, not the animals still out."),
    ("M_NAME_1", "A name that looks wider when it is written has more letters, so it is the longer name."),
    ("M_NAME_2", "Of two names one must always be longer, so two names cannot have the same number of letters."),
    ("M_NUM_1", "A bigger number has a longer number name, so 99 has the longest name."),
    ("M_NUM_2", "The dash between the two parts of a number name is a letter, so forty-two has 9 letters."),
    ("M_NUM_3", "Forty is spelled like four, with a u, so it has 6 letters."),
    ("M_NUM_4", "A teen number name is two cards put together, so Seventeen is Seven and Ten, with 8 letters."),
    ("M_NUM_5", "Number cards can go in any order, so Three then Forty makes 43."),
    ("M_PUZ_1", "In 63 to 78 the smallest number name belongs to the smallest number, 63, and not to the name with the fewest letters."),
    ("M_PUZ_2", "A riddle or a question has one answer, so you stop when one number fits."),
    ("M_GRP_1", "There is only one right way to group a set of things."),
    ("M_GRP_2", "An object that does not fit can stay out of both groups."),
    ("M_GRP_3", "Things can be grouped only by how they look, not by what they do or need."),
]

# ---------------------------------------------------------------------------
# CLASHES: judgement calls and conflicts the user must decide, one string each (shown in the structure report):
# a tool with no matching concept, a concept with no NCERT question, an approved tool the book does not support,
# a teacher instruction against a hard rule. Empty means none. Never settle one silently.
# ---------------------------------------------------------------------------
CLASHES = [
    # --- written by the tool mapper (step 2). Each is a question for the user; none is settled here. ---
    "CLASH 1, the whole tool table is a PROPOSAL of the pipeline, not the content team's table. "
    "NOTE SAYS: no content-team table existed for this chapter. The user's brief says 'If no approved tool sequence "
    "exists, propose one based on the textbook's natural learning progression', and the user chose 'propose fresh "
    "from the book'. The 7 tools below are in tool_map.md, are locked in chapter.config.json approved_tools "
    "(core/tool_map.py verify prints a match) and are mapped in tool_map.locked.md without any change of name, "
    "purpose or order. They follow the book's own order of ideas (marks, names, number names, groups). "
    "(1) Marks at the Gate: The child makes one mark for each cow that leaves the gate and strikes one out for each "
    "cow that comes back, then sees whether any cow is missing. "
    "(2) Marks for a Big Herd: The child strikes out one mark for each cow that comes home, reads the marks left to "
    "find the cows still out and the cows back, then makes separate marks for cows and sheep. "
    "(3) Longest and Shortest Name: The child counts the letters of each name and picks the longest and the "
    "shortest name, for the animal cards, for Mahesh and Kartik, and for friends' names. "
    "(4) Starting and Ending Letters: The child drops name tags into piles by their starting letter or by their "
    "ending letter and counts each pile to see which letter is used most. "
    "(5) Build a Number Name: The child lays a tens card and a ones card together to make a number name, as Teji "
    "does for 43, and counts its letters. "
    "(6) Number Name Puzzles: The child finds numbers between 1 and 99 from clues about the letters in their names "
    "(8 letters, the longest name, the riddles) and notices what same-count names share. "
    "(7) Group the Cards Two Ways: The child drags cards into two groups by a rule, finds the rule in Jojo's groups, "
    "then regroups the same cards another way so every card is in one group. "
    "OPTIONS: (a) approve the table as proposed; (b) change names, purposes or order (the table is then locked "
    "again and every step after it is redone); (c) send the content team's own table, which replaces this "
    "proposal. "
    "RECOMMENDATION: (a) approve. Every clash below is a question about this proposal, and the user's approval of "
    "the structure approves the table.",

    "CLASH 2, Tool 1 (Marks at the Gate): the exploration tool carries one book question and the opening "
    "situation. "
    "NOTE SAYS: the child makes one mark for each cow that leaves the gate, strikes one out for each cow that comes "
    "back, then sees whether any cow is missing; it sits right after the hook video, before any video names the "
    "idea. "
    "BOOK SAYS: the friend's idea (one mark on the wall for each cow that leaves, one struck out for each cow that "
    "re-enters) is printed on the first page BEFORE the question 'Did all the cows come back home?' (ch1.story2), "
    "and the answer is printed just above it ('all the marks were struck out when they came back home'). "
    "ch1.story1 'What could Deba and Deep do?' is a talk prompt, not a question. The gate lets an exploration tool "
    "hold book questions (up to the cap) and up to 3 notice prompts, and requires neither. So on Tool 1 the "
    "friend's rule can only be given as the task ('Make a mark for each cow that goes out'); what the child "
    "discovers is that struck-out marks tell whether a cow is missing. The tool must not need number names "
    "(M_MARK_1). "
    "OPTIONS: (a) ch1.story2 sits on Tool 1 with 3 notice prompts: the child does the marks, then answers the "
    "book's own question from what the tool showed; (b) Tool 1 holds the notice prompts only and ch1.story2 stays "
    "in the teaching text of the next video (28 questions on tools, ch1.story2 a teaching line). "
    "RECOMMENDATION: (a). The question is the 'then sees whether any cow is missing' of the purpose, and nothing "
    "else in the chapter practises C1."
    " QUESTION MAPPER: option (a) is kept. ch1.story2 'Did all the cows come back home?' is the one book question on "
    "Tool 1 (T1.C2), beside the tool's 3 notice prompts. The friend's rule (ch1.rule1) stays the task text of T1.C2. "
    "The answer is labelled 'From the picture': yes, all the marks were struck out, so no cow was missing (the book's "
    "own sentence above the question).",

    "CLASH 3, C1 (a mark for each animal) has no concept video of its own. "
    "NOTE SAYS: tool_map.md row 3 puts ONE concept video after Tool 1 that names the friend's idea (C1) and goes on "
    "to the marks left on the wall (C2); Tool 2 follows that video. "
    "FLOW RULES SAY: the concept video explains the concept just explored (rule 3), the matching tool applies that "
    "exact concept (rule 4), and a concept video holds ONE new_idea (gate flow: 'a concept video explains one named "
    "concept'). "
    "BOOK SAYS: the friend's idea is one sentence on the first page and Tool 1 already does it; C2 starts at the "
    "top of the second page (the 47 marks, two left). "
    "OPTIONS: (a) as proposed: video 1 is one story with ONE new_idea (C2: the marks left are the cows still out) "
    "and names the friend's idea in its opening lines, so C1 is explored on Tool 1 and named in video 1; (b) a "
    "separate short video for C1 with no tool after it (Tool 1 already did the doing), then a second video for C2 "
    "before Tool 2: 6 concept videos instead of 5; (c) no video for C2 and Tool 2 follows an image: not "
    "recommended, C2 needs the story of the two worried cowherds. "
    "RECOMMENDATION: (a).",

    "CLASH 4, Tool 2 (Marks for a Big Herd): one tool for C2 (read the marks) and C3 (marks for two kinds). "
    "NOTE SAYS: the child strikes out one mark for each cow that comes home, reads the marks left to find the cows "
    "still out and the cows back, then makes separate marks for cows and sheep. "
    "BOOK SAYS: C2 is the 47 marks on the stone slab, two marks left, 'How many cows had reached home?' "
    "(ch1.fill1, ch1.story4, ch1.fill2); C3 is one empty box: 'Help Hemant keep track of his cows and sheep by "
    "making marks like Deba and Deep' (ch1.hemant1: 36 cows and 23 sheep, 59 marks in all), and the Teacher's Note "
    "joins the two ('different strategies to count large groups of objects without using numbers'). The book "
    "draws no sheep and does not draw Hemant. One tool with two parts could ask for 47 or 59 taps, which is long "
    "for a child of 8 to 9. "
    "OPTIONS: (a) one tool, two parts (read, then make), with a short path: a group of five marks is made or struck "
    "out with one tap, and the sheep are drawn as real sheep (a real-life example that shows the animal "
    "correctly, a new visual key); (b) split Hemant's task into its own tool with an image before it: 8 tools, "
    "the table changes and every later tool is renumbered. "
    "RECOMMENDATION: (a). The pair is the book's own and C3 is the same skill with two kinds kept apart. The "
    "user decides."
    " QUESTION MAPPER: Tool 2 (T2.C2) holds 4 questions in the book's order: ch1.fill1 (47 cows), ch1.story4, "
    "ch1.fill2 (45 cows) and ch1.hemant1 (36 cows and 23 sheep), 4 of 6. The 47 is checked again on the page image: 5 "
    "+ 5 + 5 + 5 = 20 in each of two full rows, then a group of 5 and a group of 2 (5 + 2 = 7), so 20 + 20 + 7 = 47, "
    "and 47 − 2 = 45. ch1.hemant1 has a 'Sample answer' (36 marks and 23 marks kept apart, 36 + 23 = 59 in all), "
    "because the book accepts different ways (the Teacher's Note, CLASH 16).",

    "CLASH 5, Tools 3 and 4: ch1.letus3 (write the friends' names) and ch1.letus3a (tick the longest, cross the "
    "shortest) are homed on Tool 3, not on Tool 4. "
    "NOTE SAYS: Tool 3 counts the letters of names and picks the longest and the shortest, 'for friends' names'; "
    "Tool 4 piles name tags by starting or ending letter. "
    "BOOK SAYS: Let us Do 3 is ONE activity (write the names, then parts a to f), and analysis.md homes letus3 and "
    "letus3a with C5. With them Tool 4 would hold 7 questions against the cap of 6 (max_tool_questions in "
    "chapter.config.json: a config default, not a curriculum rule). letus3a is about the longest and the "
    "shortest name, the idea of Tool 3 (analysis.md itself marks it 'C5 (uses C4)'). Moved, Tool 3 holds 5 and "
    "Tool 4 holds 5. Cost: one book activity is split over two tools; the names written on Tool 3 are the names "
    "sorted on Tool 4, and Tool 4's parts b to f refer to names the child met on Tool 3. "
    "OPTIONS: (a) as proposed: letus3 and letus3a on Tool 3, letus3b to letus3f on Tool 4; (b) keep all of Let us "
    "Do 3 on Tool 4 (7 questions, Tool 3 holds 3) and raise max_tool_questions to 7 for this chapter, with the "
    "user's say-so (the cap was raised for Class 3 Chapter 2 in the same way). "
    "RECOMMENDATION: (a): it keeps the cap and puts the tick and cross where the longest and shortest are "
    "taught."
    " QUESTION MAPPER: option (a) is kept. Tool 3 (T3.C2) holds ch1.letus1, ch1.longer1, ch1.letus2, ch1.letus3 and "
    "ch1.letus3a (5 of 6). Tool 4 (T4.C2) holds ch1.letus3b to ch1.letus3f (5 of 6). ch1.letus3 and ch1.letus3a are "
    "the two stretches: the analysis gave them to C5. The names written on Tool 3 are the eight practice names of "
    "CLASH 14, and the answers of Tool 4 use the same eight.",

    "CLASH 6, Tool 3 (Longest and Shortest Name): Mahesh and Kartik. "
    "NOTE SAYS: the child counts the letters of each name and 'picks the longest and the shortest name, for the "
    "animal cards, for Mahesh and Kartik, and for friends' names'. "
    "BOOK SAYS: ch1.letus2 'Who has a longer name? Discuss.' with Mahesh and Kartik. Both have 6 letters, so by the "
    "book's own rule (the longest name has the most letters, ch1.letus1) neither is longer, and with only two "
    "names there is no longest and no shortest. In the thin handwriting of the book Mahesh looks wider (the trap "
    "M_NAME_1). The book prints no answer. For the ten animals the answer is one name each way (elephant, 8 "
    "letters; ox, 2 letters). For the eight sample names of clash 14 the longest are three names (Hemant, Mahesh, "
    "Kartik, 6 letters each) and the shortest are five (Deba, Deep, Teji, Jojo, Mala, 4 letters each): the "
    "'name(s)' of ch1.letus3a fits this. "
    "OPTIONS: (a) keep the purpose: on Tool 3 the two boys' names are counted and the tool shows 'the same number "
    "of letters, neither is longer', and a name that only looks wider is shown not to be longer; the answer to "
    "ch1.letus2 is stated by the plan and labelled 'From the picture'; (b) drop Mahesh and Kartik from Tool 3 and "
    "leave them to the concept video: this changes the proposed purpose. "
    "RECOMMENDATION: (a). The answer is a count anyone can check (Mahesh 6, Kartik 6) and it teaches that two "
    "names can have the same number of letters (M_NAME_2). The user says yes or no to stating the tie as the "
    "answer."
    " QUESTION MAPPER: recommendation (a) is used in ch1.letus2. The answer begins 'From the picture': Mahesh has 6 "
    "letters, Kartik has 6 letters, the two names are the same length and neither is longer. A step says a name that "
    "looks wider is not a longer name (M_NAME_1).",

    "CLASH 7, Tool 4 (Starting and Ending Letters): the weakest tool of the table, and it follows an image, not a "
    "video. "
    "NOTE SAYS: the child drops name tags into piles by their starting letter or by their ending letter and counts "
    "each pile to see which letter is used most; tool_map.md row 7 puts an image of name tags in a row before it, "
    "no video. "
    "BOOK SAYS: C5 is five small questions (ch1.letus3b to ch1.letus3f: the starting letter of your name, names "
    "with the same starting letter, the most used starting letter, names with the same ending letter, the letters "
    "that start no name); the book explains nothing about starting or ending letters and has no name tags (only "
    "dotted name lines). Four weaknesses: (1) the idea is small (first letter, last letter); (2) it follows an "
    "image, so the rule 'concept video, then tool' is met by an image concept: the gate accepts an image or a "
    "video before a tool, but the rule text says 'after the concept video'; (3) dragging cards into piles is also "
    "what Tool 7 does (brief section 7: do not repeat the same interaction across tools without a learning "
    "reason; here the reasons differ: piles by a letter and counted, against groups by a rule the child finds); "
    "(4) name tags and the ending-letter idea are the plan's own. "
    "OPTIONS: (a) keep Tool 4 as proposed; (b) drop the tool and make C5 one image with its five questions on the "
    "image (the gate allows book questions on an image concept when no tool follows it, see clash 13): this "
    "removes a tool, so the table changes to 6 tools and Tools 5 to 7 are renumbered; (c) keep the tool and put "
    "a short concept video before it instead of the image (6 concept videos, one image fewer). "
    "RECOMMENDATION: (a). The book's questions 3d and 3f are easier with piles, and the tool is small. The user "
    "decides, since (b) and (c) change the table or the media."
    " QUESTION MAPPER: Tool 4 (T4.C2) follows the image T4.C1 and holds 5 questions, ch1.letus3b to ch1.letus3f. Each "
    "is answered with the eight practice names, so no question needed an invented name tag.",

    "CLASH 8, Tool 6 (Number Name Puzzles): one tool for C7 and C8, holding the full 6 questions. "
    "NOTE SAYS: the child finds numbers between 1 and 99 from clues about the letters in their names (8 letters, "
    "the longest name, the riddles) and notices what same-count names share. "
    "BOOK SAYS: C7 is the 8 letter hunt (ch1.example2, ch1.think1) and the Teacher's Note 'observe what is "
    "common'; C8 is the longest number name (ch1.letus5), the two Find out riddles (ch1.letus6a, ch1.letus6b) and "
    "'Make similar puzzles of your own in your notebook and ask your classmates' (ch1.letus7). The tool holds "
    "exactly 6 book questions (the cap, none to spare). For a child of 8 to 9 a hunt, a longest name search, two "
    "riddles and an own puzzle are many steps (the brief: avoid complicated multi-step tasks), and ch1.letus7 is "
    "a notebook task for classmates, which a tool can only copy as 'make a clue for a number and test it'. "
    "OPTIONS: (a) one tool as proposed, with a short path (the 27 number cards shown so that every name can be read "
    "and counted); (b) split into two tools (C7 the hunt; C8 the longest name, the riddles, the own puzzles): 8 "
    "tools, every later tool renumbered, and a video or image before the new tool, so the table changes; (c) "
    "keep one tool and move ch1.letus7 to the closing line of the concept video (the tool holds 5; the book's "
    "question is no longer on a tool). "
    "RECOMMENDATION: (a). The same hunt with other clues is one idea, and a second tool would repeat it (brief "
    "section 7). The user decides about the split and about ch1.letus7."
    " QUESTION MAPPER: Tool 6 (T6.C2) holds exactly 6: ch1.example2, ch1.think1, ch1.letus5, ch1.letus6a, ch1.letus6b "
    "and ch1.letus7 (at the cap, none to spare, none moved). ch1.letus7 keeps the book's words and its steps are "
    "'pick numbers, write a clue, check it'. Its sample answer is a puzzle of the plan's own: the numbers 20 to 25, "
    "the longest name, answer 23 (twenty-three, 11 letters). It uses none of Tool 6's other answers.",

    "CLASH 9, Tool 6: printed-book errors and open clues that change what the tool shows (all from analysis.md "
    "section 6). "
    "(a) The stem of Q2 on pdf 6 repeats the stem of Q1 ('Write the number(s) between 1 and 99 that have the longest "
    "name'), but Q2 holds two Find out riddles that do not ask for the longest name (ch1.letus6a). "
    "(b) Riddle 1 ('two words; the first word has 6 letters, the second 5; I am very near to 100') fits 93, 97 and "
    "98 below 100 (and 23, 27, 28, 33, 37, 38, 83, 87, 88 by the letters alone); the book asks 'Who am I?' as if "
    "there were one. "
    "(c) Riddle 2 ('the numbers from 63 to 78; My number name is the smallest among all my friends'): the intended "
    "answer is the shortest name, seventy (70, 7 letters); 'smallest' can also mean the smallest number, 63. "
    "(d) 13 numbers between 1 and 99 have 8 letters (13, 14, 18, 19, 41, 42, 46, 51, 52, 56, 61, 62, 66); the book "
    "shows 56 and 42 and gives room for 5 more, and prints no answer to 'what is common'. The longest number "
    "names are 73, 77 and 78 (12 letters). "
    "OPTIONS: (a) the Q2 stem: keep as printed, or show only the two Find out boxes; (b) riddle 1: accept 93, 97 "
    "and 98, or only 97 and 98; (c) riddle 2: accept 70 and say in the feedback that 'smallest' means the fewest "
    "letters; (d) accept any of the 13 numbers and show a 'what is common' answer from the plan (each is a "
    "5-letter tens word with a 3-letter ones word: forty, fifty or sixty with one, two or six; or 13, 14, 18, 19), "
    "labelled 'Sample answer'. "
    "RECOMMENDATION: (a) show only the two Find out boxes (the stem looks like a copy slip); (b) accept 93, 97 and "
    "98 and say that each fits, because 'very near' does not choose one; (c) as stated; (d) as stated. The "
    "user decides."
    " QUESTION MAPPER: (a) done: ch1.letus6a shows only the Find out box, the repeated stem is not shown (CLASH 29). "
    "(b) done: the answer accepts ninety-three, ninety-seven and ninety-eight and says each one fits, and a step says "
    "more than one number may fit (M_PUZ_2). (c) done: a step says 'smallest' means the fewest letters, the answer is "
    "70 (seventy, 7 letters) and adds that sixty-three, the smallest number, has 10 letters (M_PUZ_1). (d) done in "
    "ch1.think1: a 'Sample answer' with five of the 13 numbers and the list of all 13, and two steps that show what "
    "is common (forty, fifty and sixty have 5 letters, one, two and six have 3, and 5 + 3 = 8; the teens are one card "
    "each). ch1.letus5 answers 73, 77 and 78 (12 letters each) and a step shows that ninety-nine has only 6 + 4 = 10.",

    "CLASH 10, Tool 7 (Group the Cards Two Ways): one tool for C10 and C11, and the printed ambiguities of its "
    "questions. "
    "NOTE SAYS: the child drags cards into two groups by a rule, finds the rule in Jojo's groups, then regroups the "
    "same cards another way so every card is in one group. "
    "BOOK SAYS: Teji's ten picture cards go into 'those that eat food' and 'those that don't eat food'; Jojo "
    "'arranged the same cards differently' and ch1.jojo1 asks 'What is common in each groups Jojo has made?' (the "
    "rule is not printed; from the picture it is things that fly: kite, aeroplane, bird, fly, drone, against mobile "
    "phone, fish, light bulb, book, rat); ch1.letus8 puts the eight household cards into 'Things that need "
    "electricity' and 'Things that don't need electricity' (four lines each); ch1.letus9 says 'Group the given "
    "objects differently' (two unlabelled panels). The Teacher's Note names both C10 and C11. Printed problems: "
    "'each groups' (grammar); a wall clock may run on a battery and a lamp may be an oil lamp (ch1.letus8); 'the "
    "given objects' of ch1.letus9 is not said (the eight household objects fit its four and four lines, the ten "
    "picture cards would need five each); Teji's grouping is split across a page turn. "
    "OPTIONS: (a) one tool with two rounds as proposed (round 1 Teji's cards and the electricity cards; round 2 "
    "Jojo's rule and the regrouping); (b) two tools: 8 tools, the table changes. Printed items: ch1.letus8 accept "
    "TV, Lamp, Clock, Fan against Chair, Bed, Pillow, Blanket, or also accept a battery clock as 'does not need "
    "electricity'; ch1.letus9 read as the eight household objects; ch1.jojo1 keep the grammar as printed or "
    "write 'group'. "
    "RECOMMENDATION: (a); the book's four and four, with the feedback saying that a clock runs on electricity from "
    "a battery or from the plug; 'the given objects' as the eight household objects; the rule of Jojo's groups "
    "labelled 'From the picture'; the wording of ch1.jojo1 kept as printed."
    " QUESTION MAPPER: Tool 7 (T7.C2) holds ch1.jojo1, ch1.letus8 and ch1.letus9 (3 of 6), in the book's order: find "
    "Jojo's rule, sort the household objects, then regroup them. The two rounds of option (a) are for the brief "
    "writer's play phase. On screen (CLASH 29): 'each group' (not 'each groups') and 'the eight household objects' "
    "(not 'the given objects'). Answers: ch1.jojo1 'From the picture': things that fly against things that do not fly "
    "(the rule is the plan's reading, the book prints none). ch1.letus8 'From the picture', four and four, the lamp "
    "read as an electric table lamp and the clock as running on electricity from a battery or the plug. ch1.letus9 "
    "'Sample answer', grouped by sleeping (Bed, Pillow, Blanket against TV, Chair, Lamp, Clock, Fan), a rule "
    "different from electricity.",

    "CLASH 11, printed-book items that change what Tools 2 to 5 show (analysis.md section 6). "
    "(a) Tool 2: ch1.fill1 depends on a picture count (47 marks: 20 + 20 + 7, in groups of five, counted by eye "
    "and by program at 250 dpi); a child who counts differently gets another answer to ch1.fill2 (47 minus 2 "
    "= 45). "
    "(b) Tool 3: ch1.letus1 says 'Some animals and birds' but all ten cards are animals (no bird among them). "
    "(c) Tool 4: ch1.letus3e 'Count the names with the same ending letter' does not say the same as what (part c "
    "says 'as yours'); ties for 'the most used' starting letter are not covered; whether the child's own name is "
    "among the eight lines is not said. "
    "(d) Tool 5: ch1.letus4a points to number cards 'at the end of the book', which are not in the chapter file; "
    "the page shows all 27 cards. "
    "OPTIONS: (a) 47 as drawn, the groups of five visible, and the child's count checked against it; (b) keep "
    "'animals and birds' as printed, or write 'animals'; (c) read 3e as the same ending letter as the child's "
    "own name, like 3c, and accept a tie in 3d; (d) the 27 cards of the page stand for the end-of-book cards. "
    "RECOMMENDATION: (a) 47; (b) keep as printed (the book's own wording, and the child sees the ten cards); "
    "(c) as stated; (d) as stated. The user decides."
    " QUESTION MAPPER: (a) followed: 47, checked again on the page image. (b) NOT followed in the FIO: ch1.letus1 "
    "reads 'Some animals got together...' without 'and birds', because the ten cards hold no bird and the user's rule "
    "is that no printed error is repeated on screen (CLASH 29; one word to restore if the user prefers the printed "
    "words). (c) followed: ch1.letus3e is read as the same ending letter as the child's own name, like part c (Mala: "
    "Deba and Mala end with a; the other reading, the biggest group with one ending letter, gives the same 2 names), "
    "and the tie of D and M is said in ch1.letus3d. (d) followed: the number cards are on the screen and the sentence "
    "about the end of the book is not shown.",

    "CLASH 12, C9 (longest and shortest place names): an image-only concept with no book question, placed after "
    "Tool 6. "
    "NOTE SAYS: tool_map.md row 13 puts a real-life image of the place signboards after Tool 6 (one image, no "
    "video, no tool) and before the grouping video. "
    "BOOK SAYS: the signboards sit on the page after the number puzzles and before Teji's cards, with two facts "
    "(Venkatanarasimharajuvaripeta is the longest name, 28 letters; Ib and Od the shortest) and no question. "
    "The idea is the length of a name (C4), so it would also fit next to Tool 3. An image concept holds exactly "
    "one image and no video or tool; with no book question it holds none. "
    "OPTIONS: (a) after Tool 6, in the book's order; (b) move it next to Tool 3, where longest and shortest names "
    "are taught; (c) keep it out of the main sequence and pin it beside the concept of Tool 3 (a reference). "
    "RECOMMENDATION: (a). It follows the book, and the brief says that when no book question exists none is "
    "invented. The journey designer moves it only if the user prefers (b) or (c).",

    "CLASH 13, C12 (hair styles): an image-only concept that holds a book question. "
    "NOTE SAYS: tool_map.md row 16 puts a real-life image of children with different hair styles after Tool 7, "
    "which the child groups and counts to fill the book's table; no tool follows it. "
    "BOOK SAYS: ch1.letus10 'Let us Do. Hair Styles ... Look at the children in your class ... Look and write down' "
    "with a table of six hair-style pictures and six empty cells; the numbers come from the child's own class. "
    "GATE CHECK (gates/flow_c34.py and topics_common.A, read and run on small made-up plans): a book question MAY "
    "sit on an image-only concept. A() refuses items only on a hook and a review; flow_c34._check_questions "
    "reports a question on a story or image concept only when a tool follows it (applies_to names it): with no "
    "tool after the image it reports nothing, and with a tool after it reports 'belong on the tool that follows "
    "it'. So letus10 sits on the image as a question block, with no tool and no screen check; if a tool is ever "
    "added after the image the question must move to it. "
    "OPTIONS: (a) keep one image with letus10 on it, the class being the book's children (clash 14); (b) a third "
    "round of Tool 7 for hair styles: Tool 7's purpose is 'two groups by a rule' and the table has six hair "
    "styles, so the purpose would change; (c) a separate tool: 8 tools, the table changes. "
    "RECOMMENDATION: (a). A look-and-count task on the child's own class would only repeat the sorting of Tool 7 "
    "with made-up data. The user decides."
    " QUESTION MAPPER: ch1.letus10 is homed on the image concept T7.C3 as the one book question that sits on an image: "
    "no tool follows it, and build.py --structure prints structure stage OK with it there. If a tool is ever added "
    "after this image, the question moves to that tool. Its answer cannot hold the six counts yet: CLASH 31.",

    "CLASH 14, sample data for the child's own names, roll number and class (Tools 3, 4, 5 and the hair styles "
    "image depend on this). "
    "NOTE SAYS: Tool 3 works 'for friends' names'; Tool 4 sorts 'name tags'; Tool 5 builds a number name 'as Teji "
    "does for 43'. "
    "BOOK SAYS: ch1.letus3 (friends' names), ch1.letus3b and ch1.letus3c ('your name', 'yours'), ch1.letus4a ('your "
    "roll number'), ch1.letus4b and ch1.letus7 (the notebook, classmates) and ch1.letus10 ('your class') ask for "
    "the child's own data, which a screen cannot hold. The only names in the book are Deba, Deep, Hemant, Mahesh, "
    "Kartik, Teji, Jojo and Mala (eight, as many as the lines of letus3), and the children of the last page. With "
    "these eight names: letters 4, 4, 6, 6, 6, 4, 4, 4; the starting letters D and M TIE for 'the most used' (two "
    "names each: Deba and Deep; Mahesh and Mala); the ending letter a is shared by Deba and Mala only; the "
    "letters that start no name are A, B, C, E, F, G, I, L, N, O, P, Q, R, S, U, V, W, X, Y, Z. The book has no "
    "name tags. "
    "OPTIONS: (a) use the book's eight names as the sample friends and its children as the sample class, labelled "
    "'practice with the book's friends'; the child taps one of the eight as 'my name' for parts b, c and e; "
    "Tool 5's roll number is a number the child picks from 1 to 99 (answers 'Sample answer'); the tie is "
    "accepted and said ('D and M: two names each'); (b) choose other sample names and numbers so that no tie "
    "occurs (the names would not be the book's); (c) let the child type their own names and numbers: no sample "
    "is needed, but the tool cannot check them. "
    "RECOMMENDATION: (a). The ties are true and show that more than one letter can be 'most used'; the book's "
    "names are the only names of the chapter, and the plan uses book characters only. The user decides."
    " QUESTION MAPPER: option (a) is used. Tool 3: ch1.letus3 answers with the eight names; ch1.letus3a ticks Hemant, "
    "Mahesh and Kartik (6 letters) and crosses Deba, Deep, Teji, Jojo and Mala (4 letters). Tool 4: 'my name' is Mala "
    "for parts b, c and e (M: Mahesh and Mala, 2 names; ending a: Deba and Mala, 2 names); D and M tie in part d (2 "
    "names each, said in the answer); part f gives the 20 letters A, B, C, E, F, G, I, L, N, O, P, Q, R, S, U, V, W, "
    "X, Y, Z (26 − 6 = 20). Tool 5: the sample roll number is 29 (Twenty, Nine: 6 + 4 = 10 letters) and ch1.letus4b "
    "gives 12, 31 and 90; none is a Tool 6 answer. Each is a 'Sample answer' that ends 'Your answer may differ'.",

    "CLASH 15, the brief's 'puzzle / activity videos' and 'chapter revision with short concept checks' have no "
    "separate slot in this pipeline. "
    "BRIEF SAYS: D, puzzle or activity videos 'when the chapter contains interesting mathematical activities, "
    "puzzles'; E, chapter revision with a visual recap and 'short concept checks and application questions'. "
    "FLOW RULES SAY: only a hook video and concept videos (each a story); a review of 1 to 2 concepts with no new "
    "video or tool, no book item of its own and no new key term; questions are the book's. "
    "BOOK SAYS: the puzzles are the 8 letter hunt and the two Find out riddles (pdf 5 and 6); there is no "
    "revision or exercise at the end. "
    "HOW EXPRESSED: the puzzle video is the concept video before Tool 6, told as a story (Teji and Jojo challenge "
    "each other) with the puzzles solved on Tool 6; the review recaps with the plan's own lines and may use "
    "pinned images, and holds no checked question. "
    "OPTIONS: (a) as expressed; (b) the review also holds 1 or 2 short check lines made from the chapter's own "
    "numbers and names (the plan's own practice, not the book's: this needs the user's say-so); (c) a pinned "
    "picture recap only. "
    "RECOMMENDATION: (a).",

    "CLASH 16, the four Teacher's Notes give a teacher a role. "
    "BRIEF SAYS: 'Do not assign a teaching role to a classroom teacher.' "
    "BOOK SAYS: ch1.tnote1 (strategies to count large groups without numbers; keep track of children entering and "
    "leaving the classroom), ch1.tnote2 (mark the shortest and longest names among boys and girls and in the "
    "class), ch1.tnote3 (observe what is common in numbers with the same letter count), ch1.tnote4 (suggest more "
    "things and group them; other ways to group; every object in one group). They are talk items, not "
    "questions. "
    "OPTIONS: (a) give each idea to the child as a line (the closing line of video 1; the 'what is common' of "
    "Tool 6; the last line of Tool 7), never as a task for a teacher; the class tasks (children entering and "
    "leaving, boys and girls, suggest more things) are not done on any tool; (b) leave the notes out. "
    "RECOMMENDATION: (a). tnote3 is already inside Tool 6's purpose ('notices what same-count names share')."
    " QUESTION MAPPER: the four Teacher's Notes stay `ncert` text items (ch1.tnote1 on T2.C1, ch1.tnote2 on T4.C1, "
    "ch1.tnote3 on T6.C1, ch1.tnote4 on T7.C1). None is a question or a task for a teacher, and the class tasks they "
    "mention (children entering and leaving, boys and girls, suggest more things) are on no tool.",

    # --- written by the journey designer (step 3). New findings only; CLASH 2 to 16 are followed as recommended and marked
    # PROVISIONAL in topics_1.py. ---
    "CLASH 17, where the two image-only concepts sit in the topics, and how the topics are grouped into modules. "
    "NOTE SAYS: tool_map.md row 13 (C9 place names: one image, no video, no tool) comes after Tool 6 and before the "
    "grouping video; row 16 (C12 hair styles: one image, nothing after it) comes after Tool 7 and before the review. The "
    "user's instruction to the journey designer: group the rows into idea topics and 3 or 4 modules 'as the flow gate "
    "allows'; C9 and C12 may sit inside a neighbouring idea topic or alone. "
    "FLOW GATE SAYS (gates/flow_c34.py): an idea topic holds 1 to 6 concepts and needs a topic objective; its concepts are "
    "story, image or tool; it cannot open with a tool; a tool follows the story or image it applies to; an image concept "
    "holds exactly one image and no video or tool and may sit anywhere in an idea topic; the review must revise a concept "
    "of every idea topic. "
    "BOOK SAYS: the place signboards sit on the page of the number puzzles, straight after 'the number(s) that have the "
    "longest name'; the hair styles task comes after the grouping tasks and asks the child to group children and count "
    "each group. "
    "DONE (PROVISIONAL): T6 = puzzle story video, Tool 6, then the place names image (C9) as its LAST concept; T7 = grouping "
    "video, Tool 7, then the hair styles image (C12) as its LAST concept. Modules: M1 Keeping Count with Marks (T1, T2), "
    "M2 Names and Their Letters (T3 to T6), M3 Grouping Things (T7), then MLAST for the review: three content modules and "
    "the review module. The review revises both images. "
    "OPTIONS: (a) as done; (b) each image alone in its own one-concept idea topic (9 topics; each needs a topic objective "
    "that repeats its concept's, and the review must cover it); (c) C9 as the FIRST concept of the grouping topic (image, "
    "video, Tool 7), so that topic opens with a picture about the length of names, not about groups; (d) four content "
    "modules (marks, letters in names, number names, groups), five modules with the review. "
    "RECOMMENDATION: (a). Each image stays beside the idea it continues (the longest number name, then the longest place "
    "name; grouping things, then grouping children), no topic opens with an image about another idea, and no topic has a "
    "single thin concept. The user decides.",

    "CLASH 18, the story thread between the cowherds and the children. "
    "NOTE SAYS: the hook and concept video 1 are about Deba and Deep in Tarakeshwar; concept videos 2 to 5 (names, number "
    "names, the number puzzle, groups) are about Mahesh and Kartik, Teji and Jojo. "
    "FLOW RULES SAY: every concept video continues the chapter's story or theme and is a story, never a lecture; a story "
    "brief may use only the characters of content.STORY (the gate checks it). "
    "BOOK SAYS: after the second page the cowherds, the village and the wall never appear again. Mahesh, Kartik, Teji, Jojo "
    "and Mala are never said to live in Tarakeshwar or to know Deba and Deep; the only link between the parts is the "
    "chapter title 'What's in a Name?' (analysis.md reads it so, the book does not say it). Hemant is 'their friend' "
    "and is not drawn. So the plan needs a link that the book does not print, and the brief writer cannot make one "
    "without a decision. "
    "OPTIONS: (a) the children of videos 2 to 5 are told as friends of Deba and Deep in the same village (Deba and Deep may "
    "stand at the edge of a scene; no character is added; the setting moves to the school and the home that the book "
    "draws), and each later video opens with one line that picks up the video before it; (b) no link: each later story "
    "stands alone with the book's children and the only thread is the theme 'names and groups' (the videos then do not "
    "continue one story); (c) Deba and Deep ask the questions in every video and the children show the answers (this "
    "changes the roles the book gives them). "
    "RECOMMENDATION: (a). It uses only the book's cast and setting and keeps one thread. The user decides.",

    # --- written by the media minimiser (step 4). Every medium of the proposal is kept (hook video 1, concept videos 5,
    # images 3 all main and none pinned, tools 7); these clashes record where one medium overlaps another and what each
    # medium may and may not show. Where a line below says JUDGEMENT it is what topics_1.py already does. ---
    "CLASH 19, image C5 (T4.C1, name tags in a row) against Tool 4 (Starting and Ending Letters). "
    "NOTE SAYS: tool_map.md row 7 is a real-life picture of name tags in a row, so the child sees the first and the "
    "last letter of each name; row 8 is Tool 4, where the child drops name tags into piles. "
    "BOOK SAYS: nothing teaches starting or ending letters and the book has no name tags (only dotted name lines on "
    "pdf 4). The flow gate asks a main image that a tool follows to bring a new real-life context (new_context true) "
    "and a tool must follow a story or image concept, so this image cannot be pinned. Image and tool both show name "
    "tags: the same object twice. "
    "JUDGEMENT: the image is the only teaching before the tool, so it is kept as a main image. Its new real-life "
    "context is the place of the tags (for example a row of school bag hooks), which the tool's screen does not show. "
    "It shows three or four of the book's eight names, never two names with the same starting or ending letter (for "
    "example Teji, Jojo, Hemant), the starting letter ringed in one colour and the ending letter in another "
    "(start_end_marker). It must NOT show piles, a count, 'the most used' letter or all eight names: Tool 4 does "
    "all of that, and eight names in a row would show the tie of D and M early (CLASH 14). "
    "OPTIONS: (a) as judged; (b) a short concept video instead of the image (6 concept videos, one image fewer, as in "
    "CLASH 7 option c); (c) no picture and Tool 4 follows nothing: not allowed by the flow gate, and the tool is "
    "locked. "
    "RECOMMENDATION: (a). One small picture is the least that can set the two words.",

    "CLASH 20, image C9 (T6.C3, place signboards) against C4 (video 2 and Tool 3). "
    "NOTE SAYS: tool_map.md row 13 is a real-life picture of the place signboards after Tool 6: the longest place "
    "name and the two shortest. "
    "BOOK SAYS: pdf 6 prints two facts with three photographs and asks nothing. The rule 'the longest name has the "
    "most letters' is taught earlier (C4), but the data of video 2 and Tool 3 are animals and friends, never places, "
    "so the picture is a new real-life example and not a repeat. The risk is accuracy, not repetition: the longest "
    "name (VENKATANARASIMHARAJUVARIPETA) has 28 letters and must be spelled exactly, the book's boards carry a local "
    "script as well as English, and a made picture can invent letters. "
    "JUDGEMENT: one image with three boards, main, no letter count shown (28, 2 and 2 are the plan's own true "
    "numbers, not the book's, and counting them is not asked); the English capitals exact letter by letter; a local "
    "script drawn only if it is real, otherwise left out; style photo, as proposed. "
    "OPTIONS: (a) as judged; (b) pin it beside Tool 3 (CLASH 12 option c): an image-only concept must sit in the "
    "main flow, so the concept would then need another medium; (c) style illustration, if a photo cannot be made "
    "with exact letters; (d) show the counts 28, 2 and 2 in the caption as the plan's own numbers. "
    "RECOMMENDATION: (a), with (c) as the fallback; not (d), because the book asks nothing here. The user decides.",

    "CLASH 21, image C12 (T7.C3, hair styles) against Tool 7 and against its own table. "
    "NOTE SAYS: tool_map.md row 16 is a real-life picture of children with different hair styles, which the child "
    "groups and counts to fill the book's table; no tool follows it. "
    "BOOK SAYS: pdf 8 draws six children (Mala and five others) and a table of six hair-style pictures with six empty "
    "cells; the numbers come from 'your class'. Grouping children by hair style is grouping again (C10), but Tool 7 "
    "puts cards into two groups by a rule, while this task sorts a picture into six kinds and counts: no "
    "interaction is repeated, and the image is the data of ch1.letus10, not a second explanation. Six children give "
    "counts of 0, 1 or 2 only, too few for a table worth filling. "
    "JUDGEMENT: one illustration of a class of ten to fifteen children (the plan's own class, labelled as practice "
    "with the book's children, CLASH 14), each child showing exactly one of the six styles, whole and not hidden, so "
    "that each group can be counted; Mala is one of them (two ponytails). The six style heads (hair_style_pictures) "
    "sit in a strip under the picture, as the book's table row, with no number. It must NOT show a count, a tick or a "
    "ring round a group, or Mala's mother (the combing scene is decoration). Illustration in the book's own drawing "
    "style, not photographs of real children. The answers are the plan's own, labelled 'From the picture'. "
    "OPTIONS: (a) as judged; (b) the book's six children only (the pdf 8 picture): a smaller picture, counts of 0, "
    "1 and 2; (c) the child's own class: a screen cannot hold it (CLASH 14 option c). "
    "RECOMMENDATION: (a). The exact number of children is for the brief writer to fix. The user decides about (b)."
    " QUESTION MAPPER: ch1.letus10 sits on this image (CLASH 13). Its answer cannot hold the six counts until the "
    "picture is made: CLASH 31.",

    "CLASH 22, video 1 (T2.C1) against the hook and Tool 1: the friend's idea given a third time, and a number in the "
    "title. "
    "NOTE SAYS: tool_map.md row 3: 'Their friend's idea of one mark for each cow; years later the wall has 47 marks, "
    "two are left when the cows return, and the marks left are the cows still out.' "
    "BOOK SAYS: the idea is one sentence on pdf 1, which Tool 1 gives as its task (CLASH 2). If video 1 named it again "
    "as a teaching step it would be a second explanation of C1 (CLASH 3). The same row names 47 and two, but Tool 2 "
    "asks them (ch1.fill1, ch1.story4, ch1.fill2) and the hand-off note says video 1 states no count. The old title "
    "'Two Marks Are Left' named a number. "
    "JUDGEMENT: the video recalls the idea in one line only, as the thread (what Deba and Deep already do), explains "
    "only C2, says no count and no number, and shows marks still left on the wall without counting them; the title "
    "becomes 'Marks Still on the Wall'. The hook may show 'their friend' as a silent listener, and no wall with marks "
    "appears in the hook. "
    "OPTIONS: (a) as judged; (b) the video says 'two marks are left' (the book's own sentence, ch1.story3), so that "
    "Tool 2 asks only the 47 and the 45: the story is closer to the book, but ch1.story4 'Why were Deba and Deep "
    "worried?' is then answered in the video; (c) no recall line: the thread to Tool 1 is lost. "
    "RECOMMENDATION: (a)."
    " QUESTION MAPPER: see CLASH 32. The sentences of ch1.wall1 and ch1.story3 that T2.C1 quotes in its `textbook` "
    "lines answer Tool 2's questions ch1.fill1, ch1.story4 and ch1.fill2.",

    "CLASH 23, video 3 (T5.C1) against Tool 5: the roll numbers 43 and 17. "
    "NOTE SAYS: tool_map.md row 9: 'Teji and Jojo make their roll numbers with number cards, Forty and Three for "
    "43'; row 10 (Tool 5): 'as Teji does for 43'. "
    "BOOK SAYS: Teji's roll number is 43, with 10 letters (ch1.example1), and Jojo's is 17 (ch1.fill3): both are "
    "questions on Tool 5. The sentence that introduces the cards says only 'Teji and Jojo are making numbers using "
    "these cards' (ch1.cards1). If the video builds 43 the tool shows the same example a second time; if it gave "
    "Teji and Jojo other roll numbers it would contradict the book. "
    "JUDGEMENT: in the video Teji and Jojo make numbers (not roll numbers) of their own: 15 (Fifteen, one card, 7 "
    "letters), 25 (Twenty, Five, 10 letters), 36 (Thirty, Six, 9 letters); all checked by program. Never 43, 17, 56 "
    "or 42, and never a number that is a Tool 6 answer (the 13 numbers of 8 letters, 70, 73, 77, 78, 93, 97, 98). "
    "The tens card goes first. The title becomes 'Making Numbers with Cards'. The traps M_NUM_3 (forty) and M_NUM_4 "
    "(a teen is one card) are met first on Tool 5, where 43 and 17 are asked. "
    "OPTIONS: (a) as judged; (b) keep the table's wording: the video builds 43 and 17, and Tool 5 then shows "
    "ch1.example1 and ch1.fill3 after they were told; (c) no video: Tool 5 follows an image of the cards. "
    "RECOMMENDATION: (a). It changes the wording of tool_map.md row 9, which is a concept video row, not an approved "
    "tool: core/tool_map.py verify still matches.",

    "CLASH 24, video 4 (T6.C1, the puzzle story) against Tool 6: one idea, one opener, no answers. "
    "NOTE SAYS: tool_map.md row 11: 'A puzzle story: 56 (fifty-six) has 8 letters; Teji and Jojo challenge each other "
    "to find more numbers with 8 letters and the number with the longest name.' The video's new_idea named both. "
    "FLOW RULES SAY: a concept video explains ONE concept; two concepts never share a video. "
    "BOOK SAYS: the 8 letter hunt is C7 (ch1.example2, ch1.think1); the longest number name, the riddles and the own "
    "puzzles are C8 (ch1.letus5 to ch1.letus7). 56 is the book's own opener and is ch1.example2, a solved example "
    "that sits on Tool 6. The brief (D) says a puzzle video keeps the book's rules and conditions, so '8 letters' and "
    "'between 1 and 99' stay. The answers that Tool 6 owns: the 13 numbers of 8 letters, the longest names (73, 77, "
    "78) and the riddle answers. "
    "JUDGEMENT: new_idea is C7 only ('different numbers can have names with the same number of letters'); the "
    "longest name is at most a closing question that the story leaves open. The video states 56 and its 8 letters as "
    "the book's opener, does not rebuild the number name from cards (video 3 did) and names no other 8 letter "
    "number, 42 included. Tool 6 then shows ch1.example2 as its first line (a recall, not a second explanation). "
    "OPTIONS: (a) as judged; (b) a different opener number and count in the video, so that Tool 6 meets 56 first: "
    "the video then departs from the book's puzzle; (c) both C7 and C8 in new_idea, as before: two concepts in one "
    "video. "
    "RECOMMENDATION: (a)."
    " QUESTION MAPPER: ch1.example2 (the solved 56) is homed on Tool 6 as the first line of the Let us Think box, "
    "before ch1.think1. The analysis gives it to C7, and its cards (Fifty, Six) also show C6's building, but the book "
    "prints the two in one box, so it has one home and the box stays whole.",

    "CLASH 25, video 5 (T7.C1) carries C10 and C11 and must not give away Jojo's rule. "
    "NOTE SAYS: tool_map.md row 14: 'Teji puts picture cards into two groups by a rule and Jojo groups the same "
    "cards another way, so the same things can be grouped in more than one way.' "
    "FLOW RULES SAY: one concept per video. "
    "BOOK SAYS: C10 (group by a rule) and C11 (another way to group the same things) are the book's own pair, Tool 7 "
    "holds both and the Teacher's Note names both. ch1.jojo1 'What is common in each groups Jojo has made?' is on "
    "Tool 7 and the book does not print the rule (from the picture, the things that fly). M_GRP_1 (only one right "
    "way) is the known misconception, and two groupings of the same cards in one story is what meets it. "
    "JUDGEMENT: one story with one new_idea ('things can be grouped by a rule, and the same things can be grouped "
    "another way'): the pair is one idea, flexible grouping. The video states Teji's rule in her own words (the book "
    "prints it: those that eat food, those that don't), shows Jojo's two groups only as cards with no label, no "
    "caption and no hint of the rule (no word like fly or air), and ends before anyone asks or says what is common. "
    "It does not use the household objects (Tool 7) or the hair styles (the image). "
    "OPTIONS: (a) as judged; (b) the video is only C10 and Jojo's regrouping is first met on Tool 7 (the story then "
    "has no problem to solve); (c) a second video for C11 with no tool after it (6 concept videos). "
    "RECOMMENDATION: (a).",

    "CLASH 26, video 2 (T3.C1) against Tool 3: what the video may count. "
    "NOTE SAYS: tool_map.md row 5: 'Mahesh and Kartik each say My name is longer; the animals pick captains by their "
    "letters; the length of a name is its letter count.' "
    "BOOK SAYS: ch1.letus1 (the captains: elephant 8 letters, ox 2), ch1.letus2 (Mahesh and Kartik: 6 and 6) and "
    "ch1.letus3 (eight friends' names) are all on Tool 3, and the handwriting makes Mahesh look wider (M_NAME_1). A "
    "video that counts any of these names gives an answer away. "
    "JUDGEMENT: the video poses the two puzzles and gives the rule in the book's words (most letters is longest, "
    "fewest letters is shortest); to show how to count it counts only a name that Tool 3 does not use, for example "
    "cow and sheep (3 and 5 letters) from the cowherd thread. It does not count Mahesh or Kartik, does not say that "
    "they are equal, does not name a captain or count an animal card, and does not tell that two names can be the "
    "same length (M_NAME_2 is met on Tool 3). "
    "OPTIONS: (a) as judged; (b) the video counts one of the ten animal names: that answer is then in two media; (c) "
    "no counting example, the rule alone (less clear for a child of 8 to 9). "
    "RECOMMENDATION: (a).",

    "CLASH 27, the review reuses earlier pictures. "
    "BRIEF SAYS: E, 'a visual recap of the important concepts; revisit the chapter's learning journey'. "
    "FLOW RULES SAY: the review has no new video or tool and no new content; at most one image per concept; no image "
    "may repeat another (same title or same thing shown). "
    "BOOK SAYS: no summary, recap or review. "
    "JUDGEMENT: the two review concepts hold no medium of their own (no video, no image, no tool). Their recap lines "
    "may show a picture already made (the wall, the animal cards, the name tags, the number cards, the signboards, "
    "the cards in two groups, the hair styles) by reference to its id; no picture is made again. "
    "OPTIONS: (a) as judged; (b) a pinned recap image on each review concept (2 images), each a collage of earlier "
    "pictures: it would repeat them, and the duplicate gate reads a repeated thing shown as a duplicate; (c) one "
    "pinned recap image for the whole chapter. "
    "RECOMMENDATION: (a).",

    "CLASH 28, VISUAL_KEY keys that the media need and the book does not give. "
    "NOTE SAYS: tools_1.py and the image briefs name visual keys; tools_1.py is locked. "
    "BOOK SAYS: the wall with marks of pdf 1 has no key (only stone_slab for the 47); no sheep is drawn; there are "
    "no name tags; the cards of pdf 5 have a key (number_card) but no key for a laid number name; the hair-style "
    "children have a key only for the six table heads; Hemant is not drawn. "
    "DONE: six keys added to content.VISUAL_KEY: wall_marks, sheep (a real sheep, never a cow), name_tag, "
    "start_end_marker (two ring colours for the starting and the ending letter), number_name_row (a laid number "
    "name: tens card first, no dash drawn) and class_children. "
    "NOT DONE: (1) the visuals lists of the tools in tools_1.py are not changed (the tools are locked): at the "
    "briefs stage Tool 1 should name wall_marks, Tool 2 sheep, Tool 4 name_tag and start_end_marker, Tools 5 and 6 "
    "number_name_row; (2) Hemant stays undrawn: the book never draws him, so Tool 2 names Hemant in words and shows "
    "only his cows and sheep. "
    "OPTIONS: (a) as done; (b) also draw Hemant like 'their friend' of pdf 1, a look the book does not give; (c) "
    "leave the locked tool lists as they are and let each tool brief name the new keys. "
    "RECOMMENDATION: (a) and (c).",

    # --- written by the question mapper (step 5). New findings only; CLASH 2 to 24 are followed as recommended and carry a
    # "QUESTION MAPPER" line where the homes touch them. ---
    "CLASH 29, the screen wording of five questions is not the printed wording. "
    "NOTE SAYS: the question mapper copies the book's wording exactly. CLASH 11 recommends keeping 'animals and birds' as "
    "printed, CLASH 10 recommends keeping 'each groups' as printed and reading 'the given objects' as the eight household "
    "objects, CLASH 9 recommends showing only the two Find out boxes, and CLASH 11 (d) lets the 27 cards of the page stand "
    "for the cards 'at the end of the book'. "
    "USER'S RULE FOR THIS STEP: no child-facing text repeats a printed error. "
    "BOOK SAYS: ch1.letus1 'Some animals and birds got together to play a game' (no bird is among the ten cards); "
    "ch1.jojo1 'What is common in each groups Jojo has made?' (a grammar slip); ch1.letus9 'Group the given objects "
    "differently' (which objects is not said); ch1.letus4a 'Number cards are given at the end of the book' (they are not "
    "in this chapter; the screen has them); ch1.letus6a is printed under the stem of Q1, 'Write the number(s) between 1 "
    "and 99 that have the longest name', which the riddles do not ask. "
    "DONE: the questions on screen read 'Some animals got together to play a game', 'each group', 'Group the eight "
    "household objects differently', 'The number cards are on the screen.', and, for ch1.letus6a, only the Find out box. "
    "Nothing else in these five questions is changed. The printed words stay in analysis.md and each change is in "
    "SOLUTION_NOTES. This departs from the recommendation 'keep as printed' of CLASH 11 (b) and of the ch1.jojo1 wording "
    "in CLASH 10. "
    "OPTIONS: (a) as done; (b) keep every printed word, as CLASH 9 to 11 recommend: the screen then shows 'birds' with no "
    "bird, 'each groups', 'the given objects', a pointer to cards at the end of a book the child does not hold, and the "
    "repeated Q2 stem; (c) keep the printed words and add a short note under each question. "
    "RECOMMENDATION: (a). Each change is one phrase and can be restored with one edit. The user decides.",

    "CLASH 30, every answer is the plan's own, and the closed ones are worked out, not read from a picture. "
    "NOTE SAYS: every plan-made answer begins exactly 'From the picture' or 'Sample answer'; an open task ends 'Your "
    "answer may differ'; no answer reads as an official book answer. "
    "BOOK SAYS: no answer is printed anywhere in the chapter. Official answer key: NONE FOUND (searched "
    "textbooks/class3/cemm1ps.pdf, the prelims, docs/, upload/ and this chapter's book folder). "
    "WHAT THE PLAN DID: 'From the picture' (12): ch1.story2, ch1.fill1 (47), ch1.story4, ch1.fill2 (45), ch1.letus1, "
    "ch1.letus2, ch1.example1, ch1.fill3, ch1.example2, ch1.jojo1, ch1.letus8, ch1.letus10. 'Sample answer ... Your answer "
    "may differ' (14), open tasks: ch1.hemant1, ch1.longer1 (crocodile, 9 letters: a real animal the book does not name), "
    "ch1.letus3 and ch1.letus3a to ch1.letus3f (the eight practice names, CLASH 14), ch1.letus4a (roll number 29), "
    "ch1.letus4b, ch1.think1, ch1.letus7 (a puzzle of the plan's own) and ch1.letus9. 'Sample answer' with no 'Your answer "
    "may differ' (3), closed answers worked out by counting letters that no picture shows: ch1.letus5 (73, 77 and 78), "
    "ch1.letus6a (93, 97 and 98) and ch1.letus6b (70). 12 + 14 + 3 = 29. "
    "OPTIONS: (a) as done; (b) write 'From the picture' on the closed counts too: not true for ch1.letus5 and the two "
    "riddles, which no picture shows; (c) wait for the content team's own key and replace every answer. "
    "RECOMMENDATION: (a). The user decides whether the three closed counted answers keep 'Sample answer'.",

    "CLASH 31, ch1.letus10 (hair styles): its answer cannot hold the six counts yet. "
    "NOTE SAYS: the image T7.C3 shows a class of ten to fifteen children, each with one of the six hair styles of the "
    "table (CLASH 21); the book question sits on that image (CLASH 13). "
    "BOOK SAYS: the six numbers come from 'the children in your class'; the book gives none. The class picture is made at "
    "the briefs stage and its exact number of children is for the brief writer, so no true count can be written now. "
    "DONE: the answer says 'From the picture: write how many children have each of the six hair styles. The six numbers "
    "together make all the children in the picture. Your own class may give other numbers.' It states no count. "
    "OPTIONS: (a) as done, and the brief writer replaces the answer with the six true counts when the picture is fixed "
    "(each count checked against the picture, and the six adding up to the number of children); (b) fix the six counts "
    "now as a requirement of the image brief, which decides the picture before the user approves the structure; (c) leave "
    "the question with no answer line. "
    "RECOMMENDATION: (a).",

    "CLASH 32, the quoted book lines of the first concept video answer Tool 2's questions. "
    "NOTE SAYS: T2.C1 (video 1) carries ch1.wall1, ch1.story3, ch1.found1 and ch1.tnote1 as text, and its `textbook` lines "
    "quote 'One day, their wall had this many marks when they left home.' and 'Two marks were still left on the wall but "
    "they didn't see any cows outside. They were worried.'; CLASH 22 says the video states no count and no 'two marks'. "
    "BOOK SAYS: those two sentences are the story the questions refer to, and the book asks ch1.fill1 (how many cows), "
    "ch1.story4 (why were they worried) and ch1.fill2 (how many reached home) right after them. Tool 2 holds all three. If "
    "the quoted lines are shown to the child before Tool 2, 'two marks were still left' and 'they were worried' give away "
    "ch1.story4 and half of ch1.fill2. "
    "NOT CHANGED: topics_1.py T2.C1 `textbook` is the journey designer's list; the question mapper did not edit it. The "
    "four items stay homed on T2.C1 through `ncert`, so coverage is complete either way. "
    "OPTIONS: (a) keep the quoted lines as they are and let the video and Tool 2 show the situation: ch1.story4 is then "
    "answered in the text; (b) take the sentence 'Two marks were still left ...' (and the 'this many marks' sentence) out "
    "of the `textbook` lines and keep ch1.wall1 and ch1.story3 only as `ncert` references, so that Tool 2 asks them first; "
    "(c) as CLASH 22 option (b): the video says 'two marks are left'. "
    "RECOMMENDATION: (b), which keeps CLASH 22's option (a). The user decides.",
]

# ---------------------------------------------------------------------------
# printed-book errors this plan corrects: {"item", "printed_solution", "correct"}; and ERRATA, exact false-equation
# chains kept verbatim from the book (copy each into chapter.config.json "eqcheck_errata" too).
# ---------------------------------------------------------------------------
SOLUTION_NOTES = [
    {"item": "all 29 questions",
     "printed_solution": "The chapter prints no answer, solution or key.",
     "correct": "No official key was found in the repository (CLASH 30). Every answer is the plan's own reading and "
                "begins 'From the picture' or 'Sample answer'; open tasks end 'Your answer may differ'. None is "
                "presented as an official book answer. The content team may replace them with a key."},
    {"item": "ch1.letus6a (and ch1.letus6b): the stem of Q2",
     "printed_solution": "Q2 on pdf 6 is printed with the stem of Q1, 'Write the number(s) between 1 and 99 that have "
                         "the longest name', but it holds two Find out riddles that do not ask for the longest name.",
     "correct": "Only the Find out boxes are shown (CLASH 9 option a, CLASH 29). The repeated stem is not shown to "
                "the child. The longest name is asked once, in ch1.letus5."},
    {"item": "ch1.letus6a: 'I am very near to 100'",
     "printed_solution": "A first word of 6 letters and a second word of 5 letters, 'very near to 100': ninety-three, "
                         "ninety-seven and ninety-eight all fit. The book asks 'Who am I?' as if there were one. No "
                         "answer is printed.",
     "correct": "The answer accepts 93, 97 and 98 and says each one fits; a step says more than one number may fit. "
                "It is labelled 'Sample answer'."},
    {"item": "ch1.letus6b: 'the smallest among all my friends'",
     "printed_solution": "'Smallest' can mean the fewest letters (seventy, 70, 7 letters) or the smallest number "
                         "(63). No answer is printed.",
     "correct": "A step says that here smallest means the name with the fewest letters. The answer is 70 (seventy, "
                "7 letters, the fewest from 63 to 78) and adds that sixty-three, the smallest number, has 10 letters. "
                "It is labelled 'Sample answer'."},
    {"item": "ch1.letus1: 'Some animals and birds'",
     "printed_solution": "The text says animals and birds, but the ten cards (tiger, dog, snake, goat, lion, elephant, "
                         "deer, ox, rat, monkey) are all animals. No bird is among them.",
     "correct": "The question on screen says 'Some animals got together to play a game' (CLASH 29). The answer is "
                "labelled 'From the picture': first team captain elephant, 8 letters; second team captain ox, 2 "
                "letters (tiger 5, dog 3, snake 5, goat 4, lion 4, elephant 8, deer 4, ox 2, rat 3, monkey 6)."},
    {"item": "ch1.longer1",
     "printed_solution": "'Do you know any animal having a longer name than the first team's captain?' The book names "
                         "no animal and prints no answer.",
     "correct": "The sample answer is the plan's own: crocodile, 9 letters, more than the 8 of elephant. It is "
                "labelled 'Sample answer' and ends 'Your answer may differ'."},
    {"item": "ch1.letus2",
     "printed_solution": "Mahesh and Kartik both have 6 letters, so by the book's own rule neither name is longer. The "
                         "book says only 'Discuss'. In the thin handwriting Mahesh looks wider. The two boys share one "
                         "bubble and the book does not say which boy has which name.",
     "correct": "The answer is labelled 'From the picture': both names have 6 letters, they are the same length, "
                "neither is longer (CLASH 6). A step says a name that looks wider is not a longer name."},
    {"item": "ch1.fill1 and ch1.fill2",
     "printed_solution": "The 47 marks are not printed as a number. They are read from the stone slab: two full rows "
                         "of 4 groups of 5, then a group of 5 and a group of 2. A child who counts differently gets a "
                         "different answer to the second blank.",
     "correct": "The plan reads 47 (20 + 20 + 7) and, after 2 marks are left, 47 \u2212 2 = 45 cows reached home. "
                "Both are labelled 'From the picture' (CLASH 11 a)."},
    {"item": "ch1.letus3 and ch1.letus3a to ch1.letus3f",
     "printed_solution": "The task asks for 'your friends' names', 'your name' and 'yours', which a screen cannot "
                         "hold. Part e does not say the same ending letter as what. Whether the child's own name is "
                         "among the eight lines, and a tie for 'the most used' starting letter, are not said.",
     "correct": "The eight names of this chapter are practice friends (CLASH 14). 'My name' is Mala for parts b, c "
                "and e. Part e is read as the same ending letter as yours, like part c. The tie of D and M is said in "
                "part d. Every answer is a 'Sample answer' that ends 'Your answer may differ'."},
    {"item": "ch1.letus4a: 'Number cards are given at the end of the book'",
     "printed_solution": "The cut-out number cards are not in this chapter file. The picture on pdf 5 shows all 27.",
     "correct": "The question on screen says 'The number cards are on the screen' (CLASH 29, CLASH 11 d). The roll "
                "number is a practice number from 1 to 99, and the sample answer is 29 (Twenty, Nine: 6 + 4 = 10 "
                "letters), labelled 'Sample answer'."},
    {"item": "ch1.example1, ch1.fill3, ch1.example2, ch1.letus4b, ch1.think1: the dash",
     "printed_solution": "Number names are written with a dash ('fifty-six', 'forty-two') but each part is its own "
                         "card ('Fifty', 'Six').",
     "correct": "The letter count ignores the dash: 56 is 5 + 3 = 8, 43 is 5 + 5 = 10, 17 is one card of 9 letters. "
                "A step says the dash is not a letter."},
    {"item": "ch1.letus7",
     "printed_solution": "'Make similar puzzles of your own in your notebook and ask your classmates.' It is a "
                         "notebook task for the class, which a screen cannot hold.",
     "correct": "The steps are 'pick numbers, write a clue, check it'. The sample answer is the plan's own puzzle: "
                "the numbers from 20 to 25 and the longest name, answer 23 (twenty-three, 11 letters). It is "
                "labelled 'Sample answer' and ends 'Your answer may differ'."},
    {"item": "ch1.jojo1: 'each groups'",
     "printed_solution": "'What is common in each groups Jojo has made?' is a grammar slip. Jojo's rule is not "
                         "printed. From the picture, one group holds the kite, aeroplane, bird, drone and fly (they "
                         "fly) and the other the mobile phone, fish, light bulb, book and rat (they do not).",
     "correct": "The question on screen says 'each group' (CLASH 29). The answer is labelled 'From the picture' and "
                "gives the plan's reading: things that fly and things that do not fly."},
    {"item": "ch1.letus8: the battery clock and the oil lamp",
     "printed_solution": "Four lines for each group suggest TV, Lamp, Clock, Fan against Chair, Bed, Pillow, "
                         "Blanket. But a wall clock may run on a battery, and a lamp may be an oil lamp.",
     "correct": "The answer is labelled 'From the picture': TV, Lamp, Clock, Fan need electricity; Chair, Bed, "
                "Pillow, Blanket do not. It says the lamp is an electric table lamp and the clock runs on electricity, "
                "from a battery or the plug (CLASH 10)."},
    {"item": "ch1.letus9: 'the given objects'",
     "printed_solution": "'Group the given objects differently.' It does not say which objects. The two panels have "
                         "no labels. Four lines each fit the eight household objects; the ten picture cards would "
                         "need five each.",
     "correct": "The question on screen says 'Group the eight household objects differently' (CLASH 29). The "
                "sample answer groups by sleeping (Bed, Pillow, Blanket against TV, Chair, Lamp, Clock, Fan) and is "
                "labelled 'Sample answer'."},
    {"item": "ch1.letus10: 'your class'",
     "printed_solution": "'Look at the children in your class.' The six hair-style pictures have no names and the "
                         "numbers come from the child's own class. No answer is printed.",
     "correct": "The picture shows a practice class (CLASH 21). The answer says how to read the six counts and states "
                "none, because the class picture is made at the briefs stage (CLASH 31). It is labelled 'From the "
                "picture'."},
    {"item": "the labels Let us Do, Q1 to Q4",
     "printed_solution": "The chapter has two sets of Let us Do questions, both numbered 1 to 4 (pdf 3 to 5 and pdf 6 "
                         "to 7), so 'Q4' means two different questions.",
     "correct": "Each question keeps the book's own number in its label. The ids ch1.letus1 to ch1.letus10 and the "
                "map in question_map.md tell them apart. A tool never holds two questions with the same label."},
]
ERRATA = [
]

DESIGN_REFERENCES = [
    {"text": "Class 3/4 story and tool flow: docs/00_overview.md. The approved tool map comes from the content team.",
     "url": ""},
]

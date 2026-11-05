# -*- coding: utf-8 -*-
from __future__ import annotations

from topics_common import A, DOER, FIO, IMG, TOPIC, VID, WE  # noqa: F401

TOPICS = []

TOPICS.append(TOPIC(
    "T1", "M1", "The Kite Fair", ["Opening"], "Understand", "",
    "Meera and Raju reach the kite fair. The child looks at a stall and notices that kites can be grouped.",
    [A("T1.C1", "The Kite Fair", "Understand", "", role="hook",
       teach=["Predict first: how many kites can you see at the stall?"], ncert=["opening"],
       video=VID("The Kite Fair", "Meera and Raju reach the fair and see a heap of kites to count.",
                 story={"characters": ["Meera", "Raju"], "setting": "the village kite fair",
                        "situation": "Meera and Raju open their stall and find a big heap of kites in a box.",
                        "open_question": "How can we count so many kites quickly?"}, seconds=60)),
     DOER("T1.C2", "Kite Spotter", "kite_spotter", "Understand", "", applies_to="T1.C1", role="explore")],
    topic_type="framing"))

TOPICS.append(TOPIC(
    "T2", "M1", "Making a Ten", ["Tens"], "Apply",
    "Students tie ten ones into one ten and say how many tens and ones a number has.",
    "Ten ones make one ten. We count the tens and the ones left over.",
    [A("T2.C1", "Ten ones make a ten", "Understand", "Students say that ten ones make one ten.", role="story",
       textbook=["Ten ones make one ten."],
       teach=["Predict first: how many sticks make one bundle?", "Ten sticks tie into one bundle.",
              "10 + 10 = 20, so two bundles are twenty."],
       ncert=["kf.rule", "kf.talk"], key_terms=["ten", "ones"], misconceptions=["M_TOY_1"],
       video=VID("Raju ties the sticks", "Raju needs to count the kite sticks and Meera shows him a quick way.",
                 new_idea="ten ones make one ten",
                 story={"characters": ["Meera", "Raju"], "setting": "the village kite fair",
                        "situation": "Raju drops a box of loose kite sticks and starts counting them one by one.",
                        "problem": "Counting one by one takes too long and he loses his place.",
                        "thread": "After seeing the heap of kites, the sticks for the kites must be counted too.",
                        "leads_to": "Ten Bundles"}, seconds=120)),
     DOER("T2.C2", "Ten Bundles", "ten_bundles", "Apply", "Students tie sticks into tens and read the tens and ones.",
          applies_to="T2.C1", recap=["Ten ones make one ten."],
          items=[FIO("kf.q1", "Let Us Do, Q1", "Tie 23 sticks into bundles of ten. How many tens are there?",
                     ["20 + 3 = 23", "2 tens and 3 ones"], "2 tens"),
                 FIO("kf.q3", "Example 1", "Meera has 3 bundles and 4 loose sticks. How many sticks is that?",
                     ["3 tens = 30", "30 + 4 = 34"], "34 sticks", kind="example")])],
    topic_type="instructional"))

TOPICS.append(TOPIC(
    "T3", "M1", "Reading the Price Board", ["Board"], "Understand",
    "Students read a two-digit price from the stall board.",
    "The price board shows a number made of tens and ones.",
    [A("T3.C1", "A price board with tens and ones", "Understand", "Students read a price board as tens and ones.",
       role="image", teach=["Predict first: what price is on the board?", "Read the tens first, then the ones."],
       key_terms=["price"],
       image=IMG("Price board at a kite stall", "A real stall board that shows the idea in a place children know.",
                 placement="main", real_life="a hand-painted price board at a small fair stall",
                 shows="a price made of tens and ones", caption="What price is on the board?", style="photo",
                 visuals=["kite"]),
       items=[FIO("kf.q2", "Try This", "Read the price on the board: 45 rupees. How many tens are in 45?",
                  ["45 = 40 + 5", "4 tens"], "4 tens", kind="prompt")])],
    topic_type="instructional"))

TOPICS.append(TOPIC(
    "T4", "MLAST", "Chapter Review", ["Review"], "Understand", "",
    "A short look back at the fair.",
    [A("T4.C1", "Back at the fair", "Understand", "Students recall that ten ones make one ten and read a price board.",
       role="review", teach=["Meera counted the sticks in tens.", "She also read the price board."],
       key_terms=["ten"], review_covers=["T2.C1", "T3.C1"], minutes=4)],
    topic_type="summary"))

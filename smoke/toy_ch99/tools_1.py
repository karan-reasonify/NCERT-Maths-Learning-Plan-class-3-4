# -*- coding: utf-8 -*-
from __future__ import annotations

from topics_common import T

TOOLS = {
    "kite_spotter": T(
        "tool_kite_spotter", "Kite Spotter", 1,
        "Students sort kites by colour and notice how many are in each group.",
        screen="One big stall with red, blue and green kites. Three coloured boxes below.",
        controls=["Tap a kite", "Tap a box"],
        instruction="Tap a kite, then tap its colour box.",
        notice=["What do you notice about the kites in one box?", "Which box has the most kites?"],
        feedback=["A kite in the right box glows and the box count goes up by one.",
                  "A kite in the wrong box slides back and the colour name is shown."],
        done_when="All the kites are in their boxes.",
        shared_state=["boxCounts"], misconceptions=[], visuals=["kite"],
        hints=["Look at the colour of the kite.", "Find the box with the same colour.",
               "Tap the kite, then the box with that colour.", "Put the red kite in the red box."]),
    "ten_bundles": T(
        "tool_ten_bundles", "Ten Bundles", 2,
        "Students tie loose sticks into bundles of ten and read the tens and the ones.",
        screen="A heap of loose sticks and a blue string. A tens box and a ones box.",
        controls=["Drag sticks", "Tie a bundle", "Reset"],
        instruction="Drag ten sticks together and tie them.",
        feedback=["Ten sticks tie into one bundle and the tens box shows 1.",
                  "Fewer than ten sticks cannot be tied; the sticks wait in the ones box."],
        done_when="Every possible bundle of ten is tied.",
        shared_state=["tens", "ones"], misconceptions=["M_TOY_1"], visuals=["bundle"],
        hints=["How many sticks make a bundle?", "Count ten sticks.", "Drag ten sticks to the string.",
               "Take 10 sticks and tie them: 10 ones make 1 ten."]),
}

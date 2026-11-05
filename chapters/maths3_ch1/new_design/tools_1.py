# -*- coding: utf-8 -*-
"""What's in a Name? (Class 3, chapter 1): the chapter's tool specs, one entry per tool of the locked table.

STRUCTURE STAGE (c34-tool-mapper): each entry carries tool_id, title (EXACTLY the name in the table), approved_no, the ONE
learning objective, the VISUAL_KEY keys it draws and, for Tool 1, the `notice` prompts. The rest of each spec (screen,
controls, instruction, feedback, done_when, shared_state, hints) is for the brief writer, after the user approves the
structure. The tool's questions are the book items (FIO in topics_N.py), never written here.

The seven tools are the pipeline's PROPOSAL, not the content team's (CLASH 1 in content.py): no content-team table existed
and the user chose "propose fresh from the book". tool_map.md -> chapter.config.json "approved_tools" holds the same names,
purposes and order; tool_map.locked.md has the concept, the place in the flow and the proposed book items of each.

A tool here is a spec + placeholder (tools_spec/TOOL_SPEC_GUIDE.md): the tool itself is built elsewhere. Nothing below is
made yet.

Notes for the brief writer (decisions are the user's, see CLASHES):
- Tools 3, 4 and 5 and the hair styles image need sample data (CLASH 14); name tags and sheep have no VISUAL_KEY key yet.
- No tool needs number names before Tool 5 (Tool 1 is for children who "do not know how to count": one mark, one cow).
"""
from __future__ import annotations

from topics_common import T  # noqa: F401

TOOLS = {
    # Tool 1: the exploration tool, right after the hook. Concept: C1 (the opening situation).
    "marks_gate": T(
        "tool_marks_at_the_gate", "Marks at the Gate", 1,
        "Students make one mark for each cow that leaves, strike one out for each that returns, "
        "and notice whether any cow is missing.",
        notice=["What do you see on the wall when a cow goes out?",
                "What happens to the marks when the cows come back?",
                "How can you tell that no cow is missing?"],
        visuals=["tally_mark", "struck_mark", "cow_shed", "cows", "deba_and_deep"]),

    # Tool 2: C2 (reading the marks) with C3 (marks for two kinds), the book's own pair.
    "marks_herd": T(
        "tool_marks_for_a_big_herd", "Marks for a Big Herd", 2,
        "Students read the marks to find the cows still out and the cows back, "
        "then make separate marks for cows and sheep.",
        visuals=["tally_mark", "struck_mark", "stone_slab", "cows", "deba_and_deep"]),

    # Tool 3: C4 (the length of a name is its letter count).
    "longest_shortest": T(
        "tool_longest_and_shortest_name", "Longest and Shortest Name", 3,
        "Students count the letters in each name and compare them to find the longest and the shortest name.",
        visuals=["animal_card", "name_big", "mahesh_kartik_boys", "tick_and_cross"]),

    # Tool 4: C5 (starting letters and ending letters). The weakest tool of the table (CLASH 7).
    "start_end_letters": T(
        "tool_starting_and_ending_letters", "Starting and Ending Letters", 4,
        "Students sort names by their starting letter or ending letter and count each group to find the letter used most.",
        visuals=["name_big", "group_box", "answer_blank"]),

    # Tool 5: C6 (number names and their letter count).
    "build_number_name": T(
        "tool_build_a_number_name", "Build a Number Name", 5,
        "Students make a number name from a tens card and a ones card and count the letters in it.",
        visuals=["number_card", "teji", "jojo", "answer_blank"]),

    # Tool 6: C7 (numbers whose names have the same letter count) with C8 (longest names, riddles, own puzzles).
    "number_puzzles": T(
        "tool_number_name_puzzles", "Number Name Puzzles", 6,
        "Students use the letter counts of number names to find numbers between 1 and 99 "
        "and notice what same-count names share.",
        visuals=["number_card", "answer_blank", "teji", "jojo", "speech_bubble"]),

    # Tool 7: C10 (group things by a rule) with C11 (another way to group the same things), the book's own pair.
    "group_two_ways": T(
        "tool_group_the_cards_two_ways", "Group the Cards Two Ways", 7,
        "Students put things into two groups by a rule, say what is common in a group, and regroup them another way.",
        visuals=["picture_card", "household_card", "group_box", "teji", "jojo"]),
}

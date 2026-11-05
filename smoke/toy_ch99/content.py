# -*- coding: utf-8 -*-
"""Smoke-test chapter: a made-up Class 3 chapter, only to exercise the pipeline end to end. Not a real NCERT chapter."""
from __future__ import annotations

CHAPTER = {"grade": 3, "label": "Class 3", "chapter_no": 99, "name": "Kite Day Toy", "book": "NCERT Maths Mela",
           "source_pdf": "textbooks/class3/none.pdf"}
CHAPTER_NAME = CHAPTER["name"]

MODULES = [
    ("M1", "Kites and Tens", "Meera and Raju count kites at the fair and find a quick way to count."),
    ("MLAST", "Chapter Review", "Remember what Meera and Raju found."),
]

STORY = {"thread": "Meera and Raju run a kite stall and must count their sticks and kites quickly.",
         "setting": "the village kite fair", "characters": ["Meera", "Raju"]}

VISUAL_KEY = {"kite": "a red diamond kite with a long yellow tail", "bundle": "ten thin sticks tied with a blue string"}

CHAPTER_APPROACH = {
    "heading": "How this chapter is taught",
    "intro": "A story opens the fair. The child explores a kite stall. A second story names the ten. A tool lets the child tie bundles.",
    "points": [{"title": "One story", "text": "Meera and Raju stay with the child from the hook to the review."}],
}

NCERT_ITEMS = [
    ("opening", "text"),
    ("kf.rule", "text"),
    ("kf.q1", "exercise"),
    ("kf.q3", "example"),
    ("kf.q2", "prompt"),
    ("kf.talk", "talk"),
]

MISCONCEPTIONS = [("M_TOY_1", "Children think ten ones and one ten are two different amounts.")]
CLASHES = []
SOLUTION_NOTES = []
ERRATA = []
DESIGN_REFERENCES = [{"text": "Smoke test fixture.", "url": ""}]

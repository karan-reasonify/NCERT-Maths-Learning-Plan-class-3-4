# -*- coding: utf-8 -*-
"""Authoring helpers shared by the topic files and the tool files: plain dicts that build.py reads directly.
Carried over from the Class 5 chapter (A, WE, FIO, DOER, TOPIC, T) with the Class 6-8 video-script, solution-card and
Questions-topic fields removed, and with VID / IMG added for the Class 3/4 story-video and real-life-image briefs.

The flow these build (gates/flow_c34.py checks it):

    TOPIC "framing"       A(role="hook", video=VID(...))  ->  DOER(role="explore", applies_to=<the hook>)
    TOPIC "instructional" A(role="story", video=VID(...)) ->  DOER(role="tool", applies_to=<that A>, items=[FIO...])
                          (a small concept may be A(role="image", image=IMG(...)) with no video and no tool)
    TOPIC "summary"       A(role="review", review_covers=[...])

Rules every string here follows: short plain sentences for a child of 8 to 10; no em dash and no en dash (use a comma,
a colon or "to"); minus is U+2212; never "NCERT", "textbook", "page N" or "Fig." in anything the child reads.
"""
from __future__ import annotations


def WE(q, steps, answer, *, ncert=(), expect=None):
    """A worked example of the PLAN's own, one step per line, with its own numbers (never the book's numbers: a
    solved example PRINTED in the book is a question, so it is an FIO(kind="example")). At most one per concept."""
    return {"q": q, "steps": list(steps), "answer": answer, "ncert": list(ncert), "expect": expect}


def FIO(cov, book, question, steps, answer, *, kind="exercise", expect=None):
    """A BOOK QUESTION (the NCERT practice). It is homed on the concept whose idea it practises: in `items` of the
    tool concept (DOER) when a tool follows the concept video, otherwise in `items` of the concept itself.

    cov       its coverage id (must appear in content.NCERT_ITEMS with the same kind)
    book      its label as the child sees it: "Example 1", "Let Us Do, Q3" (the book's own label, never a page)
    question  the book's wording, copied (say "maths book" for "textbook")
    steps     the short working, one operation per line (may be empty for a question that only needs an answer)
    answer    the short final answer ("Sample answer: ... Your answer may differ." for an open-ended item)
    kind      "example" a solved example printed in the book | "exercise" an exercise question |
              "prompt" an answerable in-text question (a Try This with an answer, a blank to fill).
              Discussion prompts and facts are not questions: leave them in the teaching text.
    """
    if kind not in ("example", "exercise", "prompt"):
        raise ValueError("FIO %s: kind must be example, exercise or prompt" % cov)
    return {"cov": cov, "book": book, "question": question, "steps": list(steps), "answer": answer, "expect": expect,
            "kind": kind}


def VID(title, purpose, *, new_idea="", story=None, seconds=None):
    """A story video. Its kind comes from the concept's role: the hook for role "hook", otherwise a concept video.

    title     what the child sees as the video's name
    purpose   one sentence: what this video is for
    new_idea  the ONE concept a concept video explains (empty for the hook: it only introduces the situation)
    story     the story brief, filled in at the briefs stage (after the user approves the structure):
                hook:    {"characters": [..], "setting": "..", "situation": "..", "open_question": ".."}
                concept: {"characters": [..], "setting": "..", "situation": "..", "problem": "..",
                          "thread": "how the story continues from the video before", "leads_to": "the tool or concept next"}
              characters must come from content.STORY["characters"]
    seconds   target length: hook up to 90, concept video up to 150
    """
    return {"title": title, "purpose": purpose, "new_idea": new_idea, "story": story or {}, "seconds": seconds}


def IMG(title, adds, *, placement="main", new_context=False, real_life="", shows="", caption="", style="photo",
        visuals=()):
    """One clean real-life image. Make it only when it adds a real-life example or a visual reference.

    adds         what it contributes that no video or tool already shows (required)
    placement    "main" (in the learning flow, with its caption, for a small concept that needs no video or tool) or
                 "pinned" (supporting reference kept beside a concept a video or tool already teaches)
    new_context  True only when a main image sits on a concept that already has a video or tool AND brings a new
                 real-life example
    real_life    the familiar object or situation (briefs stage)
    shows        what the child should notice (briefs stage)
    caption      a short prompt or caption, at most 15 words (briefs stage)
    style        "photo" | "illustration"
    visuals      keys of content.VISUAL_KEY drawn in it, so the same object looks the same everywhere
    """
    if placement not in ("main", "pinned"):
        raise ValueError("IMG %s: placement must be main or pinned" % title)
    if style not in ("photo", "illustration"):
        raise ValueError("IMG %s: style must be photo or illustration" % title)
    return {"title": title, "adds": adds, "placement": placement, "new_context": new_context, "real_life": real_life,
            "shows": shows, "caption": caption, "style": style, "visuals": list(visuals)}


def A(key, name, bloom, objective, *, role="story", textbook=(), teach=(), examples=(), ncert=(), key_terms=(),
      misconceptions=(), enrichment=None, minutes=6, video=None, image=None, items=(), review_covers=()):
    """A teaching concept.

    role         "hook" | "story" (a concept video) | "image" (an image-only small concept) | "review"
    video        VID(...), required for "hook" and "story"
    image        IMG(...), required for "image"; optional on others (pinned, or main with new_context)
    items        FIO(...) only when NO tool follows this concept (otherwise they belong on the tool)
    review_covers  keys of the earlier concepts a review concept revises ("T2.C1", ...): no new content
    enrichment   True means no objective is built; defaults to True for the hook
    teach        the plan's own teaching lines, prediction first ("Predict first: ..."), then the reveal
    textbook     the book's own lines, quoted verbatim (dashes normalised to commas, colons or "to")
    """
    if role not in ("hook", "story", "image", "review"):
        raise ValueError("concept %s: role must be hook, story, image or review" % key)
    if role in ("hook", "story") and not video:
        raise ValueError("concept %s: a %s concept needs video=VID(...)" % (key, role))
    if role == "image" and not (image and image["placement"] == "main"):
        raise ValueError("concept %s: an image concept needs image=IMG(..., placement='main')" % key)
    if role in ("hook", "review") and items:
        raise ValueError("concept %s: a %s concept holds no NCERT questions" % (key, role))
    if len(examples) > 1:
        raise ValueError("concept %s: at most one plan example" % key)
    if enrichment is None:
        enrichment = role == "hook"
    return {"key": key, "kind": "teach", "role": role, "name": name, "bloom": bloom, "objective": objective,
            "textbook": list(textbook), "teach": list(teach), "examples": list(examples), "ncert": list(ncert),
            "key_terms": list(key_terms), "misconceptions": list(misconceptions), "enrichment": enrichment,
            "minutes": minutes, "video": video, "image": image, "items": list(items),
            "review_covers": list(review_covers)}


def DOER(key, name, tool, bloom, objective, *, applies_to, role="tool", recap=(), items=(), textbook=(), ncert=(),
         misconceptions=(), enrichment=None, minutes=6, key_terms=()):
    """The tool concept: ONE tool, placed right after the concept it applies to (role "tool") or right after the hook
    (role "explore"). `tool` is a key of TOOLS (tools_N.py); the approved tool's name, purpose and number come from the
    content team's table, never from here. `items` are the NCERT questions of that concept, nothing else.
    name   what the child sees, usually the tool's own name
    """
    if role not in ("tool", "explore"):
        raise ValueError("concept %s: a tool concept's role is tool or explore" % key)
    if enrichment is None:
        enrichment = role == "explore"
    return {"key": key, "kind": "doer", "role": role, "name": name, "tool": tool, "bloom": bloom,
            "objective": objective, "applies_to": applies_to, "recap": list(recap), "items": list(items),
            "textbook": list(textbook), "ncert": list(ncert), "misconceptions": list(misconceptions),
            "enrichment": enrichment, "minutes": minutes, "key_terms": list(key_terms)}


def TOPIC(key, module, name, sections, bloom, objective, summary, concepts, *, topic_type="instructional",
          key_terms=()):
    """topic_type: "framing" (the opening: hook video + exploration tool, exactly one, no objective), "instructional"
    (an idea topic: concept video -> tool, repeated where it adds value) or "summary" (the review, exactly one, last,
    no objective)."""
    if topic_type not in ("framing", "instructional", "summary"):
        raise ValueError("topic %s: topic_type must be framing, instructional or summary" % key)
    return {"key": key, "module": module, "name": name, "ncert_sections": list(sections), "bloom": bloom,
            "objective": objective, "summary": summary, "concepts": list(concepts), "topic_type": topic_type,
            "key_terms": list(key_terms)}


def T(tool_id, title, approved_no, learning_objective, *, subtype="manipulative", screen="", controls=(),
      instruction="", notice=(), feedback=(), done_when="", shared_state=(), misconceptions=(), hints=(),
      visuals=()):
    """One tool spec ("spec + placeholder": the tool itself is built elsewhere).

    title             EXACTLY the approved tool name from the content team's table
    approved_no       its number in the approved sequence (1 is the exploration tool)
    learning_objective  ONE objective, one short sentence
    screen            what is on screen, plainly (large visuals, nothing decorative)
    controls          the simple controls, at most 4
    instruction       what the child reads on screen, at most 15 words
    notice            2 or 3 "what do you notice?" prompts, for an exploration tool only
    feedback          what the child sees for a right and a wrong try, in words that explain the result
    hints             exactly 4: orienting, strategic, specific, bottom-out (or none until the briefs stage)
    visuals           keys of content.VISUAL_KEY used, so a shape or object looks the same across the chapter
    The tool's questions are NOT written here: they are the NCERT items (FIO) of its concept, so a tool never carries
    an unrelated, extra or advanced question.
    """
    if hints and len(hints) != 4:
        raise ValueError("tool %s: give exactly 4 hints (orienting, strategic, specific, bottom-out) or none yet" % title)
    return {"tool_id": tool_id, "title": title, "subtype": subtype, "approved_no": approved_no,
            "learning_objective": learning_objective, "screen": screen, "controls": list(controls),
            "instruction": instruction, "notice": list(notice), "feedback": list(feedback), "done_when": done_when,
            "shared_state": list(shared_state), "misconceptions": list(misconceptions),
            "hint_ladder": [{"rung": r, "text": t} for r, t in
                            zip(("orienting", "strategic", "specific", "bottom-out"), hints)],
            "visuals": list(visuals)}

# -*- coding: utf-8 -*-
"""Placeholder media nodes for a Class 3/4 plan: story videos and real-life images.

Class 3-4 media are made in other folders. The plan carries one placeholder node per planned video or image, with a
reserved id and url and the brief the media team needs (`build_status: "placeholder"`, nothing rendered). A tool node
comes from tools_spec/tool_node_builder.py. This module replaces the Class 6-8 video-script and image-spec machinery,
which is not part of this pipeline.

    video_node(...)   a hook video or a concept video: a STORY with the chapter's characters, never a lecture
    image_node(...)   one clean real-life image: it adds a real-life example or visual reference, or it is not made
"""
from __future__ import annotations

VIDEO_INSTRUCTION = "Watch the story. When it asks you a question, think and say your answer before you go on."

IMAGE_NEGATIVE = (
    "clutter, crowded scenes, decorative borders, ornaments or mascots that carry no information, unrelated objects, "
    "watermarks, signatures, logos, stock-photo look; any text that is not listed, garbled or misspelled words, "
    "invented digits; any board name, publisher name, book title, page number or curriculum branding; scary or unsafe "
    "scenes; distorted hands or faces; a hyphen used as a minus sign")

IMAGE_STYLES = {
    "photo": "A clean, bright, well-lit photograph",
    "illustration": "A clean, simple, flat-colour illustration with soft shapes",
}


def story_summary(kind, brief):
    """One readable paragraph of a story brief, for the node's teaching_notes."""
    b = brief or {}
    who = ", ".join(b.get("characters") or []) or "the chapter's characters"
    parts = ["%s in %s." % (who, b.get("setting") or "the chapter's setting"), b.get("situation") or ""]
    if kind == "hook":
        if b.get("open_question"):
            parts.append("It ends on an open question: %s" % b["open_question"])
    else:
        if b.get("problem"):
            parts.append("The problem: %s" % b["problem"])
        if b.get("thread"):
            parts.append("The story thread: %s" % b["thread"])
        if b.get("leads_to"):
            parts.append("It leads into: %s" % b["leads_to"])
    return " ".join(p for p in parts if p).strip()


def video_node(media_id, concept_id, kind, title, purpose, new_idea, brief, target_seconds, *, asset_base,
               source_key, chapter_label, previous_video_id=None):
    """A placeholder story video. kind is "hook" or "concept"."""
    role_text = ("Hook video: it opens the chapter with a story and introduces the situation, not the lesson."
                 if kind == "hook" else
                 "Concept video: a story that continues the chapter's thread and explains ONE concept: %s." % new_idea)
    node = {
        "id": media_id,
        "type": "video",
        "subtype": "story",
        "title": title,
        "context": "%s. %s PLACEHOLDER: briefed, not rendered yet." % (chapter_label, role_text),
        "description": purpose,
        "concept_id": concept_id,
        "home_concept_id": concept_id,
        "aspect_ratio": "16:9",
        "video_url": "",
        "planned_url": "%s/video_v3/%s.mp4" % (asset_base, media_id),
        "video_duration_seconds": "0",
        "teaching_notes": story_summary(kind, brief),
        "instructions_for_student": VIDEO_INSTRUCTION,
        "related_concept_ids": [],
        "video_role": kind,
        "video_kind": kind,
        "purpose": purpose,
        "new_idea": new_idea if kind == "concept" else "",
        "story_brief": dict(brief or {}),
        "target_seconds": target_seconds,
        "interactive": False,
        "interaction_points": [],
        "source_video_key": source_key,
        "build_status": "placeholder",
        "serves_items": [],
    }
    if previous_video_id:
        node["continues_from"] = previous_video_id
    return node


def image_prompt(style, real_life, shows, visuals):
    """The generation prompt: one clean real-life picture that makes the concept easy to notice."""
    lead = IMAGE_STYLES.get(style, IMAGE_STYLES["photo"])
    text = "%s of %s. It shows %s. One clear main subject, plain uncluttered background, large objects, nothing " \
           "that is not needed for the concept." % (lead, real_life or "a familiar everyday scene", shows or "the concept")
    if visuals:
        text += " Draw these the same way every time: %s." % ", ".join(visuals)
    return text + " No text unless a label is listed. No digits unless the concept needs them."


def image_node(media_id, concept_id, title, adds, *, placement, new_context, real_life, shows, caption, style,
               visuals, asset_base):
    """A placeholder real-life image. placement is "main" (in the learning flow, with its short caption) or
    "pinned" (supporting material kept beside a concept a video or tool already teaches)."""
    return {
        "id": media_id,
        "type": "image",
        "subtype": "generated",
        "title": title,
        "concept_id": concept_id,
        "home_concept_id": concept_id,
        "image_url": "",
        "planned_url": "%s/image_v3/%s.png" % (asset_base, media_id),
        "generation_prompt": image_prompt(style, real_life, shows, visuals),
        "labels": [],
        "negative_prompt": IMAGE_NEGATIVE,
        "accuracy_constraints": [
            "any object, person or place that is not part of the described real-life scene",
            "any text beyond the listed labels, or any listed label misspelled",
            "any board name, publisher name, book title, page number or curriculum branding",
        ],
        "description": "%s: %s" % (title, adds),
        "context": "PLACEHOLDER: briefed, not generated yet.",
        "teaching_notes": "Adds: %s Shows: %s" % (adds, shows),
        "image_role": placement,
        "image_category": "concept",
        "aspect_ratio": "16:9",
        "placement": placement,
        "adds": adds,
        "new_context": bool(new_context),
        "real_life": real_life,
        "shows": shows,
        "caption": caption,
        "style": style,
        "visuals": list(visuals or []),
        "build_status": "placeholder",
    }

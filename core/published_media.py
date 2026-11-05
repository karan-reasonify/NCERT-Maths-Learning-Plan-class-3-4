# -*- coding: utf-8 -*-
"""Keep already-published image assets through a rebuild.

A chapter builder writes every image as a placeholder (`image_url: ""`). When the live plan already carries built
images, uploading such a rebuild takes every picture off the page and still answers `success: true` (the Class 3
trap of 11 Sep 2026, met again on the phase-3 chapters on 29 Sep 2026). So each chapter pins its published image
nodes in `published_images.json`, keyed by the media id they hold in the NEW plan, and the builder swaps them in.

    python -B pipeline/published_media.py pull <chapter_id> <version> <plan.json> <out.json> [--map old=new ...]

pulls the built image nodes of a live version into a pin file, matched to the local plan by id (or by an explicit
old=new map when a restructure renumbered them; the asset url keeps the old id, which is fine).

    python -B pipeline/published_media.py pull-tools <chapter_id> <version> <plan.json> <out.json>

does the same for built tools (published_tools.json): every live tool whose .tsx exists and whose url differs
from the local placeholder.

    python -B pipeline/published_media.py pin-videos <chapter_id> <version> <plan.json>

writes, in place, every rendered video of a live version into the local plan (matched by id and script key):
its `video_url`, its `context` and the absence of `build_status`. Rendered videos were patched straight into the
live blob (6_ch3 v91, 9_ch5 v14 on 1 Oct 2026), so a rebuild would otherwise blank them. The script text of the
node stays local (a re-render follows the new script).
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request

API = "https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/chapter/"
KEEP_LOCAL = ("id", "concept_id", "home_concept_id")


def _media(plan):
    for m in plan["modules"]:
        for s in m["segments"]:
            for t in s["topics"]:
                for x in t["media"]:
                    yield t, x


def _no_dashes(o, key=""):
    """The plan may hold no en or em dash (a standing rule); published nodes sometimes do. Urls are left alone."""
    if isinstance(o, dict):
        return {k: _no_dashes(v, k) for k, v in o.items()}
    if isinstance(o, list):
        return [_no_dashes(v, key) for v in o]
    if isinstance(o, str) and not key.endswith("url"):
        return o.replace(" — ", ", ").replace("—", ", ").replace("–", " to ")
    return o


def load_pins(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)["images"]


def pin_images(plan, path):
    """Replace each local image node whose id is pinned with the published node (local id fields kept).
    Returns the pinned ids; raises if a pin names an image the plan does not have."""
    pins = load_pins(path)
    done = set()
    for t, x in list(_media(plan)):
        if x["type"] == "image" and x["id"] in pins:
            node = _no_dashes(dict(pins[x["id"]]))
            for k in KEEP_LOCAL:
                if k in x:
                    node[k] = x[k]
            t["media"][t["media"].index(x)] = node
            done.add(x["id"])
    missing = set(pins) - done
    if missing:
        raise SystemExit(f"published_images.json pins images the plan no longer has: {sorted(missing)}")
    return done


def load_tool_pins(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)["tools"]


def pin_tools(plan, path):
    """The same for built tools: a live tool node whose `.tsx` was uploaded (its 2d_tool_url, text and subtype set
    on the live plan) replaces the local placeholder of the same id. On 30 Sep 2026 six_ch3's 13 uploaded tools
    were patched into live Phase 2 v88 and a rebuild from local files dropped them; this keeps them."""
    pins = load_tool_pins(path)
    done = set()
    for t, x in list(_media(plan)):
        if x["type"] == "2d_tool" and x["id"] in pins:
            node = _no_dashes(dict(pins[x["id"]]))
            for k in KEEP_LOCAL:
                if k in x:
                    node[k] = x[k]
            t["media"][t["media"].index(x)] = node
            done.add(x["id"])
    missing = set(pins) - done
    if missing:
        raise SystemExit(f"published_tools.json pins tools the plan no longer has: {sorted(missing)}")
    return done


def _exists(url):
    i = url.find("/learning_plan_assets/")
    u = "https://storage.googleapis.com" + url[i:] if i >= 0 else url
    try:
        return urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30).status == 200
    except Exception:
        return False


def pull_tools(chapter_id, version, local_plan, out):
    """Pin every live tool node whose .tsx exists in the bucket and differs from the local placeholder."""
    d = json.load(urllib.request.urlopen(f"{API}{chapter_id}?version={version}", timeout=120))["data"]["plan"]
    live = d["planJson"]
    live = json.loads(live) if isinstance(live, str) else live
    with open(local_plan, encoding="utf-8") as f:
        local = json.load(f)
    local_tools = {x["id"]: x for _, x in _media(local) if x["type"] == "2d_tool"}
    pins = {}
    for _, x in _media(live):
        if x["type"] != "2d_tool" or x["id"] not in local_tools or not x.get("2d_tool_url"):
            continue
        if x["2d_tool_url"] != local_tools[x["id"]].get("2d_tool_url") and _exists(x["2d_tool_url"]):
            pins[x["id"]] = x
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"source": live.get("plan_id"), "tools": pins}, f, ensure_ascii=False, indent=1)
    print(f"pinned {len(pins)} built tools from {live.get('plan_id')} into {out}")


def is_pinned_built(x):
    return x.get("type") == "image" and x.get("build_status") == "built" and bool(x.get("image_url"))


def pull(chapter_id, version, local_plan, out, mapping):
    d = json.load(urllib.request.urlopen(f"{API}{chapter_id}?version={version}", timeout=120))["data"]["plan"]
    live = d["planJson"]
    live = json.loads(live) if isinstance(live, str) else live
    with open(local_plan, encoding="utf-8") as f:
        local = json.load(f)
    local_imgs = {x["id"]: x for _, x in _media(local) if x["type"] == "image"}
    pins = {}
    for _, x in _media(live):
        if x["type"] != "image" or not x.get("image_url"):
            continue
        new_id = mapping.get(x["id"], x["id"] if not mapping else None)
        if new_id is None or new_id not in local_imgs:
            continue
        pins[new_id] = x
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"source": live.get("plan_id"), "images": pins}, f, ensure_ascii=False, indent=1)
    print(f"pinned {len(pins)} of {sum(1 for _, x in _media(live) if x['type'] == 'image' and x.get('image_url'))} "
          f"built images from {live.get('plan_id')} into {out}")


def pin_videos(chapter_id, version, plan_path):
    d = json.load(urllib.request.urlopen(f"{API}{chapter_id}?version={version}", timeout=120))["data"]["plan"]
    live = d["planJson"]
    live = json.loads(live) if isinstance(live, str) else live
    with open(plan_path, encoding="utf-8") as f:
        plan = json.load(f)
    local = {x["id"]: x for _, x in _media(plan) if x["type"] == "video"}
    n = 0
    for _, x in _media(live):
        if x["type"] != "video" or not x.get("video_url"):
            continue
        y = local.get(x["id"])
        if y is None or y.get("source_video_key") != x.get("source_video_key"):
            raise SystemExit(f"{x['id']}: rendered live video has no matching local node; refusing")
        y["video_url"] = x["video_url"]
        y["context"] = x.get("context", y.get("context"))
        if "build_status" not in x:
            y.pop("build_status", None)
        n += 1
    with open(plan_path, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    print(f"pinned {n} rendered videos from {live.get('plan_id')} into {plan_path}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "pin-videos" and len(a) >= 4:
        pin_videos(a[1], a[2], a[3])
        raise SystemExit(0)
    if a and a[0] == "pull-tools" and len(a) >= 5:
        pull_tools(a[1], a[2], a[3], a[4])
        raise SystemExit(0)
    if not a or a[0] != "pull" or len(a) < 5:
        raise SystemExit(__doc__)
    mp = dict(x.split("=", 1) for x in a[a.index("--map") + 1:]) if "--map" in a else {}
    pull(a[1], a[2], a[3], a[4], mp)

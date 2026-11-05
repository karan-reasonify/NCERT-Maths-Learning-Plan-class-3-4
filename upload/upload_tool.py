#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload a 2d_tool's .tsx and .json to the learning_plan_assets bucket.

    python upload_tool.py <tool folder> [--base URL] [--dry-run]

ONLY the .tsx and the .json. No .preview.html, no dev previews: the bucket's own
convention across all thirty-six existing tool folders is those two files and
nothing else, and the plan references exactly those two urls.

The folder path is taken from the plan's `2d_tool_url` rather than assembled
from the grade and subject. Guessing the subject folder puts the file one
directory away from where the host will look for it, and the url 404s with
everything apparently uploaded fine.

The subject folder is `mathematics` for every asset type (user rule, 12 Sep
2026): `<class>/mathematics/ch_N/2dtool/` and `<class>/mathematics/ch_N/image/`.
The bucket used to split these - tools under `maths/`, images under
`mathematics/`. Class 3 and 4 were migrated on 12 Sep 2026; classes 6-10 still
carry the split. Reading the url off the plan is what makes either work.
"""
from __future__ import annotations

import io
import json
import mimetypes
import os
import sys
import urllib.request
import uuid

BUCKET = "learning_plan_assets"
PUBLIC = "https://media.singularity-learn.com"
DEFAULT_BASE = "https://staging.singularity-learn.com"

TYPES = {".tsx": "text/plain; charset=utf-8", ".json": "application/json"}
ALLOWED = (".tsx", ".json")


def folder_from_plan(plan_path, media_id):
    """The published folder, read off the plan's own 2d_tool_url."""
    plan = json.load(io.open(plan_path, encoding="utf-8"))
    url = None
    for mod in plan["modules"]:
        for seg in mod["segments"]:
            for top in seg["topics"]:
                for m in top.get("media", []):
                    if m.get("id") == media_id:
                        url = m.get("2d_tool_url")
    if not url:
        raise SystemExit("no 2d_tool_url for %s in %s" % (media_id, plan_path))
    # .../learning_plan_assets/V2/.../<MEDIA_ID>/<MEDIA_ID>.tsx
    key = url.split("/learning_plan_assets/", 1)[1]
    return os.path.dirname(key), url


def multipart(fields, files):
    """fields: [(name, value)]  files: [(name, filename, ctype, bytes)]"""
    b = "----tool" + uuid.uuid4().hex
    out = io.BytesIO()
    def w(s):
        out.write(s.encode("utf-8") if isinstance(s, str) else s)
    for name, value in fields:
        w("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n" % (b, name, value))
    for name, fn, ctype, data in files:
        w("--%s\r\nContent-Disposition: form-data; name=\"%s\"; filename=\"%s\"\r\n"
          "Content-Type: %s\r\n\r\n" % (b, name, fn, ctype))
        w(data)
        w("\r\n")
    w("--%s--\r\n" % b)
    return "multipart/form-data; boundary=%s" % b, out.getvalue()


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    dry = "--dry-run" in argv
    base = DEFAULT_BASE
    for a in argv:
        if a.startswith("--base="):
            base = a.split("=", 1)[1]
    if not args:
        print(__doc__)
        return 2
    folder = os.path.abspath(args[0])
    media_id = os.path.basename(folder.rstrip("\\/"))
    plan = args[1] if len(args) > 1 else None
    if not plan:
        raise SystemExit("pass the plan json as the second argument")

    key_dir, url = folder_from_plan(plan, media_id)

    picked = []
    for name in sorted(os.listdir(folder)):
        ext = os.path.splitext(name)[1].lower()
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        if ext not in ALLOWED:
            print("   skip  %s" % name)
            continue
        if not name.startswith(media_id):
            print("   skip  %s  (not named by the media id)" % name)
            continue
        picked.append((name, path))

    print("tool      %s" % media_id)
    print("bucket    %s" % BUCKET)
    print("folder    %s" % key_dir)
    print("endpoint  %s/agentapi/api/topics/upload" % base)
    print("plan url  %s" % url)
    for name, path in picked:
        print("   send   %-34s %8d bytes" % (name, os.path.getsize(path)))
    if not picked:
        raise SystemExit("nothing to send")
    if dry:
        print("\nDRY RUN: nothing sent.")
        return 0

    files = []
    for name, path in picked:
        ext = os.path.splitext(name)[1].lower()
        ctype = TYPES.get(ext) or mimetypes.guess_type(name)[0] or "application/octet-stream"
        files.append(("files", name, ctype, io.open(path, "rb").read()))
    ctype, body = multipart([("folder_name", key_dir), ("bucket_name", BUCKET)], files)
    req = urllib.request.Request(base + "/agentapi/api/topics/upload", data=body,
                                 headers={"Content-Type": ctype})
    with urllib.request.urlopen(req, timeout=180) as r:
        code = r.getcode()
        payload = r.read().decode("utf-8", "replace")
    print("\n   http %s, sent %.1f KB" % (code, len(body) / 1024.0))
    try:
        data = json.loads(payload)
    except ValueError:
        print(payload[:2000])
        return 1
    print(json.dumps(data, indent=2)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

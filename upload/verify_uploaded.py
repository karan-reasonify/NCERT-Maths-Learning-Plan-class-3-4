#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""READ ONLY. Prove what the database serves for a plan that was just uploaded.

    python verify_uploaded.py <plan.json> [<plan.json> ...]

Re-derives everything from the stored blob instead of trusting the upload's own
reply: exactly one active version, and the blob equal to the file leaf for leaf.
`_activate` is expected to differ, because `?activate=true` sets it.

Uses this pipeline's own `core/config.py`, which reads `.env`/`config.json` at this
pipeline's root - no path back into any other checkout is needed. A plan can be
anywhere on disk; only the database connection is fixed, to this pipeline's own.
"""
from __future__ import annotations

import io
import json
import os
import sys

EXPECTED_DIFF = {"._activate"}

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))


def diff(a, b, path="", out=None):
    """Every leaf where the file (a) and the served blob (b) disagree."""
    if out is None:
        out = []
    if len(out) > 200:
        return out
    if type(a) is not type(b):
        out.append(path or ".")
    elif isinstance(a, dict):
        for key in sorted(set(a) | set(b)):
            if key not in a or key not in b:
                out.append("%s.%s" % (path, key))
            else:
                diff(a[key], b[key], "%s.%s" % (path, key), out)
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append("%s[len %d vs %d]" % (path, len(a), len(b)))
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                diff(x, y, "%s[%d]" % (path, i), out)
    elif a != b:
        out.append(path)
    return out


def main(paths):
    if not paths:
        print(__doc__)
        return 2
    from core import config

    dest = config.destination(None)
    conn = config.connect(readonly=True)
    cur = config.cursor(conn)

    bad = 0
    for path in paths:
        plan = json.load(io.open(path, encoding="utf-8"))
        cid = plan.get("chapter_id")
        cur.execute("SELECT plan_id, version, is_active, is_draft, phase, status "
                    "FROM {p} WHERE chapter_id = %s ORDER BY version"
                    .format(p=dest.plans), (cid,))
        rows = cur.fetchall()
        active = [r for r in rows if r["is_active"]]
        print("%s  %d version(s) in %s" % (cid, len(rows), dest.plans))
        if len(active) != 1:
            print("   FAIL  %d active version(s), expected exactly 1" % len(active))
            bad += 1
            if not active:
                continue
        row = active[0]

        cur.execute("SELECT raw_json FROM {b} WHERE plan_id = %s"
                    .format(b=dest.blobs), (row["plan_id"],))
        blob = cur.fetchone()
        if blob is None:
            print("   FAIL  %s has a plan row and NO BLOB" % row["plan_id"])
            bad += 1
            continue
        served = blob["raw_json"]
        if isinstance(served, (str, bytes)):
            served = json.loads(served)

        print("   live  %s  version %s  active=%s  draft=%s  phase %s  status %s"
              % (row["plan_id"], row["version"], row["is_active"], row["is_draft"],
                 row["phase"], row["status"]))
        unexpected = [d for d in diff(plan, served) if d not in EXPECTED_DIFF]
        if unexpected:
            print("   FAIL  the blob differs from the file at %d leaf(s):"
                  % len(unexpected))
            for leaf in unexpected[:15]:
                print("           %s" % leaf)
            bad += 1
        else:
            print("   ok    the blob matches the file")

    conn.close()
    print()
    print("PUBLISHED: %s" % ("clean" if not bad else "%d problem(s)" % bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

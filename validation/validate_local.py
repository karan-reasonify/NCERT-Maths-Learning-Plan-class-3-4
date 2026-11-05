#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_local.py - the local validation gate; writes the stamp upload_lp.py requires.

    python validation/validate_local.py <plan.json> [<chapter.config.json>]

chapter.config.json defaults to the file of that name next to the plan. Its
chapter_master_id/phase (if present) must agree with the plan's own, so a stamp can never be
produced by validating the right plan against the wrong chapter's config.

Runs gates.gate_runner against the plan exactly as it sits on disk. On zero errors, writes
`<plan>.stamp.json` (see STAMP_FORMAT.md) hashing the plan file's own bytes - not a
re-serialization - so the stamp can only ever match the file that produced it. The stamp also
records the config's own sha256, so a later swap of chapter.config.json (e.g. to a looser
eqcheck variant) invalidates it too. On any error, removes a stale stamp if one exists and
exits 1: there must never be a stamp for a plan that is not currently clean.

This must run AFTER core/set_version.py (and core/published_media.py pin-* if the chapter is
being rebuilt over live assets) - anything that changes the plan's bytes after this runs makes
the stamp stale. See STAMP_FORMAT.md for the required order.
"""
from __future__ import annotations

import datetime
import hashlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from gates import gate_runner  # noqa: E402


def stamp_path(plan_path):
    return plan_path + ".stamp.json"


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan_path = sys.argv[1]
    config_path = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(os.path.dirname(os.path.abspath(plan_path)), "chapter.config.json")
    if not os.path.exists(config_path):
        print("REFUSED: no chapter.config.json found (looked at %s) - pass it explicitly "
              "as a second argument if it lives elsewhere" % config_path)
        return 2

    with io.open(plan_path, "rb") as f:
        raw = f.read()
    plan = json.loads(raw.decode("utf-8"))
    with io.open(config_path, "rb") as f:
        config_raw = f.read()
    config = json.loads(config_raw.decode("utf-8"))

    config_problem = None
    if config.get("chapter_master_id") not in (None, plan.get("chapter_master_id")):
        config_problem = "chapter.config.json chapter_master_id %r disagrees with the plan's %r" \
            % (config.get("chapter_master_id"), plan.get("chapter_master_id"))
    elif config.get("phase") not in (None, plan.get("phase")):
        config_problem = "chapter.config.json phase %r disagrees with the plan's %r" \
            % (config.get("phase"), plan.get("phase"))
    if config_problem:
        print("REFUSED: %s - one of the two is wrong; fix it before validating" % config_problem)
        return 2

    errors, counts = gate_runner.run(plan, config)
    warnings = counts.pop("warnings", [])

    sp = stamp_path(plan_path)
    if errors:
        if os.path.exists(sp):
            os.remove(sp)
        print("%d GATE FAILURE(S) - no stamp written, %s removed if it existed:" % (len(errors), sp))
        for e in errors:
            print("  -", e)
        return 1

    if warnings:
        # Advisory only - see gates/gate_runner.py's module docstring ("Blocking errors vs
        # advisory warnings"). Printed so a human sees them, but never blocks the stamp.
        print("%d ADVISORY WARNING(S) (non-blocking):" % len(warnings))
        for w in warnings:
            print("  ~", w)

    stamp = {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "config_path": os.path.abspath(config_path),
        "config_sha256": hashlib.sha256(config_raw).hexdigest(),
        "chapter_id": plan.get("chapter_id"),
        "chapter_master_id": plan.get("chapter_master_id"),
        "phase": plan.get("phase"),
        "version": plan.get("version"),
        "plan_id": plan.get("plan_id"),
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "gate_summary": {"errors": 0, "counts": counts, "warnings": warnings},
    }
    with io.open(sp, "w", encoding="utf-8") as f:
        json.dump(stamp, f, ensure_ascii=False, indent=1)
    print("all gates passed (%s); wrote %s" % (counts, sp))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""set_version.py - stamp a built Phase 2 plan with its final, live-checked version.

There is no _V3/to_phase2.py mirror step in this pipeline (the user does not use that
convention): build.py writes one plan, already in Phase 2 shape, and this script is the one
place that sets `version` and `plan_id` on it, reading the next free version off
`GET /agentapi/.../chapter/<chapter_id>/versions` so the local counter is never trusted alone.

This must run BEFORE validation/validate_local.py, since the stamp that script writes has to
hash the plan's FINAL bytes - run it after and the stamp can never match what gets uploaded.

    python core/set_version.py <plan.json> [--base-url URL] [--version N]

Without --version, asks the server for the live max version under this plan's chapter_id and
sets version = max + 1 (or 1 if the chapter has never been uploaded). With --version, uses
that number without asking the server (for a dry run / offline test).
"""
from __future__ import annotations

import argparse
import io
import json
import sys
import urllib.error
import urllib.request


class NoVersions(Exception):
    """Raised instead of silently returning 0 when the server's shape can't be parsed, or
    rows exist but none carry a usable version/phase - defaulting to 1 in that case could
    silently collide with a live version and get overwritten by --force."""


def live_max_version(base_url, chapter_id, phase, timeout=60):
    url = "%s/agentapi/api/lp2/learning-plans/chapter/%s/versions" % (base_url.rstrip("/"), chapter_id)
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return 0
        raise

    if isinstance(data, list):
        versions = data
    elif isinstance(data, dict):
        versions = data.get("versions") or data.get("data") or []
    else:
        raise NoVersions("unexpected /versions response shape: %r" % type(data))
    if not isinstance(versions, list):
        raise NoVersions("unexpected 'versions' field shape: %r" % type(versions))
    if not versions:
        return 0

    nums = [v.get("version") for v in versions
            if isinstance(v, dict) and v.get("phase") == phase and isinstance(v.get("version"), int)]
    if not nums:
        raise NoVersions(
            "%d version row(s) exist for %s but none matched phase %r (raw: %s) - "
            "pass --version explicitly once you've checked by hand what's live"
            % (len(versions), chapter_id, phase, json.dumps(versions)[:500]))
    return max(nums)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", help="built plan.json to stamp with a version, in place")
    ap.add_argument("--base-url", default="https://staging.singularity-learn.com")
    ap.add_argument("--version", type=int, help="use this version instead of asking the server")
    args = ap.parse_args()

    plan = json.load(io.open(args.plan, encoding="utf-8"))
    chapter_id = plan.get("chapter_id")
    phase = plan.get("phase")
    if not chapter_id or phase is None:
        print("REFUSED: plan carries no chapter_id/phase to version against")
        return 2

    if args.version is not None:
        version = args.version
    else:
        try:
            version = live_max_version(args.base_url, chapter_id, phase) + 1
        except NoVersions as err:
            print("REFUSED: %s" % err)
            return 2
        print("live max version for %s phase %s: %d -> using %d" % (chapter_id, phase, version - 1, version))

    plan["version"] = version if isinstance(plan.get("version", 0), int) else str(version)
    plan["plan_id"] = "%s_v%d" % (chapter_id, version)

    with io.open(args.plan, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    print("%s: plan_id=%s version=%s" % (args.plan, plan["plan_id"], plan["version"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

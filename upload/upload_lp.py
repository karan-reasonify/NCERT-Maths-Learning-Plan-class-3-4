#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload a learning plan to the LP2 agentapi endpoint, with a preflight.

    python upload_lp.py <plan.json> [<plan.json> ...] [options]

The endpoint takes `chapter_master_id` and `phase` as FORM FIELDS, not from the
JSON. That is this route's one silent failure: a wrong `chapter_master_id`
attaches good content to the wrong chapter and still answers `success: true`. So
by default both are read from the plan itself, and a `--chapter-master-id` given
on the command line must AGREE with the plan or nothing is sent.

HARD RULE: this refuses to upload a plan unless a fresh stamp file
(`<plan>.stamp.json`, written only by validation/validate_local.py) sits next to
it, its sha256 matches the plan's exact current bytes, and its chapter_master_id
and phase agree with this plan. --skip-preflight does NOT override this - local
validation is a mechanical gate, not an optional one. See validation/STAMP_FORMAT.md.

Stdlib only, so it runs on a bare Python from any directory.

Options
  --chapter-master-id N   assert this id (must equal the plan's own)
  --phase N              override the plan's phase
  --no-activate          upload without activating (activate=true is the default)
  --base-url URL         default https://staging.singularity-learn.com
  --dry-run              preflight and print what would be sent, send nothing
  --skip-preflight       upload even if preflight finds problems (the stamp check still applies)
  --timeout SECONDS      default 600

Exit 0 only when every plan uploaded with `success: true` and no
`validation_errors`.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import io
import json
import mimetypes  # noqa: F401  (kept: some environments need it initialised)
import os
import sys
import urllib.error
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from gates.media_content import preflight, summarise, walk_media, walk_topics  # noqa: E402,F401

PATH = "/agentapi/api/lp2/learning-plans/upload"
STAMP_MAX_AGE_SECONDS = 24 * 60 * 60


def stamp_problem(path, plan, phase):
    """None if <path>.stamp.json is fresh and agrees with this plan and the PHASE ACTUALLY
    BEING SENT (not necessarily plan["phase"] - --phase can override it, and the stamp must
    cover whatever bytes+phase combination is about to go out, not just what's on disk)."""
    sp = path + ".stamp.json"
    if not os.path.exists(sp):
        return "no stamp file (%s) - run validation/validate_local.py first" % sp
    try:
        stamp = json.load(io.open(sp, encoding="utf-8"))
    except ValueError as err:
        return "stamp file is not valid JSON: %s" % err

    with io.open(path, "rb") as f:
        raw = f.read()
    actual = hashlib.sha256(raw).hexdigest()
    if stamp.get("sha256") != actual:
        os.remove(sp)
        return "stamp sha256 does not match the plan's current bytes (stale, removed) - re-run validate_local.py"

    age = None
    try:
        stamped = __import__("datetime").datetime.fromisoformat(stamp.get("timestamp", ""))
        now = __import__("datetime").datetime.now(stamped.tzinfo or None)
        age = (now - stamped).total_seconds()
    except (ValueError, TypeError):
        pass
    if age is not None and age > STAMP_MAX_AGE_SECONDS:
        os.remove(sp)
        return "stamp is older than 24h (stale, removed) - re-run validate_local.py"

    if (stamp.get("gate_summary") or {}).get("errors"):
        return "stamp records %d gate failure(s) - this plan never passed validate_local.py" \
            % stamp["gate_summary"]["errors"]

    cfg_path = stamp.get("config_path")
    if cfg_path:
        if not os.path.exists(cfg_path):
            return "stamp's chapter.config.json (%s) no longer exists - re-run validate_local.py" % cfg_path
        with io.open(cfg_path, "rb") as f:
            cfg_actual = hashlib.sha256(f.read()).hexdigest()
        if stamp.get("config_sha256") != cfg_actual:
            os.remove(sp)
            return "chapter.config.json changed since the stamp was written (stale, removed) " \
                "- re-run validate_local.py"

    if stamp.get("chapter_master_id") != plan.get("chapter_master_id"):
        return "stamp chapter_master_id %r disagrees with the plan's %r - re-run validate_local.py" \
            % (stamp.get("chapter_master_id"), plan.get("chapter_master_id"))
    if stamp.get("phase") != phase:
        return "stamp phase %r disagrees with phase %r being sent - re-run validate_local.py " \
            "(a --phase override that was never validated is refused, not silently sent)" \
            % (stamp.get("phase"), phase)
    return None


# ---------------------------------------------------------------------- upload

def post(url, path, fields, timeout):
    """Multipart POST with no third-party dependency."""
    boundary = "----lp2-%s" % uuid.uuid4().hex
    with io.open(path, "rb") as handle:
        blob = handle.read()

    parts = []
    for name, value in fields.items():
        parts.append(
            ('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n'
             % (boundary, name, value)).encode("utf-8"))
    parts.append(
        ('--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\n'
         'Content-Type: application/json\r\n\r\n'
         % (boundary, os.path.basename(path))).encode("utf-8"))
    parts.append(blob)
    parts.append(("\r\n--%s--\r\n" % boundary).encode("utf-8"))
    body = b"".join(parts)

    request = urllib.request.Request(url, data=body, method="POST")
    request.add_header("Content-Type", "multipart/form-data; boundary=%s" % boundary)
    request.add_header("Content-Length", str(len(body)))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8", "replace"), len(body)
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8", "replace"), len(body)


def report(answer):
    """Print what the endpoint actually did. `success` alone is not the verdict."""
    counts = answer.get("counts") or {}
    diff = answer.get("diff") or {}
    print("     %-9s %s  version %s  active=%s  draft=%s  phase %s"
          % (answer.get("action"), answer.get("plan_id"), answer.get("version"),
             answer.get("is_active"), answer.get("is_draft"), answer.get("phase")))
    if counts:
        print("     counts    " + "  ".join(
            "%s %s" % (k, counts[k]) for k in
            ("modules", "segments", "topics", "concepts", "objectives", "media")
            if k in counts))
    if diff:
        removed = diff.get("removed") or []
        print("     ids       %d added, %d removed, %d retained%s"
              % (len(diff.get("added") or []), len(removed),
                 diff.get("retained_count") or 0,
                 "" if not removed else "   <-- REMOVED ids are orphaned assets"))
    errors = answer.get("validation_errors") or []
    if errors:
        print("     VALIDATION ERRORS (%d):" % len(errors))
        for err in errors[:10]:
            print("       %s" % (err,))
    return bool(answer.get("success")) and not errors


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("plans", nargs="+", help="plan json file(s); globs accepted")
    ap.add_argument("--chapter-master-id", type=int,
                    help="assert this id; must equal the plan's own")
    ap.add_argument("--phase", type=int, help="override the plan's phase")
    ap.add_argument("--no-activate", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing plan version (force=true)")
    ap.add_argument("--base-url", default="https://staging.singularity-learn.com")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-preflight", action="store_true")
    ap.add_argument("--timeout", type=int, default=600)
    args = ap.parse_args()

    paths = []
    for pattern in args.plans:
        hits = sorted(glob.glob(pattern)) if any(c in pattern for c in "*?[") \
            else [pattern]
        if not hits:
            print("no file matches %r" % pattern)
            return 2
        paths.extend(hits)

    if args.chapter_master_id and len(paths) > 1:
        print("--chapter-master-id asserts ONE plan's id; %d given" % len(paths))
        return 2

    url = "%s%s?activate=%s%s" % (args.base_url.rstrip("/"), PATH,
                                  "false" if args.no_activate else "true",
                                  "&force=true" if args.force else "")

    # ----------------------------------------------------------- resolve first
    # `refused` and `unclean` are counted apart on purpose: --skip-preflight can
    # override the second and must never look like it overrides the first.
    jobs, refused, unclean = [], 0, 0
    for path in paths:
        if not os.path.isfile(path):
            print("%s  REFUSED: no such file" % path)
            refused += 1
            continue
        try:
            plan = json.load(io.open(path, encoding="utf-8"))
        except ValueError as err:
            print("%s  REFUSED: not valid JSON: %s" % (path, err))
            refused += 1
            continue

        master = plan.get("chapter_master_id")
        if args.chapter_master_id and args.chapter_master_id != master:
            print("%s  REFUSED: the plan carries chapter_master_id %r, you passed "
                  "%r. One of the two is wrong and uploading either way attaches "
                  "this content to the wrong chapter. Ask which id is right."
                  % (path, master, args.chapter_master_id))
            refused += 1
            continue
        if not master:
            print("%s  REFUSED: the plan carries no chapter_master_id, and this "
                  "endpoint will not read one from the JSON. Ask for the issued id."
                  % path)
            refused += 1
            continue

        phase = args.phase if args.phase is not None else plan.get("phase")
        if phase is None:
            print("%s  REFUSED: no phase in the plan and none given" % path)
            refused += 1
            continue
        if phase != 2:
            print("%s  REFUSED: phase %r requested - this pipeline builds and uploads Phase "
                  "2 only (no _V3/Phase 3 mirror step exists here)" % (path, phase))
            refused += 1
            continue

        bad_stamp = stamp_problem(path, plan, phase)
        if bad_stamp:
            print("%s  REFUSED: %s" % (path, bad_stamp))
            print("     --skip-preflight does NOT override this: local validation is a hard "
                  "rule, not an optional one. Run validation/validate_local.py first.")
            refused += 1
            continue

        problems = [] if args.skip_preflight else preflight(plan)
        jobs.append((path, plan, master, phase, problems))
        unclean += 1 if problems else 0

    # ------------------------------------------------------------- the summary
    print()
    print("%-46s %-8s %-6s %s" % ("plan", "master", "phase", "shape"))
    for path, plan, master, phase, problems in jobs:
        s = summarise(plan)
        print("%-46s %-8s %-6s %s"
              % (os.path.basename(path)[:46], master, phase,
                 "%d mod / %d top / %d con / %d obj / %d media (%d tools)"
                 % (s["modules"], s["topics"], s["concepts"], s["objectives"],
                    s["media"], s["tools"])))
        print("%-46s %s" % ("", plan.get("chapter_id")))
        for problem in problems:
            print("     PREFLIGHT  " + problem)
    print()
    print("-> %s" % url)

    if refused or unclean:
        print()
        print("NOTHING SENT.")
        if refused:
            print("  %d plan(s) refused: a missing file, unreadable JSON, or a "
                  "chapter_master_id that cannot be trusted. --skip-preflight "
                  "does NOT override this; the id has to be settled first."
                  % refused)
        if unclean:
            print("  %d plan(s) failed preflight. Fix them, or --skip-preflight "
                  "to upload as they are." % unclean)
        return 1
    if args.dry_run:
        print()
        print("DRY RUN: %d plan(s) would be uploaded." % len(jobs))
        return 0

    # ------------------------------------------------------------- the uploads
    print()
    good = 0
    for path, plan, master, phase, _ in jobs:
        print("%s  master=%s phase=%s" % (os.path.basename(path), master, phase))
        status, text, sent = post(url, path, {"chapter_master_id": str(master),
                                              "phase": str(phase)}, args.timeout)
        try:
            answer = json.loads(text)
        except ValueError:
            print("     http %s, unreadable reply: %s" % (status, text[:400]))
            continue
        print("     http %s, sent %.2f MB" % (status, sent / 1048576.0))
        if status >= 400:
            print("     FAILED: %s" % (answer.get("detail") or answer.get("message")
                                       or text[:300]))
            continue
        good += 1 if report(answer) else 0

    print()
    print("UPLOADED: %d of %d clean" % (good, len(jobs)))
    return 0 if good == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())

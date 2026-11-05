# -*- coding: utf-8 -*-
"""finalize_ids.py: give a built plan the id shapes the upload endpoint requires.

The Class 3/4 builder (chapter build.py) names each concept's objective "<concept id>.OBJ1" and keeps the review module's
author key "MLAST". The LP2 upload endpoint rejects that (found when Class 3 Ch 2 was first uploaded to staging):

    objectives[0]: expected objective_id='O1', got 'M1.S2.T2.C3.OBJ1'
    modules[3]: expected module_id='M4', got 'MLAST'

The Class 6 to 10 pipeline gets the same shape from core/qt.py (which renumbers the chapter). This pipeline has no question
topics, so this script does the same two things and nothing else:

    1. objectives become O1, O2, ... in list order; every reference to an old objective id is rewritten;
    2. modules become M1, M2, ... in list order; every id that starts with the old module id (segment, topic, concept,
       media id, review_covers, ncert_coverage keys, applies_to ...) gets the new prefix.

It is idempotent (a second run changes nothing) and rewrites the file in the build's own JSON format. Run it AFTER
`build.py` and BEFORE `core/set_version.py` and `validation/validate_local.py`: it changes the plan's bytes, so a stamp made
earlier is stale (validate_local.py makes a new one). A later `build.py` run writes the old ids again; run this again.

    python -I -X utf8 core/finalize_ids.py <plan.json>            rewrite in place, print what changed
    python -I -X utf8 core/finalize_ids.py <plan.json> --check    change nothing; exit 1 if the ids are not final yet

Never uploads and never touches the database.
"""
from __future__ import annotations

import io
import json
import sys


def _maps(plan):
    mod_map, obj_map = {}, {}
    for i, m in enumerate(plan.get("modules") or [], 1):
        want = "M%d" % i
        if m.get("module_id") != want:
            mod_map[m["module_id"]] = want
    for i, o in enumerate(plan.get("objectives") or [], 1):
        want = "O%d" % i
        if o.get("objective_id") != want:
            obj_map[o["objective_id"]] = want
    return mod_map, obj_map


def _fix_str(s, mod_map, obj_map):
    if s in obj_map:                       # whole-string objective ids first, on the ORIGINAL text
        return obj_map[s]
    for old, new in mod_map.items():       # then module prefixes: "MLAST", "MLAST.S9.T9.C17" ...
        if s == old or s.startswith(old + "."):
            return new + s[len(old):]
    return s


def _walk(x, mod_map, obj_map):
    if isinstance(x, dict):
        return {_fix_str(k, mod_map, obj_map): _walk(v, mod_map, obj_map) for k, v in x.items()}
    if isinstance(x, list):
        return [_walk(v, mod_map, obj_map) for v in x]
    if isinstance(x, str):
        return _fix_str(x, mod_map, obj_map)
    return x


def finalize(plan):
    """-> (new_plan, mod_map, obj_map). The input is not changed."""
    mod_map, obj_map = _maps(plan)
    if not mod_map and not obj_map:
        return plan, mod_map, obj_map
    return _walk(plan, mod_map, obj_map), mod_map, obj_map


def _check_final(plan):
    problems = []
    for i, m in enumerate(plan.get("modules") or [], 1):
        if m.get("module_id") != "M%d" % i:
            problems.append("modules[%d]: module_id %r, want 'M%d'" % (i - 1, m.get("module_id"), i))
    for i, o in enumerate(plan.get("objectives") or [], 1):
        if o.get("objective_id") != "O%d" % i:
            problems.append("objectives[%d]: objective_id %r, want 'O%d'" % (i - 1, o.get("objective_id"), i))
    return problems


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    check = "--check" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__)
        return 2
    path = paths[0]
    with io.open(path, encoding="utf-8") as f:
        plan = json.load(f)
    new_plan, mod_map, obj_map = finalize(plan)
    leftover = _check_final(new_plan)
    if leftover:
        print("ids still not final after renumbering: %s" % "; ".join(leftover[:5]))
        return 1
    if not mod_map and not obj_map:
        print("%s: ids are already final (%d modules, %d objectives)"
              % (path, len(plan.get("modules") or []), len(plan.get("objectives") or [])))
        return 0
    if check:
        print("%s: ids are NOT final: %d module id(s) and %d objective id(s) would change"
              % (path, len(mod_map), len(obj_map)))
        return 1
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(new_plan, f, ensure_ascii=False, indent=1)
    print("%s: renumbered %d module id(s) %s and %d objective id(s) (O1 to O%d)"
          % (path, len(mod_map), json.dumps(mod_map), len(obj_map), len(new_plan.get("objectives") or [])))
    return 0


if __name__ == "__main__":
    sys.exit(main())

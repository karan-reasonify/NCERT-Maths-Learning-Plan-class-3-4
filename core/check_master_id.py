#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_master_id.py - prove a plan's database keys before it is uploaded.

The one field that binds a plan to a chapter is `chapter_master_id`, and it is a
database key: getting it wrong attaches good content to the wrong chapter, which
looks like a successful upload and is not.

`chapter_id` is what the plan tables are keyed by. `chapter_master_id` is what the
plan must CARRY so it hangs off the right row of `lp2_chapters`. This checks the
second against the first, live.

    python core/check_master_id.py <plan.json> [<plan.json> ...]

The DSN and the chapter table come from `core/config.py`, which reads this
folder's own `.env` and defaults to the lpv2 destination. Read only; never
writes anything. Exits 1 on any disagreement.
"""
from __future__ import annotations

import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from core import config  # noqa: E402

CHECKED = ("chapter_master_id", "subject_ref_id", "medium_id")


def chapter_row(cur, chapter_id, dest):
    cur.execute("SELECT * FROM {chapters} WHERE chapter_id = %s"
                .format(chapters=dest.chapters), (chapter_id,))
    return cur.fetchone()


def master_row(cur, chapter_master_id):
    """The product's own chapter record, which issues chapter_master_id.

    A chapter can hold correct keys and still have no row in the plan store's
    chapter table, because that one is only written when a plan first lands.
    """
    if chapter_master_id is None:
        return None
    cur.execute('SELECT "ChapterId", "ChapterName", "SubjectId", "ChapterNumber", '
                '"MediumId", "IsActive" FROM "chapterMaster" WHERE "ChapterId" = %s',
                (chapter_master_id,))
    return cur.fetchone()


def fall_back_to_master(cur, plan, chapter_id, dest):
    master = master_row(cur, plan.get("chapter_master_id"))
    print("   PENDING  no %s row for %r, so there is no live version to supersede"
          % (dest.chapters, chapter_id))
    if master is None:
        print("   FAIL  chapter_master_id %r is not in chapterMaster either"
              % plan.get("chapter_master_id"))
        return False
    ok = master["SubjectId"] == plan.get("subject_ref_id")
    print("   %-4s chapterMaster %s = %r, SubjectId %s, chapter %s%s"
          % ("ok" if ok else "FAIL", master["ChapterId"], master["ChapterName"],
             master["SubjectId"], master["ChapterNumber"],
             "" if master["IsActive"] else "  (INACTIVE)"))
    if not ok:
        print("   FAIL  subject_ref_id: plan %s, chapterMaster %s"
              % (plan.get("subject_ref_id"), master["SubjectId"]))
    return ok


def check_plan(cur, path, dest):
    plan = json.load(io.open(path, encoding="utf-8"))
    chapter_id = plan.get("chapter_id")
    print("%s" % path)
    if not chapter_id:
        print("   FAIL  the plan carries no chapter_id")
        return 1, 0

    row = chapter_row(cur, chapter_id, dest)
    if row is None:
        return (0 if fall_back_to_master(cur, plan, chapter_id, dest) else 1), 1

    print("   chapter_id  %s  (%s, grade %s, chapter %s)"
          % (chapter_id, row["chapter_name"], row["grade"], row["chapter_number"]))
    bad = 0
    for key in CHECKED:
        mine, live = plan.get(key), row[key]
        ok = mine == live
        bad += 0 if ok else 1
        print("   %-4s %-18s plan %-6s live %-6s"
              % ("ok" if ok else "FAIL", key, mine, live))
    return bad, 0


def main():
    plans = sys.argv[1:]
    if not plans:
        print(__doc__)
        return 2
    dest = config.destination()
    conn = config.connect(readonly=True)
    cur = config.cursor(conn)
    bad = pending = 0
    for path in plans:
        disagreements, unregistered = check_plan(cur, path, dest)
        bad += disagreements
        pending += unregistered
    conn.close()

    print()
    print("MASTER IDS: %s%s"
          % ("clean" if not bad else "%d disagreement(s)" % bad,
             "" if not pending else
             ", %d chapter(s) not yet registered in %s" % (pending, dest.chapters)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

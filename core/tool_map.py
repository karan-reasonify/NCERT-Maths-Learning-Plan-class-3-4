# -*- coding: utf-8 -*-
"""Lock the approved tool map: read the content team's tool table and write it into chapter.config.json.

The curriculum / content team decides the tools, their names, their purposes and their sequence. This pipeline never
adds, drops, renames or reorders them. The table is pasted into `tool_map.md` in the chapter folder (any markdown
table is fine as long as each tool appears as "Tool N: Name" in one cell, as in the Class 5 priority document, or the
table has a "Tool" / "Name" column plus a "Purpose" / "Learning focus" column).

    python -I -X utf8 core/tool_map.py parse  <chapter>/tool_map.md          print what was read, change nothing
    python -I -X utf8 core/tool_map.py lock   <chapter>/tool_map.md          write "approved_tools" into the config
    python -I -X utf8 core/tool_map.py verify <chapter>/tool_map.md          is the config still the table? (exit 1 if not)

Each tool becomes {"no", "name", "purpose", "flow_row"}: `purpose` is the longest text the table gives for that tool
(the row of the learning flow), `flow_row` the topic name that row has. Read the result yourself: a table the parser
cannot read is a question for the user, not something to guess.
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

TOOL_CELL = re.compile(r"^\s*(?:tool\s*(\d+)\s*[:.\-)]\s*)(.+?)\s*$", re.I)


def _cells(line):
    line = line.strip()
    if not line.startswith("|"):
        return None
    cells = [c.strip() for c in line.strip("|").split("|")]
    if all(re.fullmatch(r":?-{2,}:?", c) or not c for c in cells):
        return None                       # the |---|---| separator row
    return cells


def parse(text):
    """-> list of {"no", "name", "purpose", "flow_row"} sorted by tool number. Raises ValueError when unreadable."""
    found = {}
    header = None
    for line in text.splitlines():
        cells = _cells(line)
        if cells is None:
            if not line.strip().startswith("|"):
                header = None
            continue
        low = [c.lower() for c in cells]
        if header is None and any("tool" in c or c == "name" for c in low) and \
                any(("purpose" in c or "focus" in c) for c in low):
            header = low
            continue
        hit = next(((i, TOOL_CELL.match(c)) for i, c in enumerate(cells) if TOOL_CELL.match(c)), None)
        if hit:
            i, m = hit
            no, name = int(m.group(1)), m.group(2).strip()
            after = [c for j, c in enumerate(cells) if j > i and c]
            rest = [c for j, c in enumerate(cells) if j != i and c]
            purpose = after[0] if after else (max(rest, key=len) if rest else "")
            flow = next((c for j, c in enumerate(cells) if j < i and c and not c.isdigit()), "")
            e = found.setdefault(no, {"no": no, "name": name, "purpose": "", "flow_row": ""})
            if len(purpose) > len(e["purpose"]):
                e["purpose"] = purpose
            if flow and not e["flow_row"]:
                e["flow_row"] = flow
    tools = [found[k] for k in sorted(found)]
    if not tools:
        raise ValueError("no tools found: write each tool as 'Tool N: Name' in a table cell with its purpose in "
                         "another cell of the same row")
    if [t["no"] for t in tools] != list(range(1, len(tools) + 1)):
        raise ValueError("tool numbers are not 1..N without gaps: %s" % [t["no"] for t in tools])
    empty = [t["no"] for t in tools if not t["purpose"]]
    if empty:
        raise ValueError("tool(s) %s have no purpose text in their table row" % empty)
    return tools


def _config_path(md_path):
    return os.path.join(os.path.dirname(os.path.abspath(md_path)), "chapter.config.json")


def main(argv):
    if len(argv) != 3 or argv[1] not in ("parse", "lock", "verify"):
        print(__doc__)
        return 2
    cmd, md = argv[1], argv[2]
    with io.open(md, encoding="utf-8") as f:
        tools = parse(f.read())
    if cmd == "parse":
        for t in tools:
            print("Tool %d: %s\n    row: %s\n    purpose: %s" % (t["no"], t["name"], t["flow_row"], t["purpose"]))
        return 0
    cp = _config_path(md)
    with io.open(cp, encoding="utf-8") as f:
        cfg = json.load(f)
    if cmd == "lock":
        cfg["approved_tools"] = tools
        with io.open(cp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
        print("locked %d approved tool(s) into %s" % (len(tools), cp))
        return 0
    have = [{k: t.get(k) for k in ("no", "name", "purpose")} for t in cfg.get("approved_tools") or []]
    want = [{k: t[k] for k in ("no", "name", "purpose")} for t in tools]
    if have != want:
        print("MISMATCH: chapter.config.json approved_tools differs from %s" % md)
        return 1
    print("approved_tools in the config match %s (%d tools)" % (md, len(tools)))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    try:
        sys.exit(main(sys.argv))
    except ValueError as e:
        sys.stderr.write("NEEDS INPUT: %s\n" % e)
        sys.exit(2)

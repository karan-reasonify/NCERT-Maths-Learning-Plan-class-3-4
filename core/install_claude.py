# -*- coding: utf-8 -*-
"""Install the /lp34 skill and the c34-* agents where Claude Code can see them.

Claude Code loads project skills and agents only from the `.claude/` folder of the folder it was OPENED in. This pipeline keeps
them in its own `.claude/`, so they are available when Claude Code is opened in this folder. To use them from a parent folder
(for example the workspace /root/maths-learning-plan) or from anywhere, install a copy:

    python3 core/install_claude.py --workspace /root/maths-learning-plan    copy into <folder>/.claude/
    python3 core/install_claude.py --user                                   copy into ~/.claude/ (every project)
    python3 core/install_claude.py --workspace <folder> --uninstall         remove exactly what was installed
    python3 core/install_claude.py --status                                 where is it installed, and is it current?

What is copied: .claude/skills/lp34/SKILL.md and .claude/agents/c34-*.md. In the installed SKILL.md the line
`<!-- PIPELINE_ROOT -->` becomes the absolute path of this pipeline, so the skill works whatever the session's directory is.
The originals here stay the single source of truth: edit them, then run this again. Restart the Claude Code session afterwards if
the skill does not show up (skills and agents are read when a session starts).
"""
from __future__ import annotations

import argparse
import glob
import io
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, ".claude")
MARK = "<!-- PIPELINE_ROOT -->"


def _rendered_skill():
    with io.open(os.path.join(SRC, "skills", "lp34", "SKILL.md"), encoding="utf-8") as f:
        text = f.read()
    return text.replace(MARK, "**Pipeline root (absolute path, installed by core/install_claude.py): `%s`. `cd` there before "
                              "every command.**" % ROOT.replace("\\", "/"))


def _agent_files():
    return sorted(glob.glob(os.path.join(SRC, "agents", "c34-*.md")))


def _targets(dest_claude):
    out = [(os.path.join(dest_claude, "skills", "lp34", "SKILL.md"), _rendered_skill())]
    for p in _agent_files():
        with io.open(p, encoding="utf-8") as f:
            out.append((os.path.join(dest_claude, "agents", os.path.basename(p)), f.read()))
    return out


def _read(path):
    try:
        with io.open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def install(dest_claude):
    n = 0
    for path, text in _targets(dest_claude):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        n += 1
    print("installed %d file(s) into %s (1 skill, %d agents)" % (n, dest_claude, n - 1))


def uninstall(dest_claude):
    n = 0
    for path, _ in _targets(dest_claude):
        if os.path.exists(path):
            os.remove(path)
            n += 1
    skill_dir = os.path.join(dest_claude, "skills", "lp34")
    if os.path.isdir(skill_dir) and not os.listdir(skill_dir):
        os.rmdir(skill_dir)
    print("removed %d file(s) from %s" % (n, dest_claude))


def status(places):
    for label, dest in places:
        if os.path.abspath(dest) == os.path.abspath(SRC):
            print("%-34s source of truth (%d agents + 1 skill); available when Claude Code is opened in %s"
                  % (label, len(_agent_files()), ROOT))
            continue
        t = _targets(dest)
        have = [(p, _read(p)) for p, _ in t]
        present = sum(1 for _, c in have if c is not None)
        current = sum(1 for (p, want), (_, c) in zip(t, have) if c == want)
        print("%-34s %s  (%d of %d files present, %d current)"
              % (label, "installed" if present == len(t) and current == len(t) else
                 "STALE or partial" if present else "not installed", present, len(t), current))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workspace", help="the folder Claude Code is opened in; installs into <folder>/.claude/")
    ap.add_argument("--user", action="store_true", help="install into ~/.claude/ (every project)")
    ap.add_argument("--uninstall", action="store_true")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args(argv)
    if not (a.workspace or a.user or a.status):
        ap.print_help()
        return 2
    places = []
    if a.workspace:
        places.append(("workspace " + os.path.abspath(a.workspace), os.path.join(os.path.abspath(a.workspace), ".claude")))
    if a.user:
        places.append(("user ~/.claude", os.path.join(os.path.expanduser("~"), ".claude")))
    if a.status:
        places = places or [("pipeline folder (original)", SRC)]
        status(places)
        return 0
    for label, dest in places:
        if os.path.abspath(dest) == os.path.abspath(SRC):
            print("%s is this pipeline's own .claude/: nothing to install" % label)
            continue
        (uninstall if a.uninstall else install)(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())

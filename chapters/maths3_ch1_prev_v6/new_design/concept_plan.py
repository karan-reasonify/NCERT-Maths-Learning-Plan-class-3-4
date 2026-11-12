# -*- coding: utf-8 -*-
"""The chapter's modules -> topics -> concepts and its tool specs, gathered from the topic and tool files.

Write the chapter in `topics_1.py`, `topics_2.py`, ... (each defines a list TOPICS) and `tools_1.py`, `tools_2.py`, ...
(each defines a dict TOOLS), using the helpers of `topics_common.py`. This file only collects them in natural order, so
adding `topics_3.py` needs no edit here. build.py reads CP.TOPICS and CP.TOOLS.
"""
from __future__ import annotations

import glob
import importlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def _natural(path):
    return [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", os.path.basename(path))]


def _modules(prefix):
    return [importlib.import_module(os.path.basename(p)[:-3])
            for p in sorted(glob.glob(os.path.join(HERE, prefix + "_*.py")), key=_natural)]


TOPICS = []
for _m in _modules("topics"):
    TOPICS += getattr(_m, "TOPICS", [])

TOOLS = {}
for _m in _modules("tools"):
    for _k, _v in getattr(_m, "TOOLS", {}).items():
        if _k in TOOLS:
            raise SystemExit("tool key %r is defined twice (%s)" % (_k, _m.__name__))
        TOOLS[_k] = _v

# -*- coding: utf-8 -*-
"""Plain checker for numeric relation chains in authored text (no signs, no powers/roots).

Generalized from maths6_ch3/new_design/build.py's inline eval_side()/arithmetic_in_text().
Use this variant for a chapter whose numbers are all non-negative and whose chains never
need ² ³ ⁴ or √ (whole-number/fraction arithmetic chapters). For a chapter with negative
numbers use eqcheck_signed; for one with powers/roots/brackets use eqcheck_powers (and for
both signs and powers/roots, eqcheck_signed also understands those - it is the superset).

  * Only "a op b op c = d" chains with a literal "=" are checked; every side must contain a
    digit, and comma-grouped numbers (80,000) are read as one value.
  * × and ÷ bind before + and -, left to right; values are exact Fractions.
  * Chains that glue to a letter, a slash, or an open bracket on either side are algebra and
    are skipped, not trimmed and judged.

    python -B eqcheck_plain.py      run the self-test
"""
from __future__ import annotations

import re
from fractions import Fraction

CHAIN = re.compile(r"\d[\d,]*\d(?![\d/])|\d")
# "−" (U+2212) is the minus sign the authored text uses between numbers; a number followed on the same line by a
# capitalised unit word ("90 Tens", "4 Thousand") is a place-value phrase, not a plain number. A capitalised word on
# the next line ("... × 5, new line, a capital word") is a new sentence, so the chain is read in full.
EQ = re.compile(r"(?<![\w/(])(\d[\d,]*\d|\d)(?:\s*[-−+×÷=]\s*(?:\d[\d,]*\d|\d)(?![\w/])(?![ ][A-Z][a-z]))+")


def eval_side(expr):
    toks = re.findall(r"\d[\d,]*|[-−+×÷]", expr)
    vals = []
    for t in toks:
        vals.append(t if t in "-−+×÷" else Fraction(int(t.replace(",", ""))))
    out = [vals[0]]
    i = 1
    while i < len(vals):
        op, v = vals[i], vals[i + 1]
        if op == "×":
            out[-1] = out[-1] * v
        elif op == "÷":
            out[-1] = out[-1] / v
        else:
            out += [op, v]
        i += 2
    r = out[0]
    for j in range(1, len(out), 2):
        r = r + out[j + 1] if out[j] == "+" else r - out[j + 1]
    return r


def arithmetic_in_text(text):
    """Every 'a op b = c' chain in the text must be true. Returns (failures, count_checked)."""
    fails, n = [], 0
    # a lower-case "x" between spaced numbers is the times sign ("36 = 4 x 9")
    text = re.sub(r"(?<=\d)\s+x\s+(?=\d)", " × ", text or "")
    for m in EQ.finditer(text):
        s = m.group(0)
        if "=" not in s:
            continue
        parts = [p for p in s.split("=")]
        if any(not re.search(r"\d", p) for p in parts):
            continue
        vals = [eval_side(p) for p in parts]
        n += 1
        if any(v != vals[0] for v in vals):
            fails.append(s)
    return fails, n


def false_equations(text):
    """Same interface as eqcheck_signed/eqcheck_powers, so gate_runner can pick a module by name."""
    fails, _ = arithmetic_in_text(text)
    return fails


def count_checked(text):
    _, n = arithmetic_in_text(text)
    return n


# ------------------------------------------------------------------ self-test
_TRUE_TEXT = ["73 − 37 = 36", "9 + 16 = 25", "72 ÷ 2 = 36", "80,000 × 2 = 160,000", "3 + 4 × 2 = 11", "100 - 1 = 99"]
_FALSE_TEXT = ["3 + 4 = 8", "72 ÷ 2 = 35"]
_SKIP_TEXT = ["983 = 90 Tens + 83 Ones", "x = 4", "a/2 = 1", "(2 = 2"]


def selftest():
    errs = []
    for s in _TRUE_TEXT:
        fails, n = arithmetic_in_text(s)
        if fails or n != 1:
            errs.append(f"should be TRUE: {s!r} -> fails={fails} n={n}")
    for s in _FALSE_TEXT:
        fails, n = arithmetic_in_text(s)
        if not fails:
            errs.append(f"should be FALSE: {s!r} -> fails={fails} n={n}")
    for s in _SKIP_TEXT:
        fails, n = arithmetic_in_text(s)
        if n:
            errs.append(f"should be SKIPPED: {s!r} -> fails={fails} n={n}")
    return errs


if __name__ == "__main__":
    e = selftest()
    print(f"self-test: {len(_TRUE_TEXT)} true, {len(_FALSE_TEXT)} false, {len(_SKIP_TEXT)} skipped; {len(e)} problems")
    for x in e:
        print("  -", x)

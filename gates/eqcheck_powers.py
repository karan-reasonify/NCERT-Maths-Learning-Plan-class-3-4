# -*- coding: utf-8 -*-
"""Power- and root-aware checker for numeric relation chains in authored text (no leading signs).

Generalized from maths8_ch9/new_design/eqcheck.py. Understands ² ³ ⁴, √ (on a number or a
bracket), × ÷ / + − and brackets, and the relations = ≈ < > ≤ ≥ ≠. Values are Decimals at 60
digits, so √ and squares compare exactly enough to be trusted. Unlike eqcheck_signed, a chain
here may not START with a sign (there is no "−7 + 10 = 3" handling) - use eqcheck_signed for a
chapter that also has negative numbers, since it is the superset of this variant.

  * "=" must hold to 1e-40.       "≈" must hold to one unit of the last digit shown on its plain-number side.
  * A chain glued to a letter on either side ("c² = 2", "72 = 2a²", "2n²") is algebra and is skipped.
  * A chain that is the tail of an expression ("c = √2 ≈ 1.414": the part after "c =") is skipped.
  * Unparsable chains are skipped; list notation such as (3, 4, 5) never forms a chain (no relation).

    python -B eqcheck_powers.py      run the self-test
"""
from __future__ import annotations

import re
from decimal import Decimal, getcontext

getcontext().prec = 60

SUP = {"²": 2, "³": 3, "⁴": 4}
REL = "=≈<>≤≥≠"
OPS = "+-−×÷/*"
CHARS = r"0-9.√()²³⁴+\-−×÷/*=≈<>≤≥≠ "
CHAIN = re.compile(r"[0-9√(][" + CHARS + r"]*")


class Skip(Exception):
    pass


def _tokens(s):
    out, i = [], 0
    while i < len(s):
        ch = s[i]
        if ch == " ":
            i += 1
            continue
        m = re.match(r"\d+(?:\.\d+)?", s[i:])
        if m:
            out.append(("num", Decimal(m.group(0)), m.group(0)))
            i += len(m.group(0))
            continue
        if ch in SUP:
            out.append(("sup", SUP[ch], ch))
        elif ch == "√":
            out.append(("root", None, ch))
        elif ch in "()":
            out.append((ch, None, ch))
        elif ch in OPS:
            out.append(("op", {"−": "-", "×": "*", "÷": "/"}.get(ch, ch), ch))
        elif ch in REL:
            out.append(("rel", ch, ch))
        else:
            raise Skip(ch)
        i += 1
    return out


class _P:
    def __init__(self, toks):
        self.t, self.i = toks, 0

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else (None, None, None)

    def take(self):
        tok = self.peek()
        self.i += 1
        return tok

    def expr(self):
        v = self.term()
        while self.peek()[0] == "op" and self.peek()[1] in "+-":
            op = self.take()[1]
            w = self.term()
            v = v + w if op == "+" else v - w
        return v

    def term(self):
        v = self.factor()
        while True:
            k, val, _ = self.peek()
            if k == "op" and val in "*/":
                self.take()
                w = self.factor()
                if val == "/" and w == 0:
                    raise Skip("div0")
                v = v * w if val == "*" else v / w
            elif k in ("root", "(") or (k == "num" and False):
                v = v * self.factor()          # implicit product: 9√3, 2(…)
            else:
                return v

    def factor(self):
        k, _, _ = self.peek()
        if k == "op" and self.peek()[1] == "-":
            self.take()
            return -self.factor()
        if k == "root":
            self.take()
            base = self.primary()
            if base < 0:
                raise Skip("neg root")
            v = base.sqrt()
        else:
            v = self.primary()
        while self.peek()[0] == "sup":
            v = v ** self.take()[1]
        return v

    def primary(self):
        k, val, _ = self.take()
        if k == "num":
            return val
        if k == "(":
            v = self.expr()
            if self.take()[0] != ")":
                raise Skip("bracket")
            return v
        raise Skip("primary")


def _shown(tokens):
    """Digits after the point, when a side is one plain number (used for the ≈ tolerance)."""
    if len(tokens) == 1 and tokens[0][0] == "num":
        s = tokens[0][2]
        return len(s.split(".")[1]) if "." in s else 0
    return None


def _split(toks):
    sides, rels, cur = [], [], []
    for tk in toks:
        if tk[0] == "rel":
            sides.append(cur)
            rels.append(tk[1])
            cur = []
        else:
            cur.append(tk)
    sides.append(cur)
    return sides, rels


def _holds(rel, a, b, ta, tb):
    eps = Decimal("1e-40")
    if rel == "=":
        if abs(a - b) <= eps:
            return True
        # A stated value with visible decimal places (e.g. "...= 231.22") is a rounded display
        # of the exact answer, not a claim of exact equality - accept it when the exact value
        # rounds to it at its own shown precision (half the last displayed place). Only kicks in
        # when at least one side is a plain decimal literal with >=1 shown decimal digit, so an
        # exact integer check like "3 + 4 = 7" still demands exact equality.
        d = [x for x in (_shown(ta), _shown(tb)) if x is not None and x > 0]
        if d:
            tol = Decimal(1).scaleb(-min(d)) / 2
            return abs(a - b) <= tol
        return False
    if rel == "≠":
        return abs(a - b) > eps
    if rel == "<":
        return a < b
    if rel == ">":
        return a > b
    if rel == "≤":
        return a <= b + eps
    if rel == "≥":
        return a + eps >= b
    d = [x for x in (_shown(ta), _shown(tb)) if x is not None]
    tol = Decimal(1).scaleb(-min(d)) if d else abs(b) * Decimal("1e-9")
    return abs(a - b) <= tol


def check_chain(s):
    """(True, n) / (False, detail) / (None, why) for one chain string."""
    try:
        toks = _tokens(s)
    except Skip as e:
        return None, f"token {e}"
    sides, rels = _split(toks)
    if not rels or any(not x for x in sides):
        return None, "no relation"
    if not any(t[0] == "op" or t[0] in ("sup", "root") for side in sides for t in side):
        return None, "bare numbers"
    try:
        vals = []
        for side in sides:
            p = _P(side)
            v = p.expr()
            if p.i != len(side):
                return None, "trailing"
            vals.append(v)
    except (Skip, ArithmeticError, IndexError, TypeError) as e:
        return None, f"parse {e}"
    for rel, a, b, ta, tb in zip(rels, vals, vals[1:], sides, sides[1:]):
        if not _holds(rel, a, b, ta, tb):
            return False, f"{s}  ->  {[float(x) for x in vals]}"
    return True, len(rels)


def find_chains(text):
    """Yield candidate chain strings from text, with the glue rules applied."""
    text = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", text or "")
    for m in CHAIN.finditer(text):
        raw = m.group(0)
        s = raw.rstrip(" .")
        while s and s[-1] in OPS + REL + "(":
            s = s[:-1].rstrip()
        if not any(r in s for r in REL):
            continue
        # balance brackets by trimming unmatched ones at the ends
        while s.count("(") > s.count(")") and s.startswith("("):
            s = s[1:].lstrip()
        if s.count("(") != s.count(")"):
            continue
        start, end = m.start() + (len(raw) - len(raw.lstrip())), m.start() + len(s)
        before = text[:m.start()]
        after = text[m.start() + len(raw.rstrip(" .")):] if s == raw.rstrip(" .") else text[end:]
        prev = before[-1:] if before else ""
        if prev and (prev.isalnum() or prev in "²³⁴)_/^'’"):
            continue
        bs = before.rstrip()
        if bs and bs[-1] in REL + OPS:
            continue
        nxt = after[:1]
        if nxt and (nxt.isalnum() or nxt in "…_^'’") or after.startswith(".."):
            continue
        yield s


def false_equations(text):
    """Chains that are false (the gate fails on any)."""
    bad = []
    for s in find_chains(text):
        ok, detail = check_chain(s)
        if ok is False:
            bad.append(detail)
    return bad


def count_checked(text):
    n = 0
    for s in find_chains(text):
        ok, detail = check_chain(s)
        if ok:
            n += detail
    return n


# ------------------------------------------------------------------ self-test
_TRUE = ["3² + 4² = 5²", "9 + 16 = 25", "1.41² = 1.9881", "1.414² = 1.999396", "1.4 < √2 < 1.5",
         "1.414 < √2 < 1.415", "√(2 × 12²) = √288", "16² = 256", "16 < √288 < 17", "(√72)² = 72", "√36 = 6",
         "72 ÷ 2 = 36", "9√3 ≈ 15.59", "√50 ≈ 7.07", "25 + 36 ≠ 49", "7² − 5² = 24", "(5 − 1)² + 9 = 5²",
         "4² + 3² = 5²", "(13 − 1)² + 25 = 13²", "6³ + 8³ = 728", "9³ + 10³ = 1729", "√2² = 2", "169 − 25 = 144",
         "12² + 35² = 37²", "√14.5 ≈ 3.81", "1600 + 900 = 2500", "80,000 × 2 = 160,000"]
_FALSE = ["3 + 4 = 5", "1.41² = 1.98", "16² = 289", "√2 < 1.4", "6 + 8 = 10", "25 + 36 = 49", "√50 ≈ 7.2"]
_SKIP = ["c² = 2", "72 = 2a²", "a² + b² = c²", "(3, 4, 5)", "x = 4", "So, c = √2 ≈ 1.414", "(ka)² + (kb)² = (kc)²",
         "2n² = m²", "√2 = 1.41421356…"]


def selftest():
    errs = []
    for s in _TRUE:
        got = list(find_chains(s))
        if len(got) != 1 or check_chain(got[0])[0] is not True:
            errs.append(f"should be TRUE: {s!r} -> {got} {[check_chain(g) for g in got]}")
    for s in _FALSE:
        if not false_equations(s):
            errs.append(f"should be FALSE: {s!r} -> {[check_chain(g) for g in find_chains(s)]}")
    for s in _SKIP:
        got = [g for g in find_chains(s) if check_chain(g)[0] is not None]
        if got:
            errs.append(f"should be SKIPPED: {s!r} -> {got}")
    return errs


if __name__ == "__main__":
    e = selftest()
    print(f"self-test: {len(_TRUE)} true, {len(_FALSE)} false, {len(_SKIP)} skipped; {len(e)} problems")
    for x in e:
        print("  -", x)

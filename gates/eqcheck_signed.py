# -*- coding: utf-8 -*-
"""Sign-aware checker for numeric relation chains in authored text (integers chapters).

Generalized from maths7_ch10/new_design/eqcheck.py (itself copied from maths8_ch9's
power/root-aware checker and made safe for a chapter where almost every statement starts or
ends with a negative number). This is the superset variant: it understands signs AND powers
(² ³ ⁴) AND roots (√) AND brackets. Use it for any chapter with negative numbers, whether or
not it also uses powers/roots; use eqcheck_powers only when the chapter has no negative
numbers and eqcheck_plain only when it has neither signs nor powers/roots.

  * a chain may START with a sign: "−7 + 10 = 3", "−(−5) = 5", "−4 × −2 = + 8" are checked, not skipped;
  * unary plus is understood ("= + 8"), as is unary minus after any operator ("5 × −3");
  * a sign counts as an operation, so "−(−18) = 18" and "(−8) = −8" are checked (a plain "12 = 12" is not);
  * a chain that starts with a sign right after a single-letter variable ("x − 3 = 4", "P − 5 = 2") is the tail
    of algebra and is skipped; after an ordinary word ("we get −4 × −2 = 8") the sign is unary and is checked.

A chain that ends in an operator or a relation ("5 = −4 + b", "−30 × 12 = ___") runs on into algebra or a blank
and is skipped, never trimmed and judged. "=" must hold to 1e-40, "≈" to one unit of the last digit shown; a
chain glued to a letter on either side is algebra and is skipped; a chain that follows a relation or an
operator is the tail of an expression and is skipped; unparsable chains are skipped.

    python -B eqcheck_signed.py      run the self-test
"""
from __future__ import annotations

import re
from decimal import Decimal, getcontext

getcontext().prec = 60

SUP = {"²": 2, "³": 3, "⁴": 4}
REL = "=≈<>≤≥≠"
OPS = "+-−×÷/*"
SIGNS = "+-−"
CHARS = r"0-9.√()²³⁴+\-−×÷/*=≈<>≤≥≠ "
CHAIN = re.compile(r"[0-9√(+\-−][" + CHARS + r"]*")


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
            elif k in ("root", "("):
                v = v * self.factor()          # implicit product: 9√3, 2(…)
            else:
                return v

    def factor(self):
        k, val, _ = self.peek()
        if k == "op" and val in "+-":
            self.take()
            f = self.factor()
            return -f if val == "-" else f
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
    text = re.sub(r"\.(?=\s)", ".\n", text)   # a sentence-ending period never joins two chains ("= 6. 4 × 5")
    for m in CHAIN.finditer(text):
        raw = m.group(0)
        s = raw.rstrip(" .")
        if s and s[-1] in OPS + REL:
            continue                            # "5 = −4 + b", "25 × ? =": the chain runs on into algebra or a blank
        while s and s[-1] == "(":
            s = s[:-1].rstrip()
        s = s.lstrip()
        if not any(r in s for r in REL):
            continue
        # balance brackets by trimming unmatched ones at the ends
        while s.count("(") > s.count(")") and s.startswith("("):
            s = s[1:].lstrip()
        while s.count(")") > s.count("(") and s.endswith(")"):
            s = s[:-1].rstrip()
        if s.count("(") != s.count(")"):
            continue
        lead = len(raw) - len(raw.lstrip())
        end = m.start() + lead + len(s)
        before = text[:m.start() + lead]
        after = text[end:]
        prev = before[-1:] if before else ""
        if prev and (prev.isalnum() or prev in "²³⁴)_/^'’"):
            continue
        bs = before.rstrip()
        if bs and bs[-1] in REL + OPS:
            continue
        if s[0] in SIGNS:
            # a leading sign after a single-letter variable or a closing bracket is a binary operator: algebra tail
            if re.search(r"(?:^|[^A-Za-z])[A-Za-z]$", bs) or bs.endswith((")", "]")) or (bs and bs[-1].isdigit()):
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
_TRUE = ["9 + 16 = 25", "72 ÷ 2 = 36", "3² + 4² = 5²", "√36 = 6", "80,000 × 2 = 160,000",
         "10 − 3 = 7", "−7 + 10 = 3", "−3 × −4 = 12", "−(−5) = 5", "(−4) × (−2) = 8", "5 + (−7) = −2",
         "−4 × −2 = + 8", "(−100) ÷ 25 = (−4)", "50 ÷ (−25) = (−2)", "30 × 5 + 20 × (−2) = 150 + (−40) = 110",
         "15 + (45 × (−3)) = 15 + (−135) = (−120)", "0 − 180 = (−180)", "−1 × −1 × −1 = −1",
         "(5 × −3) × 4 = −15 × 4 = −60", "−370272 < −1412 < 716 < 1412 < 335472 < 370272",
         "32 ÷ ((−36) × (−18)) = 4/81", "we get −4 × −2 = 8", "7 − 18 = 7 + (−18)", "4 − (−12) = 4 + 12",
         "+85 = 10 × 13 + 5 × (−9)", "−(18) = −18", "−(−18) = 18", "−8 = −8", "(−8) = −8"]
_FALSE = ["3 + 4 = 5", "(−4) × (−2) = −8", "(−12) ÷ (−4) = −3", "5 − (−3) = 2", "So 3 + 4 = 8", "−7 + 10 = −3",
          "4 × (−2) = 8", "−4 × 3 = 12", "7 − 18 = 11", "we get −4 × −2 = −8", "−(−18) = −18",
          "(−8) = 8", "2 × 3 = 6. 4 × 5 = 21.", "4 × 2 = 8\n4 × (−2) = 8"]
_SKIP = ["c² = 2", "a² + b² = c²", "(3, 4, 5)", "x = 4", "x − 3 = 4", "P − 5 = 2", "a ÷ −b = −(a ÷ b)",
         "Sum = −7, Difference = −1", "1 × a = a", "−1 × a = −a", "25 × ? = (−100)", "−30 × 12 = _______",
         "Q1 = 9", "12 = 12", "5 = −4 + b", "so 5 = −4 + b.", "−30 × 12 = ___ and 12 × −30 = ___"]


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

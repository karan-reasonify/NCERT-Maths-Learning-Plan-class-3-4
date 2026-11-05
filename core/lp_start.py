# -*- coding: utf-8 -*-
"""Start a new Class 3/4 chapter: the deterministic first step of the /lp34 skill (.claude/skills/lp34/SKILL.md).

    python -I -X utf8 core/lp_start.py "<chapter>" ["<book pdf>"] ["<teacher instruction>"] [--tool-map FILE] [--pages A-B]
                                      [--out DIR] [--force] [--master-id N] [--subject-ref-id M]
    python -I -X utf8 core/lp_start.py --raw "<chapter>[, <book pdf>][, <teacher instruction>]"      (the text after /lp34)

<chapter>   "class 3 ch 2", "3.2", "maths3_ch2", "grade 4 chapter 5" ...  (Class 3 and Class 4 only)
<book pdf>  optional. The NCERT Maths Mela chapter PDF is found by itself in textbooks/class3 (cemm1NN.pdf) or
            textbooks/class4 (demm1NN.pdf); give a path only for another file. A whole-book PDF is cut by the
            "<N>.1" section headings; if that fails the script stops and asks for --pages.
--tool-map  the content team's approved tool table (a markdown file). It is copied to tool_map.md and locked into
            chapter.config.json "approved_tools" (see core/tool_map.py). Without it the plan cannot pass the flow gate.

It does the parts that need no judgement, then stops. It never uploads and never touches the database.
    1. parse the chapter, resolve the repo folder name, the book PDF and the issued ids (upload/chapter_ids.local.json)
    2. copy chapter_template/ into <out>/ (default chapters/maths<G>_ch<N>/new_design/) and fill chapter.config.json
    3. cut the chapter out of the book: book/chapter.pdf, book/pages.json, book/chapter_text.md, book/outline.json,
       and one PNG per page (book/page_NNN.png) so figures can be looked at
    4. lock the approved tool map, write lp_brief.md (the inputs, the teacher instruction verbatim, what is still to
       do) and lp_state.json

Exit code 0 = scaffold ready, 2 = needs input from the user (message on stderr says what), 1 = error.
"""
from __future__ import annotations

import argparse
import glob
import io
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
TEMPLATE = os.path.join(ROOT, "chapter_template")
MASTER_IDS = os.path.join(ROOT, "upload", "chapter_master_ids.md")
LOCAL_IDS = os.path.join(ROOT, "upload", "chapter_ids.local.json")      # git-ignored: the issued ids
GRADES = (3, 4)
BOOKS = {3: ("class3", "cemm"), 4: ("class4", "demm")}     # NCERT Maths Mela: textbooks/<dir>/<prefix>1NN.pdf
ASSET_BASE = ("https://media.singularity-learn.com/learning_plan_assets/V2/cbse/cbse/english/"
              "class_{grade}/mathematics/ch_{chapter_no}")

# template file -> scaffolded name (the template keeps .template / .sample so it is never imported by accident)
COPY = {
    "build.py": "build.py",
    "chapter.config.README.md": "chapter.config.README.md",
    "content.py.template": "content.py",
    "concept_plan.py.template": "concept_plan.py",
    "topics_common.py.template": "topics_common.py",
    "topics_1.py.template": "topics_1.py",
    "tools_1.py.template": "tools_1.py",
    "tool_map.md.template": "tool_map.md",
}


class NeedInput(Exception):
    """Something only the user can answer; main() exits 2 with this message."""


# ---------------------------------------------------------------------------
# 1. chapter reference and book
# ---------------------------------------------------------------------------
def parse_chapter(text):
    """-> dict(grade, chapter_no). Raises NeedInput when it cannot tell."""
    s = text.strip().lower().replace("_", " ")
    m = re.search(r"maths?\s*(\d+)\s*ch\s*(\d+)", s)
    if m:
        return _finish(int(m.group(1)), int(m.group(2)))
    mg = re.search(r"\b(?:class|std|standard|grade|c)\s*(\d+)", s)
    mc = re.search(r"\b(?:chapter|chap|ch)\.?\s*(\d+)", s)
    if mg and mc:
        return _finish(int(mg.group(1)), int(mc.group(1)))
    m = re.match(r"\s*(\d+)\s*[.:/\- ]\s*(\d+)\s*$", s)           # "3.2", "3 2"
    if m:
        return _finish(int(m.group(1)), int(m.group(2)))
    raise NeedInput("could not read a class and chapter number from %r. Write it like 'class 3 ch 2', '3.2' or "
                    "'maths3_ch2'." % text)


def _finish(grade, chapter_no):
    if grade not in GRADES:
        raise NeedInput("this pipeline is for Class 3 and Class 4 (got Class %s)." % grade)
    return {"grade": grade, "chapter_no": chapter_no}


def textbook_for(grade, chapter_no):
    folder, prefix = BOOKS[grade]
    return os.path.join(ROOT, "textbooks", folder, "%s1%02d.pdf" % (prefix, chapter_no))


def local_ids(grade, chapter_no):
    """(chapter_master_id, subject_ref_id, platform chapter name) from upload/chapter_ids.local.json, or (None, None,
    None). That file is git-ignored and holds the ids the user issued; 'last known' only, core/check_master_id.py is the
    check against the live row."""
    if not os.path.exists(LOCAL_IDS):
        return None, None, None
    try:
        with io.open(LOCAL_IDS, encoding="utf-8") as f:
            data = json.load(f)
        g = data.get(str(grade)) or {}
        ch = (g.get("chapters") or {}).get(str(chapter_no)) or {}
        return ch.get("chapter_master_id"), g.get("subject_ref_id"), ch.get("name")
    except (OSError, ValueError):
        return None, None, None


def _plain(name):
    """A chapter name with no em or en dash (the dash gate rejects them anywhere in a plan)."""
    return re.sub(r"\s*[\u2013\u2014]\s*", " - ", name or "").strip()


def _norm(name):
    return re.sub(r"[^a-z0-9]", "", _plain(name).lower())


def last_known_master_id(grade, folder_no):
    """The id in upload/chapter_master_ids.md, or None. 'Last known' only: core/check_master_id.py is the check."""
    if not os.path.exists(MASTER_IDS):
        return None
    section = None
    with io.open(MASTER_IDS, encoding="utf-8") as f:
        for line in f:
            h = re.match(r"##\s+Grade\s+(\d+)", line)
            if h:
                section = int(h.group(1))
                continue
            if section == grade:
                r = re.match(r"\|\s*ch(\d+)\s*\|\s*(\d+)\s*\|", line)
                if r and int(r.group(1)) == folder_no:
                    return int(r.group(2))
    return None


def sibling_defaults(grade):
    """subject_ref_id / medium_id from a built chapter of the same class, and every media_tag already taken."""
    subject = medium = None
    tags = set()
    for p in sorted(glob.glob(os.path.join(ROOT, "chapters", "maths*_ch*", "new_design", "chapter.config.json"))):
        try:
            with io.open(p, encoding="utf-8") as f:
                c = json.load(f)
        except Exception:
            continue
        if c.get("media_tag"):
            tags.add(c["media_tag"])
        if c.get("grade") == grade and c.get("subject_ref_id") and subject is None:
            subject, medium = c["subject_ref_id"], c.get("medium_id", 1)
    return subject, medium or 1, tags


def pick_media_tag(grade, taken):
    for ch in "xyzwvutsrqpnmkjhgfedcba":
        t = "c%d%s" % (grade, ch)
        if t not in taken:
            return t
    raise SystemExit("no free media_tag left for class %d" % grade)


# ---------------------------------------------------------------------------
# 3. the book
# ---------------------------------------------------------------------------
SECTION = re.compile(r"^\s*(\d{1,2})\.(\d{1,2})(?:\.\d{1,2})?\s+\S")


def _lines(text):
    return [ln for ln in text.splitlines() if ln.strip()]


def find_chapter_pages(doc, chapter_no, forced=None):
    """0-based inclusive (first, last) page range of the chapter in `doc`.  Raises NeedInput when unsure."""
    n = len(doc)
    if forced:
        a, b = forced
        if not (1 <= a <= b <= n):
            raise NeedInput("--pages %d-%d is outside the book (it has %d pages)." % (a, b, n))
        return a - 1, b - 1
    if n <= 45:                                   # a one-chapter file (the NCERT Maths Mela per-chapter PDFs)
        return 0, n - 1
    texts = [doc[i].get_text() for i in range(n)]

    def heads(i):
        return {int(SECTION.match(ln).group(1)) for ln in _lines(texts[i]) if SECTION.match(ln)}

    starts = [i for i in range(n)
              if any((m := SECTION.match(ln)) and int(m.group(1)) == chapter_no and int(m.group(2)) == 1
                     for ln in _lines(texts[i]))]
    starts = [i for i in starts if len(heads(i)) <= 2 and (chapter_no + 1) not in heads(i)]
    if not starts:
        raise NeedInput("could not find where chapter %d starts in this %d-page book (no '%d.1' section heading in "
                        "the text layer). Re-run with --pages A-B (1-based page numbers of the PDF)."
                        % (chapter_no, n, chapter_no))
    first, last = starts[0], n - 1
    for i in range(first + 1, n):
        hs = heads(i)
        if (chapter_no + 1) in hs and chapter_no not in hs:
            last = i - 1
            break
    return first, last


def chapter_title(doc, first):
    """-> (title, printed chapter number). The NCERT primary-class chapter opener prints the chapter number in the biggest
    type and the title just under it in the next size; the body text starts lower. So: the biggest non-digit text on the
    first page, in reading order, is the title; the biggest digit-only text is the chapter number. (None, None) per part
    when the page has no such text."""
    spans = []
    for b in doc[first].get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            for sp in ln["spans"]:
                t = sp["text"].strip()
                if t:
                    spans.append((sp["size"], round(sp["bbox"][1]), sp["bbox"][0], t))
    words = [x for x in spans if not re.fullmatch(r"\d{1,2}", x[3]) and x[0] >= 18]
    digits = [x for x in spans if re.fullmatch(r"\d{1,2}", x[3]) and x[0] >= 18]
    number = int(max(digits)[3]) if digits else None
    title = None
    if words:
        top = max(x[0] for x in words)
        parts, seen = [], set()
        for size, y, x, t in sorted((w for w in words if abs(w[0] - top) < 0.6), key=lambda w: (w[1], w[2])):
            if (y, t) not in seen:                       # the PDFs print each title span twice
                seen.add((y, t))
                parts.append(t)
        title = " ".join(parts).strip()
        if not title or len(title) > 60 or not re.search(r"[A-Za-z]", title):
            title = None
    return title, number


def extract_book(pdf, chapter_no, forced, out_dir, dpi=100):
    try:
        import pymupdf
    except ImportError:
        raise NeedInput("PyMuPDF (pymupdf) is not installed here, and cutting the chapter out of the book needs it. "
                        "Install it (pip install pymupdf) in a virtual environment and run this script with that "
                        "interpreter.")
    doc = pymupdf.open(pdf)
    first, last = find_chapter_pages(doc, chapter_no, forced)
    title, printed_no = chapter_title(doc, first)
    bdir = os.path.join(out_dir, "book")
    os.makedirs(bdir, exist_ok=True)
    sub = pymupdf.open()
    sub.insert_pdf(doc, from_page=first, to_page=last)
    sub.save(os.path.join(bdir, "chapter.pdf"))
    pages, md, outline = {}, [], []
    for k, i in enumerate(range(first, last + 1), 1):
        txt = doc[i].get_text()
        pages[str(k)] = txt
        md.append("<!-- chapter page %d (pdf page %d) -->\n%s" % (k, i + 1, txt))
        for ln in _lines(txt):
            if SECTION.match(ln) and int(SECTION.match(ln).group(1)) == chapter_no:
                outline.append({"page": k, "heading": ln.strip()})
        doc[i].get_pixmap(dpi=dpi).save(os.path.join(bdir, "page_%03d.png" % k))
    with io.open(os.path.join(bdir, "pages.json"), "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False, indent=1)
    with io.open(os.path.join(bdir, "chapter_text.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    with io.open(os.path.join(bdir, "outline.json"), "w", encoding="utf-8") as f:
        json.dump(outline, f, ensure_ascii=False, indent=1)
    chars = sum(len(t) for t in pages.values())
    glitches = len(re.findall(r"\b[a-z]+[A-Z][a-z]+\b", " ".join(pages.values())))
    return {"pdf_pages": [first + 1, last + 1], "n_pages": last - first + 1, "title": title, "printed_no": printed_no,
            "outline": outline,
            "chars": chars, "book_total_pages": len(doc), "glitches_per_1000": round(1000.0 * glitches / max(chars, 1), 1)}


# ---------------------------------------------------------------------------
# 2. scaffold
# ---------------------------------------------------------------------------
def scaffold(out_dir, cfg, info, force, tool_map_file=None):
    os.makedirs(out_dir, exist_ok=True)
    written, kept = [], []
    for src, dst in COPY.items():
        d = os.path.join(out_dir, dst)
        if os.path.exists(d) and not force:
            kept.append(dst)
            continue
        with io.open(os.path.join(TEMPLATE, src), encoding="utf-8") as f:
            text = f.read()
        text = text.replace("TODO Chapter Name", info["name"])
        with io.open(d, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        written.append(dst)
    if tool_map_file:                                # the content team's own table replaces the template one
        shutil.copyfile(tool_map_file, os.path.join(out_dir, "tool_map.md"))
        if "tool_map.md" not in written:
            written.append("tool_map.md")
    d = os.path.join(out_dir, "chapter.config.json")
    if force or not os.path.exists(d):
        with io.open(d, "w", encoding="utf-8", newline="\n") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
        written.append("chapter.config.json")
    else:
        kept.append("chapter.config.json")
    cp = os.path.join(out_dir, "content.py")
    if "content.py" in written:
        with io.open(cp, encoding="utf-8") as f:
            t = f.read()
        t = (t.replace('"grade": 0,', '"grade": %d,' % cfg["grade"])
              .replace('"label": "Class N",', '"label": "Class %d",' % cfg["grade"])
              .replace('"chapter_no": 0,', '"chapter_no": %d,' % cfg["chapter_no"])
              .replace("textbooks/classN/TODO.pdf", info["pdf_rel"]))
        with io.open(cp, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)
    return written, kept


def write_brief(out_dir, ref, cfg, book, instruction, pdf, master_id, flags, others, tools):
    rel = os.path.relpath(out_dir, ROOT).replace("\\", "/") if out_dir.startswith(ROOT) else out_dir
    lines = [
        "# /lp34 brief: Class %d, %s" % (cfg["grade"], cfg["chapter_name"]),
        "",
        "Generated by `core/lp_start.py`. Everything below is an input or a fact to check; nothing here is approved yet.",
        "",
        "## Inputs",
        "- Asked for: `%s`" % ref["asked"],
        "- Class %d, chapter %d -> repo folder `maths%d_ch%d` (`%s`)"
        % (ref["grade"], ref["chapter_no"], ref["grade"], ref["chapter_no"], rel),
        "- Book: `%s` (%d pages in the file; chapter = pdf pages %d-%d, %d pages, %d characters of text)"
        % (pdf, book["book_total_pages"], book["pdf_pages"][0], book["pdf_pages"][1], book["n_pages"], book["chars"]),
        "- Chapter title read from the first page: %r (check it against book/page_001.png)" % (book["title"] or "NOT FOUND"),
        "- chapter_master_id: %s" % ("%d (from the issued ids on file; confirm live with "
                                     "core/check_master_id.py before any upload)" % master_id if master_id
                                     else "UNKNOWN: ask the user for the issued id"),
        "- Approved tools: %s" % ("%d locked from the content team's table: %s"
                                  % (len(tools), "; ".join("%d %s" % (t["no"], t["name"]) for t in tools))
                                  if tools else "NOT GIVEN YET (paste the content team's table into tool_map.md, "
                                                "then run core/tool_map.py lock)"),
        "",
        "## Teacher instruction (verbatim)",
        "",
        ("> " + instruction.strip().replace("\n", "\n> ")) if instruction and instruction.strip() else "_none given_",
        "",
        "## Flags to settle before building",
    ]
    lines += ["- " + f for f in flags] or ["- none"]
    if others:
        lines += ["", "## This chapter already exists elsewhere", ""] + ["- `%s`" % o for o in others]
    lines += [
        "",
        "## Scaffold (all unfinished: every TODO must go before build.py will pass)",
        "- `chapter.config.json` filled from the facts above (eqcheck `plain`; age limits for Class %d)" % cfg["grade"],
        "- `tool_map.md` (the content team's table), `content.py`, `concept_plan.py`, `topics_common.py`, `topics_1.py`, `tools_1.py`",
        "- `book/`: `chapter.pdf`, `pages.json`, `chapter_text.md`, `outline.json`, `page_NNN.png`",
        "",
        "Next: follow `.claude/skills/lp34/SKILL.md` from step 2.",
        "",
    ]
    with io.open(os.path.join(out_dir, "lp_brief.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def split_raw(raw):
    """The text after '/lp34' -> (chapter, book path or '', instruction).

    '/lp34 class 3 ch 2, textbooks/class3/cemm102.pdf, use the kite story': when a .pdf path is present the book is
    the longest tail of the comma-separated head that is an existing file; everything before it is the chapter,
    everything after it the instruction. With no .pdf the first comma-separated part is the chapter and the rest is
    the instruction (the book is then found in textbooks/ by itself)."""
    m = re.search(r"\.pdf\b", raw, re.I)
    if not m:
        head, _, tail = raw.partition(",")
        return head.strip(), "", tail.strip()
    head, tail = raw[:m.end()], raw[m.end():]
    parts = head.split(",")
    for k in range(1, len(parts)):
        cand = ",".join(parts[k:]).strip().strip('"\'')
        if os.path.isfile(cand):
            return ",".join(parts[:k]).strip(), cand, tail.lstrip(" ,;\n").strip()
    raise NeedInput("book file not found: %s" % (",".join(parts[1:]).strip() or head))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chapter", nargs="?", default="")
    ap.add_argument("book", nargs="?", default="")
    ap.add_argument("instruction", nargs="?", default="")
    ap.add_argument("--raw", help="the whole text after /lp34: '<chapter>[, <book pdf>][, <instruction>]'")
    ap.add_argument("--pages", help="1-based pdf page range of the chapter, e.g. 3-20")
    ap.add_argument("--out", help="chapter folder to create (default chapters/maths<G>_ch<N>/new_design)")
    ap.add_argument("--force", action="store_true", help="overwrite scaffold files that already exist")
    ap.add_argument("--master-id", type=int, help="chapter_master_id; default: upload/chapter_ids.local.json")
    ap.add_argument("--subject-ref-id", type=int, help="subject_ref_id; default: upload/chapter_ids.local.json")
    ap.add_argument("--tool-map", help="the content team's approved tool table (markdown file)")
    a = ap.parse_args(argv)

    tools = []
    try:
        if a.raw:
            a.chapter, a.book, a.instruction = split_raw(a.raw)
        if not a.chapter:
            raise NeedInput("give the chapter: /lp34 <chapter>[, <book pdf>][, <teacher instruction>]")
        ref = parse_chapter(a.chapter)
        ref["asked"] = a.chapter
        g, no = ref["grade"], ref["chapter_no"]
        pdf = os.path.abspath(a.book.strip().strip('"')) if a.book else textbook_for(g, no)
        if not os.path.isfile(pdf):
            raise NeedInput("book file not found: %s. The NCERT Maths Mela chapter PDFs are in textbooks/class%d/; "
                            "give the path of another file." % (pdf, g))
        forced = None
        if a.pages:
            m = re.fullmatch(r"\s*(\d+)\s*-\s*(\d+)\s*", a.pages)
            if not m:
                raise NeedInput("--pages must look like 3-20")
            forced = (int(m.group(1)), int(m.group(2)))
        if a.tool_map:
            if not os.path.isfile(a.tool_map):
                raise NeedInput("tool map file not found: %s" % a.tool_map)
            from core import tool_map as TM
            with io.open(a.tool_map, encoding="utf-8") as f:
                try:
                    tools = TM.parse(f.read())
                except ValueError as e:
                    raise NeedInput("the tool table could not be read: %s" % e)
        out_dir = os.path.abspath(a.out) if a.out else os.path.join(ROOT, "chapters", "maths%d_ch%d" % (g, no),
                                                                    "new_design")
        others = [os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "chapters", "maths%d_ch%d*" % (g, no)))
                  if os.path.abspath(p) != os.path.dirname(out_dir)]
        if os.path.isdir(out_dir) and os.listdir(out_dir) and not a.force:
            raise NeedInput("%s already has files. Re-run with --force to overwrite the scaffold files (your other "
                            "files are never deleted), or pick another --out." % out_dir)
        book = extract_book(pdf, no, forced, out_dir)
    except NeedInput as e:
        sys.stderr.write("NEEDS INPUT: %s\n" % e)
        return 2

    subject, medium, taken = sibling_defaults(g)
    l_master, l_subject, l_name = local_ids(g, no)
    subject = a.subject_ref_id or l_subject or subject
    master_id = a.master_id or l_master or last_known_master_id(g, no)
    name = book["title"] or _plain(l_name) or "TODO Chapter Name"
    completed = False
    if l_name and book["title"] and _norm(l_name) != _norm(book["title"]) and \
            _norm(l_name).startswith(_norm(book["title"])):
        name, completed = _plain(l_name), True        # the book title was cut short (e.g. a Roman numeral in its own span)
    if name.isupper():
        name = name.title()
    media_tag = pick_media_tag(g, taken)
    cfg = {
        "chapter_id": "cbse_eng_maths%d_ch%d" % (g, no),
        "phase": 2,
        "pipeline": "class3_4_story_tool_flow",
        "chapter_master_id": master_id or 0,
        "subject_ref_id": subject or 0,
        "medium_id": medium,
        "publication_id": 1,
        "grade": g,
        "grade_band": "3_4",
        "chapter_no": no,
        "chapter_name": name,
        "media_tag": media_tag,
        "eqcheck": "plain",
        "eqcheck_errata": [],
        "allow_words": [],
        "photo_rule_band": "default",
        "asset_base_template": ASSET_BASE,
        "approved_tools": tools,
        "tool_map_required": True,
        "concept_objective_word_range": [5, 30],
        "topic_objective_max_words": 40,
        "coverage_exclude_doer_role": "tool",
        "idea_topic_concept_range": [1, 6],
        "max_tool_controls": 4,
        "max_tool_questions": 6,
        "max_instruction_words": 15,
        "max_sentence_words": 14 if g == 3 else 16,
        "video_max_seconds": {"hook": 90, "concept": 150},
    }
    flags = []
    if not tools:
        flags.append("no approved tool table was given: ask the user for the content team's table (names, purposes, "
                     "sequence), paste it into tool_map.md and run core/tool_map.py lock. Do not invent tools.")
    if not master_id:
        flags.append("chapter_master_id is not known (not in upload/chapter_ids.local.json either): ask the user for "
                     "the issued id (a wrong id uploads good content to the wrong chapter and still says success).")
    elif l_master and master_id == l_master:
        flags.append("ids come from upload/chapter_ids.local.json (chapter_master_id %s, subject_ref_id %s, platform "
                     "name %r). Confirm them live with core/check_master_id.py once DATABASE_URL is set."
                     % (master_id, subject, l_name))
    if completed:
        flags.append("the title read from the book (%r) was cut short; chapter_name is the platform's %r. Check it "
                     "against book/page_001.png." % (book["title"], name))
    elif l_name and book["title"] and _norm(l_name) != _norm(book["title"]):
        flags.append("the book prints %r but the platform calls this chapter %r. chapter_name keeps the book's title; "
                     "ask the user if the platform's name should be used instead." % (book["title"], l_name))
    if not subject:
        flags.append("subject_ref_id is not known (no built chapter of Class %d to copy it from): ask the user, or read "
                     "it from the live chapterMaster row with core/check_master_id.py." % g)
    if not book["title"]:
        flags.append("the chapter title could not be read from the text layer: open book/page_001.png and set "
                     "chapter_name in chapter.config.json and content.py by hand.")
    if book["printed_no"] and book["printed_no"] != no:
        flags.append("the chapter number printed on the first page is %d, not %d: this may be the wrong file; open "
                     "book/page_001.png before going on." % (book["printed_no"], no))
    if book["chars"] < 400 * book["n_pages"]:
        flags.append("very little text per page: the PDF is mostly pictures or scanned; read the page PNGs.")
    if book["glitches_per_1000"] >= 1.0:
        flags.append("the text layer is noisy (%.1f OCR-style glitches per 1000 characters): do not trust numbers from "
                     "chapter_text.md; confirm each one against book/page_NNN.png." % book["glitches_per_1000"])
    if forced is None and book["book_total_pages"] > 45:
        flags.append("the page range was found automatically (pdf pages %d-%d): check the first and last page in "
                     "book/ before trusting it." % tuple(book["pdf_pages"]))
    flags.append("Class %d picture-book pages: the exercises sit in boxes and activities, not numbered sections; "
                 "read every page PNG, the text layer alone misses them." % g)

    pdf_rel = os.path.relpath(pdf, ROOT).replace("\\", "/") if pdf.startswith(ROOT) else pdf
    written, kept = scaffold(out_dir, cfg, {"name": name, "pdf_rel": pdf_rel}, a.force,
                             a.tool_map if tools else None)
    write_brief(out_dir, ref, cfg, book, a.instruction, pdf, master_id, flags, others, tools)
    state = {"ref": ref, "out_dir": out_dir, "pdf": pdf, "pages": book["pdf_pages"], "title": book["title"],
             "master_id": master_id, "subject_ref_id": subject, "media_tag": media_tag, "flags": flags,
             "instruction": a.instruction, "written": written, "kept": kept, "approved_tools": len(tools)}
    with io.open(os.path.join(out_dir, "lp_state.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    print("scaffold ready: %s" % out_dir)
    print("  class %d, folder maths%d_ch%d, media_tag %s, master id %s, subject_ref_id %s, approved tools %d"
          % (g, g, no, media_tag, master_id or "UNKNOWN", subject or "UNKNOWN", len(tools)))
    print("  chapter: %r  pdf pages %d-%d (%d pages)" % (name, book["pdf_pages"][0], book["pdf_pages"][1], book["n_pages"]))
    print("  written: %s" % ", ".join(written))
    if kept:
        print("  kept (already existed): %s" % ", ".join(kept))
    for fl in flags:
        print("  FLAG: " + fl)
    if others:
        print("  ALREADY EXISTS ELSEWHERE: " + ", ".join(others))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())

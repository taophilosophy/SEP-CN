# -*- coding: utf-8 -*-
"""六轴质量工序共享库（ADR-0079；q1–q6 的共同底座，非 CLI）。

职责：
  * 读取词条文档并按保护域掩码（代码块、行内代码、数学、URL、HTML 注释），
    掩码为等长空白，保证位置索引与原文对齐；
  * 抽句（正文散文，跳过标题、表格、列表符号、脚注定义、引块、参考文献节）；
  * 抽直引（弯引号对），供 q1 使用；
  * 语种判定（字符域优先，拉丁系按变音符＋特征词）；
  * 目标枚举与 JSON 输出。

设计纪律（ADR-0070）：所有函数只产候选或事实，不作裁判。
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tools.common import read_text  # noqa: E402

HAN = r"\u4e00-\u9fff\u3400-\u4dbf"
_FENCE = re.compile(r"^[ \t]*```.*?^[ \t]*```", re.S | re.M)
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_MATH = re.compile(r"\$\$.*?\$\$|\$[^$\n]{1,400}\$")
_URL = re.compile(r"https?://\S+")
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
_BIB_HEAD = re.compile(r"^#{1,3}\s*(参考文献|References|Bibliography|Works Cited)", re.I | re.M)
_HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
_TABLE = re.compile(r"^\s*\|")
_LIST = re.compile(r"^\s*(?:[*+-]|\d+[.)])\s")
_FOOTDEF = re.compile(r"^\s*\[\^[^\]]+\]:")
_QUOTEBLOCK = re.compile(r"^\s*>")
_QUOTE_PAIR = re.compile(r"[“]([^”\n]{2,600})[”]")


def target_paths(paths=None):
    """枚举目标文档。显式路径优先；否则全库 <letter>/*.md（排除桩件与补充材料子文档）。"""
    if paths:
        return [p for p in paths if os.path.isfile(p)]
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "[0-9a-z]", "*.md"))):
        name = os.path.basename(p)
        if "." in name[:-3]:           # 带点补充材料子文档
            continue
        if os.path.getsize(p) < 2048:  # 桩件
            continue
        out.append(p)
    return out


def slug_of(path):
    return os.path.splitext(os.path.basename(path))[0]


def read_doc(path):
    return read_text(path)


def protect(text):
    """把非散文区替换为等长空白（换行保留），返回掩码文本。"""
    def blank(m):
        s = m.group(0)
        return "".join("\n" if c == "\n" else " " for c in s)
    out = _FENCE.sub(blank, text)
    out = _HTML_COMMENT.sub(blank, out)
    out = _INLINE_CODE.sub(blank, out)
    out = _MATH.sub(blank, out)
    out = _URL.sub(blank, out)
    m = _BIB_HEAD.search(out)
    if m:
        out = out[:m.start()] + blank_from(out, m.start())
    return out


def blank_from(text, start):
    return "".join("\n" if c == "\n" else " " for c in text[start:])


def prose_lines(text):
    """产出 (line_no, line_start, line) 的正文行；跳过结构行。"""
    masked = protect(text)
    pos = 0
    for i, line in enumerate(masked.splitlines(True), 1):
        raw = text[pos:pos + len(line)]
        s = line.rstrip("\n")
        if (s.strip() and not _HEADING.match(s) and not _TABLE.match(s)
                and not _LIST.match(s) and not _FOOTDEF.match(s)
                and not _QUOTEBLOCK.match(s)):
            yield i, pos, raw.rstrip("\n")
        pos += len(line)


def h2_sections(text):
    """按二级标题切节：[(标题行, 节正文)]；标题本身含在节文本内。"""
    masked = protect(text)
    marks = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^##\s+.*$", masked)]
    out = []
    for k, (pos, head) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(masked)
        out.append((head.strip(), text[pos:end]))
    return out


def prose_blocks(text):
    """正文段落块：[(起始行号, 块文本)]。空行或结构行分块（跨行段落合并）。"""
    masked = protect(text)
    blocks, cur, start = [], [], None
    for i, raw in enumerate(masked.splitlines(True), 1):
        s = raw.rstrip("\n")
        structural = (not s.strip()) or _HEADING.match(s) or _TABLE.match(s) \
            or _FOOTDEF.match(s) or _QUOTEBLOCK.match(s)
        if structural:
            if cur:
                blocks.append((start, "\n".join(cur)))
                cur, start = [], None
            continue
        body = _LIST.sub("", s)
        if not start:
            start = i
        cur.append(body)
    if cur:
        blocks.append((start, "\n".join(cur)))
    return blocks


def sentences(text):
    """正文散句：[(line_no, start, sentence)]。以 。；！？ 切分，含标点。"""
    for line_no, base, line in prose_lines(text):
        masked = protect(line)
        buf, start = [], 0
        for j, ch in enumerate(masked):
            buf.append(ch)
            if ch in "。；！？":
                sent = line[start:j + 1]
                if re.search("[%s]" % HAN, sent) and len(re.findall("[%s]" % HAN, sent)) >= 6:
                    yield line_no, base + start, sent
                start = j + 1
        tail = line[start:]
        if re.search("[%s]" % HAN, tail) and len(re.findall("[%s]" % HAN, tail)) >= 6:
            yield line_no, base + start, tail


def quotes(text):
    """直引候选：[(line_no, start, inner)]；跳过保护域与参考文献节。"""
    masked = protect(text)
    for m in _QUOTE_PAIR.finditer(masked):
        inner = text[m.start(1):m.end(1)]
        line_no = text.count("\n", 0, m.start(1)) + 1
        yield line_no, m.start(1), inner


SCRIPT_RANGES = [
    ("greek", r"\u0370-\u03ff"), ("cyrillic", r"\u0400-\u04ff"),
    ("hebrew", r"\u0590-\u05ff"), ("arabic", r"\u0600-\u06ff"),
    ("devanagari", r"\u0900-\u097f"), ("tibetan", r"\u0f00-\u0fff"),
    ("kana", r"\u3040-\u30ff"), ("cjk", r"\u4e00-\u9fff\u3400-\u4dbf"),
]
_DIACRITIC = re.compile(r"[àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎđĘęĚěĞğİıŁłŃŅņŌōŐőŘřŚŜśŠšŢţŤůŮŰũŸźŻżž]")
_EN_STOP = frozenset(
    "the of and to a in that is are was were be it its as for with on by not "
    "this these those which or from at an has have had he she they we you i "
    "his her their our your there here what when who whom whose why how then "
    "so if but no yes all any some each every into over under between through "
    "during before after above below can could may might must shall should "
    "will would do does did also only very just more most other another such "
    "than one two three first second third new same own s t don now".split())
_LATIN_HINTS = {
    "german": ["der", "die", "das", "und", "ist", "nicht", "von", "als", "ein",
               "eine", "sich", "auch", "werden", "wurde", "dass", "mit"],
    "french": ["le", "la", "les", "des", "est", "que", "pour", "dans", "ne",
               "pas", "qui", "sur", "avec", "cela", "être"],
    "italian": ["il", "lo", "gli", "della", "che", "non", "sono", "questa",
                "questo", "per", "come", "anche", "del"],
    "latin": ["est", "non", "et", "in", "ad", "quod", "quae", "esse", "cum",
              "sed", "per", "sunt", "qui", "quid", "vel", "nec", "anima",
              "deus", "ens", "ratio", "naturae"],
}


def lang_of(text):
    """语种判定：字符域优先；拉丁系按变音符＋特征词；英文占比高归 none。"""
    for name, rng in SCRIPT_RANGES:
        n = len(re.findall("[" + rng + "]", text))
        if n >= 2:
            if name == "greek" and re.search(r"[\^\\=₂³]|\d\s*\^", text):
                return "none"
            if name == "cjk" and re.search(r"[\u3040-\u30ff]", text):
                return "japanese"
            return name
    words = re.findall(r"[A-Za-zÀ-ÿĀ-ſ]+", text.lower())
    if not words:
        return "none"
    ratio = sum(1 for w in words if w in _EN_STOP) / max(len(words), 1)
    scored = sorted(((sum(words.count(h) for h in hs), k)
                     for k, hs in _LATIN_HINTS.items()), reverse=True)
    if scored and scored[0][0] >= 2:
        return scored[0][1]
    if ratio >= 0.45:
        return "none"
    return "diacritic" if _DIACRITIC.search(text) else "unclassified-latin"


BCP47 = {"cjk": "zh", "kana": "ja", "japanese": "ja", "greek": "grc",
         "cyrillic": "ru", "hebrew": "he", "arabic": "ar", "devanagari": "sa",
         "tibetan": "bo", "german": "de", "french": "fr", "italian": "it",
         "latin": "la", "none": "en", "unclassified-latin": "en",
         "diacritic": "unclassified"}


def bcp47(lang):
    return BCP47.get(lang, lang)


def snippet(s, n=90):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n] + "…"


def emit(payload, out=None, as_json=False):
    """统一输出：写文件（可选）＋stdout 摘要或 JSON。"""
    if out:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            json.dump(payload, f, ensure_ascii=False, indent=1)
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=1))

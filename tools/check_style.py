# -*- coding: utf-8 -*-
"""体例检查（宪法 VI / FR-015；三校步骤的可判定工具）。

用法: python tools/check_style.py <路径>...
输出: stdout JSON {files, issues:[{path,line,rule,detail}]}
规则: curly-quotes（弯引号成对/方向，禁直引号/直角引号/日式半角引号）
      bold-spacing（** 加粗两侧空格，段首块首与标点例外）
      cjk-spacing（汉字与西文/数字之间须有半角空格）
      no-html（HTML 标签残留）、no-text-fence（```text 语言标注）
      no-asciiart（xref:/link: AsciiDoc 残留）
豁免: 围栏代码块与行内代码；英文单词内部撇号（don't、O'Brien）不算引号；
      数学定界符 $…$/$$…$$ 内的 LaTeX 记号（撇号 prime 等）不算引号；
      参考文献节（"参考文献"/"Bibliography"/"References（引用注释）" 标题及其下
      各级子标题）内**非中文行**原文照录不改写，豁免引号与中西文空格规则；
      含汉字的行（ADR-0011 还原的中国文献条目）按正体例检查。
退出码: 0 无问题；1 有 issue。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import read_text

HAN = r"\u4e00-\u9fff\u3400-\u4dbf"
RULES = ("curly-quotes", "bold-spacing", "cjk-spacing", "no-html",
         "no-text-fence", "no-asciiart")

HTML_RE = re.compile(r"</?[a-zA-Z][^>]*>")
ASCIIART_RE = re.compile(r"\b(?:xref|link):[^\s\[]*\[")
TEXT_FENCE_RE = re.compile(r"^\s*```text\s*$", re.M)
CJK_GAP_RE = re.compile(
    r"(?<=[%s])[A-Za-z0-9]|(?<=[A-Za-z0-9])[%s]" % (HAN, HAN))
EMPH_RE = re.compile(r"\*\*[^*\n]+\*\*")
AFTER_PUNCT = "，。、；：？！）】》”’…—,.!?)]}"
HEADING_RE = re.compile(r"^(#{1,6})\s")
BIB_HEADING_RE = re.compile(
    r"^#{1,6}\s*(?:参考文献|Bibliography|References（引用注释）)\s*$", re.I)
# 文献节内含汉字的行是 ADR-0011 还原的中国文献条目，按正体例检查
CJK_LINE_RE = re.compile(r"[%s]" % HAN)


def _segments(line):
    """一行拆成 [("text", …)/("code", …)] 交替段，检查只作用于正文段。"""
    parts = line.split("`")
    out, text = [], []
    for i, p in enumerate(parts):
        if i % 2 == 0:
            text.append(p)
        else:
            if text:
                out.append(("text", "".join(text)))
                text = []
            out.append(("code", ""))
    if text:
        out.append(("text", "".join(text)))
    return out


def check_line(path, lineno, line, issues):
    for kind, seg in _segments(line):
        if kind == "code" or not seg:
            continue
        # curly-quotes：直引号（词内撇号除外）、直角/半角引号、成对与方向；
        # 数学定界符 $…$/$$…$$ 内的 LaTeX 记号（如撇号 prime \mathbf{A}'）不是引号，先遮蔽再查
        stripped = re.sub(r"[A-Za-z]'[A-Za-z]", "AA", seg)
        _math = re.compile(r"\$\$.+?\$\$|\$[^$]+\$")
        stripped = _math.sub("\x00", stripped)
        for ch in stripped:
            if ch in "\"''｢｣＂＇「」『』":
                issues.append({"path": path, "line": lineno, "rule": "curly-quotes",
                               "detail": "非法引号字符 %r: %s" % (ch, seg.strip()[:40])})
        for lo, hi in (("\u201c", "\u201d"), ("\u2018", "\u2019")):
            depth = 0
            for ch in stripped:
                if ch == lo:
                    depth += 1
                elif ch == hi:
                    depth -= 1
                    if depth < 0:
                        issues.append({"path": path, "line": lineno, "rule": "curly-quotes",
                                       "detail": "右引号先于左引号: %s" % seg.strip()[:40]})
                        depth = 0
            if depth != 0:
                issues.append({"path": path, "line": lineno, "rule": "curly-quotes",
                               "detail": "引号不成对（%s…%s 差 %d）: %s"
                                         % (lo, hi, depth, seg.strip()[:40])})
        # bold-spacing
        for m in EMPH_RE.finditer(seg):
            start, end = m.start(), m.end()
            before = seg[start - 1] if start > 0 else ""
            after = seg[end] if end < len(seg) else ""
            if before and before not in " \t" and before not in "（“‘【《—…，。、；：？！）】》":
                issues.append({"path": path, "line": lineno, "rule": "bold-spacing",
                               "detail": "** 前缺空格: …%s" % seg[max(0, start - 8):end][:30]})
            if after and after not in " \t" and after not in AFTER_PUNCT:
                issues.append({"path": path, "line": lineno, "rule": "bold-spacing",
                               "detail": "** 后缺空格: %s…" % seg[start:end + 8][-30:]})
        # cjk-spacing
        for m in CJK_GAP_RE.finditer(seg):
            issues.append({"path": path, "line": lineno, "rule": "cjk-spacing",
                           "detail": "中西文之间缺空格: …%s…" % seg[max(0, m.start() - 6):m.end() + 6]})
        # no-html / no-asciiart
        for m in HTML_RE.finditer(seg):
            issues.append({"path": path, "line": lineno, "rule": "no-html",
                           "detail": m.group(0)[:40]})
        for m in ASCIIART_RE.finditer(seg):
            issues.append({"path": path, "line": lineno, "rule": "no-asciiart",
                           "detail": m.group(0)[:40]})
    if TEXT_FENCE_RE.search(line):
        issues.append({"path": path, "line": lineno, "rule": "no-text-fence",
                       "detail": "禁止 text 语言标注"})


def check_file(path):
    issues = []
    lines = read_text(path).split("\n")
    fence_open = False
    in_bib = False
    bib_lvl = 0
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            fence_open = not fence_open
            if not fence_open:
                continue
            if TEXT_FENCE_RE.search(line):
                issues.append({"path": path, "line": i, "rule": "no-text-fence",
                               "detail": "禁止 text 语言标注"})
            continue
        m_h = HEADING_RE.match(line)
        if m_h:
            lvl = len(m_h.group(1))
            if BIB_HEADING_RE.match(line):
                in_bib, bib_lvl = True, lvl
            elif not (in_bib and lvl > bib_lvl):
                in_bib = False
        if fence_open:
            continue
        if in_bib and not CJK_LINE_RE.search(line):
            continue  # 非中文照录行豁免；含汉字行（还原的中国文献）照常检查
        check_line(path, i, line, issues)
    return issues


def main(argv=None):
    paths = [a for a in (argv or sys.argv[1:]) if not a.startswith("-")]
    if not paths:
        print(json.dumps({"error": "用法: python tools/check_style.py <路径>..."},
                         ensure_ascii=False))
        return 2
    all_issues = []
    nfiles = 0
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                for name in names:
                    if name.endswith(".md"):
                        all_issues += check_file(os.path.join(root, name))
                        nfiles += 1
        elif os.path.exists(p):
            all_issues += check_file(p)
            nfiles += 1
    print(json.dumps({"files": nfiles, "issues": all_issues},
                     ensure_ascii=False, indent=2))
    return 1 if all_issues else 0


if __name__ == "__main__":
    sys.exit(main())

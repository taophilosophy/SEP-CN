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
         "no-text-fence", "no-asciiart", "italic-cjk")

HTML_RE = re.compile(r"</?[a-zA-Z][^>]*>")
ASCIIART_RE = re.compile(r"\b(?:xref|link):[^\s\[]*\[")
TEXT_FENCE_RE = re.compile(r"^\s*```text\s*$", re.M)
CJK_GAP_RE = re.compile(
    r"(?<=[%s])[A-Za-z0-9]|(?<=[A-Za-z0-9])[%s]" % (HAN, HAN))
EMPH_RE = re.compile(r"\*\*[^*\n]+\*\*")
AFTER_PUNCT = "，。、；：？！）】》”’…—（《,.!?)]}"
HEADING_RE = re.compile(r"^(#{1,6})\s")
BIB_HEADING_RE = re.compile(
    r"^#{1,6}\s*(?:参考文献|Bibliography|References（引用注释）)\s*$", re.I)
# 文献节内含汉字的行是 ADR-0011 还原的中国文献条目，按正体例检查
CJK_LINE_RE = re.compile(r"[%s]" % HAN)
# 脚注定义行 [^key]: ... 照录豁免：参考文献脚注定义区可位于 ## 学术工具 之后
FN_DEF_RE = re.compile(r"^\[\^[^\]]+\]:\s")

_START_QUOTE_RE = re.compile(r"(?<![\u4e00-\u9fff\w])['‘’](?=[^\W\d_])(?![\u4e00-\u9fff])")


def _mask_start_quote(seg):
    """遮蔽 ayn/hamza 式起始撇号（‘Abbāsid）；成对中文单引号（‘Kant’）连同闭合号一起遮蔽，
    避免留下孤立右引号造成“右引号先于左引号”假阳性。"""
    chars = list(seg)
    for m in _START_QUOTE_RE.finditer(seg):
        i = m.start()
        if chars[i] == "A":
            continue
        if seg[i] == "\u2018":
            close = seg.find("\u2019", i + 1)
            if close != -1 and chars[close] != "A":
                chars[i] = chars[close] = "A"
                continue
        chars[i] = "A"
    return "".join(chars)


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
        # 数学定界符 $…$/$$…$$ 内的 LaTeX 记号（如撇号 prime \mathbf{A}'）不是引号，先遮蔽再查；
        # 字母间的撇号（'‘’）是转写撇号（法语 l’âme、希伯来 Shi‘ur、阿拉伯 Ya’qub 等），
        # 不是引号，先遮蔽再查（[^\W\d_] 为 Unicode 字母类，覆盖变音字母）
        # 词内撇号（两侧拉丁，Ya’qub/l’âme/Shi‘ur；排除汉字邻接——“…是如何’真…”是中文引号；
        # 两侧字母类须排除汉字，否则“的‘是-否…”这类中文成对引号会被误当词内撇号吞掉一只）
        stripped = re.sub(r"(?<![\u4e00-\u9fff])[^\W\d_\u4e00-\u9fff]['‘’][^\W\d_\u4e00-\u9fff](?![\u4e00-\u9fff])", "AA", seg)
        # 转写 ayn/hamza 起始（‘Abbāsid：左邻标点/边界、右邻拉丁；任一侧邻汉字时必是中文引号）
        # 成对中文单引号（‘Kant’、‘是-否可观察量’）须连同闭合号一起遮蔽，否则留下孤立
        # 右引号，误报“右引号先于左引号”（2026-11-08 K 批实测）。
        stripped = _mask_start_quote(stripped)
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
        # italic-cjk：中文强调不使用斜体，使用加粗（用户裁定 2026-10-29）
        # 拉丁/希腊/希伯来字母的斜体（书名/术语/逻辑符号）保留不改
        # 遮蔽 **粗体**（已用 * 粗体的不重复报）与数学定界符与行内代码
        _bold_masked = EMPH_RE.sub("\x00", seg)
        _math_masked = re.sub(r"\$\$.+?\$\$|\$[^$]+\$", "\x00", _bold_masked)
        # 遮蔽含空格的多词拉丁斜体短语（如 *ceteris paribus*、*a fortiori*、*bien pensant*）：
        # 它们是拉丁术语（非中文强调，保留斜体）。单词语正则 \*([^* \x00]+)\* 无法整体匹配含空格短语，
        # 会留下裸星号与下一 *...* 错配，把其间中文误报为 "*中文*" 假阳性（一行两个 *ceteris paribus* 即触发）。
        # 只遮蔽"内容含空格"的 *...* 段，内容无空格的中文斜体 *中文* 不受影响。
        def _mask_multiword(m):
            return "\x00" if " " in m.group(0) else m.group(0)
        _multi_masked = re.sub(r"\*[^*\n]+?\*", _mask_multiword, _math_masked)
        for m2 in re.finditer(r"\*([^* \x00]+)\*", _multi_masked):
            t2 = m2.group(1)
            if t2.startswith('）') or t2.endswith('（'):
                continue
            if re.search(r"[一-鿿]", t2):
                issues.append({"path": path, "line": lineno, "rule": "italic-cjk",
                               "detail": "中文强调不应使用斜体，应改为加粗: *%s*" % m2.group(1)[:30]})

        # bold-spacing（遮蔽数学区间的 ** 误配：$w^{**}$ 等数学星号不是强调标记，
        # 与上方 italic 检测的数学遮蔽对称）
        _math_spans = [m.span() for m in re.finditer(r"\$\$.+?\$\$|\$[^$\n]+?\$", seg)]
        for m in EMPH_RE.finditer(seg):
            start, end = m.start(), m.end()
            if any(s <= start < e or s <= end - 1 < e for s, e in _math_spans):
                continue
            before = seg[start - 1] if start > 0 else ""
            after = seg[end] if end < len(seg) else ""
            if before and before not in " \t" and before not in "（“‘【《—…，。、；：？！）】》”’":
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
    lines = read_text(path).splitlines()
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
        if line.lstrip().startswith("!["):
            continue  # 图片嵌入行豁免：alt 为照录的英文机器描述，引号/空格规则针对中文正文
        if in_bib and not CJK_LINE_RE.search(line):
            continue  # 非中文照录行豁免；含汉字行（还原的中国文献）照常检查
        if FN_DEF_RE.match(line):
            continue  # 脚注定义行（[^key]: ...）照录豁免：参考文献脚注定义区可位于##学术工具之后
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

# -*- coding: utf-8 -*-
r"""译文侧数学公式门禁（021 战役，用户 2026-11-13 裁定）。

站点渲染链：markdown → .vitepress/math-plugin.mjs 保护 $…$/$$…$$ → MathJax 3
tex-svg。以下九类问题会造成红字、吞正文或体例不一，机器可判：

  C1 宏残留     公式内用了 SEP 词条宏（en/<slug>/local.js 定义，站点无此表）
                ——工具/data/sep-macro-names.json＋mathjax3-macros.json 判定
  C2 内侧空白   行内 `$ X $`：保护正则要求首尾非空白，否则漏配、裸 $ 吞正文
  C3 不可见字符 公式内零宽/控制字符（\u200b \ufeff \x01…）导致 MathJax 崩溃
  C4 未转义 %#  公式内 `%` 起注释吞掉后半段、`#` 触发宏参数错
  C5 中文入公式 \text{…} 等文本命令之外出现汉字（错配吞正文的显影）
  C6 裸 $ 残留  正文中未配对的单 $（货币、误写），与后文公式连锁错配
  C7 未转义货币 `$` 紧跟数字（$150,000）：与后文公式配对成灾，应写 \$
  C8 英连接语   \text{…} 内仍为 and/iff/then/if/for all/where 等（应译）
  C9 散文 \\(   数学段之外的 \\(…\\)（旧 SEP 记法，家法统一 $…$）

用法:
  python tools/check_math_zh.py [路径…]        # 默认全库 <letter>/*.md
  python tools/check_math_zh.py --strict       # C9/C7 也算失败
输出: 逐条问题 + 汇总；退出码 0 通过 / 1 有失败。
"""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "tools", "data")

MACRO_NAMES = json.load(open(os.path.join(DATA, "sep-macro-names.json"),
                             encoding="utf-8"))
V3 = json.load(open(os.path.join(DATA, "mathjax3-macros.json"), encoding="utf-8"))
NEEDS_EXPANSION = set(V3["needs_expansion"])

FENCE_RE = re.compile(r'(```|~~~)[^\n]*\n(?:[\s\S]*?\n\1[^\n]*|[\s\S]*$)')
TEXTCMD_RE = re.compile(
    r'\\(?:text|textrm|mbox|textnormal|textbf|textit|textsf|texttt|textup|'
    r'hbox|operatorname\*?)\s*\{')
CJK_RE = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')
INVIS_RE = re.compile('[\u200b\u200c\u200d\u2060\ufeff\x01\x02\x03\x00]')
MACRO_USE_RE = re.compile(r'\\([A-Za-z]+)')
ENGLISH_TEXT_RE = re.compile(
    r'\\(?:text|textrm|mbox|textnormal|textbf|textit|textsf|texttt|textup|'
    r'hbox)\s*\{\s*(if and only if|iff|and|then|for all|for every|where|'
    r'such that|if|or|not|is true|holds)\s*\}', re.I)
CURRENCY_RE = re.compile(r'(?<![\\$])\$(?=\d)')


def fence_ranges(text):
    return [m.span() for m in FENCE_RE.finditer(text)]


def in_ranges(pos, ranges):
    return any(a <= pos < b for a, b in ranges)


def math_spans(text, ranges):
    n = len(text)
    i = 0
    out = []
    while i < n:
        ch = text[i]
        if ch == '\\':
            i += 2
            continue
        if ch != '$' or in_ranges(i, ranges):
            i += 1
            continue
        if i + 1 < n and text[i + 1] == '$':
            close = text.find('$$', i + 2)
            if close < 0:
                i += 2
                continue
            out.append((i, close + 2, True))
            i = close + 2
            continue
        j = i + 1
        while j < n:
            cj = text[j]
            if cj == '\\':
                j += 2
                continue
            if cj == '$':
                break
            if cj == '\n' and text[j:j + 3] == '\n\n':
                break
            j += 1
        if j < n and text[j] == '$' and j > i + 1:
            out.append((i, j + 1, False))
            i = j + 1
        else:
            i += 1
    return out


def text_ranges(span):
    """span 内文本类命令的 {} 内容区间（配平）。"""
    out = []
    i = 0
    n = len(span)
    while True:
        m = TEXTCMD_RE.search(span, i)
        if not m:
            break
        start = m.end() - 1
        depth = 0
        j = start
        while j < n:
            ch = span[j]
            if ch == '\\':
                j += 2
                continue
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        out.append((start + 1, j))
        i = m.end()
    return out


def mask_text_cmds(span):
    chars = list(span)
    for a, b in text_ranges(span):
        for k in range(a, b):
            chars[k] = '\x00'
    return ''.join(chars)


def check_file(path, rel):
    text = open(path, encoding="utf-8").read()
    slug = os.path.basename(path)[:-3].split(".")[0]
    sep_macros = set(MACRO_NAMES.get(slug, ()))
    ranges = fence_ranges(text)
    issues = []

    for start, end, disp in math_spans(text, ranges):
        body = text[start:end]
        inner = body[2:-2] if disp else body[1:-1]
        if disp and not (body.startswith("$$") and body.endswith("$$")):
            inner = body[2:-2]
        # C1 宏残留
        for m in MACRO_USE_RE.finditer(inner):
            name = m.group(1)
            if name in sep_macros and name in NEEDS_EXPANSION:
                issues.append(("C1", start, "SEP 宏未展开：\\" + name))
        # C2 内侧空白（仅行内）
        if not disp:
            if inner[:1].isspace() or inner[-1:].isspace():
                head_ok = inner.lstrip().startswith("\\") and len(inner) > 2
                # 尾随空白剥掉后以 \ 结尾＝LaTeX 强制空格收尾（en 上游拆行公式
                # 形态 `\ $ $`，math-plugin 可配对、MathJax 合法），豁免；
                # 裸 \ 收尾（真缺陷）不豁免。
                tail_ok = (inner[-1:].isspace()
                           and inner.rstrip().endswith("\\")
                           and len(inner.rstrip()) > 1)
                if not (head_ok or tail_ok):
                    issues.append(("C2", start, "行内定界符内侧空白：" + body[:40]))
        # C3 不可见字符
        if INVIS_RE.search(inner):
            issues.append(("C3", start, "公式含不可见字符"))
        # C4 % 与 #
        if re.search(r"(?<!\\)%", inner):
            issues.append(("C4", start, "公式内未转义 %"))
        if re.search(r"(?<!\\)#", inner):
            issues.append(("C4", start, "公式内未转义 #"))
        # C5 中文在文本命令之外
        if CJK_RE.search(mask_text_cmds(inner)):
            issues.append(("C5", start, "公式文本命令外出现汉字：" + inner[:40]))
        # C8 英文连接语
        for m in ENGLISH_TEXT_RE.finditer(inner):
            issues.append(("C8", start, "公式内英文连接语：" + m.group(0)[:40]))

    # C6/C7/C9 基于正文（数学段之外）
    covered = [(a, b) for a, b, _ in math_spans(text, ranges)]
    pos = 0
    for i, ch in enumerate(text):
        if ch == "\\":
            continue
        if ch == "$" and not in_ranges(i, covered):
            prev = text[i - 1] if i else ""
            if prev != "\\":
                issues.append(("C6", i, "正文裸 $（未配对）"))
        # C9 散文 \(
        if ch == "\\" and text[i:i + 2] == "\\(" and not in_ranges(i, covered):
            issues.append(("C9", i, "散文中的 \\(…\\)（应改 $…$）"))
    for m in CURRENCY_RE.finditer(text):
        if not in_ranges(m.start(), covered):
            issues.append(("C7", m.start(), "未转义货币 $（应写 \\$）"))
    return issues


def iter_targets(argv):
    paths = [a for a in argv if not a.startswith("-")]
    if paths:
        for p in paths:
            p = p if os.path.isabs(p) else os.path.join(ROOT, p)
            if os.path.isdir(p):
                for name in sorted(os.listdir(p)):
                    if name.endswith(".md"):
                        yield os.path.join(p, name)
            elif p.endswith(".md"):
                yield p
        return
    for letter in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, letter)
        if not (len(letter) == 1 and letter.isalpha() and os.path.isdir(d)):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith(".md"):
                yield os.path.join(d, name)


def main(argv):
    strict = "--strict" in argv
    hard = {"C1", "C2", "C3", "C4", "C5", "C6", "C8"}
    if strict:
        hard |= {"C7", "C9"}
    total = 0
    files = 0
    fails = 0
    for path in iter_targets(argv):
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        issues = check_file(path, rel)
        if not issues:
            continue
        files += 1
        total += len(issues)
        bad = [i for i in issues if i[0] in hard]
        fails += len(bad)
        for code, pos, msg in issues[:8]:
            line = open(path, encoding="utf-8").read()[:pos].count("\n") + 1
            print(f"{rel}:{line} [{code}] {msg}")
        if len(issues) > 8:
            print(f"{rel}: …另有 {len(issues) - 8} 条")
    print(f"\n== 公式体例：{files} 文件有问题，共 {total} 条；硬错误 {fails} 条")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

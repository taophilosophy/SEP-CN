# -*- coding: utf-8 -*-
"""specs/011：ADR-0019 粗体内侧空格扫描器（栈解析版，避免跨对误报）。

解析 ** 对（栈配对），检查每对内容的首/尾字符：
  内容以空格开头或结尾 = 内侧空格违例（CommonMark 翼规则，渲染显示裸 **）。
数学/行内代码豁免；行首列表星跳过；转义星跳过。
"""
import io
import os
import re
import sys
import glob

os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))


def scan_line(line):
    """返回该行的内侧空格违例数。数学/行内代码等长占位（保 offset）。"""
    seg = re.sub(r"\$\$[^$]*\$\$|\$[^$\n]*?\$", lambda m: "M" * len(m.group(0)), line)
    seg = re.sub(r"`[^`]*`", lambda m: "C" * len(m.group(0)), seg)
    i, n = 0, len(seg)
    stack = []
    bad = 0
    while i < n:
        if seg[i] == "\\" and i + 1 < n and seg[i + 1] == "*":
            i += 2
            continue
        m = re.match(r"\*+", seg[i:])
        if not m:
            i += 1
            continue
        tok = m.group(0)
        if len(tok) >= 3:
            if stack and stack[-1][0] == "***":
                stack.pop()
            else:
                stack.append(["***", i])
            i += len(tok)
            continue
        if i == 0 or (seg[i - 1] in " \t" and (i - 2 < 0 or seg[i - 2] in " \t>")):
            if i + 1 < n and seg[i + 1] == " ":
                i += 1
                continue
        t2 = "**" if len(tok) == 2 else "*"
        if stack and stack[-1][0] == t2:
            start = stack.pop()[1]
            content = seg[start + 2:i]
            if t2 == "**" and content and (content[0] == " " or content[-1] == " "):
                bad += 1
            i += len(tok)
            continue
        stack.append([t2, i])
        i += len(tok)
    return bad


def locate_bad_pairs(line):
    """栈解析定位违例粗体对在原行中的 (start, end) 区间（end 含闭 **）。

    数学/行内代码等长占位剥离（保 offset，跨数学星号误配免疫）。
    """
    seg = re.sub(r"\$\$[^$]*\$\$|\$[^$\n]*?\$", lambda m: "M" * len(m.group(0)), line)
    seg = re.sub(r"`[^`]*`", lambda m: "C" * len(m.group(0)), seg)
    i, n = 0, len(seg)
    stack = []
    bad = []
    while i < n:
        if seg[i] == "\\" and i + 1 < n and seg[i + 1] == "*":
            i += 2
            continue
        m = re.match(r"\*+", seg[i:])
        if not m:
            i += 1
            continue
        tok = m.group(0)
        if len(tok) >= 3:
            if stack and stack[-1][0] == "***":
                stack.pop()
            else:
                stack.append(["***", i])
            i += len(tok)
            continue
        if i == 0 or (seg[i - 1] in " \t" and (i - 2 < 0 or seg[i - 2] in " \t>")):
            if i + 1 < n and seg[i + 1] == " ":
                i += 1
                continue
        t2 = "**" if len(tok) == 2 else "*"
        if stack and stack[-1][0] == t2:
            start = stack.pop()[1]
            content = seg[start + 2:i]
            if t2 == "**" and content and (content[0] == " " or content[-1] == " "):
                bad.append((start, i + 2))
            i += len(tok)
            continue
        stack.append([t2, i])
        i += len(tok)
    return bad


def fix_line(line):
    bad = locate_bad_pairs(line)
    if not bad:
        return line
    out = []
    pos = 0
    for start, end in bad:
        out.append(line[pos:start])
        core = line[start + 2:end - 2]
        out.append("**" + core.strip() + "**")
        pos = end
    out.append(line[pos:])
    return "".join(out)


def main():
    hits = {}
    for f in sorted(glob.glob("[a-z]/*.md")):
        if f.startswith(("yi-", "ren-", "mu-")):
            continue
        n = sum(scan_line(l) for l in io.open(f, encoding="utf-8").read().splitlines())
        if n:
            hits[f] = n
    total = sum(hits.values())
    print("真内侧空格违例:", total, "处/", len(hits), "文件")
    for f, n in sorted(hits.items(), key=lambda x: -x[1])[:12]:
        print("  %-32s %d" % (f, n))
    if "--fix" in sys.argv:
        fixed = 0
        for f in hits:
            lines = io.open(f, encoding="utf-8").read().splitlines()
            chg = False
            for i, line in enumerate(lines):
                if scan_line(line):
                    l2 = fix_line(line)
                    if l2 != line and scan_line(l2) < scan_line(line):
                        lines[i] = l2
                        chg = True
                        fixed += 1
            if chg:
                io.open(f, "w", encoding="utf-8", newline="").write("\n".join(lines))
        print("已 --fix，修复", fixed)


if __name__ == "__main__":
    main()

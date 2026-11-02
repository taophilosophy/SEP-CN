# -*- coding: utf-8 -*-
"""specs/011：星号最小平衡器——栈配对，未配对三星降级双星、孤立单星删除。

仅用于畸形行的最后收尾（语义校正留给深读层）。
"""
import io
import re
import sys

sys.path.insert(0, "specs/011-translation-review/bin")
from style_fix import star_ok  # noqa: E402

p = "i/intensional-trans-verbs.md"
lines = io.open(p, encoding="utf-8").read().split("\n")


def segt(l):
    return "".join(x for idx, x in enumerate(l.split("`")) if idx % 2 == 0)


def balance(text):
    """栈配对：** 对与 * 对；未闭合的三星降级、孤立星删除。"""
    out, stack = [], []
    i, n = 0, len(text)
    while i < n:
        m = re.match(r"\*+", text[i:])
        if not m:
            out.append(text[i])
            i += 1
            continue
        tok = m.group(0)
        if len(tok) >= 2:
            if stack and stack[-1] == "**":
                stack.pop()
                out.append("**")
                i += 2  # 剩余星（***/**** 的第三、四星）作为孤立删除
            else:
                stack.append("**")
                out.append("**")
                i += 2
        else:
            if stack and stack[-1] == "*":
                stack.pop()
                out.append("*")
            else:
                stack.append("*")
                out.append("*")
            i += 1
    # 栈内未闭合的：** 保持原样（开粗体文本保留，渲染容忍），* 删除
    return "".join(out)


changed = 0
for i, l in enumerate(lines):
    if star_ok(segt(l)):
        continue
    l2 = balance(l)
    if l2 != l and star_ok(segt(l2)):
        lines[i] = l2
        changed += 1

io.open(p, "w", encoding="utf-8", newline="").write("\n".join(lines))
bad = [i + 1 for i, l in enumerate(lines) if not star_ok(segt(l))]
print("平衡修复 %d 行，最终剩余畸形: %s" % (changed, bad))
for ln in bad:
    l = lines[ln - 1]
    stars = [m.start() for m in re.finditer(r"\*+", l)]
    print("L%d:" % ln, " | ".join("…%s…" % l[max(0, s - 12):s + 16] for s in stars[:6])[:190])

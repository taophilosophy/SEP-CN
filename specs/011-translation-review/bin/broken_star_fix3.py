# -*- coding: utf-8 -*-
"""specs/011：intensional 四轮收尾。"""
import io
import sys

sys.path.insert(0, "specs/011-translation-review/bin")
from style_fix import star_ok  # noqa: E402

p = "i/intensional-trans-verbs.md"
t = io.open(p, encoding="utf-8").read()

FIX = [
    ("一个动词是 ***内涵的** *（*intensional*）", "一个动词是 **内涵的**（*intensional*）"),
    ("恼人的邻居萨姆 ***就是** *那位著名作家", "恼人的邻居萨姆 **就是** 那位著名作家"),
    ("后者似乎暗示你 ***应该** *有一辆", "后者似乎暗示你 **应该** 有一辆"),
    ("理学家只会隐含 ***没有** *（而非缺乏）", "理学家只会隐含 **没有**（而非缺乏）"),
    ("又有它 **** 所表达 **** 的 **** 惯常涵义 ***。", "又有它 **所表达** 的 **惯常涵义**。"),
    ("中仅仅互换** **惯常地** **同指称的表达式", "中仅仅互换 **惯常地** 同指称的表达式"),
    ("因为这些专名现在** **指称** *它们的惯常涵义。", "因为这些专名现在 **指称** 它们的惯常涵义。"),
    ("在** **指称** *它们的惯常涵义。然而", "在 **指称** 它们的惯常涵义。然而"),
    ("的意义：从** **个体** **到** **真值** *的函数", "的意义：从 **个体** 到 **真值** 的函数"),
    ("（即 **^((every(woollen(sweater)))(woollen))** 在每", "（即**^((every(woollen(sweater)))(woollen))** 在每"),
    ("但对 **^((every(pringle(woollen))** 存在这样的 *u **，所以", "但对 **^((every(pringle(woollen)))** 存在这样的 *u*，所以"),
    ("可用。***sweater** 指称", "可用。**sweater** 指称"),
]

applied = 0
for old, new in FIX:
    n = t.count(old)
    if n == 1:
        t = t.replace(old, new)
        applied += 1
    else:
        print("FAIL(n=%d): %s" % (n, old[:46]))
io.open(p, "w", encoding="utf-8", newline="").write(t)
print("应用 %d/%d" % (applied, len(FIX)))

lines = t.split("\n")


def segt(l):
    return "".join(x for idx, x in enumerate(l.split("`")) if idx % 2 == 0)


bad = [i + 1 for i, l in enumerate(lines) if not star_ok(segt(l))]
print("剩余畸形行:", bad)
for ln in bad[:6]:
    import re
    l = lines[ln - 1]
    stars = [m.start() for m in re.finditer(r"\*+", l)]
    print("L%d:" % ln, " | ".join("…%s…" % l[max(0, s - 10):s + 14] for s in stars[:6])[:190])

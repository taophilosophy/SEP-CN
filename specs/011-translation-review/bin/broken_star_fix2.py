# -*- coding: utf-8 -*-
"""specs/011：intensional 剩余 14 行逐行精确修复。"""
import io
import sys

sys.path.insert(0, "specs/011-translation-review/bin")
from style_fix import star_ok  # noqa: E402

p = "i/intensional-trans-verbs.md"
t = io.open(p, encoding="utf-8").read()

FIX = [
    # L5
    ("一个动词是** **及物的** *（*transitive **）", "一个动词是 **及物的**（*transitive*）"),
    ("被称为** **及物地使用** *（*occur transitively*）", "被称为 **及物地使用的**（*occur transitively*）"),
    # L27
    ("分析为** **没有** *（*not having*", "分析为 **没有**（*not having*"),
    # L53
    ("既有它** *所指称 **** 的 **** 惯常指称 ****，又", "既有它 **所指称** 的 **惯常指称**，又"),
    # L61
    ("的 ***转换后** **指称——即", "的 **转换后** 指称——即"),
    # L135
    ("物理系** *获得 ***（或就此例而言", "物理系**获得**（或就此例而言"),
    # L179
    ("在 ***简单类型论** **中，像", "在 **简单类型论** 中，像"),
    # L217 逻辑式内侧空格
    ("（即 **^((every(woollen(sweater)))(woollen))** 在每", "（即 **^((every(woollen(sweater)))(woollen))** 在每"),
    # L225
    ("都是** *高阶 **** 的，因为", "都是**高阶** 的，因为"),
    # L227 逻辑式
    ("我们就有 ** (hit(someone))(jack) **。这里 ** hit ** 接受", "我们就有 **(hit(someone))(jack)**。这里 **hit** 接受"),
    # L239 句点前孤立星
    ("(jack)** *.[^note-7]", "(jack)**.[^note-7]"),
    # L241
    ("在（19）中，***a(woollen((sweater)))** 处于 **want** 的辖域内", "在（19）中，**a(woollen((sweater)))** 处于 **want** 的辖域内"),
    # L299
    ("既然** 莫里亚蒂回来了这一命题 **与** 莫里亚蒂回来了*同指称", "既然**莫里亚蒂回来了这一命题**与**莫里亚蒂回来了**同指称"),
    # L419 文献节导语
    (" ***以下文献从原文照录，不作翻译；中国文献条目（古今）一律译为中文。** *", "**以下文献从原文照录，不作翻译；中国文献条目（古今）一律译为中文。**"),
]

applied = 0
for old, new in FIX:
    n = t.count(old)
    if n == 1:
        t = t.replace(old, new)
        applied += 1
    else:
        print("FAIL(n=%d): %s" % (n, old[:50]))
io.open(p, "w", encoding="utf-8", newline="").write(t)
print("应用 %d/%d" % (applied, len(FIX)))

# 残余检查
lines = t.split("\n")


def segt(l):
    return "".join(x for idx, x in enumerate(l.split("`")) if idx % 2 == 0)


bad = [i + 1 for i, l in enumerate(lines) if not star_ok(segt(l))]
print("剩余畸形行:", bad)

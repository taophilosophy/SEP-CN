# -*- coding: utf-8 -*-
"""specs/011 v6：交叉星组纠正器（括号边界约束 + 残留形态族规则）。

每行修后以 star_ok（v2 判据）验证，不通过保持原样并报告。
"""
import io
import os
import re
import sys
import glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "specs", "011-translation-review", "bin"))
from style_fix import star_ok  # noqa: E402


def segt(l):
    return "".join(x for idx, x in enumerate(l.split("`")) if idx % 2 == 0)


def fix_line(l):
    o = l
    # P1 括号内粗体书名 → 斜体：（** X **） → （*X*）
    l = re.sub(r"（\*\*\s*([^*（）\n]{1,50}?)\s*\*\*）", r"（*\1*）", l)
    # P2 方括号内：[*X **] → [*X*]
    l = re.sub(r"\[\*([^*\[\]\n]{1,50}?)\s*\*\*\]", r"[\*\1*]", l)
    # P3 括号内斜体+双星：（*X **） → （*X*）
    l = re.sub(r"（\*([^*（）\n]{1,50}?)\s*\*\*）", r"（*\1*）", l)
    # P4 括号内反向：（** X *） → （*X*）
    l = re.sub(r"（\*\*\s*([^*（）\n]{1,50}?)\s*\*）", r"（*\1*）", l)
    # P5 斜体闭+多星：*X ** → *X*（后随空白/标点/右括号）
    l = re.sub(r"\*([^*\n]{1,40}?)\*\*(?=[\s，。；：）\]〔〕])", r"*\1*", l)
    # R2 粗体截断：** X *Y → **X** Y
    l = re.sub(r"\*\* ([^*\n]{1,60}?)\*(?=[\u4e00-\u9fffA-Za-z（“])", r"**\1**", l)
    # R3 粗体开+尾单星：**X* → **X**（后随汉字/标点）
    l = re.sub(r"\*\*([^*\n]{1,40}?)\*(?=[\u4e00-\u9fff，。；：）])", r"**\1**", l)
    # R4 斜体开+双星闭：*X ** → *X*
    l = re.sub(r"\*([^*\n（）]{1,60}?) \*\*(?=[）\s])", r"*\1*", l)
    # R5 书名斜体误加粗：《X》（*Y **）内形态
    l = re.sub(r"(《[^》]{1,30}》\*[^*\n]{1,40}?)\*\*）", r"\1*）", l)
    return l


def main():
    total_fixed = total_left = 0
    for f in sorted(glob.glob("[a-z]/*.md")):
        if f.startswith(("yi-", "ren-", "mu-")):
            continue
        lines = io.open(f, encoding="utf-8").read().split("\n")
        changed = False
        left = []
        for i, l in enumerate(lines):
            if star_ok(segt(l)):
                continue
            l2 = fix_line(l)
            if star_ok(segt(l2)):
                lines[i] = l2
                changed = True
                total_fixed += 1
            else:
                left.append(i + 1)
                total_left += 1
        if changed:
            io.open(f, "w", encoding="utf-8", newline="").write("\n".join(lines))
        if left:
            print(f, "残留:", left[:10])
    print("修 %d 行，残留 %d 行" % (total_fixed, total_left))


if __name__ == "__main__":
    main()

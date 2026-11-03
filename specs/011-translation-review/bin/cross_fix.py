# -*- coding: utf-8 -*-
"""specs/011 v5：交叉星组纠正器。

处理「平衡但交叉」形态（*X **Y** Z*），启发式规则逐行尝试，修后以 star_ok（新判据）验证，
不通过则保持原样并报告。
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
    # R1 括号内书名：（*X **） → （*X*）
    l = re.sub(r"（\*([^*（）\n]{1,60}?) \*\*）", r"（*\1*）", l)
    l = re.sub(r"（\*([^*（）\n]{1,60}?)\*\*）", r"（*\1*）", l)
    # R2 粗体截断：** X *Y → **X** Y（**开+空格+内容+单星闭）
    l = re.sub(r"\*\* ([^*\n]{1,60}?)\*(?=[\u4e00-\u9fffA-Za-z（“])", r"**\1**", l)
    # R3 粗体开+尾单星：**X* → **X**（后随汉字/标点，开粗体未闭）
    l = re.sub(r"\*\*([^*\n]{1,40}?)\*(?=[\u4e00-\u9fff，。；：）])", r"**\1**", l)
    # R4 斜体开+双星闭：（*X ** → （*X*
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

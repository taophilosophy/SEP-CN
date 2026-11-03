# -*- coding: utf-8 -*-
"""specs/011：mu-lu-s 的 [\\* 噪声前缀规范化（验证驱动）。

mu-lu-s（手编分类目录）无别名结构；SUMMARY 别名行同步时带入的 [\\* 前缀是噪声。
本脚本：统计真实噪声行 → 生成去噪预览 → 抽样打印 → --apply 执行。
噪声判定：标题文本以「\\*」开头（转义星+原别名星），即 SUMMARY 别名行的 \\*X——见Y 形态。
"""
import io
import os
import re
import sys

os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

p = "mu-lu-s.md"
lines = io.open(p, encoding="utf-8").read().splitlines(True)
noise = []  # (lineno, old_title, new_title)
for i, l in enumerate(lines, 1):
    m = re.search(r"\[(\\\\\*|\\\*)([^]]+)\]", l)
    if not m:
        continue
    old_title = m.group(2)
    # 去噪：标题文本去掉残留的「——见X：」中转段？不——mu-lu-s 无别名结构，
    # 但 SUMMARY 别名行的 zh 段本身含「——见X：Y」信息，保留正文仅去 \* 前缀。
    new_title = old_title.lstrip("*").strip()
    noise.append((i, m.group(0), "[" + new_title + "]"))

print("噪声行 %d" % len(noise))
for i, old, new in noise[:5] + noise[-3:]:
    print("  L%d: %s → %s" % (i, old[:56], new[:56]))

if "--apply" in sys.argv:
    for i, old, new in noise:
        lines[i - 1] = lines[i - 1].replace(old, new, 1)
    io.open(p, "w", encoding="utf-8", newline="").write("".join(lines))
    print("已写回")

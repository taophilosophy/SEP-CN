# -*- coding: utf-8 -*-
"""specs/011 终审二：文本重复破坏检测。

fix_seg 错配除星号错乱外还产生行内片段重复（如「通达其在，我们也无需通达其真实本性」）。
逐行检测：相邻两处 ≥8 字符相同子串（中文破坏特征）。
对照 83fc857^ 原文：原文无 && 当前有 → 复核引入 → 还原（--apply）。
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
BASE = "83fc857^"
DUP = re.compile(r"(.{8,}?)\1")


def dup_lines(t):
    out = set()
    for i, line in enumerate(t.splitlines(), 1):
        segs = line.split("`")
        text = "".join(p for idx, p in enumerate(segs) if idx % 2 == 0)
        if DUP.search(text):
            out.add(i)
    return out


def main():
    apply = "--apply" in sys.argv
    r = subprocess.run(["git", "show", "--name-only", "--format=", "83fc857"],
                       capture_output=True, text=True)
    files = [l for l in r.stdout.splitlines() if l.endswith(".md") and "/" in l
             and not l.startswith(("specs/", "tools/"))]
    total = 0
    for f in files:
        cur = io.open(f, encoding="utf-8").read()
        r2 = subprocess.run(["git", "show", "%s:%s" % (BASE, f)], capture_output=True)
        if r2.returncode != 0:
            continue
        old = r2.stdout.decode("utf-8")
        old_lines = old.splitlines()
        cur_lines = cur.splitlines()
        if len(old_lines) != len(cur_lines):
            continue
        old_d, cur_d = dup_lines(old), dup_lines(cur)
        chg = [i for i in cur_d if i not in old_d]
        if not chg:
            continue
        total += len(chg)
        for i in chg[:3]:
            m = DUP.search(cur_lines[i - 1])
            print("%s L%d 重复: %r" % (f, i, m.group(0)[:40] if m else ""))
        print("%s: 新增重复行 %s" % (f, chg[:10]))
        if apply:
            for i in chg:
                cur_lines[i - 1] = old_lines[i - 1]
            io.open(f, "w", encoding="utf-8", newline="").write("\n".join(cur_lines) + "\n")
    print("复核引入重复行共 %d（apply=%s）" % (total, apply))


if __name__ == "__main__":
    main()

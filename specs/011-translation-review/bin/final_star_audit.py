# -*- coding: utf-8 -*-
"""specs/011 终审：修复批次（83fc857 及其后的 style 修复）对每行的星号结构影响。

逐文件取 83fc857^ 原文与当前工作树，逐行 tokenizer 检查：
  原文健康 && 当前不健康 → 复核引入的破坏 → 还原该行（--apply）。
  原文就不健康 → 原始译文残缺，不动（登记）。
用法：python final_star_audit.py [--apply]
"""
import io
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
BASE = "83fc857^"


def star_ok(seg):
    i, stack, n = 0, [], len(seg)
    while i < n:
        if seg[i] == "*":
            if i + 1 < n and seg[i + 1] == "*":
                tok = "**"
            else:
                tok = "*"
            if stack and stack[-1] == tok:
                stack.pop()
            else:
                stack.append(tok)
            i += len(tok)
            continue
        i += 1
    return not stack


def star_lines(t):
    """返回 {lineno: healthy} 逐行星号健康（行内代码段剔除后检查）。"""
    out = {}
    for i, line in enumerate(t.splitlines(), 1):
        segs = line.split("`")
        text = "".join(p for idx, p in enumerate(segs) if idx % 2 == 0)
        out[i] = star_ok(text)
    return out


def main():
    apply = "--apply" in sys.argv
    r = subprocess.run(["git", "show", "--name-only", "--format=", "83fc857"],
                       capture_output=True, text=True)
    files = [l for l in r.stdout.splitlines() if l.endswith(".md") and "/" in l
             and not l.startswith(("specs/", "tools/"))]
    print("修复批次涉及词条文件 %d 个" % len(files))
    broken = introduced = 0
    for f in files:
        cur = io.open(f, encoding="utf-8").read()
        r2 = subprocess.run(["git", "show", "%s:%s" % (BASE, f)], capture_output=True)
        if r2.returncode != 0:
            continue
        old = r2.stdout.decode("utf-8")
        old_h, cur_h = star_lines(old), star_lines(cur)
        old_lines = old.splitlines()
        cur_lines = cur.splitlines()
        if len(old_lines) != len(cur_lines):
            print("行数漂移跳过: %s（%d→%d）" % (f, len(old_lines), len(cur_lines)))
            continue
        chg = []
        for i in range(1, len(old_lines) + 1):
            if old_h.get(i, True) and not cur_h.get(i, True):
                chg.append(i)
        if not chg:
            continue
        introduced += len(chg)
        print("%s: 破坏行 %s" % (f, chg[:8]))
        if apply:
            for i in chg:
                cur_lines[i - 1] = old_lines[i - 1]
            io.open(f, "w", encoding="utf-8", newline="").write("\n".join(cur_lines) + "\n")
            broken += len(chg)
    print("复核引入破坏行 %d（apply=%s，已还原 %d）" % (introduced, apply, broken))


if __name__ == "__main__":
    main()

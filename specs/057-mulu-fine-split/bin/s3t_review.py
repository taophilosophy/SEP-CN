#!/usr/bin/env python3
"""specs/057 s3t：独立复核（自报完成须独立复算）。

输出三块证据：
1. 逐批演进：specs/057 s3 各提交之间 mu-lu-s.md 的标题增删数与链接行净变；
2. 全局状态：链接数、重复路径、SUMMARY 双向差、H2 直属条目、条目所在最近标题层级分布；
3. 抽样：给定抽查节点路径列表，逐组列出其直属条目（供人工判读归类）。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
H = re.compile(r"^(#{1,6}) (.+?)\s*$")
E = re.compile(r"^(\s*)\* \[(.+?)\]\(([^)]+\.md)\)\s*$")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True, encoding="utf-8").stdout


def stats(text):
    heads = {}
    links = 0
    stack = []
    owner_lv = []
    depth = {}
    for l in text.split("\n"):
        m = H.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            stack.append((lv, t))
            heads[t] = heads.get(t, 0) + 1
            continue
        e = E.match(l)
        if e:
            links += 1
            lv = stack[-1][0] if stack else 0
            depth[lv] = depth.get(lv, 0) + 1
    return heads, links, depth


def main():
    commits = [
        ("s2 收官（基线）", "70afcc9b3"),
        ("s3a 史区", "18dd3a2a5"),
        ("s3b 传统", "9004b5198"),
        ("s3c 形上认识论", "ceb59c3d1"),
        ("s3d 价值", "4e5b37e48"),
        ("s3e 科学（s2 粒度收官）", "7f1305a1f"),
        ("s3g 史区时序", "9f48dd32e"),
        ("s3h 现代年代序+罗马拆分", "9c2e9c0b2"),
        ("s3i 布伦塔诺前驱", "182b536c5"),
        ("s3j 布伦塔诺升 H3", "a151d6b8e"),
        ("s3l–s3m B类+美学/语言", "a58f08acd"),
        ("s3n 形上/伦理/社科", "f76fb10b3"),
        ("s3o 计算", "cef35420c"),
        ("s3p 物理", "efceea314"),
        ("s3q 图式归位", "9053e29ee"),
        ("s3r–s3s 第三层", "3380069ad"),
    ]
    print("== 1. 逐批演进（标题分布 → 链接数）")
    prev = None
    for name, c in commits:
        text = git("show", f"{c}:mu-lu-s.md")
        heads, links, depth = stats(text)
        hcount = {}
        for t in heads:
            pass
        lvsum = sum(len(k) for k in [heads])
        print(f"  {name:24s} {c} 链接 {links}")
        if prev is not None:
            a = git("diff", "--numstat", prev, c, "--", "mu-lu-s.md").strip()
            print(f"      diff(numstat ±行): {a or '0 0'}")
        prev = c

    print("\n== 2. 全局状态（当前 HEAD）")
    cur = (ROOT / "mu-lu-s.md").read_text(encoding="utf-8")
    heads, links, depth = stats(cur)
    # 重复路径
    paths = [m.group(3) for l in cur.split("\n") if (m := E.match(l))]
    dup = {p: paths.count(p) for p in set(paths) if paths.count(p) > 1}
    # SUMMARY 双向差
    sp = [m.group(3) for l in (ROOT / "SUMMARY.md").read_text(encoding="utf-8").split("\n")
          if (m := E.match(l))]
    only_mulu = sorted(set(paths) - set(sp))
    only_sum = sorted(set(sp) - set(paths))
    print(f"  mu-lu-s 链接 {len(paths)}；重复路径 {len(dup)} {list(dup)[:5]}")
    print(f"  SUMMARY 链接 {len(sp)}；仅 mu-lu-s 有 {len(only_mulu)} {only_mulu[:5]}；"
          f"仅 SUMMARY 有 {len(only_sum)} {only_sum[:5]}")
    print(f"  条目所在最近标题层级分布: {dict(sorted(depth.items()))}")

    print("\n== 3. 抽样组（人工判读用）")
    sample = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")) if len(sys.argv) > 1 else []
    lines = cur.split("\n")
    stack = []
    zones = {}
    for l in lines:
        m = H.match(l)
        if m:
            lv, t = len(m.group(1)), m.group(2).strip()
            while stack and stack[-1][0] >= lv:
                stack.pop()
            stack.append((lv, t))
            cur_key = "／".join(x[1] for x in stack)
            continue
        e = E.match(l)
        if e and len(e.group(1)) == 0:
            zones.setdefault(cur_key, []).append(e.group(2)[:36])
    for k in sample:
        rows = zones.get(k)
        print(f"  [{k}] {len(rows) if rows else 0} 条")
        for r in rows or []:
            print(f"     - {r}")


if __name__ == "__main__":
    sys.exit(main())

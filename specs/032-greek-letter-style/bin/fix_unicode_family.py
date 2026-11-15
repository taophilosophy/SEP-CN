# -*- coding: utf-8 -*-
r"""specs/032 验收发现（续）：\unicode 构件家族全量修复（5 文件 27 处）。

机制：MathJax 站内包对 \unicode 扩展排版失败（两家族双页实证），统一改原生
Unicode 字符。宏语义由码点保真（en 原形 \lpar/\prurel/\bfrac 均为 SEP 词条宏、
在 needs_expansion，C1 家法强制 zh 展开——现形是翻译期展开的劣形态）。

  logic-linear    \unicode{x214b} → ⅋（U+214B par，18 处，包装 \mathrel 原样保留；
                    孤立提法与兄弟 $\\otimes$/$\\oplus$ 公式形态一致，不入裸文本）
  logic-relevance \unicode{x22b0} → ⊰（U+22B0，3 处）
  diodorus-cronus \unicode{x2B26} → ⬦（U+2B26，2 处）
  heritability    ${^{V_X}\unicode{x2044}_{V_P}}$ → $V_{X}/V_{P}$（3 处，行为遗传学
                    通行 slash 记法）
  justep-coherence ${^{1}\unicode{x2044}_{P(A)^{n-1}}}$ → $1/P(A)^{n-1}$（1 处）

五纪律：预检（树净＋出现计数断言）、逐行台账、幂等、残余门（\\unicode=0）、
结构审计（行数守恒）。
"""
import io
import json
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DRY = "--dry-run" in sys.argv
LEDGER = "specs/032-greek-letter-style/results/unicode-ledger.json"

# (file, [(old, new, expected_count), ...])
SWAPS = [
    ("l/logic-linear.md", [
        ("\\unicode{x214b}", "⅋", 18),
    ]),
    ("l/logic-relevance.md", [
        ("\\unicode{x22b0}", "⊰", 3),
    ]),
    ("d/diodorus-cronus.md", [
        ("\\unicode{x2B26}", "⬦", 2),
    ]),
    ("h/heritability.md", [
        ("$= {^{V_G}\\unicode{x2044}_{V_P}}$", "$= V_{G}/V_{P}$", 1),
        ("${^{V_E}\\unicode{x2044}_{V_P}}$", "$V_{E}/V_{P}$", 1),
        ("{^{V_A}\\unicode{x2044}_{V_P}}", "V_{A}/V_{P}", 1),
    ]),
    ("j/justep-coherence.md", [
        ("${^{1}\\unicode{x2044}_{P(A)^{n-1}}}$", "$1/P(A)^{n-1}$", 1),
    ]),
]

FILES = sorted({f for f, _ in SWAPS})


def git(args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def main():
    out = git(["status", "--porcelain", *FILES]).strip()
    if out:
        print("[拒绝] 目标文件工作区不干净：\n" + out)
        sys.exit(2)
    print("[基线] 五文件干净，基线=HEAD")

    ledger = []
    planned = {}
    for path, ops in SWAPS:
        text = open(path, encoding="utf-8").read()
        for old, new, expect in ops:
            n = text.count(old)
            if n != expect:
                print(f"[拒绝] {path}: {old!r} 出现 {n} 次 ≠ 预期 {expect}")
                sys.exit(2)
        new_text = text
        for old, new, expect in ops:
            start = 0
            while True:
                i = new_text.find(old, start)
                if i == -1:
                    break
                ln = new_text[:i].count("\n") + 1
                ledger.append({"file": path, "line": ln, "old": old, "new": new})
                start = i + len(old)
            new_text = new_text.replace(old, new)
        planned[path] = (text, new_text)

    # 残余门
    for path, (old_t, new_t) in planned.items():
        if re.search(r"\\unicode\{x?[0-9a-fA-F]+\}", new_t):
            print(f"[拒绝] {path} 残余 \\unicode 构件")
            sys.exit(2)
        if new_t.count("\n") != old_t.count("\n"):
            print(f"[拒绝] {path} 行数不守恒")
            sys.exit(2)
    print("[残余门] \\unicode 构件 = 0，行数守恒")

    if DRY:
        print(f"[dry-run] 共 {len(ledger)} 笔，不写回")
        sys.exit(0)

    for path, (old_t, new_t) in planned.items():
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new_t)
        print(f"[写回] {path}")

    json.dump({"schema": "sep-cn-unicode-fix-ledger/1", "date": "2026-11-15",
               "basis": "specs/032 验收发现，C1 家法展开优质形", "rows": ledger},
              open(LEDGER, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"[台账] {LEDGER}: {len(ledger)} 行")

    numstat = git(["diff", "--numstat", *FILES]).strip()
    print("[numstat]\n" + numstat)
    for ln in numstat.splitlines():
        a, d, f = ln.split("\t")
        if a != d:
            print(f"[拒绝] {f} 行数不守恒")
            sys.exit(2)
    print("[审计] 通过")


if __name__ == "__main__":
    main()

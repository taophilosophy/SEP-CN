# -*- coding: utf-8 -*-
r"""specs/032 验收发现：公式渲染缺陷修复（axiom-choice / belief-merging / impossible-worlds）。

三族缺陷（全为既有，非 ADR-0049 试金石回归；行号 2026-11-15 实测）：
  F1 裸 align 无 $$ 包裹（markdown 吃 \\ 成 \，MathJax processEnvironments 抓裸环境）
  F2 zh 侧 \\ 退化成 \（yuanwen 基线完好，修回即收敛，零分歧）
  F3 \bfrac 展开 artifact ${^{1}\unicode{x2044}_{2}}$ 渲染失败 → 原生 Unicode 分数
附：C1 家法宏展开（\sP→\mathcal{P}、\Def→\mathrm{Def}、\mymod→\textit{mod}，
    各取该词条译者行内先例）＋C8 同族（\mbox 内英文连接语 by/using）。

五纪律：预检（树净＋行内容断言）、逐行台账、幂等（精确串替换）、残余门
（修复后裸 align=0、\bfrac artifact=0）、结构审计（行数守恒）。
"""
import io
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

DRY = "--dry-run" in sys.argv
LEDGER = "specs/032-greek-letter-style/results/render-ledger.json"

# (file, line, [(old, new), ...]) — 行号 1-based
FIXES = [
    ("a/axiom-choice.md", 17, [
        ("\\begin{align} f_{1}(\\{0\\})", "$$\\begin{align} f_{1}(\\{0\\})"),
        ("f_{2}(\\{0, 1\\}) &= 1 \\end{align}", "f_{2}(\\{0, 1\\}) &= 1 \\end{align}$$"),
    ]),
    ("a/axiom-choice.md", 68, [
        ("${^{1}\\unicode{x2044}_{2}}$", "½"),
        ("${^{1}\\unicode{x2044}_{3}}$", "⅓"),
    ]),
    ("a/axiom-choice.md", 93, [
        ("\\begin{align} V_0", "$$\\begin{align} V_0"),
        ("V_{\\alpha} \\end{align}", "V_{\\alpha} \\end{align}$$"),
        ("\\sP(V_{\\alpha})", "\\mathcal{P}(V_{\\alpha})"),
    ]),
    ("a/axiom-choice.md", 97, [
        ("\\begin{align} L_0", "$$\\begin{align} L_0"),
        ("L_{\\alpha} \\end{align}", "L_{\\alpha} \\end{align}$$"),
        ("\\Def(L_{\\alpha})", "\\mathrm{Def}(L_{\\alpha})"),
    ]),
    ("a/axiom-choice.md", 212, [
        ("\\begin{align} \\tag{1}", "$$\\begin{align} \\tag{1}"),
        ("x = 1)] \\end{align}", "x = 1)] \\end{align}$$"),
    ]),
    ("a/axiom-choice.md", 270, [
        ("\\begin{align} x \\in U", "$$\\begin{align} x \\in U"),
        ("g(x,0) = g(x,1). \\end{align}", "g(x,0) = g(x,1). \\end{align}$$"),
        ("\\mbox{by (**)}", "\\mbox{由（**）}"),
        ("\\mbox{using (*)}", "\\mbox{用（*）}"),
    ]),
    ("b/belief-merging.md", 185, [
        ("\\begin{align} K_1", "$$\\begin{align} K_1"),
        ("\\end{align}", "\\end{align}$$"),
        ("\\mymod(K_1)", "\\textit{mod}(K_1)"),
        ("\\mymod(K_{2})", "\\textit{mod}(K_{2})"),
        ("\\mymod(K_{3})", "\\textit{mod}(K_{3})"),
    ]),
    ("i/impossible-worlds.md", 212, [
        ("&= 0 \\ v_w (\\Diamond A)", "&= 0 \\\\ v_w (\\Diamond A)"),
    ]),
]

FILES = sorted({f for f, _, _ in FIXES})


def git(args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def preflight():
    out = git(["status", "--porcelain", *FILES]).strip()
    if out:
        print("[拒绝] 目标文件工作区不干净：\n" + out)
        sys.exit(2)
    print("[基线] 三文件干净，基线=HEAD")


def main():
    preflight()
    ledger = []
    planned = {}
    for path, ln, ops in FIXES:
        lines = open(path, encoding="utf-8").read().splitlines()
        line = lines[ln - 1]
        new = line
        for old, rep in ops:
            if new.count(old) != 1:
                print(f"[拒绝] {path} L{ln} 断言失败：{old!r} 出现 {new.count(old)} 次")
                sys.exit(2)
            new = new.replace(old, rep)
        planned.setdefault(path, {})[ln] = (line, new)
        for old, rep in ops:
            ledger.append({"file": path, "line": ln, "old": old, "new": rep})

    for path, by_ln in planned.items():
        lines = open(path, encoding="utf-8").read().splitlines()
        before = len(lines)
        for ln, (old, new) in by_ln.items():
            lines[ln - 1] = new
        text = "\n".join(lines) + ("\n" if open(path, encoding="utf-8").read().endswith("\n") else "")
        if text.count("\n") != before:
            print(f"[拒绝] {path} 行数不守恒")
            sys.exit(2)
        planned[path] = text

    # 残余门：修复后三文件裸 align=0、x2044 artifact=0、sP/Def/mymod 裸用=0
    # 剥 $$ 块须带反斜杠转义感知（"令 $\$$ 是…$\$w$" 中相邻两 $ 属不同行内公式，
    # 无 lookbehind 会假配对吞块——impossible-worlds L180 实测）。
    for path in FILES:
        t = planned[path]
        stripped = re.sub(r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$", "", t)
        bare = re.findall(r"\\begin\{(?:align|aligned|gather|equation|cases|matrix)\}", stripped)
        if bare:
            print(f"[拒绝] {path} 残余裸环境 {len(bare)} 处")
            sys.exit(2)
        if "\\unicode{x2044}" in t:
            print(f"[拒绝] {path} 残余 x2044 artifact")
            sys.exit(2)
        for macro in ("\\sP", "\\Def", "\\mymod"):
            if macro in t:
                print(f"[拒绝] {path} 残余未展开宏 {macro}")
                sys.exit(2)
    print("[残余门] 裸环境/x2044/未展开宏 = 0")

    if DRY:
        print(f"[dry-run] 共 {len(ledger)} 笔操作，不写回")
        sys.exit(0)

    for path, text in planned.items():
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        print(f"[写回] {path}")

    json.dump({"schema": "sep-cn-render-fix-ledger/1", "date": "2026-11-15",
               "basis": "specs/032 验收发现，C1/C8 家法", "rows": ledger},
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

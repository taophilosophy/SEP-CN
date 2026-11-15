# -*- coding: utf-8 -*-
r"""specs/032 铺开批次 C 类嫌疑 27 处人工判读修复。

判据（ADR-0049 决策 1，GB 3102.11 变量斜体/算符正体），逐处上下文见执行记录：
  斜体（变量/具名集）：字母表与签名 Σ、可能世界集/状态集 Ω、二阶测度 μ、LU 语境 Δ
  正体（算子）：可计算性无界极小化算子 μ、ramsey 增量 Δ
"""
import io
import json
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DRY = "--dry-run" in sys.argv
LEDGER = "specs/032-greek-letter-style/results/c-deferred-ledger.json"

# (file, line, span, cls, count)
ITEMS = [
    ("c/computability.md", 38, "$\\Sigma$", "A", 2),
    ("c/computability.md", 164, "$\\mu$", "C", 1),
    ("c/computability.md", 174, "$\\mu$", "C", 1),
    ("d/dynamic-semantics.md", 122, "$\\Sigma$", "A", 2),
    ("f/fitness.md", 75, "$\\Omega$", "A", 1),
    ("i/imprecise-probabilities.md", 35, "$\\Omega$", "A", 6),
    ("i/imprecise-probabilities.md", 54, "$\\Omega$", "A", 2),
    ("i/imprecise-probabilities.md", 347, "$\\mu$", "A", 2),
    ("l/logic-linear.md", 80, "$\\Delta$", "A", 1),
    ("l/logic-linear.md", 208, "$\\Delta$", "A", 1),
    ("l/logic-linear.md", 214, "$\\Delta$", "A", 1),
    ("l/logic-preference.md", 531, "$\\Omega$", "A", 3),
    ("r/ramsey-economics.md", 164, "$\\Delta$", "C", 1),
    ("r/ramsey-economics.md", 244, "$\\mu$", "A", 1),
    ("r/ramsey-economics.md", 252, "$\\mu$", "A", 1),
    ("r/ramsey-economics.md", 270, "$\\mu$", "A", 1),
]
UNI = {"Sigma": "Σ", "mu": "μ", "Omega": "Ω", "Delta": "Δ"}
CMD = {"$\\Sigma$": "Sigma", "$\\mu$": "mu", "$\\Omega$": "Omega", "$\\Delta$": "Delta"}
FILES = sorted({f for f, *_ in ITEMS})


def git(args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def main():
    # 本阶段基线=阶段1（rollout_batch）写回后的状态，脏树属预期；
    # 归属核对：阶段1台账里的文件集合须覆盖本阶段全部目标文件
    roll = json.load(open("specs/032-greek-letter-style/results/rollout-ledger.json",
                          encoding="utf-8"))
    roll_files = {r["file"].replace("\\", "/") for r in roll["rows"]}
    for path in FILES:
        if path not in roll_files:
            print(f"[拒绝] {path} 不在阶段1台账内，脏树归属不明")
            sys.exit(2)
    dirty = [p for p in FILES if git(["status", "--porcelain", p]).strip()]
    print(f"[基线] 阶段1产物之上作业；本阶段目标 {len(FILES)} 文件，其中阶段1已改 {len(dirty)}")

    ledger = []
    planned = {}
    for path, ln, span, cls, cnt in ITEMS:
        lines = open(path, encoding="utf-8").read().splitlines()
        if path not in planned:
            planned[path] = list(lines)
        idx = ln - 1
        if planned[path][idx].count(span) != cnt:
            print(f"[拒绝] {path} L{ln} {span!r} 出现 {planned[path][idx].count(span)} 次 ≠ {cnt}")
            sys.exit(2)
        rep = UNI[CMD[span]] if cls == "C" else f"*{UNI[CMD[span]]}*"
        planned[path][idx] = planned[path][idx].replace(span, rep)
        for _ in range(cnt):
            ledger.append({"file": path, "line": ln, "old": span, "new": rep,
                           "cls": cls, "why": "算子" if cls == "C" else "变量"})

    for path, new_lines in planned.items():
        old_lines = open(path, encoding="utf-8").read().splitlines()
        if len(new_lines) != len(old_lines):
            print(f"[拒绝] {path} 行数不守恒")
            sys.exit(2)
        planned[path] = "\n".join(new_lines) + "\n"

    # 残余门：C 嫌疑码点孤立片段全库清零
    for path in FILES:
        t = planned[path]
        for ln, line in enumerate(t.splitlines(), 1):
            if "$$" in line or "`" in line:
                continue
            for m in re.finditer(r"\$(\\(?:Delta|mu|Omega|Sigma|Lambda))\$", line):
                print(f"[拒绝] {path} L{ln} 残余 {m.group(0)}")
                sys.exit(2)
    print("[残余门] C 嫌疑孤立片段 = 0")

    if DRY:
        print(f"[dry-run] 共 {len(ledger)} 笔，不写回")
        sys.exit(0)

    for path, text in planned.items():
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        print(f"[写回] {path}")

    json.dump({"schema": "sep-cn-greek-cdeferred-ledger/1", "date": "2026-11-15",
               "basis": "ADR-0049 决策1，GB 3102.11 变量斜体/算符正体", "rows": ledger},
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

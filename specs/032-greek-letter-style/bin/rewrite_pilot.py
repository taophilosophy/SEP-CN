# -*- coding: utf-8 -*-
r"""specs/032 试金石回改：三件 A/C 类孤立希腊字母公式转文字。

批量改写五纪律（rules/05）：
  1. 残余前置门   写回前断言目标清单非空、写回后 A/C 类残余=0
  2. 幂等         精确串替换，重跑无变化即退出 0
  3. 逐行身份追踪 逐处台账写 specs/032-greek-letter-style/results/ledger.json
  4. 基线还原前置 目标文件工作区必须干净（基线=HEAD），否则拒绝
  5. 写回前结构审计 行数守恒、含 $$ 行禁改、改动行数=预期、numstat 限定三件

用法: python specs/032-greek-letter-style/bin/rewrite_pilot.py [--dry-run]
"""
import io
import json
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)

DRY = "--dry-run" in sys.argv

# (file, cmd) → 类别
CLASS_MAP = {
    "b/belief-merging.md": {"omega": "A", "varphi": "A", "Phi": "A", "Delta": "C"},
    "a/axiom-choice.md": {"pi": "A", "alpha": "A", "Phi": "A", "beta": "A",
                          "kappa": "A", "lambda": "A", "mu": "A", "phi": "A"},
    "l/logic-dynamic.md": {"alpha": "A", "beta": "A", "pi": "A", "mu": "C", "Delta": "C"},
}
UNI = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
    "zeta": "ζ", "eta": "η", "theta": "θ", "iota": "ι", "kappa": "κ",
    "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π", "rho": "ρ",
    "sigma": "σ", "tau": "τ", "phi": "φ", "varphi": "φ", "chi": "χ", "psi": "ψ",
    "omega": "ω", "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ",
    "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ", "Upsilon": "Υ", "Phi": "Φ", "Psi": "Ψ",
    "Omega": "Ω",
}
FILES = list(CLASS_MAP)
LEDGER = "specs/032-greek-letter-style/results/ledger.json"


def git(args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def check_dirty():
    out = git(["status", "--porcelain", *FILES])
    if out.strip():
        print("[拒绝] 目标文件工作区不干净（基线≠HEAD），先处理再跑：")
        print(out)
        sys.exit(2)
    print("[基线] 三件工作区干净，基线=HEAD")


def scan(text, path):
    """返回 [(行号, span, cmd)]，仅纯孤立（无撇号/下标）。"""
    pmap = CLASS_MAP[path]
    hits = []
    for ln, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\$(\\([A-Za-z]+))\$", line):
            span, cmd = m.group(0), m.group(2)
            if cmd in pmap:
                hits.append((ln, span, cmd))
    return hits


def main():
    check_dirty()
    ledger = []
    planned = {}
    for path in FILES:
        text = open(path, encoding="utf-8").read()
        before_lines = text.count("\n")
        hits = scan(text, path)
        pmap = CLASS_MAP[path]
        by_cmd = {}
        for ln, span, cmd in hits:
            by_cmd.setdefault(cmd, []).append(ln)
        print(f"[计划] {path}: {len(hits)} 处 — " +
              ", ".join(f"{c}×{len(v)}({pmap[c]}→{UNI[c]})" for c, v in sorted(by_cmd.items())))
        if not hits:
            continue
        # $$ 行硬守卫
        dd_lines = {ln for ln, line in enumerate(text.splitlines(), 1) if "$$" in line}
        bad = [h for h in hits if h[0] in dd_lines]
        if bad:
            print(f"[拒绝] {path} 命中含 $$ 行 {sorted(set(b[0] for b in bad))}，人工复核")
            sys.exit(2)
        new_lines = text.splitlines()
        changed = 0
        groups = {}
        for ln, span, cmd in hits:
            groups.setdefault((ln, span, cmd), 0)
            groups[(ln, span, cmd)] += 1
        for (ln, span, cmd), cnt in groups.items():
            cls = pmap[cmd]
            rep = UNI[cmd] if cls == "C" else f"*{UNI[cmd]}*"
            idx = ln - 1
            if new_lines[idx].count(span) != cnt:
                print(f"[拒绝] L{ln} 片段 {span} 出现 {new_lines[idx].count(span)} 次 ≠ 扫描 {cnt} 次")
                sys.exit(2)
            new_lines[idx] = new_lines[idx].replace(span, rep)
            for _ in range(cnt):
                ledger.append({"file": path, "line": ln, "cls": cls,
                               "old": span, "new": rep, "cmd": cmd})
            changed += cnt
        after_text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
        if after_text.count("\n") != before_lines:
            print(f"[拒绝] {path} 行数不守恒")
            sys.exit(2)
        planned[path] = (text, after_text, changed)

    # 残余前置门（模拟写回后）
    for path, (old, new, _) in planned.items():
        resid = [h for h in scan(new, path)]
        if resid:
            print(f"[拒绝] {path} 模拟写回后仍余 {len(resid)} 处 A/C 类")
            sys.exit(2)
    print("[残余门] 模拟写回后 A/C 类残余 = 0")

    if DRY:
        print("[dry-run] 不写回，共计划 %d 处" % sum(c for _, _, c in planned.values()))
        sys.exit(0)

    for path, (old, new, changed) in planned.items():
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new)
        print(f"[写回] {path}: {changed} 处")

    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    json.dump({"schema": "sep-cn-greek-ledger/1", "date": "2026-11-15",
               "basis": "ADR-0049 proposed", "rows": ledger},
              open(LEDGER, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"[台账] {LEDGER}: {len(ledger)} 行")

    # 结构审计
    numstat = git(["diff", "--numstat", *FILES]).strip()
    print("[numstat]\n" + numstat)
    files_touched = {ln.split("\t")[2] for ln in numstat.splitlines()}
    if files_touched - set(FILES):
        print("[拒绝] numstat 越界")
        sys.exit(2)
    for ln in numstat.splitlines():
        a, d, f = ln.split("\t")
        if a != d:
            print(f"[拒绝] {f} 增删行数不等（{a}/{d}）")
            sys.exit(2)
    print("[审计] 行数守恒、范围限定三件 — 通过")


if __name__ == "__main__":
    main()

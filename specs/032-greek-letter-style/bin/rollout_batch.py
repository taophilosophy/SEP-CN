# -*- coding: utf-8 -*-
r"""ADR-0049 铺开批次：全库孤立希腊字母公式→文字（试金石三件之外的存量）。

口径（ADR-0049 accepted 决策 1/2）：
  A 类（变量）      → *α* 斜体文字
  C 类嫌疑（待人工）→ 不动，出清单：孤立 $\Delta$ / $\mu$ / $\Omega$ / $\Sigma$ / $\Lambda$
                      （算子/专名嫌疑，GB 3102.11 算符正体 vs 变量斜体须逐处判读）
  B 类（派生形/复合式/公式段）→ 不动

五纪律：预检（逐文件树净检查，脏文件跳过并报告）、逐行台账、幂等、
残余门（非嫌疑 A 类残余=0）、结构审计（行数守恒）。含 $$ 的行禁改。

用法: python specs/032-greek-letter-style/bin/rollout_batch.py [--dry-run]
"""
import io
import json
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DRY = "--dry-run" in sys.argv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
os.chdir(ROOT)
LEDGER = "specs/032-greek-letter-style/results/rollout-ledger.json"

G = ("alpha|beta|gamma|delta|epsilon|varepsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|pi|rho|"
     "sigma|tau|upsilon|phi|varphi|chi|psi|omega|varpi|varrho|varsigma|vartheta|"
     "Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega").split("|")
UNI = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
    "varepsilon": "ε", "zeta": "ζ", "eta": "η", "theta": "θ", "iota": "ι",
    "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π",
    "rho": "ρ", "sigma": "σ", "tau": "τ", "phi": "φ", "varphi": "φ", "chi": "χ",
    "psi": "ψ", "omega": "ω", "varpi": "ϖ", "varrho": "ϱ", "varsigma": "ς",
    "vartheta": "ϑ", "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ",
    "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ", "Upsilon": "Υ", "Phi": "Φ", "Psi": "Ψ",
    "Omega": "Ω",
}
# C 类嫌疑：孤立出现时须人工判读（算子/专名 vs 变量），本脚本一律不动
C_DEFER = {"Delta", "mu", "Omega", "Sigma", "Lambda"}
RE_LONE = re.compile(r"\$(\\([A-Za-z]+))\$")


def git(args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def scan_targets():
    """扫描全库 letter/*.md 的纯孤立希腊字母，按 A 可转 / C 嫌疑分桶。"""
    a_hits, c_hits = {}, {}
    for d in sorted(os.listdir(".")):
        if not (len(d) == 1 and d.isalpha() and d.islower() and os.path.isdir(d)):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            p = os.path.join(d, f)
            t = open(p, encoding="utf-8").read()
            for ln, line in enumerate(t.splitlines(), 1):
                if "$$" in line:
                    continue  # $$ 行硬守卫
                if "`" in line:
                    continue  # 反引号行守卫：行内代码与 Quine 式引名（quine-nf L13 实测）
                             # 会与代码语义冲突，整行豁免出清单人工处置
                for m in RE_LONE.finditer(line):
                    cmd = m.group(2)
                    if cmd in G:
                        (a_hits if cmd not in C_DEFER else c_hits).setdefault(p, []).append(
                            (ln, m.group(0), cmd))
    return a_hits, c_hits


def main():
    a_hits, c_hits = scan_targets()
    n_a = sum(len(v) for v in a_hits.values())
    n_c = sum(len(v) for v in c_hits.values())
    print(f"[扫描] A 类可转 {n_a} 处/{len(a_hits)} 文件；C 类嫌疑（不动，出清单）{n_c} 处/{len(c_hits)} 文件")

    # 逐文件树净检查
    dirty = [p for p in a_hits if git(["status", "--porcelain", p]).strip()]
    for p in dirty:
        print(f"[跳过] {p} 工作区脏（他会或在途），本轮不动")
        a_hits.pop(p)

    ledger = []
    planned = {}
    for p, hits in sorted(a_hits.items()):
        lines = open(p, encoding="utf-8").read().splitlines()
        new_lines = list(lines)
        changed = 0
        groups = {}
        for ln, span, cmd in hits:
            groups.setdefault((ln, span, cmd), 0)
            groups[(ln, span, cmd)] += 1
        for (ln, span, cmd), cnt in groups.items():
            rep = f"*{UNI[cmd]}*"
            idx = ln - 1
            if new_lines[idx].count(span) != cnt:
                print(f"[拒绝] {p} L{ln} 片段 {span} 出现 {new_lines[idx].count(span)} 次 ≠ 扫描 {cnt}")
                sys.exit(2)
            new_lines[idx] = new_lines[idx].replace(span, rep)
            for _ in range(cnt):
                ledger.append({"file": p, "line": ln, "old": span, "new": rep, "cmd": cmd})
            changed += cnt
        old_text = "\n".join(lines) + "\n"
        new_text = "\n".join(new_lines) + "\n"
        if new_text.count("\n") != old_text.count("\n"):
            print(f"[拒绝] {p} 行数不守恒")
            sys.exit(2)
        planned[p] = new_text

    # 残余门：非嫌疑 A 类=0（按文件重扫；$$ 行与反引号行同守卫豁免）
    for p in planned:
        t = planned[p]
        for ln, line in enumerate(t.splitlines(), 1):
            if "$$" in line or "`" in line:
                continue
            for m in RE_LONE.finditer(line):
                if m.group(2) in G and m.group(2) not in C_DEFER:
                    print(f"[拒绝] {p} L{ln} 残余 {m.group(0)}")
                    sys.exit(2)
    print("[残余门] 非嫌疑 A 类 = 0")

    if DRY:
        print(f"[dry-run] 共 {len(ledger)} 处，不写回")
        for p, hits in sorted(c_hits.items()):
            by = {}
            for _, _, cmd in hits:
                by[cmd] = by.get(cmd, 0) + 1
            print(f"  C 待审 {p}: {len(hits)} 处 {by}")
        sys.exit(0)

    for p, t in planned.items():
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(t)
        print(f"[写回] {p} ({sum(1 for r in ledger if r['file'] == p)} 处)")

    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    json.dump({"schema": "sep-cn-greek-rollout-ledger/1", "date": "2026-11-15",
               "basis": "ADR-0049 accepted 铺开批次", "rows": ledger,
               "c_deferred": {p: [{"line": ln, "span": s, "cmd": c} for ln, s, c in hits]
                              for p, hits in sorted(c_hits.items())}},
              open(LEDGER, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"[台账] {LEDGER}: {len(ledger)} 行（C 嫌疑 {n_c} 处另列 c_deferred）")

    numstat = git(["diff", "--numstat", *sorted(planned)]).strip()
    for ln in numstat.splitlines():
        a, d, f = ln.split("\t")
        if a != d:
            print(f"[拒绝] {f} 行数不守恒")
            sys.exit(2)
    print(f"[审计] 通过（{len(numstat.splitlines())} 文件）")

    print("\n== C 类待审清单（人工判读后处置，算子正体/变量斜体）：")
    for p, hits in sorted(c_hits.items()):
        for ln, span, cmd in hits:
            line = open(p, encoding="utf-8").read().splitlines()[ln - 1]
            i = line.find(span)
            print(f"  {p} L{ln} [{span}] …{line[max(0, i-40):i+len(span)+40]}…")


if __name__ == "__main__":
    main()

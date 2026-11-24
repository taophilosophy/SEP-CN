#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""归并探针（specs/060 分析用）：构造“六轴并入 S3”的假想 pipeline，跑 check_stages。

用途：证明现有谓词能否机检“归并”这一违例。结论（2026-11-25 实测）：
  六轴判据全部挂到 S3、删除 q1–q6 后，check_stages 13 项全绿——
  即 P29（六轴独立）的机检承载不足，S2 只查“一个判据多个硬拦位”，
  不查“一个节点多个判据”。本探针为该缺口的可复算凭证。

用法: python specs/060-six-axis-quality-gates/bin/probe_merge.py
输出: stdout 结论；临时文件 state/merged-test.json（运行态，不入库）。
退出码: 0 探针执行完成（不表示归并可接受）。
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
PIPE = os.path.join(ROOT, "rules", "pipeline.json")
TMP = os.path.join(ROOT, "state", "merged-test.json")
QS = ["q1", "q2", "q3", "q4", "q5", "q6"]


def main():
    with open(PIPE, "rb") as f:
        d = json.loads(f.read().decode("utf-8"))
    crit = []
    for n in d["nodes"]:
        if n["id"] in QS:
            crit += n.get("criteria", [])
    d["nodes"] = [n for n in d["nodes"] if n["id"] not in QS]
    for n in d["nodes"]:
        if n["id"] == "S3":
            n["prev"] = "global"
            n["criteria"] = crit + ["check_style", "check_images", "check_summary"]
            n["gate_owner"] = True
    owner = {k: v for k, v in d["criteria_owner"].items() if k != "note"}
    for c in crit:
        owner[c] = ["S3"]
    for c in ("check_style", "check_images", "check_summary"):
        owner.setdefault(c, ["S3"])
    d["criteria_owner"] = owner
    d["mandatory_minimum"]["nodes"] = [x for x in d["mandatory_minimum"]["nodes"]
                                       if x not in QS]
    os.makedirs(os.path.dirname(TMP), exist_ok=True)
    with open(TMP, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)

    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_stages.py"),
                        "--pipe", TMP], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    last = (r.stdout or "").strip().splitlines()[-1] if r.stdout else ""
    print("合并后节点数：%d；S3 判据数：%d" % (len(d["nodes"]), len(crit) + 3))
    print(last)
    print("结论：%s" % ("现有谓词拦不住归并（需补“每节点判据数 ≤1 或同对象类”)"
                        if r.returncode == 0 else "现有谓词可拦归并"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

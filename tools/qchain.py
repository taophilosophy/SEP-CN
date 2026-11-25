# -*- coding: utf-8 -*-
"""六轴工序编排器（ADR-0079；只编排不裁判）。

用法:
  python tools/qchain.py [路径...] [--all] [--gate] [--json] [--out PATH]

默认依次跑 cite/logic/grammar/register/measure/punct 六器的报告模式，汇总为一张
工单；--gate 追加六器门禁（各器 T0 最小档），任一失败退出码 1。

纪律：本器不产出合格判定，不替代任何单器，不写任务状态（推进仍走 task_ops）。
退出码: 0 全通过/仅报告；1 --gate 有失败；2 用法错误。
"""
import argparse
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import axis_lib as ax  # noqa: E402

TOOLS = os.path.join(ax.ROOT, "tools")
ORDER = [("rv-03", "cite_audit.py"), ("rv-04", "logic_audit.py"),
         ("rv-05", "grammar_audit.py"), ("rv-06", "register_audit.py"),
         ("rv-07", "measure_audit.py"), ("rv-08", "punct_audit.py")]


def run(script, paths, gate=False):
    cmd = [sys.executable, os.path.join(TOOLS, script)] + list(paths)
    if gate:
        cmd.append("--gate")
    cmd.append("--json")
    r = subprocess.run(cmd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    try:
        data = json.loads(r.stdout)
    except Exception:
        data = {"schema": "error", "stdout": r.stdout[-500:], "stderr": r.stderr[-500:]}
    return r.returncode, data


def summarize(name, data):
    files = data.get("files", [])
    if name == "rv-03":
        n = sum(f.get("quote_level", 0) for f in files)
    elif name in ("rv-04",):
        n = sum(f.get("sentences", 0) for f in files)
    elif name in ("rv-05", "rv-06", "rv-07", "rv-08"):
        n = sum(f.get("issues", 0) for f in files)
    else:
        n = len(files)
    return {"files": len(files), "items": n,
            "problems": len(data.get("problems", []))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.all:
        args.paths = ax.target_paths(None)
    if not args.paths:
        ap.error("需要路径或 --all")

    out = {"schema": "qchain/v1", "gate": bool(args.gate), "nodes": {}}
    fails = 0
    for node, script in ORDER:
        rc, data = run(script, args.paths, args.gate)
        out["nodes"][node] = {"tool": script, "rc": rc,
                              "summary": summarize(node, data),
                              "problems": data.get("problems", [])[:20]}
        if rc == 1:
            fails += 1
    out["failed_nodes"] = fails

    default = os.path.join(ax.ROOT, "state", "axis", "qchain-latest.json")
    ax.emit(out, args.out or default)
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        print("%-6s %-18s %6s %8s %8s %4s"
              % ("节点", "工具", "文件", "条目", "问题", "rc"))
        for node, v in out["nodes"].items():
            s = v["summary"]
            print("%-6s %-18s %6d %8d %8d %4d"
                  % (node, v["tool"], s["files"], s["items"], s["problems"], v["rc"]))
        print("\n结果：%s" % ("全通过" if fails == 0 else "%d 个节点未通过" % fails))
        print("工单：%s" % os.path.relpath(default, ax.ROOT))
    return 1 if (args.gate and fails) else 0


if __name__ == "__main__":
    sys.exit(main())

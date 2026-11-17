# -*- coding: utf-8 -*-
"""管线判据登记表核对（ADR-0068：rules/pipeline.json 为判据唯一事实源）。

四谓词（全部只读，A11 判官只读）：
  S1 链闭合   prev 链首/链尾唯一、无环、无悬挂、覆盖全部节点
  S2 判据唯一 每个判据至多一个硬拦节点（gate_owner），且与 criteria_owner 双向一致
  S3 强制集   mandatory_minimum 是节点子集，且含 R1/R2/R3
  S4 类型值域  type ∈ {pipe,stage,review,format}；review 必须属强制集

用法: python tools/check_stages.py [--json]
退出码: 0 全绿；1 有违例；2 输入缺失（A12 禁静默兜底）。
"""
import argparse
import io
import json
import os
import sys

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPE = os.path.join(ROOT, "rules", "pipeline.json")
TYPES = {"pipe", "stage", "review", "format"}


def load_pipeline(path=PIPE):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def check(pipe):
    """纯函数：对 pipeline dict 求值，返回 hits 列表（无 IO，可单测）。"""
    nodes = pipe.get("nodes", [])
    by = {n["id"]: n for n in nodes}
    ids = set(by)
    mand = set(pipe.get("mandatory_minimum", {}).get("nodes", []))
    owner = {k: v for k, v in pipe.get("criteria_owner", {}).items() if k != "note"}

    hits = []

    def rec(code, name, ok, detail=""):
        hits.append({"code": code, "name": name, "ok": bool(ok), "detail": detail})

    # ---- S1 链闭合 ----
    heads = [i for i in by if not by[i].get("prev")]
    tails = [i for i in by if i not in {n.get("prev") for n in nodes}]
    rec("S1", "链首唯一", len(heads) == 1, "链首=%s" % heads)
    rec("S1", "链尾唯一", len(tails) == 1, "链尾=%s" % tails)

    cyc = []
    for start in by:
        path, cur = [], start
        while cur and cur not in path:
            path.append(cur)
            cur = by[cur].get("prev")
        if cur:
            cyc.append(path)
    rec("S1", "无环", not cyc, "环=%s" % (cyc[:2] if cyc else "无"))

    dangling = [n["id"] for n in nodes if n.get("prev") and n["prev"] not in ids]
    rec("S1", "prev 无悬挂", not dangling, "悬挂=%s" % (dangling or "无"))

    # ---- S2 判据唯一 ----
    hard = {}
    for n in nodes:
        if n.get("gate_owner"):
            for g in n.get("criteria", []):
                hard.setdefault(g, []).append(n["id"])
    multi = {g: v for g, v in hard.items() if len(v) > 1}
    rec("S2", "判据硬拦唯一", not multi, "多挂=%s" % (multi or "无"))

    unreg, back = [], []
    for n in nodes:
        if not n.get("gate_owner"):
            continue
        for g in n.get("criteria", []):
            if g not in owner or n["id"] not in owner[g]:
                unreg.append("%s:%s" % (n["id"], g))
    for g, ns in owner.items():
        for nid in ns:
            if nid not in by or g not in by[nid].get("criteria", []):
                back.append("%s->%s" % (g, nid))
    rec("S2", "硬拦判据已登记", not unreg, "未登记=%s" % (unreg or "无"))
    rec("S2", "登记表反向完备", not back, "悬挂=%s" % (back or "无"))

    # ---- S3 强制集 ----
    rec("S3", "强制集是节点子集", mand <= ids, "越界=%s" % sorted(mand - ids))
    rec("S3", "R1/R2/R3 在强制集内", {"R1", "R2", "R3"} <= mand,
        "差集=%s" % sorted({"R1", "R2", "R3"} - mand))

    # ---- S4 类型值域 ----
    badtype = [n["id"] for n in nodes if n.get("type") not in TYPES]
    rec("S4", "type 值域合法", not badtype, "非法=%s" % (badtype or "无"))
    lax = [n["id"] for n in nodes if n.get("type") == "review" and n["id"] not in mand]
    rec("S4", "review 必属强制", not lax, "非强制=%s" % (lax or "无"))

    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--pipe", default=PIPE, help="被验的 pipeline JSON（负向测试用）")
    args = ap.parse_args()

    pipe_path = args.pipe if os.path.isabs(args.pipe) else os.path.join(ROOT, args.pipe)
    if not os.path.exists(pipe_path):
        print("输入缺失: %s（判据唯一事实源，A12 禁静默兜底）" % pipe_path, file=sys.stderr)
        return 2

    with open(pipe_path, "rb") as f:
        pipe = json.loads(f.read().decode("utf-8"))

    hits = check(pipe)
    fails = [h for h in hits if not h["ok"]]
    for h in hits:
        print("[%s] %-18s %s%s" % (h["code"], h["name"], "PASS" if h["ok"] else "FAIL",
                                    "" if h["ok"] else "  -> " + h["detail"]))
    print("汇总：%d 项，通过 %d，失败 %d" % (len(hits), len(hits) - len(fails), len(fails)))

    if args.json:
        print(json.dumps({"nodes": len(pipe.get("nodes", [])), "total": len(hits),
                          "passed": len(hits) - len(fails), "failed": len(fails),
                          "results": hits}, ensure_ascii=False, indent=1))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())

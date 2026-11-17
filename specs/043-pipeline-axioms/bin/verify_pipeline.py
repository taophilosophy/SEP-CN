# -*- coding: utf-8 -*-
"""总执行书的公理化验证：把 51 条谓词写成可执行判定，对四份输入逐条算。

为何需要：文档里"充分""融洽"是断言，不是结论。只有把每条性质写成返回布尔值的
纯函数，并对真实数据求值，才能说"成立"。本脚本不含推断，只做集合与函数计算。

输入：
  rules/pipeline.json     16 个作业节点与判据归属
  journal-schema.json  事件模型（节点集只引用，不内嵌）
  axioms.json          28 条公理、2 条定理与谓词映射
  zong-zhi-xing-shu.md 总执行书的自述块

判据分组：
  A 结构（链的唯一性、无环、覆盖、段单调与连续、出度）
  B 判据（硬拦唯一、双向登记完备、非空）
  C 强制（最小集存在性、R 链在集内、强制节点有承接）
  D 覆盖（每个要求有节点、每个节点有归属、承接体非空、独占）—— 充分性
  E 单一源（不内嵌、引用相符、强制集一致）
  F 降级（值域、replace 需有判据承接）
  G 段契约（段首接上段尾、段尾闭合）
  H 类型（值域、review 必强制）
  I 完备（产物与动作非空）
  J 输入卫生（JSON 无重复键、节点 id 唯一）
  K 公理登记（编号、类型、引用、来源、定理、退役、纪律清单）
  L 文档自述（总执行书声明的数量与实算一致）

用法: python specs/043-pipeline-axioms/bin/verify_pipeline.py [--json PATH]
      [--pipe PATH] [--schema PATH] [--plan PATH]
退出码: 0 全部通过；1 存在违反；2 输入缺失。
"""
import argparse
import io
import json
import os
import re
import sys

if getattr(sys.stdout, "encoding", None) and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PIPE = os.path.join(ROOT, "rules", "pipeline.json")
SCHEMA = os.path.join(ROOT, "jian-yi-shu", "journal-schema.json")
AXIOMS = os.path.join(ROOT, "jian-yi-shu", "axioms.json")
PLAN = os.path.join(ROOT, "jian-yi-shu", "zong-zhi-xing-shu.md")

TYPES = {"pipe", "stage", "review", "format"}
REPLAY = {"widen", "tighten", "replace"}

# 要求登记册：来源 rules/01 02 03 07 09、specs/039、ADR-0021 0024 0047 0052 0054 0062 0063
REQUIREMENTS = {
    "R01 源可信": ["s0"],
    "R02 转换保真": ["P3"],
    "R03 差异二分": ["P3"],
    "R04 md 禁实质变动": ["P3"],
    "R05 术语主形": ["s2.4"],
    "R06 勘误参考读法": ["s2.4"],
    "R07 准确性": ["s1"],
    "R08 语体": ["s2"],
    "R09 体例": ["S3"],
    "R10 学术规范": ["global"],
    "R11 全局一致性": ["global"],
    "R12 图表公式": ["global"],
    "R13 图片引用": ["S3"],
    "R14 受众适切": ["R1"],
    "R15 逻辑连贯": ["R2"],
    "R16 交付验收": ["R3"],
    "R17 目录一致": ["S3"],
    "R18 格式闭合": ["F1", "F2"],
}

# 产出节点：本身不覆盖要求，但产出被下游判据检查的对象
PRODUCERS = {
    "P1": "产出 HTML，被 s0 检",
    "P2": "产出 yuanwen，被 P3 检",
    "P4": "产出术语摘录，被 s2.4 检",
    "draft": "产出译文，被 s1 起检",
}


def load(path):
    """读取 JSON 并拒绝重复键：json 默认静默取后者，重复键会掩盖真实冲突。"""
    dup = []

    def hook(pairs):
        seen = {}
        for k, v in pairs:
            if k in seen:
                dup.append(k)
            seen[k] = v
        return seen

    with open(path, encoding="utf-8") as fh:
        data = json.load(fh, object_pairs_hook=hook)
    return data, dup


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    ap.add_argument("--pipe", default=PIPE, help="被验的 pipeline JSON（负向测试用）")
    ap.add_argument("--schema", default=SCHEMA, help="被验的 journal schema JSON")
    ap.add_argument("--plan", default=PLAN, help="被验的总执行书 Markdown")
    args = ap.parse_args()

    plan_path = args.plan if os.path.isabs(args.plan) else os.path.join(ROOT, args.plan)

    pipe_path = args.pipe if os.path.isabs(args.pipe) else os.path.join(ROOT, args.pipe)
    schema_path = args.schema if os.path.isabs(args.schema) else os.path.join(ROOT, args.schema)

    for p in (pipe_path, schema_path, AXIOMS):
        if not os.path.exists(p):
            print("输入缺失: %s" % p, file=sys.stderr)
            return 2

    pipe, dup_p = load(pipe_path)
    schema, dup_s = load(schema_path)

    nodes = pipe["nodes"]
    by = {n["id"]: n for n in nodes}
    ids = set(by)
    order = [n["id"] for n in nodes]
    mand = set(pipe["mandatory_minimum"]["nodes"])
    owner = {k: v for k, v in pipe["criteria_owner"].items() if k != "note"}

    rows = []
    pred_ids = set()

    def rec(g, name, ok, detail=""):
        rows.append({"group": g, "name": name, "ok": bool(ok), "detail": detail})
        m = re.match(r"^([A-J])(\d+)\s", name)
        if m:
            pred_ids.add(m.group(1) + m.group(2))

    # ---------- A 结构 ----------
    heads = [i for i in order if not by[i].get("prev")]
    tails = [i for i in order if i not in {n.get("prev") for n in nodes}]
    rec("A", "A1 链首唯一", len(heads) == 1, "链首=%s" % heads)
    rec("A", "A2 链尾唯一", len(tails) == 1, "链尾=%s" % tails)

    cyc, seen = [], set()
    for start in order:
        path, cur = [], start
        while cur and cur not in path:
            path.append(cur)
            cur = by[cur].get("prev")
        if cur:
            cyc.append(path)
    rec("A", "A3 无环", not cyc, "环=%s" % (cyc[:2] if cyc else "无"))

    walk, cur = [], heads[0] if heads else None
    while cur:
        walk.append(cur)
        nxt = [i for i in order if by[i].get("prev") == cur]
        cur = nxt[0] if len(nxt) == 1 else None
    rec("A", "A4 链覆盖全部节点", set(walk) == ids and len(walk) == len(nodes),
        "遍历 %d / 节点 %d" % (len(walk), len(nodes)))

    segs = [by[i]["seg"] for i in walk] if walk else []
    rec("A", "A5 段号沿链单调不减", all(segs[k] <= segs[k + 1] for k in range(len(segs) - 1)),
        "序列=%s" % segs)

    seg_runs = []
    for s in segs:
        if not seg_runs or seg_runs[-1] != s:
            seg_runs.append(s)
    rec("A", "A6 段内连续（不被打断）", len(seg_runs) == len(set(seg_runs)),
        "段串=%s" % seg_runs)

    indeg = {i: 0 for i in order}
    for n in nodes:
        p = n.get("prev")
        if p in indeg:
            indeg[p] += 1
    fan = {k: v for k, v in indeg.items() if v > 1}
    rec("A", "A7 出度不超过 1（无分叉）", not fan, "分叉=%s" % (fan or "无"))

    # ---------- B 判据 ----------
    hard = {}
    for n in nodes:
        if n.get("gate_owner"):
            for g in n.get("criteria", []):
                hard.setdefault(g, []).append(n["id"])
    multi = {g: v for g, v in hard.items() if len(v) > 1}
    rec("B", "B1 判据硬拦唯一", not multi, "多挂=%s" % (multi or "无"))

    unreg = []
    for n in nodes:
        if not n.get("gate_owner"):
            continue
        for g in n.get("criteria", []):
            if g not in owner or n["id"] not in owner[g]:
                unreg.append("%s:%s" % (n["id"], g))
    rec("B", "B2 硬拦判据已登记", not unreg, "未登记=%s" % (unreg or "无"))

    back = []
    for g, ns in owner.items():
        for nid in ns:
            if nid not in by or g not in by[nid].get("criteria", []):
                back.append("%s->%s" % (g, nid))
    rec("B", "B3 登记表反向完备", not back, "悬挂=%s" % (back or "无"))

    empty = [n["id"] for n in nodes if n.get("gate_owner") and not n.get("criteria")]
    rec("B", "B4 硬拦节点判据非空", not empty, "空判据=%s" % (empty or "无"))

    # ---------- C 强制 ----------
    rec("C", "C1 强制集是节点子集", mand <= ids, "越界=%s" % sorted(mand - ids))
    rec("C", "C2 R1 R2 R3 在强制集内", {"R1", "R2", "R3"} <= mand, "差集=%s" % sorted({"R1", "R2", "R3"} - mand))
    naked = [i for i in mand if not by[i].get("criteria") and not by[i].get("does")]
    rec("C", "C3 强制节点有承接", not naked, "无判据无动作=%s" % (naked or "无"))

    # ---------- D 覆盖（充分性） ----------
    covered = set()
    for ns in REQUIREMENTS.values():
        covered |= set(ns)
    dangling = [r for r, ns in REQUIREMENTS.items() if not set(ns) <= ids]
    rec("D", "D1 每个要求都有节点承接", not dangling, "无承接=%s" % (dangling or "无"))
    rec("D", "D2 承接节点真实存在", not (covered - ids), "虚构=%s" % sorted(covered - ids))

    orphan = [i for i in ids if i not in covered and i not in PRODUCERS]
    rec("D", "D3 每个节点都有归属", not orphan, "既无要求也非产出=%s" % (orphan or "无"))

    deadreq = [r for r, ns in REQUIREMENTS.items() if not (set(ns) & ids)]
    rec("D", "D4 要求无空映射", not deadreq, "空=%s" % (deadreq or "无"))

    hollow = []
    for r, ns in REQUIREMENTS.items():
        for nid in ns:
            if nid in by:
                n = by[nid]
                if not n.get("gate_owner") and not n.get("does"):
                    hollow.append("%s->%s" % (r, nid))
    rec("D", "D5 承接体非空（不空挂）", not hollow, "空挂=%s" % (hollow or "无"))

    exclusive = {}
    for r, ns in REQUIREMENTS.items():
        hit = set(ns) & ids
        if len(hit) == 1:
            exclusive[hit.pop()] = r
    no_excl = [i for i in ids if i not in exclusive and i not in PRODUCERS
               and by[i].get("type") != "format"]
    rec("D", "D6 承接节点须有独占要求", not no_excl, "无独占=%s" % (no_excl or "无"))

    # ---------- E 单一源 ----------
    ref = schema.get("nodes_ref") or {}
    mref = schema.get("mandatory_ref") or {}
    has_inline = bool(schema.get("nodes"))

    def _norm(p):
        return (p or "").replace("\\", "/")

    rec("E", "E1 节点集不内嵌于事件模型", not has_inline,
        "journal-schema 仍内嵌 %d 个节点" % len(schema.get("nodes", [])))
    rec("E", "E2 nodes_ref 指向 pipeline",
        _norm(ref.get("source", "")).endswith("pipeline.json#nodes"),
        "source=%s" % ref.get("source"))
    rec("E", "E3 nodes_ref.count 与实际相符", ref.get("count") == len(nodes),
        "声明=%s 实际=%d" % (ref.get("count"), len(nodes)))
    rec("E", "E4 强制集引用一致", set(mref.get("members", [])) == mand,
        "journal=%s pipe=%s" % (sorted(mref.get("members", [])), sorted(mand)))

    # ---------- F 降级 ----------
    badrep = [n["id"] for n in nodes if n.get("replay_on_change") not in REPLAY]
    rec("F", "F1 replay 值域合法", not badrep, "非法=%s" % (badrep or "无"))

    noreceive = [n["id"] for n in nodes
                 if n.get("replay_on_change") == "replace" and not n.get("gate_owner")
                 and not n.get("does")]
    rec("F", "F2 replace 档有承接", not noreceive, "无承接=%s" % (noreceive or "无"))

    # ---------- G 段契约 ----------
    seg_members = {s: [i for i in walk if by[i]["seg"] == s] for s in ("seg1", "seg2", "seg3")}
    seg_tail = {s: m[-1] for s, m in seg_members.items() if m}

    contract_bad = []
    for s, nxt in (("seg1", "seg2"), ("seg2", "seg3")):
        cand = seg_members.get(nxt) or []
        head = cand[0] if cand else None
        if head is None:
            contract_bad.append("%s 无可达节点（链断裂，无法判定段首）" % nxt)
        elif by[head].get("prev") != seg_tail.get(s):
            contract_bad.append("%s 段首 %s 的 prev=%s，应为 %s"
                                % (nxt, head, by[head].get("prev"), seg_tail.get(s)))
    rec("G", "G1 段首接上段链尾", not contract_bad, "; ".join(contract_bad) or "无")

    open_tail = []
    for s in ("seg1", "seg2", "seg3"):
        tid = seg_tail.get(s)
        if tid is None:
            open_tail.append("%s 无可达节点，段尾未闭合" % s)
            continue
        n = by[tid]
        if n["type"] != "format" and not n.get("absorbs_format"):
            open_tail.append("%s 段尾 %s 类型=%s 未声明吸收格式" % (s, tid, n["type"]))
    rec("G", "G2 段尾格式闭合", not open_tail, "; ".join(open_tail) or "无")

    # ---------- H 类型 ----------
    badtype = [n["id"] for n in nodes if n.get("type") not in TYPES]
    rec("H", "H1 type 值域合法", not badtype, "非法=%s" % (badtype or "无"))

    lax_review = [n["id"] for n in nodes if n.get("type") == "review" and n["id"] not in mand]
    rec("H", "H2 review 必属强制", not lax_review, "非强制=%s" % (lax_review or "无"))

    # ---------- I 完备 ----------
    noprod = [n["id"] for n in nodes if not n.get("products")]
    rec("I", "I1 每节点有产物", not noprod, "缺=%s" % (noprod or "无"))
    nodoes = [n["id"] for n in nodes if not n.get("does")]
    rec("I", "I2 每节点有动作", not nodoes, "缺=%s" % (nodoes or "无"))

    # ---------- J 输入卫生 ----------
    rec("J", "J1 pipeline 无重复键", not dup_p, "重复=%s" % (sorted(set(dup_p)) or "无"))
    rec("J", "J2 journal-schema 无重复键", not dup_s, "重复=%s" % (sorted(set(dup_s)) or "无"))
    rec("J", "J3 节点 id 唯一", len(ids) == len(nodes), "节点 %d 唯一 id %d" % (len(nodes), len(ids)))

    # ---------- K 公理登记册 ----------
    ax, dup_ax = load(AXIOMS)
    axs = ax.get("axioms", [])
    ths = ax.get("theorems", [])
    ax_ids = [a["id"] for a in axs]
    th_ids = [t["id"] for t in ths]
    KINDS = set(ax.get("check_kinds", {}).keys())

    rec("K", "K1 axioms 无重复键", not dup_ax, "重复=%s" % (sorted(set(dup_ax)) or "无"))

    nums = sorted(int(i[1:]) for i in ax_ids if i.startswith("P") and i[1:].isdigit())
    rec("K", "K2 公理编号连续", nums == list(range(1, len(nums) + 1)),
        "编号=%s" % (nums[:3] + ["…"] + nums[-2:] if len(nums) > 5 else nums))

    bad_kind = [a["id"] for a in axs if a["check"]["kind"] not in KINDS]
    rec("K", "K3 检查类型合法", not bad_kind, "非法=%s" % (bad_kind or "无"))

    dangling_pred, dangling_gate = [], []
    for a in axs:
        k, r = a["check"]["kind"], a["check"]["ref"]
        if k == "struct":
            refs = r if isinstance(r, list) else [r]
            dangling_pred += ["%s->%s" % (a["id"], x) for x in refs if x not in pred_ids]
        elif k == "gate" and r:
            if not os.path.exists(os.path.join(ROOT, "tools", r)):
                dangling_gate.append("%s->%s" % (a["id"], r))
    rec("K", "K4 struct 引用真实谓词", not dangling_pred, "悬挂=%s" % (dangling_pred or "无"))
    rec("K", "K5 gate 引用真实检查器", not dangling_gate, "悬挂=%s" % (dangling_gate or "无"))

    no_src = [a["id"] for a in axs if not a.get("source")]
    rec("K", "K6 每条公理有来源", not no_src, "缺源=%s" % (no_src or "无"))

    referenced = set()
    for a in axs:
        if a["check"]["kind"] == "struct":
            r = a["check"]["ref"]
            referenced |= set(r if isinstance(r, list) else [r])
    svc = set(ax.get("service_only_predicates", {}).get("ids", []))
    unref = sorted(pred_ids - referenced - svc)
    rec("K", "K7 谓词反向完备（无孤立谓词）", not unref, "未被任何公理引用=%s" % (unref or "无"))

    bad_from = []
    for t in ths:
        bad_from += ["%s->%s" % (t["id"], f) for f in t.get("from", []) if f not in ax_ids]
    rec("K", "K8 定理引用真实公理", not bad_from, "悬挂=%s" % (bad_from or "无"))

    pool = set(ax_ids) | set(th_ids)
    bad_ret = [x["old"] for x in ax.get("retired", [])
               if not any(p in (x.get("new") or "") for p in pool)]
    rec("K", "K9 退役条目有去向", not bad_ret, "无去向=%s" % (bad_ret or "无"))

    declared_disc = set(ax.get("coverage_expectation", {}).get("discipline_ids", []))
    actual_disc = {a["id"] for a in axs if a["check"]["kind"] == "discipline"}
    rec("K", "K10 discipline 清单与实际一致", declared_disc == actual_disc,
        "声明-实际=%s 实际-声明=%s" % (sorted(declared_disc - actual_disc), sorted(actual_disc - declared_disc)))

    # ---------- L 总执行书自述一致 ----------
    if os.path.exists(plan_path):
        with open(plan_path, encoding="utf-8") as fh:
            txt = fh.read()
        m = re.search(r"<!--\s*verify:(.*?)-->", txt, re.S)
        claims = {}
        if m:
            for kv in m.group(1).split():
                if "=" in kv:
                    k, v = kv.strip().split("=", 1)
                    claims[k] = v
        actual = {
            "axioms": len(axs),
            "theorems": len(ths),
            "nodes": len(nodes),
            "predicates": len(pred_ids),
            "requirements": len(REQUIREMENTS),
        }
        rec("L", "L1 执行书自述块存在且可解析", bool(claims), "claims=%s" % (claims or "无"))
        for k, v in sorted(actual.items()):
            rec("L", "L2 %s 与实算一致" % k,
                claims.get(k) == str(v), "文档=%s 实算=%s" % (claims.get(k), v))
    else:
        rec("L", "L1 总执行书存在", False, "未找到 %s" % plan_path)

    # ---------- 汇总 ----------
    fails = [r for r in rows if not r["ok"]]
    width = max(len(r["name"]) for r in rows)
    for r in rows:
        flag = "PASS" if r["ok"] else "FAIL"
        print("[%s] %-*s  %s" % (r["group"], width, r["name"], flag) +
              ("" if r["ok"] else "  -> " + r["detail"]))

    checkable = sum(1 for a in axs if a["check"]["kind"] in ("struct", "gate", "audit"))
    rate = (100.0 * checkable / len(axs)) if axs else 0.0
    print("\n公理：%d 条，定理 %d 条；可机检/人检 %d 条（%.0f%%），纯纪律 %d 条"
          % (len(axs), len(ths), checkable, rate, len(axs) - checkable))
    print("汇总：%d 项，通过 %d，失败 %d" % (len(rows), len(rows) - len(fails), len(fails)))

    out = {
        "pipeline": os.path.relpath(pipe_path, ROOT).replace("\\", "/"),
        "nodes": len(nodes),
        "requirements": len(REQUIREMENTS),
        "producers": len(PRODUCERS),
        "axioms": len(axs),
        "theorems": len(ths),
        "checkable_axioms": checkable,
        "discipline_axioms": len(axs) - checkable,
        "total": len(rows),
        "passed": len(rows) - len(fails),
        "failed": len(fails),
        "results": rows,
    }
    if args.json:
        dst = args.json if os.path.isabs(args.json) else os.path.join(ROOT, args.json)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
            fh.write("\n")

    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())

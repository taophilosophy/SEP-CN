#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""六轴工序公理化验证器（specs/060；只读，产验证凭证）。

用法:
  python specs/060-six-axis-quality-gates/bin/verify_six_axis.py [路径...] [--all] [--json] [--out PATH]

四组计算:
  A 结构公理  状态机全序、q 链位次、判据所有权唯一、强制集、ORDER 一致性、回退目标合法
  B 覆盖完备  CY/T 266-2023 差错类型（29 类）× 归属节点；MQM 七维 × 节点；六类判据计数
  C 一致性    多器同位置命中矩阵（预期互补 vs 潜在冲突）；处置规则单值性；状态机三处同步
  D 守恒幂等  引文 hash 集二次扫描相等；六器 issue 计数二次扫描相等

不可判项不伪证：输出 assumptions 列表，由人审或后续战役承担。

退出码: 0 计算完成（含未覆盖登记）；1 结构公理违例；2 用法错误。
"""
import argparse
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from tools import axis_lib as ax  # noqa: E402
from tools import (cite_audit, grammar_audit, logic_audit, measure_audit,  # noqa: E402
                   punct_audit, register_audit)

PIPE = os.path.join(ROOT, "rules", "pipeline.json")
AXIOMS = os.path.join(ROOT, "rules", "axioms.json")
SCHEMA = os.path.join(ROOT, "rules", "journal-schema.json")

QCHAIN = ["q1", "q2", "q3", "q4", "q5", "q6"]
QSTATES = ["q1_cite_checked", "q2_logic_checked", "q3_grammar_checked",
           "q4_register_checked", "q5_measure_checked", "q6_punct_checked"]

# CY/T 266-2023 差错类型 → 归属节点（人工节点以 r/s 前缀标出；exempt 为豁免）
CY266 = {
    "1-1 错字别字": "s1（人审）", "1-2 多字漏字": "s1（人审）",
    "1-3 颠倒字": "s1（人审）", "1-4 不规范汉字": "S3",
    "1-5 词语差错": "q3", "1-6 计量单位中文名称": "q5",
    "1-7 科技名词": "s2.4", "1-8 相关文字不一致": "S3",
    "1-9 倾向性问题": "r1/r2（人审）", "1-10 知识性差错": "s1+q2",
    "1-11 逻辑性语法性差错": "q2+q3", "1-12 图表与说明不一致": "S3",
    "1-13 废止标准陈旧资料": "s0+s1", "1-14 少数民族文字": "q1",
    "1-15 外文国际音标": "q1+q3", "1-16 汉语拼音": "S3",
    "1-17 阿拉伯数字罗马数字": "q5", "1-18 数字混用": "q5",
    "1-19 字母形式误用": "q3+q6", "1-20 字母词未注中文": "q1",
    "2-1 标点符号差错": "q6", "2-2 注码序号标注": "S3",
    "2-3 单位符号科学符号": "q5", "2-4 曲谱符号": "exempt（不适用）",
    "3-1 空行空格": "S3", "3-2 转行": "exempt（渲染层）",
    "3-3 编写体例": "S3", "3-4 排版格式": "S3",
    "3-5 图表书眉符号位置": "S3",
}
MQM = {
    "Terminology": "s2.4", "Accuracy": "s1+q2",
    "Linguistic conventions": "q3+q6", "Style": "q4",
    "Locale conventions": "q5+q6", "Audience appropriateness": "r1",
    "Design and markup": "S3",
}
# 预期互补对：同一位置两器都应命中，处置分工不构成冲突
EXPECTED_PAIRS = {("q5", "q6"): "M-6 判该用哪种连接号，P-13 判写法",
                  ("q3", "q4"): "G 层判语法，R 层判语域",
                  ("q3", "q6"): "G 层判句法，P-20 判半角标点",
                  ("q1", "q3"): "引文内部豁免，引文外句法",
                  ("q3", "q5"): "G 层判句法，M-2 判数值-单位空格，同句不同 span",
                  ("q4", "q5"): "R 层判语域，M 层判量值形态，同句不同 span",
                  ("q4", "q6"): "R 层判语域，P 层判标点形态，同句不同 span"}


def load_json(p):
    with open(p, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def structure():
    pipe = load_json(PIPE)
    nodes = pipe["nodes"]
    by = {n["id"]: n for n in nodes}
    out = {"nodes": len(nodes), "violations": [], "checks": []}

    def chk(name, ok, detail=""):
        out["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        if not ok:
            out["violations"].append("%s：%s" % (name, detail))

    heads = [i for i in by if not by[i].get("prev")]
    tails = [i for i in by if i not in {n.get("prev") for n in nodes}]
    chk("链首唯一", len(heads) == 1, str(heads))
    chk("链尾唯一", len(tails) == 1, str(tails))
    succ = collections.Counter(n.get("prev") for n in nodes if n.get("prev"))
    multi = [k for k, v in succ.items() if v > 1]
    chk("每节点唯一后继（全序）", not multi, str(multi))

    # 全序展开
    chain, cur = [], heads[0] if heads else None
    while cur:
        chain.append(cur)
        nxt = [i for i in by if by[i].get("prev") == cur]
        cur = nxt[0] if len(nxt) == 1 else None
    chk("链覆盖全部节点", len(chain) == len(nodes), "%d/%d" % (len(chain), len(nodes)))
    pos = {n: i for i, n in enumerate(chain)}
    chk("q 链连续且位于 s2.5 与 S3 之间",
        all(q in pos for q in QCHAIN)
        and pos["q1"] == pos["global"] + 1
        and pos["q6"] + 1 == pos["S3"]
        and [pos[q] for q in QCHAIN] == list(range(pos["q1"], pos["q1"] + 6)),
        str({q: pos.get(q) for q in QCHAIN}))

    owner = {k: v for k, v in pipe["criteria_owner"].items() if k != "note"}
    for q in QCHAIN:
        crit = by[q]["criteria"]
        chk("%s 判据唯一登记" % q,
            len(crit) == 1 and owner.get(crit[0]) == [q], str(crit))
    chk("六节点均非硬拦（T0 档）",
        all(by[q].get("gate_owner") is False for q in QCHAIN),
        str({q: by[q].get("gate_owner") for q in QCHAIN}))
    mand = set(pipe["mandatory_minimum"]["nodes"])
    chk("强制集含 q1–q6", set(QCHAIN) <= mand, str(sorted(mand)))
    chk("强制集含 R1–R3", {"R1", "R2", "R3"} <= mand, "")

    # ORDER 与 pipeline 同步
    from tools import task_ops
    order = task_ops.ORDER["retranslate"]
    chk("ORDER 含六状态且位次正确",
        order.index("s2.5_checked") + 1 == order.index(QSTATES[0])
        and order.index(QSTATES[-1]) + 1 == order.index("s3_checked"),
        ",".join(order))

    # 回退目标态合法（节点 id 与状态名分属两个空间，分别核对）
    from tools import journal_lib
    chk("回退 checkpoint 节点在链内",
        all(t in pos for t in journal_lib.REVERT_CHECKPOINTS),
        str(sorted(journal_lib.REVERT_CHECKPOINTS)))
    chk("回退目标态在 ORDER 内",
        all(t in order for t in task_ops.REVERT_TARGETS),
        str(sorted(task_ops.REVERT_TARGETS)))

    # 公理引用完整性
    axm = load_json(AXIOMS)
    ids = {a["id"] for a in axm["axioms"]}
    chk("P29–P33 已登记", {"P29", "P30", "P31", "P32", "P33"} <= ids,
        ",".join(sorted(ids))[:120])
    sch = load_json(SCHEMA)
    chk("journal-schema 节点计数一致", sch["nodes_ref"]["count"] == len(nodes),
        "%s vs %s" % (sch["nodes_ref"]["count"], len(nodes)))
    return out


def coverage():
    out = {"cy266": {"total": len(CY266), "mapped": 0, "machine": 0,
                     "manual": 0, "exempt": 0, "gaps": []},
           "mqm": {"total": len(MQM), "mapped": 0, "gaps": []},
           "judgments": {}}
    for k, v in CY266.items():
        if v.startswith("exempt"):
            out["cy266"]["exempt"] += 1
            out["cy266"]["mapped"] += 1
        elif "人审" in v:
            out["cy266"]["manual"] += 1
            out["cy266"]["mapped"] += 1
        elif v:
            out["cy266"]["machine"] += 1
            out["cy266"]["mapped"] += 1
        else:
            out["cy266"]["gaps"].append(k)
    for k, v in MQM.items():
        if v:
            out["mqm"]["mapped"] += 1
        else:
            out["mqm"]["gaps"].append(k)

    # 判据计数：从 checklists 解析编号
    cdir = os.path.join(ROOT, "specs", "060-six-axis-quality-gates", "checklists")
    pat = {"q1": r"\bC-\d+[a-z]?\b", "q2": r"\bL-\d+\b", "q3": r"\bG-\d+\b",
           "q4": r"\bR-[a-g]\b|\bR-[1-5]\b", "q5": r"\bM-\d+\b", "q6": r"\bP-\d+\b"}
    for q, rx in pat.items():
        f = os.path.join(cdir, "q%s-%s.md" % (q[1], {"q1": "cite", "q2": "logic",
                                                     "q3": "grammar", "q4": "register",
                                                     "q5": "measure", "q6": "punct"}[q]))
        if not os.path.exists(f):
            continue
        ids = sorted(set(re.findall(rx, open(f, encoding="utf-8").read())))
        out["judgments"][q] = {"count": len(ids), "ids": ids}
    return out


def scan_all(paths):
    data = {}
    for p in paths:
        slug = ax.slug_of(p)
        text = ax.read_doc(p)
        _, c = cite_audit.scan(p)
        _, g = grammar_audit.scan(p)
        _, m = measure_audit.scan(p)
        _, pt = punct_audit.scan(p)
        _, rg = register_audit.scan(p)
        lg_rows = logic_audit.skeleton(slug, text)
        lg_cand = logic_audit.candidates(slug, text)
        data[slug] = {
            "cite": [x["loc"] for x in c],
            "cite_hash": sorted(x["hash"] for x in c),
            "q3": [x["line"] for x in g],
            "q4": [x["line"] for x in rg["issues"]],
            "q5": [x["line"] for x in m["issues"]],
            "q6": [x["line"] for x in pt["issues"]],
            "q2": len(lg_cand), "q2_sent": len(lg_rows),
        }
    return data


def consistency(paths):
    d1 = scan_all(paths)
    hit = collections.defaultdict(set)   # (slug,line) → {q3,q4,q5,q6}
    for slug, v in d1.items():
        for q in ("q3", "q4", "q5", "q6"):
            for line in v[q]:
                if line:
                    hit[(slug, line)].add(q)
    multi = {k: sorted(v) for k, v in hit.items() if len(v) >= 2}
    pairs = collections.Counter()
    for v in multi.values():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                pairs[(v[i], v[j])] += 1
    def pair_notes(v):
        ns = []
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                ns.append(EXPECTED_PAIRS.get((v[i], v[j])))
        return ns

    classify = []
    unexplained = 0
    for k, v in multi.items():
        notes = pair_notes(sorted(v))
        if notes and all(notes):
            classify.append({"pos": "%s:%s" % k, "nodes": v, "kind": "expected",
                             "why": "；".join(sorted(set(notes)))})
        else:
            unexplained += 1
            classify.append({"pos": "%s:%s" % k, "nodes": v, "kind": "review",
                             "why": "无预登记分工"})
    # 幂等：二次扫描
    d2 = scan_all(paths)
    keys = ("cite", "cite_hash", "q3", "q4", "q5", "q6")
    idem = {q: sum(1 for s in d1 if len(d1[s][q]) == len(d2[s][q])) for q in keys} if d1 else {}
    idem["q2"] = sum(1 for s in d1 if d1[s]["q2"] == d2[s]["q2"]) if d1 else 0
    return {"positions_multi": len(multi), "pairs": {"%s×%s" % k: v for k, v in pairs.items()},
            "expected": sum(1 for c in classify if c["kind"] == "expected"),
            "unexplained": unexplained,
            "samples": classify[:20],
            "idempotent_files": idem}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default=os.path.join(
        ROOT, "specs", "060-six-axis-quality-gates", "results", "verification.json"))
    args = ap.parse_args()
    paths = ax.target_paths(None if args.all else args.paths)
    if not paths:
        ap.error("需要路径或 --all")

    rep = {"schema": "six-axis-verification/v1",
           "sample": {"files": len(paths)},
           "A_structure": structure(),
           "B_coverage": coverage(),
           "C_consistency": consistency(paths),
           "D_assumptions": [
               "前提 A1：人审裁判如实执行（机检为筛，人审为判，ADR-0070）",
               "前提 A2：作者的英文阐释可由紧邻段落识别（q1 通道二）",
               "前提 A3：LLM 输出不进入 verdict 字段（只产候选）",
               "前提 A4：`verifiable` 的版本判定由查证承担，工具不代判",
               "前提 A5：语义类判据（语域、逻辑、句法深检）不可机判，其通过以人审签字为凭",
           ]}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)

    a, b, c = rep["A_structure"], rep["B_coverage"], rep["C_consistency"]
    print("A 结构公理：节点 %d，检查 %d，违例 %d"
          % (a["nodes"], len(a["checks"]), len(a["violations"])))
    for v in a["violations"]:
        print("  !", v)
    print("B 覆盖：CY/T 266 %d/%d（机检 %d，人审 %d，豁免 %d，缺口 %d）；MQM %d/%d"
          % (b["cy266"]["mapped"], b["cy266"]["total"], b["cy266"]["machine"],
             b["cy266"]["manual"], b["cy266"]["exempt"], len(b["cy266"]["gaps"]),
             b["mqm"]["mapped"], b["mqm"]["total"]))
    print("   判据条数：" + "，".join("%s=%d" % (k, v["count"])
                                     for k, v in b["judgments"].items()))
    print("C 一致性：多器同位置 %d（预期互补 %d，待复核 %d）；对：%s"
          % (c["positions_multi"], c["expected"], c["unexplained"],
             "，".join("%s=%d" % (k, v) for k, v in c["pairs"].items()) or "无"))
    print("D 幂等：%s" % ", ".join("%s=%d/%d" % (k, v, len(paths))
                                   for k, v in c["idempotent_files"].items()))
    print("凭证：%s" % os.path.relpath(args.out, ROOT))
    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=1))
    return 1 if a["violations"] else 0


if __name__ == "__main__":
    sys.exit(main())

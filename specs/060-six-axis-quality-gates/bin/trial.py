#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""试金石执行器（specs/060 T0 阶段；只生成清单与拦截报告，不代签 verdict）。

用法:
  python specs/060-six-axis-quality-gates/bin/trial.py <slug> [<slug>...] [--json]

动作:
  1. 对每件跑六器 scan，--init 等价的清单骨架写入 state/axis/；
  2. 跑各器 gate，收集拦截原因（预期：未裁定项被拦，证门禁有效）；
  3. 出工单: 清单条目数、gate 通过与否、拦截原因分布、人工裁定工作量估算。

纪律: 不写任何 verdict；不推进任务状态；agent 不代替人审（ADR-0070）。
退出码: 0 生成完成；2 用法错误。
"""
import collections
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from tools import axis_lib as ax  # noqa: E402
from tools import (cite_audit, grammar_audit, logic_audit, measure_audit,  # noqa: E402
                   punct_audit, register_audit)

STATE = os.path.join(ROOT, "state", "axis")


def ensure_state():
    os.makedirs(STATE, exist_ok=True)


def init_cite(slug, items):
    data, added = cite_audit.merge_manifest(slug, items)
    with open(os.path.join(STATE, slug + ".cite.json"), "w", encoding="utf-8",
              newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    return added


def init_logic(slug, rows):
    with open(os.path.join(STATE, slug + ".logic.jsonl"), "w", encoding="utf-8",
              newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def init_grammar(slug, issues):
    grammar_audit.save(slug, issues)


def init_register(slug, data):
    data = register_audit.merge(slug, data)
    with open(os.path.join(STATE, slug + ".register.json"), "w", encoding="utf-8",
              newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


def init_measure(slug, data):
    data = measure_audit.merge(slug, data)
    with open(os.path.join(STATE, slug + ".measure.json"), "w", encoding="utf-8",
              newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


def init_punct(slug, data):
    data = punct_audit.merge(slug, data)
    with open(os.path.join(STATE, slug + ".punct.json"), "w", encoding="utf-8",
              newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


def find(slug):
    p = os.path.join(ROOT, slug[0], slug + ".md")
    return p if os.path.exists(p) else None


def run_one(slug):
    p = find(slug)
    if not p:
        return {"slug": slug, "error": "文档不存在"}
    text = ax.read_doc(p)
    ensure_state()
    out = {"slug": slug, "path": os.path.relpath(p, ROOT).replace("\\", "/"),
           "inventory": {}, "gate": {}}

    _, citems = cite_audit.scan(p)
    out["inventory"]["q1"] = len(citems)
    if citems:
        data, _ = cite_audit.merge_manifest(slug, citems)
        with open(os.path.join(STATE, slug + ".cite.json"), "w", encoding="utf-8",
                  newline="\n") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
    out["gate"]["q1"] = cite_audit.gate(slug, citems, None) if citems else []

    rows = logic_audit.skeleton(slug, text)
    bearing = sum(1 for r in rows if r.get("logic_bearing"))
    out["inventory"]["q2"] = len(rows)
    out["inventory"]["q2_bearing"] = bearing
    init_logic(slug, rows)
    out["gate"]["q2"] = logic_audit.gate(slug, rows)

    _, gissues = grammar_audit.scan(p)
    out["inventory"]["q3"] = len(gissues)
    init_grammar(slug, gissues)
    out["gate"]["q3"] = grammar_audit.gate(slug, gissues)

    _, rdata = register_audit.scan(p)
    out["inventory"]["q4"] = len(rdata["issues"])
    init_register(slug, rdata)
    out["gate"]["q4"] = register_audit.gate(slug, rdata)

    _, mdata = measure_audit.scan(p)
    out["inventory"]["q5"] = len(mdata["items"])
    init_measure(slug, mdata)
    out["gate"]["q5"] = measure_audit.gate(slug)

    _, pdata = punct_audit.scan(p)
    out["inventory"]["q6"] = len(pdata["issues"])
    init_punct(slug, pdata)
    out["gate"]["q6"] = punct_audit.gate(slug)

    out["gate_summary"] = {k: ("pass" if not v else "blocked:%d" % len(v))
                           for k, v in out["gate"].items()}
    reasons = collections.Counter()
    for v in out["gate"].values():
        for msg in v:
            reasons[msg.split(" ")[0]] += 1
    out["block_reasons"] = dict(reasons)
    # q2 待裁定实数（gate 输出截断到 80，估算不用截断值）
    lpath = os.path.join(STATE, slug + ".logic.jsonl")
    pending = 0
    if os.path.exists(lpath):
        with open(lpath, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                r = json.loads(line)
                if r.get("logic_bearing") and r.get("verdict") in (None, "", "pending"):
                    pending += 1
    out["inventory"]["q2_pending"] = pending

    # 人工裁定工作量：英文直引 10 分钟（抽查锚点），非英文直引 40 分钟（查证原文），
    # 逻辑非平凡句 5 分钟，语法/标点 10 分钟，语域/计量 15 分钟；给出上下限
    cpath = os.path.join(STATE, slug + ".cite.json")
    en_q = other_q = 0
    if os.path.exists(cpath):
        with open(cpath, "rb") as f:
            for it in json.loads(f.read().decode("utf-8")).get("items", []):
                if it.get("quote_lang") == "en":
                    en_q += 1
                else:
                    other_q += 1
    fixed = (pending * 5 + out["inventory"]["q3"] * 10 + out["inventory"]["q4"] * 15
             + out["inventory"]["q5"] * 15 + out["inventory"]["q6"] * 10)
    out["estimated_minutes_low"] = en_q * 10 + other_q * 40 + fixed
    out["estimated_minutes_high"] = en_q * 20 + other_q * 60 + fixed * 2
    out["estimated_minutes"] = out["estimated_minutes_low"]
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    slugs = [a for a in sys.argv[1:] if not a.startswith("--")]
    rep = {"schema": "six-axis-trial/v1", "items": [run_one(s) for s in slugs]}
    out = os.path.join(ROOT, "specs", "060-six-axis-quality-gates", "results",
                       "trial-report.json")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)
    print("%-24s %-42s %s" % ("slug", "清单 q1/q2/q3/q4/q5/q6", "gate"))
    for it in rep["items"]:
        if it.get("error"):
            print("%-24s %s" % (it["slug"], it["error"]))
            continue
        inv = it["inventory"]
        print("%-24s %-42s %s" % (
            it["slug"],
            "/".join(str(inv.get(k, 0)) for k in ("q1", "q2", "q3", "q4", "q5", "q6")),
            " ".join("%s=%s" % (k, v) for k, v in it["gate_summary"].items())))
        print("   人工裁定估算 %d–%d 分钟（下限–上限）；q2 待裁定 %d/%d；拦截 %d 条"
              % (it["estimated_minutes_low"], it["estimated_minutes_high"],
                 it["inventory"].get("q2_pending", 0), inv.get("q2", 0),
                 sum(len(v) for v in it["gate"].values())))
    print("工单：%s" % os.path.relpath(out, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())

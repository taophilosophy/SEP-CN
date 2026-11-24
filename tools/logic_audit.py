# -*- coding: utf-8 -*-
"""q2 逻辑一致性扫描器（ADR-0079；机检为筛，人审为判）。

用法:
  python tools/logic_audit.py [路径...] [--all] [--init] [--gate] [--json] [--out PATH]

行为:
  默认    抽正文散句，生成骨架候选并做算子配对初筛；退出码 0。
  --init  写 state/axis/<slug>.logic.jsonl（每句一条骨架，人工补 props/verdict）。
  --gate  门禁最小档：骨架覆盖率 ≥0.9、每条有 verdict 且非空、无法形式化者标
          unformalized。未达标退出码 1。

算子配对（初筛，不作裁判）: all/every/some/no/none/not/if/unless/must/should/may
与中文对应词逐一配对；英文侧计数显著高于中文侧即出候选（漏译或弱化）。
段配对按正文行号一一对应（结构对齐前提），错位产生噪声，只作候选。

依据: specs/060-six-axis-quality-gates/checklists/q2-logic.md（L-1…L-12）；
      ISO 24617-8 DR-core、ISO 24617-12 QuantML；CY/T 266-2023 表 1 第 1-11 类。
退出码: 0 通过/仅报告；1 --gate 未通过；2 用法错误。
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import axis_lib as ax  # noqa: E402

STATE_DIR = os.path.join(ax.ROOT, "state", "axis")

OPERATORS = {
    "all": r"\b(all|every|each)\b",
    "some": r"\b(some|several|a few)\b",
    "no": r"\b(no|none|nobody|nothing)\b",
    "not": r"\b(not|never)\b",
    "if": r"\b(if|provided that|in case)\b",
    "unless": r"\b(unless)\b",
    "must": r"\b(must|has to|have to)\b",
    "should": r"\b(should|ought)\b",
    "may": r"\b(may|might|can)\b",
}
ZH = {
    "all": [r"所有", r"每个", r"每一", r"一切", r"都", r"全部", r"凡", r"均", r"皆"],
    "some": [r"有些", r"某些", r"有的", r"一些", r"部分", r"某个", r"某种",
             r"若干", r"一部分"],
    "no": [r"没有", r"无", r"都不", r"没有任何", r"没有一个", r"并不", r"毫无"],
    "not": [r"不", r"没", r"非", r"未", r"别", r"无"],
    "if": [r"如果", r"若", r"假如", r"倘若", r"要是", r"一旦"],
    "unless": [r"除非"],
    "must": [r"必须", r"务必", r"一定要", r"不得不", r"只能"],
    "should": [r"应当", r"应该", r"理应", r"应"],
    "may": [r"可以", r"可能", r"也许", r"或许", r"能够", r"能", r"可"],
}


# 强逻辑算子（含量词、条件、模态、否定辖域、并列对比）；弱否定“不”不计，
# 以免把绝大多数单命题句拖进人审。命中其一即入骨架待裁定，否则标 trivial。
STRONG_OPS = [
    "所有", "每个", "每一", "任何", "有些", "某些", "有的", "没有", "并非",
    "除非", "只有", "必须", "应当", "应该", "必然", "必定", "可能", "如果",
    "若", "假如", "一旦", "无论", "不管", "不仅", "而是", "或者", "要么",
    "全部", "无一", "至少", "至多", "至多", "充分", "必要", "当且仅当",
]


def is_logic_bearing(sent):
    """句子是否含需人审的逻辑算子；trivial 句不占人审预算（仍计入覆盖率）。"""
    if any(op in sent for op in STRONG_OPS):
        return True
    if sent.count("；") + sent.count("，") >= 4:
        return True
    return False


def zh_path(slug):
    """slug → 中文文档路径（<letter>/<slug>.md）。"""
    if not slug:
        return None
    p = os.path.join(ax.ROOT, slug[0], slug + ".md")
    return p if os.path.exists(p) else None


def en_path(slug):
    p = os.path.join(ax.ROOT, "yuanwen", slug[0], slug + ".md")
    return p if os.path.exists(p) else None


def en_sections(slug):
    p = en_path(slug)
    return ax.h2_sections(ax.read_doc(p)) if p else []


def candidates(slug, zh_text):
    """按节配对：节序一致、节内段落块数一致才做算子配对；否则记 skip。"""
    out = []
    es = en_sections(slug)
    zs = ax.h2_sections(zh_text)
    if not es or len(es) != len(zs):
        return [{"rule": "align", "detail": "节数不对齐（en %d / zh %d），跳过配对"
                 % (len(es), len(zs))}]
    skipped = 0
    for (eh, ebody), (zh, zbody) in zip(es, zs):
        eb = ax.prose_blocks(ebody)
        zb = ax.prose_blocks(zbody)
        if len(eb) != len(zb):
            skipped += 1
            continue
        for (eloc, e), (zloc, z) in zip(eb, zb):
            for op, ere in OPERATORS.items():
                ec = len(re.findall(ere, e, re.I))
                if not ec:
                    continue
                zc = sum(len(re.findall(pat, z)) for pat in ZH[op])
                if ec > zc:
                    out.append({"rule": "L-3/4/5/6", "op": op, "sec": eh,
                                "en_block": eloc, "zh_block": zloc,
                                "en_count": ec, "zh_count": zc,
                                "en": ax.snippet(e, 70), "zh": ax.snippet(z, 70)})
    if skipped:
        out.append({"rule": "align", "detail": "%d 节块数不一致，已跳过" % skipped})
    return out


def skeleton(slug, text):
    rows = []
    for i, (line_no, start, sent) in enumerate(ax.sentences(text), 1):
        bearing = is_logic_bearing(sent)
        rows.append({"id": "p-%s-%04d" % (slug, i), "loc": "L%d" % line_no,
                     "zh": sent, "props": [], "mapping": "1:1",
                     "logic_bearing": bearing,
                     "verdict": "pending" if bearing else "trivial",
                     "reviewer": ""})
    return rows


def load_jsonl(path):
    if not os.path.exists(path):
        return None
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def gate(slug, rows):
    p = os.path.join(STATE_DIR, slug + ".logic.jsonl")
    saved = load_jsonl(p)
    probs = []
    if saved is None:
        return ["骨架缺失：先跑 --init"]
    if len(saved) < 0.9 * len(rows):
        probs.append("覆盖率不足：骨架 %d / 散句 %d" % (len(saved), len(rows)))
    for r in saved:
        v = r.get("verdict")
        if v in (None, "", "pending"):
            if r.get("logic_bearing", True):
                probs.append("%s 未裁定" % r.get("id"))
            continue
        if v not in ("equivalent", "weakened", "strengthened", "drifted",
                     "unformalized", "trivial"):
            probs.append("%s verdict 取值非法：%r" % (r.get("id"), v))
    return probs[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--limit", type=int, default=30)
    args = ap.parse_args()
    if args.all:
        args.paths = ax.target_paths(None)
    if not args.paths:
        ap.error("需要路径或 --all")

    report = {"schema": "logic-audit/v1", "files": [], "problems": []}
    for p in ax.target_paths(args.paths):
        text = ax.read_doc(p)
        slug = ax.slug_of(p)
        rows = skeleton(slug, text)
        cand = candidates(slug, text)
        if args.init:
            os.makedirs(STATE_DIR, exist_ok=True)
            with open(os.path.join(STATE_DIR, slug + ".logic.jsonl"),
                      "w", encoding="utf-8", newline="\n") as f:
                for r in rows:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        probs = gate(slug, rows) if args.gate else []
        for x in probs:
            report["problems"].append("%s: %s" % (slug, x))
        report["files"].append({
            "path": os.path.relpath(p, ax.ROOT).replace("\\", "/"),
            "slug": slug, "sentences": len(rows), "candidates": len(cand),
            "samples": cand[:args.limit]})

    if args.out:
        ax.emit(report, args.out)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print("文件 %d；散句 %d；算子候选 %d；问题 %d"
              % (len(report["files"]),
                 sum(f["sentences"] for f in report["files"]),
                 sum(f["candidates"] for f in report["files"]),
                 len(report["problems"])))
        for f in report["files"][:5]:
            for s in f["samples"][:3]:
                print("  ~", f["slug"], s)
    return 1 if (args.gate and report["problems"]) else 0


if __name__ == "__main__":
    sys.exit(main())

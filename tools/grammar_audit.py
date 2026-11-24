# -*- coding: utf-8 -*-
"""q3 语法扫描器（ADR-0079；机检为筛，人审为判）。

用法:
  python tools/grammar_audit.py [路径...] [--all] [--init] [--gate] [--json] [--out PATH]

三层：
  第一层 句法合法性（启发式候选）: G-1 成分残缺、G-5 句式杂糅、G-7 关联词错配
  第二层 反欧化（复用 check_prose 十一条，映射 G-9…G-16）
  第三层 和制汉语（tools/data/ja-loanwords.json 三分类词表，G-17…G-19）

防误判白名单内置（分句主语隐现、羡余非赘余、标准工具书同类用法）。
--init 写 state/axis/<slug>.grammar.json，逐条 issue 留 verdict；
--gate 校验该文件存在、无 pending 项。

依据: specs/060-six-axis-quality-gates/checklists/q3-grammar.md；CY/T 266-2023 表 1 第 1-11 类。
退出码: 0 通过/仅报告；1 --gate 未通过；2 用法错误。
"""
import argparse
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import axis_lib as ax  # noqa: E402

STATE_DIR = os.path.join(ax.ROOT, "state", "axis")
TOOLS = os.path.join(ax.ROOT, "tools")
DATA = os.path.join(TOOLS, "data")

PROSE_MAP = {
    "long-sentence": "G-11", "passive-bei": "G-9", "weak-verb": "G-10",
    "de-chain": "G-11", "plural-men": "G-15", "as-one": "G-16",
    "exists-there": "G-12", "dang-shihou": "G-16", "tense-adverb": "G-13",
    "conj-he-verb": "G-14", "chenggong-de": "G-10",
}
MIXED = [
    ("G-5", r"原因是[^。]{0,40}(造成的|所致|引起的)"),
    ("G-5", r"本着[^。]{0,30}为原则"),
    ("G-5", r"对于[^。]{0,20}上(，|,)"),
    ("G-5", r"由于[^。]{0,30}(使得|导致)"),
    ("G-7", r"不但[^。]{0,30}反而"),
    ("G-7", r"只有[^。]{0,30}就(?!业)"),
    ("G-7", r"虽然[^。]{0,40}但是[^。]{0,20}但是"),
    ("G-7", r"无论[^。]{0,30}也"),
]
G1_RE = re.compile(r"^(由于|针对|对于|关于)[^。]{4,40}(，|,)\s*(导致|使|造成|致使)")
FALSE_POSITIVE = ("正如", "彻底根治", "亲眼目睹", "凯旋归来", "免费赠送",
                  "除夕之夜", "唯一一次", "所有这一切", "付之阙如")


def load_ja_lexicon():
    p = os.path.join(DATA, "ja-loanwords.json")
    if not os.path.exists(p):
        return {"undecided": [], "deprecated": []}
    with open(p, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def run_prose(path):
    r = subprocess.run([sys.executable, os.path.join(TOOLS, "check_prose.py"), path],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    try:
        data = json.loads(r.stdout)
    except Exception:
        return []
    return data.get("issues", [])


def scan(path):
    text = ax.read_doc(path)
    slug = ax.slug_of(path)
    issues = []
    for it in run_prose(path):
        issues.append({"rule": PROSE_MAP.get(it.get("rule"), "G-12"),
                       "layer": 2, "line": it.get("line"),
                       "detail": it.get("detail", "")[:160],
                       "verdict": "pending"})
    for line_no, base, sent in ax.sentences(text):
        if any(fp in sent for fp in FALSE_POSITIVE):
            continue
        for rule, pat in MIXED:
            if re.search(pat, sent):
                issues.append({"rule": rule, "layer": 1, "line": line_no,
                               "detail": ax.snippet(sent), "verdict": "pending"})
        if G1_RE.search(sent.strip()):
            issues.append({"rule": "G-1", "layer": 1, "line": line_no,
                           "detail": ax.snippet(sent), "verdict": "pending"})
    lex = load_ja_lexicon()
    for line_no, base, sent in ax.sentences(text):
        for w in lex.get("deprecated", []):
            if w and w in sent:
                issues.append({"rule": "G-18", "layer": 3, "line": line_no,
                               "detail": "未定形日源词：%s｜%s" % (w, ax.snippet(sent, 60)),
                               "verdict": "pending"})
        for w in lex.get("undecided", []):
            if w and w in sent:
                issues.append({"rule": "G-19", "layer": 3, "line": line_no,
                               "detail": "待定形日源词：%s" % w, "verdict": "pending"})
    return slug, issues


def report_path(slug):
    return os.path.join(STATE_DIR, slug + ".grammar.json")


def save(slug, issues):
    os.makedirs(STATE_DIR, exist_ok=True)
    with open(report_path(slug), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"schema": "grammar-report/v1", "slug": slug, "issues": issues},
                  f, ensure_ascii=False, indent=1)


def gate(slug, issues):
    p = report_path(slug)
    if not os.path.exists(p):
        return ["报告缺失：先跑 --init"]
    with open(p, "rb") as f:
        saved = json.loads(f.read().decode("utf-8"))
    probs = []
    for it in saved.get("issues", []):
        if it.get("verdict") in (None, "", "pending"):
            probs.append("%s@%s 未处置" % (it.get("rule"), it.get("line")))
    if len(issues) > len(saved.get("issues", [])):
        probs.append("报告过期：现存 issue %d > 报告 %d，重跑 --init 合并"
                     % (len(issues), len(saved.get("issues", []))))
    return probs[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.all:
        args.paths = ax.target_paths(None)
    if not args.paths:
        ap.error("需要路径或 --all")

    report = {"schema": "grammar-audit/v1", "files": [], "problems": []}
    for p in ax.target_paths(args.paths):
        slug, issues = scan(p)
        if args.init:
            old = {}
            if os.path.exists(report_path(slug)):
                with open(report_path(slug), "rb") as f:
                    for it in json.loads(f.read().decode("utf-8")).get("issues", []):
                        old[(it.get("rule"), it.get("line"), it.get("detail"))] = it
            for it in issues:
                k = (it["rule"], it["line"], it["detail"])
                if k in old and old[k].get("verdict") not in (None, "", "pending"):
                    it["verdict"] = old[k]["verdict"]
            save(slug, issues)
        probs = gate(slug, issues) if args.gate else []
        for x in probs:
            report["problems"].append("%s: %s" % (slug, x))
        by = {}
        for it in issues:
            by[it["rule"]] = by.get(it["rule"], 0) + 1
        report["files"].append({
            "path": os.path.relpath(p, ax.ROOT).replace("\\", "/"),
            "slug": slug, "issues": len(issues), "by_rule": by,
            "samples": issues[:8]})

    if args.out:
        ax.emit(report, args.out)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print("文件 %d；告警 %d；问题 %d"
              % (len(report["files"]),
                 sum(f["issues"] for f in report["files"]), len(report["problems"])))
        for x in report["problems"][:30]:
            print("  -", x)
    return 1 if (args.gate and report["problems"]) else 0


if __name__ == "__main__":
    sys.exit(main())

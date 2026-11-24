# -*- coding: utf-8 -*-
"""q4 语域扫描器（ADR-0079；语义判断归人审，机检只产候选）。

用法:
  python tools/register_audit.py [路径...] [--all] [--init] [--gate] [--json] [--out PATH]

判据（checklists/q4-register.md）:
  R-a 主体档位逐节判定（人审；--init 生成节骨架，默认 pending）
  R-b 档位漂移（机检候选：口语/网络词、文言词混入）
  R-d 文言残留候选（语义判定，不按字频定罪）
  R-e 口语与方言残留
  R-f 称谓（第二人称“您”）
  R-g 样章基准比对（人审，结论入 report）

--gate：每节 register 已填、issues 无 pending。
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

CLASSICAL = [
    (r"矣[。，；]?$", "句末“矣”"), (r"焉[。，；]?$", "句末“焉”"),
    (r"哉[。，；！？]?$", "句末“哉”"), (r"耳[。，；]?$", "句末“耳”"),
    (r"乎[。，；？]?$", "句末“乎”"), (r"耶[。，；？]?$", "句末“耶”"),
    (r"者[，,][^。]{2,20}也[。，；]?", "“……者，……也”"),
    (r"吾人", "文言代词“吾人”"), (r"厥", "文言代词“厥”"),
    (r"然则", "文言连词“然则”"), (r"是以", "文言连词“是以”"),
    (r"若夫", "文言连词“若夫”"), (r"至若", "文言连词“至若”"),
]
COLLOQUIAL = ["搞", "弄", "咋", "啥", "挺", "蛮", "贼", "忽悠", "点赞",
              "干货", "走心", "上头", "破防", "内卷", "躺平"]
ADDRESS = [("您", "第二人称敬称“您”（本库用“你”）")]
DATA = os.path.join(ax.ROOT, "tools", "data")


def _load_lexicon():
    p = os.path.join(DATA, "register-lexicon.json")
    if not os.path.exists(p):
        return
    with open(p, "rb") as f:
        d = json.loads(f.read().decode("utf-8"))
    CLASSICAL[:] = [(x.get("pattern", ""), x.get("label", ""))
                    for x in d.get("classical", [])] or CLASSICAL
    COLLOQUIAL[:] = d.get("colloquial", []) or COLLOQUIAL
    ADDRESS[:] = [tuple(x) for x in d.get("address", [])] or ADDRESS


_load_lexicon()


def scan(path):
    text = ax.read_doc(path)
    slug = ax.slug_of(path)
    issues, sections = [], []
    for head, body in ax.h2_sections(text):
        sections.append({"section": head, "register": "", "verdict": "pending"})
        for line_no, base, sent in ax.sentences(body):
            clean = sent
            for pat, label in CLASSICAL:
                if re.search(pat, clean):
                    issues.append({"rule": "R-d", "line": line_no, "label": label,
                                   "detail": ax.snippet(clean), "verdict": "pending"})
            for w in COLLOQUIAL:
                if w in clean:
                    issues.append({"rule": "R-e", "line": line_no, "label": "口语/网络词：%s" % w,
                                   "detail": ax.snippet(clean, 60), "verdict": "pending"})
            for w, label in ADDRESS:
                if w in clean:
                    issues.append({"rule": "R-f", "line": line_no, "label": label,
                                   "detail": ax.snippet(clean, 60), "verdict": "pending"})
    return slug, {"schema": "register-report/v1", "slug": slug,
                  "sections": sections, "issues": issues}


def report_path(slug):
    return os.path.join(STATE_DIR, slug + ".register.json")


def merge(slug, fresh):
    old = {}
    if os.path.exists(report_path(slug)):
        with open(report_path(slug), "rb") as f:
            data = json.loads(f.read().decode("utf-8"))
        old = {(x.get("section")): x for x in data.get("sections", [])}
        oldi = {(x.get("rule"), x.get("line"), x.get("label")): x
                for x in data.get("issues", [])}
    else:
        oldi = {}
    for s in fresh["sections"]:
        p = old.get(s["section"])
        if p and p.get("register"):
            s["register"] = p["register"]
            s["verdict"] = p.get("verdict", "pending")
            s["note"] = p.get("note", "")
    for it in fresh["issues"]:
        k = (it["rule"], it["line"], it["label"])
        if k in oldi and oldi[k].get("verdict") not in (None, "", "pending"):
            it["verdict"] = oldi[k]["verdict"]
    return fresh


def gate(slug, data):
    if not os.path.exists(report_path(slug)):
        return ["报告缺失：先跑 --init"]
    with open(report_path(slug), "rb") as f:
        saved = json.loads(f.read().decode("utf-8"))
    probs = []
    for s in saved.get("sections", []):
        if not s.get("register"):
            probs.append("R-a 节未定档位：%s" % s.get("section"))
    for it in saved.get("issues", []):
        if it.get("verdict") in (None, "", "pending"):
            probs.append("R-b/d/e/f %s@%s 未处置" % (it.get("rule"), it.get("line")))
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

    report = {"schema": "register-audit/v1", "files": [], "problems": []}
    for p in ax.target_paths(args.paths):
        slug, data = scan(p)
        if args.init:
            data = merge(slug, data)
            os.makedirs(STATE_DIR, exist_ok=True)
            with open(report_path(slug), "w", encoding="utf-8", newline="\n") as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
        probs = gate(slug, data) if args.gate else []
        for x in probs:
            report["problems"].append("%s: %s" % (slug, x))
        report["files"].append({
            "path": os.path.relpath(p, ax.ROOT).replace("\\", "/"),
            "slug": slug, "sections": len(data["sections"]),
            "issues": len(data["issues"]),
            "samples": data["issues"][:6]})

    if args.out:
        ax.emit(report, args.out)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print("文件 %d；节 %d；候选 %d；问题 %d"
              % (len(report["files"]),
                 sum(f["sections"] for f in report["files"]),
                 sum(f["issues"] for f in report["files"]), len(report["problems"])))
        for x in report["problems"][:30]:
            print("  -", x)
    return 1 if (args.gate and report["problems"]) else 0


if __name__ == "__main__":
    sys.exit(main())

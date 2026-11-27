# -*- coding: utf-8 -*-
"""q6 标点扫描器（ADR-0079；形态可机判，语义类只出告警）。

用法:
  python tools/punct_audit.py [路径...] [--all] [--init] [--gate] [--json] [--out PATH]

判据（checklists/q6-punct.md，GB/T 15834-2011 十七种标点）:
  P-5 顿号（概数不用顿号）        P-7 冒号（单句不套用）
  P-8 引号（弯引号、配对、方向）   P-9 括号（配对、方向、层级）
  P-11 省略号（六连点）           P-13 连接号（三形）
  P-14 间隔号（U+2027 禁）        P-15 书名号（套用）
  P-18 引号邻接空格               P-20 半角标点

豁免：代码块、行内代码、数学、URL、参考文献节（axis_lib.protect 已处理）。
--gate：P-8/P-9/P-11/P-13/P-15/P-18/P-20 命中未处置即失败。
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
HARD = {"P-8", "P-9", "P-11", "P-13", "P-15", "P-18", "P-20"}
DATA = os.path.join(ax.ROOT, "tools", "data")
CLAUSES = {}


def _load_rules():
    p = os.path.join(DATA, "punct-rules.json")
    if not os.path.exists(p):
        return
    with open(p, "rb") as f:
        d = json.loads(f.read().decode("utf-8"))
    CLAUSES.update(d.get("clauses", {}))
    HARD.update(d.get("hard", []))


_load_rules()
HAN = r"\u4e00-\u9fff"

PAIRS = [("（", "）", "P-9"), ("【", "】", "P-9"), ("《", "》", "P-15"),
         ("〈", "〉", "P-15"), ("〔", "〕", "P-9"), ("“", "”", "P-8"),
         ("‘", "’", "P-8")]
DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
RANGE_ASCII = re.compile(r"(?<![\w-])(\d+(?:[.,]\d+)?)-(\d+(?:[.,]\d+)?)(?![\w-])")
RANGE_ENDASH = re.compile(r"(?<![\w–])(\d+(?:[.,]\d+)?)–(\d+(?:[.,]\d+)?)")
RANGE_TILDE = re.compile(r"(?<![\w~])(\d+(?:[.,]\d+)?)~(\d+(?:[.,]\d+)?)")
ELLIPSIS = re.compile(r"(?<!\.)\.{3,}(?!\.)|。{3,}")
HALF = re.compile(r"[%s][,;:?!]" % HAN)
QUOTE_GAP = re.compile(r"[“”][ \t]+[%s]|[%s][ \t]+[“”]" % (HAN, HAN))
KANJI_GAI = re.compile(r"[一二三四五六七八九十]\s*、\s*[一二三四五六七八九十]")


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def scan_text(text, slug):
    masked = ax.protect(text)
    issues = []

    def add(rule, pos, detail):
        issues.append({"rule": rule, "clause": CLAUSES.get(rule, ""),
                       "line": line_of(text, pos),
                       "detail": detail, "verdict": "pending"})

    for i, ch in enumerate(masked):
        if ch in "\u300c\u300d\u300e\u300f":
            add("P-8", i, "直角引号 U+%04X" % ord(ch))
    for m in re.finditer(r'"', masked):
        add("P-8", m.start(), "英文直双引号（应弯引号）")
    for m in re.finditer(r"(?<![A-Za-z])'(?![A-Za-z])", masked):
        add("P-8", m.start(), "孤立的英文直单引号（应弯引号）")
    for m in re.finditer(r"\u2027", masked):
        add("P-14", m.start(), "间隔号误用 U+2027（应 U+00B7）")

    for left, right, rule in PAIRS:
        idx, stack = [], []
        for i, ch in enumerate(masked):
            if ch == left:
                stack.append(i)
            elif ch == right:
                # 拉丁词内撇号（d’appui）不是单引号对
                if ch == "’" and 0 < i < len(masked) - 1 \
                        and re.match(r"[A-Za-z]", masked[i - 1]) \
                        and re.match(r"[A-Za-z]", masked[i + 1]):
                    continue
                if stack:
                    stack.pop()
                else:
                    idx.append((i, "右先于左"))
        for i, why in idx:
            add(rule, i, "%s%s %s" % (left, right, why))
        if stack:
            add(rule, stack[0], "%s%s 未闭合 %d 处" % (left, right, len(stack)))

    for m in ELLIPSIS.finditer(masked):
        add("P-11", m.start(), "省略号应为六连点“……”：%s" % m.group(0))
    for m in RANGE_ASCII.finditer(masked):
        if not DATE.match(m.group(0)):
            add("P-13", m.start(), "数值范围用一字线“—”或浪纹线“～”：%s" % m.group(0))
    for m in RANGE_ENDASH.finditer(masked):
        add("P-13", m.start(), "数值范围（en dash）应改一字线或浪纹线：%s" % m.group(0))
    for m in RANGE_TILDE.finditer(masked):
        add("P-13", m.start(), "数值范围“~”应改浪纹线“～”：%s" % m.group(0))
    for m in QUOTE_GAP.finditer(masked):
        add("P-18", m.start(), "引号与汉字之间不应有空格：%r" % m.group(0))
    for m in HALF.finditer(masked):
        add("P-20", m.start(), "正文中文旁半角标点：%s" % m.group(0))
    for m in KANJI_GAI.finditer(masked):
        add("P-5", m.start(), "概数不用顿号：%s" % m.group(0))

    # 冒号套用（按句）
    for line_no, base, sent in ax.sentences(text):
        if sent.count("：") >= 2:
            issues.append({"rule": "P-7", "line": line_no,
                           "detail": "单句冒号套用 %d 处：%s" % (sent.count("："),
                                                        ax.snippet(sent, 60)),
                           "verdict": "pending"})
    # 书名号套用
    for m in re.finditer(r"《[^》]{0,80}《", masked):
        add("P-15", m.start(), "书名号套用内层应改用单书名号〈〉")

    return {"schema": "punct-report/v1", "slug": slug, "issues": issues}


def scan(path):
    text = ax.read_doc(path)
    slug = ax.slug_of(path)
    return slug, scan_text(text, slug)


def report_path(slug):
    return os.path.join(STATE_DIR, slug + ".punct.json")


def merge(slug, fresh):
    old = {}
    if os.path.exists(report_path(slug)):
        with open(report_path(slug), "rb") as f:
            data = json.loads(f.read().decode("utf-8"))
        old = {(x.get("rule"), x.get("line"), x.get("detail")): x
               for x in data.get("issues", [])}
    for it in fresh["issues"]:
        k = (it["rule"], it["line"], it["detail"])
        if k in old and old[k].get("verdict") not in (None, "", "pending"):
            it["verdict"] = old[k]["verdict"]
    return fresh


def gate(slug):
    p = report_path(slug)
    if not os.path.exists(p):
        return ["报告缺失：先跑 --init"]
    with open(p, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    probs = []
    for it in data.get("issues", []):
        if it.get("rule") in HARD and it.get("verdict") in (None, "", "pending"):
            probs.append("%s@%s 未处置：%s" % (it["rule"], it["line"],
                                              (it.get("detail") or "")[:60]))
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

    report = {"schema": "punct-audit/v1", "files": [], "problems": []}
    for p in ax.target_paths(args.paths):
        slug, data = scan(p)
        if args.init:
            data = merge(slug, data)
            os.makedirs(STATE_DIR, exist_ok=True)
            with open(report_path(slug), "w", encoding="utf-8", newline="\n") as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
        probs = gate(slug) if args.gate else []
        for x in probs:
            report["problems"].append("%s: %s" % (slug, x))
        by = {}
        for it in data["issues"]:
            by[it["rule"]] = by.get(it["rule"], 0) + 1
        report["files"].append({
            "path": os.path.relpath(p, ax.ROOT).replace("\\", "/"),
            "slug": slug, "issues": len(data["issues"]), "by_rule": by,
            "samples": data["issues"][:6]})

    if args.out:
        ax.emit(report, args.out)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print("文件 %d；问题 %d"
              % (len(report["files"]),
                 sum(f["issues"] for f in report["files"])))
        for x in report["problems"][:30]:
            print("  -", x)
    return 1 if (args.gate and report["problems"]) else 0


if __name__ == "__main__":
    sys.exit(main())

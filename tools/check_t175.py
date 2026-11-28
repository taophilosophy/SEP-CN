#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T175 清单校验：规则差异表、11 件 pilot 计划、G5 检查单、收口声明。

用法：python tools/check_t175.py [--dir specs/064-flow-spec-audit/results]
"""
import argparse
import json
import os
import sys

SOURCES = ("rules/04", "rules/05", "specs/060", "specs/061", "specs/063", "standards.json")
SLUGS = ("h/habermas", "l/logic-preference", "e/environmental-aesthetics",
         "i/imprecise-probabilities", "a/action", "a/axiom-choice",
         "n/newton-principia", "l/logic-dynamic", "j/japanese-aesthetics",
         "k/kokugaku-school", "d/digital-art")
G5_ITEMS = ("T170–T175", "11 件", "差异表")
CLOSURE_ITEMS = ("不执行翻译", "不改任务状态", "不新增 T 号", "不整体勾选")


def _rows(text):
    out = []
    for line in text.split("\n"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or set("".join(cells)) <= set("-: "):
            continue
        out.append(cells)
    return out


def validate_rule_sync(text):
    errors = []
    rows = _rows(text)
    for source in SOURCES:
        hit = [r for r in rows if r and r[0].startswith(source)]
        if not hit:
            errors.append("差异表缺源 %s" % source)
            continue
        for row in hit:
            if len(row) < 5:
                errors.append("%s 行字段不足（需差异／落点／优先级）" % source)
                continue
            landing, priority = row[3], row[4]
            if landing in ("", "—", "TBD", "待定"):
                errors.append("%s 有悬空落点" % source)
            if priority not in ("P1", "P2", "P3", "已同步"):
                errors.append("%s 优先级非法: %r" % (source, priority))
    return errors


def validate_pilot_plan(text):
    errors = []
    if not all("P%d" % i in text for i in range(7)):
        errors.append("pilot 计划缺 P0–P6 表头")
    rows = _rows(text)
    for slug in SLUGS:
        hit = [r for r in rows if r and r[0] == slug]
        if not hit:
            errors.append("pilot 计划缺件 %s" % slug)
        elif len(hit[0]) < 9:
            errors.append("%s 行缺证据清单" % slug)
    return errors


def validate_g5(text):
    errors = [("G5 缺项 %s" % item) for item in G5_ITEMS if item not in text]
    if "未通过" not in text:
        errors.append("G5 当前结论须为未通过")
    return errors


def validate_closure(text):
    return [("收口声明缺 %s" % item) for item in CLOSURE_ITEMS if item not in text]


def run(directory):
    def read(name):
        with open(os.path.join(directory, name), encoding="utf-8") as f:
            return f.read()
    checks = {
        "rule_sync": validate_rule_sync(read("t175-rule-sync.md")),
        "pilot_plan": validate_pilot_plan(read("t175-pilot-plan.md")),
        "g5": validate_g5(read("t175-g5-checklist.md")),
        "closure": validate_closure(read("t175-closure.md")),
    }
    return checks


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="specs/064-flow-spec-audit/results")
    args = ap.parse_args(argv)
    try:
        checks = run(args.dir)
    except OSError as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 2
    checks["ok"] = not any(checks.values())
    print(json.dumps(checks, ensure_ascii=False, indent=1))
    return 0 if checks["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

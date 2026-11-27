#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""术语概念层校验（ADR-0084 D5=B）：新登记术语必须同时有概念行。

口径：
  * 指称层 `zh/shu-yu-biao.md`（键｜原文｜译法｜首现｜依据｜裁定日期）——由 check_terms 管。
  * 概念层 `baseline/term-concepts.md`（键｜定义｜学科域｜概念关系｜依据｜裁定日期）——本工具管。
  * 仅检查裁定日期 ≥ --since（默认 2026-12-01）的指称行；存量随重译补齐，不追溯。

用法:
  python tools/check_term_concepts.py [--registry PATH] [--concepts PATH]
                                      [--since 2026-12-01] [--strict]
退出码: 0 完成（告警档）；1 --strict 且存在缺概念行；2 输入缺失。
"""
import argparse
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError, OSError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "zh", "shu-yu-biao.md")
CON = os.path.join(ROOT, "baseline", "term-concepts.md")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def rows(path):
    """读 md 表格：返回 [{列名: 值}]（跳过表头与分隔行）。"""
    out, header = [], None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if header is None:
                header = cells
                continue
            if set("".join(cells)) <= set("-: "):
                continue
            out.append(dict(zip(header, cells)))
    return out


def check(reg_rows, con_rows, since):
    con = {r.get("键", "").strip() for r in con_rows
           if str(r.get("定义", "")).strip() and str(r.get("学科域", "")).strip()}
    missing = []
    for r in reg_rows:
        key = str(r.get("键", "")).strip()
        date = str(r.get("裁定日期", "")).strip()
        if not key or not DATE.match(date) or date < since:
            continue
        if key not in con:
            missing.append((key, date))
    return missing


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", default=REG)
    ap.add_argument("--concepts", default=CON)
    ap.add_argument("--since", default="2026-12-01")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args(argv)
    for p in (args.registry, args.concepts):
        if not os.path.exists(p):
            print("输入缺失: %s" % p, file=sys.stderr)
            return 2
    missing = check(rows(args.registry), rows(args.concepts), args.since)
    print("术语概念层：%d 条新登记术语缺概念行（since %s）" % (len(missing), args.since))
    for key, date in missing[:20]:
        print("  %s（%s）" % (key, date))
    if missing:
        print("  处置：在 baseline/term-concepts.md 补 定义＋学科域（概念关系可留空），"
              "或在指称行说明为何不设概念（如纯专名）。")
    return 1 if (args.strict and missing) else 0


if __name__ == "__main__":
    sys.exit(main())

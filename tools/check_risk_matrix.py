#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""风险分级矩阵校验（T172／CP-S14-16；ADR-0094）。

规则：
  A 高：人工翻译为主，独立双语审校＋领域审校＋终审；
  B 中：LLM 初译＋full PE，独立审校；
  C 低／内部：LLM＋light PE，只内部，不得出版；
  出版件只允许 full PE，禁 raw／light PE，Critical＝0。
"""
import argparse
import json
import sys

REQUIRED = ("name", "criteria", "method", "review", "publication")
EXPECTED = {"A": "human-led", "B": "llm-pe-full", "C": "llm-light"}


def validate(data):
    errors = []
    levels = data.get("levels") or {}
    for key in ("A", "B", "C"):
        rec = levels.get(key)
        if not isinstance(rec, dict):
            errors.append("缺风险级 %s" % key)
            continue
        for field in REQUIRED:
            if field not in rec or rec.get(field) in ("", None, [], {}):
                errors.append("%s 缺 %s" % (key, field))
        if rec.get("method") != EXPECTED[key]:
            errors.append("%s 方法应为 %s，实际 %r" % (key, EXPECTED[key], rec.get("method")))
    if levels.get("C", {}).get("publication") is not False:
        errors.append("C 级不得出版")
    pub = data.get("publication") or {}
    if pub.get("pe_level") != "full":
        errors.append("出版件 pe_level 须为 full")
    forbid = pub.get("forbid") or []
    for item in ("raw", "light"):
        if item not in forbid:
            errors.append("出版禁项缺 %s" % item)
    if pub.get("critical") != 0:
        errors.append("Critical 须为 0")
    return errors


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default="rules/risk-matrix.json")
    args = ap.parse_args(argv)
    try:
        with open(args.path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 2
    errors = validate(data)
    print(json.dumps({"errors": errors, "ok": not errors}, ensure_ascii=False, indent=1))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

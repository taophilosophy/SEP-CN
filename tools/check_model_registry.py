#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""模型／提示登记校验（T172／CP-S14-17；ADR-0094）。

每条模型记录须有 provider、model、version、date、params、system_prompt、
terminology_version、data_terms；id 唯一；date 为 YYYY-MM-DD。
"""
import argparse
import json
import re
import sys

REQUIRED = ("id", "provider", "model", "version", "date", "params",
            "system_prompt", "terminology_version", "data_terms")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate(data):
    errors, seen = [], set()
    models = data.get("models") or []
    if not models:
        return ["models 为空"]
    for i, rec in enumerate(models):
        label = rec.get("id") or "#%d" % i
        for field in REQUIRED:
            value = rec.get(field)
            if value in ("", None, [], {}):
                errors.append("%s 缺 %s" % (label, field))
        ident = str(rec.get("id") or "")
        if ident in seen:
            errors.append("重复模型 id: %s" % ident)
        seen.add(ident)
        if not DATE_RE.match(str(rec.get("date") or "")):
            errors.append("%s date 非 YYYY-MM-DD" % label)
        if not isinstance(rec.get("params"), dict):
            errors.append("%s params 须为对象" % label)
    return errors


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default="baseline/model-registry.json")
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

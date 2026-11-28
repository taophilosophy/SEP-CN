#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""记录／归档／度量／AI 治理／发布后校验（T174／CP-S14-26–31；ADR-0096）。

默认校验：
  rules/archive-schema.json + results/t174-archive-template.json
  rules/retention.json
  rules/metrics-baseline.json
  rules/ai-governance.json
  rules/post-publication.json
用法：python tools/check_governance.py [--archive MANIFEST]
"""
import argparse
import hashlib
import json
import os
import re
import sys

TYPES = ("spec", "source", "tbx", "model", "review", "scorecard", "editing", "release")
METRICS = ("critical", "publication_error_rate", "major_minor_density", "rework_rate",
           "pe_hours", "reviewer_consistency", "post_publication_errata", "cycle_cost")
POST_ENTRIES = ("errata", "feedback", "upstream_update", "spot_audit", "version_record")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_archive(manifest, schema=None):
    errors = []
    schema = schema or _load("rules/archive-schema.json")
    required = schema.get("required_types") or list(TYPES)
    fields = schema.get("item_fields") or ["type", "path", "sha256", "date", "owner", "status"]
    status_values = schema.get("status_values") or ["present", "missing"]
    items = manifest.get("items") or []
    seen = set()
    for item in items:
        typ = item.get("type")
        seen.add(typ)
        for field in fields:
            if field not in item:
                errors.append("%s 缺字段 %s" % (typ or "<无 type>", field))
        if item.get("status") not in status_values:
            errors.append("%s status 非法: %r" % (typ, item.get("status")))
        if item.get("status") == "missing":
            errors.append("缺归档项 %s" % typ)
        if item.get("status") == "present":
            if not item.get("path"):
                errors.append("%s 缺 path" % typ)
            elif not os.path.exists(item["path"]):
                errors.append("%s path 不存在: %s" % (typ, item["path"]))
            elif not SHA_RE.match(str(item.get("sha256") or "")):
                errors.append("%s sha256 非 64 位十六进制" % typ)
            else:
                with open(item["path"], "rb") as f:
                    actual = hashlib.sha256(f.read()).hexdigest()
                if actual != item["sha256"]:
                    errors.append("%s sha256 与文件不符" % typ)
            if not DATE_RE.match(str(item.get("date") or "")):
                errors.append("%s date 非 YYYY-MM-DD" % typ)
            if not str(item.get("owner") or "").strip():
                errors.append("%s 缺 owner" % typ)
    for typ in required:
        if typ not in seen:
            errors.append("缺归档类型 %s" % typ)
    return errors


def validate_retention(data):
    errors = []
    items = data.get("items") or {}
    for typ in TYPES:
        rec = items.get(typ)
        if not isinstance(rec, dict):
            errors.append("留存缺 %s" % typ)
            continue
        for field in ("retention", "destruction", "access", "owner"):
            if not rec.get(field):
                errors.append("%s 缺 %s" % (typ, field))
    return errors


def validate_metrics(data):
    errors = []
    metrics = data.get("metrics") or {}
    for key in METRICS:
        rec = metrics.get(key)
        if not isinstance(rec, dict):
            errors.append("缺指标 %s" % key)
            continue
        if not rec.get("source"):
            errors.append("%s 缺 source" % key)
        baseline, threshold = rec.get("baseline"), rec.get("threshold")
        if data.get("status") == "pending_pilot" and (baseline is not None or threshold is not None):
            errors.append("%s pending_pilot 时 baseline／threshold 须为 null" % key)
        if threshold is not None and baseline is None:
            errors.append("%s 未测基线不得设阈值" % key)
    return errors


def validate_ai(data):
    errors = []
    risks = data.get("risk_register") or []
    if not risks:
        errors.append("risk_register 为空")
    for rec in risks:
        for field in ("id", "risk", "likelihood", "impact", "mitigation", "owner", "status"):
            if not rec.get(field):
                errors.append("%s 缺 %s" % (rec.get("id") or "<无 id>", field))
    for key in ("impact_assessment", "model_change_regression", "vendor_data_terms",
                "incident_handling"):
        if not data.get(key):
            errors.append("缺 %s" % key)
    if "disclosure" in data:
        errors.append("不设公开 AI 披露（T174 裁定）")
    if not (data.get("incident_handling") or {}).get("steps"):
        errors.append("incident_handling 缺 steps")
    return errors


def validate_postpub(data):
    errors = []
    entries = data.get("entries") or {}
    for key in POST_ENTRIES:
        rec = entries.get(key)
        if not isinstance(rec, dict):
            errors.append("缺发布后项 %s" % key)
            continue
        for field in ("owner", "trigger", "evidence"):
            if not rec.get(field):
                errors.append("%s 缺 %s" % (key, field))
    return errors


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", default="specs/064-flow-spec-audit/results/t174-archive-template.json")
    args = ap.parse_args(argv)
    checks = []
    try:
        schema = _load("rules/archive-schema.json")
        manifest = _load(args.archive)
        checks.append(("archive", validate_archive(manifest, schema)))
        checks.append(("retention", validate_retention(_load("rules/retention.json"))))
        checks.append(("metrics", validate_metrics(_load("rules/metrics-baseline.json"))))
        checks.append(("ai", validate_ai(_load("rules/ai-governance.json"))))
        checks.append(("postpub", validate_postpub(_load("rules/post-publication.json"))))
    except (OSError, ValueError) as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 2
    out = {name: errs for name, errs in checks}
    out["ok"] = not any(errs for _, errs in checks)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISO 5060 评分卡校验与计分（T173／CP-S14-19–22；ADR-0095）。

用法:
  python tools/check_qa_scorecard.py                 # 校验 rules/qa-scorecard.json
  python tools/check_qa_scorecard.py --score FILE    # 按 findings JSON 计分
findings JSON: {"words": 10000, "items": [{"category": "accuracy", "severity": "Critical", "count": 1}]}
"""
import argparse
import json
import sys

CATEGORIES = ("terminology", "accuracy", "linguistic", "style", "locale", "audience", "design")
SEVERITIES = ("Critical", "Major", "Minor")


def validate(data):
    errors = []
    cats = data.get("categories") or {}
    for key in CATEGORIES:
        rec = cats.get(key)
        if not isinstance(rec, dict):
            errors.append("缺类别 %s" % key)
            continue
        if not rec.get("process"):
            errors.append("%s 缺 process" % key)
        if rec.get("severity") not in SEVERITIES:
            errors.append("%s severity 非法" % key)
        if not isinstance(rec.get("weight"), int) or rec["weight"] <= 0:
            errors.append("%s weight 须为正整数" % key)
    sev = data.get("severity") or {}
    for key in SEVERITIES:
        if not isinstance(sev.get(key), int) or sev[key] <= 0:
            errors.append("severity.%s 须为正整数" % key)
    if not data.get("formula"):
        errors.append("缺 formula")
    metrics = data.get("metrics") or {}
    pub = metrics.get("publication") or {}
    svc = metrics.get("service") or {}
    if pub.get("limit") != "1/10000":
        errors.append("publication.limit 须为 1/10000")
    if svc.get("limit") != "1.5‰":
        errors.append("service.limit 须为 1.5‰")
    if pub.get("limit") == svc.get("limit"):
        errors.append("出版与服务口径不得混用")
    th = data.get("thresholds") or {}
    if (th.get("publication") or {}).get("critical") != 0:
        errors.append("publication.critical 须为 0")
    sampling = (data.get("sampling") or {}).get("manual") or {}
    if sampling.get("strata") != "H2":
        errors.append("sampling.manual.strata 须为 H2")
    if sampling.get("min_per_stratum", 0) < 1:
        errors.append("sampling.manual.min_per_stratum 须 >=1")
    if not (0 < sampling.get("min_ratio", 0) <= 1):
        errors.append("sampling.manual.min_ratio 须在 (0,1]")
    if sampling.get("min_segments", 0) < 1:
        errors.append("sampling.manual.min_segments 须 >=1")
    if "sha256" not in str(sampling.get("order") or ""):
        errors.append("sampling.manual.order 须含 sha256")
    if sampling.get("critical_escalation") != "full":
        errors.append("sampling.manual.critical_escalation 须为 full")
    return errors


def score(data, words, items):
    if words <= 0:
        raise ValueError("words 须为正数")
    cats = data["categories"]
    sev = data["severity"]
    penalty = 0
    critical = 0
    for item in items:
        cat = cats.get(item.get("category"))
        if not cat:
            raise ValueError("未知类别: %r" % item.get("category"))
        level = item.get("severity")
        if level not in sev:
            raise ValueError("未知严重度: %r" % level)
        count = int(item.get("count") or 0)
        if count < 0:
            raise ValueError("count 不得为负")
        penalty += cat["weight"] * sev[level] * count
        if level == "Critical":
            critical += count
    score_value = max(0.0, 100.0 - penalty / words * 1000.0)
    pub = data["thresholds"]["publication"]
    svc = data["thresholds"]["service"]
    return {
        "words": words,
        "penalty": penalty,
        "score": round(score_value, 2),
        "critical": critical,
        "pass_publication": critical <= pub["critical"] and score_value >= pub["min_score"],
        "pass_service": critical <= svc["critical"] and score_value >= svc["min_score"],
        "scorecard_version": data.get("version"),
    }


def validate_evaluator(data):
    """评估者资格与校准登记（T173／CP-S14-23）。"""
    errors = []
    roles = data.get("roles") or {}
    for key in ("evaluator", "arbiter"):
        rec = roles.get(key)
        if not isinstance(rec, dict):
            errors.append("缺角色 %s" % key)
            continue
        for field in ("required", "independence", "calibration"):
            if not rec.get(field):
                errors.append("%s 缺 %s" % (key, field))
    cal = data.get("calibration") or {}
    if cal.get("method") != "double":
        errors.append("calibration.method 须为 double")
    if not cal.get("agreement_metric"):
        errors.append("calibration.agreement_metric 缺失")
    threshold = cal.get("threshold")
    status = cal.get("threshold_status")
    if threshold is None and status != "pending_pilot":
        errors.append("阈值未测时 threshold_status 须为 pending_pilot")
    if threshold is not None and not isinstance(threshold, (int, float)):
        errors.append("threshold 须为数值或 null")
    if not cal.get("record_fields"):
        errors.append("calibration.record_fields 缺失")
    return errors


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--score", default="")
    ap.add_argument("--card", default="rules/qa-scorecard.json")
    ap.add_argument("--evaluator", default="rules/evaluator-registry.json")
    args = ap.parse_args(argv)
    try:
        with open(args.card, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 2
    errors = validate(data)
    try:
        with open(args.evaluator, encoding="utf-8") as f:
            ev_data = json.load(f)
        errors += validate_evaluator(ev_data)
    except (OSError, ValueError) as e:
        errors.append("evaluator registry: %s" % e)
    if args.score:
        try:
            with open(args.score, encoding="utf-8") as f:
                findings = json.load(f)
            result = score(data, int(findings["words"]), findings.get("items") or [])
        except (OSError, ValueError, KeyError) as e:
            print(json.dumps({"error": str(e)}, ensure_ascii=False))
            return 2
        result["errors"] = errors
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return 0 if not errors else 1
    print(json.dumps({"errors": errors, "ok": not errors}, ensure_ascii=False, indent=1))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

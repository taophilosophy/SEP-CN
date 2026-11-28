# -*- coding: utf-8 -*-
"""文档形态与规则作用域机检（ADR-0092；T167）。

用法: python tools/check_doc_shape.py [--root .]
检查:
  1. specs/<NNN>-*/ 形态：spec.md 必有；plan.md 与 tasks.md 任一存在即须两件齐
     （单页卡＝仅 spec.md；标准三件＝spec＋plan＋tasks）。
  2. rules/0X-*.md 头部不得手写 applies_to（作用域由 rules/pipeline.json 派生）。
  3. rules/pipeline.json：节点判据须有 criteria_owner；owner 须有承载体
     （tools/<name>.py 或 criteria_carrier 例外）；owner 不得为无节点引用的孤儿。
退出码: 0 通过；1 有 issue。
"""
import argparse
import json
import os
import re
import sys

SPEC_RE = re.compile(r"^\d{3}-")
HAND_SCOPE_RE = re.compile(r"(?mi)^\s*applies_to\s*:")


def check_specs(root):
    issues = []
    specs = os.path.join(root, "specs")
    if not os.path.isdir(specs):
        return issues
    for name in sorted(os.listdir(specs)):
        d = os.path.join(specs, name)
        if not (os.path.isdir(d) and SPEC_RE.match(name)):
            continue
        spec = os.path.isfile(os.path.join(d, "spec.md"))
        plan = os.path.isfile(os.path.join(d, "plan.md"))
        tasks = os.path.isfile(os.path.join(d, "tasks.md"))
        if not spec:
            issues.append({"path": d, "rule": "spec-missing",
                           "detail": "规格容器缺 spec.md"})
        if tasks and not plan:
            issues.append({"path": d, "rule": "triple-incomplete",
                           "detail": "有 tasks.md 则须有 plan.md（三件套）"})
    return issues


def check_rule_scope(root):
    issues = []
    rules = os.path.join(root, "rules")
    if not os.path.isdir(rules):
        return issues
    for name in sorted(os.listdir(rules)):
        if not re.match(r"^0\d-.*\.md$", name):
            continue
        p = os.path.join(rules, name)
        with open(p, encoding="utf-8") as f:
            head = "".join(f.readline() for _ in range(20))
        if HAND_SCOPE_RE.search(head):
            issues.append({"path": p, "rule": "hand-scope",
                           "detail": "规则头部手写 applies_to；作用域应由 pipeline.json 派生"})
    pj = os.path.join(rules, "pipeline.json")
    if not os.path.isfile(pj):
        return issues
    with open(pj, encoding="utf-8") as f:
        pipe = json.load(f)
    owner = pipe.get("criteria_owner", {})
    carrier = pipe.get("criteria_carrier", {})
    used = set()
    for node in pipe.get("nodes", []):
        for c in node.get("criteria", []):
            used.add(c)
            if c not in owner:
                issues.append({"path": pj, "rule": "owner-missing",
                               "detail": "节点 %s 判据 %s 无 criteria_owner" % (node.get("id"), c)})
    for c in owner:
        if c == "note":
            continue
        if c not in used:
            issues.append({"path": pj, "rule": "orphan-owner",
                           "detail": "criteria_owner 键 %s 无节点引用" % c})
        if c in carrier:
            continue
        if not os.path.isfile(os.path.join(root, "tools", c + ".py")):
            issues.append({"path": pj, "rule": "carrier-missing",
                           "detail": "判据 %s 无承载体 tools/%s.py 且不在 criteria_carrier" % (c, c)})
    return issues


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args(argv)
    issues = check_specs(args.root) + check_rule_scope(args.root)
    print(json.dumps({"root": args.root, "issues": issues}, ensure_ascii=False, indent=1))
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())

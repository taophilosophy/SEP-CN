# -*- coding: utf-8 -*-
"""T167：文档形态与规则作用域机检正反例（ADR-0092）。"""
import json
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_doc_shape as cds  # noqa: E402


def touch(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


class SpecShapeTest(unittest.TestCase):
    def test_spec_only_card_ok(self):
        with tempfile.TemporaryDirectory() as d:
            touch(os.path.join(d, "specs", "001-card", "spec.md"), "# 卡\n")
            self.assertEqual(cds.check_specs(d), [])

    def test_plan_only_ok(self):
        with tempfile.TemporaryDirectory() as d:
            touch(os.path.join(d, "specs", "002-plan", "spec.md"), "# 卡\n")
            touch(os.path.join(d, "specs", "002-plan", "plan.md"), "# 方案\n")
            self.assertEqual(cds.check_specs(d), [])

    def test_full_triple_ok(self):
        with tempfile.TemporaryDirectory() as d:
            for n in ("spec", "plan", "tasks"):
                touch(os.path.join(d, "specs", "003-full", n + ".md"), "# x\n")
            self.assertEqual(cds.check_specs(d), [])

    def test_tasks_without_plan_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            touch(os.path.join(d, "specs", "004-bad", "spec.md"), "# 卡\n")
            touch(os.path.join(d, "specs", "004-bad", "tasks.md"), "# 任务\n")
            rules = {i["rule"] for i in cds.check_specs(d)}
            self.assertIn("triple-incomplete", rules)

    def test_missing_spec_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            touch(os.path.join(d, "specs", "005-bad", "plan.md"), "# 方案\n")
            rules = {i["rule"] for i in cds.check_specs(d)}
            self.assertIn("spec-missing", rules)


class RuleScopeTest(unittest.TestCase):
    def _root(self, d, hand_scope=False, criteria=("check_a",), owner=None,
              carrier=None, node_criteria=None):
        touch(os.path.join(d, "rules", "09-test.md"),
              "applies_to: x\n" if hand_scope else "# 规则\n")
        touch(os.path.join(d, "tools", "check_a.py"), "# tool\n")
        pipe = {
            "nodes": [{"id": "n1", "criteria": list(node_criteria or criteria)}],
            "criteria_owner": owner if owner is not None else {c: ["n1"] for c in criteria},
            "criteria_carrier": carrier or {},
        }
        touch(os.path.join(d, "rules", "pipeline.json"), json.dumps(pipe))
        return d

    def test_clean_ok(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(cds.check_rule_scope(self._root(d)), [])

    def test_hand_scope_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            rules = {i["rule"] for i in cds.check_rule_scope(self._root(d, hand_scope=True))}
            self.assertIn("hand-scope", rules)

    def test_owner_missing_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self._root(d, criteria=("check_a",), owner={})
            self.assertIn("owner-missing", {i["rule"] for i in cds.check_rule_scope(root)})

    def test_carrier_missing_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self._root(d, criteria=("check_b",), owner={"check_b": ["n1"]})
            self.assertIn("carrier-missing", {i["rule"] for i in cds.check_rule_scope(root)})

    def test_carrier_exception_ok(self):
        with tempfile.TemporaryDirectory() as d:
            root = self._root(d, criteria=("ext",), owner={"ext": ["n1"]},
                              carrier={"ext": {"kind": "external"}})
            self.assertEqual(cds.check_rule_scope(root), [])

    def test_orphan_owner_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self._root(d, criteria=("check_a",),
                              owner={"check_a": ["n1"], "check_c": ["n9"]})
            self.assertIn("orphan-owner", {i["rule"] for i in cds.check_rule_scope(root)})


if __name__ == "__main__":
    unittest.main()

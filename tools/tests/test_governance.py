# -*- coding: utf-8 -*-
"""记录／归档／度量／AI 治理／发布后校验（T174／CP-S14-26–31）。"""
import json
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_governance as cg  # noqa: E402


def _load(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as f:
        return json.load(f)


class TestGovernance(unittest.TestCase):
    def test_repo_template_valid(self):
        self.assertEqual(cg.validate_archive(
            _load("specs/064-flow-spec-audit/results/t174-archive-template.json")), [])
        self.assertEqual(cg.validate_retention(_load("rules/retention.json")), [])
        self.assertEqual(cg.validate_metrics(_load("rules/metrics-baseline.json")), [])
        self.assertEqual(cg.validate_ai(_load("rules/ai-governance.json")), [])
        self.assertEqual(cg.validate_postpub(_load("rules/post-publication.json")), [])

    def test_actual_entry_missing_scorecard_editing(self):
        errors = cg.validate_archive(
            _load("specs/064-flow-spec-audit/results/t174-archive-habermas.json"))
        self.assertTrue(any("scorecard" in e for e in errors))
        self.assertTrue(any("editing" in e for e in errors))

    def test_retention_missing_item(self):
        data = _load("rules/retention.json")
        del data["items"]["scorecard"]
        self.assertTrue(cg.validate_retention(data))

    def test_metrics_no_preset_threshold(self):
        data = _load("rules/metrics-baseline.json")
        data["metrics"]["critical"]["threshold"] = 0
        self.assertTrue(cg.validate_metrics(data))
        data = _load("rules/metrics-baseline.json")
        del data["metrics"]["cycle_cost"]
        self.assertTrue(cg.validate_metrics(data))

    def test_ai_risk_and_no_disclosure(self):
        data = _load("rules/ai-governance.json")
        data["risk_register"][0].pop("mitigation")
        self.assertTrue(cg.validate_ai(data))
        data = _load("rules/ai-governance.json")
        data["disclosure"] = "public"
        self.assertTrue(cg.validate_ai(data))
        data = _load("rules/ai-governance.json")
        data["incident_handling"]["steps"] = []
        self.assertTrue(cg.validate_ai(data))

    def test_postpub_missing_entry_or_field(self):
        data = _load("rules/post-publication.json")
        del data["entries"]["spot_audit"]
        self.assertTrue(cg.validate_postpub(data))
        data = _load("rules/post-publication.json")
        data["entries"]["errata"].pop("evidence")
        self.assertTrue(cg.validate_postpub(data))


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""ISO 5060 评分卡校验与计分（T173／CP-S14-19–22）。"""
import json
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_qa_scorecard  # noqa: E402


class TestQaScorecard(unittest.TestCase):
    def _data(self):
        with open(os.path.join(REPO, "rules", "qa-scorecard.json"), encoding="utf-8") as f:
            return json.load(f)

    def test_repo_scorecard_valid(self):
        self.assertEqual(check_qa_scorecard.validate(self._data()), [])

    def test_missing_category_rejected(self):
        data = self._data()
        del data["categories"]["design"]
        self.assertTrue(check_qa_scorecard.validate(data))

    def test_severity_and_metric_rules(self):
        data = self._data()
        data["categories"]["accuracy"]["severity"] = "Fatal"
        self.assertTrue(check_qa_scorecard.validate(data))
        data = self._data()
        data["metrics"]["publication"]["limit"] = "1.5‰"
        self.assertTrue(check_qa_scorecard.validate(data))

    def test_sampling_rules(self):
        data = self._data()
        data["sampling"]["manual"]["order"] = "manual"
        self.assertTrue(check_qa_scorecard.validate(data))

    def test_score_zero_findings(self):
        result = check_qa_scorecard.score(self._data(), 10000, [])
        self.assertEqual(result["score"], 100.0)
        self.assertTrue(result["pass_publication"])

    def test_critical_fails_publication(self):
        result = check_qa_scorecard.score(
            self._data(), 10 ** 9,
            [{"category": "accuracy", "severity": "Critical", "count": 1}])
        self.assertEqual(result["critical"], 1)
        self.assertFalse(result["pass_publication"])

    def test_penalty_math(self):
        result = check_qa_scorecard.score(
            self._data(), 1000,
            [{"category": "accuracy", "severity": "Critical", "count": 1}])
        self.assertEqual(result["penalty"], 100)
        self.assertEqual(result["score"], 0.0)

    def test_unknown_category_rejected(self):
        with self.assertRaises(ValueError):
            check_qa_scorecard.score(self._data(), 1000,
                                     [{"category": "bogus", "severity": "Minor", "count": 1}])

    def test_evaluator_registry_valid(self):
        with open(os.path.join(REPO, "rules", "evaluator-registry.json"), encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(check_qa_scorecard.validate_evaluator(data), [])
        data["calibration"]["threshold"] = None
        data["calibration"]["threshold_status"] = "set"
        self.assertTrue(check_qa_scorecard.validate_evaluator(data))
        del data["roles"]["arbiter"]
        self.assertTrue(check_qa_scorecard.validate_evaluator(data))


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""T175 清单校验（CP-S14-32–36）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_t175  # noqa: E402


def _read(name):
    path = os.path.join(REPO, "specs", "064-flow-spec-audit", "results", name)
    with open(path, encoding="utf-8") as f:
        return f.read()


class TestT175(unittest.TestCase):
    def test_repo_lists_valid(self):
        checks = check_t175.run(os.path.join(REPO, "specs", "064-flow-spec-audit", "results"))
        self.assertEqual(checks, {"rule_sync": [], "pilot_plan": [], "g5": [], "closure": []})

    def test_rule_sync_missing_source(self):
        text = _read("t175-rule-sync.md").replace("| specs/061 |", "| removed/061 |")
        self.assertTrue(check_t175.validate_rule_sync(text))

    def test_pilot_plan_missing_entry(self):
        text = _read("t175-pilot-plan.md").replace("| a/action |", "| a/action-x |")
        self.assertTrue(check_t175.validate_pilot_plan(text))

    def test_g5_must_be_open(self):
        text = _read("t175-g5-checklist.md").replace("未通过", "通过")
        self.assertTrue(check_t175.validate_g5(text))

    def test_closure_required_phrases(self):
        text = _read("t175-closure.md").replace("不执行翻译", "执行翻译")
        self.assertTrue(check_t175.validate_closure(text))


if __name__ == "__main__":
    unittest.main()

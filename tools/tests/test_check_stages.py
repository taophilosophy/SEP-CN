# -*- coding: utf-8 -*-
"""check_stages 判据登记表核对单测（ADR-0068：pipeline.json 判据唯一事实源）。"""
import json
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_stages import check, load_pipeline  # noqa: E402


class CheckStagesTest(unittest.TestCase):

    def test_pipeline_valid(self):
        """rules/pipeline.json 应全绿（11 项）。"""
        pipe = load_pipeline()
        hits = check(pipe)
        self.assertTrue(all(h["ok"] for h in hits), [h for h in hits if not h["ok"]])

    def test_negative_dual_gate(self):
        """构造判据双硬拦，S2 应失败。"""
        pipe = load_pipeline()
        for n in pipe["nodes"]:
            if n["id"] == "s1":
                n["criteria"] = ["check_pairs", "check_style"]
        hits = check(pipe)
        self.assertTrue(any(not h["ok"] and h["code"] == "S2" for h in hits))

    def test_negative_break_chain(self):
        """构造断链（双链首），S1 应失败。"""
        pipe = load_pipeline()
        for n in pipe["nodes"]:
            if n["id"] == "P3":
                n["prev"] = None
        hits = check(pipe)
        self.assertTrue(any(not h["ok"] and h["code"] == "S1" for h in hits))


if __name__ == "__main__":
    unittest.main()

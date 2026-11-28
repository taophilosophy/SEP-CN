# -*- coding: utf-8 -*-
"""ISO 5060 抽样计划（T173／CP-S14-21）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import qa_sample  # noqa: E402


class TestQaSample(unittest.TestCase):
    TEXT = """# 标题

## 一

第一段。

第二段。

## 二

第三段。

第四段。
"""

    def test_deterministic_and_section_covered(self):
        a = qa_sample.plan("a/x.md", self.TEXT, min_segments=2)
        b = qa_sample.plan("a/x.md", self.TEXT, min_segments=2)
        self.assertEqual(a, b)
        self.assertEqual(a["sections"], 2)
        sections = {s["section"] for s in a["selected"]}
        self.assertEqual(sections, {"一", "二"})
        self.assertGreaterEqual(a["target"], 2)

    def test_no_h2_single_section(self):
        result = qa_sample.plan("a/x.md", "# 标题\n\n只有一段。\n", min_segments=1)
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["selected"][0]["section"], "全文")

    def test_target_uses_min_segments(self):
        result = qa_sample.plan("a/x.md", self.TEXT, min_segments=20)
        self.assertEqual(result["target"], 20)
        self.assertEqual(len(result["selected"]), 4)

    def test_selected_unique(self):
        result = qa_sample.plan("a/x.md", self.TEXT, min_segments=2)
        ids = [s["index"] for s in result["selected"]]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()

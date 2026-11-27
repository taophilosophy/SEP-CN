# -*- coding: utf-8 -*-
"""punct_audit 误报单测（064 T190 q6）：法语撇号、段落换行、引号邻接空格。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import punct_audit  # noqa: E402


class ScanTextTest(unittest.TestCase):
    def test_apostrophe_not_quote_pair(self):
        data = punct_audit.scan_text("法语 point d’appui 不是单引号对。", "demo")
        self.assertEqual([i for i in data["issues"] if i["rule"] == "P-8"], [])

    def test_paragraph_break_not_quote_gap(self):
        data = punct_audit.scan_text("段落一结束。\n\n“段落二以引文开头。”", "demo")
        self.assertEqual([i for i in data["issues"] if i["rule"] == "P-18"], [])

    def test_inline_quote_gap_flagged(self):
        data = punct_audit.scan_text("他说 “你好”，随后离开。", "demo")
        self.assertTrue([i for i in data["issues"] if i["rule"] == "P-18"])

    def test_english_quote_space_not_flagged(self):
        data = punct_audit.scan_text("> a product of “reeducation” in English.", "demo")
        self.assertEqual([i for i in data["issues"] if i["rule"] == "P-18"], [])

    def test_half_width_after_han(self):
        data = punct_audit.scan_text("第 5 章, 101–105。", "demo")
        self.assertTrue([i for i in data["issues"] if i["rule"] == "P-20"])


if __name__ == "__main__":
    unittest.main()

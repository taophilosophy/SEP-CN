# -*- coding: utf-8 -*-
"""T281（G4）：ex-05 格式闭合八项正反例。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_format_closure as cfc  # noqa: E402


def rules(text):
    return [i["rule"] for i in cfc.check_text(text, "x.md")]


class FormatClosureTest(unittest.TestCase):
    def test_clean_ok(self):
        self.assertEqual(rules("# 题\n\n正文。\n"), [])

    def test_heading_skip(self):
        self.assertIn("heading-skip", rules("# 题\n\n### 跳级\n"))

    def test_heading_sequence_ok(self):
        self.assertNotIn("heading-skip", rules("# 题\n\n## 节\n\n### 小节\n"))

    def test_table_sep(self):
        self.assertIn("table-sep", rules("| 甲 | 乙 |\n| 一 | 二 |\n"))

    def test_table_with_sep_ok(self):
        self.assertNotIn("table-sep", rules("| 甲 | 乙 |\n| --- | --- |\n| 一 | 二 |\n"))

    def test_code_fence(self):
        self.assertIn("code-fence", rules("```\nx\n"))

    def test_code_fence_closed_ok(self):
        self.assertNotIn("code-fence", rules("```\nx\n```\n"))

    def test_math_delim(self):
        self.assertIn("math-delim", rules("公式 $x。\n"))

    def test_math_paired_ok(self):
        self.assertNotIn("math-delim", rules("公式 $x$。\n"))

    def test_html_entity(self):
        self.assertIn("html-entity", rules("A & B\n"))

    def test_html_entity_escaped_ok(self):
        self.assertNotIn("html-entity", rules("A &amp; B\n"))

    def test_trailing_space(self):
        self.assertIn("trailing-space", rules("正文。 \n"))

    def test_trailing_space_ok(self):
        self.assertNotIn("trailing-space", rules("正文。\n"))

    def test_consecutive_blank(self):
        self.assertIn("consecutive-blank", rules("甲\n\n\n乙\n"))

    def test_single_blank_ok(self):
        self.assertNotIn("consecutive-blank", rules("甲\n\n乙\n"))

    def test_final_newline(self):
        self.assertIn("final-newline", rules("正文。"))

    def test_final_newline_ok(self):
        self.assertNotIn("final-newline", rules("正文。\n"))


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""T274（G4）：check_math_zh C1–C10 规则正反例。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_math_zh as cm  # noqa: E402


def codes(text, name="sample.md"):
    d = tempfile.mkdtemp()
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return {c for c, _s, _m in cm.check_file(p, "")}


class MathZhRulesTest(unittest.TestCase):
    def test_clean_ok(self):
        self.assertEqual(codes("正文 $x+y$ 与 $$a=b$$ 均正常。\n"), set())

    def test_c1_sep_macro(self):
        self.assertIn("C1", codes("公式 $\\amp$。\n", name="action.md"))

    def test_c2_inner_space(self):
        self.assertIn("C2", codes("公式 $ x $。\n"))

    def test_c3_zero_width(self):
        self.assertIn("C3", codes("公式 $a\u200bb$。\n"))

    def test_c4_percent_hash(self):
        self.assertIn("C4", codes("公式 $a % b$。\n"))

    def test_c5_chinese_in_math(self):
        self.assertIn("C5", codes("公式 $中文$。\n"))

    def test_c6_unmatched_dollar(self):
        self.assertIn("C6", codes("正文 $ 未配对。\n"))

    def test_c7_currency(self):
        self.assertIn("C7", codes("价格 $150,000。\n"))

    def test_c8_english_connector(self):
        self.assertIn("C8", codes("公式 $\\text{and}$。\n"))

    def test_c9_prose_paren_math(self):
        self.assertIn("C9", codes("正文 \\(x+y\\) 旧记法。\n"))

    def test_c10_isolated_greek(self):
        self.assertIn("C10", codes("符号 $\\omega$。\n"))

    def test_fenced_code_exempt(self):
        self.assertEqual(codes("```\n$ x $\n```\n"), set())


if __name__ == "__main__":
    unittest.main()

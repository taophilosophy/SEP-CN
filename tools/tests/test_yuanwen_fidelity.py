# -*- coding: utf-8 -*-
"""yuanwen 保真工具单测：strip_math_ex 跨度统计（specs/039 I3 标定，2026-11-17）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_yuanwen_fidelity import (  # noqa: E402
    SENTINEL, strip_math, strip_math_ex)


class TestStripMathEx(unittest.TestCase):
    def test_inline_pair(self):
        t, s = strip_math_ex(r"a \(x+y\) b")
        self.assertEqual(s, {"spans": 1, "oversize": 0, "unclosed": 0})
        self.assertEqual(t, "a " + SENTINEL + " b")

    def test_display_pair_multiline(self):
        t, s = strip_math_ex("a $$x\n+y$$ b")
        self.assertEqual(s["spans"], 1)
        self.assertEqual(t, "a " + SENTINEL + " b")

    def test_left_paren_no_truncate(self):
        # \right) 内部括号不再提前截断（2026-11-16 formal-belief 判例）
        t, s = strip_math_ex(r"\(f(\left(x\right))\)")
        self.assertEqual(s["spans"], 1)
        self.assertEqual(t, SENTINEL)

    def test_escaped_opener_literal(self):
        t, s = strip_math_ex(r"价格 \$5 与 \$7")
        self.assertEqual(s, {"spans": 0, "oversize": 0, "unclosed": 0})
        self.assertIn("5", t)

    def test_unclosed_opener(self):
        t, s = strip_math_ex("a $x b")
        self.assertEqual(s["unclosed"], 1)
        self.assertEqual(s["spans"], 0)

    def test_oversize_span_flagged(self):
        body = "q" * 7000
        t, s = strip_math_ex("$" + body + "$ tail")
        self.assertEqual(s["spans"], 1)
        self.assertEqual(s["oversize"], 1)

    def test_span_count_symmetry_signal(self):
        # 合并跨度判例：html 两个公式夹正文 vs md 一个大跨度 → 计数不等
        _, sa = strip_math_ex(r"\(x\) and \(y\)")
        _, sb = strip_math_ex("$x and y$")
        self.assertEqual(sa["spans"], 2)
        self.assertEqual(sb["spans"], 1)
        self.assertNotEqual(sa["spans"], sb["spans"])  # 深比对据此判 math-asymmetric

    def test_strip_math_wrapper(self):
        self.assertEqual(strip_math(r"\(x\)"), SENTINEL)

    def test_closer_escaped_not_matched(self):
        # closer 前带反斜杠不闭合（v1 既有语义保留）
        t, s = strip_math_ex(r"\(a\) b \(c\)")
        self.assertEqual(s["spans"], 2)


if __name__ == "__main__":
    unittest.main()

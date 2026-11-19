# -*- coding: utf-8 -*-
"""term_flow 写册引号归一（rules/02 第 11 条）：直角引号不得经 rowspec 回流登记册。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.term_flow import _quote_norm, build_row  # noqa: E402


class TestQuoteNorm(unittest.TestCase):
    def test_corner_to_curly(self):
        self.assertEqual(_quote_norm('审定「畸形」为胚胎学义'), '审定“畸形”为胚胎学义')

    def test_double_corner(self):
        self.assertEqual(_quote_norm('『书』与「义」'), '‘书’与“义”')

    def test_no_corner_left(self):
        s = _quote_norm('a「b」c『d』')
        for ch in ('\u300c', '\u300d', '\u300e', '\u300f'):
            self.assertNotIn(ch, s)

    def test_non_str_passthrough(self):
        self.assertEqual(_quote_norm(None), None)

    def test_build_row_normalizes_basis(self):
        row = build_row({'en': 'abnormality', 'zh': '异常', 'table': 'term',
                         'note': '审定「畸形」为胚胎学义'}, '2026-11-19')
        self.assertNotIn('\u300c', row)
        self.assertIn('“畸形”', row)


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
"""term_grade 分档提议单元测试（specs/050 §6）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.term_grade import grade


class GradeTests(unittest.TestCase):

    def test_A_direct(self):
        # -ism / 术语后缀 / foreign 纯原文 → A
        self.assertEqual(grade({'en': 'Transmissivism', 'type': 'ism', 'freq': 2})[0], 'A')
        self.assertEqual(grade({'en': 'Wirklichkeit', 'type': 'foreign', 'freq': 2})[0], 'A')
        self.assertEqual(grade({'en': 'ontological commitment', 'type': 'phrase', 'freq': 479})[0], 'A')

    def test_C_suspend(self):
        # topic / 单 Token 大写书名 / 高频全普通词 → C
        self.assertEqual(grade({'en': 'Importance and Influence', 'type': 'topic', 'freq': 4})[0], 'C')
        self.assertEqual(grade({'en': 'Republic', 'type': 'italic', 'freq': 791})[0], 'C')
        self.assertEqual(grade({'en': 'general theory', 'type': 'phrase', 'freq': 535})[0], 'C')

    def test_P_person(self):
        self.assertEqual(grade({'en': 'David Lewis', 'type': 'person', 'freq': 481})[0], 'P')

    def test_B_default(self):
        # 多词无后缀短语 → B（需核）
        self.assertEqual(grade({'en': 'organic unity', 'type': 'phrase', 'freq': 40})[0], 'B')


if __name__ == '__main__':
    unittest.main()

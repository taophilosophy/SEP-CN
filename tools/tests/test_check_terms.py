# -*- coding: utf-8 -*-
"""check_terms 单元测试（specs/002 T003）：冲突、自洽、规范化、告警分级。"""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import check_terms

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'fixtures', 'check_terms')
REG = os.path.join(FIX, 'registry.md')
GLO = os.path.join(FIX, 'glossary.md')


def run():
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = check_terms.main(['--registry', REG, '--glossary', GLO])
    return code, buf.getvalue()


class CheckTermsTests(unittest.TestCase):

    def setUp(self):
        self.code, self.out = run()

    def test_exit_code_reflects_hard_errors(self):
        self.assertEqual(self.code, 1)

    def test_conflict_on_disjoint_translations(self):
        self.assertIn('冲突: sophia', self.out)
        self.assertIn('智慧', self.out)
        self.assertIn('知识', self.out)

    def test_broken_deprecated_chain(self):
        self.assertIn('废弃链断裂：brokenchain', self.out)

    def test_duplicate_rows(self):
        self.assertIn('重复行：dupterms|重复译法', self.out)

    def test_missing_date_is_warning_not_error(self):
        self.assertIn('缺裁定日期（告警）：nodate', self.out)

    def test_subset_is_lagging_warning(self):
        self.assertIn('词汇表滞后（告警）: lagging', self.out)

    def test_key_normalization_ignores_italics_and_case(self):
        # *isonomia*（登记册）与 isonomia（词汇表）应命中同键且无冲突
        self.assertNotIn('isonomia', ''.join(
            l for l in self.out.splitlines() if l.startswith('冲突')))

    def test_variant_split_avoids_false_conflict(self):
        # doxa 学说/意见 与 词汇表 意见 为子集关系，非冲突
        self.assertNotIn('冲突: doxa', self.out)
        self.assertIn('词汇表滞后（告警）: doxa', self.out)

    def test_intersection_count(self):
        # 交集键：abductive reasoning, isonomia, doxa, lagging, sophia
        # （oldterm/dupterms/nodate/brokenchain 仅登记册侧，ghost 仅词汇表侧）
        self.assertIn('交集键 5', self.out)


if __name__ == '__main__':
    unittest.main()

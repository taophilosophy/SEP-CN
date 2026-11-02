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
REG5 = os.path.join(FIX, 'registry5.md')
PERSONS = os.path.join(FIX, 'persons.md')
GLO = os.path.join(FIX, 'glossary.md')


def run(*extra):
    buf = io.StringIO()
    argv = ['--registry', REG, '--glossary', GLO] + list(extra)
    with redirect_stdout(buf):
        code = check_terms.main(argv)
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

    def test_glossary_superset_not_lagging(self):
        # 词汇表含更宽通行变体（甲、乙 ⊃ 登记侧 甲）不报滞后：
        # 2026-11-03 口径收窄（发布视图允许含更宽变体，只报词汇表缺登记侧变体）
        self.assertNotIn('[登记册] lagging', self.out)

    def test_key_normalization_ignores_italics_and_case(self):
        # *isonomia*（登记册）与 isonomia（词汇表）应命中同键且无冲突
        self.assertNotIn('isonomia', ''.join(
            l for l in self.out.splitlines() if l.startswith('冲突')))

    def test_variant_split_avoids_false_conflict(self):
        # doxa 学说/意见 与 词汇表 意见 为子集关系，非冲突
        self.assertNotIn('冲突: doxa', self.out)
        self.assertIn('词汇表滞后（告警）: [登记册] doxa', self.out)

    def test_intersection_count(self):
        # 交集键：abductive reasoning, isonomia, doxa, lagging, sophia
        # （oldterm/dupterms/nodate/brokenchain 仅登记册侧；ghost/alcmaeon 仅词汇表侧）
        self.assertIn('交集键 5', self.out)

    def test_person_table_conflict_detected(self):
        # 人名表与词汇表同键异译 = 冲突（Alcmaeon：克罗顿人 vs 阿尔克迈翁）
        code, out = run('--registry2', PERSONS)
        self.assertIn('冲突: Alcmaeon', out)
        self.assertIn('人名表', out)

    def test_person_table_agreement_passes(self):
        # Plato 柏拉图 与词汇表一致（词汇表无 Plato 行则不进交集，不报错）
        code, out = run('--registry2', PERSONS)
        self.assertNotIn('冲突: Plato', out)

    def test_single_injection_skips_person_table(self):
        code, out = run()
        self.assertIn('人名表 (跳过) 行 0', out)

    def test_five_column_date_and_basis_parse(self):
        code, out = run('--registry', REG5)
        # 五列行：日期与依据齐全，无告警
        self.assertNotIn('缺裁定日期（告警）：dialetheism', out)
        self.assertNotIn('缺依据列（告警）：dialetheism', out)
        # 旧四列行：缺依据 = 告警，日期仍在第 4 列可读
        self.assertIn('缺依据列（告警）：oldcol', out)
        self.assertNotIn('缺裁定日期（告警）：oldcol', out)
        # 少于四列：列数告警，不误报废弃链
        self.assertIn('仅 3 列', out)

    def test_missing_basis_is_warning_not_error(self):
        code, out = run()
        self.assertIn('缺依据列（告警）：abductive reasoning', out)
        self.assertEqual(code, 1)  # 告警不计硬错误，退出码仍由冲突/自洽决定


if __name__ == '__main__':
    unittest.main()

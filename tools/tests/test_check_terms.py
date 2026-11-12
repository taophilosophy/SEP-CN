# -*- coding: utf-8 -*-
"""check_terms 单元测试（specs/002 T003）：自洽、规范化、告警分级。

ADR-0036（2026-11-13）：发布词汇表并网删除，原「登记册↔词汇表冲突/滞后/交集」
三表比对逻辑整体移除，测试收敛为两登记册自洽口径。
"""
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
SLUG = os.path.join(FIX, 'registry_slug.md')
PERSONS_ORIG = os.path.join(FIX, 'persons_orig.md')


def run(*extra):
    buf = io.StringIO()
    argv = ['--registry', REG] + list(extra)
    with redirect_stdout(buf):
        code = check_terms.main(argv)
    return code, buf.getvalue()


class CheckTermsTests(unittest.TestCase):

    def setUp(self):
        self.code, self.out = run()

    def test_exit_code_reflects_hard_errors(self):
        self.assertEqual(self.code, 1)

    def test_broken_deprecated_chain(self):
        self.assertIn('废弃链断裂：brokenchain', self.out)

    def test_duplicate_rows(self):
        self.assertIn('重复行：dupterms|重复译法', self.out)

    def test_missing_date_is_warning_not_error(self):
        self.assertIn('缺裁定日期（告警）：nodate', self.out)

    def test_no_glossary_leg_in_output(self):
        # ADR-0036：词汇表比对腿移除后，输出不再含词汇表字样
        self.assertNotIn('词汇表', self.out)

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
        self.assertEqual(code, 1)  # 告警不计硬错误，退出码仍由自洽决定

    def test_person_table_exempt_from_orig_warning(self):
        # ADR-0030（2026-11-10）：人名表原文列留「—」不计入「非英语术语缺原文」告警
        code, out = run('--registry2', PERSONS_ORIG)
        self.assertNotIn('非英语术语缺原文: 人名表 al-Fārābī', out)
        self.assertNotIn('非英语术语缺原文: 人名表 Ibn Sīnā', out)

    def test_slug_in_translation_column_is_hard_error(self):
        # 2026-11-10 补遗：合并脚本曾把来源 slug 写进译法列，slug 被当译法变体比对，
        # 造成滞后伪欠账（lvov-warsaw / cancer / logical-consequence 三例）。
        code, out = run('--registry', SLUG)
        self.assertIn('译法列混入词条 slug：deductive system', out)
        self.assertNotIn('译法列混入词条 slug：modus ponens', out)
        self.assertEqual(code, 1)


if __name__ == '__main__':
    unittest.main()

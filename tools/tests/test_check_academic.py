# -*- coding: utf-8 -*-
"""check_academic 单元测试（specs/003 T003）：版本事实、引注配对、结构告警、任务版本钉。"""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import check_academic

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'fixtures', 'check_academic')
BASE = os.path.join(FIX, 'baseline.json')
TASKS = os.path.join(FIX, 'tasks')


def run(*extra):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = check_academic.main(['--root', FIX, '--baseline', BASE,
                                    '--tasks-dir', TASKS] + list(extra))
    return code, buf.getvalue()


class CheckAcademicTests(unittest.TestCase):

    def setUp(self):
        self.code, self.out = run()

    def test_exit_code_reflects_hard_errors(self):
        self.assertEqual(self.code, 1)

    def test_pubinfo_missing_and_mismatch(self):
        self.assertIn('[pubinfo-missing] argument/beta-li-si.md', self.out)
        self.assertIn('[pubinfo-mismatch] argument/epsilon-wang-wu.md', self.out)
        self.assertIn('2002 年 4 月 10 日', self.out)
        self.assertIn('2003 年 4 月 10 日', self.out)

    def test_pubinfo_missing_on_hard_kind_summary(self):
        self.assertIn('pubinfo-missing 1', self.out)
        self.assertIn('pubinfo-mismatch 1', self.out)

    def test_footnote_orphans(self):
        self.assertIn('[orphan-ref] argument/delta-doc.md', self.out)
        self.assertIn('[orphan-def] argument/delta-doc.md', self.out)
        self.assertIn('[^k2]', self.out)
        self.assertIn('[^k3]', self.out)

    def test_task_pin_and_evidence(self):
        self.assertIn('[task-pin-missing]', self.out)
        self.assertIn('archive_edition', self.out)
        self.assertIn('[task-evidence-missing]', self.out)
        self.assertIn('步骤 s2', self.out)

    def test_structural_warnings_not_hard(self):
        self.assertIn('[biblio-missing] argument/gamma-doc.md', self.out)
        self.assertIn('[scholar-tools-missing] argument/gamma-doc.md', self.out)
        self.assertIn('[baseline-lookup-miss] argument/gamma-doc.md', self.out)

    def test_alpha_clean(self):
        self.assertNotIn('alpha-zhang-san.md',
                         [l for l in self.out.splitlines()
                          if l.strip().startswith('[')])

    def test_stub_skipped(self):
        self.assertIn('存根跳过 1', self.out)

    def test_docs_mode_clean_entry(self):
        code, out = run('--docs', os.path.join(FIX, 'argument', 'alpha-zhang-san.md'))
        self.assertEqual(code, 0)
        self.assertIn('OK：学术规范无硬错误', out)

    def test_strict_promotes_warnings(self):
        code, out = run('--docs', os.path.join(FIX, 'argument', 'gamma-doc.md'),
                        '--strict')
        self.assertEqual(code, 1)
        self.assertIn('biblio-missing', out)

    def test_docs_missing_file_exit_2(self):
        code, _ = run('--docs', os.path.join(FIX, 'argument', 'no-such.md'))
        self.assertEqual(code, 2)


if __name__ == '__main__':
    unittest.main()

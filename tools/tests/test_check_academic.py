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

    def test_note_def_unverified_without_en_package(self):
        # 夹具无 en/ 原始包：注号（note-*）定义是否被补充材料页引用无从核对，
        # 降级为告警而非硬错误（2026-11-07 CI 误判 s/spacetime-holearg.md 实例）
        self.assertIn('[orphan-def-unverified] argument/eta-notes.md', self.out)
        self.assertIn('[^note-7]', self.out)
        self.assertNotIn('[orphan-def] argument/eta-notes.md', self.out)

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

    # ---- 2026-11-04 复核纠正：在途豁免（state ≠ done）与 `_` 前缀脚手架跳过 ----

    def test_inflight_entry_tail_deferred(self):
        # theta（state=cleared）：尾节（脚注定义表/参考文献/学术工具）未拼装
        # 属正常中间态，不得报尾节类发现
        self.assertNotIn('[biblio-missing] argument/theta-inflight.md', self.out)
        self.assertNotIn('[orphan-ref] argument/theta-inflight.md', self.out)
        self.assertNotIn('[scholar-tools-missing] argument/theta-inflight.md', self.out)
        # 在途计数：alpha（s1_checked）+ beta（drafted）+ theta（cleared）
        self.assertIn('在途豁免 3', self.out)

    def test_done_entry_pubinfo_still_enforced(self):
        # 在途豁免只覆盖尾节拼装类；pubinfo 等正文级检查对 done 词条照常全量把关
        self.assertIn('[pubinfo-mismatch] argument/epsilon-wang-wu.md', self.out)

    def test_done_entry_tail_still_enforced(self):
        # zeta（state=done）尾节缺失仍上报
        self.assertIn('[biblio-missing] argument/zeta-done.md', self.out)
        self.assertIn('[orphan-ref] argument/zeta-done.md', self.out)

    def test_underscore_scaffold_skipped(self):
        # `_` 前缀路径=会话脚手架，不按词条体例检查（防批量提示词误报）
        self.assertNotIn('_batch_prompts', self.out)
        self.assertNotIn('_workspace_note', self.out)

    def test_routine_task_pin_exempt(self):
        # 非词条绑定任务（zh_doc 为空，如每日例行漂移检查）不要求 version_pin
        self.assertNotIn('routine-drift', self.out)


if __name__ == '__main__':
    unittest.main()

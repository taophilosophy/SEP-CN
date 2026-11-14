# -*- coding: utf-8 -*-
"""mech_audit 单元测试（specs/031 FR-3/FR-5）。

只测纯函数与参数口径：分类器（pure/conn/susp）、diff 配对、无 slug 时的退出码。
不跑真实词条审计（依赖 git 历史，属批次执行面）。
"""
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import mech_audit


class ClassifyTests(unittest.TestCase):

    def test_pure_when_only_punctuation_changes(self):
        cat, why = mech_audit.classify('他来了——然后走了', '他来了：然后走了')
        self.assertEqual(cat, 'pure')

    def test_conn_when_small_word_patch(self):
        # 术语换形（≤4 字）落 conn：只产候选，须人工判读
        cat, why = mech_audit.classify('这是一种意志薄弱的现象', '这是一种不能自制的现象')
        self.assertEqual(cat, 'conn')
        self.assertIn('ins=', why)

    def test_susp_for_mid_similarity_rewrite(self):
        cat, _ = mech_audit.classify(
            '因为这一论证依赖前提的必然性所以成立',
            '该论证之所以成立，端赖前提之为必然')
        self.assertEqual(cat, 'susp')

    def test_none_for_unrelated_lines(self):
        cat, _ = mech_audit.classify('这是一段完全无关的中文', '另起一句讲别的主题内容')
        self.assertIsNone(cat)

    def test_none_when_stripped_text_empty(self):
        cat, _ = mech_audit.classify('——', '：')
        self.assertIsNone(cat)


class PairsTests(unittest.TestCase):

    def test_pairs_from_diff_groups_by_hunk(self):
        diff = ("@@ -1,2 +1,2 @@\n"
                "-旧一\n"
                "-旧二\n"
                "+新一\n"
                "+新二\n"
                "@@ -9 +9 @@\n"
                "-旧三\n"
                "+新三\n")
        self.assertEqual(mech_audit.pairs_from_diff(diff),
                         [('旧一', '新一'), ('旧二', '新二'), ('旧三', '新三')])

    def test_pairs_from_diff_skips_file_headers(self):
        diff = ("--- a/x.md\n"
                "+++ b/x.md\n"
                "@@ -1 +1 @@\n"
                "-甲\n"
                "+乙\n")
        self.assertEqual(mech_audit.pairs_from_diff(diff), [('甲', '乙')])


class CliTests(unittest.TestCase):

    def test_no_slug_returns_2(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = mech_audit.main([])
        self.assertEqual(code, 2)
        self.assertIn('用法', buf.getvalue())

    def test_missing_option_value_returns_2(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = mech_audit.main(['some-slug', '--out'])
        self.assertEqual(code, 2)
        self.assertIn('需要参数值', buf.getvalue())

    def test_unknown_slug_yields_empty_spots(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            spots = mech_audit.audit('__no_such_slug__')
        self.assertEqual(spots, [])
        self.assertIn('未找到词条文件', buf.getvalue())


if __name__ == '__main__':
    unittest.main()

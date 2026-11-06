# -*- coding: utf-8 -*-
"""check_junk 根目录白名单单测（ADR-0023：根级散件咬不住 add -A 的教训）。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_junk import ROOT_ALLOW, root_hits  # noqa: E402


def hits_of(tracked, root_dir):
    return {name: why for name, why in root_hits(tracked, root_dir)}


class RootAllowlistTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def touch(self, name):
        path = os.path.join(self.root, name)
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write('')

    def test_allowlisted_entries_pass(self):
        self.touch('SUMMARY.md')
        self.touch('rules/01-repository-structure.md')
        os.makedirs(os.path.join(self.root, 'a'))
        self.assertEqual(hits_of(['SUMMARY.md', 'rules/x.md', 'a/b.md'], self.root), {})

    def test_stray_root_file_flagged(self):
        self.touch('dev_null.json')
        hits = hits_of([], self.root)
        self.assertIn('根目录散件（工作区）', hits.get('dev_null.json', ''))

    def test_stray_root_file_flagged_even_when_tracked(self):
        # 已入库但工作区已清理：仍须报“已入库”越界，防 CI 放行
        hits = hits_of(['trans_p1.json'], self.root)
        self.assertIn('已入库', hits.get('trans_p1.json', ''))

    def test_ignored_junk_flagged(self):
        # 忽略规则漏没漏都要拦：__pycache__ 在根目录即越界
        os.makedirs(os.path.join(self.root, '__pycache__'))
        self.assertIn('__pycache__', hits_of([], self.root))

    def test_underscore_scaffolding_flagged(self):
        os.makedirs(os.path.join(self.root, '_f_pipe'))
        self.assertIn('_f_pipe', hits_of([], self.root))

    def test_letter_and_digit_dirs_allowed(self):
        for name in list('abcdefghijklmnopqrstuvwxyz') + ['1']:
            self.assertIn(name, ROOT_ALLOW)
            os.makedirs(os.path.join(self.root, name))
        self.assertEqual(hits_of([], self.root), {})


if __name__ == '__main__':
    unittest.main()

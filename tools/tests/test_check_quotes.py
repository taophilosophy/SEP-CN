# -*- coding: utf-8 -*-
"""check_quotes 直角引号总检单测（rules/02-style.md 第 11 条已立文，缺机检）。"""
import io
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_quotes import EXCLUDE_PREFIX, scan  # noqa: E402

CLEAN = '说“如此”即可，单引号用‘甲’。\n'
DIRTY = '音译连接号用间隔号「·」；ibn 译「伊本」。\n'
JAPANESE = '[^x]: 大橋良介, 1986, 「切れ」の構造, 東京：中央公論社.\n'


class ScanTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        path = os.path.join(self.root, rel)
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        return rel

    def test_clean_file_no_hit(self):
        rel = self.write('a/clean.md', CLEAN)
        hits, allowed = scan(self.root, [rel])
        self.assertEqual(hits, [])
        self.assertEqual(allowed, 0)

    def test_corner_quotes_flagged(self):
        rel = self.write('rules/x.md', DIRTY)
        hits, _ = scan(self.root, [rel])
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0][0], rel)
        self.assertEqual(hits[0][1], 1)
        self.assertEqual(len(hits[0][2]), 4)  # 「·」「伊本」共 4 个直角引号字符

    def test_allowlist_counted_not_reported(self):
        rel = self.write('j/japanese-aesthetics.md', JAPANESE)
        hits, allowed = scan(self.root, [rel])
        self.assertEqual(hits, [])
        self.assertEqual(allowed, 2)

    def test_excluded_prefix_skipped(self):
        rels = [self.write('specs/s/exec.md', DIRTY),
                self.write('en/a/page.md', DIRTY),
                self.write('yuanwen/a/page.md', DIRTY),
                self.write('a/real.md', DIRTY)]
        hits, allowed = scan(self.root, rels)
        self.assertEqual({h[0] for h in hits}, {'a/real.md'})
        self.assertEqual(allowed, 0)
        self.assertIn('specs/', EXCLUDE_PREFIX)


if __name__ == '__main__':
    unittest.main()

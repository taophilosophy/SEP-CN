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
                self.write('html/a/page.md', DIRTY),
                self.write('a/real.md', DIRTY)]
        hits, allowed = scan(self.root, rels)
        self.assertEqual({h[0] for h in hits}, {'a/real.md'})
        self.assertEqual(allowed, 0)
        self.assertIn('specs/', EXCLUDE_PREFIX)

    def test_merge_marker_flagged(self):
        # 2026-11-10 补遗：stash pop 冲突标记曾随提交进入 ren-ming-biao.md（重复行事故）
        rel = self.write('ren-ming-biao.md',
                         '| 甲 | — | 乙 |\n<<<<<<< Updated upstream\n| 丙 |\n=======\n| 丁 |\n>>>>>>> Stashed changes\n')
        hits, _ = scan(self.root, [rel])
        labels = [h[2] for h in hits]
        self.assertEqual(labels, [['合并冲突标记'], ['合并冲突标记']])
        self.assertEqual([h[1] for h in hits], [2, 6])

    def test_setext_underline_not_flagged(self):
        # `=======` 是 Markdown setext 标题下划线，不得误报
        rel = self.write('a/heading.md', '标题\n=======\n')
        hits, _ = scan(self.root, [rel])
        self.assertEqual(hits, [])


if __name__ == '__main__':
    unittest.main()

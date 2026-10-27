# -*- coding: utf-8 -*-
"""term_harvest 单元测试（specs/008 US-1）：提取、求差、幂等、注入。"""
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import term_harvest

DOC1 = '''# Test Entry

The *quuxological realism* view and the *quuxological realism* again.
“florbian transfer” is quoted here. Florbian transfer appears often.
Many scholars defend quuxianism today. Quuxianism matters.

dialetheism is already registered and must not enter the pool.
'''
DOC2 = '''# Test Entry Two

Florbian transfer and florbian transfer once more, plus prose about
the quaristic sublation mechanism across pages. Zorpia Theoretica wrote it,
and Zorpia Theoretica revised it.
'''


class TermHarvestTests(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='harvest_test_')
        self.corpus = os.path.join(self.tmp, 'corpus', 'a')
        os.makedirs(self.corpus)
        open(os.path.join(self.corpus, 'doc-one.md'), 'w',
             encoding='utf-8').write(DOC1)
        open(os.path.join(self.corpus, 'doc-two.md'), 'w',
             encoding='utf-8').write(DOC2)
        self.pool = os.path.join(self.tmp, 'pool.json')
        self.cache = os.path.join(self.tmp, 'cache')

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_harvest(self, *extra):
        buf = io.StringIO()
        argv = ['--corpus', os.path.join(self.tmp, 'corpus'), '--pool', self.pool,
                '--cache', self.cache] + list(extra)
        with redirect_stdout(buf):
            code = term_harvest.main(argv)
        return code, buf.getvalue()

    def load_pool(self):
        return json.load(open(self.pool, encoding='utf-8'))

    def test_extraction_and_diff(self):
        code, out = self.run_harvest('--letter', 'a')
        self.assertEqual(code, 0)
        pool = self.load_pool()
        keys = {c['en'].casefold(): c for c in pool['candidates']}
        # 斜体路线 + 频次合并
        self.assertIn('quuxological realism', keys)
        self.assertEqual(keys['quuxological realism']['type'], 'italic')
        # -ism 路线
        self.assertIn('quuxianism', keys)
        # 引语路线
        self.assertIn('florbian transfer', keys)
        # 人名路线
        self.assertIn('zorpia theoretica', keys)
        # 已登记词（真实登记册）不入池
        self.assertNotIn('dialetheism', keys)
        # 纯停用词短语不入池
        self.assertNotIn('the quaristic', keys)

    def test_resume_is_idempotent(self):
        self.run_harvest('--letter', 'a')
        first = self.load_pool()
        n1, f1 = first['meta']['candidates'], {
            c['en']: c['freq'] for c in first['candidates']}
        self.run_harvest('--letter', 'a')
        second = self.load_pool()
        self.assertEqual(second['meta']['candidates'], n1)
        for c in second['candidates']:
            self.assertEqual(c['freq'], f1[c['en']])
        # 缓存生效：第二次不再解析（files_processed 相同即可证幂等）
        self.assertEqual(second['meta']['files_processed'],
                         first['meta']['files_processed'])

    def test_missing_corpus_errors(self):
        code, out = self.run_harvest('--corpus',
                                     os.path.join(self.tmp, 'nope'))
        self.assertEqual(code, 2)


if __name__ == '__main__':
    unittest.main()

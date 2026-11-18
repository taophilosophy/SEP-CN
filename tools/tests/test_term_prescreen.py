# -*- coding: utf-8 -*-
"""term_prescreen / check_term_pool 单元测试（specs/050 治标+口径）。"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import term_prescreen, check_term_pool


class PrescreenClassifyTests(unittest.TestCase):

    def test_reject_deterministic_residue(self):
        # 数学/LaTeX、子句、连字符、单字泛词、书目、cjk 虚词
        self.assertEqual(term_prescreen.classify('mid cdot', 'phrase')[0],
                         '残渣:latex')
        self.assertEqual(term_prescreen.classify('am in pain', 'quoted')[0],
                         '泛词:子句片段')
        self.assertEqual(term_prescreen.classify("Kant argues", 'phrase')[0],
                         '泛词:子句片段')
        self.assertEqual(term_prescreen.classify('suárez- suárez-', 'foreign')[0],
                         '残渣:连字符')
        self.assertEqual(term_prescreen.classify('good', 'quoted')[0],
                         '泛词:单字')
        self.assertEqual(term_prescreen.classify('Thābit b. For', 'arabic')[0],
                         '残渣:书目')  # "b." 书目缩写残片
        self.assertEqual(term_prescreen.classify('之乎者也矣焉哉', 'cjk')[0],
                         '残渣:cjk虚词')

    def test_keep_real_terms(self):
        # 真术语不得误杀
        for term, typ in [('natural kind', 'phrase'),
                          ('ontological commitment', 'phrase'),
                          ('problem of evil', 'topic'),
                          ('identity of indiscernibles', 'topic'),
                          ('true belief', 'phrase'),
                          ('florbian transfer', 'quoted')]:
            self.assertIsNone(term_prescreen.classify(term, typ)[0],
                              '真术语被误杀: %s' % term)

    def test_foreign_fragment_rejected(self):
        # 英语普通词 + 原文混排 → 外语残片
        self.assertEqual(term_prescreen.classify('Gödel published', 'foreign')[0],
                         '残渣:外语残片')
        self.assertEqual(term_prescreen.classify('Künne chap', 'foreign')[0],
                         '残渣:外语残片')
        # 纯原文术语保留
        self.assertIsNone(term_prescreen.classify('Wirklichkeit', 'foreign')[0])


class CheckTermPoolGateTests(unittest.TestCase):

    def _write(self, data):
        f = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False,
                                        encoding='utf-8')
        json.dump(data, f, ensure_ascii=False)
        f.close()
        return f.name

    def test_green_pool(self):
        pool = {'candidates': [
            {'en': 'ontological commitment', 'type': 'phrase', 'status': 'new'},
            {'en': 'good', 'type': 'quoted',
             'status': 'rejected:自动预筛-泛词:单字'},
        ]}
        manifest = {'rejected': {'泛词:单字': ['good']}}
        p, m = os.path.join(tempfile.gettempdir(), 'tp_pool.json'), \
            os.path.join(tempfile.gettempdir(), 'tp_man.json')
        json.dump(pool, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump(manifest, open(m, 'w', encoding='utf-8'), ensure_ascii=False)
        self.assertEqual(check_term_pool.main(['--pool', p, '--manifest', m]), 0)

    def test_regression_and_orphan_red(self):
        pool = {'candidates': [
            {'en': 'am in pain', 'type': 'quoted', 'status': 'new'},      # I1 回归
            {'en': 'rogue-term', 'type': 'phrase',
             'status': 'rejected:自动预筛-泛词:单字'},                        # I2 孤儿
        ]}
        manifest = {'rejected': {'泛词:单字': ['good']}}
        p = os.path.join(tempfile.gettempdir(), 'tp_pool2.json')
        m = os.path.join(tempfile.gettempdir(), 'tp_man2.json')
        json.dump(pool, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
        json.dump(manifest, open(m, 'w', encoding='utf-8'), ensure_ascii=False)
        self.assertEqual(check_term_pool.main(['--pool', p, '--manifest', m]), 1)


if __name__ == '__main__':
    unittest.main()

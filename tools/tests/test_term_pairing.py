# -*- coding: utf-8 -*-
"""term_pairing 单元测试（ADR-0088 判据共享实现）。"""
import unittest

from tools import term_pairing as tp


def mini_index(records):
    idx = {'records': records, 'by_key': {}, 'en': {}, 'cn': {}}
    for i, r in enumerate(records):
        for e in tp.en_stems(r[1]):
            idx['en'].setdefault(e, []).append(i)
        for ck in tp.cn_keys(r[0]):
            idx['cn'].setdefault(ck, []).append(i)
    return idx


class TestStrong(unittest.TestCase):
    def test_possessive_stripped(self):
        # 批 41 实证：Bohr's 与 Bohr 须同形
        self.assertEqual(tp.strong("Bohr's principle"), 'bohrprinciple')

    def test_cjk_kept(self):
        # 判等不得把中文洗空（specs/058 批 29 教训）
        self.assertEqual(tp.strong('局域性'), '局域性')
        self.assertEqual(tp.strong('abc'), 'abc')


class TestEnStems(unittest.TestCase):
    def test_plural(self):
        self.assertIn('analyticset', tp.en_stems('analytic sets'))

    def test_isize(self):
        self.assertTrue(tp.en_stems('localization') & tp.en_stems('localisation'))

    def test_multi_sense(self):
        # 因果关系（causal relation; causation）按义项分拆
        self.assertTrue(tp.en_stems('causal relation; causation') & tp.en_stems('causation'))


class TestCnKeys(unittest.TestCase):
    def test_gb_bracket_optional(self):
        # 优先[方]法＝优先法／优先方法（批 49 前的实证：priority method 行）
        self.assertEqual(tp.cn_keys('优先[方]法'), {'优先法', '优先方法'})

    def test_bracket_content_kept(self):
        # 初等等价[的] 与 初等等价 同形（elementarily equivalent 行）
        self.assertIn('初等等价', tp.cn_keys('初等等价[的]'))

    def test_paren_stripped(self):
        self.assertEqual(tp.cn_keys('范式（paradigm）'), {'范式'})


class TestZhForms(unittest.TestCase):
    def test_quoted_and_shen_ding(self):
        zh = '公民不服从（审定作“公民抗命”）'
        self.assertIn(tp.strong('公民抗命'), tp.zh_forms(zh))
        self.assertIn(tp.strong('公民不服从'), tp.zh_forms(zh))


class TestLibOf(unittest.TestCase):
    def test_libs(self):
        self.assertEqual(tp.lib_of('物理学名词'), 'audit')
        self.assertEqual(tp.lib_of('海峡两岸心理学名词'), 'tw')
        self.assertEqual(tp.lib_of('国家标准文件'), 'std')
        self.assertEqual(tp.lib_of('大数据百科术语辞典'), 'other')
        self.assertIsNone(tp.lib_of(''))


class TestClassifyRow(unittest.TestCase):
    RECORDS = [
        ['停机问题', 'halting problem', '自然辩证法名词', '03.662', 'audit'],
        ['偶适概括', 'accidental regularities; uniformities; generalizations',
         '自然辩证法名词', '03.210', 'audit'],
        ['个体主义者', 'individualist', '海峡两岸心理学名词', '', 'tw'],
        ['侏儒', 'dwarf', '兽医学名词', '', 'audit'],
    ]

    def setUp(self):
        self.index = mini_index(self.RECORDS)

    def test_pair(self):
        v, ev = tp.classify_row('halting problem', '停机问题', '审定名词库', self.index)
        self.assertEqual(v, 'pair')
        self.assertEqual(ev[0], '停机问题')

    def test_en_only(self):
        # locality 审定只有 局域性（另一条），本 index 无 → en 命中走 偶适概括? 构造 en-only：
        # 用已知英文配对但中文不合的记录
        v, _ev = tp.classify_row('dwarf', '小矮人', '审定名词库', self.index)
        self.assertEqual(v, 'en-only')

    def test_cn_only(self):
        v, ev = tp.classify_row('accidental generalization', '偶适概括', '审定名词库', self.index)
        self.assertEqual(v, 'cn-only')
        self.assertEqual(ev[0], '偶适概括')

    def test_tw_only(self):
        v, ev = tp.classify_row('individualist', '个体主义者', '审定名词库', self.index)
        self.assertEqual(v, 'tw-only')
        self.assertEqual(ev[4], 'tw')

    def test_none(self):
        v, _ev = tp.classify_row('knowing how', '知道如何', '审定名词库', self.index)
        self.assertEqual(v, 'none')

    def test_slash_key_segments(self):
        # 键含「 / 」变体段时按段查（Chinese Room / Chinese Room argument 判例）
        idx = mini_index([['中文屋论证', 'Chinese room argument', '自然辩证法名词', '03.581', 'audit']])
        v, _ev = tp.classify_row('Chinese Room / Chinese Room argument',
                                 '中文屋（亦作“中文屋论证”）', '审定名词库', idx)
        self.assertEqual(v, 'pair')


class TestNeedsPairing(unittest.TestCase):
    def test_claim_requires_pairing(self):
        self.assertTrue(tp.needs_pairing('审定名词库（termonline-all，凭证 2026-11-23）'))

    def test_negative_claim_exempt(self):
        self.assertFalse(tp.needs_pairing('审定库无对口条目（2026-11-26 界面精确匹配复核：未审定）'))
        self.assertFalse(tp.needs_pairing('学界通行汉译；审定库无查询件（目录现查）'))
        self.assertFalse(tp.needs_pairing('审定库无精确命中，2026-11-25'))

    def test_acknowledged_form_exempt(self):
        self.assertFalse(tp.needs_pairing('审定作“局域性”（物理学名词；界面复核）；本行“定域性”为通行形'))

    def test_no_shen_ding_exempt(self):
        self.assertFalse(tp.needs_pairing('学界通行译名；凭证 2026-11-07'))


if __name__ == '__main__':
    unittest.main()

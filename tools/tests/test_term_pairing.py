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

    def test_loose_token_no_longer_exempts(self):
        """旧词表的单字豁免（义／异）与裸“复核”“作“”曾使 3,008 条断言几乎全豁免。"""
        self.assertTrue(tp.needs_pairing('审定名词库（termonline-all，凭证）；与本行义务论用法一致'))
        self.assertTrue(tp.needs_pairing('审定义务论；与本行差异在域'))
        self.assertTrue(tp.needs_pairing('审定库复核一致（termonline-all 浏览器通道凭证 2026-10-29）'))
        self.assertTrue(tp.needs_pairing('审定库命中；译法列作亦作“X”'))

    def test_claim_text_ignores_trans_forms(self):
        # 译法列的“亦作“X””不得进待判文本；译法列自带“审定…”时才并入
        self.assertEqual(tp.claim_text('建构主义（亦作“建构论”）', '学界通行；凭证 2026-11-07'),
                         '学界通行；凭证 2026-11-07')
        self.assertIn('审定', tp.claim_text('建构主义（审定作“构造主义”）', '凭证 2026-11-07'))

    def test_explicit_citation_per_segment(self):
        self.assertTrue(tp.explicit_citation('审定作“诠释学”（hermeneutics，自然辩证法名词）'))
        self.assertFalse(tp.explicit_citation('审定名词库（termonline-all，凭证）；亦作“解释学”'))

    def test_segment_scope_beats_row_scope(self):
        # GB 标准库的负证句不得把同行的审定正断言一起豁免（academic freedom 判例）
        self.assertTrue(tp.needs_pairing(
            '知网系 GB 标准库查证：首屏无该键配对条目（命中均为模糊邻居）；'
            '审定库复核一致（termonline-all 浏览器通道凭证 2026-10-29）'))

    def test_paren_semicolon_not_split(self):
        # 括号内的分号不切句（absolute idealism 判例）
        self.assertFalse(tp.needs_pairing(
            '审定库无对口条目（2026-11-25 界面复核：未审定；原“审定库复核一致”表述作废）'))

    def test_citation_after_library_word(self):
        # 「审定名词库“性别歧视”」虽无“作”字，也是引形
        self.assertFalse(tp.needs_pairing(
            '审定名词库“性别歧视”对应 gender discrimination（计划生育名词）'))
        self.assertFalse(tp.needs_pairing('审定作“潜变量”（社会学名词·数据分析，2025）'))

    def test_spaced_no_counterpart(self):
        self.assertFalse(tp.needs_pairing('审定库无 transcendence 对口（2026-11-26 配对复核）'))


class TestCitationLibs(unittest.TestCase):
    """库名如实（ADR-0088 第 2 条）：引证形与实际库别不符即问题。"""

    def setUp(self):
        self.index = mini_index([
            ['畸形', 'malformation', '海峡两岸解剖与组织胚胎学名词', '', 'tw'],
            ['诠释学', 'hermeneutics', '自然辩证法名词', '', 'audit'],
            ['一阐提', 'Icchantika', '中华思想文化术语传播工程', '', 'other'],
        ])

    def test_claim_extraction(self):
        claims = tp.citation_claims('审定名词库（termonline-all·地理学）作“反本质论”')
        self.assertEqual(claims[0][0], tp.LIB_AUDIT)
        claims = tp.citation_claims('海峡两岸名词对照库·心理学作“亲和性”')
        self.assertEqual(claims[0][0], tp.LIB_TW)
        # 亦作不是引证
        self.assertEqual(tp.citation_claims('删亦作“纯音乐”（撞形处置）'), [])

    def test_mislabel_flagged(self):
        bad = tp.audit_citation_libs(
            self.index, 'abnormality',
            '审定名词库（termonline-all·解剖与组织胚胎学，凭证）作“畸形”')
        self.assertEqual(len(bad), 1)
        self.assertIn('tw', bad[0])

    def test_correct_lib_silent(self):
        self.assertEqual(tp.audit_citation_libs(
            self.index, 'hermeneutics', '审定作“诠释学”（自然辩证法名词）'), [])

    def test_mixed_claim_flagged(self):
        bad = tp.audit_citation_libs(
            self.index, 'icchantika',
            '审定名词库（termonline-all·中华思想文化术语传播工程）作“一阐提”')
        self.assertTrue(bad and '既称审定' in bad[0])

    def test_negated_audit_not_mixed(self):
        # 「审定公布库无，其他术语库作 X」是负证＋库别交代，不算混标
        idx = mini_index([['平等', 'Equality', '中华思想文化术语传播工程', '', 'other']])
        self.assertEqual(tp.audit_citation_libs(
            idx, 'isonomia',
            '审定库复核查无（缓存通道 2026-10-29）；2026-11-26 界面复核：审定公布库无，'
            '其他术语库“中华思想文化术语传播工程”作“平等”（Equality，历史）'), [])

    def test_print_citation_with_code_skipped(self):
        # 带条文号的纸质审定本引证，索引未必覆盖，不作失实判定
        self.assertEqual(tp.audit_citation_libs(
            self.index, 'cardinal', '审定名词库（数学名词 01.0125，1993）作“基数”'), [])


class TestMultiFormTrans(unittest.TestCase):
    def test_semicolon_forms_split(self):
        idx = mini_index([['构造主义', 'constructivism', '自然辩证法名词', '03.272', 'audit']])
        v, _ev = tp.classify_row('constructivism', '构造主义；建构主义', '审定名词库', idx)
        self.assertEqual(v, 'pair')

    def test_slash_and_dunhao_forms_split(self):
        idx = mini_index([['斯多葛学派', 'Stoics', '自然辩证法名词', '02.142', 'audit']])
        v, _ev = tp.classify_row('Stoic', '斯多葛／斯多葛学派（亦作“斯多亚”）', '审定名词库', idx)
        self.assertEqual(v, 'pair')


if __name__ == '__main__':
    unittest.main()

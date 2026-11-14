# -*- coding: utf-8 -*-
"""yuanwen 转换器单测（023 战役）：透传 HTML 内「反斜杠紧邻 <」的转义防线。

specs/023 Phase 1 构建阻塞实证：typelogical-grammar / nonwellfounded-set-theory
的 en 源有语言学 \ 算子紧贴 <em>（嵌套表透传段），md 渲染层把 \< 当转义——
反斜杠被吃且 </em> 变孤儿，Vue 模板编译报 Invalid end tag。修法：透传消毒时
翻倍为 \\<（渲染回字面反斜杠），已翻倍不动（幂等）。
"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.yuanwen import (  # noqa: E402
    _sanitize_table_html, build_cite_keys, inline_to_md, link_citations)


class TestCitePrefixCollision(unittest.TestCase):
    """023 审计实证：姓名无右词边界时前缀子串幻配（action §7.3，2026-11-14）。

    书目同有 Clark, Philip 2010 与 Clarke, Randolph 2010；正文组
    (Clarke 2010; 2014) 曾幻挂 clark-2010。修复：姓名两侧加 \\b。"""

    def _keys(self):
        entries = [
            'Clark, Philip, 2010, “Aspects, Guises, Species and Knowing”, *Journal of Philosophy*.',
            'Clarke, Randolph, 2010, “Omissions”, between others.',
            'Clarke, Randolph, 2014, “Omissions: A Reply”, somewhere.',
        ]
        return build_cite_keys(entries)

    def test_prefix_surname_does_not_match_longer_surname_group(self):
        keys = self._keys()
        self.assertIn('clark-2010', [k['key'] for k in keys])
        text = 'This follows Clarke (Clarke 2010; 2014).'
        new, count, used = link_citations(text, keys)
        self.assertNotIn('[^clark-2010]', new)
        self.assertIn('[^clarke-2010]', new)
        self.assertNotIn('[^clarke-2014]', new)  # 分号边界：2014 不跨条误配

    def test_direct_citation_still_matches(self):
        keys = self._keys()
        text = 'The guise of the good (Tenenbaum 2007; Clark 2010; Schafer 2013).'
        new, count, used = link_citations(text, keys)
        self.assertIn('[^clark-2010]', new)

    def test_apostrophe_surname_unaffected(self):
        entries = ["O'Brien, Robert, 2007, “Do”."]
        keys = build_cite_keys(entries)
        text = 'as argued (O’Brien 2007: 5).'
        new, count, used = link_citations(text, keys)
        self.assertIn('[^o’brien-2007]', new)


class TestBackslashBeforeTag(unittest.TestCase):
    def test_passthrough_backslash_doubled(self):
        # 透传段：\<em>A</em> → \\<em>A</em>（markdown 渲染回字面 \ + 真 em 对）
        seg = '<table><tr><td><em>B</em>\\<em>A</em></td></tr></table>'
        out = _sanitize_table_html(seg, slug='t')
        self.assertIn('<em>B</em>\\\\<em>A</em>', out)
        self.assertNotIn('<em>B</em>\\<em>A', out.replace('\\\\', '\x00'))

    def test_passthrough_backslash_idempotent(self):
        seg = '<table><tr><td>x\\<em>A</em></td></tr></table>'
        once = _sanitize_table_html(seg, slug='t')
        twice = _sanitize_table_html(once, slug='t')
        self.assertEqual(once, twice)

    def test_passthrough_latex_backslash_untouched(self):
        # LaTeX 序列（\frac 等）反斜杠后是字母，不翻倍
        seg = '<table><tr><td>\\(\\frac{a}{b}\\)</td></tr></table>'
        out = _sanitize_table_html(seg, slug='t')
        self.assertIn('$', out)
        self.assertNotIn('\\\\frac', out)

    def test_passthrough_star_entity_escaped(self):
        # 裸 * 转实体：不参与 markdown 强调配对，渲染所见不变（树图 * 节点）
        seg = '<table><tr><td>a</td><td>*</td><td><em>i</em></td><td>*</td></tr></table>'
        out = _sanitize_table_html(seg, slug='t')
        self.assertNotIn('*', out)
        self.assertIn('&#42;', out)
        self.assertEqual(out.count('&#42;'), seg.count('*'))

    def test_render_chain_no_orphan_close(self):
        # 全链：嵌套表透传经 inline_to_md 后不产生「字面 <em> + 真闭合」错配
        html = ('<table><tr><td>outer</td>'
                '<td>inner<table><tr><td><em>B</em>\\<em>A</em></td></tr></table></td>'
                '</tr></table>')
        text = inline_to_md(html, slug='t')
        # 反斜杠保住且后面直接跟真 em 开标签
        self.assertIn('\\\\<em>A</em>', text)
        # 开闭 em 数量平衡（无孤儿闭合）
        self.assertEqual(text.count('<em>'), text.count('</em>'))


if __name__ == '__main__':
    unittest.main()

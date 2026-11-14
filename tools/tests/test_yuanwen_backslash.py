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

from tools.yuanwen import _sanitize_table_html, inline_to_md  # noqa: E402


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

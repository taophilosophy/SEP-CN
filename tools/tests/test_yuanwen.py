# -*- coding: utf-8 -*-
"""yuanwen 转换器单测：行内净化、引用注释、in_bib 边界（演示轮 2 复核）。"""
import os
import re
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.yuanwen import (  # noqa: E402
    build_cite_keys, extract_blocks_raw, inline_to_md, link_citations,
    protect_cross_block_math, render_blocks, restore_cross_block_math,
    strip_closed_comments, Ctx)


class TestInline(unittest.TestCase):
    def test_sub_sup_clean_text(self):
        # 用户 2026-10-27：禁止 HTML 标签——sub/sup 转纯文本记法
        self.assertEqual(inline_to_md('P<sub>H</sub>(E)'), 'P_{H}(E)')
        self.assertEqual(inline_to_md('3<sup>rd</sup> century'), '3^{rd} century')
        self.assertNotIn('<sub>', inline_to_md('V<sub>alpha</sub>'))

    def test_math_entities_decoded(self):
        out = inline_to_md(r'\(\beta &lt; \alpha\)')
        self.assertNotIn('&lt;', out)
        # 用户 2026-10-27：数学定界符统一为 LaTeX（$…$）
        self.assertIn('$\\beta < \\alpha$', out)

    def test_note_ref_prefixed_anchor(self):
        # bell-theorem 的锚是 notes.html#note-8（自带前缀），不得双重化
        out = inline_to_md('x<sup>[<a href="notes.html#note-8" id="ref-8">8</a>]</sup>', slug='s')
        self.assertEqual(out, 'x[^note-8]')
        self.assertNotIn('note-note', out)

    def test_display_math_gap_block(self):
        # 展示公式 \[…\] 常不带 <p> 标签，块间裸文本须收为 p 块
        blocks = extract_blocks_raw('<p>text before</p> \\[\\tag{27} x = y\\] <p>after</p>')
        kinds = [b['type'] for b in blocks]
        self.assertEqual(kinds.count('p'), 3)
        ctx = Ctx('t')
        render_blocks(blocks, ctx)
        self.assertIn('tag{27}', '\n'.join(ctx.out))

    def test_note_ref_and_links(self):
        out = inline_to_md('x<sup>[<a href="notes.html#1">1</a>]</sup>', slug='s')
        self.assertEqual(out, 'x[^note-1]')
        out = inline_to_md('<a href="basic.html">Supp</a>', slug='q')
        self.assertEqual(out, '[Supp](q.basic.md)')
        out = inline_to_md('<a href="../other/">o</a>')
        self.assertEqual(out, 'o')


class TestBlocks(unittest.TestCase):
    def test_preamble_rendered(self):
        blocks = extract_blocks_raw(
            '<div id="preamble"><p>Intro paragraph here.</p></div>'
            '<p>body</p>')
        ctx = Ctx('t')
        render_blocks(blocks, ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('Intro paragraph here.', text)

    def test_in_bib_resets_at_next_heading(self):
        blocks = extract_blocks_raw(
            '<h2><a id="Bib">Bibliography</a></h2>'
            '<ul><li>Entry One 2001, Book.</li></ul>'
            '<h2>Other Internet Resources</h2>'
            '<p>[Please contact the author.]</p>'
            '<h2>Related Entries</h2>'
            '<p>related stuff here</p>')
        ctx = Ctx('t')
        render_blocks(blocks, ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('Please contact the author', text)
        self.assertIn('related stuff here', text)
        self.assertEqual([e for e in ctx.bib_entries if 'Entry One' in e],
                         ['Entry One 2001, Book.'])


class TestCitations(unittest.TestCase):
    def test_acronym_krs(self):
        keys = build_cite_keys(['Kirk, G. S., Raven, J. E. and Schofield, M., '
                                '(eds.), 1983, The Presocratic Philosophers.'])
        group = '(Guthrie 1962, 341; KRS 1983, 339)'
        new, n, used = link_citations(group, keys)
        self.assertIn('[^kirk-1983]', new)

    def test_initials_filtered(self):
        keys = build_cite_keys(['Zhmud, L., 2012a, Pythagoras and the Early Pythagoreans.'])
        self.assertEqual(keys[0]['key'], 'zhmud-2012a')
        self.assertTrue(any('Zhmud' in p.pattern for p in keys[0]['pats']))

    def test_yearless_entry_kept(self):
        # 无年份文献条目（版本卷次引用）不得整条丢弃，否则条内公式随之消失
        keys = build_cite_keys(['Leibniz, G.W., Sämtliche Schriften und Briefe, '
                                'Berlin: Akademie Verlag; abbreviated [A].'])
        self.assertEqual(len(keys), 1)
        self.assertTrue(keys[0]['key'].startswith('leibniz-nd'))
        self.assertEqual(keys[0]['pats'], [])


class TestMathFidelity(unittest.TestCase):
    """2026-10-27 数学保真裁定的回归测试（全量抓取轮发现的丢失路径）。"""

    def test_extract_keeps_tagless_content(self):
        # 无任何块级标签的内容不得整体丢弃（bohr-correspondence 引文案例）
        blocks = extract_blocks_raw('plain quote with \\(m = 0\\) math')
        text = '\n'.join(inline_to_md(b['inner'], 't') for b in blocks)
        self.assertIn('m = 0', text)

    def test_blockquote_keeps_gap_math_and_lists(self):
        # 引文块内 p 间裸展示公式与无 <p> 包装列表项不得丢弃
        html = ('<p>given by</p>\\[\\tau_1 = x\\]<p>after</p>'
                '<ul><li>plain li with \\(y\\)</li></ul>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('$$\\tau_1 = x$$', text)
        self.assertIn('plain li with $y$', text)

    def test_figure_keeps_caption_formula(self):
        # SEP 常把表格+图注包进 div.figure；图注公式不得丢
        html = ('<div class="figure"><table><tr><td>\\(a\\)</td></tr></table>'
                '<p><span class="figlabel">Table 2:</span> a \\(2 \\times 2\\) table</p></div>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('2 \\times 2', text)

    def test_nested_table_cells_not_lost(self):
        # 嵌套表：非贪婪 td 匹配曾被内层 </td> 截断，外层单元格内容丢失
        html = ('<table><tr><td>outer</td>'
                '<td>inner<table><tr><td>x</td><td>y</td></tr></table></td>'
                '<td>\\(z\\)</td></tr></table>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('outer', text)
        self.assertIn('x', text)
        self.assertIn('$z$', text)

    def test_cross_block_display_math(self):
        # 横跨块级标签的展示公式整体保护，不腰斩；还原保持原始字节（零信任保真）
        region, stash = protect_cross_block_math('<p>\\[a <p>b\\]</p>')
        self.assertEqual(len(stash), 1)
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(region), ctx)
        text = restore_cross_block_math('\n'.join(ctx.out), stash)
        self.assertIn('$$a <p>b$$', re.sub(r'\s+', ' ', text))

    def test_pdf_comment_toggles_stripped(self):
        # SEP 的 <!--pdf include <table>…--> 注释开关不参与切块，注释内容丢弃
        html = ('<div class="figure">'
                '<!--pdf include <table id="x"><tr><td>pdf</td></tr></table> pdf include-->'
                '<p>caption \\(c\\)</p></div>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(strip_closed_comments(html)), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('$c$', text)
        self.assertNotIn('pdf', text)


if __name__ == '__main__':
    unittest.main()

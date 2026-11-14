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
        # 用户 2026-10-27：禁止 HTML 标签；2026-10-28 裁定：有原生 Unicode 字形
        # 直接用原生字符，无原生字形（大写下标 H、q 下标等）保持记号
        self.assertEqual(inline_to_md('P<sub>H</sub>(E)'), 'P_{H}(E)')
        self.assertEqual(inline_to_md('3<sup>rd</sup> century'), '3ʳᵈ century')
        self.assertEqual(inline_to_md('V<sub>alpha</sub>'), 'Vₐₗₚₕₐ')
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

    def test_subsup_native_unicode(self):
        # 用户 2026-10-28 裁定：上下标优先 Unicode 原生字符
        self.assertEqual(inline_to_md('u(a<sub>1</sub>)'), 'u(a₁)')
        self.assertEqual(inline_to_md('x<sup>2</sup>'), 'x²')
        self.assertEqual(inline_to_md('S<sub>x</sub>'), 'Sₓ')
        self.assertEqual(inline_to_md('v<sub>max</sub>'), 'vₘₐₓ')
        self.assertEqual(inline_to_md('X<sup>T</sup>'), 'Xᵀ')
        self.assertEqual(inline_to_md('E<sup>−1</sup>'), 'E⁻¹')
        # 无原生字形（q 下标、⊥ 上标、斜线）→ 保持记号，站点渲染层兜底
        self.assertEqual(inline_to_md('E<sub>q</sub>'), 'E_{q}')
        self.assertEqual(inline_to_md('a<sup>⊥</sup>'), 'a^{⊥}')
        self.assertEqual(inline_to_md('(x<sup>2</sup>)<sup>−1/2</sup>'), '(x²)^{−1/2}')
        # 含强调/标签的内容不可映射 → 保持记号
        self.assertEqual(inline_to_md('<sub><i>x</i></sub>'), '_{*x*}')

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

    def test_em_with_trailing_star_escaped(self):
        # 2026-11-14 全量回归：记号 <em>W*</em> / <em>L**</em> 旧式直包产出
        # *W** / *L***，斜体不闭合、末星被吃（40 词条 183 处）
        self.assertEqual(inline_to_md('<em>W*</em>'), '*W\\**')
        self.assertEqual(inline_to_md('<em>L**</em>'), '*L\\*\\**')
        self.assertEqual(inline_to_md('laws, <em>L*</em>, of nature'),
                         'laws, *L\\**, of nature')
        # 不含星号时行为不变
        self.assertEqual(inline_to_md('<em>abductive </em>ones'),
                         '*abductive* ones')


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

    def test_comma_style_citation_linked(self):
        # 2026-11-14 全量回归：SEP 正文通行「姓, 年份」带逗号式，旧匹配式
        # 卡在逗号上（124 条词条 cite_markers=0），此处锁定修复
        keys = build_cite_keys(['Opoku, K. A., 1978, West African Traditional Religion.'])
        new, n, used = link_citations('(Opoku, 1978: 152)', keys)
        self.assertIn('[^opoku-1978]', new)
        self.assertEqual(n, 1)

    def test_group_with_several_citations(self):
        keys = build_cite_keys(['Gbadegesin, Segun, 1991, African Philosophy.',
                                'Opoku, K. A., 1978, West African Traditional Religion.'])
        new, n, used = link_citations('(Gbadegesin, 1991: 45; Opoku 1978: 152)', keys)
        self.assertIn('[^gbadegesin-1991]', new)
        self.assertIn('[^opoku-1978]', new)
        self.assertEqual(n, 2)

    def test_semicolon_blocks_cross_match(self):
        # 分号仍是引证边界：A 的作者不得与 B 的年份配成一条
        keys = build_cite_keys(['Smith, A., 1990, Book One.'])
        new, n, used = link_citations('(Smith, 1990; Jones, 1991)', keys)
        self.assertEqual(n, 1)
        new2, n2, _ = link_citations('(Smith, 1999; Jones, 1991)', keys)
        self.assertEqual(n2, 0)


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

    def test_figure_caption_not_duplicated(self):
        # 2026-11-14 全量回归（缺陷三）：图注曾被摘出到块首另行成行，正文里的
        # 同一段文字仍在，致图注成对重复（logic-preference 等 198 词条）
        html = ('<div class="figure" id="f1"><p><strong>Theory A</strong></p>'
                '<p class="center"><span class="figlabel">Figure 1.</span></p></div>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        text = '\n'.join(ctx.out)
        self.assertEqual(text.count('Figure 1.'), 1, text)
        self.assertLess(text.index('Theory A'), text.index('Figure 1.'))

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


class TestAuditFixes20261113(unittest.TestCase):
    """specs/018 逐段审计发现的三类系统性转换缺陷的回归测试。"""

    def test_em_boundary_spaces_moved_outside(self):
        # em 内尾随空格是词间分隔，strip 后粘字（abduction §1.1 *abductive*ones）
        self.assertEqual(inline_to_md('<em>abductive </em>ones'), '*abductive* ones')
        self.assertEqual(inline_to_md('a<em> x</em>b'), 'a *x*b')
        self.assertEqual(inline_to_md('<strong>word </strong>next'), '**word** next')
        # 干净内容行为不变
        self.assertEqual(inline_to_md('<em>x</em>'), '*x*')
        # 空内容降级为纯空白，不产空星对
        self.assertEqual(inline_to_md('a<em> </em>b'), 'a b')

    def test_b_tag_bold_preserved(self):
        # <b> 旧无转换规则、被兜底剥标签丢加粗（abduction 书目 Peirce [CP] 条）
        self.assertEqual(inline_to_md('Peirce, C. S. [<b>CP</b>]'), 'Peirce, C. S. [**CP**]')
        self.assertEqual(inline_to_md('<b>P</b>(<em>H</em>)'), '**P**(*H*)')
        # 星交错复杂内容维持既有降级路径（无星流奇偶错乱）
        self.assertEqual(inline_to_md('<b><em>x</em>+1</b>'), '*x*+1')

    def test_blockquote_br_keeps_line_structure(self):
        # 引块内三行逻辑图式不得并行成单行（abduction §1.1 两处）
        html = ('<blockquote><p>All <i>A</i>s are <i>B</i>s.<br />'
                '<i>a</i> is an <i>A</i>.<br />Hence, <i>a</i> is a <i>B</i>.</p></blockquote>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        self.assertIn('> All *A*s are *B*s.\n> *a* is an *A*.\n> Hence, *a* is a *B*.',
                      '\n'.join(ctx.out))

    def test_blockquote_br_bare_text_lines(self):
        # 无 <p> 包装的引块裸文本同样保行结构（abduction 佛兰德图式）
        html = '<blockquote>96 per cent speak Dutch and French.<br />Louise is Flemish.</blockquote>'
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        self.assertIn('> 96 per cent speak Dutch and French.\n> Louise is Flemish.',
                      '\n'.join(ctx.out))

    def test_br_keeps_nbsp_indentation(self):
        # &nbsp;（\xa0）是诗行/书信缩进的正文内容，不得随 <br> 一并吞掉
        html = '<blockquote><p>line one,&nbsp;&nbsp;Thou<br />&nbsp;&nbsp;next line</p></blockquote>'
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        self.assertIn('> line one,\xa0\xa0Thou\n> \xa0\xa0next line', '\n'.join(ctx.out))

    def test_br_outside_blockquote_unchanged(self):
        # 非引块上下文 <br> 行为不变（最小爆炸半径）；表格/列表容器区内亦然
        self.assertEqual(inline_to_md('a<br />b'), 'a b')
        html = '<blockquote><ul><li>a<br />b</li></ul></blockquote>'
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        self.assertIn('- a b', '\n'.join(ctx.out))


class TestAuditFixes20261113Late(unittest.TestCase):
    """abhidharma 词条审计追加的两类系统性缺陷（specs/018）。"""

    def test_uppercase_year_suffix_kept_in_key(self):
        # 1992A/2004B 旧正则只认小写后缀，键退化为 gethin-nd / cox-nd-2
        keys = build_cite_keys(['Gethin, R., 1992A, The Buddhist Path to Awakening, Leiden: Brill.'])
        self.assertEqual(keys[0]['key'], 'gethin-1992a')
        keys = build_cite_keys(['Cox, C., 2004B, “Mainstream Buddhist Schools,” in Encyclopedia.'])
        self.assertEqual(keys[0]['key'], 'cox-2004b')

    def test_notes_page_title_dropped(self):
        # notes.html 自带 <h2>Notes to X</h2>，正文侧已有「## Notes（原文脚注）」
        from tools.yuanwen import convert_notes
        html = ('<!-- BEGIN ARTICLE HTML -->'
                '<h2>Notes to Abhidharma</h2>'
                '<div id="note-1"><p>First note body.</p></div>'
                '<!-- END ARTICLE HTML -->')
        defs = convert_notes(html, 'abhidharma')
        self.assertEqual(len(defs), 1)
        self.assertTrue(defs[0].startswith('[^note-1]: First note body.'))
        self.assertNotIn('Notes to', '\n'.join(defs))


class TestGuardRails(unittest.TestCase):
    """上游噪声与公式护栏边界（ADR-0016 一致性收口补测）。"""

    def test_double_escaped_entity_carried_once(self):
        # D17：上游双重转义实体单次解码后忠实带过，不得残留 &amp; 前缀
        out = inline_to_md('the author&rsquo;s &amp;rsquo; note')
        self.assertNotIn('&amp;', out)
        self.assertIn('&rsquo;', out)

    def test_unclosed_p_does_not_swallow_sections(self):
        # D16：上游漏写 </p> 时 p 按隐式闭合，余下分节不得被吞成一个块
        blocks = extract_blocks_raw(
            '<p>para without close.'
            '<h2><a id="s1">1. First Section</a></h2>'
            '<p>section one body.</p>'
            '<h2><a id="s2">2. Second Section</a></h2>'
            '<p>section two body.</p>')
        ctx = Ctx('t')
        render_blocks(blocks, ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('para without close.', text)
        self.assertIn('section one body.', text)
        self.assertIn('section two body.', text)


class TestNestedTables20261114(unittest.TestCase):
    """specs/018 转换器战役：嵌套表原样 HTML 透传 + li/dd 内表真表渲染
    （020 移交缺陷：嵌套降级 16 件/128 处、li/dd 吞表 10 件/41 表）。"""

    def test_nested_table_html_passthrough(self):
        # 单元格内嵌套公式盒：原样 HTML 透传，不再降级为「（嵌套表：…）」
        html = ('<table><tr><td>outer</td>'
                '<td>inner<table><tr><td>x</td><td>y</td></tr></table></td>'
                '<td>\\(z\\)</td></tr></table>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('<table>', text)
        self.assertNotIn('（嵌套表：', text)
        # 内层数学定界符随行内约定转 $（消毒步骤之一）
        self.assertIn('$z$', text)

    def test_nested_table_sanitized(self):
        # 消毒：font 剥壳保内容；\(\)→$；|→&#124;；压成单行
        html = ('<table><tr><td>'
                '<table><tr><td><font size="+2">|</font></td>'
                '<td>\\(a &lt; b\\)</td></tr></table>'
                '</td></tr></table>')
        out = inline_to_md('<td>' + html + '</td>', slug='t')
        self.assertNotIn('<font', out)
        self.assertIn('&#124;', out)
        self.assertNotIn(' <table', out.replace('&lt;', 'LT'))
        # 单行化：段内无换行
        self.assertNotIn('\n<table', out)

    def test_nested_table_img_src_rewritten(self):
        html = ('<table><tr><td><table><tr>'
                '<td><img src="triangle-s-dagger.jpg" alt="x" /></td>'
                '</tr></table></td></tr></table>')
        out = inline_to_md(html, slug='t')
        self.assertIn('../assets/t/triangle-s-dagger.jpg', out)

    def test_li_table_indented_md_table(self):
        # 列表项内嵌真表：内容列缩进的 md 表，不再剥壳降为裸文本
        html = ('<ul><li>rule text'
                '<table><tr><td>a</td><td>b</td></tr>'
                '<tr><td>1</td><td>2</td></tr></table>'
                'trailing</li></ul>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('- rule text', text)
        self.assertIn('\n  | a | b |', text)
        self.assertIn('\n  | --- | --- |', text)
        self.assertIn('\n\n  trailing', text)
        self.assertNotIn('<table', text)

    def test_dd_table_emitted(self):
        # dd 内嵌真表：文本段与表段按序完整转出
        html = ('<dl><dt>term</dt><dd>def text'
                '<table><tr><td>x</td></tr></table>'
                'after</dd></dl>')
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(html), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('def text', text)
        self.assertIn('| x |', text)
        self.assertNotIn('<table', text)

    def test_table_to_md_accepts_full_table_html(self):
        # 容错剥壳：传入含外层 <table> 标签的完整表 HTML 不得自吞成哨兵
        out = render_one_table('<table><tr><td>a</td></tr></table>')
        self.assertIn('| a |', out)

    def test_bib_li_table_kept(self):
        # 书目列表项内嵌表：引用定义里原样保留（saadya 4 件实证）
        from tools.yuanwen import build_cite_keys
        bib_p = '<h2>References</h2><ul><li>Author, <i>Book</i>' \
                '<table><tr><td>(a)</td><td>edition one</td></tr></table></li></ul>'
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw(bib_p), ctx)
        keys = build_cite_keys(ctx.bib_entries)
        self.assertTrue(any('<table>' in k['text'] for k in keys),
                        '书目条目内的表不得丢失')


def render_one_table(full_html):
    from tools.yuanwen import table_to_md
    return table_to_md(full_html, 't')


if __name__ == '__main__':
    unittest.main()

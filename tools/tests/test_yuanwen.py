# -*- coding: utf-8 -*-
"""yuanwen 转换器单测：行内净化、引用注释、in_bib 边界（演示轮 2 复核）。"""
import os
import re
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.yuanwen import (  # noqa: E402
    _drop_duplicate_h1, _escape_leading_hash, build_cite_keys,
    extract_blocks_raw, inline_to_md, link_citations,
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

    def test_nested_math_in_env_no_sentinel_leak(self):
        # logic-intensional 判例（2026-11-25）：裸排 align 里 \mbox{… \(f\) …}
        # 的内层行内公式占位在环境还原后才出现，必须二次清扫——否则 NUL 哨兵
        # 泄漏进 md（实测 12 处，一路污染译文）。
        html = (r'\begin{align} \cM \vDash_{v} \forall fX & '
                r'\mbox{for every \(f\)-variant \(w\) of \(v\)} \end{align}')
        out = inline_to_md(html)
        self.assertNotIn('\x00', out)
        # 2026-11-26 裁定改判：环境体内的 `\(…\)` 是公式原文（全库 21 件 84
        # 处），转 `$…$` 与 H0 文字流不等（B3.2 判 gap）——保持字面
        self.assertIn('\\(f\\)-variant \\(w\\)', out)
        self.assertNotIn('$f$', out)

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
        # *W** / *L***，斜体不闭合、末星被吃（40 词条 183 处）
        self.assertEqual(inline_to_md('<em>W*</em>'), '*W\\**')
        self.assertEqual(inline_to_md('<em>L**</em>'), '*L\\*\\**')
        self.assertEqual(inline_to_md('laws, <em>L*</em>, of nature'),
                         'laws, *L\\**, of nature')
        # 不含星号时行为不变
        self.assertEqual(inline_to_md('<em>abductive </em>ones'),
                         '*abductive* ones')

    def test_em_with_attributes_keeps_italics(self):
        # 2026-11-14 全量回归（缺陷六）：带属性的 em 旧式只认裸 <em>，
        # 标签被兜底剥除、斜体静默丢失（全库 2568 文件 37898 处）
        self.assertEqual(inline_to_md('<em lang="zh-Latn-pinyin">dao</em> 道'),
                         '*dao* 道')
        self.assertEqual(
            inline_to_md('<em style="text-indent:-2em">The Variation</em>, two volumes'),
            '*The Variation*, two volumes')


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
        # 2026-11-15 起条目为 (text, section) 二元组
        self.assertEqual([e[0] for e in ctx.bib_entries if 'Entry One' in e[0]],
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

    def test_name_outside_parens_linked(self):
        # 2026-11-14 续查：SEP 亦通行「姓 (年份)」式，姓名在括号之外，
        # 旧式只在括号内找姓名，整类永不命中（55 条词条零键标之主因）
        keys = build_cite_keys(['van der Kuijp, Leonard W.J., 1989, Review.'])
        new, n, used = link_citations('Following van der Kuijp (1989) one can', keys)
        self.assertIn('(1989)[^kuijp-1989]', new)
        self.assertEqual(n, 1)

    def test_name_outside_parens_needs_year_only(self):
        # 括号内含散文时不得借括号外的姓名挂键
        keys = build_cite_keys(['Smith, A., 1990, Book One.'])
        new, n, _ = link_citations('Smith (as everyone agrees, 1990) said', keys)
        self.assertEqual(n, 0)

    def test_bare_year_without_name_not_linked(self):
        # 括号外无紧邻姓名的裸年份不挂键
        keys = build_cite_keys(['Smith, A., 1990, Book One.'])
        new, n, _ = link_citations('He wrote in (1990) that Smith agreed', keys)
        self.assertEqual(n, 0)

    def test_year_leading_entry_ignores_section_by_default(self):
        # 2026-11-26（specs/053 第五十批）：默认不再向小节标题推断作者——键名须能由
        # md 确定性复算；无 fallback_author 时该条照旧丢弃（无键可建）
        keys = build_cite_keys([("1913, “On the constitution of atoms and molecules,”",
                                 "Works by Bohr")])
        self.assertEqual(keys, [])
        keys = build_cite_keys([("1913, “On the constitution of atoms and molecules,”",
                                 "Works by Bohr")], fallback_author='bohr-correspondence')
        self.assertEqual(keys[0]['key'], 'bohr-correspondence-1913')

    def test_year_leading_entry_section_author_when_section_free_off(self):
        # 旧行为（section_free=False）保留为对照：小节标题「Works by X」推断作者
        keys = build_cite_keys([("1913, “On the constitution of atoms and molecules,”",
                                 "Works by Bohr")], section_free=False)
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys[0]['key'], 'bohr-1913')
        new, n, _ = link_citations('(Bohr 1913, p. 4)', keys)
        self.assertIn('[^bohr-1913]', new)
        self.assertEqual(n, 1)
        keys = build_cite_keys([("1946, “A Functional Calculus of First Order”",
                                 "Ruth Barcan Marcus’s Works")], section_free=False)
        self.assertEqual(keys[0]['key'], 'marcus-1946')

    def test_year_leading_entry_without_section_still_dropped(self):
        keys = build_cite_keys([("1913, “On the constitution of atoms and molecules,”")])
        self.assertEqual(keys, [])

    def test_name_outside_parens_with_page(self):
        keys = build_cite_keys(['Lazarus, R. S., 1991, Emotion and Adaptation.'])
        new, n, _ = link_citations('(see Lazarus (1991, 122) for the list)', keys)
        self.assertIn('(1991, 122)[^lazarus-1991]', new)
        self.assertEqual(n, 1)


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

    def test_h5_heading_rendered(self):
        # 2026-11-14 全量回归（缺陷七）：BLOCK_OPEN_RE 与渲染分支都不认 h5，
        # SEP 用 <h5> 标末级小节（object 的「束理论」「裸殊相论」等 331 处），
        # 旧式整行落入正文成裸段落。
        ctx = Ctx('t')
        render_blocks(extract_blocks_raw('<h4>2.1 x</h4><p>body</p>'
                                         '<h5>Bundle theory</h5><p>y</p>'), ctx)
        text = '\n'.join(ctx.out)
        self.assertIn('##### Bundle theory', text)

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
        # 2026-11-21 结构化重构：嵌套不再降级丢加粗——<b> 套 <em> 照发异类定界符
        # （旧期望 '*x*+1' 是 [^<]* 失配后外 <b> 被兜底剥壳的丢失形态）
        self.assertEqual(inline_to_md('<b><em>x</em>+1</b>'), '***x*+1**')
        # 同类嵌套压平（保外层；内层标签归 B3.2 格式层池）
        self.assertEqual(inline_to_md('<em>a<em>b</em>c</em>'), '*abc*')
        self.assertEqual(inline_to_md('<strong>a<strong>b</strong>c</strong>'),
                         '**abc**')
        # 缺闭合开标签回删定界符、孤立闭标签忽略（不产破星）
        self.assertEqual(inline_to_md('a<em>b'), 'ab')
        self.assertEqual(inline_to_md('a</em>b'), 'ab')

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


class TestAdr0049ConverterRules(unittest.TestCase):
    """ADR-0049 转换层并入（2026-11-15 用户指令）：孤立希腊字母转文字＋裸环境包 $$。"""

    def test_lone_greek_inline_to_text(self):
        self.assertEqual(inline_to_md(r'\(\omega\)-路径'), '*ω*-路径')
        self.assertEqual(inline_to_md(r'解释 \(\omega\) 与 \(\varphi\) 的距离'), '解释 *ω* 与 *φ* 的距离')
        self.assertEqual(inline_to_md(r'\(\phi\) 与 \(\varphi\) 同归'), '*φ* 与 *φ* 同归')

    def test_c_deferred_stay_formula(self):
        self.assertEqual(inline_to_md(r'\(\mu\)-演算'), r'$\mu$-演算')
        self.assertEqual(inline_to_md(r'有限字母表 \(\Sigma\)'), r'有限字母表 $\Sigma$')
        self.assertEqual(inline_to_md(r'状态集 \(\Omega\)'), r'状态集 $\Omega$')

    def test_composite_and_primed_stay_formula(self):
        self.assertEqual(inline_to_md(r'\(\neg\varphi\) 与 \(\varphi \in A\)'),
                         r'$\neg\varphi$ 与 $\varphi \in A$')
        self.assertEqual(inline_to_md(r"则 \(\omega'\) 取距 \(\omega\) 最近的那个"),
                         r"则 $\omega'$ 取距 *ω* 最近的那个")
        self.assertEqual(inline_to_md(r'\(\alpha_1\) 换成 \(\alpha\)'),
                         r'$\alpha_1$ 换成 *α*')

    def test_display_math_untouched(self):
        self.assertEqual(inline_to_md(r'\[\omega\]'), r'$$\omega$$')

    def test_naked_env_wrapped(self):
        src = (r'\begin{align}' '\n' r'f_{1}(\{0\}) &amp;= 0 \\' '\n'
               r'f_{1}(\{1\}) &amp;= 1' '\n' r'\end{align}')
        expect = r'$$\begin{align} f_{1}(\{0\}) &= 0 \\ f_{1}(\{1\}) &= 1 \end{align}$$'
        self.assertEqual(inline_to_md(src), expect)

    def test_env_already_in_display_delims_not_rewrapped(self):
        self.assertEqual(inline_to_md(r'\[\begin{align} x &= 1 \end{align}\]'),
                         r'$$\begin{align} x &= 1 \end{align}$$')
        self.assertEqual(inline_to_md(r'$$\begin{align} x &= 1 \end{align}$$'),
                         r'$$\begin{align} x &= 1 \end{align}$$')

    def test_prose_with_env_and_inline(self):
        src = r'若 \(\Delta\) 为算子，则 \begin{gather} a \\ b \end{gather} 成立'
        out = inline_to_md(src)
        self.assertIn(r'$\Delta$', out)
        self.assertIn('$$\\begin{gather}', out)


class TestNakedEnvGuard(unittest.TestCase):
    """R2 裸排环境包裹守卫（ADR-0049 决策 6）：只包数学之外的裸环境。

    回归背景（2026-11-16）：SEP 输出 `$$ \begin{align}…\end{align} $$`（相隔空格）
    曾被紧邻 lookaround 漏判 → 双重包裹；数学**内部**的环境也被再包一层 →
    页面 MathJax 报 “Extra close brace or missing open brace”（真页面实测）。
    """

    def _wrap(self, s):
        from tools.yuanwen import wrap_naked_envs
        return wrap_naked_envs(s)

    def test_already_delimited_with_space_untouched(self):
        s = '$$ \\begin{align} a &= b \\end{align} $$'
        self.assertEqual(self._wrap(s), s)

    def test_bare_env_wrapped(self):
        s = '\\begin{align} a &= b \\end{align}'
        self.assertEqual(self._wrap(s), '$$' + s + '$$')

    def test_already_delimited_adjacent_untouched(self):
        s = '$$\\begin{align} a \\end{align}$$'
        self.assertEqual(self._wrap(s), s)

    def test_no_double_dollar_created(self):
        s = '$$ \\begin{gather} x \\end{gather} $$'
        self.assertEqual(self._wrap(s).count('$$'), 2)

    def test_env_inside_display_untouched(self):
        # hempel 形态：\frac{} 里的 gathered 属数学内部，包了即报错
        s = '$$ \\frac{\\begin{gathered} x \\\\ y \\end{gathered}}{\\neg Rc} $$'
        self.assertEqual(self._wrap(s), s)

    def test_env_inside_inline_dollar_untouched(self):
        # negation 形态：单 $ 内的 align* 渲染正常，不得改写
        s = '$\\begin{align*} A \\vdash B \\end{align*}$'
        self.assertEqual(self._wrap(s), s)

    def test_bare_env_after_closed_display_wrapped(self):
        s = '$$ a $$\n\n\\begin{align} b \\end{align}'
        self.assertEqual(self._wrap(s), '$$ a $$\n\n$$\\begin{align} b \\end{align}$$')



def render_one_table(full_html):
    from tools.yuanwen import table_to_md
    return table_to_md(full_html, 't')


class TestTitleDedupeAndHashEscape20261117(unittest.TestCase):
    """specs/039 P5 尾：双重题名守卫漏判（旧模板图先于题）与行首字面 #。

    判例：russell 等 30 件 `^# ` 双题；disjunction 例句 dd 里上游字面
    `# Absolument! …`（(31) 为紧贴 `#Absolument`）落行首成伪 H1。
    """

    def test_same_text_body_h1_dropped(self):
        md = '# T\n\n*Author*\n\n![img]\n\n*cap*\n\n# T\n\n**First published**'
        self.assertEqual(
            _drop_duplicate_h1(md),
            '# T\n\n*Author*\n\n![img]\n\n*cap*\n\n**First published**')

    def test_different_text_h1_untouched(self):
        # 异文禁静默丢文：原样返回，交重转 diff 复核兜底
        md = '# T\n\nbody\n\n# Other'
        self.assertEqual(_drop_duplicate_h1(md), md)

    def test_single_h1_untouched(self):
        md = '# T\n\nbody'
        self.assertEqual(_drop_duplicate_h1(md), md)

    def test_fence_hash_not_counted(self):
        md = '# T\n\n```sh\n# not a heading\n```\n\n# T\n\ntail'
        out = _drop_duplicate_h1(md)
        self.assertEqual(out.count('# T'), 1)  # 围栏外的第二个题名被删
        self.assertIn('# not a heading', out)  # 围栏内原样

    def test_dd_leading_hash_escaped(self):
        ctx = Ctx('disjunction')
        blocks = extract_blocks_raw('<dl class="sentag"><dt>b.</dt>'
                                    '<dd># Absolument! Et elle ira.</dd></dl>')
        render_blocks(blocks, ctx)
        self.assertIn('\\# Absolument! Et elle ira.', '\n'.join(ctx.out))

    def test_year_leading_entries_kept_with_fallback(self):
        # specs/039 I3 标定（sartre 判例）：主文献区节首年份起首条目（作者＝条目
        # 主体本人）在 prev_surnames 为空时旧式整条 continue＝文献蒸发。
        # fallback_author 兜底键保定义行；不带 fallback 时旧行为保留（禁静默变卦）。
        entries = ['1936a, *La Transcendance de l’ego*, Paris: J. Vrin.',
                   '1936b [2012], *L’imagination*, Paris: F. Alcan.',
                   'Sartre, Jean-Paul, 1943, *L’être et le néant*, Paris: Gallimard.']
        keys = build_cite_keys(entries)
        self.assertEqual(len(keys), 1)  # 旧口径：前两条蒸发
        keys_fb = build_cite_keys(entries, fallback_author='sartre')
        self.assertEqual(len(keys_fb), 3)
        self.assertEqual(keys_fb[0]['key'], 'sartre-1936a')
        self.assertEqual(keys_fb[1]['key'], 'sartre-1936b')
        self.assertEqual(keys_fb[2]['key'], 'sartre-1943')
        self.assertNotIn('pats-hit', str(keys_fb[0]))  # 兜底键不强生文内标记

    def test_fallback_not_used_when_surnames_resolvable(self):
        entries = ['Sartre, Jean-Paul, 1943, *L’être et le néant*.',
                   '1936a, *La Transcendance de l’ego*.']
        keys = build_cite_keys(entries, fallback_author='sartre')
        self.assertEqual([k['key'] for k in keys], ['sartre-1943', 'sartre-1936a'])
        # 第二条继承前条姓氏（既有语义），不走 fallback
        self.assertEqual(keys[1]['pats'] != [], True)

    def test_hash_tight_no_space_escaped(self):
        ctx = Ctx('disjunction')
        blocks = extract_blocks_raw('<p>#Absolument! Et ils étudient même les deux.</p>')
        render_blocks(blocks, ctx)
        self.assertIn('\\#Absolument', '\n'.join(ctx.out))

    def test_escape_leading_hash_non_hash_untouched(self):
        self.assertEqual(_escape_leading_hash('普通正文'), '普通正文')
        self.assertEqual(_escape_leading_hash(''), '')


    def test_continued_led_section_uses_fallback(self):
        # specs/039 D1（ibn-bajja 判例）：小节首条即续行、节内无可继承姓氏时，
        # 旧式整节 continue（889/926 字母蒸发）；兜底键保定义行
        keys = build_cite_keys(['———, 1976, Ta’liqat fi Kitab Bari Arminiyas.'],
                               fallback_author='ibn-bajja')
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys[0]['key'], 'ibn-bajja-1976')
        self.assertIn('Ta’liqat', keys[0]['text'])

    def test_continued_led_section_uses_section_author(self):
        # 有节标题时优先用节名（「Works by Bohr」），兜底键只在无节名时登场
        keys = build_cite_keys([('———, 1934, Atomic Theory.', 'Works by Bohr')],
                               fallback_author='bohr')
        self.assertEqual(keys[0]['key'], 'bohr-1934')

    def test_abbrev_bare_name_kept_as_nd_entry(self):
        # 缩写表裸姓名条目（无年份、无内容）旧式整条丢弃 → H0 的 li 在产物
        # 缺席（leibniz-ethics 判例）。2026-11-23 改判：照常建 -nd 键保定义行，
        # 无年份即无 pats，不会挂文内标记——保真优先级：文字是本体重名是辅助物。
        keys = build_cite_keys(['Descartes, René', 'Leibniz, G. W.'])
        self.assertEqual([k['key'] for k in keys], ['descartes-nd', 'leibniz-nd'])
        self.assertTrue(all(not k['pats'] and not k['pre'] for k in keys))
        self.assertEqual(keys[0]['text'], 'Descartes, René')


class TestDlGaps(unittest.TestCase):
    """specs/039 D2（al-khunaji 判例）：`<dd>` 内嵌 `<dl>` 截断后，外层尾随
    `<p>` 段落落在 match 间隙，旧式静默丢弃。"""

    def _render(self, inner):
        ctx = Ctx('probe')
        render_blocks([{'type': 'dl', 'inner': inner}], ctx)
        return '\n'.join(ctx.out)

    def test_nested_dl_trailing_paragraphs_kept(self):
        inner = ('<dd>Coincidental conditional: two interpretations:'
                 '<dl class="sentag"><dt>(i)</dt><dd>weak reading.</dd>'
                 '<dt>(ii)</dt><dd>strong reading, merely coinciding.</dd></dl>'
                 '</dd></dl><p>In neither case is there any implicative relation.</p>'
                 '<p>Avicenna used both definitions of coincidental conditionals.</p></dd>'
                 '<dt>(2)</dt><dd>Disjunctive conditional.</dd>')
        out = self._render(inner)
        self.assertIn('In neither case is there any implicative relation', out)
        self.assertIn('Avicenna used both definitions', out)
        self.assertIn('Disjunctive conditional', out)

    def test_wellformed_dl_no_extra_output(self):
        out = self._render('<dt>term</dt><dd>definition</dd>')
        self.assertNotIn('定义', out)
        self.assertEqual(out.count('**term**'), 1)
        self.assertEqual(out.count('definition'), 1)

    def test_gap_with_nested_dt_not_duplicated(self):
        # 畸形件保守处理：间隙含 dt/dd 开标签则不收编（防重复输出）
        inner = ('<dd>a<dl><dt>x</dt><dd>b</dd></dl></dd><dt>orphan</dt>'
                 '<dd>c</dd>')
        out = self._render(inner)
        self.assertEqual(out.count('orphan'), 1)


class TestDlOptionalEndTags(unittest.TestCase):
    """HTML5 允许 `<dt>`／`<dd>` 省略结束标签；SEP 大量这样写。

    旧匹配式硬要 `</dt>`／`</dd>`：未闭合 `<dt>` 的文字落进含 dt/dd 的间隙被
    跳过（anaphora `(1)`），未闭合 `<dd>` 的整段文字不入 md（criminal-law
    “We control X if …”）。回归口径：文字必在、其余格式不变。
    """

    def _render(self, html):
        ctx = Ctx('probe')
        render_blocks(extract_blocks_raw(html), ctx)
        return '\n'.join(ctx.out)

    def test_unclosed_dt_keeps_text(self):
        out = self._render('<dl class="sentag tag3em">\n<dt id="ex1">(1)\n'
                           '<dd>John is down by the bank of the river.</dd>\n</dl>')
        self.assertIn('**(1)**', out)
        self.assertIn('John is down by the bank of the river.', out)

    def test_unclosed_dd_keeps_text(self):
        out = self._render('<dl class="sentag tag4em">\n<dt>(2)</dt>\n'
                           '<dd>We control \\(X\\) if we have a reasonable '
                           'chance.\n</dl>')
        self.assertIn('**(2)**', out)
        self.assertIn('reasonable chance', out)

    def test_wellformed_unchanged(self):
        # 闭合件行为不变（不重复加粗、不重复输出）
        out = self._render('<dl><dt>(a)</dt><dd>alpha</dd></dl>')
        self.assertEqual(out.count('**(a)**'), 1)
        self.assertEqual(out.count('alpha'), 1)

    def test_nested_dl_body_untouched(self):
        # 嵌套 dl 的 dd 内容含结构标签，不补尾（既有间隙逻辑接管，防回归）
        out = self._render('<dl><dt>A</dt><dd>outer<dl><dt>B</dt>'
                           '<dd>inner</dd></dl>tail</dd></dl>')
        self.assertIn('outer', out)
        self.assertIn('inner', out)
        self.assertIn('tail', out)


class TestConverterFixes20261125(unittest.TestCase):
    """2026-11-25 B3.2 缺口族修复的定点用例（逐族一例）。"""

    def test_table_last_cell_without_closing_td(self):
        # shared-agency：末格省 `</td>`，旧式 findall 整格丢字
        from tools.yuanwen import table_to_md
        md = table_to_md('<table><tr><td>a</td><td>b</td></tr>'
                         '<tr><td>Group</td><td><sub>Yes</sub>&#9586;'
                         '<sup>No</sup>\n</tr></table>', 'x')
        self.assertIn('Group', md)
        self.assertIn('_{Yes}', md)      # 上标号 No → Unicode ᴺᵒ，按可见文断言
        self.assertIn('╲', md)

    def test_textual_note_link_keeps_words(self):
        # wilhelm-humboldt：`see <a>note 6</a>` 是散文引用，须保留词语
        out = inline_to_md('see\n <a href="notes.html#note-6">note 6</a>.')
        self.assertIn('[note 6](notes.html#note-6)', out)

    def test_numeric_note_ref_stays_marker(self):
        out = inline_to_md('x.<a href="notes.html#note-3" id="ref-3">'
                           '<sup>[3]</sup></a>')
        self.assertIn('[^note-3]', out)
        self.assertNotIn('notes.html#note-3)', out)

    def test_supsub_span_unwrapped_before_emphasis_merge(self):
        # typelogical-grammar：相邻 `*a**n*` 歧义 → 提前剥壳合并为 `*an*1`
        out = inline_to_md('<em>a</em><span class="supsub"><em>n</em>'
                           '<span class="lower">1</span></span>')
        self.assertEqual(out, '*an*1')

    def test_unbalanced_paren_in_url_percent_encoded(self):
        # pufendorf：URL 内不平衡 `)` 会被 md 链接语法提前闭合
        out = inline_to_md('<a href="https://e.org/x?f=1%27)">Zedler</a>, v.')
        self.assertIn('%27%29)', out)


if __name__ == '__main__':
    unittest.main()

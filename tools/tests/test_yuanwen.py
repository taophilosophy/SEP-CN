# -*- coding: utf-8 -*-
"""yuanwen 转换器单测：行内净化、引用注释、in_bib 边界（演示轮 2 复核）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.yuanwen import (  # noqa: E402
    build_cite_keys, extract_blocks_raw, inline_to_md, link_citations, render_blocks, Ctx)


class TestInline(unittest.TestCase):
    def test_sub_sup_clean_text(self):
        # 用户 2026-10-27：禁止 HTML 标签——sub/sup 转纯文本记法
        self.assertEqual(inline_to_md('P<sub>H</sub>(E)'), 'P_{H}(E)')
        self.assertEqual(inline_to_md('3<sup>rd</sup> century'), '3^{rd} century')
        self.assertNotIn('<sub>', inline_to_md('V<sub>alpha</sub>'))

    def test_math_entities_decoded(self):
        out = inline_to_md(r'\(\beta &lt; \alpha\)')
        self.assertNotIn('&lt;', out)
        self.assertIn(r'\(\beta < \alpha\)', out)

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


if __name__ == '__main__':
    unittest.main()

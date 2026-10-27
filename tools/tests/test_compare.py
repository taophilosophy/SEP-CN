# -*- coding: utf-8 -*-
"""compare.py 段落级 diff 机制单元测试（CI: unittest discover）。"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools.compare import diff_sections, map_zh, parse_sections

HTML_TWO_SECTIONS = """<!-- BEGIN ARTICLE HTML -->
<p>导言段落。</p>
<h2><a id="sec-1">1. First Section</a></h2>
<p>第一段。</p>
<p>第二段。</p>
<h2><a id="sec-2">2. Second Section</a></h2>
<p>表格与列表内容。</p>
<!-- END ARTICLE HTML -->
"""

HTML_MODIFIED = HTML_TWO_SECTIONS.replace("第二段。", "第二段（修订版）。")
HTML_REMOVED = HTML_TWO_SECTIONS.replace('<h2><a id="sec-2">2. Second Section</a></h2>\n<p>表格与列表内容。</p>\n', "")
HTML_ADDED = HTML_TWO_SECTIONS.replace(
    '<!-- END ARTICLE HTML -->',
    '<h2><a id="sec-3">3. Third Section</a></h2>\n<p>新节内容。</p>\n<!-- END ARTICLE HTML -->')


class TestParseSections(unittest.TestCase):
    def test_intro_and_sections(self):
        secs = parse_sections(HTML_TWO_SECTIONS)
        anchors = [a for a, _, _ in secs]
        self.assertEqual(anchors, ["(intro)", "sec-1", "sec-2"])
        self.assertIn("导言段落。", secs[0][2][0])
        self.assertIn("第一段。", secs[1][2])

    def test_paragraph_normalization(self):
        secs = parse_sections(HTML_TWO_SECTIONS)
        self.assertTrue(all(isinstance(p, str) and p == p.strip() for _, _, ps in secs for p in ps))


class TestDiffSections(unittest.TestCase):
    def test_no_change(self):
        old = parse_sections(HTML_TWO_SECTIONS)
        self.assertEqual(diff_sections(old, parse_sections(HTML_TWO_SECTIONS)), [])

    def test_modified_paragraph(self):
        old = parse_sections(HTML_TWO_SECTIONS)
        new = parse_sections(HTML_MODIFIED)
        changes = diff_sections(old, new)
        types = {c["type"] for c in changes}
        self.assertTrue("removed" in types and "added" in types)
        self.assertTrue(any("修订版" in c["excerpt"] for c in changes if c["type"] == "added"))
        self.assertTrue(all(c["anchor"] == "sec-1" for c in changes))

    def test_removed_section(self):
        old = parse_sections(HTML_TWO_SECTIONS)
        new = parse_sections(HTML_REMOVED)
        changes = diff_sections(old, new)
        self.assertTrue(any(c["type"] == "removed" and c["anchor"] == "sec-2" for c in changes))

    def test_added_section(self):
        old = parse_sections(HTML_TWO_SECTIONS)
        new = parse_sections(HTML_ADDED)
        changes = diff_sections(old, new)
        self.assertTrue(any(c["type"] == "added" and c["anchor"] == "sec-3" for c in changes))


class TestMapZh(unittest.TestCase):
    def test_missing_zh_doc(self):
        changes = [{"type": "added", "anchor": "sec-3", "title": "3. Third Section", "excerpt": ""}]
        out = map_zh(changes, None)
        self.assertIn("待建任务", out[0]["zh_section"])

    def test_section_mapping(self):
        import tempfile
        tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        tmp.write("# X\n\n## 3. Third Section\n\n正文。\n")
        tmp.close()
        try:
            import tools.compare as CMP
            orig = CMP.repo_path
            CMP.repo_path = lambda *p: tmp.name
            try:
                changes = [{"type": "added", "anchor": "sec-3", "title": "3. Third Section", "excerpt": ""}]
                out = map_zh(changes, "a/x.md")
                self.assertEqual(out[0]["zh_line"], 3)
            finally:
                CMP.repo_path = orig
        finally:
            os.unlink(tmp.name)


if __name__ == "__main__":
    unittest.main()

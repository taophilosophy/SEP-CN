# -*- coding: utf-8 -*-
"""en_source_audit 检查器单元测试：各检查类的硬/告警判定（ADR-0052）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import en_source_audit  # noqa: E402

PAGE = ("<!DOCTYPE html><html><head><title>t</title></head><body>"
        "<h2>一</h2><p>hello <a href=\"#sec-2\">next</a> world.</p>"
        "<h2 id=\"sec-2\">二</h2><p>Some <span>prose</span> here.</p>"
        "</body></html>")


def _run(raw, slug="audit-fixture", catalog=None):
    out = {"slug": slug, "hard": [], "warn": [], "info": [], "counts": {}}
    ids = {i for i in en_source_audit.ID_RE.findall(raw)}
    en_source_audit._check_page(raw, out)
    en_source_audit._check_links(raw, slug, ids, out, catalog)
    en_source_audit._check_math(raw, out)
    en_source_audit._check_tables(raw, out)
    en_source_audit._check_typo(en_source_audit._text_nodes(raw), out)
    return out


class TestEnSourceAudit(unittest.TestCase):
    def test_clean_page(self):
        out = _run(PAGE)
        self.assertEqual(out["hard"], [])
        self.assertEqual(out["warn"], [])

    def test_truncated_page_is_hard(self):
        out = _run(PAGE[:60])
        self.assertTrue(any(h["class"] == "truncation" for h in out["hard"]))

    def test_broken_anchor_is_hard(self):
        raw = PAGE.replace("href=\"#sec-2\"", "href=\"#nope\"")
        out = _run(raw)
        self.assertTrue(any(h["class"] == "anchor_missing" for h in out["hard"]))

    def test_math_delim_and_brace(self):
        raw = "<html><body><p>\\(x + y\\) 与 \\(z</p></body></html>"
        out = _run(raw)
        self.assertTrue(any(h["class"] == "math_delim" for h in out["hard"]))
        raw2 = "<html><body><p>\\(x^{y\\)</p></body></html>"
        out2 = _run(raw2)
        self.assertTrue(any(h["class"] == "math_brace" for h in out2["hard"]))
        # 平衡公式不报
        out3 = _run("<html><body><p>\\(x^{y}\\)</p></body></html>")
        self.assertEqual([h for h in out3["hard"] if h["class"].startswith("math")], [])

    def test_table_without_row_is_hard(self):
        raw = "<html><body><table><p>x</p></table></body></html>"
        out = _run(raw)
        self.assertTrue(any(h["class"] == "table_no_row" for h in out["hard"]))

    def test_typo_candidates_and_masks(self):
        raw = ("<html><body><p>It exists 3s a fact, Cambridh=ge, the the result, "
               "doi:10.1093/xx/exp043, MEGA1 and pp.109–130.</p></body></html>")
        out = _run(raw)
        kinds = {w.get("token") for w in out["warn"] if w.get("cls") == "typo_candidate"}
        self.assertIn("3s", kinds)
        self.assertIn("Cambridh=ge", kinds)
        self.assertIn("the the", kinds)
        self.assertTrue(any(t.startswith("pp.1") for t in kinds), kinds)
        self.assertNotIn("exp043", kinds)   # doi 掩蔽
        self.assertNotIn("MEGA1", kinds)    # 全大写缩写豁免

    def test_entry_link_catalog(self):
        raw = ("<html><body><p><a href=\"../abelard/\">x</a> "
               "<a href=\"../no-such-entry-xyz/\">y</a></p></body></html>")
        out = _run(raw, catalog={"abelard", "audit-fixture"})
        bad = [h for h in out["hard"] if h["class"] == "entry_link_bad"]
        self.assertEqual(len(bad), 1)
        self.assertIn("no-such-entry-xyz", bad[0]["msg"])


if __name__ == "__main__":
    unittest.main()

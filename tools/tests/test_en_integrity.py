# -*- coding: utf-8 -*-
"""en_integrity.py 深度复核机制单元测试（CI: unittest discover）。"""
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools.en_integrity import audit_dir, inbound_map, resolve_ref

PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8" />
<title>Alpha (Stanford Encyclopedia of Philosophy)</title>
<script src="../../MathJax/MathJax.js?config=TeX-MML-AM_CHTML"></script>
</head><body>
<p>正文 \\(x^2\\) 公式。</p>
<img src="fig1.png" alt="figure" />
<img src="eqn2.gif" alt="equation" />
<a href="notes.html">Notes</a>
<a href="../beta/fig-shared.png">shared figure</a>
<a href="../beta/">related entry</a>
<a href="../../css/style.css">css</a>
<a href="https://example.org/x">ext</a>
</body></html>"""


def build(root, files):
    for rel, content in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        mode = "wb" if isinstance(content, bytes) else "w"
        with open(p, mode) as f:
            f.write(content)


class TestResolveRef(unittest.TestCase):
    def test_bare_and_relative(self):
        self.assertEqual(resolve_ref("fig1.png", "alpha"), ("entry", "alpha", "fig1.png"))
        self.assertEqual(resolve_ref("../beta/x.png", "alpha"), ("entry", "beta", "x.png"))
        self.assertEqual(resolve_ref("../../entries/beta/x.png", "alpha"),
                         ("entry", "beta", "x.png"))
        self.assertEqual(resolve_ref("notes.html#s1", "alpha"),
                         ("entry", "alpha", "notes.html"))

    def test_site_external_skip(self):
        self.assertEqual(resolve_ref("../../css/style.css", "alpha"),
                         ("site", "css", "/css/style.css"))
        self.assertEqual(resolve_ref("https://example.org/x", "alpha"),
                         ("external", "example.org", "/x"))
        self.assertIsNone(resolve_ref("mailto:a@b.c", "alpha"))
        self.assertIsNone(resolve_ref("m&#97;ilto:a&#37;40b.c", "alpha"))
        self.assertIsNone(resolve_ref("", "alpha"))


class TestAuditDir(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.en = os.path.join(self.tmp, "en")
        build(self.en, {
            "alpha/index.html": PAGE,
            "alpha/fig1.png": "png",
            "alpha/eqn2.gif": "gif",
            "alpha/notes.html": "<html><body>notes</body></html>",
            "beta/fig-shared.png": "png",
        })

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def audit(self, registered=frozenset()):
        return audit_dir(self.en, "alpha", registered)

    def test_clean_package(self):
        reg = {"index.html", "fig1.png", "eqn2.gif", "notes.html"}
        res, hard = self.audit(reg)
        self.assertEqual(hard, 0)
        self.assertEqual(res["info"]["pages"], 2)
        self.assertEqual(res["info"]["site_refs"], {"css": 1, "MathJax": 1})
        self.assertEqual(res["info"]["external_refs"], {"example.org": 1})
        self.assertIn("mathjax", res)
        self.assertIn("math_inline_pages", res)
        self.assertEqual(res["math_asset_refs"], ["eqn2.gif"])

    def test_case_mismatch(self):
        os.remove(os.path.join(self.en, "alpha", "fig1.png"))
        build(self.en, {"alpha/Fig1.png": "png"})
        res, hard = self.audit({"index.html", "eqn2.gif", "notes.html"})
        self.assertEqual(res.get("case_mismatch"),
                         [{"ref": "fig1.png", "on_disk": "Fig1.png"}])
        self.assertNotIn("missing_assets", res)
        self.assertGreaterEqual(hard, 1)

    def test_missing_asset(self):
        os.remove(os.path.join(self.en, "alpha", "fig1.png"))
        res, hard = self.audit({"index.html", "eqn2.gif", "notes.html"})
        self.assertEqual(res["missing_assets"], ["fig1.png"])

    def test_cross_entry_missing(self):
        os.remove(os.path.join(self.en, "beta", "fig-shared.png"))
        res, hard = self.audit({"index.html", "fig1.png", "eqn2.gif", "notes.html"})
        self.assertEqual(res["cross_entry_missing"],
                         [{"entry": "beta", "asset": "fig-shared.png"}])

    def test_cross_entry_unmirrored_is_info_only(self):
        shutil.rmtree(os.path.join(self.en, "beta"))
        res, hard = self.audit({"index.html", "fig1.png", "eqn2.gif", "notes.html"})
        self.assertEqual(hard, 0)
        self.assertNotIn("cross_entry_missing", res)
        self.assertEqual(res["info"]["cross_links_unmirrored"], 1)

    def test_orphan_and_unregistered(self):
        build(self.en, {"alpha/leftover.html": "<html></html>",
                        "alpha/stray.dat": "x"})
        reg = {"index.html", "fig1.png", "eqn2.gif", "notes.html", "leftover.html"}
        res, hard = self.audit(reg)
        self.assertEqual(res["registered_orphans"], ["leftover.html"])
        self.assertEqual(res["unregistered_orphans"], ["stray.dat"])
        self.assertEqual(hard, 1)

    def test_registered_missing(self):
        res, hard = self.audit({"index.html", "fig1.png", "eqn2.gif", "notes.html",
                                "ghost.png"})
        self.assertEqual(res["registered_missing"], ["ghost.png"])

    def test_fetched_not_registered_is_info_only(self):
        build(self.en, {"alpha/newfig.png": "png",
                        "alpha/notes.html": '<html><img src="newfig.png"></html>'})
        res, hard = self.audit({"index.html", "fig1.png", "eqn2.gif", "notes.html"})
        self.assertEqual(res["fetched_not_registered"], ["newfig.png"])
        self.assertEqual(hard, 0)

    def test_double_slash_normalized(self):
        self.assertEqual(resolve_ref("/entries//beta/x.png", "alpha"),
                         ("entry", "beta", "x.png"))

    def test_commented_refs_ignored(self):
        build(self.en, {"alpha/index.html":
                        PAGE + '<!-- <img src="commented.png" /> -->'})
        res, hard = self.audit({"index.html", "fig1.png", "eqn2.gif", "notes.html"})
        self.assertNotIn("missing_assets", res)
        self.assertEqual(hard, 0)

    def test_subdir_target(self):
        page = ('<html><title>G (Stanford Encyclopedia of Philosophy)</title>'
                '<img src="BN/x.png"></html>')
        build(self.en, {"gam/index.html": page, "gam/BN/x.png": "png"})
        res, hard = audit_dir(self.en, "gam", {"index.html"})
        self.assertEqual(hard, 0)
        os.remove(os.path.join(self.en, "gam", "BN", "x.png"))
        res, hard = audit_dir(self.en, "gam", {"index.html"})
        self.assertEqual(res["missing_assets"], ["BN/x.png"])

    def test_not_sep_page(self):
        build(self.en, {"fake/index.html":
                        "<html><body>totally not SEP</body></html>"})
        res, hard = audit_dir(self.en, "fake", {"index.html"})
        self.assertEqual(res["not_sep_page"], ["index.html"])

    def test_marker_in_branded_text_not_flagged(self):
        page = ('<html><title>X (Stanford Encyclopedia of Philosophy)</title>'
                '<body>He said just a moment ago.</body></html>')
        build(self.en, {"fake/index.html": page})
        res, hard = audit_dir(self.en, "fake", {"index.html"})
        self.assertNotIn("suspect_page", res)
        self.assertEqual(hard, 0)

    def test_inbound_cross_ref_not_orphan(self):
        build(self.en, {"beta/index.html":
                        '<html><title>B (Stanford Encyclopedia of Philosophy)'
                        '</title><body>b</body></html>',
                        "beta/appendix.html": "<html></html>",
                        "gam/index.html":
                        '<html><title>G (Stanford Encyclopedia of Philosophy)</title>'
                        '<a href="../beta/appendix.html">app</a></html>'})
        inb = inbound_map(self.en, ["alpha", "beta", "gam"])
        self.assertEqual(inb, {"beta": {"appendix.html", "fig-shared.png"}})
        res, hard = audit_dir(self.en, "beta",
                              {"index.html", "fig-shared.png"},
                              inb.get("beta", set()))
        self.assertEqual(hard, 0)
        self.assertEqual(res["fetched_not_registered"], ["appendix.html"])
        self.assertNotIn("registered_orphans", res)

    def test_suspect_and_truncated(self):
        build(self.en, {"bad/index.html":
                        "<html>Attention Required! | Cloudflare</html>"})
        res, hard = audit_dir(self.en, "bad", {"index.html"})
        self.assertEqual(res["not_sep_page"], ["index.html"])
        build(self.en, {"bad/index.html":
                        "<html><title>X (Stanford Encyclopedia of Philosophy)</title>"
                        "<body><h1>Just a moment…</h1></body></html>"})
        res, hard = audit_dir(self.en, "bad", {"index.html"})
        self.assertIn("suspect_page", res)
        build(self.en, {"bad/index.html": "<html><body>no close"})
        res, hard = audit_dir(self.en, "bad", {"index.html"})
        self.assertEqual(res["truncated"], ["index.html"])

    def test_nested_and_empty(self):
        build(self.en, {"bad/sub/x.png": "png", "bad/index.html": PAGE,
                        "bad/empty.png": ""})
        res, hard = audit_dir(self.en, "bad", {"index.html"})
        self.assertEqual(res["nested_dirs"], ["sub"])
        self.assertEqual(res["empty_files"], ["empty.png"])


if __name__ == "__main__":
    unittest.main()

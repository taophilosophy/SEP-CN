# -*- coding: utf-8 -*-
"""fetch_audit.referenced_assets 引用闭包语义单元测试（CI: unittest discover）。"""
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tools import fetch_audit
from tools.common import repo_path


class TestReferencedAssets(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(dir=repo_path("en"), prefix="_audit_test_")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def scan(self, html):
        with open(os.path.join(self.tmp, "index.html"), "w", encoding="utf-8") as f:
            f.write("<html><body>%s</body></html>" % html)
        return fetch_audit.referenced_assets(os.path.basename(self.tmp))

    def test_bare_assets_and_media(self):
        refs = self.scan('<p><img src="fig1.png"><script src="local.js">'
                         '<a href="notes.html"><a href="sound.au">'
                         '<embed src="movie.qt"></p>')
        self.assertEqual(refs, {"fig1.png", "local.js", "notes.html",
                                "sound.au", "movie.qt"})

    def test_comments_entities_and_framework_excluded(self):
        refs = self.scan('<!-- <img src="ghost.png"> -->'
                         '<a href="m&#97;ilto:a@b.c">mail</a>'
                         '<a href="../../js/sep.js">site</a>'
                         '<a href="https://x.org/y">ext</a>'
                         '<a href="index.html">self</a>'
                         '<a href="supp.html?q=1#s">supp</a>')
        self.assertEqual(refs, {"supp.html"})

    def test_junk_shape_excluded(self):
        refs = self.scan('<a href="&nbsp;">n</a><a href="m&x">junk</a>'
                         '<a href="plainword">w</a>')
        self.assertEqual(refs, set())


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""check_images 单测：悬空、大小写、外链口径、代码块豁免、镜像缺位跳过、未引用资产。"""
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import check_images


class ScanTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        full = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="") as f:
            f.write(text)

    def scan(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_images.main(["--root", self.root,
                                      "--out", os.path.join(self.root, "state", "r.md")])
        self.assertEqual(code, 0)
        return check_images.scan(self.root)

    def test_dangling_and_resolved(self):
        self.write("a/x.md", "![ok](../assets/x/ok.png)\n\n![bad](../assets/x/no.png)\n")
        self.write("assets/x/ok.png", "x")
        res = self.scan()
        self.assertEqual([r for _, r in res["dangling"]], ["../assets/x/no.png"])
        self.assertEqual(res["case"], [])

    def test_case_mismatch(self):
        self.write("a/x.md", "![f](../assets/x/Fig.PNG)\n")
        self.write("assets/x/fig.png", "x")
        res = self.scan()
        self.assertEqual(res["dangling"], [])
        self.assertEqual(res["case"][0][2], "assets/x/fig.png")

    def test_code_fence_and_inline_code_ignored(self):
        self.write("a/x.md",
                   "`<img src=\"imageN.jpg\">` 示例\n\n```\n![](../assets/x/imageN.jpg)\n```\n")
        res = self.scan()
        self.assertEqual(res["dangling"], [])
        self.assertEqual(res["remote"], [])

    def test_external_image_reported_external_link_not(self):
        self.write("a/x.md",
                   "![](https://example.org/a.png)\n\n[外部图片](https://example.org/b.jpg)\n")
        res = self.scan()
        self.assertEqual([r for _, r in res["remote"]], ["https://example.org/a.png"])

    def test_yuanwen_ref_skipped_when_mirror_absent(self):
        self.write("a/x.md", "![m](../yuanwen/assets/x/fig.png)\n")
        res = self.scan()
        self.assertEqual(res["dangling"], [])

    def test_unreferenced_asset(self):
        self.write("a/x.md", "![ok](../assets/x/ok.png)\n")
        self.write("assets/x/ok.png", "x")
        self.write("assets/x/extra.png", "x")
        res = self.scan()
        self.assertEqual(res["orphans"], ["assets/x/extra.png"])

    def test_image_as_link_target_counts_as_referenced(self):
        self.write("a/x.md", "[![small](../assets/x/small.gif)](../assets/x/large.gif)\n")
        self.write("assets/x/small.gif", "x")
        self.write("assets/x/large.gif", "x")
        res = self.scan()
        self.assertEqual(res["orphans"], [])
        self.assertEqual(res["dangling"], [])


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""check_summary.py 的无链接分组行口径单测（ADR-0057）。

集群占位母行在 SUMMARY 里写作无链接分组行（`* \\*分类名`），不指向文件：
GitBook 要求一文件一页，182 行同指 README.md 会直接拒绝导入。本测试锁定三条：
  1. 合法无链接分组行通过，且计入 nav groups；
  2. 无子条目的空分组行是硬错误（GitBook/侧栏会留空组）；
  3. 残留链接语法碎片仍按 UNPARSED 硬错误抓出，不得被静默降级成分组行。
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(REPO, "tools", "check_summary.py")


def run(root, *args):
    cmd = [sys.executable, os.path.join(root, "tools", "check_summary.py")] + list(args)
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")


class NavRowTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name
        os.makedirs(os.path.join(self.root, "tools"))
        shutil.copy(SCRIPT, os.path.join(self.root, "tools", "check_summary.py"))
        self.write("README.md", "# 斯坦福哲学百科全书简体中文版\n")
        self.write("a/a.md", "# 词条 A\n")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        full = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(full) or self.root, exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="") as f:
            f.write(text)

    def summary(self, *rows):
        self.write("SUMMARY.md", "\n".join(rows) + "\n")

    def test_linkless_nav_row_passes(self):
        self.summary(
            "* [斯坦福哲学百科全书简体中文版](README.md)",
            "",
            "## A",
            "",
            "* \\*分组标签",
            "  * [词条 A](a/a.md)",
        )
        r = run(self.root)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("nav groups (linkless, ADR-0057): 1", r.stdout)
        self.assertIn("empty nav groups (无子条目的分组行): 0", r.stdout)
        self.assertIn("HARD ERRORS: 0", r.stdout)

    def test_empty_nav_row_fails(self):
        self.summary(
            "* [斯坦福哲学百科全书简体中文版](README.md)",
            "",
            "## A",
            "",
            "* \\*空分组标签",
            "* [词条 A](a/a.md)",
        )
        r = run(self.root)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("empty nav groups (无子条目的分组行): 1", r.stdout)
        self.assertIn("EMPTY NAV L", r.stdout)

    def test_broken_link_still_unparsed(self):
        self.summary(
            "* [斯坦福哲学百科全书简体中文版](README.md)",
            "",
            "## A",
            "",
            "* [词条 A](a/a.md",
        )
        r = run(self.root)
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("UNPARSED LINE", r.stdout)
        self.assertIn("HARD ERRORS: 1", r.stdout)

    def test_headers_mode_ignores_nav_rows(self):
        self.summary(
            "* [斯坦福哲学百科全书简体中文版](README.md)",
            "",
            "## A",
            "",
            "* \\*分组标签",
            "  * [词条 A](a/a.md)",
        )
        r = run(self.root, "--headers")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("H1 mismatch: 0", r.stdout)


if __name__ == "__main__":
    unittest.main()

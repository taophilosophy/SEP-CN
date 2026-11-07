# -*- coding: utf-8 -*-
"""check_summary.py 的 H1 一致性口径单测（ADR-0024）。

用临时仓库副本跑子进程：脚本按自身位置定位仓库根，故复制到 <tmp>/tools/ 下即可指向 <tmp>。
重点回归：标题里的转义方括号 `\\[dge lugs pa\\]` 必须整段解析——结构审计用的
`\\[([^]]*)\\]` 会在第一个 `]` 处截断，曾把 31 个 H1 写成半截标题（2026-11-07）。
"""
import json
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


class HeaderConsistencyTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name
        os.makedirs(os.path.join(self.root, "tools"))
        shutil.copy(SCRIPT, os.path.join(self.root, "tools", "check_summary.py"))

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        full = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(full) or self.root, exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="") as f:
            f.write(text)

    def summary(self, *lines):
        self.write("SUMMARY.md", "# Table of contents\n\n" + "\n".join(lines) + "\n")

    def test_escaped_brackets_parse_in_full_and_match(self):
        self.summary("* [格鲁派 Gelukpa \\[dge lugs pa\\] (Douglas Duckworth)](g/gelukpa.md)")
        self.write("g/gelukpa.md", "# 格鲁派 Gelukpa [dge lugs pa] (Douglas Duckworth)\n")
        r = run(self.root, "--headers")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_mismatch_is_hard_error(self):
        self.summary("* [知识的价值 The Value of Knowledge (Duncan Pritchard)](k/knowledge-value.md)")
        self.write("k/knowledge-value.md", "# 知识的价值 knowledge, value of (Duncan Pritchard)\n")
        r = run(self.root, "--headers")
        self.assertEqual(r.returncode, 1)
        self.assertIn("k/knowledge-value.md", r.stdout)

    def test_alias_placeholder_readme_and_frontmatter_skipped(self):
        self.summary(
            "* [\\*知识——见知识的价值 knowledge — see knowledge, value of](k/knowledge-value.md)",
            "* [\\*知识 knowledge](README.md)",
            "* [首页](README.md)",
            "* [分类目录](mu-lu-s.md)",
        )
        self.write("k/knowledge-value.md", "# 知识的价值 The Value of Knowledge\n")
        self.write("README.md", "# 斯坦福哲学百科全书简体中文版\n")
        self.write("mu-lu-s.md", "---\noutline: [1, 6]\n---\n")
        r = run(self.root, "--headers")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_sync_rewrites_h1_idempotently(self):
        self.summary("* [韩国佛教 Korean Buddhism (Lucy Hyekyung Jee)](k/korean-buddhism.md)")
        self.write("k/korean-buddhism.md", "# 韩国佛教 Buddhism\n\n正文段落\n")
        r = run(self.root, "--sync-headers")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        with open(os.path.join(self.root, "k/korean-buddhism.md"), encoding="utf-8") as f:
            self.assertEqual(f.read(), "# 韩国佛教 Korean Buddhism (Lucy Hyekyung Jee)\n\n正文段落\n")
        # 幂等：第二次同步改动 0 处
        r2 = run(self.root, "--sync-headers")
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)
        self.assertIn("H1 同步 0 处，残差 0", r2.stdout)


class AliasFragmentTest(unittest.TestCase):
    """别名行左侧英文必须是完整标题（2026-11-07 裁定）；默认审计即硬拦。"""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name
        os.makedirs(os.path.join(self.root, "tools"))
        shutil.copy(SCRIPT, os.path.join(self.root, "tools", "check_summary.py"))
        os.makedirs(os.path.join(self.root, "baseline"))
        with open(os.path.join(self.root, "baseline", "entries.json"), "w", encoding="utf-8") as f:
            json.dump({"entries": [{"slug": "biology-experiment", "title": "Experiment in Biology"}]}, f)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        full = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(full) or self.root, exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="") as f:
            f.write(text)

    def test_dangling_fragment_is_hard_error(self):
        self.write("SUMMARY.md", "* [\\*生物学——见生物学：实验生物学 in biology — see biology: experiment in](b/biology-experiment.md)\n")
        self.write("b/biology-experiment.md", "# 生物学中的实验 Experiment in Biology\n")
        r = run(self.root)
        self.assertEqual(r.returncode, 1)
        self.assertIn("ALIAS", r.stdout)

    def test_full_title_fragment_passes(self):
        self.write("SUMMARY.md", "* [\\*生物学——见生物学：实验生物学 Experiment in Biology — see biology: experiment in](b/biology-experiment.md)\n")
        self.write("b/biology-experiment.md", "# 生物学中的实验 Experiment in Biology\n")
        r = run(self.root)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()

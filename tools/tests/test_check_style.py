# -*- coding: utf-8 -*-
"""check_style 六规则正反例。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_style import check_file  # noqa: E402
from tools.common import write_text  # noqa: E402


def run(content):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.md")
        write_text(p, content)
        return check_file(p)


def rules(issues):
    return {i["rule"] for i in issues}


class TestCheckStyle(unittest.TestCase):
    def test_clean_chinese(self):
        self.assertEqual(run("# 标题\n\n这是“引号”和 **加粗** 以及 SEP 词条的空格。\n"), [])

    def test_crlf_bold_at_eol(self):
        # CRLF 文件行尾加粗不得误报“后缺空格”（splitlines 切行，\r 不参与判定）
        self.assertEqual(run("## T\n\n**首次发表于 2004 年 8 月 3 日。**\r\n\r\n正文一段。\r\n"), [])

    def test_bold_after_closing_quote(self):
        # 右引号后紧贴开粗体：02 条款「与中文标点紧贴」允许
        self.assertEqual(run("他说“……为真”**之前** 就已出现。\n"), [])

    def test_straight_quote(self):
        self.assertTrue("curly-quotes" in rules(run('他说"你好"。\n')))

    def test_uncurly_pair(self):
        self.assertTrue("curly-quotes" in rules(run("他说“你好。\n")))

    def test_apostrophe_allowed(self):
        self.assertEqual([i for i in run("这是 O'Brien 和 don't 的词内撇号。\n")
                          if i["rule"] == "curly-quotes"], [])

    def test_bold_spacing(self):
        self.assertTrue("bold-spacing" in rules(run("汉字**加粗**紧贴。\n")))

    def test_cjk_spacing(self):
        self.assertTrue("cjk-spacing" in rules(run("使用SEP词条。\n")))

    def test_html_residue(self):
        self.assertTrue("no-html" in rules(run("残留 <em>斜体</em>。\n")))

    def test_text_fence(self):
        self.assertTrue("no-text-fence" in rules(run("```text\nx\n```\n")))

    def test_asciiart(self):
        self.assertTrue("no-asciiart" in rules(run("见 xref:other[链接]。\n")))

    def test_code_block_exempt(self):
        self.assertEqual(run("```sh\nls -l \"路径\"\n```\n\n正文引用 `ls -l \"x\"` 保持原样。\n"), [])


if __name__ == "__main__":
    unittest.main()

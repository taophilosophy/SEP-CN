# -*- coding: utf-8 -*-
"""cite_audit 引块抽取单测（064 T185 q1）：引块入清单、pubinfo/照录说明不入、内层引号不重复。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import cite_audit  # noqa: E402


class BlockquoteSpansTest(unittest.TestCase):
    def test_skips_pubinfo_and_note(self):
        text = (
            "> *首次发表于 2023 年 9 月 15 日。*\n\n"
            "> 这是一个足够长的中文引块，用来验证引块抽取。\n\n"
            "> 原文参考文献已转为脚注引用：文内引用组后附标记。\n"
        )
        spans = cite_audit.blockquote_spans(text)
        self.assertEqual(len(spans), 1)
        self.assertIn("这是一个足够长的中文引块", spans[0][2])
        self.assertEqual(spans[0][0], 3)

    def test_multiline_block(self):
        text = "> 第一行引文内容足够长，\n> 第二行继续同一引块。\n"
        spans = cite_audit.blockquote_spans(text)
        self.assertEqual(len(spans), 1)
        self.assertEqual(spans[0][:2], (1, 2))
        self.assertIn("第二行", spans[0][2])


class BuildItemsTest(unittest.TestCase):
    def test_block_and_inline_without_duplicate(self):
        text = (
            "导言段。\n\n"
            "> 外部引文包含“内层短语”的完整句子。\n\n"
            "正文又说“这是另一条行内引文候选”。\n"
        )
        items = cite_audit.build_items(text, "demo")
        self.assertEqual(len(items), 2)
        self.assertEqual([it["form"] for it in items], ["block", "inline"])
        self.assertEqual([it["id"] for it in items],
                         ["c-demo-001", "c-demo-002"])
        blocks = [it for it in items if it["form"] == "block"]
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["quote_lang"], "zh")
        self.assertEqual(blocks[0]["hash"],
                         cite_audit.sha16("外部引文包含“内层短语”的完整句子。"))

    def test_ids_follow_line_order(self):
        text = (
            "行内引文“较早出现的一条候选”在前。\n\n"
            "> 引块在后，但内容也足够长。\n"
        )
        items = cite_audit.build_items(text, "demo")
        self.assertEqual([it["loc"] for it in items], ["L1", "L3"])


if __name__ == "__main__":
    unittest.main()

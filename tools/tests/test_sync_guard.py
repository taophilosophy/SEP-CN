# -*- coding: utf-8 -*-
"""sync_guard 清单解析与判弃分类单测（ADR-0028）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.sync_guard import (  # noqa: E402
    classify, parse_cherry, parse_oneline,
)


class ParseOnelineTest(unittest.TestCase):
    def test_basic(self):
        text = "abc123 固定第一条\ndef456 第二条 带空格\n"
        self.assertEqual(
            parse_oneline(text),
            [("abc123", "固定第一条"), ("def456", "第二条 带空格")],
        )

    def test_blank_and_indent_ignored(self):
        self.assertEqual(parse_oneline("\n  \nxyz789 唯一\n"), [("xyz789", "唯一")])

    def test_empty(self):
        self.assertEqual(parse_oneline(""), [])


class ParseCherryTest(unittest.TestCase):
    def test_flags(self):
        text = "- 1111111\n+ 2222222\n"
        self.assertEqual(parse_cherry(text), {"1111111": "-", "2222222": "+"})

    def test_empty(self):
        self.assertEqual(parse_cherry(""), {})


class ClassifyTest(unittest.TestCase):
    def test_all_kept(self):
        pre = [("+", "a1", "甲"), ("+", "a2", "乙")]
        post = [("b1", "甲"), ("b2", "乙")]
        lost, dropped, extra = classify(pre, post)
        self.assertEqual((lost, dropped, extra), ([], [], []))

    def test_patch_identical_dropped_is_ok(self):
        pre = [("+", "a1", "甲"), ("-", "a2", "乙（已在远程）")]
        post = [("b1", "甲")]
        lost, dropped, extra = classify(pre, post)
        self.assertEqual(lost, [])
        self.assertEqual(dropped, [("a2", "乙（已在远程）")])
        self.assertEqual(extra, [])

    def test_plus_commit_dropped_is_lost(self):
        pre = [("+", "a1", "甲"), ("+", "a2", "乙")]
        post = [("b1", "甲")]
        lost, dropped, extra = classify(pre, post)
        self.assertEqual(lost, [("a2", "乙")])
        self.assertEqual(dropped, [])

    def test_duplicate_subjects_counted(self):
        pre = [("+", "a1", "同题"), ("+", "a2", "同题")]
        post = [("b1", "同题")]
        lost, _, _ = classify(pre, post)
        self.assertEqual(len(lost), 1)  # 两件同题只保住一件，另一件判丢

    def test_extra_detected(self):
        pre = [("+", "a1", "甲")]
        post = [("b1", "甲"), ("b2", "来历不明")]
        _, _, extra = classify(pre, post)
        self.assertEqual(extra, ["来历不明"])

    def test_only_dash_commits_all_dropped(self):
        pre = [("-", "a1", "一"), ("-", "a2", "二")]
        post = []
        lost, dropped, extra = classify(pre, post)
        self.assertEqual((lost, extra), ([], []))
        self.assertEqual(len(dropped), 2)


if __name__ == "__main__":
    unittest.main()

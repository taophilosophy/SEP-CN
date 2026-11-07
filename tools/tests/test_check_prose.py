# -*- coding: utf-8 -*-
"""check_prose 八则反欧化规则与豁免的正反例。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_prose import check_file  # noqa: E402
from tools.common import write_text  # noqa: E402


def run(content):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.md")
        write_text(p, content)
        return check_file(p)


def rules(issues):
    return {i["rule"] for i in issues}


class TestCheckProse(unittest.TestCase):
    def test_clean_chinese(self):
        self.assertEqual(run(
            "溯因是扩展的推理，归纳与演绎各有所长，SEP 词条对此有详细讨论。\n"), [])

    def test_long_sentence(self):
        s = "在" * 40 + "哲学家们认为这一点至关重要并且值得反复申说" + "在" * 30 + "。"
        self.assertIn("long-sentence", rules(run(s + "\n")))

    def test_passive_bei(self):
        self.assertIn("passive-bei", rules(run("结论被推翻了，前提也被否定了。\n")))

    def test_weak_verb(self):
        self.assertIn("weak-verb", rules(run("我们进行了仔细的分析，并且作出了相应的调整。\n")))

    def test_de_chain(self):
        self.assertIn("de-chain", rules(run("他对这本书的作者的批评的理由并不充分。\n")))

    def test_plural_men(self):
        self.assertIn("plural-men", rules(run("科学家们普遍接受了这一假说。\n")))

    def test_as_one(self):
        self.assertIn("as-one", rules(run("他作为一个经验论者反对这一论证。\n")))

    def test_exists_there(self):
        self.assertIn("exists-there", rules(run("在这里存在着一个明显的困难。\n")))

    def test_dang_shihou(self):
        self.assertIn("dang-shihou", rules(run("当人们讨论归纳的时候，总会提到休谟。\n")))

    def test_ongoing_action_not_weak_verb(self):
        # "进行中的行动"是体貌义术语（S5 白名单 2026-10-31），非弱动词
        self.assertNotIn("weak-verb", rules(run("能动性只在进行中的行动中显现。\n")))

    def test_pipe_list_line_exempt(self):
        # 相关词条竖线列表行不按散文长句计
        line = "贝叶斯认识论 | 归纳问题 | 查尔斯·桑德斯·皮尔士 | 科学实在论 | 简单性 | 怀疑论\n"
        self.assertEqual(run(line), [])

    def test_bei_term_not_passive(self):
        # "被动"是术语（主动/被动），不计入被字句（S5 白名单 2026-11-08）
        self.assertNotIn("passive-bei", rules(run(
            "主动与被动之间有一个重要区别，木头对火是被动的。\n")))

    def test_mudi_not_de_chain(self):
        # "目的/目的论"词内的"的"不是结构助词（S5 白名单 2026-11-08）
        self.assertNotIn("de-chain", rules(run(
            "这种目的论的进路把目的当作行动的解释项。\n")))

    def test_exempt_refs_and_math(self):
        md = ("## 参考文献\n\n"
              "[^a-2001]: Author, A., 2001. *Some Book*, Oxford: Oxford University Press.\n\n"
              "## 正文\n\n"
              "给定 $H_{n+1} := \\neg H_1 \\wedge \\cdots \\wedge \\neg H_n$，"
              "其合取式在逻辑空间中是穷尽的。\n\n"
              "| 原文 | 译法 |\n| ---- | ---- |\n| abduction | 溯因 |\n")
        self.assertEqual(run(md), [])


if __name__ == "__main__":
    unittest.main()

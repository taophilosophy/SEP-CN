# -*- coding: utf-8 -*-
"""六轴质量工序（ADR-0079）：共享库谓词与六器机检子集的单元测试。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import axis_lib as ax  # noqa: E402
from tools import cite_audit, grammar_audit, logic_audit, measure_audit  # noqa: E402
from tools import punct_audit, register_audit, qchain, task_ops  # noqa: E402


class TestAxisLib(unittest.TestCase):
    def test_order_has_q_chain(self):
        order = task_ops.ORDER["retranslate"]
        qs = [s for s in order if s.startswith("q")]
        self.assertEqual(qs, ["q1_cite_checked", "q2_logic_checked",
                              "q3_grammar_checked", "q4_register_checked",
                              "q5_measure_checked", "q6_punct_checked"])
        self.assertLess(order.index("s2.5_checked"), order.index("q1_cite_checked"))
        self.assertLess(order.index("q6_punct_checked"), order.index("s3_checked"))

    def test_skip_q_node_rejected(self):
        self.assertEqual(task_ops.expected_prev("retranslate", "q3"),
                         "q2_logic_checked")
        self.assertEqual(task_ops.expected_prev("retranslate", "s3"),
                         "q6_punct_checked")

    def test_protect_masks_code_math_url(self):
        text = "正文$公式$。`code`\n\n```\nblock\n```\n\nhttps://x.y 收尾。"
        masked = ax.protect(text)
        self.assertNotIn("公式", masked)
        self.assertNotIn("code", masked)
        self.assertNotIn("block", masked)
        self.assertNotIn("https", masked)
        self.assertEqual(len(masked), len(text))  # 等长掩码，索引对齐

    def test_lang_of(self):
        self.assertEqual(ax.lang_of("the spirit of the age"), "none")
        self.assertEqual(ax.lang_of("der Geist der Zeit"), "german")
        self.assertEqual(ax.lang_of("ἡ ψυχὴ ἀθάνατος"), "greek")
        # 转写术语（IAST）不误判为某一自然语言；归 unclassified，由人审或术语轴处理
        self.assertIn(ax.bcp47(ax.lang_of("dharma svabhāva")), ("en", "unclassified"))

    def test_quote_level_threshold(self):
        self.assertFalse(cite_audit.is_quote_level("dharma"))
        self.assertTrue(cite_audit.is_quote_level(
            "the unexamined life is not worth living"))


class TestSixInstruments(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "sample.md")
        with open(self.path, "w", encoding="utf-8", newline="\n") as f:
            f.write("# 样本\n\n"
                    "他说：“凡不可说的，应当沉默。”\n\n"
                    "速度达到 5km，另一处写 5 km。\n\n"
                    "省略号写成了...，引号用了\"直引号\"。\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_cite_scan_finds_quote(self):
        slug, items = cite_audit.scan(self.path)
        self.assertTrue(any("凡不可说" in it["english"] or it["quote_lang"] == "zh"
                            for it in items))

    def test_measure_flags_missing_space(self):
        slug, data = measure_audit.scan(self.path)
        rules = {i["rule"] for i in data["issues"]}
        self.assertIn("M-2", rules)

    def test_punct_flags_ascii_quote_and_ellipsis(self):
        slug, data = punct_audit.scan(self.path)
        rules = {i["rule"] for i in data["issues"]}
        self.assertIn("P-8", rules)
        self.assertIn("P-11", rules)

    def test_grammar_false_positive_whitelist(self):
        p = os.path.join(self.tmp.name, "fp.md")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("# 样本\n\n正如他所说的一样，彻底根治并非易事。\n")
        slug, issues = grammar_audit.scan(p)
        self.assertFalse(any(i["rule"] == "G-5" for i in issues))

    def test_register_flags_classical_and_you(self):
        p = os.path.join(self.tmp.name, "reg.md")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("# 样本\n\n## 1. 节\n\n您认为此事可行。\n\n古人云，大道之行也。\n")
        slug, data = register_audit.scan(p)
        rules = {i["rule"] for i in data["issues"]}
        self.assertIn("R-f", rules)

    def test_logic_skeleton_covers_sentences(self):
        p = os.path.join(self.tmp.name, "logic.md")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("# 样本\n\n所有天鹅都是白的，但有些鸟不是。\n\n"
                    "如果下雨，那么地面会湿。\n")
        rows = logic_audit.skeleton("logic", ax.read_doc(p))
        self.assertGreaterEqual(len(rows), 2)
        self.assertTrue(all(r["verdict"] == "pending" for r in rows))

    def test_qchain_order(self):
        self.assertEqual([x[0] for x in qchain.ORDER],
                         ["q1", "q2", "q3", "q4", "q5", "q6"])


if __name__ == "__main__":
    unittest.main()

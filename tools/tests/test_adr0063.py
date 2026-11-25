# -*- coding: utf-8 -*-
"""ADR-0063 工具单测：体例轴四则、补丁准入谓词、保真字符流。

跑法: python -m unittest tools.tests.test_adr0063 -v
"""
import io
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

from check_en_patches import admission  # noqa: E402
from check_pairs import (check_tail_order, check_heading_number, check_h1_form,  # noqa: E402
                         HARD_RULES)
from check_yuanwen_fidelity import multiset_diff, chars, digit_count  # noqa: E402


class TestPatchAdmission(unittest.TestCase):
    """C2 准入谓词（ADR-0063 决策 6）：空白差/标记差可入池，词符差禁入。"""

    def test_blank_diff_allowed(self):
        self.assertEqual(admission("Einstein1949b", "Einstein 1949b"), "blank")

    def test_tag_diff_allowed(self):
        self.assertEqual(admission('<div class="x">a', '</div>\n<div class="x">a'), "tag")

    def test_text_layer_rejected(self):
        self.assertIsNone(admission("Renthe-Fink", "von Renthe-Fink"))
        self.assertIsNone(admission("Teubener", "Teubner"))

    def test_real_pool_patches_pass(self):
        # 池已目录化（baseline/en-patches/*.patch，ADR-0063 2026-11-16 裁定）；
        # 解析唯一实现在 tools/en_patch_lib.py。
        from tools import en_patch_lib
        patches = en_patch_lib.load_patches()
        self.assertTrue(patches, "补丁目录应有正本")
        for slug, items in patches.items():
            for p in items:
                self.assertIsNotNone(admission(p["find"], p["replace"]),
                                     "池内补丁 %s 应过准入谓词" % p["id"])


class TestTailOrder(unittest.TestCase):
    """尾节齐备与顺序 + 脚注末位（ADR-0063 判定表第一行）。"""

    def _run(self, text):
        issues = []
        check_tail_order("t.md", text, issues)
        return issues

    def test_canonical_ok(self):
        text = ("# 题\n\n正文\n\n## 1. 一\n\n## 参考文献\n\n## 学术工具\n\n"
                "## 其他网络资源\n\n## 相关词条\n")
        self.assertEqual(self._run(text), [])

    def test_missing_section(self):
        text = "# 题\n\n## 1. 一\n\n## 参考文献\n\n## 学术工具\n"
        issues = self._run(text)
        self.assertEqual(issues[0]["rule"], "tail-order")
        self.assertIn("相关词条", issues[0]["detail"])

    def test_footnote_must_be_last(self):
        text = ("# 题\n\n## 脚注\n\n## 参考文献\n\n## 学术工具\n\n"
                "## 其他网络资源\n\n## 相关词条\n")
        issues = self._run(text)
        self.assertTrue(any("末位" in i["detail"] for i in issues))


class TestHeadingNumber(unittest.TestCase):
    """编号点号式与跳号（ADR-0063 判定表第二行，用户裁定与原文一致）。"""

    def _run(self, text):
        issues = []
        check_heading_number("t.md", text, issues)
        return issues

    def test_dotted_ok(self):
        text = "## 1. 一\n\n### 1.1 子\n\n## 2. 二\n"
        self.assertEqual(self._run(text), [])

    def test_bare_number_rejected(self):
        issues = self._run("## 1 一\n")
        self.assertEqual(issues[0]["rule"], "heading-number")

    def test_skip_rejected(self):
        issues = self._run("## 1. 一\n\n## 3. 三\n")
        self.assertTrue(any("跳号" in i["detail"] for i in issues))

    def test_tail_sections_untouched(self):
        self.assertEqual(self._run("## 参考文献\n"), [])


class TestH1Form(unittest.TestCase):
    """H1 作者括号与英文题一致（ADR-0063 判定表第三行）。"""

    def test_with_author_ok(self):
        check_h1_form("t.md", "# 溯因 Abduction (Igor Douven)\n", [])  # 不新增

    def test_missing_author(self):
        issues = []
        check_h1_form("t.md", "# 溯因 Abduction\n", issues)
        self.assertEqual(issues[0]["rule"], "h1-form")

    def test_en_title_must_match_yuanwen(self):
        issues = []
        check_h1_form("t.md", "# 溯因 (Igor Douven)\n", issues,
                      yw_text="# Abduction\n")
        self.assertTrue(any("英文题" in i["detail"] for i in issues))


class TestHardRules(unittest.TestCase):
    def test_hard_rules_membership(self):
        for r in ("tail-order", "heading-number", "h1-form", "errata-apply", "pubinfo-form"):
            self.assertIn(r, HARD_RULES)


class TestFidelity(unittest.TestCase):
    """I3 字母多重集判据：移位合法、丢字叠字必现。"""

    def test_equal_after_reorder(self):
        a = "alpha beta gamma"
        b = "gamma beta alpha"
        self.assertIsNone(multiset_diff(a, b))

    def test_duplicate_title_detected(self):
        # 缺陷形态＝md 比源多出一份文字（30 件重复 H1 即此面）
        d = multiset_diff("Bertrand Russell preamble text",
                          "Bertrand Russell Bertrand Russell preamble text")
        self.assertIsNotNone(d)
        self.assertEqual(d["n_missing"], 0)
        self.assertGreater(d["n_extra"], 0)
        self.assertIn("Bertrand", d["words"])

    def test_dropped_word_detected(self):
        d = multiset_diff("the mean of the nature", "the mean of nature")
        self.assertIsNotNone(d)
        self.assertEqual(d["n_missing"], 3)  # 丢了 "the" 的三字母

    def test_superscript_forms_equivalent(self):
        # 数字化入软信号不入主判据：G₁ 与 G1 的字母流同为 ['G']
        self.assertEqual(chars("G₁"), chars("G1"))
        self.assertEqual(digit_count("G1"), 1)
        self.assertIsNone(multiset_diff("G1 model", "G₁ model"))

    def test_digit_count_soft_signal(self):
        self.assertEqual(digit_count("a1b22"), 3)

    def test_greek_letters_counted(self):
        self.assertEqual(len(chars("φψ")), 2)


class TestErrataApplyNotes(unittest.TestCase):
    """errata-apply 译注豁免：译注跨度内引用上游错字形不算违规（ADR-0062 决策 4）。"""

    def setUp(self):
        import check_pairs
        self.cp = check_pairs
        self._saved = dict(check_pairs._ERRATA_CACHE)
        check_pairs._ERRATA_CACHE.clear()
        check_pairs._ERRATA_CACHE["demo"] = [{
            "slug": "demo", "pos": "正文", "src": "`Calchi 2020`",
            "reading": "Calchi 2023", "carrier": "句内译注"}]

    def tearDown(self):
        self.cp._ERRATA_CACHE.clear()
        self.cp._ERRATA_CACHE.update(self._saved)

    def _issues(self, text):
        out = []
        self.cp.check_errata("x/demo.md", "demo", text, out)
        return [i for i in out if i["rule"] == "errata-apply"]

    def test_note_quoting_wrong_form_is_exempt(self):
        text = "见 Calchi 2023（译注：上游正文此处作 Calchi 2020，译文从文献表。）\n"
        self.assertEqual(self._issues(text), [])

    def test_body_wrong_form_still_reported(self):
        text = "正文仍作 Calchi 2020（译注：上游正文作 Calchi 2020。）\n"
        self.assertEqual(len(self._issues(text)), 1)

    def test_nested_parens_inside_note_masked(self):
        text = "见 Calchi 2023（译注：上游作 Calchi 2020，与文献表唯一 Calchi 条目（2023）矛盾。）\n"
        self.assertEqual(self._issues(text), [])

    def test_halfwidth_note_also_masked(self):
        text = "见 Calchi 2023(译注：上游作 Calchi 2020。)\n"
        self.assertEqual(self._issues(text), [])

    def test_section_carrier_satisfies_errata(self):
        # ADR-0065：承载改节级——正文干净、节内条目引用错字形，即合规
        text = ("见 Calchi 2023。\n\n## 译者注释\n\n"
                "① 位置：首段。上游正文作 Calchi 2020，系年份笔误，译文从文献表。\n")
        self.assertEqual(self._issues(text), [])

    def test_body_wrong_form_with_section_still_reported(self):
        text = ("正文仍作 Calchi 2020。\n\n## 译者注释\n\n"
                "① 位置：首段。上游正文作 Calchi 2020，系年份笔误。\n")
        self.assertEqual(len(self._issues(text)), 1)


class TestNoteSection(unittest.TestCase):
    """译者注释节锚点（ADR-0065）：节非强制；存在即查对称、连续、位次、锚点形态。"""

    def _issues(self, text):
        import check_pairs
        out = []
        check_pairs.check_note_anchor("x/demo.md", text, out)
        return [i for i in out if i["rule"] == "note-anchor"]

    def _full(self, body_anchors, entries):
        return ("# 测试条 (Author)\n\n%s\n\n## 参考文献\n\n[^k]: Book.\n\n"
                "## 学术工具\n\n## 其他网络资源\n\n## 相关词条\n\n## 脚注\n\n"
                "[^note-1]: note.\n\n## 译者注释\n\n%s\n" % (body_anchors, entries))

    def test_no_section_no_anchor_clean(self):
        self.assertEqual(self._issues("# 测试条 (Author)\n\n正文没有锚点。\n"), [])

    def test_symmetric_clean(self):
        text = self._full("第一句。① 第二句。②",
                          "① 位置：首段。上游作“x”，系排印；译文按“x”处理。\n"
                          "② 位置：次段。上游作“y”；译文按“y”处理。\n")
        self.assertEqual(self._issues(text), [])

    def test_empty_section_rejected(self):
        text = self._full("没有锚点。", "")
        self.assertEqual(len(self._issues(text)), 1)

    def test_asymmetric_rejected(self):
        text = self._full("第一句。①", "① 位置：首段。说明。\n② 位置：次段。说明。\n")
        self.assertEqual(len(self._issues(text)), 1)

    def test_broken_sequence_rejected(self):
        text = self._full("第一句。① 第二句。③",
                          "① 位置：首段。说明。\n③ 位置：次段。说明。\n")
        self.assertGreaterEqual(len(self._issues(text)), 1)

    def test_anchor_must_hug_sentence_end(self):
        text = self._full("一句① 又一句。②", "① 位置：首段。说明。\n② 位置：次段。说明。\n")
        self.assertEqual(len(self._issues(text)), 1)

    def test_anchor_without_section_rejected(self):
        self.assertEqual(len(self._issues("# 测试条 (Author)\n\n一句。①\n")), 1)

    def test_blockquote_and_footnote_defs_ignored(self):
        text = self._full("> 引文里不应计锚 ①\n\n[^k]: 定义行 ②\n\n第一句。①",
                          "① 位置：首段。说明。\n")
        self.assertEqual(self._issues(text), [])

class TestGateStateScope(unittest.TestCase):
    """第 13 项状态感知（ADR-0063）：只有 ≥rv-01 的件硬拦，其余告警不拦。"""

    def _run(self, state):
        import check_pairs as cp
        old_state, old_file, old_out = cp._task_state, cp.check_file, sys.stdout
        cp._task_state = lambda p: state
        cp.check_file = lambda p: [{"path": p, "line": 0, "rule": "tail-order", "detail": "x"}]
        buf = io.StringIO()
        sys.stdout = buf
        try:
            rc = cp.main(["--gate", "a/x.md"])
        finally:
            cp._task_state, cp.check_file, sys.stdout = old_state, old_file, old_out
        return rc, json.loads(buf.getvalue())

    def test_in_scope_blocks(self):
        rc, out = self._run("rv-02_checked")
        self.assertEqual(rc, 1)
        self.assertEqual(out["gate"]["hard_in_scope"], 1)

    def test_s24_state_blocks(self):
        rc, _out = self._run("rv-01_checked")
        self.assertEqual(rc, 1)

    def test_out_of_scope_warns(self):
        rc, out = self._run("cleared")
        self.assertEqual(rc, 0)
        self.assertEqual(out["gate"]["out_of_scope_warn"], 1)

    def test_no_task_warns(self):
        rc, out = self._run(None)
        self.assertEqual(rc, 0)
        self.assertEqual(out["gate"]["out_of_scope_warn"], 1)


if __name__ == "__main__":
    unittest.main()

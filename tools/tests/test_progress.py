# -*- coding: utf-8 -*-
"""progress.py 的 W4 切读面单元测试：验证 load_journal 折叠与核心段完成判定。

不碰真实 journal/，用临时目录注入。核心断言：进度读数只认 journal 的 pass
事件，与 tasks 的 state 游标无关（ADR-0068 W4）。
"""
import json
import os
import tempfile
import unittest

from tools import progress


def _write_ndjson(dirpath, slug, events):
    letter = slug[0] if slug and slug[0].isalnum() else "0"
    sub = os.path.join(dirpath, letter)
    os.makedirs(sub, exist_ok=True)
    path = os.path.join(sub, slug + ".ndjson")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for e in events:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")


class TestLoadJournal(unittest.TestCase):
    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self._dir.cleanup()

    def test_core_done_folds_pass_set(self):
        # 一个走完全核心段、一个只到 s1
        _write_ndjson(self._dir.name, "a-full", [
            {"type": "lock", "sha256": "0" * 64},
            {"type": "pass", "node": "draft"},
            {"type": "pass", "node": "s1"},
            {"type": "pass", "node": "s2"},
            {"type": "pass", "node": "S3"},
            {"type": "pass", "node": "R1"},
            {"type": "pass", "node": "R2"},
            {"type": "pass", "node": "R3"},
        ])
        _write_ndjson(self._dir.name, "b-part", [
            {"type": "pass", "node": "draft"},
            {"type": "pass", "node": "s1"},
        ])
        _write_ndjson(self._dir.name, "c-idle", [
            {"type": "import", "synthetic": True, "basis": "state:pending"},
        ])

        passed, node_count = progress.load_journal(self._dir.name)

        self.assertEqual(set(passed), {"a-full", "b-part", "c-idle"})
        # a-full 核心段完成，b-part 在途，c-idle 未开工
        core_done = [s for s, d in passed.items() if progress.CORE <= d]
        self.assertEqual(core_done, ["a-full"])
        self.assertEqual(node_count.get("s1"), 2)
        self.assertEqual(node_count.get("R3"), 1)

    def test_empty_journal_returns_empty(self):
        passed, node_count = progress.load_journal(self._dir.name)
        self.assertEqual(passed, {})
        self.assertEqual(node_count, {})

    def test_ignore_non_pass_events(self):
        _write_ndjson(self._dir.name, "x-mixed", [
            {"type": "rework", "from_node": "s2.4"},
            {"type": "pass", "node": "draft"},
            {"type": "lock", "sha256": "1" * 64},
        ])
        passed, _ = progress.load_journal(self._dir.name)
        self.assertEqual(passed["x-mixed"], {"draft"})


class TestCountSkeletons(unittest.TestCase):
    """账背面统计：内容状态（骨架／有正文）× 是否在账（有 journal）。

    动机：进度五项的分母是 journal 词条，而 SUMMARY 声明的重译对象是全库正式
    词条；差额（仅标题骨架）此前不出现在任何一行，完成度易被误读为占全库比例。
    """

    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()
        root = self._dir.name
        lines = ["# SUMMARY", "", "## a", ""]
        # 四类：骨架在账内、骨架在账外、有正文、别名与占位（不计入 formal）
        cases = [("a-inledger-skel", False, "linked"),
                 ("a-offledger-skel", False, "linked"),
                 ("a-with-body", True, "linked"),
                 ("a-alias", True, "alias"),
                 ("a-mother", True, "mother")]
        for slug, has_body, kind in cases:
            sub = os.path.join(root, "a")
            os.makedirs(sub, exist_ok=True)
            body = ("# 标题 Title (Author)\n\n"
                    + ("哲学论证的内容段落，足够长以过阈值，" * 12 if has_body else ""))
            with open(os.path.join(sub, slug + ".md"), "w",
                      encoding="utf-8", newline="\n") as f:
                f.write(body)
            if kind == "linked":
                lines.append("* [标题 Title (Author)](a/%s.md)" % slug)
            elif kind == "alias":
                lines.append("* \\*标题——见别处 (X — see Y)")
            else:
                lines.append("* \\*分类名")
        with open(os.path.join(root, "SUMMARY.md"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines) + "\n")

    def tearDown(self):
        self._dir.cleanup()

    def test_only_linked_nonalias_counted(self):
        s = progress.count_skeletons(journal_slugs=set(), root=self._dir.name)
        self.assertEqual(s["formal"], 3)   # 别名与占位母行不入 formal

    def test_skeleton_and_body_split(self):
        s = progress.count_skeletons(journal_slugs=set(), root=self._dir.name)
        self.assertEqual(s["skeleton"], 2)
        self.assertEqual(s["body"], 1)

    def test_onledger_offledger_split(self):
        s = progress.count_skeletons(journal_slugs={"a-inledger-skel"},
                                     root=self._dir.name)
        self.assertEqual(s["skeleton_onledger"], 1)
        self.assertEqual(s["skeleton_offledger"], 1)

    def test_identity_sum(self):
        s = progress.count_skeletons(journal_slugs=set(), root=self._dir.name)
        self.assertEqual(s["skeleton"], s["skeleton_onledger"] + s["skeleton_offledger"])
        self.assertEqual(s["formal"], s["skeleton"] + s["body"])


if __name__ == "__main__":
    unittest.main()


class TestLoadBackfillSlugs(unittest.TestCase):
    """回补标记的识别：只认 note=backfill: 的 pass（specs/052）。"""

    def setUp(self):
        self._dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self._dir.cleanup()

    def test_marks_only_backfill_passes(self):
        _write_ndjson(self._dir.name, "a-bf", [
            {"type": "pass", "node": "s0", "note": "backfill:2026-11-19（现行判据重算）"},
        ])
        _write_ndjson(self._dir.name, "b-plain", [
            {"type": "pass", "node": "s0"},
            {"type": "pass", "node": "s1", "note": "常规推进"},
        ])
        _write_ndjson(self._dir.name, "c-fail", [
            {"type": "fail", "node": "s0", "note": "backfill:2026-11-19", "reason": "x"},
        ])
        self.assertEqual(progress.load_backfill_slugs(self._dir.name), {"a-bf"})

    def test_missing_dir_returns_empty(self):
        self.assertEqual(progress.load_backfill_slugs(os.path.join(self._dir.name, "nope")), set())

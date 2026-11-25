# -*- coding: utf-8 -*-
"""术语概念层校验单测（ADR-0084 D5=B）。"""
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_term_concepts import check, rows  # noqa: E402


REG = """| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 此在 | Dasein | 此在 | a/x | ADR | 2026-12-02 |
| 旧词 | old | 旧词 | a/y | ADR | 2026-11-01 |
"""

CON = """| 键 | 定义 | 学科域 | 概念关系 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 旧词 | 旧定义 | 哲学 | — | ADR | 2026-11-01 |
"""


class TestTermConcepts(unittest.TestCase):
    def _write(self, text):
        f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        f.write(text)
        f.close()
        self.addCleanup(os.unlink, f.name)
        return f.name

    def test_new_term_without_concept_is_reported(self):
        missing = check(rows(self._write(REG)), rows(self._write(CON)), "2026-12-01")
        self.assertEqual(missing, [("此在", "2026-12-02")])

    def test_old_term_not_retroactive(self):
        reg = """| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 旧词 | old | 旧词 | a/y | ADR | 2026-11-01 |
"""
        self.assertEqual(check(rows(self._write(reg)), rows(self._write(CON)), "2026-12-01"), [])

    def test_concept_row_requires_definition_and_domain(self):
        reg = """| 键 | 原文 | 译法 | 首现 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 空定义 | x | 空定义 | a/z | ADR | 2026-12-03 |
"""
        con = """| 键 | 定义 | 学科域 | 概念关系 | 依据 | 裁定日期 |
| --- | --- | --- | --- | --- | --- |
| 空定义 |  | 哲学 | — | ADR | 2026-12-03 |
"""
        self.assertEqual(check(rows(self._write(reg)), rows(self._write(con)), "2026-12-01"),
                         [("空定义", "2026-12-03")])


if __name__ == "__main__":
    unittest.main()

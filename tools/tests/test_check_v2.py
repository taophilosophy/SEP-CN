# -*- coding: utf-8 -*-
"""流程 v2 聚合校验门（T175 P1）。"""
import os
import sys
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools import check_v2  # noqa: E402


class _Result:
    def __init__(self, code, out=""):
        self.returncode = code
        self.stdout = out
        self.stderr = ""


class TestCheckV2(unittest.TestCase):
    def test_commands_complete(self):
        self.assertEqual(len(check_v2.COMMANDS), 6)
        self.assertTrue(check_v2.COMMANDS[0][0].endswith("term_tbx.py"))

    def test_run_reports_failure_and_success(self):
        old = check_v2.subprocess.run
        try:
            check_v2.subprocess.run = lambda *a, **k: _Result(1, "bad")
            self.assertTrue(check_v2.run([("x.py",)]))
            check_v2.subprocess.run = lambda *a, **k: _Result(0, "ok")
            self.assertEqual(check_v2.run([("x.py",)]), [])
        finally:
            check_v2.subprocess.run = old


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""check_stages 判据登记表核对单测（ADR-0068：pipeline.json 判据唯一事实源）。"""
import io
import json
import os
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO)

from tools.check_stages import load_pipeline, main  # noqa: E402


def _run_main(args):
    old = sys.argv
    sys.argv = ["check_stages.py"] + args
    try:
        return main()
    finally:
        sys.argv = old


class CheckStagesTest(unittest.TestCase):

    def test_pipeline_valid(self):
        """rules/pipeline.json 应全绿（11 项）。"""
        self.assertEqual(_run_main([]), 0)

    def test_negative_dual_gate(self):
        """构造判据双硬拦，S2 应失败。"""
        pipe = load_pipeline()
        nodes = pipe["nodes"]
        for n in nodes:
            if n["id"] == "s1":
                n["criteria"] = ["check_pairs", "check_style"]
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8", newline="\n") as f:
            json.dump(pipe, f, ensure_ascii=False, indent=1)
            path = f.name
        try:
            self.assertEqual(_run_main(["--pipe", path]), 1)
        finally:
            os.remove(path)

    def test_negative_break_chain(self):
        """构造断链（双链首），S1 应失败。"""
        pipe = load_pipeline()
        for n in pipe["nodes"]:
            if n["id"] == "P3":
                n["prev"] = None
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8", newline="\n") as f:
            json.dump(pipe, f, ensure_ascii=False, indent=1)
            path = f.name
        try:
            self.assertEqual(_run_main(["--pipe", path]), 1)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()

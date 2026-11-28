#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""流程 v2 校验聚合门（T175 P1；check_all GATES）。

依次运行 T172–T175 的六个校验器；任一失败即退出 1。
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMANDS = (
    ("tools/term_tbx.py", "--check", "baseline/termbase-sample.tbx"),
    ("tools/check_risk_matrix.py",),
    ("tools/check_model_registry.py",),
    ("tools/check_qa_scorecard.py",),
    ("tools/check_governance.py",),
    ("tools/check_t175.py",),
)


def run(commands=COMMANDS):
    failures = []
    for cmd in commands:
        path = os.path.join(ROOT, cmd[0])
        r = subprocess.run([sys.executable, path] + list(cmd[1:]), cwd=ROOT,
                           capture_output=True, text=True)
        if r.returncode != 0:
            out = (r.stdout or "") + (r.stderr or "")
            failures.append("%s -> %s" % (" ".join(cmd), out.strip()[-600:]))
    return failures


def main():
    failures = run()
    if failures:
        for item in failures:
            print("[FAIL] " + item)
        return 1
    print("[OK] 流程 v2 校验 6 项全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""一键全量合规复核（用户 2026-10-27 指令：新增一整套流程确保项目整体符合
哲学学术规范并落地；收工前/推审前跑一次，输出逐项门禁结果）。

覆盖（与 checks.yml CI 一致，另含需本地数据的项）：
  check_summary / check_mulu_s / check_doc_size / check_junk / check_terms /
  check_academic（词条+任务版本钉）/ 单元测试；
  可选 --all：加 baseline_audit（依赖本地 en/ 原始物，gitignore 不入 CI）与
  compare 全量对比（依赖网络，默认不跑）。

用法:
  python tools/check_all.py [--all] [--quiet]
输出: 人读逐项结果走 stdout；退出码 0 全绿 / 1 有失败。
"""
import argparse
import io
import os
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GATES = [
    ("SUMMARY 结构审计", "check_summary.py", False),
    ("分类目录对应性", "check_mulu_s.py", False),
    ("单体文件大小", "check_doc_size.py", False),
    ("垃圾与产物入库", "check_junk.py", False),
    ("术语一致性", "check_terms.py", False),
    ("哲学学术规范", "check_academic.py", False),
]
OPTIONAL = [
    ("基线完整性审计（本地 en/）", "baseline_audit.py", False),
]


def run(name, script):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", script)],
                       cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="加本地数据项（baseline_audit）")
    ap.add_argument("--quiet", action="store_true", help="只输出失败项与汇总")
    args = ap.parse_args(argv)

    # 七项门禁相互独立，并行执行（能并行的并行）
    from concurrent.futures import ThreadPoolExecutor
    results = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futs = {pool.submit(run, name, script): name for name, script, _ in GATES}
        for fut, name in futs.items():
            rc, out = fut.result()
            results.append((name, rc, out))
    for name, rc, out in results:
        if not args.quiet or rc:
            print("[%s] %s%s" % ("OK " if rc == 0 else "FAIL", name,
                                 "" if rc == 0 else "\n" + out[-1200:]))

    # 单元测试
    r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tools/tests"],
                       cwd=ROOT, capture_output=True, text=True)
    results.append(("管线单元测试", r.returncode, (r.stdout + r.stderr).strip()))
    if not args.quiet or r.returncode:
        print("[%s] 管线单元测试" % ("OK " if r.returncode == 0 else "FAIL"))

    if args.all:
        for name, script, _ in OPTIONAL:
            rc, out = run(name, script)
            results.append((name, rc, out))
            print("[%s] %s" % ("OK " if rc == 0 else "WARN", name))

    failed = [n for n, rc, _ in results if rc not in (0,)]
    print("\n== 汇总：%d 项，失败 %d%s" % (len(results), len(failed),
                                          ("：" + "、".join(failed)) if failed else "，全绿"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

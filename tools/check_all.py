# -*- coding: utf-8 -*-
"""一键全量合规复核（用户 2026-10-27 指令：新增一整套流程确保项目整体符合
哲学学术规范并落地；收工前/推审前跑一次，输出逐项门禁结果）。

覆盖（与 checks.yml CI 一致，另含需本地数据的项；2026-11-17 增第 11 项转换保真，specs/039 P9；
2026-11-17 增目录布局一致性，ADR-0067）：
  check_summary / check_layout（layout.json 单一源，L1–L4） / check_stages（pipeline.json 判据表，S1–S4） /
  check_mulu_s / check_doc_size /
  check_junk / check_images / check_terms / check_quotes / check_academic（词条+任务版本钉）/
  check_math_zh（译文侧公式体例，021 九类，D26 接线）/
  divergence（原始物分歧账，ADR-0045：en/ 静默改动未登记即红）/ 单元测试；
  可选 --all：加 baseline_audit（依赖本地 en/ 原始物）、divergence --deep
  （base_commit 的 git blob 复算，需完整历史）与 compare 全量对比
  （依赖网络，默认不跑）。

用法:
  python tools/check_all.py [--all] [--quiet]
  python tools/check_all.py --list-gates   # 输出 CI 门禁矩阵 JSON（checks.yml 的 strategy 数据源）
输出: 人读逐项结果走 stdout；退出码 0 全绿 / 1 有失败。

门禁清单是本仓 CI 的唯一事实源：`.github/workflows/checks.yml` 不抄命令，
用 `--list-gates` 的 JSON 生成矩阵作业（每项一个作业，红灯即指向具体门禁）。
新增门禁只改 GATES，CI 自动跟随（ADR-0061）。
"""
import argparse
import io
import json
import os
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (人读名称, 矩阵键, 命令)。命令相对仓库根：门禁走 tools/，单元测试走模块。
# 可判性四件套登记（rules/08 §14；specs/040 F-10）：机检谓词＝命令本身；预期
# 命中数＝硬违例 0（常态全绿；fidelity 预期 no-baseline 2 件历史孤儿豁免不拦，
# specs/039 P9；layout 首次全量预期 L2=0/L3=0/L4=0，L1 恒 0）；幂等＝全部只读判官
# （ADR-0063 判定权表）；一行回退＝git revert 引入该门禁的提交（GATES 删行即撤，
# CI 矩阵自动跟随）。
GATES = [
    ("SUMMARY 结构审计", "summary", "tools/check_summary.py"),
    ("目录布局一致性", "layout", "tools/check_layout.py"),
    ("判据登记表一致性", "stages", "tools/check_stages.py"),
    ("分类目录对应性", "mulu", "tools/check_mulu_s.py"),
    ("单体文件大小", "docsize", "tools/check_doc_size.py"),
    ("垃圾与产物入库", "junk", "tools/check_junk.py"),
    ("图片引用完整性", "images", "tools/check_images.py --gate"),
    ("术语一致性", "terms", "tools/check_terms.py"),
    ("直角引号总检", "quotes", "tools/check_quotes.py"),
    ("哲学学术规范", "academic", "tools/check_academic.py"),
    ("公式体例总检", "mathzh", "tools/check_math_zh.py --strict"),
    ("原始物分歧账", "divergence", "tools/divergence.py verify"),
    ("转换保真（yuanwen≡基线）", "fidelity", "tools/check_yuanwen_fidelity.py --gate"),
    ("中文体例归一（s2.4 三轴结构面）", "style", "tools/check_pairs.py --gate --all"),
]
UNIT_TESTS = ("管线单元测试", "unittest", "-m unittest discover -s tools/tests")
OPTIONAL = [
    ("基线完整性审计（本地 en/）", "tools/baseline_audit.py", False),
    ("英文镜像深度复核（本地 en/）", "tools/en_integrity.py --all --quiet", False),
    ("原始物分歧深核（git 历史）", "tools/divergence.py verify --deep", False),
]


def run(cmd):
    """执行仓库根相对的命令串（如 "tools/check_images.py --gate"），返回退出码与合并输出。"""
    r = subprocess.run([sys.executable] + cmd.split(),
                       cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def gate_matrix():
    """CI 门禁矩阵数据源（checks.yml 的 plan 作业消费）：每项 key/name/run。

    run 以 `python` 书写（GitHub Actions ubuntu runner 的解释器名），与本地
    sys.executable 无关；顺序即 GATES 顺序，末尾附单元测试项。
    """
    items = [{"key": key, "name": name, "run": "python " + cmd} for name, key, cmd in GATES]
    items.append({"key": UNIT_TESTS[1], "name": UNIT_TESTS[0], "run": "python " + UNIT_TESTS[2]})
    return items


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="加本地数据项（baseline_audit）")
    ap.add_argument("--quiet", action="store_true", help="只输出失败项与汇总")
    ap.add_argument("--list-gates", action="store_true", dest="list_gates",
                    help="输出 CI 门禁矩阵 JSON（单行，供 GITHUB_OUTPUT）后退出")
    args = ap.parse_args(argv)

    if args.list_gates:
        # 单行紧凑 JSON：checks.yml 直接写入 GITHUB_OUTPUT 再 fromJSON 展开矩阵
        sys.stdout.write(json.dumps({"include": gate_matrix()},
                                    ensure_ascii=False, separators=(",", ":")))
        return 0

    # 十项门禁相互独立，并行执行（能并行的并行）
    from concurrent.futures import ThreadPoolExecutor
    results = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futs = {pool.submit(run, cmd): name for name, _key, cmd in GATES}
        for fut, name in futs.items():
            rc, out = fut.result()
            results.append((name, rc, out))
    for name, rc, out in results:
        if not args.quiet or rc:
            print("[%s] %s%s" % ("OK " if rc == 0 else "FAIL", name,
                                 "" if rc == 0 else "\n" + out[-1200:]))

    # 单元测试
    name, _key, cmd = UNIT_TESTS
    rc, out = run(cmd)
    results.append((name, rc, out))
    if not args.quiet or rc:
        print("[%s] %s" % ("OK " if rc == 0 else "FAIL", name))

    if args.all:
        for name, cmd, _ in OPTIONAL:
            rc, out = run(cmd)
            results.append((name, rc, out))
            print("[%s] %s" % ("OK " if rc == 0 else "WARN", name))

    failed = [n for n, rc, _ in results if rc not in (0,)]
    print("\n== 汇总：%d 项，失败 %d%s" % (len(results), len(failed),
                                          ("：" + "、".join(failed)) if failed else "，全绿"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

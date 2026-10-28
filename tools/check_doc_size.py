#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""单体文件大小门禁（ADR-0004 + 2026-10-27 规则文本专用阈值）。

叙事/规则/规格/指南类 markdown 单文件超过阈值（1000 行或 100KB）任一，
必须按文件夹拆分：X.md → X/index.md + 按节/附录归类的子文件。
约束性规则（rules/0X.md）适用更严阈值（300 行或 30KB）：超过即按主题拆分为
目录 rules/0X/，每文件一主题，分别存放具体规则（rules/README 规则地图同步）。
SEP 词条本体不在管辖范围；数据登记册与工具生成物豁免（见 ADR-0004 豁免表）。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMIT_LINES = 1000
LIMIT_BYTES = 100 * 1024

# 规则文本专用更严阈值：约束性规则 rules/0X.md 超 300 行或 30KB 任一即按主题拆目录
RULE_LIMIT_LINES = 300
RULE_LIMIT_BYTES = 30 * 1024
RULE_FILES = re.compile(r"^rules/0[1-9][^/]*\.md$")

# 扫描根：根级散页 + 叙事/规则/规格/指南目录；词条本体目录（a–z、集群目录、en/、yuanwen/）不扫
SCAN_DIRS = ("rules", "specs", "qian-yan", "guan-yu", "fang-fa-lun", "jian-yi-shu", ".specify")

# 豁免：单一事实源登记册（工具按单文件解析，拆分须先走 spec 改解析器）与工具生成物
EXEMPT = {
    "SUMMARY.md",
    "mu-lu-s.md",
    "yi-zhe-shuo-ming.md",
    "ren-ming-biao.md",  # ADR-0012 人名登记册，同性质豁免
    "PROGRESS.md",
    "qian-yan/ci-hui-biao.md",
}


def limits_for(rel: str) -> tuple[int, int]:
    if RULE_FILES.match(rel):
        return RULE_LIMIT_LINES, RULE_LIMIT_BYTES
    return LIMIT_LINES, LIMIT_BYTES


def over_limit(lines: int, size: int, limits: tuple[int, int]) -> bool:
    ll, lb = limits
    return lines > ll or size > lb


def iter_docs(root: Path = ROOT):
    yield from sorted(root.glob("*.md"))
    for name in SCAN_DIRS:
        base = root / name
        if base.is_dir():
            yield from sorted(base.rglob("*.md"))


def scan(root: Path = ROOT):
    """返回 [(相对路径, 行数, 字节数)]，按字节数降序。"""
    rows = []
    for path in iter_docs(root):
        data = path.read_bytes()
        rows.append((path.relative_to(root).as_posix(), data.count(b"\n"), len(data)))
    rows.sort(key=lambda r: r[2], reverse=True)
    return rows


def main() -> int:
    rows = scan()
    violations = []
    for rel, lines, size in rows:
        if rel in EXEMPT:
            continue
        ll, lb = limits_for(rel)
        if lines > ll or size > lb:
            violations.append((rel, lines, size, (ll, lb)))

    print(
        f"单体文件门禁（ADR-0004 + 规则文本阈值）：扫描 {len(rows)} 个 markdown，"
        f"通用阈值 {LIMIT_LINES} 行 / {LIMIT_BYTES} 字节，"
        f"约束性规则 rules/0X 专用 {RULE_LIMIT_LINES} 行 / {RULE_LIMIT_BYTES} 字节"
    )
    print("体量前 10（* 为豁免登记册/生成物）：")
    for rel, lines, size in rows[:10]:
        mark = " *" if rel in EXEMPT else ""
        print(f"  {size:>9} 字节 {lines:>5} 行  {rel}{mark}")
    if violations:
        print(f"HARD ERRORS: {len(violations)}")
        for rel, lines, size, (ll, lb) in violations:
            why = []
            if lines > ll:
                why.append(f"{lines} 行 > {ll}")
            if size > lb:
                why.append(f"{size} 字节 > {lb}")
            if (ll, lb) == (RULE_LIMIT_LINES, RULE_LIMIT_BYTES):
                print(f"  超限：{rel}（{'、'.join(why)}）→ 按主题拆分为目录 rules/{rel.split('/')[1].split('-')[0]}/，规则地图同步")
            else:
                print(f"  超限：{rel}（{'、'.join(why)}）→ 按 ADR-0004 拆分为文件夹")
        return 1
    print("OK：受管文件全部达标")
    return 0


if __name__ == "__main__":
    sys.exit(main())

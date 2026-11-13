# -*- coding: utf-8 -*-
"""凭证驱动的术语表“原文”列回填器（specs/008／012，2026-11-13）。

用法：
  python specs/008-terminology-campaign/bin/apply_orig_column.py           # 干跑
  python specs/008-terminology-campaign/bin/apply_orig_column.py --apply   # 写回
  python specs/008-terminology-campaign/bin/apply_orig_column.py --ledger <TSV> --apply

护栏（rules/05）：按“键”精确定位、逐行身份追踪、只写第 2／5／6 列（原文／依据／
裁定日期）、覆盖式清除“原文列待考”旧措辞、依据列含本批凭证名即跳过（幂等）、
未匹配／多匹配／列数异常残余为 0 才允许写回。凭证只取权威辞书显式印出的
天城体词头，禁止用 IAST 等转写映射表推算（ADR-0030）。
退出码：0 成功／干跑完成；1 前置门未过（拒绝写回）。
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
REG = os.path.join(ROOT, 'shu-yu-biao.md')
DEFAULT_LEDGER = os.path.join(ROOT, 'specs', '008-terminology-campaign',
                              'results', 'orig-verify-2026-11-13.tsv')
DATE = '2026-11-13'
OLD_TAG = '原文列待考'


def load_ledger(path):
    rows = []
    with io.open(path, encoding='utf-8-sig', newline='') as f:
        header = f.readline()
        assert header.startswith('键\t'), '凭证表头异常'
        for line in f:
            line = line.rstrip('\n')
            if not line:
                continue
            cells = line.split('\t')
            assert len(cells) == 5, '凭证列数异常：%s' % cells[0]
            rows.append(cells)
    return rows


def short_basis(src):
    return src.split('；')[0].strip()[:56]


def main():
    argv = sys.argv[1:]
    apply = '--apply' in argv
    path = DEFAULT_LEDGER
    if '--ledger' in argv:
        p = argv[argv.index('--ledger') + 1]
        path = p if os.path.isabs(p) else os.path.join(ROOT, p)
    tag = os.path.basename(path)
    ledger = load_ledger(path)
    wanted = {r[0]: r for r in ledger}

    with io.open(REG, encoding='utf-8-sig', newline='') as f:
        lines = f.read().split('\n')

    found, problems = {}, []
    for i, line in enumerate(lines):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if not cells or cells[0] == '键' or set(cells[0]) <= set('-: '):
            continue
        if cells[0] not in wanted:
            continue
        if cells[0] in found:
            problems.append('多匹配：%s（行 %d 与行 %d）' % (cells[0], found[cells[0]] + 1, i + 1))
            continue
        if len(cells) != 6:
            problems.append('列数异常：%s（行 %d，%d 列）' % (cells[0], i + 1, len(cells)))
            continue
        found[cells[0]] = i
    for key in wanted:
        if key not in found:
            problems.append('未匹配：%s' % key)

    plan = []
    for r in ledger:
        key = r[0]
        if key not in found:
            continue
        i = found[key]
        cells = [c.strip() for c in lines[i].strip('|').split('|')]
        if tag in cells[4]:
            plan.append((key, i + 1, None, '已回填，跳过（幂等）'))
            continue
        basis = cells[4].replace(OLD_TAG + '；', '').replace('；' + OLD_TAG, '')
        basis = basis.replace(OLD_TAG, '').rstrip('；; ')
        new_basis = '%s；原文列联网查证：%s（%s 查，凭证 %s）' % (
            basis, short_basis(r[2]), DATE, tag)
        new_cells = list(cells)
        new_cells[1], new_cells[4], new_cells[5] = r[1], new_basis, DATE
        plan.append((key, i + 1, '| %s |' % ' | '.join(new_cells), '待写'))

    print('凭证 %d 行；匹配 %d 行；残余 %d 项' % (len(ledger), len(found), len(problems)))
    for p in problems:
        print('  [残余] ' + p)
    for key, lineno, _new, status in plan:
        print('  %-34s | 行 %-5d | → %-18s | %s' % (key[:34], lineno, wanted[key][1][:18], status))
    if problems:
        print('前置门未过：残余不为 0，拒绝写回。')
        return 1
    if not apply:
        print('干跑完成；加 --apply 写回。')
        return 0
    touched = 0
    for key, lineno, new_line, status in plan:
        if new_line is None:
            continue
        lines[lineno - 1] = new_line
        touched += 1
    with io.open(REG, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(lines))
    print('写回 %d 行 → %s' % (touched, REG))
    return 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""凭证驱动的人名表“籍属／生卒”回填器（specs/013，2026-11-13）。

用法：
  python specs/013-person-attribution/bin/apply_person_meta.py            # 干跑（默认，读首轮凭证）
  python specs/013-person-attribution/bin/apply_person_meta.py --apply    # 写回
  python specs/013-person-attribution/bin/apply_person_meta.py --ledger <凭证TSV> --apply
      # 指定批次凭证；幂等标记按凭证文件名自动生成，可多批续跑

护栏（rules/05 批量改写）：
  1. 只按“键”精确定位 ren-ming-biao.md 的数据行，逐行身份追踪；
  2. 只写第 4、5、7、8 列（籍属／生卒／依据／日期），其余列原样；
  3. 覆盖式写入：先清除上一会话无凭证措辞，再写凭证短注（幂等）；
  4. 写回前置门：未匹配／多匹配／形状异常的残余必须为 0，否则禁止写回；
  5. 依据列含本批凭证名即视为已回填，重跑不改（幂等）。

凭证：specs/013-person-attribution/results/verify-2026-11-13.tsv
退出码：0 成功／干跑完成；1 前置门未过（拒绝写回）。
"""
import datetime
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
REG = os.path.join(ROOT, 'ren-ming-biao.md')
DEFAULT_LEDGER = os.path.join(ROOT, 'specs', '013-person-attribution',
                              'results', 'verify-2026-11-13.tsv')
OLD_TAG = '籍属/生卒据学界通行（2026-11-13 补）'
DATE = os.environ.get('LEDGER_DATE') or datetime.date.today().isoformat()


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
            assert len(cells) == 6, '凭证列数异常：%s' % cells[0]
            rows.append(cells)
    return rows


def short_basis(src):
    """取权威源主名（首个全角括号前），供登记册依据列短注。"""
    return src.split('（')[0].strip().rstrip('，;；')


def main():
    argv = sys.argv[1:]
    apply = '--apply' in argv
    ledger_path = DEFAULT_LEDGER
    if '--ledger' in argv:
        p = argv[argv.index('--ledger') + 1]
        ledger_path = p if os.path.isabs(p) else os.path.join(ROOT, p)
    tag = os.path.basename(ledger_path)
    ledger = load_ledger(ledger_path)
    wanted = {r[0]: r for r in ledger}

    with io.open(REG, encoding='utf-8', newline='') as f:
        lines = f.read().split('\n')

    found = {}
    problems = []
    for i, line in enumerate(lines):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if not cells or cells[0] in ('人名', '—') or set(cells[0]) <= set('-: '):
            continue
        if cells[0] not in wanted:
            continue
        if cells[0] in found:
            problems.append('多匹配：%s（行 %d 与行 %d）' % (cells[0], found[cells[0]] + 1, i + 1))
            continue
        if len(cells) != 8:
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
        if tag in cells[6]:
            plan.append((key, i + 1, cells[3], cells[4], None, '已回填，跳过（幂等）'))
            continue
        basis = cells[6].replace('；' + OLD_TAG, '').replace(OLD_TAG, '').rstrip('；; ')
        new_basis = '%s；籍属/生卒联网查证：%s（%s 查，凭证 %s）' % (
            basis, short_basis(r[3]), DATE, tag)
        new_cells = list(cells)
        new_cells[3], new_cells[4], new_cells[6], new_cells[7] = r[1], r[2], new_basis, DATE
        plan.append((key, i + 1, cells[3], cells[4], '| %s |' % ' | '.join(new_cells), '待写'))

    print('凭证 %d 行；匹配 %d 行；残余 %d 项' % (len(ledger), len(found), len(problems)))
    for p in problems:
        print('  [残余] ' + p)
    for key, lineno, old_n, old_y, new_line, status in plan:
        print('  %s | 行 %d | %s / %s → %s / %s | %s'
              % (key[:44], lineno, old_n[:16], old_y[:14],
                 wanted[key][1][:16], wanted[key][2][:14], status))
    if problems:
        print('前置门未过：残余不为 0，拒绝写回。')
        return 1
    if not apply:
        print('干跑完成；加 --apply 写回。')
        return 0
    touched = 0
    for key, lineno, _a, _b, new_line, status in plan:
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

# -*- coding: utf-8 -*-
"""specs/034 依据列全等重复子句去重（rules/05 批量改写纪律）。

只动「依据」列（术语 6 列制第 5 列 / 人名 8 列制第 7 列，0 基 cells[4]/cells[6]）；
按「；/;」拆子句、全等重复保留首个；未变更行字节不动；幂等；守恒门=每行
删去的子句数恰等于全等重复数且其余列逐字节不变。

用法：python specs/034-register-dedup/bin/dedup_evidence.py [--apply]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, REPO)

from tools.register_lib import is_data_row, person_path, split_row, term_path  # noqa: E402

import tempfile  # noqa: E402

BASIS_IDX = {'shu-yu-biao.md': 4, 'ren-ming-biao.md': 6}


def dedup_basis(cell):
    """返回（新依据列, 删去的全等重复子句列表）；顺序保持首个出现位。"""
    clauses = [c.strip() for c in cell.replace('；', ';').split(';')]
    out, seen, dropped = [], set(), []
    for c in clauses:
        if c and c in seen:
            dropped.append(c)
            continue
        if c:
            seen.add(c)
        out.append(c)
    if not dropped:
        return cell, []
    new = '；'.join(c for c in out if c)
    if not new:
        return cell, dropped
    return new, dropped


def process(path, apply):
    name = os.path.basename(path)
    idx = BASIS_IDX[name]
    lines = open(path, encoding='utf-8').read().splitlines(True)
    out, changes, residual = [], [], 0
    for line in lines:
        s = line.rstrip('\n')
        if not s.startswith('|'):
            out.append(line)
            continue
        cells = split_row(s)
        if not is_data_row(cells) or len(cells) <= idx:
            out.append(line)
            continue
        new_basis, dropped = dedup_basis(cells[idx])
        if not dropped:
            out.append(line)
            continue
        # 守恒：删去数=全等重复数；非目标列逐字节不变
        rebuilt = '| ' + ' | '.join(cells[:idx] + [new_basis] + cells[idx + 1:]) + ' |'
        old_cells = [c.strip() for c in s.strip().strip('|').split('|')]
        intact = all(old_cells[i] == cells[i] for i in range(len(cells)) if i != idx)
        if not intact:
            residual += 1
            out.append(line)
            continue
        changes.append((s, rebuilt, dropped))
        out.append(rebuilt + '\n')
    print('%s：改动 %d 行，残余 %d' % (name, len(changes), residual))
    for old, new, dropped in changes:
        print('  - 删 %d 重复子句：%s' % (len(dropped), '；'.join(dropped)[:70]))
        print('    旧：%s' % old[:110])
        print('    新：%s' % new[:110])
    if residual:
        print('拒绝写回：残余≠0（rules/05 前置门）')
        return 1
    if not apply:
        print('干跑：未写盘')
        return 0
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.dedup.tmp')
    with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
        f.write(''.join(out))
    os.replace(tmp, path)
    print('已写回')
    return 0


def main(argv):
    apply = '--apply' in argv
    rc = 0
    for path in (term_path(), person_path()):
        rc |= process(path, apply)
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

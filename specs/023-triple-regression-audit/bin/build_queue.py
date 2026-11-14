# -*- coding: utf-8 -*-
"""023 Phase 2 审校队列构建：tasks 状态 ∈ drafted 及其后（A2 口径）。

输出 specs/023-triple-regression-audit/results/queue.md（人读）与 queue.json（机读）。
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT_DIR = os.path.join(ROOT, 'specs', '023-triple-regression-audit', 'results')

IN_SCOPE = {'drafted', 's1_checked', 's2_checked', 's3_checked',
            'r1_reviewed', 'r2_reviewed', 'r3_reviewed', 'done'}
# 018 已核 10 条（镜像轴沿用，译文轴照审）
AUDITED_018 = {'abduction', 'abelard', 'abilities', 'abner-burgos', 'abortion',
               'abrabanel', 'abhidharma', 'abraham-daud', 'abstract-objects',
               'abu-bakr-al-razi'}


def task_state(path):
    try:
        d = json.load(open(path, encoding='utf-8'))
    except Exception:
        return None, None
    if isinstance(d, list):
        d = next((x for x in reversed(d) if isinstance(x, dict) and x.get('state')), {})
    return d.get('state'), d


def zh_lines(slug):
    p = os.path.join(ROOT, slug[0], slug + '.md')
    if not os.path.isfile(p):
        return -1
    return sum(1 for ln in open(p, encoding='utf-8') if ln.strip())


def main():
    rows = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'tasks', '*', '*.json'))):
        slug = os.path.basename(p)[:-5]
        letter_dir = os.path.basename(os.path.dirname(p))
        if letter_dir in ('manifests',):
            continue
        state, d = task_state(p)
        if state not in IN_SCOPE:
            continue
        kind = (d or {}).get('kind', '')
        rows.append({
            'slug': slug, 'state': state, 'kind': kind,
            'zh_lines': zh_lines(slug),
            'prior_018': slug in AUDITED_018,
        })
    rows.sort(key=lambda r: r['slug'].lower())
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, 'queue.json'), 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, 'queue.md'), 'w', encoding='utf-8') as f:
        f.write('# 023 Phase 2 审校队列（%d 条，A2 口径）\n\n' % len(rows))
        f.write('| # | slug | 状态 | zh 行数 | 018 镜像轴已核 |\n')
        f.write('| ---- | ---- | ---- | ---- | ---- |\n')
        for i, r in enumerate(rows, 1):
            f.write('| %d | %s | %s | %d | %s |\n' % (
                i, r['slug'], r['state'], r['zh_lines'],
                '是' if r['prior_018'] else ''))
        f.write('\n> 接力规则：按序号推进；已审者打勾移入 ledger-<letter>.md 台账行。\n')
    print('共 %d 条；018 已核 %d 条' % (len(rows), sum(r['prior_018'] for r in rows)))
    from collections import Counter
    print('状态分布:', dict(Counter(r['state'] for r in rows)))
    stub = [r['slug'] for r in rows if 0 <= r['zh_lines'] <= 10]
    print('zh 非存根异常（≤10 行）:', stub[:10])


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""中文主形撞车扫描（只读，2026-11-25）。

术语登记册里不同英文键落成同一中文主形（取“（”前、去书名号）是常态：同形不同义、
同概念异语都该分行（rules/03、ADR-0048）。风险在于**没有裁定痕迹**的撞形——既没并键，
也没写“同形不同义／撞形豁免”一类说明，重译时等于二选一随机。

本脚本把撞形组按“组内是否每行都带裁定标记”分开，只输出无标记组，供逐组研判。
标记词表见 MARK；拉丁原文保留／保留原文 两族是体例标签（多行共用同一标签），
用 STYLE_LABEL 排除，不参与撞形判定。

用法：
  python -I specs/058-term-full-reextraction/bin/audit_zh_collisions.py [--all]
产物：
  specs/058-term-full-reextraction/results/zh-collision-residue-2026-11-25.tsv
"""
import argparse
import collections
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

MARK = ('撞形豁免', '同形不同义', '同形异义', '同概念异语', '多义分行', '同键多义', '语境区分',
        '分行', '非同一概念', '分列', '按域分用', '按原文分列')
STYLE_LABEL = ('拉丁原文保留', '保留原文', '音译保留原名')
SKIP_KEY = ('键', '---')


def adjudicated(c):
    """该行是否留了裁定痕迹：依据带标记词，或译法带域/语种括注（“亦作”不算）。"""
    if any(mk in c[4] for mk in MARK):
        return True
    for seg in c[2].split('（')[1:]:
        seg = seg.split('）')[0].strip()
        if seg and not seg.startswith('亦作'):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--all', action='store_true', help='输出全部撞形组，不只无标记组')
    ap.add_argument('--registry', default='shu-yu-biao.md')
    ap.add_argument('--out', default='specs/058-term-full-reextraction/results/'
                                    'zh-collision-residue-2026-11-25.tsv')
    a = ap.parse_args()

    groups = collections.defaultdict(list)
    for l in io.open(a.registry, encoding='utf-8'):
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6 or c[0] in SKIP_KEY or c[2] in ('—', ''):
            continue
        # 保留书名号：概念形“万民法”与书名形“《万民法》”在正文里不冲突，
        # 剥掉书名号会把书与概念判成撞形（2026-11-25 实测多组假阳性）。
        main_zh = c[2].split('（')[0].strip()
        if not main_zh or main_zh in STYLE_LABEL:
            continue
        groups[main_zh].append(c)

    rows, n_all, n_bare = [], 0, 0
    for zh, v in sorted(groups.items()):
        if len(v) < 2:
            continue
        n_all += 1
        marked = [adjudicated(c) for c in v]
        if all(marked):
            if not a.all:
                continue
        else:
            n_bare += 1
        for c, mk in zip(v, marked):
            rows.append((zh, c[0], c[2], 'marked' if mk else 'BARE', c[4][:80]))

    with io.open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('zh_main\tkey\tzh\tmark\tbasis_head\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print('撞形组 %d，无标记组 %d，输出行 %d → %s'
          % (n_all, n_bare, len(rows), a.out))
    return 0


if __name__ == '__main__':
    sys.exit(main())

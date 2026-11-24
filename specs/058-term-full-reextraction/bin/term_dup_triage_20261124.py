# -*- coding: utf-8 -*-
"""术语译法重复 13 组裁定：2 组真合并（单复数/同义），4 组补同形异义标注，余为已有撞形豁免。"""
import io, sys
sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, term_path

p = term_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and c[0]:
            idx.setdefault(norm_key_quote(c[0]), i)

def cells(i):
    return [x.strip() for x in lines[i].strip().strip('|').split('|')]

MERGES = [
 # 保留键, 删除键, 别名追加, 追加首现, 说明
 ('moral obligation', 'moral duties', 'moral duties', '语料回收（specs/058 全库提取）',
  '合并单复数同义键（2026-11-24 复核）；删除行依据“学界通行（specs/058 A 档直裁）”并入'),
 ('moral status', 'moral standing', 'moral standing', '语料回收（specs/058 全库提取）',
  '合并同义异形键（2026-11-24 复核）；standing 与 status 同指道德地位，删除行依据“学界通行（specs/058 A 档直裁）”并入'),
]
TAGS = [
 ('choice theory', '同形异义：choice theory 指理性选择/博弈论与决策论，与 selection theory（演化选择）异概念，按条分立'),
 ('selection theory', '同形异义：selection theory 指演化选择（亲属选择等），与 choice theory（理性选择）异概念，按条分立'),
 ('cognitive ability', '同形异义：cognitive ability 指能力（able），与 cognitive capacities（官能/容量）异概念，按条分立'),
 ('cognitive capacities', '同形异义：cognitive capacities 指认知官能/容量，与 cognitive ability（能力）异概念，按条分立'),
 ('divine nature', '同形异义：divine nature 为基督教神学通用语，与 ulūhiyya / ilāhiyya（伊斯兰神学“神性”）分属两传统，按条分立'),
 ('ulūhiyya / ilāhiyya', '同形异义：伊斯兰神学“神性”（伊本·泰米叶术语），与 divine nature（基督教通用语）分属两传统，按条分立'),
]

del_idx = set(); n = 0
for keep, drop, alias, slug, note in MERGES:
    ik, idp = idx[norm_key_quote(keep)], idx[norm_key_quote(drop)]
    c, d = cells(ik), cells(idp)
    c[1] = alias if c[1] in ('—', '') else c[1] + ' / ' + alias
    if slug not in c[3]:
        c[3] = c[3] + '；' + slug
    if note not in c[4]:
        c[4] = c[4].rstrip('；') + '；' + note + '（凭证 term-dup-triage-2026-11-24.md）'
    lines[ik] = '| ' + ' | '.join(c) + ' |'
    del_idx.add(idp); n += 1
    print('合并', drop, '->', keep)

for key, note in TAGS:
    i = idx[norm_key_quote(key)]
    c = cells(i)
    if note not in c[4]:
        c[4] = c[4].rstrip('；') + '；' + note + '（2026-11-24 复核，凭证 term-dup-triage-2026-11-24.md）'
    lines[i] = '| ' + ' | '.join(c) + ' |'
    print('标注', key)

lines = [l for i, l in enumerate(lines) if i not in del_idx]
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('merged=%d deleted=%d tagged=%d' % (n, len(del_idx), len(TAGS)))

# -*- coding: utf-8 -*-
"""人名译法重复 8 组裁定：4 组同人异键合并、4 组同形异人交叉标注。"""
import io, sys
sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 8 and c[0]:
            idx.setdefault(norm_key_quote(c[0]), i)

def cells(i):
    return [x.strip() for x in lines[i].strip().strip('|').split('|')]

# (保留键, 删除键, 新别名, 新籍属或None, 新生卒或None, 追加首现, 合并说明)
MERGES = [
 ('Abraham ibn Daud', 'Abraham Ibn-Dahoud', 'Abraham Ibn-Dahoud',
  '西班牙（科尔多瓦；后居托莱多）', '约1110–约1180', 'crescas',
  '合并同人异键：Ibn-Dahoud 为语料转写形，该行依据（SEP en/abraham-daud 首句、《崇高的信仰》转译）与 slug crescas 并入'),
 ('Bhāviveka', 'Bhāvaviveka', 'Bhāvaviveka / Bhavyaviveka',
  '古印度／中观派（自续派）', '约500–578', '语料回收（全目录）',
  '合并同人异键：Bhāvaviveka 为长写形，Bhavyaviveka 为藏译转写形，同一 Wikidata Q2357245；该行 slug 并入'),
 ('Davies, Stephen', 'Davies, Stephen / Stephen Davies', 'Stephen Davies',
  '新西兰／美学', None, '语料回收（specs/058 全库提取）',
  '合并同人异键：合写键与 “Stephen Davies” 重排形同指一人（分析美学，Q7609025）；该行 slug 并入'),
 ('Vidyānandin', 'Vidyānanda Pātrakesarisvāmin', 'Vidyānanda Pātrakesarisvāmin / विद्यानन्द',
  '古印度／耆那教', '约 9 世纪（约 850）', 'jayaraasi',
  '合并同人异键：长名形（SEP en/jayaraasi 括注 c. 850）与短形同指耆那教注家；该行 slug 与梵文形并入'),
]

del_idx = set(); n = 0
for keep, drop, alias, aff, dates, slug_add, note in MERGES:
    ik, idp = idx[norm_key_quote(keep)], idx[norm_key_quote(drop)]
    c = cells(ik); d = cells(idp)
    c[1] = alias if c[1] in ('—', '') else c[1] + ' / ' + alias
    if aff: c[3] = aff
    if dates: c[4] = dates
    c[5] = c[5] + '；' + slug_add if slug_add not in c[5] else c[5]
    if note not in c[6]:
        c[6] = c[6].rstrip('；') + '；2026-11-24 复核：' + note + '（凭证 people-dup-triage-2026-11-24.md）'
    lines[ik] = '| ' + ' | '.join(c) + ' |'
    del_idx.add(idp); n += 1
    print('合并', drop, '->', keep)

# 同形异人：交叉标注
TAGS = [
 ('Collins, John', '与 Collins, John (philosophy of language)（当代语言哲学家，Columbia）同译名异人（17 世纪数学通信枢纽 vs 当代），合法并存'),
 ('Collins, John (philosophy of language)', '与 Collins, John（17 世纪英国数学通信枢纽）同译名异人，合法并存'),
 ('Menger, Karl', '与经济学家 Menger, Carl（1840–1921，奥地利经济学派创始人）同译名异人（数学家 vs 经济学家），合法并存'),
 ('Helene', '与史诗人物 Helen of Troy 同译名异人（笛卡尔家仆 vs 神话人物），合法并存'),
 ('Davis, Stephen T.', '与新西兰分析美学家 Davies, Stephen（1950– ，Q7609025）同译名异人（Davis/Davies 异姓；宗教哲学 vs 美学），合法并存'),
 ('Davies, Stephen', '与美国宗教哲学家 Davis, Stephen T.（1940– ，GND 136192661）同译名异人（Davies/Davis 异姓），合法并存'),
]
for key, note in TAGS:
    i = idx[norm_key_quote(key)]
    c = cells(i)
    if note not in c[6]:
        c[6] = c[6].rstrip('；') + '；2026-11-24 复核：' + note + '（凭证 people-dup-triage-2026-11-24.md）'
    lines[i] = '| ' + ' | '.join(c) + ' |'
    print('标注', key)

lines = [l for i, l in enumerate(lines) if i not in del_idx]
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('merged=%d deleted=%d tagged=%d' % (n, len(del_idx), len(TAGS)))

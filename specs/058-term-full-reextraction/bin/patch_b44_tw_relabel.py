# -*- coding: utf-8 -*-
"""批 44：把“审定名词库（termonline-all·X）”里实为海峡两岸库的条目改正库名（2026-11-25）。

判据（纯本地，可用 `--dry-run` 只看不写）：
  行在审计表里为 tw-only；且本地缓存中“译法主形／亦作形”只出现在 standard 含“海峡两岸”
  的条目里、没有审定公布库同形条目 → 该行括号内所引就是对照库条目，库名误写为审定。

改写只动括号里的库名：`审定名词库（termonline-all·X）` → `海峡两岸名词对照库（termonline-all·X；非审定公布库）`；
`审定名词库（海峡两岸X…）` → `海峡两岸名词对照库（X…）`。
"""
import glob
import io
import json
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')
QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
TERMS = 'shu-yu-biao.md'
AUDIT = 'specs/058-term-full-reextraction/results/term-basis-pairing-2026-11-25.tsv'
REPORT = 'specs/058-term-full-reextraction/results/tw-relabel-b44-2026-11-25.tsv'
DATE = '2026-11-25'


def strong(s):
    s = re.sub(r"['’][sS]?\b", '', str(s or ''))
    s = unicodedata.normalize('NFKD', s.casefold())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '', s)


def main(dry=False):
    tw, audit_lib = {}, {}
    for p in glob.glob(os.path.join(QD, '*.json')):
        try:
            j = json.load(io.open(p, encoding='utf-8'))
        except Exception:
            continue
        for h in j.get('hits') or []:
            std = str(h.get('standard') or h.get('source') or '')
            if not h.get('cn'):
                continue
            k = strong(h.get('cn'))
            if '海峡两岸' in std:
                tw.setdefault(k, std)
            elif std and '百科' not in std and '标准' not in std:
                audit_lib.setdefault(k, std)
    verdict = {}
    for line in io.open(AUDIT, encoding='utf-8'):
        c = line.rstrip('\n').split('\t')
        if len(c) >= 3 and c[0] != 'key':
            verdict[c[0]] = c[2]

    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    rep, out, na, nb = [], [], 0, 0
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8 and verdict.get(cells[1].strip()) == 'tw-only':
                zh = cells[3].strip()
                forms = {strong(zh.split('（')[0].strip('《》'))}
                for x in re.findall(r'[“"]([^”"]{1,14})[”"]', zh):
                    forms.add(strong(x))
                forms = {f for f in forms if f}
                hit_tw = [f for f in forms if f in tw]
                hit_au = [f for f in forms if f in audit_lib]
                b = cells[5]
                if hit_tw and not hit_au:
                    b2, k1 = re.subn(r'审定名词库（海峡两岸([^）]*)）', r'海峡两岸名词对照库（\1；非审定公布库）', b)
                    b2, k2 = re.subn(r'审定名词库（termonline-all·([^）]*)）',
                                     r'海峡两岸名词对照库（termonline-all·\1；非审定公布库）', b2)
                    if k1 or k2:
                        cells[5] = b2
                        cells[6] = ' %s ' % DATE
                        line = '|'.join(cells)
                        na += k2
                        nb += k1
                        rep.append((cells[1].strip(), zh[:24], tw[hit_tw[0]],
                                    'paren' if k2 else 'tw-named'))
        out.append(line)
    if not rep:
        print('无候选')
        return
    if dry:
        print('候选 %d 行（括号型 %d、已名两岸型 %d）：' % (len(rep), na, nb))
        for r in rep:
            print(' | '.join(r))
        return
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    with io.open(REPORT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tzh\ttw_source\tform\n')
        for r in rep:
            f.write('\t'.join(r) + '\n')
    print('改写 %d 行（括号型 %d、已名两岸型 %d）→ %s' % (len(rep), na, nb, REPORT))


if __name__ == '__main__':
    main('--dry-run' in sys.argv)

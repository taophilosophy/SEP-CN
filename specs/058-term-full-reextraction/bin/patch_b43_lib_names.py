# -*- coding: utf-8 -*-
"""批 43：改正 19 行库名误称（2026-11-25）。

两类：
  A（18 行）“审定名词库（termonline-all·海峡两岸X名词，YYYY）” —— 该条来自**海峡两岸
     名词对照库**，不是审定公布库；改记为对照库，并注明非审定。
  B（1 行）“审定名词库（termonline-all·其他，2026-11-18 JWT 直连凭证）” —— 该条来自
     **其他来源数据库**（大数据百科术语辞典，界面复核所见）；改记来源名。

只动库名一处，其余文字不动。
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-25'

PAT_A = re.compile(r'审定名词库（termonline-all·海峡两岸([^）]*?)）')
REP_A = r'海峡两岸名词对照库（termonline-all·\1；非审定公布库）'
PAT_B = '审定名词库（termonline-all·其他，2026-11-18 JWT 直连凭证）'
REP_B = '其他来源数据库（termonline-all·大数据百科术语辞典，2026-11-18 JWT 直连凭证；2026-11-25 界面复核：审定公布库无此条）'


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    na = nb = 0
    out = []
    for line in lines:
        if line.startswith('|') and ('审定名词库（termonline-all·海峡两岸' in line or PAT_B in line):
            cells = line.split('|')
            if len(cells) >= 8:
                b = cells[5]
                b2, ka = PAT_A.subn(REP_A, b)
                b2, kb = b2.replace(PAT_B, REP_B), (PAT_B in b)
                if ka or kb:
                    cells[5] = b2
                    cells[6] = ' %s ' % DATE
                    line = '|'.join(cells)
                    na += 1 if ka else 0
                    nb += 1 if kb else 0
        out.append(line)
    if not (na or nb):
        raise SystemExit('无命中，中止')
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改库名：对照库 %d 行，其他来源库 %d 行' % (na, nb))


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""批 33 一次性补丁：人名表同人重复并键 4 组＋ADR-0022 占位译法归一（2026-11-25）。

同译名撞车扫描发现 12 组，其中 4 组是同人两行（法拉比、哈特、莫扎特、因陀罗菩提·乔答摩），
并键进信息更全的一行；其余 8 组为同姓异人或异名同译，各有注，不动。
另把 22 行译法列为“保留英文（无通行汉名）”占位的行改为英文原名形——ADR-0022 的口径是
“译法=保留的英文形”，绝大多数行正是这么填的，占位行与其口径不一，且会让词条人名索引
把这些行输出成无意义文本。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

P = 'ren-ming-biao.md'
# (keeper, absorbed, 合并后键, 合并后译法, 依据追加, 合并后籍属, 合并后生卒)
MERGES = [
    ('al-Fārābī / Al-Fârâbī / Abū Naṣr al-Fārābī', 'Al-Fārābī',
     'al-Fārābī / Al-Fârâbī / Al-Fārābī / Abū Naṣr al-Fārābī',
     '法拉比（亦作“阿尔·法拉比”“阿里·法拉比”）',
     '；2026-11-25 同人并键（旧键 Al-Fārābī，旧首现 语料回收（全目录）；其 Wikidata Q160460 生卒记 约872–950，'
     '与本行 c. 870–950 并存备查）',
     '中亚法拉布（今哈萨克斯坦）／伊斯兰哲学', 'c. 870–950（Wikidata 记 约872–950）'),
    ('Hart, H. L. A. / H. L. A. Hart', 'H.L.A. Hart',
     'Hart, H. L. A. / H. L. A. Hart',
     '哈特',
     '；2026-11-25 同人并键（旧键 H.L.A. Hart，旧首现 lawphil-theory，其译法原填“哈特（首现括注 H.L.A. Hart）”，'
     'GND gnd 118546155 凭证随行并入）',
     '英国／法哲学', '1907–1992'),
    ('Mozart', 'Mozart, Wolfgang Amadeus',
     'Mozart / Mozart, Wolfgang Amadeus',
     '莫扎特',
     '；2026-11-25 同人并键（旧键 Mozart, Wolfgang Amadeus，旧首现 aesthetic-testimony；全名汉译形'
     '“沃尔夫冈·阿马德乌斯·莫扎特”备查）',
     '奥地利（萨尔茨堡）／作曲家', '1756–1791'),
    ('Indrabhūti Gautama', 'Gautama (Indrabhūti)',
     'Indrabhūti Gautama / Gautama (Indrabhūti)',
     '因陀罗菩提·乔答摩',
     '；2026-11-25 同人并键（旧键 Gautama (Indrabhūti)，旧首现 jaina-philosophy）',
     '古印度（摩揭陀）／耆那教', '—'),
]

PLACEHOLDER = '保留英文（无通行汉名）'


def latin_form(c):
    for cand in (c[1], c[0]):
        for seg in cand.split(' / '):
            seg = seg.split('（')[0].strip()
            if seg and all(ord(ch) < 0x370 or 0x1E00 <= ord(ch) <= 0x1FFF
                           for ch in seg):
                return seg
    return c[0]


def main():
    lines = io.open(P, encoding='utf-8', newline='').read().split('\n')
    idx = {}
    for i, l in enumerate(lines):
        if not l.startswith('| ') or l.startswith('| ---'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 8 and c[0] != '原文':
            idx.setdefault(c[0], (i, c))
    miss = [k for m in MERGES for k in m[:2] if k not in idx]
    if miss:
        print('键未命中:', miss)
        return 1
    for keeper, absorbed, newkey, newzh, add, aff, dates in MERGES:
        ki, kc = idx[keeper]
        ai, ac = idx[absorbed]
        kc[0] = newkey
        kc[2] = newzh
        kc[3] = aff
        kc[4] = dates
        kc[6] = kc[6].rstrip() + add
        kc[7] = '2026-11-25'
        lines[ki] = '| ' + ' | '.join(kc) + ' |'
        lines[ai] = None
    n_ph = 0
    for i, l in enumerate(lines):
        if l is None or not l.startswith('| ') or l.startswith('| ---'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 8 or not c[2].startswith(PLACEHOLDER):
            continue
        c[2] = latin_form(c)
        c[6] = (c[6].rstrip() + '；2026-11-25 译法列归一：原填“保留英文（无通行汉名）”占位，'
                '改填英文原名形，与其余 ADR-0022 行口径一致')
        c[7] = '2026-11-25'
        lines[i] = '| ' + ' | '.join(c) + ' |'
        n_ph += 1
    out = [l for l in lines if l is not None]
    print('并键 4 组，占位归一 %d 行' % n_ph)
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out))
    return 0


if __name__ == '__main__':
    sys.exit(main())

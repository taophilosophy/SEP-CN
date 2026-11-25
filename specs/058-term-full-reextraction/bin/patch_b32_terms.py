# -*- coding: utf-8 -*-
"""批 32 一次性补丁：亦作形与独立行重复的三组并键（2026-11-25）。

扫描“亦作”列出的异形是否已有独立行，得 27 处；逐处研判后，三处属同概念两行：
degree of belief／degrees of belief、correspondence theory／…of truth、Chinese Room／…argument。
其余为跨域或跨概念（直觉／直观、智者／《智者篇》、广延／外延等），不动。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

P = 'shu-yu-biao.md'
# (keeper键, absorbed键, 合并后键, 合并后译法)
MERGES = [
    ('degree of belief', 'degrees of belief',
     'degree of belief / degrees of belief', '置信度（亦作“信念度”）'),
    ('correspondence theory', 'correspondence theory of truth',
     'correspondence theory / correspondence theory of truth',
     '符合论（亦作“真理符合论”；词条题名依 SUMMARY 作“真理符合论”）'),
    ('Chinese Room', 'Chinese Room argument',
     'Chinese Room / Chinese Room argument', '中文屋（亦作“中文屋论证”“中文房间”）'),
]
NOTE = '；2026-11-25 同概念并键（旧键 %s，旧首现 %s）'


def main():
    lines = io.open(P, encoding='utf-8', newline='').read().split('\n')
    idx = {}
    for i, l in enumerate(lines):
        if not l.startswith('| ') or l.startswith('| ---'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 6 and c[0] != '键':
            idx.setdefault(c[0], (i, c))
    miss = [k for pair in MERGES for k in pair[:2] if k not in idx]
    if miss:
        print('键未命中:', miss)
        return 1
    for keeper, absorbed, newkey, newzh in MERGES:
        ki, kc = idx[keeper]
        ai, ac = idx[absorbed]
        kc[0] = newkey
        kc[2] = newzh
        kc[4] = kc[4].rstrip() + NOTE % (absorbed, ac[3])
        kc[5] = '2026-11-25'
        lines[ki] = '| ' + ' | '.join(kc) + ' |'
        lines[ai] = None
    out = [l for l in lines if l is not None]
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out))
    print('并键 3 组，删行 3')
    return 0


if __name__ == '__main__':
    sys.exit(main())

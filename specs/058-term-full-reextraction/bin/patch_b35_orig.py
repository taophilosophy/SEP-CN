# -*- coding: utf-8 -*-
"""批 35 一次性补丁：法/德/拉丁语原题行的原文列补键形（2026-11-25）。

这八行的键本身就是源语言原题（拉丁字母书写，无转写层），原文列却留「—」，
在“非英语术语缺原文”清单里驻留。原文列的语义是源语言书写形，此处与键同形，
照填并留痕；梵、藏、阿、希伯来等转写键不在此列（须工具书配对，不猜）。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

P = 'shu-yu-biao.md'
KEYS = [
    'Le Monde', 'Le Système du Monde', 'Œuvres théologiques',
    'Pensées diverses sur la comète', 'Réflexions critiques',
    'Traité de l’Esprit de l’Homme', 'Was heißt: sich im Denken orientiren?',
    'corvée',
]
NOTE = ('；2026-11-25 原文列补录：键即源语言原题（拉丁字母书写，无转写层），'
        '原文列＝键形')


def main():
    lines = io.open(P, encoding='utf-8', newline='').read().split('\n')
    hit = 0
    for i, l in enumerate(lines):
        if not l.startswith('| ') or l.startswith('| ---'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 6 or c[0] not in KEYS or c[1] != '—':
            continue
        c[1] = c[0]
        c[4] = c[4].rstrip() + NOTE
        c[5] = '2026-11-25'
        lines[i] = '| ' + ' | '.join(c) + ' |'
        hit += 1
    if hit != len(KEYS):
        print('命中 %d，应为 %d' % (hit, len(KEYS)))
        return 1
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print('补原文', hit, '行')
    return 0


if __name__ == '__main__':
    sys.exit(main())

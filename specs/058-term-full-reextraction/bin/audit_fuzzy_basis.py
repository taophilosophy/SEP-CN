# -*- coding: utf-8 -*-
"""审定依据的配对性批量审计（2026-11-25；2026-11-26 起改用共享判据 ADR-0088）。

判据与实现已收编进 `tools/term_pairing.py`（ADR-0088）；本脚本只做三件事：
读术语表引用「审定」的行 → 用预建索引（`tools/build_term_pair_index.py` 产物）逐行
classify → 落 TSV。档位：
  pair     审定条目英文＝键且中文＝译法形／亦作／所引之形
  en-only  英文配对但中文不合 → 依据所引之形须复核
  cn-only  中文同形但英文不配对 → 「审定作 X」失据，须降档或改记复合词
  tw-only  仅海峡两岸名词对照库有 → 库名须改
  none     索引查无同形（不等于审定库没有，只表示本地不可证）
输出：results/term-basis-pairing-2026-11-25.tsv
"""
import io
import sys

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

from tools import term_pairing as tp

TERMS = 'shu-yu-biao.md'
OUT = 'specs/058-term-full-reextraction/results/term-basis-pairing-2026-11-25.tsv'


def main():
    index = tp.load_index()
    print('索引条目 %d（by_key %d、en %d、cn %d）'
          % (len(index['records']), len(index['by_key']), len(index['en']), len(index['cn'])))

    rows = []
    for line in io.open(TERMS, encoding='utf-8'):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 6 or c[0] in ('键', '') or set(c[0]) <= set('-: '):
            continue
        if '审定' not in c[4]:
            continue
        rows.append(c)
    print('引用审定的行 %d' % len(rows))

    from collections import defaultdict
    cnt = defaultdict(int)
    out = []
    for c in rows:
        key, zh, basis = c[0], c[2], c[4]
        v, ev = tp.classify_row(key, zh, basis, index)
        cnt[v] += 1
        out.append((key, zh[:40], v, '%s｜%s｜%s｜%s' % (ev[0], ev[1], ev[2], ev[3])))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('key\tzh\tverdict\thit\n')
        for r in out:
            f.write('\t'.join(r) + '\n')
    print('档位分布：', dict(cnt))
    print('→', OUT)


if __name__ == '__main__':
    main()

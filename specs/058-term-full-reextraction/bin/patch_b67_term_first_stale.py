# -*- coding: utf-8 -*-
"""批 67：术语表首现指向已撤上游词条（2026-11-26）。

新接入的术语首现检查（check_terms.term_dangling_first）首跑命中 11 行，全部指向
`首现（wisdom）`。核查：

* 上游 https://plato.stanford.edu/entries/wisdom/ 返回 404（本机 2026-11-26 实测）；
  现行词条为 wisdom-analytic《Wisdom in Contemporary Analytic Philosophy》，
  页面自记 First published Thu Jul 2, 2026——旧版 Wisdom 词条已被改版撤除。
* 本库只收新条目 en/wisdom-analytic；旧版文本从未入库，11 行的术语形态与旧版对应
  （依据列已记 Ryan 智慧理论），新条目只保留其中 5 个词形的少量出现，不能算同一文本的
  首现。

处置：首现列改记来源说明（不指向不存在的 slug），依据列留核查记录，不动译法。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TABLE = 'shu-yu-biao.md'
DATE = '2026-11-26'
OLD = '首现（wisdom）'
NEW = '首现（旧版 Wisdom 词条，上游已撤）'
NOTE = ('2026-11-26 核：首现原记 slug“wisdom”，上游 /entries/wisdom/ 已 404'
        '（2026-07 起由 wisdom-analytic《Wisdom in Contemporary Analytic Philosophy》'
        '接替），本库未收旧版文本，改记来源说明')


def main():
    lines = io.open(TABLE, encoding='utf-8', newline='').read().split('\n')
    n = 0
    out = []
    for line in lines:
        if line.startswith('|') and OLD in line:
            cells = line.split('|')
            if len(cells) >= 7 and cells[1].strip():
                cells[4] = cells[4].replace(OLD, NEW)
                if NOTE not in cells[5]:
                    cells[5] = cells[5].rstrip() + '；' + NOTE + ' '
                cells[6] = ' %s ' % DATE
                line = '|'.join(cells)
                n += 1
        out.append(line)
    text = '\n'.join(out)
    io.open(TABLE, 'w', encoding='utf-8', newline='\n').write(text)
    left = sum(1 for l in out if l.startswith('|') and OLD in l)
    print('改 %d 行；残余 %d' % (n, left))
    if left:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""批 69：首现含词审计的耆那残族（2026-11-26）。

`audit_first_contains.py`（去变音符口径）在批 68 之后仍有 35 行不命中，逐行看过：
28 行是启发式假阳性（短词键 aṇu／dik／dīn、拼音与汉字题名 Han Shu→《汉书》、Sirhak 拼形
差异、SIC 缩略语等），5 行属实——同属“jaina-philosophy 正文未见原词”一族：

  kaṣāya（烦恼·耆那）、manaḥparyaya-jñāna（他心智）、nikṣepa（安立）、syādvāda（或然论）、
  syāt（或许）

处置同批 68：首现改“待核（jaina-philosophy 正文未见原词）”，依据留口径，译法不动。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TABLE = 'shu-yu-biao.md'
DATE = '2026-11-26'
NEW = '待核（jaina-philosophy 正文未见原词）'
NOTE = ('2026-11-26 核：全库正文（全部 HTML，去变音符归一）未见该词；'
        'jaina-philosophy 行文用 omniscience 等通名，术语按耆那研究通行形登记，'
        '首现待该条译出后回填')
KEYS = ['kaṣāya', 'manaḥparyaya-jñāna', 'nikṣepa', 'syādvāda', 'syāt']


def main():
    lines = io.open(TABLE, encoding='utf-8', newline='').read().split('\n')
    out, done = [], set()
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 7 and cells[1].strip() in KEYS:
                key = cells[1].strip()
                cells[4] = ' %s ' % NEW
                if NOTE not in cells[5]:
                    cells[5] = cells[5].rstrip() + '；' + NOTE + ' '
                cells[6] = ' %s ' % DATE
                done.add(key)
                line = '|'.join(cells)
        out.append(line)
    missing = set(KEYS) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(TABLE, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改 %d 行' % len(done))


if __name__ == '__main__':
    main()

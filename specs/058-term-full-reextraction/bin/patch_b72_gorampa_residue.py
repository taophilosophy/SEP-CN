# -*- coding: utf-8 -*-
"""批 72：首现含词审计收敛后的两行（2026-11-26）。

`audit_first_contains.py` 经四轮口径修补（NFD 去变音符、短键词界兜底、合写键分段、
‘/’ 撇号折叠）后全库只剩 2 行不命中，均属 gorampa：

  nonsectarian movement（无派别运动，藏文 ris med）
  overpervades（周遍过宽，藏文 khyab che ba）

核查：gorampa 正文既无英文对译形，也无 ris med／khyab；全库 "overpervad" 0 命中，
nonsectarian 只出现在 feminism-femhist（异义）、kyoto-school、tsongkhapa；
khyab 出现在 dharmakiirti、tsongkhapa（藏传因明语境）。两个词属“术语按藏传研究通行形
登记、本库正文未用原词”，与批 68 的耆那族同型。

处置：首现改“待核（gorampa 正文未见原词）”，依据列记核查范围，译法不动。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TABLE = 'shu-yu-biao.md'
DATE = '2026-11-26'
NEW = '待核（gorampa 正文未见原词）'
NOTE = ('2026-11-26 核：gorampa 正文无英文对译形，亦无 ris med／khyab；全库 overpervad 0 命中，'
        'nonsectarian 仅见异义（feminism-femhist）与他条（tsongkhapa），khyab 见 '
        'dharmakiirti／tsongkhapa；术语按藏传研究通行形登记，首现待该条译出后回填')
KEYS = ['nonsectarian movement', 'overpervades']


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

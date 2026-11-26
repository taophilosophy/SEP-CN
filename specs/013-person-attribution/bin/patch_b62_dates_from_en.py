# -*- coding: utf-8 -*-
"""批 62：从 en/ 正文括注补六人生卒（2026-11-26）。

人名线旧法（回原文括注取生卒）在“缺生卒”的 668 行上重跑：按首现 slug 搜姓氏后 70 字内的
「YYYY–YYYY」，得 40 条候选；逐条看上下文后只有 6 条可用，其余是页码区间（111–120）、
他人年份（Brouwer 夫人旁的 1881–1966 属其夫、Sturm 之父旁的 1635–1703 属其子、
Yi I 旁的 1681–1763 属 Yi Ik）或书目年份。

  采信 6：Ernst Christoph Graf von Manteuffel 1676–1749（index.html:1625）、
    E. C. Tolman 1886–1959（behaviorism/index.html:480）、E. R. Guthrie 1886–1959
    （behaviorism/index.html:481）、C. L. Hull 1884–1952（同处原文作 1884–52，上游截断）、
    Park Chungbin 1891–1943（korean-buddhism/index.html:1523）、Yi Hwang 1501–1570
    （korean-philosophy/index.html:312）。

依据列记“生卒据 en/…行号 正文括注（2026-11-26 查）”，不引 GND（此六条与 GND 无关）。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
PEOPLE = 'ren-ming-biao.md'
DATE = '2026-11-26'

FILL = {
    'Ernst Christoph Graf von Manteuffel': (
        '1676–1749', 'en/18thGerman-preKant/index.html:1625'),
    'Tolman, E.C.': ('1886–1959', 'en/behaviorism/index.html:480'),
    'Guthrie, E.R.': ('1886–1959', 'en/behaviorism/index.html:481'),
    'Hull, C.L.': ('1884–1952', 'en/behaviorism/index.html:480（原文作 1884–52，截断）'),
    'Park Chungbin, Sot’aesan': ('1891–1943', 'en/korean-buddhism/index.html:1523'),
    'Yi Hwang, T’oegye': ('1501–1570', 'en/korean-philosophy/index.html:312'),
}


def main():
    lines = io.open(PEOPLE, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 9:
                key = cells[1].strip()
                if key in FILL:
                    years, src = FILL[key]
                    if cells[5].strip() not in ('—', ''):
                        raise SystemExit('%s 生卒列非空：%r' % (key, cells[5]))
                    cells[5] = ' %s ' % years
                    cells[7] = (cells[7].rstrip() +
                                '；生卒据 %s 正文括注（%s 查） ' % (src, DATE))
                    cells[8] = ' %s ' % DATE
                    done.add(key)
                    line = '|'.join(cells)
        out.append(line)
    missing = set(FILL) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(PEOPLE, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('填生卒 %d 行' % len(done))


if __name__ == '__main__':
    main()

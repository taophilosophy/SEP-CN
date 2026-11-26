# -*- coding: utf-8 -*-
"""批 61：GND review 候选 102 条逐条判定（2026-11-26）。

工作集＝383 条 review 候选中“有生卒且有职业”的 102 条（其余 281 条无年份或同名多候选，
无法判）。逐条按「姓名＋职业＋年代＋条目语境」四者相容判同名：

  采信 6：Thijssen, Hans（buridan 注释引 Hans Thijssen，中古哲学史家）、
    Tuna, Emine Hande（imaginative-resistance 词条作者）、Planer, Ronald J.（gene 引
    Ronald J. Planer）、Hawkins, Jennifer S.（informed-consent 引 Hawkins 2008）、
    Wülfer, Daniel（johann-sturm 正文，圣洛伦茨牧师兼教长）、Rötenbeck, Georg Paul
    （johann-sturm 正文，悼文作者）。
  存疑 1：Páez, Andrés——GND 记法学家（Ibarra 1966），而 SEP 该词条记其哲学学士；
    不填，维持 SUSPECT。
  驳回 31：学界职业但与条目语境不符（同名异人）。
  驳回 65：职业非学界（摄影师／作曲家／乐手／演员／医生／牧师…），除条目本身为
    医学、音乐等题材外一律不采。

采信四人填生卒（Tuna、Planer 只有 19XX 段，不填）。依据列补 GND 号与 en/ 语境行号。
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
PEOPLE = 'ren-ming-biao.md'
DATE = '2026-11-26'

# 键 -> (生卒, GND 号, en/ 语境)
FILL = {
    'Thijssen, Hans': ('1957–', '1173828508', 'en/buridan/notes.html:182 引 Hans Thijssen'),
    'Hawkins, Jennifer': ('1980–', '1394128541', 'en/informed-consent/index.html:1853 引 Hawkins 2008'),
    'Wülfer, Daniel': ('1617–1685', '117429740', 'en/johann-sturm/index.html:230 正文'),
    'Rötenbeck, Georg Paul': ('1648–1710', '116595949', 'en/johann-sturm/index.html:302 正文'),
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
                    years, gnd, ctx = FILL[key]
                    if cells[5].strip() not in ('—', ''):
                        raise SystemExit('%s 生卒列非空：%r' % (key, cells[5]))
                    cells[5] = ' %s ' % years
                    note = '；生卒据 GND %s（%s 查；%s）' % (gnd, DATE, ctx)
                    # 原“生年无考”类旧话作废
                    cells[7] = re.sub(r'；?生年无考', '', cells[7])
                    cells[7] = cells[7].rstrip() + note + ' '
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

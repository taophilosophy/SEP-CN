# -*- coding: utf-8 -*-
"""批 51：“知网系查证在案（GB 标准库凭证）”措辞改正（2026-11-26）。

背景：termonline-standard 与 allSearch 同病——回的是模糊匹配。键 `abductive reasoning`
的缓存注记 totalRecords=100，hits 全是“Ct值”“荧光定量PCR仪”一类邻居；60 行
“知网系查证在案（termonline-standard GB 标准库凭证 2026-10-28）”按标准库缓存逐行
复核，**零配对**。该措辞原意是“查询有凭证在案”，但读者会读成“该库收了这个词”。

改法：改成可核的写法——「首屏无该键配对条目（命中均为模糊邻居）」，保留凭证日期与
通道名，不删历史，不引申为“该库没有”。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
OLD = '知网系查证在案（termonline-standard GB 标准库凭证 2026-10-28）'
NEW = ('知网系 GB 标准库查证（termonline-standard 凭证 2026-10-28）：'
       '首屏无该键配对条目（命中均为模糊邻居，2026-11-26 复核）')


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    n = 0
    out = []
    for line in lines:
        if line.startswith('|') and OLD in line:
            cells = line.split('|')
            if len(cells) >= 8:
                cells[5] = cells[5].replace(OLD, NEW)
                cells[6] = ' %s ' % DATE
                line = '|'.join(cells)
                n += 1
        out.append(line)
    if not n:
        raise SystemExit('无命中，中止')
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行措辞' % n)


if __name__ == '__main__':
    main()

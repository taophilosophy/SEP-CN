# -*- coding: utf-8 -*-
"""首现列路径形归一为裸 slug（2026-11-26）。

背景：人名表「首现」列混入 `<letter>/<slug>` 目录形（多为 f/fuller-margaret、f/falaquera
一类旧批量写法）。表头口径是“slug 或书目”，路径形与裸 slug 同指一词条，属非规范形；
check_terms.person_dangling_first 已把非规范形单列告警，本脚本做机械归一。

前置门：①只改「；」分段中整段匹配 `^[a-z]/[A-Za-z0-9][A-Za-z0-9_.-]*$` 的段；
②归一目标 en/<slug>/ 必须存在，否则中止；③改后残余非规范形必须为 0；④幂等（二次运行 0 改动）。
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
TABLE = 'ren-ming-biao.md'
PATH_RE = re.compile(r'^[a-z]/([A-Za-z0-9][A-Za-z0-9_.-]*)$')


def main():
    lines = io.open(TABLE, encoding='utf-8', newline='').read().split('\n')
    out, changed, residual = [], 0, 0
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 9 and cells[1].strip() and cells[1].strip() != '键':
                parts = re.split(r'([；;])', cells[6])
                hit = False
                for i, part in enumerate(parts):
                    m = PATH_RE.match(part.strip())
                    if not m:
                        continue
                    slug = m.group(1)
                    if not os.path.isdir(os.path.join('en', slug)):
                        raise SystemExit('目标词条不存在：en/%s（行首 %s）'
                                         % (slug, cells[1].strip()))
                    parts[i] = ' %s ' % slug
                    hit = True
                if hit:
                    cells[6] = ''.join(parts)
                    line = '|'.join(cells)
                    changed += 1
        out.append(line)
    io.open(TABLE, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    for line in out:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 9:
                for part in re.split(r'[；;]', cells[6]):
                    if PATH_RE.match(part.strip()):
                        residual += 1
    print('归一 %d 行；残余路径形 %d' % (changed, residual))
    if residual:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

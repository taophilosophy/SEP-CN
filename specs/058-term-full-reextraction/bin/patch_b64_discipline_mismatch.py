# -*- coding: utf-8 -*-
"""批 64：学科错配新查法掀出的两行改正（2026-11-26）。

查法：配对成功（英文折叠形＝键且中文＝译法形）但审定分册属“几乎不承载哲学术语”的分册
（体育／奥运、地质、畜牧、草学、测绘、电力…），且行内未写异义者 → 人工核。34 条窄口径
命中里 32 条是同一概念的冷僻分册归属（方差、边界条件、动能、射影几何等），两行需改：

  second intention：行内“（审定形，两形并行）”把审定“第二意图”当成经院逻辑的审定形；
    该条分册是**奥运体育项目名词**，系击剑的 second intention（第二意图），非本义。
    → 亦作保留为学界并行形，删审定归因并注不采。
  body：行内“审定库一致”建立在该分册条目上（身体，body，奥运体育项目名词），只算形同，
    → 写实为形同、非同域凭证。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
FIX = {
    'second intention': [
        ('；2026-11-15 补亦作（审定形，两形并行）',
         '；2026-11-15 补亦作“第二意图”（学界并行形）；2026-11-26 复核：审定“第二意图”'
         '系击剑义（second intention，奥运体育项目名词），非经院逻辑义，不采'),
    ],
    'body': [
        ('审定库一致（termonline-all 凭证 2026-11-13）',
         '审定“身体”（body，奥运体育项目名词；2026-11-26 复核：体育分册同形，非同域凭证，'
         '仅记形同）'),
    ],
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8 and cells[1].strip() in FIX:
                key = cells[1].strip()
                for old, new in FIX[key]:
                    if old not in cells[5]:
                        raise SystemExit('%s 旧串未找到：%r' % (key, old[:30]))
                    cells[5] = cells[5].replace(old, new, 1)
                cells[6] = ' %s ' % DATE
                done.add(key)
                line = '|'.join(cells)
        out.append(line)
    missing = set(FIX) - done
    if missing:
        raise SystemExit('漏改：%s' % '、'.join(sorted(missing)))
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行' % len(done))


if __name__ == '__main__':
    main()

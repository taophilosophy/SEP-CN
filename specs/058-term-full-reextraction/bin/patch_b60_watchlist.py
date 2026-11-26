# -*- coding: utf-8 -*-
"""批 60：同形异义盯防表横向复查的数据侧改动（2026-11-26）。

九键逐条对账（缓存索引＋批 41–48 界面凭证）：
  argumentation 论证（物理学 01.0133）、golden rule 黄金定则（物理学 09.0214）、
  recognition 再认（行为医学 4.034／心理学 02.559）、natural theology 自然神论（自然辩证法
  02.095）、folk psychology 民族心理学（心理学 04.091）、microworld 微观世界（物理学
  09.1087）、world community 国际社会（世界历史 01.0829）、selection function 选择函数
  （天文学 07.296；数学 02.0160 另有 choice function 选择函数，本表已另键）、
  chancellor 大学校长（教育学 08.109，president,chancellor,rector）。
九行处置全部成立；仅 Chancellor 行残留旧句“审定库复核在案（同名噪声/辅助档差异…）”，
与同行 FLAG 裁定的“chancellor＝大学校长”自相矛盾，改为写实。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'
OLD = '审定库复核在案（同名噪声/辅助档差异，保留现译 2026-10-29）'
NEW = ('审定作“大学校长”（president, chancellor, rector，教育学名词 08.109；'
       '与 chancellor 的大学主管义对口，2026-11-26 复核）')


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    n, out = 0, []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8 and cells[1].strip() == 'Chancellor' and OLD in cells[5]:
                cells[5] = cells[5].replace(OLD, NEW, 1)
                cells[6] = ' %s ' % DATE
                line = '|'.join(cells)
                n += 1
        out.append(line)
    if n != 1:
        raise SystemExit('应改 1 行，实改 %d' % n)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 Chancellor 行')


if __name__ == '__main__':
    main()

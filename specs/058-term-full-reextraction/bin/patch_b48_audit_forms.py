# -*- coding: utf-8 -*-
"""批 48：11 行“审定形”按界面精确匹配结果写明出处（2026-11-26）。

这批行的依据里都有“补亦作（审定形…）”一类措辞但没写明审定形是什么；逐条界面复核后
把审定形、分册、日期写实。两处订正：
  innateness：审定作“天赋说”（语言学名词 01.056），“天赋假说／天赋假设”未审定；
  precession of the equinoxes：“分点岁差”是海峡两岸天文学名词／测绘学名词对照形，
  审定天文学名词只作“岁差”。
"""
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')
TERMS = 'shu-yu-biao.md'
DATE = '2026-11-26'

PATCH = {
    'innateness': (
        '撞形改定 2026-11-21：审定 innateness hypothesis＝天赋假说；apriority 保留先天性',
        '撞形改定 2026-11-21：审定作“天赋说”（innateness hypothesis，语言学名词 01.056；'
        '2026-11-26 界面精确匹配复核，“天赋假说／天赋假设”未审定）；apriority 保留先天性',
    ),
    'quasi-empiricism': (
        '2026-11-15 补亦作（审定形，拟经验/准经验并行）',
        '2026-11-15 补亦作；审定作“数学拟经验论”（quasi-empiricism in mathematics，自然辩证法名词 03.247；'
        '2026-11-26 界面精确匹配复核，拟经验/准经验并行）',
    ),
    'precession of the equinoxes': (
        '2026-11-15 补亦作（审定全称形）',
        '2026-11-15 补亦作；审定天文学名词作“岁差”（precession），“分点岁差”为海峡两岸天文学名词／测绘学名词'
        '对照形、非审定公布（2026-11-26 界面精确匹配复核）',
    ),
    'Lvov-Warsaw School': (
        '2026-11-15 补亦作（审定短形）',
        '2026-11-15 补亦作；审定作“华沙学派”（The Lvov-Warsaw School; LWS，自然辩证法名词；'
        '2026-11-26 界面精确匹配复核）',
    ),
    'Sleeping Beauty': (
        '审定直接命中（自然辩证法·科学哲学）；凭证 2026-11-01',
        '审定直接命中“睡美人问题”（Sleeping Beauty problem，自然辩证法名词；2026-11-26 界面精确匹配复核）；'
        '凭证 2026-11-01',
    ),
    'laws of nature': (
        '2026-11-15 补亦作（审定形；科学哲学语境“自然律”并行）',
        '2026-11-15 补亦作；审定作“自然律”（law of nature，自然辩证法名词；2026-11-26 界面精确匹配复核，'
        '科学哲学语境并行）',
    ),
    'immutability': (
        '撞形改定 2026-11-21：审定 invariant＝不变性；immutability 为不可改变性，须分词',
        '撞形改定 2026-11-21：审定 invariant＝不变性（物理学名词；2026-11-26 界面精确匹配复核）；'
        'immutability 为不可改变性，须分词',
    ),
    'maximal act-set': (
        '审定“极大集”数学域佐证）；凭证 2026-11-01',
        '审定“极大集”（maximal set，数学名词；2026-11-26 界面精确匹配复核）为数学域佐证）；凭证 2026-11-01',
    ),
    'model surrogate': (
        '2026-11-15 补亦作（审定形，机器学习语境“代理模型”并行）',
        '2026-11-15 补亦作；审定作“代理模型”（surrogate model，化工名词（十）化工系统工程和化工信息化名词；'
        '2026-11-26 界面精确匹配复核，机器学习语境并行）',
    ),
    'part-whole relation': (
        '2026-11-15 补亦作（审定形，语序两形并行，连接号从 ADR-0041 一字线）',
        '2026-11-15 补亦作；审定作“整体与部分”（whole and part，自然辩证法名词；2026-11-26 界面精确匹配复核，'
        '语序两形并行，连接号从 ADR-0041 一字线）',
    ),
    'quantum gate': (
        '2026-11-15 补亦作（审定全称形）',
        '2026-11-15 补亦作；审定全称形“量子逻辑门”（quantum logic gate，物理学名词／计算机科学技术名词；'
        '2026-11-26 界面精确匹配复核）',
    ),
}


def main():
    lines = io.open(TERMS, encoding='utf-8', newline='').read().split('\n')
    done, out = set(), []
    for line in lines:
        if line.startswith('|'):
            cells = line.split('|')
            if len(cells) >= 8:
                key = cells[1].strip()
                if key in PATCH:
                    old, new = PATCH[key]
                    if old not in cells[5]:
                        raise SystemExit('旧依据不符，中止：%s\n 实际：%s' % (key, cells[5].strip()))
                    cells[5] = cells[5].replace(old, new)
                    cells[6] = ' %s ' % DATE
                    line = '|'.join(cells)
                    done.add(key)
        out.append(line)
    missing = set(PATCH) - done
    if missing:
        raise SystemExit('未找到行：%s' % missing)
    io.open(TERMS, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print('改正 %d 行：%s' % (len(done), '、'.join(sorted(done))))


if __name__ == '__main__':
    main()

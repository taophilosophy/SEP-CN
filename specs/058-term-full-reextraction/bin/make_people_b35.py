# -*- coding: utf-8 -*-
"""人名第三十五批（2026-11-24，中文源补证）：八人取汉名。

Butler、Jevons、Leśniewski、von Wright、Hacker、Crispin Wright、Maddy、Stump。
"""
import io
import os
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'people-cnweb-2026-11-24-b35.md'

FIX = [
    ('Judith Butler', '朱迪斯·巴特勒', None,
     '中文定名补证：中译本《性别麻烦：女性主义与身份的颠覆》（宋素凤译，上海三联书店 2009-01，'
     'ISBN 9787542628893；岳麓书社·浦睿文化 2024 修订版）作者署名“朱迪斯·巴特勒”'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Jevons, William Stanley / William Stanley Jevons', '威廉·斯坦利·杰文斯', '斯坦利·杰文斯',
     '中文定名补证：中译本《政治经济学理论》（郭大力译，商务印书馆 1984/1997，汉译世界学术名著'
     '丛书）作者署名“（英）斯坦利·杰文斯（W. Stanley Jevons）”，主形补全名“威廉·斯坦利·'
     '杰文斯”，署名形入别名（2026-11-24 查，凭证 %s）' % EV),
    ('Leśniewski, Stanisław / Stanisław Leśniewski', '斯坦尼斯瓦夫·莱斯涅夫斯基', '勒希涅夫斯基',
     '中文定名补证：南京大学黄盛学位论文《勒希涅夫斯基元命题学研究》（2020）作“勒希涅夫斯基”'
     '（台湾学界译形，入别名）；Agora 中文思想百科作“斯坦尼斯瓦夫·莱斯涅夫斯基”，通名取大陆'
     '通行音译，按 specs/058 A 档直裁（2026-11-24 查，凭证 %s）' % EV),
    ('von Wright, Georg Henrik', '格奥尔格·亨里克·冯·赖特', None,
     '中文定名补证：《解释与理解》（张留华译，浙江大学出版社 2016-09，ISBN 9787308159128）'
     '作者简介“冯·赖特（Georg Henrik von Wright，1916–2003），道义逻辑之父”；陈波译介'
     '《分析哲学：一个批判的历史概述》（南京大学实践与文本网）同（2026-11-24 查，凭证 %s）' % EV),
    ('Hacker, P. M. S.', '彼得·哈克', None,
     '中文定名补证：《维特根斯坦在20世纪哲学史上的地位》（万丹译，中国社会科学出版社 2025-07，'
     'ISBN 9787522734736）作者署名“彼得·哈克”，MARC 个人名称等同“哈克 P. M. S. 著”；'
     '台版《维根斯坦》（奚浩译，麦田 1999）作“哈克”（2026-11-24 查，凭证 %s）' % EV),
    ('Wright, Crispin', '克里斯宾·赖特', None,
     '中文定名补证：克里斯宾·赖特《真理：重温一场传统的论战》（胡兰双译），《哲学分析》2019 年'
     '第 5 期；罗蒂《真理与进步》（杨玉成译，华夏出版社 2003）篇目“‘真’是探究的目标吗？'
     '唐纳德·戴维森与克里斯宾·赖特”；澎湃新闻 2016 年荐介同（2026-11-24 查，凭证 %s）' % EV),
    ('Maddy, Penelope', '佩内洛普·麦蒂', None,
     '中文定名补证：康仕慧、郭贵春《自然主义集合实在论与数学哲学研究范式》，《哲学研究》2010 年'
     '第 4 期作“佩内洛普·麦蒂（Penelope Maddy）”；郝兆宽《不自然的自然主义》（2014）同'
     '（2026-11-24 查，凭证 %s）' % EV),
    ('Stump, Eleonore', '埃利奥诺·斯顿普', '伊莲诺·斯特普 / 埃莱奥诺·斯坦普',
     '中文定名补证：段德智《神学大全》第一集译者序（商务印书馆 2013）作“埃利奥诺·斯顿普'
     '（Eleonore Stump）”，为最权威署名；版权代理页作“伊莲诺·斯特普”，另见“埃莱奥诺·'
     '斯坦普”，异形入别名（2026-11-24 查，凭证 %s）' % EV),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0]:
            idx.setdefault(norm_key_quote(cells[0]), i)
n = 0
for key, zh, alias, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    cells[2] = zh
    if alias:
        cells[1] = alias if cells[1] in ('—', '') else cells[1] + ' / ' + alias
    if note not in cells[6]:
        cells[6] = cells[6].rstrip('；') + '；' + note
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    print('改行', key, '->', cells[2])
    n += 1
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('patch=%d' % n)

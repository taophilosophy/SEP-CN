# -*- coding: utf-8 -*-
"""著作名第十批 rowspec（2026-11-24）：17 部经典，依据商务印书馆
“汉译世界学术名著丛书”1000 种书目（2024-09-24 发布）逐条对应书名。

书名一律取该书目所载中译名；书目用旧名者，在依据列注明通行异名。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

CAT = '商务印书馆“汉译世界学术名著丛书”1000 种书目（2024-09-24，cp.com.cn）'
# (英文原题, 中译名, 书目位置, 备注)
WORKS = [
    ('Being and Time', '《存在与时间》', '哲学第 14 号', ''),
    ('An Essay Concerning Human Understanding', '《人类理解论》', '哲学第 137 号', ''),
    ('Principia Ethica', '《伦理学原理》', '哲学第 87 号', ''),
    ('The Problems of Philosophy', '《哲学问题》', '哲学第 319 号', ''),
    ('The Concept of Mind', '《心的概念》', '哲学第 205 号', ''),
    ('Philosophical Grammar', '《哲学语法》', '哲学第 235 号', ''),
    ('The Visible and the Invisible', '《可见的与不可见的》', '哲学第 71 号', ''),
    ('On the Genealogy of Morality', '《论道德的谱系》', '哲学第 91 号', ''),
    ('Thus Spoke Zarathustra', '《苏鲁支语录》', '哲学第 180 号',
     '徐梵澄译本名；通行亦作《查拉图斯特拉如是说》'),
    ('The Aim and Structure of Physical Theory', '《物理学理论的目的与结构》',
     '哲学第 194 号', ''),
    ('On Liberty', '《论自由》', '政治学·法学·社会学·教育学第 67 号', ''),
    ('Leviathan', '《利维坦》', '政治学·法学·社会学·教育学第 55 号', ''),
    ('Two Treatises of Government', '《政府论》', '政治学·法学·社会学·教育学第 140 号',
     '书目作“政府论（上下篇）”'),
    ('The Social Contract', '《社会契约论》', '政治学·法学·社会学·教育学第 100 号', ''),
    ('The Subjection of Women', '《妇女的屈从地位》',
     '政治学·法学·社会学·教育学第 80 号', '与《女权辩护》合刊'),
    ('A Vindication of the Rights of Woman', '《女权辩护》',
     '政治学·法学·社会学·教育学第 80 号', '与《妇女的屈从地位》合刊'),
    ('The Wealth of Nations', '《国民财富的性质和原因的研究》',
     '经济学·管理学第 26 号', '通行简称《国富论》'),
]

rows = []
for en, zh, where, note in WORKS:
    basis = '权威译本（%s·%s载此书名；2026-11-24 查，凭证 works-batch10-2026-11-24.md）' % (
        CAT, where)
    if note:
        basis += '；' + note
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch51-works.json')
json.dump({'batch': '058-batch51-works', 'date': '2026-11-24',
           'scope': '著作名第十批（经典 17 部，商务书目对应）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

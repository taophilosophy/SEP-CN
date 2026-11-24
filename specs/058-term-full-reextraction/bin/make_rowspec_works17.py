# -*- coding: utf-8 -*-
"""著作名第十七批 rowspec（2026-11-24）：语料高引而未登经典 8 部。

A Theory of Justice 已以键 Theory of Justice 在册，改由 patch_works17.py 补译本依据，
不另立行。Philosophical Explanations 无中译本，留证不登记。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

WORKS = [
    ('On What Matters', '《论重要之事》',
     '阮航、葛四友译，北京时代华文书局 2015-09（第一卷，ISBN 9787569901856）；'
     '《论重要之事：规范伦理学卷（上、下）》，中国人民大学出版社 2022-03（ISBN 9787300303208）'),
    ('The Possibility of Altruism', '《利他主义的可能性》',
     '应奇、何松旭、张曦译，上海译文出版社 2015-02（二十世纪西方哲学经典，ISBN 9787532768141）'),
    ('Practical Ethics', '《实践伦理学》',
     '刘莘译，东方出版社 2005-09（政治法律哲学丛书，ISBN 9787506022699）'),
    ('The Case for Animal Rights', '《动物权利研究》',
     '李曦译，北京大学出版社 2010-01（同文馆·应用伦理学丛书，ISBN 9787301159934）'),
    ('Knowledge and Its Limits', '《知识及其限度》',
     '刘占峰、陈丽译，人民出版社 2013-09（当代西方学术经典译丛，ISBN 9787010122984）'),
    ('The Right and the Good', '《正当与善》',
     '罗斯著，林南译，上海译文出版社 2008（二十世纪西方哲学译丛）／2016 精装'
     '（ISBN 9787532771035）'),
    ('Ethics and the Limits of Philosophy', '《伦理学与哲学的限度》',
     'B. 威廉斯著，陈嘉映译，商务印书馆 2017-06（ISBN 9787100129855；'
     '2018 汉译世界学术名著版 ISBN 9787100164054）'),
    ('Mortal Questions', '《人的问题》',
     '托马斯·内格尔著，万以译，上海译文出版社 2000（二十世纪西方哲学译丛）；'
     '2014 睿文馆版（ISBN 9787532765614）；2021 译文经典版（ISBN 9787532788088）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '权威译本（%s；2026-11-24 联网核对，凭证 works-batch17-2026-11-24.md）' % src
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works.json')
json.dump({'batch': '058-batch58-works', 'date': '2026-11-24',
           'scope': '著作名第十七批（高引经典 8 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

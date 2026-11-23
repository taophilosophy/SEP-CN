# -*- coding: utf-8 -*-
"""人名第十四批 rowspec（2026-11-24）：22 人，非西方传统定向补捞。

来源：定向名单（现代新儒家、京都学派、印度正理—语言哲学、伊斯兰神学、
非洲与拉美解放哲学）→ yuanwen/ 计数≥3 → 登记册键／别名／译法折叠反查。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b14.tsv'
EN = '（无通行汉名，保留英文原名）'

PEOPLE = [
    ('Xiong Shili', '熊十力', '中国', '1885–1968', 'Q699536',
     '现代新儒家开山（《新唯识论》）'),
    ('Tang Junyi', '唐君毅', '中国', '1909–1978', 'Q7682698',
     '新儒家（《中国哲学原论》）；Wikidata 标签作 Wade-Giles 形 Tang Chun-i'),
    ('Xu Fuguan', '徐复观', '中国', '1904–1982', 'Q3571061',
     '新儒家与思想史（《中国人性论史》）；通行传记多记生于 1903 年，此处取 Wikidata 1904'),
    ('Liang Shuming', '梁漱溟', '中国', '1893–1988', 'Q1167488',
     '《东西文化及其哲学》；乡村建设运动'),
    ('Li Zehou', '李泽厚', '中国', '1930–2021', 'Q708814',
     '实践美学与中国思想史（《美的历程》）'),
    ('Zhang Dongsun', '张东荪', '中国', '1886–1973', 'Q564886',
     '知识论多元论（《认识论》）'),
    ('Tanabe Hajime', '田边元', '日本', '1885–1962', 'Q1394797',
     '京都学派（《作为忏悔道的哲学》）'),
    ('Nishitani Keiji', '西谷启治', '日本', '1900–1990', 'Q1993564',
     '京都学派宗教哲学（《宗教是什么》）'),
    ('Abe Masao', '阿部正雄', '日本', '1915–2006', 'Q1975693',
     '京都学派与禅／基督教对话'),
    ('Yuasa Yasuo', '汤浅泰雄', '日本', '1925–2005', 'Q3818106',
     '身体论与日本哲学（《身体论》）'),
    ('Keta Masako', '气多雅子', '日本', '1953–', 'Q11548136',
     '京都学派与西田哲学研究'),
    ('Chad Hansen', 'Chad Hansen' + EN, '美国（任教于香港大学）', '—', '—',
     '中国语言与逻辑（《A Daoist Theory of Chinese Thought》）；Wikidata 同名项'
     'Q28131364 为美式橄榄球员，不取；本人无 Wikidata 人格项，生卒留白'),
    ('Justin Tiwald', 'Justin Tiwald' + EN, '美国（任教于香港大学）', '1974–',
     'Q113830211', '新儒家伦理（与 Van Norden 合编《Readings in Later Chinese '
     'Philosophy》）；籍属据香港大学哲学系页（2026-11-24 查）'),
    ('Bimal Krishna Matilal', '比马尔·克里希纳·马蒂拉尔', '印度', '1935–1991',
     'Q4913688', '正理—胜论与语言哲学（《Logic, Language and Reality》）'),
    ('Hossein Ziai', '侯赛因·齐亚伊', '伊朗', '1944–2011', 'Q10843548',
     '伊斯兰照明哲学（苏赫拉瓦迪研究）'),
    ('Léopold Sédar Senghor', '莱奥波尔德·塞达尔·桑戈尔', '塞内加尔／法国',
     '1906–2001', 'Q154545', '黑人性（Negritude）与非洲社会主义'),
    ('Francisco Romero', '弗朗西斯科·罗梅罗', '阿根廷／西班牙', '1891–1962',
     'Q5483895', '拉美反实证主义与「新哲学」'),
    ('Arturo Roig', '阿图罗·罗伊格', '阿根廷', '—', '—',
     '拉美解放哲学与拉丁美洲思想史；英文维基条目（无 Wikidata 项）未载生卒，'
     '留白待考'),
    ('Horacio Cerutti Guldberg', '奥拉西奥·塞鲁蒂', '阿根廷／墨西哥', '1950–',
     'Q18223552', '拉美解放哲学史与乌托邦思想'),
    ('Placide Tempels', '普拉西德·滕佩尔斯', '比利时', '1906–1977', 'Q327448',
     '《班图哲学》，非洲哲学讨论的起点'),
    ('José Carlos Mariátegui', '何塞·卡洛斯·马里亚特吉', '秘鲁', '1894–1930',
     'Q335544', '拉美马克思主义（《秘鲁的现实与神话》）'),
    ('Al-Maturidi', '马图里迪', '伊斯兰世界（撒马尔罕）', '？–944', 'Q12827721',
     '逊尼派教义学两大传统之一；生年诸说（约 853 与 893 两说），只记卒年'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    if qid == '—':
        basis = ('学界通行译名；籍属/生卒联网查证（2026-11-24 查，凭证 %s）；%s'
                 % (EV, note))
    else:
        basis = ('学界通行译名；籍属/生卒联网查证：Wikidata %s'
                 '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note))
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates, 'basis': basis, 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch40-people.json')
json.dump({'batch': '058-batch40-people', 'date': '2026-11-24',
           'scope': '人名第十四批（22 人，非西方传统）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

# -*- coding: utf-8 -*-
"""人名第十三批 rowspec（2026-11-24）：29 人，定向补捞（古典学、康德／黑格尔研究、
法哲学、后殖民与生态女性主义），Wikidata 逐人取证。

通道：候选池类型分类漏收的姓名（姓氏单独出现、或多在脚注书目中），改用
“定向名单→yuanwen/ 计数≥3→登记册键／别名／译法三列 fold 反查”获得。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b13.tsv'
EN = '（无通行汉名，保留英文原名）'

PEOPLE = [
    ('Henry Allison', '亨利·艾利森', '美国', '1937–2023', 'Q48816738',
     '康德研究（《康德的先验观念论》）；本名 Henry E. Allison'),
    ('Alfred Schütz', '阿尔弗雷德·舒茨', '奥地利／美国', '1899–1959',
     'Q94018', '现象学社会学（《社会世界的意义构成》）'),
    ('Gaston Bachelard', '加斯东·巴什拉', '法国', '1884–1962', 'Q270800',
     '认识论断裂与诗学（《科学精神的形成》）'),
    ('Lorraine Code', '洛林·科德', '加拿大', '1937–', 'Q6681600',
     '女性主义认识论（《认知责任》）'),
    ('Terry Pinkard', '特里·平卡德', '美国', '1947–', 'Q92244468',
     '黑格尔研究（《黑格尔的现象学》）'),
    ('Kate Manne', '凯特·曼恩', '美国／澳大利亚', '1983–', 'Q61303761',
     '女性主义哲学（《Down Girl》论厌女）'),
    ('Jonathan Lear', '乔纳森·里尔', '美国', '1948–2025', 'Q3809934',
     '亚里士多德伦理学与精神分析（《爱及其所是》）'),
    ('Robert Pippin', 'Robert Pippin' + EN, '美国', '—', '—',
     '黑格尔与德国观念论（芝加哥大学）；Wikidata 无人格项，英文维基摘要未载生年，'
     '生卒留白不臆造'),
    ('Béatrice Longuenesse', 'Béatrice Longuenesse' + EN, '法国／美国', '1950–',
     'Q5004982', '康德与自我意识研究'),
    ('Richard Kraut', '理查德·克劳特', '美国', '1944–', 'Q18202457',
     '柏拉图与亚里士多德伦理学（《苏格拉底与国家》）'),
    ('Paul Tannery', '保罗·塔纳里', '法国', '1843–1904', 'Q177139',
     '古代数学与科学史（《希腊几何学史》）'),
    ('Marwan Rashed', '马尔万·拉希德', '法国', '1971–', 'Q18215250',
     '希腊—阿拉伯哲学史（亚历山大注释传统）'),
    ('Andrei Marmor', '安德烈·马莫', '以色列／美国', '1959–', 'Q16507669',
     '法哲学（排他性实证主义）'),
    ('Arthur Ripstein', '阿瑟·里普斯坦', '加拿大', '1958–', 'Q93239038',
     '法哲学与康德政治哲学（《强力与自由》）'),
    ('Ulrich von Wilamowitz-Moellendorff', '乌尔里希·冯·维拉莫维茨-默伦多夫',
     '德国', '1848–1931', 'Q61863',
     '古典语文学（语料作“Wilamowitz”）'),
    ('Riccardo Chiaradonna', 'Riccardo Chiaradonna' + EN, '意大利', '1970–',
     'Q93240755', '新柏拉图主义与亚里士多德注释研究'),
    ('R. A. Duff', '安东尼·达夫', '英国', '1945–', 'Q113044445',
     '刑法哲学（《试炼与惩罚》）；本名 R. Antony Duff，语料作“R.A. Duff”'),
    ('Karl Löwith', '卡尔·洛维特', '德国', '1897–1973', 'Q75790',
     '历史哲学与尼采／海德格尔（《从黑格尔到尼采》）'),
    ('Keimpe Algra', 'Keimpe Algra' + EN, '荷兰', '1959–', 'Q15438590',
     '古代与中世纪哲学（乌得勒支）；Wikidata 未记 P27，据条目描述记荷兰'),
    ('Frederick Beiser', '弗雷德里克·拜塞尔', '美国', '1949–', 'Q5497459',
     '德国观念论与晚期启蒙（《德国观念论》）；本名 Frederick C. Beiser'),
    ('Lucius Outlaw', '卢修斯·奥特劳', '美国', '—', 'Q83432360',
     '非洲哲学与非裔美国哲学；Wikidata 生卒与 P27 皆缺'),
    ('Susanne Bobzien', '苏珊娜·博布齐恩', '德国／英国', '1960–', 'Q102366',
     '斯多亚逻辑与决定论；Wikidata 描述记 German-born British'),
    ('Quentin Meillassoux', '昆汀·梅亚苏', '法国', '1967–', 'Q644620',
     '思辨实在论（《有限性之后》）'),
    ('John D. Caputo', '约翰·卡普托', '美国', '1940–', 'Q3181313',
     '解构神学与宗教哲学；语料作“John Caputo”'),
    ('Jacob Taubes', '雅各布·陶伯斯', '奥地利／德国／美国', '1923–1987',
     'Q650151', '宗教哲学与保罗政治神学（《保罗政治神学》）'),
    ('Alastair Norcross', '阿拉斯泰尔·诺克罗斯', '美国', '—', 'Q4708764',
     '后果主义与道德心理学（scalar consequentialism）'),
    ('Maria Mies', '玛丽亚·米斯', '德国', '1931–2023', 'Q111452',
     '生态女性主义（《父权制与资本积累》）'),
    ('Katerina Deligiorgi', 'Katerina Deligiorgi' + EN, '—', '1965–',
     'Q132984107', '康德与启蒙研究（萨塞克斯大学）'),
    ('Angela Breitenbach', 'Angela Breitenbach' + EN, '英国', '—',
     'Q113753195', '康德美学与目的论（剑桥）'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    if qid == '—':
        basis = ('学界通行音译；籍属/生卒联网查证（2026-11-24 查，凭证 %s）；%s'
                 % (EV, note))
    else:
        basis = ('学界通行音译；籍属/生卒联网查证：Wikidata %s'
                 '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note))
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates, 'basis': basis, 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch39-people.json')
json.dump({'batch': '058-batch39-people', 'date': '2026-11-24',
           'scope': '人名第十三批（29 人，定向补捞）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

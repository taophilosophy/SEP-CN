# -*- coding: utf-8 -*-
"""人名第十一批 rowspec（2026-11-24）：15 人，Wikidata 逐人取证。

筛法：候选池 status=本轮新增、person 型、freq≥6、spread≥3，以 NFKD 折叠后的
“姓氏＋首名（或首字母）”对全部登记键与别名列做包含匹配，余者人工分辨真伪。
本批均为别名感知后仍缺且可确证身份者。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b11.tsv'
EN = '（无通行汉名，保留英文原名）'

# (键, 译法, 籍属, 生卒/鼎盛年, QID, 备注)
PEOPLE = [
    ('Richard von Mises', '理查德·冯·米塞斯', '奥地利／美国', '1883–1953',
     'Q84292', '概率的频率解释与实证主义科学哲学；与已登记 Ludwig von Mises 异人'),
    # W. D. Ross 在册（键 Ross, W. D.），本批只补全名别名，见 alias_patch_b11.py。
    ('David Ray Griffin', '大卫·雷·格里芬', '美国', '1939–2022', 'Q521358',
     '过程哲学与后现代科学；与已登记 James Griffin 异人'),
    ('Ralph Barton Perry', '拉尔夫·巴顿·佩里', '美国', '1876–1957', 'Q32679',
     '新实在论与价值理论；与已登记 John Perry 异人'),
    ('Madame de Staël', '斯塔尔夫人', '瑞士（日内瓦）／法国', '1766–1817',
     'Q123041', '本名 Germaine de Staël，法国浪漫主义与政治思想'),
    ('Grace Lee Boggs', '格蕾丝·李·博格斯', '美国', '1915–2015', 'Q1541053',
     '非裔与亚裔美国社会活动家、哲学家（马克思主义与黑人解放）'),
    ('Olympe de Gouges', '奥兰普·德·古热', '法国', '1748–1793', 'Q206972',
     '《女权与女公民权宣言》作者；女性主义政治思想'),
    ('Johann Georg Sulzer', '约翰·格奥尔格·祖尔策', '德国（瑞士出生）',
     '1720–1779', 'Q116036', '美学与心理学（《美的艺术的一般理论》）'),
    ('Juan Bautista Alberdi', '胡安·包蒂斯塔·阿尔韦迪', '阿根廷', '1810–1884',
     'Q722738', '拉丁美洲自由主义与民族建构（《阿根廷共和国的基础》）'),
    ('Costa de Beauregard', '奥利维耶·科斯塔·德·博勒加德', '法国', '1911–2007',
     'Q3350939', '物理学哲学（时间箭头、量子力学中的逆向因果）'),
    ('Roy Wood Sellars', '罗伊·伍德·塞拉斯', '美国', '1880–1973', 'Q4177579',
     '批判实在论；与已登记 Wilfrid Sellars（其子）异人'),
    ('Robert Gooding-Williams', 'Robert Gooding-Williams' + EN, '美国', '1953–',
     'Q29110080', '非裔美国政治思想（杜波依斯研究）'),
    ('Lynn Hankinson Nelson', 'Lynn Hankinson Nelson' + EN, '—', '1948–2024',
     'Q106378365', '女性主义科学哲学；Wikidata 未记国籍，且在册其他作者名易混'),
    ('Sir Walter Scott', '沃尔特·司各特', '英国（苏格兰）', '1771–1832', 'Q79025',
     '小说家与诗人，历史小说的苏格兰启蒙背景'),
    ('Alice Chipman Dewey', '爱丽丝·奇普曼·杜威', '美国', '1858–1927',
     'Q55720965', '教育家、女性主义者；约翰·杜威之妻'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行音译；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch37-people.json')
json.dump({'batch': '058-batch37-people', 'date': '2026-11-24',
           'scope': '人名第十一批（15 人，Wikidata 逐人取证）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

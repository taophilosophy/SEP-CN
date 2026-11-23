# -*- coding: utf-8 -*-
"""人名第二十一批 rowspec（2026-11-24）：规范伦理学、法哲学、自由意志、
女性主义哲学 20 人，Wikidata 逐人取证。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b21.tsv'
EN = '（无通行汉名，保留英文原名）'

PEOPLE = [
    ('Peter Vallentyne', '彼得·瓦伦泰恩', '美国', '1952–', 'Q4102937',
     '左翼自由至上主义（left-libertarianism）'),
    ('Brad Hooker', '布拉德·胡克', '英国', '1957–', 'Q4954005',
     '规则后果主义（《Ideal Code, Real World》）'),
    ('Ted Honderich', '泰德·洪德里奇', '加拿大／英国', '1933–2024', 'Q710767',
     '决定论与「生活意志」理论'),
    ('Michael Otsuka', '迈克尔·大塚', '美国', '1964–', 'Q14945515',
     '左翼自由至上主义与平等（《Libertarianism without Inequality》）'),
    ('Mary Kate McGowan', 'Mary Kate McGowan' + EN, '美国', '1968–', 'Q16732086',
     '言语行为与言论自由（言语施为性伤害）'),
    ('Lea Ypi', '莱娅·伊皮', '阿尔巴尼亚', '1979–', 'Q109453577',
     '规范政治理论与社会主义（《Free》）'),
    ('Eddy Nahmias', 'Eddy Nahmias' + EN, '—', '1969–', 'Q112554502',
     '自由意志的相容论与实验哲学；Wikidata 无 P27'),
    ('Ann Cudd', '安·卡德', '美国', '1950–', 'Q16148442',
     '压迫分析（《Analyzing Oppression》）'),
    ('Philip Stratton-Lake', 'Philip Stratton-Lake' + EN, '—', '1959–2022',
     'Q104583021', '直觉主义与罗斯研究；Wikidata 无 P27'),
    ('Marilyn Frye', '玛丽莲·弗莱', '美国', '1941–', 'Q13562998',
     '女性主义哲学（《The Politics of Reality》）'),
    ('Ruth Hagengruber', '露特·哈根格鲁伯', '德国', '1958–', 'Q1319977',
     '女性主义哲学史与埃米莉·杜·夏特莱研究'),
    ('Victor Tadros', '维克托·塔德罗斯', '英国', '1972–', 'Q102035729',
     '刑法哲学（《The Ends of Harm》）'),
    ('Sara Ahmed', '萨拉·艾哈迈德', '英国／澳大利亚', '1969–', 'Q15437208',
     '女性主义与「情感劳动」；《Living a Feminist Life》'),
    ('Leif Wenar', '莱夫·韦纳', '美国', '—', 'Q83963015',
     '资源权利与暴力问题（《Blood Oil》）；Wikidata 无生年'),
    ('Tom Regan', '汤姆·里根', '美国', '1938–2017', 'Q314146',
     '动物权利论（《The Case for Animal Rights》）'),
    ('Sara Heinämaa', '萨拉·海内玛', '芬兰', '1960–', 'Q11892464',
     '现象学与性别研究（胡塞尔与梅洛-庞蒂）'),
    ('Helen Steward', '海伦·斯图尔德', '英国', '1965–', 'Q21175257',
     '自由意志与行动哲学（《A Metaphysics for Freedom》）'),
    ('Diana Meyers', '黛安娜·迈耶斯', '美国', '1947–', 'Q16732533',
     '人格同一性与自主（《Self, Society, and Personal Choice》）'),
    ('Christine Swanton', '克里斯廷·斯旺顿', '—', '1947–', 'Q112410040',
     '德性伦理学（《Virtue Ethics: A Pluralistic View》）；Wikidata 无 P27'),
    ('Carolina Sartorio', '卡罗琳娜·萨托里奥', '—', '—', 'Q112714937',
     '因果性与道德责任；Wikidata 无 P27 与生年'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行译名；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch47-people.json')
json.dump({'batch': '058-batch47-people', 'date': '2026-11-24',
           'scope': '人名第二十一批（20 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

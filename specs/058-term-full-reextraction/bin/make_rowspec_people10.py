# -*- coding: utf-8 -*-
"""人名第十批 rowspec（2026-11-24）：22 人，Wikidata／网页逐人取证。

筛法：058 候选池 person 型（freq≥8、spread≥5）扣除已登记（含倒序键、姓键、
合写别名）后的真缺项；机构名、书名、头衔（Pope John 等）、残名（Ibn Abī）已剔除。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b10.tsv'
EN = '（无通行汉名，保留英文原名）'

# (键, 译法, 籍属, 生卒/鼎盛年, QID, 备注)
PEOPLE = [
    ('Mullā Ṣadrā', '穆拉·萨德拉', '波斯（萨法维）／伊斯兰哲学', '1571–1641',
     'Q2010955', '超越哲学（transcendent theosophy）；亦译「毛拉·萨德拉」'),
    ('Mīr Dāmād', '米尔·达马德', '波斯（萨法维）／伊斯兰哲学', '1561–1631',
     'Q3315763', '穆拉·萨德拉之师，「伊斯法罕学派」奠基者'),
    ('Al-Fārābī', '法拉比', '中亚（法拉布）／伊斯兰哲学', '约872–950', 'Q160460',
     '阿拉伯哲学「第二导师」；Wikidata 记 872–951，通说卒于大马士革，取约数'),
    ('Vācaspati Miśra', 'Vācaspati Miśra' + EN, '古印度／弥曼差·吠檀多注释者',
     '约 10 世纪（活动期）', 'Q1292812',
     '《正理纲要》作者；Wikidata 记 900–980 系近似值，汉译未定故保留原名'),
    ('Šāntideva', '寂天', '古印度（那烂陀）／佛教中观', '约 8 世纪（活动期）',
     'Q445460', '《入菩萨行论》作者；取佛教传统译名「寂天」，Wikidata 记 685–763'),
    ('King Xuan', '齐宣王', '中国（战国·齐）', '？–前301（在位约前319–前301）',
     'Q580333', '孟子所见齐君；Wikidata 仅记卒年与在位年，生年不传'),
    ('John Haugeland', '约翰·豪格兰德', '美国', '1945–2010', 'Q1405211',
     '心灵哲学与海德格尔研究（《真正的心智》）'),
    ('Uma Narayan', '乌玛·纳拉扬', '印度／美国', '1958–', 'Q4003299',
     '后殖民女性主义（《殖民主义脉络中的异文化》）'),
    ('Paul Draper', '保罗·德雷珀', '美国', '1957–', 'Q3898047',
     '宗教哲学（恶的论证、自然主义）；与同名英国音乐人异人'),
    ('Stephen Toulmin', '斯蒂芬·图尔敏', '英国', '1922–2009', 'Q472676',
     '论证理论与伦理认识论（《理性的地方与一般》）'),
    ('Michael Devitt', '迈克尔·德维特', '澳大利亚／美国', '1938–', 'Q15462718',
     '科学实在论与语义学外在主义'),
    ('Rosalind Hursthouse', '罗莎琳·赫斯特豪斯', '新西兰', '1943–', 'Q3480230',
     '德性伦理学（《论德性伦理学》）'),
    ('James Griffin', '詹姆斯·格里芬', '英国', '1933–2019', 'Q14945583',
     '道德哲学与人权理论（《论人权》）；经英文维基“James Griffin (philosopher)”'
     '反查得 QID'),
    ('John Nash', '约翰·纳什', '美国', '1928–2015', 'Q128736',
     '博弈论（纳什均衡），1994 年诺贝尔经济学奖'),
    ('Oliver Wendell Holmes', '奥利弗·温德尔·霍姆斯', '美国', '1841–1935',
     'Q360574', '小霍姆斯，最高法院大法官，《普通法》作者；语料见于契约法条目'),
    ('Andy Clark', '安迪·克拉克', '英国（生于伦敦）', '1957–', 'Q4760523',
     '延展心智与具身认知；Wikidata P27 记美国，据 LCNAF／Who’s Who 从英国'),
    ('Mark Johnston', '马克·约翰斯顿', '澳大利亚', '1954–', 'Q20645836',
     '形而上学与道德哲学（《无价值的客体》）'),
    ('Hasok Chang', 'Hasok Chang' + EN, '美国（生于韩国）', '1967–', 'Q24238917',
     '科学哲学与化学哲学（《创造温度》）'),
    ('Salazar Bondy', '奥古斯托·萨拉萨尔·邦迪', '秘鲁', '1925–1974', 'Q5711746',
     '拉丁美洲解放哲学（《拉丁美洲哲学的本质》）'),
    ('Graff Fara', '德莉亚·格拉夫·法拉', '美国', '1969–2017', 'Q21525754',
     'Sorites 悖论与模态（本名 Delia Graff Fara）'),
    ('Michael Martin', '迈克尔·马丁', '美国', '1932–2015', '—',
     '无神论哲学（《无神论的哲学证成》）；波士顿大学讣告与英文维基'
     '“Michael Lou Martin”记 1932-02-03 生、2015-05-27 卒（2026-11-24 查），'
     'Wikidata 无人格项；与已登记 M. G. F. Martin 异人'),
    ('Ruth Chang', 'Ruth Chang' + EN, '美国', '—', 'Q7382918',
     '价值不可通约性与抉择理论；Wikidata 无生卒'),
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
out = os.path.join(RES, 'rowspec-batch36-people.json')
json.dump({'batch': '058-batch36-people', 'date': '2026-11-24',
           'scope': '人名第十批（22 人，Wikidata／网页逐人取证）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

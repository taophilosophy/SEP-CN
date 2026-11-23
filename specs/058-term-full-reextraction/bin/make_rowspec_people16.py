# -*- coding: utf-8 -*-
"""人名第十六批 rowspec（2026-11-24）：教父与中世纪、汉传佛教、道教、
藏传佛教、环境与技术哲学、黑人研究 17 人，Wikidata／网页取证。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b16.tsv'
EN = '（无通行汉名，保留英文原名）'

PEOPLE = [
    ('Ambrose', '安布罗斯', '古罗马（米兰）', '约339–397', 'Q43689',
     '米兰主教，教父；《论责任》'),
    ('Irenaeus', '爱任纽', '小亚细亚／高卢（里昂）', '约130–约202', 'Q182123',
     '《驳异端》，教父神学'),
    ('Novatian', '诺瓦天', '古罗马', '约220–258', 'Q222890',
     '三世纪罗马神学家；Wikidata 生卒为近似值'),
    ('Isidore of Seville', '塞维利亚的伊西多尔', '西哥特王国（西班牙）',
     '约560–636', 'Q166876', '《词源》，中世纪百科全书传统'),
    ('Basil of Caesarea', '凯撒利亚的巴西尔', '卡帕多细亚（罗马帝国）',
     '约329–379', 'Q44258', '卡帕多细亚教父；《hexaemeron》'),
    ('Cassiodorus', '卡西奥多鲁斯', '东哥特王国／拜占庭', '约487–约583',
     'Q192365', '《神圣文献与世俗文献提要》，修道院学术传统'),
    ('Zhanran', '湛然', '中国（唐）', '711–782', 'Q2305079',
     '天台宗六祖，无情有性说'),
    ('Cheng Xuanying', '成玄英', '中国（唐）', '约7世纪（活动期）', 'Q1069899',
     '重玄学与《庄子疏》；Wikidata 生卒为占位值不取'),
    ('Mipham', '米滂', '西藏', '1846–1912（传统纪年）', 'Q6871584',
     '宁玛派学者米滂·蒋贝甲措；Wikidata 无生卒，取通行纪年'),
    ('Atiśa', '阿底峡', '孟加拉（波罗王朝）／西藏', '982–1054', 'Q320150',
     '噶当派奠基者，《菩提道灯论》'),
    ('Arne Næss', '阿恩·奈斯', '挪威', '1912–2009', 'Q335152',
     '深层生态学；经验语义学'),
    ('Andrew Feenberg', '安德鲁·芬伯格', '美国（任教加拿大）', '1943–',
     'Q2846598', '技术批判理论（《技术批判理论》）'),
    ('Don Ihde', '唐·伊德', '美国', '1934–2024', 'Q5292818',
     '技术现象学与后现象学'),
    ('Trevor Pinch', '特雷弗·平奇', '英国／美国', '1952–2021', 'Q3538596',
     '科学知识社会学与技术的社会建构'),
    ('Debra Satz', '黛布拉·萨茨', '美国', '1956–', 'Q5248510',
     '市场伦理与平等（《Why Some Things Should Not Be for Sale》）'),
    ('Sylvia Wynter', '西尔维娅·温特', '牙买加／美国', '1928–', '—',
     '黑人研究与人文学科认识论（“human as praxis”）；'
     '英文维基条目（无 Wikidata 人格项）记 1928-05-11 生（2026-11-24 查）'),
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
out = os.path.join(RES, 'rowspec-batch42-people.json')
json.dump({'batch': '058-batch42-people', 'date': '2026-11-24',
           'scope': '人名第十六批（16 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

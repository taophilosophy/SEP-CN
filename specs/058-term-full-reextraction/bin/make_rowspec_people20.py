# -*- coding: utf-8 -*-
"""人名第二十批 rowspec（2026-11-24）：古典柏拉图主义、日本京都学派、
印度现代、当代中国哲学 8 人，Wikidata 取证。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b20.tsv'

PEOPLE = [
    ('Atticus', '阿提库斯', '古希腊（雅典）', '约150–约200', 'Q758060',
     '中期柏拉图主义者，反亚里士多德《论<蒂迈欧>中的宇宙生成》'),
    ('Miki Kiyoshi', '三木清', '日本', '1897–1945', 'Q1894578',
     '京都学派与「构想力」的逻辑；《历史哲学》'),
    ('Sri Aurobindo', '室利·阿罗频多', '印度', '1872–1950', 'Q192207',
     '整体不二论与「超心智进化」'),
    ('Swami Vivekananda', '辨喜', '印度', '1863–1902', 'Q47478',
     '新吠檀多与实践瑜伽（芝加哥宗教议会 1893）'),
    ('Sarvepalli Radhakrishnan', '萨瓦帕利·拉达克里希南', '印度', '1888–1975',
     'Q156349', '新吠檀多与比较宗教哲学；印度第二任总统'),
    ('Zhang Dainian', '张岱年', '中国', '1909–2004', 'Q11066965',
     '中国哲学范畴史（《中国哲学大纲》）'),
    ('Liu Xiaogan', '刘笑敢', '中国', '1947–', 'Q98097728',
     '道家与郭店楚简研究；Wikidata 项描述为「professor of Chinese religion '
     'and culture」，无 P27，籍属据其中文姓名与著作记中国'),
    ('Jiang Qing', '蒋庆', '中国', '—', '—',
     '大陆新儒家（政治儒学）；无 Wikidata 人格项、英文维基无条目，生卒留白'),
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
out = os.path.join(RES, 'rowspec-batch46-people.json')
json.dump({'batch': '058-batch46-people', 'date': '2026-11-24',
           'scope': '人名第二十批（8 人）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

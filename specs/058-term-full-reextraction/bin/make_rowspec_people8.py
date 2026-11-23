# -*- coding: utf-8 -*-
"""人名第八批 rowspec（2026-11-24）：六人，Wikidata 取证。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b8.tsv'

PEOPLE = [
    ('Cook Wilson', 'Cook Wilson（无通行汉名，保留英文原名）', '英国',
     '1849–1915', 'Q3817476',
     '牛津大学哲学家，命题知识与“实用主义倒转”论题'),
    ('Kristie Dotson', 'Kristie Dotson（无通行汉名，保留英文原名）', '美国',
     '—', 'Q57756823',
     '认识论中的压迫与「无知认识论」（epistemology of ignorance）研究；在世，Wikidata 无生卒'),
    ('John Finnis', '约翰·菲尼斯', '澳大利亚／美国', '1940–', 'Q3312283',
     '自然法理论家；《自然法与自然权利》通行汉译用「菲尼斯」'),
    ('Shannon Sullivan', 'Shannon Sullivan（无通行汉名，保留英文原名）',
     '美国', '—', 'Q21062465',
     '女性主义哲学与批判种族理论；在世，Wikidata 无生卒'),
    ('Van Bendegem', 'Van Bendegem（无通行汉名，保留英文原名）', '—',
     '1953–', 'Q2229166',
     '数学哲学家（布鲁塞尔自由大学）；Wikidata P27 记荷兰王国，学界通说比利时人，籍属存疑不写'),
    ('Philip Quinn', '菲利普·奎因', '美国', '1940–2004', 'Q7183930',
     '宗教哲学家；与已登记的 Warren Quinn（沃伦·奎因）为异人'),
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
out = os.path.join(RES, 'rowspec-batch34-people.json')
json.dump({'batch': '058-batch34-people', 'date': '2026-11-24',
           'scope': '人名第八批（Wikidata 逐人取证）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

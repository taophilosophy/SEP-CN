# -*- coding: utf-8 -*-
"""著作名第三十批 rowspec（2026-11-24）：6–7 频次段 16 部。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch30-2026-11-24.md'

WORKS = [
    ('Reconstruction in Philosophy', '《哲学的改造》',
     '许崇清译，商务印书馆 1958（汉译世界学术名著，ISBN 9787100005159）；'
     '2009-04 珍藏本（ISBN 9787100059923）'),
    ('Introduction to the Human Sciences', '《精神科学引论》',
     '艾彦译，译林出版社 2014-10（汉译经典名著，第一卷，ISBN 9787544749633）'),
    ('The System of Nature', '《自然的体系》',
     '管士滨译，商务印书馆 1999-03（汉译世界学术名著，ISBN 9787100024914）'),
    ('Discourses on Livy', '《论李维》',
     '冯克利译，上海人民出版社 2005-05（世纪文库，ISBN 9787208053625）；'
     '2012-04 版（ISBN 9787208104907）'),
    ('De officiis', '《论义务》',
     '本库译名（西塞罗著；王焕生译本，中国政法大学出版社 1999）'),
    ('The American Scholar', '《美国学者》',
     '本库译名（爱默生演讲，1837；语料 7 处一致）'),
    ('The Education of a Christian Prince', '《论基督君主的教育》',
     '本库译名（伊拉斯谟著，1516；语料 7 处一致）'),
    ('De fato', '《论命运》',
     '本库译名（西塞罗著，残篇；语料 7 处一致）'),
    ('The Principles of Logic', '《逻辑原理》',
     '本库译名（布拉德雷著，1883；语料 6 处一致）'),
    ('Cosmogony', '《宇宙发生论》',
     '本库译名（厄棱费尔著；语料 6 处一致）'),
    ('Pensées diverses sur la comète', '《关于彗星的种种思考》',
     '本库译名（培尔著，1682；语料 6 处一致）'),
    ('Beauty and Other Forms of Value', '《美与其他价值形式》',
     '本库译名（亚历山大著，1933；语料 6 处一致）'),
    ('Moral Thinking', '《道德思维》',
     '本库译名（黑尔著，1981；语料 6 处一致）'),
    ('Sefer ha-Mevaqqesh', '《求索者之书》',
     '本库译名（法拉奎拉著，1263；语料 6 处一致）'),
    ('Deʿot ha-Filosofim', '《哲学家之意见》',
     '本库译名（法拉奎拉百科全书式著作；语料 6 处一致）'),
    ('Tantravārttika', '《随文释补》',
     '本库译名（鸠摩利罗著，《颂释补》姊妹篇；语料 6 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works30.json')
json.dump({'batch': '058-batch58-works30', 'date': '2026-11-24',
           'scope': '著作名第三十批（6–7 频次段 16 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

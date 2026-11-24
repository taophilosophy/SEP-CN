# -*- coding: utf-8 -*-
"""著作名第十九批 rowspec（2026-11-24）：中文侧高频差集第二组 9 部。

键取英文语料 <em> 原形；译名取中文语料通行形。Defensor Pacis 短形“保卫者”
另由 patch_works19.py 补入既有行，不另立行。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch19-2026-11-24.md'

WORKS = [
    ('Sentences', '《箴言四书》',
     '学界通行（《箴言四书》为中世纪经院哲学通行译名，见在册 Sentences Commentary 行；'
     '未见全译本，语料 47 处一致）'),
    ('Kuzari', '《库扎里》',
     '学界通行（犹太学文献通行音译；未见中译本，语料 39 处一致）'),
    ('Phaedrus', '《斐德罗篇》',
     '朱光潜译《柏拉图文艺对话集》收《斐德若篇》，人民文学出版社 1959-12（ISBN 9787020066681；'
     '1963 印次 ISBN 9787020025053）'),
    ('Of the Standard of Taste', '《论趣味的标准》',
     '肖聿译《休谟散文集》收《论趣味的标准》，中国社会科学出版社 2006-10（ISBN 9787500456872）；'
     '吴兴华译收入《石头与星宿：译文集》，广西师范大学出版社 2017'),
    ('An Enquiry Concerning Political Justice', '《政治正义论》',
     '何慕李译，商务印书馆 1997-04（汉译世界学术名著丛书，全 2 册，ISBN 9787100022781）'),
    ('The Spirit of Utopia', '《乌托邦的精神》',
     '梁锡江译《乌托邦精神》，中国社会科学出版社 2025-08（ISBN 9787522750200）；'
     '语料通行形作《乌托邦的精神》'),
    ('Manyōshū', '《万叶集》',
     '杨烈译，湖南人民出版社 1984-07（诗苑译林）；赵乐甡译，译林出版社 2002-04'
     '（ISBN 9787806572115）'),
    ('Awakening of Faith in Mahayana', '《大乘起信论》',
     '真谛译，高振农校释《大乘起信论校释》，中华书局 1992-04（中国佛教典籍选刊第一辑，'
     'ISBN 9787101008050）'),
    ('Universal Natural History and Theory of the Heavens', '《自然通史》',
     '全增嘏译、王福山校《宇宙发展史概论》，上海译文出版社 2001-08（1972-05 上海人民出版社初版）；'
     '李秋零译《一般自然史与天体理论》收入《康德著作全集》第一卷，中国人民大学出版社 2003；'
     '语料通行形作《自然通史》'),
]

rows = []
for en, zh, src in WORKS:
    basis = '权威译本／学界通行（%s；2026-11-24 联网核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works19.json')
json.dump({'batch': '058-batch58-works19', 'date': '2026-11-24',
           'scope': '著作名第十九批（中文侧高频差集第二组 9 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

# -*- coding: utf-8 -*-
"""著作名第十八批 rowspec（2026-11-24）：中文侧反查高引经典 10 部。

选目：译文语料《书名》频次反查在册差集，逐部联网核中译本（书名、译者、社、年、ISBN）。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

WORKS = [
    ('Theaetetus', '《泰阿泰德篇》',
     '詹文杰译《泰阿泰德》，商务印书馆 2018-12（ISBN 9787100164221）；'
     '溥林（熊林）译，希汉对照《柏拉图全集》本，商务印书馆 2022-07（ISBN 9787100211826）'),
    ('Parmenides', '《巴门尼德篇》',
     '陈康译注《巴曼尼得斯篇》，商务印书馆 1982-08（汉译世界学术名著丛书，ISBN 9787100023818）；'
     '王太庆重译收入《柏拉图对话集》（2004）作《巴门尼德篇》'),
    ('Meno', '《美诺篇》',
     '王太庆译《柏拉图对话集》收《枚农篇》，商务印书馆 2004-07（ISBN 9787100036146）；'
     '单行本《卡尔弥德篇 枚农篇》，商务印书馆 2018-11（ISBN 9787100164030）'),
    ('Sophistical Refutations', '《辩谬篇》',
     '苗力田主编《亚里士多德全集》第一卷（工具论）收《辩谬篇》，中国人民大学出版社 1990-09'
     '（ISBN 9787300008509）'),
    ('Discourse on the Method', '《方法谈》',
     '王太庆译本，商务印书馆 2000-11（汉译世界学术名著丛书，ISBN 9787100030908），题作《谈谈方法》；'
     '语料通行形作《方法谈》'),
    ('New Essays on Human Understanding', '《人类理智新论》',
     '陈修斋译，商务印书馆 1982-11（汉译世界学术名著丛书·哲学，ISBN 9787100020107）'),
    ('Spirit of the Laws', '《论法的精神》',
     '张雁深译，商务印书馆 1961-11（上、下册，ISBN 9787100005685／9787100005692）；'
     '2020-12 精装典藏版（ISBN 9787100189484）'),
    ('Prolegomena to Any Future Metaphysics', '《未来形而上学导论》',
     '庞景仁译，全题《任何一种能够作为科学出现的未来形而上学导论》，商务印书馆 1978-08／1997-04'
     '（汉译世界学术名著丛书·哲学，ISBN 9787100017985）'),
    ('Between Facts and Norms', '《在事实与规范之间》',
     '童世骏译《在事实与规范之间：关于法律和民主法治国的商谈理论》，生活·读书·新知三联书店 2003-08'
     '（学术前沿，ISBN 9787108018502）；2014-09 精装（ISBN 9787108051004）'),
    ('The Birth of Tragedy', '《悲剧的诞生》',
     '周国平译，三联书店 1986（《悲剧的诞生：尼采美学文选》，现代西方学术文库，ISBN 9787108005342）；'
     '译林出版社 2011-08（汉译经典，ISBN 9787544720120）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '权威译本（%s；2026-11-24 联网核对，凭证 works-batch18-2026-11-24.md）' % src
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works18.json')
json.dump({'batch': '058-batch58-works18', 'date': '2026-11-24',
           'scope': '著作名第十八批（中文侧反查高引经典 10 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

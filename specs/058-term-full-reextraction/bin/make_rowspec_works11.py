# -*- coding: utf-8 -*-
"""著作名第十一批 rowspec（2026-11-24）：23 部，逐部核对中译本（译者、出版社、出版年）。

依据一律为实际查到的版权信息（豆瓣/馆藏 OPAC/出版社官页），逐条记入依据列；
查证 URL 汇总见 results/works-batch11-2026-11-24.md。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

# (原题, 中译名, 译者·出版社·年份, 备注)
WORKS = [
    ('The Structure of Scientific Revolutions', '《科学革命的结构》',
     '金吾伦、胡新和译，北京大学出版社 2012（第 4 版）', ''),
    ('Discipline and Punish', '《规训与惩罚》',
     '刘北成、杨远婴译，生活·读书·新知三联书店 1999 初版 / 2012 修订译本', ''),
    ('The History of Sexuality', '《性经验史》',
     '佘碧平译，上海人民出版社 2002 初版 / 2016 增订', ''),
    ('Of Grammatology', '《论文字学》',
     '汪堂家译，上海译文出版社 1999 初版 / 2005 再版', ''),
    ('After Virtue', '《德性之后》',
     '龚群、戴扬毅等译，中国社会科学出版社 1995 初版 / 2020 再版',
     '通行别译《追寻美德》（宋继杰译，译林出版社）'),
    ('The Concept of Law', '《法律的概念》',
     '许家馨、李冠宜译，法律出版社 2006 初版 / 2018 第三版', ''),
    ('The Origins of Totalitarianism', '《极权主义的起源》',
     '林骧华译，生活·读书·新知三联书店 2008', ''),
    ('Being and Event', '《存在与事件》',
     '蓝江译，南京大学出版社 2018', ''),
    ('Writing and Difference', '《书写与差异》',
     '张宁译，生活·读书·新知三联书店 2001', ''),
    ('Sources of the Self', '《自我的根源：现代认同的形成》',
     '韩震译，译林出版社 2012', ''),
    ('Taking Rights Seriously', '《认真对待权利》',
     '信春鹰、吴玉章译，中国大百科全书出版社 1998', ''),
    ('The Open Society and Its Enemies', '《开放社会及其敌人》',
     '陆衡等译，中国社会科学出版社 1999', ''),
    ('The Poverty of Historicism', '《历史决定论的贫困》',
     '杜汝楫、邱仁宗译，华夏出版社 1987',
     '另有中译本《历史主义贫困论》'),
    ('The Logic of Scientific Discovery', '《科学发现的逻辑》',
     '查汝强、邱仁宗、万木春译，中国美术学院出版社 2008', ''),
    ('Conjectures and Refutations', '《猜想与反驳：科学知识的增长》',
     '傅季重、纪树立、周昌忠、蒋戈为译，上海译文出版社 1986', ''),
    ('Against Method', '《反对方法：无政府主义知识论纲要》',
     '周昌忠译，上海译文出版社 2007', ''),
    ('Eichmann in Jerusalem', '《艾希曼在耶路撒冷：一份关于平庸的恶的报告》',
     '安尼译，译林出版社 2016', ''),
    ('The Concept of the Political', '《政治的概念》',
     '刘宗坤等译，上海人民出版社 2004（施米特文集）', ''),
    ('Spheres of Justice', '《正义诸领域：为多元主义与平等一辩》',
     '褚松燕译，译林出版社 2002', ''),
    ('The German Ideology', '《德意志意识形态》',
     '中共中央马克思恩格斯列宁斯大林著作编译局译，人民出版社 2003（节选本）', ''),
    ('Capital', '《资本论》',
     '中共中央马克思恩格斯列宁斯大林著作编译局译，人民出版社 2004（第一卷）', ''),
    ('Logic of Sense', '《意义的逻辑》',
     '董树宝译，上海文艺出版社 2024（首个中译本）', ''),
    ('Timaeus', '《蒂迈欧篇》',
     '谢文郁译，上海人民出版社 2005（世纪文库）', ''),
]

rows = []
for en, zh, edition, note in WORKS:
    basis = '权威译本（%s；2026-11-24 联网核对，凭证 works-batch11-2026-11-24.md）' % edition
    if note:
        basis += '；' + note
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch52-works.json')
json.dump({'batch': '058-batch52-works', 'date': '2026-11-24',
           'scope': '著作名第十一批（23 部，逐部核对中译本）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

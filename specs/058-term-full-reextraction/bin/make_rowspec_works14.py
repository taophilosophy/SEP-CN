# -*- coding: utf-8 -*-
"""著作名第十四批 rowspec（2026-11-24）：39 部经典（37 部商务书目＋2 部克尔凯郭尔文集）。"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

CAT = '商务印书馆“汉译世界学术名著丛书”1000 种书目（2024-09-24）'
WORKS = [
    ('Philosophical Fragments', '《哲学片段》', '哲学第 230 号', ''),
    ('De Genesi ad litteram', '《论〈创世记〉》', '哲学第 89 号',
     '书目作“论《创世记》”；奥古斯丁的〈创世记〉字解'),
    ('Kant and the Problem of Metaphysics', '《康德与形而上学疑难》', '哲学第 274 号', ''),
    ('The Metaphysical Foundations of Modern Physical Science',
     '《近代物理科学的形而上学基础》', '哲学第 273 号', '伯特'),
    ('From the Closed World to the Infinite Universe', '《从封闭世界到无限宇宙》',
     '哲学第 254 号', '柯瓦雷；张卜天译'),
    ('The Logical Structure of the World', '《世界的逻辑构造》', '哲学第 298 号', '卡尔纳普'),
    ('The Transcendence of the Ego', '《自我的超越性》', '哲学第 247 号', '萨特'),
    ('The Structure of Behavior', '《行为的结构》', '哲学第 44 号', '梅洛-庞蒂'),
    ('How to Do Things with Words', '《如何以言行事》', '哲学第 149 号', '奥斯汀'),
    ('An Inquiry into Meaning and Truth', '《意义与真理的探究》', '哲学第 220 号', '罗素'),
    ('Philosophy and the Mirror of Nature', '《哲学和自然之镜》', '哲学第 228 号', '罗蒂'),
    ('Contributions to Philosophy', '《哲学论稿》', '哲学第 229 号', '海德格尔'),
    ('On the Way to Language', '《在通向语言的途中》', '哲学第 224 号', '海德格尔'),
    ('What Is Called Thinking?', '《什么叫思想？》', '哲学第 296 号', '海德格尔'),
    ('Pathmarks', '《路标》', '哲学第 81 号', '海德格尔'),
    ('Holzwege', '《林中路》', '哲学第 78 号', '海德格尔；孙周兴译'),
    ('Philosophy of New Music', '《新音乐的哲学》', '哲学第 312 号', '阿多诺'),
    ('The Human Place in the Cosmos', '《人在宇宙中的地位》', '哲学第 295 号', '舍勒'),
    ('I and Thou', '《我与你》', '哲学第 305 号', '布伯'),
    ('Thought and Reality', '《思想与实在》', '哲学第 299 号', '达米特'),
    ('Logical Investigations', '《逻辑研究》', '哲学第 109 号', '胡塞尔；倪梁康译'),
    ('On the Phenomenology of the Consciousness of Internal Time',
     '《内时间意识现象学》', '哲学第 120 号', '胡塞尔'),
    ('The Crisis of European Sciences', '《欧洲科学的危机与超越论的现象学》',
     '哲学第 124 号', '胡塞尔'),
    ('Contributions to the Theory of Transfinite Numbers', '《超穷数理论基础》',
     '哲学第 11 号', '康托'),
    ('De revolutionibus', '《天球运行论》', '哲学第 184 号', '哥白尼'),
    ('The Mathematical Principles of Natural Philosophy', '《自然哲学的数学原理》',
     '哲学第 244 号', '牛顿'),
    ('What Is Life?', '《生命是什么》', '哲学第 157 号', '薛定谔'),
    ('The Computer and the Brain', '《计算机与人脑》', '哲学第 271 号', '冯·诺依曼'),
    ('Cybernetics', '《控制论》', '哲学第 277 号', '维纳'),
    ('The Human Use of Human Beings', '《人有人的用处》', '哲学第 145 号', '维纳'),
    ('Silent Spring', '《寂静的春天》', '哲学第 272 号', '卡森'),
    ('The Sociology of Science', '《科学社会学》', '哲学第 64 号', '默顿'),
    ('Science, Technology and Society in Seventeenth-Century England',
     '《十七世纪英格兰的科学、技术与社会》', '哲学第 163 号', '默顿'),
    ('The Grand Titration', '《文明的滴定》', '哲学第 188 号', '李约瑟'),
    ('The Beginnings of Western Science', '《西方科学的起源》', '哲学第 307 号', '林德伯格'),
    ('The Social Function of Science', '《科学的社会功能》', '哲学第 275 号', '贝尔纳'),
    ('Newtonian Studies', '《牛顿研究》', '哲学第 292 号', '柯瓦雷'),
    ('The Sickness unto Death', '《致死的疾病》', '克尔凯郭尔文集第 6 卷',
     '京不特译，中国社会科学出版社 2013（与《畏惧与颤栗》《恐惧的概念》合刊）'),
    ('Either/Or', '《非此即彼：一个生命的残片》', '克尔凯郭尔文集第 2–3 卷',
     '京不特译，中国社会科学出版社 2009'),
]

rows = []
for en, zh, where, note in WORKS:
    if where.startswith('克尔凯郭尔'):
        basis = ('权威译本（%s，%s；2026-11-24 联网核对，凭证 '
                 'works-batch14-2026-11-24.md）' % (where, note))
    else:
        basis = '权威译本（%s·%s 载此书名；2026-11-24 查，凭证 works-batch10-2026-11-24.md）' % (
            CAT, where)
        if note:
            basis += '；' + note
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch55-works.json')
json.dump({'batch': '058-batch55-works', 'date': '2026-11-24',
           'scope': '著作名第十四批（39 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

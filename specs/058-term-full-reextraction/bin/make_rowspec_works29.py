# -*- coding: utf-8 -*-
"""著作名第二十九批 rowspec（2026-11-24）：跨传统补漏 16 部。

La Dioptrique 补语料另形“屈光学”由 patch_works29.py 补。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch29-2026-11-24.md'

WORKS = [
    ('The Principle of Hope', '《希望的原理》',
     '梦海译，上海译文出版社 2012-12（第一卷，ISBN 9787532755660）'),
    ('In Praise of Folly', '《愚人颂》',
     '许崇信译，辽宁教育出版社 2001-02（新世纪万有文库，ISBN 9787538258943）；'
     '刘曙光译，北京图书馆出版社 1999-06'),
    ('The Two Sources of Morality and Religion', '《道德与宗教的两个来源》',
     '王作虹、成穷译，贵州人民出版社 2000-10（ISBN 9787221052520）；'
     '译林出版社 2014-10（汉译经典，ISBN 9787544749985）'),
    ('Democracy and Education', '《民主与教育》',
     '王承绪译《民主主义与教育》，人民教育出版社 2001-05（外国教育名著丛书，ISBN 9787107106873）'),
    ('Against Method', '《反对方法》',
     '周昌忠译《反对方法：无政府主义知识论纲要》，上海译文出版社 1992-01／2007-08'
     '（二十世纪西方哲学译丛，ISBN 9787532742738）'),
    ('Lotus Sutra', '《法华经》',
     '汉译佛典通行经题（鸠摩罗什译《妙法莲华经》；非抉择项）'),
    ('The Four Books', '《四书》',
     '汉文经典通行名（《大学》《中庸》《论语》《孟子》，朱熹章句集注系统；非抉择项）'),
    ('Self-Reliance', '《自立》',
     '本库译名（爱默生论文，1841；通译《自立》，收入多部随笔译本）'),
    ('Enchiridion militis christiani', '《基督精兵手册》',
     '本库译名（伊拉斯谟著，1503；语料 8 处一致）'),
    ('Mabādiʾ ārāʾ ahl al-madīna al-fāḍila', '《德性城邦》',
     '本库译名（法拉比著；全题《德性城邦居民的原理与意见》；语料 8 处一致）'),
    ('Sefer ha-Qabbalah', '《传统之书》',
     '本库译名（伊本·达乌德史学著作，约 1160／61；语料 8 处一致）'),
    ('De substantia orbis', '《论天体实体》',
     '本库译名（阿威罗伊著；语料 8 处一致）'),
    ('De Sensibus', '《论感觉》',
     '本库译名（特奥弗拉斯托斯短论；语料 8 处一致）'),
    ('al-Mabāḥith al-mashriqiyya', '《东方探究》',
     '本库译名（法赫尔丁·拉齐著；语料 8 处一致）'),
    ('Strix', '《女巫》',
     '本库译名（詹弗朗切斯科·皮科著，1523；意大利文译本 1524；语料 8 处一致）'),
    ('Ordinatio', '《奥狄纳齐奥》',
     '本库译名（邓斯·司各脱著；语料 8 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 联网／语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works29.json')
json.dump({'batch': '058-batch58-works29', 'date': '2026-11-24',
           'scope': '著作名第二十九批（跨传统补漏 16 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

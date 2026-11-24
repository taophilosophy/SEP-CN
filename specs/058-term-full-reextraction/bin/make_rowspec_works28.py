# -*- coding: utf-8 -*-
"""著作名第二十八批 rowspec（2026-11-24）：跨传统稀见题 16 部。

on generation and corruption、sophist 两行异形由 patch_works28.py 补。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch28-2026-11-24.md'

WORKS = [
    ('De libero arbitrio', '《论自由意志》',
     '本库译名（奥古斯丁著；语料 9 处一致）'),
    ('Proofs and Refutations', '《证明与反驳》',
     '康宏逵译《证明与反驳：数学发现的逻辑》，上海译文出版社 1987-10（二十世纪西方哲学译丛）'),
    ('The Literary Work of Art', '《文学的艺术作品》',
     '本库译名（英伽登著；中国文联出版公司 1988-01 中译本《对文学的艺术作品的认识》（陈燕谷、晓未译，'
     'ISBN 9787505902817）系另一著作 The Cognition of the Literary Work of Art）'),
    ('Kitāb al-Shifāʾ', '《治疗论》',
     '本库译名（伊本·西那百科全书，约 1027；语料 9 处一致）'),
    ('Chaldean Oracles', '《迦勒底神谕》',
     '本库译名（新柏拉图主义秘传文献；语料 9 处一致）'),
    ('Kojiki', '《古事记》',
     '周作人译，上海人民出版社 2015-08（2001 中国对外翻译出版公司初版，苦雨斋译丛，'
     'ISBN 9787500107941）'),
    ('Concerning the End for Which God Created the World', '《创世的目的》',
     '本库译名（爱德华兹著，1765 身后刊行；语料 9 处一致）'),
    ('Fifteen Sermons', '《布道文》',
     '本库译名（巴特勒著，1726；语料 10 处一致）'),
    ('Kitāb al-Ḥudūd', '《定义书》',
     '本库译名（伊斯拉埃利著，约 10 世纪；语料 9 处一致）'),
    ('Summa philosophiae', '《哲学大全》',
     '本库译名（十三世纪匿名著作，曾误归格罗斯泰斯特名下；语料 9 处一致）'),
    ('Reshit Hokhmah', '《智慧之始》',
     '本库译名（法拉奎拉著；语料 9 处一致）'),
    ('al-Jadīd fī ʾl-ḥikma', '《新智慧》',
     '本库译名（库特布丁·设拉子著；语料 9 处一致）'),
    ('Nova dilucidatio', '《新阐明》',
     '本库译名（康德著，1755；语料 9 处一致）'),
    ('A Discourse Concerning the Love of God', '《论上帝之爱》',
     '本库译名（达玛里斯·玛莎姆著，1696；语料 9 处一致）'),
    ('Observationes Medicae', '《医学观察》',
     '本库译名（托马斯·西德纳姆著，1676；语料 9 处一致）'),
    ('ha-Emunah ha-Ramah', '《崇高的信仰》',
     '本库译名（伊本·达乌德著，约 1160；英译 The Exalted Faith；语料 8 处一致）'),
    ('Scriptum super primum Sententiarum', '《箴言书疏》',
     '本库译名（奥雷奥利著；语料 9 处一致）'),
    ('Expositio in libros Physicorum', '《物理学注疏》',
     '本库译名（奥卡姆著；语料 9 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works28.json')
json.dump({'batch': '058-batch58-works28', 'date': '2026-11-24',
           'scope': '著作名第二十八批（跨传统稀见题 16 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

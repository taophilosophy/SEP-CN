# -*- coding: utf-8 -*-
"""著作名第二十四批 rowspec（2026-11-24）：稀见题第三组 11 部。

Sentences、Discourse on Metaphysics 两行异形由 patch_works24.py 补。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch24-2026-11-24.md'

WORKS = [
    ('Le Monde', '《世界》',
     '本库译名（笛卡尔遗著，Clerselier 编；语料 18 处一致）'),
    ('De occulta philosophia', '《论秘术哲学》',
     '本库译名（阿格里帕著，1531–1533；语料 14 处一致）'),
    ('Risālah fī al-ʿaql', '《论理智》',
     '本库译名（法拉比著；亚历山大同名论著 De intellectu 亦译《论理智》，按语境分指；语料 14 处一致）'),
    ('Adversus Mathematicos', '《驳数学家》',
     '本库译名（塞克斯都·恩披里柯著；语料 12 处一致）'),
    ('Kashf al-Asrār', '《揭开通向思想幽微之秘》',
     '本库译名（胡纳吉著；全题 Kashf al-Asrār ʿan Ghawāmiḍ al-Afkār，英译 The Disclosure of Secrets；'
     '语料 14 处一致，正文多简称拉丁题）'),
    ('Pulssi chappyŏn', '《佛氏杂辨》',
     '本库译名（郑道传著，14 世纪末；英译 Array of Critiques of Mr. Buddha；语料 14 处一致）'),
    ('Of Being', '《论存在》',
     '本库译名（爱德华兹短论；同名他著按语境分指；语料 15 处一致）'),
    ('Essay on the Passions', '《论激情》',
     '本库译名（哈奇森著；全题 An Essay on the Nature and Conduct of the Passions and Affections；'
     '语料 13 处一致）'),
    ('Kitāb al-siyāsa al-madaniyya', '《政治体制》',
     '本库译名（法拉比著；亦名《存在物的原理》；语料 13 处一致）'),
    ('Réflexions critiques', '《批判反思》',
     '本库译名（杜博斯著，1719；全题《诗与画批判反思》；语料 18 处一致）'),
    ('Yesod Mora', '《敬畏之基》',
     '本库译名（伊本·以斯拉著，晚年论圣经诫命；语料 12 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works24.json')
json.dump({'batch': '058-batch58-works24', 'date': '2026-11-24',
           'scope': '著作名第二十四批（稀见题第三组 11 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

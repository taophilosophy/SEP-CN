# -*- coding: utf-8 -*-
"""著作名第二十三批 rowspec（2026-11-24）：中世纪／近代稀见题 19 部。

键取语料原形（拉丁／希伯来／梵文／阿拉伯转写）；有同名多著的键加人物括注。
Proslogion、Elements of Theology 两行异形由 patch_works23.py 补。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')

EV = 'works-batch23-2026-11-24.md'

WORKS = [
    ('Essays on the Intellectual Powers of Man', '《人类心灵论文集》',
     '本库译名（里德著，Brookes 编；语料 32 处一致；中译本通行题《论人的理智能力》）'),
    ('Zubdat al-ḥaqāʾiq', '《实在的精髓》',
     '本库译名（艾因·古达特著，约 1120 年代；语料 30 处一致；未见中译本）'),
    ('Reply to Porphyry', '《答波菲利》',
     '本库译名（杨布里科斯著；全题《阿巴蒙大师对波菲利致阿涅波书信的答复》；'
     '拉丁传统题 De mysteriis／《论埃及秘仪》；语料 27 处一致）'),
    ('De modis significandi', '《论意指样式》',
     '本库译名（埃尔福特的托马斯著，1310 年前；摩迪斯泰派标准教科书；语料 22 处一致）'),
    ('al-Maṭālib al-ʿāliya', '《至高论题》',
     '本库译名（法赫鲁丁·拉齐晚年《大全》；全题 al-Maṭālib al-ʿāliya min al-ʿilm al-ilāhī；'
     '语料 21 处一致）'),
    ('Sefer ha-ʿIqqarim', '《原则之书》',
     '本库译名（约瑟夫·阿尔博著，1425；语料 21 处一致；未见中译本）'),
    ('De constantia', '《论坚定》',
     '本库译名（利普修斯著，1584；斯多葛式对话；语料 21 处一致）'),
    ('De divina omnipotentia', '《论神圣全能》',
     '本库译名（伯多禄·达弥盎著，约 1067；语料 21 处一致）'),
    ('On First Philosophy (al-Kindi)', '《论第一哲学》',
     '本库译名（肯迪著，题献穆塔西姆；阿拉伯题 Fī al-falsafa al-ūlā；语料 18 处一致）'),
    ('Tractatus de universalibus', '《论共相》',
     '本库译名（同名两著：布里丹与彭比古尔各有此题；语料 18 处一致，按语境分指）'),
    ('De vanitate', '《论虚妄》',
     '本库译名（阿格里帕著，1530；全题 De incertitudine et vanitate scientiarum；语料 17 处一致）'),
    ('Beḥinat ha-Dat', '《信仰的考察》',
     '本库译名（以利亚·德尔梅第戈著，1490 年代；英译 Examination of Religion；语料 17 处一致）'),
    ('The Nature of True Virtue', '《真美德》',
     '本库译名（爱德华兹著，1765 身后刊行；语料 16 处一致）'),
    ('Ślokavārttika', '《颂释补》',
     '本库译名（鸠摩利罗著，偈颂体批判注释；语料 16 处一致；未见中译本）'),
    ('Theologia Aristotelis', '《亚里士多德神学》',
     '本库译名（普罗提诺作品的阿拉伯语改编本；语料 15 处一致）'),
    ('Space, Time, and Deity', '《空间、时间与神性》',
     '本库译名（亚历山大著，1920；语料 15 处一致）'),
    ('The Creative Mind', '《创造的心灵》',
     '本库译名（柏格森文集，1934；法文原题 La Pensée et le mouvant；语料 15 处一致）'),
    ('Discourses (Epictetus)', '《论说集》',
     '本库译名（爱比克泰德著；语料 22 处一致；键加人物括注避与《方法谈》等混淆）'),
    ('Placita', '《学说说》',
     '本库译名（伪普鲁塔克／埃提乌斯系统，公元 2 世纪；五卷自然哲学；语料 22 处一致）'),
]

rows = []
for en, zh, src in WORKS:
    basis = '%s（2026-11-24 语料核对，凭证 %s）' % (src, EV)
    rows.append({'en': en, 'zh': zh, 'table': 'term',
                 'first_seen': '语料回收（specs/058 全库提取）',
                 'basis': basis, 'date': '2026-11-24'})
out = os.path.join(RES, 'rowspec-batch58-works23.json')
json.dump({'batch': '058-batch58-works23', 'date': '2026-11-24',
           'scope': '著作名第二十三批（中世纪／近代稀见题 19 部）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
print('rows=%d -> %s' % (len(rows), out))

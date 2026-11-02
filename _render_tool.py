# -*- coding: utf-8 -*-
"""Render c/<slug>.md from _asm_<slug>.json + header config. Deep-entry format."""
import re, sys, json

MON = {'Jan':'1','Feb':'2','Mar':'3','Apr':'4','May':'5','Jun':'6','Jul':'7','Aug':'8','Sep':'9','Oct':'10','Nov':'11','Dec':'12'}

def trans_date(line):
    m = re.search(r'First published\s+\w+\s+(\w+)\s+(\d+),?\s+(\d{4})', line)
    m2 = re.search(r'substantive revision\s+\w+\s+(\w+)\s+(\d+),?\s+(\d{4})', line)
    fp = f'首次发表于 {m.group(3)} 年 {MON.get(m.group(1),m.group(1))} 月 {int(m.group(2))} 日' if m else '首次发表于'
    sr = f'{m2.group(3)} 年 {MON.get(m2.group(1),m2.group(1))} 月 {int(m2.group(2))} 日实质修订' if m2 else '实质修订'
    return f'**{fp}；{sr}。**'

CONFIG = {
 'chinese-phil-medicine': {
   'h1_zh': '中国哲学与中医', 'en_title': 'Chinese medicine', 'author': 'Lisa Raphals',
   'headers': {
     '## 1. Introduction: Shared Intellectual Contexts': '## 1 导言：共同的思想背景',
     '### 1.1 *Yin-yang*, *Qi* and *Wuxing*': '### 1.1 阴阳、气与五行',
     '### 1.2 Body, State and Cosmos': '### 1.2 身体、国家与宇宙',
     '## 2. Nurturing Life (*yang sheng*)': '## 2 养生',
     '## 3. Daoist Medical Traditions and Physicians': '## 3 道教医学传统与医家',
     '### 3.1 Ge Hong': '### 3.1 葛洪',
     '### 3.2 Tao Hongjing': '### 3.2 陶弘景',
     '### 3.3 Sun Simiao': '### 3.3 孙思邈',
     '## 4. Zhang Xichun on Chinese Philosophy and Chinese Medicine': '## 4 张锡纯论中国哲学与中国医学',
     '## 5. Conclusion': '## 5 结语',
   },
 },
 'children': {
   'h1_zh': '儿童哲学', 'en_title': 'children, philosophy for', 'author': 'Michael Pritchard',
   'headers': {
     '## 1. Can Children Philosophize?': '## 1 儿童能进行哲学思考吗？',
     '## 2. Philosophy in a Crowded Curriculum': '## 2 拥挤课程中的哲学',
     '## 3. The Institute for the Advancement of Philosophy for Children (IAPC)': '## 3 儿童哲学促进协会（IAPC）',
     '## 4. Philosophizing With Others?': '## 4 与他人一起做哲学？',
     '## 5. Philosophy For Children Today': '## 5 今日的儿童哲学',
   },
 },
 'computability': {
   'h1_zh': '可计算性与复杂度', 'en_title': 'computability and complexity', 'author': 'Neil Immerman',
   'headers': {
     '## 1. What can be computed in principle? Introduction and History': '## 1 原则上能计算什么？导言与历史',
     '## 2. Turing Machines': '## 2 图灵机',
     '### 2.1 Universal Machines': '### 2.1 通用机',
     '### 2.2 The Halting Problem': '### 2.2 停机问题',
     '### 2.3 Computable Functions and Enumerability': '### 2.3 可计算函数与可枚举性',
     '### 2.4 The Unsolvability of the Halting Problem': '### 2.4 停机问题的不可解性',
     '## 3. Primitive Recursive Functions': '## 3 原始递归函数',
     '### 3.1 Recursive Functions': '### 3.1 递归函数',
     '## 4. Computational Complexity: Functions Computable in Practice': '## 4 计算复杂性：实践中可计算的函数',
     '### 4.1 Reductions and Completeness': '### 4.1 归约与完全性',
     '### 4.2 Significance of Complexity': '### 4.2 复杂性的意义',
   },
 },
 'copernicus': {
   'h1_zh': '尼古拉·哥白尼', 'en_title': 'Nicolaus Copernicus', 'author': 'Sheila Rabin',
   'headers': {
     '## 1. Life and Works': '## 1 生平与著作',
     '## 2. Astronomical Ideas and Writings': '## 2 天文学思想与著作',
     '### 2.1 Pre-Copernican Astronomy': '### 2.1 前哥白尼天文学',
     '### 2.2 The *Commentariolus*': '### 2.2 《短论》（*Commentariolus*）',
     '### 2.3 *On the Revolutions*': '### 2.3 《天体运行论》（*On the Revolutions*）',
     '### 2.4 Rheticus and the *Narratio prima*': '### 2.4 雷蒂库斯与《初述》（*Narratio prima*）',
     '### 2.5 Printing *On the Revolutions* and Osiander’s Preface': '### 2.5 《天体运行论》的刊印与奥西安德尔的序言',
     '### 2.6 Sixteenth Century Reactions to *On the Revolutions*': '### 2.6 十六世纪对《天体运行论》的反应',
   },
 },
 'condemnation': {
   'h1_zh': '1277 年巴黎谴责', 'en_title': 'condemnation of 1277', 'author': 'Hans Thijssen',
   'headers': {
     '## 1. The events leading up to March 7, 1277': '## 1 1277 年 3 月 7 日之前的事件',
     '## 2. The juridical context of Tempier’s condemnation': '## 2 坦皮尔谴责的法理背景',
     '## 3. What was condemned?': '## 3 谴责了什么？',
     '## 4. Who was condemned on March 7, 1277?': '## 4 1277 年 3 月 7 日谁被谴责？',
     '## 5. The doctrinal significance of Tempier’s condemnation': '## 5 坦皮尔谴责的教义意义',
     '## 6. Tempier’s other 1277 condemnations': '## 6 坦皮尔 1277 年的其他谴责',
   },
 },
 'conceptual-art': {
   'h1_zh': '概念艺术', 'en_title': 'Conceptual Art', 'author': 'Elisabeth Schellekens',
   'headers': {
     '## 1. Conceptual Art – What Is It?': '## 1 概念艺术——它是什么？',
     '### 1.1 Introduction': '### 1.1 导言',
     '### 1.2 The Limits of Art and the Role of Artists': '### 1.2 艺术的边界与艺术家的角色',
     '### 1.3 Artistic Media': '### 1.3 艺术媒介',
     '### 1.4 Art as Idea': '### 1.4 作为观念的艺术',
     '### 1.5 Semantic Representation': '### 1.5 语义呈现',
     '## 2. The Philosophy of Conceptual Art – What is it?': '## 2 概念艺术的哲学——它是什么？',
     '## 3. Five Philosophical Themes': '## 3 五个哲学主题',
     '### 3.1 The Definition of Art': '### 3.1 艺术的定义',
     '### 3.2 The Ontology and Media of Art': '### 3.2 艺术的本体论与媒介',
     '### 3.3 The Aesthetic Value of Art': '### 3.3 艺术的审美价值',
     '### 3.4 The Interpretation of Art': '### 3.4 艺术的诠释',
     '### 3.5 The Cognitive Value of Art': '### 3.5 艺术的认知价值',
     '## 4. Further Questions': '## 4 进一步的问题',
   },
 },
}

TAIL = {
  '## References（引用注释）': '## 参考文献',
  '## Academic Tools': '## 学术工具',
  '## Other Internet Resources': '## 其他网络资源',
  '## Related Entries': '## 相关词条',
}

def render(slug):
    cfg = CONFIG[slug]
    blocks = json.load(open(f'_asm_{slug}.json', encoding='utf-8'))
    out = []
    nmiss = 0
    for typ, txt in blocks:
        if typ == 'h1':
            out.append(f"# {cfg['h1_zh']} {cfg['en_title']} ({cfg['author']})")
        elif typ == 'date':
            out.append(trans_date(txt))
        elif typ == 'author':
            pass
        elif typ == 'header':
            tr = cfg['headers'].get(txt.strip())
            out.append(tr if tr else txt.strip())
        elif typ == 'para':
            if txt.startswith('<<<MISSING>>>'):
                nmiss += 1
                out.append('<<<MISSING>>>' + txt[len('<<<MISSING>>>'):])
            else:
                out.append(txt)
        elif typ == 'tail':
            for o, t in TAIL.items():
                txt = txt.replace(o, t)
            out.append(txt)
    md = '\n\n'.join(o for o in out if o is not None and o.strip())
    md = re.sub(r'\n{3,}', '\n\n', md)
    open(f'c/{slug}.md', 'w', encoding='utf-8').write(md)
    print(f'RENDERED {slug}: {len(md)} chars, missing {nmiss}')

for s in sys.argv[1:]:
    render(s)

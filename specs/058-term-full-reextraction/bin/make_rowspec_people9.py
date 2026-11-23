# -*- coding: utf-8 -*-
"""人名第九批 rowspec（2026-11-24）：55 人，Wikidata 逐人取证。

取 058 语料人名候选（频次≥8、分布≥3 条）中经反查确认未登记者。
凡无通行汉名者，译法列按既有体例记“（无通行汉名，保留英文原名）”。
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
EV = 'people-wikidata-2026-11-24-b9.tsv'
EN = '（无通行汉名，保留英文原名）'

# (键, 译法, 籍属, 生卒/鼎盛年, QID, 备注)
PEOPLE = [
    ('Sharon Street', '莎伦·斯特里特', '美国', '1973–', 'Q28976544',
     '元伦理学建构主义（休谟式建构主义）'),
    ('Susan Haack', '苏珊·哈克', '英国', '1945–2026', 'Q3173010',
     '基础融贯论（foundherentism）；2026-03-10 卒于迈阿密，见迈阿密大学讣告'),
    ('Jean-Luc Marion', '让-吕克·马里翁', '法国', '1946–', 'Q460824',
     '法国现象学与宗教哲学，给予性现象学'),
    ('Terence Horgan', '特伦斯·霍根', '美国', '1948–', 'Q1702848',
     '心灵哲学与元伦理学（非自然主义实在论、语义学）'),
    ('Nathan Salmon', '内森·萨尔蒙', '美国', '1951–', 'Q516801',
     '语言哲学，直接指称论'),
    ('E. J. Lowe', 'E. J. 洛', '英国', '1950–2014', 'Q3742339',
     '本体论与形而上学（四范畴本体论）；勿与同名气象学家 Edward Joseph Lowe 混'),
    ('Ludwik Fleck', '路德维希·弗莱克', '波兰', '1896–1961', 'Q523087',
     '科学知识社会学先驱（思维集体、思维风格）'),
    ('Talcott Parsons', '塔尔科特·帕森斯', '美国', '1902–1979', 'Q203913',
     '社会学家，结构功能主义'),
    ('Charles Lyell', '查尔斯·莱尔', '英国', '1797–1875', 'Q5333',
     '地质学家，均变论；旧译“赖尔”'),
    ('Alexander von Humboldt', '亚历山大·冯·洪堡', '德国（普鲁士）',
     '1769–1859', 'Q6694',
     '博物学家、地理学家；与已登记 Wilhelm von Humboldt（威廉·冯·洪堡）为兄弟异人'),
    ('Alfred Russel Wallace', '阿尔弗雷德·拉塞尔·华莱士', '英国', '1823–1913',
     'Q160627', '博物学家，与达尔文并提的自然选择发现者'),
    ('Simón Bolívar', '西蒙·玻利瓦尔', '委内瑞拉', '1783–1830', 'Q8605',
     '南美独立运动领袖'),
    ('Cass Sunstein', '凯斯·桑斯坦', '美国', '1954–', 'Q956164',
     '法学家，行为经济学与法律；与 Richard Thaler 合著《助推》'),
    ('Andrea Dworkin', '安德烈亚·德沃金', '美国', '1946–2005', 'Q241398',
     '激进女性主义作家；与已登记 Ronald Dworkin（罗纳德·德沃金）异人同姓'),
    ('Angela Davis', '安吉拉·戴维斯', '美国', '1944–', 'Q160456',
     '政治活动家、哲学家（批判种族与监狱问题）'),
    ('Judea Pearl', '朱迪亚·珀尔', '以色列／美国', '1936–', 'Q92824',
     '因果推断与贝叶斯网络'),
    ('Paul Samuelson', '保罗·萨缪尔森', '美国', '1915–2009', 'Q102454',
     '经济学家，新古典综合'),
    ('Huang Zongxi', '黄宗羲', '中国（明末清初）', '1610–1695', 'Q31754',
     '《明夷待访录》；与黄俊杰、黄勇等已登记黄姓学者异人'),
    ('Jin Yuelin', '金岳霖', '中国', '1895–1984', 'Q329906',
     '中国现代逻辑学与知识论奠基者'),
    ('Richard Joyce', '理查德·乔伊斯', '新西兰', '1966–', 'Q2149904',
     '道德虚构主义（道德错误论）；与已登记 James Joyce（小说家）异人'),
    ('James Woodward', '詹姆斯·伍德沃德', '美国', '1946–', 'Q30329545',
     '因果的干预主义理论；经英文维基“James Woodward (philosopher)”反查得 QID'),
    ('Tim Maudlin', '蒂姆·莫德林', '美国', '1958–', 'Q75377',
     '物理学哲学（时空、量子力学）'),
    ('Robert Kane', '罗伯特·凯恩', '美国', '1938–2024', 'Q913046',
     '自由意志论（事件因果的自由意志论）'),
    ('Charles Larmore', '查尔斯·拉莫尔', '美国', '1950–', 'Q2959578',
     '政治自由主义与道德哲学'),
    ('Ernest Renan', '埃内斯特·勒南', '法国', '1823–1892', 'Q157155',
     '民族主义理论（《民族是什么》）'),
    ('Charlotte Perkins Gilman', '夏洛特·珀金斯·吉尔曼', '美国', '1860–1935',
     'Q287752', '女性主义作家与社会理论'),
    ('Reinhold Niebuhr', '莱因霍尔德·尼布尔', '美国', '1892–1971', 'Q358561',
     '基督教现实主义神学家；与其弟 H. Richard Niebuhr 异人'),
    ('Alison Jaggar', '艾莉森·贾格尔', '美国', '1942–', 'Q16730135',
     '女性主义哲学（女性主义伦理学与社会正义）'),
    ('Solomon Feferman', '所罗门·费弗曼', '美国', '1928–2016', 'Q957416',
     '数理逻辑（证明论、 predicative analysis）'),
    ('Ueda Shizuteru', '上田闲照', '日本', '1926–2019', 'Q430420',
     '京都学派哲学家，西谷启治弟子'),
    # H. H. Price 与 John Herschel 已在册（Price, Henry Habberley / Herschel, John F. W.），
    # 本批只补别名，不重复落册（见 alias_patch_b9.py）。
    ('Aníbal Quijano', '阿尼瓦尔·基哈诺', '秘鲁', '1930–2018', 'Q1432523',
     '殖民性（coloniality）理论；出生年另有 1928 说，从 Wikidata 1930'),
    ('Frances Kamm', '弗朗西丝·卡姆', '美国', '—', 'Q5478769',
     '规范伦理学（电车难题、不可侵犯性）；Wikidata 无生年'),
    ('David O. Brink', 'David O. Brink' + EN, '美国', '1958–', 'Q21903486',
     '元伦理学（道德实在论与自然主义）'),
    ('Marilyn Friedman', 'Marilyn Friedman' + EN, '美国', '1945–', 'Q14816066',
     '关怀伦理与女性主义政治哲学'),
    ('Susanna Siegel', 'Susanna Siegel' + EN, '美国', '1970–', 'Q16885971',
     '知觉哲学'),
    ('Amie Thomasson', 'Amie Thomasson' + EN, '美国', '1968–', 'Q15429029',
     '本体论与形而上学（易进路、虚构对象）'),
    ('Rae Langton', 'Rae Langton' + EN, '澳大利亚／英国', '1961–', 'Q15990111',
     '语言哲学与女性主义哲学（言语行为与色情）'),
    ('Neil Levy', 'Neil Levy' + EN, '—', '1967–', 'Q42722093',
     '神经伦理学与自由意志；Wikidata 未记国籍'),
    ('Kent Bach', 'Kent Bach' + EN, '美国', '1943–', 'Q6391616',
     '语言哲学与心智哲学（隐含交流）'),
    ('David Copp', 'David Copp' + EN, '加拿大', '1948–', 'Q93247149',
     '元伦理学（社会中心道德理论）'),
    ('Michael Huemer', 'Michael Huemer' + EN, '美国', '1969–', 'Q1927910',
     '认识论与政治哲学（现象保守主义、直觉主义）'),
    ('Anna Stilz', 'Anna Stilz' + EN, '—', '1976–', 'Q112555472',
     '政治哲学（领土权与政治义务）'),
    ('Leslie Green', 'Leslie Green' + EN, '英国（苏格兰）／加拿大', '1956–',
     'Q129722',
     '法哲学（法律实证主义）；Wikidata Q129722 生年记 1918 有误，从英文维基百科 1956'),
    ('Naomi Zack', 'Naomi Zack' + EN, '美国', '1944–', 'Q16199936',
     '种族哲学与女性主义哲学'),
    ('Jennifer Saul', 'Jennifer Saul' + EN, '英国', '1968–', 'Q17011286',
     '语言哲学与女性主义哲学（含隐含义与欺骗）'),
    ('Louise Antony', 'Louise Antony' + EN, '美国', '1950–', 'Q16731647',
     '心智哲学与女性主义哲学'),
    ('Berys Gaut', 'Berys Gaut' + EN, '英国', '1958–', 'Q55104651',
     '美学与伦理学（艺术与道德）；本名 Berys Nigel Gaut'),
    ('William Galston', 'William Galston' + EN, '美国', '1946–', 'Q8009645',
     '政治哲学（自由主义与至善论）'),
    ('Mathias Risse', 'Mathias Risse' + EN, '—', '1970–', 'Q112487296',
     '政治哲学（世界主义、全球正义）'),
    ('Eva Kittay', 'Eva Kittay' + EN, '瑞典／美国', '1946–', 'Q16730899',
     '关怀伦理与残障哲学'),
    ('Susan Bordo', 'Susan Bordo' + EN, '美国', '1947–', 'Q7647596',
     '女性主义哲学（身体与饮食失调）'),
    ('Michael Ayers', 'Michael Ayers' + EN, '英国', '1935–', 'Q15452144',
     '早期近代哲学（洛克研究）'),
    ('Robert Sugden', 'Robert Sugden' + EN, '英国', '1949–', 'Q7350145',
     '经济学哲学（机会均等、自发秩序）'),
]

rows = []
ev = ['en\tqid\tzh\taff\tdates']
for key, zh, aff, dates, qid, note in PEOPLE:
    rows.append({'en': key, 'zh': zh, 'table': 'person', 'affiliation': aff,
                 'dates': dates,
                 'basis': '学界通行音译；籍属/生卒联网查证：Wikidata %s'
                          '（2026-11-24 查，凭证 %s）；%s' % (qid, EV, note),
                 'date': '2026-11-24'})
    ev.append('%s\t%s\t%s\t%s\t%s' % (key, qid, zh, aff, dates))
out = os.path.join(RES, 'rowspec-batch35-people.json')
json.dump({'batch': '058-batch35-people', 'date': '2026-11-24',
           'scope': '人名第九批（55 人，Wikidata 逐人取证）', 'rows': rows},
          io.open(out, 'w', encoding='utf-8', newline='\n'),
          ensure_ascii=False, indent=1)
io.open(os.path.join(RES, EV), 'w', encoding='utf-8',
        newline='\n').write('\n'.join(ev) + '\n')
print('rows=%d -> %s' % (len(rows), out))

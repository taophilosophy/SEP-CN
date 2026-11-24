# -*- coding: utf-8 -*-
"""vives 词条登记批（2026-11-25）：人物 19 行、著作 30 行、术语 25 行，
另修 Vives 生卒、haecceity 并 ecceitas、SUMMARY/mu-lu-s 主形对齐。幂等。"""
import io
import re
import sys
import unicodedata

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key  # noqa: E402

DATE = '2026-11-25'


def _skey(s):
    s = unicodedata.normalize('NFKD', s)
    return ''.join(ch for ch in s if not unicodedata.combining(ch)).lower()


def insert_sorted(lines, sec_title, row_key, row, keycol=0):
    """在 ## sec 标题下按 keycol 排序位置插入 row 行。"""
    ini = lines.index('## ' + sec_title)
    nxt = len(lines)
    for j in range(ini + 1, len(lines)):
        if lines[j].startswith('## '):
            nxt = j
            break
    pos = nxt
    for j in range(ini + 1, nxt):
        if not lines[j].startswith('| ') or lines[j].startswith('| 键') or lines[j].startswith('| 原文'):
            continue
        c = lines[j].split('|')
        if len(c) < 2:
            continue
        if _skey(c[1].strip()) > _skey(row_key):
            pos = j
            break
    lines.insert(pos, row)
    return lines


def exists(lines, key, keycol=0):
    k = norm_key(key)
    for l in lines:
        if not l.startswith('| '):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 2:
            continue
        for part in re.split(r'[;、]', c[keycol]):
            part = part.strip()
            if part and part != '—' and norm_key(part) == k:
                return True
        if norm_key(c[keycol]) == k:
            return True
    return False


def add_term(lines, key, orig, zh, first, basis):
    if exists(lines, key):
        print('跳过（已登记）', key)
        return
    row = '| %s | %s | %s | %s | %s | %s |' % (key, orig, zh, first, basis, DATE)
    sec = key[0].upper()
    if not sec.isalpha():
        sec = '#'
    insert_sorted(lines, sec, key, row, keycol=0)
    print('登记', sec, key)


def add_person(lines, orig, alias, zh, region, life, first, basis):
    if exists(lines, orig):
        print('跳过（已登记）', orig)
        return
    row = '| %s | %s | %s | %s | %s | %s | %s | %s |' % (orig, alias, zh, region, life, first, basis, DATE)
    sec = orig[0].upper()
    insert_sorted(lines, sec, orig, row, keycol=0)
    print('登记', sec, orig)


# ---------------- shu-yu-biao ----------------
TERMS = [
    ("maker's knowledge (tradition)", '—', '制作者知识（亦作“制造者知识”）', 'vives',
     '学界语境义译（Pérez-Ramos 论培根所本传统；knowing as making，verum factum）；中文两译并存，本库统一取“制作者知识”；exa 检索凭证 2026-11-25'),
    ('sermo communis', 'sermo communis', '日常言谈', 'vives', '拉丁术语义译（ordinary discourse），与形而上学抽象语言对举'),
    ('anticipationes', 'anticipationes', '前概念', 'vives', '希腊化认识论 prolepsis（西塞罗拉丁作 anticipationes）学界通行译法'),
    ('naturales informationes', 'naturales informationes', '自然概念', 'vives', '义译（natural notions），与 anticipationes 并列'),
    ('opera divina', 'opera divina', '神圣之作', 'vives', '义译；人不可穷究自然内里的论证语'),
    ('mancipium animi', 'mancipium animi', '灵魂的奴仆', 'vives', '拉丁语随文括注义译'),
    ('agens praecipuum', 'agens praecipuum', '首要动原', 'vives', '义译（principal agent），De anima et vita 灵魂定义语'),
    ('affectus sive affectiones', 'affectus sive affectiones', '情感', 'vives', '拉丁并列式义译；De anima et vita 核心术语'),
    ('Peripatetic', 'Peripatetic', '逍遥学派', 'vives', '学界通行（亚里士多德学派）'),
    ('Christian humanism', '—', '基督教人文主义', 'vives', '学界通行'),
    ('Collegium Trilingue', 'Collegium Trilingue', '三语学院', 'vives', '通行译名（卢万三语学院，伊拉斯谟式人文主义建制）'),
    ('cogitative soul', '—', '思维灵魂', 'vives', '官能心理学语境义译（anima cogitativa）'),
    ('vegetative soul', '—', '植物灵魂', 'vives', '亚里士多德灵魂论通行译法'),
    ('sensitive soul', '—', '感觉灵魂', 'vives', '亚里士多德灵魂论通行译法'),
    ('estimative power', '—', '估计力', 'vives', '阿维森纳 vis aestimativa 通行译法'),
    ('topics (loci)', 'loci', '论题术', 'vives', '人文主义辩证法通行（topica/loci）；与亚里士多德《论题篇》分条'),
    ('humors', '—', '体液', 'vives', '盖伦医学通行'),
    ('temperament', '—', '体质', 'vives', '盖伦语境通行（temperamentum）'),
    ('commonweal', '—', '公共福祉', 'vives', '义译（common weal）'),
    ('signification', '—', '意谓', 'vives', '中世纪语义学通行（与 suppositio＝指代 对举）'),
    ('grammar', '—', '语法', 'vives', '通行'),
    ('dialectician', 'dialectician', '辩证论者', 'vives', '经院语境（dialectici）；学科义 dialectic＝辩证法另有行'),
    ('aphorism', '—', '箴言', 'vives', '通行'),
    ('Estudio General', 'Estudio General', '普通学馆', 'vives', '西班牙旧制高等教育机构义译，随文括注原文'),
    ('Corpus Christi College', '—', '基督圣体学院', 'vives', '牛津学院通行译名'),
    ('vernacular', '—', '俗语（白话）', 'vives', '文艺复兴语境通行'),
    ('sublunary world', '—', '月下世界', 'vives', '亚里士多德宇宙论通行'),
]

BOOKS = [
    ('De disciplinis / On the Disciplines', '—', '《论学科》', 'vives',
     '本库统一形（拉丁义译；SEP 英文对题 On the Disciplines）；中文文献另见“论训练”“论纪律”（omnesmag 2023，exa 凭证 2026-11-25）'),
    ('De anima et vita / On the Soul and Life', '—', '《论灵魂与生命》', 'vives',
     '通行；台湾教育大辞书作“论心灵”（exa 凭证 2026-11-25），本库统一取《论灵魂与生命》（Routledge 对题 On the Soul and Life）'),
    ('In pseudodialecticos / Against the Pseudo-Dialecticians', '—', '《驳伪辩证论者》', 'vives',
     '本库统一形（义译；Guerlac／Fantazzi 英译）；拉丁变体 Adversus pseudodialecticos 同条'),
    ('De institutione feminae Christianae / The Education of a Christian Woman', '—', '《论基督徒妇女的教育》', 'vives',
     '本库统一形（Fantazzi 英译 The Education of a Christian Woman）'),
    ('Introductio ad sapientiam / Introduction to Wisdom', '—', '《智慧导论》', 'vives',
     '本库统一形（SEP 英文对题）；变体 Ad sapientiam introductio 同条'),
    ('De subventione pauperum / On Assistance to the Poor', '—', '《论济贫》', 'vives',
     '本库统一形（Tobriner 英译 On Assistance to the Poor）'),
    ('De concordia et discordia in humano genere / On Concord and Discord in Humankind', '—', '《论人类的和睦与不和》', 'vives',
     '本库统一形（SEP 英文对题）'),
    ('De veritate fidei Christianae / On the Truth of the Christian Faith', '—', '《论基督教信仰的真理》', 'vives',
     '本库统一形（SEP 英文对题）'),
    ('De causis corruptarum artium / On the Causes of the Corruption of the Arts', '—', '《论学艺败坏之因》', 'vives',
     '本库统一形（SEP 英文对题）；德译本题 Über die Gründe des Verfalls der Künste'),
    ('De tradendis disciplinis / On Handing Down the Disciplines', '—', '《论学科传授》', 'vives',
     '本库统一形（SEP 英文对题）'),
    ('De artibus / On the Arts', '—', '《论诸艺》', 'vives', '本库统一形（SEP 英文对题）'),
    ('De prima philosophia / On First Philosophy', '—', '《论第一哲学》', 'vives', '本库统一形（SEP 英文对题）'),
    ('De censura veri / On the Assessment of Truth', '—', '《论真理的判定》', 'vives', '本库统一形（SEP 英文对题）'),
    ('De explanatione cuiusque essentiae / On the Explanation of Each Essence', '—', '《论每一本质的解释》', 'vives',
     '本库统一形（SEP 英文对题）'),
    ('De instrumento probabilitatis / On the Instrument of Probability', '—', '《论盖然性工具》', 'vives',
     '本库统一形（SEP 英文对题）'),
    ('De disputatione / On Disputation', '—', '《论论辩》', 'vives', '本库统一形（随既有 disputation＝论辩）'),
    ('Censura de Aristotelis operibus / Assessment of Aristotle\u2019s Works', '—', '《亚里士多德著作评鉴》', 'vives',
     '本库统一形（SEP 英文对题）'),
    ('Dialectices libri quatuor / Four Books of Dialectic', '—', '《辩证法四书》', 'vives', '本库统一形（SEP 英文对题）'),
    ('Fabula de homine / A Fable about Man', '—', '《人的寓言》', 'vives', '本库统一形（Lenkeith 英译 A Fable about Man）'),
    ('De initiis, sectis et laudibus philosophiae / On the Origins, Schools and Merits of Philosophy', '—',
     '《论哲学的起源、学派与功绩》', 'vives', '本库统一形（SEP 英文对题）'),
    ('Satellitium animi / The Soul\u2019s Escort', '—', '《灵魂护卫队》', 'vives',
     '本库统一形（SEP 英文对题 The Soul\u2019s Escort）；Tello 2023 版题 Satellitium siue symbola, or the Squadron of symbolic maxims'),
    ('Opera omnia', 'Opera omnia', '《全集》', 'vives',
     '拉丁集合题义译；Mayans y Siscár 编（Valencia 1782–90；伦敦 1964 重印本为本文引据版）'),
    ('De veris principiis et vera ratione philosophandi contra pseudophilosophos / On the True Principles and True Method of Philosophizing against the Pseudo-Philosophers', '—',
     '《论真原理与真正的哲学方法——驳伪哲学家》', 'vives', '本库统一形（SEP 英文对题；Nizolio 1553）；正文随文简称《论真原理》'),
    ('Quod nihil scitur / That Nothing is Known', '—', '《论一无所知》', 'vives',
     '本库统一形（Sanches 1581；SEP 英文对题 That Nothing is Known）'),
    ('Exercitationes paradoxicae adversus Aristoteleos / Paradoxical Exercises against the Aristotelians', '—',
     '《驳亚里士多德派的悖论练习》', 'vives', '本库统一形（Gassendi 1624；SEP 英文对题）'),
    ('Commentarius de anima / Commentary on the Soul', '—', '《灵魂评注》', 'vives',
     '本库统一形（Melanchthon 1540；SEP 英文对题）'),
    ('El examen de ingenios para las ciencias / The Examination of Men\u2019s Wits', '—', '《检验诸学的才能》', 'vives',
     '中译著作沿用形（《堂吉诃德的世纪》2022 中译本，exa 凭证 2026-11-25）；Carew 英译 The Examination of Men\u2019s Wits'),
    ('The Anatomy of Melancholy', '—', '《忧郁的解剖》', 'vives', '学界通行（Burton 1621）'),
    ('De natura deorum / On the Nature of the Gods', '—', '《论神性》', 'vives', '学界通行（西塞罗）'),
    ('De legibus / On the Laws', '—', '《论法律》', 'vives', '学界通行（西塞罗）'),
]

PERSONS = [
    ('Agricola, Rudolph', 'Rudolph Agricola', '鲁道夫·阿格里科拉', '尼德兰（弗里西亚）', '1443–1485', 'vives',
     '学界通行音译（人文主义者、《论题术发明》作者）；生卒据 SEP 原文括注（1443–85）'),
    ('Sanches, Francisco', 'Francisco Sanches', '弗朗西斯科·桑切斯', '葡萄牙', '1551–1623', 'vives',
     '学界通行音译（怀疑论者、医生，《论一无所知》作者）；生卒据 SEP 原文括注'),
    ('Huarte de San Juan, Juan', 'Juan Huarte de San Juan', '胡安·瓦尔特·德·圣胡安', '西班牙（纳瓦拉）', '约1529–1588', 'vives',
     '中译著作沿用形（《堂吉诃德的世纪》2022 中译本，exa 凭证 2026-11-25）；生卒 1529?–1588'),
    ('Burton, Robert', 'Robert Burton', '罗伯特·伯顿', '英国', '1577–1640', 'vives',
     '学界通行汉译（《忧郁的解剖》作者）；生卒通行'),
    ('Nizolio, Mario', 'Mario Nizolio', '马里奥·尼佐利奥', '意大利', '1488–1567', 'vives',
     '学界通行音译（文艺复兴亚里士多德批评者）；生卒据 SEP 原文括注'),
    ('Francis I', '—', '法兰西一世', '法国', '1494–1547', 'vives', '学界通行（法国国王）；生卒通行'),
    ('Henry VIII', '—', '亨利八世', '英国', '1491–1547', 'vives', '学界通行（英格兰国王）；生卒通行'),
    ('Catherine of Aragon', '—', '阿拉贡的凯瑟琳', '西班牙／英国', '1485–1536', 'vives',
     '学界通行（亨利八世王后）；生卒通行'),
    ('Lax, Gaspar', 'Gaspar Lax', '加斯帕尔·拉克斯', '西班牙（阿拉贡）', '1487–1560', 'vives',
     '学界通行音译（巴黎蒙塔吉学院逻辑教师）；生卒据 SEP 原文括注'),
    ('Dullaert, Jan', 'Jan Dullaert', '扬·杜拉尔特', '佛兰德', '–1513', 'vives',
     '学界通行音译（巴黎博韦学院教师）；生年无考，卒年据 SEP 原文括注'),
    ('Bérault, Nicolas', 'Nicolas Bérault', '尼古拉·贝罗', '法国', '约1470–约1545', 'vives',
     '学界通行音译（巴黎人文主义者）；生卒据 SEP 原文括注（c.1470–c.1545）'),
    ('Dolz, Juan', 'Juan Dolz', '胡安·多尔兹', '西班牙（瓦伦西亚）', '—', 'vives', '学界通行音译；生卒无考'),
    ('Croy, William de', 'William of Croy', '威廉·德·克罗伊', '佛兰德', '–1521', 'vives',
     '学界通行音译（佛兰德贵族，比韦斯任其师）；卒年据 SEP 原文（1521 早逝），生年无确'),
    ('March, Blanquina', 'Blanquina March', '布兰基娜·马尔奇', '西班牙（瓦伦西亚）', '1473–1508', 'vives',
     '学界通行音译（比韦斯之母）；生卒据 SEP 原文括注'),
    ('Vives Valeriola, Luis', 'Luis Vives Valeriola', '路易斯·比韦斯·瓦莱里奥拉', '西班牙（瓦伦西亚）', '1453–1524', 'vives',
     '学界通行音译（比韦斯之父）；生卒据 SEP 原文括注'),
    ('Valldaura, Margarita', 'Margarita Valldaura', '玛加丽塔·瓦利亚乌拉', '西班牙（瓦伦西亚）', '—', 'vives',
     '学界通行音译（比韦斯之妻，1524 年成婚）；生卒无考'),
    ('Mary I', '—', '玛丽一世', '英国', '1516–1558', 'vives', '学界通行（英格兰女王，比韦斯的学生）；生卒通行'),
    ('Casini, Lorenzo', 'Lorenzo Casini', '洛伦佐·卡西尼', '意大利', '—', 'vives', '音译（本篇作者）；生卒无考'),
    ('Mayans y Siscár, Gregorio', 'Mayans y Siscár', '格雷戈里奥·马扬斯·伊·西斯卡尔', '西班牙', '1699–1781', 'vives',
     '学界通行音译（《全集》编者）；生卒通行'),
]

tp = 'shu-yu-biao.md'
tl = io.open(tp, encoding='utf-8', newline='').read().split('\n')
for k, o, z, f, b in TERMS:
    add_term(tl, k, o, z, f, b)
for k, o, z, f, b in BOOKS:
    add_term(tl, k, o, z, f, b)

# Vives 生卒修正＋标题对齐注记
for i, l in enumerate(tl):
    if l.startswith('| Juan Luis Vives ') or l.startswith('| Vives, Juan Luis '):
        if '1492–1540' in l:
            l = l.replace('1492–1540', '1493–1540').replace(
                '生卒通行作 1493–1540', '生卒订正 1492→1493（SEP 原文明言“非 1492”，2026-11-25）')
            tl[i] = l
            print('修正 Vives 生卒')
rp = 'ren-ming-biao.md'
rl = io.open(rp, encoding='utf-8', newline='').read().split('\n')
for o, a, z, r, lf, f, b in PERSONS:
    add_person(rl, o, a, z, r, lf, f, b)

# haecceity 并 ecceitas
for i, l in enumerate(rl):
    if l.startswith('| haecceity'):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == 8 and 'ecceitas' not in c[0]:
            c[0] = c[0] + '；ecceitas（司各脱拉丁异形，vives 用 ecceitates）'
            c[6] = c[6].rstrip('；') + '；ecceitas 并条 2026-11-25（vives 正文出现 ecceitates）'
            rl[i] = '| ' + ' | '.join(c) + ' |'
            print('haecceity 并 ecceitas')

io.open(tp, 'w', encoding='utf-8', newline='\n').write('\n'.join(tl))
io.open(rp, 'w', encoding='utf-8', newline='\n').write('\n'.join(rl))

# SUMMARY／mu-lu-s 主形对齐（registry 主形 比韦斯）
for p in ('SUMMARY.md', 'mu-lu-s.md'):
    t = io.open(p, encoding='utf-8', newline='').read()
    n = t.count('维夫斯')
    if n:
        t = t.replace('胡安·路易斯·维夫斯', '胡安·路易斯·比韦斯')
        io.open(p, 'w', encoding='utf-8', newline='\n').write(t)
        print(p, '主形对齐 ×', n)
print('DONE')

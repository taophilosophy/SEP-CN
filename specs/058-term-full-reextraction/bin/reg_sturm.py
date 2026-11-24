# -*- coding: utf-8 -*-
"""johann-sturm 重译批登记（2026-11-25）：人物 24、术语 26、著作 8。幂等。
依据栏不写检索凭证（本轮检索通道不可用）；沿用 2026-11-10 前轮联网凭证与学界通行译名。"""
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
        if norm_key(c[keycol].split('（')[0]) == k or norm_key(c[keycol]) == k:
            return True
        for part in re.split(r'[;、/]', c[keycol]):
            if part.strip() and norm_key(part.strip()) == k:
                return True
    return False


def add_term(lines, key, orig, zh, first, basis):
    if exists(lines, key):
        print('跳过', key)
        return
    row = '| %s | %s | %s | %s | %s | %s |' % (key, orig, zh, first, basis, DATE)
    sec = key[0].upper() if key[0].isalpha() else '#'
    insert_sorted(lines, sec, key, row, keycol=0)
    print('登记', sec, key)


def add_person(lines, orig, alias, zh, region, life, first, basis):
    if exists(lines, orig):
        print('跳过', orig)
        return
    row = '| %s | %s | %s | %s | %s | %s | %s | %s |' % (orig, alias, zh, region, life, first, basis, DATE)
    insert_sorted(lines, orig[0].upper(), orig, row, keycol=0)
    print('登记', orig[0].upper(), orig)


TERMS = [
    ('passive form', '—', '被动形式（亦作“受动形式”）', 'johann-sturm',
     '施图尔姆研究语境义译（passive forms，与主动本原 active principle 对举）；本库统一形'),
    ('active principle', '—', '主动本原', 'johann-sturm', '学界通行（Leibniz《论自然本身》论战核心概念）'),
    ('local motion', '—', '局部运动', 'johann-sturm', '笛卡尔物理学通行译法（motus localis）'),
    ('mode of matter', '—', '物质样态', 'johann-sturm', '随既有 mode＝样态'),
    ('supralunary', '—', '月上世界', 'johann-sturm', '亚里士多德宇宙论通行（与月下世界对举）'),
    ('conservation of motion', '—', '运动守恒', 'johann-sturm', '物理学史通行（动量守恒前史语境）'),
    ('mind-body union', '—', '心身联合', 'johann-sturm', '笛卡尔主义通行（unio mentis et corporis）'),
    ('pre-Socratic', '—', '前苏格拉底', 'johann-sturm', '学界通行'),
    ('Cartesianism', '—', '笛卡尔主义', 'johann-sturm', '学界通行'),
    ('Gassendism', '—', '伽桑狄主义', 'johann-sturm', '随既有伽桑狄；学界通行'),
    ('alchemy', '—', '炼金术', 'johann-sturm', '学界通行'),
    ('Spagyric', 'Spagyric', '医药化学派', 'johann-sturm', '近代化学史通行（spagyrici＝医药化学家）'),
    ('Lutheran', '—', '路德宗', 'johann-sturm', '学界通行（亦作信义宗）'),
    ('Counter-Reformation', '—', '反宗教改革', 'johann-sturm', '学界通行'),
    ('Latin school', '—', '拉丁学校', 'johann-sturm', '近代早期欧洲教育史通行'),
    ('amanuensis', '—', '文书（抄写助手）', 'johann-sturm', '义译'),
    ('telescope', '—', '望远镜', 'johann-sturm', '通行'),
    ('microscope', '—', '显微镜', 'johann-sturm', '通行'),
    ('air pump', '—', '抽气机', 'johann-sturm', '物理学史通行（真空泵）'),
    ('calendar', '—', '历书', 'johann-sturm', '历法史通行（近代早期历书 calender）'),
    ('hypothesis', '—', '假说', 'johann-sturm', '审定库通行；科学哲学语境'),
    ('experimental method', '—', '实验方法', 'johann-sturm', '通行'),
    ('Ockham’s razor', '—', '奥卡姆剃刀', 'johann-sturm', '学界通行'),
    ('potentia absoluta', 'potentia absoluta', '绝对能力', 'johann-sturm', '经院神学通行（potentia ordinata 相对）'),
    ('potentia respectiva & hypothetica', 'potentia respectiva & hypothetica', '相对能力与假设能力', 'johann-sturm',
     '施图尔姆术语义译（相对的与假设的能力）'),
    ('causa exigens', 'causa exigens', '要求因', 'johann-sturm', '施图尔姆术语义译（requiring cause）'),
    ('physica generalis', 'physica generalis', '普通物理学', 'johann-sturm', '近代早期物理学分类通行'),
    ('physica specialis', 'physica specialis', '特殊物理学', 'johann-sturm', '同上'),
    ('physica specialissima', 'physica specialissima', '最特殊物理学', 'johann-sturm', '同上（施图尔姆三分之末）'),
    ('collegium', 'collegia', '讲习班', 'johann-sturm', '近代大学史通行（专题课程建制）'),
    ('polyhistor', '—', '博通学者', 'johann-sturm', '近代学术史通行（百科全书式学者）'),
    ('sectarian (philosophy)', 'secta', '宗派（宗派哲学）', 'johann-sturm', '折衷主义文献通行（与折衷论者对举）'),
    ('eclectic (philosopher)', '—', '折衷论者', 'johann-sturm', '随既有 eclecticism＝折衷主义'),
]

BOOKS = [
    ('Physica Conciliatrix (Sturm)', '—', '《调停物理学》', 'johann-sturm', '本库统一形（PC，1684）'),
    ('Physica Electiva sive Hypothetica (Sturm)', '—', '《选择物理学或假设物理学》', 'johann-sturm',
     '本库统一形（PE，1697/1722；Wolff 1722 刊行第二部分）'),
    ('Compendium Physicae Modernae Sanioris (Sturm)', '—', '《较健全的近代物理学纲要》', 'johann-sturm',
     '本库统一形（CPMS，1704 身后刊行）'),
    ('De Ipsa Natura (Leibniz)', '—', '《论自然本身》', 'johann-sturm', '莱布尼茨研究通行（1698）'),
    ('Collegium experimentale sive curiosum (Sturm)', '—', '《实验讲习或奇物》', 'johann-sturm', '本库统一形（1676/1685）'),
    ('De Philosophia Sectaria & Electiva (Sturm)', '—', '《论宗派哲学与折衷哲学》', 'johann-sturm',
     '本库统一形（DSE，1679 论辩）'),
    ('Philosophia eclectica (Sturm)', '—', '《折衷哲学》', 'johann-sturm', '本库统一形（1686/1698 两卷）'),
    ('De vera philosophandi libertate (Bornius)', '—', '《论哲学思考的真自由》', 'johann-sturm',
     '本库统一形（博尔尼乌斯 1653 就职演讲）'),
]

PERSONS = [
    ('Sturm, Johann Eucharius', '—', '约翰·欧夏里乌斯·施图尔姆', '德国（希尔波尔特施泰因）', '—', 'johann-sturm',
     '学界通行音译（施图尔姆之父，裁缝与宫廷管事）；生年无考'),
    ('Bock, Gertraud', '—', '格特劳德·博克', '德国', '—', 'johann-sturm', '学界通行音译（施图尔姆之母）'),
    ('Bock, Konrad', '—', '康拉德·博克', '德国（利本施塔特）', '—', 'johann-sturm', '学界通行音译（乡村牧师）'),
    ('Beurer, Johann Jakob', '—', '约翰·雅各布·博伊雷尔', '德国', '—', 'johann-sturm', '学界通行音译（宫廷牧师）'),
    ('Hupfer, Johannes', '—', '约翰内斯·胡普费尔', '德国（魏森堡）', '—', 'johann-sturm', '学界通行音译（拉丁学校校长）'),
    ('Wülfer, Daniel', '—', '丹尼尔·维尔费尔', '德国（纽伦堡）', '—', 'johann-sturm', '学界通行音译（圣洛伦茨牧师）'),
    ('Spoercke, Henning', '—', '亨宁·施珀克', '德国', '—', 'johann-sturm', '学界通行音译（耶拿神学教师）'),
    ('Raey, Johannes De', 'Johannes De Raey', '约翰内斯·德·拉伊', '荷兰', '1622–1702', 'johann-sturm',
     '学界通行音译（莱顿哲学教师）；生卒据 SEP 原文括注'),
    ('Goldmann, Nicolai', '—', '尼科拉伊·戈尔德曼', '德国', '1611–1665', 'johann-sturm',
     '学界通行音译（莱顿私授建筑教师）；生卒据 SEP 原文括注'),
    ('Bornius, Henricus', '—', '亨里库斯·博尔尼乌斯', '荷兰', '1617–1665', 'johann-sturm',
     '学界通行音译（莱顿伦理学教授）；生卒据 SEP 原文括注'),
    ('Trew, Abdias', '—', '阿布迪亚斯·特鲁', '德国', '1597–1669', 'johann-sturm',
     '学界通行音译（阿尔特多夫数学与物理学教授）；生卒据 SEP 原文括注'),
    ('Scheuchzer, Johann Jakob', '—', '约翰·雅各布·舍伊赫策尔', '瑞士', '1672–1733', 'johann-sturm',
     '学界通行音译（瑞士博物学家）；生卒据 SEP 原文括注'),
    ('Doppelmayr, Johann Gabriel', '—', '约翰·加布里埃尔·多佩尔迈尔', '德国', '1671–1750', 'johann-sturm',
     '学界通行音译（数学家、百科编纂者）；生卒据 SEP 原文括注'),
    ('Müller, Johann Heinrich', '—', '约翰·海因里希·米勒', '德国', '1671–1731', 'johann-sturm',
     '学界通行音译（施图尔姆教席继承人；与既有 Johannes Müller 生理学家、Adam Müller 分立）；生卒据 SEP 原文括注'),
    ('Knorre, Martin', '—', '马丁·克诺雷', '德国', '1657–1699', 'johann-sturm', '学界通行音译；生卒据 SEP 原文括注'),
    ('Hamberger, Georg Albrecht', '—', '格奥尔格·阿尔布雷希特·哈姆贝格尔', '德国', '1662–1716', 'johann-sturm',
     '学界通行音译（沃尔夫之师）；生卒据 SEP 原文括注'),
    ('Kesler, Barbara Johanna', '—', '芭芭拉·约翰娜·凯斯勒', '德国', '–1679', 'johann-sturm',
     '学界通行音译（施图尔姆首任妻子）；卒年据 SEP 原文'),
    ('Höchstetter, Maria Salome', '—', '玛丽亚·萨洛梅·赫希施泰特', '德国', '–1691', 'johann-sturm',
     '学界通行音译（施图尔姆第二任妻子）；卒年据 SEP 原文'),
    ('Göring, Dorothea Elisabeth', '—', '多罗特娅·伊丽莎白·格林', '德国', '—', 'johann-sturm',
     '学界通行音译（施图尔姆第三任妻子）；生卒无考'),
    ('Sturm, Leonhard Christoph', '—', '莱昂哈德·克里斯托夫·施图尔姆', '德国', '1669–1719', 'johann-sturm',
     '学界通行（巴洛克建筑理论家，施图尔姆诸子中最知名者）；生卒学界通行'),
    ('Rötenbeck, Georg Paul', '—', '格奥尔格·保罗·勒滕贝克', '德国', '—', 'johann-sturm',
     '学界通行音译（阿尔特多夫政治学与逻辑教授，悼文作者）；生年无考'),
    ('Johann-Friedrich of Pfalz-Hilpoltstein', '—', '约翰·弗里德里希（普法尔茨-希尔波尔特施泰因伯爵）', '德国', '1587–1644',
     'johann-sturm', '学界通行（新教诸侯，1644 年卒）'),
    ('Wolfgang Wilhelm', '—', '沃尔夫冈·威廉', '德国（普法尔茨-诺伊堡）', '1578–1653', 'johann-sturm',
     '学界通行（1613 年改宗天主教）'),
]

tp = 'shu-yu-biao.md'
tl = io.open(tp, encoding='utf-8', newline='').read().split('\n')
for k, o, z, f, b in TERMS:
    add_term(tl, k, o, z, f, b)
for k, o, z, f, b in BOOKS:
    add_term(tl, k, o, z, f, b)
io.open(tp, 'w', encoding='utf-8', newline='\n').write('\n'.join(tl))

rp = 'ren-ming-biao.md'
rl = io.open(rp, encoding='utf-8', newline='').read().split('\n')
for o, a, z, r, lf, f, b in PERSONS:
    add_person(rl, o, a, z, r, lf, f, b)
io.open(rp, 'w', encoding='utf-8', newline='\n').write('\n'.join(rl))
print('DONE')

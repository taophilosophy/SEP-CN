# -*- coding: utf-8 -*-
"""词汇表并网执行器（ADR-0036）：qian-yan/ci-hui-biao.md 行分流两登记册。

用法:
  python specs/008-terminology-campaign/bin/bing_wang.py plan            # 产出决策账（只读）
  python specs/008-terminology-campaign/bin/bing_wang.py apply           # 写回两登记册（守恒门）
  python specs/008-terminology-campaign/bin/bing_wang.py apply --dry     # 只打印写盘预览

流程: 解析词汇表 412 未命中行 → 人名倒装/变体拆分/姓前缀匹配判重 → 分流
（术语/书名/地名/人名新增、泛指废弃、变体归并）→ 守恒门（412 = 写入 + 废弃）→ 写回。
决策账落 specs/008-terminology-campaign/results/bing-wang-2026-11-13.json。
冲突裁定（CONFLICT_EDITS）与变体归并（MERGE）随 apply 一并写盘。
"""
import io
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
GLO = os.path.join(ROOT, 'qian-yan', 'ci-hui-biao.md')
TERM = os.path.join(ROOT, 'shu-yu-biao.md')
PERSON = os.path.join(ROOT, 'ren-ming-biao.md')
LEDGER = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                      'bing-wang-2026-11-13.json')
UNMATCHED = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                         'bing-wang-unmatched.tsv')
DATE = '2026-11-13'
SRC = '词汇表并网（ADR-0036）'


def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    for ch in 'ʿʾʻʼ':
        s = s.replace(ch, '')
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return s.strip()


def load_unmatched():
    rows = {}
    for line in io.open(UNMATCHED, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line:
            continue
        ln, key, zh, note = line.split('\t', 3)
        rows[int(ln)] = {'line': int(ln), 'key': key, 'zh': zh, 'note': note}
    return rows


def registry_index(path):
    """fold(变体) -> (lineno, key_cell, trans)；多键行按「 / 」拆变体逐个入索引。"""
    idx = {}
    for lineno, line in enumerate(io.open(path, encoding='utf-8'), 1):
        line = line.rstrip('\n')
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if not cells or not cells[0] or set(cells[0]) <= set(':-: '):
            continue
        trans = cells[2] if len(cells) > 2 else ''
        for part in re.split(r'\s*/\s*', cells[0]):
            if part.strip():
                idx[fold(part)] = (lineno, cells[0], trans, line)
    return idx


def zh_core(s):
    """译法核心形：去括注/亦作/标点，取主形。"""
    s = re.split(r'（|\(|；|;|，|,', s)[0]
    s = re.sub(r'[·\-—–\s]', '', s)
    return s


def zh_agree(a, b):
    """译法一致性：核心形相等或互为子串（如“布拉德雷”与“F. H. 布拉德雷”）。"""
    x, y = zh_core(a), zh_core(b)
    return bool(x and y and (x == y or x in y or y in x))


PARTICLES = {'of', 'de', 'van', 'von', 'der', 'al', 'ibn', 'bin', 'du', 'le', 'la'}


def name_tokens(k):
    return {t for t in k.split() if t and t not in PARTICLES}


def person_match(pidx, k, zh):
    """人名判重（保守）：exact/倒装/of 倒装 → dup；
    姓匹配候选须同时满足 ①名字 token 全覆盖 ②译法一致，才判 dup，否则 new
    （交 check_terms 同键告警人工合并）。"""
    toks = k.split()
    cands = [k]
    if len(toks) >= 2:
        cands.append(' '.join(reversed(toks)))
        if len(toks) == 3 and toks[1] == 'of':
            cands.append('%s %s' % (toks[2], toks[0]))
    for c in cands:
        if c in pidx:
            return ('dup', c)
    mine = name_tokens(k)
    if len(toks) == 1:
        hits = [kk for kk in pidx if kk and k in name_tokens(kk)]
    else:
        hits = [kk for kk in pidx if kk and toks[-1] in name_tokens(kk)]
        if not hits:
            hits = [kk for kk in pidx if kk and toks[0] in name_tokens(kk)]
    if not hits:
        return None
    ok = []
    for kk in hits:
        other = name_tokens(kk)
        if len(mine) > 1 and not mine.issuperset(other - {toks[-1]}):
            continue
        if zh_agree(zh, pidx[kk][2]):
            ok.append(kk)
    if len(ok) == 1:
        return ('dup', ok[0])
    if len(ok) > 1:
        # 册内同姓多行且译法均可容纳（泛指姓行）：留账废弃，不新增
        return ('ambiguous', ok[:6])
    return None


def is_english(k):
    """ASCII 可打印即视为英文题名/术语（含标点）；非 ASCII 保留原形入原文列。"""
    return all(ord(c) < 128 for c in k)


# ---- 分流处置（按词汇表行号；未列出的行默认 action=term）----------------
BOOK = {602, 603, 619, 642, 646, 692, 728, 732, 769, 778, 832, 858, 863, 872,
        991, 1038, 1055, 1057, 1081, 1082, 1083, 1122, 1158, 1170, 1176, 1209,
        1223, 1266, 1287, 1305, 1329, 1374, 1389, 1391}
PLACE = {671, 1003, 1259}          # 奥弗涅 / 拉丁美洲 / 圣彼得堡（地名）
EPONYM = {844, 999, 1000, 1406}    # EPR / Kochen-Specker / KS 定理 / Zermelo-Fraenkel
DROP = {
    632: '泛指简称（Albert），具体所指见专条', 698: '泛指姓（Benjamin），见专条',
    773: '泛指姓（Cohen），见专条', 1053: '泛指姓（More），见专条',
    1194: '泛指名（Samuel），见专条', 1273: '泛指姓（Sturm），见专条',
    1397: '泛指姓（Williams），见专条', 1398: '泛指姓（Wilson），见专条',
    678: '泛指姓（Bacon），Francis/Roger 册行已分立', 644: 'SEP 旧文章题名，非现行对照对象',
    1302: '碎片键（Tetsurō），Watsuji Tetsurō 行覆盖', 1335: '泛词（triumph），词典义无对照价值',
    1325: '复数异形（Tokens），术语册 Token 行覆盖', 1350: '复数异形（Types），本批 type 行合并覆盖',
    1017: '勋爵衔形（Lord Monboddo），并入本批新增 Burnett, James 行',
    1135: '复数异形（possible worlds），本批 possible world 行合并覆盖',
    648: '泛指同名（Ammonius 泛指），Ammonius Hermiae 行分立后此行废弃',
}
# 变体归并：词汇表行号 → (目标行任一变体的 fold, 追加到键列的别形)
MERGE = {
    889: ('voltaire', 'François-Marie d’Arouet'),
    741: ('burley walter', 'Burleigh'),
    983: ('sturm johann christoph', 'Johann Sturm'),
    1173: ('al razi', 'Razi'),
    600: ('shaftesbury 3rd earl of', '3rd Earl of Shaftesbury'),
    1222: ('shaftesbury 3rd earl of', 'Lord Shaftesbury'),
    656: ('cooper anthony ashley 3rd earl of shaftesbury', 'Anthony Ashley Cooper'),
}
# 人名判重指派（自动匹配不到位、但登记册行明确存在者；译法冲突者标 conflict 供送审）
PERSON_DUP_OVERRIDE = {
    647: 'ammonius hermeiou',
    690: 'beauvoir simone de',       # 波伏瓦 vs 册行波伏娃：译法冲突送审
    1227: 'beauvoir simone de',
    1031: 'mctaggart j m e',         # 麦克塔格特 vs 册行麦克塔加特：译法冲突送审
    756: 'carl stumpf',              # Carl Friedrich Stumpf = Carl Stumpf
    1272: 'carl stumpf',
    1288: 'alfred tarski',           # Tarski 姓行 = Alfred Tarski 行
    1045: 'montague richard',        # Montague = Richard Montague（册行保留英文）
    982: 'sturm johann christoph',   # 与 MERGE[983] 同目标
    1224: 'william of sherwood',     # Sherwood = William of Sherwood
    1370: 'juan luis vives',         # 维夫斯 vs 册行比韦斯：译法冲突送审
    1108: 'strawson p f',            # Peter Frederick Strawson = Strawson, P.F.
    738: 'burali forti cesare',      # Burali-Forti = Cesare Burali-Forti
    873: 'fakhr al din al razi',     # Fakhr al-Din = Fakhr al-Dīn al-Rāzī（册内另有 al-Rāzī, Fakhr al-Dīn 重复行）
    1411: 'thabit ibn qurra',        # 塔比 vs 册行萨比特：译法冲突送审
}
# 译法冲突送审清单（人名册为决策源，词汇表注记主张改形者；交用户裁定后回写）
PERSON_CONFLICT_FLAG = {690, 1227, 1031, 1370, 1411}
# 人名行（script 匹配判 dup/new；1222 Lord Shaftesbury 亦属人名）
PERSON_SET = {683, 604, 607, 617, 625, 626, 629, 630, 631, 633, 638, 643, 654,
          661, 672, 673, 681, 684, 690, 699, 700, 701, 702, 703, 714, 716,
          718, 721, 722, 723, 725, 729, 730, 733, 734, 735, 738, 739, 740, 742,
          743, 746, 748, 749, 750, 754, 756, 758, 760, 763, 764, 810, 816, 827,
          834, 837, 842, 859, 873, 885, 886, 887, 888, 892, 897, 898, 900, 901,
          903, 905, 910, 912, 914, 916, 919, 920, 921, 922, 923, 928, 932, 934,
          935, 970, 974, 975, 976, 977, 978, 979, 981, 982, 985, 988, 998,
          1001, 1007, 1019, 1020, 1021, 1025, 1031, 1045, 1060, 1072,
          1074, 1103, 1107, 1108, 1112, 1114, 1179, 1192, 1195, 1197, 1200,
          1224, 1227, 1228, 1244, 1253, 1255, 1263, 1264, 1267, 1268,
          1272, 1284, 1283, 1286, 1288, 1289, 1294, 1315, 1322, 1326, 1343,
          1344, 1351, 1360, 1362, 1370, 1380, 1381, 1383, 1385, 1386, 1387,
          1388, 1394, 1396, 1399, 1401, 1404, 1405, 1411}
# 人名新增行的籍属/生卒（教科书级确定者；其余留 — 交 specs/013 回填）
PERSON_META = {
    630: ('英国', '1912–1954'), 721: ('丹麦', '1885–1962'), 897: ('德国', '1845–1918'),
    758: ('德国／美国', '1891–1970'), 1020: ('奥地利／英国', '1889–1951'),
    700: ('英国', '1748–1832'), 701: ('英国', '1859–1933'), 1288: ('波兰／美国', '1901–1983'),
    1388: ('英国', '1861–1947'), 1399: ('德国', '1842–1915'), 1381: ('日本', '1889–1960'),
    749: ('法国（阿尔及尔生）', '1913–1960'), 1197: ('法国', '1905–1980'),
    859: ('德国', '1885–1977'), 1228: ('法国', '1909–1943'), 920: ('英国', '1820–1903'),
    921: ('德国', '1842–1918'), 1060: ('德国', '1854–1924'), 760: ('德国／瑞典', '1874–1945'),
    723: ('英国', '1865–1916'), 816: ('德国', '1831–1916'), 1021: ('荷兰', '1881–1966'),
    886: ('爱尔兰', '1694–1746'), 900: ('苏格兰', '1719–1796'), 901: ('苏格兰', '1698–1748'),
    903: ('苏格兰', '1672–1729'), 837: ('苏格兰', '1753–1828'), 977: ('苏格兰', '1726–1797'),
    168: ('苏格兰', '1718–1800'), 975: ('苏格兰', '1714–1799'), 974: ('苏格兰', '1735–1803'),
    919: ('美国', '1916–2001'), 1179: ('德国／奥地利', '1758–1823'), 912: ('德国', '1852–1933'),
    1294: ('意大利', '1508–1588'), 892: ('德国', '1828–1875'), 898: ('爱尔兰', '1685–1753'),
    1284: ('法国', '1585–1628'), 885: ('英国', '1846–1924'), 1362: ('意大利', '1407–1457'),
    1370: ('西班牙／尼德兰', '1492–1540'),
}
# 特殊术语行定制（zh/orig/basis/key 覆写；value=None 表示该行并入他行或废弃）
TERM_OVERRIDES = {
    605: {'zh': '溯因', 'basis': '学界通行（与 abductive reasoning 溯因推理 同义异形，键形分立）'},
    612: {'zh': '学园怀疑主义', 'basis': '学界通行（Skepticism 两译并存：怀疑论／怀疑主义）'},
    613: {'zh': '顺应；调节', 'basis': '按语境取义：科学哲学“顺应”、视觉生理学“调节”、语用学“顺应”'},
    614: {'zh': '解释；说明；原理', 'basis': '按语境取义（give an account of 译“对……给出说明/解释”）'},
    835: {'zh': '学说史传统；学说汇编', 'basis': '学界通行（doxography；阿尔克迈翁条术语）'},
    848: None,
    849: {'zh': '经验的；实证的', 'basis': '两义并存（empiricism 才是“经验主义”）；《地理研究》2020 年专文（汤茂林、黄展）；凭证 2026-11-13 并网合并两行'},
    862: {'zh': '伦理学', 'basis': '作学科名与书名（斯宾诺莎《伦理学》）；《模糊性的道德》随已出版书名译“道德”'},
    867: {'zh': '经验；体验', 'basis': '经验主义与认识论语境译“经验”；现象学语境（lived experience）译“体验”'},
    720: {'zh': '玻姆', 'basis': '学界通行（形容词形：Bohmian mechanics 玻姆力学，德布罗意—玻姆理论）'},
    874: {'zh': '堕落', 'basis': '学界通行（the Fall，神学与奥古斯丁语境）'},
    908: {'zh': '大学问', 'basis': '王阳明《大学问》；儒家经典《大学》英译亦作 the Great Learning，按语境分辨'},
    949: {'zh': '个体', 'basis': '学界通行（斯特劳森《个体》（Individuals, 1959）书名语境）'},
    992: None,
    993: {'zh': '证成（认识论语境）；辩护（行动语境）', 'basis': '双义分工（并网合并两行）'},
    1134: {'zh': '可能世界', 'basis': '学界通行（复数 possible worlds 同）'},
    1246: {'zh': '种类词', 'basis': '哲学逻辑术语（计数与个体化、同一性标准）；中文文献亦多保留英文原词'},
    1348: {'zh': '类型', 'basis': '学界通行（type-token 类型—殊例之分；复数 Types 同）'},
    647: {'zh': '赫尔米亚的阿莫尼俄斯', 'key': 'Ammonius Hermiae',
          'basis': '学界通行（5 世纪亚历山大里亚亚里士多德注释家，赫尔米亚之子）'},
    1259: {'zh': '圣彼得堡（地名）', 'basis': '学界通行（与圣彼得堡悖论 St. Petersburg paradox 分立）'},
    671: {'zh': '奥弗涅', 'basis': '学界通行（法国地区；奥弗涅的威廉 William of Auvergne 语境）'},
    1003: {'zh': '拉丁美洲', 'basis': '学界通行（地域名）'},
    844: {'zh': '爱因斯坦-波多尔斯基-罗森', 'basis': '学界通行（EPR 论证，三人姓氏连用）'},
    999: {'zh': '科亨-施佩克尔', 'basis': '学界通行（Kochen–Specker 定理语境，双人名连用）'},
    1000: {'zh': 'KS 定理', 'basis': '学界通行（Kochen–Specker 定理缩写形）'},
    1406: {'zh': '策梅洛-弗兰克尔', 'basis': '学界通行（Zermelo–Fraenkel 集合论，双人名连用）'},
    1004: {'zh': '拉丁西方', 'basis': '中世纪语境通行译法；旧译“西方拉丁世界”废弃'},
    1170: {'zh': '《论文集》', 'orig': 'Rasâ’il', 'basis': '伊本·库拉书信集通行题名'},
    1054: {'zh': '最著名的一对', 'basis': '学界通行（binarium famosissimum 的英文别称）'},
    708: {'zh': '最著名的一对', 'orig': 'binarium famosissimum', 'basis': '拉丁术语，学界通行义译'},
    1266: {'zh': '局外人', 'basis': '加缪小说 L’Étranger 英译题名 The Stranger；上海译文等中译通行《局外人》'},
}
# 冲突仲裁（ADR-0036 决策 3：以术语在线审定为准；termonline 查无/异学科→登记册维持）
CONFLICT_EDITS = [
    {'key_fold': 'akrasia', 'new_trans': '意志薄弱（akrasia；亦作“不能自制”）',
     'basis_append': '；2026-11-13 补亦作（词汇表旧形“不能自制”并网，termonline-all 查无，希腊哲学通行维持）'},
    {'key_fold': 'paradox of suspense', 'new_trans': '悬念悖论（亦作“悬疑悖论”）',
     'basis_append': '；2026-11-13 补亦作（SUMMARY 题名形，termonline-all 查无）'},
    {'key_fold': 'square of opposition', 'new_trans': '对当方阵（亦作“逻辑方阵”）',
     'basis_append': '；2026-11-13 补亦作（逻辑文献通行异名，termonline-all 查无）'},
]
# 冲突衍生新行（同键多义分工，Cardinal 教会义；rationality 废弃词汇表行留账）
CONFLICT_ADD = [
    '| Cardinal（教会职衔） | Cardinal | 枢机主教 | 语料回收（词汇表并网） | 学界通行（天主教会职衔；与 cardinal 基数 同键多义分工；termonline-all 命中“基数词/基本方位”均异学科，凭证 2026-11-13） | 2026-11-13 |',
]


def plan():
    rows = load_unmatched()
    tidx = registry_index(TERM)
    pidx = registry_index(PERSON)
    ledger, dups = [], []
    for ln in sorted(rows):
        r = rows[ln]
        k = fold(r['key'])
        raw = TERM_OVERRIDES.get(ln)
        o = raw if isinstance(raw, dict) else {}
        act = 'term'
        matched = None
        if raw is None and ln in TERM_OVERRIDES:
            act = 'drop'          # 显式 None：并入同键他行
        elif ln in DROP:
            act = 'drop'
        elif ln in MERGE:
            act = 'merge'
        elif ln in PERSON_DUP_OVERRIDE:
            act = 'person-dup'
            matched = PERSON_DUP_OVERRIDE[ln]
        elif ln in PERSON_SET:
            m = person_match(pidx, k, r['zh'])
            if m is None:
                act = 'person-new'
            elif m[0] == 'dup':
                act = 'person-dup'
                matched = m[1]
            else:
                act = 'drop'
                matched = '泛指姓（册内同姓多行：%s）' % '、'.join(m[1])
        elif ln in BOOK:
            act = 'book'
        if act in ('person-dup', 'drop'):
            dups.append((ln, act, matched))
        entry = {'line': ln, 'key': r['key'], 'zh': o.get('zh', r['zh']),
                 'note': r['note'], 'action': act}
        if o.get('key'):
            entry['final_key'] = o['key']
        if o.get('orig'):
            entry['orig'] = o['orig']
        if o.get('basis'):
            entry['basis'] = o['basis']
        if matched:
            entry['matched'] = matched
        if act == 'person-new' and ln in PERSON_META:
            entry['guojia'], entry['dates'] = PERSON_META[ln]
        if ln in PERSON_CONFLICT_FLAG:
            entry['conflict'] = '译法与册行不一致，待裁定'
        ledger.append(entry)
    assert len(ledger) == len(rows), '行数不守恒'
    # 同批「姓」行与「全名」行并存：留全名行，姓行废弃留账（避免同册重复）
    news = [e for e in ledger if e['action'] == 'person-new']
    for a in news:
        at = name_tokens(fold(a['key']))
        if len(at) != 1:
            continue
        for b in news:
            bt = name_tokens(fold(b['key']))
            if b is a or len(bt) < 2:
                continue
            if at <= bt and zh_agree(a['zh'], b['zh']):
                a['action'] = 'drop'
                a['matched'] = '泛指姓（同批全名行 %s）' % b['key']
                dups.append((a['line'], 'drop', a['matched']))
                break
    json.dump({'date': DATE, 'source': SRC, 'rows': ledger},
              io.open(LEDGER, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    stat = {}
    for e in ledger:
        stat[e['action']] = stat.get(e['action'], 0) + 1
    print('决策账 → %s' % LEDGER)
    print('分布:', json.dumps(stat, ensure_ascii=False))
    print('\n-- person-dup / ambiguous（登记册为准，废弃留痕；译法核对）--')
    for ln, act, m in dups:
        e = next(x for x in ledger if x['line'] == ln)
        print('  g%-5d %-10s %-22s → %s | 词汇表:%s' % (ln, act, e['key'], m, e['zh']))


def sec_letter(key):
    c = fold(key)[:1].upper()
    return c if re.match(r'[A-Z]', c) else '#'


def build_rows(data):
    term_rows, person_rows = [], []
    for e in data['rows']:
        act = e['action']
        if act in ('drop', 'person-dup', 'merge'):
            continue
        basis = e.get('basis') or (e['note'][:90] if e['note'] else
                                   '学界惯例（词汇表并网迁移，待 008 审定库复核）')
        basis = basis.rstrip('；;、')
        basis = basis + '；' + SRC
        key = e.get('final_key') or e['key']
        if act == 'person-new':
            gu = e.get('guojia', '—')
            dt = e.get('dates', '—')
            person_rows.append('| %s | — | %s | %s | %s | 语料回收（全目录） | %s | %s |'
                               % (key, e['zh'], gu, dt, basis, DATE))
        else:
            orig = e.get('orig') or ('—' if is_english(key) else key)
            term_rows.append('| %s | %s | %s | 语料回收（词汇表并网） | %s | %s |'
                             % (key, orig, e['zh'], basis, DATE))
    return term_rows, person_rows


def insert_section(lines, row):
    """行插到对应字母节数据行尾（azsort 随后归位排序）。"""
    sec = sec_letter(row.split('|')[1].strip())
    idx = next((i for i, l in enumerate(lines)
                if re.match(r'^## %s\s*$' % re.escape(sec), l)), None)
    if idx is None:
        lines.append(row)
        return
    j, last = idx + 1, idx
    while j < len(lines) and not re.match(r'^## ', lines[j]):
        if lines[j].startswith('|'):
            last = j
        j += 1
    lines.insert(last + 1, row)


def apply_conflicts(lines):
    """冲突行变更：新主译 + 依据追加 + 裁定日期更新（术语册）。"""
    n = 0
    for i, l in enumerate(lines):
        cells = [c.strip() for c in l.strip('|').split('|')]
        if len(cells) < 6:
            continue
        for ed in CONFLICT_EDITS:
            if fold(cells[0]) == ed['key_fold']:
                cells[2] = ed['new_trans']
                cells[4] = cells[4].rstrip('；;') + ed['basis_append']
                cells[5] = DATE
                lines[i] = '| %s |' % ' | '.join(cells)
                n += 1
    return n


def apply_merges(lines):
    """变体归并：目标行（任一变体 fold 命中）键列追加「 / 别形」。"""
    n = 0
    for i, l in enumerate(lines):
        if not l.startswith('|'):
            continue
        cells = [c.strip() for c in l.strip('|').split('|')]
        if not cells or not cells[0]:
            continue
        for ln, (target, form) in MERGE.items():
            variants = [fold(v) for v in re.split(r'\s*/\s*', cells[0])]
            if target in variants and fold(form) not in variants:
                cells[0] = cells[0] + ' / ' + form
                lines[i] = '| %s |' % ' | '.join(cells)
                n += 1
    return n


def apply(dry):
    data = json.load(io.open(LEDGER, encoding='utf-8'))
    term_rows, person_rows = build_rows(data)
    dropped = sum(1 for e in data['rows'] if e['action'] in ('drop', 'person-dup'))
    written = len(term_rows) + len(person_rows) + len(MERGE)
    total = len(data['rows'])
    print('守恒: %d = 写入 %d（术语/书名/地名 %d + 人名新增 %d + 归并 %d）+ 废弃 %d；另冲突衍生新行 %d'
          % (total, written, len(term_rows), len(person_rows), len(MERGE),
             dropped, len(CONFLICT_ADD)))
    if dry:
        print('\n-- 术语册新行预览（前 12）--')
        for r in term_rows[:12]:
            print(' ', r[:150])
        print('\n-- 人名册新行预览（全部）--')
        for r in person_rows:
            print(' ', r[:170])
        return
    assert written + dropped == total, '守恒残余 ≠ 0，拒绝写回'
    tl = io.open(TERM, encoding='utf-8', newline='').read().split('\n')
    pl = io.open(PERSON, encoding='utf-8', newline='').read().split('\n')
    nc = apply_conflicts(tl)
    nm_t = apply_merges(tl)
    nm_p = apply_merges(pl)
    for r in term_rows:
        insert_section(tl, r)
    for r in CONFLICT_ADD:
        insert_section(tl, r)
    for r in person_rows:
        insert_section(pl, r)
    with io.open(TERM, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(tl))
    with io.open(PERSON, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(pl))
    print('已写盘: 术语册 +%d 行（冲突变更 %d，归并 %d）| 人名册 +%d 行（归并 %d）'
          % (len(term_rows), nc, nm_t, len(person_rows), nm_p))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'plan'
    if cmd == 'plan':
        plan()
    elif cmd == 'apply':
        apply('--dry' in sys.argv)
    else:
        print(__doc__)

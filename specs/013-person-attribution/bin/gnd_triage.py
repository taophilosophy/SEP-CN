# -*- coding: utf-8 -*-
"""GND 候选池判定线（specs/013 两档收口，2026-11-26）。

输入：results/gnd-candidates-2026-11-26.tsv（gnd_batch_candidates.py 产物）
输出：results/gnd-triage-2026-11-26.tsv（键｜verdict｜理由｜候选明细）
      results/gnd-auto-ledger-2026-11-26.tsv（auto 档 → apply_person_meta 凭证格式）

判据（specs/013 两档收口方案；GND 会错例与赛马/政客撞名防线）：
  R1 无逗号键（原形／古典单名）且候选生年 > 1850 → 不自动采（review）
  R2 候选含 floruit（fl.）且年份 ≥ 2020 → 不自动采（review）
  R3 三重判据全过 → auto：姓匹配＋名（或首字母）匹配＋职业为学界职业
     否则 → review
  ZERO/ERR → none
auto 档的籍属走德文→中文国家映射表（映射表外 → review，不硬译）。
"""
import io
import re
import sys
import unicodedata

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

SRC = 'specs/013-person-attribution/results/gnd-candidates-2026-11-26.tsv'
OUT = 'specs/013-person-attribution/results/gnd-triage-2026-11-26.tsv'
LEDGER = 'specs/013-person-attribution/results/gnd-auto-ledger-2026-11-26.tsv'
SHORT = 'specs/013-person-attribution/results/gnd-review-short-2026-11-26.tsv'

DE2ZH = {
    'Deutschland': '德国', 'Frankreich': '法国', 'USA': '美国', 'Großbritannien': '英国',
    'Österreich': '奥地利', 'Schweiz': '瑞士', 'Italien': '意大利', 'Spanien': '西班牙',
    'Niederlande': '荷兰', 'Belgien': '比利时', 'Polen': '波兰', 'Russland': '俄罗斯',
    'Russisches Reich': '俄罗斯帝国', 'Türkei': '土耳其', 'Griechenland': '希腊',
    'Iran': '伊朗', 'Irak': '伊拉克', 'Syrien': '叙利亚', 'Ägypten': '埃及',
    'Marokko': '摩洛哥', 'Tunesien': '突尼斯', 'Algerien': '阿尔及利亚', 'Japan': '日本',
    'China': '中国', 'Indien': '印度', 'Kanada': '加拿大', 'Australien': '澳大利亚',
    'Ungarn': '匈牙利', 'Tschechien': '捷克', 'Rumänien': '罗马尼亚', 'Dänemark': '丹麦',
    'Norwegen': '挪威', 'Schweden': '瑞典', 'Finnland': '芬兰', 'Irland': '爱尔兰',
    'Portugal': '葡萄牙', 'Israel': '以色列', 'Libanon': '黎巴嫩', 'Jemen': '也门',
    'Ukraine': '乌克兰', 'Litauen': '立陶宛', 'Lettland': '拉脱维亚', 'Estland': '爱沙尼亚',
    'Bulgarien': '保加利亚', 'Serbien': '塞尔维亚', 'Kroatien': '克罗地亚',
    'Slowakei': '斯洛伐克', 'Slowenien': '斯洛文尼亚', 'Island': '冰岛', 'Brasilien': '巴西',
    'Argentinien': '阿根廷', 'Mexiko': '墨西哥', 'Südafrika': '南非', 'Neuseeland': '新西兰',
    'Georgien': '格鲁吉亚', 'Armenien': '亚美尼亚', 'Aserbaidschan': '阿塞拜疆',
    'Kasachstan': '哈萨克斯坦', 'Usbekistan': '乌兹别克斯坦', 'Pakistan': '巴基斯坦',
    'Bangladesch': '孟加拉国', 'Sri Lanka': '斯里兰卡', 'Thailand': '泰国',
    'Vietnam': '越南', 'Indonesien': '印度尼西亚', 'Philippinen': '菲律宾',
    'Südkorea': '韩国', 'Nordkorea': '朝鲜', 'Taiwan': '中国台湾', 'Hongkong': '中国香港',
}
CITY2ZH = {
    'Königsberg': '普鲁士（今俄罗斯加里宁格勒）', 'Berlin': '德国', 'Wien': '奥地利',
    'Paris': '法国', 'London': '英国', 'Oxford': '英国', 'Cambridge': '英国',
    'Edinburgh': '英国', 'Dublin': '爱尔兰', 'Amsterdam': '荷兰', 'Leiden': '荷兰',
    'Utrecht': '荷兰', 'Leuven': '比利时', 'Löwen': '比利时', 'Gent': '比利时',
    'Zürich': '瑞士', 'Basel': '瑞士', 'Genf': '瑞士', 'Bern': '瑞士',
    'München': '德国', 'Leipzig': '德国', 'Jena': '德国', 'Halle': '德国',
    'Göttingen': '德国', 'Heidelberg': '德国', 'Freiburg': '德国', 'Tübingen': '德国',
    'Köln': '德国', 'Frankfurt': '德国', 'Hamburg': '德国', 'Stuttgart': '德国',
    'Bonn': '德国', 'Marburg': '德国', 'Erlangen': '德国', 'Würzburg': '德国',
    'Rostock': '德国', 'Greifswald': '德国', 'Breslau': '普鲁士（今波兰弗罗茨瓦夫）',
    'Danzig': '普鲁士（今波兰格但斯克）', 'Prag': '捷克', 'Praha': '捷克',
    'Brünn': '捷克', 'Krakau': '波兰', 'Warschau': '波兰', 'Lemberg': '波兰（今乌克兰利沃夫）',
    'Budapest': '匈牙利', 'Ofen': '匈牙利', 'Bukarest': '罗马尼亚', 'Sofia': '保加利亚',
    'Belgrad': '塞尔维亚', 'Zagreb': '克罗地亚', 'Laibach': '斯洛文尼亚',
    'Rom': '意大利', 'Mailand': '意大利', 'Neapel': '意大利', 'Florenz': '意大利',
    'Bologna': '意大利', 'Padua': '意大利', 'Pisa': '意大利', 'Turin': '意大利',
    'Madrid': '西班牙', 'Barcelona': '西班牙', 'Salamanca': '西班牙', 'Sevilla': '西班牙',
    'Lissabon': '葡萄牙', 'Coimbra': '葡萄牙', 'Athen': '希腊', 'Konstantinopel': '土耳其',
    'Istanbul': '土耳其', 'Kairo': '埃及', 'Alexandria': '埃及', 'Damaskus': '叙利亚',
    'Bagdad': '伊拉克', 'Teheran': '伊朗', 'Isfahan': '伊朗', 'Jerusalem': '以色列',
    'Moskau': '俄罗斯', 'Sankt Petersburg': '俄罗斯', 'Kiew': '乌克兰', 'Charkiw': '乌克兰',
    'Kopenhagen': '丹麦', 'Stockholm': '瑞典', 'Uppsala': '瑞典', 'Oslo': '挪威',
    'Helsinki': '芬兰', 'Åbo': '芬兰', 'Riga': '拉脱维亚', 'Reval': '爱沙尼亚',
    'Wilna': '立陶宛', 'New York': '美国', 'Boston': '美国', 'Chicago': '美国',
    'Princeton': '美国', 'Cambridge, Mass.': '美国', 'Berkeley': '美国',
    'Toronto': '加拿大', 'Montreal': '加拿大', 'Sydney': '澳大利亚', 'Melbourne': '澳大利亚',
    'Peking': '中国', 'Beijing': '中国', 'Shanghai': '中国', 'Nanking': '中国',
    'Tokyo': '日本', 'Kyoto': '日本', 'Seoul': '韩国', 'Delhi': '印度',
}

# 学界职业词（德文为主，含学术通称；命中即视为“学界职业”判据过）
SCHOLAR_RE = re.compile(
    r'Philosoph|philosoph|Professor|Dozent|Hochschullehrer|Wissenschaftler|Forscher|'
    r'Historiker|Theologe|Mathematiker|Physiker|Chemiker|Biologe|Mediziner|Arzt|Jurist|'
    r'Rechtswissenschaftler|Ökonom|Soziolog|Psycholog|Orientalist|Semitist|Altphilologe|'
    r'Klassische Philolog|Latinist|Hellenist|Islamwissenschaftler|Sinolog|Japanolog|'
    r'Iranist|Indolog|Buddhismuskund|Kulturwissenschaftler|Gelehrter|Gelehrte|'
    r'Schriftsteller|Autor|Publizist|Editor|Übersetzer|Bibliothekar|Archivar|'
    r'Astronom|Logiker|Ethiker|Epistemolog|Political scientist|Economist|Historian|'
    r'Philosopher|Theologian|Mathematician|Physicist|Scholar|Academic|Writer', re.I)


def fold(s):
    s = unicodedata.normalize('NFKD', str(s or '').casefold())
    return ''.join(ch for ch in s if not unicodedata.combining(ch))


def parse_year(v):
    m = re.search(r'(\d{4})', str(v or ''))
    return int(m.group(1)) if m else None


def name_tokens(key):
    """键拆姓/名：'Last, First' 或单名（古典）。返回 (姓, [名token], 无逗号)。"""
    k = str(key).strip()
    if ',' in k:
        last, first = k.split(',', 1)
        return fold(last.strip()), [t for t in re.split(r'[\s.\-]+', fold(first)) if t], False
    return fold(k), [], True


def parse_candidates(cand_text):
    """解析候选列（q=…; verdict=…; gndIdentifier=…; …，多候选以 || 分隔）。
    返回候选 dict 列表（verdict=HIT 且带 gndIdentifier 的）。"""
    out = []
    for part in (cand_text or '').split(' || '):
        part = part.strip()
        if not part:
            continue
        kv = {}
        for seg in part.split('; '):
            if '=' in seg:
                k, _, v = seg.partition('=')
                kv[k.strip()] = v.strip()
        if kv.get('verdict') == 'HIT' and kv.get('gndIdentifier'):
            out.append(kv)
    return out


def triage_one(key, cand_text):
    """返回 (verdict, 理由, 候选明细)。verdict ∈ auto/review/none。

    自动档要求（全过）：
      A. 姓名：姓匹配，且名 token 全命中（缩写形按首字母）
      B. 职业：professionOrOccupation 命中学界词；职业**缺省**时才允许以“全名精确匹配”
         补位（姓≥4 字母、名给出全称），职业非学界者一律不作候选（Ashton 判例：
         同名金融经纪人）。
      C. 生卒：至少一个年份可读（无年份者无法回填，降 review）
      D. 防线：R1 无逗号键且生年>1850 不采；R2 floruit≥2020 不采
      籍属：countryOfActivity → 国家表；否则 placeOfBirth → 城市表；仍无则留「—」（两档口径）。
    """
    cands = parse_candidates(cand_text)
    if not cands:
        return 'none', 'GND 无命中', ''
    if len(cands) > 1:
        # 同名多候选即歧义（Collins/Blake/Crupi 判例：GND 命中为同名的音乐家、
        # 作家、文学研究者），自动档一律不采，留 review 人工消歧
        return 'review', 'GND 同名候选 %d 条，需人工消歧' % len(cands), cand_text[:400]
    last, firsts, single = name_tokens(key)
    best = None
    for kv in cands:
        occ_s = kv.get('professionOrOccupation') or ''
        pref_f = fold(kv.get('preferredName'))
        if last not in pref_f:
            continue
        ok_first = bool(firsts)
        for f in firsts:
            f0 = f.rstrip('0123456789')
            if not f0:
                continue
            if f0 in pref_f:
                continue
            if len(f0) == 1 and f0 in pref_f:
                continue
            ok_first = False
        if not ok_first:
            continue
        scholar = bool(SCHOLAR_RE.search(occ_s))
        exact_full = (not single and len(firsts) >= 1 and len(last) >= 4
                      and all(len(f) >= 3 for f in firsts)
                      and all(f in pref_f for f in firsts))
        if not scholar:
            # 职业缺省或非学界：不进自动档（名单保留在 review 供人工判）
            continue
        by = parse_year(kv.get('dateOfBirth'))
        dy = parse_year(kv.get('dateOfDeath'))
        cand = {'gnd': kv['gndIdentifier'], 'pref': kv.get('preferredName'),
                'birth': kv.get('dateOfBirth'), 'death': kv.get('dateOfDeath'),
                'coa': kv.get('countryOfActivity'), 'pob': kv.get('placeOfBirth'),
                'occ': occ_s, 'has_year': bool(by or dy), 'scholar': scholar}
        # 优先有年份、有学界职业的候选
        score = (cand['has_year'], cand['scholar'], -len(occ_s))
        if best is None or score > best[0]:
            best = (score, cand)
    if best is None:
        return 'review', '有命中但无一过姓名＋职业判据', cand_text[:400]
    best = best[1]
    if not best['has_year']:
        return 'review', '姓名匹配但 GND 无生卒年份', cand_text[:400]
    by = parse_year(best['birth'])
    if single and by and by > 1850:
        return 'review', 'R1：无逗号键且候选生年 %d > 1850（GND 会错例防线）' % by, cand_text[:400]
    if by and by >= 1980:
        return 'review', 'R3：候选生年 %d ≥ 1980（SEP 作者群极少年份，疑同名）' % by, cand_text[:400]
    for dv in (best['birth'], best['death']):
        if dv and re.match(r'\s*[Ff]l', str(dv)):
            y = parse_year(dv)
            if y and y >= 2020:
                return 'review', 'R2：floruit ≥ 2020', cand_text[:400]
    country = ''
    for k, v in DE2ZH.items():
        if k.casefold() in fold(best['coa']):
            country = v
            break
    if not country:
        for k, v in CITY2ZH.items():
            if fold(k) and fold(k) in fold(best['pob']):
                country = v
                break
    if not country:
        country = '—'
    _by = re.sub(r'\s+', '', best['birth'] or '')
    _dy = re.sub(r'\s+', '', best['death'] or '')
    # 只写年（GND 常给 YYYY-MM-DD；登记册生卒列体例是年）
    _by = (_by[:4] if len(_by) >= 4 and _by[:4].isdigit() else _by)
    _dy = (_dy[:4] if len(_dy) >= 4 and _dy[:4].isdigit() else _dy)
    years = ('%s–%s' % (_by, _dy)) if (_by and _dy) else (_by or _dy)
    reason = '判据过（%s；%s%s）' % (
        best['occ'][:32] or '全名精确匹配', years,
        '；籍属待补' if country == '—' else '')
    detail = ('gnd=%s; name=%s; birth=%s; death=%s; coa=%s; pob=%s; occ=%s; country=%s'
              % (best['gnd'], best['pref'], best['birth'], best['death'],
                 best['coa'], best['pob'], best['occ'], country))
    return 'auto', reason, detail


def best_brief(key, cand_text):
    """供人工扫读的紧凑候选：先按姓名过滤（姓须出现），再优先「有年份且职业为学界」。"""
    cands = parse_candidates(cand_text)
    if not cands:
        return None
    last, _firsts, _single = name_tokens(key)
    cands = [kv for kv in cands if last in fold(kv.get('preferredName'))] or []
    if not cands:
        return None
    best = None
    for kv in cands:
        occ = kv.get('professionOrOccupation') or ''
        by = parse_year(kv.get('dateOfBirth'))
        dy = parse_year(kv.get('dateOfDeath'))
        score = (bool(by or dy), bool(SCHOLAR_RE.search(occ)))
        if best is None or score > best[0]:
            best = (score, kv)
    kv = best[1]
    b = (kv.get('dateOfBirth') or '')[:4]
    d = (kv.get('dateOfDeath') or '')[:4]
    years = ('%s–%s' % (b, d)) if (b and d) else (b or d)
    return (kv.get('preferredName') or '', years,
            kv.get('placeOfBirth') or '', (kv.get('professionOrOccupation') or '')[:40],
            kv.get('gndIdentifier') or '')


def main():
    rows, auto, review, none_cnt = [], [], [], 0
    brief_rows = []
    for line in io.open(SRC, encoding='utf-8'):
        c = line.rstrip('\n').split('\t')
        if len(c) < 4 or c[0] == '键':
            continue
        key, cand_text = c[0], c[3]
        v, reason, detail = triage_one(key, cand_text)
        if v == 'auto':
            auto.append((key, detail, reason))
        elif v == 'review':
            review.append(key)
        else:
            none_cnt += 1
        rows.append((key, v, reason, detail))
        b = best_brief(key, cand_text)
        brief_rows.append((key, v, b))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\tverdict\t理由\t候选\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    with io.open(LEDGER, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\t籍属\t生卒/鼎盛年\t联网查证权威源（GND lobid，2026-11-26 查）\t本地来源页（en/，行号）\t判定与备注\n')
        for key, detail, reason in auto:
            kv = dict(seg.split('=', 1) for seg in detail.split('; ') if '=' in seg)
            f.write('%s\t%s\t%s\tGND %s｜%s\t\t%s\n'
                    % (key, kv['coa'], kv['birth'] + '–' + kv['death'], kv['gnd'],
                       kv['name'], reason))
    with io.open(SHORT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\t状态\t候选名\t生卒\t出生地\t职业\tGND\n')
        for key, v, b in brief_rows:
            if b:
                f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % ((key, v) + b))
            else:
                f.write('%s\t%s\t—\t\t\t\t\n' % (key, v))
    print('分诊 %d 行：auto %d、review %d、none %d' % (len(rows), len(auto), len(review), none_cnt))
    print('→', SHORT)
    print('→', OUT)
    print('→', LEDGER)


if __name__ == '__main__':
    main()

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
    """返回 (verdict, 理由, 候选明细)。verdict ∈ auto/review/none。"""
    cands = parse_candidates(cand_text)
    if not cands:
        return 'none', 'GND 无命中', ''
    best = None
    for kv in cands:
        occ_s = kv.get('professionOrOccupation') or kv.get('type') or ''
        if not SCHOLAR_RE.search(occ_s):
            continue
        last, firsts, single = name_tokens(key)
        pref_f = fold(kv.get('preferredName'))
        if last not in pref_f:
            continue
        ok_first = True
        for f in firsts:
            f0 = f.rstrip('0123456789')
            if f0 and (f0 in pref_f or (len(f0) == 1 and (' ' + f0 in pref_f or f0 + ' ' in pref_f))):
                continue
            if len(f0) == 1 and pref_f.replace('-', ' ').count(f0):
                continue
            ok_first = False
        if not ok_first:
            continue
        cand = {'gnd': kv['gndIdentifier'], 'pref': kv.get('preferredName'),
                'birth': kv.get('dateOfBirth'), 'death': kv.get('dateOfDeath'),
                'coa': kv.get('countryOfActivity'), 'occ': occ_s}
        if best is None or (cand['birth'] and not best['birth']):
            best = cand
    if best is None:
        return 'review', '有命中但无一过三重判据', cand_text[:400]
    # 防线
    by = parse_year(best['birth'])
    if single and by and by > 1850:
        return 'review', 'R1：无逗号键且候选生年 %d > 1850（GND 会错例防线）' % by, cand_text[:400]
    for dv in (best['birth'], best['death']):
        y = parse_year(dv)
        if y and re.match(r'\s*[Ff]l', str(dv) or '') and y >= 2020:
            return 'review', 'R2：floruit ≥ 2020', cand_text[:400]
    country = ''
    for src in (best['coa'], best['birth'], best['death']):
        for k, v in DE2ZH.items():
            if k.casefold() in fold(src):
                country = v
                break
        if country:
            break
    if not country:
        return 'review', '国别 %r／%r／%r 无德→中映射，须人工' % (
            best['coa'], best['birth'], best['death']), cand_text[:400]
    years = ''
    if best['birth'] or best['death']:
        years = '%s–%s' % (re.sub(r'\s+', '', best['birth']) or '?',
                           re.sub(r'\s+', '', best['death']) or '?')
    reason = '三重判据过（%s；%s）' % (best['occ'][:40], years)
    detail = ('gnd=%s; name=%s; birth=%s; death=%s; coa=%s; occ=%s'
              % (best['gnd'], best['pref'], best['birth'], best['death'],
                 best['coa'], best['occ']))
    return 'auto', reason, detail


def main():
    rows, auto, review, none_cnt = [], [], [], 0
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
    print('分诊 %d 行：auto %d、review %d、none %d' % (len(rows), len(auto), len(review), none_cnt))
    print('→', OUT)
    print('→', LEDGER)


if __name__ == '__main__':
    main()

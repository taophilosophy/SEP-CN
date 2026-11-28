# -*- coding: utf-8 -*-
"""人名表存量缺口自动回填（Wikidata，身份可确证者才写）。

用法:
  python specs/058-term-full-reextraction/bin/backfill_auto.py --start 0 --limit 200 [--apply]

口径:
  * 只处理 person-missing.txt 中缺籍属/生卒的行（运行时重查登记册，已补者跳过）。
  * 检索词 = 姓, 名 反转；候选须 label 与人名匹配（大小写折叠包含）且描述含学术词，或为唯一命中。
  * 多个学术候选/无学术候选/生卒与国籍全缺 → 不写，留痕 excluded。
  * 籍属 = P27 国籍 QID → 中文映射（未知 QID 留空）；生卒 = P569/P570 年份（BCE 记前 N）。
"""
import argparse
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.register_lib import norm_key_quote, person_path  # noqa: E402

RES = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
MISSING = os.path.join(ROOT, 'specs', '013-person-attribution', 'results',
                       'person-missing.txt')
CTX = ssl.create_default_context()  # 默认证书/主机名校验（2026-11-28 安全审计）
OP = urllib.request.build_opener(
    urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7890',
                                 'https': 'http://127.0.0.1:7890'}),
    urllib.request.HTTPSHandler(context=CTX))

ACADEMIC = ('philosoph', 'logician', 'ethicist', 'mathematician', 'historian',
            'physicist', 'biologist', 'psychologist', 'linguist', 'economist',
            'sociologist', 'anthropologist', 'scientist', 'scholar',
            'professor', 'academic', 'researcher', 'theologian', 'orientalist',
            'archaeologist', 'classicist', 'political theorist', 'legal',
            'jurist', 'cognitive scientist', 'computer scientist', 'engineer',
            'physician', 'psychoanalyst', 'translator', 'writer', 'poet')
COUNTRY = {
    'Q30': '美国', 'Q145': '英国', 'Q142': '法国', 'Q183': '德国',
    'Q40': '奥地利', 'Q39': '瑞士', 'Q38': '意大利', 'Q27': '爱尔兰',
    'Q29': '西班牙', 'Q31': '比利时', 'Q55': '荷兰', 'Q20': '挪威',
    'Q34': '瑞典', 'Q33': '芬兰', 'Q35': '丹麦', 'Q43': '土耳其',
    'Q159': '俄罗斯', 'Q148': '中国', 'Q148?': '中国', 'Q16': '加拿大',
    'Q414': '阿根廷', 'Q155': '巴西', 'Q739': '哥伦比亚', 'Q664': '新西兰',
    'Q408': '澳大利亚', 'Q96': '墨西哥', 'Q17': '日本', 'Q884': '韩国',
    'Q668': '印度', 'Q794': '伊朗', 'Q801': '以色列', 'Q41': '希腊',
    'Q36': '波兰', 'Q213': '捷克', 'Q214': '斯洛伐克', 'Q28': '匈牙利',
    'Q218': '罗马尼亚', 'Q219': '保加利亚', 'Q403': '塞尔维亚',
    'Q224': '克罗地亚', 'Q215': '斯洛文尼亚', 'Q212': '乌克兰',
    'Q258': '南非', 'Q79': '埃及', 'Q1028': '摩洛哥', 'Q948': '突尼斯',
    'Q822': '黎巴嫩', 'Q858': '叙利亚', 'Q796': '伊拉克', 'Q843': '巴基斯坦',
    'Q252': '印度尼西亚', 'Q928': '菲律宾', 'Q881': '越南', 'Q334': '新加坡',
    'Q174193': '英国', 'Q179876': '英国', 'Q21': '英国', 'Q262': '英国',
    'Q26': '英国', 'Q23667': '英国', 'Q191': '爱沙尼亚', 'Q211': '拉脱维亚',
    'Q236': '格鲁吉亚', 'Q817': '约旦', 'Q733': '巴拉圭', 'Q735': '苏里南',
    'Q750': '玻利维亚', 'Q298': '智利', 'Q736': '厄瓜多尔', 'Q774': '乌拉圭',
    'Q241': '古巴', 'Q786': '多米尼加', 'Q783': '洪多斯',
    'Q784': '危地马拉', 'Q804': '巴拿马', 'Q805': '哥斯达黎加',
    'Q191': '爱沙尼亚',
}
DESC_NATION = [
    ('American', '美国'), ('British', '英国'), ('English', '英国'),
    ('Scottish', '英国'), ('Welsh', '英国'), ('Irish', '爱尔兰'),
    ('Canadian', '加拿大'), ('French', '法国'), ('German', '德国'),
    ('Austrian', '奥地利'), ('Swiss', '瑞士'), ('Italian', '意大利'),
    ('Spanish', '西班牙'), ('Dutch', '荷兰'), ('Belgian', '比利时'),
    ('Danish', '丹麦'), ('Norwegian', '挪威'), ('Swedish', '瑞典'),
    ('Finnish', '芬兰'), ('Polish', '波兰'), ('Russian', '俄罗斯'),
    ('Israeli', '以色列'), ('Indian', '印度'), ('Japanese', '日本'),
    ('Chinese', '中国'), ('Korean', '韩国'), ('Brazilian', '巴西'),
    ('Argentine', '阿根廷'), ('Argentinian', '阿根廷'),
    ('Mexican', '墨西哥'), ('Australian', '澳大利亚'),
    ('New Zealand', '新西兰'), ('Greek', '希腊'), ('Turkish', '土耳其'),
    ('Iranian', '伊朗'), ('Czech', '捷克'), ('Hungarian', '匈牙利'),
    ('Romanian', '罗马尼亚'), ('Bulgarian', '保加利亚'),
    ('Serbian', '塞尔维亚'), ('Croatian', '克罗地亚'),
    ('Ukrainian', '乌克兰'), ('South African', '南非'),
]


def get(url):
    for k in range(5):
        try:
            req = urllib.request.Request(
                url, headers={'User-Agent': 'SEP-CN-research/1.0'})
            with OP.open(req, timeout=12) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception:
            if k == 2:
                return None
            time.sleep(4 * (k + 1))


def search(name):
    d = get('https://www.wikidata.org/w/api.php?action=wbsearchentities'
            '&format=json&language=en&limit=10&search='
            + urllib.parse.quote(name))
    return (d or {}).get('search', [])


def claims(qid):
    d = get('https://www.wikidata.org/w/api.php?action=wbgetentities'
            '&format=json&props=claims|labels&languages=en&ids=' + qid)
    return ((d or {}).get('entities', {}).get(qid) or {}).get('claims', {})


def year(prop, cl):
    try:
        v = cl[prop][0]['mainsnak']['datavalue']['value']['time']
        y = int(v[1:].split('-')[0])
        if v[0] == '-':
            return '前%d' % y
        return str(y)
    except Exception:
        return ''


def year_or_fl(cl):
    b = year('P569', cl)
    d = year('P570', cl)
    # Wikidata 占位年（1900-01-01 常表未知）与生卒倒序一律不给日期
    if b in ('1900',) or d in ('1900',):
        return ''
    if b and d and int(b.lstrip('前')) >= int(d.lstrip('前')):
        return ''
    if b and d and b != d:
        return '%s–%s' % (b, d)
    if b and not d:
        return b + '–'
    if d and not b:
        return '–' + d
    return ''


def aff_from_desc(desc):
    out = []
    for word, zh in DESC_NATION:
        if re.search(r'\b' + word, desc) and zh not in out:
            out.append(zh)
    return '／'.join(out[:2])


def done_keys(ev_path):
    """证据 TSV 已记键：person-missing.txt 由 check_terms 重生成、行序随回填漂移，
    故去重只认键，不认 --start 偏移（2026-11-23 第四批踩坑后加）。"""
    out = set()
    if not os.path.exists(ev_path):
        return out
    with io.open(ev_path, encoding='utf-8') as f:
        for line in f:
            p = line.rstrip('\n').split('\t')
            if len(p) >= 7 and p[0] and p[0] != 'en':
                out.add(p[0])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--start', type=int, default=0)
    ap.add_argument('--limit', type=int, default=200)
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    ev_path = os.path.join(RES, 'backfill-auto-2026-11-23.tsv')
    seen = done_keys(ev_path)
    # 检索撞名/身份存疑：本批人工排除（详见 execution-log）
    EXCLUDE = {'Charles Mills', 'Audrey', 'Batterman, Robert',
               'Brock, Gillian', 'Epiphanius', 'della Valle, Paolo',
               'Balog, Katalin',
               # 第二批逐条人工复核后的撞名/身份不符（详见 execution-log）
               'Gerbrandy, Jelle', 'Grant, Robert', 'Green, Adam',
               'Hanson, William', 'Hill, Thomas', 'Hippo', 'Homer',
               'Howard', 'Hyland, Martin', 'Iris', 'John Pollock',
               'Jonah', 'Klein, Peter', 'Ladner, Richard E.',
               # 第三批逐条人工复核后的撞名/身份不符
               'MacLeod, Colin', 'McKay, Thomas', 'Meskin, Aaron',
               'Moran, Thomas', 'Murphy, Peter', 'Nishimura', 'Pease, Adam',
               'Perry, John', 'Radcliff', 'Richmond, Marsha',
               # 第五批逐条人工复核后的撞名/无法对应/无数据
               'Selig, Richard', 'Sextus', 'Shanahan, Murray', 'Simmons, Craig',
               'Skow, Bradford', 'Solomon', 'Squatrito, Theresa',
               'Stanhope, Philip', 'Stephens, Chris', 'Tian Pian',
               'Turner, Dale', 'Ubaldo', 'Uniacke, Suzanne', 'Wagener',
               'Weckert, John', 'Weinrich, Martin', 'Yin Xian', 'Zosimus'}
    entries = []
    with io.open(MISSING, encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 3:
                entries.append((parts[0], parts[2]))
    path = person_path()
    lines = io.open(path, encoding='utf-8', newline='').read().split('\n')
    idx = {}
    for i, l in enumerate(lines):
        if l.startswith('| '):
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if len(cells) == 8 and cells[0] \
                    and not set(cells[0]) <= set(':-— '):
                idx.setdefault(norm_key_quote(cells[0]), i)
    out_rows = ['en\tqid\tlabel\tverdict\t籍属\t生卒\t为何不写']
    todo = [(k, m) for k, m in entries if k not in seen]
    todo = todo[args.start:args.start + args.limit]
    changed = 0
    for n, (key, miss) in enumerate(todo):
        if key in EXCLUDE:
            out_rows.append('%s\t\t\t%s\t\t\t身份存疑，人工排除' % (key, miss))
            continue
        i = idx.get(norm_key_quote(key))
        if i is None:
            out_rows.append('%s\t\t\t%s\t\t\t登记行未找到' % (key, miss))
            continue
        cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
        need_aff = cells[3] in ('—', '')
        need_dates = cells[4] in ('—', '')
        if not (need_aff or need_dates):
            out_rows.append('%s\t\t\t%s\t\t\t已补（运行时复核）' % (key, miss))
            continue
        toks = [t.strip() for t in key.split('/')][0]
        if ',' in toks:
            last, first = [x.strip() for x in toks.split(',', 1)]
            disp = '%s %s' % (first, last)
        else:
            disp = toks
        time.sleep(2)
        res = search(disp)
        cands = []
        for it in res:
            desc = (it.get('description') or '').lower()
            lab = (it.get('label') or '').casefold()
            if disp.casefold() in lab and any(
                    w in desc for w in ACADEMIC):
                cands.append((it['id'], it.get('description') or ''))
        if len(cands) != 1:
            why = '学术候选 %d 个' % len(cands) if res else '检索无命中'
            out_rows.append('%s\t\t\t%s\t\t\t%s' % (key, miss, why))
            continue
        qid, desc = cands[0]
        time.sleep(1)
        cl = claims(qid)
        affs = []
        for c in cl.get('P27', []):
            try:
                q = c['mainsnak']['datavalue']['value']['id']
                if q in COUNTRY:
                    affs.append(COUNTRY[q])
            except Exception:
                pass
        aff = '／'.join(dict.fromkeys(affs))
        if not aff:
            aff = aff_from_desc(desc)
        dates = year_or_fl(cl)
        if not aff and not dates:
            out_rows.append('%s\t%s\t%s\t%s\t\t\tWikidata 无可用数据'
                            % (key, qid, desc, miss))
            continue
        if need_aff and aff:
            cells[3] = aff
        if need_dates and dates:
            cells[4] = dates
        ev = '籍属/生卒联网查证：Wikidata %s（2026-11-24 查，凭证 %s）' % (
            qid, 'backfill-auto-2026-11-23.tsv')
        if ev not in cells[6]:
            cells[6] = cells[6].rstrip('|') + '；' + ev
        lines[i] = '| ' + ' | '.join(cells) + ' |'
        changed += 1
        out_rows.append('%s\t%s\t%s\t%s\t%s\t%s\tOK' % (
            key, qid, desc, miss, cells[3], cells[4]))
    print('处理 %d，待改 %d' % (len(todo), changed))
    out = os.path.join(RES, 'backfill-auto-2026-11-23.tsv')
    io.open(out, 'a', encoding='utf-8', newline='\n').write(
        '\n'.join(out_rows) + '\n')
    if args.apply and changed:
        io.open(path, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
        print('已写回 %s' % path)


if __name__ == '__main__':
    main()

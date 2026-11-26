# -*- coding: utf-8 -*-
"""量测：缺籍属的人名行，能否从 en/ 正文“the <国别> <身份> Name”式表述取国别（2026-11-26）。

只认姓名前 70 字内的国别形容词，且必须是紧邻的名词短语（the German philosopher …），
避免“German idealism”一类学派名误配。输出候选供人工核；不自动写表。
"""
import html
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = 'script/tmp/person-nation-harvest.tsv'

NATIONS = {
    'German': '德国', 'French': '法国', 'American': '美国', 'British': '英国',
    'English': '英国', 'Scottish': '英国（苏格兰）', 'Irish': '爱尔兰', 'Italian': '意大利',
    'Spanish': '西班牙', 'Portuguese': '葡萄牙', 'Dutch': '荷兰', 'Belgian': '比利时',
    'Swiss': '瑞士', 'Austrian': '奥地利', 'Polish': '波兰', 'Russian': '俄罗斯',
    'Czech': '捷克', 'Hungarian': '匈牙利', 'Danish': '丹麦', 'Swedish': '瑞典',
    'Norwegian': '挪威', 'Finnish': '芬兰', 'Greek': '希腊', 'Roman': '古罗马',
    'Chinese': '中国', 'Japanese': '日本', 'Korean': '韩国', 'Indian': '印度',
    'Persian': '伊朗', 'Arabic': '阿拉伯', 'Islamic': '阿拉伯', 'Jewish': '犹太',
    'Canadian': '加拿大', 'Australian': '澳大利亚', 'Brazilian': '巴西',
    'Mexican': '墨西哥', 'Argentine': '阿根廷', 'Turkish': '土耳其', 'Egyptian': '埃及',
}
NAMES = '|'.join(NATIONS)


def clean(t):
    t = html.unescape(t)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t)


def load(slug):
    for name in ('index.html', 'notes.html'):
        p = os.path.join('en', slug, name)
        if os.path.exists(p):
            return clean(io.open(p, encoding='utf-8', errors='replace').read())
    return ''


def surname(key):
    return key.split(',')[0].strip() if ',' in key else key.strip()


def main():
    rows = []
    for l in io.open('ren-ming-biao.md', encoding='utf-8', newline=''):
        if not l.startswith('|'):
            continue
        c = [x.strip() for x in l.split('|')]
        if len(c) < 9 or not c[1] or c[1] == '键':
            continue
        key, nation, first = c[1], c[4], c[6]
        if nation not in ('—', ''):
            continue
        if not re.match(r'^[A-Za-z0-9_.-]+$', first or ''):
            continue
        rows.append((key, first))
    got = 0
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('键\t首现\t国别候选\t上下文\n')
        for key, slug in rows:
            sn = surname(key)
            if len(sn) < 4:
                continue
            txt = load(slug)
            for m in re.finditer(re.escape(sn), txt, re.I):
                lo = max(0, m.start() - 90)
                pre = txt[lo:m.start()]
                nm = None
                for adj in NATIONS:
                    if re.search(r'\b' + adj + r'\b', pre):
                        nm = adj
                if nm:
                    f.write('%s\t%s\t%s\t%s\n'
                            % (key, slug, NATIONS[nm], (pre[-80:] + '[' + sn + ']').strip()))
                    got += 1
                    break
    print('缺籍属行 %d，国别候选 %d' % (len(rows), got))


if __name__ == '__main__':
    main()

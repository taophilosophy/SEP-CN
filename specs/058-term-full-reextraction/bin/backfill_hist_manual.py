# -*- coding: utf-8 -*-
"""历史人物定点回填（2026-11-24）：person-missing 中可确证的前 1900 年人物。"""
import io
import sys

sys.path.insert(0, '.')
from tools.register_lib import norm_key_quote, person_path

EV = 'people-wikidata-2026-11-24-hist.tsv'
# (键, 籍属, 生卒/鼎盛年, QID, 备注)
FIX = [
    ('Zhang Taiyan', '中国', '1869–1936', 'Q11068767',
     '生卒为学界通行（章炳麟，1869–1936）'),
    ('Emperor Wu (Han)', '中国（西汉）', '前156–前87', 'Q7225',
     '汉武帝刘彻'),
    ('Emperor Zhao (Han)', '中国（西汉）', '前94–前74', 'Q7227',
     '汉昭帝刘弗陵'),
    ('Mao Heng', '中国', '约前3–前2世纪（活动期）', 'Q10370954',
     '依条目描述“约前3/前2世纪经学家”记活动期'),
    ('Pak Cheka', '朝鲜', '1750–1815', 'Q562695', '朴齐家，朝鲜实学家'),
    ('King Milinda', '印度－希腊', '前300–前130', 'Q347878',
     '即印度-希腊国王米南德一世（Milinda＝Menander I）'),
    ('Eubulides of Miletus', '古希腊', '约前4世纪（活动期）', 'Q461007',
     'Wikidata 生卒前500–前400，与通说（前4世纪活动）不合，从通说'),
    ('Philo the Logician', '古希腊', '约前4世纪（活动期）', 'Q1366567',
     'Wikidata 生卒前400–前300，与通说（前4世纪活动）不合，从通说'),
    ('Theognis', '古希腊（麦加拉）', '约前570–前485', 'Q336115', '忒奥格尼斯'),
    ('Epimenides', '古希腊', '约前700–前600', 'Q319406', '生卒取 Wikidata'),
    ('Roger Swineshead', '英国', '？–约1365', 'Q18527586',
     'Wikidata 仅记卒年约 1365'),
    ('Metternich', '奥地利', '1773–1859', 'Q45662', '克莱门斯·冯·梅特涅'),
    ('Disraeli', '英国', '1804–1881', 'Q82006', '本杰明·迪斯雷利'),
    ('Montezuma', '阿兹特克（墨西加）', '1466–1520', 'Q141791',
     '蒙特祖马二世'),
    ('Jesus of Nazareth', '罗马帝国（犹太）', '约前7–30', 'Q302',
     '生卒取 Wikidata（学界通说约前6/前4–30/33）'),
    ('Paul (apostle)', '罗马帝国（塔尔苏斯）', '约5–66', 'Q9200',
     '生卒取 Wikidata（学界通说约5–约64/67）'),
    ('Zoroaster', '古波斯', '约前628–前551（传统纪年）', 'Q35811',
     '琐罗亚斯德生卒纪年学有争议，取 Wikidata 传统纪年'),
    ('Kang Chŏngildang', '朝鲜', '1772–1832', 'Q12583085', '朝鲜女性儒者'),
    ('Yi Onjŏk', '朝鲜', '1491–1553', 'Q624894', '李彦迪，朝鲜性理学家'),
    ('Eustratios of Nicaea', '拜占庭', '约1050–约1120', 'Q3561265',
     '拜占庭哲学家与神学家'),
]

p = person_path()
lines = io.open(p, encoding='utf-8', newline='').read().split('\n')
idx = {}
for i, l in enumerate(lines):
    if l.startswith('| '):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) == 8 and cells[0] and not set(cells[0]) <= set(':-— '):
            idx.setdefault(norm_key_quote(cells[0]), i)
n = 0
for key, aff, dates, qid, note in FIX:
    i = idx.get(norm_key_quote(key))
    if i is None:
        print('未找到', key)
        continue
    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
    if cells[3] in ('—', '') and aff != '—':
        cells[3] = aff
    if cells[4] in ('—', '') and dates != '—':
        cells[4] = dates
    ev = '籍属/生卒联网查证：Wikidata %s（2026-11-24 查，凭证 %s）；%s' % (
        qid, EV, note)
    if 'Wikidata %s' % qid not in cells[6]:
        cells[6] = cells[6].rstrip('|') + '；' + ev
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    n += 1
    print('%-24s %s｜%s' % (key, cells[3], cells[4]))
io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('written', n)

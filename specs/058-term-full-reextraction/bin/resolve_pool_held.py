# -*- coding: utf-8 -*-
"""池 held 项结算（2026-11-24）：今日已立册的书与人名，held 状态改 published。"""
import io
import json
import os
import sys

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools.register_lib import norm_key  # noqa: E402

DONE = ['Kashf al-Asrār', 'Zubdat al-ḥaqāʾiq', 'Beḥinat ha-Dat', 'Pulssi chappyŏn',
        'Tamhīdāt', 'al-Maṭālib al-ʿāliya', 'Maqāṣid', 'Maqāṣid al-Falāsifah',
        'Shem Tov Ibn Falaquera', 'Abū Ḥātim']

p = 'tasks/term-pool.json'
d = json.load(io.open(p, encoding='utf-8'))
done = {norm_key(x) for x in DONE}
n = 0
for c in d['candidates']:
    st = str(c.get('status', ''))
    if not st.startswith('held'):
        continue
    if norm_key(c.get('en') or '') in done:
        c['status'] = 'published@2026-11-24（held 结算：词条已立册）'
        print('结算', c.get('en'), '->', c['status'])
        n += 1
json.dump(d, io.open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False)
print('resolved=%d' % n)

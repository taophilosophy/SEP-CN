# -*- coding: utf-8 -*-
r"""021 诊断：指定文件里残留宏的成因（表缺失 / 数学段未覆盖 / 表内已展开）。"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')
sys.path.insert(0, HERE)
from expand_macros import MATH_SPAN_RE, mask_code, unmask_code  # noqa: E402

table = json.load(open(os.path.join(RESULTS, 'macro-table.json'), encoding='utf-8'))
macro_names = sys.argv[1].split(',')
for rel in sys.argv[2:]:
    path = os.path.join(REPO, rel)
    slug = os.path.basename(rel)[:-3].split('.')[0]
    macros = table.get(slug)
    print(f'== {rel}  slug={slug}  table={"有 %d 宏" % len(macros) if macros else "无"}')
    if macros:
        for m in macro_names:
            if m in macros:
                print(f'   {m} = {macros[m]!r}')
    text = open(path, encoding='utf-8').read()
    masked, spans = mask_code(text)
    covered = [m.group(0) for m in MATH_SPAN_RE.finditer(masked)]
    for m in macro_names:
        pat = re.compile(r'\\' + m + r'(?![a-zA-Z])')
        hits = list(pat.finditer(text))
        if not hits:
            continue
        # 检查每处是否位于某个数学段内
        outside = 0
        for h in hits[:20]:
            seg = text[max(0, h.start() - 400):h.start()]
            # 粗略：向前找最近的未配对 $ 或 \(
            if seg.rfind('$') < seg.rfind('\n'):
                outside += 1
        print(f'   {m}: 残留 {len(hits)} 处；前文同段无 $ 的 {outside} 处')
        for h in hits[:3]:
            print('      ', repr(text[max(0, h.start() - 70):h.start() + 50]))

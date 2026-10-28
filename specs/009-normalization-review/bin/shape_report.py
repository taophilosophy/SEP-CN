#!/usr/bin/env python3
"""009 形态分布报告生成器：聚合 results/para-review/<slug>.json 的 shape_pairs，
输出 T-01…T-09 全库形态分布表 → results/transpile-rules.md（骨架，人工裁定列留白）。

用法: python specs/009-normalization-review/bin/shape_report.py
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, '..', 'results', 'para-review')
RULES_MD = os.path.join(HERE, '..', 'results', 'transpile-rules.md')

RULE_OF = [
    ('T-01', ['h', 'p', 'pubinfo', 'preamble', 'merged'], '区块结构与 div 语义分类'),
    ('T-02', [], '行内构件（强调/上下标/链接）'),
    ('T-03', ['mathblock'], '数学定界'),
    ('T-04', ['table'], '表格（含嵌套扁平化）'),
    ('T-05', ['ul', 'ol', 'dl'], '列表嵌套'),
    ('T-06', ['figure', 'image'], '图与题注本地化'),
    ('T-07', ['bib-container'], '引文键与文献转脚注'),
    ('T-08', [], '脚注与补充材料'),
    ('T-09', [], '目录镜像'),
]


def main():
    shapes = Counter()
    n_entries = 0
    n_flagged = 0
    for f in sorted(os.listdir(OUT_DIR)):
        if not f.endswith('.json'):
            continue
        d = json.load(open(os.path.join(OUT_DIR, f), encoding='utf-8'))
        n_entries += 1
        n_flagged += 1 if d.get('state') == 'flagged' else 0
        for k, v in d.get('shape_pairs', {}).items():
            shapes[k] += v
    rows = []
    rows.append('# 转译规则目录与全库形态分布（009）\n')
    rows.append('生成：shape_report.py 聚合 para-review/<slug>.json；'
                '词条数 %d，flagged %d。\n' % (n_entries, n_flagged))
    rows.append('形态记法 `html块型→md块型`；`merged×n(A→B)`＝区段拆/合块转译'
                '（整组比值 ≥0.95，内容完整，T-01 形态注记）。\n')
    rows.append('| 规则 | 构件 | 形态对 | 全库计数 | 人工裁定 |')
    rows.append('| ---- | ---- | ---- | ---- | ---- |')
    for rid, keys, desc in RULE_OF:
        hits = {k: v for k, v in sorted(shapes.items(), key=lambda x: -x[1])
                if any(t in k for t in keys)} if keys else {}
        top = '；'.join('%s=%d' % (k, v) for k, v in list(hits.items())[:12]) or '（由分歧段人工归类）'
        rows.append('| %s | %s | 见左 | %s | 待填 |' % (rid, desc, top))
    rows.append('')
    rows.append('## 全部形态对（按计数降序）\n')
    rows.append('| 形态对 | 计数 |')
    rows.append('| ---- | ---- |')
    for k, v in shapes.most_common():
        rows.append('| %s | %d |' % (k, v))
    with open(RULES_MD, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(rows) + '\n')
    print('written', os.path.normpath(RULES_MD), 'entries=', n_entries)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""specs/033 卡钉基准：两登记册解析/折叠指纹采集（只读，不写登记册）。

用法：python specs/033-register-library/bin/pin.py <标签>
输出：specs/033-register-library/results/pin-<标签>.json

指纹面（specs/033 spec.md FR-3）：
  * 两登记册文件 sha256（并行会话改动登记册时作废当次对比，重采两侧）
  * 每登记册：数据行数、azsort 分节桶计数
  * 三口径逐行折叠指纹：各口径现存属主模块的折叠函数按数据行首列逐行求值，
    行序拼接后取 sha256（任何一行输出变化都显影）
  * parse_register2_full 行元组序列摘要 + 告警数
  * azsort scan+render 干跑内容 sha256（不写盘）
"""
import collections
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(os.path.dirname(HERE), 'results')
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, REPO)

from tools import (check_terms, cnki_query, registry_azsort, term_coverage,  # noqa: E402
                   term_flow, term_harvest, term_relations)

REGISTERS = [
    ('term', os.path.join(REPO, 'shu-yu-biao.md'), False),
    ('person', os.path.join(REPO, 'ren-ming-biao.md'), True),
]

# 口径 → 现存属主（specs/033 §2；迁移后函数名不变，经属主模块调用即验到调用点）
FOLDERS = [
    ('A_check_terms', check_terms, 'norm_key'),
    ('B_harvest', term_harvest, 'norm_key'),
    ('B_cnki', cnki_query, 'norm_key'),
    ('B_coverage', term_coverage, 'fold'),
    ('B_relations', term_relations, 'fold'),
    ('B_flow', term_flow, 'norm_key'),
    ('C_azsort', registry_azsort, 'norm_key'),
]


def _sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def pin_register(path, person):
    text = open(path, encoding='utf-8').read()
    lines = text.splitlines(True)
    out = {'sha256': _sha(text), 'buckets': {}, 'folds': {}, 'parse': {}}
    keys = []
    for line in lines:
        s = line.rstrip('\n')
        if s.startswith('|'):
            cells = check_terms.split_row(s)
            if check_terms.is_data_row(cells):
                keys.append(cells[0])
    out['row_count'] = len(keys)
    buckets = collections.Counter(registry_azsort.bucket_of(k) for k in keys)
    out['buckets'] = dict(sorted(buckets.items()))
    for label, mod, fname in FOLDERS:
        f = getattr(mod, fname)
        out['folds'][label] = _sha('\n'.join(f(k) for k in keys))
    rows2, warns = check_terms.parse_registry2_full(path)
    out['parse'] = {'digest': _sha(repr(rows2)), 'row_count': len(rows2),
                    'warn_count': len(warns)}
    header, rows, docs = registry_azsort.scan(lines)
    content, _b = registry_azsort.render(header, rows, docs, person=person)
    out['azsort_render'] = _sha(content)
    return out


def main(argv):
    label = argv[1] if len(argv) > 1 else 'snap'
    data = {'label': label,
            'registers': {name: pin_register(path, person)
                          for name, path, person in REGISTERS}}
    os.makedirs(RESULTS, exist_ok=True)
    out = os.path.join(RESULTS, 'pin-%s.json' % label)
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
    print('已采集：%s' % out)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

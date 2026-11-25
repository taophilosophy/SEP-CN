#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补丁池目录正本：迁移与再生（ADR-0062/0063，2026-11-16 用户裁定）。

正本布局：
  baseline/en-patches/<id>.patch   一补丁一文件（unified diff，头部注释承载登记字段）
  baseline/en-patches/INDEX.json   生成物（id→字段＋patch sha256），禁手改

行锚定语义：补丁以**整行**为 find/replace，并带 1 行上下文——上下文一并参与
`git apply --check` 校验，比 token 级替换更严（en/ 已冻结，上下文变了正是要的信号）。

用法:
  python specs/039-md-standardization/bin/migrate_en_patches.py            # 迁移旧 JSON（一次性）
  python specs/039-md-standardization/bin/migrate_en_patches.py --refresh  # 从现有 *.patch 再生（幂等）
退出码: 0 成功；1 拒绝（目标非空且未 --force）；2 输入错误/失配。
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
from tools.common import repo_path  # noqa: E402

POOL = repo_path('baseline', 'en-patches.json')
OUTDIR = repo_path('baseline', 'en-patches')
CTX = 1


def _strip_ws(s):
    return ''.join(s.split())


def _strip_tags(s):
    return _strip_ws(re.sub(r'<[^>]*>|<!--.*?-->', '', s, flags=re.S))


def admission(find, replace):
    if _strip_ws(find) == _strip_ws(replace):
        return 'blank'
    if _strip_tags(find) == _strip_tags(replace):
        return 'tag'
    return None


def build_patch(p):
    full = repo_path(p['file'])
    raw = open(full, encoding='utf-8', newline='').read()
    lines = raw.split('\n')
    hits = [i for i, ln in enumerate(lines) if ln == p['find']]
    if len(hits) != p['expect']:
        raise SystemExit('MISMATCH %s：整行命中 %d 次，expect %d（上游漂移？）'
                         % (p['id'], len(hits), p['expect']))
    if len(hits) != 1:
        raise SystemExit('UNSUPPORTED %s：补丁跨多行（行 %s），需人工改写为多 hunk'
                         % (p['id'], [i + 1 for i in hits]))
    idx = hits[0]
    new = p['replace']
    if admission(p['find'], new) is None:
        raise SystemExit('TEXT-LAYER %s：整行替换改动词符，禁入池' % p['id'])
    start = max(0, idx - CTX)
    end = min(len(lines), idx + CTX + 1)
    body_lines = []
    for i in range(start, end):
        if i == idx:
            body_lines.append('-%s' % lines[i])
            body_lines.append('+%s' % new)
        else:
            body_lines.append(' %s' % lines[i])
    n = start + 1
    count = end - start
    head = [
        '# SEP-CN 格式层补丁正本（ADR-0062/0063）——一补丁一文件，本目录即事实源。',
        '# 行锚定：find/replace 取整行并带上下文；命中计数必须等于 expect，失配即该件转换硬失败。',
        '# id: %s' % p['id'],
        '# slug: %s' % p['slug'],
        '# file: %s' % p['file'],
        '# expect: %s' % p['expect'],
        '# category: %s' % p['category'],
        '# origin: %s' % p['origin'],
        '# source: %s' % p['source'],
        '# created: %s' % (p.get('created') or datetime.now(timezone.utc).strftime('%Y-%m-%d')),
        '--- a/%s' % p['file'],
        '+++ b/%s' % p['file'],
        '@@ -%d,%d +%d,%d @@' % (n, count, n, count),
    ]
    return '\n'.join(head + body_lines) + '\n'


def parse_patch(text):
    meta = {}
    for line in text.split('\n'):
        if line.startswith('# '):
            key, _, val = line[2:].partition(': ')
            meta[key.strip()] = val.strip()
        elif line.startswith('--- '):
            break
    minus, plus = [], []
    for line in text.split('\n'):
        if line.startswith('--- ') or line.startswith('+++ ') or line.startswith('@@'):
            continue
        if line.startswith('-'):
            minus.append(line[1:])
        elif line.startswith('+'):
            plus.append(line[1:])
    if len(minus) != 1 or len(plus) != 1:
        raise SystemExit('UNSUPPORTED：补丁含 %d 减行 / %d 加行（应各 1）' % (len(minus), len(plus)))
    p = {'id': meta.get('id'), 'slug': meta.get('slug'), 'file': meta.get('file'),
         'expect': int(meta.get('expect') or 0), 'category': meta.get('category'),
         'source': meta.get('source'), 'origin': meta.get('origin'),
         'created': meta.get('created'),
         'find': minus[0], 'replace': plus[0]}
    missing = [k for k, v in p.items() if not str(v).strip()]
    if missing:
        raise SystemExit('FIELD MISSING %s：%s' % (p['id'] or '?', ','.join(missing)))
    return p


def write_index(patches):
    index = []
    for p, body in patches:
        index.append({'id': p['id'], 'slug': p['slug'], 'file': p['file'],
                      'expect': p['expect'], 'category': p['category'],
                      'source': p['source'], 'origin': p['origin'],
                      'patch': 'baseline/en-patches/%s.patch' % p['id'],
                      'sha256': hashlib.sha256(body.encode('utf-8')).hexdigest()})
    idx = {'schema': 'sep-cn-en-patches-dir/1',
           'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'note': '生成物，禁手改；正本为同目录 *.patch（ADR-0063 补丁池目录化）。',
           'count': len(index), 'patches': index}
    path = os.path.join(OUTDIR, 'INDEX.json')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(idx, ensure_ascii=False, indent=2) + '\n')
    return index


def main(argv):
    force = '--force' in argv
    refresh = '--refresh' in argv
    if refresh:
        files = sorted(f for f in os.listdir(OUTDIR) if f.endswith('.patch'))
        if not files:
            sys.stderr.write('无 *.patch 可再生\n')
            return 2
        out = []
        for fn in files:
            path = os.path.join(OUTDIR, fn)
            with open(path, encoding='utf-8', newline='') as f:
                p = parse_patch(f.read())
            body = build_patch(p)
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(body)
            out.append((p, body))
        write_index(out)
        print(json.dumps({'refreshed': len(out), 'outdir': OUTDIR}, ensure_ascii=False))
        return 0
    if not os.path.exists(POOL):
        sys.stderr.write('旧池不存在: %s（如需从现有目录再生请用 --refresh）\n' % POOL)
        return 2
    if os.path.isdir(OUTDIR) and os.listdir(OUTDIR) and not force:
        sys.stderr.write('目标目录非空（%s）；确认要覆盖请加 --force\n' % OUTDIR)
        return 1
    pool = json.load(open(POOL, encoding='utf-8'))
    os.makedirs(OUTDIR, exist_ok=True)
    out = []
    for p in pool.get('patches', []):
        body = build_patch(p)
        path = os.path.join(OUTDIR, '%s.patch' % p['id'])
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(body)
        out.append((p, body))
    write_index(out)
    os.remove(POOL)
    print(json.dumps({'migrated': len(out), 'outdir': OUTDIR,
                      'removed': POOL}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

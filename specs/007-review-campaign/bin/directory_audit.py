# -*- coding: utf-8 -*-
"""目录层逐行全量审计（specs/007-review-campaign，用户 2026-10-29 指令
"逐个复核全量 summary mu-lu-s"）。

背景：political-philosophy 遗留桩（SUMMARY 正式行、盘面有 stub、无 baseline、
上游 404 且不在目录）此前逃过全部检查——check_summary 只验盘面结构、
check_mulu_s 只验两册互一致、report 的反向标题索引被同题歧义击穿。
本审计补上缺失的维度：每行对上游目录的存在性语义核验。

对 SUMMARY.md 每一行（区分 正式/别名/占位/导航 四类）核：
  S1 盘面 stub 存在（正式/别名）
  S2 上游对应：正式行 slug ∈ catalog items；别名行英文名 ∈ 某条目 aliases；
     6 条裁定保留的撤稿词条与显式豁免除外——否则 finding no-upstream
  S3 baseline 登记存在（正式行；无 = finding no-baseline）
  S4 mu-lu-s 收录（正式行；无 = finding mulu-missing）
对 mu-lu-s.md 每一行核：
  M1 路径在 SUMMARY 中（无 = finding mulu-orphan）
  M2 盘面 stub 存在
  M3 上游对应（正式行，同 S2 口径）
输出：stdout 摘要 + --out 逐行凭证 JSONL。
退出码：0 无 finding；1 有 finding。
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from tools.common import load_json, repo_path, utcnow_iso  # noqa: E402

ADJUDICATED_ABSENT = {  # 裁定保留的撤稿词条（c75cc794/2eecf911）与历史裁定豁免
    'continental-rationalism', 'pineal-gland', 'qm-action-distance',
    'scientific-explanation', 'time-experience', 'wisdom',
}
ROW_RE = re.compile(r'^(\s*\*\s*)\[(.+)\]\(([^)]+)\)(.*)$')


def classify_line(line):
    """SUMMARY 行分类：formal | alias | placeholder | nav | other。"""
    if '——见' in line or '— see ' in line:
        return 'alias'
    if re.match(r'^\s*\*\s*\\\*\*', line) or re.match(r'^\s*\*\s*\\\*', line):
        return 'placeholder'
    m = re.search(r'\]\(([^)]+)\)', line)
    if m:
        t = m.group(1)
        if t.endswith('README.md') or '/' not in t:
            return 'nav'
        if re.match(r'^[a-z0-9]/[A-Za-z0-9.\-]+\.md$', t):
            return 'formal'
    return 'other'


def main():
    catalog = load_json(repo_path('baseline', 'catalog.json'))
    upstream_slugs = {it['slug'] for it in catalog['items'] if not it.get('alias_of')}
    alias_names = set()
    for it in catalog['items']:
        for a in (it.get('aliases') or []):
            alias_names.add(re.sub(r'[^a-z0-9]+', '', a.lower()))
    base = load_json(repo_path('baseline', 'entries.json'))
    base_slugs = {r['slug'] for r in base['entries']}

    summary_lines = open(repo_path('SUMMARY.md'), encoding='utf-8').read().split('\n')
    mulu_lines = open(repo_path('mu-lu-s.md'), encoding='utf-8').read().split('\n')
    summary_paths = set()
    for l in summary_lines:
        m = re.search(r'\]\(([^)]+)\)', l)
        if m:
            summary_paths.add(m.group(1))

    rows, findings = [], []
    s_counts = {'formal': 0, 'alias': 0, 'placeholder': 0, 'nav': 0, 'other': 0}

    for idx, line in enumerate(summary_lines, 1):
        m = ROW_RE.match(line)
        if not m:
            continue
        kind = classify_line(line)
        s_counts[kind] = s_counts.get(kind, 0) + 1
        text, target = m.group(2), m.group(3)
        rec = {'file': 'SUMMARY.md', 'line': idx, 'kind': kind,
               'path': target, 'title': text.strip()[:60]}
        slug = None
        pm = re.match(r'^([a-z0-9])/([A-Za-z0-9.\-]+)\.md$', target)
        if pm:
            slug = pm.group(2)
        if kind == 'formal':
            rec['upstream'] = slug in upstream_slugs
            rec['adjudicated_absent'] = slug in ADJUDICATED_ABSENT
            rec['baseline'] = slug in base_slugs if slug else False
            rec['mulu'] = any('](%s)' % target in ml for ml in mulu_lines)
            if not rec['upstream'] and not rec['adjudicated_absent']:
                findings.append({**rec, 'finding': 'no-upstream'})
            if not rec['baseline']:
                findings.append({**rec, 'finding': 'no-baseline'})
            if not rec['mulu']:
                findings.append({**rec, 'finding': 'mulu-missing'})
        elif kind == 'alias':
            stub = repo_path(target)
            rec['stub'] = os.path.exists(stub)
            # 行结构：`中文别名——见中文全名 english-alias — see english-full-name`
            # 别名 = " — see " 之前的段落的尾部拉丁文段（非 see 之后的全名）。
            # 层级别名（"父: 子"/"姓, 名"）另备叶节点候选。
            seg = re.split(r'\s+—\s+see\s+', text)[0]
            tail = re.split(r'[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef—–‧·：]', seg)[-1].strip()
            cands = {tail}
            if ':' in tail:
                cands.add(tail.split(':')[-1].strip())
            if ',' in tail:
                cands.add(tail.split(',')[-1].strip())
            norms = {re.sub(r'[^a-z0-9]+', '', c.lower()) for c in cands if c}
            norms.discard('')
            rec['alias_label'] = tail[:60]
            rec['alias_in_upstream'] = bool(norms & alias_names) if norms else None
            if not rec['stub']:
                findings.append({**rec, 'finding': 'no-stub'})
            if rec['alias_in_upstream'] is False:
                findings.append({**rec, 'finding': 'alias-not-in-upstream'})
        elif kind == 'placeholder':
            rec['stub'] = os.path.exists(repo_path(target))
            if not rec['stub'] and not target.endswith('README.md'):
                findings.append({**rec, 'finding': 'no-stub'})
        rows.append(rec)

    for idx, line in enumerate(mulu_lines, 1):
        m = ROW_RE.match(line)
        if not m:
            continue
        target = m.group(3)
        rec = {'file': 'mu-lu-s.md', 'line': idx, 'path': target,
               'title': m.group(2).strip()[:60]}
        in_summary = target in summary_paths
        stub = os.path.exists(repo_path(target))
        rec['in_summary'] = in_summary
        rec['stub'] = stub
        if not in_summary:
            findings.append({**rec, 'finding': 'mulu-orphan'})
        if not stub:
            findings.append({**rec, 'finding': 'no-stub'})
        pm = re.match(r'^([a-z0-9])/([A-Za-z0-9.\-]+)\.md$', target)
        if pm:
            slug = pm.group(2)
            rec['upstream'] = slug in upstream_slugs or slug in ADJUDICATED_ABSENT
            if not rec['upstream']:
                findings.append({**rec, 'finding': 'no-upstream'})
        rows.append(rec)

    from collections import Counter
    fc = Counter(f['finding'] for f in findings)
    summary = {'rows': len(rows), 'summary_lines': len(summary_lines),
               'summary_kinds': s_counts, 'findings': len(findings),
               'finding_kinds': dict(fc), 'at': utcnow_iso()}
    out_path = repo_path('specs', '007-review-campaign', 'results',
                         'directory-audit.jsonl')
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(json.dumps(summary, ensure_ascii=False))
    for x in findings:
        print('FINDING', json.dumps(x, ensure_ascii=False))
    return 0 if not findings else 1


if __name__ == '__main__':
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.exit(main())

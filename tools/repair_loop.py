# -*- coding: utf-8 -*-
"""递归修复循环：文件布局变更后，使 SUMMARY / mu-lu-s / baseline 与磁盘一致，
直至零断链、零丢失（用户 2026-10-27 指令"递归执行，直至无任何问题"）。

每轮：
  1. 建立盘上 basename → 实际路径 索引（词条区全量）；
  2. SUMMARY/mu-lu-s 断链改指实际位置；basename 找不到的记为"丢失"；
  3. 丢失文件从 git 历史找回，放入 pending/ 待人工归类；
  4. 盘上孤儿（未被 SUMMARY 引用）收编：非 stub 文件补 SUMMARY 行（按文件首行标题）；
  5. baseline.zh_doc 全量重同步；
  6. 验证：断链=0 且孤儿增量=0 → 终止。
"""
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import (  # noqa: E402
    read_text, repo_path, write_json_verified, write_text_verified)

SKIP_DIRS = {'.git', '.gitbook', '.github', '.vitepress', 'node_modules', 'baseline',
             'en', 'specs', 'tasks', 'yuanwen', 'script', '__pycache__', 'public',
             'pending', 'guan-yu', 'qian-yan'}
LINK_RE = re.compile(r'\]\(([^)]+\.md)\)')


def is_entry_area(rel):
    first = rel.split('/')[0]
    return first not in ('qian-yan', 'guan-yu', 'mu-lu-s.md', 'README.md') and \
        not rel.startswith(('baseline/', 'specs/', 'tasks/', 'yuanwen/', 'en/'))


def census():
    """盘上 md 索引：basename → [路径]；全部路径集合。"""
    base, allpaths = {}, []
    for root, dirs, files in os.walk(repo_path('.')):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(root, f), repo_path('.')).replace(os.sep, '/')
            allpaths.append(rel)
            base.setdefault(os.path.basename(rel), []).append(rel)
    return base, allpaths


def git_historical_content(rel):
    """从 git 历史找回文件的最后已提交内容。"""
    try:
        r = subprocess.run(['git', 'log', '--all', '--format=%H', '-1', '--', rel],
                           cwd=repo_path('.'), capture_output=True, text=True, timeout=30)
        sha = r.stdout.strip()
        if not sha:
            return None
        r2 = subprocess.run(['git', 'show', '%s:%s' % (sha, rel)],
                            cwd=repo_path('.'), capture_output=True, timeout=30)
        if r2.returncode == 0:
            return r2.stdout.decode('utf-8', 'replace')
    except Exception:
        pass
    return None


def repair_once(pending_used):
    base, allpaths = census()
    stats = {'fixed_links': 0, 'lost': 0, 'pending': 0, 'orphans': 0, 'baseline_sync': 0}

    # 1+2. SUMMARY / mu-lu-s 断链修复
    for rel in ('SUMMARY.md', 'mu-lu-s.md'):
        lines = read_text(repo_path(rel)).split('\n')
        out, changed = [], False
        for line in lines:
            pm = LINK_RE.search(line)
            if pm:
                target = pm.group(1)
                if target.startswith(('http', 'mu-lu-s')) or target in allpaths:
                    out.append(line)
                    continue
                cand = base.get(os.path.basename(target))
                if cand and len(cand) == 1:
                    newline = line.replace('](%s)' % target, '](%s)' % cand[0])
                    out.append(newline)
                    changed = True
                    stats['fixed_links'] += 1
                    continue
                # 丢失：从 git 历史找回 → pending/
                hist = git_historical_content(target)
                if hist:
                    pdir = repo_path('pending')
                    os.makedirs(pdir, exist_ok=True)
                    dst = os.path.join(pdir, os.path.basename(target))
                    if not os.path.exists(dst):
                        write_text_verified(dst, hist)
                    newline = line.replace('](%s)' % target, '](pending/%s)' % os.path.basename(target))
                    out.append(newline)
                    changed = True
                    stats['lost'] += 1
                    stats['pending'] += 1
                    continue
                stats['lost'] += 1
                out.append(line)
                continue
            out.append(line)
        if changed:
            write_text_verified(repo_path(rel), '\n'.join(out))

    # 3. 孤儿收编：盘上有、SUMMARY 无 → 若非 H1 桩则补 SUMMARY 行（附于文件所在目录语义下暂置末尾）
    summary = read_text(repo_path('SUMMARY.md'))
    refs = set(LINK_RE.findall(summary)) | set(LINK_RE.findall(read_text(repo_path('mu-lu-s.md'))))
    tail = []
    for p in sorted(allpaths):
        if p in refs or p.startswith('pending/'):
            continue
        body = read_text(repo_path(p))
        lines_nz = [l for l in body.split('\n') if l.strip()]
        if len(lines_nz) <= 1:
            stats['orphans'] += 1
            continue  # H1 桩：已在裁决表排队，不自动收编
        tail.append(p)
        stats['orphans'] += 1
    if tail:
        add = '\n'.join('* [%s](%s)' % (os.path.basename(p)[:-3], p) for p in tail)
        write_text_verified(repo_path('SUMMARY.md'),
                            read_text(repo_path('SUMMARY.md')).rstrip('\n') + '\n\n# 待归类（自动收编）\n\n' + add + '\n')

    # 4. baseline.zh_doc 重同步
    base_data = load_json_safe()
    n = 0
    for r in base_data.get('entries', []):
        zh = r.get('zh_doc')
        if zh and not os.path.exists(repo_path(zh)):
            cand = base.get(os.path.basename(zh))
            if cand and len(cand) == 1:
                r['zh_doc'] = cand[0]
                n += 1
    if n:
        base_data['updated_at'] = utcnow_iso()
        write_json_verified(repo_path('baseline', 'entries.json'), base_data)
    stats['baseline_sync'] = n

    # 5. 验证
    summary = read_text(repo_path('SUMMARY.md'))
    refs = set(LINK_RE.findall(summary)) | set(LINK_RE.findall(read_text(repo_path('mu-lu-s.md'))))
    broken = [l for l in refs
              if not l.startswith(('http', 'mu-lu-s', 'README')) and not os.path.exists(repo_path(l))]
    stats['broken_after'] = len(broken)
    return stats, broken[:10]


def load_json_safe():
    p = repo_path('baseline', 'entries.json')
    if os.path.exists(p):
        return read_text and __import__('tools.common', fromlist=['load_json']).load_json(p)
    return {'entries': []}


def main(argv):
    rounds = int(argv[0]) if argv else 5
    pending_used = set()
    for i in range(1, rounds + 1):
        stats, broken = repair_once(pending_used)
        print(json.dumps({'round': i, **stats, 'sample_broken': broken},
                         ensure_ascii=False))
        if stats['broken_after'] == 0:
            print(json.dumps({'status': 'CONVERGED', 'rounds': i}, ensure_ascii=False))
            return 0
    print(json.dumps({'status': 'NOT CONVERGED'}, ensure_ascii=False))
    return 1


def utcnow_iso():
    from tools.common import utcnow_iso as u
    return u()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

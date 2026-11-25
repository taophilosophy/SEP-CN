# -*- coding: utf-8 -*-
"""阶段 1.2 辅助：en/ 本轮变化性质分类（specs/062 SOP §1.2）。

判据（按强度递减）：

  new           新增文件（基线无此路径）
  layout        可见文本逐字等值，仅换行／标签属性／注释／模板重排
  tokens        可见文本词元多重集等值但词序变（极罕见，人工核）
  text          可见文本有实质改动（上游修订或改名传播），需逐件裁定
  binary        图片／二进制资产（含 .svg）：sha 变化即随钉替换入库，不建账
  asset         脚本／样式资产（sha 变化即随钉入库）

辅助列：chrome（框架行）、rename（croce／history 改名波纹）的增删行数。

输出：results/en-delta.json 与 results/en-delta.md。
用法：
  python specs/062-phase12-recheck/bin/en_delta.py            # 工作区 vs HEAD（抓取后未提交时）
  python specs/062-phase12-recheck/bin/en_delta.py --base REV # REV..HEAD（已提交后复跑）
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RES = os.path.join(ROOT, 'specs', '062-phase12-recheck', 'results')

STRIP = re.compile(r'(?s)<(script|style)[^>]*>.*?</\1>|<!--.*?-->|<[^>]+>')
CHROME = ('site-logo', 'listheader', 'menu-block', 'id="footer"', 'id="navbar"',
          'sep-man-red', 'bootstrap', 'stylesheet')
# 上游目录改名的下游波纹（引用文字随目录改名而变，非正文修订）
RENAME = ('croce-aesthetics', 'history, philosophy of',
          'history and historiography, philosophy of',
          'privacy-medicine', 'in health care and research')


def visible(s):
    s = STRIP.sub(' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


BIB = ('id="bibliography"', 'id="otherinternet"', 'Other Internet Resources', 'id="archives"')


def classify_line(line):
    body = line[1:]
    if any(k in body for k in CHROME):
        return 'chrome'
    if any(k in body for k in RENAME):
        return 'rename'
    return 'body'


def git(*args):
    return subprocess.run(['git'] + list(args), cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout


def changed_files(base=None):
    """收集变化文件；base 给定时取 REV..HEAD（已提交复跑），否则工作区 vs HEAD。"""
    if base:
        out = git('diff', '--name-status', base, 'HEAD', '--', 'en/')
        files = []
        for line in out.splitlines():
            parts = line.split('\t', 1)
            if len(parts) < 2 or parts[0].strip() == 'D':
                continue
            path = parts[1].strip().strip('"')
            if path.startswith('en/_catalog'):
                continue
            files.append(('M' if parts[0].strip() == 'M' else 'A',
                          path.replace('\\', '/')))
        return sorted(files)
    out = git('status', '--porcelain', '--', 'en/')
    files = []
    for line in out.splitlines():
        if len(line) < 4:
            continue
        st, path = line[:2].strip(), line[3:].strip().strip('"')
        if st in ('M', '??', 'A') and not path.startswith('en/_catalog'):
            files.append((st, path.replace('\\', '/')))
    return sorted(files)


def per_file(st, path, base=None):
    if path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico', '.pdf', '.zip', '.svg')):
        return 'binary', Counter(), 0, 0   # 图片资产（含 SVG）：按 sha 随钉替换，无文字面
    if path.lower().endswith(('.js', '.css')):
        return 'asset', Counter(), 0, 0    # 脚本／样式资产（如 local.js 宏定义），不建账
    rev = base + ':' + path if base else 'HEAD:' + path
    old = git('show', rev) if st == 'M' else ''
    full = os.path.join(ROOT, path.replace('/', os.sep))
    new = open(full, encoding='utf-8', errors='replace').read() if os.path.exists(full) else ''
    o, n = visible(old), visible(new)
    if st != 'M':
        kind = 'new'
    elif o == n:
        kind = 'layout'
    elif Counter(o.split()) == Counter(n.split()):
        kind = 'tokens'
    else:
        kind = 'text'
    diff_args = ['-U0'] + ([base, 'HEAD'] if base else []) + ['--', path]
    c = Counter()
    for line in git('diff', *diff_args).splitlines():
        if line[:3] in ('+++', '---') or line.startswith(('diff ', 'index ', '@@')):
            continue
        if line.startswith(('+', '-')):
            c[classify_line(line)] += 1
    total = sum(c.values())
    if kind == 'text' and total and c.get('rename', 0) == total:
        kind = 'rename-wave'   # 增删行全部是目录改名波纹
    return kind, c, total, c.get('rename', 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', help='REV..HEAD 复跑（抓取结果已提交后用）')
    args = ap.parse_args()
    os.makedirs(RES, exist_ok=True)
    rows, kinds = [], Counter()
    for st, path in changed_files(args.base):
        kind, c, nops, wave = per_file(st, path, args.base)
        kinds[kind] += 1
        slug = path.split('/')[1] if path.count('/') >= 2 else path
        rows.append({'path': path, 'slug': slug, 'status': st, 'kind': kind,
                     'ops': nops, 'wave': wave,
                     'chrome': c.get('chrome', 0), 'rename': c.get('rename', 0),
                     'body': c.get('body', 0)})
    report = {'schema': 'sep-cn-en-delta/2', 'files': len(rows),
              'slugs': len({r['slug'] for r in rows}),
              'kinds': dict(kinds), 'rows': rows}
    with open(os.path.join(RES, 'en-delta.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(report, ensure_ascii=False, indent=1) + '\n')
    L = ['# en/ 本轮变化性质分类', '',
         '变化文件 %d，涉及词条 %d；%s' % (len(rows), report['slugs'],
                                    json.dumps(dict(kinds), ensure_ascii=False)), '',
         '| 词条 | 文件 | 判定 | 增删行 | 波纹行 | 框架行 | 其余 |',
         '| --- | --- | --- | --- | --- | --- | --- |']
    for r in rows:
        L.append('| %s | %s | %s | %d | %d | %d | %d |'
                 % (r['slug'], r['path'].split('/')[-1], r['kind'], r['ops'], r['wave'],
                    r['chrome'], r['body']))
    with open(os.path.join(RES, 'en-delta.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')
    print(json.dumps({'files': len(rows), 'slugs': report['slugs'],
                      'kinds': dict(kinds)}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""阶段 1.2 编排器：HTML 重抓·基线更新·补丁复核·转换进度（specs/062 SOP §1.2）。

用法：
  python specs/062-phase12-recheck/bin/phase12.py --fetch        # 全量重抓并复核
  python specs/062-phase12-recheck/bin/phase12.py --no-fetch     # 只复核与出报告
  可选：--config A|B（默认 A）  --no-convert  --limit N  --only slug...

判据（写入报告）：
  有效   补丁命中数 == expect（补丁仍必要且可用）
  已修复 命中 0 且 replace 已存在（上游已修，补丁可退役）
  失配   其余（上游漂移或补丁失效，转换层会硬失败）

输出：results/phase12-run.json（机读）＋ results/phase12-report.md（人读）。
"""
import json
import os
import shutil
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RES = os.path.join(ROOT, 'specs', '062-phase12-recheck', 'results')
ENTRIES = os.path.join(ROOT, 'baseline', 'entries.json')


def run(args):
    p = subprocess.run([sys.executable, '-B'] + args, cwd=ROOT,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return p.returncode, (p.stdout or '').strip(), (p.stderr or '').strip()


def run_stream(args):
    """长任务：逐行转发到 stderr（保持进度可见），返回合并输出。"""
    p = subprocess.Popen([sys.executable, '-B'] + args, cwd=ROOT,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, encoding='utf-8', errors='replace', bufsize=1)
    lines = []
    for line in p.stdout:
        sys.stderr.write(line)
        sys.stderr.flush()
        lines.append(line.rstrip('\n'))
    return p.wait(), '\n'.join(lines), ''


def last_json(text):
    text = (text or '').strip()
    try:
        return json.loads(text)          # 整段 JSON（多行 indent 输出）
    except ValueError:
        pass
    for line in reversed(text.splitlines()):
        line = line.strip()
        if line.startswith('{') and line.endswith('}'):
            try:
                return json.loads(line)
            except ValueError:
                pass
    return None


def snap(path):
    d = json.load(open(path, encoding='utf-8'))
    return {e['slug']: {f['path']: f['sha256'] for f in e.get('files', [])}
            for e in d['entries']}


def diff_snap(a, b):
    return {'changed': sorted(s for s in a if s in b and a[s] != b[s]),
            'added': sorted(set(b) - set(a)),
            'removed': sorted(set(a) - set(b))}


def patch_review():
    sys.path.insert(0, ROOT)
    from tools import en_patch_lib
    rows = []
    for items in en_patch_lib.load_patches(notice=False).values():
        for p in items:
            full = os.path.join(ROOT, p['file'].replace('/', os.sep))
            html = open(full, encoding='utf-8', errors='replace').read() if os.path.exists(full) else ''
            n = html.count(p['find'])
            if n == p['expect']:
                verdict = '有效'
            elif n == 0 and p['replace'] in html:
                verdict = '已修复'
            else:
                verdict = '失配'
            rows.append({'id': p['id'], 'slug': p['slug'], 'origin': p['origin'],
                         'expect': p['expect'], 'hits': n, 'verdict': verdict})
    return rows


def progress():
    d = json.load(open(ENTRIES, encoding='utf-8'))
    kinds = Counter(f.get('kind') for e in d['entries'] for f in e.get('files', []))
    yw = sum(1 for base, _, fs in os.walk(os.path.join(ROOT, 'yuanwen')) for f in fs
             if f.endswith('.md'))
    out = {'entries': len(d['entries']), 'files_by_kind': dict(kinds), 'yuanwen_md': yw}
    for name, key in (('assembly-scan-all.json', 'b31'), ('page-scan-all.json', 'b32')):
        p = os.path.join(ROOT, 'specs', '053-en-template-audit', 'results', name)
        if os.path.exists(p):
            j = json.load(open(p, encoding='utf-8'))
            out[key] = ({'ok': j.get('ok'), 'fail': j.get('fail'), 'total': j.get('total')}
                        if key == 'b31' else {'counts': j.get('counts'), 'total': j.get('total')})
    return out


def main(argv=None):
    argv = argv or sys.argv[1:]
    fetch = '--no-fetch' not in argv
    config = 'A'
    if '--config' in argv:
        config = argv[argv.index('--config') + 1]
    os.makedirs(RES, exist_ok=True)

    before_path = os.path.join(RES, 'entries-before.json')
    if fetch or not os.path.exists(before_path):
        shutil.copyfile(ENTRIES, before_path)
    before = snap(before_path)

    fetch_last = os.path.join(RES, 'fetch-last.json')
    fetch_result = None
    if fetch:
        args = ['tools/fetch_all.py', '--config', config]
        if '--no-convert' in argv:
            args.append('--no-convert')
        if '--limit' in argv:
            args += ['--limit', argv[argv.index('--limit') + 1]]
        if '--only' in argv:
            tail = [a for a in argv[argv.index('--only') + 1:] if not a.startswith('-')]
            args += ['--only'] + tail
        code, out, err = run_stream(args)
        fetch_result = {'exit': code, 'json': last_json(out),
                        'tail': (out or err).splitlines()[-3:]}
        with open(fetch_last, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(json.dumps(fetch_result, ensure_ascii=False, indent=1) + '\n')
        print('[%s] fetch_all（exit %d）' % ('OK' if code == 0 else 'WARN', code))
    elif os.path.exists(fetch_last):
        fetch_result = json.load(open(fetch_last, encoding='utf-8'))
        fetch_result['reused'] = True

    # 补转（2026-11-25，specs/062 R-6）：转换失败不阻塞抓取，但必须自动补转并留痕；
    # Windows 文件占用（PermissionError）多为瞬时句柄，串行重试一次即可。
    convert_retry = None
    fails = ((fetch_result or {}).get('json') or {}).get('convert_failures') or []
    if fetch and fails:
        convert_retry = []
        for f in fails:
            slug = f.get('slug')
            if not slug:
                continue
            time.sleep(1.5)   # 让上一轮写句柄释放
            c, o, e = run(['tools/yuanwen.py', slug])
            entry = {'slug': slug, 'exit': c, 'recovered': c == 0,
                     'at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
            if c != 0:
                entry['error'] = ((e or o).splitlines() or [''])[-1][:300]
            convert_retry.append(entry)
            print('[%s] 补转 %s%s' % ('OK' if c == 0 else 'FAIL', slug,
                                     '' if c == 0 else '：' + entry['error']))

    after = snap(ENTRIES)
    delta = diff_snap(before, after)
    print('[OK] 差集：变化 %d／新增 %d／移除 %d'
          % (len(delta['changed']), len(delta['added']), len(delta['removed'])))

    # B 族账本刷新（2026-11-25，specs/062 第四十四批教训）：en/ 变了以后，版面账
    # （copyright/site_year/era）与结构账（rel_items、hids）仍是旧版，B3.2 会把这些
    # 陈旧字段报成 gap（62 件里 40 件属此）。固定顺序：两账 → B3.1 扫描 → 池重建 → 终判。
    b3_rebuild = None
    if '--rebuild-b3' in argv:
        steps = [
            ('版面账 page_layout', ['specs/053-en-template-audit/bin/page_layout.py']),
            ('结构账 article_ledger', ['specs/053-en-template-audit/bin/article_ledger.py']),
            ('B3.1 往返扫描', ['specs/053-en-template-audit/bin/reassemble.py', '--all',
                            '--out',
                            'specs/053-en-template-audit/results/assembly-scan-all.json']),
            ('B3.2 池重建', ['specs/053-en-template-audit/bin/page_assemble.py',
                           '--all', '--build']),
            ('B3.2 终判', ['specs/053-en-template-audit/bin/page_assemble.py', '--all']),
        ]
        b3_rebuild = []
        for name, cmd in steps:
            t0 = time.time()
            c, o, e = run_stream(cmd)
            b3_rebuild.append({'step': name, 'exit': c,
                               'seconds': round(time.time() - t0, 1)})
            print('[%s] %s（%.0f 秒）'
                  % ('OK' if c == 0 else 'FAIL', name, time.time() - t0))

    code, out, err = run(['tools/check_en_patches.py', '--strict'])
    patches = last_json(out)
    review = patch_review()
    print('[%s] 补丁复核（%d 条，失配 %d）'
          % ('OK' if code == 0 else 'FAIL', len(review),
             sum(1 for r in review if r['verdict'] == '失配')))

    code, out, err = run(['tools/check_yuanwen_fidelity.py', '--gate'])
    fidelity = last_json(out)
    print('[%s] I2 转换保真' % ('OK' if code == 0 else 'FAIL'))

    prog = progress()
    report = {'schema': 'sep-cn-phase12/1',
              'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
              'fetch': fetch_result, 'convert_retry': convert_retry,
              'b3_rebuild': b3_rebuild,
              'delta': {k: v[:200] for k, v in delta.items()},
              'delta_counts': {k: len(v) for k, v in delta.items()},
              'patches': {'summary': patches, 'review': review},
              'fidelity': fidelity, 'progress': prog}
    with open(os.path.join(RES, 'phase12-run.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(report, ensure_ascii=False, indent=1) + '\n')
    write_md(report)
    ok = ((patches or {}).get('mismatch', 1) == 0
          and (fidelity or {}).get('issue_total', 1) == 0
          and all(x['recovered'] for x in (convert_retry or [])))
    print(json.dumps({'phase': '1.2', 'ok': ok,
                      'delta': report['delta_counts'],
                      'patch_verdicts': Counter(r['verdict'] for r in review),
                      'i2_issues': (fidelity or {}).get('issue_total')},
                     ensure_ascii=False, default=dict))
    return 0 if ok else 1


def write_md(r):
    L = ['# 阶段 1.2 报告：HTML 重抓·基线更新·补丁复核·转换进度', '',
         '生成时间：%s' % r['generated_at'], '',
         '## 一、抓取与差集', '',
         '| 项 | 值 |', '| --- | --- |',
         '| 抓取 | %s |' % ('执行' if r['fetch'] else '跳过（--no-fetch）'),
         '| 变化件 | %d |' % r['delta_counts']['changed'],
         '| 新增件 | %d |' % r['delta_counts']['added'],
         '| 移除件 | %d |' % r['delta_counts']['removed'],
         '| 补转 | %s |' % ('无失败' if not r.get('convert_retry') else
                            '；'.join('%s %s' % (x['slug'], '成功' if x['recovered'] else '仍失败')
                                     for x in r['convert_retry'])), '']
    if r['delta_counts']['changed']:
        L += ['变化清单（前 50）：' + '、'.join('`%s`' % s for s in r['delta']['changed'][:50]), '']
    L += ['## 二、补丁复核（必要性／有效性／一致性）', '',
          '| 补丁 | 词条 | 出处 | 命中/expect | 判定 |', '| --- | --- | --- | --- | --- |']
    for p in r['patches']['review']:
        L.append('| %s | %s | %s | %d/%d | **%s** |'
                 % (p['id'], p['slug'], p['origin'], p['hits'], p['expect'], p['verdict']))
    L += ['', '一致性：INDEX／C2 准入／`git apply --check` 见 `check_en_patches` 汇总 %s。'
          % json.dumps(r['patches']['summary'] or {}, ensure_ascii=False), '']
    f = r['fidelity'] or {}
    L += ['## 三、转换进度', '',
          '| 指标 | 值 |', '| --- | --- |',
          '| I2 转换保真 | %d 件，issue %s |' % (f.get('checked', 0), f.get('issue_total')),
          '| 钉账词条 | %d |' % r['progress']['entries'],
          '| yuanwen md | %d |' % r['progress']['yuanwen_md'],
          '| B3.1 装配 | %s |' % r['progress'].get('b31'),
          '| B3.2 页面 | %s |' % r['progress'].get('b32'),
          '| 资产分类 | %s |' % r['progress']['files_by_kind'], '']
    L += ['## 四、判据', '',
          '* 有效＝命中数等于 expect；已修复＝命中 0 且 replace 已存在（可退役）；失配＝其余（转换层会硬失败）。',
          '* 补丁必要性以“上游是否修复”为准；一致性由 INDEX／C2／git apply 三面承载。', '']
    with open(os.path.join(RES, 'phase12-report.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(L))


if __name__ == '__main__':
    sys.exit(main())

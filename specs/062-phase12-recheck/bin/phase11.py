# -*- coding: utf-8 -*-
"""阶段 1.1 编排器：目录抓取与四方互转复核（specs/062 SOP §1.1）。

一键复跑：
  python specs/062-phase12-recheck/bin/phase11.py            # 抓上游目录 + 全链复核
  python specs/062-phase12-recheck/bin/phase11.py --offline  # 不联网，仅用最新钉存快照复核

步骤（顺序固定）：fetch_catalog → summary_sync report → catalog_drift --latest →
rebuild_catalog --check → check_catalog_network --gate → gen_en_summary --check →
check_mulu_s → sync_official_snapshot --check。

输出：results/phase11-run.json（机读）＋终端摘要；退出码 0＝全绿（漂移 allowed 时另报）。
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RES = os.path.join(ROOT, 'specs', '062-phase12-recheck', 'results')


def run(args):
    p = subprocess.run([sys.executable, '-B'] + args, cwd=ROOT,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    return p.returncode, (p.stdout or '').strip(), (p.stderr or '').strip()


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


def main(argv=None):
    argv = argv or sys.argv[1:]
    offline = '--offline' in argv
    os.makedirs(RES, exist_ok=True)
    steps = []

    def add(name, code, out, err, extra=None):
        rec = {'step': name, 'exit': code, 'ok': code == 0,
               'json': last_json(out), 'tail': (out or err).splitlines()[-1:] or ['']}
        if extra:
            rec.update(extra)
        steps.append(rec)
        print('[%s] %s%s' % ('OK' if code == 0 else 'FAIL', name,
                             '' if code == 0 else '（exit %d）' % code))

    if offline:
        code, out, err = run(['tools/fetch_catalog.py', '--reparse'])
        add('fetch_catalog --reparse', code, out, err)
    else:
        code, out, err = run(['tools/fetch_catalog.py'])
        add('fetch_catalog', code, out, err)

    if all(s['ok'] for s in steps):
        code, out, err = run(['tools/summary_sync.py', 'report'])
        add('summary_sync report', code, out, err)

    code, out, err = run(['tools/catalog_drift.py', '--latest',
                          '--json', os.path.join(RES, 'phase11-drift.json'),
                          '--md', os.path.join(RES, 'phase11-drift.md')])
    drift = last_json(out)
    add('catalog_drift --latest', code, out, err,
        extra={'changed': (drift or {}).get('changed')})

    code, out, err = run(['tools/rebuild_catalog.py', '--check'])
    add('rebuild_catalog --check', code, out, err)

    code, out, err = run(['tools/check_catalog_network.py', '--gate'])
    net = last_json(out)
    (net or {}).pop('gates', None) if isinstance(net, dict) else None
    add('check_catalog_network --gate', code, out, err,
        extra={'json': net} if net else None)

    code, out, err = run(['tools/gen_en_summary.py', '--check'])
    add('gen_en_summary --check', code, out, err)

    code, out, err = run(['tools/check_mulu_s.py'])
    add('check_mulu_s', code, out, err)

    code, out, err = run(['tools/sync_official_snapshot.py', '--check'])
    add('sync_official_snapshot --check', code, out, err)

    ok = all(s['ok'] for s in steps)
    report = {'schema': 'sep-cn-phase11/1',
              'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
              'offline': offline, 'ok': ok, 'steps': steps}
    with open(os.path.join(RES, 'phase11-run.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(report, ensure_ascii=False, indent=1) + '\n')
    print(json.dumps({'phase': '1.1', 'ok': ok, 'steps': len(steps),
                      'failed': [s['step'] for s in steps if not s['ok']],
                      'drift_changed': (drift or {}).get('changed')}, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())

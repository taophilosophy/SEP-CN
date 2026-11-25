# -*- coding: utf-8 -*-
"""术语在线限流感知扫描（2026-11-25）：慢节奏、可续跑、遇封即退。

背景：接口在突发请求后会长时间回“success=true 且全库零”，与真实空结果同形。
实测同一 token 在慢节奏下可稳定取数（Python 直连也取到过上千条），故改用
“慢 + 探针 + 退避”的无人值守扫描，而不是短时高频抓取。

节奏：词间 --gap 秒（默认 15）；每 --probe-every 个词或遇零结果时查一次
abduction 探针；探针为零则退避 --backoff 秒（默认 120），连续 --max-wait 次
探针失败即退出（退出码 2），下次运行从进度处续跑。

产物：JSONL（每行 {key,total,hits,tries}）与进度文件；均可用
`bin/apply_recheck.py` 落成 termonline-all 凭证。
"""
import argparse
import io
import json
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools import cnki_query as cq  # noqa: E402


def load_token(path='.secrets/termonline-session.json'):
    return json.load(io.open(path, encoding='utf-8'))['jwt']


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--keys', default='specs/058-term-full-reextraction/results/'
                                    'recheck-priority-2026-11-25.json')
    ap.add_argument('--state', default='C:/Users/ykla/AppData/Local/Temp/tl_sweep_prog.json')
    ap.add_argument('--out', default='C:/Users/ykla/AppData/Local/Temp/tl_sweep.jsonl')
    ap.add_argument('--gap', type=float, default=15)
    ap.add_argument('--probe-every', type=int, default=10)
    ap.add_argument('--backoff', type=int, default=120)
    ap.add_argument('--max-wait', type=int, default=8)
    a = ap.parse_args(argv)

    cq._ACTIVE_TOKEN = load_token()
    keys = json.load(io.open(a.keys, encoding='utf-8'))
    st = json.load(io.open(a.state, encoding='utf-8')) if os.path.exists(a.state) else {'next': 0}
    print('[%s] 起跑 next=%d/%d' % (time.strftime('%H:%M:%S'), st['next'], len(keys)))

    def probe():
        try:
            return cq._tl_all_probe()
        except Exception as exc:
            print('  探针异常 %s' % type(exc).__name__)
            return 0

    waited = 0
    out = io.open(a.out, 'a', encoding='utf-8', newline='\n')
    while st['next'] < len(keys):
        if st['next'] % a.probe_every == 0 or waited:
            total = probe()
            if not total:
                waited += 1
                if waited > a.max_wait:
                    print('探针连续失败 %d 次，停批；下次续跑' % a.max_wait)
                    return 2
                print('  探针 0，退避 %ds（第 %d 次）' % (a.backoff, waited))
                time.sleep(a.backoff)
                continue
            waited = 0
        key = keys[st['next']]
        try:
            data = cq._tl_all_fetch(key, 30)
            hits, note = cq._tl_all_parse(data)
            total = cq._tl_all_total(data)
        except Exception as exc:
            print('  %-40s 异常 %s' % (key[:40], type(exc).__name__))
            time.sleep(a.backoff)
            continue
        rec = {'key': key, 'total': total, 'hits': hits, 'tries': 1,
               'at': datetime.now(timezone.utc).isoformat(timespec='seconds')}
        out.write(json.dumps(rec, ensure_ascii=False) + '\n')
        out.flush()
        st['next'] += 1
        json.dump(st, io.open(a.state, 'w', encoding='utf-8'))
        print('  %3d/%d %-40s total=%-6d hits=%d' % (st['next'], len(keys), key[:40], total, len(hits)))
        time.sleep(a.gap)
    print('全部完成')
    return 0


if __name__ == '__main__':
    sys.exit(main())

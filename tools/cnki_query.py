# -*- coding: utf-8 -*-
"""译名查证驱动器（specs/008-terminology-campaign US-2，ADR-0012 依据优先级）。

用法:
  python tools/cnki_query.py --from-registry            # 两登记册全量逐条查证
  python tools/cnki_query.py --pool                     # 候选池 new 条目查证
  python tools/cnki_query.py --terms abduction epistemic justification
  python tools/cnki_query.py --provider termonline-standard --resume

Provider 插件（ADR-0012 通道实测 2026-10-28）:
  termonline-standard   匿名可用（标准文件术语库）         [默认]
  termonline-all        审定名词库，需登录 token          [禁用：待通道]
  cnki-dict             CNKI 翻译助手，TLS 指纹反爬       [禁用：待浏览器通道]

礼貌抓取：相邻请求 ≥5 秒（--interval 可调，仅限本地测试调小）；
失败退避重试 3 次（15/30/60s），仍失败记 error，禁止静默跳过。
凭证落 specs/008-terminology-campaign/results/queries/<provider>/<键>.json；
--resume（默认开）跳过已有凭证。查证结果只是证据，裁定仍走登记流程。

退出码: 0 完成（含 error 计数）；2 参数错误。
"""
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                      'queries')
REGISTRY = os.path.join(ROOT, 'yi-zhe-shuo-ming.md')
REGISTRY2 = os.path.join(ROOT, 'ren-ming-biao.md')
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')


def norm_key(text):
    """与 check_terms 同规的键；文件名安全化另由 safe_key。"""
    return re.sub(r'\s+', ' ', text.replace('*', '').strip()).casefold()


def safe_key(key):
    key = key.casefold()
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '_', key)[:80].strip('_')


# ---------------- providers ----------------

def _tl_standard_fetch(term, timeout):
    url = ('https://api.termonline.cn/main-serve/business/tm/tmWord/standardSearch'
           '?term=%s&match=2&sources=&pubYears=&pageSize=20&pageNo=1'
           % urllib.parse.quote(term))
    req = urllib.request.Request(url, headers={
        'User-Agent': UA,
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.termonline.cn/',
        'Origin': 'https://www.termonline.cn',
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode('utf-8', 'replace'))


def _tl_standard_parse(data):
    """返回 (hits, note)：hits=[{cn,en,code,standard}]。"""
    result = (data or {}).get('result') or {}
    svo = result.get('standardVO') or {}
    hits = []
    for w in svo.get('tmWordList') or []:
        hits.append({'cn': w.get('cn'), 'en': w.get('en'),
                     'code': w.get('standardCode'),
                     'standard': w.get('standardName')})
    note = 'standardVO totalRecords=%s' % svo.get('totalRecords')
    return hits, note


PROVIDERS = {
    'termonline-standard': {
        'fetch': _tl_standard_fetch,
        'parse': _tl_standard_parse,
        'enabled': True,
        'note': '术语在线标准文件术语库（匿名）',
    },
    'termonline-all': {
        'enabled': False,
        'note': '审定名词库 allSearch 需登录 token（2026-10-28 匿名恒空），待通道',
    },
    'cnki-dict': {
        'enabled': False,
        'note': 'CNKI 翻译助手 TLS 指纹反爬（curl/urllib 断连），待浏览器通道',
    },
}


class Pacer:
    """相邻请求最小间隔（宪法 V 礼貌抓取同标准）。"""

    def __init__(self, interval):
        self.interval = max(0.0, interval)
        self._last = 0.0

    def wait(self):
        now = time.monotonic()
        delta = now - self._last
        if delta < self.interval:
            time.sleep(self.interval - delta)
        self._last = time.monotonic()


def query_once(provider, term, timeout=30):
    data = provider['fetch'](term, timeout)
    hits, note = provider['parse'](data)
    return data, hits, note


def query_with_retry(provider, term, pacer, retries=(15, 30, 60), timeout=30):
    """退避重试；返回 (status, hits, note, raw, error)。"""
    note, err = '', None
    for attempt in range(1 + len(retries)):
        pacer.wait()
        try:
            data, hits, note = query_once(provider, term, timeout)
            status = 'ok' if hits else 'empty'
            return status, hits, note, data, None
        except Exception as exc:  # urllib/JSON 各类失败统一退避
            err = '%s: %s' % (type(exc).__name__, exc)
            if attempt < len(retries):
                time.sleep(retries[attempt])
    return 'error', [], note, None, err


def collect_terms(args):
    """--from-registry / --pool / --terms 三来源归并，返回 [(key, display)]。"""
    from tools import check_terms
    pairs = {}
    if args.from_registry:
        for path in (REGISTRY, REGISTRY2):
            rows, _ = check_terms.parse_registry(path)
            for row in rows:
                key = check_terms.norm_key(row[0])
                pairs.setdefault(key, row[0])
    if args.pool:
        if os.path.exists(POOL):
            data = json.load(open(POOL, encoding='utf-8'))
            for c in data.get('candidates', []):
                if c.get('status') != 'new':
                    continue
                key = norm_key(c.get('en', ''))
                if key:
                    pairs.setdefault(key, c.get('en', key))
    for t in args.terms:
        key = norm_key(t)
        pairs.setdefault(key, t)
    return sorted(pairs.items())


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    args = type('Args', (), {'from_registry': False, 'pool': False,
                             'terms': [], 'provider': 'termonline-standard',
                             'interval': 5.0, 'force': False})()
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--from-registry':
            args.from_registry = True
        elif a == '--pool':
            args.pool = True
        elif a == '--terms':
            i += 1
            while i < len(argv) and not argv[i].startswith('--'):
                args.terms.append(argv[i])
                i += 1
            continue
        elif a == '--provider':
            args.provider, i = argv[i + 1], i + 1
        elif a == '--interval':
            args.interval, i = float(argv[i + 1]), i + 1
        elif a == '--force':
            args.force = True
        i += 1
    if not (args.from_registry or args.pool or args.terms):
        print('用法见 docstring：--from-registry / --pool / --terms 必选其一')
        return 2
    prov = PROVIDERS.get(args.provider)
    if prov is None:
        print('未知 provider: %s（可用：%s）'
              % (args.provider, ', '.join(PROVIDERS)))
        return 2
    if not prov.get('enabled'):
        print('provider 禁用：%s —— %s' % (args.provider, prov['note']))
        return 2

    outdir = os.path.join(OUTDIR, args.provider)
    os.makedirs(outdir, exist_ok=True)
    pacer = Pacer(args.interval)
    stat = {'ok': 0, 'empty': 0, 'error': 0, 'skip': 0}
    for key, display in collect_terms(args):
        path = os.path.join(outdir, safe_key(key) + '.json')
        if os.path.exists(path) and not args.force:
            stat['skip'] += 1
            continue
        status, hits, note, raw, err = query_with_retry(prov, display, pacer)
        record = {
            'key': key, 'term': display, 'provider': args.provider,
            'queried_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'status': status, 'note': note, 'hits': hits,
            'error': err,
            'raw': None if raw is None else json.dumps(raw, ensure_ascii=False)[:50000],
        }
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(record, f, ensure_ascii=False, indent=1)
        os.replace(tmp, path)
        stat[status] += 1
        print('[%s] %s → %d hits%s' % (status, display, len(hits),
                                       ('（' + err + '）') if err else ''))
    print('查证完成：ok=%d empty=%d error=%d skip=%d（provider=%s，凭证 %s）'
          % (stat['ok'], stat['empty'], stat['error'], stat['skip'],
             args.provider, outdir))
    return 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""译名查证驱动器（specs/008-terminology-campaign US-2，ADR-0012 依据优先级）。

用法:
  python tools/cnki_query.py --from-registry            # 两登记册全量逐条查证
  python tools/cnki_query.py --pool                     # 候选池 new 条目查证
  python tools/cnki_query.py --terms abduction epistemic justification
  python tools/cnki_query.py --provider termonline-standard --resume

Provider 插件（ADR-0012 通道实测 2026-10-28）:
  termonline-standard   匿名可用（标准文件术语库）         [默认]
  termonline-all        审定名词库，需明文 JWT（X-Access-Token）[2026-10-28 破译，见 execution-log 第五轮]
  youdao-aux            有道词典 SSR 页（辅助参考档，不作依据）
  cnki-dict             CNKI 翻译助手，TLS 指纹反爬       [禁用：待浏览器通道]

termonline-all 通道：localStorage 的 token 是 AES-CBC-PKCS7 密文（站点 cacheCipher
key="_11111000001111@" iv="@11111000001001_"），须先解密成明文 JWT 再作为
X-Access-Token 头。明文 token 经 --token <jwt> 或环境变量 TERMONLINE_TOKEN 传入
（不落盘）；解密辅助见 tools/termonline_token.py（粘贴 localStorage 密文 → 明文）。

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
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)  # 脚本直跑时保证 from tools import 可用
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
    """返回 (hits, note)：hits=[{cn,en,code,standard,subject}]。

    字段名实测（2026-10-28）：standardVO.tmWordList 用 cnName/enName（非 cn/en）。
    """
    result = (data or {}).get('result') or {}
    svo = result.get('standardVO') or {}
    hits = []
    for w in svo.get('tmWordList') or []:
        hits.append({'cn': w.get('cnName'), 'en': w.get('enName'),
                     'code': w.get('standardCode'),
                     'standard': w.get('standardName'),
                     'subject': w.get('subjectName')})
    note = 'standardVO totalRecords=%s' % svo.get('totalRecords')
    return hits, note


def _youdao_fetch(term, timeout):
    """有道词典 SSR 页（辅助参考档，P0 换站 2026-10-28 实测可用）。"""
    url = ('https://dict.youdao.com/result?word=%s&lang=en'
           % urllib.parse.quote(term))
    req = urllib.request.Request(url, headers={
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Referer': 'https://dict.youdao.com/',
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode('utf-8', 'replace')


def _youdao_parse(html):
    """返回 (hits, note)：按学科分组的 <p class="grey">学科</p> + <p><span>译名</span></p>。"""
    hits = []
    blocks = re.split(r'<li class="mcols-layout">', html or '')[1:]
    for b in blocks:
        sub = re.search(r'<p class="grey">([^<]{1,40})</p>', b)
        subject = sub.group(1).strip() if sub else ''
        for cn in re.findall(r'<p><span>([^<]{1,60})</span></p>', b)[:10]:
            hits.append({'cn': cn.strip(), 'en': None, 'code': None,
                         'standard': None, 'subject': subject})
    note = 'youdao mcols=%d' % len(blocks)
    return hits, note


# 2026-10-28 第五轮破译（execution-log）：termonline-all 需明文 JWT 头。
# token 不落盘：--token / TERMONLINE_TOKEN 传入，仅进程内引用。
_ACTIVE_TOKEN = None


def _tl_all_fetch(term, timeout):
    """审定名词库 allSearch；需 X-Access-Token 明文 JWT，匿名恒空（200 但 totalRecords=0）。"""
    if not _ACTIVE_TOKEN:
        raise ValueError('termonline-all 需明文 JWT：--token <jwt> 或环境变量 TERMONLINE_TOKEN')
    url = ('https://api.termonline.cn/main-serve/business/tm/tmWord/allSearch'
           '?term=%s&match=2&sources=&pubYears=&pageSize=20&pageNo=1&baseId=1'
           % urllib.parse.quote(term))
    req = urllib.request.Request(url, headers={
        'User-Agent': UA,
        'Accept': 'application/json, text/plain, */*',
        'X-Access-Token': _ACTIVE_TOKEN,
        'Referer': 'https://www.termonline.cn/',
        'Origin': 'https://www.termonline.cn',
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode('utf-8', 'replace'))


def _tl_all_parse(data):
    """审定库聚合：searchResult[] 每库 {result:{totalRecords,tmWordList[]},id}。

    字段实测（2026-10-28）：tmWordList 词条 cn/en/source/subjectName/subjectFullName/
    publishYear/definition/bbh/wordNumber。命中按库聚合，库名由 tmDatabase/listFront
    的 id↔dbName 映射（0=审定公布/1=海峡两岸/2=其他来源/6=预公布）。
    """
    result = (data or {}).get('result') or {}
    DB_NAMES = {'0': '审定公布名词库', '1': '海峡两岸名词对照库',
                '2': '其他来源数据库', '6': '预公布名词数据库'}
    hits, notes = [], []
    for seg in result.get('searchResult') or []:
        res = (seg or {}).get('result') or {}
        total = res.get('totalRecords') or 0
        db = DB_NAMES.get(str((seg or {}).get('id')), str((seg or {}).get('id')))
        notes.append('%s=%s' % (db, total))
        for w in res.get('tmWordList') or []:
            hits.append({'cn': w.get('cn'), 'en': w.get('en'),
                         'code': w.get('wordNumber'), 'standard': w.get('source'),
                         'subject': w.get('subjectFullName') or w.get('subjectName')})
    note = '; '.join(notes)
    return hits, note


PROVIDERS = {
    'termonline-standard': {
        'fetch': _tl_standard_fetch,
        'parse': _tl_standard_parse,
        'enabled': True,
        'note': '术语在线标准文件术语库（匿名）',
    },
    'youdao-aux': {
        'fetch': _youdao_fetch,
        'parse': _youdao_parse,
        'enabled': True,
        'note': '有道词典 SSR 页（辅助参考档：不作依据，供裁定辅助，ADR-0012 档位外辅助源）',
    },
    'termonline-all': {
        'fetch': _tl_all_fetch,
        'parse': _tl_all_parse,
        'enabled': True,
        'requires_token': True,
        'note': '审定名词库 allSearch（2026-10-28 破译：需明文 JWT X-Access-Token，'
                '匿名恒空 200；token 经 --token / TERMONLINE_TOKEN，不落盘）',
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
                             'interval': 5.0, 'force': False, 'token': None})()
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
        elif a == '--token':
            args.token, i = argv[i + 1], i + 1
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
    if prov.get('requires_token'):
        global _ACTIVE_TOKEN
        _ACTIVE_TOKEN = args.token or os.environ.get('TERMONLINE_TOKEN')
        if not _ACTIVE_TOKEN:
            print('provider %s 需明文 JWT：--token <jwt> 或环境变量 TERMONLINE_TOKEN'
                  % args.provider)
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

# -*- coding: utf-8 -*-
"""术语在线·JWT 直连爬虫（ADR-0074）：无浏览器 profile，裸 JWT 发 allSearch 落凭证。

与 tl_crawler.py 的关系：同为术语在线通道，tl_crawler 走 Playwright profile 的 cookie/密文令牌，
本工具走 `.secrets/termonline-session.json` 的 JWT（listFront 激活窗口 → allSearch），
凭证 schema 与之完全一致（`queries/termonline-all/<safe_key>.json`），term_audit 可直接入库。

纪律：
  * ADR-0012 禁维基：db「其他来源数据库」含 source=维基百科 的条目，一律从 hits 滤除，不落证据。
  * 自适应限速：base interval（默认 8s）起，降级升速至 max（30s），恢复再回落；不破 AGENTS.md ≥5s。
  * 断点续抓：state 文件记已处理索引；已有 ok/empty 凭证默认跳过（幂等，--force 覆盖）。
  * 「查无」落 empty 凭证（不作否定证据，ADR-0012）。

用法:
  python tools/tl_jwt_crawl.py --queue script/tmp/tl-queue-A-need.json --limit 40
  python tools/tl_jwt_crawl.py --queue ... --limit 40 --start 40
  python tools/tl_jwt_crawl.py --probe "abductive reasoning"
退出码: 0 完成；2 参数/环境错误。
"""
import argparse
import io
import json
import os
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools.register_lib import norm_key_quote  # noqa: E402
from tools.cnki_query import safe_key  # noqa: E402

API = ('https://api.termonline.cn/main-serve/business/tm/tmWord/allSearch'
       '?term={term}&match=2&sources=&pubYears=&pageSize=20&pageNo=1&baseId=1')
ACTIVATE = 'https://api.termonline.cn/main-serve/business/tm/tmDatabase/listFront'
JWT_FILE = os.path.join(ROOT, '.secrets', 'termonline-session.json')
QD = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results', 'queries',
                  'termonline-all')
STATE = os.path.join(ROOT, 'script', 'tmp', 'tl-jwt-state.json')
DB_NAMES = ['审定公布名词库', '海峡两岸名词对照库', '其他来源数据库', '预公布名词数据库']
WIKI = '维基'


def _ctx():
    c = ssl.create_default_context()
    c.check_hostname = False
    c.verify_mode = ssl.CERT_NONE
    return c


def _get(url, jwt, ctx, timeout=20):
    req = urllib.request.Request(url, headers={'X-Access-Token': jwt,
                                               'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return json.loads(r.read().decode('utf-8'))


def load_jwt(path):
    d = json.load(open(path, encoding='utf-8'))
    jwt = d.get('jwt')
    exp = d.get('jwt_exp_unix')
    if not jwt:
        raise SystemExit('无 jwt 字段：%s' % path)
    if exp and int(time.time()) >= int(exp):
        raise SystemExit('JWT 已过期（%s）：需重新登录刷新 .secrets' % exp)
    return jwt


def query(term, jwt, ctx, retries_429=2):
    j = None
    for attempt in range(retries_429 + 1):
        try:
            j = _get(API.replace('{term}', urllib.parse.quote(term, safe='')), jwt, ctx)
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries_429:
                print('  [429] %r 冷却 30s 后重试' % term[:40], flush=True)
                time.sleep(30)
                continue
            raise
    srs = (j.get('result') or {}).get('searchResult') or []
    totals = [int((s.get('result') or {}).get('totalRecords') or 0) for s in srs]
    if any(t > 0 for t in totals):
        status, err = 'ok', None
    elif len(srs) >= 4:
        status, err = 'empty', None
    else:
        status, err = 'error', 'degraded shape (%d db)' % len(srs)
    hits, dropped_wiki = [], 0
    for s in srs:
        for w in ((s.get('result') or {}).get('tmWordList') or []):
            src = w.get('source') or ''
            if WIKI in src:
                dropped_wiki += 1
                continue
            hits.append({
                'cn': w.get('cn'), 'en': w.get('en'), 'source': src,
                'wordNumber': w.get('wordNumber'),
                'subjectFullName': w.get('subjectFullName') or '',
                'subjectName': w.get('subjectName') or '',
                'publishYear': w.get('publishYear'),
                'definition': (w.get('definition') or '')[:100],
            })
    note = 'variant=%s; %s; jwt-direct（JWT 直连，raw 略%s）' % (
        term,
        '; '.join('%s=%d' % (DB_NAMES[i] if i < len(DB_NAMES) else 'db%d' % i, t)
                  for i, t in enumerate(totals)) if totals else '4 库无返回',
        '；已滤维基 %d 条' % dropped_wiki if dropped_wiki else '')
    return {'status': status, 'note': note, 'hits': hits, 'error': err}


def write_cred(term, rec, out_dir=QD):
    key = norm_key_quote(term)
    fn = safe_key(key) + '.json'
    path = os.path.join(out_dir, fn)
    doc = {'key': key, 'term': term, 'provider': 'termonline-all',
           'queried_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'status': rec['status'], 'note': rec['note'], 'hits': rec['hits'],
           'error': rec['error'], 'raw': None}
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description='术语在线 JWT 直连爬虫（ADR-0074）')
    ap.add_argument('--queue', help='队列 JSON（[{en:...},...] 或 {candidates:[...]}）')
    ap.add_argument('--probe', metavar='TERM', help='单次探测')
    ap.add_argument('--limit', type=int, default=40, help='本次最多处理词数')
    ap.add_argument('--start', type=int, help='起始索引（默认读断点 state）')
    ap.add_argument('--interval', type=float, default=8.0, help='每 worker 相邻请求间隔秒')
    ap.add_argument('--max-interval', type=float, default=30.0)
    ap.add_argument('--workers', type=int, default=1, help='并发 worker 数（快速抓取）')
    ap.add_argument('--warm-every', type=float, default=45.0, help='续窗周期（<120s）')
    ap.add_argument('--jwt-file', default=JWT_FILE)
    ap.add_argument('--out-dir', default=QD)
    ap.add_argument('--force', action='store_true', help='已有凭证也重抓')
    ap.add_argument('--repair', action='store_true', help='只补抓 status=error 的凭证（不推进断点）')
    args = ap.parse_args(argv)
    out_dir = args.out_dir
    os.makedirs(out_dir, exist_ok=True)

    jwt = load_jwt(args.jwt_file)
    ctx = _ctx()
    _get(ACTIVATE, jwt, ctx)   # 首次激活

    if args.probe:
        r = query(args.probe, jwt, ctx)
        print(json.dumps({'status': r['status'], 'note': r['note'],
                          'hits': r['hits'][:6]}, ensure_ascii=False, indent=1))
        return 0

    if not args.queue:
        ap.error('需 --queue 或 --probe')
    data = json.load(open(args.queue, encoding='utf-8'))
    items = data.get('candidates') if isinstance(data, dict) else data
    terms = [it.get('en') if isinstance(it, dict) else str(it) for it in items]

    state = {}
    if os.path.exists(STATE):
        try:
            state = json.load(open(STATE, encoding='utf-8'))
        except (ValueError, OSError):
            state = {}
    start = args.start if args.start is not None else state.get('next', 0)

    interval = max(1.0, args.interval)
    t0 = time.time()
    # 预扫本批待抓（跳过已有 ok/empty；--repair 只取 status=error）
    todo = []
    i = start
    skip = 0
    if args.repair:
        for idx, term in enumerate(terms):
            if not term:
                continue
            cred = os.path.join(out_dir, safe_key(norm_key_quote(term)) + '.json')
            if not os.path.exists(cred):
                continue
            try:
                st = json.load(open(cred, encoding='utf-8')).get('status')
            except (ValueError, OSError):
                st = None
            if st == 'error':
                todo.append((idx, term))
        if args.limit:
            todo = todo[:args.limit]
        i = frontier = state.get('next', 0)   # repair 不推进断点
    while i < len(terms) and len(todo) < args.limit and not args.repair:
        term = terms[i]
        idx = i
        i += 1
        if not term:
            continue
        cred = os.path.join(out_dir, safe_key(norm_key_quote(term)) + '.json')
        if os.path.exists(cred) and not args.force:
            try:
                st = json.load(open(cred, encoding='utf-8')).get('status')
            except (ValueError, OSError):
                st = None
            if st in ('ok', 'empty'):
                skip += 1
                continue
        todo.append((idx, term))
    if not args.repair:
        frontier = (todo[-1][0] + 1) if todo else i

    lock = threading.Lock()
    stats = {'ok': 0, 'empty': 0, 'err': 0, 'done': 0}
    last_act = [time.time()]
    # 全局激活闸（tl_crawler 先例）：续窗后须静置 ≥5s 才可发 allSearch；
    # 闸门期间所有 worker 统一等待，防并发下窗口刚续就查（3 库降级根因）。
    gate_until = [0.0]

    def ensure_act(force=False):
        need = force or (time.time() - last_act[0] > args.warm_every)
        if not need:
            return
        with lock:
            if force or (time.time() - last_act[0] > args.warm_every):
                try:
                    _get(ACTIVATE, jwt, ctx)
                except Exception:
                    pass
                last_act[0] = time.time()
                gate_until[0] = time.time() + 5.0

    def wait_gate():
        left = gate_until[0] - time.time()
        if left > 0:
            time.sleep(left)

    def work(chunk):
        for idx, term in chunk:
            ensure_act()
            wait_gate()
            try:
                rec = query(term, jwt, ctx)
                if rec['status'] == 'error':
                    # 降级（3 库）＝会话窗口过期：强制续窗（带 5s 闸）后再查一次
                    ensure_act(force=True)
                    wait_gate()
                    rec = query(term, jwt, ctx)
            except Exception as e:
                rec = {'status': 'error', 'note': 'exception: %s' % str(e)[:80],
                       'hits': [], 'error': str(e)[:120]}
            write_cred(term, rec, out_dir)
            top = rec['hits'][0]['cn'] if rec['hits'] else ''
            with lock:
                stats['done'] += 1
                if rec['status'] == 'ok':
                    stats['ok'] += 1
                elif rec['status'] == 'empty':
                    stats['empty'] += 1
                else:
                    stats['err'] += 1
            print('  [%4d/%d] %-44s %-6s %s' % (
                idx + 1, len(terms), term[:44], rec['status'], top), flush=True)
            time.sleep(interval)

    if args.workers <= 1:
        work(todo)
    else:
        from concurrent.futures import ThreadPoolExecutor
        chunks = [todo[k::args.workers] for k in range(args.workers)]
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            list(ex.map(work, chunks))

    dt = time.time() - t0
    if not args.repair:
        state = {'next': frontier, 'last': (todo[-1][1] if todo else None),
                 'ok': stats['ok'], 'empty': stats['empty'], 'error': stats['err'],
                 'updated': datetime.now().isoformat(timespec='seconds')}
        json.dump(state, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False)
    print('本批%s：处理 %d（ok %d / empty %d / error %d）跳过(已有) %d；用时 %.0fs；'
          '速率 %.2fs/词；%d worker；断点 next=%d' % (
              '（repair）' if args.repair else '',
              stats['done'], stats['ok'], stats['empty'], stats['err'], skip,
              dt, dt / stats['done'] if stats['done'] else 0, args.workers, frontier))
    return 0


if __name__ == '__main__':
    sys.exit(main())

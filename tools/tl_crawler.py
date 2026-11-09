# -*- coding: utf-8 -*-
"""术语在线·审定名词库爬虫（编程式 HTTP 抓取，不做页面点击）。

与 tl_browser_batch.py 的分工：本工具是「爬」的部分（浏览器只承载登录态，请求全部由
程序发出、自己节流、自己判定降级、自己续跑）；tl_browser_batch.py 仍是「落凭证/审计」
的标准入口（--ingest → term_audit），批次文件 schema 完全一致。

机制（2026-11-09 实测）：
  * 登录态 = 真实浏览器 profile 里的会话 cookie（httpOnly）+ localStorage 的 AES 密文
    令牌（解密后取 .value 即 JWT，塞进 X-Access-Token 头）。直连 4 库全 0 的根因不是
    「Python 不行」，而是**服务端会话窗口要由应用自己发起的检索激活**：未激活时
    allSearch 只回 3 个空库（降级形态），激活后 4 库齐全。
  * 因此每批先 page.goto(search?searchText=…)（页面加载时应用自己会调一次 allSearch），
    再走 context.request.get（自动带 cookie 罐），全程无任何点击。
  * 降级绝不落盘为「查无」：连续 2 次降级 → 重新激活 + 退避（60s→300s），同词最多 3 试。

用法：
  python tools/tl_crawler.py --login
      打开可见窗口到术语在线，人工登录一次（profile 持久化到 state/tl-profile）。
  python tools/tl_crawler.py --probe "abductive reasoning"
      一次请求，打印四库形态（判登录/激活是否成立）。
  python tools/tl_crawler.py --crawl --queue <tmp>/az-term.json --batches 3
      按队列顺序爬，每批 8 词写 <out-dir>/tl-crawl-<offset>.json；默认断点续跑。

节奏：批内相邻请求默认 ≥8s（AGENTS.md 硬约束 ≥5s），批间默认 20s，可用
--interval / --batch-gap 调整。批次文件由 --ingest 入库，凭证覆盖写、幂等。
"""
import argparse
import io
import json
import os
import sys
import time
from datetime import datetime, timezone

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

PROFILE = os.path.join(ROOT, 'state', 'tl-profile')
STATE = os.path.join(ROOT, 'state', 'tl-crawl-state.json')
TOKEN_KEY = 'TERMONLINE__PRODUCTION__3.1.7__TOKEN__'
API = ('https://api.termonline.cn/main-serve/business/tm/tmWord/allSearch'
       '?term={term}&match=2&sources=&pubYears=&pageSize=20&pageNo=1&baseId=1')
WARM = 'https://www.termonline.cn/search?searchText={q}'
KEY = b'_11111000001111@'
IV = b'@11111000001001_'


def _decrypt_token(cipher):
    """AES-128-CBC/PKCS7 → JWT（.value）。只用内置库，避免额外依赖。"""
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    import base64
    raw = base64.b64decode(cipher)
    d = Cipher(algorithms.AES(KEY), modes.CBC(IV)).decryptor()
    plain = d.update(raw) + d.finalize()
    pad = plain[-1]
    plain = plain[:-pad] if 0 < pad <= 16 else plain
    return json.loads(plain.decode('utf-8')).get('value')


def _classify(srs):
    """四态：ok / empty（4 库真查无）/ error（降级或结构异常）。"""
    totals = [(s.get('result') or {}).get('totalRecords') or 0 for s in srs]
    if any(t > 0 for t in totals):
        return 'ok', None
    if len(srs) >= 4:
        return 'empty', None
    return 'error', 'degraded shape (%d db, all-zero)' % len(srs)


class Crawler:
    def __init__(self, headless=True, interval=8.0, batch_gap=20.0):
        from playwright.sync_api import sync_playwright
        self.interval = interval
        self.batch_gap = batch_gap
        self._pw = sync_playwright().start()
        kwargs = dict(headless=headless, viewport={'width': 1280, 'height': 900},
                      args=['--disable-blink-features=AutomationControlled'])
        os.makedirs(PROFILE, exist_ok=True)
        try:
            self.ctx = self._pw.chromium.launch_persistent_context(
                PROFILE, channel='chrome', **kwargs)
        except Exception:
            self.ctx = self._pw.chromium.launch_persistent_context(PROFILE, **kwargs)
        self.page = self.ctx.pages[0] if self.ctx.pages else self.ctx.new_page()
        self.degraded_streak = 0

    def close(self):
        try:
            self.ctx.close()
        finally:
            self._pw.stop()

    # ---- 登录态 ----
    def open_login(self):
        self.page.goto(WARM.format(q='logic'), wait_until='domcontentloaded')
        self.page.wait_for_timeout(4000)
        return self.token()

    def token(self):
        try:
            cipher = self.page.evaluate(
                "() => localStorage.getItem(%r)" % TOKEN_KEY)
        except Exception:
            return None
        if not cipher:
            return None
        try:
            return _decrypt_token(cipher)
        except Exception:
            return None

    def warm(self, q='logic', extra_wait=6000):
        """导航搜索页：应用自己会发一次 allSearch，服务端会话窗口由此激活。"""
        self.page.goto(WARM.format(q=q), wait_until='domcontentloaded')
        self.page.wait_for_timeout(extra_wait)

    # ---- 单次查询 ----
    def query(self, term, token):
        from urllib.parse import quote
        url = API.replace('{term}', quote(term, safe=''))
        try:
            r = self.ctx.request.get(url, headers={'X-Access-Token': token or ''},
                                     timeout=20000)
            j = r.json()
        except Exception as e:  # 网络/会话异常
            return {'term': term, 'status': 'error', 'dbs': [],
                    'error': 'request failed: %s' % e}
        srs = (j.get('result') or {}).get('searchResult') or []
        status, err = _classify(srs)
        dbs = []
        for s in srs:
            res = s.get('result') or {}
            dbs.append({'db': s.get('id'), 'total': res.get('totalRecords') or 0,
                        'words': [{'cn': w.get('cn'), 'en': w.get('en'),
                                   'source': w.get('source'),
                                   'wordNumber': w.get('wordNumber'),
                                   'subjectFullName': w.get('subjectFullName'),
                                   'subjectName': w.get('subjectName'),
                                   'publishYear': w.get('publishYear'),
                                   'definition': (w.get('definition') or '')[:100]}
                                  for w in (res.get('tmWordList') or [])[:12]]})
        return {'term': term, 'status': status, 'dbs': dbs, 'error': err}

    # ---- 批次循环 ----
    def run_batch(self, items, out_path, retries=3):
        token = self.token()
        if not token:
            raise SystemExit('未检测到登录令牌：先跑 --login 人工登录')
        out = []
        for it in items:
            r = None
            for attempt in range(1, retries + 1):
                r = self.query(it['display'], token)
                if r['status'] != 'error':
                    self.degraded_streak = 0
                    break
                self.degraded_streak += 1
                if self.degraded_streak >= 2:
                    wait = 60 if attempt == 1 else 300
                    print('  [降级] 第 %d 次，重新激活并冷却 %ds' % (attempt, wait))
                    self.warm('logic', extra_wait=8000)
                    token = self.token() or token
                    time.sleep(wait)
                time.sleep(self.interval)
            r['row_key'] = it['row_key']
            out.append(r)
            print('  %-42s %-5s %s' % (it['display'][:42], r['status'],
                                       '/'.join(str(d['total']) for d in r['dbs'])
                                       or '-'))
            time.sleep(self.interval)
        with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
            json.dump({'results': out}, f, ensure_ascii=False, indent=1)
        return out


def _load_state():
    if os.path.exists(STATE):
        try:
            return json.load(open(STATE, encoding='utf-8'))
        except (ValueError, OSError):
            pass
    return {'next_offset': 0}


def _save_state(offset):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    tmp = STATE + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'next_offset': offset,
                   'updated': datetime.now(timezone.utc).isoformat(timespec='seconds')},
                  f, ensure_ascii=False)
    os.replace(tmp, STATE)


def main(argv=None):
    ap = argparse.ArgumentParser(description='术语在线审定库爬虫（编程式 HTTP）')
    ap.add_argument('--login', action='store_true', help='打开可见窗口人工登录')
    ap.add_argument('--login-wait', type=int, default=240,
                    help='--login 时等待登录令牌的秒数（默认 240）')
    ap.add_argument('--probe', metavar='TERM', help='单次探测四库形态')
    ap.add_argument('--crawl', action='store_true', help='按队列爬取')
    ap.add_argument('--queue', help='emit 产出的队列 JSON')
    ap.add_argument('--out-dir', default=os.environ.get('TEMP', '/tmp'))
    ap.add_argument('--start', type=int, help='起始 offset（默认读断点）')
    ap.add_argument('--size', type=int, default=8, help='每批词数（≤8）')
    ap.add_argument('--batches', type=int, default=1, help='本进程跑几批')
    ap.add_argument('--interval', type=float, default=8.0, help='批内相邻请求秒数')
    ap.add_argument('--batch-gap', type=float, default=20.0, help='批间秒数')
    ap.add_argument('--headed', action='store_true', help='有头模式（默认无头）')
    ap.add_argument('--no-warm', action='store_true', help='跳过每批激活')
    args = ap.parse_args(argv)

    if args.login:
        c = Crawler(headless=False)
        try:
            c.page.goto(WARM.format(q='logic'), wait_until='domcontentloaded')
            c.page.wait_for_timeout(3000)
            deadline = time.time() + args.login_wait
            tok = c.token()
            while not tok and time.time() < deadline:
                time.sleep(3)
                tok = c.token()
            if tok:
                print('已检测到登录令牌（长度 %d）。profile: %s' % (len(tok), PROFILE))
                return 0
            print('窗口已打开但 %ds 内未检测到登录令牌；登录完成后重跑 --probe 验证。'
                  % args.login_wait)
            return 1
        finally:
            c.close()

    if args.probe:
        c = Crawler(headless=not args.headed)
        try:
            tok = c.token()
            if not tok:
                print('无登录令牌：先 --login')
                return 2
            c.warm('logic', extra_wait=8000)
            tok = c.token() or tok
            r = c.query(args.probe, tok)
            print(json.dumps(r, ensure_ascii=False, indent=1)[:1500])
            return 0 if r['status'] != 'error' else 1
        finally:
            c.close()

    if args.crawl:
        if not args.queue:
            ap.error('--crawl 需要 --queue')
        data = json.load(open(args.queue, encoding='utf-8'))
        items = data.get('items') or []
        st = _load_state()
        offset = args.start if args.start is not None else st.get('next_offset', 0)
        c = Crawler(headless=not args.headed, interval=args.interval,
                    batch_gap=args.batch_gap)
        try:
            if not c.token():
                print('无登录令牌：先 --login')
                return 2
            for b in range(args.batches):
                chunk = items[offset:offset + args.size]
                if not chunk:
                    print('队列已到末尾（offset=%d / %d）' % (offset, len(items)))
                    break
                if not args.no_warm:
                    c.warm(chunk[0]['display'] or 'logic')
                out_path = os.path.join(args.out_dir, 'tl-crawl-%d.json' % offset)
                print('batch offset=%d n=%d → %s' % (offset, len(chunk), out_path))
                c.run_batch(chunk, out_path)
                offset += len(chunk)
                _save_state(offset)
                if b + 1 < args.batches:
                    time.sleep(args.batch_gap)
            print('done；next_offset=%d / %d' % (offset, len(items)))
            return 0
        finally:
            c.close()

    ap.print_help()
    return 2


if __name__ == '__main__':
    sys.exit(main())

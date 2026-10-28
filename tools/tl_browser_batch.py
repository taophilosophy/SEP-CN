# -*- coding: utf-8 -*-
"""termonline 审定名词库·浏览器通道批量查询（specs/008 第六轮标准流程）。

背景（2026-10-28 实测修正第五轮结论）：审定库 allSearch 的鉴权凭据是登录
cookie 会话（httpOnly，JS 与 Python 均不可读出复制），X-Access-Token 头单独
发送会被服务端静默降级为「200 + 全库 totalRecords=0」（与匿名不可区分）。
cookie 会话只在真实浏览器内成立，故查询经 ZCode 浏览器页面内 fetch
（credentials:"include"）执行；本工具承担两个纯本地环节：

  emit   产出查询清单 [{row_key, variant, display}]（登记册全量，归并行
         「主形 / 他形」拆成变体分别查询、结果合并回整行键）。
  ingest 把浏览器批次结果按 row_key 归并，写成与 cnki_query.py 同 schema 的
         凭证 JSON（provider=termonline-all，note 记各库 totalRecords，
         raw 留空——浏览器通道不落原始报文，hits 即凭证）。

标准作业（S.O.P. 全文见 specs/008-terminology-campaign/contracts/browser-channel.md）：
  1) python tools/tl_browser_batch.py --emit --out <tmp>/tl-batch.json
  2) 浏览器 REPL 按批次（每批 ≤10 词、相邻请求 ≥5s）fetch allSearch，
     结果 JSON 存 <tmp>/tl-batch-N.json
  3) python tools/tl_browser_batch.py --ingest <tmp>/tl-batch-N.json
  4) python tools/term_audit.py 复核四态；登记修改走登记流程（只报告不修改）。

退出码：0 完成；2 参数/输入错误。
"""
import io
import json
import os
import re
import sys
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

QUERIES = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                       'queries')
OUTDIR = os.path.join(QUERIES, 'termonline-all')
PROVIDER = 'termonline-all'
# 与 cnki_query._tl_all_parse 的库名映射保持一致（tmDatabase/listFront 序）。
DB_NAMES = {'0': '审定公布名词库', '1': '海峡两岸名词对照库',
            '2': '其他来源数据库', '6': '预公布名词数据库'}


def _db_name(raw):
    """API 的 id 为 32 位十六进制串（…0006），折算十进制后查库名。"""
    s = str(raw)
    short = str(int(s, 16)) if re.fullmatch(r'[0-9a-fA-F]{4,}', s) else s
    return DB_NAMES.get(short, short)


def emit(out_path, pool=False):
    """产出批次清单：登记册（+可选池）全量，归并行拆变体。"""
    from tools import check_terms, cnki_query
    args = type('Args', (), {'from_registry': True, 'pool': pool, 'terms': []})()
    pairs = cnki_query.collect_terms(args)
    items = []
    for key, display in pairs:
        variants = [v.strip() for v in display.split('/') if v.strip()]
        if len(variants) > 1:
            for v in variants:
                items.append({'row_key': key, 'variant': v, 'display': v})
        else:
            items.append({'row_key': key, 'variant': display, 'display': display})
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                   'count': len(items), 'items': items},
                  f, ensure_ascii=False, indent=1)
    print('emit %d 项（%d 行，归并行拆变体）→ %s'
          % (len(items), len(pairs), out_path))
    return 0


def _record_status(group):
    stats = [g.get('status') for g in group]
    if any(s == 'ok' for s in stats):
        return 'ok'
    if all(s == 'error' for s in stats):
        return 'error'
    return 'empty'


def load_variant_map(map_path):
    """emit 清单 → {norm_key(variant): row_key}；变体冲突取首个并告警。"""
    from tools import cnki_query
    if not map_path or not os.path.exists(map_path):
        return {}
    data = json.load(open(map_path, encoding='utf-8'))
    vmap, clash = {}, []
    for item in data.get('items', []):
        k = cnki_query.norm_key(item.get('variant', ''))
        if not k:
            continue
        if k in vmap and vmap[k] != item.get('row_key'):
            clash.append(k)
            continue
        vmap[k] = item['row_key']
    if clash:
        print('变体键冲突（取首）：', sorted(set(clash)))
    return vmap


def ingest(in_path, map_path=None):
    """浏览器批次结果 → 凭证 JSON（按 row_key 归并，覆盖写）。"""
    from tools import cnki_query
    batch = json.load(open(in_path, encoding='utf-8'))
    results = batch.get('results') if isinstance(batch, dict) else batch
    if not isinstance(results, list):
        print('输入须为 {results:[...]} 或 [...]（浏览器批次结果）')
        return 2
    vmap = load_variant_map(map_path)
    groups = {}
    order = []
    for r in results:
        key = r.get('row_key')
        if key is None:
            nk = cnki_query.norm_key(r.get('term', ''))
            key = vmap.get(nk, nk)
        if key not in groups:
            groups[key] = []
            order.append(key)
        groups[key].append(r)
    os.makedirs(OUTDIR, exist_ok=True)
    stat = {'ok': 0, 'empty': 0, 'error': 0}
    for key in order:
        group = groups[key]
        hits, notes, errs = [], [], []
        for g in group:
            notes.append('variant=%s' % g.get('term', g.get('variant', '')))
            if g.get('error'):
                errs.append('%s: %s' % (g.get('term'), g['error']))
            for db in g.get('dbs') or []:
                name = _db_name(db.get('db'))
                notes.append('%s=%s' % (name, db.get('total') or 0))
                for w in db.get('words') or []:
                    hits.append({'cn': w.get('cn'), 'en': w.get('en'),
                                 'code': w.get('wordNumber'),
                                 'standard': w.get('source'),
                                 'subject': w.get('subjectFullName')
                                 or w.get('subjectName')})
        status = _record_status(group)
        display = ' / '.join(dict.fromkeys(
            g.get('term', g.get('variant', '')) for g in group))
        record = {
            'key': key, 'term': display, 'provider': PROVIDER,
            'queried_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'status': status,
            'note': '; '.join(notes) + '; browser-channel（cookie 会话，raw 略）',
            'hits': hits[:60],
            'error': '; '.join(errs) if errs else None,
            'raw': None,
        }
        path = os.path.join(OUTDIR, cnki_query.safe_key(key) + '.json')
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(record, f, ensure_ascii=False, indent=1)
        os.replace(tmp, path)
        stat[status] += 1
        print('[%s] %s → %d hits' % (status, display, len(hits)))
    print('ingest 完成：ok=%d empty=%d error=%d（凭证 %s）'
          % (stat['ok'], stat['empty'], stat['error'], OUTDIR))
    return 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    out_path, in_path, map_path, pool = None, None, None, False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == '--emit':
            pass
        elif a == '--ingest':
            i += 1
            in_path = argv[i]
        elif a == '--out':
            i += 1
            out_path = argv[i]
        elif a == '--map':
            i += 1
            map_path = argv[i]
        elif a == '--pool':
            pool = True
        i += 1
    if in_path:
        return ingest(in_path, map_path)
    if out_path:
        return emit(out_path, pool)
    print(__doc__)
    return 2


if __name__ == '__main__':
    raise SystemExit(main())

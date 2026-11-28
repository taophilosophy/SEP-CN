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

失败退避重试 3 次（15/30/60s），仍失败记 error，禁止静默跳过
（2026-11-18 废除礼貌抓取间隔规则，ADR-0069：不再有最小请求间隔）。
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

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)  # 脚本直跑时保证 from tools import 可用
from tools.register_lib import norm_key, person_path, term_path  # noqa: E402

OUTDIR = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                      'queries')
REGISTRY = term_path()
REGISTRY2 = person_path()
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')

# 键口径说明（specs/033 §2）：本工具缓存/查证键用 B 基础折叠键（norm_key），
# 与 check_terms 的 A 引号折叠键（norm_key_quote）是**有意分歧**——引号形键会
# 生成两份缓存凭证，属可接受冗余；升 A 会翻动既有凭证文件名，未纳入（历史
# docstring 曾误称「与 check_terms 同规」，2026-11-15 更正）。


_GREEK = {
    'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta', 'ε': 'epsilon',
    'ζ': 'zeta', 'η': 'eta', 'θ': 'theta', 'ι': 'iota', 'κ': 'kappa',
    'λ': 'lambda', 'μ': 'mu', 'ν': 'nu', 'ξ': 'xi', 'ο': 'omicron',
    'π': 'pi', 'ρ': 'rho', 'σ': 'sigma', 'ς': 'sigma', 'τ': 'tau',
    'υ': 'upsilon', 'φ': 'phi', 'χ': 'chi', 'ψ': 'psi', 'ω': 'omega',
}


def safe_key(key):
    """文件名安全键。希腊字母须音译：否则 ω-consistency 被剥成 consistency，
    与真词 consistency 的凭证同名覆盖（2026-11-12 实踩）。"""
    key = key.casefold().translate(str.maketrans(_GREEK))
    return re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '_', key)[:80].strip('_')


_JWT_RE = re.compile(r'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}')


def redact_secrets(text):
    """凭证落盘前脱敏：JWT 与 token=... 查询串不进入证据文件。

    2026-11-28 安全审计：termonline 的 401 响应会把带 token 的回源 URL 写进
    message；原样落 raw 等于把会话令牌写进公开仓库。
    """
    if not text:
        return text
    text = _JWT_RE.sub('[REDACTED-JWT]', text)
    return re.sub(r'(?i)(token(?:=|%3D)(?:%22)?)[^&\s"\\]+', r'\1[REDACTED]', text)


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


class ChannelSuspect(RuntimeError):
    """通道看似成功实则不可用（限流、后端抖动、回包结构变更）。不重试、不记空命中。"""


def _tl_all_fetch(term, timeout):
    """审定名词库 allSearch；需 X-Access-Token 明文 JWT，匿名恒空（200 但 totalRecords=0）。

    2026-11-25 实测：后端有间歇性“全零回包”（同 token 同参数，前一次 0、隔几秒再查
    上千条）。全零时重查一次，宁可多一次请求，也不把瞬时故障记成“确无收录”。
    """
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
        data = json.loads(resp.read().decode('utf-8', 'replace'))
    if _tl_all_total(data):
        return data
    time.sleep(2)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode('utf-8', 'replace'))


def _tl_all_total(data):
    """四库 totalRecords 之和；用于全零判定与探针。"""
    result = (data or {}).get('result') or {}
    return sum(((s or {}).get('result') or {}).get('totalRecords') or 0
               for s in result.get('searchResult') or [])


_DB_NAMES = {0: '审定公布名词库', 1: '海峡两岸名词对照库',
             2: '其他来源数据库', 6: '预公布名词数据库'}


def _db_name(raw):
    """分库 id → 库名。id 为 32 位补零数字串，取末位数字归一；未知库记 db-<n>。"""
    s = str(raw or '').strip().lstrip('0') or '0'
    if not s.isdigit():
        return 'db-' + str(raw)[:8]
    return _DB_NAMES.get(int(s), 'db-' + s)


def _tl_all_probe(timeout=30):
    """正控制探针：查 abduction（自然辩证法名词·2024 等，实测上千条），返回四库总数。

    接口在限流或后端抖动时会回 success=true 且各库全零，与“确无收录”同形；只有探针
    能把通道坏与词条空分开。探针本身不写凭证（2026-11-25 实测：同一 token 在浏览器
    里能查到，脚本连发 20 余次后开始全零，隔数分钟后恢复）。
    """
    return _tl_all_total(_tl_all_fetch('abduction', timeout))


def _tl_all_parse(data):
    """审定库聚合：searchResult[] 每库 {result:{totalRecords,tmWordList[]},id}。

    字段实测（2026-10-28）：tmWordList 词条 cn/en/source/subjectName/subjectFullName/
    publishYear/definition/bbh/wordNumber。库名由 tmDatabase/listFront 的 id↔dbName
    映射：id 是 32 位补零形（"00000000000000000000000000000000"＝审定公布、
    …0001＝海峡两岸、…0002＝其他来源、…0006＝预公布），故取末位数字归一，
    不能按字面 '0'/'1' 比对（2026-11-25 更正：曾把补零形当成 UUID 误判为通道故障）。

    空包识别交给探针（见 _tl_all_probe）：token 权限不足时接口仍回 success=true 且
    各库 totalRecords=0，与“确无收录”同形，只有正控制探针能区分。
    """
    result = (data or {}).get('result') or {}
    hits, notes = [], []
    for seg in result.get('searchResult') or []:
        res = (seg or {}).get('result') or {}
        total = res.get('totalRecords') or 0
        notes.append('%s=%s' % (_db_name((seg or {}).get('id')), total))
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
        'probe': _tl_all_probe,
        'note': '审定名词库 allSearch（需明文 JWT X-Access-Token；限流/抖动时回'
                'success=true 全零，靠 abduction 正控制探针识别；token 经 --token / '
                'TERMONLINE_TOKEN，不落盘）',
    },
    'cnki-dict': {
        'enabled': False,
        'note': 'CNKI 翻译助手 TLS 指纹反爬（curl/urllib 断连），待浏览器通道',
    },
}


def query_once(provider, term, timeout=30):
    data = provider['fetch'](term, timeout)
    hits, note = provider['parse'](data)
    return data, hits, note


def query_with_retry(provider, term, retries=(15, 30, 60), timeout=30):
    """退避重试；返回 (status, hits, note, raw, error)。

    ChannelSuspect（通道结构/权限异常）不重试、不记空命中：status='denied'。
    """
    note, err = '', None
    for attempt in range(1 + len(retries)):
        try:
            data, hits, note = query_once(provider, term, timeout)
            status = 'ok' if hits else 'empty'
            return status, hits, note, data, None
        except ChannelSuspect as exc:
            return 'denied', [], '', None, redact_secrets('%s: %s' % (type(exc).__name__, exc))
        except Exception as exc:  # urllib/JSON 各类失败统一退避
            err = redact_secrets('%s: %s' % (type(exc).__name__, exc))
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
                             'force': False, 'token': None})()
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
    if prov.get('probe'):
        try:
            total = prov['probe']()
        except Exception as exc:
            print('探针异常：%s: %s' % (type(exc).__name__, exc))
            return 1
        if not total:
            print('通道探针 0 命中（abduction 应有多库收录）：限流、token 失效或通道异常，'
                  '本批不写任何凭证；稍后重试')
            return 1
        print('探针 belief 命中 %d 条，通道正常' % total)
    stat = {'ok': 0, 'empty': 0, 'error': 0, 'skip': 0, 'denied': 0}
    for key, display in collect_terms(args):
        path = os.path.join(outdir, safe_key(key) + '.json')
        if os.path.exists(path) and not args.force:
            stat['skip'] += 1
            continue
        status, hits, note, raw, err = query_with_retry(prov, display)
        if status == 'denied':
            # 通道异常不落凭证：留一条“无收录”凭证会成假证据，且 --resume 会挡住重试
            stat['denied'] += 1
            print('[denied] %s → 不写凭证（%s）' % (display, err))
            continue
        record = {
            'key': key, 'term': display, 'provider': args.provider,
            'queried_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'status': status, 'note': redact_secrets(note), 'hits': hits,
            'error': redact_secrets(err),
            'raw': None if raw is None else redact_secrets(json.dumps(raw, ensure_ascii=False))[:50000],
        }
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(record, f, ensure_ascii=False, indent=1)
        os.replace(tmp, path)
        stat[status] += 1
        print('[%s] %s → %d hits%s' % (status, display, len(hits),
                                       ('（' + err + '）') if err else ''))
    print('查证完成：ok=%d empty=%d error=%d denied=%d skip=%d（provider=%s，凭证 %s）'
          % (stat['ok'], stat['empty'], stat['error'], stat['denied'],
             stat['skip'], args.provider, outdir))
    return 0


if __name__ == '__main__':
    sys.exit(main())

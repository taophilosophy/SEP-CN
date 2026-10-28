# -*- coding: utf-8 -*-
"""两登记册全量逐条审阅驱动器（specs/008-terminology-campaign US-3）。

用法:
  python tools/term_audit.py                        # 全量审阅，报告落 specs/008 results/
  python tools/term_audit.py --registry <路径> --queries <目录> --out <目录>  # 注入测试

对登记册/人名表每一行关联查证凭证（results/queries/<provider>/），四态判定：
  一致    现行译法与源译名有交集
  不一致  源有译名但与现行互斥（列建议，待裁定）
  查无    凭证齐但源库无收录（不作否定证据）
  未查证  无凭证（待 cnki_query 补跑）
另排查「依据」列维基来源（ADR-0012 禁令，标红）。
核验器只报告不修改；修正走裁定 → 登记册 Edit → check_terms 门禁。

退出码: 0 完成（无论四态分布）；2 参数错误。
"""
import io
import json
import os
import re
import sys
from datetime import date

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)  # 脚本直跑时保证 from tools import 可用
QUERIES = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                       'queries')
OUT = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results')
REGISTRY = os.path.join(ROOT, 'yi-zhe-shuo-ming.md')
REGISTRY2 = os.path.join(ROOT, 'ren-ming-biao.md')


def _relevant(hit_en, term):
    """命中 EN 侧与查询词相关性（审定库 match=2 模糊匹配噪声过滤）。

    规则：查询词元（剥尾 s）须全部出现在命中 EN 侧；单词查询要求精确相等。
    变音符先 NFD 折叠（ADR-0013）：否则 Rāzī 会被 [a-z0-9] 碎裂成 r/z。
    """
    import unicodedata

    def toks(s):
        s = unicodedata.normalize('NFD', s or '')
        s = ''.join(ch for ch in s if not unicodedata.combining(ch))
        out = set()
        for w in re.findall(r'[a-z0-9]+', s.casefold()):
            out.add(w[:-1] if len(w) > 3 and w.endswith('s') else w)
        return out

    a, b = toks(hit_en), toks(term)
    if not a or not b:
        return False
    if len(b) == 1:
        return a == b
    return b <= a


def _relevant_any(hit_en, term):
    """归并行拆「/」变体逐个判相关性；无「/」退化为 _relevant。"""
    if '/' not in term:
        return _relevant(hit_en, term)
    return any(_relevant(hit_en, v.strip())
               for v in term.split('/') if v.strip())


def audit_rows(rows, label, queries_root):
    from tools import check_terms
    providers = sorted(d for d in os.listdir(queries_root)
                       if os.path.isdir(os.path.join(queries_root, d))) \
        if os.path.isdir(queries_root) else []
    out = []
    for term, trans, first_seen, basis, row_date, lineno in rows:
        key = check_terms.norm_key(term)
        row_out = {'table': label, 'line': lineno, 'term': term,
                   'trans': trans, 'basis': basis, 'status': '未查证',
                   'hits': [], 'providers': []}
        cred_stats = []
        for prov in providers:
            safe = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', '_', key)[:80].strip('_')
            path = os.path.join(queries_root, prov, safe + '.json')
            if not os.path.exists(path):
                continue
            try:
                rec = json.load(open(path, encoding='utf-8'))
            except (ValueError, OSError):
                continue
            row_out['providers'].append(prov)
            cred_stats.append(rec.get('status'))
            if rec.get('status') == 'ok':
                raw_hits = rec.get('hits', [])[:60]
                for h in raw_hits:
                    # en 缺省（有道等直接查词通道）视为相关；有 en 的按词元过滤；
                    # 归并行（「主形 / 他形」）逐变体判，任一变体相关即保留
                    if h.get('en') is not None and not _relevant_any(h.get('en'), term):
                        continue
                    row_out['hits'].append(
                        {'provider': prov, 'cn': h.get('cn'), 'en': h.get('en'),
                         'source': h.get('standard') or h.get('code')
                         or h.get('subject') or prov})
        if not row_out['providers']:
            row_out['status'] = '未查证'
        elif 'ok' in cred_stats and row_out['hits']:
            mine = check_terms.translations(trans)
            theirs = set()
            for h in row_out['hits']:
                theirs |= check_terms.translations(h.get('cn') or '')
            row_out['status'] = '一致' if (mine & theirs) else '不一致'
        else:
            row_out['status'] = '查无'
        if basis and '维基' in basis:
            row_out['wiki'] = True
        out.append(row_out)
    return out, providers


def write_report(results, providers, out_dir, today):
    os.makedirs(out_dir, exist_ok=True)
    counts = {}
    for r in results:
        counts[r['status']] = counts.get(r['status'], 0) + 1
    wiki_rows = [r for r in results if r.get('wiki')]
    mismatch = [r for r in results if r['status'] == '不一致']

    lines = ['# 术语战役审阅报告 %s' % today, '',
             '基线：术语/人名两登记册全量 %d 行；查证 provider：%s；四态 + 维基排查。' % (
                 len(results), '、'.join(providers) or '（无凭证）'), '',
             '## 汇总', '',
             '| 状态 | 行数 |', '| ---- | ---- |']
    for k in ('一致', '不一致', '查无', '未查证'):
        lines.append('| %s | %d |' % (k, counts.get(k, 0)))
    lines.append('| 维基来源（禁令排查） | %d |' % len(wiki_rows))
    lines += ['', '## 不一致明细（需裁定，只报告不修改）', '',
              '| 表 | 行 | 原文 | 现行译法 | 源译名（provider:cn） |', '| ---- | ---- | ---- | ---- | ---- |']
    for r in mismatch[:200]:
        theirs = '；'.join('%s:%s' % (h['provider'], h['cn'])
                           for h in r['hits'][:6])
        lines.append('| %s | %d | %s | %s | %s |'
                     % (r['table'], r['line'], r['term'], r['trans'], theirs))
    lines += ['', '## 维基来源排查（ADR-0012 禁令）', '']
    if wiki_rows:
        for r in wiki_rows:
            lines.append('* [%s 第 %d 行] %s —— 依据：%s' %
                         (r['table'], r['line'], r['term'], r['basis']))
    else:
        lines.append('未发现依据列含维基来源的行。')
    lines += ['', '## 查无（标准库未收录，不作否定证据）', '']
    none_rows = [r for r in results if r['status'] == '查无']
    if none_rows:
        lines.append('；'.join(r['term'] for r in none_rows))
    else:
        lines.append('无。')
    lines += ['', '## 未查证（待 cnki_query 补跑）', '']
    unv = [r for r in results if r['status'] == '未查证']
    if unv:
        lines.append('；'.join('[%s %d] %s' % (r['table'], r['line'], r['term'])
                               for r in unv[:300]))
    else:
        lines.append('无。')

    md = '\n'.join(lines) + '\n'
    md_path = os.path.join(out_dir, 'audit-%s.md' % today)
    js_path = os.path.join(out_dir, 'audit-%s.json' % today)
    for p, content in ((md_path, md), (js_path, json.dumps(
            {'date': today, 'providers': providers, 'counts': counts,
             'results': results}, ensure_ascii=False, indent=1))):
        tmp = p + '.tmp'
        with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        os.replace(tmp, p)
    return md_path, js_path, counts


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    reg1, reg2, queries, out = REGISTRY, REGISTRY2, QUERIES, OUT
    i = 0
    while i < len(argv):
        if argv[i] == '--registry':
            reg1, i = argv[i + 1], i + 1
        elif argv[i] == '--registry2':
            reg2, i = argv[i + 1], i + 1
        elif argv[i] == '--queries':
            queries, i = argv[i + 1], i + 1
        elif argv[i] == '--out':
            out, i = argv[i + 1], i + 1
        i += 1
    from tools import check_terms
    rows1, w1 = check_terms.parse_registry(reg1)
    rows2, w2 = check_terms.parse_registry(reg2)
    results, providers = [], []
    if rows1:
        r, p = audit_rows(rows1, '术语', queries)
        results += r
        providers = p
    if rows2:
        r, p = audit_rows(rows2, '人名', queries)
        results += r
        providers = p or providers
    today = date.today().isoformat()
    md_path, js_path, counts = write_report(results, providers, out, today)
    print('审阅 %d 行（术语 %d + 人名 %d）| providers: %s' %
          (len(results), len(rows1), len(rows2), '、'.join(providers) or '无'))
    print('四态：%s | 维基排查：%d' % (
        ' '.join('%s=%d' % (k, v) for k, v in sorted(counts.items())),
        sum(1 for r in results if r.get('wiki'))))
    print('报告：%s' % md_path)
    return 0


if __name__ == '__main__':
    sys.exit(main())

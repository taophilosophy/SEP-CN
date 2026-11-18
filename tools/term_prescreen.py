# -*- coding: utf-8 -*-
"""候选池自动预筛（specs/046 治标）：对 term-pool.json 的 new 候选逐条判非术语，
确定性/高置信残渣与泛词标 rejected:自动预筛-<类>，把待人工裁定量压到可裁量级。

口径（2026-11-18 用户「标本兼治，不计成本」批准）：
  * 只处理 status=startswith('new') 的候选，绝不动 published/held/rejected 既有裁定账。
  * type=person 一律跳过（人名走人名表 workflow，不属术语预筛）。
  * 分类全部落在「确定性残渣」与「保守泛词表」两类，每类可凭 manifest 复核撤销。
  * 复用 tools/term_harvest.py 的同一套守卫常量（单一事实源，防漂移）。

用法:
  python tools/term_prescreen.py --dry-run           # 只报告，不改文件
  python tools/term_prescreen.py                     # 实写：标 rejected + 落 manifest
  python tools/term_prescreen.py --pool <路径> --out <目录>   # 注入测试
退出码: 0 完成；2 参数/路径错误。
"""
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools import term_harvest as th  # noqa: E402

POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')
OUT = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results')


def classify(en, typ):
    """返回 (类别, 理由) 或 (None, '')。

    确定性残渣（latex/书目/重复/出版社/cjk虚词/句子级/结构标题）单独打标签；
    其余一律交给 term_harvest.termhood_ok（单一事实源）判，False 即「泛词」。
    """
    toks = th.WORD_RE.findall(en)
    low = [w.casefold() for w in toks]
    # ⓪ 数学/LaTeX 残渣
    if '\\' in en or (set(low) & th.MATH_TOKENS):
        return '残渣:latex', '数学/LaTeX 命令残留'
    # 书目缩写残片
    if th.BIB_RE.search(en):
        return '残渣:书目', '书目缩写（b./p./ed. 等）'
    # 重复残片（同一词元 ≥3 次）
    if toks and max(Counter(low).values()) >= 3:
        return '残渣:重复', '同一词元重复 ≥3 次（解析残片）'
    # 出版社/城市残片
    if len(toks) >= 2 and any(t in th.PUB_BAD for t in low):
        return '残渣:出版社', '含出版社/城市名（书目残片）'
    # cjk 虚词 / 句子级串
    if typ == 'cjk':
        s = en.strip()
        han = [ch for ch in s if '\u4e00' <= ch <= '\u9fff'
               or '\u3400' <= ch <= '\u4dbf']
        if (len(s) == 1 and s in th.CJK_FUNC):
            return '残渣:cjk虚词', '单字古汉语虚词'
        if len(han) >= 2 and all(ch in th.CJK_FUNC for ch in han):
            return '残渣:cjk虚词', '纯虚词/常用字串'
        if len(s) > 8:
            return '残渣:句子级', '汉字串 >8 字（句子级）'
    # 结构标题
    if typ == 'topic' and th.STRUCT_HEAD.match(en.strip()):
        return '残渣:结构标题', '结构标题（Introduction/Appendix 等）'
    # 语义层：交给 termhood_ok（子句片段/连字符残片/单字泛词/搭配/标题复合）
    if not th.termhood_ok(en, typ):
        # 细分标签，便于复核
        for t in toks:
            b = t.casefold().replace('\u2019', "'").replace('\u2018', "'")
            if b in th.CLAUSE_TOKENS:
                return '泛词:子句片段', '含系动词/助动词/报道动词（句子片段）'
        if any(t.endswith('-') and len(t.strip('-')) >= 3 for t in toks):
            return '残渣:连字符', '连字符截断残片'
        if any(v >= 2 and len(k) >= 3
               for k, v in Counter(t.strip('-').casefold()
                                   for t in toks).items()):
            return '残渣:重复', '词干重复残片'
        if typ == 'topic':
            return '泛词:标题', '标题/节名（结构词/连词/超长/supplement）'
        if typ == 'foreign' and (any(w in th.CLOSING_WORDS for w in low)
                                 or (any(ord(ch) > 127 for ch in en)
                                     and any(re.fullmatch(r"[a-z][a-z'\-]*", t)
                                             for t in toks))):
            return '残渣:外语残片', '英语普通词 + 原文混排（解析残片）'
        if typ in ('quoted', 'italic', 'foreign') and len(toks) == 1:
            return '泛词:单字', '单字普通英语词'
        if typ == 'phrase':
            return '泛词:搭配', '通用搭配/全普通词'
        return '泛词:其他', '术语性不足'
    return None, ''


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    pool_path, out_dir, dry = POOL, OUT, False
    i = 0
    while i < len(argv):
        if argv[i] == '--pool':
            pool_path, i = argv[i + 1], i + 1
        elif argv[i] == '--out':
            out_dir, i = argv[i + 1], i + 1
        elif argv[i] == '--dry-run':
            dry = True
        i += 1
    if not os.path.exists(pool_path):
        print('候选池缺失: %s' % pool_path)
        return 2

    pool = json.load(open(pool_path, encoding='utf-8'))
    cands = pool.get('candidates', [])
    counts = Counter()
    samples = defaultdict(list)
    touched = 0
    for c in cands:
        if not str(c.get('status', '')).startswith('new'):
            continue
        typ = c.get('type', '')
        if typ == 'person':
            counts['跳过:person'] += 1
            continue
        en = c.get('en', '')
        cat, reason = classify(en, typ)
        if not cat:
            counts['保留:术语候选'] += 1
            continue
        counts[cat] += 1
        if len(samples[cat]) < 30:
            samples[cat].append(en)
        if not dry:
            c['status'] = 'rejected:自动预筛-' + cat
            c['note'] = (c.get('note', '') + ' | ' if c.get('note') else '') \
                + '自动预筛 ' + reason + '（specs/046，可凭 manifest 撤销）'
            touched += 1

    total = sum(v for k, v in counts.items() if not k.startswith('跳过'))
    noise = sum(v for k, v in counts.items()
                if k.startswith('残渣') or k.startswith('泛词'))
    print('=== 自动预筛（%s）===' % ('dry-run 未改文件' if dry else '已实写'))
    for k in sorted(counts, key=lambda x: (-counts[x], x)):
        print('  %-18s: %d' % (k, counts[k]))
    print('  ---')
    print('  处理合计: %d | 判噪声: %d (%.1f%%) | 保留: %d'
          % (total, noise, 100.0 * noise / total if total else 0,
             counts['保留:术语候选']))

    manifest = {'date': __import__('datetime').date.today().isoformat(),
                'script': 'tools/term_prescreen.py',
                'pool': os.path.relpath(pool_path, ROOT),
                'dry_run': dry, 'touched': touched,
                'counts': dict(counts),
                'samples': {k: v for k, v in samples.items()}}
    if not dry:
        os.makedirs(out_dir, exist_ok=True)
        mpath = os.path.join(out_dir, 'prescreen-%s.json' % manifest['date'])
        tmp = mpath + '.tmp'
        with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=1)
        os.replace(tmp, mpath)
        # 原子写回候选池
        tmp2 = pool_path + '.tmp'
        with open(tmp2, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(pool, f, ensure_ascii=False, indent=1)
        os.replace(tmp2, pool_path)
        print('  manifest → %s' % mpath)
        print('  已写回候选池：%d 条置 rejected:自动预筛-*' % touched)
    return 0


if __name__ == '__main__':
    sys.exit(main())

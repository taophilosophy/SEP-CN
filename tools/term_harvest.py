# -*- coding: utf-8 -*-
"""逐篇遍历 yuanwen/ 全库提取术语/人名候选（specs/008-terminology-campaign US-1）。

用法:
  python tools/term_harvest.py                # 全库遍历（按字母分批缓存，可中断续跑）
  python tools/term_harvest.py --letter a     # 只跑一个字母批次
  python tools/term_harvest.py --refresh      # 忽略缓存重提

五路提取（term-candidates.json 先例方法扩展全库）:
  ①斜体术语 *...* ②引语术语 “...” ③-ism 词族 ④高频概念短语（二元/三元，去停用词）
  ⑤人名序列（大写二元组，type=person 供裁定）
与两登记册 + 词汇表 + 候选池已登记键求差后入池。幂等：单篇提取结果缓存于
specs/008-terminology-campaign/results/harvest-cache/，重跑只增量解析新文件。

退出码: 0 成功；2 参数/路径错误。
"""
import io
import json
import os
import re
import sys
from collections import Counter

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)  # 脚本直跑时保证 from tools import 可用
CORPUS = os.path.join(ROOT, 'yuanwen')
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')
CACHE = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                     'harvest-cache')
REGISTRY = os.path.join(ROOT, 'yi-zhe-shuo-ming.md')
REGISTRY2 = os.path.join(ROOT, 'ren-ming-biao.md')
LEGACY_POOL = os.path.join(ROOT, 'tasks', 'term-candidates.json')

STOPWORDS = set('''the a an and or of to in on for with as by at from is are was
were be been being that this these those it its their his her our your not no
nor but if then than so such can could may might must shall should will would
do does did done have has had having we they he she i you one two three first
second new other more most same own only very just also into over under about
between among through during before after above below up down out off again
further once all any both each few some what which who whom when where why how
there here whose which while because until against although though yet both
either neither whether rather quite even ever never always often sometimes
stanford encyclopedia philosophy press stanfordedu entry preview pdf version
substantive revision original publication academic tools friends pdfs Sep
sep society look references key doi isbn issn eds ed trans pp vol cited
available online internet philosophy ontology project inpho enhanced
bibliography google scholar crossref wikipedia wikimedia url http https www
edu archives acprof oso doi langle rangle begin end align varnothing mathbb
vdash forall exists frac sqrt textbf subsection appendix preprint scholar
oxford cambridge routledge princeton chicago dordrecht kluwer springer brill
blackwell clarendon wiley elsevier hackett university press handbook companion
edition translated translation issn furthermore moreover however therefore
hence thus namely perhaps possibly importantly consider suppose see section
criticism criticisms mechanisms different ways kinds sorts thing things
united'''.split())

PHRASE_MIN_FREQ = 20   # 全库阈值；低频尾部留存 harvest-cache（本地），随词条翻译时核定
OTHER_MIN_FREQ = 2
MIN_FREQ = {'phrase': PHRASE_MIN_FREQ, 'ism': OTHER_MIN_FREQ,
            'italic': OTHER_MIN_FREQ, 'quoted': 3, 'person': 5, 'arabic': 2}
# 词元：拉丁字母含扩展区（变音符 Suhrawardî/Ṣadrā 与 ʿayn/hamza 首字符，ADR-0013）
UP = 'A-Z\u00C0-\u024F\u1E00-\u1EFF\u02BE\u02BF'
LO = 'a-z\u00DF-\u024F\u1E00-\u1EFF\u02BE\u02BF'
WORD_RE = re.compile(r'[' + UP + LO + r'][' + UP + LO + r'\u2018\u2019\'\-]+')
QUOTED_RE = re.compile(r'\u201c([^\u201c\u201d]{2,80})\u201d')
ITALIC_RE = re.compile(r'\*([^*\n]{2,80})\*')
ISM_RE = re.compile(r'\b([A-Za-z][A-Za-z\'\-]{4,}isms?)\b', re.I)
ISM_STOP = {'organism', 'organisms', 'criticism', 'criticisms', 'mechanisms',
            'mechanism', 'syllogism', 'syllogisms', 'witticism', 'witticisms',
            'anachronism', 'anachronisms', 'neologism', 'neologisms',
            'paradoxism'}  # 假词干/泛词（term-candidates pool_sweep 先例扩展）
CAP_PAIR_RE = re.compile(
    r'\b([' + UP + r'][^\W\d_]{2,})\s+([' + UP + r'][^\W\d_]{2,})\b')
# 阿位专名路由（ADR-0013）：含定冠词同化形/谱系词/尊称的专名序列
ARAB_PART = (r'(?:[' + UP + r'][^\W\d_]*(?:-[^\W\d_]+)*|'  # 含 Al-Fârâbî 型连字符词
             r'(?:al|ad|as|at|an|ar|az|adh)-[^\W\d_]*|'
             r'ibn|bin|b\.(?=\s)|abu|ab\u016B|abd|umm|dhu|dh\u016B)')
ARAB_NAME_RE = re.compile(
    r'\b(?:' + ARAB_PART + r')(?:[\s\u2019](?:' + ARAB_PART + r'))+\b')
ARAB_PARTICLES = re.compile(
    r'^(?:(?:al|ad|as|at|an|ar|az|adh)-|ibn|bin|b\.|abu|abū|abd|umm|dhu|dhū)',
    re.I)


def norm_key(text):
    """候选键：剥斜体与空白、变音符折叠、casefold（ADR-0013 同人归并）。"""
    import unicodedata
    s = unicodedata.normalize('NFD', text.replace('*', '').strip())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).casefold()


def clean_phrase(text):
    """候选清洗：剥书名/引用杂质，仅留字母短语。"""
    text = text.strip().strip('.,;:!?')
    if not text or any(ch in text for ch in '=<>()[]{}$\\|/数字'):
        return ''
    words = WORD_RE.findall(text)
    if not (1 <= len(words) <= 4):
        return ''
    low = [w.casefold() for w in words]
    if any(w in STOPWORDS for w in low) and len(low) > 1 and low[0] in STOPWORDS:
        return ''
    if all(w in STOPWORDS for w in low):
        return ''
    if any(len(w) < 2 for w in low):
        return ''
    return ' '.join(words)


def extract_slug(path):
    """单篇五路提取 → Counter(键 → 频次) 与原始形、类型映射。"""
    text = open(path, encoding='utf-8').read()
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)  # 代码块剔除
    # 尾部站点节裁剪：参考文献/学术工具/相关条目（书目作者对与导航噪声主源）
    text = re.split(r'\n## (?:References|Bibliography|Academic Tools|'
                    r'Other Internet Resources|Related Entries)[^\n]*\n',
                    text)[0]
    body = '\n'.join(l for l in text.split('\n')
                     if not l.startswith(('#', '>', '|', '!')))
    counter = Counter()
    forms, types = {}, {}

    def add(raw, typ):
        key = norm_key(raw)
        if not key or len(key) > 60:
            return
        counter[key] += 1
        forms.setdefault(key, raw.strip())
        prev = types.get(key)
        if 'arabic' in (prev, typ):
            types[key] = 'arabic'  # ADR-0013：阿位专名优先标注
        elif prev != typ:
            types[key] = 'person' if 'person' in (prev, typ) else (prev or typ)

    for m in ITALIC_RE.finditer(body):
        c = clean_phrase(m.group(1))
        if c and not re.match(r'^(19|20)\d\d', c):
            add(c, 'italic')
    for m in QUOTED_RE.finditer(body):
        c = clean_phrase(m.group(1))
        if c:
            add(c, 'quoted')
    for m in ISM_RE.finditer(body):
        if m.group(1).casefold() not in ISM_STOP:
            add(m.group(1), 'ism')
    for m in CAP_PAIR_RE.finditer(body):
        pair = '%s %s' % (m.group(1), m.group(2))
        if m.group(1).casefold() not in STOPWORDS:
            add(pair, 'person')
    # 阿位专名（ADR-0013）：序列内含定冠词/谱系词/尊称颗粒才算
    for m in ARAB_NAME_RE.finditer(body):
        seq = m.group(0).strip()
        toks = seq.replace('\u2019', ' ').split()
        if any(ARAB_PARTICLES.match(t) for t in toks):
            add(seq, 'arabic')
    # 概念短语：段落词序列滑窗（停用词断窗）
    for para in body.split('\n'):
        words = WORD_RE.findall(para)
        low = [w.casefold() for w in words]
        n = len(words)
        for i in range(n):
            if low[i] in STOPWORDS or len(words[i]) < 3:
                continue
            for j in (i + 1, i + 2):
                if j >= n or low[j] in STOPWORDS or len(words[j]) < 3:
                    break
                add(' '.join(words[i:j + 1]), 'phrase')
    return counter, forms, types


def load_registered_keys():
    """已登记键：两登记册 + 词汇表 + 旧候选池 + 新候选池。"""
    from tools import check_terms
    keys = set()
    for path in (REGISTRY, REGISTRY2):
        rows, _ = check_terms.parse_registry(path)
        for row in rows:
            keys.add(check_terms.norm_key(row[0]))
            # 归并行变体拆分（ADR-0013：「主形 / 他形」逐变体作键）
            for part in re.split(r'\s*/\s*', row[0]):
                if part.strip():
                    keys.add(check_terms.norm_key(part))
    glos_rows, _ = check_terms.parse_glossary(
        os.path.join(ROOT, 'qian-yan', 'ci-hui-biao.md'))
    for row in glos_rows:
        keys.add(check_terms.norm_key(row[0]))
    for pool_path in (LEGACY_POOL, POOL):
        if os.path.exists(pool_path):
            try:
                data = json.load(open(pool_path, encoding='utf-8'))
                for c in data.get('candidates', []):
                    for part in re.split(r'\s*/\s*', c.get('en', '')):
                        if part.strip():
                            keys.add(norm_key(part))
            except (ValueError, OSError):
                pass
    return keys


def iter_corpus(corpus, letter):
    for dirpath, _dirs, files in os.walk(corpus):
        for fn in sorted(files):
            if not fn.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), corpus)
            top = rel.split(os.sep)[0]
            if top.upper() == 'ASSETS' or top == 'SUMMARY.md':
                continue
            if letter and top.casefold() != letter.casefold():
                continue
            yield rel, os.path.join(dirpath, fn)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    letter, refresh = None, False
    corpus, pool_path, cache = CORPUS, POOL, CACHE
    i = 0
    while i < len(argv):
        if argv[i] == '--letter':
            letter, i = argv[i + 1], i + 1
        elif argv[i] == '--refresh':
            refresh = True
        elif argv[i] == '--corpus':
            corpus, i = argv[i + 1], i + 1
        elif argv[i] == '--pool':
            pool_path, i = argv[i + 1], i + 1
        elif argv[i] == '--cache':
            cache, i = argv[i + 1], i + 1
        i += 1
    if not os.path.isdir(corpus):
        print('语料目录缺失: %s' % corpus)
        return 2

    registered = load_registered_keys()
    pool = {'meta': {}, 'candidates': []}
    if os.path.exists(pool_path):
        try:
            pool = json.load(open(pool_path, encoding='utf-8'))
        except ValueError:
            pass
    known = {norm_key(c['en']): c for c in pool.get('candidates', [])
             if '/' not in c.get('en', '')}

    os.makedirs(cache, exist_ok=True)
    total, new_hits = 0, 0
    per_run = Counter()
    run_types, run_forms = {}, {}
    run_sources = {}
    for rel, path in iter_corpus(corpus, letter):
        slug = rel[:-3].replace(os.sep, '.')
        cache_path = os.path.join(cache, slug + '.json')
        if refresh or not os.path.exists(cache_path):
            counter, forms, types = extract_slug(path)
            data = {'counts': dict(counter), 'forms': forms, 'types': types}
            tmp = cache_path + '.tmp'
            with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, ensure_ascii=False, sort_keys=True)
            os.replace(tmp, cache_path)
        else:
            data = json.load(open(cache_path, encoding='utf-8'))
            counter = Counter(data.get('counts', {}))
            forms, types = data.get('forms', {}), data.get('types', {})
        total += 1
        stem = rel[:-3]
        for key, freq in counter.items():
            per_run[key] += freq
            run_types.setdefault(key, types.get(key, 'phrase'))
            run_forms.setdefault(key, forms.get(key, key))
            run_sources.setdefault(key, []).append(stem)

    fresh = []
    for key, freq in per_run.items():
        if key in registered:
            continue
        typ = run_types.get(key, 'phrase')
        min_freq = MIN_FREQ.get(typ, OTHER_MIN_FREQ)
        if freq < min_freq:
            continue
        entry = known.get(key)
        if entry is None:
            entry = {'en': run_forms.get(key, key), 'freq': freq, 'type': typ,
                     'suggest': '', 'status': 'new', 'sources': []}
            known[key] = entry
            new_hits += 1
        # entry 为旧池对象时 status/suggest/note 字段自动沿用
        entry['freq'] = max(entry.get('freq', 0), freq) if letter else freq
        entry['type'] = typ
        entry['en'] = run_forms.get(key, entry.get('en', key))
        if letter:  # 字母批次增量：来源并集；全量跑以本轮为权威
            entry['sources'] = sorted(set(entry.get('sources', []))
                                      | set(run_sources.get(key, [])))
        else:
            entry['sources'] = run_sources.get(key, [])
        fresh.append(entry)
    if letter:
        # 字母批次：保留池中未被本轮触达的既有条目
        seen = {id(e) for e in fresh}
        fresh.extend(c for c in pool.get('candidates', []) if id(c) not in seen)
    pool['candidates'] = fresh

    pool['candidates'].sort(key=lambda c: -c.get('freq', 0))
    pool['meta'] = {
        'generated_at': __import__('datetime').date.today().isoformat(),
        'script': 'tools/term_harvest.py',
        'corpus': 'yuanwen/ 全库镜像',
        'scope': letter or 'all',
        'files_processed': total,
        'candidates': len(pool['candidates']),
        'new_this_run': new_hits,
        'method': '六路提取：斜体/引语/-ism/高频短语/人名序列/阿位专名（ADR-0013，变音符折叠键）；'
                  '与两登记册+词汇表+候选池求差；'
                  '按型阈值 phrase=%d ism/italic/arabic=%d quoted=3 person=5；'
                  '低频尾部留存单篇缓存（results/harvest-cache/，本地）；' % (
                      PHRASE_MIN_FREQ, OTHER_MIN_FREQ),
        'usage': 'status 状态机沿用 term-candidates.json：new→published@日期|held:理由|rejected:理由',
    }
    tmp = pool_path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(pool, f, ensure_ascii=False, indent=1, sort_keys=False)
    os.replace(tmp, pool_path)
    print('语料 %d 件（范围 %s）| 候选池 %d 条（新增 %d）→ %s'
          % (total, letter or 'all', len(pool['candidates']), new_hits, pool_path))
    return 0


if __name__ == '__main__':
    sys.exit(main())

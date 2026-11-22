# -*- coding: utf-8 -*-
"""specs/058 第二轮全库术语提取：高精度分型 + 折叠键去重 + A–Z 总表。

用法:
  python specs/058-term-full-reextraction/bin/reextract.py            # 全库
  python specs/058-term-full-reextraction/bin/reextract.py --limit 20 # 试金石
  python specs/058-term-full-reextraction/bin/reextract.py --build-only  # 只重建总表

输入: yuanwen/<letter>/<slug>.md 全库；tasks/term-pool.json；两登记册。
输出:
  specs/058-term-full-reextraction/results/candidates.json   全量候选（含来源）
  specs/058-term-full-reextraction/results/az/<A-Z|#>.md      A–Z 总表
  specs/058-term-full-reextraction/results/summary.md         口径与计数

分型优先级: person > work > term > sentence > foreign > script > topic。
"""
import collections
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools import term_harvest as th  # noqa: E402
from tools.register_lib import (bucket_of, fold_nfd, norm_key,  # noqa: E402
                                norm_key_quote, parse_registry2_full,
                                parse_registry_full, person_path, term_path)

CORPUS = os.path.join(ROOT, 'yuanwen')
OUT = os.path.join(ROOT, 'specs', '058-term-full-reextraction', 'results')
AZ = os.path.join(OUT, 'az')
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')
FULL = os.path.join(ROOT, 'script', 'tmp', 'candidates-full.json')
CAND = os.path.join(OUT, 'candidates.json.gz')


def dump_json(doc, path):
    import gzip
    data = json.dumps(doc, ensure_ascii=False).encode('utf-8')
    if path.endswith('.gz'):
        with gzip.open(path, 'wb') as f:
            f.write(data)
    else:
        open(path, 'wb').write(data)


def load_json(path):
    import gzip
    if path.endswith('.gz'):
        with gzip.open(path, 'rb') as f:
            return json.loads(f.read().decode('utf-8'))
    return json.load(open(path, encoding='utf-8'))

# ---------------------------------------------------------------------------
# 人名：2–4 个首字母大写词元，允许 J. / van / de / ibn / al- 等颗粒。
# 题名式术语（Public Reason 等）靠上下文与尾词表排除。
# ---------------------------------------------------------------------------
CAP = r"[A-Z][a-z\u00C0-\u024F]*(?:['\u2019\-][A-Za-z\u00C0-\u024F]+)*"
INITIAL = r"[A-Z]\."
PART = r"(?:van|von|de|der|den|du|la|le|di|da|del|della|ibn|bin|bint|al|el|abu|abd|umm|st)"
NAME_RX = re.compile(
    r"\b((?:%s|%s)(?:\s+(?:%s\s+)?(?:%s|%s)){1,3})\b"
    % (INITIAL, CAP, PART, INITIAL, CAP))
PERSON_AFTER = re.compile(
    r"^\s*(?:\(?(?:c\.\s*)?\d{3,4}|"
    r"(?:argues?|argued|claims?|claimed|holds?|held|says?|said|writes?|wrote|"
    r"notes?|noted|suggests?|suggested|maintains?|maintained|observes?|observed|"
    r"proposes?|proposed|defends?|defended|objects?|objected|replies?|replied|"
    r"contends?|contended|thinks?|thought|believes?|believed|points? out|"
    r"concludes?|concluded|explains?|explained|shows?|showed|distinguishes?|"
    r"identifies?|identified|describes?|described|characteri[sz]es?|"
    r"defines?|defined|offers?|offered|develops?|developed|introduces?|"
    r"introduced|rejects?|rejected|accepts?|accepted|denies?|denied|insists?|"
    r"remarks?|remarked|asks?|asked|wonders?|wondered|urges?|urged|"
    r"recommends?|recommended|warns?|warned|adds?|added|continues?|continued|"
    r"states?|stated|reports?|reported|agrees?|agreed|admits?|admitted|"
    r"concedes?|conceded|criticizes?|criticized|reconstructs?)\b)")
PERSON_BEFORE = re.compile(r"(?:according to|as\s+|by|with|against)\s*$")
TERM_HEAD = set('''logic ethics theory theories reason reasons rights science
sciences experience philosophy ontology epistemology metaphysics politics law
language mind truth knowledge belief beliefs justice freedom liberty action
agency perception consciousness causation necessity possibility reality world
nature values morality virtue happiness beauty emotion emotions will power state
society history meaning reference semantics mathematics physics biology
economics principles principle problem problems argument arguments view views
thesis hypothesis paradox fallacy model models structure structures system
systems approach approaches analysis method methods concept concepts idea ideas
notion notions claim claims question questions answer answers debate debates
critique defense defence response responses objection objections interpretation
interpretations reading readings account accounts perspective perspectives
framework frameworks'''.split())
LEAD_BAD = set('''the this that these those a an in on for with from by as at if
when where why how what which who whom whose it its his her their our your my no
not all some any both each every such other another most many few several one two
three first second third new old good bad great modern contemporary classical
ancient early late analytic continental western eastern moral political social
natural human physical mental rational empirical transcendental pure practical
theoretical general special formal material public private common civil legal
economic historical philosophical scientific religious christian jewish islamic
greek roman indian chinese japanese german french british american european'''.split())
KNOWN_WORKS = {'principia', 'tractatus', 'phaedo', 'republic', 'timaeus',
               'organon', 'meditations', 'confessions', 'phenomenology',
               'groundwork', 'prolegomena', 'monadology', 'theodicy'}
WORK_TAIL_OK = {'ethics', 'politics', 'metaphysics', 'republic', 'laws', 'logic',
                'physics', 'poetics', 'rhetoric', 'confessions', 'meditations',
                'phenomenology', 'dialectic', 'enquiry', 'essay', 'treatise',
                'principia', 'tractatus', 'discourse', 'groundwork'}
# 斜体/引语路线的高频噪声（书目与图表标记、拉丁缩写残片）
NOISE_TERM = {'et al', 'et alia', 'ibid', 'idem', 'passim', 'cf', 'viz', 'ie',
              'eg', 'figure', 'figures', 'fig', 'figs', 'table', 'tables',
              'note', 'notes', 'chapter', 'chapters', 'section', 'sections',
              'volume', 'volumes', 'ibidem', 'infra', 'supra', 'priori',
              'posteriori', 'op cit', 'loc cit', 'ms', 'mss', 'trans', 'ed',
              'eds', 'pp', 'p', 'see', 'see also', 'contra', 'versus'}
# 机构/题名尾词：出现即不是人名（Oxford University Press、Vienna Circle 类）
ORG_WORDS = {'university', 'universities', 'press', 'institute', 'institution',
             'society', 'association', 'academy', 'college', 'school', 'circle',
             'center', 'centre', 'department', 'foundation', 'review', 'journal',
             'quarterly', 'studies', 'conference', 'congress', 'committee',
             'council', 'union', 'party', 'church', 'museum', 'library',
             'publishing', 'publications', 'books', 'editions', 'series'}
# 地名/民族形容词起首：不是人名（Latin American、Chinese Philosophy 类）
DEMONYM = {'latin', 'american', 'european', 'african', 'asian', 'chinese',
           'indian', 'greek', 'roman', 'german', 'french', 'british', 'italian',
           'spanish', 'russian', 'japanese', 'korean', 'arabic', 'islamic',
           'jewish', 'christian', 'muslim', 'hindu', 'buddhist', 'medieval',
           'ancient', 'modern', 'contemporary', 'analytic', 'continental',
           'western', 'eastern', 'oxford', 'cambridge', 'harvard', 'yale',
           'princeton', 'berkeley', 'chicago', 'vienna', 'frankfurt', 'kyoto'}
TYPE_PRIORITY = ['person', 'work', 'term', 'sentence', 'foreign', 'topic',
                 'arabic', 'greek', 'hebrew', 'cyrillic', 'devanagari', 'cjk']
NONPERSON_TAIL = TERM_HEAD | {'test', 'machine', 'experiment', 'theorem',
                              'lemma', 'proof', 'circle', 'school', 'movement',
                              'tradition', 'debate', 'controversy', 'question',
                              'answer', 'principle', 'hypothesis', 'theory',
                              'model', 'problem', 'paradox', 'argument',
                              'monism', 'dualism', 'pluralism', 'realism',
                              'idealism', 'empiricism', 'rationalism'}


def pri(t):
    return TYPE_PRIORITY.index(t) if t in TYPE_PRIORITY else 99


def is_work(raw):
    words = re.findall(r"[A-Za-z][\w'\u2019\-]*", raw)
    if not words:
        return False
    caps = sum(1 for w in words if w[0].isupper())
    if len(words) == 1:
        return words[0].casefold() in KNOWN_WORKS
    if caps < 2:
        return False
    if len(words) >= 3 and caps >= max(2, int(len(words) * 0.6)):
        return True
    if ':' in raw and caps >= 2:
        return True
    return words[-1].casefold() in WORK_TAIL_OK


def clean_person(seq):
    toks = seq.split()
    if toks and re.search(r"['\u2019]s$", toks[-1]):
        toks[-1] = re.sub(r"['\u2019]s$", '', toks[-1])
    while toks and toks[0].casefold() in LEAD_BAD:
        toks.pop(0)
    while toks and (toks[-1].casefold() in NONPERSON_TAIL
                    or toks[-1].casefold() in ORG_WORDS
                    or toks[-1].casefold() in DEMONYM
                    or toks[-1].casefold() in PART.split('|')):
        toks.pop()
    if len(toks) < 2 or len(toks) > 4:
        return ''
    if any(t.casefold() in ORG_WORDS for t in toks):
        return ''
    if toks[0].casefold() in DEMONYM:
        return ''
    if all(t.casefold() in NONPERSON_TAIL for t in toks):
        return ''
    if toks[-1].endswith(('ism', 'isms')):
        return ''
    # 二元"人名"末词为抽象名词后缀者多为术语（Abelard’s Solutions 类）
    if len(toks) == 2 and th.RE_TERM_SUFFIX.search(toks[-1]) \
            and toks[-1][0].islower():
        return ''
    if sum(1 for t in toks if len(t.rstrip('.')) >= 2) < 1:
        return ''
    return ' '.join(toks)


def person_ok(seq, body, start, end):
    after = body[end:end + 90]
    before = body[max(0, start - 30):start]
    toks = seq.split()
    if PERSON_AFTER.match(after) or PERSON_BEFORE.search(before):
        return True
    if any(th.ARAB_PARTICLES.match(t) for t in toks):
        return True
    if len(toks) >= 3 and not any(t.casefold() in TERM_HEAD for t in toks[1:]):
        return True
    return False


def is_sentence(raw):
    words = raw.split()
    if len(raw) > 80 and len(words) >= 5:
        return True
    if len(words) >= 6 and re.search(r'\b(?:is|are|was|were|means|refers|ought|'
                                     r'must|shall|should)\b', raw):
        return True
    return False


def clean_sentence(text):
    """句级长词条清洗：保留完整句，不做 4 词上限；拒收表格/LaTeX 残渣。"""
    t = re.sub(r'\s+', ' ', text).strip().strip('.,;:!?')
    t = t.lstrip('\u2026\u2025—–- ')
    if not (2 <= len(t) <= 300):
        return ''
    if any(ch in t for ch in '|\\{}*=<>' ):
        return ''
    if re.match(r'^\(\d+\)', t):
        return ''
    if len(t.split()) < 2:
        return ''
    return t


def load_registered():
    terms = set()
    rows, _ = parse_registry_full(term_path())
    for r in rows:
        terms.add(norm_key_quote(r[0]))
    persons = set()
    PARTS = {'van', 'von', 'de', 'der', 'den', 'du', 'la', 'le', 'di', 'da',
             'del', 'della', 'ibn', 'bin', 'bint', 'al', 'el', 'abu', 'abd'}
    HONOR = {'lady', 'sir', 'saint', 'st', 'pope', 'princess', 'king',
             'queen', 'emperor', 'cardinal', 'bishop', 'father'}
    rows2, _ = parse_registry2_full(person_path())
    for r in rows2:
        key = norm_key_quote(r[0])
        persons.add(key)
        for p in key.split('/'):
            p = p.strip()
            persons.add(p)
            toks = p.split()
            clean = [t for t in toks if t not in HONOR]
            if clean and clean != toks:
                persons.add(' '.join(clean))
                toks = clean
            if len(toks) >= 2:
                persons.add('%s %s' % (toks[-1], ' '.join(toks[:-1])))
                persons.add('%s, %s' % (toks[-1], ' '.join(toks[:-1])))
            for i, t in enumerate(toks):
                if t in PARTS and i > 0:
                    persons.add(' '.join(toks[i:]))
            if ',' in p:
                last, first = [x.strip() for x in p.split(',', 1)]
                persons.add('%s %s' % (first, last))
                persons.add(last)
    return terms, persons


def load_pool_status():
    d = json.load(open(POOL, encoding='utf-8'))
    out = {}
    for c in d['candidates']:
        k = norm_key(c.get('en', ''))
        out[k] = c.get('status', 'new')
        out.setdefault(norm_key_quote(c.get('en', '')), c.get('status', 'new'))
    return out


def status_of(c, terms, persons, pool):
    if c['type'] == 'person':
        return ('已登记（人名表）' if c['key'] in persons else
                ('池:' + pool[c['key']] if c['key'] in pool else '本轮新增'))
    if c['key'] in terms:
        return '已登记（术语表）'
    st = pool.get(c['key']) or pool.get(norm_key(c['en']))
    return '池:' + st if st else '本轮新增'


def corpus_files(limit=None):
    files = sorted(glob.glob(os.path.join(CORPUS, '*', '*.md')))
    if limit:
        files = files[:limit]
    return files


def scan_file(path):
    """返回 Counter(key -> freq), forms, types, hits[(key, raw, typ)] 与句级长词条。"""
    text = io.open(path, encoding='utf-8').read()
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)
    text = re.sub(r'\$\$.*?\$\$', ' ', text, flags=re.S)
    text = re.sub(r'\$[^$\n]*\$', ' ', text)
    text = re.sub(r'\\\(.*?\\\)', ' ', text, flags=re.S)
    text = re.sub(r'\\\[.*?\\\]', ' ', text, flags=re.S)
    text = re.split(r'\n## (?:References|Bibliography|Academic Tools|'
                    r'Other Internet Resources|Related Entries)[^\n]*\n', text)[0]
    body = '\n'.join(l for l in text.split('\n')
                     if not l.startswith(('#', '>', '|', '!')))
    out = collections.Counter()
    forms, types = {}, {}
    slug = os.path.splitext(os.path.basename(path))[0]
    letter = os.path.basename(os.path.dirname(path))

    def add(raw, typ):
        raw = raw.strip().strip('.,;:')
        key = norm_key_quote(raw)
        if not key or len(key) > 300:
            return
        if typ in ('italic', 'quoted', 'phrase'):
            if th.NONASCII_LATIN.search(raw) or th.GERMAN_SUFFIX_RE.search(raw) \
                    or key in th.FOREIGN_LEXICON:
                typ = 'foreign'
        # 全大写短缩略（ABD/SEP 类）不是术语候选；保留 2–5 位、含元音者以防 KD/MP 等例外
        if re.fullmatch(r'[A-Z]{2,5}', raw) and not re.search(r'[AEIOU]', raw):
            return
        if key in NOISE_TERM:
            return
        if typ not in ('person', 'sentence', 'work') and not th.termhood_ok(raw, typ):
            return
        out[key] += 1
        prev = types.get(key)
        if prev is None or pri(typ) < pri(prev):
            forms[key] = raw
        if prev is None:
            types[key] = typ
        elif prev != typ:
            types[key] = typ if pri(typ) < pri(prev) else prev

    for m in th.ITALIC_RE.finditer(body):
        c = th.clean_phrase(m.group(1))
        if not c or re.match(r'^(19|20)\d\d', c):
            continue
        add(c, 'work' if is_work(c) else 'term')
    for m in re.finditer(r'\u201c([^\u201c\u201d]{2,300})\u201d', body):
        raw = m.group(1)
        c = clean_sentence(raw)
        if not c:
            continue
        if len(c.split()) <= 4 and '(' not in c and '=' not in c:
            cp = th.clean_phrase(c)
            if cp:
                add(cp, 'term')
                continue
        add(c, 'sentence')
    for m in th.ISM_RE.finditer(body):
        if m.group(1).casefold() not in th.ISM_STOP:
            add(m.group(1), 'term')
    for m in NAME_RX.finditer(body):
        seq = clean_person(m.group(1))
        if seq and person_ok(seq, body, m.start(1), m.start(1) + len(m.group(1))):
            add(seq, 'person')
    for m in th.ARAB_NAME_RE.finditer(body):
        seq = m.group(0).strip()
        if any(th.ARAB_PARTICLES.match(t) for t in seq.replace('\u2019', ' ').split()):
            add(seq, 'arabic')
    for para in body.split('\n'):
        for sent in re.split(r'(?<=[.!?:\uff1b;])\s+', para):
            words = th.WORD_RE.findall(sent)
            low = [w.casefold() for w in words]
            n = len(words)
            for i in range(n):
                if low[i] in th.STOPWORDS or len(words[i]) < 3:
                    continue
                for j in (i + 1, i + 2):
                    if j >= n or low[j] in th.STOPWORDS or len(words[j]) < 3:
                        break
                    add(' '.join(words[i:j + 1]), 'phrase')
    for line in text.split('\n'):
        m = re.match(r'(#{1,2})\s+(.+?)\s*$', line)
        if not m:
            continue
        h = re.sub(r'^\d+(\.\d+)*\.?\s*', '', m.group(2))
        h = re.sub(r'\s*[(\[][^)\]]*[)\]]\s*$', '', h)
        for seg in re.split(r'[:：;；—–]', h):
            c = th.clean_topic(seg)
            if c and c.casefold() not in th.TOPIC_GENERIC:
                add(c, 'topic')
    for typ, rx in th.SCRIPT_ROUTES:
        for m in rx.finditer(body):
            seq = m.group(0).strip()
            if len(seq) < 2 and typ != 'cjk':
                continue
            add(seq, typ)
    return out, forms, types, slug, letter


def build():
    terms, persons = load_registered()
    pool = load_pool_status()
    agg = {}
    sources = collections.defaultdict(set)
    files = corpus_files(int(sys.argv[sys.argv.index('--limit') + 1])
                         if '--limit' in sys.argv else None)
    print('corpus files=%d' % len(files))
    for n, path in enumerate(files, 1):
        cnt, forms, types, slug, letter = scan_file(path)
        for key, freq in cnt.items():
            a = agg.get(key)
            if a is None:
                a = agg[key] = {'key': key, 'en': forms[key], 'freq': 0,
                                'type': types[key], 'types': {}, 'sources': []}
            a['freq'] += freq
            a['sources'].append('%s/%s' % (letter, slug))
            a['types'][types[key]] = a['types'].get(types[key], 0) + freq
        if n % 200 == 0:
            print('  %d/%d keys=%d' % (n, len(files), len(agg)), flush=True)

    cands = []
    for a in agg.values():
        typ = max(a['types'].items(), key=lambda kv: (kv[1],
                   -TYPE_PRIORITY.index(kv[0]) if kv[0] in TYPE_PRIORITY else -99))[0]
        a['type'] = typ
        spread = len(set(a['sources']))
        a['spread'] = spread
        a['sources'] = sorted(set(a['sources']))
        # 短语保留下限：freq>=5 且 spread>=3，或 freq>=3 且术语后缀
        if typ == 'phrase':
            last = a['en'].split()[-1]
            keep = (a['freq'] >= 5 and spread >= 3) or \
                   (a['freq'] >= 4 and spread >= 2 and th.RE_TERM_SUFFIX.search(last))
            if not keep:
                a['kept'] = False
            else:
                a['kept'] = True
        else:
            a['kept'] = True
        a['status'] = status_of(a, terms, persons, pool)
        if a['freq'] >= 20 and spread >= 5:
            a['tier'] = 'T1'
        elif a['freq'] >= 5 and spread >= 2:
            a['tier'] = 'T2'
        elif a['freq'] >= 2:
            a['tier'] = 'T3'
        else:
            a['tier'] = 'T4'
        cands.append(a)

    kept = [c for c in cands if c['kept']]
    dropped = [c for c in cands if not c['kept']]
    kept.sort(key=lambda c: (bucket_of(c['en']), fold_nfd(c['en'])))
    meta = {'generated_at': '2026-11-22', 'files': len(files),
            'all_keys': len(cands), 'kept': len(kept),
            'dropped_lowfreq_phrase': len(dropped)}
    persist(kept, meta, dropped)
    return kept, dropped


def persist(kept, meta, dropped):
    dump_json({'meta': meta, 'candidates': kept}, FULL)
    compact = [{k: c[k] for k in ('key', 'en', 'type', 'freq', 'spread',
                                  'tier', 'status')} for c in kept]
    for cs, c in zip(compact, kept):
        cs['sources'] = c['sources'][:3]
        cs['n_sources'] = len(c['sources'])
    dump_json({'meta': meta, 'candidates': compact}, CAND)
    write_az(kept, dropped)


PUBINFO_RX = re.compile(
    r'(?i)\b(?:first|last)\s+(?:published|updated)\b|'
    r'\bpublished\s+(?:mon|tue|tues|wed|thu|thur|thurs|fri|sat|sun)\b')
PARTICLE_NAME_RX = re.compile(
    r"^(?:van|von|de|der|den|du|la|le|di|da|del|ibn|bin|bint|al|el|abu|abd)\s+[A-Z]")


def clean_catalog(cands):
    out = []
    for c in cands:
        if PUBINFO_RX.search(c['en']) or c['key'] in NOISE_TERM:
            continue
        if c['type'] == 'phrase' and PARTICLE_NAME_RX.match(c['en']):
            c['type'] = 'person'
        out.append(c)
    return out


def restatus():
    d = load_json(FULL)
    terms, persons = load_registered()
    pool = load_pool_status()
    cands = clean_catalog(d['candidates'])
    for c in cands:
        c['status'] = status_of(c, terms, persons, pool)
    d['candidates'] = cands
    d['meta']['kept'] = len(cands)
    persist(cands, d['meta'], d['meta'].get('dropped_lowfreq_phrase', 0))
    print('restatus done: %d' % len(cands))


def write_az(kept, dropped):
    os.makedirs(AZ, exist_ok=True)
    n_drop = dropped if isinstance(dropped, int) else len(dropped)
    groups = collections.defaultdict(list)
    for c in kept:
        groups[bucket_of(c['en'])].append(c)
    order = [chr(x) for x in range(ord('A'), ord('Z') + 1)] + ['#']
    total = 0
    index = []
    for letter in order:
        rows = groups.get(letter, [])
        rows.sort(key=lambda c: fold_nfd(c['en']))
        total += len(rows)
        lines = ['键\t类型\t频次\t篇数\t档\t状态\t来源（至多三篇）']
        for c in rows:
            src = '；'.join(c['sources'][:3])
            if c['n_sources'] > 3 if 'n_sources' in c else len(c['sources']) > 3:
                src += ' 等%d篇' % (c.get('n_sources') or len(c['sources']))
            lines.append('%s\t%s\t%d\t%d\t%s\t%s\t%s'
                         % (c['en'], c['type'], c['freq'], c['spread'],
                            c['tier'], c['status'], src))
        with io.open(os.path.join(AZ, '%s.tsv' % letter), 'w',
                     encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines) + '\n')
        index.append((letter, len(rows)))

    index_md = ['# specs/058 A–Z 总表索引', '',
                '> 本目录为生成物，勿手改。每字母一份 TSV，UTF-8，制表符分隔；'
                '首行为列名。全表按词首字母分节，非拉丁与数字起首归 `#`。', '',
                '| 节 | 行数 |', '| --- | --- |']
    for letter, n in index:
        index_md.append('| [%s](%s.tsv) | %d |' % (letter, letter, n))
    index_md += ['', '总计 %d 行。口径与状态说明见 `../summary.md`。' % total]
    with io.open(os.path.join(AZ, 'README.md'), 'w', encoding='utf-8',
                 newline='\n') as f:
        f.write('\n'.join(index_md) + '\n')

    by_type = collections.Counter(c['type'] for c in kept)
    by_tier = collections.Counter(c['tier'] for c in kept)
    by_status = collections.Counter(
        '已登记' if c['status'].startswith('已登记') else
        ('池:' + c['status'].split(':', 1)[1].split('@')[0] if c['status'].startswith('池:') else '本轮新增')
        for c in kept)
    summary = ['# specs/058 提取总表口径与计数（2026-11-22）', '',
               '- 语料：yuanwen/ 全库，%d 篇' % len(corpus_files()),
               '- 去重键：register_lib.norm_key_quote（A 口径，引号与变音符折叠）',
               '- 保留候选：%d 条；因低频短语下限未列出：%d 条（freq<5 且无术语后缀的二元/三元片段）' % (len(kept), n_drop),
               '- 类型分布：' + '，'.join('%s %d' % kv for kv in by_type.most_common()),
               '- 档位分布：T1 %d／T2 %d／T3 %d／T4 %d' % (by_tier['T1'], by_tier['T2'], by_tier['T3'], by_tier['T4']),
               '- 状态分布：已登记 %d／池内 %d／本轮新增 %d' % (
                   sum(v for k, v in by_status.items() if k == '已登记'),
                   sum(v for k, v in by_status.items() if k.startswith('池:')),
                   by_status.get('本轮新增', 0)), '',
               '## 状态说明', '',
               '- 已登记（术语表／人名表）：折叠键命中登记册既有行。',
               '- 池:published/held/rejected/new：命中 tasks/term-pool.json 的既有状态。',
               '- 本轮新增：两处均未命中，属第二轮新提取候选，需按 A/B/C 分档裁定。', '',
               '## 未列出部分', '',
               '低频短语片段（freq<5 且尾词无术语后缀）留在 candidates.json.gz 之外的统计中，不进入总表；'
               '这是刻意的精度取舍，不是丢弃证据：candidates.json.gz 记录了 kept 全量，未列出部分仅计数。']
    with io.open(os.path.join(OUT, 'summary.md'), 'w', encoding='utf-8',
                 newline='\n') as f:
        f.write('\n'.join(summary) + '\n')
    print('kept=%d dropped=%d az_total=%d' % (len(kept), n_drop, total))


def main():
    if '--restatus' in sys.argv:
        restatus()
    elif '--build-only' not in sys.argv:
        build()
    else:
        d = load_json(CAND)
        write_az(d['candidates'], d['meta'].get('dropped_lowfreq_phrase', 0))


if __name__ == '__main__':
    main()

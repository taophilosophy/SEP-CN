# -*- coding: utf-8 -*-
"""逐篇遍历 en/ 全库提取术语/人名候选（specs/008-terminology-campaign US-1）。

用法:
  python tools/term_harvest.py                # 全库遍历（按字母分批缓存，可中断续跑）
  python tools/term_harvest.py --letter a     # 只跑一个字母批次
  python tools/term_harvest.py --refresh      # 忽略缓存重提

多语种智能提取（2026-10-30 用户裁定：原文不一定是英语；词汇不一定是英语）:
  ①斜体术语 *...* ②引语术语 “...” ③-ism 词族 ④高频概念短语（二元/三元，去停用词）
  ⑤人名序列（大写二元组，type=person）⑥阿位专名（罗马化颗粒路由，ADR-0013）
  ⑦主题词（H1 题名 + 章节标题关键短语，type=topic）⑧原文文字路线：阿拉伯/希腊/
  希伯来/西里尔/天城体/汉字字母原文（type=arabic/greek/hebrew/cyrillic/devanagari/cjk）
  ⑨罗马化外语词重分类：含非 ASCII 拉丁扩展或德语名词标记的斜体/引语候选 → type=foreign
与两登记册 + 候选池已登记键求差后入池（ADR-0036：词汇表已并网删除）。幂等：单篇提取结果缓存于
specs/008-terminology-campaign/results/harvest-cache/，重跑只增量解析新文件；
路线/停用词/阈值变更后必须 --refresh（缓存嵌旧词表）。

退出码: 0 成功；2 参数/路径错误。
"""
import io
import json
import os
import re
import sys
from collections import Counter

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)  # 脚本直跑时保证 from tools import 可用
from tools.register_lib import norm_key, norm_key_quote, person_path, term_path  # noqa: E402
CORPUS = os.path.join(ROOT, 'en')
POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')
CACHE = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results',
                     'harvest-cache')
REGISTRY = term_path()
REGISTRY2 = person_path()
# 旧候选池已于 2026-11-18 全量并入 term-pool.json 并删除（specs/050 §8）；
# LEGACY_POOL 保留为兼容占位（文件不存在即跳过），历史裁定账已在新池 candidates 内。

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
            'italic': OTHER_MIN_FREQ, 'quoted': 3, 'person': 5, 'arabic': 2,
            'topic': 1, 'foreign': 2, 'greek': 1, 'hebrew': 1,
            'cyrillic': 1, 'devanagari': 1, 'cjk': 1}
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
# 原文文字路线（2026-10-30 用户裁定「还有阿拉伯语」等）：非拉丁字母原文序列
SCRIPT_ROUTES = (
    ('arabic', re.compile(
        r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+'
        r'(?:[\s\u060C\u061B][\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+)*')),
    ('greek', re.compile(
        r'[\u0370-\u03FF\u1F00-\u1FFF]+(?:[\s\u00B7,][\u0370-\u03FF\u1F00-\u1FFF]+)*')),
    ('hebrew', re.compile(r'[\u0590-\u05FF]+(?:[\s][\u0590-\u05FF]+)*')),
    ('cyrillic', re.compile(r'[\u0400-\u04FF]+(?:[\s][\u0400-\u04FF]+)*')),
    ('devanagari', re.compile(r'[\u0900-\u097F]+(?:[\s][\u0900-\u097F]+)*')),
    ('cjk', re.compile(r'[\u4E00-\u9FFF\u3400-\u4DBF]+(?:[\u3001\u00B7]?[\u4E00-\u9FFF\u3400-\u4DBF]+)*')),
)
SCRIPT_TYPES = {t for t, _ in SCRIPT_ROUTES} | {'arabic'}
# 罗马化外语词标记：非 ASCII 拉丁扩展字母 / 德语名词后缀 / 无缀经典词小词典（可扩充）
NONASCII_LATIN = re.compile(r'[\u00C0-\u024F\u1E00-\u1EFF]')
GERMAN_SUFFIX_RE = re.compile(
    r'(?:heit|keit|ung|schaft|t\u00e4t|isch|lichkeit|smus)$', re.I)
FOREIGN_LEXICON = {
    'dasein', 'lebenswelt', 'weltanschauung', 'aufhebung', 'aufheben',
    'bildung', 'geist', 'wissenschaft', 'urteil', 'erlebnis', 'einfuhlung',
    'einf\u00fclung', 'geltung', 'anschauung', 'begriff', 'vorstellung',
    'ding an sich', 'polis', 'logos', 'nous', 'pathos', 'ethos', 'doxa',
    'paideia', 'phronesis', 'eudaimonia', 'aret\u00eA', 'arete', 'techne',
    'episteme', 'dharma', 'karma', 'nirvana', 'dao', 'qi', 'ren', 'xiao',
    'tian', 'wu-wei', 'atman', '\u0101tman', 'sunyata',
}
TOPIC_GENERIC = {
    'introduction', 'references', 'bibliography', 'conclusion',
    'further reading', 'academic tools', 'other internet resources',
    'related entries', 'appendix', 'appendices', 'summary', 'notes',
    'acknowledgments', 'primary literature', 'secondary literature',
    'glossary', 'see also', 'historical dictionary', 'reading',
}

# ---------------------------------------------------------------------------
# 术语性守卫（2026-11-18，specs/050 术语提取降噪）
# 治本：在提取端就拦下「非术语」——单字泛词、通用搭配、结构标题、书目残片、
# 句子级串、古汉语虚词。确定性残渣自动拦；语义泛词用保守泛词表拦，
# 全部可在预筛账（specs/008 results/prescreen-*）复核撤销。
# ---------------------------------------------------------------------------

# ① 单字泛词：quoted/italic/foreign 单字命中即非术语（术语后缀/非拉丁原文除外）
COMMON_SINGLE = set('''good true false yes no real natural possible impossible
proof theorem rule definition element system person proposition formal internal
external absolute relative religion god optimism pessimism knowledge belief truth
reality existence world object thing kind sort way case part point fact idea concept
view theory sense reason language meaning value action right law state property
quality relation mind body soul spirit life death experience perception thought
argument conclusion premise statement sentence term word name being entity cause
effect function structure process event phenomenon content form matter substance
essence accident category universal particular individual whole unity plurality
necessity possibility contingency actuality potentiality freedom liberty justice
equality duty obligation virtue vice happiness pleasure pain evil wrong moral
aesthetic logic metaphysics epistemology ontology ethics political social science
philosophy nature artificial normative descriptive analytic synthetic necessary
sufficient contingent actual ideal material abstract concrete general singular
diverse same similar identical distinct one two three first second third
important central crucial basic several various different recent widely generally
usually often sometimes always never already still yet also just even only very
quite rather somewhat particularly especially specifically actually really simply
merely mainly mostly largely partly fully completely entirely almost nearly
approximately roughly today now here there'''.split())

# ② 短语不良词元：phrase 路含此集合词元即泛搭配（取最不可能构成哲学术语的实动词/副词）
PHRASE_BAD = set('''take takes took taken taking make makes made making give gives
gave given giving get gets got getting go goes went gone going come comes came coming
put puts putting say says said saying see sees saw seen call calls called find finds
found show shows shown happen happens happened occur occurs occurred remain remains
seem seems seemed appear appears become becomes became play plays played want wants
wanted try tries tried look looks looked feel feels felt too much many later earlier
ago already still yet also just even only very quite rather somewhat actually really
simply merely mostly largely partly fully completely entirely almost nearly
approximately roughly'''.split())

# ③ 古汉语虚词/常用字（单字 cjk 命中即非术语；概念字 理道仁義德性心情智禮孝忠勇廉恥法術勢 保留）
CJK_FUNC = set('之乎者也矣焉哉而則乃然若如其此彼所以為於于與及皆亦又且夫蓋故可非有能得欲見聞知行成同明利虛則是一二三四五六七八九十')

# ④ 英文句首虚词（阿位序列末词命中即书目残片 "b. For"/"b. The"）
EN_SENT_STOP = set('''the for in of and but this that a an to as at by on or
with from is are was were be been being if then than so such not no nor'''.split())

# ⑤ 术语后缀（单字/短语术语性弱信号：命中即可越过泛词表）
RE_TERM_SUFFIX = re.compile(
    r'(ism|isms|ology|ologies|tion|sion|ity|ities|ness|ship|hood|ment|ence|ance|'
    r'graphy|cracy|nomy|metry|geny|morphism|logy|ist)s?$', re.I)

# ⑥ 结构标题（topic 路命中即非术语）
STRUCT_HEAD = re.compile(
    r'^(introduction|chapter|appendix|supplement|notes?|references?|bibliograph|'
    r'further reading|related entries|academic tools|other internet|acknowledg|'
    r'summary|conclusion|see also|primary literat|secondary literat|glossary|'
    r'historical dictionary|figure|table|preface|foreword|afterword)\b', re.I)

# ⑦ 出版社/城市残片（foreign/arabic 序列含之即书目残片）
PUB_BAD = {'press', 'university', 'publishing', 'publisher', 'edition',
           'editions', 'volume', 'volumes', 'translated', 'translation',
           'library', 'bombay', 'leiden', 'leipzig', 'dordrecht', 'kluwer',
           'springer', 'routledge', 'blackwell', 'clarendon', 'hackett',
           'kegan', 'wiley', 'elsevier', 'brill', 'tuebingen', 'muenchen',
           'milano', 'firenze', 'louwain', 'leuven'}
# ⑧ 书目缩写残片（"b." "p." "ed." 等）
BIB_RE = re.compile(
    r'(?<![A-Za-z])(b|p|pp|ed|eds|vol|vols|no|nos|trans|n\.d|s\.v|cf|et al|'
    r'ibid|op\. ?cit|repr)\.', re.I)

# ⑨ 数学/LaTeX 残渣词元（未包在 $..$ 里的残留命令；剥反斜杠后成普通词）
MATH_TOKENS = {'cdot', 'rightarrow', 'leftarrow', 'uparrow', 'downarrow',
               'langle', 'rangle', 'frac', 'sqrt', 'varnothing', 'mathbb',
               'vdash', 'forall', 'exists', 'mapsto', 'subseteq', 'supseteq',
               'infty', 'neg', 'land', 'lor', 'leq', 'geq', 'equiv', 'iff',
               'lim', 'sum', 'prod', 'int', 'partial', 'nabla', 'otimes',
               'oplus', 'ast', 'circ', 'simeq', 'approx', 'cong', 'neq',
               'pm', 'mp', 'dagger', 'bot', 'top', 'notin', 'subset', 'supset',
               'cap', 'cup', 'emptyset', 'mathcal', 'textbf', 'textsf',
               'mathrm', 'texttt', 'emph', 'operatorname', 'mathrel',
               'mathbin', 'bigcup', 'bigcap', 'dots', 'quad', 'qquad',
               'varepsilon', 'imath', 'ket', 'bra', 'vec', 'bar', 'amp',
               'colon'}

# ⑩ 子句/句子标志（系动词/助动词/报道动词；术语是名词短语，含量词动词即句子片段）。
# 刻意排除 will / being / matter：free will、human being、prime matter 等均为术语。
CLAUSE_TOKENS = {'is', 'are', 'am', 'was', 'were', 'be', 'been', 'has', 'have',
                 'had', 'do', 'does', 'did', 'would', 'can', 'could', 'may',
                 'might', 'must', 'shall', 'should', 'said', 'says', 'wrote',
                 'writes', 'argues', 'argued', 'cannot',
                 "isn't", "aren't", "wasn't", "weren't", "doesn't", "don't",
                 "didn't", "won't", "shouldn't", "couldn't", "wouldn't",
                 "mightn't", "mustn't", "can't"}

# ⑩b 外语路 English 残片尾词（foreign 候选含之即 "术语+英语普通词" 解析残片）
CLOSING_WORDS = {'chap', 'chapter', 'vol', 'volume', 'ed', 'edition', 'trans',
                 'translator', 'pp', 'himself', 'herself', 'itself',
                 'themselves', 'works', 'term', 'person', 'care', 'disciple',
                 'perspective', 'structures', 'section', 'ibid'}


# ⑪ 全普通词短语白名单（"全普通词→泛搭配"规则的例外：这些确是真术语）
TERM_KEEP = {
    'natural kind', 'natural kinds', 'natural law', 'natural right',
    'natural rights', 'natural language', 'natural selection', 'natural theology',
    'true belief', 'good will', 'common good', 'common sense', 'public reason',
    'public interest', 'public good', 'civil society', 'social contract',
    'general will', 'basic structure', 'original position', 'veil of ignorance',
    'moral luck', 'moral sense', 'moral law', 'free will', 'private property',
    'social justice', 'distributive justice', 'corrective justice', 'common law',
    'good faith', 'perfect duty', 'imperfect duty', 'general term', 'singular term',
}


def termhood_ok(raw, typ):
    """术语性守卫：返回 True 表示可入池，False 表示确定性/高置信非术语。

    治本核心（specs/050）：把「单字泛词、通用搭配、结构标题、书目残片、
    句子级串、古汉语虚词」在提取端就拦下。只拦确定性/高置信非术语，
    语义待定者一律放行留给人审（机检为筛、人审为判，ADR-0070）。
    """
    toks = WORD_RE.findall(raw)
    low = [w.casefold() for w in toks]
    # ⓪ 数学/LaTeX 残渣（未包在 $..$ 里漏网的命令词）
    if '\\' in raw or (set(low) & MATH_TOKENS):
        return False
    # ⓪b 子句/句子片段（系动词/助动词/报道动词 → 非名词性术语）
    for t in toks:
        b = t.casefold().replace('\u2019', "'").replace('\u2018', "'")
        if b in CLAUSE_TOKENS:
            return False
    # ⓪c 连字符/重复残片（"suárez- suárez-"、"löwenstein- özbe-"）
    if any(t.endswith('-') and len(t.strip('-')) >= 3 for t in toks):
        return False
    _stem = Counter(t.strip('-').casefold() for t in toks)
    if any(v >= 2 and len(k) >= 3 for k, v in _stem.items()):
        return False
    # ⓪d 跨句粘连（phrase 滑窗跨句界产生 "theory Instead"/"requires" 类；
    # 词元含句内大写专名亦非术语）——由提取端句界断窗兜底，此处拦形容词化副词尾
    if typ == 'phrase' and re.search(r'\b(Instead|Like|Also|Moreover|'
                                     r'However|Thus|Therefore|Rather|'
                                     r'According)\b', raw):
        return False
    # ① 单字泛词（quoted/italic/foreign）
    if typ in ('quoted', 'italic', 'foreign') and len(toks) == 1:
        if low[0] in COMMON_SINGLE and not RE_TERM_SUFFIX.search(low[0]) \
                and not NONASCII_LATIN.search(raw):
            return False
    # ② 通用搭配（phrase）
    if typ == 'phrase':
        if any(w in PHRASE_BAD for w in low):
            return False
        if len(low) >= 2 and all(w in COMMON_SINGLE for w in low) \
                and re.sub(r'\s+', ' ', raw.strip().casefold()) not in TERM_KEEP \
                and not any(RE_TERM_SUFFIX.search(w) for w in low):
            return False
    # ③ 阿位书目残片（末词为英文句首虚词）
    if typ == 'arabic' and toks and low[-1] in EN_SENT_STOP:
        return False
    if typ == 'arabic' and toks and (len(toks) >= 2) and any(w in PUB_BAD for w in low):
        return False
    # ④ 结构标题（topic）：标题/节名不是原子术语，从严
    if typ == 'topic':
        if STRUCT_HEAD.match(raw.strip()):
            return False
        if re.search(r'\bsupplement\b', raw, re.I):
            return False
        if len(toks) > 3:
            return False
        # 含连词的复合标题（"Descartes and Ethics"/"X or Y"）非术语；
        # 含 of/on 的（"problem of evil"/"identity of indiscernibles"）可为术语，保留
        if re.search(r'\b(and|or)\b', raw):
            return False
    # ⑤ cjk 虚词与句子级串
    if typ == 'cjk':
        s = raw.strip()
        if len(s) == 1 and s in CJK_FUNC:
            return False
        # 纯虚词/常用字串（如「之乎者也矣焉哉」）非术语
        han = [ch for ch in s if '\u4e00' <= ch <= '\u9fff'
               or '\u3400' <= ch <= '\u4dbf']
        if len(han) >= 2 and all(ch in CJK_FUNC for ch in han):
            return False
        if len(s) > 8:
            return False
    # ⑥ foreign/arabic 书目残片（出版社/城市/缩写）
    if typ in ('foreign', 'arabic') and (BIB_RE.search(raw)
                                          or (len(toks) >= 2 and any(w in PUB_BAD for w in low))):
        return False
    # ⑥b foreign 解析残片：English 尾词，或「英语小写词 + 非拉丁原文」混排
    #    （"Künne chap"/"Gödel's inner model"/"disciple Kamalaśīla"/"structures dào"）
    if typ == 'foreign':
        if any(w in CLOSING_WORDS for w in low):
            return False
        has_nonascii = any(ord(ch) > 127 for ch in raw)
        has_ascii_lower = any(re.fullmatch(r"[a-z][a-z'\-]*", t) for t in toks)
        if has_nonascii and has_ascii_lower:
            return False
    return True


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


def clean_topic(text):
    """主题词清洗：剥首尾停用词（不拒收），保留 1-4 词关键短语。"""
    words = WORD_RE.findall(text.strip().strip('.,;:!?'))
    if not (1 <= len(words) <= 4):
        return ''
    while words and words[0].casefold() in STOPWORDS:
        words = words[1:]
    while words and words[-1].casefold() in STOPWORDS:
        words = words[:-1]
    if not words or any(len(w) < 2 for w in words):
        return ''
    return ' '.join(words)


def extract_slug(path):
    """单篇五路提取 → Counter(键 → 频次) 与原始形、类型映射。"""
    text = open(path, encoding='utf-8').read()
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)  # 代码块剔除
    # 数学模式剔除（2026-11-18 specs/050 治本）：$..$ / $$..$$ / \(..\) / \[..\]。
    # 旧版漏剔，反斜杠被 WORD_RE 剥掉后残留 cdot/rightarrow/langle 等，
    # 曾产出 "mid cdot"「rightarrow rightarrow」类 LaTeX 残渣（freq 数百）。
    text = re.sub(r'\$\$.*?\$\$', ' ', text, flags=re.S)
    text = re.sub(r'\$[^$\n]*\$', ' ', text)
    text = re.sub(r'\\\(.*?\\\)', ' ', text, flags=re.S)
    text = re.sub(r'\\\[.*?\\\]', ' ', text, flags=re.S)
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
        # 罗马化外语词重分类（2026-10-30）：斜体/引语候选含非 ASCII 拉丁扩展、
        # 德语名词后缀或经典词小词典 → foreign（阿位专名与人名优先级更高）
        if typ in ('italic', 'quoted', 'phrase'):
            if NONASCII_LATIN.search(raw) or GERMAN_SUFFIX_RE.search(raw) \
                    or key in FOREIGN_LEXICON:
                typ = 'foreign'
        # 术语性守卫（2026-11-18 specs/050 治本）：确定性/高置信非术语在提取端拦下
        if not termhood_ok(raw, typ):
            return
        counter[key] += 1
        forms.setdefault(key, raw.strip())
        prev = types.get(key)
        if 'arabic' in (prev, typ):
            types[key] = 'arabic'  # ADR-0013：阿位专名优先标注
        elif prev in SCRIPT_TYPES or typ in SCRIPT_TYPES:
            types[key] = prev if prev in SCRIPT_TYPES else typ
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
    # 概念短语：句子级词序列滑窗（specs/050 治本：按句界断窗，杜绝跨句粘连）。
    # 句界：句末标点（.!?；）或分号/冒号——术语是名词短语，跨句共现必是残片。
    for para in body.split('\n'):
        for sent in re.split(r'(?<=[.!?:；;])\s+', para):
            words = WORD_RE.findall(sent)
            low = [w.casefold() for w in words]
            n = len(words)
            for i in range(n):
                if low[i] in STOPWORDS or len(words[i]) < 3:
                    continue
                for j in (i + 1, i + 2):
                    if j >= n or low[j] in STOPWORDS or len(words[j]) < 3:
                        break
                    add(' '.join(words[i:j + 1]), 'phrase')
    # 主题词路线（2026-10-30）：H1 题名 + 章节标题关键短语（含各语种原文标题词）
    for line in text.split('\n'):
        m = re.match(r'(#{1,2})\s+(.+?)\s*$', line)
        if not m:
            continue
        h = re.sub(r'^\d+(\.\d+)*\.?\s*', '', m.group(2))   # 剥节号
        h = re.sub(r'\s*[(\[][^)\]]*[)\]]\s*$', '', h)       # 剥尾括注/作者
        for seg in re.split(r'[:：;；—–]', h):
            c = clean_topic(seg)
            if c and c.casefold() not in TOPIC_GENERIC:
                add(c, 'topic')
    # 原文文字路线（2026-10-30）：非拉丁字母序列（阿拉伯/希腊/希伯来/西里尔/天城体/汉字）
    # 单字母（希腊/拉丁数学变量 φ、α）非术语，除汉字外要求 ≥2 字符
    for typ, rx in SCRIPT_ROUTES:
        for m in rx.finditer(body):
            seq = m.group(0).strip()
            if len(seq) < 2 and typ != 'cjk':
                continue
            add(seq, typ)
    return counter, forms, types


def load_registered_keys():
    """已登记键（A 口径 norm_key_quote，specs/033）：两登记册 + 旧候选池 + 新候选池。

    2026-11-18 specs/050 §7：池侧原用 B 口径 norm_key（不折叠撇号），与登记册侧
    （check_terms.norm_key 实际是 A 口径）不对称，致 ʿ/’ 与 ' 变体（如 ʿaql↔'aql、
    Bayes’ Theorem↔bayes' theorem）漏扣。统一改 A 口径折叠撇号，消除漏扣。
    """
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
    for pool_path in (POOL,):
        if os.path.exists(pool_path):
            try:
                data = json.load(open(pool_path, encoding='utf-8'))
                for c in data.get('candidates', []):
                    for part in re.split(r'\s*/\s*', c.get('en', '')):
                        if part.strip():
                            keys.add(norm_key_quote(part))
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
        entry = known.get(key)
        if entry is None:
            # 新键：已登记（在别处完成裁定）或低于阈值 → 不入池
            typ = run_types.get(key, 'phrase')
            # 已登记求差走 A 口径（key 为 B 口径池键，须再折叠撇号后比对，specs/050 §7）
            if norm_key_quote(key) in registered:
                continue
            if freq < MIN_FREQ.get(typ, OTHER_MIN_FREQ):
                continue
            entry = {'en': run_forms.get(key, key), 'freq': freq, 'type': typ,
                     'suggest': '', 'status': 'new', 'sources': []}
            known[key] = entry
            new_hits += 1
        else:
            typ = run_types.get(key, entry.get('type', 'phrase'))
        # entry 为旧池对象时 status/suggest/note 字段自动沿用
        entry['freq'] = freq if not letter else max(entry.get('freq', 0), freq)
        entry['type'] = typ
        entry['en'] = run_forms.get(key, entry.get('en', key))
        if letter:  # 字母批次增量：来源并集；全量跑以本轮为权威
            entry['sources'] = sorted(set(entry.get('sources', []))
                                      | set(run_sources.get(key, [])))
        else:
            entry['sources'] = run_sources.get(key, [])
        fresh.append(entry)
    # 旧池=裁定账本：未被本轮触达的条目（含已登记键的老条目）一律保留。
    # （2026-10-30 修：原 registered 差集作用于全部键，第二次全量跑会把
    #   除新键外的整个账本裁掉——62828→12930 事故即此因。）
    seen = {id(e) for e in fresh}
    fresh.extend(c for c in pool.get('candidates', []) if id(c) not in seen)
    pool['candidates'] = fresh

    pool['candidates'].sort(key=lambda c: -c.get('freq', 0))
    pool['meta'] = {
        'generated_at': __import__('datetime').date.today().isoformat(),
        'script': 'tools/term_harvest.py',
        'corpus': 'html/ 全库镜像',
        'scope': letter or 'all',
        'files_processed': total,
        'candidates': len(pool['candidates']),
        'new_this_run': new_hits,
        'method': '多语种提取（2026-10-30）：斜体/引语/-ism/高频短语/人名序列/阿位专名'
                  '（ADR-0013 变音符折叠键）/主题词（题名+章节标题）/原文文字'
                  '（阿拉伯-希腊-希伯来-西里尔-天城体-汉字）/罗马化外语重分类；'
                  '与两登记册+候选池求差；'
                  '按型阈值 phrase=%d ism/italic/foreign/arabic=%d quoted=3 '
                  'person=5 topic/greek/hebrew/cyrillic/devanagari/cjk=1；'
                  '低频尾部留存单篇缓存（results/harvest-cache/，本地）；' % (
                      PHRASE_MIN_FREQ, OTHER_MIN_FREQ),
        'usage': 'status 状态机（沿袭原 term-candidates.json 先例，已并入本池）：new→published@日期|held:理由|rejected:理由',
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

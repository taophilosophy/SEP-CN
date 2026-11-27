# -*- coding: utf-8 -*-
r"""登记册共享解析/折叠库（specs/033）。

两登记册（shu-yu-biao.md 术语、ren-ming-biao.md 人名）的键折叠、表格行解析与
A–Z 分节原语的唯一实现。此前散落 6 处副本（check_terms / registry_azsort /
term_flow / term_harvest / cnki_query / term_coverage / term_relations），
已两次发案静默漂移（specs/033 spec.md §1），本模块收敛后各工具一律引用此处，
禁止再复制函数体。

**口径纪律（specs/033 spec.md §2/§4，三口径不得互相合并）**：

* `norm_key_quote` —— A 引号折叠键：ʾʿ’‘ʼ′\`→'＋剥 *＋NFD 去组合符＋空白归一＋
  casefold。登记册↔正文一致性比对用（check_terms / cnki_query 登记侧）。
* `norm_key` —— B 基础折叠键：剥 *＋NFD 去组合符＋空白归一＋casefold。
  候选池键、凭证键、核销键用（term_flow / term_harvest / cnki_query /
  term_coverage / term_relations）。
* `fold_nfd` —— C 排序内层键：NFD 去组合符＋空白归一＋strip＋casefold（无剥 *、
  无引号折叠）。registry_azsort 节内排序专用；换口径＝登记册重排，禁改。

仅标准库；不 import tools 其他模块（叶子模块，防循环依赖）。
"""
import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TERM_FILE = 'zh/shu-yu-biao.md'
PERSON_FILE = 'zh/ren-ming-biao.md'


def term_path():
    """术语登记册绝对路径。"""
    return os.path.join(ROOT, TERM_FILE)


def person_path():
    """人名登记册绝对路径。"""
    return os.path.join(ROOT, PERSON_FILE)


# ---------------------------------------------------------------------------
# 折叠层（三口径，语义见模块 docstring）
# ---------------------------------------------------------------------------

# A 口径引号折叠表（check_terms 2026-11-10 补遗）：阿拉伯转写的 hamza/ayn
# （ʾ ʿ U+02BE/02BF）与弯/直撇号（’ ‘ ʼ ′）在登记册与词汇表间常混用，
# 曾使同一键被算作两个（Ikhwān al-Ṣafāʾ 与 Ikhwān al-Ṣafā’ 互不相等 →
# 虚假孤儿键，且真实冲突可借此藏身）。
QUOTE_FOLD = str.maketrans({'ʾ': "'", 'ʿ': "'", '’': "'",
                            '‘': "'", 'ʼ': "'", '′': "'", '`': "'"})


def norm_key_quote(text):
    """A 口径：剥斜体标记与空白、引号类折叠、变音符折叠（ADR-0013 同人归并）、casefold 比对。"""
    s = unicodedata.normalize('NFD', text.replace('*', '').strip().translate(QUOTE_FOLD))
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).casefold()


def norm_key(text):
    """B 口径：剥斜体与空白、变音符折叠、casefold（候选/凭证/核销键）。"""
    s = unicodedata.normalize('NFD', text.replace('*', '').strip())
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).casefold()


def fold_nfd(text):
    """C 口径：NFD 去组合符 → 空白归一 → strip → casefold（排序内层，无引号/星号处理）。"""
    s = unicodedata.normalize('NFD', text or '')
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).strip().casefold()


# ---------------------------------------------------------------------------
# 表格行解析层（check_terms 逐字迁移）
# ---------------------------------------------------------------------------

HEADER_WORDS = {'原文', '译法', '首现', '依据', '裁定日期', '人名', '文献',
                '条目', 'term', '原文形态', '通行中文', '键', '出处', '日期',
                '英语', '中文'}  # 词汇表内嵌第二表头（|英语|中文|）不得当数据行


def split_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def is_data_row(cells):
    # 只校验首列：六列新格式的第二列（原文）允许为空/「—」，不能据此丢弃数据行
    return (len(cells) >= 2 and cells[0]
            and cells[0].casefold() not in HEADER_WORDS
            and not set(cells[0]) <= set(':-— '))


def parse_registry2_full(path):
    """人名表八列解析（2026-11-07 籍属/年代列迁移）。

    返回 rows=[(term, orig, trans, nation, years, first_seen, basis, date, lineno)]。
    nation/years 为 None 表示「旧六列没有这两列」（区别于新格式留空或填「—」）。
    术语表仍是六列，此处 nation/years 恒为 None。
    """
    rows, warns = [], []
    if not path or not os.path.exists(path):
        return rows, warns
    for lineno, line in enumerate(open(path, encoding='utf-8'), 1):
        if not line.startswith('|'):
            continue
        cells = split_row(line)
        if not is_data_row(cells):
            continue
        n = len(cells)
        if n >= 8:
            term, orig, trans = cells[0], cells[1], cells[2]
            nation, years = cells[3], cells[4]
            first_seen, basis, date = cells[5], cells[6], cells[7]
            if n > 8:
                warns.append('第 %d 行 %d 列（应为 8，已取前 8 列）：%s'
                             % (lineno, n, term))
            if not basis:
                warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
        elif n == 6:
            term, orig, trans = cells[0], cells[1], cells[2]
            first_seen, basis, date = cells[3], cells[4], cells[5]
            nation = years = None
            if not basis:
                warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
        elif n >= 5:
            term, orig, trans = cells[0], None, cells[1]
            first_seen = cells[2] if n >= 3 else ''
            basis, date = cells[3], cells[4]
            nation = years = None
            if not basis:
                warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
        elif n == 4:
            term, orig, trans = cells[0], None, cells[1]
            first_seen, basis, date = cells[2] if n >= 3 else '', '', cells[3]
            nation = years = None
            warns.append('缺依据列（告警）：%s（第 %d 行）' % (term, lineno))
        else:
            term, orig, trans = cells[0], None, cells[1]
            first_seen = cells[2] if n >= 3 else ''
            basis, date = '', ''
            nation = years = None
            warns.append('第 %d 行仅 %d 列（应为 8）：%s'
                         % (lineno, n, term))
        rows.append((term, orig, trans, nation, years,
                     first_seen, basis, date, lineno))
    return rows, warns


def parse_registry_full(path):
    """返回 rows=[(term, orig, trans, first_seen, basis, date, lineno)] 与解析告警。

    六列（键|原文|译法|出处|依据|日期，2026-11-06 原文列迁移）为标准格式；
    人名表八列（多「籍属」「生卒/鼎盛年」）由 parse_registry2_full 解析后投影，
    这里只保留原有七元组签名，故旧工具（term_audit / tl_browser_batch）无需改动。
    此时 orig=None 表示「旧格式没有原文列」（区别于新格式的留空或填「—」）。
    """
    rows2, warns = parse_registry2_full(path)
    rows = [(t, orig, trans, fs, basis, date, ln)
            for t, orig, trans, _nation, _years, fs, basis, date, ln in rows2]
    return rows, warns


def parse_registry(path):
    """兼容旧签名：rows=[(term, trans, first_seen, basis, date, lineno)]。

    列位解析见 parse_registry_full（六列标准格式 + 旧五/四列兼容）。
    """
    full, warns = parse_registry_full(path)
    return [(t, trans, fs, basis, date, ln)
            for t, _orig, trans, fs, basis, date, ln in full], warns


# ---------------------------------------------------------------------------
# A–Z 分节层（registry_azsort 逐字迁移）
# ---------------------------------------------------------------------------

# 前置装饰符：书名号/引号/括号/星号/反引号等；ʿʾ 等转写修饰符按约定并入地名首字母
DECOR = set('《》〈〉「」『』“”‘’"\'`*\\_~([{（【［〔 \t\u02bf\u02be\u02bb\u02bc\u2018\u2019\u0060')
FOLD_CHARS = {'Ł': 'L', 'ł': 'l', 'Ø': 'O', 'ø': 'o', 'Đ': 'D', 'đ': 'd',
              'Æ': 'A', 'æ': 'a', 'Œ': 'O', 'œ': 'o', 'ß': 'S', 'Þ': 'T', 'þ': 't',
              'Ð': 'D', 'ð': 'd', 'ı': 'i'}
GREEK_BUCKET = {'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'e',
                'θ': 't', 'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x',
                'ο': 'o', 'π': 'p', 'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'u',
                'φ': 'f', 'χ': 'c', 'ψ': 'y', 'ω': 'o'}


def bucket_of(key):
    """首字母分节桶：A–Z 或 '#'。"""
    s = (key or '').strip()
    while s and s[0] in DECOR:
        s = s[1:].lstrip()
    if not s:
        return '#'
    c = s[0]
    base = unicodedata.normalize('NFD', c)[0]
    if base.isascii() and base.isalpha():
        return base.upper()
    if c in FOLD_CHARS:
        return FOLD_CHARS[c].upper()
    if c in GREEK_BUCKET:
        return GREEK_BUCKET[c].upper()
    return '#'

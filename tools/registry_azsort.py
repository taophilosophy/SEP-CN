# -*- coding: utf-8 -*-
"""登记册 A–Z 分节重排（术语表 / 人名表，specs/008 配套设施）。

用法：
  python tools/registry_azsort.py                       # 干跑：分桶统计 + 守恒校验
  python tools/registry_azsort.py --apply               # 写回（守恒残余≠0 或工作区脏则拒绝）
  python tools/registry_azsort.py --apply --allow-dirty # 带未提交改动时强行重排

设计与纪律（rules/05「生成器与批量改写」）：
  * 行内容零改写：只重排行序、插入字母节标题；守恒验收=数据行字节多重集相等，
    残余≠0 一律拒绝写回；
  * 幂等：首跑插入 <!-- az-sort:v1 --> 标记，重跑输出逐字节相同；
  * 基线：默认要求文件与 git HEAD 一致（未提交改动会被重排卷入他人工作）；
  * 原子写：临时文件 + os.replace。

分节规则：
  * 键=首列（词条键）；剥离开头装饰符（《》、引号、括号、ʿ/ʾ 等）与变音符后
    取首个拉丁字母为节；希腊字母按转写首字母归档；汉字/阿拉伯文/数字起首归 `#`。
  * 节内按折叠键排序（NFD 去组合符 + casefold + 空白归一），同键行保持原相对次序
    （以原行号保底，重跑稳定）。

保留区：人名表的「伊斯兰阿拉伯人物体例注」「登记格式说明」「待裁定」三段说明文字
原位保留（其数据行并入字母节）；术语表的 4 行历史表头/分隔行移除。
"""
import hashlib
import io
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter

_enc = getattr(sys.stdout, 'encoding', None)
if not _enc or _enc.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from tools import check_terms  # noqa: E402

MARKER = '<!-- az-sort:v1 -->'
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
LETTER_HEAD_RE = re.compile(r'^## ([A-Z#])$')

# 前置装饰符：书名号/引号/括号/星号/反引号等；ʿʾ 等转写修饰符按约定并入地名首字母
DECOR = set('《》〈〉「」『』“”‘’"\'`*\\_~([{（【［〔 \t\u02bf\u02be\u02bb\u02bc\u2018\u2019\u0060')
FOLD = {'Ł': 'L', 'ł': 'l', 'Ø': 'O', 'ø': 'o', 'Đ': 'D', 'đ': 'd',
        'Æ': 'A', 'æ': 'a', 'Œ': 'O', 'œ': 'o', 'ß': 'S', 'Þ': 'T', 'þ': 't',
        'Ð': 'D', 'ð': 'd', 'ı': 'i'}
GREEK = {'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'e',
         'θ': 't', 'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x',
         'ο': 'o', 'π': 'p', 'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'u',
         'φ': 'f', 'χ': 'c', 'ψ': 'y', 'ω': 'o'}

TERM_FILE = 'yi-zhe-shuo-ming.md'
PERSON_FILE = 'ren-ming-biao.md'

PERSON_DOC_PREFIXES = ('## 伊斯兰阿拉伯人物', '## 登记格式说明', '## 待裁定')

TERM_LEGEND = [
    '# 译者说明：术语对照表',
    '',
    '> 本文件为 SEP-CN 全库**术语**译名登记的单一事实源（宪法 III）。规则：新术语先登记、'
    '后使用；三校步骤校验正文用词与本表一致。',
    '>',
    '> **排序体例**：全表按词条首字母 A–Z 分节；分节键=首列键剥离前置装饰符（《》、引号、'
    '括号、ʿ/ʾ 等）与变音符后的首个拉丁字母，非拉丁字母（希腊/阿拉伯/汉字）或数字起首归'
    '末节 `#`；节内按折叠键排序，同键行保持原相对次序。',
    '>',
    '> **列序**：键 ｜ 原文 ｜ 译法 ｜ 首现（slug 或书目）｜ 依据 ｜ 裁定日期。依据档位见 '
    'ADR-0012（知网系权威源 → 权威译本 → 学界惯例；禁维基）。',
    MARKER,
]

PERSON_ORDER_NOTE = (
    '> **排序体例**：全表按人名首字母 A–Z 分节；分节键=首列键剥离前置装饰符与变音符后的'
    '首个拉丁字母，非拉丁字母或数字起首归末节 `#`；节内按折叠键排序，同键行保持原相对次序。'
    'ADR-0013 伊斯兰阿拉伯人名体例不变，其词条已并入同一 A–Z 索引（体例注见文末）。')


def norm_key(text):
    """折叠键：NFD 去组合符 → casefold → 空白归一。"""
    s = unicodedata.normalize('NFD', text or '')
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s).strip().casefold()


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
    if c in FOLD:
        return FOLD[c].upper()
    if c in GREEK:
        return GREEK[c].upper()
    return '#'


def is_registration(cells):
    """数据行判定：常规数据行，或首列撞 HEADER_WORDS 但末列是日期的真实登记行。"""
    if check_terms.is_data_row(cells):
        return True
    return (len(cells) >= 4 and DATE_RE.match(cells[-1] or '') is not None)


def _is_dropped_header(line):
    """历史遗留表头/分隔行（术语表 4 行、人名表 2 行）：全由表头词/短横组成。"""
    cells = check_terms.split_row(line)
    if not cells:
        return False
    if all(set(c) <= set(':-— ') for c in cells if c):
        return True  # 分隔行 | --- | --- |
    return cells[0].casefold() in check_terms.HEADER_WORDS and not DATE_RE.match(cells[-1] or '')


def scan(lines):
    """切分：header 行（首个 ## 之前）、数据行、文档段（人名表三段说明）。"""
    header, rows, docs = [], [], []
    fence = False
    idx = 0
    doc = None
    for line in lines:
        s = line.rstrip('\n')
        if s.lstrip().startswith('```'):
            fence = not fence
            if doc is not None:
                doc['lines'].append(line)
            elif not rows:
                header.append(line)
            idx += 1
            continue
        if fence:
            if doc is not None:
                doc['lines'].append(line)
            idx += 1
            continue
        if doc is not None:
            if s.startswith('## ') and not s.startswith(tuple(PERSON_DOC_PREFIXES)):
                docs.append(doc)
                doc = None
            elif s.startswith('|') and is_registration(check_terms.split_row(s)):
                # 说明段后追加的登记行：并入字母节，说明文字原位保留
                rows.append({'line': line, 'key': check_terms.split_row(s)[0], 'idx': idx})
                idx += 1
                continue
            elif s.startswith('|') and _is_dropped_header(s):
                idx += 1
                continue
            else:
                doc['lines'].append(line)
                idx += 1
                continue
        if s.startswith('## ') and s.startswith(tuple(PERSON_DOC_PREFIXES)):
            doc = {'header': s, 'lines': [line]}
            idx += 1
            continue
        if s.startswith('|'):
            cells = check_terms.split_row(s)
            if is_registration(cells):
                rows.append({'line': line, 'key': cells[0], 'idx': idx})
            elif not _is_dropped_header(s):
                raise SystemExit('未识别的表格行（既不属数据也不属历史表头）：%s' % s[:80])
        elif not rows:
            header.append(line)
        else:
            # 字母节/其余正文：重排时丢弃（由 letter 节统一重生成）
            pass
        idx += 1
    if doc is not None:
        docs.append(doc)
    return header, rows, docs


def render(header, rows, docs):
    buckets = {}
    for r in rows:
        b = bucket_of(r['key'])
        buckets.setdefault(b, []).append(r)
    for b in buckets:
        buckets[b].sort(key=lambda r: (norm_key(r['key']), r['idx']))

    out = list(header)
    while out and not out[-1].strip():
        out.pop()
    out.append('')
    order = [chr(c) for c in range(ord('A'), ord('Z') + 1)] + ['#']
    for b in order:
        if b not in buckets:
            continue
        out.append('## %s' % b)
        out.append('')
        out.extend(r['line'] for r in buckets[b])
        out.append('')
    for doc in docs:
        out.extend(doc['lines'])
        while out and not out[-1].strip():
            out.pop()
        out.append('')
    while out and not out[-1].strip():
        out.pop()
    return '\n'.join(x.rstrip('\n') for x in out) + '\n', buckets


def _git_clean(path):
    try:
        r = subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', path],
                           cwd=ROOT, capture_output=True)
        return r.returncode == 0
    except OSError:
        return True


def process(path, allow_dirty=False, apply=False):
    rel = os.path.relpath(path, ROOT)
    before = open(path, encoding='utf-8').read().splitlines(True)
    text_before = ''.join(before)
    header, rows, docs = scan(before)

    if os.path.basename(path) == PERSON_FILE:
        if MARKER not in text_before and not any('排序体例' in l for l in header):
            # 在说明块引结尾后插入排序体例
            pos = max(i for i, l in enumerate(header) if l.startswith('>')) + 1
            header[pos:pos] = ['>', PERSON_ORDER_NOTE + '\n']
        if MARKER not in ''.join(header):
            header.append(MARKER + '\n')
    else:
        if MARKER not in text_before:
            header = [l + '\n' if not l.endswith('\n') else l for l in TERM_LEGEND]

    content, buckets = render(header, rows, docs)

    # 守恒门：数据行字节多重集相等
    new_lines = content.splitlines(True)
    _h2, new_rows, _d2 = scan(new_lines)
    h_before = Counter(hashlib.sha1(r['line'].encode()).digest() for r in rows)
    h_after = Counter(hashlib.sha1(r['line'].encode()).digest() for r in new_rows)
    residual = sum((h_before - h_after).values()) + sum((h_after - h_before).values())

    hist = ' '.join('%s:%d' % (b, len(v)) for b, v in
                    ((b, buckets[b]) for b in ([chr(c) for c in range(65, 91)] + ['#'])
                     if b in buckets))
    print('%s：数据行 %d → %d；周界 %d（%s）' % (rel, len(rows), len(new_rows), residual,
                                       '守恒' if residual == 0 else '不守恒'))
    print('  分节：' + hist)
    if residual:
        print('  拒绝写回：残余 %d 行（rules/05 批量改写前置门）' % residual)
        return 1
    if not _git_clean(rel) and not allow_dirty:
        print('  拒绝写回：工作区有未提交改动（先让并行会话收口或加 --allow-dirty）')
        return 1
    if not apply:
        print('  干跑：未写盘（--apply 写回）')
        return 0
    if content == text_before:
        print('  幂等：内容与现状一致，无需写回')
        return 0
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.azsort.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    print('  已写回：%s（%d 行）' % (rel, len(new_lines)))
    return 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    apply = '--apply' in argv
    allow_dirty = '--allow-dirty' in argv
    rc = 0
    for name in (TERM_FILE, PERSON_FILE):
        rc |= process(os.path.join(ROOT, name), allow_dirty=allow_dirty, apply=apply)
    return rc


if __name__ == '__main__':
    sys.exit(main())

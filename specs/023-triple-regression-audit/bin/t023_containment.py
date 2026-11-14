# -*- coding: utf-8 -*-
"""023 内容级表对账：en 顶层表每行内容（含嵌套表行）必须出现在 yw 全文。

背景：转换器 2026-11-14 起嵌套表透传（specs/018 spec A4 / 020 移交缺陷），
yuanwen 表数与 en 表数不再一一对应（嵌套表进 HTML 透传、列表项内嵌表成
独立缩进块），t020_cmp 的按索引对齐在新设计下必然错位。本工具只做内容
包含性判定：归一化后 en 行在 yw 全文找不到 = 真丢失；找到 = 设计内形态。

归一化：剥标签、实体反解、上下标 Unicode 折半角、只留 [0-9a-z 汉字]。
判断仍由人眼定性（018 先例：程序化比对只作拦截网）。

用法: python -I specs/023-triple-regression-audit/bin/t023_containment.py <slug>...
"""
import html as htmllib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
from tools.yuanwen import _split_tables  # noqa: E402

SUBSUP = str.maketrans('₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ⁺⁻'
                       'ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ'
                       'ᵦᵧᵨᵩᵪ',
                       '01234567890123456789n+-'
                       'abcdefghijklmnoprstuvwxyz'
                       'βγρφχ')


def norm(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = htmllib.unescape(s).translate(SUBSUP)
    return re.sub(r'[^0-9a-z\u4e00-\u9fff]+', '', s.lower())


NOTE_REF_RE = re.compile(
    r'<sup>\s*\[?\s*<a\s+href="notes\.html#(?P<ref>[A-Za-z0-9_-]+)"[^>]*>\s*\d*\s*</a>\s*\]?\s*</sup>', re.I)


def en_rows(slug):
    """en 正文顶层表 → [(表序, 行文本, 原始行前 90 字符)]。

    与转换器同法先剥完整注释（编辑性注释一贯丢弃，注释内表格不入对账）；
    注引标记按转换器同形转 [^note-N]（否则 norm 后 5≠note5 假阳性）；
    Academic Tools 三行（PDF 预览/InPhO/PhilPapers）为设计性豁免，过滤。"""
    p = os.path.join(ROOT, 'en', slug, 'index.html')
    if not os.path.isfile(p):
        return None
    text = open(p, encoding='utf-8', errors='replace').read()
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    out = []
    for ti, (_, seg) in enumerate([t for t in _split_tables(text) if t[0]]):
        seg = re.sub(r'<table[^>]*>', '', seg, count=1, flags=re.I)
        seg = re.sub(r'</table>\s*$', '', seg, flags=re.I)
        for ri, tr in enumerate(re.findall(r'<tr\b.*?</tr>', seg, re.S)):
            cells = [NOTE_REF_RE.sub(lambda m: '[^note-%s]' % re.sub('^note-', '', m.group('ref')), td)
                     for td in re.findall(r'<t[dh]\b.*?</t[dh]>', tr, re.S)]
            cells = [re.sub(r'<[^>]+>', ' ', td) for td in cells]
            txt = re.sub(r'\s+', ' ', htmllib.unescape(' '.join(cells))).strip()
            if not txt:
                continue
            if re.search(r'Preview the PDF|Friends of the SEP Society|InPhO|PhilPapers', txt, re.I):
                continue
            out.append((ti, ri, txt))
    return out


def yw_norm(slug):
    letter = slug[0]
    p = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    if not os.path.isfile(p):
        return None
    text = open(p, encoding='utf-8', errors='replace').read()
    # 图片接线 ![alt](path)：alt 文本插在行中间会破坏包含性判定，整段剥除
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', text)
    return norm(text)


def report(slug):
    rows = en_rows(slug)
    yn = yw_norm(slug)
    if rows is None or yn is None:
        print(f'===== {slug} ===== 缺文件')
        return
    miss = []
    for ti, ri, txt in rows:
        n = norm(txt)
        if n and n not in yn:
            miss.append((ti, ri, txt))
    print(f'===== {slug} ===== en 行 {len(rows)} | 丢失 {len(miss)}')
    for ti, ri, txt in miss[:10]:
        print(f'    表{ti} 行{ri}: {txt[:100]}')
    if len(miss) > 10:
        print(f'    ...共 {len(miss)} 行')


if __name__ == '__main__':
    for s in sys.argv[1:]:
        report(s)

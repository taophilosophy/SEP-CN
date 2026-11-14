# -*- coding: utf-8 -*-
"""逐段三向对齐（specs/028 试点人审辅助；ADR-0043 s2.5 逐段比较的机械前置）。

zh 标题已汉化，无法按标题名匹配 → 按**序位**对齐（节数须相等，否则报结构缺口）。
每节内按段序配对，输出「段数不等」「长度比离群」候选，供人工逐条判读。
用法: python -I tri-align.py <zh_doc>...
输出: stdout JSON + 人读摘要
告警级：只产候选，不作判定。
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

# 照录/结构节：不参与逐段内容比对
EXEMPT = re.compile(r'^(参考文献|学术工具|其他网络资源|相关词条|致谢|'
                    r'References|Academic Tools|Other Internet Resources|'
                    r'Related Entries|Acknowledgments|Notes|原文脚注)')


def split_sections(text):
    """返回 [(heading_text, [paras])]，按出现顺序。"""
    lines = text.splitlines()
    secs, cur, buf = [], '（序）', []
    depth = 0
    for ln in lines:
        s = ln.strip()
        if re.match(r'^#{1,4}\s', s):
            if buf or cur != '（序）':
                secs.append((cur, buf))
            cur, buf = s, []
            continue
        buf.append(ln)
    secs.append((cur, buf))
    out = []
    for h, ls in secs:
        body = '\n'.join(ls)
        body = re.sub(r'```[\s\S]*?```', '', body)
        body = re.sub(r'^[|>].*$', '', body, flags=re.M)          # 表格行、引用块
        body = re.sub(r'^\[\^[^\]]+\]:.*$', '', body, flags=re.M)  # 书目/注 def
        body = re.sub(r'<[^>]+>', '', body)                        # 残留 HTML
        paras = []
        for blk in re.split(r'\n\s*\n', body):
            b = ' '.join(x.strip() for x in blk.splitlines()).strip()
            if b:
                paras.append(b)
        out.append((h, paras))
    return out


def plain(p):
    p = re.sub(r'\[\^[^\]]*\]', '', p)
    p = re.sub(r'\$\$[^$]*\$\$|\$[^$\n]*\$', ' X ', p)
    p = re.sub(r'[*_`]', '', p)
    return p


def head_key(h):
    """取标题文字并去掉编号与括号注，用于识别照录节。"""
    t = re.sub(r'^#+\s*', '', h).strip()
    t = re.sub(r'^[\d.]+\s*', '', t)
    return t


def ratio(zh, yw):
    a = len(re.findall(r'[\u4e00-\u9fff]', zh))
    b = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", yw))
    if b < 8:
        return None
    return round(a / b, 2)


def run(zh_doc):
    slug = os.path.splitext(os.path.basename(zh_doc))[0]
    letter = os.path.basename(os.path.dirname(os.path.abspath(zh_doc)))
    yw_p = os.path.join(ROOT, 'yuanwen', letter, slug + '.md')
    zh = io.open(zh_doc, encoding='utf-8').read()
    yw = io.open(yw_p, encoding='utf-8').read()
    zs, ys = split_sections(zh), split_sections(yw)
    flags = []
    ratios = []
    if len(zs) != len(ys):
        flags.append({'kind': 'section-count', 'zh': len(zs), 'yw': len(ys),
                      'zh_heads': [head_key(h) for h, _ in zs],
                      'yw_heads': [head_key(h) for h, _ in ys]})
    for i, ((zh_h, zps), (yw_h, yps)) in enumerate(zip(zs, ys), 1):
        if EXEMPT.match(head_key(zh_h)):
            continue
        if len(zps) != len(yps):
            flags.append({'kind': 'para-count', 'sec': i, 'head': head_key(zh_h),
                          'zh': len(zps), 'yw': len(yps)})
        for j, (zp, yp) in enumerate(zip(zps, yps), 1):
            zp, yp = plain(zp), plain(yp)
            r = ratio(zp, yp)
            if r is None:
                continue
            ratios.append(r)
            # 实测标定（15 件 1,300 段）：汉译 chars/words 中位 1.46，常态 1.2–1.8。
            # <0.85 疑漏译/合并过度；>2.6 疑增译/夹带译注。
            if r < 0.85 or r > 2.6:
                flags.append({'kind': 'len-outlier', 'sec': i, 'head': head_key(zh_h),
                              'idx': j, 'ratio': r,
                              'zh': zp[:90], 'yw': yp[:130]})
    return {'slug': slug, 'zh_sections': len(zs), 'yw_sections': len(ys),
            'n_paras': len(ratios),
            'median': round(sorted(ratios)[len(ratios) // 2], 2) if ratios else None,
            'flags': flags}


res = [run(a) for a in sys.argv[1:]]
print(json.dumps(res, ensure_ascii=False, indent=1))
print('\n'.join('== %s 节 zh%d/yw%d  flag %d' % (r['slug'], r['zh_sections'],
                                                r['yw_sections'], len(r['flags'])) for r in res))

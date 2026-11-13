# -*- coding: utf-8 -*-
r"""019 译文侧公式缺陷分类器（拟升级为 tools/check_math_zh.py 门禁）。

对 <letter>/<slug>.md 逐文件扫描，产出逐条缺陷（禁抽样=全量过一遍）：
  D1 paren-residual   \(…\) 残留（站点不识别，rules/02 只认 $/$$）
  D2 cjk-outside-text 公式内 \text{}/\mbox{} 之外出现中日韩字符
                     （游离 $ 错配吞正文的显影，实证 actualism 第 5 条）
  D3 zero-width       公式内混入零宽/不可见字符
  D4 percent         公式内出现未转义 %（TeX 注释，译文被吞）
  D5 hash            公式内出现 #（宏参数符，报错）
  D6 dollar-odd       行内 $ 定界符不成对（渲染层守卫失效的上游）
  D7 multiset         与 en 快照公式多重集差分：en 有 zh 无 / zh 有 en 无
  D8 empty            公式体为空或纯空白
用法: python -I spec_scan.py [slug...]   （默认全量）
输出 results/zh-defects.jsonl + stdout 汇总
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RESULTS = os.path.join(HERE, '..', 'results')

sys.path.insert(0, HERE)
from align import load, norm, strip_delims  # noqa: E402

CJK_RE = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]')
TEXTCMD_RE = re.compile(
    r'\\(?:text|mbox|textnormal|textrm|textup|textbf|textit|textsf|texttt|'
    r'operatorname\*?|hbox)\s*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}')
ZW_RE = re.compile('[\u200b\u200c\u200d\u2060\ufeff]')


def scan_formula(kind, body, f, idx, out, summary):
    bare = strip_delims(kind, body)
    if not bare.strip():
        summary['D8_empty'] += 1
        out.write(json.dumps({'f': f, 'i': idx, 'code': 'D8',
                              'x': body[:120]}, ensure_ascii=False) + '\n')
        return
    if CJK_RE.search(TEXTCMD_RE.sub('', bare)):
        summary['D2_cjk_outside_text'] += 1
        out.write(json.dumps({'f': f, 'i': idx, 'code': 'D2',
                              'x': body[:200]}, ensure_ascii=False) + '\n')
    if ZW_RE.search(bare):
        summary['D3_zero_width'] += 1
        out.write(json.dumps({'f': f, 'i': idx, 'code': 'D3',
                              'x': body[:200]}, ensure_ascii=False) + '\n')
    if re.search(r'(?<!\\)%', bare):
        summary['D4_percent'] += 1
        out.write(json.dumps({'f': f, 'i': idx, 'code': 'D4',
                              'x': body[:200]}, ensure_ascii=False) + '\n')
    if re.search(r'(?<!\\)#', bare):
        summary['D5_hash'] += 1
        out.write(json.dumps({'f': f, 'i': idx, 'code': 'D5',
                              'x': body[:200]}, ensure_ascii=False) + '\n')


def dollar_balance(f, text):
    """行内 $ 配对：去掉 $$…$$、\\(…\\)、\\(…\\) 后数 $ 奇偶。"""
    t = re.sub(r'\$\$.*?\$\$', '', text, flags=re.S)
    t = re.sub(r'\\\(.*?\\\)', '', t, flags=re.S)
    t = re.sub(r'\\\[.*?\\\]', '', t, flags=re.S)
    return t.count('$')


def main(argv):
    zh_path = os.path.join(RESULTS, 'render-zh.jsonl')
    en_path = os.path.join(RESULTS, 'en-formulas.jsonl')
    zhseq = load(zh_path)
    enseq = load(en_path)
    out = open(os.path.join(RESULTS, 'zh-defects.jsonl'), 'w', encoding='utf-8')
    summary = collections.Counter()

    for f, seq in sorted(zhseq.items()):
        # D1/D6 基于原始 markdown
        md = os.path.join(REPO, f)
        text = open(md, encoding='utf-8').read()
        for m in re.finditer(r'\\\((.*?)\\\)', text, re.S):
            summary['D1_paren_residual'] += 1
            out.write(json.dumps({'f': f, 'code': 'D1',
                                  'x': m.group(0)[:160]},
                                 ensure_ascii=False) + '\n')
        odd = dollar_balance(f, text)
        if odd % 2:
            summary['D6_dollar_odd'] += 1
            out.write(json.dumps({'f': f, 'code': 'D6',
                                  'x': f'unpaired $ count={odd}'},
                                 ensure_ascii=False) + '\n')
        for idx, (kind, body) in enumerate(seq):
            scan_formula(kind, body, f, idx, out, summary)
        # D7 多重集差分
        slug = os.path.basename(f)[:-3].split('.')[0]
        base = os.path.basename(f)[:-3]
        cand = [f'{slug}/index.html', f'{base}/index.html',
                f'{slug}/{base.split(".")[-1]}.html']
        eh = next((c for c in cand if c in enseq), None)
        if eh:
            ec = collections.Counter(norm(x) for _, x in enseq[eh])
            zc = collections.Counter(norm(x) for _, x in seq)
            for body, n in (ec - zc).items():
                summary['D7_missing_bodies'] += n
                out.write(json.dumps({'f': f, 'code': 'D7-missing',
                                      'x': body[:200], 'n': n},
                                     ensure_ascii=False) + '\n')
            for body, n in (zc - ec).items():
                summary['D7_extra_bodies'] += n
                out.write(json.dumps({'f': f, 'code': 'D7-extra',
                                      'x': body[:200], 'n': n},
                                     ensure_ascii=False) + '\n')
    out.close()
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main(sys.argv[1:])

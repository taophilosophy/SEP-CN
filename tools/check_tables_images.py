# -*- coding: utf-8 -*-
"""表格与图片预检（ADR-0037；020 表格图片复核战役的候选清单生成器）。

检查项（zh 模式，默认扫顶层字母目录译文）：
  1. table-cols      —— 表头/分隔/数据行列数不一致（客观）；
  2. academic-table  —— `## 学术工具` 节用表格形态（ADR-0037 归一为列表）；
  3. table-compact   —— 非空单元格管道内侧多空格填充（禁对齐填充；单空格合法）；
     table-fullwidth —— 单元格含全角空格（rules/02 一律改半角）；
  3b. table-no-sep   —— 表块缺分隔行（渲染不成表格，硬缺陷）；
  4. table-en-prose  —— 单元格去代码/数学后 ≥4 英文词且无汉字（未译候选，
                        逐个定性：文献条目照录待括注汉译／漏译）；
  5. alt-lang        —— 图片 alt 无汉字（ADR-0037：alt 译中文；候选）；
  6. img-base        —— 中文词条图片引用不以 `../assets/` 开头
                        （rules/01、ADR-0037；客观违例）；
  7. img-resolve     —— 图片引用解析不到本地文件（客观）。

--yuanwen：扫 en/ 镜像，只查 table-cols 与 img-resolve（镜像保持源样，
不套 zh 体例）；镜像引用 `../assets/<slug>/…` 相对 en/<letter>/ 解析。
--corpus <file>：写出全部表格/图片词条并集清单（020 台账初始化数据）。

口径：
  * 只报告不改内容；所有发现默认告警级（exit 0），--gate 把客观项
    （img-base、img-resolve）升为硬错误（exit 1）；候选项永不升格。
  * 机器预检只出候选清单，正确性与一致性由人眼逐处定性（020 spec A3）。
"""
import argparse
import io
import json
import os
import re
import sys

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CJK = re.compile(r'[\u4e00-\u9fff]')
EN_WORD = re.compile(r'[A-Za-z]{3,}')
IMG_MD = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)[^)]*\)')
# 表行：行首管道；引块（> ）与列表项内容列缩进（018 转换器 li 内表形态）均认
TABLE_LINE = re.compile(r'^(?:>\s?)?[ \t]*\|')
SEP_CELL = re.compile(r'^:?-+:?$')
HARD_RULES = ('img-base', 'img-resolve')


def strip_code_math(cell):
    cell = re.sub(r'`[^`]*`', '', cell)
    cell = re.sub(r'\$[^$]*\$', '', cell)
    return cell


def split_row(line):
    body = line.strip()
    body = re.sub(r'^>\s?', '', body).strip()
    body = body[1:] if body.startswith('|') else body
    body = body[:-1] if body.endswith('|') else body
    # 按未转义管道切分（单元格内 `\|` 是字面管道，不切）
    cells = re.split(r'(?<!\\)\|', body)
    return [c.replace('\\|', '|').strip() for c in cells]


def parse_tables(lines):
    """产出 [ (起始行号, 节标题, 原始行表, [[cell,...],...] ), ... ]；连续表行聚一块。

    节标题取该块之前最近的 `## ` 行文本，供样板表分类（Academic Tools）。
    """
    blocks, cur, raw, start, heading = [], [], [], None, ''
    fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            if cur:
                blocks.append((start, heading, raw, cur))
                cur, raw, start = [], [], None
            continue
        if fence:
            continue
        m = re.match(r'^##\s+(.+?)\s*$', line)
        if m:
            heading = m.group(1)
        if TABLE_LINE.match(line):
            if start is None:
                start = i
            cur.append(split_row(line))
            raw.append(line.strip())
        elif cur:
            blocks.append((start, heading, raw, cur))
            cur, raw, start = [], [], None
    if cur:
        blocks.append((start, heading, raw, cur))
    return blocks


def is_boilerplate(heading):
    """样板节（Academic Tools）——每词条同构；源头单测覆盖，译文侧只查形态。"""
    h = heading.strip().lower()
    return h in ('academic tools', '学术工具')


def check_file(path, yuanwen=False):
    issues = []
    text = open(path, encoding='utf-8').read()
    lines = text.split('\n')
    for start, heading, raw, rows in parse_tables(lines):
        if not rows:
            continue
        ncols = [len(r) for r in rows]
        if len(set(ncols)) > 1:
            issues.append((start, 'table-cols',
                           f'列数不一致 {sorted(set(ncols))}'))
        sep_idx = next((i for i, r in enumerate(rows)
                        if all(SEP_CELL.match(c) for c in r if c)
                        and any(c for c in r)), None)
        if sep_idx is None:
            issues.append((start, 'table-no-sep',
                           '表块无分隔行，渲染不成表格（首行会被当作段落）'))
        if yuanwen:
            continue
        if is_boilerplate(heading):
            issues.append((start, 'academic-table',
                           '学术工具节为表格形态，应改列表（ADR-0037）'))
        for off, rawline in enumerate(raw):
            if sep_idx is not None and off == sep_idx:
                continue
            body = re.sub(r'^(?:>\s?)?\|', '', rawline)
            body = body[:-1] if body.endswith('|') else body
            for cell in body.split('|'):
                core = cell.strip()
                if '\u3000' in cell:
                    issues.append((start + off, 'table-fullwidth',
                                   f'单元格含全角空格：{core[:40]!r}'))
                    break
                if core and (len(cell) - len(cell.lstrip(' ')) >= 2
                             or len(cell) - len(cell.rstrip(' ')) >= 2):
                    issues.append((start + off, 'table-compact',
                                   f'单元格多空格填充：{core[:40]!r}'))
                    break
        cleaned = strip_code_math('|'.join(c for row in rows for c in row))
        words = EN_WORD.findall(cleaned)
        if len(words) >= 4 and not CJK.search(cleaned):
            issues.append((start, 'table-en-prose', f'未译候选：{words[:4]}'))
    base = os.path.dirname(path)
    fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        for alt, src in IMG_MD.findall(line):
            if yuanwen:
                if src.startswith('../assets/'):
                    resolved = os.path.normpath(os.path.join(base, src))
                    if not os.path.isfile(resolved):
                        issues.append((i, 'img-resolve', f'解析不到：{src}'))
                continue
            if not CJK.search(alt):
                issues.append((i, 'alt-lang', f'alt 非中文：{alt[:40]!r}'))
            if not src.startswith('../assets/'):
                issues.append((i, 'img-base', f'基座违规：{src}'))
                resolved = os.path.normpath(os.path.join(base, src))
            else:
                resolved = os.path.normpath(os.path.join(base, src))
            if not os.path.isfile(resolved):
                issues.append((i, 'img-resolve', f'解析不到：{src}'))
    return issues


ROOT_TABLES = ('ren-ming-biao.md', 'shu-yu-biao.md', 'yi-zhe-shuo-ming.md')


def iter_zh():
    for name in sorted(os.listdir(ROOT)):
        d = os.path.join(ROOT, name)
        if os.path.isdir(d) and len(name) == 1 and name.isalpha():
            for f in sorted(os.listdir(d)):
                if f.endswith('.md'):
                    yield os.path.join(d, f)
    # 根级登记册与说明页（020 战役补：原扫描漏掉，导致人名/术语两册文字墙长期未入检）
    for name in ROOT_TABLES:
        p = os.path.join(ROOT, name)
        if os.path.isfile(p):
            yield p


def iter_yuanwen():
    yw = os.path.join(ROOT, 'en')
    for letter in sorted(os.listdir(yw)):
        d = os.path.join(yw, letter)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith('.md'):
                    yield os.path.join(d, f)


def corpus(out_path):
    """020 台账初始化：并集清单（zh 译文按 slug 对应 yuanwen 件）。"""
    yw_tables, yw_imgs = {}, {}
    for p in iter_yuanwen():
        slug = os.path.splitext(os.path.basename(p))[0]
        text = open(p, encoding='utf-8').read()
        n_tab = sum(1 for _, h, _, rows in parse_tables(text.split('\n'))
                    if rows and not is_boilerplate(h))
        n_img = len(IMG_MD.findall(text))
        if n_tab:
            yw_tables.setdefault(slug, []).append(p)
        if n_img:
            yw_imgs.setdefault(slug, []).append(p)
    entries = []
    for p in iter_zh():
        slug = os.path.splitext(os.path.basename(p))[0]
        text = open(p, encoding='utf-8').read()
        n_tab = sum(1 for _, h, _, rows in parse_tables(text.split('\n'))
                    if rows and not is_boilerplate(h))
        n_img = len(IMG_MD.findall(text))
        zh_tab = slug in yw_tables or n_tab
        zh_img = slug in yw_imgs or n_img
        if zh_tab or zh_img:
            entries.append({'zh': os.path.relpath(p, ROOT), 'slug': slug,
                            'tables': n_tab, 'images': n_img,
                            'yw_tables': len(yw_tables.get(slug, [])),
                            'yw_images': len(yw_imgs.get(slug, []))})
    seen = {e['slug'] for e in entries}
    for slug, paths in sorted(yw_tables.items()):
        if slug not in seen:
            entries.append({'zh': None, 'slug': slug,
                            'tables': 0, 'images': 0,
                            'yw_tables': len(paths),
                            'yw_images': len(yw_imgs.get(slug, []))})
    for slug, paths in sorted(yw_imgs.items()):
        if slug not in seen:
            entries.append({'zh': None, 'slug': slug,
                            'tables': 0, 'images': 0,
                            'yw_tables': len(yw_tables.get(slug, [])),
                            'yw_images': len(paths)})
    entries.sort(key=lambda e: e['slug'])
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(entries, fh, ensure_ascii=False, indent=1)
    print(f'corpus: {len(entries)} 词条 → {out_path}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--yuanwen', action='store_true')
    ap.add_argument('--corpus')
    ap.add_argument('--gate', action='store_true')
    args = ap.parse_args()
    if args.corpus:
        corpus(args.corpus)
        return
    issues = []
    files = iter_yuanwen() if args.yuanwen else iter_zh()
    n_files = 0
    for p in files:
        n_files += 1
        for lineno, rule, msg in check_file(p, yuanwen=args.yuanwen):
            issues.append({'path': os.path.relpath(p, ROOT).replace('\\', '/'),
                           'line': lineno, 'rule': rule, 'msg': msg})
    by_rule = {}
    for it in issues:
        by_rule.setdefault(it['rule'], []).append(it)
    print(f'scan: {n_files} 个文件 | 发现 {len(issues)} 处')
    for rule in sorted(by_rule):
        print(f'  {rule}: {len(by_rule[rule])}')
    if not args.yuanwen:
        json.dump(issues, open(os.path.join(ROOT, 'state', 'tables-images-report.json'),
                               'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if args.gate and any(it['rule'] in HARD_RULES for it in issues):
        hard = [it for it in issues if it['rule'] in HARD_RULES]
        for it in hard:
            print(f"  [HARD] {it['path']}:{it['line']} {it['rule']} {it['msg']}")
        sys.exit(1)


if __name__ == '__main__':
    main()

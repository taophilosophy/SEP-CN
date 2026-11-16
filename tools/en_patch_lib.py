# -*- coding: utf-8 -*-
"""格式层补丁池目录正本：解析与准入（ADR-0062/0063）。

正本布局：
  baseline/en-patches/<id>.patch   一补丁一文件（unified diff，头部注释承载登记字段）
  baseline/en-patches/INDEX.json   生成物（禁手改）

本模块是**唯一解析实现**：转换器（`tools/yuanwen.py`）、离线体检
（`tools/check_en_patches.py`）与迁移脚本共用，避免三处各写一套。

补丁语义（行锚定）：
  每个 *.patch 恰含 1 个减行与 1 个加行；`find` 取减行全文、`replace` 取加行全文。
  命中计数必须等于头部 `expect`——不符即该件转换硬失败（防上游漂移静默失配）。
  上下文行（' ' 前缀）不参与应用，供 `git apply --check` 独立校验。

准入谓词（C2）：去空白后 find≡replace（空白差）或剥标签后 find≡replace（标记差）；
二者皆不成立即文字层，禁入池、禁改 yuanwen（转全局勘误表＋中文译注）。
"""
import os
import re

from tools.common import repo_path

PATCH_DIR = ('baseline', 'en-patches')
REQUIRED_FIELDS = ('id', 'slug', 'file', 'expect', 'category', 'source')
TAG_RE = re.compile(r'<[^>]*>|<!--.*?-->', re.S)


def patch_dir():
    return repo_path(*PATCH_DIR)


def _strip_ws(s):
    return re.sub(r'\s+', '', s)


def _strip_tags(s):
    return _strip_ws(TAG_RE.sub('', s))


def admission(find, replace):
    """C2 准入谓词：'blank'（空白差）／'tag'（标记差）／None（文字层，禁入池）。"""
    if _strip_ws(find) == _strip_ws(replace):
        return 'blank'
    if _strip_tags(find) == _strip_tags(replace):
        return 'tag'
    return None


def parse_patch_text(text):
    """解析单个补丁正本。返回 dict（含 find/replace/context 与登记字段）。

    格式不符（减行/加行数≠1、字段缺失）抛 ValueError——调用方按硬失败处理。
    """
    meta = {}
    for line in text.split('\n'):
        if line.startswith('# '):
            key, _, val = line[2:].partition(': ')
            meta[key.strip()] = val.strip()
        elif line.startswith('--- '):
            break
    minus, plus, context = [], [], []
    for line in text.split('\n'):
        if line.startswith('--- ') or line.startswith('+++ ') or line.startswith('@@'):
            continue
        if line.startswith('#'):
            continue
        if line.startswith('-'):
            minus.append(line[1:])
        elif line.startswith('+'):
            plus.append(line[1:])
        elif line.startswith(' '):
            context.append(line[1:])
    if len(minus) != 1 or len(plus) != 1:
        raise ValueError('补丁须恰含 1 减行与 1 加行（实为 %d/%d）' % (len(minus), len(plus)))
    p = {'id': meta.get('id'), 'slug': meta.get('slug'), 'file': meta.get('file'),
         'expect': int(meta['expect']) if meta.get('expect', '').isdigit() else None,
         'category': meta.get('category'), 'source': meta.get('source'),
         'find': minus[0], 'replace': plus[0], 'context': context}
    missing = [k for k in REQUIRED_FIELDS if not str(p.get(k) or '').strip()]
    if missing:
        raise ValueError('字段缺失: %s' % ','.join(missing))
    return p


def load_patches(dirpath=None):
    """读目录正本，返回 {slug: [patch, ...]}（按文件名排序，稳定）。"""
    base = dirpath or patch_dir()
    out = {}
    if not os.path.isdir(base):
        return out
    for fn in sorted(os.listdir(base)):
        if not fn.endswith('.patch'):
            continue
        path = os.path.join(base, fn)
        with open(path, encoding='utf-8', newline='') as f:
            p = parse_patch_text(f.read())
        p['patch_file'] = 'baseline/en-patches/%s' % fn
        out.setdefault(p['slug'], []).append(p)
    return out

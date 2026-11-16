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
import json
import os
import re
import sys

from tools.common import repo_path, utcnow_iso

PATCH_DIR = ('baseline', 'en-patches')
REQUIRED_FIELDS = ('id', 'slug', 'file', 'expect', 'category', 'source')
TAG_RE = re.compile(r'<[^>]*>|<!--.*?-->', re.S)
# 独立记录文件（运行态，state/ 不入库）：每进程首次解析补丁池时追加一行
RECORD = ('state', 'en-patches-loader.jsonl')


class PatchPoolMissing(Exception):
    """补丁池不可得：目录缺失，或目录内既无 *.patch 又无 INDEX.json。

    硬失败，禁静默降级（ADR-0063）：静默返回空池会让格式补丁悄悄失效，
    等价于派生物无据偏离 oracle。修复：恢复 `baseline/en-patches/`，或跑
    `specs/039-md-standardization/bin/migrate_en_patches.py --refresh` 再生 INDEX。
    """


_announced = False


def patch_dir():
    return repo_path(*PATCH_DIR)


def _index_info(base):
    """读 INDEX.json（生成物）仅作告知与留痕，不作判据（判据是 *.patch 正本）。"""
    path = os.path.join(base, 'INDEX.json')
    if not os.path.exists(path):
        return {'present': False}
    try:
        with open(path, encoding='utf-8') as f:
            idx = json.load(f)
    except (OSError, ValueError) as ex:
        return {'present': True, 'error': repr(ex)}
    return {'present': True, 'schema': idx.get('schema'), 'count': idx.get('count'),
            'ids': [p.get('id') for p in idx.get('patches', [])]}


def _announce(base, count, ids, index):
    """告知信息（stderr）＋独立记录文件（同进程一次；写失败必须喊出来，禁静默）。"""
    global _announced
    if _announced:
        return
    _announced = True
    idx = ('present(count=%s)' % index.get('count')) if index.get('present') else 'absent'
    if index.get('error'):
        idx = 'unreadable(%s)' % index['error']
    sys.stderr.write('[en-patches] 布局=目录正本 %s：生效补丁 %d 条 [%s]；INDEX %s；记录 %s\n'
                     % (base, count, ','.join(i or '?' for i in ids), idx,
                        repo_path(*RECORD)))
    rec = {'at': utcnow_iso(), 'layout': 'dir', 'dir': base, 'count': count,
           'ids': ids, 'index': index}
    try:
        path = repo_path(*RECORD)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'a', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    except OSError as ex:
        sys.stderr.write('[en-patches] 记录文件写入失败（不阻断转换，但须人工补记）：%s\n' % ex)


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


def load_patches(dirpath=None, notice=True):
    """读目录正本，返回 {slug: [patch, ...]}（按文件名排序，稳定）。

    有界解析：只看给定目录（缺省 `baseline/en-patches/`）这一处，逐级搜索禁行。
    目录缺失，或目录内既无 *.patch 又无 INDEX.json → 抛 PatchPoolMissing（硬失败，
    绝不静默返回空池）。INDEX 的 count=0 视为合法空池。
    """
    base = dirpath or patch_dir()
    if not os.path.isdir(base):
        raise PatchPoolMissing(
            '补丁池目录缺失：%s（禁静默降级；恢复目录或跑 specs/039 bin/migrate_en_patches.py --refresh）'
            % base)
    files = [fn for fn in sorted(os.listdir(base)) if fn.endswith('.patch')]
    index = _index_info(base)
    if not files and not index.get('present'):
        raise PatchPoolMissing('补丁池目录为空（无 *.patch 且无 INDEX.json）：%s' % base)
    out = {}
    for fn in files:
        path = os.path.join(base, fn)
        with open(path, encoding='utf-8', newline='') as f:
            p = parse_patch_text(f.read())
        p['patch_file'] = 'baseline/en-patches/%s' % fn
        out.setdefault(p['slug'], []).append(p)
    if notice:
        ids = [p['id'] for items in out.values() for p in items]
        _announce(base, len(ids), ids, index)
    return out

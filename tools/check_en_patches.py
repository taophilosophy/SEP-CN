#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补丁池离线校验（ADR-0062；ADR-0063 扩准入谓词与追溯）

用法: python tools/check_en_patches.py [--slug X] [--pool 路径] [--strict]

逐条校验 baseline/en-patches.json 中每条格式层补丁在当前 en/ 上的命中计数
是否等于 expect（补丁池只承载格式层修正；文字层缺陷登记全局勘误表并以中文
译注承载，不入池）。失配即报——上游漂移或补丁失效时，转换层（yuanwen.py）
会硬失败，本工具供不转换时快速体检。

ADR-0063 新增 C2 准入谓词：一条 find→replace 允许入池，当且仅当下列至少其一成立
  (a) 空白差：去掉全部空白后 find ≡ replace（例 `Einstein1949b`→`Einstein 1949b`）
  (b) 标记差：剥除标签与注释后 find ≡ replace（例 补 `</div>`、`-->`）
二者皆不成立 ⇒ 改动落在字母数字或词序 ⇒ 文字层，禁入池、禁改 yuanwen。
`--strict` 时谓词不符即退出码 1；默认只报不拦（存量池体检用）。

追溯：每条补丁须有非空 `source`（指向全局勘误表条目），字段齐备（id/slug/file/
find/replace/expect/category/source）。反向（勘误表格式层行须带补丁 id）待 P6
在勘误表增列后启用——该表当前由并行会话持有，本工具先不读。

退出码: 0 全通过；1 有失配、谓词不符（--strict）或字段缺失；2 池文件缺失。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import repo_path  # noqa: E402

REQUIRED_FIELDS = ("id", "slug", "file", "find", "replace", "expect", "category", "source")
TAG_RE = re.compile(r"<[^>]*>|<!--.*?-->", re.S)


def _strip_ws(s):
    return re.sub(r"\s+", "", s)


def _strip_tags(s):
    return _strip_ws(TAG_RE.sub("", s))


def admission(find, replace):
    """C2 准入谓词：返回 'blank'（空白差）/'tag'（标记差）/None（文字层，禁入池）。"""
    if _strip_ws(find) == _strip_ws(replace):
        return "blank"
    if _strip_tags(find) == _strip_tags(replace):
        return "tag"
    return None


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    only = None
    pool_path = repo_path('baseline', 'en-patches.json')
    strict = '--strict' in argv
    i = 0
    while i < len(argv):
        if argv[i] == '--slug' and i + 1 < len(argv):
            only = argv[i + 1]
            i += 2
        elif argv[i] == '--pool' and i + 1 < len(argv):
            pool_path = argv[i + 1]
            i += 2
        elif argv[i] == '--strict':
            i += 1
        else:
            sys.stderr.write(__doc__)
            return 2
    if not os.path.exists(pool_path):
        sys.stderr.write('[en-patches] 补丁池缺失: %s\n' % pool_path)
        return 2
    pool = json.load(open(pool_path, encoding='utf-8'))
    patches = pool.get('patches', [])
    bad = 0
    checked = 0
    admission_bad = 0
    field_bad = 0
    for p in patches:
        if only and p.get('slug') != only:
            continue
        missing = [f for f in REQUIRED_FIELDS if not str(p.get(f, '')).strip()]
        if missing:
            print('FIELD MISSING %s 补丁 %s 缺字段 %s'
                  % (p.get('slug', '?'), p.get('id', '?'), ",".join(missing)))
            field_bad += 1
            bad += 1
        kind = admission(p.get('find', ''), p.get('replace', ''))
        if kind is None:
            print('TEXT-LAYER %s 补丁 %s 改动词符或词序，禁入池（转全局勘误表＋译注）'
                  % (p.get('slug', '?'), p.get('id', '?')))
            admission_bad += 1
            if strict:
                bad += 1
        full = repo_path(p['file'])
        if not os.path.exists(full):
            print('MISSING FILE %s（补丁 %s）' % (p['file'], p.get('id', '?')))
            bad += 1
            continue
        html = open(full, encoding='utf-8', newline='').read()
        n = html.count(p['find'])
        checked += 1
        if n != p['expect']:
            print('MISMATCH %s 补丁 %s 命中 %d 次 expect %d（上游漂移？）'
                  % (p['slug'], p.get('id', '?'), n, p['expect']))
            bad += 1
    print(json.dumps({'schema': pool.get('schema'), 'patches': len(patches),
                      'checked': checked, 'mismatch': bad,
                      'admission_bad': admission_bad, 'field_bad': field_bad},
                     ensure_ascii=False))
    return 0 if bad == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

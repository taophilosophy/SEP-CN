#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补丁池目录正本离线校验（ADR-0062；ADR-0063 扩准入谓词与追溯）

用法: python tools/check_en_patches.py [--slug X] [--dir 路径] [--strict] [--no-git-check]

逐条校验 baseline/en-patches/*.patch（一补丁一文件，目录即事实源）在当前 en/ 上的
命中计数是否等于 expect，并复核 INDEX.json 与正本一致。失配即报——上游漂移或补丁
失效时，转换层（yuanwen.py）会硬失败；本工具供不转换时快速体检。

C2 准入谓词（唯一实现在 tools/en_patch_lib.py）：一条 find→replace 允许入池，
当且仅当下列至少其一成立
  (a) 空白差：去掉全部空白后 find ≡ replace（例 `Einstein1949b`→`Einstein 1949b`）
  (b) 标记差：剥除标签与注释后 find ≡ replace（例 补 `</div>`、`-->`）
二者皆不成立 ⇒ 改动落在字母数字或词序 ⇒ 文字层，禁入池、禁改 yuanwen。
`--strict` 时谓词不符即退出码 1；默认只报不拦（存量池体检用）。

独立校验：默认对每条补丁跑 `git apply --check`（只读预演，不写 en/），
上下文失配即报；`--no-git-check` 关闭（无 git 环境时用）。

追溯：每条补丁须有非空 `source`（指向全局勘误表条目）；INDEX.json 为生成物，
与正本不一致即红（禁止手改索引）。反向（勘误表格式层行须带补丁 id）待 P6
勘误表增列后启用——该表当前由并行会话持有，本工具先不读。

退出码: 0 全通过；1 有失配、谓词不符（--strict）或索引不一致；2 池目录缺失。
"""
import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import en_patch_lib  # noqa: E402
from tools.common import repo_path  # noqa: E402
from tools.en_patch_lib import admission  # noqa: E402,F401 （兼容旧导入；唯一实现在 en_patch_lib）


def _index_issues(base):
    """INDEX.json 与正本一致性：条数、id 集合、sha256。返回问题列表。"""
    issues = []
    idx_path = os.path.join(base, 'INDEX.json')
    if not os.path.exists(idx_path):
        return ['INDEX.json 缺失（生成物：跑 specs/039 bin/migrate_en_patches.py --refresh）']
    try:
        idx = json.load(open(idx_path, encoding='utf-8'))
    except Exception as ex:
        return ['INDEX.json 不可解析: %s' % ex]
    listed = {p.get('id'): p for p in idx.get('patches', [])}
    files = sorted(f for f in os.listdir(base) if f.endswith('.patch'))
    ids = {f[:-len('.patch')] for f in files}
    if set(listed) != ids:
        issues.append('INDEX 与正本 id 集合不一致：index=%s files=%s'
                      % (sorted(set(listed) - ids), sorted(ids - set(listed))))
    for fn in files:
        pid = fn[:-len('.patch')]
        path = os.path.join(base, fn)
        raw = open(path, encoding='utf-8', newline='').read()
        got = hashlib.sha256(raw.encode('utf-8')).hexdigest()
        want = (listed.get(pid) or {}).get('sha256')
        if want != got:
            issues.append('INDEX sha256 与正本不符：%s（跑 --refresh 再生）' % fn)
    return issues


def _git_check(path):
    r = subprocess.run(['git', 'apply', '--check', path], capture_output=True, text=True)
    return r.returncode == 0, (r.stderr or r.stdout).strip()


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    only = None
    base = en_patch_lib.patch_dir()
    strict = '--strict' in argv
    git_check = '--no-git-check' not in argv
    i = 0
    while i < len(argv):
        if argv[i] == '--slug' and i + 1 < len(argv):
            only = argv[i + 1]
            i += 2
        elif argv[i] == '--dir' and i + 1 < len(argv):
            base = argv[i + 1]
            i += 2
        elif argv[i] in ('--strict', '--no-git-check'):
            i += 1
        else:
            sys.stderr.write(__doc__)
            return 2
    if not os.path.isdir(base):
        sys.stderr.write('[en-patches] 补丁目录缺失: %s\n' % base)
        return 2
    patches = []
    for slug, items in sorted(en_patch_lib.load_patches(base).items()):
        if only and slug != only:
            continue
        patches.extend(items)
    bad = 0
    checked = 0
    admission_bad = 0
    index_bad = 0
    git_bad = 0
    for p in patches:
        kind = en_patch_lib.admission(p['find'], p['replace'])
        if kind is None:
            print('TEXT-LAYER %s 补丁 %s 改动词符或词序，禁入池（转全局勘误表＋译注）'
                  % (p['slug'], p['id']))
            admission_bad += 1
            if strict:
                bad += 1
        full = repo_path(p['file'])
        if not os.path.exists(full):
            print('MISSING FILE %s（补丁 %s）' % (p['file'], p['id']))
            bad += 1
            continue
        html = open(full, encoding='utf-8', newline='').read()
        n = html.count(p['find'])
        checked += 1
        if n != p['expect']:
            print('MISMATCH %s 补丁 %s 命中 %d 次 expect %d（上游漂移？）'
                  % (p['slug'], p['id'], n, p['expect']))
            bad += 1
        if git_check:
            ok, err = _git_check(p['patch_file'])
            if not ok:
                print('GIT-CHECK %s 补丁 %s 上下文不适用：%s'
                      % (p['slug'], p['id'], err.splitlines()[0] if err else ''))
                git_bad += 1
                bad += 1
    if not only:
        for msg in _index_issues(base):
            print('INDEX %s' % msg)
            index_bad += 1
            bad += 1
    print(json.dumps({'schema': 'sep-cn-en-patches-dir/1', 'patches': len(patches),
                      'checked': checked, 'mismatch': bad,
                      'admission_bad': admission_bad, 'index_bad': index_bad,
                      'git_check_bad': git_bad},
                     ensure_ascii=False))
    return 0 if bad == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

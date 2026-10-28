# -*- coding: utf-8 -*-
"""SUMMARY / mu-lu-s 目录同步（FR-021/022/023，用户 2026-10-27 三条裁定）。

政策：
- 词条为根级 <slug>.md 单文件（ADR-0008 词条文件化，英文侧 yuanwen/<slug>.md 镜像），
  文件名与 SEP slug 一致，Windows 不兼容字符换下划线；拼音文件名已随重建淘汰；
- 上游 slug 变更 → 中文文件名同步改；上游删除词条 → stub 一并删除；
- mu-lu-s 仅保留去重结果、按分类组织；归类与节内次序为编辑判断，工具不自动归类。

命令：
  report                     全量对比 → 目录裁决表 catalog-verdict.json（ADD/REMOVE/RENAME 候选）
  apply-add <slug> --title-zh "中文标题" [--file NAME]
                             建桩（H1=中文 英文 (作者)）+ SUMMARY 字母节按英文标题字母序插入
                             + baseline.zh_doc + yuanwen 转换
  apply-remove <slug> [--yes] SUMMARY 行删除 + stub 删除 + baseline/tasks/yuanwen 清理（默认 dry-run）
  apply-rename <slug> --new-slug NS [--yes]
                             文件名同步改：git mv + 全库链接改写 + SUMMARY 文字 slug 段更新
  mu-lu-s-dedupe             mu-lu-s 去重（保留首次出现，报告删除行）
  migrate-plan               存量拼音文件名 → slug 全库改名计划（dry-run JSON，不执行）

输出：人读进度走 stderr，结果 JSON 走 stdout；退出码 0 成功 / 1 失败 / 2 用法 / 3 前置不满足。
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import yuanwen as Y  # noqa: E402  (复用 parser/extract/convert 基础设施)
from tools.common import (  # noqa: E402
    find_zh_doc, load_json, read_text, repo_path, sha256_file, utcnow_iso,
    write_json_verified, write_text_verified)

SLUG_SAFE = re.compile(r'[^a-z0-9_-]')


def _upstream_doc_order():
    """上游 contents.html 最新快照中真条目（alias_of=None）的文档顺序。"""
    import glob
    from tools import parser as _parser
    snaps = sorted(glob.glob(repo_path('en', '_catalog', '*-contents.html')))
    if not snaps:
        return []
    p = _parser._CatalogHTMLParser()
    p.feed(open(snaps[-1], 'rb').read().decode('utf-8', 'replace'))
    p.close()
    seen, out = set(), []
    for it in p.items:
        if not it.get('alias_of') and it['slug'] not in seen:
            seen.add(it['slug'])
            out.append(it['slug'])
    return out


def _summary_slug_lines(lines):
    """SUMMARY 中各 slug 最后一条正式行 → {slug: (行号, 行)}。"""
    out = {}
    for i, l in enumerate(lines):
        m = re.match(r'^(\s*)\* \[(.*)\]\(([^)]*)\)\s*$', l)
        if not m:
            continue
        path = m.group(3)
        if not re.fullmatch(r'[a-z0-9]/[A-Za-z0-9][A-Za-z0-9.\-]*\.md', path):
            continue
        title = m.group(2)
        if '— see' in title or title.lstrip().startswith('*'):
            continue
        out[path.rsplit('/', 1)[-1][:-3]] = (i, l)
    return out


def slug_file(slug):
    """slug → 文件名（Windows 不兼容字符换下划线，FR-021）。"""
    return SLUG_SAFE.sub('_', slug)


def load_upstream():
    return load_json(repo_path('baseline', 'catalog.json'))['items']


def summary_lines():
    return read_text(repo_path('SUMMARY.md')).split('\n')


def write_summary_lines(lines):
    write_text_verified(repo_path('SUMMARY.md'), '\n'.join(lines))


def entry_from_baseline(slug):
    for r in load_json(repo_path('baseline', 'entries.json'))['entries']:
        if r['slug'] == slug:
            return r
    return None


def english_of(link_text):
    """SUMMARY 链接文字 '中文 English (Authors)' → 英文标题部分（排序键）。"""
    t = re.sub(r'\(([^)]*)\)\s*$', '', link_text).strip()
    t = re.sub(r'^[^A-Za-z0-9\*\[]*', '', t)   # 去掉开头的中文与 * 前缀
    return t.lower()


# --------------------------------------------------------------- report ----

def report():
    upstream = load_upstream()
    lines = summary_lines()
    mapped, add = {}, []
    for it in upstream:
        if it['alias_of']:
            continue
        zh = find_zh_doc(it['slug'], it['title'])
        if zh:
            mapped[it['slug']] = zh
        else:
            add.append({'slug': it['slug'], 'title_en': it['title'],
                        'authors': it['authors'],
                        'proposed_file': '%s/%s.md' % (it['slug'][0], slug_file(it['slug'])),
                        'disposition': 'ADD（需人工定中文标题）'})
    mapped_paths = set(mapped.values())
    # 反向标题索引：SUMMARY 英文标题 → 上游 slug（正向匹配漏掉的集群子词条在此回收）。
    # 同题歧义计数：上游多个词条同题（如五个 "*-political" 子词条同题
    # "political philosophy"）时，标题反查无法定案——此类行必须转人工裁定，
    # 不得静默放行（specs/007 审阅实证：political-philosophy 遗留桩因此漏检）。
    title_index = {}
    title_count = {}
    for it in upstream:
        t = re.sub(r'[^a-z0-9]+', '', it['title'].lower())
        if t:
            title_index.setdefault(t, it['slug'])
            title_count[t] = title_count.get(t, 0) + 1
    remove = []
    for idx, line in enumerate(lines):
        pm = re.search(r'\]\(([^)]+)\)', line)
        if not pm:
            continue
        path = pm.group(1)
        if not re.fullmatch(r'[a-z0-9]/[A-Za-z0-9][A-Za-z0-9.\-]*\.md', path):
            continue  # 仅 <letter>/<slug>.md 词条文件（ADR-0009 A–Z 字母目录）
        if '-see-' in path.lower():
            continue  # 别名 stub：上游别名无独立 slug，另行人工核对
        if path in mapped_paths:
            continue
        base = path.rsplit('/', 1)[-1].split('.')[0]
        en = english_of(re.search(r'\[([^\]]+)\]', line).group(1) if re.search(r'\[([^\]]+)\]', line) else base)
        rev = title_index.get(re.sub(r'[^a-z0-9]+', '', en))
        rev_ambiguous = title_count.get(re.sub(r'[^a-z0-9]+', '', en), 0) > 1
        if rev and not rev_ambiguous:
            continue  # 反向唯一命中：映射方向伪影，非真删除
        if rev_ambiguous:
            remove.append({'line': idx + 1, 'path': path,
                           'disposition': 'REMOVE/RENAME 候选（上游同题歧义，'
                                          '标题反查无法定案，需逐行人工裁定）'})
        remove.append({'line': idx + 1, 'path': path,
                       'disposition': 'REMOVE/RENAME 候选（上游无对应；'
                                      '若字母目录中有同义 ADD 则为改名对）'})
    # RENAME 配对：REMOVE 候选路径的目录字母 == ADD slug 首字母且英文标题相近
    out = {'generated_at': utcnow_iso(), 'add': add, 'remove': remove,
           'mapped': len(mapped)}
    write_json_verified(repo_path('specs/001-sep-sync-pipeline', 'catalog-verdict.json'), out)
    print(json.dumps({'add': len(add), 'remove': len(remove), 'mapped': len(mapped),
                      'verdict': 'specs/001-sep-sync-pipeline/catalog-verdict.json'},
                     ensure_ascii=False))
    return 0


# -------------------------------------------------------------- apply-add ---

def apply_add(slug, title_zh, file_name=None):
    rec = entry_from_baseline(slug)
    if rec is None:
        raise Precondition('词条 %s 不在基线，先 fetch_entry.py %s' % (slug, slug))
    if not rec.get('title'):
        raise Precondition('基线记录缺 title')
    fname = slug_file(file_name or slug)
    rel = '%s/%s.md' % (slug[0], fname)
    full = repo_path(rel)
    if os.path.exists(full):
        raise Precondition('目标文件已存在: %s' % rel)
    title_en = rec['title']
    authors = ', '.join(rec.get('authors') or [])
    link_text = ('%s %s (%s)' % (title_zh, title_en, authors)) if authors \
        else ('%s %s' % (title_zh, title_en))

    # 1) SUMMARY 插入：按上游目录文档顺序，锚定前驱/后继条目行（ADR-0009 字母目录，
    #    SUMMARY 行序镜像 contents.html，非纯字母序，不能按标题重排插入）
    lines = summary_lines()
    new_line = '* [%s](%s)' % (link_text, rel)
    ins, where = None, None
    order = _upstream_doc_order()
    if slug in order:
        idx = order.index(slug)
        prevs = [s for s in order[:idx][::-1] if s in _summary_slug_lines(lines)]
        nexts = [s for s in order[idx + 1:] if s in _summary_slug_lines(lines)]
        if prevs:
            i, l = _summary_slug_lines(lines)[prevs[0]]
            ins = i + 1
            where = 'after %s' % prevs[0]
        elif nexts:
            i, l = _summary_slug_lines(lines)[nexts[0]]
            ins = i
            where = 'before %s' % nexts[0]
        pr = re.match(r'^(\s*)\* \[', l) if (prevs or nexts) and l else None
        ind = len(pr.group(1)) if pr else 0
        new_line = ' ' * ind + new_line
    if ins is None:
        ins, where = len(lines), 'append（上游顺序无锚点，回退尾部）'
    lines.insert(ins, new_line)
    write_summary_lines(lines)
    print(json.dumps({'inserted_at': ins + 1, 'anchor': where}, ensure_ascii=False))

    # 2) 建桩（H1 与 SUMMARY 条目文字完全一致，file-name-check 零噪音）
    write_text_verified(full, '# %s\n' % link_text)

    # 3) baseline.zh_doc + yuanwen
    base = load_json(repo_path('baseline', 'entries.json'))
    for r in base['entries']:
        if r['slug'] == slug:
            r['zh_doc'] = rel
            break
    base['updated_at'] = utcnow_iso()
    write_json_verified(repo_path('baseline', 'entries.json'), base)
    Y.convert_entry(slug)

    print(json.dumps({'added': slug, 'file': rel, 'summary_line': ins + 1,
                      'link_text': link_text,
                      'todo': 'git add %s SUMMARY.md baseline/entries.json 后提交' % rel},
                     ensure_ascii=False, indent=2))
    return 0


# ----------------------------------------------------------- apply-remove --

def apply_remove(slug, yes=False):
    zh = find_zh_doc(slug)
    if not zh:
        raise Precondition('SUMMARY 中找不到 %s 的条目' % slug)
    plan = {'slug': slug, 'summary_line': zh, 'delete_file': zh,
            'policy': 'FR-022 上游删除→stub 一并删除'}
    # 全库引用扫描
    refs = []
    for root, dirs, files in os.walk(repo_path('.')):
        dirs[:] = [d for d in dirs if d not in ('.git', '.gitbook', 'node_modules',
                                                'en', 'script', 'yuanwen', '__pycache__')]
        for f in files:
            if f.endswith('.md'):
                fp = os.path.join(root, f)
                if zh in read_text(fp):
                    refs.append(os.path.relpath(fp, repo_path('.')))
    plan['referenced_by'] = refs
    if not yes:
        plan['note'] = 'dry-run：确认后加 --yes 执行'
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    lines = summary_lines()
    lines = [l for l in lines if not (zh in l and '](%s)' % zh in l)]
    write_summary_lines(lines)
    full = repo_path(zh)
    if os.path.exists(full):
        os.remove(full)
    base = load_json(repo_path('baseline', 'entries.json'))
    base['entries'] = [r for r in base['entries'] if r['slug'] != slug]
    base['updated_at'] = utcnow_iso()
    write_json_verified(repo_path('baseline', 'entries.json'), base)
    plan['executed'] = True
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


# ----------------------------------------------------------- apply-rename --

def apply_rename(slug, new_slug, yes=False):
    old_zh = find_zh_doc(slug)
    if not old_zh:
        raise Precondition('SUMMARY 中找不到 %s' % slug)
    new_zh = '%s/%s.md' % (new_slug[0], slug_file(new_slug))
    old_full, new_full = repo_path(old_zh), repo_path(new_zh)
    plan = {'slug': slug, 'new_slug': new_slug, 'old': old_zh, 'new': new_zh,
            'policy': 'FR-022 文件名同步改'}
    refs = []
    for root, dirs, files in os.walk(repo_path('.')):
        dirs[:] = [d for d in dirs if d not in ('.git', '.gitbook', 'node_modules',
                                                'en', 'script', '__pycache__')]
        for f in files:
            if f.endswith('.md'):
                fp = os.path.join(root, f)
                if old_zh in read_text(fp):
                    refs.append(os.path.relpath(fp, repo_path('.')))
    plan['links_to_rewrite'] = refs
    if not yes:
        plan['note'] = 'dry-run：确认后加 --yes 执行'
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    subprocess.run(['git', 'mv', old_zh.replace('/', os.sep), new_zh.replace('/', os.sep)],
                   check=True, cwd=repo_path('.'))
    for rel in refs:
        fp = repo_path(rel)
        t = read_text(fp).replace(old_zh, new_zh)
        if rel == 'SUMMARY.md':
            # 链接文字中的旧 slug 段同步更新（如 "... old-slug (Author)" → new-slug）
            t = re.sub(r'(?<![\w-])%s(?![\w-])' % re.escape(slug), new_slug, t)
        write_text_verified(fp, t)
    base = load_json(repo_path('baseline', 'entries.json'))
    for r in base['entries']:
        if r['slug'] == slug:
            r['slug'] = new_slug
            r['zh_doc'] = new_zh
    base['updated_at'] = utcnow_iso()
    write_json_verified(repo_path('baseline', 'entries.json'), base)
    plan['executed'] = True
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


# ---------------------------------------------------------- mu-lu-s -------

def mu_lu_s_dedupe():
    path = repo_path('mu-lu-s.md')
    lines = read_text(path).split('\n')
    seen, out, removed = set(), [], []
    for l in lines:
        pm = re.search(r'\]\(([^)]+)\)', l)
        if pm and pm.group(1) in seen and l.lstrip().startswith('*'):
            removed.append(l.strip()[:80])
            continue
        if pm:
            seen.add(pm.group(1))
        out.append(l)
    if removed:
        write_text_verified(path, '\n'.join(out))
    print(json.dumps({'duplicates_removed': len(removed), 'lines': removed},
                     ensure_ascii=False, indent=2))
    return 0


# --------------------------------------------------------- migrate-plan ----

def migrate_plan():
    upstream = load_upstream()
    plan, phase2 = [], []
    for it in upstream:
        if it['alias_of']:
            continue
        zh = find_zh_doc(it['slug'], it['title'])
        if not zh:
            continue
        base = zh.rsplit('/', 1)
        if base[1] == 'README.md':
            new = '%s/README.md' % slug_file(it['slug'])
        elif '/' in zh.strip('/') and len(base) == 2 and base[0] != it['slug'][0]:
            # 集群子词条：目录需改为父 slug，子文件名映射属第二阶段（需子词条 slug 对应）
            phase2.append({'old': zh, 'parent_dir': base[0]})
            continue
        else:
            new = '%s/%s.md' % (it['slug'][0], slug_file(it['slug']))
        if new != zh:
            plan.append({'old': zh, 'new': new, 'slug': it['slug']})
    out = {'generated_at': utcnow_iso(), 'renames': plan,
           'phase2_cluster_children': len(phase2),
           'note': 'dry-run 计划；执行需 git mv + 全库链接改写，且应等并行会话停止写入后进行'}
    write_json_verified(repo_path('specs/001-sep-sync-pipeline', 'migration-plan.json'), out)
    print(json.dumps({'file_renames': len(plan), 'phase2_cluster_children': len(phase2)},
                     ensure_ascii=False))
    return 0


class Precondition(Exception):
    pass


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        if not argv:
            print(__doc__)
            return 2
        cmd = argv[0]
        if cmd == 'report':
            return report()
        if cmd == 'apply-add':
            slug = argv[1]
            tz = None
            fn = None
            for i, a in enumerate(argv):
                if a == '--title-zh':
                    tz = argv[i + 1]
                if a == '--file':
                    fn = argv[i + 1]
            if not tz:
                raise Precondition('apply-add 需要 --title-zh "中文标题"（翻译裁定）')
            return apply_add(slug, tz, fn)
        if cmd == 'apply-remove':
            return apply_remove(argv[1], '--yes' in argv)
        if cmd == 'apply-rename':
            slug, ns = argv[1], None
            for i, a in enumerate(argv):
                if a == '--new-slug':
                    ns = argv[i + 1]
            if not ns:
                raise Precondition('apply-rename 需要 --new-slug')
            return apply_rename(slug, ns, '--yes' in argv)
        if cmd == 'mu-lu-s-dedupe':
            return mu_lu_s_dedupe()
        if cmd == 'migrate-plan':
            return migrate_plan()
        print(json.dumps({'error': '未知命令 %s' % cmd}, ensure_ascii=False))
        return 2
    except Precondition as e:
        print(json.dumps({'error': str(e)}, ensure_ascii=False))
        return 3


if __name__ == '__main__':
    sys.exit(main())

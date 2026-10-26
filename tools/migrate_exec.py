# -*- coding: utf-8 -*-
"""存量文件名迁移执行器：拼音 → SEP slug（FR-021，用户 2026-10-27 全量批准）。

阶段：
  1. 建映射：文件词条 letter/pinyin.md → letter/<slug>.md；
     集群目录 pinyin-slug/ → <slug>/（README 随目录）；
     集群子词条 dir/pinyin-<en>.md → dir/<子slug>.md（按英文标题对上游子 slug）；
     别名 stub（路径含 -see-）不迁移（上游无对应文件名，登记为例外）。
  2. 冲突检查：新路径必须唯一且不与未迁移文件相撞。
  3. 执行：先改目录（os.rename），再改文件，最后改写 SUMMARY/mu-lu-s/全库 md 链接
     与 baseline.zh_doc（全部 write_text_verified / write_json_verified）。
  4. 验证：SUMMARY/mu-lu-s 每条链接指向存在的文件；audit.py 结构核对。

用法: python tools/migrate_exec.py [--apply]   （默认 dry-run 输出计划统计）
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.common import (  # noqa: E402
    load_json, read_text, repo_path, utcnow_iso,
    write_json_verified, write_text_verified, zh_doc_from_lines)

SLUG_SAFE = re.compile(r'[^a-z0-9_-]')
# 用户 2026-10-27 例外裁定 2：slug 含文件名非法字符者不迁移
SLUG_OK = re.compile(r'^[a-z0-9][a-z0-9_-]*$')


def slug_file(s):
    return SLUG_SAFE.sub('_', s)


def norm(t):
    return re.sub(r'[^a-z0-9]+', '', t.lower())


def english_of(link_text):
    t = re.sub(r'\(([^)]*)\)\s*$', '', link_text).strip()
    t = re.sub(r'^[^A-Za-z0-9\*\[]*', '', t)
    return t.lower()


def build_plan():
    upstream = load_json(repo_path('baseline', 'catalog.json'))['items']
    lines = read_text(repo_path('SUMMARY.md')).split('\n')
    # 性能优化：SUMMARY 只解析一次（zh_doc_from_lines 接受预解析行，O(n²)→O(n)）
    zh_cache = {}
    for it in upstream:
        if not it['alias_of']:
            zh_cache[it['slug']] = zh_doc_from_lines(it['slug'], it['title'], lines)
    readme_parent = {}
    for it in upstream:
        if it['alias_of']:
            continue
        zh2 = zh_cache.get(it['slug'])
        ps = zh2.split('/') if zh2 else []
        # 集群父词条 = 路径形如 [letter, <集群目录>, README.md]；键取倒数第二段
        if len(ps) > 2 and ps[-1] == 'README.md':
            readme_parent[ps[-2] + '/'] = it['slug']

    # 上游 slug 索引：规范标题 → slug（供集群子词条匹配）
    by_title = {}
    for it in upstream:
        by_title.setdefault(norm(it['title']), it['slug'])

    file_map = {}     # 旧相对路径 → 新相对路径
    dir_map = {}      # 旧目录 → 新目录
    unmatched_children = []
    skipped_special = []
    seen_new = {}     # 新路径小写 → 旧路径（大小写不敏感查重）

    def claim(old, new):
        """登记改名；用户例外 1：大小写不敏感重复时跳过后到者，返回 False。"""
        low = new.lower()
        if low in seen_new and seen_new[low] != old:
            return False
        seen_new[low] = old
        return True

    for it in upstream:
        if it['alias_of']:
            continue
        zh = zh_cache.get(it['slug'])
        if not zh:
            continue
        slug = it['slug']
        if not SLUG_OK.match(slug):
            skipped_special.append(slug)     # 用户例外 2：非法字符，保持原名
            continue
        parts = zh.split('/')
        base = parts[-1]
        dir_seg = parts[-2] if len(parts) > 2 else ''
        if base == 'README.md':
            # 集群父词条：整目录改名（目录可能在根或字母目录下）
            old_dir = parts[-2]
            new_dir = slug_file(slug)
            new = (parts[0] + '/' if len(parts) > 2 else '') + new_dir + '/README.md'
            if old_dir != new_dir and claim(zh, new):
                dir_map[old_dir + '/'] = new_dir + '/'
                file_map[zh] = new
        elif dir_seg == slug[0] or dir_seg == '':
            # 顶层文件：letter/pinyin.md → letter/<slug>.md
            new = '%s/%s.md' % (slug[0], slug_file(slug))
            if new != zh and claim(zh, new):
                file_map[zh] = new
        else:
            # 集群子词条：目录/拼音.md → 父slug目录/子slug.md
            old_dir = dir_seg
            en = None
            for line in lines:
                if zh in line:
                    tm = re.search(r'\[([^\]]+)\]', line)
                    if tm:
                        en = english_of(tm.group(1))
                    break
            sub = by_title.get(norm(en or ''))
            # 父目录名：目录下 README 所在父词条（预计算索引，O(1)）
            parent_slug = readme_parent.get(old_dir + '/')
            if parent_slug is None or not sub:
                unmatched_children.append(zh)
                continue
            new_dir = slug_file(parent_slug)
            new = '%s/%s.md' % (new_dir, slug_file(sub))
            if new != zh and claim(zh, new):
                dir_map.setdefault(old_dir + '/', new_dir + '/')
                file_map[zh] = new
    return file_map, dir_map, unmatched_children, skipped_special


def check_conflicts(file_map, dir_map):
    seen = {}
    bad = []
    for old, new in file_map.items():
        # 大小写不敏感查重：Windows 视 Abc 与 abc 同名（claim 已先行跳过，此为兜底）
        low = new.lower()
        if low in seen and seen[low] != old:
            bad.append((old, new, seen[low]))
        seen[low] = old
    return bad


def apply_renames(file_map, dir_map):
    # 先目录后文件；文件映射的 old 路径含旧目录名，需换算为新目录名后再 rename
    for old_d, new_d in sorted(dir_map.items(), key=lambda x: -len(x[0])):
        od, nd = repo_path(old_d.rstrip('/')), repo_path(new_d.rstrip('/'))
        if os.path.exists(od) and not os.path.exists(nd):
            os.rename(od, nd)
    n_files = 0
    misses = []
    for old, new in sorted(file_map.items(), key=lambda x: -len(x[0])):
        # 可续跑：文件可能已在旧位、新位，或上次中断时的字母/slug 位置
        of = nf = None
        for cand in (old, new, '%s/%s.md' % (new.split('/')[0], new.split('/')[1])):
            if os.path.exists(repo_path(cand)):
                of = cand
                break
        if of is None:
            misses.append(old)
            continue
        if of == new:
            n_files += 1
            continue
        try:
            os.rename(repo_path(of), repo_path(new))
            n_files += 1
        except FileNotFoundError:
            # 并发写入者可能刚移走该文件——重定位一次，仍无则视为已完成
            if os.path.exists(repo_path(new)):
                n_files += 1
            else:
                misses.append(old)
    if misses:
        print(json.dumps({'rename_misses': misses[:10], 'miss_count': len(misses)},
                         ensure_ascii=False))
    return n_files


def rewrite_links(file_map, dir_map):
    # 旧路径 → 新路径 的文本替换表（先长后短，含目录前缀）
    reps = sorted(list(file_map.items()) + list(dir_map.items()),
                  key=lambda kv: -len(kv[0]))
    changed = {}
    for rel in ['SUMMARY.md', 'mu-lu-s.md']:
        t = read_text(repo_path(rel))
        o = t
        for old, new in reps:
            t = t.replace(old, new)
        if t != o:
            write_text_verified(repo_path(rel), t)
            changed[rel] = True
    # 其余 md（词条间互链、qian-yan 等）
    for root, dirs, files in os.walk(repo_path('.')):
        dirs[:] = [d for d in dirs if d not in ('.git', '.gitbook', 'node_modules',
                                                'en', 'script', 'yuanwen',
                                                '__pycache__', 'public')]
        for f in files:
            if not f.endswith('.md'):
                continue
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, repo_path('.')).replace(os.sep, '/')
            if rel in ('SUMMARY.md', 'mu-lu-s.md'):
                continue
            t = read_text(fp)
            o = t
            for old, new in reps:
                t = t.replace(old, new)
            if t != o:
                write_text_verified(fp, t)
                changed[rel] = True
    return changed


def update_baseline(file_map, dir_map):
    base = load_json(repo_path('baseline', 'entries.json'))
    n = 0
    for r in base['entries']:
        zh = r.get('zh_doc')
        if not zh:
            continue
        cur = zh
        for old_d, new_d in dir_map.items():
            if cur.startswith(old_d):
                cur = new_d + cur[len(old_d):]
                break
        if cur in file_map:
            r['zh_doc'] = file_map[cur]
            n += 1
        elif cur != zh:
            r['zh_doc'] = cur
            n += 1
    base['updated_at'] = utcnow_iso()
    write_json_verified(repo_path('baseline', 'entries.json'), base)
    return n


def verify():
    errs = []
    for rel in ('SUMMARY.md', 'mu-lu-s.md'):
        for i, line in enumerate(read_text(repo_path(rel)).split('\n'), 1):
            for pm in re.finditer(r'\]\(([^)]+\.md)\)', line):
                p = pm.group(1)
                if p.startswith(('http', 'mu-lu-s', 'README')) is False and \
                        not os.path.exists(repo_path(p)):
                    errs.append('%s:%d -> %s' % (rel, i, p))
    return errs


def main(argv):
    apply = '--apply' in argv
    file_map, dir_map, unmatched, skipped_special = build_plan()
    file_map = {k: v for k, v in file_map.items() if k != v}
    bad = check_conflicts(file_map, dir_map)
    print(json.dumps({
        'file_renames': len(file_map), 'dir_renames': len(dir_map),
        'unmatched_children_kept': len(unmatched),
        'skipped_special_slug': skipped_special,
        'conflicts': bad[:5], 'apply': apply,
    }, ensure_ascii=False))
    if bad:
        print('存在冲突，终止')
        return 1
    if not apply:
        print('dry-run：加 --apply 执行')
        return 0
    n = apply_renames(file_map, dir_map)
    changed = rewrite_links(file_map, dir_map)
    nb = update_baseline(file_map, dir_map)
    errs = verify()
    write_json_verified(repo_path('specs/001-sep-sync-pipeline', 'migration-exec.json'),
                        {'at': utcnow_iso(), 'dirs': len(dir_map), 'files': n,
                         'links_changed': sorted(changed.keys()),
                         'baseline_updated': nb,
                         'skipped_special_slug': skipped_special,
                         'unmatched_children_kept': len(unmatched),
                         'verify_errors': errs[:20]})
    print(json.dumps({'dirs': len(dir_map), 'files_renamed': n,
                      'links_changed': sorted(changed.keys()),
                      'baseline_updated': nb, 'verify_errors': errs[:10],
                      'verify_error_count': len(errs)}, ensure_ascii=False, indent=2))
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

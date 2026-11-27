# -*- coding: utf-8 -*-
"""本地垃圾清理器（ADR-0003）：删除工作区中未跟踪的缓存与临时文件。

用法:
  python tools/clean.py                    # 试运行：列出将删除的目标，退出 0
  python tools/clean.py --check            # 只读检查：列出目标，退出 0（有垃圾也不拦）
  python tools/clean.py --check --strict   # 只读检查：保护件缺失/越界风险退 1
  python tools/clean.py --go               # 实际删除未跟踪垃圾

安全边界:
  - 只删未跟踪的杂物（对照 git ls-files，跟踪文件绝不触碰）；
  - 跳过 .git/、node_modules/、en/、yuanwen/、baseline/、script/、.specify/、.zcode/；
  - 垃圾目录整体作为目标（target/、__pycache__、pytest/mypy/ruff 缓存、
    .vitepress/cache|dist），不逐个枚举其内部文件；
  - 保护件（en/、yuanwen/、zh/、baseline/、zh/SUMMARY.md）缺失或目标越界时，--strict 退 1。

退出码: 0 成功/只读正常；1 --strict 发现保护件缺失或越界风险；2 用法错误。
"""
import argparse
import os
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {'.git', 'node_modules', 'en', 'yuanwen', 'baseline', 'script',
             '.specify', '.zcode'}
PROTECTED_PATHS = ('en', 'yuanwen', 'zh', 'baseline', 'zh/SUMMARY.md')
JUNK_DIRS = {'__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache',
             'target', '.screenshots'}
JUNK_DIR_PREFIXES = ('.vitepress/cache', '.vitepress/dist')
JUNK_FILES = {'.DS_Store', 'Thumbs.db', 'desktop.ini'}
JUNK_SUFFIXES = ('.pyc', '.pyo', '.tmp', '.bak', '.swp', '.log')


def tracked_set():
    out = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT,
                         capture_output=True, check=True).stdout
    return {p.decode('utf-8') for p in out.split(b'\0') if p}


def posix(rel):
    return rel.replace(os.sep, '/')


def under(rel, prefixes):
    rel = posix(rel)
    return any(rel == p or rel.startswith(p + '/') for p in prefixes)


def is_junk_file(rel, name):
    if name in JUNK_FILES:
        return True
    if name.endswith(JUNK_SUFFIXES):
        return True
    return under(rel, JUNK_DIR_PREFIXES)


def is_junk_dir(rel, name):
    if name in JUNK_DIRS:
        return True
    return under(rel, JUNK_DIR_PREFIXES)


def has_tracked_under(rel, tracked):
    prefix = posix(rel) + '/'
    return any(t.startswith(prefix) for t in tracked)


def collect(tracked):
    """返回 [(full, rel, kind)]，kind=dir|file；不进入垃圾目录内部。"""
    targets = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        top = rel_dir.split(os.sep)[0] if rel_dir != '.' else ''
        if top in SKIP_DIRS:
            dirnames[:] = []
            continue

        keep = []
        for d in dirnames:
            rel = d if rel_dir == '.' else os.path.join(rel_dir, d)
            if d in SKIP_DIRS:
                continue
            if is_junk_dir(rel, d):
                if not has_tracked_under(rel, tracked):
                    targets.append((os.path.join(dirpath, d), posix(rel), 'dir'))
                continue
            keep.append(d)
        dirnames[:] = keep

        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = posix(os.path.relpath(full, ROOT))
            if rel in tracked:
                continue
            if is_junk_file(rel, fn):
                targets.append((full, rel, 'file'))

    targets.sort(key=lambda x: x[1])
    return targets


def protected_issues(targets):
    issues = []
    for p in PROTECTED_PATHS:
        if not os.path.exists(os.path.join(ROOT, p)):
            issues.append('保护件缺失：%s' % p)
    for _, rel, _ in targets:
        if under(rel, PROTECTED_PATHS):
            issues.append('越界目标：%s' % rel)
    return issues


def delete(targets):
    failures = []
    for full, rel, kind in targets:
        try:
            if kind == 'dir':
                shutil.rmtree(full)
            else:
                os.remove(full)
        except OSError as e:
            failures.append('%s：%s' % (rel, e))
    return failures


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='清理未跟踪缓存与临时文件（ADR-0003）')
    parser.add_argument('--check', action='store_true',
                        help='只读检查，发现垃圾也退 0')
    parser.add_argument('--strict', action='store_true',
                        help='只读检查；保护件缺失或目标越界退 1')
    parser.add_argument('--go', action='store_true', help='实际删除')
    args = parser.parse_args(argv)

    if args.go and (args.check or args.strict):
        parser.error('--go 不能与 --check/--strict 同用')

    tracked = tracked_set()
    targets = collect(tracked)
    if targets:
        label = '删除' if args.go else '只读检查：发现'
        print('%s %d 项目标：%s' % (
            label, len(targets),
            ', '.join(rel for _, rel, _ in targets[:15]) +
            ('…' if len(targets) > 15 else '')))
    else:
        print('未发现本地垃圾。')

    if args.strict:
        issues = protected_issues(targets)
        if issues:
            for issue in issues:
                print(issue)
            return 1

    if args.go:
        failures = delete(targets)
        if failures:
            for failure in failures:
                print('删除失败：%s' % failure)
            return 1
        if targets:
            print('已清理。')
    return 0


if __name__ == '__main__':
    sys.exit(main())

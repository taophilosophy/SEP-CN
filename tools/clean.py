# -*- coding: utf-8 -*-
"""本地垃圾清理器（ADR-0003）：删除工作区中未跟踪的缓存与临时文件。

用法: python tools/clean.py            # 试运行：仅列出将删除的目标
      python tools/clean.py --go      # 实际删除
安全边界:
  - 只删未跟踪的杂物（对照 git ls-files，跟踪文件绝不触碰）；
  - 跳过 .git/、node_modules/（体积大但可重建，删除需重装，不属垃圾）、
    en/（原始抓取物，受宪法 II 保护）、script/（个人草稿区，自行管理）、
    .specify/ 与 .zcode/（工具脚手架）；
  - .pyc 等；VitePress 构建产物；系统与编辑器杂物。
退出码: 0 成功（含试运行）。
"""
import io
import os
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {'.git', 'node_modules', 'en', 'script', '.specify', '.zcode'}
JUNK_DIRS = {'__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache'}
JUNK_DIR_PREFIXES = (os.path.join('.vitepress', 'cache') + os.sep,
                     os.path.join('.vitepress', 'dist') + os.sep)
JUNK_FILES = {'.DS_Store', 'Thumbs.db', 'desktop.ini'}
JUNK_SUFFIXES = ('.pyc', '.pyo', '.tmp', '.bak', '.swp', '.log')


def tracked_set():
    out = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT,
                         capture_output=True, check=True).stdout
    return {p.decode('utf-8') for p in out.split(b'\0') if p}


def is_junk(rel, name):
    if name in JUNK_DIRS:
        return True
    if name in JUNK_FILES:
        return True
    if name.endswith(JUNK_SUFFIXES):
        return True
    if rel.replace(os.sep, '/').startswith(tuple(p.replace(os.sep, '/') for p in JUNK_DIR_PREFIXES)):
        return True
    return False


def main():
    go = '--go' in sys.argv
    tracked = tracked_set()
    targets = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        top = rel_dir.split(os.sep)[0] if rel_dir != '.' else ''
        if top in SKIP_DIRS or rel_dir == '.' and False:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames
                       if d not in SKIP_DIRS and d not in JUNK_DIRS
                       and os.path.join(rel_dir, d).replace(os.sep, '/') not in
                       tuple(p.rstrip(os.sep) for p in JUNK_DIR_PREFIXES)]
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT).replace(os.sep, '/')
            if rel in tracked:
                continue
            if is_junk(rel, fn):
                targets.append(full)

    if not targets:
        print('未发现本地垃圾。')
        return 0
    size = sum(os.path.getsize(t) for t in targets if os.path.isfile(t))
    print('%s %d 项目标（约 %.1f KB）：%s' %
          ('删除' if go else '将删除（试运行，加 --go 执行）', len(targets),
           size / 1024, ', '.join(os.path.relpath(t, ROOT) for t in targets[:15]) +
           ('…' if len(targets) > 15 else '')))
    if go:
        for t in targets:
            if os.path.isdir(t):
                os.rmdir(t) if not os.listdir(t) else None
            else:
                os.remove(t)
        # 自底向上清掉空掉的缓存目录
        for dirpath, dirnames, filenames in os.walk(ROOT):
            if os.path.basename(dirpath) in JUNK_DIRS and not os.listdir(dirpath):
                os.rmdir(dirpath)
        print('已清理。')
    return 0


if __name__ == '__main__':
    sys.exit(main())

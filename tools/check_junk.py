# -*- coding: utf-8 -*-
"""垃圾入库门禁（ADR-0003）：扫描 git 跟踪清单，命中垃圾/产物模式即非零退出。

用法: python tools/check_junk.py
规则: 原始抓取物（en/）、运行时报告（.github/sep-sync-report/）、字节码缓存、
      构建产物（node_modules、.vitepress/cache|dist、.astro、.turbo、dist、coverage）、
      系统与编辑器杂物（.DS_Store、Thumbs.db、desktop.ini、*~、*.swp、*.tmp、*.bak、*.log）
      一律不得入库。可入库的事实源：baseline/、.github/sep-baseline/、PROGRESS.md（生成但受控）。
豁免: 无——命中即硬错误，由人工 git rm --cached 并补忽略规则。
退出码: 0 无垃圾入库；1 命中。
"""
import io
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATTERNS = [
    (r'(^|/)__pycache__/', 'Python 字节码缓存'),
    (r'\.(pyc|pyo)$', 'Python 字节码'),
    (r'\.log$', '日志'),
    (r'\.tmp$', '临时文件'),
    (r'\.bak$', '备份文件'),
    (r'\.swp$', '编辑器交换文件'),
    (r'~$', '编辑器备份'),
    (r'(^|/)\.DS_Store$', 'macOS 桌面杂物'),
    (r'(^|/)Thumbs\.db$', 'Windows 缩略图缓存'),
    (r'(^|/)desktop\.ini$', 'Windows 桌面配置'),
    (r'^node_modules/', 'npm 依赖（构建产物）'),
    (r'^\.vitepress/(cache|dist)/', 'VitePress 构建产物'),
    (r'^\.astro/', 'Astro 构建产物'),
    (r'^\.turbo/', 'Turbo 缓存'),
    (r'^dist/', '构建输出'),
    (r'^coverage/', '测试覆盖率输出'),
    (r'^\.(pytest_cache|mypy_cache|ruff_cache)/', '工具缓存'),
    (r'^en/', '原始抓取物（宪法 II / FR-014：仅存本地）'),
    (r'^\.github/sep-sync-report/', '同步检查运行时报告'),
    (r'^[^/]+\.html$', '根级 HTML 残留（站点页面误抓，仓库无合法根级 html；2026-10-27 audit 教训）'),
]


def tracked_files():
    out = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT,
                         capture_output=True, check=True).stdout
    return [p.decode('utf-8') for p in out.split(b'\0') if p]


def main():
    hits = []
    for path in tracked_files():
        for pat, why in PATTERNS:
            if re.search(pat, path):
                hits.append((path, why))
                break
    if hits:
        print('垃圾/产物入库：%d 个文件（退出码 1，需 git rm --cached 并补忽略）' % len(hits))
        for path, why in hits[:50]:
            print('  %s  <-  %s' % (path, why))
        if len(hits) > 50:
            print('  … 其余 %d 个略' % (len(hits) - 50))
        return 1
    print('垃圾/产物入库检查：0 命中（跟踪文件 %d 个）' % len(tracked_files()))
    return 0


if __name__ == '__main__':
    sys.exit(main())

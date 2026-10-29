# -*- coding: utf-8 -*-
"""加粗坍缩扫描器（specs/007 事故固化，2026-10-30）。

背景：先前会话某个加粗处理脚本以跨行正则吞掉了相邻加粗 span 之间的文本
（含段内前缀与整段），波及 abduction/abelard/abner-burgos（工作区，已按
HEAD 恢复）与 abhidharma Cox 段、abortion 两列表项（已入库，按 git 原文/
EN 源重建）。para_align 只对块配对、不比对块内文字，对这类坍缩免疫——
本扫描器是补偿性控制。

签名（命中即候选，需人工对照 yuanwen/HEAD 裁定）：
  A  pubinfo 行 `** 首次发表于 ……**` 后仍跟正文（段首坍缩并入）
  B  同行两个加粗 span 仅隔空白（跨 span 吞并残留）
  C  段首加粗 `** ……**`（前缀丢失候选；豁免已登记合法形态）

用法: python specs/007-review-campaign/bin/check_bold_collapse.py [路径...]
退出码: 0 无候选；1 有候选（人工裁定）；2 用法错误。
"""
import io
import os
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SIG_PUB = re.compile(r'^\*\* 首次发表于[^\n]*\*\*\s*\S')
SIG_PAIR = re.compile(r'\*\*[^*\n]+?\*\*\s+\*\*[^*\n]+?\*\*')
SIG_HEAD = re.compile(r'^\*\* [^*]+\*\*(?:\s|$)')
# 已裁定合法的段首加粗形态（登记册）
EXEMPT_PREFIX = ('** 首次发表于', '** 以下文献', '** （译注', '** [', '**I.**')
SKIP_DIRS = {'.git', 'node_modules', 'en', 'yuanwen', 'baseline',
             '.vitepress', 'tools', '.zcode', '.specify', 'specs', 'tasks'}


def scan(paths):
    hits = []
    if paths:
        it = [Path(p) for p in paths]
    else:
        it = []
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in files:
                if f.endswith('.md'):
                    it.append(Path(root, f))
    for p in it:
        try:
            for i, l in enumerate(open(p, encoding='utf-8'), 1):
                ls = l.strip()
                if SIG_PUB.match(ls):
                    hits.append((p.as_posix(), i, 'A', ls[:90]))
                elif SIG_PAIR.search(ls):
                    hits.append((p.as_posix(), i, 'B', ls[:90]))
                elif SIG_HEAD.match(ls) and not ls.startswith(EXEMPT_PREFIX) \
                        and not re.match(r'^\*\*[IVX]+\.\*\*', ls):
                    hits.append((p.as_posix(), i, 'C', ls[:90]))
        except (OSError, UnicodeDecodeError) as e:
            print('[跳过] %s: %s' % (p, e))
    return hits


def main(argv):
    paths = [a for a in argv if not a.startswith('-')]
    hits = scan(paths)
    for f, i, k, t in hits:
        print('%s:%d [%s] %s' % (f, i, k, t))
    print('候选 %d 行（0=通过；候选需人工对照 yuanwen/HEAD 裁定）' % len(hits))
    return 1 if hits else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

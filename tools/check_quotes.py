# -*- coding: utf-8 -*-
"""文本卫生总检：直角引号（rules/02-style.md 第 11 条）＋ 合并冲突标记残留。

为何单列一具：`check_style.py` 已有 curly-quotes 规则但只对单篇词条跑
（--docs 模式），登记册、词汇表、规则与叙事文档从不经过它，导致 2026-11-10
在三个受跟踪文件里积出 536 处直角引号而门禁全绿。本具把该条按全库扫描补上。

范围：`git ls-files '*.md'` 全量，剔除
  * en/、yuanwen/  —— 英文原始抓取与镜像（源语言文本，非我方译文）；
  * specs/         —— 历史执行记录（既成事实存档，改则失真）；
  * .zcode/        —— 工具状态目录；
  * node_modules/  —— 依赖；
  * ALLOW_FILES    —— 日文正字法书名等（ADR-0011 引文原文语言还原）。

用法:
  python tools/check_quotes.py            # 全库扫描
  python tools/check_quotes.py --quiet    # 仅汇总
退出码: 0 无违例；1 有违例；4 git 不可用。
"""
import io
import os
import subprocess
import sys

if getattr(sys.stdout, 'encoding', None) and sys.stdout.encoding.lower() not in ('utf-8', 'utf8'):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAD = {'\u300c': 'U+300C 「', '\u300d': 'U+300D 」',
       '\u300e': 'U+300E 『', '\u300f': 'U+300F 』'}
# 合并/储藏冲突标记：行首七连符号（`=======` 是 setext 标题下划线，不查）
MARKERS = ('<<<<<<< ', '>>>>>>> ', '||||||| ')
EXCLUDE_PREFIX = ('en/', 'yuanwen/', 'specs/', '.zcode/', 'node_modules/')
ALLOW_FILES = {
    # 日文书名「切れ」の構造：日文正字法，改成弯引号即失真（ADR-0011）
    'j/japanese-aesthetics.md',
}


def tracked_md():
    try:
        r = subprocess.run(['git', '-c', 'core.quotepath=false', 'ls-files', '-z', '*.md'],
                           cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    except OSError:
        return None
    if r.returncode != 0:
        return None
    return [p for p in r.stdout.split('\x00') if p]


def scan(root, files, allow=ALLOW_FILES):
    """返回 (hits, allowed_count)。hits=[(rel, lineno, [标签], 摘录)]。"""
    hits, allowed = [], 0
    for rel in files:
        if rel.startswith(EXCLUDE_PREFIX):
            continue
        path = os.path.join(root, rel)
        try:
            with io.open(path, encoding='utf-8') as f:
                text = f.read()
        except (OSError, UnicodeDecodeError) as e:
            print('读取失败：%s（%s）' % (rel, e))
            continue
        for i, line in enumerate(text.split('\n'), 1):
            if line.startswith(MARKERS):
                hits.append((rel, i, ['合并冲突标记'], line.strip()[:60]))
                continue
            found = [BAD[ch] for ch in line if ch in BAD]
            if not found:
                continue
            if rel in allow:
                allowed += len(found)
                continue
            hits.append((rel, i, found, line.strip()[:60]))
    return hits, allowed


def main(argv=None):
    quiet = '--quiet' in (argv or sys.argv[1:])
    files = tracked_md()
    if files is None:
        print('git ls-files 不可用，无法确定扫描范围（退出码 4）')
        return 4
    hits, allowed_hit = scan(ROOT, files)
    files_hit = {h[0] for h in hits}
    for rel, lineno, found, snippet in hits:
        print('%s:%d  直角引号 %s：%s' % (rel, lineno, '、'.join(found), snippet))
    n = sum(len(h[2]) for h in hits)
    if not quiet or n:
        print('违例：%d 处 / %d 文件（其中直角引号 %d 处；豁免 %d 处，日文正字法）'
              % (n, len(files_hit), n - sum(1 for h in hits if h[2] == ['合并冲突标记']),
                 allowed_hit))
        print('处置：直角引号改弯引号（“”‘’），见 rules/02-style.md 第 11 条；'
              '冲突标记须解决后重提交')
    return 1 if n else 0


if __name__ == '__main__':
    sys.exit(main())

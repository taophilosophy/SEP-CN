# -*- coding: utf-8 -*-
"""defs 拼接工具（specs/007 摩擦 #2 修复）。

把 yuanwen/<letter>/<slug>.md 的 defs 区（首个 [^key]: 至文件尾，含 ### 子节头）
拼接到 zh/<letter>/<slug>.md 的 <!--DEFS--> 标记处，同时：
  1. 全文直引号成对→中文弯引号；
  2. 字母间 U+2019 所有格撇号 → ASCII 撇号（check_style 豁免规则）；
  3. 拼接后核验 defs 键集与键序与 yuanwen 一致；
  4. 校验 zh 文件不含 EN 正文混入（### 行只允许出现在 defs 区）。
替换 <!--DEFS--> 标记后自动移除该标记。

用法: python specs/007-review-campaign/bin/splice_defs.py <slug>
退出码: 0 成功；1 键集不一致/EN 混入；2 文件缺失。
"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main(slug):
    yw_path = 'yuanwen/%s/%s.md' % (slug[0], slug)
    zh_path = '%s/%s.md' % (slug[0], slug)
    try:
        yw = open(yw_path, encoding='utf-8').read()
        zh = open(zh_path, encoding='utf-8').read()
    except FileNotFoundError as e:
        print('文件缺失:', e)
        return 2

    # 定位 yuanwen defs 起点：第一个 [^ 开头的行（跳过 ### 节标题、## 节标题、> 引块）
    yw_lines = yw.split('\n')
    def_start = None
    for i, l in enumerate(yw_lines):
        if re.match(r'\[\^[^\]]+\]:', l):
            def_start = i
            break
    if def_start is None:
        print('yuanwen 无 defs（[^key]: 行）')
        return 2

    # defs 区含 ### 子节头（照录）+ defs 行 + 空行
    defs_block = yw_lines[def_start:]

    # 替换 zh 文件的 <!--DEFS--> 标记
    if '<!--DEFS-->' not in zh:
        print('zh 文件无 <!--DEFS--> 标记')
        return 2
    zh = zh.replace('<!--DEFS-->', '\n'.join(defs_block).rstrip('\n'))

    # 全文直引号成对→中文弯引号
    out = []
    oq = True
    for ch in zh:
        if ch == '"':
            out.append('\u201c' if oq else '\u201d')
            oq = not oq
        else:
            out.append(ch)
    zh = ''.join(out)

    # 字母间 U+2019 所有格撇号 → ASCII
    zh = re.sub(r'(?<=[A-Za-z])\u2019(?=[A-Za-z])', "'", zh)

    # 写回
    open(zh_path, 'w', encoding='utf-8', newline='\n').write(zh)

    # 核验 defs 键集与键序
    yk = [m.group(1) for l in defs_block if (m := re.match(r'\[\^([^\]]+)\]:', l))]
    zk = [m.group(1) for l in zh.split('\n') if (m := re.match(r'\[\^([^\]]+)\]:', l))]
    keys_ok = yk == zk

    # 校验 EN 正文未混入：defs 区之前不允许出现 ### 开头的 EN 子节头
    zh_lines = zh.split('\n')
    refs_start = next(i for i, l in enumerate(zh_lines) if '照录' in l)
    defs_zh_start = next(i for i, l in enumerate(zh_lines) if re.match(r'\[\^[^\]]+\]:', l))
    en_leak = [l[:50] for i, l in enumerate(zh_lines[refs_start:defs_zh_start], refs_start)
               if re.match(r'^(?:\*\*)?[A-Z][a-z]+(?: [A-Z][a-z]+)+', l.strip())]

    print('defs: %d/%d 键序一致: %s | EN混入: %s' % (
        len(zk), len(yk), keys_ok,
        en_leak[:3] if en_leak else '无'))
    return 0 if keys_ok and not en_leak else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: splice_defs.py <slug>')
        sys.exit(2)
    sys.exit(main(sys.argv[1]))

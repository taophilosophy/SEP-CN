# -*- coding: utf-8 -*-
"""中文斜体→加粗批量转换 + bold-spacing 修正（specs/007 规则落地）。

转换：`*中文内容*` → `**中文内容**`（含 CJK 的斜体→粗体）。
排除：`**粗体**`（已加粗）、列表项 `* text`、defs 照录区。
bold-spacing：`**` 前后紧邻 CJK 正文字符时自动加半角空格。
"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
CJK = r'[\u4e00-\u9fff]'
FILES = sys.argv[1:] if len(sys.argv) > 1 else [
    'a/abduction.md', 'a/abelard.md', 'a/abhidharma.md',
    'a/african-sage.md', 'a/abner-burgos.md']

for path in FILES:
    lines = open(path, encoding='utf-8').read().split('\n')
    # 定位 defs 起始行（首个 [^key]: 行）—— defs 区豁免
    def_start = None
    for i, l in enumerate(lines):
        if re.match(r'\[\^[^\]]+\]:', l):
            def_start = i
            break
    converted = 0
    out = []
    for i, l in enumerate(lines):
        if def_start is not None and i >= def_start:
            out.append(l)
            continue
        # 1) 把 *CJK内容* 转为 **CJK内容**（先处理非 ** 的单星对）
        #    跳过列表项、图注标记
        if not re.match(r'^\*\s', l) and not l.startswith('*Figure') and not l.startswith('*Table'):
            # 先遮蔽 **粗体** 避免误改
            placeholders = {}
            def _mask(m):
                key = '\x00%d\x00' % len(placeholders)
                placeholders[key] = m.group(0)
                return key
            masked = re.sub(r'\*\*[^*\n]+\*\*', _mask, l)
            # 转换 *CJK* → **CJK**
            def _convert(m):
                t = m.group(1)
                if re.search(CJK, t):
                    return '**' + t + '**'
                return m.group(0)
            masked = re.sub(r'\*([^*\n]+)\*', _convert, masked)
            # 恢复粗体
            for k, v in placeholders.items():
                masked = masked.replace(k, v)
            # bold-spacing：** 前后紧邻 CJK 时加半角空格
            masked = re.sub(r'(?<=' + CJK + r')\*\*', ' **', masked)
            masked = re.sub(r'\*\*(?=' + CJK + r')', '** ', masked)
            converted += 1 if masked != l else 0
            out.append(masked)
        else:
            out.append(l)
    open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
    print(path, 'converted lines:', converted)

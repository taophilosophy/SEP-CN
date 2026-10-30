#!/usr/bin/env python3
"""强调星内空格修正（2026-10-31，ADR-0019 配套）

把 `** 内容 **`（星内空格，CommonMark 翼规则下永不渲染）按体例修正：
中文内容 → **内容**（粗体）；拉丁内容 → *内容*（斜体，依源 <em>）；
短编号（ABD1、CP 类，源无标签）→ 纯文本。代码块豁免。

**仅处理星内空格**；错位单星、公式交错等复合形态不在此管线（需逐例对源）。
每文件写回前跑 git diff 结构审计（列表/标题行守恒），不符自动回退。

用法： python tools/fix_emphasis_spacing.py [文件...]
不带参数时自动扫描 <letter>/*.md。
"""
import glob
import re
import subprocess
import sys

cjk = lambda s: bool(re.search(r'[\u4e00-\u9fff]', s))
short_code = lambda s: bool(re.fullmatch(r'[A-Z]{1,4}\d{0,2}', s))


def convert_pairs(t):
    def _md(m):
        inner = m.group(1).strip()
        if short_code(inner):
            return inner
        return ('**' + inner + '**') if cjk(inner) else ('*' + inner + '*')

    return re.sub(r'\*\*\s*([^*]+?)\s*\*\*', _md, t)


def audit_lists(diff):
    dels = [l[1:] for l in diff.splitlines() if l.startswith('-') and not l.startswith('---')]
    adds = [l[1:] for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++')]
    for pre in ('* ', '## ', '### ', '  * ', '> '):
        if len([l for l in dels if l.startswith(pre)]) != len([l for l in adds if l.startswith(pre)]):
            return False
    return True


def has_defect(t):
    t = re.sub(r'```[\s\S]*?```|`[^`\n]*`', ' ', t)
    for m in re.finditer(r'\*\*([^*]+)\*\*', t):
        if m.group(1) != m.group(1).strip():
            return True
    return False


def main():
    files = sys.argv[1:] or glob.glob('[a-z0-9]/*.md')
    fixed, skipped, reverted = [], [], []
    for f in files:
        t = open(f, encoding='utf8').read()
        if not has_defect(t):
            continue
        t2 = convert_pairs(t)
        if t2 == t:
            continue
        open(f, 'w', encoding='utf8').write(t2)
        d = subprocess.run(['git', 'diff', '--', f], capture_output=True, text=True).stdout
        if audit_lists(d):
            fixed.append(f)
        else:
            subprocess.run(['git', 'checkout', '--', f])
            reverted.append(f)
    print(f'修正: {len(fixed)}  回退(结构不符): {len(reverted)}')
    for f in reverted:
        print('  回退:', f)
    return 0


if __name__ == '__main__':
    sys.exit(main())

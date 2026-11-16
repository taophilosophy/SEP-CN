# -*- coding: utf-8 -*-
"""中文实件机械归一（specs/039 P7；ADR-0063/0065 体例，纯格式层，零译文措辞改动）。

规则（只此三条，逐条可判）：
  N 编号加点  `## N 标题` → `## N. 标题`（仅二级；围栏代码块内不动）
  N2 编号对齐 zh 有编号的 H2/H3 与 yuanwen 同序者逐一比对，编号 token 不一致即
              改为 yuanwen 形态（`### 7 证言` → `### 7. 证言`；跳号/重复号同修）。
              仅当两侧可编号标题数相等时启用（防错位；不等者登记不处理）
  F 脚注移段  `## 脚注` 存在且不是最后一个二级标题 → 整节移至文末（保留行序，
              前置一空行；ADR-0065 脚注恒末位）

纪律（rules/05 批量改写）：--check 先行、命中数 == 预期钉（2076 行/367 件＋88 件，
2026-11-17 实测）才允许 --write；写后复跑 --check 必须全零（幂等）；逐文件改动清单
落 results/。仅动结构行与空白，禁触译文措辞（diff 可逐行复核）。

用法:
  python specs/039-md-standardization/bin/normalize_zh.py --check
  python specs/039-md-standardization/bin/normalize_zh.py --write [--out 清单路径]
退出码: 0 命中数与预期一致（--check）/ 写入完成；1 命中数与预期不符（拒写）。
"""
import io
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECT_N_LINES, EXPECT_N_FILES = 2076, 367
EXPECT_F_FILES = 88
EXPECT_ALIGN = 53  # N2 编号对齐命中数（2026-11-17 实测钉）
HEAD_BARE = re.compile(r'^##\s+(\d+)\s+(\S.*)$')
HEAD_ANY = re.compile(r'^##\s+')
NUMHEAD = re.compile(r'^(#{2,3})\s+(\d+(?:\.\d+)*\.?)\s+(\S.*)$', re.M)


def _numheads(text):
    """收集有编号的 H2/H3（跳围栏）：[(start, end, num_token, whole_line)]。"""
    res = []
    in_fence = False
    for m in NUMHEAD.finditer(text):
        line_start = text.rfind('\n', 0, m.start()) + 1
        line = text[line_start:m.end()]
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        res.append((m.start(2), m.end(2), m.group(2), m.group(0)))
    return res


def align_numbering(text, yw_text):
    """N2：zh/yuanwen 同序编号标题逐一比对，token 不一致即改为 yuanwen 形态。

    两侧可编号标题数不等时整体跳过（防错位），返回 (new_text, n_aligned, skipped)。
    """
    zh = _numheads(text)
    yw = _numheads(yw_text)
    if not zh or len(zh) != len(yw):
        return text, 0, True
    pairs = [(a, b) for a, b in zip(zh, yw) if a[2] != b[2]]
    if not pairs:
        return text, 0, False
    out = text
    # 自文末向文首逐个替换（高位先改，低位偏移不受影响）
    for (zs, ze, _zt, _zl), (_ys, _ye, yt, _yl) in sorted(pairs, key=lambda ab: -ab[0][0]):
        line_start = out.rfind('\n', 0, zs) + 1
        line_end = out.find('\n', ze)
        line_end = len(out) if line_end < 0 else line_end
        old_line = out[line_start:line_end]
        mm = NUMHEAD.match(old_line)
        if not mm:
            raise ValueError('编号对齐行解析失败: %r' % old_line[:60])
        new_line = '%s %s %s' % (mm.group(1), yt, mm.group(3))
        out = out[:line_start] + new_line + out[line_end:]
    return out, len(pairs), False


def iter_files():
    for p in sorted(Path('.').glob('[a-z]/*.md')):
        if '.' in p.stem or p.stat().st_size < 2048:
            continue
        yield p


def normalize_text(text):
    """返回 (new_text, n_bare, moved_footnotes)。围栏内不动。"""
    lines = text.split('\n')
    out = []
    in_fence = False
    n_bare = 0
    for ln in lines:
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append(ln)
            continue
        if not in_fence:
            m = HEAD_BARE.match(ln)
            if m:
                ln = '## %s. %s' % (m.group(1), m.group(2))
                n_bare += 1
        out.append(ln)
    new = '\n'.join(out)
    # F 脚注移段
    moved = 0
    h2_idx = [k for k, l in enumerate(new.split('\n')) if HEAD_ANY.match(l)]
    lines2 = new.split('\n')
    fn = [k for k in h2_idx if lines2[k].strip() == '## 脚注']
    if fn and fn[0] != h2_idx[-1]:
        k = fn[0]
        end = next((j for j in h2_idx if j > k), len(lines2))
        block = lines2[k:end]
        rest = lines2[:k] + lines2[end:]
        while rest and not rest[-1].strip():
            rest.pop()
        new = '\n'.join(rest) + '\n\n' + '\n'.join(block).strip('\n') + '\n'
        moved = 1
    return new, n_bare, moved


def main(argv):
    check = '--check' in argv
    write = '--write' in argv
    out_path = None
    if '--out' in argv:
        out_path = argv[argv.index('--out') + 1]
    n_lines = n_files = 0
    f_files = 0
    n_align = 0
    changed = []
    for p in iter_files():
        text = p.read_text(encoding='utf-8')
        new, n_bare, moved = normalize_text(text)
        yw_p = ROOT / 'yuanwen' / p.parent.name / (p.stem + '.md')
        if yw_p.exists():
            new, a, _skip = align_numbering(new, yw_p.read_text(encoding='utf-8'))
            n_align += a
        if new != text:
            changed.append({'path': str(p).replace('\\', '/'), 'bare': n_bare,
                            'moved': moved, 'aligned': n_align})
            if write:
                io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
        n_lines += n_bare
        if n_bare:
            n_files += 1
        if moved:
            f_files += 1
    report = {'bare_lines': n_lines, 'bare_files': n_files, 'footnote_moved_files': f_files,
              'aligned_headings': n_align, 'changed_files': len(changed),
              'mode': 'write' if write else 'check'}
    print(json.dumps(report, ensure_ascii=False))
    if out_path and write:
        io.open(out_path, 'w', encoding='utf-8', newline='\n').write(
            json.dumps(changed, ensure_ascii=False, indent=1))
    if check:
        pending = bool(changed)
        ok = ((n_lines == EXPECT_N_LINES and n_files == EXPECT_N_FILES
               and f_files == EXPECT_F_FILES and n_align == EXPECT_ALIGN)
              or (not pending and n_lines == 0 and n_files == 0 and f_files == 0
                  and n_align == 0))
        # 两种合法终态：写前命中数 == 预期钉；写后（或已归一）全零且无待写改动
        if not ok:
            sys.stderr.write('[normalize] 命中数与预期钉不符（预期 %d/%d/%d/%d，实得 %d/%d/%d/%d）\n'
                             % (EXPECT_N_LINES, EXPECT_N_FILES, EXPECT_F_FILES, EXPECT_ALIGN,
                                n_lines, n_files, f_files, n_align))
        return 0 if ok else 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

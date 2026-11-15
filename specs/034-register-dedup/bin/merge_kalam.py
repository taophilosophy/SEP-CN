# -*- coding: utf-8 -*-
"""specs/034 Kalām 同键行合并。

阿拉伯文行避免全串匹配坑：按首列折叠键（norm_key_quote）定位，逐列取文件自身
内容拼接合并行，仅注入纯中文注记。守恒：恰 2 行定位、其余行零触碰、原子写 LF。

用法：python specs/034-register-dedup/bin/merge_kalam.py [--apply]
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, REPO)

from tools.register_lib import norm_key_quote, split_row, term_path  # noqa: E402

NOTE = '2026-11-15 合并同键行（specs/034）'


def main(argv):
    apply = '--apply' in argv
    path = term_path()
    lines = open(path, encoding='utf-8', newline='').read().split('\n')
    idxs = [i for i, l in enumerate(lines)
            if l.startswith('|') and split_row(l)
            and norm_key_quote(split_row(l)[0]) == 'kalam'
            and '凯拉姆' in l and '已废弃' not in l]
    if len(idxs) != 2:
        print('拒绝：期望恰 2 行，实得 %d' % len(idxs))
        return 1
    c1 = split_row(lines[idxs[0]])
    c2 = split_row(lines[idxs[1]])
    # 基行取「凯拉姆；伊斯兰教义学…」全形行（c2）；键取小写 kalām（先登记正形）
    if '伊斯兰教义学' not in c2[2]:
        c1, c2 = c2, c1
    if '伊斯兰教义学' not in c2[2] or '凯拉姆' not in c1[2]:
        print('拒绝：两行译法形态与预期不符：%s | %s' % (c1[2][:30], c2[2][:30]))
        return 1
    merged = '| ' + ' | '.join([c2[0], c2[1], c2[2],
                                c1[3] + '；' + c2[3],
                                c1[4] + '；' + c2[4] + '；' + NOTE,
                                max(c1[5], c2[5])]) + ' |'
    print('旧行 1：%s' % lines[idxs[0]])
    print('旧行 2：%s' % lines[idxs[1]])
    print('并行  ：%s' % merged)
    if not apply:
        print('干跑：未写盘')
        return 0
    out = lines[:idxs[0]] + lines[idxs[0] + 1:idxs[1]] + [merged] + lines[idxs[1] + 1:]
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.merge.tmp')
    with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out))
    os.replace(tmp, path)
    print('已写回：删 1 行合 1 行（总行数 −1）')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# -*- coding: utf-8 -*-
"""预建审定条目配对索引（ADR-0088，2026-11-26）。

扫 `specs/008-terminology-campaign/results/queries/termonline-all/` 全部缓存，
建 records＋by_key／en／cn 三映射的索引并 gz 落盘（`tools/term_pairing.INDEX_PATH`）。
`check_terms` 的审定引用配对检查与 `specs/058` 批量审计都读这份索引。

缓存新增（爬虫新批、界面通道回写缓存）后重跑本脚本刷新：
  python -I tools/build_term_pair_index.py
"""
import glob
import io
import os
import sys

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')

from tools import term_pairing as tp


def main():
    files = sorted(glob.glob(os.path.join(tp.QD, '*.json')))
    index = tp.build_index(files=files)
    size = tp.save_index(index)
    # 标准文件术语库（GB 标准）：同一套判据，条目全按标准库计
    sfiles = sorted(glob.glob(os.path.join(tp.STD_QD, '*.json')))
    sindex = tp.build_index(files=sfiles, force_lib=tp.LIB_STD)
    ssize = tp.save_index(sindex, tp.STD_INDEX_PATH)
    recs = len(index['records'])
    by_lib = {}
    for r in index['records']:
        by_lib[r[4]] = by_lib.get(r[4], 0) + 1
    print('缓存 %d 份 → 条目 %d（%s）' % (len(files), recs,
          '／'.join('%s %d' % (k, v) for k, v in sorted(by_lib.items()))))
    print('映射：by_key %d、en %d、cn %d；索引 %s（%.1f MB）'
          % (len(index['by_key']), len(index['en']), len(index['cn']),
             tp.INDEX_PATH, size / 1048576.0))
    print('标准库：缓存 %d 份 → 条目 %d；索引 %s（%.2f MB）'
          % (len(sfiles), len(sindex['records']), tp.STD_INDEX_PATH,
             ssize / 1048576.0))


if __name__ == '__main__':
    main()

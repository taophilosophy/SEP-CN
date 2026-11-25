# -*- coding: utf-8 -*-
"""为无任务账的词条补建“待译（cleared）”账（specs/062，用户 2026-11-25「全部置空」）。

背景：全库正文已 H1-only、1,200 条任务已 cleared，但 catalog 主条目 1,873 中有 673 件
从未建过 retranslate 账（历史账外件）。本脚本以状态机正规原语补齐：

  create(slug, "retranslate") → clear(slug)
  clear 的 gate 未过时按 ADR-0081 精神强制置 cleared，并在 steps 记明（不静默）。

幂等：已有任务账的件跳过。正文不动（置空由 tools/wipe_translations.py 负责）。

用法:
  python specs/062-phase12-recheck/bin/wipe_missing_tasks.py --limit 5   # 试金石
  python specs/062-phase12-recheck/bin/wipe_missing_tasks.py --apply     # 全量
输出: results/missing-task-backfill.json
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from tools import task_ops  # noqa: E402
from tools.common import load_json, repo_path  # noqa: E402

RES = os.path.join(ROOT, 'specs', '062-phase12-recheck', 'results')
ACTOR = 'wipe-2026-11-25'
REASON = '全库置空（用户 2026-11-25 裁定）：补齐账外件的待译账，正文仅留 H1'


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args(argv)

    cat = load_json(repo_path('baseline', 'catalog.json'))
    slugs = sorted(i['slug'] for i in cat['items'] if not i.get('alias_of'))
    todo = [s for s in slugs if not task_ops.load_task(s)]
    if args.limit:
        todo = todo[:args.limit]

    rows = []
    for s in todo:
        rec = {'slug': s}
        if not args.apply:
            rec['status'] = 'would-create'
            rows.append(rec)
            continue
        try:
            task_ops.create(s, 'retranslate')
            try:
                task_ops.clear(s)
                rec['status'] = 'created+cleared'
            except task_ops.PreconditionError as exc:
                t = task_ops.load_task(s)
                t['state'] = 'cleared'
                t.setdefault('steps', []).append({
                    'step': 'clear', 'status': 'ok', 'actor': ACTOR,
                    'at': task_ops.utcnow_iso(),
                    'evidence': '全库置空（强制）：clear gate 未过——%s；%s'
                                % (str(exc)[:300], REASON)})
                task_ops.save_task(t)
                rec['status'] = 'forced-cleared'
                rec['gate'] = str(exc)[:200]
        except Exception as exc:  # 逐条记录，不静默
            rec['status'] = 'error'
            rec['error'] = repr(exc)[:200]
        rows.append(rec)

    out = {'schema': 'sep-cn-missing-task-backfill/1', 'apply': args.apply,
           'candidates': len(todo) if not args.limit else len(todo),
           'status': {k: sum(1 for r in rows if r['status'] == k)
                      for k in {r['status'] for r in rows}},
           'rows': rows}
    os.makedirs(RES, exist_ok=True)
    with open(os.path.join(RES, 'missing-task-backfill.json'), 'w',
              encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(json.dumps({'apply': args.apply, 'count': len(rows),
                      'status': out['status']}, ensure_ascii=False))
    return 0 if not any(r['status'] == 'error' for r in rows) else 1


if __name__ == '__main__':
    sys.exit(main())

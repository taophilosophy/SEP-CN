# -*- coding: utf-8 -*-
"""把浏览器内重查结果（JSONL）落成 termonline-all 凭证，供离线审计重放。

输入：临时 JSONL，每行 {key, total, hits[{cn,en,code,standard,subject}], tries}
输出：specs/008-terminology-campaign/results/queries/termonline-all/<键>.json
      结构与 cnki_query 写入的一致（key/term/provider/queried_at/status/note/hits/error/raw），
      按 A（norm_key_quote）与 B（norm_key）两种键名各写一份，避免下游两种口径漏读。
"""
import io
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding='utf-8')
from tools.cnki_query import safe_key  # noqa: E402
from tools.register_lib import norm_key, norm_key_quote  # noqa: E402

QD = 'specs/008-terminology-campaign/results/queries/termonline-all'
DB = {'0': '审定公布名词库', '1': '海峡两岸名词对照库', '2': '其他来源数据库', '6': '预公布名词数据库'}


def main(paths):
    n = 0
    for path in paths:
        if not os.path.exists(path):
            continue
        for line in io.open(path, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            key = r['key']
            hits = r.get('hits') or []
            rec = {
                'key': key, 'term': key, 'provider': 'termonline-all',
                'queried_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                'status': 'ok' if hits else 'empty',
                'note': '浏览器页内 fetch 重查；total=%d；tries=%s' % (r.get('total', 0), r.get('tries')),
                'hits': hits, 'error': None, 'raw': None,
            }
            body = json.dumps(rec, ensure_ascii=False, indent=1)
            for name in {safe_key(norm_key_quote(key)), safe_key(norm_key(key))}:
                p = os.path.join(QD, name + '.json')
                tmp = p + '.tmp'
                with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(body)
                os.replace(tmp, p)
            n += 1
    print('落凭证', n, '条 →', QD)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or ['C:/Users/ykla/AppData/Local/Temp/tl_recheck.jsonl',
                                   'C:/Users/ykla/AppData/Local/Temp/tl_recheck2.jsonl']))

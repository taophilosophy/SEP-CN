# -*- coding: utf-8 -*-
"""候选池术语性门禁（specs/050 口径层）：防提取噪声回归 + 自动预筛可追溯。

两条不变量（幂等只读）：
  I1 无回归：status=new 的非人名候选不得违反 termhood_ok（提取端守卫的镜像），
     即确定性残渣/子句片段/连字符残片/单字泛词/结构标题等不得再出现在 new。
  I2 可追溯：每条 rejected:自动预筛-* 的键须能在 prescreen-*.json 全量撤销清单中找到，
     防止绕过预筛工具手工塞入「自动预筛」裁定。

用法:
  python tools/check_term_pool.py            # 人读报告，违例即退出 1
  python tools/check_term_pool.py --gate     # CI 门禁（同判据，--gate 仅语义标识）
  python tools/check_term_pool.py --pool <p> --manifest <m>
退出码: 0 全绿；1 有违例；2 参数/路径错误。
"""
import glob
import io
import json
import os
import sys

# 就地重配置编码：不替换 sys.stdout 对象，避免被 unittest 等宿主导入时缓冲区已关闭
try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, ValueError, OSError):
    pass
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
from tools import term_harvest as th  # noqa: E402
from tools.register_lib import norm_key  # noqa: E402

POOL = os.path.join(ROOT, 'tasks', 'term-pool.json')
RESULTS = os.path.join(ROOT, 'specs', '008-terminology-campaign', 'results')


def latest_manifest(results_dir):
    files = sorted(glob.glob(os.path.join(results_dir, 'prescreen-*.json')))
    return files[-1] if files else None


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    pool_path, manifest_path = POOL, None
    i = 0
    while i < len(argv):
        if argv[i] == '--pool':
            pool_path, i = argv[i + 1], i + 1
        elif argv[i] == '--manifest':
            manifest_path, i = argv[i + 1], i + 1
        i += 1
    if not os.path.exists(pool_path):
        print('候选池缺失: %s' % pool_path)
        return 2
    if manifest_path is None:
        manifest_path = latest_manifest(RESULTS)

    pool = json.load(open(pool_path, encoding='utf-8'))
    cands = pool.get('candidates', [])

    # I1 无回归：new 中不得有违反守卫的候选
    regress = []
    for c in cands:
        if not str(c.get('status', '')).startswith('new'):
            continue
        if c.get('type') == 'person':
            continue
        if not th.termhood_ok(c.get('en', ''), c.get('type', '')):
            regress.append((c.get('type', ''), c.get('en', '')))

    # I2 可追溯：自动预筛裁定 ⊆ manifest 撤销清单
    orphan = []
    manifest_keys = None
    if manifest_path and os.path.exists(manifest_path):
        m = json.load(open(manifest_path, encoding='utf-8'))
        manifest_keys = {norm_key(k) for lst in m.get('rejected', {}).values()
                         for k in lst}
    for c in cands:
        if not str(c.get('status', '')).startswith('rejected:自动预筛'):
            continue
        if manifest_keys is None:
            continue  # 无 manifest：降级为仅报数，不判违例
        if norm_key(c.get('en', '')) not in manifest_keys:
            orphan.append(c.get('en', ''))

    ok = not regress and not orphan
    print('=== 候选池术语性门禁 ===')
    print('候选池: %s（%d 条）' % (os.path.relpath(pool_path, ROOT), len(cands)))
    print('manifest: %s' % (os.path.relpath(manifest_path, ROOT)
                            if manifest_path else '（无，I2 降级跳过）'))
    print('I1 无回归（new 不得违反 termhood_ok）: %s（违例 %d）'
          % ('OK' if not regress else 'FAIL', len(regress)))
    for t, e in regress[:20]:
        print('    [%s] %r' % (t, e))
    print('I2 可追溯（自动预筛 ⊆ manifest）: %s（孤儿 %d）'
          % ('OK' if not orphan else 'FAIL', len(orphan)))
    for e in orphan[:20]:
        print('    %r' % e)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())

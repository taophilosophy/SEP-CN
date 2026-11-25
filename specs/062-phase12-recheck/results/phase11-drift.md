## 上游目录漂移巡检

- 生成时间：2026-11-25T02:43:06Z
- 上游快照：20261125T023957Z-contents.html
- 上游统计：主条目 1873／别名行 652／簇母行 187

其余 10 项均无差异：上游新增条目、上游删除条目、上游改名、作者变更、别名新增、别名消失、上游有而 SUMMARY 无、SUMMARY 有而上游无、上游有而 mu-lu-s 无、mu-lu-s 有而上游无

### 处置路线（specs/054 §3 单向波纹）
1. `python tools/fetch_catalog.py`（落快照＋重写 baseline/catalog.json＋与上次快照 diff）
2. `python tools/summary_sync.py report`（裁决表 ADD/REMOVE/RENAME）
3. 人工裁定中文标题与归类 → `apply-add`/`apply-rename`/`apply-remove`
4. `python tools/rebuild_catalog.py --build`（池随快照重冻）→ `--check` 全等
5. `python tools/check_catalog_network.py --gate` 四门全绿


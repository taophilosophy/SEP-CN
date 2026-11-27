# Open issues 处置记录（2026-11-27）

## #55 SEP 上游变化同步报告

- 漂移：`moral-epistemology-a-priori` 作者 `Michael DePaul and Amelia Hicks` → `Elijah Chudnoff`；目录四方其余无差异。
- 处置：
  - `python tools/fetch_catalog.py`：快照 `20261127T013538Z-contents.html`，entries 1873／aliases 652。
  - 同步 `SUMMARY.md`、`mu-lu-s.md`、`baseline/mulu-map.json`、`m/moral-epistemology-a-priori.md` H1、`yuanwen/SUMMARY-en.md`。
  - `sync_official_snapshot.py --write`：作者变更 1，main 1873／alias 652。
  - `rebuild_catalog.py --build` → `--check`：sha `0a92b8e272ef653f61b8bf85739f282630ef0ae0feac591c7300fe64b76bf45f` 全等；residual 194。
  - `check_catalog_network.py --gate`：G1–G5 全绿。
  - `catalog_drift.py --latest`：`changed=false`；`summary_sync.py report`：add 0／remove 0／mapped 1873。
- 提交：`d12e87f01`；issue 已评论并关闭（completed）。

## #53 EN 互转漂移报告

- 最新报告信号：`croce-aesthetics` → `croce` 换发（+1／−1），`croce-aesthetics` 页面转差。
- 现状：换发已由 `0ae9d83b6` 落地；053 第 58 批基线 `97d272a10` 双绿。
- 本地复核（2026-11-27）：
  - `divergence.py verify`：checked 4847／pristine 4847／divergent 0。
  - `check_yuanwen_fidelity.py --gate`：checked 1873／issues 0。
  - B3.1 `assembly-scan-all.json`：ok 1873／fail 0。
  - B3.2 `page-scan-all.json`：rule 0／pool 1873／gap 0／stale 0。
  - 无新增转差、无词条增删。
- issue 已评论并关闭（completed）；若下一班巡检复现，重开并附运行工件。

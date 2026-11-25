# 阶段 1.1 报告：目录抓取与四方互转复核（2026-11-25）

任务卡：specs/062。四方＝上游 `contents.html`（钉存）／`yuanwen/SUMMARY-en.md`／`SUMMARY.md`／`mu-lu-s.md`，支撑账＝`baseline/catalog.json`、`catalog-skeleton.json`、`catalog-residual.json`、`mulu-map.json`。

## 一、执行与结果

| # | 命令 | 结果 |
| --- | --- | --- |
| 1 | `python tools/fetch_catalog.py` | 新快照 `en/_catalog/20261125T023957Z-contents.html`（2026-11-25T02:40:06Z）；items 1873／alias_rows 652／簇母 187；与上一基线（2026-11-24T18:25:19Z）比，added／removed／renamed／alias_changed **四项全空** |
| 2 | `python tools/summary_sync.py report` | `add 0 / remove 0 / mapped 1873` |
| 3 | `python tools/gen_en_summary.py --check` | 最新：词条 1873／分组行 820／跳过 16 |
| 4 | `python tools/catalog_drift.py --latest` | `changed=false`；新增／删除／改名／作者变更／别名增删／SUMMARY 与 mu-lu-s 双向差集共 10 项全零；挂起集清零 |
| 5 | `python tools/check_catalog_network.py --gate` | G1–G5 **全绿**（G4 unmapped 0／extra 0；G5 main 1873＝1873，title／authors 变更空） |
| 6 | `python tools/rebuild_catalog.py --check` | 逐字节全等：`sha_rebuilt == sha_snapshot == c60c25f048076181a6167e28005873ab004c119f14c8959e355fbe092bde90ac`，`residual_used=194` |
| 7 | `python tools/check_mulu_s.py` | 六项检查 **0 硬错**（4 条“SUMMARY 有而 mu-lu-s 无”为已知非词条件：mu-lu-s 自身、版权说明、日志三卷） |
| 8 | `python tools/sync_official_snapshot.py --check` → `--write` | 内容无变化（main 1873／alias 652）；`--write` 仅刷新 `fetched_at` 一行（内容 hash 不变） |

证据：`results/phase11-drift.json`、`results/phase11-drift.md`、`results/phase11-network.json`。

## 二、结论

1. **上游目录无漂移**：与 2026-11-24 快照逐项比较，条目、别名、题名、作者、簇结构均无变化；无需 ADD／REMOVE／RENAME 裁定。
2. **四方互转闭合**：contents → catalog 账（G1 装配 sha 全等）→ SUMMARY-en（G2）→ mu-lu-s（G3）→ SUMMARY（G4）→ 官方快照（G5）全部通过；转换网络在该快照上可逐字节重放。
3. **croce 换发已闭环**：`croce-aesthetics → croce` 的旧 slug 不再出现在任何差集；首轮漂移报告中的“已挂起不计：croce-aesthetics”来自旧 `catalog-verdict.json` 的 remove 行，`summary_sync report` 重生成后挂起集为空，二次运行已无该提示。
4. **阶段 1.1 收口**：抓取、基线更新、四方比较三项完成，无待裁定项。

## 三、观察（非本卡缺陷，登记建议）

1. `AGENTS.md` 硬约束表仍写“抓取礼貌：相邻请求至少间隔 5 秒”，与 ADR-0069（2026-11-18 废除强制间隔）及 `tools/fetch.py` 头部说明冲突。属文档陈旧，建议走 rules 修订（本卡不动）。
2. G5 输出字段 `baseline_fetched_at` 读的是 `official-snapshot.json` 的 `fetched_at`，不是 `baseline/catalog.json` 的，两个时间戳语义不同（本次分别为 11-24 18:25 与 11-25 02:40）；排查时易误读为“基线未更新”。建议改名或加注（本卡不动）。
3. 挂起集是 `catalog-verdict.json` 的派生快照，`summary_sync report` 重生成会改变它；同一快照先后两次 `catalog_drift` 可能得到不同的“挂起”提示，属预期行为，报告以最终一次为准。

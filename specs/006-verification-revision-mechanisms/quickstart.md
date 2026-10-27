# Quickstart：会话按批次执行核验（specs/006）

**前置**：读 `specs/005-translation-campaign/session-handoff.md`（开工三件事与纪律）与本 feature 契约。

## 标准动线（每批次）

```
1. 领批   python tools/campaign.py status / next / claim <批> --session <会话名>
2. 目录核验  运行既有目录门禁与上游对照，汇总该批差异清单
3. 抓取核验  运行引用闭包审计（fetch_audit），缺件补齐/缺省件登记
4. 转换核验  批次内逐词条中英节序列对照 + 公式/表格/脚注计数
5. 出报告  specs/006-verification-revision-mechanisms/reports/<批>.json
6. 裁定    逐差异项显式裁定（豁免/增量登记/修正），silent 归零
7. 复跑    核验收敛（0 新增差异）→ 批次核验收口
```

## 全库节奏

* 批次并行：多会话各自认领（账本互斥），核验报告按批归属。
* 收敛判定：全库轮次迭代至差异项 0 新增（同 fetch_audit 不动点语义）。
* 修订例行化：每存档季（3/6/9/12 月 21 日）fetch_catalog + compare 全量，漂移自动进 update 队列。

## 验收自查（对 checklist.md）

每批次收口前过一遍 checklist 的"批次核验"段：差异清单零 silent、覆盖率四项计数齐、节序列对照齐、复核记录字段齐。

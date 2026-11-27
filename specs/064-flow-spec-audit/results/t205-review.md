# T205 现行文档路径改写

- 日期：2026-11-27。
- 已改：`AGENTS.md`（单一事实源、更新流程、结构形态、必读表、进度入口）、`rules/01-repository-structure.md`（目录职责、根白名单、SUMMARY 规则、豁免）、`rules/03`／`04`／`05`／`06`／`09`／`11`／`README` 的现行路径语义、`.vitepress/README.md`、根 `README.md`、壳仓 `README.md`、`specs/001-sep-sync-pipeline/contracts/cli.md`、`specs/005-translation-campaign/session-handoff.md`、`specs/064` 计划与任务书。
- 语义口径：`html/` = 原始 HTML（冻结）；`en/` = Markdown 转换镜像；`zh/` = 中文正文与登记册。
- 未改：`rules/adr/`（ADR 只追加，保留历史原文）与 `journal/` 事件（只记 slug，不含路径）；旧路径只保留在历史规格与 ADR 中，供追溯。
- 验收：`check_layout` L2 双向 0；`check_summary` 0 硬错误；`check_mulu_s` 坏链 0。

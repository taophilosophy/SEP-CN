# Feature Specification: 全库 A–Z 审阅战役（抓取→本地HTML比对→英语markdown复核）

**Feature Branch**: `007-review-campaign`

**Created**: 2026-10-28

**Status**: In progress

**Input**: 用户指令（2026-10-28）："建立审阅任务，按照网页A-Z顺序，逐个抓取-比较本地HTML-复核英语markdown。批准批量比较。不计成本"；补充指令："还需要比较summary 和mu-lu-s"。

## 目标与范围

对全库词条按**网页 A–Z 顺序**逐个执行三步审阅，并对目录层（SUMMARY.md、mu-lu-s.md）与上游目录快照比对：

1. **抓取**：在线抓取词条最新 HTML（`compare.py` 内建礼貌 5 秒，快照落 `script/tmp/`（gitignore），不覆盖 `en/` 不可变基线）。
2. **比较本地HTML**：与基线 `en/<slug>/index.html` 逐节逐段比对；有变更由 `compare.py` 自动落盘持久变更文件 `specs/001-sep-sync-pipeline/compare/<slug>.json`（update 任务 `changes:` 证据的引用载体）。
3. **复核英语markdown**：`en_integrity.py`（en/ 包深度审计：页面真实性、引用闭包、数学形态、游离件）+ `check_math.py`（yuanwen md 公式保真）+ 收尾 `yuanwen.py --all-baselined` 确定性重转换比对（字节一致 = 转换器与产物无漂移）。

目录层（用户补充指令）：

* `fetch_catalog.py` 抓最新 contents.html 快照 → `summary_sync.py report` 重新生成 SUMMARY↔上游三方裁决表 `catalog-verdict.json`；
* `check_mulu_s.py` + `check_summary.py` 复核 mu-lu-s 分类覆盖与 SUMMARY 结构。

**范围**：baseline 全部 1878 词条（= 上游 1872 正式词条全量 + 6 条撤稿留存词条）；别名（— see，603 条）无词条包，不在逐词条范围，由目录层覆盖。

## 用户裁定（授权记录）

* **批准批量比较**（2026-10-28 用户指令）：全库批量执行 `compare.py`，无需逐条请示。
* **不计成本**：时长/算力不设限；仍守宪法礼貌抓取约束。
* **并行配置先例**：`fetch_all.py` 配置 A=16路×5秒、B=64路×10秒 系用户先前指定并实测未触发限流（见 contracts/cli.md）。本战役取**8 路×5 秒**保守执行 compare 抓取。

## 已知例外（预期非失败）

6 条撤稿留存词条（`continental-rationalism`、`pineal-gland`、`qm-action-distance`、`scientific-explanation`、`time-experience`、`wisdom`）：在线 URL 为撤稿页（横幅在 BEGIN/END ARTICLE 标记之外，正文仍可抓），冒烟实测 wisdom 在线正文与归档版基线**零漂移**；**保留依据为归档版基线**（c75cc794 / 2eecf911 裁定）。审阅照常执行比较；`expected_offline_404` 仅作防御性分类（若真返回 404/410 则归入此类，不计失败）。

## 分级语义（2026-10-28 冒烟后定）

* compare：`ok`（无变更）/ `changed`（有变更，工具已落盘变更文件）/ `error`（真异常）/ `expected_offline_404`（防御）。
* integrity：`ok` / `finding`（硬问题，完整明细落 results/integrity/）。
* math（check_math 退出码只由 missing 驱动）：`ok` / `warn`（unbalanced 渲染歧义警告，明细落 results/math/，不计 finding）/ `finding`（公式丢失，硬失真）。

## 验收标准

1. 目录层：目录快照 diff、catalog-verdict.json、check_mulu_s/check_summary 结果全部留档，差异逐条有显式裁定或既有登记。
2. 逐词条：1878/1878 每条一行 JSONL 凭证（compare 结果 + en_integrity 摘要 + check_math 摘要）；中断可续跑；硬问题逐条落盘完整 JSON。
3. 英语markdown：重转换后 `git diff yuanwen/` 为空（或差异全部归因登记）；`en_integrity.py --all --out` 全库凭证落盘且硬问题为 0。
4. 汇总：执行日志（execution-log.md）留痕；九门禁全绿；分批提交（不 push）。

## 产物

* `specs/007-review-campaign/execution-log.md` —— 干活日志
* `specs/007-review-campaign/results/review-log.jsonl` —— 逐词条凭证（一行一条）
* `specs/007-review-campaign/results/status.json` —— 检查点（断点续跑）
* `specs/007-review-campaign/results/en-integrity-full.json` —— 全库收尾凭证
* `specs/007-review-campaign/results/catalog-*.json` —— 目录层结果存档
* `specs/007-review-campaign/bin/review_campaign.py` —— 驱动器（A–Z 顺序、路通道节拍、续跑；script/ 为不入库杂物抽屉，驱动器随战役归档入库）
* 变更词条：`specs/001-sep-sync-pipeline/compare/<slug>.json`（工具自动产出）

# 实施计划：六轴独立质量工序（specs/060）

> 立项依据：用户 2026-11-25 批准立项至 r2_reviewed；四项补裁见 `spec.md` §11 与本文件 §1。
> 决策记录：`rules/adr/0079-六轴独立质量工序与状态机v3.md`。
> 交付物：本文件为实施计划，任务清单见 `tasks.md`，完成判据是任务清单全部 pass（rules/08 §14）。

## 1 目标态与边界

| 项 | 内容 |
| ---- | ---- |
| 目标态 | r2_reviewed。任何件走完 q1–q6 后可推进 r1、r2；r3 仍按 ADR-0054 需用户另行指定 |
| 用户补裁 | ① 原文补齐对现代著作也逐条查初版或权威版；② 补入原文与英译用方括号；③ 术语级全部首现括注；④ 目标态 r2_reviewed |
| 非目标 | 不替用户裁定任何 verdict；不自动改写译文；不把 LLM 输出当裁判；不因本项目改动 `en/`、`yuanwen/`（ADR-0062） |
| 回退 | `git revert` 本批次提交；任务侧 `revert-state --to s2.5_checked`；pipeline 删六节点即恢复 16 节点（ORDER 自动推导） |

## 2 阶段

| 阶段 | 内容 | 验收判据 | 状态 |
| ---- | ---- | ---- | ---- |
| T0 报告档 | 六器全库扫描出数，不拦任何提交；建 `state/axis/` 与 `qchain-latest.json` | 六类各出命中数与误报样本；`check_all` 全绿 | 进行中 |
| T1 新件 | 新译件走完整 q1–q6；机检硬拦项按各判据档位 | 试金石 3 件走通；新件 q 链 pass 率可核 | 未开始 |
| T2 存量 | A–Z 分批回炉；机检类清零后 `gate_owner=true` | 每类“残余 0 或全部登记豁免” | 未开始 |
| T3 固化 | 六器入 `check_all` 与 CI；规则定稿；ADR 状态转 accepted | CI 全绿；rules／pipeline／axioms／standards 四处一致 | 未开始 |

## 3 批次设计

* **试金石 3 件**（先于一切铺量，ADR-0039 §10）：一件引文密集（`ibn-gabirol` 或 `aesthetics-18th-german`）、一件逻辑密集（量词与否定多）、一件计量密集（单位与换算多）。
* **引文分四批**（B1 希腊拉丁德法、B2 阿拉伯波斯、B3 梵藏巴利、B4 汉语日语），不按字头，理由见 `checklists/q1-cite.md` §5。
* **存量回炉按字头 A–Z**，每批内 q1→q6 顺序固定；同件不得被两个会话同时判。
* **每批收口**：该批 q1–q6 全 pass 且 `check_all` 全绿；未清零不宣布该类完成。

## 4 依赖与顺序

1. `pipeline.json` 节点 → `journal_lib` 映射 → `task_ops` ORDER（自动推导），任一处不同步即 `check_stages` 红。
2. 六器与 `tools/data/` 先于 `gate_owner=true`（S5 承载体可解析）。
3. 单测（`tools/tests/test_six_axis.py`）先于 T1，防止门禁挂上后退化。
4. `register-baseline.md` 与 `logic-baseline.jsonl` 待用户裁定后入库，T1 前完成。

## 5 风险与处置

| 风险 | 处置 |
| ---- | ---- |
| q 链使在途件卡住 | T0 期 `gate_owner=false`；`task_ops` 只对已进入 q 节点的件挂 gate，存量 s2.4 不受影响 |
| 六器误报率高 | 每器 `--init` 留 verdict 字段，误报记 `false-positive`；同类误报两次即沉淀白名单（ADR-0039） |
| 全量回炉拖垮进度 | 分批＋试金石；每批独立收口；不做“一次全库” |
| 原文补齐引发幻觉 | `unavailable` 允许保留英文；`verifiable` 须记版本与页码；禁止模型生成原文 |
| 规则与工具漂移 | `check_stages` S2/S5 硬拦；`punct-rules.json`／`units.json` 为条款映射唯一入口 |

## 6 度量

| 指标 | 口径 |
| ---- | ---- |
| 六类命中数 | 各器 `--all` 汇总，入 `state/axis/qchain-latest.json` |
| 误报率 | `false-positive` 处置数 ÷ 命中数，按批统计 |
| 返工率 | q 链退回次数 ÷ 件数（q 链重入上限 1） |
| 编校差错率 | CY/T 266-2023 万分之一合格线；ISO 5060 七维只作过程度量 |

# Implementation Plan: 全流程一致性验证与修订机制

**Branch**: `006-verification-revision-mechanisms` | **Date**: 2026-10-27 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/006-verification-revision-mechanisms/spec.md`

## Summary

为五项要求建立"验证与修订机制"：①三方目录一致性核验（SUMMARY↔官方快照↔mu-lu-s，含别名/递归条目）与中英结构一致；②抓取内容完全离线（引用闭包收敛）；③HTML→markdown 转换保真核验（节序列/公式/表格/脚注）；④上游修订吸收机制（检测→变更记录→任务→闭环）；⑤复核留痕与抽查机制。执行按 a–z 批次并行（沿用 specs/005 批次账本与会话协议）。技术路径以**复用既有机制为主**：现有门禁与工具已覆盖大部分核验能力，本 feature 的增量是把它们组织成"按批次的核验计划 + 缺口工具 + 修订闭环"，见 research.md 的机制盘点。

## Technical Context

**Language/Version**: Python 3（仅标准库，与仓库现行工具一致）

**Primary Dependencies**: 无新增依赖（复用 tools/ 既有门禁与管线工具）

**Storage**: 版本库文件（SUMMARY/mu-lu-s/baseline/tasks/en/yuanwen 本地相）；无数据库

**Testing**: unittest（tools/tests，金样本 fixtures）

**Target Platform**: 仓库本地执行（Windows/Linux 双侧，Linux 为 CI 裁判）

**Project Type**: 文档管线 + CLI 验证工具

**Performance Goals**: 单批次核验分钟级；全库收敛轮次 ≤3

**Constraints**: 抓取礼貌 ≥5 秒；多会话并行（认领互斥）；不建备份文件

**Scale/Scope**: 1872 上游条目、1799 本地正式条目、27 个 a–z 批次

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| 宪法原则 | 本 feature 落地 | 判定 |
|---|---|---|
| I 零信任 | 核验以"换命令重算复核"为标准动作；三方核验的裁判基准是官方快照与原始物，非既有结论 | ✅ |
| II 可追溯 | 每批核验出具差异清单与覆盖率报告，逐条可回溯到 slug/锚点 | ✅ |
| III 单一事实源 | SUMMARY 为目录裁判；核验结果不直接改目录，差异走显式裁定 | ✅ |
| IV 流程先行 | 本 spec→plan→tasks 先行，执行暴露问题回流修订 | ✅ |
| V 礼貌抓取 | 补抓走既有 fetch 层（≥5 秒/退避重试） | ✅ |
| VI 体例即契约 | 核验产出物遵循 rules/01 体例；`check_style`/`check_all` 门禁复核 | ✅ |
| 备份豁免 | 不建立任何备份文件（用户 2026-10-27 裁定） | ✅ |

## Project Structure

### Documentation (this feature)

```text
specs/006-verification-revision-mechanisms/
├── plan.md              # This file
├── research.md          # Phase 0：既有机制盘点与缺口分析
├── data-model.md        # Phase 1：核验实体与状态模型
├── quickstart.md        # Phase 1：会话按批次执行核验的快速指南
├── contracts/           # Phase 1：核验流程契约（每批次的产出物契约）
└── tasks.md             # Phase 2 output ($speckit-tasks command)
```

### Source Code (repository root)

```text
tools/                    # 增量核验工具落位于此（复用优先，缺口最小化）
specs/005-translation-campaign/   # 批次账本与会话协议（并行执行复用）
```

## Phase 0 设计要点（research.md 详述）

1. **机制盘点**：六条 FR 逐条映射既有工具能力，识别三个增量缺口——(a) 中英节序列对照（FR-003/004 现仅逐条 compare，无批量核验报告）；(b) 三方目录核验的"按批次出具差异清单"（现有门禁是全库单报告）；(c) 复核记录的结构化留痕格式（现有 tasks evidence 为自由文本）。
2. **裁决**：增量工具以"产出核验报告 + 走既有裁定流程"为边界，不新造目录改动逻辑（目录修正仍走显式裁定）。

## Phase 1 设计要点

* data-model.md：核验实体（批次核验报告/差异项/变更记录/复核记录）与状态机（差异项：静默→裁定→修正→闭环）。
* contracts/：每批次核验的产出物契约（报告结构、差异项字段、复核记录字段）。
* quickstart.md：会话领取批次 → 运行核验 → 出报告 → 裁定 → 复跑收敛的标准动线。

## Constitution Check（Phase 1 后复核）

* 增量工具不绕过既有门禁（check_all 仍为总闸）✅
* 差异裁定走单一事实源流程，核验器只报告不修改 ✅
* 批次并行复用 specs/005 会话协议（认领互斥、断点续上）✅

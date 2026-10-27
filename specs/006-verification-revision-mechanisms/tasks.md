# Tasks: 全流程一致性验证与修订机制

**Branch**: `006-verification-revision-mechanisms` | **Date**: 2026-10-27 | **Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

**输入文档**：research.md（机制盘点与三缺口）、data-model.md（实体与状态机）、contracts/verification-contract.md（产出物契约）、quickstart.md（标准动线）

**并行执行**：任务按批次并行（复用 specs/005 批次账本：campaign.py claim 互斥、断点续上）；标 `[P]` 的任务可与其他批次同类任务并行；标 `[顺序]` 的有前置依赖。

## Phase 1: Setup

- [ ] T001 建立 specs/006 报告落位目录 `reports/` 与批次报告命名约定（`reports/<batch>.json`，契约 1）
- [ ] T002 核对既有核验工具可运行基线：check_summary / check_mulu_s / rebuild check / fetch_audit / check_math / check_academic 全绿（run: `check_all --quiet`）

## Phase 2: Foundational（阻塞全部用户故事）

- [ ] T003 `[顺序]` 实现批次核验组织层（契约 1）：按 a–z 批次运行三类核验（目录/抓取/转换），汇总产出 `reports/<batch>.json`（findings/coverage/verdict 字段）
- [ ] T004 `[P]` 差异项状态机落地：DiffItem（silent→ruled→fixed→closed）在批次报告中的登记与裁定字段（契约 2）
- [ ] T005 `[P]` 结构化复核记录格式落地：ReviewRecord 字段（subject/doubt/ruling/evidence_anchor/reviewer/recomputed）落位任务 JSON reviews 数组或批次复核报告（契约 4）

## Phase 3: US-1 三方目录一致性核验（P1）

**Story 目标**：每批次出具"SUMMARY↔官方快照↔mu-lu-s"差异清单，静默差异 0

**独立测试**：任取批次运行目录核验，差异清单每条指向显式裁定或修正提交

- [ ] T006 `[P]` 按批次运行既有目录门禁与上游对照（check_summary / check_mulu_s / rebuild check / summary_sync report / upstream-increment），逐批汇总目录差异清单（FR-001）
- [ ] T007 `[P]` 别名与递归条目专项核验：别名 100% 链接有效、递归条目不产生断链（FR-001；ADR-0007/0009 语义）
- [ ] T008 `[顺序]` 差异项逐条显式裁定（豁免/增量登记/修正提交），批次报告 silent 归零（契约 2；SC-001）

## Phase 4: US-2 抓取内容完全离线（P1）

**Story 目标**：引用闭包收敛，缺省件 100% 登记，覆盖率报告出具

**独立测试**：任取批次审计，四项计数（审计/完整/缺省件/可补抓），可补抓为 0

- [ ] T009 `[P]` 按批次运行引用闭包审计（fetch_audit），逐批覆盖率计数入批次报告（FR-002；SC-002）
- [ ] T010 `[P]` 缺省件 100% 显式登记核对（上游本没有 vs 应抓未抓），补抓走 fetch_audit 自动补齐（FR-002）

## Phase 5: US-3 转换保真与中英结构一致（P1）

**Story 目标**：中英节序列对照报告覆盖批次内全部词条，保真零静默偏差

**独立测试**：任取词条比对中英节序列（数量/顺序/标题）+ 公式/表格/脚注计数一致

- [ ] T011 `[顺序]` 实现中英节序列批量对照（复用 compare.py 节序列解析，FR-003/004；research 缺口 G2）
- [ ] T012 `[P]` 按批次运行节序列对照，逐词条输出（节数量/顺序/标题差异）入批次报告（FR-003/004）
- [ ] T013 `[P]` 公式/表格/脚注计数对照入批次报告（FR-003；check_math 全量门禁为总闸）
- [ ] T014 `[顺序]` 不一致项显式登记或修正，批次报告 silent 归零（契约 2）

## Phase 6: US-4 修订吸收机制（P2）

**Story 目标**：模拟/真实修订全链演练通过（检测→变更记录→任务→闭环）

**独立测试**：变化被检测、变更记录含节级定位、任务建立并闭环

- [ ] T015 `[顺序]` 变更记录闭环字段落地（ChangeRecord：open→claimed→closed，含处理人/方式/验证证据，契约 3；FR-005）
- [ ] T016 `[P]` 模拟修订全链演练（compare --html 模拟变更 → 变更文件 → update 任务 → 处理 → 闭环验证），演练产物清理并留痕（SC-004）
- [ ] T017 `[P]` 存档季例行调度登记（3/6/9/12 月 21 日 fetch_catalog + compare 全量，零噪音验证：无变化时报告无变化，FR-005）

## Phase 7: US-5 复核与校对机制强化（P2）

**Story 目标**：复核留痕 100%、证据锚点 100%、独立重算 0 差异

**独立测试**：任取批复核记录抽查（结构化字段齐 + 换命令重算）

- [ ] T018 `[P]` 复核记录结构化落地试运行：任取一批次为已核条目补结构化 ReviewRecord（FR-006；T005 字段）
- [ ] T019 `[P]` 批次抽查机制落地：独立重算（换命令/换环境）+ 0 信任核对记录入批次报告（FR-006；SC-005）
- [ ] T020 `[顺序]` 违规判定规则登记：改写无英文源锚点且无译注 → 违规回炉（契约 4；rules/07 联动）

## Phase 8: Polish

- [ ] T021 全库收敛验证：核验轮次迭代至差异项 0 新增，覆盖率报告全库出具（SC-002/SC-003）
- [ ] T022 执行记录与 G4 门禁记录入 specs/001 execution-log（doctrine 最小字段）
- [ ] T023 文档同步：契约变更回写 specs/001 contracts、暴露问题回流 spec.md（版本号 v1.x）

## 依赖与执行顺序

```text
Phase 1 Setup → Phase 2 Foundational（T003/T004/T005）
  → Phase 3/4/5 可并行（US-1/2/3 各自独立可验；批次为并行单元）
  → Phase 6/7（US-4/5，依赖 Phase 3-5 建立的对应关系）
  → Phase 8 Polish（T021 依赖全部批次核验收口）
```

## 并行执行示例

```text
会话 A：领批次 a → T006 目录核验 → T009 抓取核验 → T012 节序列对照 → T008 裁定
会话 B：领批次 b → 同上（批次账本互斥，无耦合）
会话 C：T005 复核记录格式（与 A/B 并行）
```

## MVP 范围建议

Phase 1–4（T001–T010）即交付价值：目录与抓取两类核验按批次出具、静默差异归零。

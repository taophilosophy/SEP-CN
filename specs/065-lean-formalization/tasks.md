# 任务清单：065 Lean 引入处置与机械化编目

- 输入：`specs/065-lean-formalization/spec.md`（rev 1）、§1 决策记录 D-1–D-6、§2 外部事实钉、§3 与 064 边界表
- 状态：**2 项已验证（T001、T002）；13 项未开始（T003–T015）**。合计 **15 个编号**（W2／W3 经 2026-11-28 复核后全部批准落号）
- 编号纪律：本文件 `T001–T015` 为本卡自有序号；新增任务从下一可用号顺序分配，不预写占位号
- 门禁编号：不预写“第 N 项”；以 `check_all.py --list-gates` 实际输出为准
- ADR 编号：不预占；实施前重读 `rules/adr/` 尾部取实际最大号
- 格式：`[ID] [工作包] 描述（含文件路径与验收）`；`[P]`＝不同文件、无依赖，可并行
- 证据路径：一律落 `specs/065-lean-formalization/results/`，命名见 `results/README.md`
- 零代码纪律：W0／W1 只做检索、对接与文档；不建 Lean 工程、不改工具链、不进 CI

## 工作包 W0 基点与候选池

- [x] T001 [W0] 复算候选池：`grep` 全库 `en/` 显式 Proof 节与展示公式词条，逐件记录 slug、节标题、行号、形式内容类型（证明／推导／模型构造／其他）；产出 `results/proof-candidates.tsv`。**已完成**（2026-11-28：命中 30 ＝候选 28（补充证明页，归属 5 词条）＋题名误命中 2；含 `$$` 文件 416；方法见 `results/t001-counts.md`）；验收：30／416 与评估口径一致，差异（2 件题名误命中）逐条说明
- [x] T002 [W0] 编目 schema 与骨架：`results/catalog.md` 表头与字段说明（slug／证据节／对接成果／来源 URL／版本或提交钉／三分类／凭据），与 spec §0.4.2 字段一致。**已完成**（2026-11-28：字段定义＋固定枚举＋收口判据入档）；验收：字段齐备、三分类枚举固定（已机械化／可对接／无从对接）

## 工作包 W1 机械化编目

- [ ] T003 [W1] Gödel／不完备族对接：候选池中不完备性相关词条逐件对 FFL（Gödel I／II 2024-09 sorry-free、Rosser、Löb、Tarski、Church）与 Isabelle AFP（Popescu／Traytel 抽象版）检索配对。验收：每件给出对接成果名、来源 URL、版本钉、分类与凭据（前置 T001）
- [ ] T004 [W1] 模态／可证性逻辑族对接：对 Solovay GL 算术完备性（FFL 2025-04）、lean4-logic（K／KD／S4／S5、Gödel–McKinsey–Tarski）检索配对。验收：同 T003 字段（前置 T001）
- [ ] T005 [W1] 集合论／模型论族对接：对向下 Löwenheim–Skolem、ZFC 相对一致性、切消除等 FFL 成果检索配对。验收：同 T003 字段（前置 T001）
- [ ] T006 [W1] 其他族对接：按候选池剩余项分配；无既有成果者标“无从对接”并留检索记录（查询式与结果状态）。验收：候选池 100% 有分类，无静默跳过（前置 T001）
- [ ] T007 [W1] 编目总表收口：三分类 100%、凭据逐条、URL 与版本钉齐全；复算总数与候选池一致；产出 `results/catalog.md` 定稿。验收：独立复算一致；无未处置告警（前置 T002–T006）
- [ ] T008 [W1] 译注对接：仅对“已机械化／可对接”件，按 ADR-0076 勘误通道产出译注／勘误条目（`baseline/en-errata/en-errata.md` 或词条译者注释节），格式合规、双向可追溯。验收：`check_academic --strict` 与 `check_pairs` 全绿；勘误条目与编目表互链（前置 T007）

## 工作包 W2 A 轨替代：PBT 试点（已批准 2026-11-28）

- [ ] T009 [W2] 试点方案与属性清单：状态机 vs 对账生成器；属性（幂等／守恒／round-trip）；与 064 T166 边界；`hypothesis` 引入方式；产出 `results/t009-pbt-plan.md`。验收：属性逐条对应现有函数与判据，边界声明明确，可独立复算
- [ ] T010 [W2] `hypothesis` 依赖接入与 CI 步骤（若 T009 判定需入 CI）：依赖声明、`check_all.py` 实际门禁清单为准（不预写项号）。验收：CI 绿、本地可重放（前置 T009）
- [ ] T011 [W2] 属性测试编写：落 `tools/tests/`；确定性重复（同种子同结果）；不重复 064 T166 既有用例。验收：测试通过、复算一致（前置 T009；与 T010 可并行）
- [ ] T012 [W2] 收口报告：`results/t012-report.md`（三段式：做了什么／残余与豁免／作废判据）。验收：报告入库、复算记录齐全（前置 T011）

## 工作包 W3 从零形式化试点（已批准 2026-11-28；先立 ADR）

- [ ] T013 [W3] 立 ADR＋验收判据＋作废条件：合格线＝引用既有机械化定理而非自证；ADR 号取 `rules/adr/` 实际最大号并更新 `rules/adr/README.md`。验收：ADR 入库、索引一致
- [ ] T014 [W3] 选 1–2 条候选并形式化（须 T013 完成且 Mathlib 缓存迁移解除）：Lean 工程放 `specs/065-lean-formalization/bin/`（不新增根级条目，ADR-0023）；产出 `results/t014-*.md`＋工程。验收：sorry-free、无 sorryAx、引用既有定理清单与版本钉（前置 T013）
- [ ] T015 [W3] 独立复算收口：编译复算（Linux CI 侧 `lake check`）、范围正向陈述、证据快照。验收：报告＋快照入库（前置 T014）

## 执行记录

- T001（2026-11-28）：候选池复算完成——30 命中 ＝ 28 候选（bayes-theorem 1、common-knowledge 13、frege-theorem 10、infinity 1、kochen-specker 3）＋ 2 题名误命中（proof-theory、proof-theoretic-semantics）；含 `$$` 文件 416。证据：`results/proof-candidates.tsv`、`results/t001-counts.md`。
- T002（2026-11-28）：编目骨架完成——字段定义、三分类枚举、收口判据入 `results/catalog.md`。

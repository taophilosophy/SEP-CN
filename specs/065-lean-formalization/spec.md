# 065 — Lean 引入处置与机械化编目任务书

- 编号：`specs/065-lean-formalization`；立项日期：2026-11-28；**状态**：rev 2 全部批准（W0 已执行；W1–W3 待开工）
- 承办：主会话（ADR-0034 主代理单干）
- 上位：项目宪法（`.specify/memory/constitution.md`）、`rules/` 与其 ADR；机读事实源仍以 `rules/pipeline.json`（节点与判据）、`rules/naming.json`（标识）、`rules/axioms.json`（P1–P33）、`rules/standards.json`（标准登记）为准
- 兄弟卡：`specs/064-flow-spec-audit`（翻译全流程全要素审计、公理化、标准化与规范化）。**本卡不复制其任何范围**；边界见 §3。064 §0.3.6 的“不另立 065”只约束 064 自身的建议线（2026-11-26 裁定），本卡为 2026-11-28 用户新指令所立的独立论域，不构成对该裁定的违背
- 版本：**rev 2**（2026-11-28；用户复核后全部批准 → D-4／D-5 转已批准，W2／W3 落号 T009–T015；W0 已执行）
- 施工图：`tasks.md`（W0／W1 共 8 个编号；W2／W3 待裁定，不预写编号）
- 事实口径：`current`＝事实源现状；`target`＝拟议目标；`approved`＝用户批准范围；`verified`＝已有验收证据；四者不得互代

## 0 方向声明（rules/08 §1）

### 0.1 指令链

| 轮次 | 用户指令 | 产出 |
| ---- | ---- | ---- |
| 1 | 评估引入 lean 证明的意义、可行性、价值、后果（2026-11-28） | 双轨评估框架（A 工程规格形式化／B 词条形式内容保真） |
| 2 | 裁定：双轨全面评估 | 两轨各给四维结论与统一建议，含联网检索凭证 |
| 3 | 立 065 任务书和 specs，不要与 064 任务书重复；继续 | 本卡 rev 1 |
| 4 | **复核后全部批准**（2026-11-28） | rev 2：D-4／D-5 转已批准；W2／W3 编号 T009–T015；W0 开工（T001–T002 完成） |

### 0.2 目标

1. 把 Lean 引入评估的结论固化为可复核的决策记录（D-1–D-6，§1），附外部事实钉（§2）。
2. 把唯一获准的衍生形态落为可执行工作包：**机械化编目**——既有机器验证成果与 `en/` 形式内容词条的对接目录及译注（W1）。
3. 为 A 轨（工程规格形式化）登记替代方案口径：property-based testing 试点（W2，范围待裁定）。
4. 登记重评触发条件与作废条件（§6），防止此线反复重启。

### 0.3 非目标

1. 不把 Lean 引入主管线：不进 `check_all.py`、不进 CI、不进站点构建、不新增根级条目（ADR-0023）。
2. 不做词条从零形式化（D-4 未裁定；若将来启动，须先立 ADR＋验收判据＋作废条件，合格线为“引用既有机械化定理”而非自证）。
3. 不重复 064 的任何任务：翻译流程审计、公理化、标准映射与回写、E2E 试点词条、TBX／概念库、测试补齐均属 064（边界见 §3）。
4. 不动 `en/`、`html/`、`zh/` 正文、任务 JSON、登记册数据。
5. 不新增标准登记；涉标准引用沿用 064 §0.1a 已登记基线，并按 ADR-0088／0089／0090 的配对与库名如实纪律执行。
6. 不设常驻监控：重评触发由用户裁定或 064 线发现后按 §6 处置。

### 0.4 验收判据（本卡整体）

1. 本卡入库，`check_all.py` 全绿（本卡自身不新增门禁项）。
2. W1 编目表每条候选具备：词条 slug、证据节位置、对接成果名、来源 URL、版本或提交钉、三分类结论（已机械化／可对接／无从对接）、凭据。
3. W2 若启动：属性测试入 `tools/tests/`，确定性重复（同种子同结果），且不重复 064 T166 既有用例。
4. 译注对接若产出：走 ADR-0076 勘误通道，格式合规、双向可追溯。

### 0.5 作废条件

1. Mathlib Initiative 缓存基建迁移期间（2026 Q4–2027 Q1）不启动任何 Lean 代码类工作；W3 永远受此约束。
2. 规格-代码鸿沟无法用现有门禁表达时，停止扩展任何形式化工作。
3. 用户裁定“全盘引入 Lean”或“彻底删除本线”时，本卡按新裁定重写或废止。

## 1 评估结论（决策记录）

| 编号 | 结论 | 主要理由（证据钉见 §2） | 状态 |
| ---- | ---- | ---- | ---- |
| D-1 | A 轨（工程规格形式化）**否决** | 对账四原则恰为 property-based testing 性质，直测真实实现优于对模型证明；Rust 稳态判据内核为既定最高保障线（三门定案 2026-11-26）；Lean 证明对象是模型而非代码，规格-代码鸿沟与判例四“卡内互证假一致”教训冲突；成本阶梯上证明助手属最高档（10–50× 换边际保障）；破坏工具链节俭先例 | 立卡依据 |
| D-2 | B 轨（词条形式内容）**不作为翻译质量工序** | 项目 oracle 是对 `en/` 的保真（I2／I3 重放已机械等值），公式转录已有 `check_math_zh` 与 MathJax 全源码覆盖；`en/` 全库显式 Proof 节仅 30 件（2421 件中），SEP 证明多为非正式概要，形式化属重构而非校验；2026 综述钉“编译通过≠忠实表达源意图” | 立卡依据 |
| D-3 | 唯一正当衍生形态＝**机械化编目** | 既有 sorry-free 成果现成（§2.3），只做对接与译注，低成本、不动管线、撤出成本≈0；与 ADR-0076 勘误通道兼容 | 立卡依据（W1） |
| D-4 | 从零形式化试点 1–2 条 | 合格线＝引用既有机械化定理而非自证；须先立 ADR＋验收判据＋作废条件 | **已批准**（2026-11-28；W3，T013–T015） |
| D-5 | A 轨替代＝property-based testing 试点 | `hypothesis` 直测对账生成器／任务状态机属性（幂等、守恒、round-trip）；不重复 064 T166 既有用例 | **已批准**（2026-11-28，范围按建议口径；W2，T009–T012） |
| D-6 | 重评触发 | 状态机演化为并发协议／分布式语义时，重议 TLA+／P（非 Lean）；AI 形式化出现可审计的忠实性标准时，重议 B 轨 | 登记（§6） |

## 2 外部事实钉（2026-11-28 检索）

### 2.1 Lean 生态

- Lean v4.35.0（2026-10-12）为最新稳定版，月度发版、无 semver；下游按 `v4.X.Y` 钉工具链（[Math 2.0 研究底表](https://math2.tamnd.com/spec/01-research-2026/)）。
- mathlib 约 248 万行／29.1 万定理／772 贡献者（2026-10-25 统计）；`lake exe cache get` 需拉取 5000+ 文件；Mathlib Initiative 缓存基建迁移 2026 Q4–2027 Q1（[roadmap](https://mathlib-initiative.org/roadmap/)）。
- `lake check` 沙箱重核（4.35 新增）**Linux-only**；CI 即便挂接也只能在 Linux 侧执行。

### 2.2 AI 形式化 SOTA

- Aristotle（Harmonic）：IMO 2025 金牌等价 5/6，仅题面人工形式化，200B+ 模型＋大规模并行搜索（[arXiv 2510.01346](https://arxiv.org/html/2510.01346v1)）。
- Gauss（Math, Inc.，DARPA expMath 资助）：强素数定理 3 周约 2.5 万行 Lean，官方口径“依赖人类数学家提供自然语言脚手架、需高层专家指导”（[math.inc/gauss](https://www.math.inc/gauss)）。
- 2026 综述：编译通过只证明“在指定环境中可展开”，不证明忠实表达源意图；规格忠实性（specification fidelity）未解，验证范围须正向陈述（[arXiv 2607.07779](https://arxiv.org/html/2607.07779v2)）。

### 2.3 既有机械化成果（编目对接源）

- Lean 4 FormalizedFormalLogic：Gödel I／II sorry-free（2024-09，首个完全算术内）、Solovay GL 算术完备性（2025-04）、向下 Löwenheim–Skolem、切消除、Löb、Tarski、Church、ZFC 相对一致性（[论文](https://formalizedformallogic.org/Mechanizing-Godels-Incompleteness-Theorems-and-Provability-Logic/main.pdf)、[仓库](https://github.com/FormalizedFormalLogic/Foundation)）。
- Isabelle AFP：Popescu／Traytel 抽象版 Gödel 不完备性（[AFP 条目](https://isa-afp.org/entries/Goedel_Incompleteness.html)）。
- mathlib `docs/100.yaml` 已收录哥德尔不完备；lean4-logic 覆盖模态 K／KD／S4／S5 与一阶完备性（[仓库](https://github.com/FormalMathematicsLab/lean4-logic)）。

### 2.4 哲学侧工具（对照物，不引入）

- Carnap：50+ 形式系统、按教材证明规则镜像、累计 400 万题／4.5 万学生（[Carnap Ten Years Later](https://arxiv.org/html/2607.07722)）。
- Open Logic Project／forall x Calgary 与 ndprover（[forallx.openlogicproject.org](https://forallx.openlogicproject.org/)）。

### 2.5 成本参照

- AWS：形式方法是选择性补充能力，最适并发／容错设计；工程师 2–3 周可上手 TLA+（[CACM 2015](https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/)、[ACM FACS 2026 批判性评估](https://dl.acm.org/doi/10.1145/3815784)）。
- Hillel Wayne：实现量不足一周的东西不值得规格化（[business case](https://www.hillelwayne.com/post/business-case-formal-methods/)）。
- 成本阶梯：证明助手为最高档（月—年级、专家技能；整机校验 10–50× 边际保障）。

### 2.6 本地基数（2026-11-28 复算）

- `en/` 2421 件中显式 Proof 节 30 件、含展示公式 416 件（候选池上限）。
- 门禁 23 项（`check_all.py --list-gates` 实测）、管线单测 807 件（049 提交口径）。
- 正式词条 1873 件、未开工骨架 1862 件（`zh/PROGRESS.md` 2026-11-28）。

## 3 与 064 的边界（防重复）

| 域 | 064 是否管 | 065 是否管 | 说明 |
| ---- | ---- | ---- | ---- |
| 翻译流程节点／状态机／门禁的审计与规范化 | 管 | 不管 | 属 064 公理化与规范化范围 |
| ISO／GB／CY/T 标准映射与回写 | 管 | 不管 | 065 不新增标准登记 |
| E2E 试点词条（habermas 等 11 件） | 管 | 不管 | 064 S-1／S14 |
| TBX／概念库与机器生产治理 | 管 | 不管 | 064 T172 线（ADR-0094） |
| 管线单测补齐 | 管（T166） | 不管 | 065 W2 若启动只做属性测试，不重复既有用例 |
| Lean／形式化处置与机械化编目 | 曾明示不涉（其 §0.3.6 只约束自身建议线） | 管 | 本卡论域 |
| 重评触发（并发协议／AI 忠实性标准） | 不管 | 管 | §6 |

## 4 工作包

### W0 基点与候选池（T001–T002）

- T001 复算候选池：`en/` 显式 Proof 节清单＋形式内容类型，产出 `results/proof-candidates.tsv`。
- T002 编目 schema 与骨架：`results/catalog.md` 表头与字段说明，字段与 §0.4.2 一致。

### W1 机械化编目（T003–T008）

- T003 Gödel／不完备族对接（FFL、AFP）。
- T004 模态／可证性逻辑族对接（Solovay GL、lean4-logic）。
- T005 集合论／模型论族对接（Löwenheim–Skolem、ZFC 相对一致性）。
- T006 其他族对接（切消除、Löb、Tarski、Church 等，按候选池分配）。
- T007 编目总表收口：三分类 100%、凭据逐条、来源 URL 与版本钉齐全。
- T008 译注对接：仅已对接件，按 ADR-0076 通道产出译注／勘误条目。

### W2 A 轨替代：PBT 试点（已批准 2026-11-28；T009–T012）

- T009 试点方案与属性清单：状态机 vs 对账生成器、属性（幂等／守恒／round-trip）、与 064 T166 边界、`hypothesis` 引入方式。
- T010 `hypothesis` 依赖接入与 CI 步骤（若 T009 判定需入 CI；门禁项号以实际清单为准）。
- T011 属性测试编写（落 `tools/tests/`；确定性重复；不重复 T166 既有用例）。
- T012 收口报告（三段式：做了什么／残余与豁免／作废判据）。

### W3 从零形式化试点（已批准 2026-11-28；T013–T015；先立 ADR）

- T013 立 ADR＋验收判据＋作废条件：合格线＝引用既有机械化定理而非自证；ADR 号取 `rules/adr/` 实际最大号，并更新 `rules/adr/README.md`。
- T014 选 1–2 条候选并形式化（须 T013 完成且 Mathlib 缓存迁移解除）：Lean 工程放 `specs/065-lean-formalization/bin/`，不新增根级条目（ADR-0023）；要求 sorry-free、无 sorryAx、引用既有定理清单与版本钉。
- T015 独立复算收口：编译复算（Linux CI 侧 `lake check`）、范围正向陈述、证据快照。

## 5 执行纪律

- 开工前重读 `check_all.py --list-gates` 实际输出与 `rules/adr/` 尾部实际最大号；不预占门禁项号与 ADR 编号。
- 每任务独立收口，证据落 `specs/065-lean-formalization/results/`；文件命名见 `results/README.md`。
- 小步提交、中文一行信息、只提交相关文件、提交即推（ADR-0059）。
- W1 全程零代码依赖：只做检索、对接与文档，不建 Lean 工程、不改工具链。

## 6 重评触发与作废条件

| 触发 | 判据 | 处置 |
| ---- | ---- | ---- |
| 状态机演化为并发协议／分布式语义 | `task_ops`／管线出现并发写入或分布式状态语义 | 重议 TLA+／P（非 Lean），另立规格 |
| AI 形式化出现可审计的忠实性标准 | 出现可复核的“形式化陈述≡源意图”判定流程与工具 | 重议 B 轨（D-2），评估是否入管线 |
| Mathlib 缓存迁移完成 | Initiative roadmap 宣布迁移收口 | 解除 §0.5.1 对 Lean 代码类工作的冻结（仅影响 W3） |
| 用户裁定全盘引入或删除本线 | 显式指令 | 按新裁定重写或废止本卡 |

## 7 变更记录

- rev 1（2026-11-28）：立项。固化评估结论 D-1–D-6；立 W0／W1 任务；W2／W3 待裁定。
- rev 2（2026-11-28）：用户复核后全部批准。D-4／D-5 转已批准；W2／W3 落号 T009–T015；W0 执行（T001–T002 完成：候选池 28 件候选＋2 件题名误命中、416 件含展示公式；编目骨架落 `results/catalog.md`）。

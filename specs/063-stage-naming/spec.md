# 063 — 阶段轨命名与线级标记登记（stages＋marks 双块，五段制）

- 编号：specs/063-stage-naming；立项日期：2026-11-26；状态：待执行（rev 2，2026-11-26 用户裁定消解 ex 段）
- 承办：主会话（[ADR-0034](../../rules/adr/0034-主代理单干.md) 主代理单干）
- 上位：[ADR-0080](../../rules/adr/0080-节点标识三层与状态名统一.md)（节点标识三层）、specs/062-phase12-recheck（阶段 1.1／1.2 先例）、specs/061-standards-realignment-2026（标准对照基线）、`rules/naming.json`（标识类事实单一事实源）、`rules/08-intent-first.md`（知难行易）
- 类型：结构登记＋机检扩展（不翻译、不改历史正文）

## 0. 方向声明（rules/08 §0）

### 0.1 指令链（2026-11-26，用户逐轮裁定）

1. 仿照阶段 1.1/1.2 对其余翻译流程阶段重新进行标准化命名，结合国内国际标准给出建议。
2. 阶段不够细粒度，22 节点应分别归入某个 x.y。
3. 旧的 B0–B3 等标记仍然保留（重新拟定）——B0–B3、G1–G5、I1–I6、T0–T3、q1–q6、W/O、D1–D5、P 系列等旧字母数字标记**一律保留原名原义**，撤撞名消解与加前缀改造。
4. 1.4（资产闭包审计）、1.5（补丁池体检）撤号并入 1.2（站内工序承载）；1.3 保留独立站（节律与凭证硬差异）。
5. 1.1 显式分两半段（联网抓取／离线复核，`--offline` 模式与 CI 编排面为证）。
6. 1.2／1.3 与大段 2 的关系定为：大段 2 提供工序、1.2 批量编排、1.3 交割给生产线；三条不变量＝判据单源、ex-04 唯一、交割无旁路。
7. 不把阶段 2 变成 1.2.1–5 而保持编号独立（`calls` 字段表达的方案）。
8. **【rev 2 裁定】将阶段 2 消解进 1.2／1.3 成为其子节**——大段由六段缩为五段，ex 五节点按用途分配（ex-01／02／03／05 入 1.2，**ex-04 入 1.3.3 放行门**）；三级号（`N.M.K`）就此引入，取代 `calls` 字段与 SOP 步骤号双轨；大段 2–4 维持 M＝段内节点号。

### 0.2 目标

建立**阶段轨**（stages，三级 `N.M[.K]`）与**线级标记层**（marks），与节点轨（ADR-0080 的 22 节点 ex/tr/rv/sg）衔接：阶段轨管“站序与全库战役编址”，节点轨管“工序标识”，marks 管“各专项线既有标记的登记与挂靠”。阶段划分与术语对齐 ISO 17100:2015／GB/T 19363.1-2022，使流程对外可声明。

**关键结构选择（rev 2）**：ex 段不设独立大段，五节点按用途寄居于源侧段——四个批量镜像工序入 1.2，源审计放行门入 1.3。这样“1.3 是源侧出口、ex-04 是出口闸门”的语义与“交割无旁路”不变量天然一致。

### 0.3 验收判据（概要，详见 §4）

stages 40 项＋marks 10 项入册；S7 扩展五条校验生效并经反例试金石验证；22 节点归属唯一且 ex 五节点分配固定；旧标记来源文件零改写；specs/062 仅加头注一行；ADR-0089 登记；`check_all` 全绿；提交即推。

## 1. 命名体系定案

### 1.1 三层阶段语言

| 层 | 编号形态 | 承载内容 | 事实源 | 写入面 |
| ---- | ---- | ---- | ---- | ---- |
| **节点轨**（ADR-0080 既定，不动） | `ex-01`…`sg-03` | 单词条工序标识：journal、tasks.steps、状态机、PROGRESS 计数 | `rules/naming.json` nodes 块 | 逐件执行 |
| **阶段轨**（本卡新立） | `N.M` 或 `N.M.K`（正则 `^[1-9]\.[0-9]{1,2}(\.[0-9]{1,2})?$`） | 站序位置＋全库战役／维护编址；不进 journal、不进状态机 | `rules/naming.json` stages 块 | spec 卡、执行账、跨卡引用 |
| **线级标记层**（本卡登记，不改现状） | 字母前缀原样（B0–B3、G1–G5…） | 各专项线内部递进阶段与判据号 | `rules/naming.json` marks 块 | 原线内继续流通 |

三层规则：阶段号管“站与站内工序”，marks 管专项线内记号。**三级号取代原 SOP 步骤号**——`specs/062/sop.md` 的九步今后即 1.2.1–1.2.9，两套编号合一。`calls` 字段不再使用（从属由编号直接表达）。

### 1.2 五段划分与映射规则

| 大段 | 名称 | 与 seg 关系 | 子节编号规则 |
| ---- | ---- | ---- | ---- |
| 1 | 源侧镜像与交割 | seg1（英语文本提取）＋维护 | 按作业序编 M.K；ex 节点固定寄居（见 §1.4） |
| 2 | 中文翻译 | seg2 | **M＝段内节点号**（2.1↔tr-01 … 2.5↔tr-05） |
| 3 | 审阅校对 | seg3 前段 | **M＝段内节点号**（3.1↔rv-01 … 3.9↔rv-09） |
| 4 | 终审签字与发布 | seg3 末段 | **M＝段内节点号**（4.1↔sg-01 … 4.3↔sg-03） |
| 5 | 战役与治理 | 组织级，无 seg | M 按登记序，不绑节点 |

节点预留随号段自动预留：tr-06–09→2.6–2.9、rv-10–19→3.10–3.19、sg-04–09→4.4–4.9、ex-06–09→1.2.10–1.2.13 或 1.3.4 起（按用途）。

### 1.3 阶段总表（stages 块 40 项全列）

**大段 1：源侧镜像与交割**

| 号 | name | label | 节点 | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1.1 | mirror.catalog-recheck | 目录抓取与四方互转 | — | 源文本接受（5.3） | accepted（specs/062） |
| 1.1.1 | mirror.catalog-fetch | 抓取半段：落钉存快照、重建 catalog 账、四差集 | — | — | accepted |
| 1.1.2 | mirror.catalog-replay | 复核半段：G1–G5、四方差集、mulu 六项、官方快照（`--offline` 可重放；CI 每日三班跑此面） | — | — | accepted |
| 1.2 | mirror.refetch-recheck | HTML 重抓·基线·补丁复核（批量） | — | 源文本接受（5.3） | accepted（specs/062） |
| 1.2.1 | extract.fetch | 抓取与版本钉 | **ex-01** | 前期准备（5.3） | accepted |
| 1.2.2 | extract.convert | HTML 转 Markdown | **ex-02** | 前期准备（5.3） | accepted |
| 1.2.3 | extract.fidelity | 转换保真校验（挂 I1–I6） | **ex-03** | 前期准备（5.3） | accepted |
| 1.2.4 | extract.format | 镜像格式闭合（补丁应用与命中校验） | **ex-05** | 前期准备（5.3） | accepted |
| 1.2.5 | mirror.asset-closure | 资产闭包审计（`fetch_audit` 至不动点） | — | — | accepted |
| 1.2.6 | mirror.delta-classify | 差集分类（`en_delta` new/layout/tokens/text ＋`entry_meta_delta`） | — | — | accepted |
| 1.2.7 | mirror.patch-recheck | 补丁复核三判定（必要性／有效性／一致性） | — | — | accepted |
| 1.2.8 | mirror.b-ledger-refresh | B 族账本刷新（挂 B0–B3.2） | — | — | accepted |
| 1.2.9 | mirror.progress-report | 进度报告（覆盖／I2／B3.1／B3.2／池面） | — | — | accepted |
| 1.3 | mirror.change-settle | 上游同步与建账交割 | — | 源文本接受（5.3） | registered（specs/001） |
| 1.3.1 | mirror.change-intake | 变更识别与建账（`compare` → create／reopen --clear／--upstream-sync） | — | — | registered |
| 1.3.2 | mirror.wipe | 置空（`clear`，仅留 H1；基线 gate 照常） | — | — | registered |
| 1.3.3 | extract.source-audit | **源审计放行**（en_integrity＋en_source_audit；零信任出口） | **ex-04** | **源文本接受性检查**（5.3） | accepted |

**大段 2：中文翻译（seg2）**

| 号 | name | label | 节点 | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2.1 | translate.preprocess | 译前预处理 | tr-01 | 术语工作（5.3；语义错位已注记） | accepted |
| 2.2 | translate.draft | 初译 | tr-02 | **笔译**；LLM 件＝**译后编辑**（ISO 18587:2017／GB/T 40036-2021） | accepted |
| 2.3 | translate.accuracy | 准确性校（一校） | tr-03 | **自检**（checking，GB/T 3.2.5） | accepted |
| 2.4 | translate.fluency | 行文通顺校（二校） | tr-04 | **自检**（checking） | accepted |
| 2.5 | translate.format | 段内格式闭合 | tr-05 | — | accepted |

**大段 3：审阅校对（seg3 前段）**

| 号 | name | label | 节点 | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 3.1 | review.terminology | 术语与勘误锁定（挂 D1–D5） | rv-01 | **术语工作** | accepted |
| 3.2 | review.consistency | 全局一致性 | rv-02 | **双语审校**（revising，GB/T 3.4.5，**强制**） | accepted |
| 3.3 | review.cite | 引文锁定（挂 q1、T0–T3） | rv-03 | **单语审校**（review，GB/T 3.4.6） | accepted |
| 3.4 | review.logic | 逻辑一致性（q2） | rv-04 | 单语审校 | accepted |
| 3.5 | review.grammar | 语法与病句校（q3） | rv-05 | 单语审校 | accepted |
| 3.6 | review.register | 语域（q4） | rv-06 | 单语审校 | accepted |
| 3.7 | review.measure | 计量（q5） | rv-07 | 单语审校 | accepted |
| 3.8 | review.punctuation | 标点（q6） | rv-08 | 单语审校 | accepted |
| 3.9 | review.style | 体例终校 | rv-09 | **校对**（proofreading，GB/T 3.4.7；CY/T 266 计错） | accepted |

**大段 4：终审签字与发布（seg3 末）**

| 号 | name | label | 节点 | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 4.1 | signoff.verity | 受众适切性（初审） | sg-01 | **最终验证**（final verification） | accepted |
| 4.2 | signoff.coherence | 连贯性（复审） | sg-02 | 最终验证 | accepted |
| 4.3 | signoff.acceptance | 交付验收（终审；`--mandate`；CY/T 266 万分之一线） | sg-03 | 最终验证与**发布**（release） | accepted |

> 发布动作（提交即推＋壳仓拉取制，ADR-0059/0064）为大段 4 收尾动作，**不占号**（避免与 sg-04 预留撞号）。节点绑定子节 5（1.2.1–1.2.4＋1.3.3）＋5＋9＋3＝**22**，与节点总数对齐。

**大段 5：战役与治理**

| 号 | name | label | 落点 | 状态 |
| ---- | ---- | ---- | ---- | ---- |
| 5.1 | campaign.wipe-restart | 全库置空与重译启动 | ADR-0081/0082、specs/062 §6 | registered（已执行） |
| 5.2 | campaign.term-extraction | 术语全库提取 | specs/058 | active（在批） |
| 5.3 | campaign.en-template-audit | EN 模板审计（挂 B0–B3.2 阶梯） | specs/044/047/053 | active（在批） |
| 5.4 | campaign.mulu-recategorize | 目录六区重分类 | specs/055/056/057 | registered（已执行） |
| 5.5 | campaign.rework-backfill | 受控回炉与回补 | specs/028/030/052 | active（在批） |
| 5.6 | campaign.standards-review | 标准对齐复核（挂 061 号域） | specs/061 | registered（已收口） |

### 1.4 ex 节点寄居表（rev 2 核心）

ex 段不设独立大段，五节点按用途寄居于源侧段：

| 节点 | 寄居号 | 理由 |
| ---- | ---- | ---- |
| ex-01 抓取与版本钉 | 1.2.1 | 批量重抓的首道工序 |
| ex-02 HTML 转 Markdown | 1.2.2 | 重抓后随即批量转换 |
| ex-03 转换保真校验 | 1.2.3 | I2 复核属批量收口 |
| ex-05 镜像格式闭合 | 1.2.4 | 补丁批应用属批量收口 |
| **ex-04 源完整性审计** | **1.3.3** | **置空之后的放行门**——审计不在批量作业面，只在逐件交割时执行（任务状态机强制集，tr-02 之前） |

由此 1.3 成为完整的交割界面：**识别变更（1.3.1）→ 置空（1.3.2）→ 源审计放行（1.3.3）**，出口即“可译任务”。

### 1.5 三条关系不变量

1. **判据单源**：1.2 不是第二套判据，是同一组不变量（I1–I6、补丁准入、差集口径）的批量调用；批量路径绕过钉账纪律即事故（specs/062 `upsert_baseline` 无 `files` 拒收护栏为既有防线）。
2. **ex-04 唯一性**：审计只发生在 1.3.3 逐件过站，1.2 的任何子节不得调用审计；存量补课（specs/036）按 1.3.3 补做，状态不迁移。
3. **交割无旁路**：源侧世界进入翻译世界只经 1.3.1→1.3.2→1.3.3 这一条链；1.2 重抓再多件也不直接产生任务。

三条不变量各由 S7 第 2、3 条机检（见 §3）。

### 1.6 线级标记层（marks 块 10 项，原名全保留）

| prefix | range | line | attach（rev 2） | source | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| B | B0–B3.2（B3.1 装配／B3.2 判断） | en-template-audit | 5.3 主挂；1.2.8 刷新 | specs/044-b0b1-baseline、specs/047-structural-reverse-check、specs/053-en-template-audit | live |
| G | G1–G5 | catalog-network | 1.1.2 复核半段（五门入 CI） | specs/054-catalog-network-replay | live |
| I | I1–I6 | conversion-fidelity | 1.2.3 判据面 | ADR-0063 | live |
| T | T0–T3 | six-axis-rollback | 3.3–3.8 升档时相（主挂 3.3） | specs/060-six-axis-quality-gates | live |
| q | q1–q6 | six-axis-checklist | 3.3–3.8 轴标签与清单文件名 | specs/060；ADR-0080 既裁沿用 | live |
| D | D1–D5 | term-diff-classification | 3.1 定性判据 | rules/03-terminology.md | live |
| W/O | spec 内未决项 | per-spec | —（spec 内引用，跨卡须带 spec 号） | 各 spec | live |
| P | P1–P33 | axioms | 全流程引用 | rules/axioms.json | live |
| P | P1–P4 | legacy-node-name | — | ADR-0080 收编为 aliases | retired |
| G/D/P（061 号域） | 061-G1–G16、061-D1–D5、061-P0–P2 | standards-realignment | 5.6 历史凭证 | specs/061 | retired |

> marks 层**只登记不改写**：不重命名、不加前缀、不消解撞名（用户 2026-11-26 裁定）；跨线引用须带线名或 spec 号。ADR 与 spec 原文一字不动。

### 1.7 标准对照锚点（2026-11-26 联网核验）

- ISO 17100:2015＋Amd 1:2017（现行，修订 AWI 约至 2029）：§5.3 前期准备（源文本接受性、术语工作）、§5.4 翻译过程（笔译→自检→双语审校〔强制〕→单语审校〔可选〕→校对〔可选〕→最终验证与发布）。
- GB/T 19363.1-2022（等同采用 ISO 17100，现行）：**自检＝checking（3.2.5）、双语审校＝revising（3.4.5）、单语审校＝reviewing（3.4.6）、校对＝proofreading（3.4.7）**。
- 译后编辑：ISO 18587:2017／GB/T 40036-2021（ADR-0084 D2 已承接）。
- 评审质量：ISO 5060:2024（Verity／Annex E／评分卡）；计错：CY/T 266-2023。
- 命名与标识：ISO/IEC 11179-5:2015／GB/T 18391.5-2009（标识与名称分离、唯一、稳定、不复用）——阶段号 identifier 沿用同一哲学。
- 本项目 review／proofreading 做成强制工序是**超出基线**而非偏离（ISO 17100 中为可选），无需登记偏离项。

## 2. 非目标

1. 不改 22 节点 id／name／label（ADR-0080 既定），不动状态机、journal、tasks。
2. 不改写任何历史文档正文（specs/044/047/053/055–058/060/061、rules/03、ADR 全部原文不动）；specs/062 仅加头部注记一行。
3. 不实施 marks 的撞名前缀改造（用户裁定保留）；不改 q1–q6 清单文件名、B3.1/B3.2 工具名等任何现行用法。
4. 不改 1.1／1.2 已定名称与语义（用户 2026-11-25 裁定）；1.2 的九个子节为既有 SOP 九步的正式编号化，非新增工序。
5. 本卡不产出任何译文，不动 en/／yuanwen/／SUMMARY。

## 3. 实施步骤

1. **naming.json 升 v2**：schema 升 `sep-naming/v2`；增 `stages`（40 项，按 §1.3 全量登记，含 1.1.1／1.1.2 两半段）与 `marks`（10 项，按 §1.6）双块；`patterns` 增 stage identifier 三级正则；`revision` 补记 rev 2 消解 ex 段。
2. **S7 扩展**（`tools/check_stages.py`）五条校验：
   - ① stages 自洽：identifier 唯一、符合三级正则、`specs` 落点存在、status ∈ {accepted, registered, active, reserved}。
   - ② **节点归属唯一**：每个 pipeline 节点恰出现于一个 stages 子节（含预留号说明）；大段 2–4 的子节号须等于节点号（M＝节点号规则）。
   - ③ **ex 寄居表校验**：ex-01→1.2.1、ex-02→1.2.2、ex-03→1.2.3、ex-05→1.2.4、ex-04→**1.3.3**，逐条硬比对；**ex-04 出现在 1.2 任何子节即红**（不变量 2 的机检形态，取代原 `calls` 校验）。
   - ④ marks 自洽：`attach` 指向存在的阶段号，status ∈ {live, retired}。
   - ⑤ 非节点子节（1.1.1／1.1.2／1.2.5–1.2.9／1.3.1／1.3.2）须有 `specs` 落点或 1.2 母节点归属，不得游离。
3. **反例试金石**（rules/08 §9–12，判据须可证伪）：S7 扩展后先注入两反例验证机检确实拦——a）把 ex-04 的归属改为 1.2.5 应红；b）把 tr-03 的子节改为 2.4（撞 tr-04）应红。随后还原复跑应绿。evidence 落 `results/s7-probe.json`。
4. **specs/062 头部注记**：spec.md 首行下加一行“注（2026-11-26）：阶段 1＝源侧镜像与交割；1.1／1.2 两半段与九步细分、1.3 三联交割（含 ex-04 放行门）见 specs/063 与 ADR-0089”——正文不动；`sop.md` 增一行“九步即 1.2.1–1.2.9 的对应表见 specs/063 §1.3”（不改动原步骤文字）。
5. **追溯登记**：1.1／1.2（specs/062）、5.1（ADR-0081/0082）、5.4（specs/055–057）、5.6（specs/061）以 accepted／registered 入册，不改各 spec 原文。
6. **ADR-0089**：`rules/adr/0089-阶段轨命名与线级标记登记.md`（背景＝§0–§1 摘要；决策＝五段制＋三级号＋双块＋ex 寄居表＋五条 S7 校验；后果＝跨卡引用可机检、marks 冻结不消解、ex 段无独立阶段号）。
7. **指针登记**：specs/README.md 卡表 063 行（已登记，rev 2 时改描述）；`rules/04-translation-workflow.md`“节点标识与旧名”节末增阶段轨指针；AGENTS.md 按任务必读表与硬约束表各增指针（不复制数字）。
8. **收口**：`check_all` 全绿；提交即推（中文一行信息）；`git log origin/main..main` 为空。

## 4. 验收判据

1. `rules/naming.json` schema 为 `sep-naming/v2`，stages 40 项＋marks 10 项在册，patterns 含三级正则。
2. S7 五条校验生效：注入反例（ex-04 错寄 1.2／tr 子节号撞号）必红，还原后必绿；probe 凭证在 `results/`。
3. 22 节点归属唯一；ex 五节点寄居与 §1.4 表逐条一致；`check_all` 全绿（门禁清单以 `--list-gates` 为准）。
4. marks 来源文件零改写：本卡 diff 触及面仅 `rules/naming.json`、`tools/check_stages.py`、`specs/062…/spec.md`（一行）与 `sop.md`（一行）、`specs/063…/`（本卡）、`specs/README.md`、`rules/adr/0089…`、`rules/04…`、`AGENTS.md`。
5. 跨卡引用可解析：库内既有“阶段 1.1／1.2”引用（specs/053 执行账、specs/062）与 stages 块语义一致；新引用“阶段 1.3”等可按册解析。
6. 提交推送后 `git log origin/main..main` 为空；推送后 CI 为最终裁判。

## 5. 决策记录（用户 2026-11-26 裁定链）

| 决策 | 裁定 |
| ---- | ---- |
| 大段划分 | rev 2 定为**五段制**（源侧／翻译／审校／终审／战役），六段制作废 |
| 22 节点归位 | 全部归入 x.y；ex 五节点寄居 1.2.1–1.2.4 与 1.3.3 |
| 旧标记（B/G/I/T/q/W/O/D/P）处置 | 一律保留原名原义，撤撞名消解与加前缀 |
| 1.4/1.5 归属 | 撤号并入 1.2（1.2.5 资产闭包／1.2.7 补丁三判定） |
| 1.3 归属 | 保留独立站，扩为三联交割（建账→置空→放行） |
| 1.1 内部结构 | 两半段显式编号（1.1.1／1.1.2） |
| 阶段 2 处置 | **消解进 1.2／1.3 成为子节**；编号独立＋`calls` 方案作废 |
| 三级号 | 引入（取代 SOP 步骤号双轨） |
| stages/marks 登记处 | `rules/naming.json`（单一事实源，S7 一次机检） |
| ADR 号 | 0089（0087／0088 已被术语线占用） |
| 追溯登记 | 已完成战役以 registered 状态入册，不改原文 |

## 6. 执行记录

- **rev 1（2026-11-26）**：立卡，六段制；提交 `0938d40e1`。
- **rev 2（2026-11-26）**：用户裁定消解 ex 段，改五段制＋三级号；本文件重写。代码侧未动（naming.json 尚未升 v2），故无迁移成本。

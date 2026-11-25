# 063 — 阶段轨命名与线级标记登记（stages＋marks 双块）

- 编号：specs/063-stage-naming；立项日期：2026-11-26；状态：待执行
- 承办：主会话（[ADR-0034](../../rules/adr/0034-主代理单干.md) 主代理单干）
- 上位：[ADR-0080](../../rules/adr/0080-节点标识三层与状态名统一.md)（节点标识三层）、specs/062-phase12-recheck（阶段 1.1／1.2 先例）、specs/061-standards-realignment-2026（标准对照基线）、`rules/naming.json`（标识类事实单一事实源）、`rules/08-intent-first.md`（知难行易）
- 类型：结构登记＋机检扩展（不翻译、不改历史正文）

## 0. 方向声明（rules/08 §0）

### 0.1 指令链（2026-11-26，用户逐轮裁定）

1. “仿照阶段 1.1/1.2 对其余翻译流程阶段重新进行标准化命名。结合国内国际标准，给出你的建议。”
2. “阶段不够细粒度，22 个多阶段应分别归入某个 x.y”——22 节点逐个归位到子阶段。
3. “旧的 b123 等标记仍然保留。重新拟定”——B0–B3、G1–G5、I1–I6、T0–T3、q1–q6、W/O、D1–D5、P 系列等旧字母数字标记**一律保留原名原义**，撤撞名消解与加前缀改造。
4. “1.3–2.5 不应该属于 1.2 的子节吗？”——1.4（资产闭包审计）、1.5（补丁池体检）撤号并入 1.2（以 SOP 步骤号承载）；1.3 保留独立站（节律与凭证硬差异）。
5. “其实 1.1 也实际包含了两个阶段吧”——1.1 显式分两半段（联网抓取／离线复核，`--offline` 模式与 CI 编排面为证）。
6. “1.2、1.3 和大段 2 的关系是？”——定为大段 2 提供工序、1.2 批量编排工序、1.3 交割给生产线；判据单源、ex-04 唯一、交割无旁路三条不变量。
7. “为何不把阶段 2 变成 1.2.1–5 二级？”——编号不合并（2.4 不在 1.2 作业面、ex 工序生命周期独立、节点 id 是体系键、归谬会消解节点轨），从属关系改用 `calls` 字段表达。

### 0.2 目标

建立**阶段轨**（stages，两级 N.M）与**线级标记层**（marks），与节点轨（ADR-0080 的 22 节点 ex/tr/rv/sg）衔接为两层阶段语言：阶段轨管“站序与战役编址”，节点轨管“工序标识”，marks 管“各专项线既有标记的登记与挂靠”。阶段对照对齐 ISO 17100:2015／GB/T 19363.1-2022 的流程分段与术语定名，使流程对外可声明。

### 0.3 验收判据（概要，详见 §4）

stages 31 项＋marks 10 项入册；S7 扩展五条校验生效且经反例试金石验证；22 节点归属唯一；旧标记来源文件零改写；specs/062 仅加头注一行；ADR-0089 登记；`check_all` 全绿；提交即推。

## 1. 命名体系定案

### 1.1 两层阶段语言

| 层 | 编号形态 | 承载内容 | 事实源 | 写入面 |
| ---- | ---- | ---- | ---- | ---- |
| **节点轨**（ADR-0080 既定，不动） | `ex-01`…`sg-03` | 单词条工序标识：journal、tasks.steps、状态机、PROGRESS 计数 | `rules/naming.json` nodes 块 | 逐件执行 |
| **阶段轨**（本卡新立） | `N.M`（两级，`^[1-9]\.[0-9]{1,2}$`） | 站序位置＋全库战役／维护编址；不进 journal、不进状态机 | `rules/naming.json` stages 块 | spec 卡、执行账、跨卡引用 |
| **线级标记层**（本卡登记，不改现状） | 字母前缀原样（B0–B3、G1–G5…） | 各专项线内部递进阶段与判据号 | `rules/naming.json` marks 块 | 原线内继续流通 |

三层规则：阶段号管“站”，SOP 步骤号管“站内工序”（如 1.2 的九步），marks 管线内记号。**不引入三级号**（1.2.1 式），从属与调用关系用 `nodes`／`calls` 字段表达。

### 1.2 大段划分与映射规则

大段 N 绑定段（承 ADR-0080 号段语义）：**1＝上游镜像与基线维护（无节点绑定）、2＝ex 段、3＝tr 段、4＝rv 段、5＝sg 段、6＝战役与治理（无节点绑定）**。子阶段 M＝段内节点号（2.1↔ex-01 … 5.3↔sg-03）；1.x／6.x 的 M 号归维护与战役。节点预留号段（ex-06–09、tr-06–09、rv-10–19、sg-04–09）对应阶段号自动预留（2.6–2.9、3.6–3.9、4.10–4.19、5.4–5.9）。

### 1.3 阶段总表（stages 块 31 项全列）

**大段 1：上游镜像与基线维护**

| 号 | name | label | nodes/calls | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1.1 | mirror.catalog-recheck | 目录抓取与四方互转 | nodes []；calls []（两半段见 1.4） | 源文本接受（5.3） | accepted（specs/062） |
| 1.2 | mirror.refetch-recheck | HTML 重抓·基线·补丁复核 | nodes []；**calls [2.1, 2.2, 2.3, 2.5]** | 源文本接受（5.3） | accepted（specs/062） |
| 1.3 | mirror.change-settle | 上游同步与建账置空 | nodes []；calls [] | 源文本接受（5.3） | registered（specs/001；重抓场景由 1.2 批量触发，日常漂移独立触发） |
| 1.4+ | —（预留） | — | — | — | reserved |

**大段 2：英语源生产与审计（ex 段）**

| 号 | name | label | nodes | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2.1 | extract.fetch | 抓取与版本钉 | [ex-01] | 前期准备（5.3） | accepted |
| 2.2 | extract.convert | HTML 转 Markdown | [ex-02] | 前期准备（5.3） | accepted |
| 2.3 | extract.fidelity | 转换保真校验 | [ex-03]（挂 I1–I6） | 前期准备（5.3） | accepted |
| 2.4 | extract.source-audit | 源完整性审计 | [ex-04] | **源文本接受性检查**（5.3） | accepted |
| 2.5 | extract.format | 镜像格式闭合 | [ex-05] | 前期准备（5.3） | accepted |
| 2.6–2.9 | —（预留） | — | ex-06–09 | — | reserved |

**大段 3：中文翻译（tr 段）**

| 号 | name | label | nodes | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 3.1 | translate.preprocess | 译前预处理 | [tr-01] | 术语工作（5.3；语义错位已注记） | accepted |
| 3.2 | translate.draft | 初译 | [tr-02] | **笔译**；LLM 件＝**译后编辑**（ISO 18587:2017／GB/T 40036-2021） | accepted |
| 3.3 | translate.accuracy | 准确性校（一校） | [tr-03] | **自检**（checking，GB/T 3.2.5） | accepted |
| 3.4 | translate.fluency | 行文通顺校（二校） | [tr-04] | **自检**（checking） | accepted |
| 3.5 | translate.format | 段内格式闭合 | [tr-05] | — | accepted |
| 3.6–3.9 | —（预留） | — | tr-06–09 | — | reserved |

**大段 4：审阅校对（rv 段）**

| 号 | name | label | nodes | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 4.1 | review.terminology | 术语与勘误锁定 | [rv-01]（挂 D1–D5） | **术语工作** | accepted |
| 4.2 | review.consistency | 全局一致性 | [rv-02] | **双语审校**（revising，GB/T 3.4.5，**强制**） | accepted |
| 4.3 | review.cite | 引文锁定 | [rv-03]（挂 q1、T0–T3） | **单语审校**（review，GB/T 3.4.6） | accepted |
| 4.4 | review.logic | 逻辑一致性 | [rv-04]（挂 q2） | 单语审校 | accepted |
| 4.5 | review.grammar | 语法与病句校 | [rv-05]（挂 q3） | 单语审校 | accepted |
| 4.6 | review.register | 语域 | [rv-06]（挂 q4） | 单语审校 | accepted |
| 4.7 | review.measure | 计量 | [rv-07]（挂 q5） | 单语审校 | accepted |
| 4.8 | review.punctuation | 标点 | [rv-08]（挂 q6） | 单语审校 | accepted |
| 4.9 | review.style | 体例终校 | [rv-09] | **校对**（proofreading，GB/T 3.4.7；CY/T 266 计错） | accepted |
| 4.10–4.19 | —（预留） | — | rv-10–19 | — | reserved |

**大段 5：终审签字与发布（sg 段）**

| 号 | name | label | nodes | 标准对照 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 5.1 | signoff.verity | 受众适切性（初审） | [sg-01] | **最终验证**（final verification） | accepted |
| 5.2 | signoff.coherence | 连贯性（复审） | [sg-02] | 最终验证 | accepted |
| 5.3 | signoff.acceptance | 交付验收（终审） | [sg-03]（`--mandate`；CY/T 266 万分之一线） | 最终验证与**发布**（release） | accepted |
| 5.4–5.9 | —（预留） | — | sg-04–09 | — | reserved |

> 发布（提交即推＋壳仓拉取制，ADR-0059/0064）为大段 5 收尾动作，**不占号**（避免与 sg-04 预留撞号）。

**大段 6：战役与治理**

| 号 | name | label | 落点 | 状态 |
| ---- | ---- | ---- | ---- | ---- |
| 6.1 | campaign.wipe-restart | 全库置空与重译启动 | ADR-0081/0082、specs/062 §6 | registered（已执行） |
| 6.2 | campaign.term-extraction | 术语全库提取 | specs/058 | active（在批） |
| 6.3 | campaign.en-template-audit | EN 模板审计 | specs/044/047/053（挂 B0–B3.2 阶梯） | active（在批） |
| 6.4 | campaign.mulu-recategorize | 目录六区重分类 | specs/055/056/057 | registered（已执行） |
| 6.5 | campaign.rework-backfill | 受控回炉与回补 | specs/028/030/052 | active（在批） |
| 6.6 | campaign.standards-review | 标准对齐复核 | specs/061（挂 061 评估号） | registered（已收口） |

**计数核对**：节点绑定子阶段 5＋5＋9＋3＝22，与节点总数对齐。

### 1.4 1.x 段特殊形态

1. **两半段统一形态**（SOP 步骤号承载，不占阶段号）：
   - 1.1＝抓取半段（SOP ①，联网，CI 不跑）＋复核半段（SOP ②–⑧，`--offline` 可重放，CI 每日三班跑此面）；
   - 1.2＝重抓半段（SOP ①–④：快照、重抓、资产闭包、差集）＋复核半段（SOP ⑤–⑨：补丁三判定、I2、B 族账本刷新、建账出口、报告）。
2. **1.2 站内工序九步**（specs/062 sop.md 现行七步增补两步）：①抓取前快照；②全量重抓（unchanged 不写盘不动钉，ADR-0045）；③**资产闭包审计**（`fetch_audit` 闭包至不动点——原预留 1.4 并入）；④差集分类（`en_delta` new/layout/tokens/text＋`entry_meta_delta`）；⑤补丁复核三判定（必要性／有效性／一致性；`check_en_patches --strict` 三面——原预留 1.5 并入）；⑥I2 转换保真（`check_yuanwen_fidelity --gate`）；⑦B 族账本刷新（page_layout→article_ledger→B3.1→B3.2）；⑧**建账出口**（text 清单→1.3→置空待译）；⑨进度报告。
3. **1.3 独立站**：日常漂移建账（CI 三班检出→`compare`→建账→置空）节律与凭证独立（specs/062 SOP“与既有线的分工”明文建账走 specs/001）；1.2 重抓场景的批量建账出口走同一 1.3。
4. **calls 字段**：1.2 的 stages 登记含 `calls: ["2.1", "2.2", "2.3", "2.5"]`，显式声明编排关系；**2.4 不得出现在任何战役的 calls 里**（审计不进批量，S7 机检硬拦）。1.2 自有工序（差集、补丁三判定、B 族账本、建账出口）归 SOP 步骤号，不入 calls。

### 1.5 三条关系不变量（1.2／1.3／大段 2）

1. **判据单源**：1.2 不是第二套判据，是同一组不变量（I1–I6、补丁准入、差集口径）的批量调用；批量路径绕过钉账纪律即事故（specs/062 `upsert_baseline` 无 `files` 拒收护栏为既有防线）。
2. **ex-04 唯一性**：审计只发生在生产链逐件过站（2.4，任务状态机强制集）；1.2／1.3 一律不做审计放行。
3. **交割无旁路**：源侧世界（1.x）进入翻译世界（2.4 之后）只经 1.3 建账置空这一个界面。

### 1.6 线级标记层（marks 块 10 项，原名全保留）

| prefix | range | line | attach | source | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| B | B0–B3.2（B3.1 装配／B3.2 判断） | en-template-audit | 6.3 主挂；1.2 步骤⑦刷新 | specs/044-b0b1-baseline、specs/047-structural-reverse-check、specs/053-en-template-audit | live |
| G | G1–G5 | catalog-network | 1.1 通过判据（五门入 CI） | specs/054-catalog-network-replay | live |
| I | I1–I6 | conversion-fidelity | 2.3 判据面 | ADR-0063 | live |
| T | T0–T3 | six-axis-rollback | 4.3 升档时相 | specs/060-six-axis-quality-gates | live |
| q | q1–q6 | six-axis-checklist | 4.3–4.8 轴标签与清单文件名 | specs/060；ADR-0080 既裁沿用 | live |
| D | D1–D5 | term-diff-classification | 4.1 定性判据 | rules/03-terminology.md | live |
| W/O | spec 内未决项 | per-spec | —（spec 内引用，跨卡须带 spec 号） | 各 spec | live |
| P | P1–P33 | axioms | 全流程引用 | rules/axioms.json | live |
| P | P1–P4 | legacy-node-name | — | ADR-0080 收编为 aliases | retired |
| G/D/P（061 号域） | 061-G1–G16、061-D1–D5、061-P0–P2 | standards-realignment | 6.6 历史凭证 | specs/061 | retired |

> marks 层**只登记不改写**：不重命名、不加前缀、不消解撞名（用户 2026-11-26 裁定）；跨线引用须带线名或 spec 号。ADR 与 spec 原文一字不动。

### 1.7 标准对照锚点（2026-11-26 联网核验）

- ISO 17100:2015＋Amd 1:2017（现行，修订 AWI 约至 2029）：§5.3 前期准备（源文本接受性、术语工作）、§5.4 翻译过程（笔译→自检→双语审校〔强制〕→单语审校〔可选〕→校对〔可选〕→最终验证与发布）。条款结构以 specs/061 `version-audit.md` 为准。
- GB/T 19363.1-2022（等同采用 ISO 17100，现行）：**自检＝checking（3.2.5）、双语审校＝revising（3.4.5）、单语审校＝reviewing（3.4.6）、校对＝proofreading（3.4.7）**。
- 译后编辑：ISO 18587:2017／GB/T 40036-2021（ADR-0084 D2 已承接）。
- 评审质量：ISO 5060:2024（Verity／Annex E／评分卡）；计错：CY/T 266-2023。
- 命名与标识：ISO/IEC 11179-5:2015／GB/T 18391.5-2009（标识与名称分离、唯一、稳定、不复用）——阶段号 identifier 沿用同一哲学。
- 本项目 review／proofreading 做成强制工序是**超出基线**而非偏离（ISO 17100 中为可选），无需登记偏离项。

## 2. 非目标

1. 不改 22 节点 id／name／label（ADR-0080 既定），不动状态机、journal、tasks。
2. 不改写任何历史文档正文（specs/044/047/053/055–058/060/061、rules/03、ADR 全部原文不动）；specs/062 仅加头部注记一行。
3. 不实施 marks 的撞名前缀改造（用户裁定保留）；不改 q1–q6 清单文件名、B3.1/B3.2 工具名等任何现行用法。
4. 不引入三级阶段号；不改 1.1／1.2 已定名称与语义（用户 2026-11-25 裁定）。
5. 本卡不产出任何译文，不动 en/／yuanwen/／SUMMARY。

## 3. 实施步骤

1. **naming.json 升 v2**：schema 升 `sep-naming/v2`；增 `stages`（31 项，按 §1.3 全量登记）与 `marks`（10 项，按 §1.6）双块；`patterns` 增 stage identifier／name 正则；`revision` 补记。stage 的 name 域：mirror（1.x）／extract（2.x）／translate（3.x）／review（4.x）／signoff（5.x）／campaign（6.x）——有节点对应者 name 逐字复用节点 name。
2. **S7 扩展**（`tools/check_stages.py`）五条：①stages 自洽（identifier 唯一、正则、specs 落点存在）；②nodes 归属唯一（每个 pipeline 节点恰出现于一个 stages.nodes；nodes 非空者与段绑定规则一致）；③calls 指向存在的节点子阶段，且 **2.4 不得出现在任何 calls**；④marks 自洽（attach 指向存在的阶段号，status ∈ {live, retired}）；⑤非节点子阶段（nodes [] 且无 calls 者）须有 specs 落点。
3. **反例试金石**（rules/08 §9–12，判据可证伪）：S7 扩展后先注入两反例验证机检确实拦——a）把 2.4 加入某战役 calls 应红；b）删除某节点的归属应红；随后还原复跑应绿。evidence 落 `results/s7-probe.json`。
4. **specs/062 头部注记**：spec.md 首行下加一行“注（2026-11-26）：阶段 1＝上游镜像与基线维护；1.1/1.2 两半段与 calls 登记、1.3 独立站，见 specs/063 与 ADR-0089”——正文不动。
5. **追溯登记**：1.1／1.2（specs/062）、6.1（ADR-0081/0082）、6.4（specs/055–057）、6.6（specs/061）初版即以 accepted／registered 入册（stages 块 status 列），不改各 spec 原文。
6. **ADR-0089**：`rules/adr/0089-阶段轨命名与线级标记登记.md`（背景＝本卡 §0–§1 摘要、决策＝两层阶段语言＋双块＋五条 S7 校验、后果＝跨卡引用可机检／marks 冻结不消解）。
7. **指针登记**：specs/README.md 卡表加 063 行；`rules/04-translation-workflow.md`“节点标识与旧名”节末增一句阶段轨指针；AGENTS.md 按任务必读表“改目录、标题、结构”行与硬约束表各增指针（不复制数字）。
8. **收口**：`check_all` 全绿；提交即推（中文一行信息）；`git log origin/main..main` 为空。

## 4. 验收判据

1. `rules/naming.json` schema 为 `sep-naming/v2`，stages 31 项＋marks 10 项在册，patterns 含 stage 正则。
2. S7 扩展生效：注入反例（calls 含 2.4／nodes 归属破坏）必红，还原后必绿；probe 凭证在 `results/`。
3. 22 节点归属唯一且与段绑定一致；`check_all` 全绿（门禁清单以 `--list-gates` 为准）。
4. marks 来源文件零改写：本卡 diff 触及面仅 `rules/naming.json`、`tools/check_stages.py`、`specs/062…/spec.md`（一行）、`specs/063…/`（新卡）、`specs/README.md`、`rules/adr/0089…`、`rules/04…`、`AGENTS.md`。
5. 跨卡引用可解析：库内既有“阶段 1.1／1.2”引用（specs/053 执行账、specs/062、CI 讨论记录）与 stages 块语义一致。
6. 提交推送后 `git log origin/main..main` 为空；推送后 CI 为最终裁判。

## 5. 决策记录（用户 2026-11-26 裁定链）

| 决策 | 裁定 |
| ---- | ---- |
| 大段六段制＋22 节点归位 x.y | 采纳（细化至节点级） |
| 旧标记（B/G/I/T/q/W/O/D/P）处置 | 一律保留原名原义，撤撞名消解与加前缀 |
| 1.4/1.5 归属 | 撤号并入 1.2（SOP 步骤号承载） |
| 1.3 归属 | 保留独立站（节律凭证硬差异） |
| 1.1 内部结构 | 两半段显式登记（抓取／复核） |
| 2.x 与 1.2 的编址关系 | 编号独立；从属以 calls 字段表达；2.4 禁入 calls |
| stages/marks 登记处 | `rules/naming.json`（单一事实源，S7 一次机检） |
| 追溯登记 | 已完成战役以 registered 状态入册，不改原文 |

## 6. 执行记录

（待填：按 §3 步骤逐项登记，evidence 落 `results/`。）

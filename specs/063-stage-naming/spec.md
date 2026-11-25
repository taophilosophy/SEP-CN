# 063 — 阶段轨命名与线级标记登记（rev 3：四段纯流程＋独立战役块）

- 编号：specs/063-stage-naming；立项日期：2026-11-26；状态：待执行（rev 3）
- 承办：主会话（[ADR-0034](../../rules/adr/0034-主代理单干.md) 主代理单干）
- 上位：[ADR-0080](../../rules/adr/0080-节点标识三层与状态名统一.md)（节点标识三层）、specs/062-phase12-recheck（阶段 1.1／1.2 先例）、specs/061-standards-realignment-2026（标准对照基线，每节必有适用标准或不适用结论）、`rules/naming.json`（标识类事实单一事实源）、`rules/pipeline.json`（判据、次序、对象域）、`rules/08-intent-first.md`（知难行易）
- 类型：结构登记＋机检扩展＋派生视图（不翻译、不改历史正文）
- 版本史：rev 1 六段制（`0938d40e1`）→ rev 2 五段制、ex 段消解（`1cad6ed4a`）→ **rev 3 四段制＋战役独立＋12 项重审修正**

## 0. 方向声明（rules/08 §0）

### 0.1 指令链（2026-11-26）

1. 仿照阶段 1.1/1.2 对其余翻译流程阶段重新标准化命名，结合国内国际标准给出建议。
2. 阶段不够细粒度，22 节点应分别归入某个 x.y。
3. 旧的 B0–B3 等标记一律保留原名原义（撤撞名消解与加前缀改造）。
4. 1.4／1.5 撤号并入 1.2；1.3 保留独立站。
5. 1.1 显式分两半段（抓取／复核）。
6. 1.2／1.3／大段 2 的关系＝批量编排／交割界面／工序层；三条不变量。
7. 编号不合并（曾拟 `calls` 字段表达从属）。
8. 阶段 2 消解进 1.2／1.3 成为子节；三级号引入，`calls` 作废。
9. **重新审视任务书，按不计成本给最佳建议并修订**——本 rev 3 即审查产出。

### 0.2 重审发现与修正（12 项）

| # | 类型 | 发现 | rev 3 修正 |
| ---- | ---- | ---- | ---- |
| D1 | 硬缺陷 | ex-05 语义错判：实为 markdown 语法层闭合（`type=format`、`gate_owner=false`），补丁由 ex-02 生成并应用 | 1.2.4 撤销；ex-05 归 1.3.4，label 改“镜像格式闭合（markdown 语法层）” |
| D2 | 硬缺陷 | 顺序倒置：pipeline 链 ex-04→ex-05，rev 2 却把 ex-05 排在 ex-04 之前 | ex-05 随 ex-04 入 1.3，顺序 1.3.3→1.3.4 |
| D3 | 硬缺陷 | “1.2 九步＝SOP 九步”不成立（SOP ①无号、⑧移 1.3.1、ex-02／ex-05 不在九步内） | 1.2 定为 8 子节；另立 §1.6 显式映射表，删除“一一对应／非新增工序”表述 |
| D4 | 设计 | 标准对照列“—”既非适用也非不适用结论，违反 specs/061 §10 | 逐节填满：工程层写 12207:2026／29148，无对应者写“不适用（理由）”；§1.9 全量对照 |
| D5 | 设计 | 战役混入流程段，语义正交被压平 | **战役独立成 campaigns 块（C1–C6）**，stages 只含 1–4 四段纯流程 |
| D6 | 设计 | 阶段不可消费（无派生视图、无写入禁令） | 增 `tools/stage_of.py`（只读派生）＋“阶段号永不写入”原则＋S7 禁写校验 |
| D7 | 设计 | 无 state→stage 映射 | 增 `state_stage_map`（§1.7），15 状态逐条映射 |
| D8 | 一致性 | 预留号未入册 | 26 项 `status: reserved` 入册；总册 60 项 |
| D9 | 一致性 | S7 五条不全 | 扩为八条（§3 第 2 项） |
| D10 | 一致性 | ex-05 无状态位，“格式闭合完成”无载体 | stage_of 采“最近前驱状态”规则；状态机增设登记为后续项（不在本卡） |
| D11 | 一致性 | 1.3 父 registered、子 accepted，无父子规则 | 父子 status 独立登记，规则入 §1.1 |
| D12 | 表述 | 子节号多轮漂移 | §1.3 总表为唯一事实源，他处只引号不重复列名 |

### 0.3 目标

建立**阶段轨**（stages，四段纯流程，三级 `N.M[.K]`）、**战役块**（campaigns，C1–C6）与**线级标记层**（marks），与节点轨（ADR-0080 的 22 节点）构成四层标识：节点管工序、阶段管位置、战役管全库元活动、marks 管专项线记号。阶段划分与术语对齐 ISO 17100:2015／GB/T 19363.1-2022。

**核心设计命题**：阶段号是**派生视图**，不是事实——事实只有 `tasks.state`；阶段由 state 映射而得，永不写入 tasks／steps／journal。这条命题使阶段轨与 ADR-0080 关于“状态不可由 journal 严格重放”的经验相容，同时保证任何时刻“词条在哪一站”只有一个答案。

### 0.4 验收判据（概要，详见 §4）

stages 60 项＋campaigns 9 项＋marks 10 项入册；S7 八条校验生效且经三个反例试金石验证；`stage_of.py` 可对全部 1873 件输出阶段；22 节点归属唯一；旧标记来源文件零改写；specs/062 加头注；ADR-0089 登记；`check_all` 全绿；提交即推。

## 1. 命名体系定案

### 1.1 四层标识与三条规则

| 层 | 编号形态 | 承载内容 | 事实源 | 写入面 | 写入禁令 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| **节点轨**（ADR-0080 既定） | `ex-01`…`sg-03` | 工序标识 | `rules/naming.json` nodes | journal、tasks.steps、状态机 | — |
| **阶段轨**（本卡新立） | `N.M`／`N.M.K`（正则 `^[1-9]\.[0-9]{1,2}(\.[0-9]{1,2})?$`） | 生产线位置 | `rules/naming.json` stages | spec 卡头、执行账、跨卡引用 | **禁入 tasks／steps／journal**（D6） |
| **战役块**（本卡新立） | `C1`…`C6`（正则 `^C[1-9]$`） | 全库元活动 | `rules/naming.json` campaigns | spec 卡头、执行账 | 同上 |
| **线级标记层**（登记不改写） | 字母前缀原样 | 专项线内递进阶段与判据号 | `rules/naming.json` marks | 原线内继续流通 | — |

**规则一（派生性）**：阶段号永不写入机读载体，由 `state_stage_map` 派生；`stage_of.py` 是唯一读取入口。
**规则二（正交性）**：战役与阶段正交——一场战役可跨多个阶段，一个阶段可受多场战役影响；故不同编号空间、不互相嵌套。
**规则三（status 语义）**：`accepted`（已认可且常态执行）／`registered`（已登记落点、未常态执行）／`active`（当前在批）／`reserved`（号位预留未分配）／`retired`（退役，号不回收）。父子 status 独立登记，不要求一致（D11）：1.3 整体 `registered` 而其子节 1.3.3 因已入状态机强制集而为 `accepted`。

### 1.2 四段划分与映射规则

| 大段 | 名称 | 与 seg 关系 | ISO 17100 对应 | 子节编号规则 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | 源侧镜像与交割 | seg1＋维护 | §5.3 前期准备 | 批量作业面节点子节＝节点号（1.2.1↔ex-01）；交割面节点接在交割三步之后（1.3.3 起） |
| 2 | 中文翻译 | seg2 | §5.4 笔译＋自检 | M＝段内节点号（2.1↔tr-01 … 2.5↔tr-05） |
| 3 | 审阅校对 | seg3 前段 | §5.4 双语审校／单语审校／校对 | M＝段内节点号（3.1↔rv-01 … 3.9↔rv-09） |
| 4 | 终审签字与发布 | seg3 末段 | §5.4 最终验证与发布 | M＝段内节点号（4.1↔sg-01 … 4.3↔sg-03） |

预留：1.4–1.9（6）、2.6–2.9（4，tr-06–09）、3.10–3.19（10，rv-10–19）、4.4–4.9（6，sg-04–09），共 26 项以 `reserved` 入册。

### 1.3 阶段总表（stages 60 项，唯一事实源）

#### 大段 1：源侧镜像与交割

| 号 | name | label | 节点 | 标准对照 | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1.1 | mirror.catalog-recheck | 目录抓取与四方互转 | — | 源文本接受（ISO 17100 §5.3） | accepted |
| 1.1.1 | mirror.catalog-fetch | 抓取半段：落钉存快照、重建 catalog 账、四差集 | — | ISO 8601-1／GB/T 7408.1（时间戳钉）、ISO 15489-1（记录） | accepted |
| 1.1.2 | mirror.catalog-replay | 复核半段：G1–G5、四方差集、mulu 六项、官方快照（`--offline` 可重放；CI 每日三班跑此面） | — | ISO/IEC/IEEE 12207:2026（配置核验）、ISO 15489-1 | accepted |
| 1.2 | mirror.refetch-recheck | HTML 重抓·基线·补丁复核（批量作业面） | — | 源文本接受（§5.3） | accepted |
| 1.2.1 | extract.fetch | 抓取与版本钉（前置：抓取前 `entries-before` 快照） | **ex-01** | ISO 11669:2024（项目规格）、ISO 8601-1、ISO 15489-1 | accepted |
| 1.2.2 | extract.convert | HTML 转 Markdown（含格式差异补丁的生成与转换层应用） | **ex-02** | ISO/IEC/IEEE 12207:2026、ISO/IEC/IEEE 29148:2018 | accepted |
| 1.2.3 | extract.fidelity | 转换保真校验（挂 I1–I6） | **ex-03** | ISO 15489-1（完整性）、ADR-0062 | accepted |
| 1.2.4 | mirror.asset-closure | 资产闭包审计（`fetch_audit` 迭代至不动点） | — | 不适用（引用闭包属工程层判据，ISO 无对应条款） | accepted |
| 1.2.5 | mirror.delta-classify | 差集分类（`en_delta` new/layout/tokens/text ＋`entry_meta_delta`） | — | 不适用（工程层；变更记录可参照 ISO 15489-1） | accepted |
| 1.2.6 | mirror.patch-recheck | 补丁复核三判定（必要性／有效性／一致性） | — | ISO/IEC/IEEE 12207:2026（配置审计） | accepted |
| 1.2.7 | mirror.b-ledger-refresh | B 族账本刷新（挂 B0–B3.2） | — | 不适用（内部产物，无外部标准对象） | accepted |
| 1.2.8 | mirror.progress-report | 进度报告（覆盖／I2／B3.1／B3.2／池面） | — | ISO 15489-1（报告留存） | accepted |
| 1.3 | mirror.change-settle | 上游同步与建账交割 | — | 源文本接受（§5.3）；ISO 11669（风险评估） | registered |
| 1.3.1 | mirror.change-intake | 变更识别与建账（`compare` → create／reopen --clear／--upstream-sync） | — | ISO 15489-1、ISO/IEC/IEEE 12207:2026（配置标识） | registered |
| 1.3.2 | mirror.wipe | 置空（`clear`，仅留 H1；基线 gate 照常） | — | ISO 15489-1（记录保留；ADR-0082 偏离已登记） | registered |
| 1.3.3 | extract.source-audit | **源审计放行**（en_integrity＋en_source_audit；零信任出口） | **ex-04** | **ISO 17100 §5.3 源文本接受性检查**、ISO 5060:2024 §5.3、ISO 11669（风险评估） | accepted |
| 1.3.4 | extract.format | 镜像格式闭合（markdown 语法层：标题不跳级、表格对齐行、代码块闭合、定界符配对、实体转义、行尾空白、末换行） | **ex-05** | CY/T 154-2017（混排）、GB/T 15834-2011 | accepted |
| 1.4–1.9 | — | 预留（未来源侧工序，ex-06–09 按用途分配） | — | — | reserved |

#### 大段 2：中文翻译（seg2）

| 号 | name | label | 节点 | 标准对照 | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 2.1 | translate.preprocess | 译前预处理 | tr-01 | ISO 11669:2024、ISO 704:2022／1087:2019（术语摘录） | accepted |
| 2.2 | translate.draft | 初译 | tr-02 | **ISO 17100／GB/T 19363.1 笔译**、GB/T 19682-2005、CY/T 123-2015；LLM 件另按 ISO 18587:2017／GB/T 40036-2021（译后编辑） | accepted |
| 2.3 | translate.accuracy | 准确性校（一校） | tr-03 | ISO 17100（复核）、ISO 5060:2024（错误类型）、CY/T 266-2023 | accepted |
| 2.4 | translate.fluency | 行文通顺校（二校） | tr-04 | ISO 5060:2024（Fluency／Style）、GB/T 15834／15835、CY/T 118／154 | accepted |
| 2.5 | translate.format | 段内格式闭合 | tr-05 | GB/T 15834、GB/T 15835、CY/T 154、GB/T 7714-2025 | accepted |
| 2.6–2.9 | — | 预留（tr-06–09） | — | — | reserved |

#### 大段 3：审阅校对（seg3 前段）

| 号 | name | label | 节点 | 标准对照 | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 3.1 | review.terminology | 术语与勘误锁定（挂 D1–D5） | rv-01 | ISO 704:2022／1087:2019／860:2007／10241-1:2011／30042:2019、GB/T 44227-2024、GB/T 10112、CY/T 119／123 | accepted |
| 3.2 | review.consistency | 全局一致性（**双语审校**，强制） | rv-02 | ISO 5060:2024 Annex E、ISO 17100（revising） | accepted |
| 3.3 | review.cite | 引文锁定（挂 q1、T0–T3） | rv-03 | ISO 690、GB/T 7714-2025、ISO 24229:2022（转写代码）、CY/T 122／121／123 | accepted |
| 3.4 | review.logic | 逻辑一致性（q2） | rv-04 | ISO 24617-8／-11／-12、ISO 704（概念关系） | accepted |
| 3.5 | review.grammar | 语法与病句校（q3） | rv-05 | GB/T 15834、通用规范汉字表、ISO 5060（Linguistic conventions）、CY/T 118 | accepted |
| 3.6 | review.register | 语域（q4） | rv-06 | ISO 5060（Style）、ISO 11669:2024（受众）、CY/T 123 | accepted |
| 3.7 | review.measure | 计量（q5） | rv-07 | ISO 80000-1:2022、SI Brochure 第 9 版（4.01）、GB 3100／3101／3102、GB/T 8170／15835、CY/T 170 | accepted |
| 3.8 | review.punctuation | 标点（q6） | rv-08 | GB/T 15834-2011、CY/T 154／123／122 | accepted |
| 3.9 | review.style | 体例终校（**校对**） | rv-09 | CY/T 266-2023、GB/T 7714-2025、CY/T 118／120／170／171、GB/T 22466、ISO 999、GB/T 1.1-2020 | accepted |
| 3.10–3.19 | — | 预留（rv-10–19） | — | — | reserved |

#### 大段 4：终审签字与发布（seg3 末）

| 号 | name | label | 节点 | 标准对照 | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 4.1 | signoff.verity | 受众适切性（初审） | sg-01 | ISO 5060:2024（Verity）、ISO 11669:2024（受众与用途） | accepted |
| 4.2 | signoff.coherence | 连贯性（复审） | sg-02 | ISO 5060:2024 Annex E | accepted |
| 4.3 | signoff.acceptance | 交付验收（终审；`--mandate`；CY/T 266 万分之一线） | sg-03 | ISO 5060:2024 §6.4／6.5、GB/T 19682-2005、CY/T 266-2023、ISO 17100 符合性、图书质量保障体系第八条 | accepted |
| 4.4–4.9 | — | 预留（sg-04–09） | — | — | reserved |

> **发布动作**（提交即推＋壳仓拉取制，ADR-0059/0064）登记为 4.3 的 `closing_action` 字段，不占号（避免挤占 sg 预留）。**节点绑定子节计数**：1.2.1／1.2.2／1.2.3／1.3.3／1.3.4（5）＋2.1–2.5（5）＋3.1–3.9（9）＋4.1–4.3（3）＝**22**，与节点总数对齐。

> **D10 观察项**：ex-05 无状态位（state null），1.3.4 无法由 state 派生；`stage_of` 采“最近前驱状态”规则（见 §1.7 注）。为 ex-05 增设状态位属状态机变更，另卡处理。

### 1.4 战役块（campaigns 9 项）

| 号 | name | label | 落点 | 标准对照 | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| C1 | campaign.wipe-restart | 全库置空与重译启动 | ADR-0081/0082、specs/062 §6 | 不适用（组织级活动；记录保留偏离见 ADR-0082／ISO 15489-1 D4 登记） | registered |
| C2 | campaign.term-extraction | 术语全库提取 | specs/058 | ISO 704／1087／30042、GB/T 44227（术语数据模型） | active |
| C3 | campaign.en-template-audit | EN 模板审计（挂 B0–B3.2 阶梯） | specs/044/047/053 | 不适用（工程层语料装配；配置管理参照 12207:2026） | active |
| C4 | campaign.mulu-recategorize | 目录六区重分类 | specs/055/056/057 | 不适用（内部目录体系，无外部标准对象） | registered |
| C5 | campaign.rework-backfill | 受控回炉与回补 | specs/028/030/052 | ISO 5060（质量复核）、ISO 17100（复核独立性） | active |
| C6 | campaign.standards-review | 标准对齐复核（挂 061 号域） | specs/061 | 自身即标准符合性评估，不另引标准 | registered |
| C7–C9 | — | 预留 | — | — | reserved |

**正交性示例**（写入 ADR-0089 与 naming.json 注释）：C3 影响 1.2.7（B 族账本）与 1.3.4（格式闭合）；C5 影响 3.1–3.9；C2 影响 2.1 与 3.1。战役与阶段是多对多，不得嵌套编号。

### 1.5 ex 节点寄居表（修改后）

| 节点 | 寄居号 | 归属理由 | pipeline 依据 |
| ---- | ---- | ---- | ---- |
| ex-01 抓取与版本钉 | 1.2.1 | 批量作业面首道工序 | `prev=None`，`gate_owner=true` |
| ex-02 HTML 转 Markdown | 1.2.2 | 批量作业面第二道；补丁在此生成并应用 | `prev=ex-01`，`criteria=check_en_patches,divergence` |
| ex-03 转换保真校验 | 1.2.3 | 批量收口的保真复核（I2／I3） | `prev=ex-02`，`criteria=check_yuanwen_fidelity` |
| **ex-04 源完整性审计** | **1.3.3** | **交割放行门**：只在逐件建账后执行，不进批量 | `prev=ex-03`，`criteria=en_integrity,en_source_audit` |
| **ex-05 镜像格式闭合** | **1.3.4** | **放行后的格式闸**：markdown 语法层 | `prev=ex-04`，`type=format`，`gate_owner=false` |

D1／D2 修正要点：ex-05 是**语法格式层检查**而非补丁应用；其 pipeline 前驱是 ex-04，故必须排在 1.3.3 之后。

### 1.6 1.2 与 SOP 的映射（D3 修正）

`specs/062/sop.md` 现行九步与 rev 3 子节的映射如下——**不是一一对应**，两处差异已标明：

| SOP 步 | 内容 | rev 3 归属 |
| ---- | ---- | ---- |
| ① | 抓取前快照 | 并入 1.2.1 前置（不占号） |
| ② | 全量重抓 | 1.2.1（ex-01） |
| ③ | 资产闭包 | 1.2.4 |
| ④ | 差集分类 | 1.2.5 |
| ⑤ | 补丁复核三判定 | 1.2.6 |
| ⑥ | I2 转换保真 | 1.2.3（ex-03） |
| ⑦ | B 族账本刷新 | 1.2.7 |
| ⑧ | 建账出口 | **移出 1.2** → 1.3.1 |
| ⑨ | 进度报告 | 1.2.8 |
| — | HTML 转 Markdown | 1.2.2（ex-02，SOP 未单列，因 phase12 内部执行） |

### 1.7 state → stage 映射（D7）

| tasks.state | 阶段号 | 阶段名 |
| ---- | ---- | ---- |
| pending | null | 未进入源侧作业 |
| cleared | 1.3.2 | 置空完成 |
| ex-04_checked | 1.3.3 | 源审计放行完成 |
| tr-02_checked | 2.2 | 初译完成 |
| tr-03_checked | 2.3 | 一校完成 |
| tr-04_checked | 2.4 | 二校完成 |
| rv-01_checked | 3.1 | 术语与勘误锁定完成 |
| rv-02_checked | 3.2 | 全局一致性完成 |
| rv-03_checked | 3.3 | 引文锁定完成 |
| rv-04_checked | 3.4 | 逻辑一致性完成 |
| rv-05_checked | 3.5 | 语法校完成 |
| rv-06_checked | 3.6 | 语域完成 |
| rv-07_checked | 3.7 | 计量完成 |
| rv-08_checked | 3.8 | 标点完成 |
| rv-09_checked | 3.9 | 体例终校完成 |
| sg-01_checked | 4.1 | 初审完成 |
| sg-02_checked | 4.2 | 复审完成 |
| sg-03_checked | 4.3 | 终审完成 |
| done | 4.3＋发布 | 交付完成 |

**注（D10）**：无状态位节点（ex-01／ex-02／ex-03／ex-05／tr-01／tr-05）的完成不上报状态；`stage_of` 以其**最近前驱有状态节点的阶段号**表示当前所在站，并输出 `derived_from` 字段说明派生依据，不伪造状态。

### 1.8 线级标记层（marks 10 项，原名全保留）

| prefix | range | line | attach | source | status |
| ---- | ---- | ---- | ---- | ---- | ---- |
| B | B0–B3.2（B3.1 装配／B3.2 判断） | en-template-audit | C3 主挂；1.2.7 刷新 | specs/044-b0b1-baseline、specs/047-structural-reverse-check、specs/053-en-template-audit | live |
| G | G1–G5 | catalog-network | 1.1.2 | specs/054-catalog-network-replay | live |
| I | I1–I6 | conversion-fidelity | 1.2.3 | ADR-0063 | live |
| T | T0–T3 | six-axis-rollback | 3.3–3.8（主挂 3.3） | specs/060-six-axis-quality-gates | live |
| q | q1–q6 | six-axis-checklist | 3.3–3.8（逐轴对应） | specs/060；ADR-0080 既裁沿用 | live |
| D | D1–D5 | term-diff-classification | 3.1 | rules/03-terminology.md | live |
| W/O | spec 内未决项 | per-spec | —（跨卡须带 spec 号） | 各 spec | live |
| P | P1–P33 | axioms | 全流程引用 | rules/axioms.json | live |
| P | P1–P4 | legacy-node-name | — | ADR-0080 收编为 aliases | retired |
| G/D/P（061 号域） | 061-G1–G16／061-D1–D5／061-P0–P2 | standards-realignment | C6 历史凭证 | specs/061 | retired |

> marks 只登记不改写：不重命名、不加前缀、不消解撞名（用户 2026-11-26 裁定）。跨线引用须带线名或 spec 号。ADR 与 spec 原文一字不动。

### 1.9 标准对照锚点

- ISO 17100:2015＋Amd 1:2017（现行；AWI 修订约至 2029）§5.3 前期准备（源文本接受性、术语工作）、§5.4 翻译过程（笔译→自检→双语审校〔强制〕→单语审校〔可选〕→校对〔可选〕→最终验证与发布）。
- GB/T 19363.1-2022（等同采用 ISO 17100，现行）：自检＝checking（3.2.5）、双语审校＝revising（3.4.5）、单语审校＝reviewing（3.4.6）、校对＝proofreading（3.4.7）。
- 译后编辑：ISO 18587:2017／GB/T 40036-2021（ADR-0084 D2）。评审质量：ISO 5060:2024。计错：CY/T 266-2023。
- 工程层：ISO/IEC/IEEE 12207:2026（2017 已废止，ADR-0083）、ISO/IEC/IEEE 29148:2018。
- 标识：ISO/IEC 11179-5:2015／GB/T 18391.5-2009（标识与名称分离、唯一、稳定、不复用）。
- 本项目把 review／proofreading 做成强制工序是**超出基线**而非偏离（ISO 17100 中为可选），无需登记偏离。
- 每子节的“不适用”结论均附理由（D4），满足 specs/061 §10 第 2 条验收。

## 2. 非目标

1. 不改 22 节点 id／name／label（ADR-0080 既定），不动状态机、journal、tasks。
2. 不改写任何历史文档正文（specs/044/047/053/055–058/060/061、rules/03、ADR 原文不动）；specs/062 仅加头注一行、sop.md 加一行映射指针。
3. 不实施 marks 的撞名前缀改造；不改 q1–q6 清单文件名、B3.1／B3.2 工具名。
4. 不改 1.1／1.2 已定名称与语义；1.2 的子节是本卡新编址，不改 phase12.py 的执行步骤。
5. 本卡不产出译文，不动 en/／yuanwen/／SUMMARY。
6. **不增设 ex-05 状态位**（属状态机变更，另卡；D10 观察项）。不改 `PROGRESS.md` 版式（阶段分布视图登记为后续项）。

## 3. 实施步骤

1. **naming.json 升 v2**：schema `sep-naming/v2`；增 `stages`（60 项）、`campaigns`（9 项）、`marks`（10 项）、`state_stage_map`（§1.7）；`patterns` 增 stage 三级正则与 campaign 正则；`revision` 记 rev 3。
2. **S7 扩展**（`tools/check_stages.py`）八条：
   ① stages 自洽：identifier 唯一、符合正则、`specs` 落点存在、status 枚举内。
   ② 节点↔阶段**双向**一致：每个 pipeline 节点恰出现于一个 stages 子节；每个 `stages[].nodes` 的 id 在 nodes 块存在。
   ③ 大段 2–4 子节号＝节点号（M＝节点号规则）。
   ④ ex 寄居表逐条硬比对：ex-01→1.2.1、ex-02→1.2.2、ex-03→1.2.3、ex-04→1.3.3、ex-05→1.3.4；**ex-04 出现在 1.2 任何子节即红**（不变量 2 的机检形态）。
   ⑤ marks 自洽：`attach` 指向存在的 stages 号或 campaigns 号；status ∈ {live, retired}。
   ⑥ 非节点子节须有 `specs` 落点或母节归属，不得游离。
   ⑦ **预留完整性**：1.4–1.9／2.6–2.9／3.10–3.19／4.4–4.9／C7–C9 以 `reserved` 在册；已用号与 reserved 号不得重叠；retired 号不复用。
   ⑧ **映射完整性**：`state_stage_map` 的键集＝naming.json 中 state 非 null 的节点 state 集；值皆为存在的 stages 号。**另加写入禁令校验**：扫描 `tasks/` 与 `journal/` 不得出现阶段号／战役号模式。
3. **反例试金石**（rules/08 §9–12）：注入三个反例验证机检确拦——a）ex-04 归属改 1.2.4 应红；b）tr-03 子节改 2.4 撞 tr-04 应红；c）tasks 中植入字符串 `1.2.3` 应红。还原复跑应绿。evidence 落 `results/s7-probe.json`。
4. **`tools/stage_of.py`（新增，D6）**：只读派生视图。
   - 单件：`python tools/stage_of.py <slug>` → 输出当前阶段号、name、label、`derived_from`（派生依据状态）、下一站。
   - 全库：`--all` → 阶段分布计数（按 stages 号聚合，供 PROGRESS 后续消费）。
   - 纪律：只读、不写盘、不修改 tasks；无状态节点按 §1.7 注取最近前驱。
5. **specs/062 注记**：spec.md 首行下加一行“注（2026-11-26）：阶段 1＝源侧镜像与交割；1.1 两半段、1.2 八子节、1.3 四步交割（含 ex-04／ex-05 放行门）见 specs/063 与 ADR-0089”；sop.md 加一行“九步与 stages 子节的映射见 specs/063 §1.6”。正文不动。
6. **ADR-0089**：`rules/adr/0089-阶段轨命名与线级标记登记.md`。内容：背景（§0.1–§0.2 摘要）、决策（四层标识、阶段派生原则、四段＋战役正交、ex 寄居表、八条 S7、stage_of 唯一入口）、后果（跨卡引用可机检、marks 冻结、战役与阶段不嵌套、ex-05 无状态位为已知缺口）、回退（naming.json 单文件、git revert 整体可退）。
7. **指针登记**：specs/README.md 063 行（rev 3 描述）；`rules/04-translation-workflow.md`“节点标识与旧名”节末增阶段轨＋战役块＋stage_of 三行指针；AGENTS.md 按任务必读表与硬约束表各增指针（不复制数字）。**该步待并行会话收工后执行**（AGENTS.md／rules/04 当前有他人在途改动）。
8. **后续项登记**（不在本卡实施）：①ex-05 状态位；②PROGRESS 增“阶段分布”节（消费 `stage_of --all`）；③spec 卡头“阶段／战役”字段模板（写入 `specs/README.md` 表列后续演进）。

**收口**：`check_all` 全绿；提交即推；`git log origin/main..main` 为空。

## 4. 验收判据

1. `rules/naming.json` schema `sep-naming/v2`，stages 60／campaigns 9／marks 10／state_stage_map 18 在册。
2. S7 八条生效；三个反例（ex-04 错寄／tr 撞号／tasks 植入阶段号）必红，还原必绿；probe 凭证落盘。
3. `stage_of.py` 对全部 1873 件输出阶段，无异常；`--all` 分布计数与 `tasks.state` 聚合一致（独立复算）。
4. 22 节点归属唯一且与 §1.5 寄居表逐条一致；`check_all` 全绿（清单以 `--list-gates` 为准）。
5. 每个 stages／campaigns 条目有标准对照，或“不适用”附理由（specs/061 §10 第 2 条）。
6. marks 来源文件零改写；本卡 diff 触及面仅 `rules/naming.json`、`tools/check_stages.py`、`tools/stage_of.py`（新）、`specs/062…/spec.md`＋`sop.md`（各一行）、`specs/063…/`、`specs/README.md`、`rules/adr/0089…`、`rules/04…`、`AGENTS.md`。
7. 提交推送后 `git log origin/main..main` 为空；CI 为最终裁判。

## 5. 决策记录

| 决策 | 裁定 |
| ---- | ---- |
| 大段划分 | rev 3：**四段纯流程**（源侧／翻译／审校／终审）＋**战役独立块**；五段制作废 |
| 战役编号空间 | 独立 C1–C6（不与阶段嵌套，正交多对多） |
| 22 节点归位 | 全部归 x.y；ex 寄居 1.2.1／1.2.2／1.2.3／1.3.3／1.3.4 |
| 旧标记处置 | 一律保留原名原义，撤撞名消解与加前缀 |
| 1.4／1.5（旧预留） | 并入 1.2（1.2.4 资产闭包／1.2.6 补丁三判定） |
| 1.3 归属 | 独立站，扩为四步交割（建账→置空→源审计→格式闭合） |
| 1.1 内部结构 | 两半段显式编号 1.1.1／1.1.2 |
| 阶段 2 处置 | 消解进 1.2／1.3；编号独立＋`calls` 作废 |
| 三级号 | 引入 |
| 阶段与状态关系 | **阶段是派生视图，永不写入**（D6） |
| 预留号 | 26＋3 项以 reserved 入册（D8） |
| stages／campaigns／marks 登记处 | `rules/naming.json` 单一事实源 |
| ADR 号 | 0089（0087／0088 已被术语线占用） |
| 追溯登记 | 已完成战役以 registered 入册，不改原文 |
| spec 号 | 063（062 已被阶段 1.1／1.2 占用） |

## 6. 执行记录

- **rev 1（2026-11-26）**：立卡，六段制；提交 `0938d40e1`。
- **rev 2（2026-11-26）**：阶段 2 消解进 1.2／1.3，五段制＋三级号；提交 `1cad6ed4a`。
- **rev 3（2026-11-26）**：不计成本重审，修正 D1–D12；四段制＋战役独立＋stage_of＋S7 八条。代码侧仍未动（naming.json 未升 v2），无迁移成本。

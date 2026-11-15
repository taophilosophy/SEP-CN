# 流程过程标准

本规则用软件工程理论把本仓库全流程（入库、翻译、校审、更新、战役、维护）标准化为可审计的过程体系：过程架构按 ISO/IEC/IEEE 12207（软件生命周期过程）四过程组，信息项按 ISO/IEC/IEEE 15289（生命周期信息项），评审按 IEEE 1028（五类评审），异常与度量按 IEEE 1044 与 ISO/IEC 15939（测量过程），文档质量按 ISO/IEC/IEEE 26514 / GB/T 32424，翻译服务按 ISO 17100 / GB/T 19363.1 与 ISO 18587 / GB/T 40036。规范基线清单与版本钉见 [README](README.md)“规范性引用标准”节（ADR-0041）；适用筛查义务见 [08](08-intent-first.md) §13（ADR-0042）。决策记录：[ADR-0044](adr/0044-流程过程标准化.md)。

条文用词按 GB/T 1.1-2020 助动词分级：**应**＝要求，**宜**＝推荐，**可**＝允许（ADR-0041 决策 8）。

## 1. 过程架构（12207 四过程组映射）

| 过程组（12207） | 本仓库过程 | 权威文件 |
| ---- | ---- | ---- |
| 协议过程组（顾客-供方） | 用户裁定接收与登记（spec Assumptions、ADR）；读者勘误通道（issue→勘误） | [06](06-governance.md) 变更管理 |
| 组织级项目使能 | 治理（rules/ADR/宪法）、定岗与并发纪律、生命周期模型维护（本文件＋[04](04-translation-workflow.md)） | [06](06-governance.md)、[ADR-0028](adr/0028-双机定岗分工与同步积压线.md) |
| 技术管理过程组 | 立卡与规划（specs）、基线钉、度量与风险、批次控制 | [08](08-intent-first.md) §9、specs/NNN |
| 技术过程组 | 入库→翻译→校审→收尾的实现流程（§2 阶段定义）、转换器与门禁维护 | [04](04-translation-workflow.md)、[05](05-ci-and-tools.md)、specs/001 |

## 2. 生命周期阶段定义（技术过程组）

各阶段的目的、活动细则与判例以 [04](04-translation-workflow.md) 为准（单一事实源，本表不复制）；本表补齐其标准化字段——**角色、输入/输出信息项、验证门禁**。角色：R0 治理线、R1 译者/写者、R2 校者（应独立于 R1，ISO 17100/ADR-0020）、R3 评审线、R4 管线会话。

| 阶段 | 角色 | 输入信息项 | 验证门禁 | 输出信息项 |
| ---- | ---- | ---- | ---- | ---- |
| P0 入库 intake | R4 | catalog 漂移报告、baseline 登记 | fetch_audit 闭包、check_summary | baseline、en/、yuanwen/、骨架任务 |
| P0.5 源审计 s0 | R2/R4 | en/ 包、yuanwen/、分歧账与 errata 册 | en_integrity＋en_source_audit 硬错误拦（ADR-0052） | HTML 本体核查记录、镜像轴保真记录、勘误/登记处置 |
| P1 初译 draft | R1 | 英文源、登记册摘录、账本模板 | 守恒校验（残余≠0 禁写回） | 译文、ledger（step1/step2）、任务 steps |
| P2 一校 s1 | R1/R2 | 英文源、账本 step1 | 残留外文碎片 0 | 对照记录（锚点/diff） |
| P3 二校 s2 | R1/R2 | 译文、反欧化条款 | check_prose 告警清零或豁免留痕 | 修改 diff、语体结论 |
| P4 术语校 s2.4 | R1/R2 | 两登记册 | check_terms --docs 硬错误拦 | 登记册对照核验记录（ADR-0043） |
| P5 审计 s2.5 | R2（宜非 R1） | en/、yuanwen/、译文 | check_math_zh 默认档＋独立性机检 | 三向比对记录、密度统计、增项处置 |
| P5.5 形态清账（s3 前置独立步骤） | R2/R4 | 已译集合、en/ 正典形态 | `indep_review.py --scan` 该字头该类残余 0 或全登记豁免（告警级，不进 CI） | scan JSON、裁定表、manifest（ADR-0047） |
| P6 三校 s3 | R1/R2 | 译文、ADR-0041 规范清单 | check_style 0 issue＋markdownlint | 体例处置记录、规范基线筛查结论 |
| P7 三审 r1–r3 | R3 | 前六阶段全部输出 | check_academic --strict、CI、独立性机检 | 自审/复核/验收签字、问题单 |
| P8 收尾 done | R3/R0 | r3 凭证 | CI 全绿 | 归档任务、PROGRESS |
| P9 更新 update | R1–R3 | compare 变更清单 | 变更段同口径门禁 | 变更文件、变更段凭证 |
| P10 战役 | R0 立卡＋R1–R3 执行 | 任务书（specs） | 批次卡钉、试金石、独立复算 | execution-log、manifest |
| P11 登记册维护 | R0/R4 | 查证凭证、候选池 | check_terms 硬门禁、先登记后使用 | 登记册行（原文/译法/首现/依据/裁定日期） |

**角色约束**：R2 校者应独立于 R1（资质相当，ISO 17100 §5.5.4/ADR-0020）；单会话形态应按 [04](04-translation-workflow.md) 记明冷置或密度统计补偿（task_ops 机检实拦）。P10 战役任务书应含 作废条件、基准钉、试金石、独立复算、归因登记 五要素（ADR-0039）。

## 3. 信息项规范（15289 对齐）

每类信息项应具备**标识、版本/时点、状态、责任者、保留策略**五属性；缺任一属性的信息项不应作为质量门凭证。

| 信息项 | 标识 | 版本/时点 | 状态 | 责任者 | 保留 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 任务 JSON | slug 路径 | created_at＋steps[].at | state | steps[].actor | 永久（append-only） |
| 翻译账本 | slug.ledger.yaml | 段 id＋批次 | in_fill/done | 执行会话 | 永久 |
| 规格 spec | specs/NNN | 文头版本行 | 状态行 | 承办会话 | 永久；销案注记保留原文 |
| 执行记录 | execution-log | 追加行日期 | 进行中/收口 | 承办会话 | 永久 |
| ADR | NNNN-标题 | 日期＋状态 | proposed/accepted/superseded | 治理线 | 永久（只追加） |
| 登记册行 | 五列 | 首现＋裁定日期 | 现行/held/rejected | 裁定会话 | 永久（废弃不删行） |
| 凭证（结果物） | specs/NNN/bin｜results/ 文件名 | 文内 ran_at/at | — | 产出会话 | 永久；临时件归 script/ |

信息项命名与归置应合 [01](01-repository-structure.md) 与 ADR-0023（散件归 script/state/specs bin|results）；生成物不应承载规则（ADR-0015）。

## 4. 评审体系（IEEE 1028 五类映射）

| 1028 评审类 | 本仓库实体 | 证据要求 |
| ---- | ---- | ---- |
| Management Review（管理评审） | 战役/批次立卡评审、任务书签发 | spec 方向声明＋用户裁定登记 |
| Technical Review（技术评审） | r3 终审、ADR 评审 | 验收签字＋CI 全绿 |
| Inspection（审查，检查单驱动） | s2.4/s2.5/s3 机检＋检查单走查 | 检查器输出＋逐条处置 |
| Walkthrough（走查） | r1 自审、脱稿通读 | 语体结论＋自审记录 |
| Audit（审计，独立方） | 023/028 类全库战役、baseline_audit、en_integrity | 台账＋快照对账 0 差异 |

评审发现一律入异常分类（§4.1）；**判定权分离**应维持——机械可判定项交脚本，语义结论由评审人附证据句作出（doctrine 09 §2.3）。

### 4.1 异常分类（IEEE 1044 对齐）

四方对照表钉死于 [specs/004 §五](../specs/004-engineering-doctrine/spec.md)（MQM 维 × A–D 类 × Critical/Major/Minor × R1–R5 成因）；任何会话不应再造新分类体系，跨体系换算以该表为准。配对/方向/数量/引用一致性/悬空的机检由 `tools/check_pairs.py` 承载（告警级，ADR-0046）。返工按 ADR-0039 四元组登记，同一成因二次发案防线升级（约定→门禁→硬门禁）。

## 5. 度量与测量过程（ISO/IEC 15939）

* 测量三要素应成对登记：**指标—数据源—判定阈值**。已运行指标：门禁硬错误数（check_all 10 项）、灭错率候选（校对规程 75%/75%/≤1‱ 模型）、差错率候选（CY/T 266 四档）、密度统计（破折号/“一个”/AI 词）。
* 新指标入 rules/05 登记表并声明：数据源（哪份信息项）、采集命令、阈值来源（标准条款或基线报告）；无阈值来源的指标只报告不判定。
* 量化验收线研究（specs/028 R2）产出基线报告后方可立判定阈值；不以无基线的阈值设门。

## 6. 过程符合性自检

* **批次开工**（P10）：方向声明（含适用规范基线行）｜卡钉基准｜作废条件｜试金石计划。
* **阶段推进**（P1–P8）：本表门禁通过｜evidence 五属性齐（§3）｜actor 记名｜禁跳步。
* **收工**：check_all 10 项全绿｜积压清零（ADR-0028）｜不留半成品｜本次改变了哪个决策/产物/门禁（[08](08-intent-first.md) §4）。
* 自检结论入对应信息项（任务 evidence、execution-log）；缺失视为未立项（[06](06-governance.md) 质量门）。

## 7. 裁剪与反形式主义

* 极简任务（一句话可收口、无信息项产出）可豁免 §6 自检单，但**不应**豁免 evidence 与门禁（00b 极简口径）。
* 本文件与 00/01 doctrine 同受形式主义判定约束：任何条文答不出“它改变了哪个决策/产物/门禁”即删除或降级（doctrine 00 §9）。
* 过程变更走 ADR；本文件修订应同步 rules/README 索引与 [04](04-translation-workflow.md) 指针。

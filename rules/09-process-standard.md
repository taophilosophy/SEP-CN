# 流程过程标准

本规则用软件工程理论把本仓库全流程（入库、翻译、校审、更新、战役、维护）标准化为可审计的过程体系：过程架构按 ISO/IEC/IEEE 12207（软件生命周期过程）四过程组，信息项按 ISO/IEC/IEEE 15289（生命周期信息项），评审按 IEEE 1028（五类评审），异常与度量按 IEEE 1044 与 ISO/IEC 15939（测量过程），文档质量按 ISO/IEC/IEEE 26514 / GB/T 32424，翻译服务按 ISO 17100 / GB/T 19363.1 与 ISO 18587 / GB/T 40036。规范基线清单与版本钉见 [README](README.md)“规范性引用标准”节（ADR-0041）；适用筛查义务见 [08](08-intent-first.md) §13（ADR-0042）。决策记录：[ADR-0044](adr/0044-流程过程标准化.md)。

条文用词按 GB/T 1.1-2020 助动词分级：**应**＝要求，**宜**＝推荐，**可**＝允许（ADR-0041 决策 8）。

## 1. 过程架构（12207 四过程组映射）

| 过程组（12207） | 本仓库过程 | 权威文件 |
| ---- | ---- | ---- |
| 协议过程组（顾客-供方） | 用户裁定接收与登记（spec Assumptions、ADR）；读者勘误通道（issue→勘误） | [06](06-governance.md) 变更管理 |
| 组织级项目使能 | 治理（rules/ADR/宪法）、定岗与并发纪律、生命周期模型维护（本文件＋[04](04-translation-workflow.md)） | [06](06-governance.md)、[ADR-0028](adr/0028-双机定岗分工与同步积压线.md) |
| 技术管理过程组 | 立卡与规划（specs）、基线钉、度量与风险、批次控制 | [08](08-intent-first.md) §9、specs/NNN |
| 技术过程组 | 入库→翻译→校审→收尾的实现流程（§2 阶段定义）、转换器与门禁维护 | [04](04-translation-workflow.md)、[05](05/index.md)、specs/001 |

## 2. 生命周期阶段定义（技术过程组）

各阶段的目的、活动细则与判例以 [04](04-translation-workflow.md) 为准（单一事实源，本表不复制）；本表补齐其标准化字段——**角色、输入/输出信息项、验证门禁**。角色：治理线、译者/写者、校者（应独立于译者，ISO 17100/ADR-0020）、评审线、管线会话。

| 阶段 | 角色 | 输入信息项 | 验证门禁 | 输出信息项 |
| ---- | ---- | ---- | ---- | ---- |
| P0 入库 intake | 管线会话 | catalog 漂移报告、baseline 登记 | fetch_audit 闭包、check_summary | baseline、html/、en/、骨架任务 |
| P0.5 源审计 ex-04 | 校者/管线会话 | html/ 包、en/、分歧账与 errata 册 | en_integrity＋en_source_audit 硬错误拦（ADR-0052） | HTML 本体核查记录、镜像轴保真记录、勘误/登记处置 |
| P1 初译 tr-02 | 译者 | 英文源、登记册摘录、账本模板 | 守恒校验（残余≠0 禁写回） | 译文、ledger（step1/step2）、任务 steps |
| P2 一校 tr-03 | 译者/校者 | 英文源、账本 step1 | 残留外文碎片 0 | 对照记录（锚点/diff） |
| P3 二校 tr-04 | 译者/校者 | 译文、反欧化条款 | check_prose 告警清零或豁免留痕 | 修改 diff、语体结论 |
| P4 术语校 rv-01 | 译者/校者 | 两登记册 | check_terms --docs 硬错误拦 | 登记册对照核验记录（ADR-0043） |
| P5 审计 rv-02 | 校者（宜非译者） | html/、en/、译文 | check_math_zh 默认档＋check_style（O1）＋独立性机检 | 三向比对记录、密度统计、增项处置 |
| P5.5 形态清账（rv-09 前置独立步骤） | 校者/管线会话 | 已译集合、html/ 正典形态 | `indep_review.py --scan` 该字头该类残余 0 或全登记豁免（告警级，不进 CI） | scan JSON、裁定表、manifest（ADR-0047） |
| P6 三校 rv-09 | 译者/校者 | 译文、ADR-0041 规范清单 | check_academic --strict＋check_math_zh --strict＋check_style 0 issue＋markdownlint | 体例处置记录、规范基线筛查结论 |
| P7 三审 sg-01–sg-03 | 评审线 | 前六阶段全部输出 | check_academic --strict、CI、独立性机检、competence 机检、sg-03 须用户指定终审会话（ADR-0054） | 自审/复核/验收签字、问题单 |
| P8 收尾 done | 评审线/治理线 | sg-03 凭证 | CI 全绿 | 归档任务、PROGRESS |
| P9 更新 update | 译者至评审线 | compare 变更清单 | 变更段同口径门禁 | 变更文件、变更段凭证 |
| P10 战役 | 治理线立卡、译者至评审线执行 | 任务书（specs） | 批次卡钉、试金石、独立复算 | execution-log、manifest |
| P11 登记册维护 | 治理线/管线会话 | 查证凭证、候选池 | check_terms 硬门禁、先登记后使用 | 登记册行（原文/译法/首现/依据/裁定日期） |

**角色约束**：审校四环节 actor 两两不同——译者（tr-02）≠双语审校（sg-01）≠复审（sg-02）≠终审（sg-03），依据 ISO 17100 5.3.3／《图书质量保障体系》第八条／[ADR-0093](adr/0093-项目规格扩展与四审分离.md)；前两审不再接受冷置或密度补偿。RACI、能力记录与独立性细则见 §2.1。P10 战役任务书应含 作废条件、基准钉、试金石、独立复算、归因登记 五要素（ADR-0039）。

### 2.1 角色矩阵、能力记录与审校独立性（ADR-0093）

**RACI**（R＝执行，A＝批准／最终负责，C＝咨询，I＝知会；阶段对应 `results/target-workflow.md` §4）：

| 角色 | P0 立项 | P1 源准备 | P2 翻译／PE | P3 独立审校 | P4 语言 QA | P5 编辑出版 | P6 发布归档 | P7 发布后 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 项目经理 PM | A/R | A | A | A | A | A | A | A |
| 译者／译后编辑 | C | C | R | C | C | I | I | I |
| 双语审校（sg-01） | I | I | C | R | C | C | I | I |
| 复审（sg-02） | I | I | I | R | C | I | I | I |
| 终审（sg-03） | I | I | I | A | A | C | A | I |
| 领域审校 | C | C | I | R | C | C | I | I |
| 术语员 | C | R | C | C | C | C | I | I |
| 校对 | I | I | I | I | C | R | I | I |
| 编辑 copyeditor | I | I | I | I | C | R | C | I |
| QA lead | C | C | I | C | R/A | C | C | R |
| AI／数据 steward | C | C | C | I | I | I | C | C |

**能力记录**（ISO 17100 3.1.3–3.1.7）：任务 JSON 的 `competences[actor]` 逐人登记 `qualification`／`experience`／`domain`／`training` 四项，均为必填；`sg-01`／`sg-02`／`sg-03` 推进前由 `task_ops.py` 校验，缺项即拒。登记命令：`python tools/task_ops.py competence <slug> --actor <actor> --qualification ... --experience ... --domain ... --training ...`。

**独立性**：tr-02、sg-01、sg-02、sg-03 的 actor 两两不同；领域审校与校对独立于译者；`sg-01`／`sg-02` 与初译同人的 V01 偏离已撤销（`rules/standards.json` 不再登记），冷置／密度补偿不适用于任何审校环节。

### 2.2 机器／LLM 生产门（T172／ADR-0094）

* 出版件只允许 **full PE**；raw MT／light PE 不得出版。
* 禁止模型生成、补全或“修正”引文与参考文献；引文须回源，q1 引文 hash 锁定。
* 必须逐段对照源文；禁止只读译文润色。
* QE／COMET 只作分流，不作发布门。
* 风险分级见 `rules/risk-matrix.json`：A 人工为主，B full PE，C 仅内部。
* 模型／提示／参数登记见 `baseline/model-registry.json`；模型或提示变更须重跑固定样本与评分卡。
* 校验：`python tools/check_risk_matrix.py`、`python tools/check_model_registry.py`。

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

### 3.1 文档形态与规则作用域

* **形态三分**：单页卡＝仅 `spec.md`（允许 `plan.md` 单存为规划卡）；标准三件＝`spec.md`＋`plan.md`＋`tasks.md`，有 `tasks.md` 必有 `plan.md`；登记／规则类不建 `specs/` 空壳。判据见 [ADR-0092](adr/0092-文档形态三分与规则作用域派生.md)。
* **作用域派生**：规则作用域只从 `rules/pipeline.json` 的 `criteria_owner`／`criteria_carrier` 派生；`rules/0X-*.md` 头部不得手写 `applies_to`。
* **机检**：`python tools/check_doc_shape.py`；正反例 `tools/tests/test_doc_shape.py`。

### 3.2 项目规格字段（`project_spec`，ADR-0093）

建账时写入项目默认值；逐项可覆盖，未知字段或空值拒建账。进 `tr-02` 前 16 字段全部非空，且 `risk_level`／`pe_level` 枚举合法、`pe_level` 与 `translation_mode` 一致。

| 字段 | 类别 | 类型 | 必填 | 默认／说明 |
| ---- | ---- | ---- | ---- | ---- |
| language_pair | 内容 | string | 是 | en → zh-Hans |
| content_type | 内容 | string | 是 | 学术百科词条（SEP） |
| audience | 内容 | string | 是 | 中文哲学读者（研究者与研究生为主） |
| purpose | 内容 | string | 是 | 学术阅读与引用 |
| subject_field | 内容 | string | 是 | 哲学（按词条分支） |
| terminology_basis | 内容 | string | 是 | 两登记册＋term-concepts |
| register | 内容 | string | 是 | 现代汉语学术书面语 |
| workflow | 过程 | string | 是 | retranslate 22 节点 |
| pe_level | 过程 | enum | 是 | full／light／n/a（人工翻译） |
| qa_level | 过程 | string | 是 | CY/T 266＋ISO 5060 |
| pre_edit | 过程 | string | 是 | 源审计后按 tr-01 准备 |
| risk_level | 其他 | enum | 是 | A 高／B 中／C 低／内部 |
| confidentiality | 其他 | string | 是 | 未公开草稿不入模型 |
| delivery | 其他 | string | 是 | GitBook Markdown＋VitePress |
| communication | 其他 | string | 是 | 任务 evidence＋journal |
| qualifications | 其他 | string | 是 | 见 task.competences |

## 4. 评审体系（IEEE 1028 五类映射）

| 1028 评审类 | 本仓库实体 | 证据要求 |
| ---- | ---- | ---- |
| Management Review（管理评审） | 战役/批次立卡评审、任务书签发 | spec 方向声明＋用户裁定登记 |
| Technical Review（技术评审） | sg-03 终审、ADR 评审 | 验收签字＋CI 全绿 |
| Inspection（审查，检查单驱动） | rv-01/rv-02/rv-09 机检＋检查单走查 | 检查器输出＋逐条处置 |
| Walkthrough（走查） | sg-01 自审、脱稿通读 | 语体结论＋自审记录 |
| Audit（审计，独立方） | 023/028 类全库战役、baseline_audit、en_integrity | 台账＋快照对账 0 差异 |

评审发现一律入异常分类（§4.1）；**判定权分离**应维持——机械可判定项交脚本，语义结论由评审人附证据句作出（doctrine 09 §2.3）。

### 4.1 异常分类（IEEE 1044 对齐）

四方对照表钉死于 [specs/004 §五](../specs/004-engineering-doctrine/spec.md)（MQM 维 × A–D 类 × Critical/Major/Minor × 译者–R5 成因）；任何会话不应再造新分类体系，跨体系换算以该表为准。配对/方向/数量/引用一致性/悬空的机检由 `tools/check_pairs.py` 承载（告警级，ADR-0046）。返工按 ADR-0039 四元组登记，同一成因二次发案防线升级（约定→门禁→硬门禁）。

## 5. 度量与测量过程（ISO/IEC 15939）

* 测量三要素应成对登记：**指标—数据源—判定阈值**。已运行指标：门禁硬错误数（check_all，门禁清单以 `--list-gates` 为准）、灭错率候选（校对规程 75%/75%/≤1‱ 模型）、差错率候选（CY/T 266 四档）、密度统计（破折号/“一个”/AI 词）。
* 评分卡与抽样（T173）：`rules/qa-scorecard.json`；计分 `python tools/check_qa_scorecard.py --score <findings>`；抽样 `python tools/qa_sample.py <zh-doc>`；评估者登记 `rules/evaluator-registry.json`。
* 新指标入 rules/05 登记表并声明：数据源（哪份信息项）、采集命令、阈值来源（标准条款或基线报告）；无阈值来源的指标只报告不判定。
* 量化验收线研究（specs/028 校者）产出基线报告后方可立判定阈值；不以无基线的阈值设门。

### 5.1 记录、归档、度量与 AI 治理（T174／ADR-0096）

* **归档包**：`rules/archive-schema.json` 定 spec／source／tbx／model／review／scorecard／editing／release 八类；`results/t174-archive-template.json` 为项目级示例；每件须有 path／sha256／date／owner／status，缺项即红；校验 `python tools/check_governance.py`。
* **留存**：`rules/retention.json` 定八类记录的留存期限、销毁条件、访问级别与责任人；永久留存，销毁只走 ADR；对齐 ISO 15489-1／GB/T 26162。
* **度量**：`rules/metrics-baseline.json` 定 Critical、出版差错率（1/10000）、Major／Minor 密度、返工率、PE 工时、审校一致性、发布后勘误、周期成本八项；`pending_pilot` 时 baseline／threshold 均为 null，先测基线再定阈值。
* **AI 治理**：`rules/ai-governance.json` 定风险登记、影响评估、模型变更回归、供应商与数据条款、事件处理；对齐 ISO/IEC 42001／23894；不设公开 AI 披露。
* **发布后**：`rules/post-publication.json` 定勘误、反馈、上游更新、抽审、版本记录五项；每项有 owner／trigger／evidence。

## 6. 过程符合性自检

* **批次开工**（P10）：方向声明（含适用规范基线行）｜卡钉基准｜作废条件｜试金石计划｜`check_doc_shape`（形态与作用域）。
* **阶段推进**（P1–P8）：本表门禁通过｜evidence 五属性齐（§3）｜actor 记名｜禁跳步。
* **收工**：`check_all.py` 全绿（门禁清单以 `--list-gates` 为准）｜`git log origin/main..main` 为空（提交即推，ADR-0059）｜不留半成品｜本次改变了哪个决策/产物/门禁（[08](08-intent-first.md) §4）。
* 自检结论入对应信息项（任务 evidence、execution-log）；缺失视为未立项（[06](06-governance.md) 质量门）。

## 7. 裁剪与反形式主义

* 极简任务（一句话可收口、无信息项产出）可豁免 §6 自检单，但**不应**豁免 evidence 与门禁（00b 极简口径）。
* 本文件与 00/01 doctrine 同受形式主义判定约束：任何条文答不出“它改变了哪个决策/产物/门禁”即删除或降级（doctrine 00 §9）。
* 过程变更走 ADR；本文件修订应同步 rules/README 索引与 [04](04-translation-workflow.md) 指针。

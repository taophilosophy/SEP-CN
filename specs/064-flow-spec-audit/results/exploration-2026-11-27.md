# 064 独立探索建议书（2026-11-27；全要素广撒网）

- 编号：`specs/064-flow-spec-audit/results/exploration-2026-11-27.md`；状态：**独立建议书，待批**
- 定位：与 064 任务书并列的独立探索产出；**不并入 064 任务书、不占 T 号、不改 105/92/13 计数、不执行任何作业**
- 用户裁定（2026-11-27）：**不研究、不纳入 AI 披露与版权有关问题**；本建议书全文不含这两类内容，已核查的来源中凡涉此两类者一律不计入发现
- 探索方法：6 批共 **24 项联网核查**（ISO 官方页/ISO 状态检索、W3C/NISO/OASIS 官方、国家标准全文公开系统、ACL Anthology/期刊论文、行业报告）；每条发现附来源链接
- 排程草案性质：**全部“待批”**；候选任务不预占 T 号；获批准后另行建账并按 064 检查点规则分配编号

## 0 方向声明（rules/08 §1）

### 0.1 本轮方向卡

| 字段 | 内容 |
| ---- | ---- |
| 目标 | 对 064 任务书及关联 specs（060–063、005、rules/04）做全要素联网探索，形成可独立评审的探索建议书；发现→映射→候选工作包→排程草案 |
| 非目标 | 不研究、不纳入 AI 披露与版权有关问题；不执行翻译/工具改造；不改 064 任务书与计数；不新增 spec 卡；不把候选写成已批准 |
| 验收判据 | 每条发现有来源链接；标准状态区分“现行／在研／草案／已撤销”；候选任务有判据、依赖、优先级；排程草案全部标“待批” |
| 作废条件 | 事实源在复核前变化（如 ISO 18587:2026 正式发布）；必须借实施才能判定；出现与 P1–P33 的上位冲突未处理 |
| 约束 | 不计成本但不牺牲正确性与可追溯；只读探索；不碰他人工作树 |

## 1 探索范围与边界

| 域 | 覆盖内容 | 边界外 |
| ---- | ---- | ---- |
| 翻译服务与 PE | ISO 17100/18587 修订动态、GB/T 三件、ISO 5060/11669 | AI 披露、版权 |
| AI 治理 | 42001/23894/42005/5338/5339/42006/25058/22989 生态 | AI 披露、EU AI Act 透明度义务 |
| 术语与知识组织 | 704/1087/860/10241/30042、26162 系列、16642、24613 系列、25964/SKOS、GB/T 10112/13725、术语抽取研究 | 版权 |
| 质量评估与 QE | MQM 2.0 与 2024 评分模型、COMET/MetricX/BLEURT/CometKiwi、LLM-as-judge、PE 工时/HTER | —— |
| 学术出版与元数据 | Google Scholar citation_*、Crossref DOI、JATS、ISO 999、WCAG 2.2/ISO/IEC 40500/GB/T 37668 | 版权、许可 |
| 交换与工具链/供应链 | XLIFF/TMX/SRX（OASIS/ISO 21720）、SPDX/CycloneDX/SLSA | —— |
| 记录与风险 | ISO 15489/GB/T 26162、ISO 31000、ISO/IEC 27005 | —— |

## 2 探索发现（2026-11-27 联网核查）

### 2.1 翻译服务与译后编辑

| # | 发现 | 来源 | 对 064 的含义 |
| ---- | ---- | ---- | ---- |
| F1 | ISO/DIS 18587:2026（Post-editing of non-human translation output）DIS 投票截止 **2026-11-27**（ISO Update 2026-10）；截至本建议书日**尚未发布**，现行仍为 ISO 18587:2017（full PE 为核心，light PE 资料性）；新版范围扩为 non-human output，并承认更宽 PE 谱系与混合场景（EUATC 2026-10-12 webinar） | [ISO 88184](https://www.iso.org/standard/88184.html)、[ISO Update 2026-10](https://www.iso.org/files/live/sites/isoorg/files/news/magazine/ISOupdate/EN/2026/iso_update_202610_en.pdf)、[EUATC 2026-10-13](https://euatc.org/standards-quality/emerging-iso-standards-for-ai/) | §21.4“出版件 full PE”判据不变；投票截止后任一阶段跃迁（40.60/50.00/60.60）即触发 EP-01 重评 |
| F2 | ISO/AWI 17100 第 2 版处于 20.00 立项早期，行业预计约 2029；现行认证仍按 17100:2015+Amd1 | [ISO 89761](https://www.iso.org/standard/89761.html)、[EUATC](https://euatc.org/standards-quality/iso-17100-18587-04-2026/) | 17100 相关判据继续以 2015 版为锚；新版发布前不得按草案改写 |
| F3 | 新版 17100 方向：纳入 MT/AI 混合流程、风险管理、从“角色”转向“人与能力”框架；长期目标与 18587 合并为统一标准（18587 过渡期独立存在）；18587 新版承认混合场景下“人工翻译/记忆/AI 输出交替”的生产形态 | [ATC 2025-05](https://euatc.org/wp-content/uploads/2026/04/ATC-ISO-Blog-17100-Translation-Services-Review-05-2025.pdf)、[EUATC 2026-04](https://euatc.org/standards-quality/iso-17100-18587-04-2026/) | 064 的角色/独立性设计（§21.3）与“能力”框架兼容；混合场景须仍满足“出版件 full PE＋独立审校”，不得以混合形态降档 |
| F4 | GB/T 19363.1-2022（IDT 17100）、GB/T 40036-2021（IDT 18587:2017）均为现行 | [openstd 19363.1](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=80ABBCA2B9AD293C9C3F39C1C494DB5C)、[openstd 40036](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=A033EC5FE5544C460DEF326C22B5586B) | rules/04 已引用；标准登记回写（T169）继续有效 |

### 2.2 AI 治理

| # | 发现 | 来源 | 对 064 的含义 |
| ---- | ---- | ---- | ---- |
| F5 | ISO/IEC 42005:2025 已发布（AI 系统影响评估指南；规划/部署前/部署后三阶段） | [ISO 42005](https://www.iso.org/standard/42005) | T174 的 AI 风险登记可升级为“风险＋影响评估”双层；42005 是指南非认证标准 |
| F6 | ISO/IEC 5338:2023（AI 生命周期过程）已发布；扩展 12207/15289，含数据管理、模型开发、持续学习；配套 ISO/IEC 5339:2024 应用指南；ISO/IEC CD 25704 过程评估在研 | [ISO 5338](https://www.iso.org/standard/81118.html)、[NIST 交叉表](https://airc.nist.gov/docs/Crosswalk_NIST_AI_RMF_and_ISO_5338_5339.pdf) | 模型/提示登记（CP-S14-17）可按 5338 生命周期视角补“训练/更新/退役”位 |
| F7 | ISO/IEC 42006:2025 已发布（AIMS 审核/认证机构要求），与 42001/42005 构成 AIMS 合规生态 | [IEC 博客](https://www.iec.ch/blog/new-international-standard-sets-rules-auditing-ai-management-systems) | 记录为生态事实；本卡不认证、不承诺认证 |
| F8 | ISO/IEC TS 25058:2024 已发布（AI 系统质量评估指南）；AWI 25058 修订在研，将扩为 AI 质量模型度量 | [ISO 25058](https://www.iso.org/standard/82570.html)、[ISO AWI 25058](https://www.iso.org/standard/91881.html) | §21.4 的 AI 质量度量可引 25058 作“度量来源候选”，仍须经 T174 落地 |
| F9 | 风险与安全基线：ISO 31000:2018（通用风险）＋ISO/IEC 27005:2022（信息安全风险，支撑 27001）均现行 | [ANSI 博客](https://blog.ansi.org/ansi/iso-iec-27005-2022-security-risk-management) | R9–R15 的缓解列可引用 31000/27005 作方法论锚点（保密、供应商条款） |

### 2.3 术语与知识组织

| # | 发现 | 来源 | 对 064 的含义 |
| ---- | ---- | ---- | ---- |
| F10 | ISO 26162:2012 已撤销；现行为 **ISO 26162 系列（2019 起）**：Part 1 设计、Part 2 计算机应用、Part 3 管理、Part 4 术语库质量管理 | 检索汇总（ISO ICS 01.020） | T172 的 TBX 设计应改引 26162 系列，并把 Part 4“库质量管理”作为校验判据来源 |
| F11 | ISO 16642:2017（TMF）现行；ISO 24613:2008（LMF）已撤销，改为多部（24613-1:2019 核心等）；LMF/TMF 统一化（UMF）已有研究 | [ISO 16642](https://www.iso.org/standard/56063.html)、[ISO 24613-1](https://www.iso.org/standard/68516.html) | 概念条目模型以 TBX 为主；TMF/LMF 记为“观察线”，不迁移 |
| F12 | ISO 25964-1:2011/-2:2013 现行；W3C SKOS（2009 Rec）用于 Web 发布；SKOS–25964 对齐存在公认困难；SKOS-XL 交换有 NKOS 文档 | [SKOS](https://www.w3.org/2004/02/skos/)、[NISO](http://www.niso.org/schemas/iso25964)、[NKOS 映射](https://nkos-eu.github.io/2012/presentations/ISO25964-mapping-to-SKOS-XL_TPDL-2012-09-27v6.pdf) | 概念关系若需 Web 发布，SKOS 是出口；25964 是建设规则；二者分工写入术语库设计 |
| F13 | 中文术语国标：GB/T 10112-2019（术语工作 原则与方法）、GB/T 13725-2019（建立术语数据库的一般原则与方法）均现行 | [openstd 10112](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=0A63743C8C1993736445B41545925CFF)、[openstd 13725](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=8E24EBB690EE751AF0CDA643E6B0EAA5) | TBX 设计与迁移样本（CP-S14-13）应同时满足 13725 的库建设原则 |
| F14 | 术语数据质量可引 ISO 8000 系列（ISO/DIS 8000-2 第 6 版在 DIS；主数据系列 8000-100+）；AI 质量度量另有 SQuaRE 25058 | 检索汇总（ISO OBP/ECCMA） | TBX 校验（CP-S14-15）可加“数据质量”维度（完整性/一致性/来源），来源标 8000/25012 |
| F15 | 术语抽取研究活跃：ACM 2026 综述（Recent Advances in Automatic Term Extraction）、Xu 2025 综述、SAGE 2025 工具综述；LLM 辅助双语词表构建兴起；Sketch Engine 等语料法仍有效 | [ACM 2026](https://dl.acm.org/doi/10.1145/3787584)、[SAGE 2025](https://journals.sagepub.com/doi/10.1177/18758967251392652) | specs/058 的 13 路线提取与 T172 候选流程可吸收“抽取→人审→登记”研究结论；LLM 抽取只产候选（禁自审定） |

### 2.4 质量评估与 QE

| # | 发现 | 来源 | 对 064 的含义 |
| ---- | ---- | ---- | ---- |
| F16 | **MQM 2.0 为当前版本**（7 维错误类型）；MQM Council 2024-07 发布“Multi-Range Theory of TQE”，给出 **Linear Calibrated Scoring Model** 与多区间两套评分模型，并与统计质量控制（SQC）整合；DQF 类型学与 MQM 2.0 兼容 | [MQM Typology](https://www.themqm.org/mqm-pillars/typology)、[AMTA 2024](https://aclanthology.org/2024.amta-presentations.6.pdf)、[Slator](https://slator.com/mqm-council-releases-multi-range-theory-of-translation-quality-evaluation-with-new-scoring) | T173 评分卡（CP-S14-22）应以 MQM 2.0＋2024 评分模型为设计输入；SQC 可作“批次收口”的统计方法候选 |
| F17 | 参考类神经指标 SOTA：COMET/XCOMET-XL、MetricX-23/24、BLEURT；无参考 QE 有 CometKiwi-XL、COMET-source；WMT25 出现长上下文 ESA 扩展 | [COMET](https://github.com/Unbabel/COMET)、[WMT25 长上下文](https://aclanthology.org/2025.wmt-1.64) | QE 分流（§21.4“只分流”）可指定 CometKiwi/XCOMET 作候选工具；不得作裁判 |
| F18 | LLM-as-judge 可靠性证据混杂：Apple 研究指出人/模型在 MT 质量标注上都有困难；大规模研究指出提示敏感、跑次不一致、位置偏差；细粒度错误跨度上分歧大 | [Apple Research](https://machinelearning.apple.com/research/llm-translation-quality-annotation)、[arXiv 综述](https://arxiv.org/html/2606.19544v1) | 强化“LLM 不得作裁判”的判据：结构化 rubric＋双评＋人审为准；AI judge 最多产候选（P33/判官只读） |
| F19 | PE 工时度量：HTER 为经典（Specia 2010）；**编辑距离不是实际省力的好指标**（Nimdzi）；认知努力需键击日志/眼动等补充；错误类型与翻译方向影响工时 | [Specia 2010](https://aclanthology.org/2010.jec-1.5)、[Nimdzi 2020]（行业）、[Sun 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12306749) | T174 度量基线（CP-S14-28）的“PE 工时”不得只用编辑距离；按错误类型/方向分层记录 |
| F20 | WMT25 General MT：36 队参评、更难测试集、细粒度评估为主线；WMT24 结论“LLM 时代已至但 MT 未解决”；WMT25 另设自动翻译评估系统任务 | [WMT25 Findings](https://aclanthology.org/2025.wmt-1.22.pdf) | 哲学学术文本的 LLM 输出仍须按 full PE＋人审治理；不得以“SOTA”减免审校 |

### 2.5 学术出版·元数据·无障碍

| # | 发现 | 来源 | 对 064 的含义 |
| ---- | ---- | ---- | ---- |
| F21 | Google Scholar 收录最低要求：`citation_*` 元标签至少含标题、至少一位作者全名、URL/DOI；Crossref DOI 写入 `citation_doi`；兼容 Eprints/DOAJ/PRISM | [Scholar 收录指南](https://scholar.google.com/intl/en/scholar/inclusion.html)、[PKP 文档](https://docs.pkp.sfu.ca/google-scholar/en) | P6 发布门可增“学术元数据检查点”：每词条页注入 `citation_*`（标题/作者/日期/源 URL），提升可检索性 |
| F22 | JATS（ANSI/NISO Z39.96-2021；v1.4 2024 修订）为学术文章 XML 标注现行标准 | [NISO](http://www.niso.org/publications/z3996-2021-jats)、[JATS 官网](https://jats.nlm.nih.gov) | 记为“结构化输出观察线”：若未来需要归档/交换，JATS 是候选；不改变现有 md/HTML 管线 |
| F23 | ISO 999（索引）处于 FDIS 50.00（第 3 版待批），预计近期发布 | 检索汇总（ISO 87175） | 当前词条无索引；若 P5 增索引/译名对照，ISO 999 Ed.3 是判据来源候选；低优先 |
| F24 | 无障碍：WCAG 2.2（W3C Rec，2023-10）为现行 Web 指南；ISO/IEC 40500:2012 仅覆盖 WCAG 2.0；中文对齐标准 **GB/T 37668-2019**（58 项要求，四原则，网页＋移动应用）现行 | [GB/T 37668 全文](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=35ECC696805C1A67C93B74FB6D0D8EFB)、[W3C 博客](https://www.w3.org/zh-hans/blog/2020/updated-chinese-accessibility-standard) | P6 可增“无障碍检查点”：GB/T 37668 四原则抽样（对比度、替代文本、键盘可达、标题结构）；候选为告警档 |

### 2.6 交换与工具链／供应链

| # | 发现 | 来源 | 对 064 的含义 |
| ---- | ---- | ---- | ---- |
| F25 | XLIFF 2.1 已成 **ISO 21720:2024**；XLIFF 2.2 于 2025-03 成 OASIS CS 并改多部（Core/Extended）；TMX 1.4b、SRX 2.0 长期稳定 | [OASIS XLIFF 2.1](https://docs.oasis-open.org/xliff/xliff-core/v2.1/xliff-core-v2.1.html)、[XLIFF 2.2 Part1](https://docs.oasis-open.org/xliff/xliff-core/v2.2/xliff-core-v2.2-part1.html) | 记为“互操作观察线”：未来若引入 CAT 工具，XLIFF 2.x＋TMX/SRX 是交换契约候选；当前管线不迁移 |
| F26 | 供应链：SPDX 3.0（安全/VEX）、CycloneDX 1.7（AI/ML 组件、pedigree）、SLSA v1.0（构建出处）成熟；CISA SBOM 最小元素映射双格式 | [Sonatype 2026](https://www.sonatype.com/state-of-the-software-supply-chain/2026/software-compliance)、[CycloneDX](https://cyclonedx.org/docs/latest) | WP-R1（sep-core Rust）启动时应把 SBOM/SLSA 写入契约：crate 清单、构建出处、禁 yanked（与 T043 呼应） |

### 2.7 记录与风险

| # | 发现 | 来源 | 对 064 的含义 |
| ---- | ---- | ---- | ---- |
| F27 | ISO 15489-1:2016（90.92 修订中）、GB/T 26162-2021 现行；ISO 31000:2018、ISO/IEC 27005:2022 现行 | [ANSI 27005](https://blog.ansi.org/ansi/iso-iec-27005-2022-security-risk-management) | T174 留存与风险登记已引 15489/26162；风险方法论可补 31000/27005 锚点 |

## 3 对 064 与关联 specs 的映射

| 发现 | 064 落点 | 关联卡落点 |
| ---- | ---- | ---- |
| F1–F3（17100/18587 动态） | §5 标准行、§21.4 full PE 判据 | 061 standards.json（后续回写）、T169 |
| F5–F9（AI 治理族） | §21.6 T174、§16 R15 | 060（机筛人判 P33） |
| F10–F15（术语族） | §21.4 TBX、T172 | specs/058 术语提取线、rules/03 |
| F16（MQM 2.0/评分模型） | §21.4/T173 评分卡 | 060 判据表 |
| F17–F20（QE/LLM-judge/PE 工时） | §21.4 QE 只分流、§16 R11/R12 | 060 六轴、返工理论（judge 只读） |
| F21–F24（元数据/JATS/索引/无障碍） | §21.2 P5–P6、§21.5 G-Proof/G-Release | 037/038 站点主题、062 SOP |
| F25（OASIS 交换） | 观察线；不迁移 | —— |
| F1（18587 谱系细化） | §21.4 判据重评触发条件 | 061 standards.json（EP-01） |
| F26（SBOM/SLSA） | WP-R1 前置（T043 cargo-deny 呼应） | 064 §12 供应链 |
| F27（记录/风险） | T174、§16 R 系列 | rules/09 |

## 4 候选工作包与检查点（全部“待批”）

> 候选任务**不预占 T 号**；批准后按 tasks.md“从下一可用号顺序分配”规则展开，并按 064 检查点规则设验收。父链一律挂 064 的 S14/WP-T 或另立治理批，不并入既有任务计数。

| 候选包 | 内容（检查点种子） | 优先级 | 依赖 | 验收判据 |
| ---- | ---- | ---- | ---- | ---- |
| **EP-01 标准动态监测** | 建“标准状态监测表”：17100 Ed.2（约 2029）、18587:2026（DIS→发布即触发重评）、25058 AWI、999 Ed.3、8000-2 DIS；触发条件与重评动作 | 高 | — | 每项标准有触发条件、责任人、证据位；触发即登记 A064/EP 编号 |
| **EP-02 术语库深化** | TBX schema 对齐 26162-1/-2/-4＋GB/T 13725；抽取研究结论入流程（ACM 2026/SAGE 2025）；数据质量维度（ISO 8000/25012）；正反例 | 高 | T170/T172 | 样本往返；校验含数据质量；两表仍为生成视图 |
| **EP-03 知识组织观察** | SKOS/25964/LMF/TMF 差异登记；概念关系（上下位/关联）在 TBX 中的表达；不迁移 | 低 | EP-02 | 差异表 + 不迁移理由 |
| **EP-04 评分卡与校准** | ISO 5060＋MQM 2.0（Linear Calibrated/Multi-Range 二选一并记录理由）；抽样方案；双评校准（一致性指标先测后定） | 高 | T173 | 评分卡版本化；校准记录；SQC 候选评估 |
| **EP-05 QE 分流试点** | CometKiwi/XCOMET 在试金石件上产分流候选；与人工结论对照；产出“分流有效性”报告；LLM-judge 只产候选不得裁判 | 中 | EP-04 | 对照报告；误分流率与成本数据；不改判据所有权 |
| **EP-06 PE 工时度量** | 按“错误类型×方向”分层记录 PE 时间；编辑距离仅辅助；基线入 T174 指标表 | 中 | T174 | 分层基线表；无“编辑距离=省力”表述 |
| **EP-07 AI 治理增强** | 42005:2025 影响评估三阶段表；5338 生命周期位（数据/模型/更新/退役）；25058 度量来源；42006 记为生态事实 | 高 | T174 | 风险登记＋影响评估表；模型变更回归 |
| **EP-08 学术元数据与无障碍** | 词条页 `citation_*`（标题/作者/日期/源 URL）；无障碍抽样（GB/T 37668 四原则，告警档）；ISO 999 索引为低优先观察 | 中 | P5/P6 试点 | 元数据注入清单；无障碍抽样报告 |
| **EP-09 交换与供应链观察** | XLIFF 2.2/ISO 21720/TMX/SRX 差异登记；SBOM（SPDX 3.0/CycloneDX 1.7）＋SLSA v1.0 写入 WP-R1 契约候选 | 低 | WP-R1 立项 | 差异表；sep-core 契约草案含 SBOM/SLSA 条款 |

## 5 排程草案（全部“待批”）

> 波次仅表达依赖与优先级；不预约日期；上一波未过不进下一波；全部不执行、不改 064 任务计数。

| 波次 | 内容 | 候选任务（源） | 入口 | 出口 | 状态 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| **E0 监测建账** | EP-01 标准监测表；非采纳记录迁移确认 | EP-01 | 用户批准 | 监测表在位；触发条件齐全 | 待批 |
| **E1 术语深化** | EP-02（与 S14 T172 衔接）；EP-03 观察表 | EP-02、EP-03 | E0 出口 | TBX 校验含数据质量；观察表 | 待批 |
| **E2 评分与分流** | EP-04 评分卡校准；EP-05 QE 分流试点（11 件试金石样本） | EP-04、EP-05 | E1 出口 | 校准记录；分流对照报告 | 待批 |
| **E3 AI 治理** | EP-07 影响评估/生命周期/度量 | EP-07 | E1 出口 | 风险＋影响表；回归记录 | 待批 |
| **E4 出版增强** | EP-08 元数据注入＋无障碍抽样（试金石件先行）；ISO 999 观察 | EP-08 | E2 出口 | 元数据清单；无障碍报告 | 待批 |
| **E5 供应链观察** | EP-09 差异表＋WP-R1 契约草案条款 | EP-09 | WP-R1 立项 | 差异表；契约草案 | 待批 |
| —— | EP-06 PE 工时度量随 E2/E4 pilot 顺带采集 | EP-06 | 试点启动 | 分层基线表 | 待批 |

## 6 验收判据与风险

| 项 | 内容 |
| ---- | ---- |
| 验收 | 每条发现有来源；标准状态分列；候选任务有判据/依赖/优先级；排程全“待批”；全文不涉 AI 披露与版权 |
| 风险 1 | ISO 18587:2026 若在探索结论落地前发布 → 触发 EP-01 重评，§5 行同步 |
| 风险 2 | QE 工具被误用作裁判 → 以“只分流＋误分流率监控”约束，判据所有权不变 |
| 风险 3 | 术语库双源（TBX 与两表并行为事实源）→ 两表必须为生成视图，校验绑定 |
| 风险 4 | 无障碍抽样成本 → 告警档起步、试金石件先行，不设硬门 |
| 风险 5 | 供应链工具噪声 → 仅作为 WP-R1 契约候选，不新增现行门禁 |

## 7 来源清单（按域）

- 翻译服务与 PE：[ISO 88184](https://www.iso.org/standard/88184.html)｜[ISO 89761](https://www.iso.org/standard/89761.html)｜[ISO Update 2026-10](https://www.iso.org/files/live/sites/isoorg/files/news/magazine/ISOupdate/EN/2026/iso_update_202610_en.pdf)｜[EUATC 2026-04](https://euatc.org/standards-quality/iso-17100-18587-04-2026/)｜[EUATC 2026-10-13](https://euatc.org/standards-quality/emerging-iso-standards-for-ai/)｜[ATC 17100 修订](https://euatc.org/wp-content/uploads/2026/04/ATC-ISO-Blog-17100-Translation-Services-Review-05-2025.pdf)｜[openstd 19363.1](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=80ABBCA2B9AD293C9C3F39C1C494DB5C)｜[openstd 40036](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=A033EC5FE5544C460DEF326C22B5586B)
- AI 治理：[ISO 42005](https://www.iso.org/standard/42005)｜[ISO 5338](https://www.iso.org/standard/81118.html)｜[ISO 5339](https://www.iso.org/standard/81120.html)｜[NIST 交叉表](https://airc.nist.gov/docs/Crosswalk_NIST_AI_RMF_and_ISO_5338_5339.pdf)｜[IEC 42006 博客](https://www.iec.ch/blog/new-international-standard-sets-rules-auditing-ai-management-systems)｜[ISO 25058](https://www.iso.org/standard/82570.html)｜[ISO AWI 25058](https://www.iso.org/standard/91881.html)｜[ANSI 27005](https://blog.ansi.org/ansi/iso-iec-27005-2022-security-risk-management)
- 术语与知识组织：[ISO 16642](https://www.iso.org/standard/56063.html)｜[ISO 24613-1](https://www.iso.org/standard/68516.html)｜[SKOS](https://www.w3.org/2004/02/skos/)｜[NISO 25964](http://www.niso.org/schemas/iso25964)｜[NKOS SKOS-XL 映射](https://nkos-eu.github.io/2012/presentations/ISO25964-mapping-to-SKOS-XL_TPDL-2012-09-27v6.pdf)｜[openstd 10112](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=0A63743C8C1993736445B41545925CFF)｜[openstd 13725](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=8E24EBB690EE751AF0CDA643E6B0EAA5)｜[ACM 2026 抽取综述](https://dl.acm.org/doi/10.1145/3787584)｜[SAGE 2025 工具综述](https://journals.sagepub.com/doi/10.1177/18758967251392652)
- 质量评估与 QE：[MQM Typology](https://www.themqm.org/mqm-pillars/typology)｜[AMTA 2024 评分](https://aclanthology.org/2024.amta-presentations.6.pdf)｜[Slator MQM 2024](https://slator.com/mqm-council-releases-multi-range-theory-of-translation-quality-evaluation-with-new-scoring)｜[COMET](https://github.com/Unbabel/COMET)｜[WMT25 长上下文 QE](https://aclanthology.org/2025.wmt-1.64)｜[WMT25 Findings](https://aclanthology.org/2025.wmt-1.22.pdf)｜[Apple MT 标注研究](https://machinelearning.apple.com/research/llm-translation-quality-annotation)｜[LLM-judge 综述](https://arxiv.org/html/2606.19544v1)｜[Specia 2010 HTER](https://aclanthology.org/2010.jec-1.5)｜[Sun 2025 方向效应](https://pmc.ncbi.nlm.nih.gov/articles/PMC12306749)
- 学术出版·元数据·无障碍：[Scholar 收录指南](https://scholar.google.com/intl/en/scholar/inclusion.html)｜[PKP citation_* 文档](https://docs.pkp.sfu.ca/google-scholar/en)｜[NISO JATS](http://www.niso.org/publications/z3996-2021-jats)｜[JATS 官网](https://jats.nlm.nih.gov)｜[ISO 999](https://www.iso.org/standard/87175.html)｜[GB/T 37668 全文](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=35ECC696805C1A67C93B74FB6D0D8EFB)｜[W3C 中文无障碍博客](https://www.w3.org/zh-hans/blog/2020/updated-chinese-accessibility-standard)
- 交换与供应链：[XLIFF 2.1](https://docs.oasis-open.org/xliff/xliff-core/v2.1/xliff-core-v2.1.html)｜[XLIFF 2.2 Part1](https://docs.oasis-open.org/xliff/xliff-core/v2.2/xliff-core-v2.2-part1.html)｜[Sonatype 2026](https://www.sonatype.com/state-of-the-software-supply-chain/2026/software-compliance)｜[CycloneDX](https://cyclonedx.org/docs/latest)｜[SLSA–SBOM](https://slsa.dev/blog/2022/05/slsa-sbom)

## 8 边界与不做清单

1. **不研究、不纳入 AI 披露与版权有关问题**（用户 2026-11-27 裁定）；检索命中的相关内容一律不计入发现、不写入建议。
2. 不并入 064 任务书；不占 T 号；不改 105/92/13、16 分区、29 工作包计数。
3. 不执行候选工作包；不预约日期；全部“待批”。
4. 不新增 spec 卡；本文件即独立建议书载体。
5. 不把“行业报告/博客”当标准；行业证据只作趋势参考并显式标注。

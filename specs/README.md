# 规格目录索引

<!-- 本文件由 `tools/spec_index.py` 生成，不手改；门禁 check_layout 的 L3 以此文件为 specs 的索引。 -->

容器 schema 见 `rules/layout.json` 的 `specs_container`：必需 `spec.md`；禁止 `tmp/`、`__pycache__/`；规格根不得放 JSON（`results/` 承载）；`execution-log.md` 与 `execution-log/` 二选一。

| 编号 | 标题 | 状态 | bin | results | 执行记录 |
| --- | --- | --- | --- | --- | --- |
| [001-sep-sync-pipeline](001-sep-sync-pipeline/spec.md) | Feature Specification: SEP 同步管线（抓取 · 更新 · 比较 · 翻译） | — | ✓ | ✓ | 单文件 |
| [002-term-consistency](002-term-consistency/spec.md) | Feature Specification: 术语一致性检查器（tools/check_terms.py） | — | — | — | — |
| [003-academic-norms](003-academic-norms/spec.md) | Feature Specification: 学术规范门禁（tools/check_academic.py） | — | — | — | — |
| [004-engineering-doctrine](004-engineering-doctrine/spec.md) | 004 · rules/reference/engineering-doctrine 落地映射与技术债务登记 | Draft | — | — | — |
| [005-translation-campaign](005-translation-campaign/spec.md) | 规划书：全流程翻译与债务偿还（specs/005） | 草稿（待用户批准基线） | ✓ | ✓ | — |
| [006-verification-revision-mechanisms](006-verification-revision-mechanisms/spec.md) | Feature Specification: 全流程一致性验证与修订机制（SUMMARY/en/yuanwen） | — | — | — | — |
| [007-review-campaign](007-review-campaign/spec.md) | Feature Specification: 全库 A–Z 审阅战役（抓取→本地HTML比对→英语markdown复核） | — | ✓ | ✓ | 单文件 |
| [008-terminology-campaign](008-terminology-campaign/spec.md) | Feature Specification: 术语战役（全量审阅 + 逐篇抓取 + 知网查证 + 人名表拆分） | — | ✓ | ✓ | 目录 |
| [009-normalization-review](009-normalization-review/spec.md) | Feature Specification: 目录与镜像归一性复核（SUMMARY ↔ mu-lu-s ↔ yuanwen ↔ en） | — | ✓ | ✓ | 单文件 |
| [010-mulu-recategorize](010-mulu-recategorize/spec.md) | 010 mu-lu-s 分类体系重构 | — | ✓ | ✓ | 单文件 |
| [011-translation-review](011-translation-review/spec.md) | specs/011 全量翻译复核战役（复核既有所有翻译 + 术语表同步 + 人名表反向校对） | — | ✓ | ✓ | 单文件 |
| [012-orig-column](012-orig-column/spec.md) | Feature Specification: 登记册「原文」列（非英语术语原文规范） | — | — | — | 单文件 |
| [013-person-attribution](013-person-attribution/spec.md) | Feature Specification: 人名表「籍属」「生卒/鼎盛年」两列 | — | ✓ | ✓ | 单文件 |
| [014-multi-machine-cutover](014-multi-machine-cutover/spec.md) | Feature Specification: 双机双克隆工作区（M1 迁入本地 C 盘） | — | ✓ | — | 单文件 |
| [015-style-register-review](015-style-register-review/spec.md) | specs/015 译文语体全局复核（禁文言与破折号滥用） | — | ✓ | ✓ | — |
| [016-mulu-history-recategorize](016-mulu-history-recategorize/spec.md) | 016 mu-lu-s 按传统哲学史重分类 | — | ✓ | ✓ | 单文件 |
| [017-mulu-completeness](017-mulu-completeness/spec.md) | 017 mu-lu-s 分类完整性修订 | — | ✓ | ✓ | — |
| [018-yuanwen-en-audit](018-yuanwen-en-audit/spec.md) | 018 — yuanwen ↔ en 原文转换逐段人眼审计战役 | — | ✓ | ✓ | 目录 |
| [020-table-image-audit](020-table-image-audit/spec.md) | 020 — 表格与图片逐个复核战役（正确性·一致性·可渲染·格式） | — | — | ✓ | 目录 |
| [021-math-formula-audit](021-math-formula-audit/spec.md) | 021 — 数学公式全量审计战役（en/ 基准面 + 译文修订面 + 规则修订） | — | ✓ | ✓ | 目录 |
| [022-post-reconvert-proofread](022-post-reconvert-proofread/spec.md) | 022 重转后基准偿还校对战役（zh ↔ yuanwen@b20ab51b8） | — | ✓ | ✓ | 目录 |
| [023-triple-regression-audit](023-triple-regression-audit/spec.md) | 023 三向回归审校战役（en ↔ yuanwen ↔ 译文，逐行人审） | — | ✓ | ✓ | 目录 |
| [024-mathjax-v4-upgrade](024-mathjax-v4-upgrade/spec.md) | 024 MathJax v4 升级（阅读站数学渲染 3.2.2 → 4.1.3） | — | — | — | — |
| [025-standards-alignment](025-standards-alignment/spec.md) | 规格：标准规范对齐基线（standards-alignment） | 基线（Tier 1+2 获批，Tier 3 未批） | ✓ | — | 单文件 |
| [026-standards-tier3-rollout](026-standards-tier3-rollout/spec.md) | 规格：标准对齐 Tier 3 与 P1-P16 全面执行（standards-tier3-rollout） | 执行中（批 A1 连接号归一已落地；批 A2 已出任务书 ren-wu-shu-a2.md 转阶段交付；批 B/C/D 归治理会话） | ✓ | ✓ | 单文件 |
| [027-audit-stage-tasks](027-audit-stage-tasks/spec.md) | 任务书：审计已译环节增项与存量撤销（audit-stage-tasks） | 任务书交付（本会话仅出任务书，不执行具体任务——用户指令「你仅出任务书。具体任务交付给 s3_checked 之前的阶段，既有 s3_checked 完成的也撤销到该任务之前」） | — | — | — |
| [028-s25-termchecked-rollout](028-s25-termchecked-rollout/spec.md) | 任务书（合并版）：s2.4/s2.5 前置阶段滚动执行（s25-termchecked-rollout） | 执行中（回退批次） | ✓ | ✓ | — |
| [029-process-audit](029-process-audit/spec.md) | 流程全量审计 | 已完成（2026-11-15 执行） | — | — | — |
| [030-independent-review](030-independent-review/spec.md) | 独立形态审校流程（specs/030） | — | — | ✓ | — |
| [031-term-judgment-tools](031-term-judgment-tools/spec.md) | 术语判读台账与机械替换回溯工具（specs/031） | — | — | — | 单文件 |
| [032-greek-letter-style](032-greek-letter-style/spec.md) | 孤立希腊字母文字化体例试金石（specs/032） | — | ✓ | ✓ | 单文件 |
| [033-register-library](033-register-library/spec.md) | 登记册共享解析/折叠库（specs/033） | — | ✓ | ✓ | 单文件 |
| [034-register-dedup](034-register-dedup/spec.md) | 两登记册去重（specs/034） | — | ✓ | — | 单文件 |
| [035-entry-pdf](035-entry-pdf/spec.md) | 词条 Friends 版式仿排 PDF 管线 | — | ✓ | — | 单文件 |
| [036-source-preaudit](036-source-preaudit/spec.md) | 源审计前置与存量补课（specs/036） | — | — | ✓ | 单文件 |
| [037-vitepress-sep-theme](037-vitepress-sep-theme/spec.md) | SEP 版式 VitePress 主题（specs/037） | — | — | ✓ | 单文件 |
| [038-bilingual-compare](038-bilingual-compare/spec.md) | 中英比较界面重做（specs/038） | — | — | ✓ | 单文件 |
| [039-md-standardization](039-md-standardization/spec.md) | 中文 Markdown 标准化（s2.4 三轴与派生保真） | — | ✓ | ✓ | 单文件 |
| [040-coherence-audit](040-coherence-audit/spec.md) | 全系统融洽性审计（数理逻辑证明＋计算） | 进行中 | ✓ | ✓ | 单文件 |
| [041-axiom-system](041-axiom-system/spec.md) | 项目公理体系与形式化充分性审计（存根） | 已整合（存根） | ✓ | ✓ | 单文件 |
| [042-progress-model-v2](042-progress-model-v2/spec.md) | 进度模型重建（v3 · 三段 · 节点可插 · 类型定判据） | 已整合（C 系列并入 `rules/axioms.json` P 系列；三级结构落地为 `rules/pipeline.json`） | ✓ | ✓ | — |
| [043-pipeline-axioms](043-pipeline-axioms/spec.md) | 总执行书的公理化验证 | — | ✓ | ✓ | — |
| [044-b0b1-baseline](044-b0b1-baseline/spec.md) | 044 — B0/B1 前置基线：HTML 模板一致性与 markdown 跨词条一致性的公理化充分性证明 | — | ✓ | ✓ | — |
| [045-parallelism](045-parallelism/spec.md) | 045 — 全翻译流程并行性的公理化证明：充分性、一致性、完备性 | — | ✓ | — | — |
| [046-standards-compliance](046-standards-compliance/spec.md) | 046 — 规范对齐公理体系：翻译质量/校对/参考文献/工具链安全/合规的充分性、一致性、完备性 | — | ✓ | ✓ | — |
| [047-structural-reverse-check](047-structural-reverse-check/spec.md) | 047 — 结构反向核验：md ↔ HTML 结构比对补 I2 自证盲区 | — | ✓ | ✓ | 单文件 |
| [048-independent-judge](048-independent-judge/spec.md) | 048 — 独立模型族辅助判官：GEMBA-MQM 落地（供人审，不替代） | — | — | — | — |
| [049-enhancements](049-enhancements/spec.md) | 049 — 翻译增强三件：术语自动提取回填 / 回译核验 / 实时术语提示 | — | — | — | — |
| [050-term-extraction-denoise](050-term-extraction-denoise/spec.md) | specs/050 术语提取降噪（标本兼治） | — | — | ✓ | — |
| [051-pipeline-gap-audit](051-pipeline-gap-audit/spec.md) | 翻译全流程遗漏审计（2026-11-19） | — | — | — | — |
| [052-mandatory-backfill](052-mandatory-backfill/spec.md) | 强制集存量回补与跨机收编件处置（specs/052） | — | ✓ | ✓ | — |
| [053-en-template-audit](053-en-template-audit/spec.md) | 053 — EN 语料模板审计与勘误装配线 | — | ✓ | ✓ | 单文件 |
| [054-catalog-network-replay](054-catalog-network-replay/spec.md) | specs/054 — 目录四方重放网络（catalog 网络转换完备性） | — | — | ✓ | 单文件 |
| [055-mulu-frontier-recategorize](055-mulu-frontier-recategorize/spec.md) | specs/055 — mu-lu-s 前沿分类重审（两案骨架预览→选型→写回） | — | ✓ | ✓ | — |
| [056-mulu-entrywise-adjudication](056-mulu-entrywise-adjudication/spec.md) | specs/056 — mu-lu-s 逐条目分类研判（不计成本全量覆盖） | — | ✓ | ✓ | — |
| [057-mulu-fine-split](057-mulu-fine-split/spec.md) | 现象学／存在主义／诠释学拆分与全库“能细分就细分” | — | ✓ | ✓ | — |
| [058-term-full-reextraction](058-term-full-reextraction/spec.md) | 规格：全库术语二次提取与 A–Z 总表（specs/058） | — | ✓ | ✓ | 目录 |
| [059-toc-title-normalize](059-toc-title-normalize/spec.md) | specs/059 — 目录条目标题体例规范化实施（甲类机械＋乙类补译，丙类裁定不归一） | — | ✓ | ✓ | — |
| [060-six-axis-quality-gates](060-six-axis-quality-gates/spec.md) | 六轴独立质量工序建议书（标点、语法、语域、引文、计量、逻辑） | — | ✓ | ✓ | — |
| [061-standards-realignment-2026](061-standards-realignment-2026/spec.md) | 翻译全流程国标／国际规范复核（2026-11-25） | — | — | — | — |
| [062-phase12-recheck](062-phase12-recheck/spec.md) | 062 — 阶段 1.1／1.2：目录四方互转复核与 HTML 重抓·基线·转换补丁复核 | — | ✓ | ✓ | — |

共 61 个规格目录。

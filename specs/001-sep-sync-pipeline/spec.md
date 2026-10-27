# Feature Specification: SEP 同步管线（抓取 · 更新 · 比较 · 翻译）

**Feature Branch**: `001-sep-sync-pipeline`

**Created**: 2026-10-26

**Status**: Draft

**Input**: User description: "分析SEP网站结构，为后续翻译抓取、更新、比较建立一套完整可行的流程。其中翻译任务需要细化到每个文档和三审三校完整流程。坚持软件工程原则和0信任原则。有任何问题问我。力求清楚明白。然后干执行一遍做实际演示进行纠正，如此循环"

## 网站结构事实基础（2026-10-26 完整抽样分析）

以下事实经 9 个结构迥异词条（set-theory / logic-classical / bayes-theorem / bell-theorem / aristotle-logic / consciousness / ibn-sina / quine / anaxagoras）+ 辅助页面的完整抽样确认，作为本规格的领域事实：

* **词条页**（`https://plato.stanford.edu/entries/<slug>/`）：正文范围由 `<!-- BEGIN ARTICLE HTML -->` 与 `<!-- END ARTICLE HTML -->` 注释界定；版本元数据固定为 `<div id="pubinfo"><em>First published …; substantive revision …</em></div>`；分节 `<h2><a id="锚">N. 标题</a></h2>`（h2/h3/h4 嵌套），与 `<div id="toc">` 一一对应；结尾固定有 Related Entries；作者/版权在 `<div id="article-copyright">`。
* **数学**：行内 `\(...\)`（logic-classical 达 1385 处）、行间 `\[...\]`、少量 `$$..$$` 与 LaTeX 环境 `\begin{...}`；MathJax 客户端渲染；无 MathML。
* **图片**：`<div class="figure">`（可带 `avoid-break`）内 `<img src="imageN.jpg">` 为**词条目录下的相对路径文件**，须单独抓取；图注 `<span class="figlabel">Figure N</span>`；部分图注明 "reprinted with permission"。
* **脚注**：正文引用形如 `<sup>[<a href="notes.html#1">1</a>]</sup>`，脚注正文在词条目录下独立文件 `notes.html`（存在性因词条而异，404 为正常缺省形态）。
* **补充材料**：词条目录下任意命名的 `.html`（如 set-theory 的 `basic-set-theory.html`）。
* **表格**：高频元素（bayes-theorem 25 个），常嵌于 `<blockquote><table>` 内承载编号定义/公式。
* **全目录**（`contents.html`）：`- [标题](entries/<slug>/) (作者)`；别名词条 `别名 — see [目标](entries/<目标>/)` 无作者、无正文页；集群母词条（如 artificial intelligence）下嵌套子词条。
* **更新信号三源**：① RSS `rss/sep.xml` 与 `new.html`（近三个月滚动窗口，条目含 "New Entry / Revised entry by …, Changes to: Main text, Bibliography"）；② `cgi-bin/encyclopedia/archinfo.cgi?entry=<slug>`（逐词条权威版本历史：各存档版 + substantive/minor 变更类型 + 新增作者）；③ 存档日历（Spring 3/21、Summer 6/21、Fall 9/21、Winter 12/21）。
* **存档版**（`archives/<ed>/entries/<slug>/`）：与在线版正文逐字节等价（仅站点框架不同）；robots.txt 禁爬 /archives/，**用户已于 2026-10-26 明确授权绕过**。
* **爬取礼貌**：robots.txt 声明 `crawl-delay: 5`；用户授权绕过禁区，但 5 秒间隔保留为默认礼貌策略。

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 词条快照基线（Priority: P1）

对任意指定词条执行抓取，形成完整"词条包"基线：原始 HTML（正文 + 脚注文件（若存在）+ 补充材料（若存在）+ 图片）、版本元数据（首版/实质修订日期、作者、最新存档版名）、内容哈希与抓取时间，登记进基线清单。零信任要求：原始抓取物不可变，任何后续提取/转换都可由原始物重算复核。

**Why this priority**: 抓取、更新、比较、翻译四条流程的共同地基；没有可信基线，后续全部环节失去裁判依据。

**Independent Test**: 抓取 5 个样本词条（重数学、含图、含脚注、含补充材料、纯文本各一），逐一核对：每件材料存在、哈希已登记、pubinfo 与 archinfo 版本信息一致。

**Acceptance Scenarios**:

1. **Given** 词条 set-theory（含补充材料），**When** 执行抓取，**Then** 词条包内正文、basic-set-theory.html、图片（若有）、元数据齐备，各文件哈希登记在案。
2. **Given** 词条 bayes-theorem（有脚注），**When** 执行抓取，**Then** notes.html 在包内且哈希登记；词条 anaxagoras（无脚注）抓取时，notes.html 404 被记为"缺省件"而非错误。
3. **Given** 抓取中断（网络错误或 5xx），**When** 重试耗尽，**Then** 该词条标记为失败并记录原因，不静默跳过。

---

### User Story 2 - 上游更新检测（Priority: P2）

按需或定期检测 SEP 上游变化并输出"待处理清单"：① RSS/new.html 近三月增量（新增/修订词条及变更范围）；② archinfo 逐词条版本核对（权威）；③ contents.html 全目录结构 diff（新增/缺失/改名/别名变化/子词条调整）。

**Why this priority**: 决定翻译工作管线的输入；没有它，翻译对象是盲的。

**Independent Test**: 对 2026-10 已知有修订的词条（如 kant-transcendental，2026-10-24 修订 Main text + Bibliography），检测流程能列出该事件；对 2026-10 新增词条（如 academic-freedom）能识别为"待首译"。

**Acceptance Scenarios**:

1. **Given** RSS 报告 kant-transcendental 于 2026-10-24 修订，**When** 运行更新检测，**Then** 待处理清单含该词条且标注"上游更新"与变更范围。
2. **Given** 基线清单有词条 X 而最新 contents.html 已无，**When** 运行目录 diff，**Then** X 被报告为"上游缺失/改名"，需人工确认。
3. **Given** 某词条 archinfo 显示的存档版名与基线记录不同，**When** 运行 archinfo 核对，**Then** 该词条进入"待比较"队列。

---

### User Story 3 - 英文版本比较（Priority: P2）

对任一有新版本的词条，将新快照与基线快照比较，产出段落级变更清单（新增/删除/修改/移动），每条变更标注英文节号并映射到中文仓库对应 md 文档。

**Why this priority**: 把"上游变了"翻译成"哪个中文文档、哪一段要动"。

**Independent Test**: 用一个两版差异已知的词条验证清单完整（无漏报、无多余项）。

**Acceptance Scenarios**:

1. **Given** 词条 A 的旧快照与新快照，**When** 运行比较，**Then** 输出变更清单，每条含：变更类型、英文节号/位置、原文摘录。
2. **Given** 变更清单，**When** 执行映射，**Then** 每条变更指向中文仓库的具体 md 文档路径；无对应文档者（如新词条）标注"待建任务"。

---

### User Story 4 - 每文档翻译任务与三审三校（Priority: P3）

每个中文文档（对应一个词条正文页或其组成部分）有独立任务记录：英文源版本钉、当前状态、三审三校每一步的完成标记与执行者。任务分两类：**重译任务**（清空既有正文、以英文源为唯一底稿从头翻译）与**更新任务**（上游变化引发，一校只过变更段落）。翻译/更新工作一律按该流程推进。

**Why this priority**: 用户点名的核心要求，但其运转依赖故事 1–3 的产出。

**Independent Test**: 任选一个文档任务，检查其流程记录：状态机当前节点、已完成步骤、执行者、时间戳齐全可追溯。

**Acceptance Scenarios**:

1. **Given** 新翻译文档任务，**When** 按流程推进，**Then** 三审三校各步依次完成且有可判定标志（检查脚本通过、对照记录、复核签字）。
2. **Given** 上游更新引发文档修订任务，**When** 处理变更条目，**Then** 仅受影响段落重走相应校次，其余内容不重复劳动（不复查旧错原则）。

---

### User Story 5 - 实际演示与流程纠偏循环（Priority: P1）

以上四条流程在真实词条上完整跑通一轮演示（抓取→检测→比较→翻译样例），以演示暴露的问题修订流程文档；该"执行→纠偏"循环按用户要求持续进行。

**Why this priority**: 用户明确要求"执行一遍做实际演示进行纠正，如此循环"；流程的可行性只能由实跑证明。

**Independent Test**: 演示日志（各步命令、输出、异常）与流程文档修订 diff 可查。

**Acceptance Scenarios**:

1. **Given** 已产出的流程文档，**When** 完成一轮真实词条演示，**Then** 暴露的每个问题在流程文档中有对应修订或被明确记录为"维持原设计"的理由。

---

### Edge Cases

* 词条无脚注（notes.html 404）、无图片、无补充材料 → 记为"缺省件"，不算错误，但要显式记录。
* 别名词条（— see 型）无正文页 → 在目录层登记映射关系，不建翻译任务。
* 词条改名/拆分 → 目录 diff 呈现旧 slug → 新 slug 映射，转人工确认，禁止自动改中文仓库。
* 429/503/超时 → 退避重试，重试耗尽则记录失败状态，禁止静默跳过。
* 存档版与在线版差异 → 抓取源一律用在线版（权威、最新），存档版仅作固定引用指针。
* HTML 实体（`&mdash;` 等）与 MathJax 定界符 → 原样保留，禁止转换后二次编辑；任何格式转换必须可由原始 HTML 复算。
* contents.html 与 SUMMARY.md 结构不一致 → 以 diff 报告呈现，人工裁决，禁止机械同步。

## Requirements *(mandatory)*

### Functional Requirements

**抓取**

* **FR-001**: 系统必须能抓取任意指定词条的完整词条包：正文页、脚注文件（存在时）、补充材料页（存在时）、词条目录下图片、版本元数据。
* **FR-002**: 系统必须为每件抓取物保存原始不可变副本，并登记 SHA-256 哈希、抓取时间、源 URL。
* **FR-003**: 系统必须从抓取物提取版本元数据（First published / substantive revision 日期、作者），并经 archinfo 核对最新存档版名。
* **FR-004**: 相邻 HTTP 请求间隔必须 ≥5 秒；对 4xx/5xx/超时必须退避重试并记录最终状态，禁止静默跳过。
* **FR-005**: 词条目录下的图片必须随词条包一并抓取并存于仓库本地（禁止外链引用），"reprinted with permission" 图片必须在译文中标注来源。

**更新检测**

* **FR-006**: 系统必须能解析 RSS（sep.xml）与 new.html，输出近三个月新增/修订事件清单（含变更范围说明与日期）。
* **FR-007**: 系统必须能对 contents.html 全目录与基线清单做结构 diff，报告新增/缺失/改名/别名变化。
* **FR-008**: 系统必须能按词条查询 archinfo，获得权威版本历史（存档版序列、substantive/minor 标记、新增作者）。

**比较**

* **FR-009**: 给定同一词条的两个快照，系统必须产出段落级变更清单（新增/删除/修改/移动），每条标注英文节号与原文摘录。
* **FR-010**: 变更清单必须映射到中文仓库对应 md 文档；无对应者标注"待建任务"。

**翻译任务与三审三校**

* **FR-011**: 每个待译/待更新中文文档必须有独立任务记录，含英文源版本钉（pubinfo 日期 + 存档版名 + 哈希）、当前状态、三审三校各步完成标记与执行者。
* **FR-012**: 三审三校采用**经典出版映射**（用户 2026-10-26 裁定）：三审=初审（对照原文自审并签字）/复审（逐句回核原文与逻辑）/终审（终稿验收 + CI 全绿）；三校=一校（准确性：漏译/错译/事实错误）/二校（语言：欧化句、口吻、流畅）/三校（体例：引号、空格、术语表、格式检查脚本）。每个文档任务一律走完整六道，顺序 一校→二校→三校→初审→复审→终审。
* **FR-013**: 管线覆盖**全量完全重译**（用户 2026-10-26 裁定）：既有词条正文全部清空（仅保留标题与文件结构），一律以新抓取的英文源为唯一底稿从头重译，**禁止以既有中文译文作为底稿或修改依据**（零信任，杜绝错误沿袭）；上游更新同步（比较/差异/更新）作为重译完成后的常态流程持续运行。清空动作：保留文件 H1（由 SUMMARY.md/CI 管理的标题），正文清空；该动作在全库执行前必须先有该词条的可信英文基线。
* **FR-014**: 存储策略（用户 2026-10-26 裁定）：**版本元数据清单入库**（slug、版本日期、存档版名、SHA-256 哈希、抓取时间——作为审计索引随 git 分发）；**原始 HTML 与提取文本存本地** `en/` 目录（gitignore，不随仓库分发）。

**体例**

* **FR-015**: 译文必须遵守仓库体例（中文弯引号成对、CJK 与加粗空格、代码块语言标注、术语表登记、禁止 HTML/AsciiDoc 残留），并通过仓库既有检查脚本与 markdownlint。
* **FR-016**: 代码块内命令、版本号、错误信息禁止改动；数学定界符与 LaTeX 内容原样保留。

**审计（零信任）**

* **FR-017**: 每次抓取/提取/翻译变更必须留下可复核凭证（哈希、时间戳、原文锚点或 diff），任何成品可回溯到具体英文源版本。
* **FR-018**: 禁止以缓存、既有翻译或中间产物替代原始源验证；可疑处必须回到原始 HTML 或官方页面核对。
* **FR-019**: 管线必须在 `yuanwen/` 下维护一套与中文仓库同构的原文 Markdown 镜像（用户 2026-10-27 裁定）：字母目录同构、`yuanwen/SUMMARY.md` 镜像根 SUMMARY（已转换条目改链 yuanwen 路径）；转换一律以本地原始 HTML（en/，不可变快照）为唯一输入、确定性可复算（同源 HTML 必得同 md），避免反复抓取；脚注（notes.html）、补充材料、图片完全本地化（用户 2026-10-27 新增要求）：复制进 yuanwen/assets/<slug>/，正文以 ../assets/ 相对引用，yuanwen 项目自包含；yuanwen/ 为本地工作底稿（gitignore），转换登记（md 哈希+源哈希）入 baseline。
* **FR-020**: 原文 Markdown 中参考文献必须转为引用注释（用户 2026-10-27 裁定）：文内“作者-年份”引用组后追加 [^key] 脚注标记，文献节改为 [^key]: 条目的脚注定义；数学公式完全转为 LaTeX（用户 2026-10-27 新增要求）：定界符统一 $…$ / $$…$$（LaTeX 内容不变），禁止任何 HTML 标签残留——<sub>/<sup> 一律转纯文本记法 _{x} / ^{x}（用户同日指令"保持洁净"）；DK 编号、古代作品行号原样保留。

### Key Entities *(include if feature involves data)*

* **词条（Entry）**: SEP 唯一 slug、中英标题、作者、首版日期、最近实质修订日期、最新存档版名、别名映射（see 型词条指向目标 slug）。
* **快照（Snapshot）**: 某词条某时点的原始 HTML 包（正文/脚注/补充/图片）+ 各文件哈希 + 抓取时间 + 源 URL + 版本元数据。
* **变更记录（Change）**: 两快照间段落级差异清单，含类型、英文节号、原文摘录、中文文档映射。
* **文档任务（Doc Task）**: 中文 md 文档的翻译流程状态记录：版本钉、状态、三审三校步骤与执行者。
* **术语登记（Term Registry）**: 新术语的译法与首现位置（沿用仓库 yi-zhe-shuo-ming.md 机制）。

## Success Criteria *(mandatory)*

### Measurable Outcomes

* **SC-001**: 对 5 个结构迥异样本词条（重数学/含图/含脚注/含补充材料/纯文本），抓取成功率 100%，缺省件 100% 被如实登记为缺省而非错误。
* **SC-002**: 对 2026-10 内已知修订与新增词条，更新检测双源（RSS + archinfo）命中一致，无漏报。
* **SC-003**: 给定两版差异已知的词条，比较输出的变更清单与人工核对结果一致（无漏报、无多余项）。
* **SC-004**: 任一文档任务的三审三校进度可在 1 分钟内查清（当前状态、已完成步骤、执行者、时间戳）。
* **SC-005**: 演示轮结束后流程文档至少完成一次依演示结果的修订，修订记录可查。

## Assumptions

* 用户已于 2026-10-26 明确授权绕过 robots.txt 目录禁区（含 /archives/）；5 秒请求间隔仍保留为默认礼貌策略。
* 用户已于 2026-10-27 裁定"5 秒间隔太长，测试极限并发"：授权以递增并发探测 SEP 服务器耐受上限（出现 429/5xx 即收敛），全量抓取采用实测不触发限流的最大并发；逐请求留痕与退避重试纪律不变。单请求串行工具默认间隔仍为 5 秒，仅并发模式经本裁定放宽。
* 用户已于 2026-10-27 强调"内含大量数学公式，必须格式准确"：yuanwen 转换对数学内容必须逐条保真——原始 HTML 中每个 `\(...\)`/`\[...\]`/`$$…$$` 公式的内容（实体解码后）必须在产物 md 中原样出现；转换器只统一定界符（`\(…\)`→`$…$`、`\[…\]`→`$$…$$`），不得改动公式内部任何字符。此要求由 tools/check_math.py 门禁机器核验。
* 用户已于 2026-10-27 允许重写 git 记录（含改写已推送历史与 force push）。适用约束：重写前必须确认共享工作区内无并行会话正在提交（重写会孤儿化其新提交），完成后须告知所有克隆重新同步。当前待办：tools/**pycache** 字节码于 42dcff53、4d45d42f、271c9a16 入库，2026-10-27 已停止跟踪并生效 .gitignore 既有规则，待工作区空闲后用 `git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch tools/__pycache__ tools/tests/__pycache__' -- 42dcff53~1..HEAD` 清除历史中的 *.pyc 并 force push（波及最近 10 个提交）。
* SEP 词条文本许可为 CC BY-NC-SA；翻译项目沿用仓库现行 BSD-2-Clause 许可与既有发布方式；"reprinted with permission" 图片在译文中标注来源。
* 仓库现有 CI 工作流（sync-headers、mulu、markdownlint、md-padding、AutoCorrect 等）继续生效，本流程产物不得与之冲突。
* AGENTS.md 的归属修正由其他会话处理，本 feature 不触碰 AGENTS.md 与 .gitignore 残留。
* `.specify/memory/constitution.md` 目前为空白模板；本 feature 顺带以零信任与软件工程原则将其填充为正式项目宪法。
* 用户已于 2026-10-27 裁决目录重建（ADR-0005）：中文译文按 a–z 文件夹平铺放置 .md（SEP slug 命名），英文原文保留在 yuanwen/ 本地库且结构与中文侧一模一样（`yuanwen/<letter>/<slug>.md` 逐字符镜像）；别名（标题含 `— see`）与递归自指条目不列入；本轮只建空目录与仅含一行 H1 的 .md，不覆盖既有内容；先同步规则再同步目录，英文侧先行，中文侧（含 SUMMARY.md/mu-lu-s.md 路径改写）待英文侧核验后另行执行；slug 推导不确定者记 needs_review 人工裁决，不静默猜测。
* 用户已于 2026-10-27 二次裁决并取代上条（ADR-0007）：统一 SUMMARY 与磁盘结构为**上游同构**——词条为目录 `<slug>/index.md`（中文，仓库根）与 `yuanwen/<slug>/index.md`（英文，省掉 entries/ 层），先删全部词条内容目录（保留治理与项目设施）；SUMMARY 条目链接 `<slug>/index.md`、别名行保留并链到目标词条、由单一会话独自重写；mu-lu-s.md 仅同步改写链接路径；yuanwen 既有扁平内容迁入新结构；ADR-0005 的 a–z 平铺方案作废，其 slug 取证规则与存疑 slug 清单继续有效。
* 用户已于 2026-10-27 补充裁定：README 微信二维码图 wechat.png 一并删除（README 引用行同步移除，.gitbook/assets 清空）；抓取的 HTML 原文一律存 en/<slug>/（不可变原始物，不入库，与现状一致），yuanwen/ 只存转换后的 md 镜像；yuanwen.py 输出路径已对齐 ADR-0007（yuanwen/<slug>/index.md、补充材料 <x>.md、图片上游同名存词条目录）。遗留待对齐：tools/summary_sync.py 与 tools/repair_loop.py 仍按旧 a–z 字母方案定位文件，需按 ADR-0007 改造。
* 用户已于 2026-10-27 三次裁决并修订 ADR-0007（ADR-0008）：index.md 过于赘余，去掉——词条为**单文件** `<slug>.md`（中文根目录）与 `yuanwen/<slug>.md`（英文），SUMMARY/mu-lu-s 链接 `<slug>.md`；补充材料 `<slug>.<x>.md` 点号命名；图片本地化 `yuanwen/assets/<slug>/`（md 内 assets/<slug>/ 相对引用）；存量 `<slug>/index.md` 全部迁移；都是本会话的工作，summary_sync.py、repair_loop.py、common.py、progress.py、migrate_exec.py（标记废弃）等全部工具由本会话对齐。

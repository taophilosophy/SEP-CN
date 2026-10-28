# Feature Specification: 目录与镜像归一性复核（SUMMARY ↔ mu-lu-s ↔ yuanwen ↔ en）

**Feature Branch**: `009-normalization-review`

**Created**: 2026-10-29

**Status**: Created（待开工）

**Input**: 用户指令（2026-10-29）："建立任务书复核 summary、mu-lu-s、yuanwen、en 文件夹内容，格式、结构的归一性"。

## 目标与范围

对四个结构性资产做**内容、格式、结构三维归一性**复核，重点是它们**相互之间**的一致性（007 审阅战役已覆盖单对象内部质量，本战役补跨对象归一核对）：

| 对象 | 角色 | 规模底数（2026-10-29 实测） | 入库状态 |
| ---- | ---- | ---- | ---- |
| `SUMMARY.md` | 目录结构唯一数据源（GitBook 侧边栏） | 2649 个 md 链接 | 入库 |
| `mu-lu-s.md` | 手编分类目录（独立学科视图） | 1888 个 md 链接 | 入库（登记册豁免拆分） |
| `yuanwen/` | 英文转换镜像（ADR-0009 双库镜像英文侧） | 2427 个 md（含 SUMMARY 与补充材料） | gitignore，仅 6 个演示条目入库 |
| `en/` | 英文原始抓取（不可变基线） | 1880 个目录 = 1878 词条包 + `_catalog`/`_manual` 管线原位 | gitignore，本地态 |

范围基线：`baseline/entries.json` 1878 词条（正式 1872 + 撤稿留存 6）；别名（— see，603 条）无词条包，由目录层覆盖。en/ 1878 词条包对 baseline **零缺包**（实测）。计数以 `PROGRESS.md` 与 `specs/004` 登记表为准，上表为开工底数快照。

## 三维复核矩阵

**对象 1：SUMMARY.md**

* 结构（硬）：条目路径形态 `<letter>/<slug>.md`（ADR-0009）；章节层级完整；别名行指向存在的目标且为导航形态；无游离于 baseline 的条目路径。
* 格式（硬）：链接文本转义规则（`\*`/`\[`/`\]` 为 markdown 链接语法所需，保留不删，rules/01）；行格式统一。
* 内容（硬）：条目集合 = baseline 1878；条目文字 = 各 zh 词条 H1（sync-headers 单一事实源方向：SUMMARY → H1）。

**对象 2：mu-lu-s.md**

* 结构（硬）：分类树形态；条目路径必须存在于 SUMMARY（rules/01）。
* 格式（硬）：条目链接文本与 SUMMARY 一致（转义写法可不同，还原后必须相同）；无坏链。
* 内容（硬）：分类覆盖完整；复用 `tools/check_mulu_s.py`（坏链 0、路径在 SUMMARY、共有路径标题一致），另参照在途工具 `specs/007-review-campaign/bin/mulu_classify_71.py` 的分类学口径（并行会话产出，收敛后纳入）。

**对象 3：yuanwen/**（本地镜像态为准，gitignore）

* 结构（硬）：`yuanwen/<letter>/<slug>.md` 与 zh 侧一一对应；`yuanwen/SUMMARY.md` 结构镜像（2649 链接同数同目标方向）；图片布局 `yuanwen/assets/<slug>/`（ADR-0008/0010）。
* 格式（硬）：归一化四项（无 BOM、LF、换行收尾、无全角空格）+ H1 = 英文标题 + markdown 全要素（`bin/check_markdown.py`：脚注配对/表格列数/链接图片目标在盘）。
* 内容（硬）：重转换零漂移——`bin/yuanwen_recheck.py` 真实 convert_entry 路径字节一致。**字节一致只证转换器确定性，不证转译正确性，故仅为必要条件**；充分性由「格式转译一致性」专节承担。

**对象 4：en/**（不可变原始物，只读）

* 结构（硬）：`en/<slug>/` 包形态；引用闭包齐备（`tools/en_integrity.py` / `tools/fetch_audit.py`）；`_catalog`/`_manual` 管线原位豁免。
* 格式（硬）：BEGIN/END ARTICLE 标记完整；HTML 可解析。
* 内容（硬）：SHA-256 与 `baseline/entries.json` 版本钉一致；404 缺省件登记在册（零信任：翻译依据必须是登记过的英文源）。

**跨对象归一性（本战役核心增量，007 未单列）**

1. **四方集合一致性**：`baseline/entries.json` ↔ SUMMARY 条目集 ↔ `yuanwen/<letter>/` ↔ `en/` 包集，逐条列出多/缺并裁定（当前已知：四方零缺包零多余，复核须重新证实）。
2. **标题链三方一致**：SUMMARY 条目文字 ↔ zh `<letter>/<slug>.md` H1 ↔ `yuanwen/<letter>/<slug>.md` H1（↔ en `index.html` 文档标题作参照），不一致处逐条裁定。
3. **链接目标在盘存在**：check_markdown 已硬拦（数学记号伪链接守卫生效），复跑取数。

## 格式转译一致性（反机械复核核心，2026-10-29 用户裁定）

**裁定**：禁止机械复核，必须确保格式的转译一致性。检查器全绿（check_markdown/check_math/重转换字节一致）只是**必要非充分**；复核结论以转译规则目录的构件级核对与人工裁定为准。

**转译链**：`en/<slug>/index.html`（SEP HTML 构件）→ `convert_entry`（tools/yuanwen.py）→ `yuanwen/<letter>/<slug>.md` → zh 翻译侧逐节镜像（rules/04）。格式一致性 = 这条链上**同一 HTML 构件类全库转译为唯一 md 形态**，且语义无静默损失。

**转译规则目录**（自转换器构件面归纳，逐条编号，开工时落 `results/transpile-rules.md` 并允许增补）：

| 规则号 | 构件（源码依据） | 一致性判据 |
| ---- | ---- | ---- |
| T-01 | 区块结构与 div 语义分类（`_div_kind`/`render_blocks`） | 同类 div → 同级标题/段落形态；标题层级不跳级 |
| T-02 | 行内构件（`inline_to_md`/`_subsup_md`） | em/strong/code/a/上下标各自形态唯一；SEP 术语音译标记不漂移 |
| T-03 | 数学（`protect/restore_cross_block_math`） | 行内 `$…$`/行间 `$$…$$` 归属唯一；跨块数学还原无损 |
| T-04 | 表格（`table_to_md`/`_flatten_nested_tables`） | 同构表格 → 同形态 md 表；嵌套扁平化策略全库一致 |
| T-05 | 列表（`list_to_md`） | ol/ul 嵌套缩进规则唯一 |
| T-06 | 图（`figure_to_md`） | figure/img → `../assets/<slug>/` 引用形态唯一（ADR-0008/0010） |
| T-07 | 引文键（`build_cite_keys`/`link_citations`） | 作者-年份键生成与链接规则全库一致（007 的 276 缺口属此规则核对范围） |
| T-08 | 脚注与补充材料（`convert_notes`/`convert_supplement`） | 参考文献全量转脚注体例唯一；补充材料转译形态一致 |
| T-09 | 目录镜像（`write_summary`） | yuanwen/SUMMARY 生成规则与 zh 侧导航改写规则一致 |

**每条规则的三级结论**（缺一不可，逐条留凭证）：

1. **形态唯一性**（动态全库）：全库扫描该构件类的转译形态分布；同一构件类出现多种 md 形态 = finding，逐例人工裁定归一方向。
2. **语义保真**（抽样人工）：每条规则至少抽 5 例（覆盖最复杂词条），HTML 源与 md 产物人工比对——无构件被静默丢弃、降级或改义；抽样必须记录词条名与比对结论，不勾选式通过。
3. **zh 镜像兼容**（结构锚点）：转译产物的结构锚点（H1/分节/脚注/表格/公式）满足 zh 翻译工作流逐节镜像假设；锚点缺失或漂移处登记。

**执行方式**：先静态（读 convert_entry 源码归纳目录）→ 再动态（全库形态分布扫描）→ 分歧处逐例人工裁定 → 抽样语义保真。机械检查器全部保留，但输出仅作前置筛选与回归防线，不构成复核结论本身。

## 全量逐段复核（长线战役，2026-10-29 改令）

**口径**：baseline 全部 1878 词条，逐条对 `en/<slug>/index.html` 与 `yuanwen/<letter>/<slug>.md` 做全段对齐比对（复用 convert_entry 切块路径：HEAD/TAIL_RE 取 article + `extract_blocks_raw`；md 侧剥标题/作者行、截 Notes 与引用定义尾部、空行分块）。补充材料不逐段（D14 家族在途修复），只登记数量与形状。

**对齐判据**：文本骨架归一（HTML 侧去标签/去实体/数字引用标记剔除/公式定界内容→⟦M⟧；md 侧剥语法/脚注键剔除/公式→⟦M⟧/图片语法剔除留题注）后 difflib 序列对齐：

* `match` 对：记录形状特征（html 块型 ↔ md 块型）与比值，聚合成 T-01…T-09 的**全库形态分布**证据——本战役即形态唯一性扫描本体，独立 transpile 扫描器不再单列；
* `replace/insert/delete` 段与比值 <0.97 的对：**分歧段，100% 人工复核**，逐条裁定落 `adjudication.jsonl`（slug、对位、T-xx 归类、裁定、动作）；
* 逐条同时采集**标题链三元组**（SUMMARY 条目文字 / zh H1 / yuanwen H1）比对结果——"确保 SUMMARY 正确"的全量逐条凭证。

**人工复核协议（反机械，每条词条）**：分歧段全量；无分歧段抽检 ≥3 段——最长段、含公式段、含表格或链接段各一，读原文与镜像确认语义保真（非勾选式，记录词条名与结论）。

**长线战役组织**：

* **批次**：按字母 A–Z 分批，每批完成即分批提交（不 push）；
* **断点**：`results/para-review/review-log.jsonl` 一行一词（state ok/flagged/error + 计数），驱动器续跑自动跳过已录入词条，`--force` 重跑；
* **多会话认领**：认领以字母批为单位，开工三件事（status/next/claim）登记 execution-log，完成该字母批后注销认领；
* **零写入**：en/、yuanwen/、baseline 只读；裁定不改被审文件，修复走归属会话或 update 任务；
* **并行在途**：mirror 会话在途编辑文件（如 s/spacetime-holearg.md）若被扫出分歧，登记归属不裁改。

**进度口径**：战役进度以 `review-log.jsonl` 聚合为准（驱动器 `--summary`），不写 PROGRESS.md。

## 工具（复用优先，零新建起步）

既有：`tools/check_summary.py`、`tools/check_mulu_s.py`、`tools/summary_sync.py report`（上游三方裁决）、`tools/en_integrity.py`、`tools/fetch_audit.py`、`tools/yuanwen.py --all-baselined`、007 `bin/yuanwen_recheck.py`、`bin/check_markdown.py`。

唯一预期新建：四方集合一致性与标题链比对驱动器 `bin/quad_norm.py`（纯本地读盘 + baseline，无网络；输出逐条 JSON 凭证）。若既有工具组合足以覆盖则不建，缺口先在执行日志登记再动手。

## 已知发现基线（承接 007，预期非失败）

复审时以下发现若**维持原状**不计新失败；若**新增或扩大**记 finding 并归属：

* 457 脚注悬空（yuanwen：181 条补充材料 `[^note-N]` 在途修复 + 276 条作者-年份引用键缺口）——移交镜像责任会话；
* 46 未换行收尾、5 处 pm-notation 表格、232 条 math warn——归属镜像责任会话；
* `s/spacetime-holearg.md`（crlf + 4 断链）——并行会话在途编辑；
* yuanwen/SUMMARY 断链 167→0 已修复（007 收尾，write_summary 导航行 `../` 改写）。

## 约束与用户裁定

* **禁止机械复核（用户裁定 2026-10-29）**："必须确保格式的转译一致性"——检查器全绿是必要非充分条件；验收以「格式转译一致性」专节的转译规则目录核对与人工裁定为准。
* **逐段抽样→全量（用户指令 2026-10-29 两连）**：先"随机抽取1%的html yuanwen en进行逐段审阅"，随即改令"改为全量逐段复核，建立长线任务书"。全量口径见「全量逐段复核（长线战役）」节；1% 抽样方案作废，种子名单不再产出。
* **确保 SUMMARY 正确（用户指令 2026-10-29 补充）**：SUMMARY.md 正确性列为本战役硬门槛——①条目集 = baseline 1878（多/缺逐条裁定）；②条目路径在盘且为 `<letter>/<slug>.md` 形态；③标题链 SUMMARY 条目文字 ↔ zh H1 ↔ yuanwen H1 **全量逐条**核对（para_review 采集，全量凭证落盘）；④转义规则（`\*`/`\[`/`\]`）保留 + 既有 `check_summary.py`/`check_mulu_s.py` 门禁全绿。
* **零写入被审对象**：en/ 与 baseline 只读；yuanwen/ 仅 yuanwen_recheck 的窥探比对路径（不落盘）；产物只落 `results/`。
* **并行会话共存**：当前工作树有在途编辑（mu-lu-s.md、yuanwen/SUMMARY.md、tools/yuanwen.py 等已 staged）。复核在当前磁盘态执行；发现与在途编辑冲突处**只登记归属，不裁改**。
* **礼貌抓取不适用**：本战役纯本地比对，无网络请求；如需上游快照对照，走 `fetch_catalog` 既有 5 秒礼貌。
* **不可变约束**：发现问题的修复一律不在本战役内直接改被审文件（除执行日志登记后显式裁定的小修），修复走归属会话或 update 任务。

## 验收标准

1. 三维矩阵 4×3 逐格有凭证落 `results/`（各检查器原始输出 + 汇总 JSON）。
2. **转译规则目录（T-01…T-09+）建成**：每条规则有形态唯一性结论（全库扫描）+ 语义保真抽样凭证（≥5 例/条，记录词条名与比对结论）+ zh 镜像兼容结论；分歧处逐例裁定，零未裁决项。
3. 四方集合一致性：多/缺 = 0，或逐条有显式裁定登记。
4. 标题链三方比对：不一致 = 0，或逐条有显式裁定登记。
5. 007 已知发现基线不扩大（逐项对照计数）。
6. **全量逐段复核完成（长线）**：1878/1878 词条对齐凭证落盘（review-log.jsonl）；分歧段 100% 人工裁定（adjudication.jsonl 零未裁决）；无分歧段每条 ≥3 段抽检留痕；T-01…T-09 全库形态分布报告落 transpile-rules.md。
7. 执行日志留痕；`python tools/check_all.py` 九项全绿（含 `--all` 基线审计与英文镜像复核）；分批提交（不 push）。

## 产物

* `specs/009-normalization-review/spec.md` —— 本任务书
* `specs/009-normalization-review/execution-log.md` —— 干活日志
* `specs/009-normalization-review/bin/quad_norm.py` —— 四方集合/标题链比对驱动器（如需）
* `specs/009-normalization-review/bin/transpile_scan.py` —— 独立扫描器取消：全量逐段形状直方图即 T-rule 分布扫描（2026-10-29 改令并入 para_review.py）
* `specs/009-normalization-review/bin/para_review.py` —— 全量逐段复核驱动器（A–Z 分批、断点续跑、形状特征采集 = T-rule 全库分布证据）
* `specs/009-normalization-review/results/transpile-rules.md` —— 转译规则目录（T-xx 逐条：构件、判据、形态分布、抽样凭证、裁定）
* `specs/009-normalization-review/results/para-review/` —— review-log.jsonl（一行一词断点凭证）+ `<slug>.json`（逐条对齐明细）+ adjudication.jsonl（分歧段人工裁定）+ para-review-summary.md（汇总裁定）
* `specs/009-normalization-review/results/` —— 矩阵逐格凭证（目录层 / yuanwen / en / 跨对象四组）

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
* 内容（硬）：重转换零漂移——`bin/yuanwen_recheck.py` 真实 convert_entry 路径字节一致（= 镜像与 en/ 原始抓取经转换器无漂移）。

**对象 4：en/**（不可变原始物，只读）

* 结构（硬）：`en/<slug>/` 包形态；引用闭包齐备（`tools/en_integrity.py` / `tools/fetch_audit.py`）；`_catalog`/`_manual` 管线原位豁免。
* 格式（硬）：BEGIN/END ARTICLE 标记完整；HTML 可解析。
* 内容（硬）：SHA-256 与 `baseline/entries.json` 版本钉一致；404 缺省件登记在册（零信任：翻译依据必须是登记过的英文源）。

**跨对象归一性（本战役核心增量，007 未单列）**

1. **四方集合一致性**：`baseline/entries.json` ↔ SUMMARY 条目集 ↔ `yuanwen/<letter>/` ↔ `en/` 包集，逐条列出多/缺并裁定（当前已知：四方零缺包零多余，复核须重新证实）。
2. **标题链三方一致**：SUMMARY 条目文字 ↔ zh `<letter>/<slug>.md` H1 ↔ `yuanwen/<letter>/<slug>.md` H1（↔ en `index.html` 文档标题作参照），不一致处逐条裁定。
3. **链接目标在盘存在**：check_markdown 已硬拦（数学记号伪链接守卫生效），复跑取数。

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

* **零写入被审对象**：en/ 与 baseline 只读；yuanwen/ 仅 yuanwen_recheck 的窥探比对路径（不落盘）；产物只落 `results/`。
* **并行会话共存**：当前工作树有在途编辑（mu-lu-s.md、yuanwen/SUMMARY.md、tools/yuanwen.py 等已 staged）。复核在当前磁盘态执行；发现与在途编辑冲突处**只登记归属，不裁改**。
* **礼貌抓取不适用**：本战役纯本地比对，无网络请求；如需上游快照对照，走 `fetch_catalog` 既有 5 秒礼貌。
* **不可变约束**：发现问题的修复一律不在本战役内直接改被审文件（除执行日志登记后显式裁定的小修），修复走归属会话或 update 任务。

## 验收标准

1. 三维矩阵 4×3 逐格有凭证落 `results/`（各检查器原始输出 + 汇总 JSON）。
2. 四方集合一致性：多/缺 = 0，或逐条有显式裁定登记。
3. 标题链三方比对：不一致 = 0，或逐条有显式裁定登记。
4. 007 已知发现基线不扩大（逐项对照计数）。
5. 执行日志留痕；`python tools/check_all.py` 九项全绿（含 `--all` 基线审计与英文镜像复核）；分批提交（不 push）。

## 产物

* `specs/009-normalization-review/spec.md` —— 本任务书
* `specs/009-normalization-review/execution-log.md` —— 干活日志
* `specs/009-normalization-review/bin/quad_norm.py` —— 四方集合/标题链比对驱动器（如需）
* `specs/009-normalization-review/results/` —— 矩阵逐格凭证（目录层 / yuanwen / en / 跨对象四组）

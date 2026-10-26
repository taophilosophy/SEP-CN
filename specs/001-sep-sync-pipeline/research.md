# Research: SEP 同步管线

**Feature**: specs/001-sep-sync-pipeline | **Date**: 2026-10-26

每项决策格式：Decision / Rationale / Alternatives considered。所有 NEEDS CLARIFICATION 已在 spec 阶段由用户裁定（三审三校=经典出版映射；范围=全量重译+常态更新；存储=元数据入库+原文本地），此处仅余技术选型。

## D1. HTTP 客户端：标准库 urllib

* **Decision**: 用 `urllib.request`，不自装 requests/httpx。
* **Rationale**: 零信任原则下依赖面最小化——第三方包是供应链信任对象，能免则免；抓取需求（GET、超时、重试、UA 头）stdlib 完全覆盖。
* **Alternatives**: requests（API 友好但引入依赖与版本管理）；httpx（同上且过重）。

## D2. HTML 提取：html.parser 自写选择器

* **Decision**: 用 `html.parser.HTMLParser` 自写提取器，按 spec"网站结构事实基础"的标记契约定位（`<!-- BEGIN ARTICLE HTML -->` 边界、`<div id="pubinfo">`、`<div id="toc">`、`<div class="figure">`、`<sup>[<a href="notes.html#N">`、`<h2><a id="锚">`）。
* **Rationale**: SEP 页面结构稳定（2007 年以来一致），选择器契约已固化进 spec；自写提取器无依赖、行为完全可审计（零信任 II）。
* **Alternatives**: BeautifulSoup/lxml（更省事但增依赖；其解析容错行为是黑盒，出错难以归因）。

## D3. 段落级 diff：difflib.SequenceMatcher

* **Decision**: 把两版正文各切分为块序列（`<p>`/`<h2>`/`<h3>`/`<blockquote>`/`<table>`/`<div class="figure">`），HTML 实体解码后对块文本做 `difflib.SequenceMatcher` 对齐，输出 add/remove/replace/move 四类。
* **Rationale**: stdlib 自带；块级对齐与"段落级变更清单"（FR-009）语义一致；行级 diff 对 HTML 源码无语义（一行可能是半个段落）。
* **Alternatives**: XML tree-diff（实现复杂度不成比例）；整页哈希（只能回答"变没变"，不能回答"哪里变了"）。

## D4. 元数据清单：baseline/entries.json 单文件

* **Decision**: 一个 JSON 数组，slug 为主键；历史维度交给 git 历史。
* **Rationale**: 文本可 diff、入版本库天然带时间线；1800 词条 × ~10 字段 ≈ 数百 KB，单文件可控。
* **Alternatives**: SQLite（查询强，但二进制入库不可 diff、冲突难合并）；每词条一个 JSON（文件数翻倍，git 状态噪音大）。

## D5. 任务记录：tasks/<首字母>/<slug>.json

* **Decision**: 每文档任务一个 JSON 状态机文件。
* **Rationale**: SC-004 要求 1 分钟内查清进度——按 slug 定位一查即得；JSON 不触发 markdownlint/links 等 CI；可机读可机写。
* **Alternatives**: markdown 台账（人易读但与 CI 扫描冲突、易手改失真）；GitHub Issues（强依赖网络与权限，离线不可用）。

## D6. 三源权威序

* **Decision**: 版本权威=archinfo（逐词条、含 substantive/minor）；发现源=RSS + new.html（三个月滚动窗、带变更范围）；结构权威=contents.html（全目录、含别名/子词条）。冲突时以 archinfo + contents.html 裁决，RSS 仅作触发信号。
* **Rationale**: RSS 描述的是"事件"，archinfo 描述的是"状态"；零信任要求以状态为准。
* **Alternatives**: 只用 RSS（漏掉三个月窗口外的变化；RSS 描述与实际不符时无从纠正）。

## D7. 检测节奏：存档日历驱动 + 每日 RSS

* **Decision**: 每季存档日（3/21、6/21、9/21、12/21）后 7 天内跑一轮全量 archinfo 核对（1800 请求 × 5s ≈ 2.5 小时）；平时每日跑 RSS 增量。
* **Rationale**: SEP 变更集中在存档日前后；全量核对保证零信任"不信任增量"。
* **Alternatives**: 每日全量（对服务器不礼貌且无信息增益）；只看 RSS（见 D6）。

## D8. Windows/CI 双平台陷阱

* **Decision**: 全链路 UTF-8 无 BOM、LF 行尾；文件名一律取 contents.html 的 slug 原样（小写连字符）；图片文件名保留 SEP 原名并**逐字符**写入引用；路径拼接用 os.path 并以仓库根为基准。
* **Rationale**: 本仓库 D 盘经 UNC 挂载且 Windows 大小写不敏感——本地通过、Linux CI 404 是本仓库已知事故形态；编码不一致会让哈希跨机不复算。
* **Alternatives**: 无（这是约束不是选择）。

## D9. 体例检查脚本：新建 tools/check_style.py

* **Decision**: 新写 `tools/check_style.py`，检查：中文弯引号成对与方向、加粗 `**` 两侧空格、CJK 与西文/数字间空格、HTML 标签残留、`text` 代码块标注、日式/直角引号。
* **Rationale**: 三校步骤（FR-012）需要可判定工具；本仓库 `script/` 只有 audit.py，姊妹项目的引号/加粗检查脚本不在本仓库，不能假设存在（零信任：不信任未核验的假设）。
* **Alternatives**: 只靠 markdownlint（覆盖不到中文标点/空格体例）。

## D10. 清空重译的原子性与前置条件

* **Decision**: 每文档一次提交完成"清空+重写"；执行前强制校验该词条基线存在且哈希可复算（`task_ops.py` 内置 gate）；清空仅删正文，保留 H1。
* **Rationale**: 宪法附加约束"全库级破坏性动作必须先有可信基线"；单文档原子提交保证可回溯、可中断续作。
* **Alternatives**: 批量清空脚本（一次提交动千文件，违背宪法 IV 高频小步提交）。

## D11.（演示轮 1 增补）产物防丢失：git add 前置化

* **Decision**: 每份产物写盘后立即 `git add` 并高频 commit；单文件"写入成功"不作数，跨进程双视角复核。
* **Rationale**: 演示轮 1 实录：并行会话的 git 清理曾清掉未跟踪的 6 份产物；对象库是唯一可信底（详见 plan.md 环境补充约束）。
* **Alternatives**: 仅本地副本（换机即失）；与并行会话协商文件锁（无协调机制，不可依赖）。

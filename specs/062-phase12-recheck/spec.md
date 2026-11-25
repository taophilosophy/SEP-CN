# 062 — 阶段 1.1／1.2：目录四方互转复核与 HTML 重抓·基线·转换补丁复核

- 编号：specs/062；立项日期：2026-11-25；状态：执行中（阶段 1.1 先行，1.2 随后）
- 承办：主会话（ADR-0034 主代理单干）
- 上位：specs/054（目录四方重放网络）、specs/053（EN 模板审计与逆向装配）、specs/044（B0–B3 保真基线族）、specs/001（同步管线）、rules/08（知难行易）

## 0. 方向声明（rules/08 §0）

用户 2026-11-25 指令：“忽略礼貌抓取，重新抓取 HTML，更新本地基线，复核既有 HTML markdown 转换补丁的必要性，有效性，一致性，以及转换进度报告。并将上述流程标准化，记为阶段 1.2。1.1 阶段是抓取目录，比较四方目录转换。现在先进行阶段 1.1 再进行阶段 1.2。”

复述为两个有序阶段：

**阶段 1.1 — 抓取目录、比较四方目录转换**（先行）
1. 重抓上游 `contents.html`，落新钉存快照 `en/_catalog/<ts>-contents.html`，重建 `baseline/catalog.json`。
2. 比较四方目录工件：上游 contents.html（钉存）／`yuanwen/SUMMARY-en.md`／`SUMMARY.md`／`mu-lu-s.md`，含支撑账（`baseline/catalog.json`、`catalog-skeleton.json`、`catalog-residual.json`、`mulu-map.json`）。
3. 以既有五向门禁（G1–G5）＋漂移比对出报告：集合差、行文字差、重放等值、词条增删改名。

**阶段 1.2 — 重抓 HTML、更新本地基线、补丁复核、进度报告**（1.1 完成后）
1. 全量重抓各词条 HTML，与既有钉账比对，更新本地基线（en/ 与 baseline 钉账；ADR-0045 双账语义不变：`files[].sha256` 永不改写，新差异走分歧账）。
2. 复核 `baseline/en-patches/` 既有补丁的**必要性**（上游修订后是否仍然必要）、**有效性**（命中计数硬校验）、**一致性**（补丁↔勘误表↔divergences 账↔转换器行为）。
3. 出转换进度报告：yuanwen 转换覆盖、I2/I3、B3.1／B3.2 面、补丁池与残差池状态。
4. 把上述流程标准化，写入本 spec 的 SOP（命令、判据、失败处理、证据留痕）。

## 1. 非目标

- 不改 `en/` 的文字与格式层（ADR-0062）；不改译文措辞，不重译。
- 不改 `tools/yuanwen.py` 的转换规则（若 1.2 发现转换器缺陷，只登记并提出，不在本卡直接改）。
- 不新建翻译任务（上游真漂移需建账的，只出清单与建议，按 specs/001 compare 流程另批）。
- 不动 `mu-lu-s.md` 的归类语义（人工裁定优先）；不重做 specs/055–057 的分类结论。

## 2. 验收判据

阶段 1.1：
1. 新快照落盘且可复算：`fetch_catalog.py` 输出的 added/removed/renamed/alias_changed 有记录（空也要记录“无变动”）。
2. G1–G5 全绿或每一项红都有归因与落点；`catalog_drift --latest` 四方差集为零或逐条解释。
3. `summary_sync report`（add/remove/mapped）与 `gen_en_summary --check` 状态入报告。
4. 报告落 `results/phase11-report.md`＋机读 JSON，结论可复核（命令与时间戳在案）。

阶段 1.2：
1. 重抓结果与旧钉逐件比对，新增／缺失／内容变化三族计数与清单在案。
2. 每条补丁给出必要性／有效性／一致性三判定之一：保留／退役／改写／登记例外，并留证据（命中计数、上游 sha、分歧账行）。
3. 进度报告给出可核对的计数（转换覆盖、I2/I3、B3.1/B3.2、池面），不复制过期数字。
4. SOP 写入本 spec（或 `sop.md`），命令可照抄复跑；`check_all` 全绿；提交推送且 `git log origin/main..main` 为空。

## 3. 授权与偏离登记

- **抓取节律**：用户 2026-11-25 指令“忽略礼貌抓取”。事实核对：`rules/05` 的 5 秒间隔已于 2026-11-18 由 ADR-0069 废除，`tools/fetch.py` 已无强制间隔，本次无需改代码；本条作为用户授权的形式确认入档。发现 `AGENTS.md` 硬约束表仍写“相邻请求至少间隔 5 秒”，与 ADR-0069 冲突，登记为文档陈旧项（见 `results/phase11-report.md` 观察节），修复走 rules 修订流程。
- **robots**：沿用 2026-10-26 用户授权（含 `/archives/`），不另议。
- **并发**：重抓可并发，但重试退避、逐请求留痕、禁止静默跳过三条纪律不变（宪法 V）。

## 4. 阶段 1.1 执行记录（2026-11-25）

- 抓取：`python tools/fetch_catalog.py` → 快照 `en/_catalog/20261125T023957Z-contents.html`，`baseline/catalog.json` 更新（fetched_at 2026-11-25T02:40:06Z）。
- 解析计数：items 1873、alias_rows 652、cluster_mothers（以重建结果为准）。
- 与上一基线（2026-11-24T18:25:19Z）比较：added／removed／renamed／alias_changed **四项全空**。
- 四方门禁与报告：见 `results/phase11-report.md`。

## 5. 阶段 1.2 执行记录（2026-11-25）

**执行方式**：`python specs/062-phase12-recheck/bin/phase12.py --fetch --config A`（16 路，ADR-0069 无强制间隔）。

**前置修复**（本阶段发现并修复，见 tools 单测）：

1. `tools/fetch_all.py` 自 2026-11-18 起不可用：`CONFIGS` 已改为整数线程数，第 162 行仍按 `cfg[0]` 取数 → `TypeError`；worker 内 `_checkpoint(..., cfg)` 引用不存在的 `cfg`。
2. `fetch_one` 的 `unchanged` 结果（无 `files`）被 worker 直接送 `upsert_baseline` 会整条覆盖钉账、丢失 `files[].sha256`（ADR-0045 风险）。现改为：unchanged 不写盘、不动账、仍转换；`upsert_baseline` 增护栏，无 `files` 的拒收。

**差集口径**：`results/entries-before.json`（抓取前）↔ 抓取后 `baseline/entries.json`，按 `slug → {path: sha256}` 比较。en/ 文件的性质分类用 `bin/en_delta.py`：

| 判定 | 判据 | 处置 |
| ---- | ---- | ---- |
| `new` | HEAD 无此路径 | 随钉入库，走 specs/001 建账 |
| `layout` | 可见文本逐字等值（仅换行／标签属性／注释／模板重排） | 不建账；钉前移照常 |
| `tokens` | 词元多重集等值但词序变 | 人工核对 |
| `text` | 可见文本有实质改动 | 出建账清单，走 compare → 置空待译（ADR-0050/0068） |

**结果**（2026-11-25，`results/phase12-run.json`、`phase12-analysis.md`）：

* **抓取**：1873/1873，0 抓取失败；unchanged 1351、账变化 522；耗时 1414 秒（16 路）。账变化的主体是 `local.js` 补登（存量文件入 `files[]`，盘面不变），磁盘真变化 126 文件／100 词条。
* **转换**：1871 件成功；2 件因 Windows 文件占用 `PermissionError` 失败（frege-logic、scientific-reproducibility），补转后 I2 复核 **1873 件 0 issue**。
* **磁盘变化分类**（`en_delta.py`）：`text` 65、`layout` 40、`rename-wave` 17、`binary` 3（含重导出的 2 件 SVG）、`asset` 1（合计 126；SVG 并入资产类，sha 变化即随钉替换，不建账）。`text` 中的大改件与 10 件 `substantive_revision` 变更完全对应（justice-retributive、hume-moral、plato-sophstate、culture-cogsci、gorampa、logic-deontic、delusion、embodied-cognition、rule-following、schopenhauer）。
* **元数据**（`entry_meta_delta.py`）：29 件变化，其中 `substantive_revision` 变更 10 件（上游 2026-11-21～24 发布）。
* **补丁**：3 条全部“有效”（命中 1/1），`mismatch 0`、`admission_bad 0`、`index_bad 0`、`public_candidates 0`；无需退役或改写。
* **基线**：B3.1 重跑 1663／210，与旧基线集合零差（转好 0／转差 0）；B3.2 judge（旧池）pool 1780／gap 48／stale 45（叙述值，无落盘凭证），`--build` 重建池后 pool 1811／gap 62／stale 0；相对旧基线（1851／22／0）新增 gap 40、修复 0——新增族集中在本轮 `en` 变化件，待 053 线下批四出口处置。
* **收口复核**（`results/phase12-review.md`，独立复算）：实质数字全部成立；订正本卡 `text 66`→65 与分类串；修复 `logic-deontic` 重钉时 3 个旧图摘钉（按 `registered_orphans` 口径恢复登记，`en_integrity --all` 硬发现 4→3，余项均既存）；新登记待处置项——上游新版 `aristotle-psychology/notes.html` 双点错链 `index..html#ref-1`（建议补丁 P-004 或格式例外）、`.svg` 重导出被判 `layout` 的分类盲区、`en_integrity` 未入 `check_all`、`upsert_baseline` 整体替换 `files[]`。
* **处置**：`text` 65 件出建账清单（10 件正式修订优先），走 `compare.py` → 置空待译；`layout`／`rename-wave`／`binary`／`asset` 不建账；`522` 账变化不构成上游更新。

## 6. 全库置空复核与账外补建（2026-11-25，用户指令“所有中文条目全部置空只 H1、允许重写进度”）

**复核事实**：`[a-z]/*.md` 共 1880 件，正文全部为 H1-only（0 件有正文、0 件缺 H1）；`tools/wipe_translations.py --apply` 报 `already 1868`、任务 `already-cleared 1200`，幂等零写盘。

**发现的缺口**：catalog 主条目 1873 件中只有 1200 件有 retranslate 任务账，**673 件从未建账**（历史账外件）——正文虽已 H1，但无“待译”状态位，进度视图记为账外。

**处置**：

1. `bin/wipe_missing_tasks.py`：对无账件走状态机正规原语 `create(retranslate)` → `clear`；试金石 5 件先行，全量 668 件全部 `created+cleared`（forced 0、error 0）。
2. journal 壳补齐 656 件（progress 的“已建任务”口径按 journal 词条计），使账外归零。
3. `progress.py` 重写 PROGRESS：已建任务 1873、账外 0、骨架 1873（全部在账内）、有正文 0、账实不符 0、核心段完成 0、在途 0、阻塞 0。
4. `check_all` 19 项全绿；`wipe-2026-11-25.json` 报告随批刷新。

**口径说明**：新建账的 673 条任务各带 1 条 `clear` 步骤（过程凭证，ADR-0084 D4 只追加），正文不动。

## 7. CI 面更新（2026-11-25，用户批准）

用户提问“是否合并 1.1/1.2 的两个 CI”；结论是**不合并**（判据所有权、issue 口径、失败域隔离、耗时与只读面均不同），只做两处补强：

1. `catalog-drift.yml` 增“目录网络五门（G1–G5）”步骤：此前定时面只跑 G1 装配核验，G2–G5 仅在 push 的 `checks.yml`；现每日三班的 1.1 判据完整。目录四方无漂移而五门红（派生链断裂）另报 `sep-sync-broken`。
2. `en-roundtrip.yml` 增“②′ 补丁池体检（`check_en_patches --strict`）”步骤（约 2 秒，含公共性探针），并把 `en-patches` 登记进 `tools/check_all.py` 的 `GATES`（现 20 项）；巡检自身失败条件并入补丁池红。
3. 1.2 的全量重抓**不进定时 CI**（4528 资产请求 × 日三次不礼貌、CI 只读不能落钉），保持本地 `bin/phase12.py --fetch`；上游修订的 CI 面由 `detect_updates`（元数据）与基线差集承载。


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

## 5. 阶段 1.2 执行记录

（1.1 收口后填写；残差族与补丁判定逐条落 results。）

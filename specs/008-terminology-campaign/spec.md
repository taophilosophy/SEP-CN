# Feature Specification: 术语战役（全量审阅 + 逐篇抓取 + 知网查证 + 人名表拆分）

**Spec ID**: `008-terminology-campaign` | **Created**: 2026-10-28 | **Status**: In progress

**Input**: 用户裁定（2026-10-28，登记于 [rules/adr/0012](../../rules/adr/0012-译名依据源与人名表拆分.md)）四点：① 术语表全量逐个审阅、更新；② 从英文原文**逐篇遍历**抓取更多哲学术语扩充词汇表（不计成本）；③ 所有翻译原则上不采纳维基百科译名、确保符合学术规范、**优先从知网查询**；④ 建立标准流程，同时从术语表拆分出人名表（要求同上）。

## 裁定与假设（Assumptions）

* **ADR-0012**（2026-10-28）：译名依据优先级 = 知网系权威源（CNKI 翻译助手、术语在线审定名词）→ 权威译本与学术出版通行译法 → 学界惯例；**禁止维基百科及任何大众百科译名**作为依据；两登记册统一五列（原文|译法|首现|依据|裁定日期），依据必填。
* **通道实测**（2026-10-28，P0 换站后更新）：
  * 术语在线 `api.termonline.cn/main-serve/business/tm/tmWord/standardSearch`（参数 `term&match=2&sources=&pubYears=&pageSize=20&pageNo=1`）**匿名可用**，返回标准文件术语库（GB 标准）数据（字段 `cnName/enName`）；审定名词库主接口 `tmWord/allSearch` 需登录 token（手机/微信注册），匿名恒回空 `totalRecords=0`。
  * **有道词典 `dict.youdao.com/result?word=X&lang=en` 匿名可用**（SSR 页，按学科分组释义），P0 换站裁定接入为 `youdao-aux` provider——**辅助参考档**：不作依据，供裁定辅助与多义区分（如 abduction 逻辑学义=溯因推理、法学义=诱拐罪）。
  * CNKI 翻译助手 dict.cnki.net 对非浏览器 TLS 指纹（curl/urllib/UND）断连或返回空壳 SPA；通道为浏览器辅助或后续发现的内部 API，插件位保留。
  * P0 换站探测未通（2026-10-28）：中国大百科全书 www.zgbk.com（可达但 content-protect/mtoken 请求签名，SSR 壳无结果）；国家哲社文献中心 www.ncpssd.org（可达但 /searchHandler/search 需会话参数，站点自带查询串亦回 0）；必应词典（重定向无数据）。**结论：查证通道主力仍待审定库 token 或浏览器通道；有道辅助参考已投产。**
  * 结论：`cnki_query.py` 以 provider 插件化设计（termonline-standard 与 youdao-aux 可用即录；cnki-dict 与 termonline-审定库在获得通道后接入），每条查询结果落凭证 JSON，含来源档位。
* **礼貌抓取**：对知网系站点请求间隔 ≥5 秒（宪法 V 同标准），4xx/5xx/断连退避重试并记录，禁止静默跳过。
* **零信任**：知网/术语在线返回的译名只是**证据**，不是裁定；入库仍走"先登记后使用"，冲突时人工（会话）裁定并留痕。
* **范围**：语料 = `yuanwen/<字母>/<slug>.md` 全量镜像（2427 件，2026-10-28 计数）与 `en/` 原始抓取；人名候选与术语候选同池分型。

## User Scenarios & Testing

### User Story 1 — 逐篇遍历抓取术语候选（P1）

`python tools/term_harvest.py [--letter a]`：遍历 yuanwen/ 全库（可按字母分批），从英文正文提取术语候选（-ism 词族、斜体术语、高频概念短语、括注定义式），与两登记册 + 词汇表 + 候选池已登记条目求差，落 `tasks/term-pool.json`（沿用 published/held/rejected 状态机），断点续跑（每字母一批，进度落盘）。

**Acceptance**:

1. 全库跑完产出候选池，含来源（slug 清单）与频次；已登记条目零重复入库。
2. 中断重跑不重复计频（幂等：按 slug 缓存单篇提取结果）。
3. 人名候选单独分型（person），与规则 03 体例（现代人名保留英文）联动过滤。

### User Story 2 — 知网查证与依据落库（P1）

`python tools/cnki_query.py --from-registry` / `--terms <词>`：对登记册/人名表/候选池逐条查证（termonline-standard 等 provider），≥5s 间隔、断点续跑、凭证落 `specs/008-terminology-campaign/results/`。输出每条：各源译名、来源档位建议、与现行译法一致性判定。

**Acceptance**:

1. 每条登记行有可追溯凭证文件（查询词、时间、原始 JSON）。
2. 查证失败（通道断/无结果）记 `unverified`，不阻塞门禁，不臆造。
3. --resume 跳过已查条目；重复运行幂等。

### User Story 3 — 全量逐条审阅驱动（P1）

`python tools/term_audit.py`：读两登记册全量行，逐条关联查证凭证，产出审阅报告（specs/008-terminology-campaign/results/audit-<日期>.md）：一致/不一致/查无/未查证四态；不一致行给出建议译法与新依据文本，**只报告不修改**（核验器只报告不修改，specs/006 裁决沿用），修正走裁定 → Edit 登记册 → check_terms 门禁。

**Acceptance**:

1. 报告覆盖两登记册 100% 行（154 术语 + 19 人名为 2026-10-28 基线）。
2. 每行状态可机读（results/*.json 同步落盘）。
3. 维基来源排查：依据列含"维基"字样即标红（存量禁令）。

### User Story 4 — 三表一致性门禁（P0，已交付）

`tools/check_terms.py` 三表校验 + 缺依据告警（2026-10-28 完成，ADR-0012 批次 16b325ac），`check_all.py` 已挂。

## Requirements

* **FR-001**: 候选池、查证凭证、审阅报告均为持久文件，可断点续跑（战役跨会话多日执行）。
* **FR-002**: 所有网络访问 ≥5s 间隔 + 退避重试 + 失败记录（礼貌抓取）。
* **FR-003**: 纯标准库实现（tools/ 既有约定），UTF-8、LF，docstring 声明用法与退出码。
* **FR-004**: 核验器只报告不修改；登记册修改一律走登记流程（先登记后使用）。
* **FR-005**: provider 插件化：termonline-standard（可用）、cnki-dict（浏览器辅助/待通道）、termonline-审定（待 token）；provider 失效自动降级并明示。
* **FR-006**: 人名与术语分池分型；人名候选进人名表流程，遵守"现代人名保留英文"体例。

## Edge Cases

* 术语在线匿名接口对部分词返回空（标准库覆盖率低）→ 记"标准库无收录"，不作为否定证据。
* CNKI 断连为常态 → 退避重试 3 次后记 unverified，轮内跳过，轮后再试（迭代至不动点）。
* 同英文术语多译法并存（审定/标准/学界不一致）→ 全列，裁定进登记册时分主译/亦作。
* 希腊文/德文原词（如 suniêmi、Lehrfreiheit）不在知网系源覆盖内 → 依据走学界惯例档，如实标注。
* 大小写与斜体变体（Bayesianism/bayesianism）→ 键规范化后归并，展示保留首见形。

## Success Criteria

* SC-1: 两登记册 100% 行有查证凭证与四态判定（首基线 154+19 行）。
* SC-2: 全库候选池产出，零已登记重复；人名候选分型可用。
* SC-3: check_terms 三表全绿；依据列无"维基"来源残留。
* SC-4: 凭证目录 results/ 全部入库（证据可追溯）。

## 执行批次

* B0（2026-10-28，本次）：ADR-0012 立法 + 拆分 + check_terms 三表 + spec + 工具链 + 登记册基线首轮查证。
* B1+：逐字母批次（harvest → 查证 → 裁定 → 登记），断点续跑，多会话可接手（交接卡见 execution-log.md）。

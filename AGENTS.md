# AGENTS.md

本文件是 AI 编码代理（Claude Code、ZCode 等）在本仓库工作的 **入口指引**。本仓库是《斯坦福哲学百科全书》（Stanford Encyclopedia of Philosophy, SEP）的简体中文翻译项目，基于 GitBook 格式、辅以本地 VitePress 双语阅读站发布。

> 历史注记：本文件曾误植另一项目（UNIX 书翻译）的规范全文，已于 2026-10-27（ADR-0001）改写为入口指针。规则正文一律以 `rules/` 为准。

## 规范层级（冲突时上位覆盖下位）

1. **项目宪法** `.specify/memory/constitution.md` —— 零信任、可追溯、单一事实源、流程先行、礼貌抓取、体例即契约。
2. **全局规则** `rules/` —— 宪法的操作性展开，修订走 `rules/adr/`（决策记录 9 个，取代链完整）；`rules/README.md` 的**规则地图**给出九类规则/文档的唯一存放位置。
3. **参考方法论** `rules/reference/` —— engineering-doctrine（G0-G5 门禁、32 条总纲、FR/NFR、交付清单），**不具约束力**，采纳进 rules/ 才生效。
4. **工程规格** `specs/<NNN>-*/` —— 单项工程的规格、契约（contracts/cli.md 职责权属）与执行记录（execution-log.md）。
5. `README.md` —— 面向访客的说明。

## 按任务类型的必读

| 要做什么 | 先读 |
| ---- | ---- |
| 翻译 / 校对词条 | `rules/04-translation-workflow.md`（先建任务 `tools/task_ops.py`，状态机禁止跳步）、`rules/02-style.md`、`rules/03-terminology.md`、`rules/07-academic-norms.md`（学术规范，s3/r3 挂钩实拦）；翻译工程标准 v1.0 见 `fang-fa-lun/gong-cheng-fang-fa.md`（散页标准，待折叠进 rules/04） |
| 改目录 / 标题 / 结构 | `rules/01-repository-structure.md`（SUMMARY.md 唯一数据源；词条为 `<letter>/<slug>.md` A–Z 字母目录，ADR-0009；mu-lu-s.md 为手编分类目录） |
| 接入新词条 / 更新任务 | `specs/001-sep-sync-pipeline/contracts/cli.md` 职责权属表：apply-add 唯一入口、compare 持久变更文件 → update 任务 changes: 证据 |
| 提交 / 用工具 / CI | `rules/05-ci-and-tools.md` |
| 修订规则 / 批量与破坏性动作 / 多会话协作 | `rules/06-governance.md` + `rules/adr/` |

## 会话开工五分钟

1. `git log --oneline -5` + `git status`——核对基点；本仓库多会话并行，**推送前先 `git pull --rebase`**（并行会话 push 竞态会孤儿化对方提交，见 `rules/06-governance.md`）；
2. 通读 `rules/README.md` 的“规则地图”与“快速判例”；
3. 跑门禁：`python tools/check_all.py`（一键全量：七项门禁 + 单元测试，并行约 6 秒，应全绿）；
4. 查进度与任务：`PROGRESS.md`、`python tools/task_ops.py show <slug>`；
5. 收工前：相关检查器复跑、相关文件提交（中文一行信息），不留未提交的半成品。

## 当前阶段与主战场（2026-10-27）

基础设施已全部就绪：结构定型（ADR-0009）、抓取完整性收敛（fetch_audit 不动点 1724/1724）、管线无矛盾（八项职责权属契约化）、门禁全绿、学术规范挂钩实拦、G5 里程碑 tag `v2026.10.27-目录重建定型`。**主战场**：① 首轮真实翻译（1791 词条，abduction 任务已就绪，走完整三审三校验证工作流）；② 74 条上游增量 intake（`specs/001-sep-sync-pipeline/dir-rebuild/upstream-increment.json`：建任务 → 译名登记 → apply-add）；③ 更新流程例行化（存档季 `fetch_catalog` + `compare`，漂移自动进 update 任务）。进度看 `PROGRESS.md`，技术债务看 `specs/004-engineering-doctrine/spec.md` 登记表。

## 硬约束速览

* **零信任**：既有中文译文一律不作底稿或修改依据；可疑处回原始 HTML（`en/` 原始抓取、`yuanwen/` 转换镜像，均不入库）核对；一切成品可回溯到英文源版本钉（pubinfo + 存档版名 + SHA-256）。
* **单一事实源**：结构看 `SUMMARY.md`，术语看 `yi-zhe-shuo-ming.md`，版本看 `baseline/`，任务状态看 `tasks/`；两处不一致时修弱势方。
* **流程先行**：动笔前先有任务记录（`tasks/`）；先登记术语后使用；每步留 `evidence` 凭证。
* **提交纪律**：高频小步提交，中文一行信息；只提交相关文件；直接提交 main；未经用户要求不 push、不 force；**推送前先 pull --rebase**（并行会话竞态，见 `rules/06-governance.md`）。
* **抓取礼貌**：相邻 HTTP 请求 ≥5 秒；4xx/5xx/超时退避重试并记录，禁止静默跳过。
* **抓取完整性**：词条包内被引用资产必须齐备——`tools/fetch_audit.py`（引用闭包迭代至不动点，缺件自动补抓，404=缺省件登记）。
* **更新流程**：`fetch_catalog` 检测漂移 → `compare.py <slug>` 产出持久变更文件 → `task_ops.py` update 任务（evidence 以 `changes:` 开头）→ 三校走变更段。
* **结构形态**：词条为 `<letter>/<slug>.md`（SEP slug 命名，字母目录 A–Z），别名链目标、导航链 README；英文镜像 `yuanwen/<letter>/<slug>.md` 逐字符一致（ADR-0009）。
* **单体文件**：叙事/规则/规格类 md 超 1000 行或 100KB 必须按文件夹拆分（登记册与生成物豁免，见 ADR-0004）；门禁 `tools/check_doc_size.py`。
* **检查**：本地一键 `python tools/check_all.py`（七项门禁 + 单元测试；`--all` 加基线审计）；定点 `check_academic.py --docs <路径> --strict`；推送后 CI 为最终裁判。

# AGENTS.md

本文件是 AI 编码代理（Claude Code、ZCode 等）在本仓库工作的**入口指引**。本仓库是《斯坦福哲学百科全书》（Stanford Encyclopedia of Philosophy, SEP）的简体中文翻译项目，基于 GitBook 格式、辅以本地 VitePress 双语阅读站发布。

> 历史注记：本文件曾误植另一项目（UNIX 书翻译）的规范全文，已于 2026-10-27（ADR-0001）改写为入口指针。规则正文一律以 `rules/` 为准。

## 规范层级（冲突时上位覆盖下位）

1. **项目宪法** `.specify/memory/constitution.md` —— 零信任、可追溯、单一事实源、流程先行、礼貌抓取、体例即契约。
2. **全局规则** `rules/` —— 宪法的操作性展开，修订走 `rules/adr/`。
3. **工程规格** `specs/<NNN>-*/` —— 单项工程的规格、计划与验收清单。
4. `README.md` —— 面向访客的说明。

## 按任务类型的必读

| 要做什么 | 先读 |
| ---- | ---- |
| 翻译 / 校对词条 | `rules/04-translation-workflow.md`（先建任务 `tools/task_ops.py`，状态机禁止跳步）、`rules/02-style.md`、`rules/03-terminology.md` |
| 改目录 / 标题 / 结构 | `rules/01-repository-structure.md`（SUMMARY.md 唯一数据源；改标题只改 SUMMARY；mu-lu-s.md 为手编分类目录） |
| 提交 / 用工具 / CI | `rules/05-ci-and-tools.md` |
| 修订规则 / 批量与破坏性动作 / 多会话协作 | `rules/06-governance.md` + `rules/adr/` |

## 会话开工五分钟

1. `git log --oneline -5` + `git status`——核对基点；本仓库多会话并行，先确认没有未预期的变动；
2. 通读 `rules/README.md` 的"快速判例"；
3. 跑门禁：`python tools/check_summary.py`、`python tools/check_mulu_s.py`（应 0 退出）；
4. 查进度与任务：`PROGRESS.md`、`python tools/task_ops.py show <slug>`；
5. 收工前：相关检查器复跑、相关文件提交（中文一行信息），不留未提交的半成品。

## 硬约束速览

* **零信任**：既有中文译文一律不作底稿或修改依据；可疑处回原始 HTML（本地 `yuanwen/`、`en/`，不入库）核对；一切成品可回溯到英文源版本钉（pubinfo + 存档版名 + SHA-256）。
* **单一事实源**：结构看 `SUMMARY.md`，术语看 `yi-zhe-shuo-ming.md`，版本看 `baseline/`，任务状态看 `tasks/`；两处不一致时修弱势方。
* **流程先行**：动笔前先有任务记录（`tasks/`）；先登记术语后使用；每步留 `evidence` 凭证。
* **提交纪律**：高频小步提交，中文一行信息；只提交相关文件；直接提交 main；未经用户要求不 push、不 force；提交前核对 HEAD（本仓库多会话并行，见 `rules/06-governance.md`）。
* **抓取礼貌**：相邻 HTTP 请求 ≥5 秒；4xx/5xx/超时退避重试并记录，禁止静默跳过。
* **检查**：本地预检 `python tools/check_style.py`、`python tools/check_summary.py`、`python tools/check_mulu_s.py`；推送后 CI 为最终裁判。

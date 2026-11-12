# AGENTS.md

本文件是 AI 编码代理在本仓库工作的**入口指针**：只放仓库定位、规范层级、按任务必读与硬约束，规则正文一律以 `rules/` 为准。仓库是《斯坦福哲学百科全书》（Stanford Encyclopedia of Philosophy, SEP）简体中文翻译项目：GitBook 格式，辅以本地 VitePress 双语阅读站。

> 历史注记：本文件曾误植另一项目（UNIX 书翻译）的规范全文，2026-10-27（ADR-0001）改写为入口指针。

## 规范层级（冲突时上位覆盖下位）

1. **项目宪法** `.specify/memory/constitution.md`：零信任、可追溯、单一事实源、流程先行、礼貌抓取、体例即契约、知难行易。
2. **全局规则** `rules/`：宪法的操作性展开；修订走 `rules/adr/`（ADR 只追加，取代链完整）；存放位置见 `rules/README.md` 的规则地图。
3. **参考方法论** `rules/reference/`：engineering-doctrine，不具约束力，采纳进 `rules/` 才生效。
4. **工程规格** `specs/<NNN>-*/`：规格、契约（`contracts/cli.md` 职责权属）与执行记录。
5. **访客说明** `README.md`。

## 按任务类型的必读

| 要做什么 | 先读 |
| ---- | ---- |
| 收到新指令、需求含糊 | `rules/08-intent-first.md`：先复述目标、非目标与验收判据，再选手段；含糊先问不猜 |
| 翻译、校对词条 | `rules/04-translation-workflow.md`（任务先行，状态机禁跳步）、`rules/02-style.md`、`rules/03-terminology.md`、`rules/07-academic-norms.md`；工程标准见 `fang-fa-lun/gong-cheng-fang-fa.md` |
| 改目录、标题、结构 | `rules/01-repository-structure.md`：`SUMMARY.md` 唯一数据源；词条为 `<letter>/<slug>.md`（ADR-0009）；`mu-lu-s.md` 为手编分类目录 |
| 接入新词条、更新任务 | `specs/001-sep-sync-pipeline/contracts/cli.md` 职责权属表：`apply-add` 唯一入口；`compare` 产出变更文件后转 update 任务 |
| 提交、用工具、CI | `rules/05-ci-and-tools.md` |
| 修订规则、批量与破坏性动作、多会话协作 | `rules/06-governance.md`、`rules/adr/` |

## 开工与收工

开工（每会话按序做完）：

0. **方向确认**：按 `rules/08-intent-first.md` 复述用户到底要什么，写清目标、非目标与验收判据；含糊先问不猜，禁止猜着做。
1. **基点核对**：`git log --oneline -5`、`git status`；开工先 `python tools/sync_guard.py pull`（判弃自检实拦，ADR-0028），落后不干活。本机定岗见 ADR-0028：M1 只做词条翻译，M2 管其余全部。
2. **读规则地图**：`rules/README.md` 的规则地图与快速判例。
3. **跑门禁**：`python tools/check_all.py`（八项门禁加单元测试，共 9 项，应全绿）。
4. **看进度与任务**：`PROGRESS.md`、`python tools/task_ops.py show <slug>`。

收工：复跑相关检查器；相关文件提交（中文一行信息）；未推送提交清零（ADR-0028）；不留半成品。

## 硬约束速览

| 约束 | 要点 | 权威 |
| ---- | ---- | ---- |
| 知难行易 | 先明确方向与验收判据，再选手段；工具与文档篇幅都不是完成证据 | `rules/08-intent-first.md`、宪法 VII |
| 零信任 | 既有中文译文不作底稿或修改依据；可疑处回 `en/`、`yuanwen/` 核对；成品可回溯到英文源版本钉（pubinfo、存档版名、SHA-256） | 宪法、ADR-0027 |
| 主代理单干 | 禁止调用子代理（`Agent`、`Task` 及 workflow 扇出）；唯一例外是用户当轮显式批准并写明范围 | ADR-0034 |
| 单一事实源 | 结构 `SUMMARY.md`、术语 `shu-yu-biao.md`、人名 `ren-ming-biao.md`、版本 `baseline/`、任务 `tasks/`；不一致时修弱势方 | ADR-0012、ADR-0036 |
| 流程先行 | 动笔前先建任务；先登记术语后使用；每步留 `evidence` | `rules/04`、`rules/03` |
| 提交纪律 | 小步提交、中文一行信息、只提交相关文件、直接提交 main；未经要求不 push、不 force；推送前先 pull --rebase；积压线途中不超过 1 条、收工清零 | `rules/06`、ADR-0026、ADR-0028 |
| 抓取礼貌 | 相邻请求至少间隔 5 秒；4xx、5xx、超时退避重试并记录，禁止静默跳过 | `rules/05` |
| 抓取完整性 | 词条包内被引用资产必须齐备；`tools/fetch_audit.py` 闭包迭代至不动点，缺件自动补抓 | `tools/fetch_audit.py` |
| 更新流程 | `fetch_catalog` 检测漂移，`compare.py` 产出变更文件，转 update 任务（`changes:`），三校走变更段 | `specs/001-sep-sync-pipeline/contracts/cli.md` |
| 结构形态 | 词条 `<letter>/<slug>.md`，别名链目标、导航链 README；`yuanwen/<letter>/<slug>.md` 镜像逐字符一致 | `rules/01`、ADR-0009 |
| 单体文件 | 叙事、规则、规格类 md 超 1000 行或 100 KB 必须按文件夹拆分（登记册与生成物豁免） | ADR-0004、`check_doc_size.py` |
| 根目录白名单 | 根层只放白名单条目；散件归 `script/`（本地）、`state/`（运行态）或 `specs/<NNN>-*/` 的 `bin`、`results` 子目录；新增根级条目走 ADR | ADR-0023、`check_junk.py` |
| 批量改写 | 写回前置门（残余不为 0 禁止写回）、幂等、逐行身份追踪、改写前强制基线还原 | `rules/05` |
| 检查 | `check_all.py`（9 项，`--all` 为 11 项）；定点 `check_academic.py --docs <路径> --strict`；推送后 CI 为最终裁判 | `rules/05` |

## 现状与进度

阶段、计数与主战场一律看 `PROGRESS.md`（`tools/progress.py` 生成）与 `specs/005-translation-campaign/session-handoff.md`（开工卡：status、next、claim）；**本文件不复制数字**（ADR-0015）。多机定岗与同步协议（各持独立克隆、只经 `origin/main` 同步）见 `rules/06-governance.md` 的多机并行一节。

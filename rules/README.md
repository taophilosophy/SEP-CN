# 规则目录

本目录是 SEP-CN（斯坦福哲学百科全书简体中文版）全局规则的唯一存放处。任何体例、结构、流程、治理问题，先查这里。

## 规范层级

发生冲突时，按以下优先级裁决（上位覆盖下位）：

1. **项目宪法** `.specify/memory/constitution.md` —— 六项核心原则（零信任、可追溯、单一事实源、流程先行、礼貌抓取、体例即契约）。修订须在提交信息中注明“修订宪法 vX.Y”并说明理由。
2. **本目录规则** `rules/` —— 宪法的操作性展开。修订须走 ADR（见 `rules/adr/`）。
3. **各 feature 规格** `specs/<NNN>-*/` —— 某项工程的规格、计划与验收清单，只约束该 feature。
4. **README.md** —— 面向访客的项目说明，不承载规则。

## 规则索引

| 文件 | 内容 | 约束对象 |
| ---- | ---- | -------- |
| [01-repository-structure.md](01-repository-structure.md) | 仓库结构、目录职责、命名、SUMMARY 与分类目录、单体文件治理 | 全部贡献者 |
| [02-style.md](02-style.md) | 编写体例：引号、空格、代码块、表格、图片 | 译文与说明页 |
| [03-terminology.md](03-terminology.md) | 术语治理：登记册与发布词汇表的关系、登记流程 | 译文 |
| [04-translation-workflow.md](04-translation-workflow.md) | 翻译与三审三校流程、任务联动、重译纪律 | 翻译与校对会话 |
| [05-ci-and-tools.md](05-ci-and-tools.md) | CI 工作流约定、本地工具清单、提交策略 | 全部会话 |
| [06-governance.md](06-governance.md) | 软件工程治理：单一事实源登记表、变更管理、并发会话纪律、质量门 | 全部会话 |
| [07-academic-norms.md](07-academic-norms.md) | 哲学学术规范：版本事实、引文文献、禁幻觉引文、结构完整、译注、审校挂钩 | 译文与校对会话 |

## 规则地图（统一规范化存储，2026-10-27 分门别类）

每一类流程规则/文档有唯一存放位置；新增内容先归入对应类别，不散落。

| 类别 | 存放位置 | 内容 | 权属 |
| ---- | ---- | ---- | ---- |
| 宪法 | `.specify/memory/constitution.md` | 最高原则 | 治理会话 |
| 约束性规则 | `rules/01-07` + `rules/adr/`（决策记录）；单文件超 300 行/30KB 按主题拆为 `rules/0X/` 目录 | 可执行条文 + ADR 决策史 | 治理会话（修订走 ADR） |
| 参考方法论 | `rules/reference/`（[engineering-doctrine](reference/engineering-doctrine/README.md)：G0-G5 门禁、32 条总纲、FR/NFR、交付清单） | 方法论基线，**不具约束力**，采纳进 rules/ 才生效 | 全体可读 |
| 站点实现文档 | [`.vitepress/README.md`](../.vitepress/README.md) | 阅读站构建、主题、搜索、双语配对的实现说明（**非规则**，冲突以 rules/ 为准；ADR-0015） | 站点会话 |
| 工程规格 | `specs/<NNN>-*/spec.md`（+ plan/tasks/checklist）——含 [specs/005 全流程翻译与债务偿还规划书](../specs/005-translation-campaign/spec.md) | 单项工程规格与验收 | 该工程会话 |
| 管线契约 | `specs/<NNN>-*/contracts/cli.md` | 工具职责权属、CLI 行为 | 该工程会话 |
| 执行记录 | `specs/<NNN>-*/execution-log.md`（+ demo-log、分析记录） | 干执行凭证与流程修订输入 | 该工程会话 |
| 散页标准 | `fang-fa-lun/gong-cheng-fang-fa.md`（翻译工程标准 v1.0）等 | 各会话产出的操作性标准，**待逐步折叠进 rules/**，折叠前以本表登记为准 | 原产出会话 |
| 任务状态 | `tasks/<slug>.json` | 翻译/更新任务 | 对应会话 |
| 进度汇总 | `PROGRESS.md`（生成物，不手改） | `tools/progress.py` 输出 | 管线 |

> 生成物不承载规则：`PROGRESS.md`、Qoder 仓库 Wiki（`.qoder/repowiki`，2026-10-28 折叠退役，ADR-0015）均非事实源；与它们冲突时以本目录与 `specs/` 为准。

## 快速判例

* 改标题 → 只改 `SUMMARY.md`，文件 H1 交由 CI 同步（[01](01-repository-structure.md)）。
* 新术语 → 先登记 `yi-zhe-shuo-ming.md`，再使用（[03](03-terminology.md)）。
* 动手翻译 → 先建/查任务 `tasks/`，按状态机推进，禁止跳步（[04](04-translation-workflow.md)）。
* 引号、空格、表格格式 → 按 [02](02-style.md)，机器可判部分用 `tools/check_style.py` 预检。
* 学术规范（参考文献/译注/版本事实）→ 按 [07](07-academic-norms.md)，定点 `tools/check_academic.py --docs <路径> --strict`；收工前 `python tools/check_all.py` 一键全量。
* 推送 → 先 `git pull --rebase`，被拒不硬推；force push 属用户授权期专属（[06](06-governance.md)）。
* 批量或破坏性动作 → 先满足宪法附加约束（可信基线 + 可回溯），见 [06](06-governance.md)。
* 单体文档超 1000 行或 100KB → 按文件夹拆分（登记册与生成物豁免），见 [01](01-repository-structure.md) 与 ADR-0004。
* 改站点构建 / 主题 / 搜索 → 先读 [`.vitepress/README.md`](../.vitepress/README.md)；命令与门禁口径仍以 [05](05-ci-and-tools.md) 为准。

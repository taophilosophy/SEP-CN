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
| [01-repository-structure.md](01-repository-structure.md) | 仓库结构、目录职责、命名、SUMMARY 与分类目录 | 全部贡献者 |
| [02-style.md](02-style.md) | 编写体例：引号、空格、代码块、表格、图片 | 译文与说明页 |
| [03-terminology.md](03-terminology.md) | 术语治理：登记册与发布词汇表的关系、登记流程 | 译文 |
| [04-translation-workflow.md](04-translation-workflow.md) | 翻译与三审三校流程、任务联动、重译纪律 | 翻译与校对会话 |
| [05-ci-and-tools.md](05-ci-and-tools.md) | CI 工作流约定、本地工具清单、提交策略 | 全部会话 |
| [06-governance.md](06-governance.md) | 软件工程治理：单一事实源登记表、变更管理、并发会话纪律、质量门 | 全部会话 |

## 快速判例

* 改标题 → 只改 `SUMMARY.md`，文件 H1 交由 CI 同步（[01](01-repository-structure.md)）。
* 新术语 → 先登记 `yi-zhe-shuo-ming.md`，再使用（[03](03-terminology.md)）。
* 动手翻译 → 先建/查任务 `tasks/`，按状态机推进，禁止跳步（[04](04-translation-workflow.md)）。
* 引号、空格、表格格式 → 按 [02](02-style.md)，机器可判部分用 `tools/check_style.py` 预检。
* 批量或破坏性动作 → 先满足宪法附加约束（可信基线 + 可回溯），见 [06](06-governance.md)。

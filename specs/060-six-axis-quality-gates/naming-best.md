# 节点标识与命名：不计成本最优方案

> 与 `naming-proposal.md`（成本约束案：四段式直改）并列；本文件是不计成本案，主推。
> 交付物类型：评估类（结论＋建议，不含实施）。实施须另立卡。

## 1 结论

**三层分离**：稳定标识符（identifier）＋可演进名称（name）＋展示标签（label）；状态名改为 `<identifier>_checked`，与名称彻底解耦。历史 journal 与 `tasks.steps` 原样保留为事实，`tasks.state` 作为视图迁移并由 journal 重放校验 100%。

这不是“为了标准而复杂化”，而是因为项目已经具备了实施它的两个前提：

1. **状态是视图**：ADR-0068 明定“日志为事实，状态为视图”，`journal_view.stage_done` 已能从日志折叠出已 pass 节点集——状态可重建，因此可安全改名。
2. **记录不可篡改**：journal 1199 个文件、4276 个 node 事件，`tasks.steps` 是过程证据链——它们**不改写**，靠别名解析。改名风险因此不落在历史数据上。

## 2 标准依据

| 标准 | 状态 | 要求 |
| ---- | ---- | ---- |
| ISO/IEC 11179-5:2015 | 现行（2020 复审确认；第 4 版 DIS 在投票，发布后重核条款） | **标识（identifier）与名称（name）分离**：标识唯一、稳定、不可复用；名称可演进，命名约定须成文 |
| GB/T 18391.5-2009 | 现行（等同采用 11179-5:2005；2022-01-10 复审继续有效） | 同上（中文采标） |
| ISO 15489-1:2016 / GB/T 26162-2021 | 现行 | 记录不可篡改、可追溯 |
| ISO/IEC/IEEE 12207:2017 | 现行 | 配置标识唯一且稳定 |

现行命名把 identifier 与 name 合成一个字符串（`s2.4`、`global`、`S3`），于是“改语义名”就等于“改标识”，这是全部麻烦的根源。

## 3 三层模型

| 层 | 内容 | 可变性 | 例 |
| ---- | ---- | ---- | ---- |
| identifier | 段缩写＋两位序号 | **永不变、永不复用** | `rv-03` |
| name | `<段>.<阶段>`，全小写 kebab | 可演进，带 `name_version` | `review.cite` |
| label | 中文展示名 | 可翻译 | 引文锁定 |
| state | `<identifier>_checked` | 随 identifier 固定 | `rv-03_checked` |

段缩写 `ex`／`tr`／`rv`／`sg` 只是助记，不承载语义：即使将来段重组，identifier 也不变。

## 4 22 个标识符分配（含预留）

| identifier | name | label | state | object_class |
| ---- | ---- | ---- | ---- | ---- |
| ex-01 | extract.fetch | 抓取与版本钉 | — | source |
| ex-02 | extract.convert | HTML 转 Markdown | — | conversion |
| ex-03 | extract.fidelity | 转换保真校验 | — | conversion |
| ex-04 | extract.source-audit | 源完整性审计 | ex-04_checked | source |
| ex-05 | extract.format | 镜像格式闭合 | — | — |
| tr-01 | translate.preprocess | 译前预处理 | — | term |
| tr-02 | translate.draft | 初译 | tr-02_checked | — |
| tr-03 | translate.accuracy | 准确性校（一校） | tr-03_checked | consistency |
| tr-04 | translate.fluency | 行文通顺校（二校） | tr-04_checked | grammar |
| tr-05 | translate.format | 中文段内格式闭合 | — | — |
| rv-01 | review.terminology | 术语与勘误锁定 | rv-01_checked | term |
| rv-02 | review.consistency | 全局一致性 | rv-02_checked | 多域（提示） |
| rv-03 | review.cite | 引文锁定 | rv-03_checked | cite |
| rv-04 | review.logic | 逻辑一致性 | rv-04_checked | logic |
| rv-05 | review.grammar | 语法 | rv-05_checked | grammar |
| rv-06 | review.register | 语域 | rv-06_checked | register |
| rv-07 | review.measure | 计量 | rv-07_checked | measure |
| rv-08 | review.punctuation | 标点 | rv-08_checked | punct |
| rv-09 | review.style | 体例终校 | rv-09_checked | format |
| sg-01 | signoff.verity | 受众适切性 | sg-01_checked | review |
| sg-02 | signoff.coherence | 连贯性 | sg-02_checked | review |
| sg-03 | signoff.acceptance | 交付验收 | sg-03_checked | aggregate |

**预留**：`ex-06…09`、`tr-06…09`、`rv-10…19`、`sg-04…09`。新节点只追加，不插队、不复用。

## 5 状态名统一

旧状态有四种后缀（`drafted`、`_checked`、`_termchecked`、`_reviewed`），是历史偶然。统一为 `_checked`：

| 旧 state | 新 state |
| ---- | ---- |
| `drafted` | `tr-02_checked` |
| `s0_source_checked` | `ex-04_checked` |
| `s1_checked` / `s2_checked` | `tr-03_checked` / `tr-04_checked` |
| `s2.4_termchecked` / `s2.5_checked` | `rv-01_checked` / `rv-02_checked` |
| `q1…q6_*` | `rv-03…08_checked` |
| `s3_checked` | `rv-09_checked` |
| `r1…r3_reviewed` | `sg-01…03_checked` |
| `pending`／`cleared`／`done` | 保留（非节点状态） |

收益：后缀单一、机器可判；“reviewed 与 checked 的差别”不再是隐含语义。

## 6 迁移：三层各归其位

| 数据 | 量 | 处置 | 理由 |
| ---- | ---- | ---- | ---- |
| journal `node` 值 | 4276 事件／1199 文件 | **不改**；`alias` v1→identifier 解析 | 记录不可篡改 |
| `tasks.steps[].step`（历史证据） | 全量 | **不改**；读取时 alias 归一 | 证据链不可篡改 |
| `tasks.state`（视图） | 1200 条 | 迁移为 identifier 形式，**journal 重放校验 100%** | ADR-0068 状态为视图 |
| 命令行短名（`s0/s24/s25/s3/r1…`） | — | 保留为输入别名，内部转 identifier | 不动肌肉记忆 |
| 文档引用 | 约 1033 处 | 双列写法（identifier＋name），脚本替换＋人工核 10 处高风险 | 可读性 |

## 7 重放校验（本方案的核心，不可省）

新增 `tools/replay_state.py`：从 journal 事件折叠每个任务的 state（`alias → identifier`；`pass`／`fail`／`clear`／`reopen`／`done`），与 `tasks.state` 逐条比对。

验收：1200/1200 一致；任一条不一致即停并归因（R1 视图错误 / R2 写入脱核 / R3 基准漂移）。

没有这一步，改名就是“把视图改坏而无法发现”；有了这一步，改名变成可证伪的工程。

## 8 落地顺序（一次性，可整体回退）

1. 建 `rules/naming.json`：identifier／name／name_version／label／state／alias／object_class 七列单一事实源。
2. `pipeline.json` 以 identifier 作 `id`；`criteria_owner` 同步。
3. `journal_lib` 加 alias 解析（读旧、写新）；`step_to_event` 写 identifier。
4. `tasks.state` 迁移脚本：先备份、幂等、逐条报告；迁移后用 `replay_state.py` 校验。
5. 文档双列改写（脚本＋人工核）。
6. `check_stages` 增 S7：identifier 唯一且匹配 `^(ex|tr|rv|sg)-\d{2}$`、预留号段不越界、name 版本非空、alias 可解析、state 与 identifier 对应。
7. 一次性提交；回退 = `git revert` 该提交，并从 journal 重建 state。

## 9 与“四段式直改”案的差别

| 维度 | 四段式直改（`naming-proposal.md`） | 三层（本方案） |
| ---- | ---- | ---- |
| 改名成本 | 每次改名动约 1033 处文档与 1200 条 state | 只改 name／label，标识与 state 不动 |
| 旧名复用冲突 | 靠“永不复用”人工纪律 | 标识天然不复用 |
| 状态语义 | 随名称走，改名即改状态 | 与名称解耦 |
| 复杂度 | 低 | 中：多一张表＋一个重放器 |
| 标准符合度 | 部分 | 完全（identifier／name 分离） |

## 10 唯一可以不采纳的条件

若判定 22 节点的语义**永久冻结**、将来只增不改，则三层的主要收益（改名零成本）为零，四段式直改＋alias 足够。这是本方案唯一的退出条件；除此之外，“不计成本”下应按标准做三层。

## 11 证据

* journal：1199 文件、4276 个 node 事件，distinct node 值仅 10 个（S3 457、draft 447、s1 439、s2 439、R1 430、s0 429、R2 425、s2.4 407、R3 406、global 397）；q1–q6 为 0 事件（新节点接入后尚未推进任务）。
* tasks：1200 条（pending 619、s2.4_termchecked 408、cleared 146、drafted 16、s0_source_checked 5、s2.5_checked 3、r2_reviewed 3），另有 `tasks/manifests/` 95 个非条目文件（无 state，不参与迁移）。
* 文档引用：约 1033 处（rules 与 specs/060）。
* 状态可重建：`journal_view.stage_done` 已实现日志折叠；`rules/journal-schema.json` 的 `derived_views` 明列“stage_done／saturate／stale／attempt”。

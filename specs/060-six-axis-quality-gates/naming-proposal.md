# 节点命名规范建议（22 节点）

> 交付物类型：评估类（结论＋建议，不含实施，rules/08 §14）。
> **状态：已由不计成本案取代并落地**（2026-11-25）：最终采用 identifier／name／state 三层（本文件 B1＋B2 的对象保留，状态名改由 identifier 派生），见 `naming-best.md` 与 ADR-0080；本文件留作成本约束案的备查记录。

## 1 结论

现命名不满足“唯一、无歧义、成文约定”三项基本要求，也不满足本项目自己的 S6 对象域登记（id 与对象域无对应）。建议分两期：

* **B1（零风险，立即可做）**：建立 `rules/naming.json` 单一事实源（id／label／state／object_class／alias 五列），规范 label，`check_stages` 增 S7 命名词表校验。不改 id、不改状态名、不动历史 journal。
* **B2（一次性，需批准）**：按 §4 映射表重命名节点 id，历史 journal 靠 `node_alias` 解析（只追加不改写，P5），状态名保持不动（1200 条任务零迁移）。

不建议彻底重命名状态名：1199 个 journal 文件共 4276 个 node 事件不可改写，1200 条任务 JSON 全量迁移风险大于收益。

## 2 标准依据

| 标准 | 状态 | 要求 |
| ---- | ---- | ---- |
| ISO/IEC 11179-5:2015（第 3 版） | 现行（2020 复审确认；第 4 版 DIS 在投票，发布后重核） | 命名与标识原则：标识唯一、命名约定须成文、名称须无歧义且可解析 |
| GB/T 18391.5-2009 | 现行（等同采用 ISO/IEC 11179-5:2005；2022-01-10 复审继续有效） | 同上（中文采标） |
| ISO/IEC/IEEE 12207:2017 | 现行 | 配置标识：配置项须有唯一、稳定的标识符 |

## 3 现状违例（逐条，带证据）

| # | 违例 | 证据 |
| ---- | ---- | ---- |
| V1 | 同一前缀两种语义 | `P1–P3` 是转换管线，`P4` 是中文预处理（stage） |
| V2 | 大小写混用 | `S3` 大写，`s0/s1/s2/s2.4` 小写；`R1–R3` 大写，`q1–q6` 小写 |
| V3 | 一实体三名且不互推 | 节点 `global` ↔ 状态 `s2.5_checked`；节点 `S3` ↔ 状态 `s3_checked`；节点 `s2.4` ↔ 状态 `s2.4_termchecked` |
| V4 | 编号序列断裂 | s0、s1、s2、s2.4、s3（小数为历史插入）；q1–q6 另起一段 |
| V5 | 唯一无前缀节点 | `draft` 与全表风格不符 |
| V6 | 单字母前缀不可自解释 | P／F／q／R 须查表；违反“名称无歧义” |
| V7 | id 与对象域无对应 | `global` 的 object_class 有 4 个域（academic／consistency／format／punct），名字看不出 |

另：节点 id 与 state 分离是历史合理设计（ADR-0068 零迁移），但缺少一张把两者对齐的登记表，导致 V3。

## 4 命名规则草案

1. **语法**：`<seg>.<phase>`，全小写 ASCII；`seg` 限 `extract`／`translate`／`review`／`signoff` 四值，`phase` 用 kebab-case。
2. **唯一**：id 全局唯一，永不复用（ISO/IEC 11179-5）。
3. **稳定**：已发布 id 不得改义；改名走 `node_alias` 追加，不删除旧项。
4. **自解释**：id 不依赖查表；缩写限标准词（draft、audit、format、style）。
5. **四元登记**：id、label、state、object_class 必须同表登记；state 与 id 不要求同形，但必须可互推（消除 V3）。
6. **禁用**：大小写混用、小数编号、裸单词作 id、seg 与 phase 之外的第三层。

## 5 映射表（建议）

| 现 id | 建议 id | label（规范） | state（不动） | object_class |
| ---- | ---- | ---- | ---- | ---- |
| P1 | extract.fetch | 抓取与版本钉 | — | source |
| P2 | extract.convert | HTML 转 Markdown | — | conversion |
| P3 | extract.fidelity | 转换保真校验 | — | conversion |
| s0 | extract.source-audit | 源完整性审计 | s0_source_checked | source |
| F1 | extract.format | 镜像格式闭合 | — | — |
| P4 | translate.preprocess | 译前预处理 | — | term |
| draft | translate.draft | 初译 | drafted | — |
| s1 | translate.accuracy | 准确性校（一校） | s1_checked | consistency |
| s2 | translate.fluency | 行文通顺校（二校） | s2_checked | grammar |
| F2 | translate.format | 中文段内格式闭合 | — | — |
| s2.4 | review.terminology | 术语与勘误锁定 | s2.4_termchecked | term |
| global | review.consistency | 全局一致性 | s2.5_checked | 多域（提示） |
| q1 | review.cite | 引文锁定 | q1_cite_checked | cite |
| q2 | review.logic | 逻辑一致性 | q2_logic_checked | logic |
| q3 | review.grammar | 语法 | q3_grammar_checked | grammar |
| q4 | review.register | 语域 | q4_register_checked | register |
| q5 | review.measure | 计量 | q5_measure_checked | measure |
| q6 | review.punctuation | 标点 | q6_punct_checked | punct |
| S3 | review.style | 体例终校 | s3_checked | format |
| R1 | signoff.verity | 受众适切性 | r1_reviewed | review |
| R2 | signoff.coherence | 连贯性 | r2_reviewed | review |
| R3 | signoff.acceptance | 交付验收 | r3_reviewed | aggregate |

计数：extract 5 ＋ translate 5 ＋ review 9 ＋ signoff 3 = 22。

要点：`q1–q6` 归入 `review.*` 而非另设 `axis.*`，因为六轴属 seg3；“轴”的区分已由 `object_class` 承担，不再造新前缀。

## 6 迁移影响

| 层 | 量 | 处置 |
| ---- | ---- | ---- |
| 节点 id（pipeline／criteria_owner／journal 解析） | 22 个 | 脚本重命名＋`node_alias` 表 |
| 历史 journal node 值 | 4276 事件（S3 457、draft 447、s1 439、s2 439、R1 430、s0 429、R2 425、s2.4 407、R3 406、global 397） | **不改写**，读取时经 alias 归一 |
| 任务 state | 1200 条 | **不改**（state 名保留） |
| 文档引用 | 约 1033 处（rules 与 specs/060） | 脚本幂等替换＋人工核对 10 处高风险（表格与代码块） |
| 命令行短名 | `s0/s24/s25/s3/r1–r3` | 保留为别名，不动 |

**回退**：id 重命名集中在一次提交，`git revert` 可整体回退；alias 表为纯追加，删除即恢复旧解析。

## 7 验收判据（实施时）

1. S7 命名词表校验：id 符合 `^[a-z]+(\.[a-z0-9-]+)+$`，四值前缀，label 非空，state 在 ORDER 内，alias 可解析。
2. `check_stages` 全绿（S1–S7）；`python -m unittest discover` 全绿。
3. 旧 id 在规则与规格文档中零残留（`grep` 除外 alias 表与历史记录）。
4. `journal_view.py` 对旧事件仍可解析（alias 生效）。

## 8 不建议

* **彻底重命名状态名**（`s2.5_checked`→`review.consistency`）：journal 不可改写，只能 alias；tasks 全量迁移会制造新的回退风险，收益仅是“名字好看”。
* **引入数字段号**（`1.1`、`2.3`）：与 rules/04 的小节编号混淆，且顺序变化即改号，违反稳定性。
* **保留现状只改 label**：治标不治本，V1–V7 仍在。

# B0+B1 全库遍历对账（1,872 词条，2026-11-18）

**性质**：只读审计记录｜**边界**：不写 `en/`、不改 `yuanwen/`、不产译文（ADR-0072 决策 1）
**判定器**：`bin/verify_b0b1.py`（B0 十谓词 + B1 双不变量）｜**扫描器**：`bin/b0b1_scan_all.py`（schema v3）
**机读产物**：`results/b0b1-scan-all.json`｜**复算命令**：`python -I specs/044-b0b1-baseline/bin/b0b1_scan_all.py`

## 1. 求值视图（决定结论成立与否的前提）

| 判据 | 视图 | 同源对象 |
| ---- | ---- | ---- |
| B0 十谓词 | 转换输入 `en ⊕ patches` | `yuanwen.convert_entry`（先补丁后解析） |
| B1·I2 重放等值 | 转换输入（登记 `source_sha256`） | 同上 |
| B1·I3 词元流 | 转换输入（`html_text(apply_patches=True)`） | 同上 |

补丁池 × B0 交集验证（`bin/verify_patch_intersection.py`，产物 `patch-intersection.json`）：3 条补丁件 HTML 均实际改动、**B0 前后皆通过**——交集为空。含义是：本池补丁全为格式层（缺空格类），B0 不判空格，故"补丁是否影响 B0"无数据可证，视图正确性只能靠代码同源对照保证（ADR-0073 同源对照条）。

## 2. 全量结果

| 项 | 数值 |
| ---- | ---- |
| 词条总数 | 1,872 |
| B0 与 B1 双过 | **1,816** |
| B0 失败 | **9** |
| B1 失败 | **47** |
| asym 判据不适用 | **320** |
| 无 en 快照 | 0 |

## 3. 四态对账（对账律，doctrine 10 / ADR-0073 决策 4）

| 态 | B0 | B1 | 含义 |
| ---- | ---- | ---- | ---- |
| `known-errata`（确证疏漏） | 8 | 3 | `en-errata.md` 已登记、参考读法已定 |
| `known-errata-ambiguity`（登记待裁定） | 1 | 0 | 登记在案但性质为判据歧义，"登记"≠"缺陷成立" |
| `known-converter`（转换器账） | 0 | 44 | `specs/039` 已逐件定性 |
| `new`（两账皆无） | **0** | **0** | — |
| 合计 | 9 | 47 | 账本闭合（扫描器退出码 0） |

### 3.1 B0 失败 9 件（逐件）

| slug | 失败谓词 | 态 | 载于 |
| ---- | ---- | ---- | ---- |
| common-knowledge | math_delim | known-errata | en-errata §十 |
| discourse-representation-theory | math_delim | known-errata | §十 |
| phil-bio-latin-america | math_delim | known-errata | §十（`]→\)` 误植） |
| ramsey | math_delim | known-errata | §十（`\)(R\)` 错位） |
| typelogical-grammar | math_delim | known-errata | §十（`<em>` 与定界符交错） |
| epistemic-game | math_brace | known-errata | §十（`\text{}` 内嵌 `\(`） |
| goedel | math_brace | known-errata | §十（`2^{\kappa\)`、`\(+}`） |
| logic-propositional | math_brace | known-errata | §十（`\AxiomC{...\)`） |
| **questions** | math_delim | **known-errata-ambiguity** | §十（`\\(` 为换行命令＋字面括号，疑似合法） |

### 3.2 B1 失败 47 件

- `known-errata` 3：`emerson`、`leibniz-ethics`、`publichealth-ethics`（上游文字层，`pin_bad` 全为 False，即非手改/非漂移）；
- `known-converter` 44：全部命中 `specs/039` 的 `text-stream-diff` 账（三族转换器缺陷已修 + 白名单合法移位 + ≤30 字母零星差异）。

**交集证明**：B1 失败集 ∩ 039 `text-stream-diff` = **47**；`仅 B1` 为空、`仅 039` 为空——双向差集皆空，故 B1 失败面与 039 定性面**完全重合**。

## 4. asym 面的分层核对（勿混读两个 320 与 273）

`specs/039` 报告的 `math_asymmetric = 320` 是"判据不适用"**总面**（只存计数）；其 `issues` 里的 `math-asymmetric-diff = 273` 是其中有可报字母差的**子集**。本轮扫描按三层核对：

| 层 | 扫描 | 039 账 | 结论 |
| ---- | ---- | ---- | ---- |
| 总面（判据不适用） | 320 | 320 | 计数一致 |
| diff 面（有字母差可报） | 273 | 273 | 集合一致，双向差集空 |
| 残差面（两侧跨度对称、无差可报） | 47 | 由总数推得 | 320 = 273 + 47 |

若直接用 273 与 320 求差集，会把 47 件读成"仅扫描有"的伪新增——这是本轮修正的一处口径错误（见 §6）。

## 5. 待裁定事项（唯一一件）

`questions` 是本轮**唯一同时落在两个"未验证"面**的词条：

| 信号 | 实测 | 性质 |
| ---- | ---- | ---- |
| B0 `math_delim` | 上游正文 `\(C\in X\)\\(\{P\}\)` 中 `\\(` 为 LaTeX 换行命令＋字面 `(` | 判据歧义（负向后顾可排除开界符，但其配对 `\)` 前为 `}`，无法对称排除） |
| B1 I3 | md 侧 spans 353 / oversize 1 / unclosed 1，与 html 侧 367 不对称 → 判据不适用 | 未验证 |

**已排除"真实丢文"**：逐节词覆盖度实测——Preliminaries / semantics / Why-questions / Embedded / Bibliography / Academic Tools / Other Internet Resources / Related Entries **八节全部 1.00**；朴素口径字母量 md/html = 1.04（md 反而略多）。故缺口是两侧定界符体系不同（html `\(...\)` vs md `$...$`）产生的口径差，非内容缺失。

**裁定需求**：该处 `\\(` 在 MathJax 下的渲染语义（换行后接括号）是否合法。合法则 B0 应予豁免并调判据；不合法则入勘误表补登记。两者皆不动 `en/`（冻结）。

## 6. 本轮修正的三处缺陷

| # | 缺陷 | 影响 | 修法 |
| ---- | ---- | ---- | ---- |
| 1 | 扫描器只 join `en-errata.md`，未 join 039 转换器账 | 首跑报 `B1 new = 44`，把已定性项当新发现 | join 两账，四态归类，未对账集为空才退出 0 |
| 2 | `iter_entries` 只枚举 `a-z` 单字母目录 | 漏 `yuanwen/1/`，`18thGerman-preKant` 报 "no yuanwen md"（假失败） | 目录名接受单数字；补 4 项回归单测并以"注入旧谓词→测试红"验证可证伪 |
| 3 | `b1_ok` 的 `asym` 为 `or` 链，命中计数时返回 int（个别件为 `2`） | 机读字段 `token_asym` 类型混杂，消费方按 `== True` 比较会漏判 | 显式 `bool()`；终跑 1,872 件全为 bool |

另：`check_yuanwen_fidelity --gate` 全量复跑（`html_text` 改动后）**1,872 件受检、`issue_total 0`**——此前仅抽样 100 件。

## 7. 结论与边界

**结论**：全库 B0/B1 的失败面**全部可归属既有账本，新发现为 0**。这确认了 `specs/039` 对 47 件的定性覆盖完整，也确认 9 件 B0 失败皆为已在案的量。

**边界（不得越读）**：

1. "0 新发现"不等于"已验证"。B0 判的是形式可解析、不判内容对（ADR-0070 附录盲区 1–5）；B1·I2 是自证（转换器 bug 两边都错则不见）。
2. **320 件 asym 属未验证面**，不是通过面；本轮只做了分层核对与一件抽查（§5）。
3. 未覆盖：`notes.html` 的补丁面（当前池无 notes 补丁）、`no-baseline` 2 件孤儿镜像（`health-well-being-personal-relationships`、`on-utopia`，库存异常待裁定，specs/039 §四）。

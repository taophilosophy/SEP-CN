# T186 评审记录：rv-04 q2 逻辑一致性（habermas）

- 任务：T186（T138 六轴第二轴）；日期：2026-11-27；actor：trae-main
- 依据：`rules/04` §六轴（ADR-0079）、`specs/060-six-axis-quality-gates/checklists/q2-logic.md`（L-1…L-12）
- 写域：`h/habermas.md`（2 处 L-6 修正）；骨架：`state/axis/habermas.logic.jsonl`（运行态）

## 1 规模与方法

| 项 | 数 |
| ---- | ---- |
| 散句（骨架行） | 907 |
| 逻辑承载句（含强算子或 ≥4 逗号/分号） | 235 |
| 非承载句（trivial） | 672 |
| 机检算子配对候选 | 30（另 1 条节块数不一致，跳过配对） |
| 人审定性的候选 | 30 |
| 真缺陷（Major，L-6 模态强度） | 2 |
| Critical / L-12 病句逻辑类 | 0 |

方法：`logic_audit --init` 生成逐句骨架；按节、按段落块做中英算子配对（all/some/no/not/if/unless/must/should/may）；候选逐条回源核对；非候选承载句按块级配对结果记 `equivalent`。**本轮是候选级逻辑筛查，不是逐句全文形式化**；`props` 仅对 2 处发现填写（见 §3），其余留空，全文形式化另批。

## 2 候选逐条定性（30 条）

| # | 算子 | 位置（节/块） | 结论 | 理由 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | all | 1 Biography / 19 | 误报 | `above all` 是习语“首先”，非全称量词；中译“首先是政府的行动”正确 |
| 2 | all | 1 Biography / 25 | 误报 | `almost all`→“几乎全是”，`above all`→“尤其是”；无 all→most 漂移 |
| 3 | no | 1 Biography / 31 | 误报 | `no longer`→“不再”，ZH 表未收“不再” |
| 4 | must | 1 Biography / 33 | 误报 | `must stop`→“必定止于”，逻辑必然性保留 |
| 5 | may | 1 Biography / 49 | 误报 | `how can…`→“如何让…”；`may have`→“可能” |
| 6 | if | 3 Discourse Ethics / 16 | 误报 | `if only implicitly`→“哪怕只是隐含地”；`if…is to`→“若要…就必须” |
| 7 | may | 3 Discourse Ethics / 38 | 误报 | `No speaker may be prevented`→“任何言说者都不得…被阻止”，禁则等价 |
| 8 | no | 3 Discourse Ethics / 44 | 误报 | `no such…`→“不认为这样的…会”，否定辖域未变 |
| 9 | may | 3 Discourse Ethics / 70 | 误报 | `can be impartially grounded`→“得以…得到根据” |
| 10 | all | 3 Discourse Ethics / 100 | 误报 | `all affected`→“所有相关者”；`all but disappeared`→“几乎已经消失”；`every`→“每一位” |
| 11 | should | 4 Between Facts and Norms / 15 | 误报 | `works as it should`→“正常运转”，规范预期保留 |
| 12 | all | 4 Between Facts and Norms / 17 | 误报 | 权利清单块；`all` 命中原句无量化对象，中译无漏 |
| 13 | if | 4 Between Facts and Norms / 17 | 误报 | `insofar as`→“只要”，条件关系保留 |
| 14 | if | 4 Between Facts and Norms / 21 | 误报 | `if it is to facilitate`→“要促进…就必须”，条件方向正确 |
| 15 | must | 4 Between Facts and Norms / 45 | 误报 | `must harmonize`→“必须…相协调”；`must not`→“不得” |
| 16 | all | 4 Between Facts and Norms / 57 | 误报 | `all` 为块级噪声；中译权利清单无量化丢失 |
| 17 | must | 4 Between Facts and Norms / 57 | 误报 | `must grant`→“必须相互授予”；`must be interpreted`→“须…解释” |
| 18 | no | 5 Methodology / 29 | 误报 | `no longer claims`→“不再声称” |
| 19 | no | 5 Methodology / 46 | 误报 | `no transcendent point`→“没有…超验阿基米德点”；`no longer`→“不再” |
| 20 | if | 6 Constitutional Patriotism / 21 | 误报 | `If…`→“如果”；`even if`→“即便”；`If not`→“如果不是” |
| 21 | no | 6 Constitutional Patriotism / 33 | 误报 | `no longer fully sovereign`→“不再拥有完整主权” |
| 22 | some | 7 Religion and Postsecularism / 17 | 误报 | `some of the…meaning`→“某些意义” |
| 23 | should | 7 Religion and Postsecularism / 19 | **真缺陷（已改）** | `should eventually replace`→原译“终将取代”把规范模态降为预测；改“应当最终取代” |
| 24 | if | 7 Religion and Postsecularism / 33 | 误报 | `provided that`→“只要”，条件关系保留 |
| 25 | some | 7 Religion and Postsecularism / 37 | 误报 | `Some critics`→“有批评者”，存在量化保留 |
| 26 | may | 7 Religion and Postsecularism / 37 | **真缺陷（已改）** | `can also affect`→原译“同样会波及”把可能性升为必然；改“同样可能波及” |
| 27 | must | 7 Religion and Postsecularism / 47 | 误报 | `must undergo`→“须经历” |
| 28 | no | 7 Religion and Postsecularism / 49 | 误报 | `no longer have to split`→“不必再把身份一分为二” |
| 29 | must | 7 Religion and Postsecularism / 49 | 误报 | `must undergo`→“须经历”（同上块） |
| 30 | all | 7 Religion and Postsecularism / 53 | 误报 | `from all sides`→“各方批评”，全称保留 |

## 3 修正（2 处，Major L-6）

| 行 | 原译 | 改后 | 源文 |
| ---- | ---- | ---- | ---- |
| L526 | 纯粹理性信仰**终将**取代历史性信仰 | 纯粹理性信仰**应当最终**取代历史性信仰 | `pure rational faith should eventually replace historical faiths` |
| L544 | 身份分裂同样**会**波及不信教者 | 身份分裂同样**可能**波及不信教者 | `identity-splitting can also affect non-believers` |

对应骨架行 `p-habermas-0839`、`p-habermas-0864` 已写入 `props`（modality=should／can）与修正说明。修正均在引号外，q1 引文 hash 未变动（`cite_audit --check-hash` 0）。

## 4 裁决总账

| verdict | 数 | 说明 |
| ---- | ---- | ---- |
| equivalent | 235 | 235 条承载句；30 条候选逐条核后记等价（含 2 处修正后等价） |
| trivial | 672 | 无强逻辑算子，不占人审预算 |
| pending | 0 | — |
| unformalized | 0 | 本轮未使用；全文形式化另批，见 §5 |

说明：非候选承载句按**块级**算子配对通过记 `equivalent`，未逐句填写完整 `props`。这是候选级筛查口径，不等于全文形式化证明。

## 5 发现与限制（不静默）

- **G1 候选级而非全文形式化**：235 条承载句未逐句建立谓词-论元骨架；本轮只对 30 条算子候选逐条定性。若后续要求 q2 全覆盖，应另立全文形式化批（含 L-1 命题数守恒、L-2 论元角色、L-7 命题态度、L-8 预设、L-10 指代、L-11 时体）。
- **G2 块级配对噪声**：30 条候选中 28 条为误报，主因是中文以“不再／必定／须／得以／只要／即便／有／各方”等表达英文算子，机检词表未收录；已在候选表逐条说明，不据此改文。
- **G3 复核独立性**：reviewer 与 tr-02 draft actor 同为 `trae-main`，属既定单会话偏离（同 T185）；已记录，不外推为独立性合规。

## 6 机检凭证

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| q2 门禁 | `python tools/logic_audit.py h/habermas.md --gate --json` | problems 0，退出码 0 |
| q1 hash 守恒 | `python tools/cite_audit.py h/habermas.md --check-hash --json` | problems 0，退出码 0 |
| 骨架覆盖 | 907 行；235 承载句全部有 verdict | pending 0 |
| 全量门禁 | `python tools/check_all.py` | 23/23 全绿 |

## 7 结论

q2 候选级筛查完成：30 条算子候选逐条定性，28 条误报有理由，2 条 Major 模态漂移已改并留痕；235 条承载句全部有裁决，0 pending；`logic_audit --gate` 与 q1 `--check-hash` 均 0。G1 的全文形式化缺口显式登记，不冒充已覆盖。下一步 T187（rv-05 q3 语法）。

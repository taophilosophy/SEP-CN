# 11 件 pilot 复跑记录（2026-11-28）

- 范围：`t175-pilot-plan.md` 的 11 件；全部内部边界
- 性质：**P3 sg-01 全量独立初审完成**（用户裁定"禁止抽审查，全量"；actor `glm-main`＝GLM-5.3-Flash，与初译 `trae-main`＝DeepSeek-V4.1-Flash 分离，满足 ADR-0093）
- 结论：11 件 sg-01 全量初审**全部通过**（无 Critical／Major）；中文侧 Minor 与 en 源候选逐件留痕移交；**sg-02 复审按 ADR-0093 须异于 `trae-main` 与 `glm-main`，待用户指定第三 actor**；P5／P6 未执行。**G5 仍未通过，不得扩量。**

## 1 逐件状态（sg-01 全量）

| 件 | P0 规范 | P1 源 | P2 full PE | P3 sg-01（全量） | P4 抽样 | P5 编校 | P6 发布 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| h/habermas | 通过（16 字段） | 通过 | 通过 | **通过（全量重做，抽审作废）** | 已出计划 | 未执行 | 未执行 |
| l/logic-preference | 通过 | 通过 | 通过 | **通过** | 已出计划 | 未执行 | 未执行 |
| e/environmental-aesthetics | 通过 | 通过 | 通过 | **通过** | 已出计划 | 未执行 | 未执行 |
| i/imprecise-probabilities | 通过 | 通过 | 通过 | **通过**（数学复算全对） | 已出计划 | 未执行 | 未执行 |
| a/action | 通过 | 通过 | 通过 | **通过** | 已出计划 | 未执行 | 未执行 |
| a/axiom-choice | 通过 | 通过 | 通过 | **通过**（中文侧零发现） | 已出计划 | 未执行 | 未执行 |
| n/newton-principia | 通过 | 通过 | 通过 | **通过**（中文侧零发现） | 已出计划 | 未执行 | 未执行 |
| l/logic-dynamic | 通过 | 通过 | 通过 | **通过** | 已出计划 | 未执行 | 未执行 |
| j/japanese-aesthetics | 通过 | 通过 | 通过 | **通过** | 已出计划 | 未执行 | 未执行 |
| k/kokugaku-school | 通过 | 通过 | 通过 | **通过** | 已出计划 | 未执行 | 未执行 |
| d/digital-art | 通过 | 通过 | 通过 | **通过**（中文侧零发现） | 已出计划 | 未执行 | 未执行 |

## 2 逐件 sg-01 证据与要点

| 件 | 记录 | 中文侧要点 | en 源候选 |
| ---- | ---- | ---- | ---- |
| habermas | `sg01-habermas.md` | Minor 9（含"科学之王"queen 意象错位）；discourse principle 异译（商谈原则 vs 话语原则）移交 rv-01 | 8（dividend／Augustin／he instrumental／缺右括号等） |
| logic-preference | `sg01-logic-preference.md` | Minor 9（C8 公式内英文缺口 2 处） | 3（R3 "ψ similar to ψ" 自我指涉、公式错插等） |
| environmental-aesthetics | `sg01-environmental-aesthetics.md` | Minor 8（**Muir 篇名"远观"应为"近观"**，优先修正） | 12（distinterestedness、mixedenvironments 等） |
| imprecise-probabilities | `sg01-imprecise-probabilities.md` | 术语移交 2（credal state 异译"信态"／弹珠 vs 球）；Minor 3；数学复算 3 处全对 | 0 |
| action | `sg01-action.md` | Minor 1（Rugen"杀死自己父亲"指派错）；en 候选含 1 概念性（Libet 'action potentials' 应 readiness potentials） | 8 |
| axiom-choice | `sg01-axiom-choice.md` | 零发现；数学全对（置换模型／采样引理／Diaconescu） | 2（Lindenbaum 正文 Mostowski vs 引用 Tarski） |
| newton-principia | `sg01-newton-principia.md` | 零发现 | 1（标题上标残留） |
| logic-dynamic | `sg01-logic-dynamic.md` | Minor 1（"托尼·霍尔"增译 Tony） | 1（Lange 年份） |
| japanese-aesthetics | `sg01-japanese-aesthetics.md` | Minor 5（Rickert 混排、市川崑、泼墨/破墨双名等） | 2（**golden Tai-an 待庵史实疑误**，移交 sg-02 研判） |
| kokugaku-school | `sg01-kokugaku-school.md` | Minor／移交 3（**《神祇志》应为《神祇式》**、汉心/汉意、mono no aware 跨件异名） | 2（arahaniyo 转写疑误） |
| digital-art | `sg01-digital-art.md` | 零发现（Ackermann 译注处置完整） | 2（Haugeland "Analog and Analog" 重复，待联网查证） |

## 3 证据

* 逐件记录：`results/pilot/<slug>.json`（P3.sg-01 scope=full）；汇总：`results/pilot/run-summary.json`。
* 全量初审详录：`results/pilot/sg01-<slug>.md`（11 件，各含全量范围、四维结论、Minor 清单、en 候选、排除记录）。
* steps／journal：各件 `tasks/<letter>/<slug>.json` 追加 glm-main sg-01 条目、`journal/<letter>/<slug>.ndjson` 同步。
* competence：11 件 `competences["glm-main"]` 经 `task_ops.py competence` CLI 登记（四字段齐）。
* P0／P1／P2／P4：维持首轮预检结论（`run-summary.json`）。

## 4 阻塞与下一步

1. **sg-02 复审**：按 ADR-0093（译者≠初审≠复审≠终审），sg-02 须异于 `trae-main` 与 `glm-main`——**须用户指定第三 actor**（例如另一模型会话）；建议优先研判 sg01 详录中标注"优先修正／研判"的移交项（habermas discourse principle、environmental-aesthetics Muir 篇名、japanese-aesthetics golden Tai-an、kokugaku 神祇式、logic-dynamic 托尼·霍尔）。
2. **P4 计分**：抽样计划已出；ISO 5060 人工评分需独立评估者（`rules/evaluator-registry.json` 双评制）。
3. **P5**：八项编校需真实样本与 copyedit／proofs；当前无件级产物。
4. **P6**：无 release sign-off 与件级归档；不得发布预演。
5. G5 放行仍需 sg-02／P5／P6 与基线测量；本轮不改变 G5 结论。

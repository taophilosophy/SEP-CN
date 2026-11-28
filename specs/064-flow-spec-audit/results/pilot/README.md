# 11 件 pilot 首轮预检记录（2026-11-28）

- 范围：`t175-pilot-plan.md` 的 11 件；全部内部边界
- 性质：**首轮预检（P0／P1／P2／P4 抽样）**；P3 独立审校、P5 编校、P6 发布预演未执行
- 结论：11 件 P0 规范补齐、P1 源记录、P2 PE 留痕、P4 抽样计划均已完成；P3 因单代理同 actor 阻塞，P5／P6 未执行。**G5 仍未通过，不得扩量。**

## 1 逐件状态

| 件 | P0 规范 | P1 源 | P2 full PE | P3 独立审校 | P4 抽样 | P5 编校 | P6 发布 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| h/habermas | 通过（16 字段） | 通过 | 通过（llm-pe／full） | 阻塞（同 actor） | 已出计划 | 未执行 | 未执行 |
| l/logic-preference | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| e/environmental-aesthetics | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| i/imprecise-probabilities | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| a/action | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| a/axiom-choice | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| n/newton-principia | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| l/logic-dynamic | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| j/japanese-aesthetics | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| k/kokugaku-school | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |
| d/digital-art | 通过 | 通过 | 通过 | 阻塞 | 已出计划 | 未执行 | 未执行 |

## 2 证据

* 逐件记录：`results/pilot/<slug>.json`；汇总：`results/pilot/run-summary.json`。
* 抽样计划：`results/pilot/samples/<slug>.json`（`qa_sample.py` 生成；每层≥1、总量≥max(20,10%)、sha256 定序）。
* P0：11 件 `project_spec` 已补到 16 字段（未改 state／steps）。
* P3：11 件的 `sg-01`／`sg-02` 仍为 `trae-main`，与 `tr-02` 同 actor；`competences` 为空。按 T171 硬门不能声称独立审校。

## 3 阻塞与下一步

1. **P3**：需用户指定独立审校 actor（sg-01／sg-02）并登记 competence 四字段；单代理不能伪造。
2. **P4 计分**：抽样计划已出，但 ISO 5060 人工评分需独立评估者；当前只到计划。
3. **P5**：八项编校需真实样本与 copyedit／proofs；当前无件级产物。
4. **P6**：无 release sign-off 与件级归档；不得发布预演。
5. G5 放行仍需 P3／P5／P6 与基线测量；本轮不改变 G5 结论。

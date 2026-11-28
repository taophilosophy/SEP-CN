# T175 验收证据：规则卡同步＋11 件 pilot 计划（CP-S14-32–36）

- 日期：2026-11-28
- 范围：T313–T317；T175 为容器，不整体勾选
- 清单：`t175-rule-sync.md`、`t175-pilot-plan.md`、`t175-pilot-record-template.md`、`t175-g5-checklist.md`、`t175-closure.md`
- 校验：`tools/check_t175.py`

## 1 逐项验收

| 任务 | 检查点 | 落点 | 验收结果 | 结论 |
| ---- | ---- | ---- | ---- | ---- |
| T313 | CP-S14-32 | `t175-rule-sync.md` | 6 源 18 项；每项有差异／落点／优先级；P1 5 项；无悬空 | 通过 |
| T314 | CP-S14-33 | `t175-pilot-plan.md` | 11 件×P0–P6；每件有证据清单；全部内部边界 | 通过 |
| T315 | CP-S14-34 | `t175-pilot-record-template.md` | spec／角色／TBX／full PE／评分卡／编校／归档字段齐；失败样本要求可复现 | 通过 |
| T316 | CP-S14-35 | `t175-g5-checklist.md` | 三项检查；T170–T175 是、差异表是、pilot 基线否；G5 未通过 | 通过（检查单） |
| T317 | CP-S14-36 | `t175-closure.md` | 只出清单／记录；不执行翻译、不改任务状态、不新增 T 号、不整体勾选 | 通过 |

## 2 机检与证据位置

- `python tools/check_t175.py`：rule_sync／pilot_plan／g5／closure 全部 0 errors。
- `python -m unittest tools.tests.test_t175`：**5 tests OK**（含缺源、缺件、G5 误判、收口缺句反例）。
- `python tools/check_all.py`：**23 项，失败 0，全绿**。

## 3 边界与交接

- 本批**未执行 11 件 pilot**：计划与模板已出，P0–P6 均未跑；G5 第 2 项为“否”，故 G5 未通过，不得扩量。
- 本批**未执行翻译**：未改 `zh/`、`en/`、`html/`、`yuanwen/`、ledger；未改 `tasks/*.json` 状态。
- P1 差异 5 项（rules/04 评分卡指针、rules/04 P5–P7、rules/05 工具表、rules/05 门禁、specs/061 缺口状态）须在 pilot 前同步；本批只登记，不改规则。
- 下一步：用户决定是否启动 pilot；启动后按模板逐件记录并测八项基线，G5 三项齐全后再评估扩量。

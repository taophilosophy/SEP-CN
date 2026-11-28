# T173 验收证据：ISO 5060 评分卡＋学术编校（CP-S14-19–25）

- 日期：2026-11-28
- 范围：T300–T306；T173 为容器，不整体勾选
- 数据：`rules/qa-scorecard.json`、`rules/evaluator-registry.json`
- 工具：`tools/check_qa_scorecard.py`、`tools/qa_sample.py`
- 规则：`rules/09`、`rules/10`；ADR-0095

## 1 逐项验收

| 任务 | 检查点 | 落点 | 验收结果 | 结论 |
| ---- | ---- | ---- | ---- | ---- |
| T300 | CP-S14-19 | `results/t173-iso5060-map.md`；`qa-scorecard.json` | 七类全部映射到 rv-01／tr-03／rv-02／q1–q6／rv-09／sg；每类有缺口说明 | 通过 |
| T301 | CP-S14-20 | 评分卡 severity／category weights | Critical／Major／Minor 权重齐；Critical 一票否决；权重入机读卡 | 通过 |
| T302 | CP-S14-21 | `qa_sample.py`＋评分卡 sampling | H2 分层、每层≥1、总量≥max(20, 10%)、sha256 定序；出版前审校不替代 | 通过 |
| T303 | CP-S14-22 | `check_qa_scorecard.py --score` | 七类字段、公式、阈值、Critical；按件计分；版本随结果返回 | 通过 |
| T304 | CP-S14-23 | `evaluator-registry.json`＋`t173-calibration-template.md` | evaluator／arbiter 资格与独立性；双评字段；阈值 pending_pilot | 通过（模板） |
| T305 | CP-S14-24 | 评分卡 metrics＋`rules/10` §10.4 | 出版 1/10000 与服务 1.5‰ 分写；project_spec.qa_level 须写明门 | 通过 |
| T306 | CP-S14-25 | `t173-academic-checklist.md`＋`rules/10` §10.8 | 八项编校逐项有样本／验收；不设权利门 | 通过（清单） |

## 2 机检与证据位置

- `python -m unittest tools.tests.test_qa_scorecard tools.tests.test_qa_sample`：**13 tests OK**（评分卡 9＋抽样 4）。
- `python tools/check_qa_scorecard.py`：0 errors（含 evaluator registry）；`--score` 可按 findings JSON 计分。
- `python tools/qa_sample.py <zh-doc>`：输出可复算抽样计划。
- `python tools/check_all.py`：**23 项，失败 0，全绿**。

## 3 边界与交接

- 评估者校准只出模板与登记表：当前无真实双评数据，`threshold_status=pending_pilot`，阈值须 pilot 实测后设定；不伪造校准记录。
- 学术编校清单八项尚无真实 P5 样本；样本随 11 件 pilot 的 P5 预演补齐。
- 评分卡权重（Critical 10／Major 5／Minor 1）为首版，pilot 后按分布复算；评分卡版本写入每次 evidence。
- 出版与服务口径已分写；GB/T 19682 的 1.5‰ 不得用作出版门。

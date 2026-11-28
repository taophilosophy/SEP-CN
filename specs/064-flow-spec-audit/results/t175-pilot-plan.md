# T175 11 件 pilot 计划（CP-S14-33）

- 日期：2026-11-28
- 范围：11 件 E2E 词条；**只做内部 pilot 计划，不执行翻译、不发布**
- 口径：E2E 已完成≠v2 pilot 已过；每件须重过 P0–P6，证据逐项登记
- 边界：全部内部；P6 只做发布预演，不公开、不扩量

## 1 逐件计划

| 件 | P0 规范 | P1 源 | P2 full PE | P3 独立审校 | P4 评分卡 | P5 编校 | P6 发布预演 | 证据清单 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| h/habermas | 待建 16 字段 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e-habermas、scorecard、editing |
| l/logic-preference | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| e/environmental-aesthetics | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| i/imprecise-probabilities | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| a/action | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| a/axiom-choice | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| n/newton-principia | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| l/logic-dynamic | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| j/japanese-aesthetics | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| k/kokugaku-school | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |
| d/digital-art | 待建 | 复用 E2E ex-04 | 复用译文；补 PE 留痕 | 待独立 | 待评分 | 待八项 | 内部 | task、e2e 记录、scorecard、editing |

## 2 P0–P6 门定义

| 门 | 判据 | 证据 |
| ---- | ---- | ---- |
| P0 | `project_spec` 16 字段齐；风险级、PE 级别、QA 等级明确 | 任务 JSON `project_spec` |
| P1 | 源钉有效；ex-04 记录；TBX 概念条目可用 | 源审计记录、`baseline/termbase-sample.tbx` 或件级 TBX |
| P2 | full PE；模型／提示登记；账本守恒 | `baseline/model-registry.json`、PE 记录、ledger |
| P3 | 译者≠初审≠复审≠终审；competence 四字段 | step actor、`competences` |
| P4 | 评分卡计分；Critical＝0；抽样可复算 | `rules/qa-scorecard.json`、`qa_sample.py` 输出 |
| P5 | 八项编校清单逐项有样本 | `results/t173-academic-checklist.md` |
| P6 | release sign-off；CI 全绿；内部预演 | 归档 manifest、release 记录 |

## 3 复盘产出

每件须产出：pilot 记录（模板见 `t175-pilot-record-template.md`）、失败样本（可复现命令／输入／期望）、基线数据（Critical、1/10000、Major／Minor、返工、PE 工时、一致性、发布后勘误、周期成本）。未出记录不得称“pilot 通过”。

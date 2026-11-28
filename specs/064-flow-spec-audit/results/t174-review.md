# T174 验收证据：记录／归档／度量＋AI 治理＋发布后（CP-S14-26–31）

- 日期：2026-11-28
- 范围：T307–T312；T174 为容器，不整体勾选
- 数据：`rules/archive-schema.json`、`rules/retention.json`、`rules/metrics-baseline.json`、`rules/ai-governance.json`、`rules/post-publication.json`
- 工具：`tools/check_governance.py`；规则：`rules/09`；ADR-0096

## 1 逐项验收

| 任务 | 检查点 | 落点 | 验收结果 | 结论 |
| ---- | ---- | ---- | ---- | ---- |
| T307 | CP-S14-26 | `archive-schema.json`＋`t174-archive-template.json`＋`t174-archive-habermas.json` | 八类齐；每件 path／sha256／date／owner；模板绿；habermas 实际件缺 scorecard／editing 判红 | 通过 |
| T308 | CP-S14-27 | `retention.json` | 八类 retention／destruction／access／owner；永久留存、销毁只走 ADR；对齐 ISO 15489／GB/T 26162 | 通过 |
| T309 | CP-S14-28 | `metrics-baseline.json` | 八项指标；baseline／threshold 全 null；`pending_pilot`；未测基线不得设阈值 | 通过 |
| T310 | CP-S14-29 | `ai-governance.json` | 风险登记 3 条、影响评估、模型变更回归、供应商条款、事件处理；无 disclosure 字段 | 通过 |
| T311 | CP-S14-30 | `post-publication.json` | 勘误／反馈／上游更新／抽审／版本记录五项，均有 owner／trigger／evidence | 通过 |
| T312 | CP-S14-31 | `tools/tests/test_governance.py` | 缺归档项、缺留存项、预设阈值、缺 AI 风险字段、缺发布后项均红；6 tests OK | 通过 |

## 2 机检与证据位置

- `python -m unittest tools.tests.test_governance`：**6 tests OK**。
- `python tools/check_governance.py`：项目级模板全部 0 errors；`--archive t174-archive-habermas.json` 返回 `缺归档项 scorecard／editing`（预期红灯）。
- `python tools/check_all.py`：**23 项，失败 0，全绿**。

## 3 边界与交接

- 项目级模板的 scorecard／editing 暂以 `rules/qa-scorecard.json` 与 `results/t173-academic-checklist.md` 代表；实际件须在 P5 后替换为件级产物，否则 `t174-archive-habermas.json` 持续红灯。
- 度量基线全部待 pilot 实测；当前不得设阈值或宣称 KPI。
- AI 影响评估、模型变更回归、供应商条款审查待实际模型变更或 pilot 时填充；本任务只建登记与校验。
- 发布后五项流程已登记，实际勘误／反馈样本随发布后运行产生。

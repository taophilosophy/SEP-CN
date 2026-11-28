# T175 规则卡差异表（CP-S14-32）

- 日期：2026-11-28
- 范围：`rules/04`、`rules/05`、`specs/060`、`specs/061`、`specs/063`、`rules/standards.json`
- 口径：只列差异、落点与优先级，**本任务不修改规则正文**；P1＝扩量前必须同步，P2＝pilot 期间同步，P3＝pilot 后整理。
- 结论：六源均有差异项，且每项有落点；无悬空。

| 源 | 差异项 | 差异 | 落点 | 优先级 |
| ---- | ---- | ---- | ---- | ---- |
| rules/04 | ISO 5060 评分卡／抽样／评估者 | 规则仍只写问题分级与 CY/T 266，未指向 `qa-scorecard.json`／`qa_sample.py`／`evaluator-registry.json` | `rules/04` §复核独立性与问题分级 | P1 |
| rules/04 | P5–P7 生命周期 | 流程止于 sg-03／done；P5 编校、P6 发布归档、P7 发布后未入规则正文 | `rules/04` 末节（新增 P5–P7 段） | P1 |
| rules/04 | TBX 概念流程 | tr-01 术语摘录未指向 `rules/03` 概念库流程与 `term_tbx.py --check` | `rules/04` tr-01 段 | P2 |
| rules/04 | 模型／提示登记 | 译后编辑段未指向 `baseline/model-registry.json` 与变更回归 | `rules/04` 译后编辑定位段 | P2 |
| rules/05 | 工具表缺新工具 | `tools.md` 未登记 `term_tbx.py`、`check_risk_matrix.py`、`check_model_registry.py`、`check_qa_scorecard.py`、`qa_sample.py`、`check_governance.py` | `rules/05/tools.md` | P1 |
| rules/05 | 新校验器未入门禁 | 六个新校验器未进 `check_all.py` GATES／CI 矩阵 | `rules/05/index.md`＋`tools/check_all.py` | P1 |
| rules/05 | 发布与归档记录 | 提交流程未写 release sign-off／archive manifest 的存放与复核点 | `rules/05/commit-policy.md` | P2 |
| specs/060 | ISO 5060 评分卡交叉引用 | 六轴规格未链到七类评分卡与 Critical＝0 计分口径 | `specs/060/spec.md` §7 | P2 |
| specs/060 | 评分卡版本 | q1–q6 凭据未要求记录 scorecard_version | `specs/060/spec.md` §4 | P3 |
| specs/061 | 缺口状态过期 | G3／G4／G6／G8 已在 T170–T174 关闭，061 仍写未落地 | `specs/061/spec.md` §1、§6 | P1 |
| specs/061 | 评估快照 | §5 流程矩阵未标“历史快照”与新锚点回链 | `specs/061/spec.md` §5 | P2 |
| specs/063 | P0–P7 与阶段轨 | 063 的 60 项阶段轨未给 P0–P7 生命周期 crosswalk | `specs/063/spec.md` §1.2／§1.3 | P2 |
| specs/063 | 阶段轨实施状态 | 063 仍为设计卡，P0–P7 由 064 target-workflow 承载，未在 063 声明 | `specs/063/spec.md` §0.3 | P2 |
| specs/063 | state→stage 映射 | 19 状态映射未覆盖 P0／P5–P7 新增阶段语义 | `specs/063/spec.md` §1.7 | P3 |
| standards.json | ACLS 未登记 | ACLS 学术翻译指南为非标准最佳实践，登记册无条目 | `rules/standards.json` cited 层 | P2 |
| standards.json | TBX／评分卡承接 | ISO 30042／GB/T 44227 TBX 与 ISO 5060 评分卡工具未各立 adopted 承接项 | `rules/standards.json` adopted 层 | P2 |
| standards.json | GB/T 19682 状态 | S11 仍写“adopted（部分）”，服务口径与出版口径已分写 | `rules/standards.json` S11 | P2 |
| standards.json | 已完成项 | V01 已撤销；42001／23894 已入册（T174）；无需再改 | `rules/standards.json`（已同步） | 已同步 |

**P1 清单**：rules/04 评分卡指针、rules/04 P5–P7、rules/05 工具表、rules/05 门禁、specs/061 缺口状态，共 5 项；扩量前须完成。

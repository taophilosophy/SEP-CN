# T171 验收证据：项目规范＋角色与独立性（CP-S14-06–11）

- 日期：2026-11-28
- 范围：T287–T292；T171 为容器，不整体勾选
- 代码：`tools/task_ops.py`；规则：`rules/04`、`rules/09`、`rules/standards.json`、`rules/README.md`；ADR：`rules/adr/0093-项目规格扩展与四审分离.md`

## 1 逐项验收

| 任务 | 检查点 | 落点 | 验收结果 | 结论 |
| ---- | ---- | ---- | ---- | ---- |
| T287 | CP-S14-06 | `PROJECT_SPEC_SCHEMA`／`PROJECT_SPEC_FIELDS`／`PROJECT_SPEC_DEFAULT`；`rules/09` §3.2 | 内容 7＋过程 4＋其他 5＝16 字段；类型、默认、必填齐；未知字段与空值拒建账 | 通过 |
| T288 | CP-S14-07 | `_project_spec_gate`；`advance tr-02` 挂钩 | 16 字段全非空；`risk_level`／`pe_level` 枚举校验；`pe_level` 与 `translation_mode` 一致；缺受众／用途／QA／PE／风险任一即拒 | 通过 |
| T289 | CP-S14-08 | `rules/09` §2.1 | 11 角色×P0–P7 的 R/A/C/I；PM、译者／PE、双语审校、领域审校、术语员、校对、copyeditor、QA、AI steward 全列 | 通过 |
| T290 | CP-S14-09 | `competences` 字段、`set_competence`、`competence` CLI、`_review_competence_gate` | 每人四字段（qualification／experience／domain／training）；缺项拒登记、缺记录拒推进 | 通过 |
| T291 | CP-S14-10 | `_review_independence_gate`；`rules/04` 复核独立性；`standards.json` 移除 V01；ADR-0093 | 译者（tr-02）≠初审（sg-01）≠复审（sg-02）≠终审（sg-03）；无冷置／密度补偿；V01 撤销 | 通过 |
| T292 | CP-S14-11 | `tools/tests/test_task_ops.py` | 同人审校红、独立审校绿、缺 competence 红；37 tests OK | 通过 |

## 2 机检与证据位置

- `python -m unittest tools.tests.test_task_ops`：**37 tests OK**（含新增 6 项：三类 schema、五关键缺项、枚举／PE 一致性、competence 硬门、四审同人红、CLI 登记）。
- `python tools/check_all.py`：**23 项，失败 0，全绿**。
- 任务计数：新增 T287–T292 六个原子号；编号 203→209，已验证 132→138，未开始 56（不含工作包容器）。

## 3 边界与交接

- 既有 done 任务的 `project_spec` 仍为旧六字段，不回填；如重开推进 `tr-02`，须先补齐 16 字段，否则机检拒绝（ADR-0093 决策 5）。
- 领域审校与校对的独立性写入 RACI 与 `rules/09`，当前 22 节点无对应推进步，未另设机检；待 P5 编校链落地时接入。
- V01 从 `standards.json.deviations` 移除；ADR-0084 作为历史记录保留，其 D1 由 ADR-0093 取代。
- T170 登记的标准锚点漂移中，`rules/09` 一处已在本任务改为 ISO 17100 5.3.3；`specs/041`／`specs/063` 两处仍归 T175。

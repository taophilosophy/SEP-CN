# T172 验收证据：TBX＋机器／LLM 治理（CP-S14-12–18）

- 日期：2026-11-28
- 范围：T293–T299；T172 为容器，不整体勾选
- 代码：`tools/term_tbx.py`、`tools/check_risk_matrix.py`、`tools/check_model_registry.py`
- 数据：`baseline/termbase-sample.tbx`、`baseline/model-registry.json`、`rules/risk-matrix.json`
- 规则：`rules/03`、`rules/04`、`rules/09`、`rules/10`；ADR-0094

## 1 逐项验收

| 任务 | 检查点 | 落点 | 验收结果 | 结论 |
| ---- | ---- | ---- | ---- | ---- |
| T293 | CP-S14-12 | `term_tbx.py` 的 `DESCRIP_KEYS`／`render`／`parse_tbx` | 概念 ID、学科域、定义、术语、来源、语境、语法、交叉引用、状态、日期、负责人齐；状态限 candidate／current／deprecated | 通过 |
| T294 | CP-S14-13 | `migrate_items`／`write_sample`／`render_view` | 两表各 5 行→10 条 TBX；两表视图由 TBX 生成；样本往返测试通过 | 通过 |
| T295 | CP-S14-14 | `rules/03` 概念库流程 | 候选→审定→登记→使用→变更；模型不得自审；弃用词、首现括注、变更记录有规则 | 通过 |
| T296 | CP-S14-15 | `term_tbx.py --check` | 正例绿；缺 ID／缺术语／状态非法／日期非法／重复 ID 红；10 项测试通过 | 通过 |
| T297 | CP-S14-16 | `rules/risk-matrix.json`＋`check_risk_matrix.py` | A 人工为主、B full PE、C 仅内部；出版件 full PE、禁 raw／light、Critical＝0；5 项反例测试 | 通过 |
| T298 | CP-S14-17 | `baseline/model-registry.json`＋`check_model_registry.py` | provider／model／version／date／params／prompt／术语版本／数据条款齐；重复 ID、坏日期、缺字段红；5 项测试 | 通过 |
| T299 | CP-S14-18 | `rules/09` §2.2；`rules/04` 指针 | 禁 raw／light PE 出版、禁模型生成引文、逐段回源、QE 只分流 | 通过 |

## 2 机检与证据位置

- `python -m unittest tools.tests.test_term_tbx tools.tests.test_risk_matrix tools.tests.test_model_registry`：**20 tests OK**。
- `python tools/term_tbx.py --check baseline/termbase-sample.tbx`：0 errors；5 条 current 术语缺定义告警（`baseline/term-concepts.md` 尚无概念行）。
- `python tools/check_risk_matrix.py`、`python tools/check_model_registry.py`：均 0 errors。
- `python tools/check_all.py`：**23 项，失败 0，全绿**。

## 3 边界与交接

- 全量 14,000＋术语未一次性迁入 TBX：`baseline/term-concepts.md` 尚无概念行，批量转换会产生空定义壳；本次只做 10 条迁移样本（两表各 5）与视图往返，全量切换随 T175 pilot 与概念行补齐推进。
- 样本视图在 `specs/064-flow-spec-audit/results/t172-views/`，仅作验收材料，不替代正式两表。
- 模型登记当前 1 条（DeepSeek-V4.1-Flash）；模型、提示或参数变更须追加记录并重跑固定样本与评分卡。
- 风险矩阵与模型登记校验器暂未挂入 `check_all`，由 `tools/tests/` 的管线单元测试覆盖；如需硬门，另立门禁项（不在 T172 擅自扩充门禁清单）。

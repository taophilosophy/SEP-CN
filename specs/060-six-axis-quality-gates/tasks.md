# 任务清单：六轴独立质量工序（specs/060）

> 状态值：done／in_progress／pending／blocked。完成判据一律为可复算的验收，不以“已写文档”作完成证据（rules/08 §4）。

## A 立项与规则

| ID | 任务 | 产出 | 验收 | 状态 |
| ---- | ---- | ---- | ---- | ---- |
| T-01 | 立项与 ADR | `spec.md`（accepted）、`plan.md`、`tasks.md`、ADR-0079 | 文件入库；ADR 四件套齐全 | done |
| T-02 | 状态机 v3 | `pipeline.json` 22 节点；`journal_lib` 映射；`task_ops` q 链与 `_axis_gate` | `check_stages` 13 项全绿；ORDER 含 q1–q6 | done |
| T-03 | 规则正文 | `rules/02`（标点归 q6）、`rules/03`（和制汉语）、`rules/04`（六工序）、`rules/05/tools.md`、`rules/07`（引文全语种）、`rules/README`（标准清单） | 条款可回溯；`check_doc_size` 绿 | done |
| T-04 | 公理与事件模型 | `axioms.json` P29–P33；`journal-schema.json` 节点计数 | `check_stages` 绿 | done |

## B 工具与判据

| ID | 任务 | 产出 | 验收 | 状态 |
| ---- | ---- | ---- | ---- | ---- |
| T-05 | 共享库 | `tools/axis_lib.py` | 掩码等长、句/块/节抽取、语种判定单测通过 | done |
| T-06 | q1 引文 | `tools/cite_audit.py` | `--init`／`--gate`／`--check-hash` 可跑；单件引文级候选可复算 | done |
| T-07 | q2 逻辑 | `tools/logic_audit.py` | 骨架 jsonl 生成；按节配对出候选；`--gate` 覆盖率检查 | done |
| T-08 | q3 语法 | `tools/grammar_audit.py` | 三型启发式＋`check_prose` 复用＋日源词表；白名单防误判 | done |
| T-09 | q4 语域 | `tools/register_audit.py` | 逐节档位骨架；文言/口语/称谓候选 | done |
| T-10 | q5 计量 | `tools/measure_audit.py` | 单位白名单、空格、同量集合、数值范围；`--init`／`--gate` | done |
| T-11 | q6 标点 | `tools/punct_audit.py` | 十七种标点机检子集；条款映射输出 | done |
| T-12 | 编排器 | `tools/qchain.py` | 六器顺序汇总；不写任务状态 | done |
| T-13 | 数据表 | `tools/data/units.json`、`ja-loanwords.json`、`register-lexicon.json`、`punct-rules.json` | 工具读取生效；变更可回退 | done |
| T-14 | 单测 | `tools/tests/test_six_axis.py`、`test_task_ops.py` 适配 | `unittest discover` 全绿 | done |
| T-22 | 公理化验证 | `bin/verify_six_axis.py`、`verification.md`、`results/verification.json`、`results/verification-a.json` | A 组结构违例 0；CY/T 266 覆盖 29/29、MQM 7/7；判据交待复核 0；幂等全过 | done |
| T-23 | 三审三校对接口分析 | `triple-proofreading.md`、`bin/probe_merge.py` | 结论＋负向实验可复算；S6 谓词建议 | done |

## C 运行与验收

| ID | 任务 | 产出 | 验收 | 状态 |
| ---- | ---- | ---- | ---- | ---- |
| T-15 | T0 全库摸底 | `state/axis/qchain-latest.json` 与各类命中数 | 六类皆有数；误报样本登记 | in_progress |
| T-16 | 试金石 3 件 | 三件 q1–q6 工单与人工裁定 | 三件走通至 r1/r2；gate 按预期拦未裁定项 | pending |
| T-17 | 语域样章基准 | `baseline/register-baseline.md` | 用户裁定 3–5 段后入库 | blocked（待裁） |
| T-18 | 逻辑骨架金样本 | `baseline/logic-baseline.jsonl` | 用户定 100 句试标后扩至 500 句 | blocked（待裁） |
| T-19 | T1 新件硬拦 | `pipeline.json` 六节点 `gate_owner=true` | 新件 q 链 pass；存量不受影响 | pending |
| T-20 | T2 存量回炉 | A–Z 分批记录 | 每类残余 0 或全部豁免 | pending |
| T-21 | T3 固化 | `check_all` GATES 挂六器；CI 绿 | `--list-gates` 含六器；CI 通过 | pending |

## D 已知限制

1. q2 逻辑骨架的 `props` 需人工填写，工具只产骨架与算子候选；这是设计（可判性边界），不是缺陷。
2. q3 第一层（成分残缺/搭配/语序）无可靠机检，`--gate` 只校验处置留痕，不判对错。
3. q4 档位判定全靠人审；工具只查“有没有定档”。
4. q1 的 `verifiable` 判定依赖版本知识，工具不能替代查证；`unavailable` 必须写明理由。
5. 六器全部为“筛”，`--gate` 通过不等于内容合格（ADR-0070）。

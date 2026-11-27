# T138 拆解：rv-03–08 六轴原子任务（方案）

- 日期：2026-11-27
- 依据：`tasks.md` T138（工作包）、`rules/04` rv-03–08、`rules/05` 检查器地图
- 原则：T138 是容器，**不得整体勾选**；q1→q6 顺序固定；每个原子任务单独编号、单独验收、单独留证
- **2026-11-27 更正**：原稿把六轴误写为“版面／体例／术语／事实／引用／语言”；权威定义见 `rules/04` §六轴（ADR-0079）——q1 引文、q2 逻辑、q3 语法、q4 语域、q5 计量、q6 标点。下表与任务书已按权威定义更正。
- 编号：**已入册 T185–T190**（2026-11-27 按下一可用号实际分配；T185＝q1 … T190＝q6）；本方案不预写占位号的做法不变
- 共同写域：`h/habermas.md`；账本 `tasks/h/habermas.ledger.yaml` 只在需要同步时改
- 共同证据目录：`state/axis/habermas/`（按轴一文件）

## 六个原子任务

| 轴 | 名称 | 范围与手段 | 验收 | 证据 |
| ---- | ---- | ---- | ---- | ---- |
| **q1** | 引文锁定（rv-03） | 成句直引；原著语种与原文可得性（na/present/verifiable/unavailable）；hash 锁定；`cite_audit --init/--gate` | 清单完备（C-1）、字段合法（C-2）、anchor 非空（C-6）、verdict 无 pending、hash 守恒（C-7） | `state/axis/habermas.cite.json`＋`results/t185-review.md` |
| **q2** | 逻辑一致性（rv-04） | 谓词-论元骨架、量化与辖域、条件方向、模态；`logic_audit`（只产候选） | 候选逐条定性；无未处置告警 | `state/axis/habermas.logic.jsonl`＋`results/t186-review.md` |
| **q3** | 语法（rv-05） | 句法合法性、反欧化、和制汉语；`grammar_audit`（吸收 `check_prose`） | 告警清零或逐条豁免 | `state/axis/habermas.grammar.json`＋`results/t187-review.md` |
| **q4** | 语域（rv-06） | 五档标尺、档位漂移、语气；`register_audit`（只产候选） | 漂移逐条定性；无未处置告警 | `state/axis/habermas.register.json`＋`results/t188-review.md` |
| **q5** | 计量（rv-07） | 量值-单位、数字形态、换算；`measure_audit` | 硬错误 0；告警逐条处置 | `state/axis/habermas.measure.json`＋`results/t189-review.md` |
| **q6** | 标点（rv-08） | GB/T 15834 十七种标点、邻接与禁则；`punct_audit`（吸收 `check_style` 标点项） | 告警清零或逐条豁免 | `state/axis/habermas.punct.json`＋`results/t190-review.md` |

## 依赖与顺序

```
q1 → q2 → q3 → q4 → q5 → q6 → T139（rv-09 体例终校）
```

- 每轴完成即写证据并勾选该原子任务；**T138 本身保持未勾选**，只作容器。
- q3 语法可复用 T135 的 `check_prose` 处置表；q6 标点可复用 T136 的体例与标点结论；均须在轴内重跑并重新留证。
- 任一轴发现需改正文，先改 `h/habermas.md`，再复跑该轴与下游轴；不得以“上游已过”为由跳过下游复跑。
- q1 之后所有轴不得改动引文内部文字与标点（C-7 hash 守恒）；q4 语域以 `register_audit` 候选为辅、人审定档为主，不得用全库门禁绿替代。

## 入册规则

执行第一轴前，把六个原子任务按下一可用 T 号写入 `tasks.md` 的 S-1 分区，并在 T138 行注明“已拆为 T…–T…”；同时更新 `results/axioms-tasks.md` 的计数与拓扑序。未入册前不得开工，也不得把 T138 当已完成。

**状态**：已于 2026-11-27 入册为 T185–T190（`tasks.md` S-1；`axioms-tasks.md` §17 rev22 复算 107/107）；T185（q1）、T186（q2）已完成，T187–T190 未启动。

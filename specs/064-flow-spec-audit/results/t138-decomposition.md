# T138 拆解：rv-03–08 六轴原子任务（方案）

- 日期：2026-11-27
- 依据：`tasks.md` T138（工作包）、`rules/04` rv-03–08、`rules/05` 检查器地图
- 原则：T138 是容器，**不得整体勾选**；q1→q6 顺序固定；每个原子任务单独编号、单独验收、单独留证
- 编号：执行时从**下一可用 T 号**顺序分配（当前下一可用为 T185；本方案不预写占位号）
- 共同写域：`h/habermas.md`；账本 `tasks/h/habermas.ledger.yaml` 只在需要同步时改
- 共同证据目录：`state/axis/habermas/`（按轴一文件）

## 六个原子任务

| 轴 | 名称 | 范围与手段 | 验收 | 证据 |
| ---- | ---- | ---- | ---- | ---- |
| **q1** | 版面（rv-03） | 表格/图/标题层级/空行/图注/图片引用闭包；`check_tables_images --gate`、`check_images`、`check_layout` | 0  issue；表图与源结构对应；无孤图 | `state/axis/habermas/q1-layout.md` |
| **q2** | 体例（rv-04） | H1 中英题＋作者、pubinfo 引块、尾节顺序、编号点号式、脚注/译者注释位置；`check_style`、`check_pairs`、`check_quotes` | 0 issue；尾序 canonical；编号与源一致 | `state/axis/habermas/q2-style.md` |
| **q3** | 术语（rv-05） | 术语/人名登记核对；D1–D5 定性；三出口（改/登记/豁免）；`check_terms --docs`、`check_term_concepts` | 硬错误 0；告警逐条处置；无未登记新词 | `state/axis/habermas/q3-terms.md` |
| **q4** | 事实（rv-06） | 日期、人物、机构、著作名、论点归属逐项回源/权威核对；无法回源者标“待核”并说明 | 无未支撑事实；待核项有清单与理由 | `state/axis/habermas/q4-facts.md` |
| **q5** | 引用（rv-07） | 脚注标记/定义、书目条目、引文边界、页码/版本；`check_academic --strict`、`check_quotes`、`check_pairs` | 标记/定义全等；引文与源一致；无悬空引用 | `state/axis/habermas/q5-citations.md` |
| **q6** | 语言（rv-08） | 语体、反欧化、标点、长句；`check_prose`、`check_style`；告警逐条改/豁免 | 告警清零或逐条豁免；无新欧化句式 | `state/axis/habermas/q6-language.md` |

## 依赖与顺序

```
q1 → q2 → q3 → q4 → q5 → q6 → T139（rv-09 体例终校）
```

- 每轴完成即写证据并勾选该原子任务；**T138 本身保持未勾选**，只作容器。
- q3 可复用 T136 的术语结论；q6 可复用 T135 的 `check_prose` 处置表，但必须在六轴门下重跑并重新留证。
- 任一轴发现需改正文，先改 `h/habermas.md`，再复跑该轴与下游轴；不得以“上游已过”为由跳过下游复跑。
- q4 无专用检查器，以源文逐项核对为主，机检只作辅助；不得用“全库门禁绿”替代事实核对。

## 入册规则

执行第一轴前，把六个原子任务按下一可用 T 号写入 `tasks.md` 的 S-1 分区，并在 T138 行注明“已拆为 T…–T…”；同时更新 `results/axioms-tasks.md` 的计数与拓扑序。未入册前不得开工，也不得把 T138 当已完成。

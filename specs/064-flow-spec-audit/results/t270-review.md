# T270 证据：digital-art rv-02＋六轴＋rv-09

- 日期：2026-11-28
- 任务：T270；状态 `rv-01_checked → rv-02_checked → rv-09_checked`
- 范围：`zh/d/digital-art.md` 全件；六轴凭据落 `state/axis/digital-art.*`

## 一、rv-02 两轴比较

| 项 | zh | en | 结论 |
| ---- | ---- | ---- | ---- |
| 账本段 | 158 | — | `step2` 回放与正文（除 H1／pubinfo 与句内译注）逐字相等 |
| 标题 | 16（H2 9＋H3 7） | 16 | 顺序与编号一致 |
| 正文段（§1–§5） | 24／9／9／16／8 | 24／9／9／16／8 | §5 多 1 段为句内译注 |
| 引块 | 9 组 | 9 组 | 出版信息引块 +1、学术工具改列表 −1，净数相同 |
| 列表 | 13＋学术工具 4 | 13 | 学术工具按体例转列表 |
| 脚注定义 | 60 | 60 | 键集完全一致 |
| 代码块 | 1 | 1 | ASCII 兔子，闭合 |

- 审计独立性（同源盲区对冲）：同一 actor 情形下采用“冷置回读”——T261–T267 全部落盘后隔批重读全文，并以密度统计补偿（段数 158、汉字 18,988、定义 60、年份集合 38）复算，不以初译记忆代审计。

## 二、六轴

### q1 引文（`cite_audit --gate`，问题 0）

- 直引级候选 23（inline 19、block 4）；全部 `pass`，anchor 落 `loc`，hash 锁定。
- 引文均为英文著作中译；原文语种标 `en`，原始版本 `unavailable`（以 `en/` 为源），无待补原文。

### q2 逻辑（`logic_audit --gate`，问题 0）

- 散句 442；`logic_bearing` 153，全部裁定 `equivalent`；其余 289 `trivial`。
- 算子候选 3 条：`each`／`all`／`some` 的计数差异均为汉语分配式表达（“每个”“所有”“某些”），语义等价，判 false-positive（不计缺陷）。

### q3 语法（`grammar_audit --gate`，问题 0）

- 46 条 G-11（长句 17＋“的”链 29）逐条 `waived`，理由同 T268 tr-04。
- 1 条 G-7（“无论……也即便……”关联词错配）已改写为“无论……还是……”，重跑后消除。
- G-1／G-5 为 0；和制汉语无命中。

### q4 语域（`register_audit --gate`，问题 0）

- 5 节全部 R-1（学术书面语），无 R-4／R-5 越界。
- 3 条 R-d“文言连词‘是以’”为 `以数字方式`／`以悲剧收场` 子串误报，全部 false-positive。

### q5 计量（`measure_audit --gate`，问题 0）

- 量值条目 0；数值范围 6：正文 2 处用一字线（`0—50`、`2010—2023`），引文页码 4 处用 en dash（`117–8`、`224–43`、`60–97`、`37–38`）。
- M-6“连接号混用”为聚合告警：正文范围与引文页码分属两种体例，判 false-positive。

### q6 标点（`punct_audit --gate`，问题 0）

- 4 条 P-13 均为引文页码 en dash，`waived`（与既有件口径一致）。
- 正文数值范围改一字线后无新增；P-8／P-20 为 0。

## 三、rv-09 体例终校

| 检查 | 结果 |
| ---- | ---- |
| `check_style --docs` | 0 |
| `check_quotes --docs` | 0（直角引号 0） |
| `check_pairs --gate` | 0（tail-order／h1-form／pubinfo-form／errata-apply／note-anchor 全过） |
| `check_terms --docs` | 硬 0、疑似缺译法 0 |
| `check_academic --strict` | 无硬错误（在途豁免） |
| `check_math_zh --strict` | 0（本件无公式） |
| `check_all` | 23/23 全绿 |

结论：六轴与 rv-09 通过；状态至 `rv-09_checked`。继续 T271（sg-01／sg-02；sg-03 待 mandate）。

# T242 证据：logic-dynamic rv 全链

- 日期：2026-11-28
- 任务：T242（T158 拆站第 8 项）；状态 `tr-04_checked → rv-01_checked → … → rv-09_checked`
- 对象：`zh/l/logic-dynamic.md`；凭据目录 `state/axis/`（本地运行态，按 `.gitignore` 不入库）

## 一、逐环节结果

| 环节 | 机检 | 结果与处置 |
| ---- | ---- | ---- |
| rv-01 术语轴 | `check_terms` | 硬错误 0、词条告警 0；人工对照 22 条 PDL 登记术语：D1 两处（“复杂度”混形 5 处统一为“复杂性”；“确定”改“是确定的”1 处），无 D2–D5；`mech_audit` pure／conn／susp 均 0 |
| rv-01 体例／勘误轴 | `check_pairs --gate`、`check_style`、`check_quotes` | 全 0；尾节序、编号、H1、pubinfo 均过；勘误 3 行承载均“无需译注” |
| rv-02 审计已译 | `check_math_zh`、`check_style`、`check_pairs`、`check_academic --strict` | 逐段回 en 复校，Critical／Major／Minor 均 0；H2 9／H3 10 同构、55 脚注键同序、表行 6/6/8/15 一致、图 2 路径基座正确；破折号 25 对（en 23）、“一个”65 处、AI 套话 0；单会话以密度统计＋冷置回读补偿（ADR-0020） |
| rv-03 引文 | `cite_audit --gate` | 直引级候选 10，全部为语义读法／记法括注（q1 §1 边界），逐条 `waived`；无原文补入义务；hash 10/10 守恒 |
| rv-04 逻辑 | `logic_audit --gate` | 骨架 365 句，逻辑承载 104 句逐句人审全部 `equivalent`；261 句 `trivial`；算子候选 3 处均假阳性（no→不使用、some→某一次、if→当…时） |
| rv-05 语法 | `grammar_audit --gate` | 告警 0；G-1／G-3／G-5／G-7 无命中；反欧化 0；仅用定型日源词，无未定形生造词 |
| rv-06 语域 | `register_audit --gate` | 5 节均 R-1（说明段 R-2），无 R-4／R-5 越界；R-d 候选“总是以 B 为后条件”判假阳性；AI 腔 0 |
| rv-07 计量 | `measure_audit --gate` | 量值-单位对 0、范围 0；18 处 M-4 候选均为 model2／A2／A3／SP2 等标识符，判假阳性；无换算 |
| rv-08 标点 | `punct_audit --gate` | P-7 冒号套用 1 处已改为逗号；P-18 两处为公式剥离假阳性；其余硬档零命中 |
| rv-09 体例终校 | `check_style`、`check_quotes`、`check_pairs --gate`、`check_math_zh`、`check_terms`、`check_academic --strict` | 全 0；尾节、H1、pubinfo、脚注恒末位均过 |

## 二、全件指标

573 行／9,685 汉字；账本 251 段守恒；602 行内公式、4 display 对、55 脚注定义、2 图、H2 9／H3 10。

结论：rv 全链通过，无 Critical／Major 遗留；状态至 `rv-09_checked`。

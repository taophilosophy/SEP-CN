# 任务书：审计已译环节增项与存量撤销（audit-stage-tasks）

**版本**：v1.0 | **日期**：2026-11-14 | **状态**：任务书交付（本会话仅出任务书，不执行具体任务——用户指令「你仅出任务书。具体任务交付给 s3_checked 之前的阶段，既有 s3_checked 完成的也撤销到该任务之前」）

## 1. 方向声明（rules/08 §1）

* **意图复述**：用户裁定四张预研卡（specs/025 §7 P12–P15）批准落地，但**本会话只产出任务书**；新增检查项的具体执行作为 **audited 阶段（s2_checked → s3_checked 之间）的例行作业**交付给执行会话；已推进到 s3_checked 及之后的在途任务**回滚到该阶段之前**重过。
* **目标**：四张任务书（T1 环节增项执行卡、T2 存量撤销卡、T3 PPL 预研卡、T4 量化基线卡）＋两件机件（FR-001/002，已实现并测试）。
* **非目标**：本会话不执行 T1–T4 的具体作业；不改任何词条语料；done 词条不在 T2 撤销范围（由 specs/023 回炉承接同一增项，承 [ADR-0040](../../rules/adr/0040-审计已译环节与题注编号.md) 决策 5；如需含 done 的状态机回滚，另行裁定）。
* **验收判据**：T2 执行后，state ∈ {s3_checked, r1_reviewed, r2_reviewed, r3_reviewed} 的在途任务清零（全部回滚至 s2_checked）；T1 执行后每词条 audited 凭证含密度统计与新规则处置记录；T3/T4 各出报告一份。
* **作废条件**：新机检误报失控（同类误报 ≥10 处未沉淀白名单，承 fang-fa-lun S5）；连接号类符号归一出现语义误伤重演（specs/026 教训）；T2 回滚误伤 done 或 cleared 任务。

## 2. 机件基线（已实现，任务书引用不重做）

* **FR-001 审计独立性机检**：`tools/task_ops.py` `_audit_independence_gate`——audit 与初译 actor（retranslate 取 draft、update 取 s1）全同且 evidence 无“冷置/密度”记明即拒绝（specs/004 W11 同源盲区对冲；单测 `test_audit_independence_same_actor_requires_compensation` 等，34 测试绿）。
* **FR-002 check_prose 三则**：`tense-adverb`（曾于/已于+纪年）、`conj-he-verb`（“和/与/及”连接动词对或“，和”接分句）、`chenggong-de`（“成功地”）——告警级，登记 rules/05（2026-11-14 扩项）。

## 3. T1 审计环节增项执行卡（交付：audited 阶段执行会话，逐词条）

| # | 作业 | 依据 | 凭证 |
| ---- | ---- | ---- | ---- |
| 1 | `check_prose` 三则新告警（tense-adverb/conj-he-verb/chenggong-de）逐条人工判断后修改或豁免，禁机械改写 | rules/02 反欧化条款、fang-fa-lun S5 | evidence 记处置数与豁免留痕 |
| 2 | **密度统计**：全篇破折号数、量词“一个”频次、AI 高频词共现——写入 evidence（单会话审计必做，即独立性补偿） | rules/04 审计环节“全局”；specs/004 W11 | evidence 记「密度：破折号 N／一个 M／AI 词 K」 |
| 3 | AI 腔五形态走查（增译套话／空洞拔高／模糊归因／公式化排比／高频词密度） | rules/02“AI 腔与套话” | 逐处处置记录 |
| 4 | 译者省略“[……]”体例核验（引文含省略号的词条） | rules/02 内容纪律（CY/T 122 §7/§8） | 逐处核验记录 |
| 5 | 表身空值细则核验（含表格词条：不适用空白／无法获得一字线／零填 0） | rules/02 排版元素（CY/T 170） | 逐表核验记录 |
| 6 | 文字技术整理十项裁剪清单走查（注码注文相符、图表编序连续、目录与标题一致、插图说明相符等） | rules/04 审计环节“全局”（《图书校对工作基本规程》） | 十项逐项勾选入 evidence |

**验收**：上述六项 0 未处置或逐条豁免留痕；audited 凭证形态＝「三向比对记录＋密度统计＋新规则处置」三段齐备。

## 4. T2 存量撤销卡（交付：治理/管线会话）

* **范围**：`tasks/` 下 state ∈ {s3_checked, r1_reviewed, r2_reviewed, r3_reviewed} 的**在途任务**，逐条回滚到 **s2_checked**（重过 audited＋s3）。执行前逐条 `task_ops show` 快照存本 spec `results/rollback-baseline.json`。
* **done 词条不回滚**：由 specs/023 回炉承接 T1 同款作业（023 范围即 drafted 及其后含 done），承 ADR-0040 决策 5「不走 reopen」；cleared/pending/drafted/s1/s2 任务本就未到审计点，不在范围。
* **工具前置（本任务书内的工具任务）**：`task_ops.py` 现无状态回滚命令（`reopen` 仅 done→pending；tasks/README 禁手改状态字段）——实现 `rollback <slug> --to s2_checked --reason <因>`：仅允许 T2 范围内的状态迁移，steps 追加 `{"step": "rollback", ...}` 留史，旧 steps 不删；单测锁定（回滚后 advance audit 须带补偿 evidence）。
* **验收**：回滚清单与快照逐条对账 0 差异；回滚后任务推进 audited 必须走 T1 增项。

## 5. T3 PPL 通道预研卡（P12；交付：管线会话）

1. 选型：本地小模型 CPU 推理（如 qwen2.5-0.5B 类）或批量 API 打分，二选一先试金石（≥3 词条）。
2. 抽样：023 已审词条（缺陷已知）＋未审词条各若干，产出 PPL 分布报告 `results/ppl-pilot.json`。
3. 对照：高 PPL 段落与已知缺陷（翻译腔/AI 腔）重合率分析，划定告警阈值。
4. 验收：预研报告一份（含选型结论、重合率、阈值建议）；**告警级不进门禁**（ADR-0033 口径：非关键词检测器）。

## 6. T4 量化基线卡（P13；交付：管线会话）

1. 数据源：specs/023 台账已审词条的 Critical/Major/Minor 逐条记录＋字数。
2. 模型：差错率＝（计错数÷千字），四档分值映射试算（CY/T 266：2/1/0.5/0.1；校对规程灭错率递进 75%/75%/≤1‱ 作参照）。
3. 产出：`results/quant-baseline.md` 基线报告——只出报告供裁定是否立线，**不设门**。

## 7. 风险与未决

| 项 | 影响 | 处理 |
| --- | --- | --- |
| 新机检误报 | 复核负担增大 | 误报按 S5 沉淀白名单；失控即回退规则（作废条件） |
| T2 回滚与并行会话竞态 | 回滚目标被同时推进 | 执行前 reflog/show 快照核对归属（specs/004 W9 教训）；冲突态冻结 |
| T3 本地模型不可用 | 预研受阻 | 改 API 批量打分口径，成本入 evidence |
| done 是否纳入状态机回滚 | 与 ADR-0040 决策 5 的取舍 | 本任务书按「023 承接」执行；用户改判则 T2 范围扩并补 reopen 批量卡 |

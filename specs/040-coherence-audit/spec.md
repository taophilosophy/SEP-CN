# specs/040-coherence-audit：全系统融洽性审计（数理逻辑证明＋计算）

**状态**：进行中 | **日期**：2026-11-17 | **承办**：pc6 主会话

## 方向声明（rules/08 §1）

* **意图复述**：用户要求"从数理逻辑角度证明、计算目前翻译全流程、规则、工具链是融洽的，有问题的地方列举到某个文件中"；追加"全面证明上述内容的工具链能否实现任务要求目的（先证明要求目的成立）"；约束"覆盖度 100%""已完成的任务只审计既有尚在成果"。
* **目标**：①把现行规范层（宪法＋rules/01–09＋65 件 ADR＋tasks/README＋cli.md 契约）与工具链（59 具 tools 脚本、11 项门禁＋单测）建成形式模型，逐性质判定融洽；②先证明"要求目的"命题 Φ 本身良构（无冲突、可判定、可满足），再证明工具链对 Φ 的充分性并给出残差；③全部缺陷集中登记于 `results/findings.md`（唯一问题清单文件）。
* **非目标**：不修任何缺陷（只登记）；不重审已销案 specs 的历史过程；不改变更链与状态机语义。
* **验收判据**：本 spec 给出模型与两条证明；`bin/audit_coherence.py` 跑通并落 `results/audit-report.json`；findings 逐条带 file:line 证据；审计只读（除本 spec 目录三文件）。
* **作废条件**：若计算发现架构级矛盾（裁决序不可消解、门禁与规范根本相左）则本结论作废，升级为整改任务。
* **适用规范基线**：GB/T 1.1-2020（助动词分级，条文用语）；IEEE 1028 Audit 型独立审计（本任务自审＝审计面，判官只读，见 rules/05 判定权表）。

## 一、系统目的命题 Φ（从宪法与 AGENTS.md 提取）

Φ ≝ "在本仓约束下产出并持续维护 SEP 简体中文译本，使每一件中文成品满足以下子目标，且全程可审计"：

| 号 | 子目标 | 内容 | 权威 |
| ---- | ---- | ---- | ---- |
| Φ1 | 版本钉 | 每件成品可回溯 pubinfo＋存档版名＋SHA-256 | 宪法 I、rules/06 §审计 |
| Φ2 | 保真链 | en/＝原始钉（I1）；yuanwen＝convert(en⊕补丁)（I2）；文字流等值（I3）；补丁准入＋命中计数（I4） | ADR-0062/0063 |
| Φ3 | 结构完整 | SUMMARY 唯一源、镜像、节集合、脚注配对、图片闭合 | rules/01/07 |
| Φ4 | 体例合规 | 引号/空格/表格/公式/尾序/编号/H1 | rules/02、ADR-0063/0065 |
| Φ5 | 术语一致 | 两登记册单源、先登记后使用、禁机械替换 | rules/03 |
| Φ6 | 语言质量 | 现代汉语学术书面语、禁文言/欧化/AI 腔 | rules/02 §语体、ADR-0033 |
| Φ7 | 内容正确 | 零幻觉引文、逐条对照搬运、零信任 | rules/07 |
| Φ8 | 流程可审计 | 13 步状态机、append-only steps/evidence、复核独立性、r3 用户指定 | rules/04、ADR-0052/0054 |

## 二、定理一：Φ 良构（要求目的成立）

**（a）无冲突性（在裁决序下）**。子目标间不存在不可消解的义务冲突：唯一看似相斥的面是"Φ2 冻结（禁改 en/）× Φ7 要求改正上游缺陷"——ADR-0062 以分流消解：en/ 冻结为字节事实，改正读法分两路承载（全局勘误表＋中文译注、格式补丁池），缺陷知识不丢失、冻结不破（ADR-0062 决策 2–4，rules/README 判例）。同理 Φ5 的"全库一致"×"条目主题优先"由 ADR-0048 D1–D5 消解；Φ6 的语义判定×机器不可判由"人审＋留痕机检"消解（rules/02 §检查）。裁决序为全序：宪法 > rules > specs > 生成物，ADR 只追加、新代旧显式登记（rules/README §规范层级；rules/adr/README 编号约定）——计算面证实 26 处取代关系显式可追、65 件编号连续、全库 60 个 ADR 引用零悬空（results/audit-report.json §C）。

**（b）可判定性**。每个子目标都有三型验收判据之一：①机器谓词（Φ1–Φ4、Φ5 一致性面、Φ8：GATES 11 项＋状态机步级挂钩）；②留痕机检（Φ6/Φ7 的语义结论由人作出、其"是否留痕"由机检验：task-style-attest、evidence 必填、--mandate 硬门、独立性机检，check_academic.py:414–431、task_ops.py:139–177）；③人审判据带凭证强制（语体/术语正确性：evidence 五属性，rules/09 §3）。判据缺失面为零——findings 中无一条"目的无判据"。

**（c）可满足性（witness）**。①仓库级：`check_all` 12 项全绿（本会话开工实测，2026-11-17）；②件级：现存 done 任务 2 件，version_pin 完备 2/2，且通过 check_academic 的 task-pin/task-evidence/语体留痕机检（phi_witness，audit-report §D）；③保真链级：divergence verify 全 pristine（4410 件，GATES 第 10 项绿）＋fidelity 门绿（GATES 第 11 项）。∴ Φ 非空可满足。□

## 三、定理二：工具链对 Φ 的充分性（分解证明）

**T1 机器可判定面：完备**。Γ: Φ 的机器可判定子目标 → {GATES, 步级挂钩}，逐项验证（audit-report §A/B 与本会话读码）：

| 子目标 | 判官（只读） | 挂载点 |
| ---- | ---- | ---- |
| I1 en＝钉 | `divergence.py verify` | GATES[10]；check_all |
| I2/I3 yuanwen 保真 | `check_yuanwen_fidelity.py --gate` | GATES[11]；md-hand-edited/source-drift/text-stream-diff |
| I4 补丁准入＋命中 | `en_patch_lib.py`（C2 谓词）＋`check_en_patches.py`＋yuanwen.py 转换层硬失败 | 转换内嵌＋离线体检 |
| Φ3 结构 | check_summary（H1/别名/空组硬门）、check_mulu_s、check_images --gate、check_academic（脚注配对）、check_pairs --gate | GATES[1,2,5,8]＋s2.4 _style_gate |
| Φ4 体例 | check_quotes、check_style、check_math_zh --strict、check_doc_size、check_junk | GATES[3,4,6,7,9] |
| Φ5 一致性 | check_terms（自洽硬）＋s24 _term_gate | GATES[6]＋s2.4 挂钩 |
| Φ8 流程 | task_ops 禁跳步/changes:/mandate/独立性/s0 前置＋check_academic 任务面 | 步级挂钩五处 |

CI 侧单一事实源在实现层成立：checks.yml:32 实跑 `check_all.py --list-gates` 生成矩阵（读码证实），本地与 CI 同源无"多查一项"。

**T2 语义面：受控人审＋留痕闭环**。Φ6/Φ7 的语义判断不可机检（ADR-0033 明文禁关键词机检），工具链的承载方式是"人判→evidence 留痕→机检查留痕"：语体结论（check_academic task-style-attest，步级时点 ADR-0058）、r3 mandate（--mandate 缺失即拒）、复核独立性（actor 同源须"冷置/密度"记明）、evidence 非空（advance 强制）。闭环在实现层完整（task_ops.py:139–201、check_academic.py:405–431）。

**T3 残差（工具不可判，由流程补偿）**：

| 残差 | 补偿控制 |
| ---- | ---- |
| 术语译名"正确性"（对错，非一致） | 登记册先登记后使用＋D1–D5 查证凭证＋告警三出口（rules/03） |
| 语体优度、破折号功能 | 复核人语义通读＋留痕机检（rules/02 §语体） |
| 引文内容逐条忠实 | s1/r2 逐句回源人审＋mech_audit 回溯候选（rules/07 禁幻觉） |
| 上游时效（上游已变未抓） | drift_scan/compare 按需回源（登记面，非实时） |
| 站点部署时效 | 壳仓定时拉取兜底（cron 实测失准已登记 ADR-0064，属外部面） |

**结论**：工具链能实现 Φ——机器可判定面逐项有谓词且入闸（T1），语义面有留痕闭环（T2），残差均有显式补偿控制（T3）。"能否实现"的答案为**能**，其证明依赖 findings 中登记的文档滞后项被收敛（它们削弱"文档声称＝实现事实"这条元性质，不削弱实现本身）。

## 四、形式模型与计算

设 D_norm＝规范文本集、D_tool＝tools/*.py、D_data＝baseline/tasks/数据。融洽性判定为四层：

1. **LTS 层**：任务状态机 M＝(S_kind, s0, →, done)。→ 由 task_ops.STEP_EXPECT_PREV（实现）∪ clear/reopen/revert 命令边构成；文档侧由 tasks/README 状态块声明。判定：P1 文档≡实现（逐态出现，PASS，0 缺）；P2 可达性（两 kind 全态可达、无死端，PASS）；P3 目标态∈ORDER[kind]（FAIL×1：update 经 draft 漂入 drafted，F-01）；P4 前驱唯一性（FAIL×3：s0/s1 元组并集语义跨 kind 互通、audit 死条目，F-02/F-03）。
2. **Γ 层**：GATES（11＋单测）↔ 规范锚与登记面。判定：锚完备（11/11 在 rules/05 工具表，PASS）；登记完备（FAIL：16 具未入 tools 表，F-09）；计数一致（FAIL：rules/05/06/09 六处过时，F-08）。
3. **ADR 链层**：(ADR, ⊳) 偏序＋引用集。判定：编号连续、零悬空、26 处取代显式（PASS）；索引/正文状态一致（FAIL×1：ADR-0017，F-11）；引用语义正确（FAIL×2 工具错引，F-12）。
4. **声称-事实层**：文档数字 vs D_data。判定：门禁计数（FAIL，F-08）、rules/01:80 行数声称（FAIL，F-14）；数据面全吻合（divergences 0/113、补丁池 3=3、基线 1872/钉 4524/yuanwen 1872、勘误表 §八起 31 行，PASS）。
5. **规范语义层**：O/F 冲突通读裁定（FAIL×4 组＋2 处规则间冲突，F-19~F-24）。

计算器：`bin/audit_coherence.py`（只读；stdout JSON→results/audit-report.json，stderr 摘要）。

## 五、总裁定

**系统融洽（结构层成立，文档层带 29 项登记缺陷）**：架构无不可消解矛盾——状态机线性健全、门禁-规范映射完备、ADR 链闭合、判官只读成立、写路径读回核验在位、目的 Φ 良构且工具链充分。全部缺陷（findings.md F-01…F-29）均为一行级文本/谓词/登记修正，无一触及架构。按 rules/08 §14，各缺陷修复时填四件套（谓词/命中数/幂等/回退）。

## Assumptions

* "融洽"取三义：规范层无不可消解冲突（consistency）、状态机健全（soundness）、文档-实现-数据三面对账（correspondence）；不承诺完备性（未被规则禁止≠允许的完整性判定不在本任务面）。
* 2026-11-16"取消双机定岗"的用户裁定仅存于项目记忆、库内无 ADR——按"只审计现行成果"以库内条文为准，该差异列为 F-24 待用户裁定收编或否认。
* 三处脏区（ri-zhi、en-errata、036 execution-log）为本会话开工前既有，未纳入审计亦未触碰。

# specs/041-axiom-system：项目公理体系与形式化充分性审计

**状态**：进行中 | **日期**：2026-11-17 | **承办**：pc6 主会话

## 方向声明（rules/08 §1）

* **意图复述**：用户要求"为整个项目，基于当前软件工程理论和规则，工具链，建立公理体系，形式化充分性审计"。
* **目标**：①从宪法七原则、rules/09 已映射的软件工程理论（ISO/IEC/IEEE 12207/15289/1028/1044/15939、ISO 17100/18587、GB/T 1.1、CY/T 系列、MQM）与现行工具链中提炼一套公理体系（原语＋公理＋推演规则）；②对其做形式化充分性审计——公理层（锚存在、无冲突、非冗余）、接地层（规范↔公理、门禁↔公理双向 grounding）、目的层（Φ1–Φ8 可由公理导出）三面全绿；③缺口如实登记。
* **非目标**：不改任何规则、工具与门禁（纯审计层，判官只读）；不重述 specs/040 已完成的缺陷台账（其复算结果作为本审计的输入事实）。
* **验收判据**：`bin/axiom_audit.py` 跑通且 `results/axiom-report.json` 全绿（或缺口逐条登记于 findings）；登记册 `results/axioms.md` 每行机检通过。
* **作废条件**：发现公理间不可消解冲突，或 Φ 某子目标无法由公理集导出且无补偿控制。
* **适用规范基线**：GB/T 1.1-2020（助动词）、ISO/IEC/IEEE 12207 §技术过程、15289 §信息项、ISO 17100 §5.5.4（复核独立）——均已在 rules/README"规范性引用标准"节登记版本钉，按 rules/08 §13 引条款号不重读全集。

## 一、原语（不定义，仅约定用法）

`Entry`（词条）、`En(e)`（e 的原始抓取字节）、`Pin(e)`（e 的版本钉三元组）、`Deriv`（转换算子：En→Yuanwen→Zh）、`Task`（状态机实例）、`Step`（append-only 步记录）、`Evidence`（可复核凭证）、`Registry`（登记册行）、`Gate`（只读判定谓词）、`Session`（会话/actor）。

## 二、公理（14 条，四组）

命题均为全称断言；判面三型：**机检**（谓词＋入闸）、**留痕**（人判结论＋机检查痕）、**纪律**（无载体，例外须显式批准）。权威锚与机器载体逐条登记于 `results/axioms.md`（机读行，计算器逐项核验存在性）。

**组 I·真相（Truth）**

* **A1 钉一致**：∀e: bytes(En(e)) = Pin(e)。en/ 是上游字节事实，任何变动禁止；偏离唯一出口＝补丁池（格式层，命中计数硬校验）。〔宪法 I；ADR-0027/0062〕
* **A2 源唯一裁决**：译文命题的正确性唯一裁决对象是 En(e)——既有中文译文、缓存、脚本中间产物、模型记忆一律不作底稿或修改依据；可疑处回 En 核对。〔宪法 I；rules/04 重译纪律〕

**组 II·记录（Record）**

* **A3 三元钉可追溯**：每件成品可回溯 (pubinfo, archive_edition, sha256)，登记于 baseline 与任务 JSON；版本事实由登记数据说了算。〔宪法 I/II；rules/06 §审计；rules/07 版本事实〕
* **A4 只追加**：En、Yuanwen、Task.steps、divergences(tombstone) 只追加不改写；不可变语义由版本历史承担。〔宪法 II；rules/09 §3 信息项保留〕
* **A5 单一事实源**：每类事实域恰有一个登记源（结构=SUMMARY、术语=shu-yu-biao、人名=ren-ming-biao、版本=baseline、任务=tasks）；两处不一致时修弱势方。〔宪法 III；ADR-0012/0036；rules/06 登记表〕

**组 III·过程（Process）**

* **A6 流程先行**：无方向声明（意图/目标/非目标/验收判据/作废条件/规范基线）不入质量门；写不出视为未立项。〔宪法 IV/VII；rules/08 §1；rules/06 质量门〕
* **A7 禁跳步**：任务状态转移仅沿 ORDER[kind] 相邻对（合法前驱由单一事实源推导），目标态越界即拒；blocked 冻结一切转移。〔rules/04；tasks/README；task_ops.expected_prev——specs/040 F-01/02/03 收口〕
* **A8 复核独立**：校者应独立于译者且资质相当（ISO 17100 §5.5.4）；单会话形态须冷置/密度补偿并在 evidence 记明，机检实拦。〔rules/04 复核独立性；rules/09 §2 角色约束；ADR-0020/0058〕
* **A9 终审主权**：R3 仅用户显式指定的会话执行（--mandate 硬门，缺失即拒，step 留 mandate 字段）；未指定时条目停 r2_reviewed。〔ADR-0054〕
* **A10 单写入者**：主代理单干，禁止子代理/workflow 扇出；写入路径唯一、核对链闭合；例外仅用户当轮显式批准。〔ADR-0034〕——纪律面（违例处置：不计入质量门、逐条重做重验）。

**组 IV·机器（Machine）**

* **A11 判官只读＋四件套**：判定器不得同时具备写回能力；规则升门须填机检谓词/预期命中数/幂等证明/一行回退。〔ADR-0063 判定权表；rules/05 判定权节；rules/08 §14〕
* **A12 显式失败＋礼貌**：禁静默跳过与静默兜底降级——前置失配即硬失败（缺失补丁池＝硬失败、残余≠0 禁写回）；HTTP 相邻请求 ≥5 秒、4xx/5xx 退避留痕。〔宪法 V；rules/05 生成器前置门；en_patch_lib.PatchPoolMissing；fetch.py 节拍〕
* **A13 先登记后使用＋禁机械替换**：术语/人名先登记后使用；语义层变更禁以 sed/re.sub 批量套改，修复以句/段为单位回源重译。〔宪法 VI；rules/03 NON-NEGOTIABLE；ADR-0048〕
* **A14 可追溯写**：结构化落盘一律写后读回核验（写临时→比对→原子替换→再核验），任何不符即抛错。〔宪法 II（SMB 假成功实证）；common.write_json_verified/write_text_verified〕

## 三、推演规则（自公理到条文/工具的推导形状）

* **R1 钉→门禁**：机检面公理的可执行谓词必须入 GATES 或步级挂钩（A7/A11/A12 联合蕴含）。
* **R2 单源→校验工具**：每登记源须有对应性校验工具（A5 ⇒ check_summary/check_terms/check_mulu_s/register_lib 三口径唯一实现）。
* **R3 失配→拒绝**：一切前置谓词失配＝拒绝推进（exit 3），禁降级放行（A12）。
* **R4 人判→留痕**：语义结论必须落 evidence 且 done 前机检查痕（A6/A8 ⇒ task-style-attest、evidence 必填）。
* **R5 语义变更→回源**：词面/句法/术语变更必须回 En/Yuanwen 对照后逐处人工改（A2/A13）。
* **R6 不可逆→方向声明＋护栏**：结构重排/批量改写/数据格式/对外发布前置 A6 与回退保障（宪法 VII；rules/05 生成器纪律）。

## 四、定理（本审计判定对象）

* **T1 门禁覆盖**：全部机检面公理的谓词已入闸（11 GATES＋5 步级挂钩，无缺载）。〔计算器 S3 反向接地〕
* **T2 保真链**：I1≡A1；I2/I3＝A1+A4+R1（fidelity 门）；I4＝A4+A12（补丁池准入＋命中计数）；I5＝A5+R2（check_pairs 体例硬档）；I6＝A13（mech_audit 回溯）。〔ADR-0063 不变量表〕
* **T3 状态机健全**：A7 ⇒ 全态可达、无死端、严格前驱——specs/040 audit v2 A 组零违例复算为证。
* **T4 一致性**：公理间无 O/F 冲突——规范层冲突面（specs/040 G 组）已清零；残余张力（冻结×改正、全库一致×条目主题优先、语义判定×机器不可判）各有裁决性消解（ADR-0062 分流、ADR-0048 D1–D5、ADR-0033 留痕机检）。
* **T5 非冗余**：每条公理至少有一条独占规范（删它则该规范失去裁决根基）——登记册"独占"列逐条给出。
* **T6 充分性**：Φ1–Φ8 每项由公理子集导出且有现行 witness（导出表见 §六，计算器逐项核验载体存在）。

## 五、形式化充分性审计（判定面定义）

充分性 ≝ 以下五面全绿：

* **S1 锚存在**：每条公理的全部权威锚（file::keyword）在库内现行文本中命中——无凭空公理。
* **S2 载体存在**：每条公理声明的机器载体（gate/tool/hook/impl）真实存在于工具链——无虚载。
* **S3 反向接地**：每条门禁/挂钩/不变量工具可上溯 ≥1 条公理——无无根基的强制力。
* **S4 正向接地**：每条硬约束规范（AGENTS 硬约束速览＋rules/09 阶段门禁列）可映射 ≥1 公理——无无根基的义务。
* **S5 目的导出**：Φ1–Φ8 每项给出公理子集＋witness——目的不是悬空口号。

计算器：`bin/axiom_audit.py`（只读；S1–S5 逐项判定，输出 results/axiom-report.json）。登记面：`results/axioms.md`（公理行＋正向接地表＋Φ 导出表三节，均机读）。

## 六、Φ 导出表（S5 内容，登记于 axioms.md §三）

| 子目标 | 公理子集 | witness（现行载体） |
| ---- | ---- | ---- |
| Φ1 版本钉 | A3, A4 | GATES academic（task-pin-missing）＋baseline/entries.json |
| Φ2 保真链 | A1, A4, A11, A12 | GATES divergence＋fidelity；check_en_patches；en_patch_lib |
| Φ3 结构完整 | A5, R2 | GATES summary/mulu/images＋check_academic 脚注配对 |
| Φ4 体例合规 | A11, R1 | GATES quotes/mathzh＋check_style＋check_pairs --gate（s24） |
| Φ5 术语一致 | A5, A13 | GATES terms＋s24 _term_gate |
| Φ6 语言质量 | A6, R4 | task-style-attest（check_academic）＋check_prose 告警面 |
| Φ7 内容正确 | A2, A13 | s1/r2 人审留痕＋mech_audit 回溯 |
| Φ8 流程可审计 | A4, A6, A7, A8, A9, A10, A14 | task_ops steps/mandate/独立性机检＋check_academic 任务面 |

## Assumptions

* 公理层是**重构**不是新立法：每条公理的效力来自其权威锚（宪法/rules/ADR 已 accepted 的裁定），本 spec 不新增义务。
* A10 是全系统唯一纯纪律面公理（写入路径唯一无法机检）——其补偿控制＝违例处置条款（rules/06 §子代理禁用）＋审计面抽验。
* 并行会话 yuanwen 重转在途面不属本审计对象；本审计只读 specs/040 复算报告作为输入事实。

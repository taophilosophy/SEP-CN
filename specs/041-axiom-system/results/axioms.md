# 公理登记册（specs/041；机读面，bin/axiom_audit.py 逐行核验）

约定：权威锚＝`路径::关键词`（关键词须在该文件现行文本中命中）；机器载体前缀——`gate:`＝check_all GATES 键、`tool:`＝tools/ 脚本、`impl:模块(符号)`＝模块源码含该符号、`hook:`＝task_ops 步级挂钩族、`discipline:`＝纯纪律面（计算器只验非空）。判面＝机检／留痕／纪律。

## 一、公理（14 条）

| 公理 | 命题（浓缩） | 判面 | 权威锚 | 机器载体 | 独占规范（非冗余凭据） |
| ---- | ---- | ---- | ---- | ---- | ---- |
| A1 | bytes(En(e))=Pin(e)；en/ 冻结，偏离唯一出口＝格式补丁池（命中计数硬校验） | 机检 | .specify/memory/constitution.md::零信任、rules/06-governance.md::原始物双账、rules/adr/0062-en原始物文字冻结与全局勘误表.md::绝对冻结 | gate:divergence、tool:baseline_audit、tool:check_en_patches、tool:en_patch_lib | AGENTS 硬约束"更新流程"行（en/ 绝对冻结面） |
| A2 | 译文命题唯一裁决对象＝En；旧译/缓存/记忆不作底稿 | 留痕 | .specify/memory/constitution.md::既有中文译文一律不作为底稿、rules/04-translation-workflow.md::重译纪律 | tool:mech_audit、impl:task_ops(evidence 必填)、discipline:s1/r2 逐句回源人审 | rules/04 §语体不合规的置空返工（不以旧译为底稿） |
| A3 | 成品可回溯 (pubinfo, archive_edition, sha256)，登记于 baseline＋任务 JSON | 机检 | .specify/memory/constitution.md::版本钉、rules/06-governance.md::每件成品可回溯、tools/task_ops.py::版本钉从基线取（零信任 | gate:academic、impl:task_ops(_version_pin)、tool:baseline_audit | rules/06 §审计"任务 JSON 的 version_pin" |
| A4 | En/Yuanwen/steps/divergences 只追加不改写 | 机检＋纪律 | .specify/memory/constitution.md::只追加、rules/09-process-standard.md::append-only、tools/task_ops.py::append-only | gate:divergence、tool:divergence、impl:task_ops(steps 追加) | rules/09 §3 信息项“永久（append-only）” |
| A5 | 每类事实域恰一登记源；冲突修弱势方 | 机检 | .specify/memory/constitution.md::单一事实源、rules/06-governance.md::单一事实源登记表、rules/03-terminology.md::以登记册 | gate:summary、gate:terms、tool:check_mulu_s、tool:register_lib | rules/06 §单一事实源登记表（整表） |
| A6 | 无方向声明不入质量门；写不出视为未立项 | 留痕 | .specify/memory/constitution.md::流程先行、rules/08-intent-first.md::视为尚未立项、rules/06-governance.md::方向声明缺失视为未立项 | gate:academic（task-evidence-missing）、impl:task_ops(evidence 必填) | rules/08 §1 表（作废条件/规范基线行） |
| A7 | 转移仅沿 ORDER[kind] 相邻对；目标态越界即拒；blocked 冻结 | 机检 | rules/04-translation-workflow.md::禁止跳步、tasks/README.md::禁止跳步、tools/task_ops.py::expected_prev | impl:task_ops(expected_prev)、gate:unittest（test_skip_step_rejected） | rules/04 §任务类型与状态机"禁跳步" |
| A8 | 校者独立于译者（ISO 17100 §5.5.4）；同源须冷置/密度留痕，机检实拦 | 机检（留痕判定） | rules/04-translation-workflow.md::复核独立性、rules/09-process-standard.md::R2 校者应独立、tools/task_ops.py::复核独立性机检 | hook:independence | rules/04 §同源盲区对冲（冷置/密度补偿） |
| A9 | R3 仅用户显式指定（--mandate 硬门，缺失即拒） | 机检 | rules/04-translation-workflow.md::终审会话门槛、rules/adr/0054-终审须用户显式指定会话.md::mandate、tools/task_ops.py::R3 终审须用户显式指定 | hook:r3_mandate | ADR-0054 决策（指定不继承、真实性属审计面） |
| A10 | 主代理单干，禁子代理/扇出；写入路径唯一；例外仅用户当轮批准 | 纪律 | rules/06-governance.md::子代理禁用、rules/adr/0034-主代理单干禁调子代理.md::主代理单干 | discipline:ADR-0034 违例处置不计质量门且逐条重做 | rules/06 §子代理禁用整节 |
| A11 | 判官只读；升门须填谓词/命中数/幂等/回退 | 机检 | rules/05-ci-and-tools.md::判官只读、rules/08-intent-first.md::四件套、rules/adr/0063-中文体例归一入s2.4双轴与转换保真不变量.md::判定权 | tool:check_yuanwen_fidelity、tool:en_patch_lib、impl:check_all(可判性四件套登记) | rules/05 §判定权表（一条规则一个 owner） |
| A12 | 禁静默跳过/兜底降级，失配即硬失败；抓取 ≥5 秒退避留痕 | 机检 | .specify/memory/constitution.md::礼貌抓取与失败显式化、rules/05-ci-and-tools.md::写回前置门、tools/en_patch_lib.py::PatchPoolMissing、tools/fetch.py::5 秒 | impl:en_patch_lib(PatchPoolMissing)、tool:fetch、impl:common(write_json_verified)、gate:junk | en_patch_lib 解析三律（缺失即硬失败，禁静默空池） |
| A13 | 体例即契约：术语先登记后使用；译文必过既有检查；语义层禁机械替换 | 机检＋留痕 | .specify/memory/constitution.md::术语先登记后使用、rules/03-terminology.md::禁止机械替换、rules/adr/0048-术语落地差异处置标准.md::禁机械替换 | gate:terms、tool:mech_audit、tool:term_coverage、tool:term_relations、gate:quotes、gate:mathzh | rules/03 §术语落地 NON-NEGOTIABLE（禁 sed/re.sub 批量套改） |
| A14 | 结构化落盘写后读回核验，不符即抛错 | 机检 | .specify/memory/constitution.md::可追溯与不可变原始物、tools/common.py::写后读回自校验 | impl:common(write_json_verified)、impl:common(write_text_verified) | common.py 零信任约束（SMB 假成功实证） |

## 二、正向接地表（S4：硬约束规范 → 公理）

| 规范（AGENTS 硬约束速览） | 公理 |
| ---- | ---- |
| 知难行易 | A6 |
| 零信任 | A1, A2, A3 |
| 主代理单干 | A10 |
| 单一事实源 | A5 |
| 流程先行 | A6, A14 |
| 提交纪律 | A4, A6 |
| 抓取礼貌 | A12 |
| 抓取完整性 | A12, A1 |
| 更新流程 | A1, A4, A12 |
| 结构形态 | A5, A7 |
| 单体文件 | A5, A11 |
| 批量改写 | A13, A12 |
| 术语落地 | A5, A13 |
| 检查 | A11, R1 |
| 体例归一 | A13, A11 |
| 派生保真 | A1, A4, A11 |

| 规范（rules/09 §2 阶段验证门禁） | 公理 |
| ---- | ---- |
| P0 入库 intake | A1, A12 |
| P0.5 源审计 s0 | A1, A2 |
| P1 初译 draft | A6, A14 |
| P2 一校 s1 | A2 |
| P3 二校 s2 | A13 |
| P4 术语校 s2.4 | A5, A13 |
| P5 审计 s2.5 | A8, A11 |
| P5.5 形态清账 | A11 |
| P6 三校 s3 | A13, A11 |
| P7 三审 r1–r3 | A8, A9 |
| P8 收尾 done | A6 |
| P9 更新 update | A2, A5 |
| P10 战役 | A6, A12 |
| P11 登记册维护 | A5, A13 |

## 三、Φ 导出表（S5）

| 子目标 | 公理子集 | witness（现行载体） |
| ---- | ---- | ---- |
| Φ1 版本钉 | A3, A4 | gate:academic（task-pin-missing）、tool:baseline_audit |
| Φ2 保真链 | A1, A4, A11, A12 | gate:divergence、gate:fidelity、tool:check_en_patches、tool:en_patch_lib |
| Φ3 结构完整 | A5, A11 | gate:summary、gate:mulu、gate:images、tool:check_academic |
| Φ4 体例合规 | A11, A13 | gate:quotes、gate:mathzh、tool:check_style、impl:task_ops(_style_gate) |
| Φ5 术语一致 | A5, A13 | gate:terms、impl:task_ops(_term_gate) |
| Φ6 语言质量 | A6, A8 | gate:academic（task-style-attest）、tool:check_prose |
| Φ7 内容正确 | A2, A13 | tool:mech_audit、discipline:s1/r2 逐句回源 |
| Φ8 流程可审计 | A4, A6, A7, A8, A9, A10, A14 | impl:task_ops(mandate)、hook:independence、gate:academic、impl:common(write_json_verified) |

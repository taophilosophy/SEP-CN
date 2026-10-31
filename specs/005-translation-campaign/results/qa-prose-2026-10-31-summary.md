# A 批全量语言复核汇总（2026-10-31）

**依据**：用户裁定 2026-10-31「全部批准，现在全量复核」（[ADR-0020](../../rules/adr/0020-译文语言质量门禁.md) 后果节）。抽样复核（qa-findings-2026-10-31.md）扩展为全量。
**执行者**：复核会话（只读扫描＋登记，不改词条正文——rules/06 所有权边界）。
**机器凭证**：`results/qa-prose-2026-10-31.jsonl`（162 文件逐条一行，白名单校准后口径）；复跑命令 `python tools/check_prose.py a/*.md s/spacetime-holearg.md`。

## 口径与范围

* 扫描范围：A 批全部 162 个 md ＋ s 批 done 词条 spacetime-holearg；142 个文件零告警（存根/未处理存量）。
* 工具：`tools/check_prose.py`（ADR-0020，告警级），八则反欧化模式；本次按 S5 校准白名单两项（「进行中/的」体貌义豁免、竖线列表行豁免），单测 12 例全过。
* 人工抽验：abduction 全读＋英文镜像逐点核对；action/abelard/academic-freedom 各抽 12 条告警人工判定（de-chain 与 long-sentence 真问题率约八成，余为可辩护的紧凑表达，逐条人工裁量）。
* 术语横扫：16 个 done 词条全查「不完全决定／非充分决定性／不充分决定性」「验证理论／确证」「最佳说明推理／最佳解释推理」及判词（只配/够格）、成语（付之阙如）。

## 全量结果（done 词条 16，告警合计 1075）

| 词条 | 合计 | de-chain | long-sentence | passive-bei | weak-verb | 其他 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| a/action.md | 136 | 83 | 38 | 5 | 9 | men 1 |
| a/action-perception.md | 113 | 65 | 23 | 19 | 6 | — |
| a/academic-freedom.md | 107 | 59 | 29 | 7 | 9 | as-one 2、dang 1 |
| a/abelard.md | 88 | 50 | 24 | 9 | 5 | — |
| a/actualism-possibilism-ethics.md | 79 | 42 | 32 | 4 | 1 | — |
| a/abhidharma.md | 77 | 48 | 16 | 5 | 5 | as-one 3 |
| a/advance-directives.md | 76 | 47 | 29 | 0 | 0 | — |
| a/abstract-objects.md | 73 | 47 | 17 | 4 | 1 | as-one 2、men 2 |
| a/abduction.md | 69 | 28 | 25 | 3 | 10 | men 3 |
| a/abrabanel.md | 55 | 31 | 17 | 5 | 1 | men 1 |
| a/abu-bakr-al-razi.md | 47 | 35 | 8 | 3 | 1 | — |
| a/abortion.md | 39 | 23 | 9 | 4 | 2 | as-one 1 |
| a/abraham-daud.md | 39 | 22 | 7 | 2 | 0 | men 8 |
| a/abilities.md | 35 | 20 | 10 | 4 | 1 | — |
| a/abner-burgos.md | 30 | 22 | 7 | 0 | 1 | — |
| a/abduction.peirce.md（补充材料） | 12 | 5 | 5 | 0 | 2 | — |

非 done 但有告警（各自校次消化，不入返工队列）：a/addams-jane.md（cleared，翻译会话在途 84 条）、a/alcmaeon.md（s1_checked 45 条）、a/african-sage.md（pending，存量旧译文 92 条，重译即消）。s/spacetime-holearg.md（done）零告警。

## 术语与判词横扫

* **术语混形**：仅 a/abduction.md——不完全决定／不充分决定性／非充分决定性三形并用（L57）＋验证理论（×4）与确证（×3）并存；其余 15 词条在本表术语族上无混形。
* **判词/成语误用**：仅 a/abduction.md（L73「只配」、L91「付之阙如」主语错位）。

## 分级与返工队列

* **Critical（定点改，改前回核英文镜像）**：abduction 五项——①L29 made likely→「变得可能」应为「很可能」；②L73 warrant→「只配」＋破句；③L75 句法破散；④L101 reasoner→「说者」；⑤L57 术语三形统一为主形（rules/03 ADR-0020 条款；L433 相关词条行「非充分决定性」为跨词条既定名不动）；附 L143 验证理论/确证取舍（随⑤一并裁定措辞）。行号与英文对照见 qa-findings-2026-10-31.md。
* **Major（s2 语言返工批次，按词条认领）**：上表全部 de-chain／long-sentence／passive-bei／weak-verb 告警——返工会话对每词条复跑 `check_prose.py <路径>` 取全量行号清单，逐条人工判断改写或豁免留痕；优先序建议：action（136）→ action-perception（113）→ academic-freedom（107）→ abelard（88）→ actualism-possibilism-ethics（79）→ 其余。
* **Minor**：as-one／dang-shihou／plural-men 零星项随同词条 Major 批次顺带处理。
* 深度核读现状说明（2026-10-31 更新）：本汇总原为模式扫描＋抽样判定；同日用户裁定「禁止抽样，继续遍历」后，16 done 词条＋补充材料已完成**全读逐段遍历**（中译↔英文镜像逐段核对），accuracy 实锤与返工序以 [qa-traverse-2026-10-31.md](qa-traverse-2026-10-31.md) 全册汇总为准（Critical 15＋1 附／Major 37／Minor 157）；本文件的欧化密度统计（check_prose 口径）继续有效，作为 Major 语言批次的行号清单来源。

## 返工作业程序（翻译会话）

1. `python tools/task_ops.py create <slug> --kind qa-rework`（任务协议 kind 为自定枚举；若 task_ops 限定枚举则用 update 并在 evidence 说明）；
2. evidence 首条写 `changes: specs/005-translation-campaign/results/qa-prose-2026-10-31-summary.md#返工队列`；
3. 状态机按 rules/04 更新任务语义只走变更段（pending → s1（Critical 定点核对）→ s2（语言告警清零/豁免留痕）→ s3 → r3），不复查旧错；
4. 收尾 `check_prose.py <路径> --strict` 0 或逐条豁免留痕 ＋ `check_academic --docs --strict` 0 硬错误。

## 工具校准记录（S5）

* 2026-10-31 白名单两项：`进行中/进行中的`（体貌义术语，action.md 11 条误报）、含 ≥2 个未转义 `|` 的列表行（相关词条行误报）；沉淀于脚本 docstring 与单测（12 例）。
* 升硬观察口径：A 批收口时统计返工后残留告警与误报率，误报率 <30% 且白名单稳定即提请升 `checks.yml`（--strict 仅对新 done 词条生效，存量豁免单另管）。

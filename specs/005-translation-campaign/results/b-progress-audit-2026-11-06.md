# B 批词条翻译进度对账（2026-11-06）

**会话**：B-main-20261106（接管 B 批翻译，主会话直译，不用子代理） | **工具**：`script/b_audit.py`（四源只读核对，本地草稿区）

## 方法

对 `SUMMARY.md` 中 b 字母目录 62 个正式词条（无别名/占位需排除）逐条核对四源：`SUMMARY.md` 正式条目、`tasks/b/<slug>.json` 状态机（state/steps/version_pin）、`b/<slug>.md` 正文、`yuanwen/b/<slug>.md` 镜像与 `baseline/entries.json`；另核对 `tasks/b/*.ledger.yaml` 组稿账本。

内容维度对每条有正文者比对：①H2 节数（剔除转换器 `Notes（原文脚注）` 包装标题）；②脚注引用多重集（剔除转换器伪标记 `[^key]`）；③defs 键集（`note-*` 备注型新增属允许）；④按状态机判定正文规模（cleared=H1 桩，drafted 起须有实译正文）。

## 实测数字（与 `campaign.py status` 实时推导一致）

| 指标 | 数值 |
|---|---|
| 正式词条 | 62 |
| 已建基线 | 62 |
| 英文镜像 | 62 |
| 已建任务 | 62 |
| done | 1 |
| 有正文（在途＋done） | 17 |
| cleared（H1 桩，待译） | 45 |
| NO_LEDGER（有正文无组稿账本） | 17 |

**状态分布**：cleared 45 / drafted 2 / s3_checked 14 / done 1 = 62。

**进度**：done 1/62（1.6%），有正文 17/62（27.4%），其余 45 条为清空待译（基线哈希门禁已过、version_pin 齐备，可直接全量重译）。

- done 1：boolalg-math（九步＋done 齐全，r1/r2/r3 于 11-06T00:57Z 收口）。
- s3_checked 14：basing-epistemic / bauer / bayes-theorem / bayle / behaviorism / bergson / binarium / boethius-dacia / boethius / bradley / buddha / buddhism-chan / buddhism-huayan / butler-moral——步骤链均为 clear/draft/s1/s2/s3，待 r1/r2/r3。
- drafted 2：bessarion / brouwer——正文已成形（6969 / 7232 汉字），draft 步 evidence 为空（actor `?`），属旧留痕缺口，按 NO_LEDGER 旧存量裁定不补造。

## 偏差发现与纠正

1. **账本 b 批补记计数过时**：原记「cleared 45/drafted 2/s3_checked 15」合计 62，但 boolalg-math 已于 11-06T00:57Z 走完 r1/r2/r3→done，该补记同时漏计 done。已 `campaign.py advance b translate --note` 追加更正条款（原补记保留留痕）：现记 62=cleared 45/drafted 2/s3_checked 14/done 1。
2. **正文实缺一处（内容缺陷）**：behaviorism（s3_checked）正文末段「（见 Ross et al. 2008, especially p. 10）」丢了行内脚注引用 `[^ross-2008]`（源文该段出现两次，译文只剩一次），defs 与其余标记齐备。留待 r1 实修，不进账本计数。
3. **PROGRESS.md**：B 行 62/62/62/1 与实际一致；工作区版本存在并行会话推进造成的其他字母漂移（modesty-humility、organ-donation），已重新生成纳入。
4. **NO_LEDGER 17**：B 批无段落账本体系（`tasks/b/*.ledger.yaml` 0 份），属已知旧存量缺口，按既有裁定不补造，逐条「无账本勿补造」留痕。
5. **状态机↔文件偏差**：零（无缺任务、无缺镜像、无缺基线、无 cleared 却含正文、无 done 缺 done 步、无损坏 json）。
6. **段落结构/脚注守恒**：15 条有正文者 H2 节数全等；脚注引用多重集除 behaviorism 一处外全等；defs 键集无缺失（binarium/basing-epistemic 等的 `note-*` 为备注型新增，非缺件）。

## 作业队列（按 `yuanwen` 行数升序，先短后长）

待全量重译 45 条，头 12 条：burke 293 / black-reparations 312 / bradley-moral 361 / baudrillard 375 / burley 399 / bloch 411 / beauty 428 / bohr-correspondence 430 / bradley-regress 440 / buber 441 / brentano 457 / buddhism-tiantai 468。
在途 16 条（s3_checked 14＋drafted 2）走 r1→r2→r3→done 收口，与新增翻译交错推进。

## 结论

B 批 phase=translate 与事实相符，账本计数经更正后零漂移；62 条中基线/镜像/任务/正文字段零缺项。继续由 B-main-20261106 按状态机推进：cleared 45 条全量九步重译、在途 16 条 r1–r3 收口，批次 done=62 后 `campaign.py advance b done` 收口。

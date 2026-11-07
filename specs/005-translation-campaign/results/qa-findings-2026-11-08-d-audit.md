# QA 对账记录：D 批翻译进度计算、同步与纠正（2026-11-08）

**范围**：D 字母批（`D-main-20261107` 认领，本会话 `D-main-20261108` 接管）正式词条 92 条。
**方法**：只读对账脚本 `script/audit_d_progress_20261108.py`（可复跑；输出 CSV `script/audit_d_progress_20261108.csv`，script/ 为 gitignored 草稿区）——在 C 批脚本基础上修两处口径：①账本解析改与 `script/lq.py` 同构的正则（PyYAML 会把 `source` 文本内的 `- id: N` 误当分段，虚报 87/87）；②`step2: TBD` 不计已填；③新增 `UNDER_LEDGER_GT_STATE`（账本已填但状态机仍 ≤cleared）。辅助脚本：`script/cd_verify_d.py`（五维对照）、`script/d_head_resid.py`（全库英文残留标题扫描）。

## 一、计算（对账结果）

| 维度 | 实况 |
| --- | --- |
| 正式词条 | 92（SUMMARY 为准；基线 92、任务 92 齐） |
| 状态分布 | pending 66 / cleared 4 / s3_checked 11 / done 11 |
| 文件形态 | stub 70 / translated 22 |
| 已译英文源词数 | 198,571（22 条 translated 合计） |
| 待译英文源词数 | 1,176,200（70 条合计；min 11,647 / 中位 16,061 / max 31,810） |
| 完成率 | done 11/92 = 12.0%；含在途 s3_checked 22/92 = 23.9% |
| 对账异常 | 19（NO_LEDGER 18 + 在途半成品 1） |
| 任务孤儿 | 0（`tasks/d/*.json` 与 `d/*.md` 双向反查干净） |

状态机本身**零虚挂**：22 条高状态条目的 `steps[]` 与 `state` 一一对应、无跳步；translated 22 件全部含 `## 参考文献` 与 `## 学术工具` 尾节（`TAIL_INCOMPLETE` 为 0）。

s3_checked 11 条 = 11-04~11-07 产出：descartes-ethics、descartes-ideas、dewey-moral、dewey-political、double-effect、du-bos、demonstration-medieval（旧存量 7）+ dai-zhen、dialectical-school、diodorus-cronus、deductivism-mathematics（11-07 D-main-20261107 产出 4）。
done 11 条 = david、delmedigo、democritus、descartes-ontological、descartes-physics、descartes-works、desgabets、doxography-ancient、duhem、duns-scotus、dynamic-choice。

**口径**：D 批进度一律以 `tasks/d/*.json` 状态机 + git log 为准；本文件与 `PROGRESS.md` 为生成物快照。s3_checked 11 条的 r1–r3 复审归 `R-main-20261108` 评审线（`session-handoff.md` §6 用户裁定），本线不自行推进。

## 二、纠正

1. **disability-care-rationing**（对账前唯一实质异常 `UNDER_LEDGER_GT_STATE`）：D-main-20261107 于 2026-11-08 05:09 留下在途件——账本 87 段（body 86 + oir 1）仅填 43 段，`step2: TBD` 44 段，正文仍为标题行，状态机停 cleared。本会话核对基线 hash、段数/kind/source 身份后按 lq 协议续译（详见本文件 §五 收口记录）。另记账本既有缺陷 1 处：段 32 `**` 计数 src=0 / step2=2（译文增粗体），写回前须废稿重做该段。
2. **PROGRESS.md 重生成**：done 179→181、在途 245（含其他字母并行会话产出）；D 行 92/92/92/11 不变——生成物与 `tasks/` 一致，无需修正。
3. **campaign 批账本**：`campaign.py status` 的 d 批 92/92/92/11 与 tasks 一致；`specs/005-translation-campaign/ledger.json` 的 d 注为 11-06 旧口径，已补记 2026-11-08 对账（`script/cd_ledger_sync_d0811.py`，往返格式断言通过）。

## 三、登记不改的遗留项（移交）

1. **NO_LEDGER 18 条**（ADR-0021 生效前旧存量 17 + duhem）：done/s3_checked 但无段落账本，无法追造双版留痕，只登记口径、不补文件。清单：david、delmedigo、democritus、descartes-ontological、descartes-physics、descartes-works、desgabets、doxography-ancient、duhem、duns-scotus、dynamic-choice、demonstration-medieval、descartes-ethics、descartes-ideas、dewey-moral、dewey-political、double-effect、du-bos。
2. **prose 语言告警 1,106 处 / 20 件**（`check_prose.py d/*.md`）：dewey-political 125、descartes-physics 124、demonstration-medieval 108、dewey-moral 89、desgabets 87、duhem 83、dynamic-choice 81、double-effect 80、descartes-ethics 63、doxography-ancient 62、descartes-ideas 48、duns-scotus 37、descartes-ontological 35、du-bos 27、delmedigo 17、democritus 14、david 9、descartes-works 9、deductivism-mathematics 5、dialectical-school 2、diodorus-cronus 1。其中 8 条（david、descartes-physics、desgabets、dewey-moral、doxography-ancient、du-bos、duns-scotus、dynamic-choice）的 `steps[].evidence` 无 prose 实修/豁免留痕，属 ADR-0020 口径缺口，交 QA 返工线（照 `qa-rework-2026-11-08.md` 程序）。
3. **参考文献英文小节标题 18 处 / 9 件**（dai-zhen 2、democritus 1、descartes-ontological 2、descartes-works 3、dewey-moral 2、dialectical-school 1、diodorus-cronus 2、duhem 2、duns-scotus 3）：`fan-yi-mu-ban.md` §4 模板写明“原小节标题保留英文”，C 批复审实践则汉化为“中文（English）”。**两处规则冲突，待用户裁定统一后再批量处理**，本会话不擅改。
4. **六检结论**：`check_style.py d/` 仅 1 处告警（descartes-ethics 标题行 `Descartes’` 弯引号右先于左，属专名撇号，非硬错误）；`check_math.py` 全库 missing 0；`check_academic.py --strict` 对 translated 22 件无硬错误。

## 四、后续译序（体量升序，前 10）

disability-care-rationing 11,647（在途续译）→ disability 11,738 → dietrich-freiberg 11,812 → dynamic-semantics 12,032 → decision-causal 12,276 → della-porta 12,276 → desire 12,302 → determinism-causal 12,432 → decision-theory-descriptive 12,504 → discourse-representation-theory 12,904 → derrida 12,975（中位 16,061，单条工时按 `fan-yi-mu-ban.md` §6.5 节奏分批收口）。

## 五、本会话进展

* 对账完成：92 条定性（见 §一），异常从 19 收窄到 1 件在途。
* PROGRESS.md 与 specs/005 批账本 d 注已同步。
* disability-care-rationing 续译收口：待本条目的 lq 守恒（残余=0）、compose、s1–s3 四检完成后回填。

# A 批译文质量复核发现（2026-10-31）

**触发**：用户指令"复核目前 A 开头词条的翻译流程……我认为目前的译文不够清晰，流程，准确度有问题，存在欧化汉语等问题"。
**复核视角**：规则/治理会话（非翻译会话）。范围：A 批 done 词条抽样——abduction 全读＋英文镜像（yuanwen/a/abduction.md）逐点核对；action、actualism-possibilism-ethics、abstract-objects、academic-freedom 模式计数。
**决策记录**：[ADR-0020](../../rules/adr/0020-译文语言质量门禁.md)。本文件是返工裁定的证据清单；行号以当前工作区为准。

## 一、误译实锤（abduction，已 done）

| # | 位置 | 中文（a/abduction.md） | 英文（yuanwen 镜像） | 问题 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | L29 | "（而只是使之变得可能）" | "(but only made likely)" | likely＝"很可能"，译作"可能"语义减弱 |
| 2 | L73 | "有人认为溯因只配推出……只配推出……" | "abduction warrants an inference only to…" | warrant 误译"只配"（语域错乱）；"最佳解释的大概为真"破句 |
| 3 | L75 | "相对于我们所考虑的那组假说的最佳解释，与……相比，也会胜出" | "the best explanation relative to the set of hypotheses that we consider would also come out as being best…" | 句法破散：主语悬空、介词短语错位，语义难以复原 |
| 4 | L101 | "说者一方享有难以置信的特权" | "an implausible privilege on the reasoner's part" | reasoner＝推理者，误作"说者" |

## 二、术语一致性（abduction）

* L57 同一行内三形并用：**不完全决定论证**（×2）→**不充分决定性论证**（×1）；同词条 L433 相关词条行又作"科学理论的**非充分决定性**"。
* 登记册 L343：主形"不完全决定（亦作'非充分决定性''不充分决定性'）"，且变体系 2026-10-30 因"abduction 正文落地形"补认——**登记册随正文走**，方向倒挂（宪法 III）。
* L143 节标题"贝叶斯**验证**理论"与正文"**确证**问题／确证理论"并存（登记册两行并存所致），同词条内未作取舍说明。

## 三、欧化密度（模式计数，正文行）

| 词条 | 被字（正文） | ≥70 字长句 | 三连"的" |
| ---- | ---- | ---- | ---- |
| a/abduction.md | 38 | 26 | 21 |
| a/action.md | 70 | 42 | 69 |
| a/actualism-possibilism-ethics.md | 53 | 34 | 25 |

`tools/check_prose.py`（ADR-0020，告警级）首跑 abduction：69 条（de-chain 28／long-sentence 25／weak-verb 10／plural-men 3／passive-bei 3）。

## 四、流程发现（复核流程本身）

1. **六道独立性失真**：abduction s1→r3 同一 actor（ses-007-rev）十分钟连走六步（`tasks/a/abduction.json` 2026-10-28T17:07:31Z→17:17:41Z），三审三校实为一人连跑；ISO 17100"校者独立于译者"未落实。ADR-0020 给出阶梯方案，默认形态待裁定。
2. **语言道（s2）无机器底**：体例／学术／术语三道均有检查器，唯欧化与清晰度全靠人工自觉——已 done 词条仍混入上表实伤。check_prose.py 补位（告警级）。
3. **问题无分级**：缺陷分类见 fang-fa-lun S5，但任务 evidence 无 Critical／Major／Minor 分级，Critical 漏入 done 无拦截（ADR-0020 补）。

## 五、待用户裁定

1. **返工范围**：A 批 done 词条按本清单定点返工（开 update/quality 任务走变更段），还是全量复查后再定？
2. **复核独立性默认形态**：双会话交叉认领 r1–r3，还是单会话冷置重读？
3. **check_prose 升硬时机**：告警级运行至 A 批收口、校准白名单后，是否进 `checks.yml` 硬门禁？

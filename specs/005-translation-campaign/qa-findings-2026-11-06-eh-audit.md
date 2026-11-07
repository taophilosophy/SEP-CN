# E–H 批进度对账与纠正记录（2026-11-06）

**会话**：EH-main-20261106　**范围**：`e/` `f/` `g/` `h/` 四批共 305 条正式词条
**方法**：三方对账——任务 JSON（状态机）× 段落账本（`lq.py check` 段数/双版/守恒）× 正文落盘（段数比、指纹命中）× 英文镜像段数。工具：`script/_audit_eh.py`、`script/_cov_eh.py`、`script/_integrity_eh.py`（`script/` 为草稿区，不入库，结论以本文件为准）。

## 1. 对账结论（2026-11-06 10:0x UTC）

| 字母 | 总 | done | s3_checked（待复审） | 有账本（含半截） | 未开工 | 段覆盖率 |
| --- | --- | --- | --- | --- | --- | --- |
| E | 99 | 0 | 16 | 4（13–77%） | 83 | 3.7% |
| F | 96 | 0 | 0 | 2（film 77/77、frame-problem 0） | 94 | 2.0% |
| G | 49 | 0 | 0 | 0 | 49 | 0% |
| H | 61 | 6 | 0 | 13 | 42 | 3.2% |

全体 E–H：账本段 955 / 源段 38614 ≈ **2.5%**；状态机 done 6 / 305 ≈ **2.0%**。

## 2. 抓到的三类偏差与处置

1. **账本虚高（段数缺口）**：`lq.py check` 实测 hamann 3/76、hilbert-program 3/63、hume-moral 7/92、heytesbury 11/193、haecceitism 13/122、holes 9/14。状态均为 `cleared`，"半截账本"不等于将完成。处置：派入 lane1 补齐至 `s3_checked`。
2. **假双版（违 ADR-0021 反思两步）**：step2 与 step1 逐字符相同的段——halevi 48/48、holkot 35/35、han-dynasty 35/36、hume-aesthetics 39/64、hutcheson 68/145，且 hare/hartshorne（已 done）亦残留 15/18 段。处置：hutcheson/halevi/holkot 派 lane2 逐段重写 step2；已 done 两条登记为返工债（见 §4）。
3. **旧文未清（违零信任）**：`f/frame-problem.md`（36K）、`g/gene.md`（77K）、`h/heraclitus.md`（3.5K）在 state=pending/cleared 时仍带旧中文正文。处置：frame-problem 走 `task_ops clear` 正规清空；gene/heraclitus 正文复位为 H1 并在任务 JSON 追加 `doc-reset` 步骤留痕（旧文可由 git 回溯）。

## 3. 已完成的纠正

* **f/film**：旧协议账本（`id: p1`、`|` 块标量）归一为 lq 格式；补 8 个节标题段 + 1 个 oir 段至 77/77；step2 里误写的 `**中文**` 还原为 `*中文*`（`**` 守恒门硬拦；粗体化属正文级，由 `script/italic_to_bold_cjk.py` 在 compose 后执行）。守恒门通过 → compose 20767 字符 → 转粗 14 行 → `check_style` 0 / `check_academic` OK，状态推进 `cleared → drafted`。s1/s2/s3 待续（prose 告警 41 条待实修）。
* **E 批 16 条 s3_checked**：四项检查器预检——style/academic/math 全绿，prose 告警合计 694（de-chain 与 long-sentence 为主），说明 subagent 批次的 s2 语言层欠修。复审按最小条先行（elias 已收口，见 §5）。

## 4. 债务登记（不补造、留痕）

* **ADR-0021 账本缺档**：E 批 16 条 s3_checked 与 H 批已 done 的 hare/hartshorne 等，系旧管线（无账本或仅骨架）产物，双版纪律无法事后核验。处置：不补造账本；逐条在 r3 evidence 记明，作为系统性债务在本表登记。
* **done 条假双版**：hare（15/120）、hartshorne（18/76）已 done，step1==step2 段保留待返工；h/humanism-civic done 而账本 0 段（旧存量豁免，NO_LEDGER）。
* **film/film.md 学术工具节**：沿用旧 compose 的表格形（`> |` 块引用表格）；新 compose 输出为列表形，属体例不一致，待统一时一并处理。

## 5. 复审流水（r1–r3 判据记录位置）

每条收口时在任务 JSON `steps` 内写 evidence：r1 段级核销（数字/专名/编号/脚注键）、r2 句级复读（`check_prose` 残余与豁免依据）、r3 终检（style/academic/math 全绿 + 账本或豁免）。首批收口：

* **elias**：prose 13→1（唯一残余为 15 人名单长句，列举类豁免，ADR-0020）；修正 prefect 释义与 "evidence is scant" 逻辑误读；529/541/CLIII/22 次/15 处/12 讲逐项核对一致。

## 6. 续记（复审中发现的条目级缺陷）

* **e/epistemology-language-tibetan**：源参考文献含 `### A. Sources and translations` / `#### 1. Pre-classical period` / `#### 2. Classical and post-classical period` / `### B. Modern studies` 四层书目子标题，中文侧随「参考文献脚注化」（refs_kind=modern）转换而合并消失（55 个条目本身齐全）。属转换器范式缺陷而非漏译；手工重构需打散 55 条定义顺序，风险高于收益，**登记为转换器债**，留待 refs 转换器统一处理。

* **E 批 4 条半截账本不可再 compose**：emotion-Christian-tradition 10/74、epictetus 20/61、erfurt 27/60、equal-ed-opportunity 79/103 段。这些账本系旧管线中途产物，`lq.py check` 会报「段数不符」HARD-FAIL；**禁止**据此 compose（会截断正文）。正文完整性以节标题/脚注键/段数比三方核销为准，账本仅作历史证据保留。

# QA 对账记录：C 批翻译进度计算、同步与纠正（2026-11-07）

**范围**：C 字母批（CD-main-20261106 认领，本会话接管）正式词条 172 条。
**方法**：只读对账脚本 `script/audit_c_progress_20261107.py`（可复跑；输出 CSV `script/audit_c_progress_20261107.csv`，script/ 为 gitignored 草稿区）——在 2026-11-06 c/d 对账脚本（`audit_cd_progress_20261106.py`）基础上补英文源词数（yuanwen 镜像）与账本分段/已填分段（ruamel.yaml）两维，逐条核对：任务 JSON 状态机 vs steps 凭证 vs 文件实况 vs 账本 vs 尾节完整性 vs 孤儿反查。

## 一、计算（对账结果）

| 维度 | 实况 |
| --- | --- |
| 正式词条 | 172（SUMMARY 为准） |
| 状态分布 | pending 145 / s3_checked 27（对账后）/ done 0 |
| 文件形态 | stub 145 / translated 27 |
| 已译英文源词数 | 196,179（27 条 translated 合计） |
| 待译英文源词数 | 2,589,766（145 条 pending 合计；min 8,586 / 中位 16,427 / max 46,221） |
| 对账异常 | 0（纠正前 1，见下） |
| 任务孤儿 | 0（tasks/c/*.json 与 *.ledger.yaml 双向反查干净） |

s3_checked 27 条 = C28 批产物 26 条（前会话三校完成、待 r1–r3 复审）+ contractarianism（本会话收口，commit 87ecbb29）。

## 二、纠正

1. **contractarianism**（对账前唯一异常 `UNDER_FILE_GT_STATE`：文件已译 8,897 汉字但状态机仅 cleared）——前会话在途件，账本 36/36 已填但未推进状态机。本会话：lq 守恒门通过（段数/kind/source 逐字符一致、脚注键与 $ 守恒）→ compose 幂等核验（与成品逐行一致）→ s1 逐节核销实修（性质赔错字、帕累托定义倒置、Walsh 句末残句、交叉引用节名、人名 ADR-0022 归一，共 18 处）→ s2 prose 29→4（余 4 条逐条豁免留痕）→ s3 四检全绿（含 done 级取消在途豁免的模拟核查 0 硬 0 警）→ 状态机 draft→s1→s2→s3 各步凭证齐。术语登记 8 行 + 人名 1 行（卡罗尔·帕特曼）。落账 commit `87ecbb29`。
2. **PROGRESS.md 重生成**：done 134、在途 257，contractarianism 行 cleared→s3_checked（生成物，`python tools/progress.py`）。
3. campaign.py 批账本无错（c 批 phase=translate、done 0 与 tasks/ 一致），不动。

## 三、同步要点（计数口径）

* C 批进度一律以 `tasks/c/*.json` 状态机 + git log 为准；本文件与 PROGRESS.md 为生成物快照。
* 27 条 s3_checked 的 r1–r3 复审由本批会话承担（初译 actor 为另一会话，独立性满足 ADR-0020；冷置回读）。
* pending 145 条开译顺序按体量升序（词数），与批次内先小后大惯例一致；单条周期照 specs/005 `fan-yi-mu-ban.md` §6.5 与 ADR-0021 段落账本协议。

## 四、后续工作清单

1. r1–r3 冷置复审（体量升序）：cockburn 3,557 → crathorn 3,751 → conway 4,173 → condemnation 4,907 → cordemoy 5,128 → cambridge-platonists 5,657 → creation-conservation 6,013 → childhood 6,135 → cognitive-science 6,288 → causation-medieval 6,300 → …（全 27 条平均 7,265 词）。
2. pending 开译（体量升序，前 10）：colonialism 8,586 → chinese-phil-science 8,898 → cosmology-30s 10,247 → conscience 10,427 → crescas 10,472 → cosmopolitanism 10,820 → closure-epistemic 11,198 → content-externalism 11,452 → cugoano 11,510 → cosmology-theology 11,578（全部 ≥8,586 词，median 16,427，单条工时大，按 session-handoff 节奏分批收口）。

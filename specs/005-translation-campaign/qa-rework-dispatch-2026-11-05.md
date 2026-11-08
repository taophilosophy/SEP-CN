# QA A 批返工派发清单（2026-11-05）

**依据**：用户裁定 2026-11-05「按程序定点返工」（qa-findings-2026-10-31.md §五.1 之推荐项；不计成本）。
**机制**：既有任务记录保持 `state=done` 不动（状态机无重开节点，不擅改 rules/04）；每词条任务已追加 `rework-open` 步登记立项（governance-session，2026-11-05）。认领会话在既有任务上按 **update 语义只走变更段** 推进，逐步追加 `rework-s1/s2/s3/r3` 步留证。
**范围来源**：`results/qa-prose-2026-10-31-summary.md`（欧化告警行号清单）＋ `results/qa-traverse-2026-10-31.md`（全读遍历实锤：Critical 15＋1 附／Major 37／Minor 157）。

## 认领优先序（按告警量降序）

| 序 | 词条 | 欧化告警 | 任务记录 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | action | 136 | tasks/a/action.json | de-chain 83／long-sentence 38；✅ 2026-11-08 返工收口 7b9c536d（138→2，引文豁免 2） |
| 2 | action-perception | 113 | tasks/a/action-perception.json | passive-bei 19；✅ 2026-11-08 返工收口 4a371187（112→23，引文豁免 23） |
| 3 | academic-freedom | 107 | tasks/a/academic-freedom.json | |
| 4 | abelard | 88 | tasks/a/abelard.json | |
| 5 | actualism-possibilism-ethics | 79 | tasks/a/actualism-possibilism-ethics.json | |
| 6 | abhidharma | 77 | tasks/a/abhidharma.json | 拼接残迹已清（007） |
| 7 | advance-directives | 76 | tasks/a/advance-directives.json | |
| 8 | abstract-objects | 73 | tasks/a/abstract-objects.json | |
| 9 | abduction（含 abduction.peirce 补充材料） | 69+12 | tasks/a/abduction.json | Critical 五项 011 已修大半，认领时先逐项复核定账 |
| 10 | abrabanel | 55 | tasks/a/abrabanel.json | |
| 11 | abu-bakr-al-razi | 47 | tasks/a/abu-bakr-al-razi.json | |
| 12 | abortion | 39 | tasks/a/abortion.json | |
| 13 | abraham-daud | 39 | tasks/a/abraham-daud.json | men 8 条 |
| 14 | abilities | 35 | tasks/a/abilities.json | |
| 15 | abner-burgos | 30 | tasks/a/abner-burgos.json | EN 未译 6 处已清（007） |

非 done 词条（addams-jane／alcmaeon／african-sage）各自校次消化，**不入本队列**（见 qa-prose summary 口径）。

## 作业程序（认领会话）

1. 认领：在本表备注列登记会话名；从任务既有 `rework-open` 步接续。
2. s1（Critical 定点核对）：对照 `qa-traverse-2026-10-31.md` 实锤清单逐项复核——011/007 可能已修部分（如 abduction「只配」已消失），已修项记 evidence 销账，未修项改前回核英文镜像（零信任）。
3. s2（语言批次）：复跑 `python tools/check_prose.py a/<slug>.md` 取全量行号，逐条人工判断改写或豁免留痕；Minor（as-one／dang-shihou／plural-men）顺带。
4. s3→r3：变更段复核；术语族复核按 ADR-0020 条款（跨词条既定名不动）。
5. 收尾门禁：`check_prose.py <路径> --strict` 0 或逐条豁免留痕 ＋ `check_academic.py --docs <路径> --strict` 0 硬错误；`check_prose` 升硬观察口径不变（误报率 <30% 且白名单稳定）。

## 纪律

* 状态字段保持 `done`；不得手改既有步骤，只追加 rework-* 步。
* 改写前回核 `yuanwen/a/<slug>.md` 对应段（宪法 II 零信任）。
* 完成一件在本表划账（备注列记提交号）。

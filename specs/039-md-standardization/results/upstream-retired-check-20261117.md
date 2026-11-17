# 上游退役件复核（2026-11-17，用户指示“复核上游／复核 SUMMARY 对应条目”）

**方法**：逐条访问 `https://plato.stanford.edu/entries/<slug>/`（WebFetch，相邻请求间隔 ≥6 秒，
均落在同一会话内），读退休公告与“superseded by”字样；再与本地 `baseline/retired.json`（2026-11-12
登记，7 条）、`SUMMARY.md` 对应条目、本地后继件包名三方对照。

## 一、孤儿 yuanwen 镜像（无 en 包／无 baseline／无 zh／SUMMARY 无引用）

| slug | 上游结果 | 本地状态 | 处置 |
| ---- | ---- | ---- | ---- |
| `health-well-being-personal-relationships` | **404**（无此条目） | 仅残余 yuanwen 主件 | **已删**（git rm，2026-11-17） |
| `on-utopia` | **404**（无此条目） | 仅残余 yuanwen 主件 | **已删**（git rm，2026-11-17） |

两件与 `baseline/retired.json` 无关（不在任何登记），来自 2026-11-14「原始物入库（补）」恢复提交。

## 二、en 包无 yuanwen 主件的 5 件：全部＝官方退役件的残留包

| slug | 本地包标题 | 上游现状 | 上游“superseded by” | 登记表 successor | 本地后继件 | 判定 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| `scientific-explanation` | Scientific Explanation（Woodward & Ross） | Document Retired | 20th Century Theories of Scientific Explanation | `scientific-explanation-20th` | 有（在册） | 旧件退役，**后继件已收** |
| `wisdom` | Wisdom（Fall 2023） | Document Retired | Wisdom in Contemporary Analytic Philosophy（重写再发） | `wisdom-analytic` | 有（在册） | 同上 |
| `wyclif-political` | John Wyclif’s Political Philosophy | Document Retired | John Wyclif（扩写并入） | `wyclif` | 有（在册） | 同上 |
| `time-experience` | The Experience and Perception of Time | Document Retired | Temporal Consciousness | `consciousness-temporal` | 有（在册） | 同上 |
| `qm-action-distance` | Action at a Distance in Quantum Mechanics | Document Retired（移入 SEP Archives，公告**无** successor） | — | `null`（登记表一致） | 无 | 旧件退役，无后继 |

**回答“重名还是内容替换”**：都不是同一 slug 的内容替换，也不是本地改名——是**上游把旧条目整件退役**
（retire），其中 4 件明确指定后继条目（后继件的 slug 与我们 SUMMARY 在册条目一致，内容已另件收录），
1 件（`qm-action-distance`）无后继、仅存档。因此本地这 5 个 en 包是**退役件残留**：
`baseline/retired.json` 的登记说明写的是「抓取物与译文已移除」，但 2026-11-14 的恢复提交
把这 5 个 en 包又带回了工作树，与登记相矛盾。

**建议处置（待用户裁定，未动）**：`git rm -r` 这 5 个 en 包（无 pin、不在钉账、无 zh、SUMMARY 无对应），
使工作树与 `retired.json` 一致；若要留档，registry 已写明 `content_recoverable_at`
（19eb975e…），删后仍可从 git 历史取回。

## 三、相邻发现（同一类问题，登记未动）

`yuanwen/p/pineal-gland.figure1..6.md` 六件补充材料镜像：无 en 包、无 zh 件、不在 SUMMARY、
不在 baseline。上游 `pineal-gland` 为 **Document Retired**（标题 “Descartes and the Pineal Gland”，
指向 Summer 2026 存档版），且 `retired.json` 未登记该条。

**建议**：① 六件 yuanwen 补充镜像一并删除；② 在 `baseline/retired.json` 补登 `pineal-gland`
（notice=Document Retired，archive_edition=sum2026，successor=null，zh_lines=0，task=null）。
两项均属清理性动作，待裁定。

# catalog-verdict REMOVE 候选裁决留档（2026-10-28）

`summary_sync.py report` 基于 contents.html 目录判定 REMOVE 候选时，会把
"上游目录未列但词条页在线"的条目误列为删除候选。经逐条 URL 探测（HTTP 状态
即裁决证据，抓取礼貌间隔 ≥5s），以下 6 条**裁决保留**，不得执行 REMOVE：

| slug | 探测结果 | 裁决 |
| --- | --- | --- |
| continental-rationalism | HTTP 200 | 保留：词条在线，contents.html 未列（目录缺口，非词条退役） |
| pineal-gland | HTTP 200 | 保留：同上；slug 已由撤稿裁定确认（见 execution-log） |
| qm-action-distance | HTTP 200 | 保留：同上 |
| scientific-explanation | HTTP 200 | 保留：同上；其子条目 scientific-explanation-20th 等在 ADD 队列 |
| time-experience | HTTP 200 | 保留：文件已由 the-experience-and-perception-of 改名归位 |
| wisdom | HTTP 200（软 404） | **保留（2026-10-28 复核改回，恢复已删行+文件+账本记录）**：六条的 /entries/ URL 同为软 404（"HTTP 200=在线"系误读），在册依据同为归档版基线——wisdom@fall2023 经 --archive-edition 建基线（index.html+notes.html），与五条同案同判；上游集群头呈现与 wisdom-analytic 后继不构成删除理由（scientific-explanation 同构而保留） |


> **2026-10-28 复核事实更正**：本表 6 条保留项的 /entries/<slug>/ URL 全部返回 SEP 软 404 错误页（HTTP 200 + "Document Not Found" 正文），"词条在线"的初判依据不成立；六条保留的实际依据是**归档版基线**（--archive-edition 抓取，见 baseline/entries.json 各条 archive_edition 字段与 execution-log 2026-10-28 续篇）。6 条同案同判，均保留。

已实际执行的删除（ upstream 404/无身份，证据同为 URL 探测与目录缺席）：

* health-well-being-personal-relationships（HTTP 404，内容并入 disability-well-being，ADD 队列）
* on-utopia（HTTP 404，内容并入 plato-laws，词条已正式化）
* indian-philosophy（contents.html 无此 slug，仅为占位导航借用文件，已改链 README）

残余已登记差异（等 ADD 队列 apply-add 后自然消除）：

* SUMMARY 别名行 `\*数学哲学——见数学哲学：数学哲学中的唯名论 …` 暂指
  f/fictionalism-mathematics.md（真实目标 nominalism-metaphysics 尚无文件，在 ADD 队列）。
* 快照别名表 654 名中 68 个目标路径缺 SUMMARY 别名行，绝大多数随对应条目
  的 ADD 一并补齐。

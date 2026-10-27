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
| ~~wisdom~~ | HTTP 200（软 404） | **改判删除**：fetch_entry 软 404 检测显示该 URL 返回 SEP 错误页（词条已撤稿），初判仅凭 HTTP 200 有误；上游目录以无链接集群头呈现 wisdom、子条目 wisdom-analytic（ADD 队列）为唯一后继。已删行+文件+账本记录 |

已实际执行的删除（ upstream 404/无身份，证据同为 URL 探测与目录缺席）：

* health-well-being-personal-relationships（HTTP 404，内容并入 disability-well-being，ADD 队列）
* on-utopia（HTTP 404，内容并入 plato-laws，词条已正式化）
* indian-philosophy（contents.html 无此 slug，仅为占位导航借用文件，已改链 README）

残余已登记差异（等 ADD 队列 apply-add 后自然消除）：

* SUMMARY 别名行 `\*数学哲学——见数学哲学：数学哲学中的唯名论 …` 暂指
  f/fictionalism-mathematics.md（真实目标 nominalism-metaphysics 尚无文件，在 ADD 队列）。
* 快照别名表 654 名中 68 个目标路径缺 SUMMARY 别名行，绝大多数随对应条目
  的 ADD 一并补齐。

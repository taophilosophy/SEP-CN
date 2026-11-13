# specs/015 交接卡（语体全局复核）

更新：2026-11-11（pc6）。进度只认 `results/verdicts.jsonl`，不认会话记忆。

## 已完成

* 规则与门禁：`rules/02` 语体与文风条款、`rules/04` 二校/r1 通读、ADR-0033、`check_academic` 的 `task-style-attest`（只查语义复核留痕）、`task_ops.py reopen`（done→pending）。
* 2026-11-10：J 批 12 条 done 全部语义通读（classical：jayaraasi、john-norris、johann-sturm；mixed：john-italos、jaina-philosophy；余 7 modern），5 条已置空。
* 2026-11-11：全库快速复核（用户指令「每个 .md 随机抽查 3 段，语义分析，同类条目置空」）。方法：每文件随机 3 段语义抽样 + `bin/register_metrics.py` 的真·之/的比与文言句式定位（剔除“之一/之后/之间”等现代固定搭配；**命中数不作判定依据**）。新判 23 条，入 `verdicts.jsonl`（累计 35 条）。

| verdict | 本轮词条 | 处置 |
| ---- | ---- | ---- |
| classical | intentionality-ancient、james-mill、israeli、early-modern-india | 置空（cleared） |
| mixed | africana、aesthetics-18th-german | 置空（cleared） |
| modern（保留） | buddha、davidson、legrand、confucius、korean-philosophy、natphil-ren、albalag、kukai、dai-zhen、knowledge-acquaindescrip、newton-philosophy、cudworth、luxemburg、peter-damian、peter-damian.supplement、telesio、gorampa | none（其中 davidson/legrand/dai-zhen/knowledge-acquaindescrip/gorampa 有个别文言句，列入定点改写） |

* 本轮 6 条置空均按 ADR-0033：`reopen` → `clear`，正文仅余 H1，任务状态 `cleared`，旧 steps 与账本保留为历史凭证。其中 james-mill、early-modern-india 原为 `s3_checked`（在途），按同一语义手工追记 `reopen` 步后回 `pending`，再经 `clear` 工具门置空。
* 判定分界（与 015 先例一致）：真·之/的 ≥0.35 或文言句式成段 → classical/mixed；<0.35 且主体句法为现代汉语 → modern（个别文言句按定点改写登记，不整篇回炉）。john-italos（0.53）判 mixed 的既有先例即此线的上端。

## 待办

1. `results/queue.jsonl` 现 391 条 done 词条（2026-11-13 重生成，done 计数随各批收口增长）。全量逐条通读按 done 时间升序推进，结论追加 `verdicts.jsonl`；判 classical/mixed 即 `reopen` + `clear`。
2. 通读口径：排除 `>` 引块中的直接引文、典籍原文、碑铭、题记原引文与参考文献照录区；判据是“当代中文学术读者能否自然读懂”，不按关键词命中数判定。
3. 破折号：`bin/dash_scan.py` 只排复核优先级；本轮 verdicts 的 `dash` 字段一律记 `pending`（破折号线未评），由 `dash-verdicts.jsonl` 另线推进。
4. 定点改写候选（不置空，待语体全量复核完成后统一处理）：davidson 一处文言收束句、legrand「危乎殆哉」、dai-zhen「欲两部分俱成全」句、knowledge-acquaindescrip 散见文言成分、gorampa「既已……便……」句。
5. 每批复核后重生成 queue 与 `PROGRESS.md`，跑 `check_all.py`，提交相关文件。

## 2026-11-13 软复核开工（用户裁定：全量逐条通读；只登记不处置）

* 用户裁定「软全局复核」= 覆盖不软、处置软：全量逐条通读照旧，但本轮**只写 verdicts＋证据句，不 reopen 不置空**，汇总后另行裁定处置。
* 首批 5 条（M 批 done，兼补 s2 语体留痕）：mandeville、marsilius-padua、model-organisms、moral-learning、music，全部判 `modern`（`dash=ok`），`action=none`；证据句见 `verdicts.jsonl`。s2 evidence 已按 ADR-0033 追补「语体：」结论，`check_all` 9 项复绿。
* 台账口径：`verdicts.jsonl` 累计 100 条（modern 89／classical 7／mixed 4）。按 done 时间升序推进，每 5 条一批提交；2026-11-13 当日已推进 45 条（第 1–9 批），全部判 modern；A 批（a/ 首段队列）及 d/、i/ 若干条已通读完毕。


## 注意

* 置空会改变 `PROGRESS.md` 的 done 计数与批次统计（生成物实时推导），不要手工回填。
* 旧账本（如 `tasks/j/jayaraasi.ledger.yaml`）仍在库内，仅作违规记录；重译时覆盖前先确认新建。
* 若并行会话正在写同一条目，先 `git status` 与 mtime 判落定再动。
* 抽样工具：`bin/register_metrics.py`（指标与证据句，`--json` 落 `script/tmp/register_metrics.json`）、`bin/review_cards.py`（复核卡）。二者只定位、不判级。

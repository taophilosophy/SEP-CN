# specs/015 交接卡（语体全局复核）

更新：2026-11-10 18:10（pc6）。进度只认 `results/verdicts.jsonl`，不认会话记忆。

## 已完成

* 规则与门禁：`rules/02` 语体与文风条款、`rules/04` 二校/r1 通读、ADR-0033、`check_academic` 的 `task-style-attest`（只查语义复核留痕）、`task_ops.py reopen`（done→pending）。
* J 批 12 条 done 全部语义通读完毕，结论入 `verdicts.jsonl`：

| verdict | 词条 |
| ---- | ---- |
| classical（置空） | jayaraasi、john-norris、johann-sturm |
| mixed（置空） | john-italos、jaina-philosophy |
| modern | japanese-aesthetics、joane-petrizi、james-ward、justus-lipsius、james、justice-virtue、justep-coherence |

* 5 条不合规词条已按用户裁定置空（`reopen` → `clear`），正文仅余 H1，任务状态 `cleared`，回到重译队列；旧 steps 与账本保留为历史凭证。新 draft 必须新建账本，不得沿用旧 step2。

## 待办

1. `results/queue.jsonl` 现有 301 条 done 词条（置空 5 条后重生成）。按 done 时间升序逐条通读，结论追加 `verdicts.jsonl`；判 classical/mixed 即 `task_ops.py reopen` + `clear`。
2. 通读口径：排除 `>` 引块中的直接引文、典籍原文、碑铭、题记原引文与参考文献照录区；判据是“当代中文学术读者能否自然读懂”，不按关键词命中数判定。
3. 破折号：`bin/dash_scan.py` 只排复核优先级，不产生结论；滥用与否按语义判断。
4. 每批复核后重生成 queue 与 `PROGRESS.md`，跑 `check_all.py`，提交相关文件。

## 注意

* 置空会改变 `PROGRESS.md` 的 done 计数与批次统计（生成物实时推导），不要手工回填。
* 旧账本（如 `tasks/j/jayaraasi.ledger.yaml`）仍在库内，仅作违规记录；重译时覆盖前先确认新建。
* 若并行会话正在写同一条目，先 `git status` 与 mtime 判落定再动。

# 任务目录

本目录存放**文档任务**（Doc Task）的状态记录：每个待译/待更新/重译的中文词条文档一条记录。流程规则见 `rules/04-translation-workflow.md`；本 README 只定义记录格式与操作方式。

## 存储约定

* 一词条一文件：`tasks/<slug 首字母>/<slug>.json`，slug 为 SEP 词条标识（如 `tasks/a/alcmaeon.json`）。
* 例外：`tasks/term-candidates.json` 为**术语候选清单**（词汇表复核流程的中间记录，无 slug/state），不属于文档任务；`tools/progress.py` 统计时自动跳过。
* 文件由 `tools/task_ops.py` 创建与推进，**不要手改状态字段**；`evidence` 等叙述字段可由执行会话补写。
* 记录入库（git 分发），与 `baseline/entries.json` 的版本钉互为凭证。

## 记录 schema

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| `slug` | string | SEP 词条标识，同文件名 |
| `kind` | string | `retranslate`（重译）或 `update`（上游更新） |
| `zh_doc` | string | 中文文档路径，如 `a/ke-luo-dun-deaer-ke-mai-weng-alcmaeon-carl-huffman.md` |
| `state` | string | 状态机当前节点（见下） |
| `steps` | array | 每步一条：`step` / `status` / `actor` / `at`（ISO 8601）/ `evidence` |
| `blockers` | array | 阻塞说明；blocked 状态独立于 state |
| `created_at` | string | 任务创建时间 |
| `version_pin` | object | 英文源版本钉：`pubinfo_date` + `archive_edition` + `sha256` |

## 状态机

```
retranslate: pending → cleared → drafted → s1_checked → s2_checked → s3_checked
             → r1_reviewed → r2_reviewed → r3_reviewed → done
update:      pending → s1_checked（仅变更段）→ s2_checked（变更段所在节）
             → s3_checked（全文档）→ r1_reviewed → r2_reviewed → r3_reviewed → done
```

* 六道与三审三校的对应、各步合格凭证：见 `rules/04-translation-workflow.md`。
* **禁止跳步**；`blocked` 标志独立于状态，解除用 `advance --unblock`。

## 操作（`python tools/task_ops.py`）

```sh
python tools/task_ops.py create <slug> --kind retranslate                    # 建重译任务（前置：基线已登记；zh-doc 可自动定位）
python tools/task_ops.py create <slug> --kind update --from <变更清单.json>   # 建更新任务（--from 指向 baseline/changes/ 下清单）
python tools/task_ops.py show <slug>                                          # 查看当前状态与步骤
python tools/task_ops.py clear <slug>                                         # 清空既有正文（retranslate 专用，前置：基线可信）
python tools/task_ops.py advance <slug> --step s1 --actor <执行者> --evidence <凭证说明>
python tools/task_ops.py advance <slug> --unblock --evidence <解除说明>        # 解除阻塞
python tools/task_ops.py block <slug> --reason <原因>                          # 标记阻塞
```

* 退出码：0 成功；1 任务不存在；2 用法错误；3 前置条件不满足。
* CLI 契约细节见 `specs/001-sep-sync-pipeline/contracts/cli.md`。

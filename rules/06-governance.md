# 软件工程治理

本规则把宪法六原则落实为日常可执行的治理机制：单一事实源登记、变更管理、并发会话纪律、质量门与审计。

## 单一事实源登记表

同一类事实只允许一个地方说了算；两处不一致时，修弱势一方向登记源看齐。

| 事实域 | 登记源 | 派生视图 / 校验工具 |
| ---- | ---- | ---- |
| 目录结构与标题 | `SUMMARY.md` | 各文件 H1（CI 同步，别名行不覆盖）；`tools/check_summary.py` |
| 学科分类目录 | `mu-lu-s.md`（手编） | `tools/check_mulu_s.py` 对应性检测 |
| 英文原文镜像 | `yuanwen/<letter>/<slug>.md`（管线转换，不入库） | `tools/compare.py`、`rebuild_dir.py check`、`baseline_audit.py` |
| 术语译法 | `yi-zhe-shuo-ming.md` 登记册 | `qian-yan/ci-hui-biao.md` 发布词汇表 |
| 词条版本事实 | `baseline/` 元数据清单 | `tools/baseline_audit.py` |
| 文档任务状态 | `tasks/<slug>.json` | `tools/task_ops.py show` |
| 流程与验收标准 | `specs/<NNN>-*/spec.md`、`plan.md` | `checklists/`、`demo-log.md` |
| 最高原则 | `.specify/memory/constitution.md` | 本目录规则为其操作性展开 |

## 变更管理

* **规则变更走 ADR**：影响面超出单词条的规则修订，在 `rules/adr/NNNN-标题.md` 新建决策记录（背景、决策、后果），再改规则文件；ADR 只追加不删除，废弃标记 superseded。
* **宪法修订**：提交信息注明“修订宪法 vX.Y”并说明理由（宪法 Governance 节）。
* **破坏性动作** （批量清空、重命名、结构重排）前置条件：受影响词条已有可信英文基线；动作可由 git 历史回溯；完成后运行对应校验工具并留凭证。
* **历史改写与批次护栏（tag）**：已裁定允许重写 git 记录（含 force push）。护栏约定：改写或批量动作前先打备份 tag（`git tag backup/<YYYY-MM-DD-说明>`），改写后立即 push 分支与 tag；每完成一个批次打 `batch/<批次名>` tag。tag 不限制自由，只保证任何时刻有退路。
* **CI 工作流变更** 须同步更新 `rules/05-ci-and-tools.md` 的工作流清单表。

## 并发会话纪律（多会话并行开发）

本仓库常有多个 AI 会话/人工同时工作，纪律如下：

1. **提交前核对 HEAD**：`git log --oneline -3` + `git status`，确认基点未变；基点变了先 `git diff HEAD` 重放自己的改动。
2. **提交竞态重试**：commit 失败或“no changes added”时，先检查自己的文件是否已被对方提交卷入，确认内容无误后不必重复提交；确有剩余再补提交。
3. **推送先 pull**（2026-10-27 教训固化）：`git push` 被拒（non-fast-forward）或对方已推送时，先 `git fetch && git pull --rebase origin main` 再推；带未授权 force push 期间，其他会话应停手或改为先 pull 再推——本日两次 force push 各孤儿化了并行会话的一个提交（587ec741、fb2a3317），其内容需对方会话重新落地。
4. **目录所有权边界**：词条内容归翻译会话；`specs/`、`.specify/`、`tools/`（管线包）、`baseline/` 归管线会话；`rules/`、`tasks/README.md`、`AGENTS.md` 归治理。跨界修改先在提交信息说明理由。
5. **不抢改他人正在写的文件**：发现非本人改动先读再动，禁止用 `git checkout --` / `reset --hard` 清理他人未提交工作。
6. **`script/` 为个人草稿区** （gitignore），一次性脚本与临时日志放这里；沉淀为正式工具的脚本移入 `tools/` 并登记 README；`script/tmp/` 临时文件用 `tools/clean.py` 定期清理。

## 质量门与完成定义

* **一键全量复核**：`python tools/check_all.py`（七项门禁：结构/分类/单体/垃圾/术语/学术规范/汇总 + 单元测试；`--all` 加基线审计）——收工前与推审前必跑。
* **文档任务 done** = 六道全部完成（状态机 `r3_reviewed → done`）+ 学术规范挂钩通过（s3/r3 自动跑 `check_academic --docs --strict`，0 硬错误）+ `tools/check_style.py` 0 issue + markdownlint 绿 + CI 全绿。
* **结构改动 done** = `check_summary.py` 与 `check_mulu_s.py` 报告 0 坏链 0 标题不一致；`rebuild_dir.py check` 镜像无缺口。
* **术语改动 done** = 登记册新行有首现与裁定日期；发布词汇表同步。
* **更新任务输入** = `tools/compare.py <slug>` 的段落级变更清单（spec 001 US-3），evidence 以 `changes:` 开头引用。
* 每次提交 = 一个可回溯单元：中文一行提交信息 + 相关文件 + 必要凭证（任务 JSON 的 evidence、demo 日志）。

## 审计与可追溯（宪法 I/II 落地）

* 每件成品可回溯到英文源版本：任务 JSON 的 `version_pin`（pubinfo 日期 + 存档版名 + SHA-256）+ `baseline/entries.json`。
* 原始物不可变：`en/`、`yuanwen/` 的抓取副本不修改，一切产物可由原始物复算复核。
* 演示轮的流程问题与裁定记录在 `specs/<feature>/demo-log.md`，作为流程文档修订的输入。

## 规则自身的维护

* 本目录文件由治理职责的会话维护；其他会话发现规则缺失或过时，开 ADR 草案提请修订，不直接改条文。
* 规则与宪法冲突时：宪法优先；同时按上一条提交 ADR 修正规则。

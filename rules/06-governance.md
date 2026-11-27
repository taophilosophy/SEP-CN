# 软件工程治理

本规则把宪法七原则落实为日常可执行的治理机制：单一事实源登记、变更管理、并发会话纪律、质量门与审计。

## 单一事实源登记表

同一类事实只允许一个地方说了算；两处不一致时，修弱势一方向登记源看齐。

| 事实域 | 登记源 | 派生视图 / 校验工具 |
| ---- | ---- | ---- |
| 目录结构与标题 | `zh/SUMMARY.md` | 各文件 H1（CI 同步，别名行不覆盖）；`tools/check_summary.py` |
| 学科分类目录 | `zh/mu-lu-s.md`（手编） | `tools/check_mulu_s.py` 对应性检测 |
| 英文原文镜像 | `en/<letter>/<slug>.md`（管线转换，不入库） | `tools/compare.py`、`rebuild_dir.py check`、`baseline_audit.py` |
| 术语译法 | `zh/shu-yu-biao.md` 登记册（ADR-0036 改名） | ——（发布词汇表已并网删除，ADR-0036） |
| 人名译法 | `zh/ren-ming-biao.md` 登记册（ADR-0012） | ——（发布词汇表已并网删除，ADR-0036） |
| 词条版本事实 | `baseline/` 元数据清单 | `tools/baseline_audit.py` |
| 文档任务状态 | `tasks/<首字母>/<slug>.json` | `tools/task_ops.py show` |
| 流程与验收标准 | `specs/<NNN>-*/spec.md`、`plan.md` | `checklists/`、`demo-log.md` |
| 最高原则 | `.specify/memory/constitution.md` | 本目录规则为其操作性展开 |

## 变更管理

* **规则变更走 ADR**：影响面超出单词条的规则修订，在 `rules/adr/NNNN-标题.md` 新建决策记录（背景、决策、后果），再改规则文件；ADR 只追加不删除，废弃标记 superseded。
* **宪法修订**：提交信息注明“修订宪法 vX.Y”并说明理由（宪法 Governance 节）。
* **破坏性动作** （批量清空、重命名、结构重排）前置条件：受影响词条已有可信英文基线；动作可由 git 历史回溯；完成后运行对应校验工具并留凭证。
* **历史改写与批次护栏（tag）**：已裁定允许重写 git 记录（含 force push），**仅限用户显式授权期**（rules/README 判例：force push 属用户授权期专属；日常提交即推沿 ADR-0059 禁 force）。护栏约定：改写或批量动作前先打备份 tag（`git tag backup/<YYYY-MM-DD-说明>`），改写后立即 push 分支与 tag；每完成一个批次打 `batch/<批次名>` tag。tag 不限制自由，只保证任何时刻有退路。
* **CI 工作流变更** 须同步更新 `rules/05/ci-workflows.md` 的工作流清单表。

## 任务方向声明（宪法 VII 落地）

任何任务（翻译、结构、术语、工具、站点、规则修订、发布）开工前，按 [08-intent-first.md](08-intent-first.md) 写方向声明：一句话复述用户到底要什么，列目标、非目标与验收判据；需求含糊先问不猜。落点：文档任务写任务 JSON 的 `evidence` 首条；工程改动写 `specs/<NNN>-*/spec.md` 的 Assumptions 或 ADR 背景节。方向声明缺失视为未立项，质量门不予验收。

## 并发会话纪律（多会话并行开发）

本仓库常有多个 AI 会话/人工同时工作，纪律如下：

1. **提交前核对 HEAD**：`git log --oneline -3` + `git status`，确认基点未变；基点变了先 `git diff HEAD` 重放自己的改动。
2. **提交竞态重试**：commit 失败或“no changes added”时，先检查自己的文件是否已被对方提交卷入，确认内容无误后不必重复提交；确有剩余再补提交。提交默认免签（本机 GPG 已根治：`gpg.program` 指向 gpg4win、关闭自动签名，2026-11-06 用户裁定，与 [05](05/index.md) 提交策略同源）——无需 `--no-gpg-sign`；需要签名时显式 `git commit -S`（交互输口令）。
3. **推送先 pull**（2026-10-27 教训固化）：`git push` 被拒（non-fast-forward）或对方已推送时，先 `python tools/sync_guard.py pull`（含 fetch+rebase+判弃自检，ADR-0028）再推；带未授权 force push 期间，其他会话应停手或改为先 pull 再推——本日两次 force push 各孤儿化了并行会话的一个提交（587ec741、fb2a3317），其内容需对方会话重新落地。**提交即推**（ADR-0059，2026-11-16 用户裁定）：每次 commit 成功后立即 push，不再等用户要求；本条其余纪律不变。
4. **目录所有权边界**：词条内容归翻译会话；`specs/`、`.specify/`、`tools/`（管线包）、`baseline/` 归管线会话；`rules/`、`tasks/README.md`、`AGENTS.md` 归治理。跨界修改先在提交信息说明理由。
5. **不抢改他人正在写的文件**：发现非本人改动先读再动，禁止用 `git checkout --` / `reset --hard` 清理他人未提交工作。
6. **`script/` 为个人草稿区** （gitignore），一次性脚本与临时日志放这里；沉淀为正式工具的脚本移入 `tools/` 并登记 README；`script/tmp/` 临时文件用 `tools/clean.py` 定期清理。

### 子代理禁用（2026-11-10 用户裁定，ADR-0034）

* **主代理单干**：禁止主代理调用子代理（`Agent`／`Task` 工具，以及 workflow 的多子代理扇出）；翻译、校对、检索、核对、工具编写、批量改写一律由主会话亲自完成。写入路径唯一、核对链闭合，是宪法 I（零信任）与 II（可追溯）在会话层的落实。
* **唯一例外**：用户在本轮提示词中显式批准，并写明范围（任务边界、可写文件面、是否允许写入）；批准只对当轮有效，不继承到下一轮、下一任务或下一会话。
* **并行不是理由**：需要并行时改为串行，或由用户另开独立会话；独立会话之间只经 `origin/main` 同步（见下节），不属主从派发，也不因此获得豁免。
* **违例处置**：发现无主会话核对记录的写入（子代理产物），不得计入质量门全绿；须由主会话逐条重做、留证据后重新验收，并在对应 `specs/<NNN>-*/execution-log.md` 记一笔。
* **历史口径作废**：2026-11-02“不用子代理直译”与 2026-11-06“机械/工程类批量任务至多滚动 3 路子代理”不再有效，不得援引为先例。

### 多机并行（2026-11-09 起，ADR-0026；sync_guard 判弃自检 ADR-0028；提交即推 ADR-0059；定岗取消收编 ADR-0066）

* 两台机各持**独立克隆**：M1 `C:\Users\ykla\Documents\SEP-CN`（DESKTOP-RLOEIG9）、M2 `D:\SEP-CN`（Desktop-m5p610n）。**唯一同步面是 `origin/main`**，不以对方工作树为真值；共享克隆时代结束。（M1 侧的 `D:` 是映射网络盘 `\\Desktop-m5p610n\d`，只作只读观测，不写。）
* **分工不设岗（ADR-0066 收编 2026-11-16 用户裁定，取代 ADR-0028 定岗分工）**：任一机可做全部工作，无“词条翻译机／管线机”之分；同工种并行时按批次认领互斥（`campaign.py claim`/`release`），唯一同步面仍是 `origin/main`。ADR-0028 中继续有效的是 sync_guard 判弃自检与孤儿件处置（ADR-0059 已将其“积压线”作废）。
* 开工先对齐：`git fetch && git status -sb && python tools/sync_guard.py pull`（包装 `pull --rebase`，判弃自检实拦，ADR-0028），落后不干活。
* **提交即推（ADR-0059，2026-11-16 用户裁定）**：每次 `git commit` 成功后立即 `git push`；推前 `git fetch`，落后先 `python tools/sync_guard.py pull`，被拒重跑再推；`--force` 仍禁。ADR-0028 的“积压线”（途中 ≤1、收工清零）作废，收工核对改为 `git log origin/main..main` 为空；推不出去（代理不可用、网络中断）时记录失败命令与时间，恢复后第一时间补推。批次认领／`campaign.py advance`／条目 done 三个检查点仍必须已推送。
* **孤儿件处置（ADR-0028）**：本地提交不在远程历史时，先 `git cherry` 判内容是否已在远程；已在→本地弃置；不在→reflog 恢复后推送。处置记入对应 spec execution-log，禁止静默。
* **机器身份以 IP 区分**（两机 git 用户名同为 `ykla`）：M1 `192.168.5.6` → `pc6`，M2 `192.168.5.4` → `pc4`；标签存各克隆本地配置 `git config --local ykla.machine`，会话 ID 前缀取之（`pc6-c-s3-20261109`）。当场取法：`ipconfig | grep -a IPv4 | head -1`。批次交接用 `campaign.py release <批> --note`，接手方重新 claim。
* **生成物冲突不手工解**：`zh/PROGRESS.md` 任取一侧后 `tools/progress.py` 重生成；`zh/SUMMARY.md` 取并集后 `check_summary.py`；账本 rebase 后重放 `campaign.py advance`（幂等）；术语表／人名表追加式书写，冲突取并集后 `check_terms.py`。
* 两机尽量不同时开工同一字母批，压低 `zh/SUMMARY.md` 与登记册的文本冲突面；本地相（`script/`、`state/`、`.secrets/`；`html/`、`en/` 已随 ADR-0027 入库）各机自持，不入库不共享。
* **M1 的 GitHub 访问经 M2 代理**（`192.168.5.4:7890`，本机直连因 TLS 吊销检查脱机不可用）；M2 关机时 M1 无法 push/pull，需等其上线或改用局域网直连仓库应急。`check_all --all` 每次会改写 `specs/001/en-integrity-full.json` 的 `ran_at`，提交前还原，别把时间戳当改动。

## 质量门与完成定义

* **一键全量复核**：`python tools/check_all.py`——门禁清单以 `python tools/check_all.py --list-gates` 为准（`GATES` 为唯一事实源，ADR-0061；本文件不复制项数，ADR-0015）；`--all` 另加基线审计、英文镜像复核与分歧深核。收工前与推审前必跑。
* **文档任务 done** = 六道与 s2.4/s2.5 前置环节全部完成（状态机 `r3_reviewed → done`，含 `s2.4_termchecked`/`s2.5_checked`，ADR-0040/0043；**r3 终审仅用户显式指定的会话执行，未指定时条目停 r2_reviewed、done 冻结，ADR-0054**）+ 学术规范挂钩通过（s3/r3 自动跑 `check_academic --docs --strict`，0 硬错误）+ `tools/check_style.py` 0 issue + markdownlint 绿 + CI 全绿。
* **结构改动 done** = `check_summary.py` 与 `check_mulu_s.py` 报告 0 坏链 0 标题不一致；`rebuild_dir.py check` 镜像无缺口。
* **术语改动 done** = 登记册新行有首现与裁定日期（ADR-0036：发布词汇表已并网删除，无同步步骤）。
* **更新任务输入** = `tools/compare.py <slug>` 的段落级变更清单（spec 001 US-3），evidence 以 `changes:` 开头引用。
* **完成定义以验收判据为准**：不以工具使用、流程走完、文档篇幅或工时衡量；收工自检“本次改变了哪个决策、产物或门禁”（[08](08-intent-first.md)）。
* 每次提交 = 一个可回溯单元：中文一行提交信息 + 相关文件 + 必要凭证（任务 JSON 的 evidence、demo 日志）。

## 审计与可追溯（宪法 I/II 落地）

* 每件成品可回溯到英文源版本：任务 JSON 的 `version_pin`（pubinfo 日期 + 存档版名 + SHA-256）+ `baseline/entries.json`。
* 原始物双账：`html/` 的台账 sha256 永远是**原始网页钉**（不随勘误/重转改写），批准勘误的本地偏离逐条登记 `baseline/en-errata/divergences.json`（ADR-0076），未登记的静默改动由 `divergence.py verify` 门禁红灯；`en/` 的抓取与转换副本不修改，一切产物可由原始字节复算复核（ADR-0027/0038/0045）。
* 演示轮的流程问题与裁定记录在 `specs/<feature>/demo-log.md`，作为流程文档修订的输入。

## 规则自身的维护

* 本目录文件由治理职责的会话维护；其他会话发现规则缺失或过时，开 ADR 草案提请修订，不直接改条文。
* 规则与宪法冲突时：宪法优先；同时按上一条提交 ADR 修正规则。
* **文档质量五属性年审**（GB/T 32424 / ISO/IEC/IEEE 26514，2026-11-14 采纳，ADR-0041）：本目录规则文件年度复审时按完整性、正确性、清晰性、一致性、可用性五属性逐件过一遍；任一属性失守的条文按形式主义条款（doctrine 00 §9）删除、降级或修订。

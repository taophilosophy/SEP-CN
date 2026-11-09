# Feature Specification: 双机双克隆工作区（M1 迁入本地 C 盘）

**Spec ID**: `014-multi-machine-cutover` | **Created**: 2026-11-09 | **Status**: Ready（cutover 待执行）

**Input**：用户指令（2026-11-09）：「把 UNC 路径的 SEP-CN git 到本地 C 盘文档下面。以后都在 C 盘文档的 SEP-CN fork 分支工作，仅必要的才 push 到 SEP-CN main。」；补充「D 盘在另一个电脑上会同步处理其他条目的翻译。你设计一下。准备迁移。」

## 背景（2026-11-09 实测）

| 事实 | 值 |
| --- | --- |
| 现工作区真实路径 | `//Desktop-m5p610n/d/SEP-CN`（SMB 共享，非本地盘） |
| 仓库规模 | 7461 个跟踪文件；1188 个 `tasks/*.json`；`.git` 136.9 MB pack；含 `en/`+`yuanwen/` 工作树 2.1 GB |
| 基础操作耗时（SMB） | `git status` 495 ms / `git diff --stat` 1067 ms / `git log` 278 ms |
| 全量门禁耗时（SMB） | `check_all.py` 27 s（AGENTS.md 记录的本地基线 ~6 s） |
| 最长跟踪路径 | 138 字符（`specs/008-.../results/queries/termonline-all/...json`） |
| 绝对路径耦合 | 0（tools/specs/rules 无 `D:\SEP-CN`、无 `Desktop-m5p610n` 引用） |
| 本机 | `DESKTOP-RLOEIG9`，**192.168.5.6**；C 盘余量 812 GB；`Documents` 未被 OneDrive 重定向（OneDrive 根在 `C:\Users\ykla\OneDrive`） |
| 另一台机 | `Desktop-m5p610n`，**192.168.5.4**，`D:\SEP-CN` 即其本地克隆 |
| git 作者 | 两机同为 `ykla <yklaxds@gmail.com>` —— **提交作者无法区分机器** |
| origin | `taophilosophy/SEP-CN`（**private**），唯一异地副本 |

## 目标

1. **M1（本机）** 在 `C:\Users\ykla\Documents\SEP-CN` 建立独立本地克隆，日常操作脱离 SMB。
2. **M2（Desktop-m5p610n）** 保留 `D:\SEP-CN` 原克隆，继续并行处理**其他词条**，两机经 `origin/main` 同步。
3. 非入库本地相（`en/`、`yuanwen/`、`script/`、`state/`、`.secrets/`、`node_modules/`）搬迁或重建，`check_all --all` 9/9 全绿。
4. 双机双写协议写进规则（ADR 0026 + `rules/06` + `AGENTS.md`），不依赖会话记忆。

## 非目标

- 不建 GitHub fork（自家 private 仓库，fork 是多余层）；「fork 分支」落地为**短命本地批次分支**或直接 main + 小提交。
- 不改词条内容与工具逻辑（零硬编码路径，迁移零改码）。
- 不把 `en/`、`yuanwen/` 入库（宪法 II 不变，各机自持本地相）。
- 不做长期分叉线：两机必须高频对齐 `origin/main`。

## 裁定与假设

* **落点** `C:\Users\ykla\Documents\SEP-CN`：根 40 字符 + 最长路径 138 = 178 < 260，无需 `core.longpaths`；`Documents` 不在 OneDrive 同步范围。
* **同步面唯一**：`origin/main`。两机都不以对方工作树为真值。
* **push 节奏 = 三个检查点**（这是「仅必要的才 push」的可执行定义）：① 批次认领（抢锁）② 阶段推进（`campaign.py advance`）③ 条目 done 收口。其余微提交留本地。
* **生成物冲突不手工解**：`PROGRESS.md` 冲突任取一侧后 `python tools/progress.py` 重生成；`SUMMARY.md` 取并集后 `check_summary.py`。
* **机器身份以 IP 区分**（两机 git 用户名同为 `ykla`，作者名不可辨）：M1 `192.168.5.6` → 标签 `pc6`，M2 `192.168.5.4` → 标签 `pc4`。标签存于各克隆**本地配置** `git config --local ykla.machine`（不入库、不随克隆走），会话 ID 前缀取该标签（如 `pc6-c-s3-20261109`），`campaign.py status` 一眼可辨归属。DHCP 变更时以当场 `ipconfig` 为准并回写本文。
* **记忆按路径键**：现有键 `sep-cn-33d65d943eb3eb8a` 是路径派生，迁移后新路径产生**空记忆项目**，必须人工搬运（runbook §5）。

## 职责分工

* 批次级互斥由账本认领保证（`campaign.py claim/advance/release`），**不按字母硬分**——已认领批次即锁。
* 两机**尽量不同时开工同一字母批**，以降低 `SUMMARY.md`／术语表／人名表的文本冲突面。
* 交接：`campaign.py release <批> --note "转交 m2-…"`，接手方重新 claim。

## 同步协议（每次开工与收口）

```bash
# 开工
git fetch origin && git status -sb          # behind 即先 rebase
git pull --rebase origin main
python tools/campaign.py status

# 认领（抢锁后立即推，别攒）
python tools/campaign.py claim <批> --session pc6-<场景>-<日期>
git add specs/005-translation-campaign/ledger.json && git commit -m "…"
git push

# 收口
python tools/progress.py                    # 生成物重生成，避免手改冲突
python tools/check_all.py
git add -A <本批文件>
git commit -m "…"
git fetch && git pull --rebase origin main && git push
```

## 冲突面与处置

| 文件 | 并发概率 | 处置 |
| --- | --- | --- |
| 词条 `<letter>/<slug>.md`、`tasks/<letter>/*` | 无（slug 互斥） | — |
| `specs/005-translation-campaign/ledger.json` | 低（按批次键分行） | rebase 后重放 `campaign.py advance`（幂等）；手工合并时两侧批次键都保留，再 `campaign.py status` 校验 |
| `PROGRESS.md` | 高（生成物） | 任取一侧 → `python tools/progress.py` |
| `SUMMARY.md` | 中（两侧加不同字母） | 取并集 → `python tools/check_summary.py` |
| 术语表／人名表／词汇表 | 中高 | **追加式**：只在本节末加行、不改序、不动他人行；冲突取并集 → `python tools/check_terms.py` |
| `en/`、`yuanwen/` | 无（不入库） | 各机自算；以 `baseline/`、`specs/001/en-integrity-full.json` 台账为准 |

## 验收判据

1. C: 克隆 `HEAD == origin/main`，`git status` 干净。
2. `python tools/check_all.py --all` **9/9 全绿**（第 9 项「英文镜像深度复核」依赖本地 `en/`，缺则必红）。
3. `python tools/campaign.py status` 与 M2 同刻输出一致（允许在途差异，须可解释）。
4. 抽 1 条在途词条：`task_ops.py show <slug>` + 段落账本 `lq check` 干跑通过。
5. `en/` 顶层条目数、`yuanwen/` 镜像缺口与 D: 一致（差值 0，或已登记原因）。
6. 本机不再可写 D:（卸载映射或只读），`/d/SEP-CN` 写入即失败。
7. 新路径下记忆可用：`MEMORY.md` 行数与旧键一致（20+ 行）。

## 关键文件

* `specs/014-multi-machine-cutover/cutover-runbook.md` —— 开闸后的逐步操作单
* `specs/014-multi-machine-cutover/bin/verify-clone.sh` —— 验收脚本
* `rules/adr/0026-双机双克隆工作区.md` —— 决策记录
* `rules/06-governance.md` §并发会话纪律 —— 双机条款
* `AGENTS.md` —— 开工五分钟与提交纪律同步改写

## 风险与回退

| 风险 | 缓解 |
| --- | --- |
| cutover 期间本机仍有会话写 D:，造成双写 | 本机所有会话先停；切换后卸载 D: 映射，物理上禁止写 |
| 2.1 GB 本地相拷贝中断 | `robocopy /MIR /R:1 /W:1` 幂等续传；先拷再验收 |
| M2 在拷贝期间继续抓取写入 `en/` | 目标只是本机副本，无写冲突；验收按「拷贝时刻」快照比对 |
| 两机同改登记册造成文本冲突 | 追加式纪律 + 冲突取并集 + `check_terms` 兜底 |
| 密钥/凭证外泄 | `.secrets/` 只做本机 robocopy，任何情况下不入库（`.gitignore` 已含） |
| 迁移失败 | **零损失回退**：D: 未删未改，本机直接回 D: 继续工作；唯一不可逆点是 C: 上的写入 |
| **M1 的 GitHub 访问依赖 M2 代理**（`192.168.5.4:7890`，本机直连因 TLS 吊销检查脱机不可用） | M2 关机即断同步面。缓解：本机自建代理／修根证书吊销／SSH over 443。在解决前，M2 需常开 |

**回退触发**：`check_all --all` 9/9 不过且 30 分钟内无法修复 → 本机回 D: 工作，C: 克隆保留待查。

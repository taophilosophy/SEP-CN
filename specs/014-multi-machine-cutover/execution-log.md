# 014 双机双克隆工作区 · 执行记录

## 2026-11-09 准备阶段：设计与开工单（完成，未执行 cutover）

**指令来源**：用户「把 UNC 路径的 SEP-CN git 到本地 C 盘文档下面……仅必要的才 push 到 SEP-CN main」；补充「D 盘在另一个电脑上会同步处理其他条目的翻译。你设计一下。准备迁移。」

**方向声明**：把共享的 SMB 克隆拆成两台机的独立克隆（M1 本机 C 盘、M2 保留 D 盘），只经 `origin/main` 同步；迁移期间 M2 不停工。

**落地物**

* `specs/014-multi-machine-cutover/spec.md` —— 目标/非目标、同步协议、冲突面与处置、验收判据
* `specs/014-multi-machine-cutover/cutover-runbook.md` —— 7 段开工单（预检 → 克隆 → 搬本地相 → 环境 → 验收 → 记忆迁移 → 封口）
* `specs/014-multi-machine-cutover/bin/verify-clone.sh` —— 验收脚本（HEAD/工作树/本地相/门禁，可 `--skip-gate`）
* `rules/adr/0026-双机双克隆工作区.md` + 索引 —— 决策记录
* `rules/06-governance.md` §并发会话纪律 → 新增「多机并行」小节
* `AGENTS.md` —— 开工五分钟、多会话分批、提交纪律三处同步改写

**实测基线（迁移前，SMB）**

| 项 | 值 |
| --- | --- |
| 工作区路径 | `//Desktop-m5p610n/d/SEP-CN` |
| 跟踪文件 | 7461 |
| `tasks/*.json` | 1188 |
| 工作树（含 en/yuanwen） | 2.1 GB |
| `.git` pack | 136.9 MB |
| `git status` | 495 ms |
| `git diff --stat` | 1067 ms |
| `check_all.py` | 27 s（本地基线 ~6 s） |
| 最长跟踪路径 | 138 字符（C 盘落点后 178 < 260） |
| 绝对路径引用 | 0 处 |

**迁移期间观察到的并行活动**：本会话开始后 D: 侧仍在高频提交（HEAD 从 `8f106564` 推进到 `722a9f94`，5 分钟 5 提交，并已有 push 落到 origin）。因此 cutover 的冻结范围限定为**本机（M1）会话**，M2 不需停手。

**未做（留待开闸）**：克隆、本地相拷贝、`bun install`、`check_all --all` 验收、记忆搬运、D: 卸载、`batch/cutover-20261109` tag。

**风险预记**：最大风险是 cutover 期间本机仍有人写 D:，造成双写；封口步骤（卸载映射 → 写入必须失败）是硬验收项。

## 2026-11-09 补记：机器身份改用 IP 区分

**指令**：用户「另一个机器上用户名也是 ykla。用 IP 进行区分。」

**裁定**

* 两机 git 作者同为 `ykla <yklaxds@gmail.com>`，提交历史无法区分来源；原 `m1-/m2-` 前缀是人为约定，易混。
* 改用**局域网 IP 标签**：M1 `192.168.5.6` → `pc6`（DESKTOP-RLOEIG9，C 盘克隆）；M2 `192.168.5.4` → `pc4`（DESKTOP-M5P610N，`D:\SEP-CN`）。
* 标签存于各克隆**本地配置** `git config --local ykla.machine`（不入库、不随克隆传递，M2 需自行设一次）；会话 ID 形如 `pc6-c-s3-20261109`。
* 已同步改写：`spec.md`（背景表 + 裁定 + 协议示例）、`rules/adr/0026`（决策 8）、`rules/06-governance.md`（多机并行条款）、`cutover-runbook.md`（§0 预检、§1 克隆、§6 封口）。
* DHCP 前提：地址若变，以当场 `ipconfig` 为准并回写 ADR 与本文。

**并发实例（本次发生）**：本会话 `git add` 014 与规则文件后，另一并行会话先一步 `git add -A` 提交，本会话 commit 报 "no changes added"；核对 `git ls-files` 确认全部文件已入 9857e239 / 73a61548，按 `rules/06` 第 2 条不重复提交。这是双机双克隆后会更频繁的竞态，验证了「认领即推、生成物重生成」设计的必要性。

## 2026-11-09 执行：cutover §1–§5（完成）

**网络插曲**：本机直连 GitHub 失败（`CRYPT_E_REVOCATION_OFFLINE` + github.com 超时）；用户指定代理 `192.168.5.4:7890`（M2 上）。设 `git config --global http(s).proxy` 后 `ls-remote` 正常，origin/main = `94790df1`，与 D: HEAD 一致。

| 步骤 | 实测 |
| --- | --- |
| SMB 克隆（先试） | **失败**：`.git` 停在 70 MB，16 s 无增长（源仓库被他机 git 操作占锁）→ 终止并删除半成品 |
| origin 克隆 | **127 s**，7488 个文件（走代理） |
| 配置 | `user.name/email`、`core.ignorecase=true`、`ykla.machine=pc6`、`autocrlf` 继承全局 `input` |
| 本地相 robocopy | **27 s**：`en` 5434 文件/0.35 GB、`yuanwen` 4267/0.29 GB、`script` 7185/0.41 GB、`state` 58、`.secrets` 2 |
| 两机比对 | en 顶层 1884:1884、递归 5434:5434；yuanwen 29:29、4267:4267 —— 零差异 |
| `bun install` | 8 s，135 包，`node_modules` 99 项 |
| `check_all --all` | **9/9 全绿**（冷启 44 s） |
| `check_all`（7 项） | 冷 15 s / 温 13 s（D: 同项 27 s） |
| `verify-clone.sh` | 全部 OK |

**发现的两个噪声源（已还原，建议跟进）**

* `bun.lock`：本机 bun 1.4.4 安装时补写 `"configVersion": 0`，与仓库现有 lock 有格式差；已 `git checkout --`。
* `specs/001-sep-sync-pipeline/en-integrity-full.json`：`check_all --all` 每次都改写 `ran_at`（本次仅时间戳变，audited/clean/1879 与 hard=0 不变）→ **每次 `--all` 必脏一处**。建议让 `tools/en_integrity.py` 在结论未变时不改写该字段（或用 `--quiet` 抑制写回）。双机后这条会成为常态噪声。

**记忆迁移（提前完成）**：反解出键算法 `sep-cn-` + `sha256(工作区路径小写、反斜杠形式)[:16]`（校验：`d:\sep-cn` → `33d65d943eb3eb8a`）。新键 `sep-cn-1f5dbdf5bb3376f8` 已预建并全量拷贝 20 个文件，新路径首次开会话即可召回，无需手工搬运。

**新增约束（重要）**：M1 的 GitHub 访问**依赖 M2 上的代理** `192.168.5.4:7890`（本机直连因 TLS 吊销检查脱机不可用）。M2 关机时 M1 无法 push/pull——「唯一同步面」反而被单点化。缓解方向：本机自建代理／修复根证书吊销检查／或改用 SSH over 443。已记入 `spec.md` 风险表。

## 2026-11-09 复验：一次真实的并发中间态红

`verify-clone.sh` 首轮 9/9 绿之后十余分钟，`check_terms` 报硬错误 1（`paradox of suspense`：登记册「悬念悖论」vs 词汇表「悬疑悖论」）。追查结论：

* 该红**不是迁移缺陷**，是并行会话在 17:3x 把 M2 的登记册 A–Z 分节重构合入 C: 时的**中间态**；M2 于 17:49 提交 `2f3b394d`（词汇表行补「亦作『悬念悖论』」）后，合并入 C: 即复绿（现 9/9）。
* 取证方法可复用：`check_terms.py --registry <单提交导出> --glossary <同>` 注入单表模式，能判定冲突属于哪个提交，不必动他人工作树。
* **暴露的纪律问题**：C: 历史出现多个 `Merge branch 'main' of https://github.com/...`（`1839013b`/`3070e112`/`2ce504be`），说明有会话用裸 `git pull`（merge）而非 `--rebase`，与 `rules/06` 第 3 条相悖；双机后合并图会越来越乱，须纠正。
* **脚本改进点**：`verify-clone.sh` 首轮把 `git status` 报成 45 项脏，实为 clone 后 index 未刷新的 racy-git 假阳性（随后自收敛到 2 项）。建议脚本开头加 `git update-index --refresh >/dev/null 2>&1 || true` 再计数。

## 2026-11-09 原始物入库（ADR-0027）

用户裁定「en、yuanwen 也入 git 库；其他应入 git 库的文件应入尽入」。落地为宪法 II 修订（v1.2.0 → **v1.3.0**）+ ADR-0027。

**边界**：`en/`、`yuanwen/` 入库；`.secrets/`（凭证）永不入库；`script/`（个人草稿）、`state/`（运行态）、`node_modules/`、缓存与生成物仍忽略——「应入尽入」以规则既有边界为准。

**改动面**：`.gitignore` 撤 `/en/`×2 与 `/yuanwen`；`.gitattributes` 新增 `en/** -text`、`yuanwen/** -text`（**关键**：全局 `core.autocrlf=input` 会把 CRLF 归一化，破坏原始物字节与 sha256 对账）；`check_junk` 撤 `^en/` 规则；`clean.py` 的 `SKIP_DIRS` 增 `yuanwen`；`check_images`/`check_academic` 的「CI 无原始物」降级注释改写；`rules/01`、`rules/05`、`AGENTS.md`、`tools/README.md`、`specs/001` FR-014 同步。

**体积**（实测）

| 目录 | 文件 | 文本 | 图片 |
| --- | --- | --- | --- |
| `en/` | 5434 | 273 MB（3595） | 106 MB（1839） |
| `yuanwen/` | 4262 | 209 MB（2428） | 106 MB（1839，与 en 同内容，git 自动去重） |

未推提交的压缩包实测 **233 MiB**（`git pack-objects` 全量重算）。

**事故：en/ 被并行客户端清空**。19:2x 时 `en/` 从 5434 文件变成 0 文件（仅剩 2 个空目录）。根因线索：GitHub Desktop 于 09:19Z 把 `C:\Users\ykla\Documents\SEP-CN` 加入其仓库列表，随后在 09:45Z 有 commit 动作，日志中出现 `Unable to create index.lock`——GUI 客户端与本会话争用同一仓库，其「丢弃更改」类操作会删除未跟踪文件，而当时 `en/` 尚未入库。处置：从 M2 副本 `robocopy /MIR` 恢复（5434 文件，27 s），随即 `git add en` 入库，**已跟踪后不会再被 clean 类操作删除**。

**分叉与 rebase**：本地 3 提交（宪法修订 / yuanwen / en）与 M2 的 23 提交分叉，`git pull --rebase` **零冲突**——文件面完全不重叠（本地改规则/工具/宪法，M2 改词条/任务/登记册）。rebase 后 M2 又推进 6 提交，再次 rebase 仍零冲突。

**带宽与推送策略**：代理 `192.168.5.4:7890` 上行实测 **87 KB/s**（10 MB 上传 120 s 超时）；直连 GitHub 被 reset，代理是唯一通路 → 233 MiB ≈ 45 分钟。为免「每被 M2 顶掉一次就重传 233 MB」，先推独立分支 `archive/raw-20261109`（main 移动不影响它），对象在 GitHub 侧共享，随后推 main 只传 commit 对象增量。

**遗留纪律问题**：GitHub Desktop 用 merge 而非 rebase，且会与命令行争用 `index.lock`——建议 M1 关闭该仓库的 GUI 窗口，否则双机合并图与工作树都会被它搅乱。

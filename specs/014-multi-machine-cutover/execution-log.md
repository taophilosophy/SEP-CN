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

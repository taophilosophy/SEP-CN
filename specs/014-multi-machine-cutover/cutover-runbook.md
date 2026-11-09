# Cutover Runbook：M1 迁入 `C:\Users\ykla\Documents\SEP-CN`

**版本**：v1.0 | **日期**：2026-11-09 | **对应规格**：`specs/014-multi-machine-cutover/spec.md`

> 执行前提：本机（DESKTOP-RLOEIG9）所有会话已停手；D: 侧（Desktop-m5p610n）**可以继续工作**，不需冻结。
> 每一步都有验收点，不过不进下一步。

## 0. 预检（2 分钟）

```bash
cd /d/SEP-CN
git log --oneline -3
git status --porcelain | wc -l          # 必须为 0：本机在途工作先自行提交并 push
git fetch origin && git status -sb      # 记录基点：HEAD 与 origin/main 的关系
ls -d .secrets script state en yuanwen  # 本地相清单
```

验收：无本机未提交文件；`en/`、`yuanwen/`、`script/`、`state/`、`.secrets/` 均存在。

> 若 `git status` 非空：先确认这些改动属于**本机**会话。属于 D: 侧会话的改动不要代提交，等其收口。

## 1. 建克隆（2–5 分钟）

```bash
git clone https://github.com/taophilosophy/SEP-CN.git /c/Users/ykla/Documents/SEP-CN
cd /c/Users/ykla/Documents/SEP-CN
git config user.name  ykla
git config user.email yklaxds@gmail.com
git config core.ignorecase true
git config core.longpaths false          # 最长路径 178 < 260，无需开启
```

验收：

```bash
git log -1 --format='%h %ad %s' --date=iso
git rev-list --count HEAD..origin/main   # 0
git ls-files | wc -l                     # ≈7461（随 M2 新提交略增）
```

**不从 SMB 克隆**：origin 的 pack 更干净，且顺便验证异地备份可用。

## 2. 搬本地相（20–40 分钟，最慢一步）

在 **cmd** 中执行（Git Bash 的路径翻译会干扰 robocopy）：

```bat
robocopy "\\Desktop-m5p610n\d\SEP-CN\en"      "C:\Users\ykla\Documents\SEP-CN\en"      /MIR /R:1 /W:1 /MT:16 /NFL /NDL /NP
robocopy "\\Desktop-m5p610n\d\SEP-CN\yuanwen" "C:\Users\ykla\Documents\SEP-CN\yuanwen" /MIR /R:1 /W:1 /MT:16 /NFL /NDL /NP
robocopy "\\Desktop-m5p610n\d\SEP-CN\script"  "C:\Users\ykla\Documents\SEP-CN\script"  /MIR /R:1 /W:1 /MT:16 /NFL /NDL /NP
robocopy "\\Desktop-m5p610n\d\SEP-CN\state"   "C:\Users\ykla\Documents\SEP-CN\state"   /MIR /R:1 /W:1 /MT:16 /NFL /NDL /NP
robocopy "\\Desktop-m5p610n\d\SEP-CN\.secrets" "C:\Users\ykla\Documents\SEP-CN\.secrets" /MIR /R:1 /W:1 /MT:16 /NFL /NDL /NP
```

验收（Git Bash）：

```bash
cd /c/Users/ykla/Documents/SEP-CN
ls en | wc -l                 # 与 D: 同刻 `ls /d/SEP-CN/en | wc -l` 比对（≈1884）
ls .secrets                   # cnki-session.json termonline-session.json
git status --porcelain        # 必须为空：这些目录均在 .gitignore 内
```

## 3. 环境（5–10 分钟）

```bash
bun install
bun .vitepress/prepare-assets.mjs
bun .vitepress/prepare-gitstamps.mjs
```

Python 侧无第三方依赖（tools 全用标准库，Python 3.15），不需要 venv。

验收：`bun .vitepress/prepare-assets.mjs` 无报错；`ls node_modules | wc -l` ≈100。

## 4. 验收（硬门槛，10–20 分钟）

```bash
python tools/check_all.py --all       # 9/9 全绿（第 9 项要 en/）
python tools/check_all.py             # 7/7
python tools/campaign.py status       # 与 M2 同刻输出比对
python tools/task_ops.py show <在途slug>   # 抽一条
bash specs/014-multi-machine-cutover/bin/verify-clone.sh
```

**不过不进第 5 步。**

## 5. 记忆迁移（关键，易漏）

ZCode 的项目记忆按工作区路径派生目录键。新路径会打开一个**空记忆项目**——现有 20+ 条 SOP、用户裁定、对账口径全部不会加载。

```bash
# 1) 在新路径（C:\Users\ykla\Documents\SEP-CN）开一次会话，让新键目录生成
# 2) 找到新键（sep-cn- 前缀，hash 与旧键不同）
ls /c/Users/ykla/.zcode/cli/memories/projects | grep '^sep-cn-'
# 3) 搬运（旧键：sep-cn-33d65d943eb3eb8a）
cp -r /c/Users/ykla/.zcode/cli/memories/projects/sep-cn-33d65d943eb3eb8a/memory/. \
      /c/Users/ykla/.zcode/cli/memories/projects/<新键>/memory/
```

验收：新会话里 `MEMORY.md` 行数与旧键一致；能召回 `sep-cn-abcde-takeover-sop`。

## 6. 切换与封口（5 分钟）

```bash
cd /c/Users/ykla/Documents/SEP-CN
git tag batch/cutover-20261109 && git push origin batch/cutover-20261109
```

本机（DESKTOP-RLOEIG9）：

* 所有会话改在 `C:\Users\ykla\Documents\SEP-CN` 打开。
* **卸载/只读 D:**：`net use D: /delete`（若为映射盘）；或移除 `\\Desktop-m5p610n\d` 凭据，确保 `/d/SEP-CN` 写入失败。
* 验收：`touch /d/SEP-CN/.write-test` 必须失败。

D: 侧（Desktop-m5p610n）：

* 原克隆保持不动，按双机协议继续（开工 pull、认领即 push）。
* `SEP-CN-headcheck` worktree 由该机自行决定去留（与 M1 无关）。

## 7. 记录（5 分钟）

在 `specs/014-multi-machine-cutover/execution-log.md` 记录：

* 实际耗时（克隆 / 拷贝 / 安装 / 验收分段）
* 拷贝前后 `en/`、`yuanwen/` 文件数
* `check_all --all` 原始输出结论
* 迁移中遇到的新坑与处置

## 回退

任一硬门槛不过且 30 分钟内无法修复：

```bash
cd /d/SEP-CN          # 回到原克隆继续工作（D: 未删未改，零损失）
```

C: 克隆保留待查，不删除、不影响 D:。

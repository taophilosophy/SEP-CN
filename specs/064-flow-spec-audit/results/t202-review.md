# T202 起点登记（免备份）

- 日期：2026-11-27
- 裁定：用户明确“不设备份，Git 管理”；`state/layout-backup/2026-11-27/` 不创建。
- 本仓起始 commit：`df3dce234b2fed79903eb304939ab7cda4674ab8`
- 壳仓起始 commit：`571b16267a0d99bcfacf4138fa1b2facbb1de885`（本地 `docs/` 为目录联接，壳仓 `git status` 显示 `M docs` 属预期）
- 起始工作区：除本卡文档外干净；`check_all.py` 23/23 全绿（2026-11-27）。
- 待迁清单：`en/` 1875 个一级目录（HTML 源）、`yuanwen/` 28 个一级目录（Markdown 镜像＋`assets`）、根级 31 个目录（27 字母／数字＋4 中文目录）、`SUMMARY.md` 2787 行。
- 回退方式：
  1. 单步：`git restore --staged --worktree .`（未提交时）或 `git checkout -- <path>`；
  2. 整体：`git reset --hard df3dce234b2fed79903eb304939ab7cda4674ab8`，再 `git clean -fd` 清除未跟踪文件；
  3. 壳仓：`git -C taophilosophy.github.io reset --hard 571b16267a0d99bcfacf4138fa1b2facbb1de885`（只影响壳侧文件；`docs` 指针随本仓恢复）。
- 验收：起始 commit 可解析、回退命令已复核；工作区在开工前干净。

# 提交策略

* 高频小步提交：完成一个单元立即提交，不攒大批改动。
* 提交信息中文一行简述，如“重译 阿尔克迈翁：初译 + 一校”。
* 只提交与本次工作相关的文件；原始物（`en/`、`yuanwen/`、`script/`）不入库。
* 直接提交 main 分支；**提交即推**（ADR-0059，2026-11-16 用户裁定）：`git commit` 成功后立即 `git push`，推前 `git fetch`、落后先 `python tools/sync_guard.py pull`，被拒重跑 pull 再推；`--force` 仍禁。
* 本机 GPG 已根治（2026-11-06 用户裁定）：私钥在 gpg4win（`C:/Program Files/GnuPG/bin/gpg.exe`）而全局曾配 `commit.gpgsign=true` 是“签名失败/挂死”根源；现已全局 `gpg.program` 指向 gpg4win 并关闭自动签名——提交默认免签、无需 `--no-gpg-sign`，需要签名时显式 `git commit -S`（交互输口令）。

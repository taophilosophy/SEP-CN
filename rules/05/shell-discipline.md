# 本机 shell 工具纪律（2026-11-06 考据）

ZCode Bash 工具在本机（Windows + Git Bash）的三条实测判据，均为静默失真类；细则与回归探针见项目记忆“本机工具坑”。

* **grep 实为 ZCode 注入函数（ugrep 7.8.4）**：函数预置 `-G --ignore-files --hidden -I`（定义在会话启动脚本，晚于用户 profile），**`--ignore-files` 按 .gitignore 语义过滤**——查 `en/`、`yuanwen/`、`script/` 等被忽略路径或做全量计数会**静默假 0**。判据：用 `command grep`／`/usr/bin/grep`，或追加 `--no-ignore-files`（ugrep 后旗标优先，实测可反转）；可疑时 `type -a grep` 验身份。
* **Bash 参数反斜杠连串减半**：MSYS argv 层把不在 `"` 前的 `\` 连串按 ceil(n/2) 减半（`\\`→`\`、`\\\\`→`\\`），quoted heredoc 不保护；单反斜杠（`\d`、sed `\t`、Windows 路径）与 `\` 紧邻 `"` 场景无损。判据：要 N 连串写 2N 个；正则块、多表达式 sed、含 `\\` 的 python 一律 Write 落盘再执行、sed 用 `-f`。
* **中文内联编码复测无损**（2026-11-06，python 3.14 UTF-8 默认）；中文落盘仍优先 Write 脚本文件（防御性，成本为零）。

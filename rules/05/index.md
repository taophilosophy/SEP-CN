# CI 约定与本地工具（总览）

本规则约定 CI 工作流的行为边界与本地工具的使用方式。**本地脚本只是 CI 的预演，结果以 CI 为准**（宪法 VI）。

工具与工作流都是手段：新增或修改检查器前，先确认要拦哪类错误、以哪条门禁验收；不以工具数量、运行时长或 CI 次数衡量治理成效（[08](../08-intent-first.md)）。

## 子文件索引

本目录于 2026-11-19 按 ADR-0004 拆分（原 `rules/05-ci-and-tools.md` 达 30KB 触顶）：每文件一主题，改哪类规则就改哪份文件。

| 子文件 | 内容 |
| ---- | ---- |
| [ci-workflows.md](ci-workflows.md) | CI 工作流清单、运行时基线、工作流变更纪律 |
| [tools.md](tools.md) | 本地工具表、快速命令、lint 配置与表格风格 |
| [site.md](site.md) | 站点运行（本地预演） |
| [batch-rewrite.md](batch-rewrite.md) | 生成器与批量改写脚本纪律 |
| [judgment-rights.md](judgment-rights.md) | 判定权与规则所有权（ADR-0063）、升门四件套、测量效度 |
| [commit-policy.md](commit-policy.md) | 提交策略（提交即推，ADR-0059） |
| [shell-discipline.md](shell-discipline.md) | 本机 shell 工具纪律（Windows + Git Bash 实测判据） |

* 新增门禁/工具时：先改 `tools/check_all.py` 的 `GATES`（CI 矩阵自动跟随），再在 [tools.md](tools.md) 工具表与 [ci-workflows.md](ci-workflows.md) 工作流条目登记；判定权归属在 [judgment-rights.md](judgment-rights.md) 认领。
* 本目录内引用其他规则用相对路径 `../0X-*.md`，引用 ADR 用 `../adr/`。

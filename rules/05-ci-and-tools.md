# CI 约定与本地工具

本规则约定 CI 工作流的行为边界与本地工具的使用方式。**本地脚本只是 CI 的预演，结果以 CI 为准**（宪法 VI）。

## CI 工作流清单（`.github/workflows/`）

| 工作流 | 行为 | 触发 |
| ---- | ---- | ---- |
| `sync-headers.yml` | 把每个 SUMMARY 条目对应文件的 H1 改写为条目文字（含转义还原 `\* \[ \]`；跳过 frontmatter 文件；覆盖缩进子条目），自动提交 | push |
| `file-name-check.yml` | 校验 SUMMARY 条目文件存在，缺失自动开 issue | push |
| `markdown-lint2.yml` / `Markdown-lint2-pr.yml` | markdownlint 检查（配置 `.github/.markdownlint.json`） | push / PR |
| `check-images.yml` | 图片引用检查（悬空、可解析、本地化） | push |
| `links.yml` | 链接检查 | push |
| `md-padding.yml`、`AutoCorrect.yml` | 手动触发，自动补 CJK 空格并以 PR 提交，合并前人工核对 diff | 手动 |
| `Auto-Assign.yml`、`GC.yml`、`create-pdf.yml` | issue/PR 自动分配、垃圾回收、PDF 导出 | 各自约定 |

* 不要新增与上述约定冲突的本地规则；需要新检查时先改 `tools/` 并在此登记。
* 修改工作流须同步更新本表（变更管理见 [06-governance.md](06-governance.md)）。

## 本地工具（`tools/`，Python 3 仅标准库）

| 工具 | 用途 |
| ---- | ---- |
| `fetch.py` / `fetch_catalog.py` / `fetch_entry.py` | SEP 抓取（正文、目录、词条包；≥5 秒间隔，失败显式化） |
| `extract_text.py` / `parser.py` / `yuanwen.py` | 原始 HTML → 提取文本（`en/`、`yuanwen/`，不入库） |
| `baseline_audit.py` | 基线清单审计（哈希、版本钉一致性） |
| `task_ops.py` | 文档任务状态机（show / create / advance / clear / block） |
| `check_style.py` | 体例检查（引号、空格、HTML/AsciiDoc 残留；输出 JSON） |
| `check_summary.py` | SUMMARY.md 结构审计（条目解析、缺失文件、孤儿文件、命名、重复） |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测（坏链、覆盖缺口、标题不一致、重复收录） |
| `tests/` | 管线单元测试（unittest，金样本 fixtures） |

* 快速命令：

  ```sh
  python tools/check_style.py a/某词条.md      # 译文体例预检
  python tools/check_summary.py                # 目录结构审计
  python tools/check_mulu_s.py                 # 分类目录对应性
  python tools/task_ops.py show <slug>         # 查任务状态
  ```

* markdownlint（仓库根目录执行）：

  ```sh
  markdownlint-cli2 "**/*.md" "!en/**" "!yuanwen/**" "!script/**" "!node_modules/**" --config .github/.markdownlint.json
  ```

## 提交策略

* 高频小步提交：完成一个单元立即提交，不攒大批改动。
* 提交信息中文一行简述，如"重译 阿尔克迈翁：初译 + 一校"。
* 只提交与本次工作相关的文件；原始物（`en/`、`yuanwen/`、`script/`）不入库。
* 直接提交 main 分支；未经用户要求不 push、不做 force 操作。
* 本机 git 配置了 GPG 签名但无私钥时，用 `git commit --no-gpg-sign`。

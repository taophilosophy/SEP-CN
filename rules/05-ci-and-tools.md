# CI 约定与本地工具

本规则约定 CI 工作流的行为边界与本地工具的使用方式。**本地脚本只是 CI 的预演，结果以 CI 为准** （宪法 VI）。

## CI 工作流清单（`.github/workflows/`）

| 工作流 | 行为 | 触发 |
| ---- | ---- | ---- |
| `checks.yml` | 仓库一致性门禁：`check_summary.py` + `check_mulu_s.py` + `check_junk.py`（垃圾/产物入库）+ `check_terms.py`（术语一致性）+ 管线单元测试，硬错误即红灯 | push / 手动 |
| `sync-headers.yml` | 把每个 SUMMARY 条目对应文件的 H1 改写为条目文字（含转义还原 `\* \[ \]`；跳过 frontmatter 文件；覆盖缩进子条目），自动提交 | push |
| `file-name-check.yml` | 校验 SUMMARY 条目文件存在，缺失自动开 issue | push |
| `markdown-lint2.yml` / `Markdown-lint2-pr.yml` | markdownlint 检查（统一配置 `.markdownlint-cli2.jsonc`；手动触发，带 `--fix` 自动开格式化 PR） | 手动 |
| `check-images.yml` | 图片引用检查（悬空、可解析、本地化） | push |
| `links.yml` | 链接检查 | push |
| `md-padding.yml`、`AutoCorrect.yml` | 手动触发，自动补 CJK 空格并以 PR 提交，合并前人工核对 diff | 手动 |
| `Auto-Assign.yml`、`GC.yml`、`create-pdf.yml` | issue/PR 自动分配、垃圾回收、PDF 导出 | 各自约定 |

* 不要新增与上述约定冲突的本地规则；需要新检查时先改 `tools/` 并在此登记。
* lint 配置统一在根目录 `.markdownlint-cli2.jsonc`（规则、纳入范围、按文件豁免），`.github/.markdownlint.json` 保留为等价规则副本；`yuanwen/`（原文照录）与 `.zcode/`（本地工具）不参与 lint。
* 修改工作流须同步更新本表（变更管理见 [06-governance.md](06-governance.md)）。

## 本地工具（`tools/`，Python 3 仅标准库）

| 工具 | 用途 |
| ---- | ---- |
| `fetch.py` / `fetch_catalog.py` / `fetch_entry.py` | SEP 抓取（正文、目录、词条包；串行默认 ≥5 秒间隔，失败显式化；并发模式间隔按 2026-10-27 用户裁定，见 specs/001 Assumptions） |
| `fetch_all.py` | 全量抓取+原文镜像驱动器（并发节拍 A=16 路×5s / B=64 路×10s，实测均无限流；`--resume` 断点续跑；逐条留痕 `script/fetch-all-log.jsonl`） |
| `extract_text.py` / `parser.py` / `yuanwen.py` | 原始 HTML → 提取文本（`en/`、`yuanwen/`，不入库）；数学保真（2026-10-27 裁定）：跨块公式保护、公式内部原样保留，仅定界符统一 `$`/`$$`、空白折叠、表格内 `|` 用 `&#124;` 保义 |
| `baseline_audit.py` | 基线清单审计（哈希、版本钉一致性） |
| `task_ops.py` | 文档任务状态机（show / create / advance / clear / block） |
| `check_style.py` | 体例检查（引号、空格、HTML/AsciiDoc 残留；输出 JSON） |
| `check_summary.py` | SUMMARY.md 结构审计（条目解析、缺失文件、孤儿文件、命名、重复）；硬错误退出码 1 |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测（坏链、覆盖缺口、标题不一致、重复收录）；坏链/路径错/标题不一致为硬错误，退出码 1 |
| `check_junk.py` | 垃圾/产物入库门禁（ADR-0003）：原始物、缓存、构建产物、系统杂物命中即退出码 1 |
| `check_terms.py` | 术语一致性门禁（specs/002）：登记册 ↔ 词汇表译法互斥冲突、登记册废弃链/重复为硬错误（退出码 1）；词汇表滞后、缺裁定日期、`--docs` 定点核销仅告警 |
| `check_math.py` | 数学保真门禁（2026-10-27 裁定）：原始 HTML 每条公式内容必须原样出现在 yuanwen 产物；占位符残留、行内 `$` 失衡为硬错误（退出码 1） |
| `clean.py` | 本地垃圾清理器：默认试运行，`--go` 删除未跟踪缓存与临时文件（不触碰跟踪文件与 en/ 原始物） |
| `progress.py` | 生成 `PROGRESS.md` 进度汇总（自动生成，不手改） |
| `tests/` | 管线单元测试（unittest，金样本 fixtures） |

* 快速命令：

  ```sh
  python tools/check_style.py a/某词条.md      # 译文体例预检
  python tools/check_summary.py                # 目录结构审计（门禁）
  python tools/check_mulu_s.py                 # 分类目录对应性（门禁）
  python tools/baseline_audit.py [slug...]     # 基线完整性（需本地 en/ 原始物，不进 CI）
  python tools/progress.py                     # 重新生成 PROGRESS.md
  python tools/task_ops.py show <slug>         # 查任务状态
  ```

* markdownlint（配置驱动，仓库根目录执行）：

  ```sh
  markdownlint-cli2            # 按 .markdownlint-cli2.jsonc 的 globs 与规则检查
  markdownlint-cli2 --fix      # 自动修复可修复项
  ```

## 提交策略

* 高频小步提交：完成一个单元立即提交，不攒大批改动。
* 提交信息中文一行简述，如“重译 阿尔克迈翁：初译 + 一校”。
* 只提交与本次工作相关的文件；原始物（`en/`、`yuanwen/`、`script/`）不入库。
* 直接提交 main 分支；未经用户要求不 push、不做 force 操作。
* 本机 git 配置了 GPG 签名但无私钥时，用 `git commit --no-gpg-sign`。

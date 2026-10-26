# 工具目录

本目录是唯一入库的脚本目录，分两部分：**同步管线包** （specs/001 产物）与 **目录治理工具**。约定：Python 3 仅标准库；文件 UTF-8 无 BOM、LF；失败显式化、禁止静默跳过；退出码约定见各工具 docstring。使用与提交约定见 `rules/05-ci-and-tools.md`。

## 同步管线包（specs/001-sep-sync-pipeline）

| 模块 | 职责 |
| ---- | ---- |
| `common.py` | 公共件：路径解析、JSON 读写校验、时间戳 |
| `fetch.py` | 礼貌抓取层：相邻请求 ≥5 秒（宪法 V）、退避重试、逐请求留痕 |
| `fetch_catalog.py` | 全目录抓取（contents.html）与结构解析 |
| `fetch_entry.py` | 单词条包抓取：正文、脚注、补充材料、图片、pubinfo |
| `extract_text.py` / `parser.py` | 原始 HTML → 提取文本（含数学与上下标实体解码） |
| `yuanwen.py` | `yuanwen/` 英文原文对照文本管理 |
| `baseline_audit.py` | 基线审计：对 `baseline/entries.json` 登记物复算 SHA-256 并核对存在（依赖本地 `en/` 原始物，不进 CI） |
| `task_ops.py` | 文档任务状态机：show / create / advance / clear / block（契约见 `specs/001-sep-sync-pipeline/contracts/cli.md`） |
| `tests/` | unittest 单元测试 + 金样本 fixtures（CI 门禁项） |

## 目录治理工具（CI 门禁项）

| 工具 | 职责 |
| ---- | ---- |
| `check_style.py` | 体例检查（宪法 VI）：curly-quotes、bold-spacing、cjk-spacing、no-html、no-text-fence、no-asciiart；输出 JSON，退出码 0/1 |
| `check_summary.py` | SUMMARY 结构审计（条目解析、缺失文件、命名、重复）；硬错误退出码 1 |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测；坏链/路径错/标题不一致为硬错误（退出码 1），覆盖缺口与重复收录仅报告 |
| `progress.py` | 从 SUMMARY/baseline/tasks 生成 `PROGRESS.md` 进度汇总（自动生成，不手改） |

## 快速命令

```sh
python tools/check_style.py a/某词条.md      # 译文体例预检
python tools/check_summary.py                # 目录结构审计（门禁）
python tools/check_mulu_s.py                 # 分类目录对应性（门禁）
python tools/baseline_audit.py [slug...]     # 基线完整性（需本地 en/ 原始物）
python tools/progress.py                     # 重新生成 PROGRESS.md
python tools/task_ops.py show <slug>         # 查任务状态
python -m unittest discover -s tools/tests   # 管线单元测试
markdownlint-cli2                            # lint（配置见 .markdownlint-cli2.jsonc）
```

## 约定

* 一工具一职责；新工具入库须在本 README 登记（规则见 `rules/06-governance.md`）。
* 一次性脚本、临时日志放 `script/`（gitignore 草稿区），沉淀为正式工具时迁入本目录并补登记。
* 管线行为变更须同步 `rules/05-ci-and-tools.md` 与 `specs/001-sep-sync-pipeline/contracts/cli.md`。
* 门禁项随 `.github/workflows/checks.yml` 在 push 时自动运行；`baseline_audit.py` 因依赖本地原始物仅在本地执行。

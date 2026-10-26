# 工具目录

本目录是唯一入库的脚本目录，分两部分：**同步管线包**（specs/001 产物）与**目录治理工具**。约定：Python 3 仅标准库；文件 UTF-8 无 BOM、LF；失败显式化、禁止静默跳过；退出码约定见各工具 docstring。使用与提交约定见 `rules/05-ci-and-tools.md`。

## 同步管线包（specs/001-sep-sync-pipeline）

| 模块 | 职责 |
| ---- | ---- |
| `common.py` | 公共件：路径解析、JSON 读写校验、时间戳 |
| `fetch.py` | 礼貌抓取层：相邻请求 ≥5 秒（宪法 V）、退避重试、逐请求留痕 |
| `fetch_catalog.py` | 全目录抓取（contents.html）与结构解析 |
| `fetch_entry.py` | 单词条包抓取：正文、脚注、补充材料、图片、pubinfo |
| `extract_text.py` / `parser.py` | 原始 HTML → 提取文本（含数学与上下标实体解码） |
| `yuanwen.py` | `yuanwen/` 英文原文对照文本管理 |
| `baseline_audit.py` | 基线审计：对 `baseline/entries.json` 登记物复算 SHA-256 并核对存在 |
| `task_ops.py` | 文档任务状态机：show / create / advance / clear / block（契约见 `specs/001-sep-sync-pipeline/contracts/cli.md`） |
| `check_style.py` | 体例检查（宪法 VI）：curly-quotes、bold-spacing、cjk-spacing、no-html、no-text-fence、no-asciiart；输出 JSON，退出码 0/1 |
| `tests/` | unittest 单元测试 + 金样本 fixtures（`python -m unittest discover -s tools/tests`） |

## 目录治理工具

| 工具 | 职责 |
| ---- | ---- |
| `check_summary.py` | SUMMARY.md 结构审计：条目解析（含转义方括号）、缺失文件、孤儿文件、命名违规、重复路径 |
| `check_mulu_s.py` | 分类目录 ↔ SUMMARY 对应性检测：坏链、路径覆盖（别名/占位/假条目单独归类）、标题不一致、重复收录 |

用法：

```sh
python tools/check_summary.py            # 审计 SUMMARY 结构
python tools/check_mulu_s.py             # 检测 mu-lu-s.md 对应性
python tools/baseline_audit.py [slug...] # 审计基线完整性
```

## 约定

* 一工具一职责；新工具入库须在本 README 登记（规则见 `rules/06-governance.md`）。
* 一次性脚本、临时日志放 `script/`（gitignore 草稿区），沉淀为正式工具时迁入本目录并补登记。
* 管线行为变更须同步 `rules/05-ci-and-tools.md` 与 `specs/001-sep-sync-pipeline/contracts/cli.md`。

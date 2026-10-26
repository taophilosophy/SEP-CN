# Implementation Plan: 学术规范门禁（tools/check_academic.py）

**Branch**: `003-academic-norms` | **Created**: 2026-10-27

## 方案

单文件工具 `tools/check_academic.py`，纯标准库，风格对齐 `check_terms.py`：`io.TextIOWrapper` 包装 stdout、docstring 声明用法与退出码、`main(argv)` 可注入测试。

**数据源**（全部入库，CI 可用）：

| 数据 | 用途 |
| ---- | ---- |
| 词条文档本身（文件系统扫描） | 版本事实行、脚注配对、章节结构、译注 |
| `baseline/entries.json` | pubinfo 交叉核对（zh_doc 精确 → slug 词元回退） |
| `tasks/<字母>/<slug>.json` | version_pin 完整性、done 任务 evidence |

**不依赖**：`SUMMARY.md`（并行目录重建中间态，90 条缺失路径）；`yuanwen/`、`en/`（gitignore，CI 无原始物）。

## 检查矩阵

| 检查 | 级别 | 判定 |
| ---- | ---- | ---- |
| pubinfo-missing / pubinfo-mismatch | 硬 | 非存根词条 ↔ baseline 日期元组比对 |
| orphan-ref / orphan-def | 硬 | `[^key]` 引用与定义集合对称差（跳过代码块） |
| task-pin-missing | 硬 | version_pin 三字段非空 |
| task-evidence-missing | 硬 | done 任务步数 ≥6 且步步有 evidence |
| biblio-missing / scholar-tools-missing / biblio-note-missing / trans-note / baseline-lookup-miss | 告警 | `--strict` 升硬 |

## 工件

* `tools/check_academic.py`
* `tools/tests/test_check_academic.py` + `tools/tests/fixtures/check_academic/`（注入 `--root/--baseline/--tasks-dir` 指向 fixtures）

## 风险与对策

* baseline `zh_doc` 滞后/为 null（目录重建中间态）→ slug 词元回退 + 歧义告警，宁可跳过不误报硬错误。
* 日期格式变体 → 英文月名前 3 字符 casefold 解析；解析失败降为告警。
* 误伤非词条 md → 目录/文件排除清单 + H1 门闩 + 存根阈值三重过滤。

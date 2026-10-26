# 方法论文档索引（fang-fa-lun/）

本目录存放 SEP-CN 翻译工程的方法论与标准文档（均不入 SUMMARY，不影响发布目录）。入口标准与文档清单如下。

## 文档

| 文件 | 内容 | 版本/状态 |
| ---- | ---- | ---- |
| [gong-cheng-fang-fa.md](gong-cheng-fang-fa.md) | **翻译工程标准 v1.0**：双表架构、术语四回路、三审三校质量门、任务文件 schema、缺陷分类、别名/重名处置、提交纪律、修订规则 | v1.0（2026-10-27） |
| [zheng-fan-wu-yong-shou-ce.md](zheng-fan-wu-yong-shou-ce.md) | 日常词哲学术义与正反误用手册：一校/复审必查清单 | 持续回填 |
| [ci-hui-biao-fu-he-bao-gao.md](ci-hui-biao-fu-he-bao-gao.md) | 词汇表复核报告：三轮复核记录（46 处修正、同步发布、全局遍历）、联网核查来源、裁定沿革 | 随复核追加 |

## 配套任务文件（tasks/）

| 文件 | 内容 |
| ---- | ---- |
| tasks/ci-hui-biao.json | 词汇表维护任务：已完成步骤与持续待办（提交信息挖掘、双向同步） |
| tasks/term-candidates.json | 原文术语候选清单（55 条，建议译法待裁定） |
| tasks/<slug>.json | 各词条翻译任务（schema 见标准 S4） |

## 本地工具（script/，不入库）

| 工具 | 用途 |
| ---- | ---- |
| check_all.py | **一键质量门**：glossary_lint + mu-lu-s 检测 + tasks JSON 合法性 + markdownlint（豁免清单见标准 S7） |
| glossary_lint.py | 词汇表有效性检查 v2（极端情况兼容 + 登记簿同步检查） |
| extract_terms.py | 原文术语五路提取（yuanwen/ + en/ 语料） |
| fix_table_style.py | 表格紧凑化（MD060），批量修复前先单文件验证 diff |
| check_mulu_s.py | mu-lu-s.md 对应性检测（只检测不改动） |

## 相关文档

* `specs/001-sep-sync-pipeline/`：抓取/更新/比较/翻译管线规格（FR-001 起），他会话维护，本目录与其引用对齐。
* `yi-zhe-shuo-ming.md`：术语登记簿（单一事实源）。
* `qian-yan/ci-hui-biao.md`：词汇表发布表。

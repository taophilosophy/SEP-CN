# Implementation Plan: SEP 同步管线（抓取 · 更新 · 比较 · 翻译）

**Branch**: `001-sep-sync-pipeline` | **Date**: 2026-10-26 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-sep-sync-pipeline/spec.md`

## Summary

为 SEP-CN 仓库建立"抓取 → 更新检测 → 版本比较 → 每文档翻译（三审三校）"的完整可执行管线：以在线词条页为唯一抓取源形成不可变基线快照；以 RSS/new.html + archinfo + contents.html 三源检测上游变化；以段落级 diff 把变化映射到中文文档；每个文档走"一校→二校→三校→初审→复审→终审"六道状态机完成全量重译（既有译文不作底稿）。全部环节以零信任原则落地：哈希登记、双源核对、凭证留痕。

## Technical Context

**Language/Version**: Python 3.15（本机已有，仅标准库；见 research D1/D2 的零依赖决策）

**Primary Dependencies**: 无第三方运行时依赖（stdlib：urllib.request、html.parser、hashlib、json、difflib、unittest）；markdownlint-cli2（已装，npm）用于体例检查

**Storage**: 本地文件系统 `en/`（原始 HTML + 提取文本，gitignore）；版本库内 `baseline/`（元数据清单 JSON，入库）与 `tasks/`（文档任务状态 JSON，入库）

**Testing**: unittest（stdlib）+ 9 个结构迥异样本词条的金样本 fixtures；验收以 spec 成功标准 SC-001…005 为准

**Target Platform**: Windows 10+ 本地执行；产物须兼容 GitHub Actions Ubuntu CI（UTF-8 无 BOM、LF、大小写逐字符一致）

**Project Type**: 内容仓库 + 管线脚本集（无服务、无前端）

**Performance Goals**: 全库基线抓取一轮 ≤4 小时（约 1800 词条 × 5 秒间隔）；每日增量更新检测 ≤5 分钟；单词条比较 ≤2 秒

**Constraints**: 相邻请求 ≥5 秒（宪法 V）；缺省件显式登记；Windows 大小写不敏感陷阱（图片引用名必须与磁盘逐字符一致，否则 Linux CI 404）；正文清空必须先有该词条可信基线（宪法附加约束）

**Scale/Scope**: 约 1800 个词条（SUMMARY.md 全目录），全量重译战役 + 常态更新运维

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| 宪法门 | 检查结果 |
| ------ | -------- |
| I. 零信任 | 通过——基线快照先于一切翻译动作；既有译文不作底稿（FR-013）；pubinfo+archinfo 双源核对（FR-003） |
| II. 可追溯 | 通过——SHA-256 + 抓取时间 + 源 URL 登记（FR-002/017）；原始物存 `en/` 不可变 |
| III. 单一事实源 | 通过——结构以 SUMMARY.md 为准（比较映射源）；术语以 yi-zhe-shuo-ming.md 为准；元数据清单 `baseline/` 为版本事实源 |
| IV. 流程先行 | 通过——本 feature 即流程文档；演示→纠偏循环为 User Story 5 |
| V. 礼貌抓取 | 通过——≥5 秒间隔、显式失败、缺省件登记（FR-004/005） |
| VI. 体例即契约 | 通过——三校步骤绑定检查脚本（FR-015/016）；`tools/check_style.py` 弥补本仓库无引号/空格检查脚本的空缺（research D9） |

Phase 1 设计后复查：**通过**（无违宪项，Complexity Tracking 留空）。

**环境补充约束（2026-10-26 演示轮 1 实录）**：本仓库存在**并行工作会话**（用户安排的另一会话），实测行为包括 pull/reset/commit 与批量清理词条正文；本 feature 的未跟踪产物曾因此被清除（specs/ 下 6 件产物于 23:52–00:08 之间丢失，最初误诊为 SMB 假成功）。对策（宪法 I 落地）：

1. 每份产物写盘后**立即** `git add` + 高频 commit，以对象库为唯一可信底；
2. 任何批量动作前 `git status` 留痕，动作后 `git ls-files` 复核；
3. 与并行会话的裁定冲突（如其把 `/tools`、`/.specify`、`/.zcode` 加入 .gitignore）不当场对抗，登记进报告交用户裁决；
4. 单文件"写入成功"不可信：跨进程（bash + PowerShell）双视角复核大小与哈希。

## Project Structure

### Documentation (this feature)

```text
specs/001-sep-sync-pipeline/
├── plan.md              # 本文件
├── research.md          # Phase 0 产出：技术决策与理由
├── data-model.md        # Phase 1 产出：实体与状态机
├── quickstart.md        # Phase 1 产出：端到端验证指南
├── contracts/
│   └── cli.md           # 管线工具的 CLI 接口契约
├── checklist.md         # 验收检查点（产出）
└── tasks.md             # 任务分解（产出）
```

### Source Code (repository root)

```text
tools/                    # 管线脚本（本计划裁定：入版本库；⚠️ 并行会话已把 /tools 加入 .gitignore，入库与否待用户裁定）
├── fetch_entry.py        # 抓取单个词条包（正文+脚注+补充+图片+元数据）
├── fetch_catalog.py      # 抓取 contents.html → 目录结构 JSON
├── detect_updates.py     # RSS/new.html + archinfo 三源更新检测（未实现，T020-21）
├── compare_versions.py   # 两快照段落级 diff + 中文文档映射（未实现，T024-25）
├── extract_text.py       # 原始 HTML → 提取文本（可复算复核）
├── task_ops.py           # 文档任务状态机操作（建/查/推进/签字）
├── check_style.py        # 体例检查（引号/加粗空格/CJK 空格/HTML 残留）
├── baseline_audit.py     # 基线完整性审计（哈希复算、缺省件核对）
├── fetch.py              # 礼貌抓取层（≥5s 间隔、退避重试、http-log.jsonl）
├── common.py             # UTF-8 无 BOM 读写、写后读回自校验
├── parser.py             # 标记契约解析器（spec"网站结构事实基础"）
└── tests/                # unittest 金样本测试（26 例，fixtures 取自抽样）

en/                       # 原始抓取物（gitignore，本地）
├── _catalog/             # contents.html、new.html、sep.xml 的时点快照
├── <slug>/               # 每词条一目录：index.html、notes.html、<补充>.html、image*.jpg
└── <slug>.txt            # 提取文本（与 index.html 哈希绑定）

baseline/                 # 元数据清单（入版本库）
├── entries.json          # slug 主键：标题、作者、pubinfo、存档版、各文件哈希、抓取时间
├── catalog.json          # contents.html 最新解析（目录事实源）
└── changes/              # 比较产出的变更清单

tasks/                    # 文档任务状态机（入版本库）
└── <首字母>/<slug>.json   # 六道状态机记录 + 版本钉 + 凭证
```

**Structure Decision**: 管线代码 `tools/`（本计划裁定入版本库保证可复现；并行会话已将 `/tools` 加入 .gitignore，两裁定冲突待用户裁决——冲突期间工具在本地可用，不阻塞流程）；原始物 `en/` 本地留存；审计索引与任务状态入版本库（`baseline/`、`tasks/`），与用户裁定的"元数据入库+原文本地"一致。

## Complexity Tracking

> Constitution Check 无违宪项，表格留空。

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| （无） | | |

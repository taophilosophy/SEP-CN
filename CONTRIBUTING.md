# 贡献指南

本项目是《斯坦福哲学百科全书》（Stanford Encyclopedia of Philosophy）的简体中文翻译，基于 GitBook 发布、辅以本地 VitePress 双语阅读站。贡献前请先读：

* [AGENTS.md](AGENTS.md) —— AI 代理入口与规范层级
* [规则目录](rules/README.md) —— 仓库结构、编写体例、术语、翻译流程、CI、治理
* [任务协议](tasks/README.md) —— 文档任务与三审三校状态机
* [项目宪法](.specify/memory/constitution.md) —— 六项核心原则

## 如何参与

1. **翻译 / 校对词条**：在 [PROGRESS.md](PROGRESS.md) 与 `tasks/` 领取任务 → `python tools/task_ops.py create <slug> --kind retranslate`（前置：词条已建英文基线）→ 按六道状态机推进（一校→二校→三校→初审→复审→终审，禁止跳步）→ 每步留 `evidence` 凭证 → 完成即提交（中文一行信息）。
2. **新词条 / 新页面**：文件与路径由 ykla 统一创建；缺条目请开 issue。
3. **术语**：先登记 `yi-zhe-shuo-ming.md` 后使用；发布词汇表 `qian-yan/ci-hui-biao.md` 向登记册看齐（见 `rules/03-terminology.md`）。
4. **改结构 / 标题**：只改 `SUMMARY.md`，各文件 H1 由 CI 同步；分类目录 `mu-lu-s.md` 改动后跑 `python tools/check_mulu_s.py`。
5. **提交前**：跑门禁 `python tools/check_summary.py`、`python tools/check_mulu_s.py`、`python tools/check_style.py <改动文件>`，以及 `markdownlint-cli2`。

## 历史说明

* 早期条目由机器翻译（GPT-3.5，工具链与参数见 git 历史）生成，质量不达标。项目已裁定 **全量重译**：既有译文不作底稿或修改依据，一律以新抓取的英文源为唯一底稿（宪法 I、FR-013）。
* 当前进度见 [PROGRESS.md](PROGRESS.md)（由 `tools/progress.py` 自动生成）。

## 许可

工程产物使用 BSD-2-Clause；SEP 词条原文为 CC BY-NC-SA，译文项目沿用仓库现行许可与发布方式，“reprinted with permission” 图片在译文中标注来源。

# journal 目录

本目录是**条目事件日志**——进度模型三存储之一的事实源（ADR-0068）。`state` 字段不再作为事实，而是由本目录的事件流派生的视图。

## 内容

* 每个词条一个文件：`journal/<letter>/<slug>.ndjson`，每行一个事件，按 `seq` 递增，只追加（P5）。
* 事件六类（`jian-yi-shu/journal-schema.json` 定义）：`lock`（源钉）、`pass`（节点判据通过）、`fail`（节点判据失败）、`rework`（开返工分支）、`merge`（分支合回）、`import`（迁移期合成快照，`synthetic:true`）。
* 本目录由 `tools/journal_migrate.py`（一次性迁移，ADR-0068 W1）生成；后续推进由 `tools/journal_ops.py` 写入（W3 起）。

## 怎么读

* 派生视图：`python tools/journal_view.py`（只读，不写文件）。
* 节点集与判据归属：`rules/pipeline.json`（唯一事实源，`tools/check_stages.py` 校验）。
* 事件模型：`jian-yi-shu/journal-schema.json`。

## 迁移口径（2026-11-18）

* 源：`tasks/**/*.json` 的 `steps` 与 `version_pin`；只读换算，不改任何任务文件。
* `done`／`clear` 不落 journal（`done` 是派生量，饱和由 `pass` 集合推导）。
* 无阶段记录的条目合成 `import{synthetic:true, basis:state}`，不推断中间节点。
* 只迁 `retranslate`／`update` 词条任务；`glossary-maintenance`／`daily-check` 例行任务不迁。

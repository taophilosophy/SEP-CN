# Data Model: SEP 同步管线

**Feature**: specs/001-sep-sync-pipeline | **Date**: 2026-10-26

## 实体

### Entry（词条）

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| slug | string（主键） | SEP 唯一标识，取自 contents.html 链接路径，如 `anaxagoras` |
| title_en | string | 英文标题（contents.html 链接文字） |
| title_zh | string | 中文标题（SUMMARY.md 对应条目文字） |
| authors | string[] | 作者名（contents.html 括注 / archinfo） |
| alias_of | string \| null | 别名词条（— see 型）指向的目标 slug；正文词条为 null |
| first_published | date | 首版日期（pubinfo） |
| substantive_revision | date | 最近实质修订日期（pubinfo） |
| archive_edition | string | 最新存档版名（archinfo），如 `fall2026` |
| zh_doc | string \| null | 中文文档路径（按 SUMMARY.md 映射），别名词条为 null |
| version_history | object[] | 各存档版序列：`{edition, change_type: substantive\|minor, new_authors[]}` |

约束：slug 全库唯一；`alias_of` 非空时 `zh_doc` 必须为空且 `version_history` 允许为空。

### Snapshot（快照，抓取物）

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| slug | string（外键→Entry） | |
| fetched_at | ISO 8601 时间戳 | 抓取时刻（UTC） |
| source_url | string | 正文页 URL（一律在线版） |
| files | object[] | `[{path, sha256, bytes, kind: main\|notes\|supplement\|image}]` |
| pubinfo | object | `{first_published, substantive_revision}`（从正文提取，与 Entry 核对） |
| missing | object[] | 显式缺省件：`[{expected, http_status}]`，如 notes.html 404 |
| immutable | bool 恒真 | 原始物一旦落盘不修改；重抓存新副本不覆盖 |

存储：`en/<slug>/`（原始 HTML 与图片）+ `en/<slug>.txt`（提取文本）；登记于 `baseline/entries.json`（保留历史各轮）。

### Change（变更记录）

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| slug | string（外键） | |
| old_ref / new_ref | 快照引用 | 两轮快照标识（fetched_at 对） |
| items | object[] | `[{type: add\|remove\|replace\|move, section: 英文节号, excerpt_en: 原文摘录, zh_doc: 中文文档路径 \| "待建任务", anchor: 位置}]` |

存储：`baseline/changes/<slug>-<日期>.json`（入版本库——它是翻译更新任务的直接输入）。

### DocTask（文档任务）

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| slug | string（主键） | |
| zh_doc | string | 对应中文 md 路径 |
| kind | enum | `retranslate`（清空重译）/ `update`（上游更新） |
| version_pin | object | `{pubinfo_date, archive_edition, sha256}` 翻译依据的英文源版本钉 |
| state | enum | 状态机当前节点（见下） |
| steps | object[] | 每步 `{step, status, actor, at, evidence}`，evidence 为检查输出/diff/签字引用 |
| blockers | string[] | 阻塞原因（如"基线缺失"） |

存储：`tasks/<首字母>/<slug>.json`（入版本库）。

#### DocTask 状态机（retranslate，宪法 VI + FR-012）

```text
pending → cleared → drafted → s1_checked → s2_checked → s3_checked
        → r1_reviewed → r2_reviewed → r3_reviewed → done
任意节点 → blocked（blockers 记录原因）→ 可回到原节点
```

* `cleared`：正文已清空（保留 H1），前置 gate=基线哈希复算通过
* `drafted`：以英文源为唯一底稿初译完成；新术语先登记再使用
* `s1_checked`：一校（准确性）——对照英文源逐句，变更段任务只过变更段落
* `s2_checked`：二校（语言）——欧化句、口吻、流畅
* `s3_checked`：三校（体例）——check_style.py + markdownlint 通过
* `r1_reviewed`：初审——对照原文自审签字
* `r2_reviewed`：复审——逐句回核原文与逻辑
* `r3_reviewed`：终审——CI 全绿 + 版本钉核对 + 抽查
* `done`：终审通过且已提交

#### DocTask 状态机（update）

```text
pending → s1_checked(仅变更段) → s2_checked(变更段所在节) → s3_checked(全文档)
        → r1 → r2 → r3(全文档) → done
```

### TermRegistry（术语登记）

沿用 `yi-zhe-shuo-ming.md` 既有机制：新术语先登记（英文原名、中文译法、首现词条、裁定日期）再使用；三校步骤校验正文用词与登记一致。

## 关系

* Entry 1—N Snapshot（每轮检测产生新快照）
* Snapshot 1—N Change（两两比较产生；实际只对相邻两轮比）
* Change 1—N DocTask(update)（每条变更映射一个文档的一份工作量）
* Entry 1—1 DocTask(retranslate)（全量重译战役期）
* Entry N—N TermRegistry（词条内新术语登记）

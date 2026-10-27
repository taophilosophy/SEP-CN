# 数据模型：核验实体与状态（specs/006）

**日期**：2026-10-27 | **输入**：spec.md Key Entities + research.md 缺口裁决

## 一、实体

### 1. 批次核验报告（BatchVerificationReport）

| 字段 | 类型 | 说明 |
|---|---|---|
| batch | string | 批次（1 或 a–z） |
| ran_at | timestamp | 核验时间 |
| findings | DiffItem[] | 差异项列表（见 2） |
| coverage | object | 覆盖计数（条目数/已核/缺失/多余/别名错链/分类缺口/节序列不一致） |
| verdict | enum | clean / findings（有差异项）/ needs-review（差异项待裁定） |

### 2. 差异项（DiffItem）

| 字段 | 类型 | 说明 |
|---|---|---|
| kind | enum | missing / extra / alias-broken / mu-lu-s-gap / section-mismatch / asset-missing / conversion |
| slug | string | 涉及条目 |
| detail | string | 具体差异（路径/锚点/计数） |
| disposition | enum | **silent → ruled → fixed → closed**（状态机，见二.2） |
| ruling | string | 显式裁定（豁免/增量登记/修正提交/任务号） |

### 3. 变更记录（ChangeRecord，FR-005 闭环）

| 字段 | 类型 | 说明 |
|---|---|---|
| detected_at | timestamp | 检测时间（fetch_catalog/compare 触发） |
| slug | string | 词条 |
| section_ref | string | 节级定位（锚点/节号） |
| affected_doc | string | 受影响中文文档路径 |
| task | string | update 任务号 |
| resolved_by / resolved_how | string | 处理人 / 处理方式 |
| verification | string | 验证证据（重算/复核引用） |
| status | enum | open → claimed → closed |

### 4. 复核记录（ReviewRecord，FR-006 结构化载体）

| 字段 | 类型 | 说明 |
|---|---|---|
| subject | string | 复核对象（词条/节/译文段） |
| doubt | string | 存疑提问（史实/引文/年代/译法） |
| ruling | string | 裁定（回原文核对结果/译注说明） |
| evidence_anchor | string | 证据锚点（en/ 路径、notes 主键、SUMMARY 行号） |
| reviewer | string | 复核人 |
| recomputed | bool | 独立重算结果（0 信任复核） |

### 5. 批次（Batch，复用 specs/005 账本）

批次账本（ledger.json）只存意图与认领；本 feature 的核验报告按批次归属，与账本 `slugs` 命令同源推导，不重复存储。

## 二、状态机

### 1. 核验流程

```
领取批次 → 运行三类核验（目录/抓取/转换）→ 批次报告（findings）
  → 逐差异项裁定（ruled）→ 修正或登记（fixed）→ 复跑收敛（closed）
```

### 2. 差异项状态机（禁止静默）

```
silent（核验发现）→ ruled（显式裁定：豁免/增量登记/待处理任务）
  → fixed（修正提交或登记完成）→ closed（复跑确认 0 差异）
```

任何 DiffItem 不得停留在 silent 状态收口——这正是 spec SC-001"静默差异 0"的数据表达。

### 3. 变更记录状态机

```
open（检测产出）→ claimed（update 任务认领）→ closed（处理完成 + 验证证据）
```

## 三、不变式

1. 核验器只产出报告，不直接修改目录/译文——修正走既有显式裁定流程（summary_sync/rebuild/check 门禁）。
2. 报告按批次归属，批次词条集合由 SUMMARY 实时推导（不重复存储，零漂移）。
3. 差异项从产生到收口全程留痕（含"豁免"裁定本身也是留痕）。

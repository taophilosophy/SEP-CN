# 契约：批次核验流程与产出物（specs/006）

**日期**：2026-10-27 | **输入**：plan.md Phase 1 设计要点 + research.md 缺口裁决

## 契约 1：批次核验运行（三阶段命令行为）

```text
运行方: 任意会话（复用 specs/005 批次账本：campaign.py status/next/claim/slugs）
输入:   批次（1 或 a–z）
阶段:
  ① 目录核验   运行既有目录门禁与上游对照（SUMMARY↔官方快照↔mu-lu-s），
              产出该批差异清单（缺失/多余/别名错链/mu-lu-s 分类缺口）
  ② 抓取核验   运行引用闭包审计，产出该批覆盖率计数（审计/完整/缺省件/可补抓）
  ③ 转换核验   对批次内逐词条产出中英节序列对照清单（数量/顺序/标题）
              + 公式/表格/脚注计数对照
输出:   specs/006-verification-revision-mechanisms/reports/<batch>.json
        {batch, ran_at, findings:[DiffItem], coverage:{...}, verdict}
约束:   核验器只报告不修改；补抓/修正走既有流程（fetch_audit/summary_sync/rebuild）
退出码: 0 clean；1 findings；2 错误
```

## 契约 2：差异项处置（DiffItem 状态机）

```text
silent（核验发现）→ ruled（显式裁定，写明：豁免/增量登记/待处理任务号）
  → fixed（修正提交或登记完成）→ closed（复跑确认 0 差异）
收口判据: 批次报告内 silent 项 = 0（SC-001）
裁定落位: 目录修正走既有门禁流程；增量走 summary_sync apply-add；
        别名/递归/分类缺口按 ADR-0007/0009 语义处置
```

## 契约 3：变更记录闭环（FR-005）

```text
检测: 存档季（3/6/9/12 月 21 日）fetch_catalog + compare 全量
产出: 变更记录（open）——含节级定位与受影响中文文档
处置: update 任务认领（claimed）→ 仅变更段重校 → 验证证据（closed）
零噪音: 无上游变化时报告"无变化"，不产生空任务/空变更记录
```

## 契约 4：复核记录（FR-006 结构化载体）

```text
落位: 任务 JSON 的 reviews 数组 或 批次复核报告
必填: subject / doubt（存疑提问）/ ruling（裁定）/
      evidence_anchor（en/ 路径、notes 主键、SUMMARY 行号）/ reviewer
0 信任: 批次抽查含独立重算（换命令/换环境重算 diff 一致）
违规判定: 改写无英文源锚点且无译注说明 → 违规，回炉
```

## 契约 5：并行执行

```text
批次认领: 复用 campaign.py（claim 互斥、断点续上、账本经版本库同步）
无耦合: 会话只触碰本批报告与裁定；核验器无共享进行中状态
收敛: 全库核验轮次迭代至差异项 0 新增（引用闭包同款不动点语义）
```

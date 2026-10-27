# 会话开工卡：多会话分批执行交接（specs/005）

**版本**：v1.0 | **日期**：2026-10-27 | **用途**：新会话拿此卡即可独立开工，无需其他上下文
**前置阅读**：`specs/005-translation-campaign/parallel-design.md`（批次模型与会话协议）

## 1. 开工三件事（每个会话）

```
python tools/campaign.py status          # 全局统计表（断点即在此）
python tools/campaign.py next            # 取未认领批次建议
python tools/campaign.py claim <批次> --session <你的会话名>
```

## 2. 分工（按此优先级领取）

| 阶段 | 内容 | 认领方式 | 前置 |
|---|---|---|---|
| **A. 工作流验证**（首个会话，P0） | Wave 0 五词条**翻译**全流程实跑：abduction（短）、logic-classical（1545 公式）、action-perception（含图）、bayes-theorem（脚注+表格）、set-theory（补充材料）——specs/005 Wave 0 | 手动认领 `a/c/l/b/s` 批次中对应词条 | 无——**批量翻译须等本阶段通过** |
| **B. 批次预处理**（可 N 会话并行） | 各批 intake → fetch → convert 三阶段（`campaign.py next` 领批） | `campaign.py claim` | 无——可与阶段 A 并行 |
| **C. 批次翻译**（可 N 会话并行） | 各批 translate 阶段：`campaign.py slugs <批>` 逐词条 `task_ops.py create --kind retranslate` + 状态机 | `campaign.py claim` | **阶段 A 验收通过后** |

当前批次状态（2026-10-27）：`1`/`z`/`j` 已至 convert；其余 24 批 pending；`next` 依次建议 `a`（154 词条，14 缺基线 3 缺镜像）→ `b` → `c` …

## 3. 各阶段的标准作业（每批次）

| phase | 命令 | 完成判据 |
|---|---|---|
| intake | `python tools/summary_sync.py report` 查看 ADD 队列；逐条 `apply-add <slug> --title-zh "译名"`（译名先登记 yi-zhe-shuo-ming.md，沿用集群命名惯例） | `report` 队列清空 |
| fetch | `python tools/fetch_entry.py $(python tools/campaign.py slugs <批>)`；`fetch_audit.py $(...)` 补缺件 | `campaign.py status` 该批 基线=总 |
| convert | `python tools/yuanwen.py $(python tools/campaign.py slugs <批>)` | 该批 镜像=总 |
| translate | 逐词条 `task_ops.py create <slug> --kind retranslate` → clear → draft → s1→s2→s3→r1→r2→r3 → done（s3/r3 学术挂钩自动拦截）；**骨架与元素映射一律照 [fan-yi-mu-ban.md](fan-yi-mu-ban.md)**；s1 含文献还原：脚注定义条中的中国文献按 [ADR-0011](../../rules/adr/0011-引文原文语言与中文文献翻译.md) 译为中文（定位 `tools/biblio_audit.py <slug>`，译名对 yi-zhe-shuo-ming.md「文献译名」表，三来源幻觉防线） | 该批 done=总 |
| 收口 | `campaign.py advance <批> done`；`check_all` 全绿；G4 记录入 specs/001 execution-log | 批次 phase=done |

每阶段完成后：`campaign.py advance <批次> <下一阶段> --note "计数依据"`。**账本阶段只在事实满足时推进**（note 写明计数）。

> **工作量提示（ADR-0011）**：含中国文献的词条（chinese-* 簇约 30 条 + 全库罗马化线索约 170–280 条，探针见 `tools/biblio_audit.py --all` 的 flagged）文献还原额外 +10–15% 工时；认领 chinese-* 簇的会话按此排程。

## 4. 纪律（违反即返工）

1. **只动你认领的批次**；协调只经账本（提交），不共享进行中文件。
2. **推送先 `git pull --rebase`**；账本冲突 rebase 后重放 advance（幂等）。
3. **零信任**：既有译文不作底稿；术语先登记 yi-zhe-shuo-ming.md 后使用。
4. **抓取礼貌** ≥5 秒/请求；429 即收敛并记录。
5. **不备份文件**（用户裁定，git 即管理）；`script/` 为个人草稿区。
6. **中断随时可停**：重跑 `status` 即断点，工具全部幂等。
7. 演练/试跑产生的假任务与假变更文件必须清理，状态复位 pending 并留痕。

## 5. 验收与升级

* 批次收口 → G4 记录（doctrine 最小字段）入 `specs/001-sep-sync-pipeline/execution-log.md`。
* 阶段 A 验收 → checklist 见 `specs/005-translation-campaign/checklist.md`。
* 规划书修订（暴露问题回流）→ specs/005 spec.md 版本号 v1.x + 提交说明。
* 技术债务消化 → specs/004 登记表逐项标记。

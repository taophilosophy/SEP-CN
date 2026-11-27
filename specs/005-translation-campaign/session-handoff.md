# 会话开工卡：多会话分批执行交接（specs/005）

**版本**：v2.0 | **日期**：2026-11-26（v1.0 2026-10-27，旧断点已随全库置空作废，留档见 §7）
**用途**：新会话拿此卡即可独立开工，无需其他上下文
**前置阅读**：`specs/005-translation-campaign/parallel-design.md`（批次模型与会话协议）、`rules/08-intent-first.md`、`rules/04-translation-workflow.md`

## 0. 现状（2026-11-26 复账；数字现查，不在本卡复制）

| 事实 | 口径 |
| --- | --- |
| 正式词条 1873 件**全部** `state=cleared`、正文仅 H1 | ADR-0081/0082 全库置空，重译起点 |
| 任务账 1873＝SUMMARY 链接 1873＝journal 1873，`version_pin` 100% 齐 | `zh/PROGRESS.md`、`task_ops.py show` |
| journal：1800 件无事件、73 件仅 `fetch_entry` 的 `lock` 记录 | 均属未开工 |
| 批次账 27 批已清空认领（2026-11-26 复账），phase 仅作历史阶段记录 | `campaign.py status` |
| 现行 `campaign.py next` 应指向 `a` 批 | 阶段机只进不退，`done` 批按 phase 跳过 |
| 术语表 8948 行、人名表 4974 行，由独立线推进（§4），不阻塞翻译 | `check_terms.py` |

> **执行闸（2026-11-26 并入 064）**：`specs/064-flow-spec-audit/results/schedule.md` 的 rev17 排程翻译站段全部未启动、**G0 未过，禁入任何翻译站段**（同文件 :40）。S16 临时布局迁移（T202–T207）已于 2026-11-27 完成，只动目录与工具链，不构成翻译站段放行。G0 通过或用户明确放行前，本卡只执行 §2“预处理”与 §4 各线，§3 的 translate 与收口不开放。

**不要**凭本卡判断进度：一律跑 `python tools/campaign.py status` 与看 `zh/PROGRESS.md`（journal 口径，由 `tools/progress.py` 生成）。

## 1. 开工四件事（每个会话）

```
python tools/sync_guard.py pull            # 落后不干活（ADR-0028）
python tools/campaign.py status            # 全局统计表（断点即在此）
python tools/campaign.py next              # 取未认领批次建议
python tools/campaign.py claim <批次> --session <你的会话名>
```

开工前按 `rules/08` 写方向声明：本批目标、非目标与完成判据（以 §3 为准）；批次或词条范围含糊时先问不猜。动笔翻译前先钉基准：该批 `en/` 镜像 commit 与转换器版本写入首批任务 evidence（`rules/08` §9）；053 线会全量重转 md，pull 后须同时钉 053 转换器版本＋镜像 commit，待 053 收敛再定基线。

## 2. 分工（按此优先级领取）

| 阶段 | 内容 | 认领方式 | 前置 |
| --- | --- | --- | --- |
| **预处理**（可 N 会话并行） | 各批 intake → fetch → convert 三阶段 | `campaign.py claim` | 无 |
| **翻译**（可 N 会话并行） | 批内词条逐条 `task_ops.py create <slug> --kind retranslate` → 状态机全流程 | `campaign.py claim` | 该件基线已建、镜像已转换 |

原 v1.0 的 Wave 0 五词条验证已于 2026-11 完成，不再要求单独认领；旧“A/C/L/B/S 批次对应词条”约定随之失效。064 排程另有 11 件逐件表（habermas、logic-preference、environmental-aesthetics、imprecise-probabilities、action、axiom-choice、newton-principia、logic-dynamic、japanese-aesthetics、kokugaku-school、digital-art），G0 通过后按该表逐件串行，字母批不得抢先。

## 3. 各阶段的标准作业（每批次）

| phase | 命令 | 完成判据 |
| --- | --- | --- |
| intake | `python tools/summary_sync.py report` 查看 ADD 队列；逐条 `apply-add <slug> --title-zh "译名"`（译名先登记 `zh/shu-yu-biao.md`，沿用集群命名惯例） | `report` 队列清空 |
| fetch | `python tools/fetch_entry.py $(python tools/campaign.py slugs <批>)`；`fetch_audit.py $(...)` 补缺件 | `campaign.py status` 该批 基线=总 |
| convert | `python tools/yuanwen.py $(python tools/campaign.py slugs <批>)` | 该批 镜像=总；`check_yuanwen_fidelity --gate` 绿 |
| translate | 逐词条 `task_ops.py create <slug> --kind retranslate` → 按 `rules/04` 状态机推进（节点名以 `task_ops.py show` 与 ADR-0080 为准：`tr-*`／`rv-*`／`sg-*`／`ex-*`）；**开工先钉基准**；骨架与元素映射照 [fan-yi-mu-ban.md](fan-yi-mu-ban.md)；s1 含文献还原（ADR-0011，定位 `tools/biblio_audit.py <slug>`，译名对 `zh/shu-yu-biao.md` 文献译名表，三来源幻觉防线） | 该件走完核心段与强制集（口径见 `zh/PROGRESS.md`） |
| 收口 | `campaign.py advance <批> done`；`check_all` 全绿；G4 记录入 `specs/001-sep-sync-pipeline/execution-log.md`（此 G4 指 doctrine 最小字段的收口记录，与 064 的 G4 规范闸同号异指） | 批次 phase=done |

每阶段完成后：`campaign.py advance <批次> <下一阶段> --note "计数依据"`。**账本阶段只在事实满足时推进**（note 写明计数）。注意 `advance --note` 会覆盖该批 note 历史，只在确需改写时使用。

> **术语两件事（2026-11-26 并入）**：① 新登记术语同写概念行——`baseline/term-concepts.md`（ADR-0084 D5=B；2026-12-01 起 `check_term_concepts` 已入 `check_all` 门禁）；② 首现回填——该件涉及的“语料回收”行在正文译出后改记实际 slug（全库去变音命中口径，参照 `specs/058-term-full-reextraction/execution-log/2026-11-26-shouxian-chuzhi.md`）。

> **工作量提示（ADR-0011）**：含中国文献的词条（`chinese-*` 簇约 30 条 + 全库罗马化线索约 170–280 条，探针见 `tools/biblio_audit.py --all` 的 flagged）文献还原额外 +10–15% 工时。

## 4. 并行线（不占批次，独立交接）

| 线 | 范围 | 目录 | 交接要点 |
| --- | --- | --- | --- |
| 人名表 | 籍属/生卒补捞、译法归一、撞形处置 | `specs/013-person-attribution/` | 缺项已判终态者按 `check_terms` 终态口径，不反复回填 |
| EN 模板审计 | B3.1/B3.2 残差收敛期（第 51 批，2026-11-26；残差 81 件待分族） | `specs/053-en-template-audit/` | `html/` 绝对冻结（ADR-0062），改动只走补丁池与勘误表；入口 `execution-log/2026-11-26.md` |
| 术语 | 全库二次提取、审定库配对、候选池裁定 | `specs/058-term-full-reextraction/`、`tasks/term-pool.json` | 池是库存不是欠账，按词条取用 |
| 流程审计 | 流程规格逐件核对与排程 | `specs/064-flow-spec-audit/` | rev17 排程见 `results/schedule.md`，全部未启动；G0 为翻译开工闸（§0） |

各线开工同样先 `sync_guard pull`，收工 `check_all` 绿。

## 5. 纪律（违反即返工）

1. **只动你认领的批次**；协调只经账本（提交），不共享进行中文件。
2. **推送先 `git fetch` + `pull --rebase`**；账本冲突 rebase 后重放 advance（幂等）；禁 force。
3. **零信任**：既有译文不作底稿；术语先登记 `zh/shu-yu-biao.md` 后使用。
4. **禁子代理**（ADR-0034）：翻译与复核由主代理单干，唯一例外是用户当轮显式批准并写明范围。
5. **抓取礼貌** ≥5 秒/请求；429 即收敛并记录。
6. **不备份文件**（git 即管理）；`script/` 为个人草稿区。
7. **中断随时可停**：重跑 `status` 即断点，工具全部幂等。
8. 演练/试跑产生的假任务与假变更文件必须清理，状态复位 pending 并留痕。
9. **暂存与提交须连续**：不留跨会话暂存内容（053 五十批暂存被 064 提交收编，2026-11-26 判例）。

## 6. 评审线接管

- 全库置空后**无 s3 存量**，原先「R-main-20261108 接管 77 条 r1→r3」的安排自动终止。
- 重译产出的评审仍按件走 `rv-*`／`sg-*` 节点；`r3` 默认停在上一节点，`advance --step r3` 必须带 `--mandate`，且指定的 mandate 不继承（ADR-0054）。
- 复核独立性：actor 须异于原初译，或 evidence 记明冷置回读/密度统计补偿。

## 7. 已作废条目（留档，勿再执行）

| 条目 | 作废原因 |
| --- | --- |
| 27 批 `translate` 旧断点（2026-11-08~24 的 done 计数与认领） | 全库置空（ADR-0081/0082），计数已归零；2026-11-26 清空认领 |
| Wave 0 五词条验证 | 2026-11 已完成 |
| 411 件 `s2.4_termchecked` 体例归一重走队列（specs/039） | 随置空清零，不再有该状态存量 |
| R-main 评审线存量接管（§6 旧文） | 无 s3 存量 |
| 参考文献英文小节标题汉化的待裁定项 | 随重译按 `fan-yi-mu-ban.md` 重新决定 |

## 8. 验收与升级

* 批次收口 → G4 记录（doctrine 最小字段）入 `specs/001-sep-sync-pipeline/execution-log.md`。
* 批次收口 → **语体结论第二读者抽查**：抽 3 条该批完成词条复核语体结论与证据句（specs/015 判据，D29；ADR-0034 相容）。
* 规划书修订（暴露问题回流）→ `specs/005` spec.md 版本号 + 提交说明。

# 并行设计：多会话批次模型（specs/005）

**版本**：v1.0 | **日期**：2026-10-27 | 用户指令："把下载流程，翻译流程等整个大流程的内部设计为支持多个会话并行的（按 a-z 拆分批次，有全局统计表，便于随时中断续上，不同会话之间独立无耦合）"

## 1. 批次模型

大流程按 **a–z 字母批次**拆分（数字开头词条归批次 `1`，共 27 批）。每批是一个独立工作单元：

```
批次 = { letter, phase, claimed_by, claimed_at, note }
phase: pending → intake → fetch → convert → translate → done
```

* 批次的词条集合**不存账本**，由 SUMMARY 实时推导（slug 首字符 → 批次）——单一事实源，账本永不漂移。
* 各阶段与既有工具一一对应，**本设计只记账不重做**：

| 阶段 | 工具 | 幂等性 |
|---|---|---|
| intake | `summary_sync.py apply-add <slug>` | 已存在即 Precondition |
| fetch | `fetch_entry.py <slugs>` / `fetch_audit.py <slugs>` | upsert 幂等 |
| convert | `yuanwen.py <slugs>` | 确定性重转换 |
| translate | `task_ops.py create/advance`（s1→r3） | 状态机单调 |
| done | `check_all` 全绿 | 幂等 |

## 2. 全局统计表（ledger）

`specs/005-translation-campaign/ledger.json` 是**唯一协调点**：只存"意图与认领"（phase、claimed_by/at、note），**不存计数**——计数（每批词条数/已抓/已译/done）由 `tools/campaign.py status` 从仓库实时推导（SUMMARY、baseline、tasks、yuanwen 文件），账本与事实零漂移。

## 3. 会话协议（独立无耦合，随时中断续上）

1. **开工**：`campaign.py status` 看全局统计表 → `campaign.py next` 取"未完成且未认领"的批次建议 → `campaign.py claim <批次> --session <ID>`。
2. **干活**：按该批 phase 运行对应工具（见上表）；每个阶段完成后 `campaign.py advance <批次> <下一阶段>`。
3. **中断**：随时可停——重新开工时 `status` 即是断点，重复运行对应工具幂等无害。
4. **认领过期**：`claimed_at` 超过 7 天的批次可 `claim --force` 抢占（原会话可能已失联）。
5. **无耦合**：不同会话认领不同批次，不共享任何进行中文件；协调只经由账本（git 提交）。

## 4. 本地相与 git 相（多机并行语义）

| 阶段 | 状态存放 | 多机语义 |
|---|---|---|
| fetch / convert | 本地 en/、yuanwen/（gitignore） | **每机各自幂等执行**（原料可再生，不共享） |
| intake / translate / done | git（SUMMARY、译文、tasks、baseline） | 真正的多会话并行面，账本协调 |

## 5. 冲突纪律

* 一个批次同一时刻只有一个认领者（账本记录）；抢占需 `--force` 且留 note。
* 提交只触碰本批文件 + 账本；推送先 `pull --rebase`（rules/06）。
* 账本更新冲突：rebase 后重放 `advance`（幂等）。

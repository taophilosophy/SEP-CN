# I 批翻译进度对账与纠正（2026-11-09）

**执行会话**：I-main-20261109（承接 I-main-20261108 倒序线）｜**形态**：主会话直译，无子代理（用户 2026-11-09 指令）
**依据**：`rules/04`（状态机与 ADR-0021 账本协议）、`rules/08`（方向先行）、`specs/005-translation-campaign/session-handoff.md` §3
**口径**：任务 JSON 状态机 × 段落账本实填 × 正文落盘 × 英文镜像词数，四方核销；计数以 `PROGRESS.md`／`campaign.py status` 生成物为准，本文件只记对账结论与纠正项。

## 1. 方向声明（rules/08）

| 字段 | 内容 |
| ---- | ---- |
| 意图复述 | 用户：先“计算、同步、纠正目前 I 词条的翻译进度”，然后“现在由你负责翻译 I 词条，但是倒序”。 |
| 目标 | ① 用四方核销算出 I 批真实进度并对齐 PROGRESS.md／campaign 账本／任务 JSON；② 纠正记录与实体不一致处；③ 以**倒序**（SUMMARY 次序自尾向首）续译 I 批未完成词条。 |
| 非目标 | 不改英文源与 `yuanwen/` 镜像；不补内容、不造引文；不动他批词条与 SUMMARY 结构；不 push；不使用子代理。 |
| 验收判据 | 三方计数一致（本文件 §3 表 = `PROGRESS.md` I 行 = `campaign.py status` 的 i 行）；账本 `script/lq.py check` HARD=0；成品 `check_style`／`check_academic --strict`／`check_math` 全 0；`check_all` 绿。 |
| 约束与代价 | 多会话并行工作区：提交一律带 pathspec 只碰 I 批文件；共享 `ledger.json` 只落己方 hunk（他会未提交记录保留在工作区）。 |

## 2. 对账方法

1. **清单**：`SUMMARY.md` 中 `(i/<slug>.md)` 且非「——见／— see」别名行 → 正式词条 75 条（与 `campaign.py` 的 `batch_counts('i').total` 一致）。
2. **状态**：`tasks/i/<slug>.json` 的 `state`（唯一事实源）。
3. **账本**：`tasks/i/<slug>.ledger.yaml` 按 `script/lq.py` 的解析口径逐段判 `step1`/`step2` 是否实填（`TBD` 不算填）。
4. **正文**：`i/<slug>.md` 的体量与尾节（参考文献／学术工具／相关词条）齐备度，对照 `yuanwen/i/<slug>.md` 段数。
5. **词数**：`yuanwen/i/<slug>.md` 的英文词数（`[A-Za-z][A-Za-z'\-]*` 计）。

## 3. 真实进度总表（2026-11-09 03:05 UTC+8 实测）

I 批共 **75 条**，英文 **1,210,525 词**。

| 状态 | 条数 | 英文词数 | 词数占比 | 说明 |
| ---- | ---: | ------: | -------: | ---- |
| done | 21 | 236,095 | 19.5% | 其中 3 条账本era（imprecise-probabilities／israeli／intentionality-ancient，账本 167/80/45 段全填），18 条为 2026-11-01/02「40 路批」存量（无账本，前置账本时代） |
| s3_checked | 2 | 17,332 | 1.4% | illumination（账本 90/90）、ingarden（55/55）——三道已过，待 r1→r2→r3→done |
| cleared | 7 | 100,299 | 8.3% | 见表 §4，均非「已译待收」而是**待推进的在途态** |
| pending | 45 | 856,799 | 70.8% | 未动工 |
| **合计** | **75** | **1,210,525** | 100% | done 条数占比 28.0%（21/75） |

与 `campaign.py status`（i 行 75／75／75／21）及 `PROGRESS.md`（`|I|75|75|75|21|`）**一致**，无需改数。

## 4. 在途 9 条细表（纠正重点）

| # | slug | 状态 | 账本实填 | 正文实体 | 判定与处置 |
| ---: | ---- | ---- | ---- | ---- | ---- |
| 70 | intuitionism-ethics | cleared | **30/147**（31–147 段为 TBD） | 旧译 39,933 字（11-02 在途快照，与新账本非同文） | ① 段 8／段 10 `$` 守恒 HARD（src=1, t2=0，公式定界符被吃）待实修；② 补齐 117 段后 compose 覆盖旧译；③ **倒序队列下一条** |
| 46 | it-moral-values | cleared | **98/114**（99–114 段 TBD） | 空壳（H1 44 字） | 续译 16 段（含 oir 1＋note 2）→ compose |
| 63 | intrinsic-extrinsic | cleared | 无账本 | 23,506 字，无尾节 | 11-02 在途快照草稿（无账本＝ADR-0021 不合规，不能作 draft 凭证）；按待译处理，重走账本 |
| 43 | information-biological | cleared | 无账本 | 13,872 字，无尾节 | 同上 |
| 34 | impossible-worlds | cleared | 无账本 | 49,397 字，**末行截断**（`[^sendłak-`）、无学术工具/相关词条 | 同上；快照件本身有截断损坏，不可续用 |
| 27 | imaginative-resistance | cleared | 无账本 | 39,167 字，尾节齐 | 同上 |
| 29 | immunology | cleared | 无账本 | 空壳（H1 78 字） | 未动工 |
| 2 | illumination | s3_checked | 90/90 | 45,038 字，尾节齐 | 待 r1–r3 |
| 49 | ingarden | s3_checked | 55/55 | 49,668 字，尾节齐 | 待 r1–r3 |

**快照遗留的来历（可回溯）**：`d5d3ccd2`（2026-10-27）时上述 5 个文件为 60–101 字节的 H1 骨架；`641faf13`（2026-11-02「在途快照：A–K 批 48 词条翻译中间态入库」）将它们扩为完整正文。即：正文系本战役「40 路批」自产草稿，**非战前旧译**；但无账本、无 step1/step2 双版，不符合 ADR-0021，只能作历史证据，不得作为 draft 凭证或改写底稿（rules/04 零信任）。

## 5. 纠正项（本次已做／待做）

| # | 问题 | 处置 | 状态 |
| ---: | ---- | ---- | ---- |
| C1 | `campaign 账本` i 批 note 已过期（记 pending 47／cleared 7，并把 illumination 记为「在途」；实际 pending 45／s3 2／cleared 7，且 intuitionism-ethics 实填仅 30/147、it-moral-values 98/114） | 用本节实测计数重写 note，认领转交 I-main-20261109 | 本次 |
| C2 | `tasks/i/it-moral-values.json` 的 `cleared`（及 clear 步 evidence）仅在工作区，未提交 | 随本报告提交，恢复「账本＝状态机」一致 | 本次 |
| C3 | intuitionism-ethics 账本段 8／段 10 `$` 守恒 HARD（公式定界符丢失） | 续译时逐段实修后重跑 `lq.py check` | 倒序首条 |
| C4 | `identity-ethics` 已 done 但 steps 缺 `clear`／`draft`（仅 7 步） | 系 2026-11-01「40 路批」存量记录形态（该批从 pending 直接记 s1–s3，draft 未入 steps）；不伪造步骤，只在本表留痕；复核独立性由 ses-FGHIJK-main-1103 满足 | 记录，不改 |
| C5 | 5 条快照遗留（§4）状态为 cleared 而正文有未认证草稿 | 保留正文作历史证据（git 可回溯），一律按待译走账本重译后 compose 覆盖；禁止据半截正文续写 | 记录，随倒序队列处置 |

## 6. 倒序队列（自 #75 向 #1，跳过 done）

未完成 54 条按 SUMMARY 次序倒排，前 12 条：

| 顺位 | SUMMARY 序 | slug | 现状态 | 备注 |
| ---: | ---: | ---- | ---- | ---- |
| 1 | 70 | intuitionism-ethics | cleared | 账本 30/147，续译＋修 2 处 HARD |
| 2 | 69 | intuitionism | pending | 81,736 词 |
| 3 | 68 | intuitionistic-logic-development | pending | 175,231 词 |
| 4 | 67 | international-justice | pending | 145,866 词 |
| 5 | 65 | intuition | pending | 114,893 词 |
| 6 | 64 | introspection | pending | 187,980 词 |
| 7 | 63 | intrinsic-extrinsic | cleared | 快照遗留，重走账本 |
| 8 | 62 | international-law | pending | 114,046 词 |
| 9 | 60 | intentionality | pending | 112,580 词 |
| 10 | 59 | intention | pending | 88,947 词 |
| 11 | 56 | insolubles | pending | 130,133 词 |
| 12 | 55 | inner-speech | pending | 123,969 词 |

（余下 42 条：54、52、51、50、49、48、46、45、43、42、41、40、39、38、37、34、32、31、29、28、27、26、25、24、22、21、20、19、16、15、14、13、12、11、10、9、8、7、5、4、3、2、1，其中 49／2 为 s3_checked 待 r1–r3。）

## 7. 生成物与一致性

* `PROGRESS.md`（2026-11-08 18:30 UTC 生成）I 行 `75|75|75|21` 与本次实测一致。
* `campaign.py status` 的 i 行（75／75／75／21）与本次实测一致；批次 `phase=translate` 不变（未达 done=总）。
* 本文件为对账凭证；倒序翻译逐条的六道凭证落在 `tasks/i/<slug>.json` 的 `steps[].evidence` 与 `tasks/i/<slug>.ledger.yaml`。

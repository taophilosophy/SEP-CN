# B 批词条翻译进度对账（2026-11-09）

**会话**：B-main-20261109b（用户指令：现在由你负责翻译 B，主会话直译、不用子代理）
**工具**：`script/b_audit2_20261109.py`＋`script/b_queue.py` 实时推导（本地草稿区，只读核对）；`campaign.py status`／`progress.py` 复核

## 1. 方法

四源交叉核对 62 个 b 字母目录正式词条：

1. `SUMMARY.md` 正式条目（剔别名「——见」行）→ 62 条，与 `b/*.md` 文件集、`tasks/b/*.json` 任务集三方闭合（无缺文件、无缺任务、无孤儿文件）；
2. `tasks/b/<slug>.json`：state、steps 步序（`clear→draft→s1→s2→s3→r1→r2→r3→done`）、每步 actor/at/evidence 非空、时间单调、`version_pin`（pubinfo 日期对 `baseline/entries.json` 的 substantive_revision，无修订者对 first_published）；
3. `b/<slug>.md` 正文实态：按状态机判规模（cleared＝仅 H1 桩；drafted 起须有实译正文）、H1 对 SUMMARY 登记名；
4. `yuanwen/b/<slug>.md` 源文词数（首个 `[^key]:` 之前、去行内脚注标记）＋ `tasks/b/<slug>.ledger.yaml` 段落账本（`lq.py check`）。

## 2. 实测数字（2026-11-09 02:42 UTC+8）

| 指标 | 条数 | 源文英文词数 | 占比（词） |
|---|---|---|---|
| 正式词条 | 62 | 761,167 | 100% |
| done | 15 | 125,767 | 16.5% |
| r1_reviewed（评审线） | 1 | 6,829 | 0.9% |
| s3_checked（评审线） | 6 | 54,938 | 7.2% |
| drafted（待 s1→s3） | 3 | 20,240 | 2.7% |
| cleared（待全量重译） | 37 | 553,393 | 72.7% |

- **有正文 25 条 / 227,774 词（29.9%）**；清空桩 37 条。
- done 15：boolalg-math、biology-philosophy、bloch、blame、bohr-correspondence、bradley-moral、bodily-awareness、binarium、basing-epistemic、bauer、bayes-theorem、bayle、behaviorism、bergson、buridan。
- s3_checked 6（归 R-main 评审线 r1–r3）：boethius、bradley、buddha、buddhism-chan、buddhism-huayan、butler-moral。
- r1_reviewed 1：boethius-dacia（R-main 初审 02431e93 已提交，待 r2/r3）。
- drafted 3：bessarion、brouwer（旧存量）、belief-merging（B-main-20261109 收口件 f6cec931）。

## 3. 一致性与偏差

**零偏差项**：文件集＝任务集＝SUMMARY 集（62/62/62）；基线与镜像 62/62；步序无跳步、无回退；done 全部九步齐（bauer 另附 qa-rework 开项，属既定语义）；cleared 37 条正文均为 H1 桩（无 cleared 却含正文）；无 pending 却含正文；`version_pin` 62 条与基线逐条一致。

**登记在案的历史遗留（不补造、不改写）**：

1. `boolalg-math` steps 首位多一 `intent` 步，且其时间戳（2026-10-31T22:11:27Z）晚于 `clear`（22:07:25Z）——系旧会话直写 JSON 的方向声明步，`task_ops.py` 的 STEPS 表不含该名；不参与状态判定（state=done 与末步 done 一致），不改写他会话已提交的凭证链。
2. `bessarion`、`brouwer` 的 draft 步 evidence 为空（actor `?`，2026-11-02 旧存量），维持 11-07 队列文档「不补造」裁定。
3. NO_LEDGER 61：B 批段落账本体系自 belief-merging 起才建立（`tasks/b/belief-merging.ledger.yaml`，112 段 step1/step2 双版齐，`lq.py check` HARD=0，`compose` 与正文行尾归一后逐字节一致）；其余 61 条无账本，按既有「旧存量不补造」口径登记为 ADR-0021 债。
4. H1 与 SUMMARY 两处形差（`binarium`、`burley`）为 SUMMARY 转义方括号 `\[...\]` 与正文实形之差，`check_summary.py` 归一化范围，非缺陷。

## 4. 纠正动作（本次落盘）

1. **批次账本注记过时**：原记「done 7/62、cleared 39 按序推进、在途 16」，与事实（done 15、cleared 37、在途 10）不符——已 `campaign.py` 追加 2026-11-09 复账段（原注记保留留痕，不覆盖）。
2. **队列文档三表过时**：`b-batch-queue-2026-11-07.md` 的计数表与队列 A/B 表按实测重建（队列 A 37 条、队列 B 10 条，并补 r1_reviewed 行与 belief-merging/boethius-dacia 备注）；`script/b_queue.py` 同步扩展支持 r1_reviewed 状态。
3. **PROGRESS.md**：重生成后 B 行 62/62/62/15 与实测一致（全局 done 222）。
4. **认领转交**：批次 b 自 B-main-20261109 转 B-main-20261109b（用户改派，`--force` 认领，同 11-08 接管先例）；注记中明示原会话勿再推进 B 批词条，避免同件双写。

## 5. 下一步（翻译线队列）

- 队列 A 队首 **brentano-judgement**（11,321 词）起按源文词数升序全量重译（九步，账本双版）；
- `belief-merging` 已 drafted，其 s1→s3 归本线续做，但暂不与其前序会话同件；
- s3_checked 6 条与 r1_reviewed 1 条的 r1–r3 仍归 R-main 评审线（session-handoff §6），本线不自推。

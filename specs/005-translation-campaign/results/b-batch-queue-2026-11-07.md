# B 批作业队列与接管记录（2026-11-07）

**会话**：B-main-20261106（接管 B 批翻译，主会话直译，不用子代理） | **账本**：`campaign.py status --batch b`

## 当前计数（2026-11-07 实测，四源实时推导）

| 指标 | 数值 |
|---|---|
| 正式词条 | 62 |
| done | 15（boolalg-math、binarium、biology-philosophy、bauer、basing-epistemic、behaviorism、bloch、bayes-theorem、bayle、blame、bergson、bohr-correspondence、bradley-moral、bodily-awareness、buridan） |
| r1_reviewed（待 r2→r3→done，评审线） | 1 |
| s3_checked（待 r1→r3→done 收口，评审线） | 6 |
| drafted（待 s1→s3→r1→r3→done） | 3 |
| cleared（待全量重译） | 37 |

## 队列 A：cleared 37 条全量重译（按源文词数升序，先短后长）

> 词数口径：源文正文（首个 `[^key]:` defs 行之前）去掉行内脚注标记后的英文词数；由 `script/b_queue.py` 实时推导。

| 词数 | slug | 词数 | slug |
|---|---|---|---|
| 11321 | brentano-judgement | 11411 | brentano |
| 11460 | byzantine-philosophy | 11682 | black-reparations |
| 11745 | bosanquet | 12038 | broad |
| 12085 | biomedicine | 12120 | bodin |
| 12315 | buber | 12359 | bradley-regress |
| 12615 | beauty | 12960 | bioethics-latin-america |
| 12960 | bolzano-logic | 13139 | biology-experiment |
| 13452 | baudrillard | 13594 | biodiversity |
| 13615 | burke | 13691 | biology-individual |
| 13857 | boole | 14137 | bonaventure |
| 14290 | belief | 14470 | beauvoir |
| 14825 | biology-developmental | 15273 | boyle |
| 15355 | berkeley | 15509 | branching-time |
| 16102 | bentham | 16476 | burley |
| 17225 | boundary | 17506 | berlin |
| 17802 | benjamin | 18713 | bruno |
| 19438 | bell-theorem | 20403 | beardsley-aesthetics |
| 21130 | bounded-rationality | 22856 | buddhism-tiantai |
| 23464 | bolzano |  |  |

## 队列 B：在途 10 条收口（r1 复审口径）

| 词数 | slug | 状态 | 备注 |
|---|---|---|---|
| 6829 | boethius-dacia | r1_reviewed | 评审线 R-main 初审已过 02431e93；待 r2/r3 |
| 8049 | buddha | s3_checked |  |
| 8905 | butler-moral | s3_checked |  |
| 9181 | boethius | s3_checked |  |
| 9268 | buddhism-chan | s3_checked |  |
| 9440 | bradley | s3_checked |  |
| 10095 | buddhism-huayan | s3_checked |  |
| 4223 | bessarion | drafted | draft 步 evidence 空（旧留痕缺口，不补造）；待 s1→s3 |
| 4827 | brouwer | drafted | 同上 |
| 11190 | belief-merging | drafted | draft 收口 f6cec931，账本 112 段双版齐；待 s1→s3 |

## 本批确认的家法（biology-philosophy 首例实证）

1. **原生脚注型拆分**：`[^note-N]` 内容注 → 译入 `## 脚注`；书目区 defs（含 `there-*`/`-nd` 等散文型导语注）→ 留在 `## 参考文献` 逐字符照录（与 reism/kokugaku-school 等 done 条目一致）。
2. **参考文献节**只留一行 **照录说明**（bold），转换器 blockquote 注记可省（check_academic 二者皆认）。
3. **人名**：按 ren-ming-biao 既有裁定——Sarkar 保留英文、Wimsatt 温萨特、Hull 赫尔；无通行汉名者（Woodger/Beckner/Ghiselin/Amundson/Grene/Ferguson）保留英文并登记 ADR-0022。
4. **术语冲突先查**：`supervenience` 词汇表定名 随附性（我初登记 随附 触发 check_terms 硬冲突，已改）；登记后必跑 `check_all` 第七项。
5. **组装门**：assemble 脚本内建标记多重集等值 + defs 键集 + 段落数前置门；组装后只改 OUT、不再重跑 assemble。
6. 相邻字母条目共用的术语先登记再用；跨条同名者（如 基切尔/沙夫纳）后续条目直接复用本批登记行。

## 进度流水（追加）

- 2026-11-07：`biology-philosophy`（076c04d9）、`bloch`（d6fff72c）九步入 done。bloch 首例实证"原生脚注型"组装：note-1..12 译出进 `## 脚注`，书目 defs（含散文型导语注）照录进 `## 参考文献`，assemble 门内建 note-N 键集与非 note defs 计数双校。**教训**：prose 批量改写会丢行内脚注标记（moltmann-1964 一例），改写后必须重跑 marker/defs 守恒门。
- 2026-11-07（续）：`blame`（da46a7cc）九步入 done。首例无内容性脚注条目（源无 Notes 区，defs 全为书目）；撇号键（o’brien-2022）须用 U+2019 与 defs 逐字符一致；斜体→加粗批处理须用 `\*([^*
]+)\*` 逐跨度匹配，否则跨强调对粘连（areté 句事故已修复）。
- 2026-11-07（续二）：`bohr-correspondence`（f7f8bb71）九步入 done。首例含图与公式条目：公式 128 个零失衡、图路径改 `../yuanwen/assets/`；斜体→加粗逐跨度正则会把 `**已加粗**` 吃成三连星，需后处理修复；`Copenhagen interpretation` 统一词汇表定名“哥本哈根诠释”，`Jammer` 按人名表作“贾默”。
- 2026-11-07（续三）：`bodily-awareness` 九步入 done（15 575 汉字 / 5 节 14 小节 / 207 条书目 defs 照录 / 242 标记 242 守恒）。首例**零内容性脚注且无 `## 脚注` 节**（源无 Notes 区）；`O’Shaughnessy` 撇号键为 U+2019，须与 defs 逐字符一致；`enactive approach` 沿词汇表定名“生成进路”（初写“生成式进路”已改）；prose 34 条告警逐句实修至 0。队列表由 `script/b_queue.py` 重建，避免手改错位。
- 2026-11-08：`bradley-moral` 九步入 done（15 870 汉字 / 8 节 / 13 段直引 / 84 条书目含三个书目小节）。两处实测教训：① **`目的` 内含 `的` 字**，`de-chain` 把它计入“的”数，改写时用 `目标` 可消误报；② 斜体→加粗批量正则（`\*([^*]+)\*`）会跨强调对粘连，并与残留 `***` 叠加，事后须跑 `\*{3,}` 归一、并把拉丁单字 `*A*` 还原（本轮 7 个分片被伤，已修）。

## 2026-11-08 接管对账（B-main-20261108）

**接管**：用户改派，`campaign.py claim b --force` 自 B-main-20261106 接手；其遗留在途件三笔已核实收编：

1. **术语修正三件**（008 审定库 2026-11-08 裁定行回写，登记行已在 HEAD）：bohr-correspondence 作用量子→量子作用、bodily-awareness 情感性触觉→情感性触摸（×2）、buddhism-chan 关怀伦理→关怀伦理学。提交 ba860cda。
2. **behaviorism 收口**：并行会话 R-main-20261108 于 12:27 完成 r1–r3→done（026e9564），补回审计发现的 `[^ross-2008]` 缺标记，登记项销账。
3. **buridan 组装稿收编**：前会话十分片组装稿（382 行）未 advance 即中断；独立只读对账（script/verify_buridan_20261108.py）五项全绿——行内标记 79:79 多重集与顺序全等、note 键集 57/57、书目 defs 105 全覆盖、H2 7/7、段落 50:50、年份 45:45、尾节四件套齐——advance draft 收编，待 s1–s3、r1–r3。

**当前计数**（campaign.py status 实时推导，2026-11-08 12:45）：done 12 / s3_checked 9 / drafted 2 / cleared 39 = 62；campaign 账本零漂移，PROGRESS.md 已刷新（B 行 done=12）。

**s3_checked 9**：bayes-theorem / bergson / boethius-dacia / boethius / bradley / buddha / buddhism-chan / buddhism-huayan / butler-moral（behaviorism 已销账）。**drafted 3**：bessarion / brouwer（旧存量，draft 步 evidence 空缺口维持不补造裁定）/ buridan（新收编）。

**队列 A 头部更新**：cleared 39 条队首为 belief-merging 11190 / brentano-judgement 11321 / brentano 11411（buridan 已出队）。

## 2026-11-08（续）：buridan 九步入 done＋分工裁定

- **buridan** 九步完整闭环（B-main-20261108）：接管收编前会话组装稿（draft 步）→ s1 回源逐段实修 52 处 → s2 术语 27 项核销＋token 册行订正「殊例」＋人名补登 12 行（含 Seneca the Elder 与既有 Seneca 行分立）→ s3 四检全绿 → r1 57 内容注通读对照＋四处同键异译回改正形（波纳文图拉/因根的马西利乌斯/菲洛波努斯/达西亚的波爱修斯）＋注内学者补登 5 行 → r2 拉丁短语守恒＋引注抽查 → r3 check_all 七项全绿 → done。成稿 19 746 汉字 7 节，57 内容注译出、105 书目 defs 照录。凭证链 d2ed3ff4 → e8ede11a →（本提交）。
- **并行收口波**：R-main-20261108 在收口 s3_checked 存量（behaviorism/bayle/bauer/bayes-theorem/bergson 已 done）；**分工裁定——s3_checked 余 7 条（boethius-dacia/boethius/bradley/buddha/buddhism-chan/buddhism-huayan/butler-moral）归 R-main 收口波，B-main-20261108 转向 cleared 队列全量翻译**，互不抢件。
- **当前计数**（2026-11-08 13:10）：done 15 / s3_checked 7 / drafted 2 / cleared 38 = 62。drafted 2 = bessarion/brouwer（旧存量）＋buridan 已出队。

## 2026-11-09 复账接管（B-main-20261109b）

**接管**：用户指令「现在由你负责翻译 B」（主会话直译、不用子代理），`campaign.py claim b --force` 自 B-main-20261109 接手；对账全文见 `b-progress-audit-2026-11-09.md`。

**实测**（2026-11-09 02:42 UTC+8，`script/b_queue.py` 实时推导）：62 条 = done 15（125,767 词）/ r1_reviewed 1（boethius-dacia，评审线）/ s3_checked 6（评审线）/ drafted 3（bessarion 4,223、brouwer 4,827、belief-merging 11,190）/ cleared 37（553,393 词）；有正文 25 条（227,774 词，29.9%），清空桩 37 条。四源闭合零缺项（SUMMARY＝文件＝任务 62/62/62），步序、凭证、时间单调、version_pin 四维探针零异常。

**纠正三件**：①批次账本注记原记「done 7/cleared 39/在途 16」已过时 → 按实测重记（原注记保留，追加不覆盖）；②本队列三表重建（cleared 37、在途 10，补 r1_reviewed 行与 belief-merging/boethius-dacia 备注；`script/b_queue.py` 扩展支持 r1_reviewed）；③PROGRESS.md 重生成，B 行 62/62/62/15 与实测一致。

**在途件归属**：belief-merging draft 为 B-main-20261109 收口件（f6cec931；账本 112 段双版齐、`lq.py check` HARD=0、compose 与正文归一后逐字节一致），其 s1→s3 由本线续做；boethius-dacia r1 为 R-main 评审线件（02431e93）。原 B-main-20261109 会话请勿再推进 B 批词条（防同件双写），s3_checked 6 条与 r1_reviewed 1 条的 r1–r3 仍归 R-main。

**队列 A 队首**：brentano-judgement 11,321 词（belief-merging 已出队）；按源文词数升序全量重译，账本双版随 draft 入库。

- 2026-11-09：`brentano-judgement` 立账（219 段：body 184 / note 34 / biblio 照录 74 / oir 1，源 11,321 词），账本 p1（段 1–20）双版落盘。**方向声明**（rules/08）：意图＝按 SEP 英文源全量重译布伦塔诺判断理论词条；目标＝九步走完、四检全绿、术语与人名先登记；非目标＝不改英文源、不补内容、不造引文；验收＝`lq.py check` HARD=0＋compose 与正文逐字节一致＋s3 学术挂钩 0 硬错误。术语首译登记 12 行（承认 Anerkennung／明证性 Evidenz／存在判断／直言判断／假言判断／命题态度等）。接力点：段 21。

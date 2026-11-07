# B 批作业队列与接管记录（2026-11-07）

**会话**：B-main-20261106（接管 B 批翻译，主会话直译，不用子代理） | **账本**：`campaign.py status --batch b`

## 当前计数（2026-11-07 实测，四源实时推导）

| 指标 | 数值 |
|---|---|
| 正式词条 | 62 |
| done | 6（boolalg-math、biology-philosophy、bloch、blame、bohr-correspondence、bodily-awareness） |
| s3_checked（待 r1→r3→done 收口） | 14 |
| drafted（待 s1→s3→r1→r3→done） | 2 |
| cleared（待全量重译） | 40 |

## 队列 A：cleared 40 条全量重译（按源文词数升序，先短后长）

> 词数口径：源文正文（首个 `[^key]:` defs 行之前）去掉行内脚注标记后的英文词数；由 `script/b_queue.py` 实时推导。

| 词数 | slug | 词数 | slug |
|---|---|---|---|
| 10815 | bradley-moral | 11097 | buridan |
| 11190 | belief-merging | 11321 | brentano-judgement |
| 11411 | brentano | 11460 | byzantine-philosophy |
| 11682 | black-reparations | 11745 | bosanquet |
| 12038 | broad | 12085 | biomedicine |
| 12120 | bodin | 12315 | buber |
| 12359 | bradley-regress | 12615 | beauty |
| 12960 | bioethics-latin-america | 12960 | bolzano-logic |
| 13139 | biology-experiment | 13452 | baudrillard |
| 13594 | biodiversity | 13615 | burke |
| 13691 | biology-individual | 13857 | boole |
| 14137 | bonaventure | 14290 | belief |
| 14470 | beauvoir | 14825 | biology-developmental |
| 15273 | boyle | 15355 | berkeley |
| 15509 | branching-time | 16102 | bentham |
| 16476 | burley | 17225 | boundary |
| 17506 | berlin | 17802 | benjamin |
| 18713 | bruno | 19438 | bell-theorem |
| 20403 | beardsley-aesthetics | 21130 | bounded-rationality |
| 22856 | buddhism-tiantai | 23464 | bolzano |

## 队列 B：在途 16 条收口（r1 复审口径）

| 词数 | slug | 状态 | 备注 |
|---|---|---|---|
| 3385 | binarium | s3_checked |  |
| 4223 | bessarion | drafted | draft 步 evidence 空（旧留痕缺口，不补造） |
| 4827 | brouwer | drafted | 同上 |
| 6829 | boethius-dacia | s3_checked |  |
| 7416 | bauer | s3_checked |  |
| 7753 | basing-epistemic | s3_checked |  |
| 7829 | behaviorism | s3_checked | **实缺 [^ross-2008]** 正文末句，r1 必修 |
| 8049 | buddha | s3_checked |  |
| 8674 | bayes-theorem | s3_checked |  |
| 8905 | butler-moral | s3_checked |  |
| 9181 | boethius | s3_checked |  |
| 9268 | buddhism-chan | s3_checked |  |
| 9440 | bradley | s3_checked |  |
| 9561 | bayle | s3_checked |  |
| 10095 | buddhism-huayan | s3_checked |  |
| 10525 | bergson | s3_checked |  |

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

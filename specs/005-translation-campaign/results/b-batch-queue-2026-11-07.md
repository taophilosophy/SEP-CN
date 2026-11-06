# B 批作业队列与接管记录（2026-11-07）

**会话**：B-main-20261106（接管 B 批翻译，主会话直译，不用子代理） | **账本**：`campaign.py status --batch b`

## 当前计数（2026-11-07 实测，四源实时推导）

| 指标 | 数值 |
|---|---|
| 正式词条 | 62 |
| done | 2（boolalg-math、biology-philosophy） |
| s3_checked（待 r1→r3→done 收口） | 14 |
| drafted（待 s1→s3→r1→r3→done） | 2 |
| cleared（待全量重译） | 44 |

## 队列 A：cleared 44 条全量重译（按源文词数升序，先短后长）

| 词数 | slug | 词数 | slug |
|---|---|---|---|
| 7873 | bloch | 12718 | biology-experiment |
| 10028 | blame | 12993 | biology-individual |
| 10150 | bohr-correspondence | 13118 | biodiversity |
| 10433 | bodily-awareness | 13223 | burke |
| 10490 | bradley-moral | 13646 | bonaventure |
| 10579 | bodin | 13749 | belief |
| 10756 | belief-merging | 13993 | biology-developmental |
| 10759 | buridan | 14094 | beauvoir |
| 10939 | brentano-judgement | 14589 | boyle |
| 11045 | byzantine-philosophy | 14793 | berkeley |
| 11065 | broad | 15332 | branching-time |
| 11084 | brentano | 15427 | bentham |
| 11519 | black-reparations | 16186 | burley |
| 11558 | bosanquet | 16295 | boundary |
| 11617 | biomedicine | 16613 | berlin |
| 11829 | buber | 16825 | benjamin |
| 11956 | bradley-regress | 17475 | bruno |
| 12231 | beauty | 18936 | bell-theorem |
| 12424 | bioethics-latin-america | 20203 | beardsley-aesthetics |
| 12665 | bolzano-logic | 20254 | bounded-rationality |
| 12682 | baudrillard | 21541 | bolzano |
| 12694 | boole | 22600 | buddhism-tiantai |

## 队列 B：在途 16 条收口（r1 复审口径）

| 词数 | slug | 状态 | 备注 |
|---|---|---|---|
| 2920 | binarium | s3_checked | 备注型 note-* defs 已齐（47 defs） |
| 6483 | boethius-dacia | s3_checked | |
| 7521 | basing-epistemic | s3_checked | |
| 7561 | behaviorism | s3_checked | **实缺 [^ross-2008]** 正文末句，r1 必修 |
| 7732 | buddha | s3_checked | |
| 8344 | bayes-theorem | s3_checked | |
| 8541 | butler-moral | s3_checked | |
| 8922 | boethius | s3_checked | |
| 9170 | buddhism-chan | s3_checked | |
| 9253 | bayle | s3_checked | |
| 9261 | bradley | s3_checked | |
| 9889 | buddhism-huayan | s3_checked | |
| 10261 | bergson | s3_checked | |
| 7151 | bauer | s3_checked | |
| 4029 | bessarion | drafted | draft 步 evidence 空（旧留痕缺口，不补造） |
| 4462 | brouwer | drafted | 同上 |

## 本批确认的家法（biology-philosophy 首例实证）

1. **原生脚注型拆分**：`[^note-N]` 内容注 → 译入 `## 脚注`；书目区 defs（含 `there-*`/`-nd` 等散文型导语注）→ 留在 `## 参考文献` 逐字符照录（与 reism/kokugaku-school 等 done 条目一致）。
2. **参考文献节**只留一行 **照录说明**（bold），转换器 blockquote 注记可省（check_academic 二者皆认）。
3. **人名**：按 ren-ming-biao 既有裁定——Sarkar 保留英文、Wimsatt 温萨特、Hull 赫尔；无通行汉名者（Woodger/Beckner/Ghiselin/Amundson/Grene/Ferguson）保留英文并登记 ADR-0022。
4. **术语冲突先查**：`supervenience` 词汇表定名 随附性（我初登记 随附 触发 check_terms 硬冲突，已改）；登记后必跑 `check_all` 第七项。
5. **组装门**：assemble 脚本内建标记多重集等值 + defs 键集 + 段落数前置门；组装后只改 OUT、不再重跑 assemble。
6. 相邻字母条目共用的术语先登记再用；跨条同名者（如 基切尔/沙夫纳）后续条目直接复用本批登记行。

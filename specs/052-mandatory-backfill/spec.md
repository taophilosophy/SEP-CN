# 强制集存量回补与跨机收编件处置（specs/052）

**性质**：账务重算与回炉｜**边界**：不修内容、不翻译（ADR-0072）、不改 `en/`
**触发**：用户 2026-11-19「批准1、2」＝批准 `specs/051` §2 待决策第 1 条（启动强制集回补批次）与第 2 条（18 件 cleared 有正文的处置）
**权威**：ADR-0075（存量回补与跨机收编件的账务规则）

## 0. 结论摘要

| 项 | 处置前 | 处置后 |
| ---- | ---- | ---- |
| 曾走到 R3 的 400 件中，强制集（s0/s2.4/global/R1/R2/R3）成立 | 按 journal 计 0 件（s0 有 17、s2.4 与 global 各 0） | **394 件**（6 件存续失败，逐件定性见 §1.5） |
| s0 / s2.4 / global 的 journal 覆盖（400 件面） | 17 / 0 / 0 | 397 / 394 / 394 |
| 账实不符（`check_taskfile_invariant`） | 19 件 | **0 件**（严格档已入 `check_all` GATES） |
| 任务游标与 journal 的偏差 | 400 件游标停在 s2.4 或更早 | 不变（回补不迁移状态，见 §1.2） |

一句话：**"完成"现在可以按现行强制集成立 394 件，另外 6 件不成立且已定性；18 件账外内容回到了账上。**

## 1. 第 1 条：强制集在完成件上零覆盖

### 1.1 缺口量化（复算基准）

目标面 = journal 有 `R3` pass 的 **400 件**（不是"核心段完成"394 件：`abelard`、`abhidharma`、`abner-burgos`、`abortion`、`advance-directives`、`identity-ethics` 六件 R3 已过但缺 `draft` 记录，用核心段口径会把它们整批漏掉）。

| 节点 | 处置前有 pass | 缺口 |
| ---- | ---- | ---- |
| `s0` | 17 / 400 | 383 |
| `s2.4` | 0 / 400 | 400 |
| `global` | 0 / 400 | 400 |
| `R1`/`R2`/`R3` | 400 / 400 | 0 |

成因不是"判据不严"，而是**环节是后加的**：s0 于 2026-11-15 前移（ADR-0052）、s2.4 于 11-16/17 上线（ADR-0043/0063）。400 件的完成发生在这些环节存在之前，`revert-state` 只把游标退到 s2.4，从未产生 s0/s2.4/global 的 pass。

### 1.2 为什么是"重算判据"而非"补状态"

`rules/journal-schema.json` 的 `replay_on_change.tighten` 已经写明这类处置：

> 新判据是旧判据的超集（收紧）：对既存 pass 重跑新判据；`state_migration: 0`；追加 pass（`gate_version+1`）或 fail。

所以回补**不改任务状态、不写 steps**，只向 journal 追加 `pass`/`fail`；`state` 仍是推进游标。这样做的代价是"游标落后于 journal"，收益是"不把一次机检伪装成一次人工校次"——`s2.5_checked` 的语义含人审，回补无权声称。

### 1.3 记账规则

* 每件按 `s0 → s2.4 → global` 顺序求值；某节点 fail 即停，下游不记 pass（schema：fail 之后下游不得 pass）。
* `pass` 写 `gate`（现行判据名，非空）、`gate_version`（`sep-pipeline/v2@2026-11-17`）、`witness`（批次账定位）、`note = "backfill:<date>"`。
* `fail` 另写 `reason`（失败命令 + 输出尾部 6 行，截 600 字）。
* 幂等：已有 pass 跳过；本批次已判 fail 的节点默认跳过（`--recheck` 才重判）。
* 凭证纪律：只有全量运行写主账；`--limit`/`--slugs` 只写 `-partial`（`specs/051` §1.5 的凭证覆写教训）。

### 1.4 执行与批次账

| 轮次 | 目标 | 结果 | 产物 |
| ---- | ---- | ---- | ---- |
| 试跑 | 5 件 | 只读试算（`apply=false`，验证判据串接与凭证结构） | `results/backfill-20261119-partial.json` |
| 首轮 | 394 件（核心段口径） | s0 376 pass / s2.4 383 / global 383；fail 3 / 7 / 0 | `results/backfill-20261119-run1.json` |
| 修正后 | 394 件 | s2.4 补记 4 件（首轮假阳性），global 4 件 | 并入主账 |
| 补角 | 400 件（R3 口径） | 6 件补齐：s0 +4、s2.4 +6、global +6，全过 | `results/backfill-20261119.json` |

批次总账（按 journal 的 `backfill:` 标记计，不按某一轮动作计）：

| 节点 | 批次写入 pass | 存续 fail | 处置后有 pass |
| ---- | ---- | ---- | ---- |
| `s0` | 380 | 3 | 397 / 400 |
| `s2.4` | 394 | 3 | 394 / 400 |
| `global` | 394 | 0 | 394 / 400 |

### 1.5 存续失败 6 件（逐件定性）

| 件 | 节点 | 判据 | 现象 | 类别 |
| ---- | ---- | ---- | ---- | ---- |
| `idiolects` | s0 | `en_integrity` | `en/idiolects/` 内有 `appendix.html` 未登记（`unregistered_orphans`） | 源包账务（登记缺口） |
| `saadya` | s0 | `en_integrity` | 同上，`notes.html` 未登记 | 源包账务（登记缺口） |
| `logic-preference` | s0 | `en_source_audit` | `\[` 45 处与 `\]` 43 处不配对（硬） | 源本体缺陷 |
| `ibn-sina` | s2.4 | `check_style` | 第 129 行单引号不成对（嵌套引文层叠） | 译文体例 |
| `implicature-optimality-games` | s2.4 | `check_style` | 第 101 行公式内 `\text{’}`（右引号先于左引号） | 转换/源体例，待定性 |
| `quine-nf` | s2.4 | `check_style` | 第 13 行同上 | 转换/源体例，待定性 |

两类都不属"重译"：前三件的修法是补登记／修源本体（`en/` 侧另案，ADR-0062 冻结不阻登记），后三件是体例层面的定点修（`implicature`/`quine-nf` 的 `\text{’}` 疑为转换产物，须先定性再改）。按边界，本轮不动内容。

### 1.6 更正链（必须留痕）

首轮 7 项 s2.4 fail 中 4 项不是内容失败，而是**判官崩溃**：`check_terms --docs` 触发 `write_person_missing` / `write_orig_missing`，两函数用固定 `.tmp` 名 + 无重试的 `os.replace`，8 路并发下抛 `WinError 2/5/32`，进程以 1 退出，被上层读成"术语门禁未通过"。

* 假阳性件：`antonio-rosmini`、`deductivism-mathematics`、`kierkegaard`、`sharpe`。
* 修法：`tools/check_terms.py` 新增 `_atomic_write`（pid 后缀 tmp + 60 次 50ms 退避），两处报告写出改用之；补 2 项单测。
* 修后重判 4 件全 pass；`fail` 事件留史（只追加），存续失败按"同节点无 pass"口径计，故账上是 3 而不是 7。
* 教训入 ADR-0075 决策 6：**判官崩溃不得被读成被judged对象失败**。

### 1.7 新发现（不属本轮实施，待裁定）

`s2.4` 的术语轴 `check_terms --docs` 在代码里是 `if docs: return 0`——**恒告警，永不失败**（`tools/tests/test_check_terms.py` 有断言如此）。也就是说 s2.4 的硬拦实际只由 `check_pairs --gate`（体例/勘误）与 `check_style` 承担，"术语一致性"这一条从未拦过任何东西。这与 `markdownlint`（`specs/051` §1.2）是同一族：声明硬拦、实际不拦。

是否收紧（收紧到"缺登记译法"还是只到"主译未落地"）、以及收紧后 394 件里会有多少转红，须单独裁定；本轮**未改**该判据，只在回补账上如实记 `gate` 名。

## 2. 第 2 条：18 件 cleared 有正文

### 2.1 事实链

18 件的 `steps` 只有一条 `clear`（2026-11-01 至 11-12），正文首次入库则在 clear 之后：

| 首次入库提交 | 件数 | 说明 |
| ---- | ---- | ---- |
| `641faf13a`（2026-11-02「在途快照：A–K 批 48 词条翻译中间态入库（cleared/drafted/s1，正文未完尾节未拼）」） | 7 | 提交信息自述"中间态、尾节未拼" |
| `05b58570c` / `000c18c58`（2026-11-13 跨机 WIP 快照） | 2 | `axiom-choice` 11-12 版 2 行 → 11-13 版 319 行 |
| 其余（`e50c204d7`、`91e25c206`、`61f03060a`、`ca4853c2c`、`0cd06b97a`、`7a52044ad`、`2c8a05ddf`） | 9 | 单件入库，均无 journal 事件 |

逐件 commit／sha256／汉字数见 `results/adopt-provenance.json`（18 行，哈希为调查时实测；处置时逐件复核，不符即拒）。

### 2.2 处置

**没有选"补 pass 凭证"**：正文是"中间态"，补 pass 等于凭空造一次校次。改为：

1. 补记 `import` 事件：`synthetic: true`（事后补记）、`basis: "state"`、`state_at_import: "cleared"`、`note` 记首次入库 commit／日期／sha256 前 16 位／汉字数——**不推断中间节点**。
2. 回炉：`advance --step s0`（真跑 `en_integrity` ＋ `en_source_audit`，18 件全过）→ `advance --step draft`，进入 s1 队列。
3. 截断件停在 `s0_source_checked` 并 `block`：
   * `haecceitism`：EN 块 199/249 未配对（zh 26 块 / 2,898 汉字）
   * `hamann`：EN 块 195/263 未配对（zh 5 块 / 365 汉字，正文仅存导言）
   两者都是"正文只译了开头"，不能声称 `drafted`。

结果：16 件 `drafted`、2 件 `s0_source_checked` ＋ 阻塞；`check_taskfile_invariant` 的 I1 违例 18 → 0。

### 2.3 顺带修掉的最后一处违例

`ci-hui-biao`（词汇表维护任务）的 `zh_doc` 指向 `qian-yan/ci-hui-biao.md`，该文件已于 `5b8ab13b7`（2026-11-13）并入 `shu-yu-biao.md`（ADR-0036 并网）。指针未随并网更新，故报 `maintenance-doc-missing`。处置：`zh_doc` 改为 `shu-yu-biao.md`，追加 `zh-doc-repoint` 步骤记录（append-only）。

违例清零后 `check_taskfile_invariant --strict` 升入 `check_all.py` 的 `GATES`（CI 矩阵自动跟随），从"每日告警"变为"硬拦"。

## 3. 未做与边界

* **未做内容修复**：6 件失败件、2 件截断件的修复属后续批次；不做翻译（ADR-0072）。
* **未改判据强度**：`markdownlint` 仍告警位；术语轴仍恒 0（§1.7 待裁定）。
* **未动 `specs/051` §2 的其余 5 条**（③ 骨架页呈现、④ R3 时点、⑤ draft/F1/F2 判据、⑥ replay 三档、⑦ 漏译入 CI）。
* **未迁移状态**：400 件游标仍在 s2.4 或更早；回补只补 journal。副作用是 `PROGRESS.md` 的"强制集完成"与"核心段完成"不再同源，已在读数下加口径注。

## 4. 复算命令

```
python tools/mandatory_backfill.py --all --jobs 6            # 只读复核（不写 journal）
python tools/check_taskfile_invariant.py --strict            # 应为 0 违例
python tools/progress.py                                     # 强制集完成 394，其中回补 394
python tools/check_stages.py                                 # 判据表 13 项
python -m unittest tools.tests.test_mandatory_backfill tools.tests.test_check_terms
```

## 5. 与既有规格的关系

* `specs/051` §2 第 1、2 条由本 spec 收口；其余 5 条状态不变。
* `specs/036` 的存量批次（s0 源审计补课）与本批次**不同轴**：036 判"翻译依据可不可信"，本批判"完成能不能按现行强制集成立"。036 的 s0 门禁在本次回补中被真实调用（397/400 通过），其存量批次仍待批。
* `specs/044` 的逐段对齐（`haecceitism`/`hamann` 截断）是本 spec §2.2 阻断判据的来源，口径一致。

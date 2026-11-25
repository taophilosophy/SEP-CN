# 阶段 1.2 分析报告：上游重抓、基线更新、补丁复核、转换进度

任务卡：specs/062。执行日：2026-11-25。机读证据：`phase12-run.json`、`en-delta.json`、`entry-meta-delta.md`、`fetch-last.json`。

## 一、抓取

| 项 | 值 |
| --- | --- |
| 词条 | 1873／1873，抓取失败 0 |
| 未变（unchanged） | 1351（不写盘、不动钉账，仍转换） |
| 钉账变化 | 522（主体为 `local.js` 补登：存量文件入 `files[]`，盘面不变） |
| 磁盘真变化 | 126 文件／100 词条 |
| 耗时 | 1414 秒（16 路，ADR-0069 无强制间隔） |
| 转换 | 1871 成功；2 件 `PermissionError`（Windows 文件占用：frege-logic、scientific-reproducibility），补转后 I2 复核 1873 件 0 issue |

## 二、磁盘变化分类（`bin/en_delta.py`，可见文本判据）

| 判定 | 文件数 | 含义 | 处置 |
| --- | --- | --- | --- |
| `text` | 65 | 可见文本实质改动 | 出建账清单（见 §六） |
| `layout` | 40 | 逐字等值，仅换行／标签属性／注释／模板重排 | 不建账 |
| `rename-wave` | 17 | 增删行全部是目录改名波纹（croce／history／privacy） | 不建账，随目录线 |
| `binary` | 3 | 图片资产（berlin.png＋重导出的 2 件 SVG） | 按 sha 随钉替换入库，不建账 |
| `asset` | 1 | 脚本／样式资产（voting-methods/local.js） | 随钉入库 |

`text` 中最大的六件与上游正式修订完全对应：justice-retributive（3725 行）、hume-moral（2580）、plato-sophstate（2098）、culture-cogsci（1849）、gorampa（1841）、logic-deontic（1333）。

## 三、上游修订信号（`bin/entry_meta_delta.py`）

元数据变化 29 件，其中 `substantive_revision` 变更 10 件（上游 2026-11-21～24 发布）：

| 词条 | 旧 | 新 |
| --- | --- | --- |
| culture-cogsci | 无 | Nov 21, 2026 |
| delusion | May 4, 2022 | Nov 21, 2026 |
| embodied-cognition | 无 | Nov 21, 2026 |
| hume-moral | Aug 20, 2018 | Nov 22, 2026 |
| justice-retributive | Jul 31, 2020 | Nov 24, 2026 |
| logic-deontic | Mar 11, 2021 | Nov 23, 2026 |
| plato-sophstate | Feb 26, 2020 | Nov 22, 2026 |
| rule-following | 无 | Nov 23, 2026 |
| schopenhauer | Sep 9, 2021 | Nov 23, 2026 |
| gorampa | Mar 29, 2021 | 无（修订行撤销，需对照 archinfo 复核） |

## 四、补丁复核（必要性／有效性／一致性）

| 补丁 | 词条 | 出处 | 命中/expect | 判定 |
| --- | --- | --- | --- | --- |
| P-001 | incommensurability | upstream-typo | 1/1 | 有效 |
| P-002 | lakatos | upstream-typo | 1/1 | 有效 |
| P-003 | yorck | upstream-typo | 1/1 | 有效 |

一致性：`check_en_patches --strict` 报 `mismatch 0`、`admission_bad 0`、`index_bad 0`、`git_check_bad 0`、`public_candidates 0`。结论：三条补丁在上游重抓后仍必要且可用，不满足 ADR-0085 的升档条件（各仅命中 1 件、变更核心跨件 0），维持池内。

## 五、转换与基线进度

| 指标 | 值 |
| --- | --- |
| yuanwen 文件 | 2421（主条目 1873＋补充材料等） |
| I2 转换保真 | 1873 件，issue 0 |
| B3.1 往返不动点 | 1663／1873（失败 210；与旧基线集合零差，转好 0／转差 0） |
| B3.2 页面判定（旧池 judge） | pool 1780／gap 48／stale 45（叙述值，无落盘凭证；算术 1780＋48＋45＝1873 自洽）；与旧基线（pool 1851／gap 22／stale 0）比，转差 71 件、转池 0——全部为本轮 `en` 变化件的旧池失效，属预期 |
| B3.2 页面判定（`--build` 重建池后） | pool 1811／gap 62／stale 0（池 118 MB，占页 50.12%）；与旧基线（1851／22／0）比新增 gap 40、修复 0——新增族集中在本轮 `en` 变化件，待 053 线下批按四出口处置 |
| 补丁池 | 3 条（全部 `upstream-typo`） |
| 钉账资产 | main 1873／notes 683／supplement 467／script 458／image 1477（抓取后初为 1474，复核恢复 3 个旧图登记后回到 1477；`local.js` 补登 430 件） |

## 六、建账清单（`text` 类，65 件）

处置：走 specs/001 `compare.py` 产出变更文件 → 建 update 任务置空待译（ADR-0050/0068）。带正式修订标记的 10 件优先。清单按增删行数降序：

| 词条 | 文件 | 增删行 |
| --- | --- | --- |
| justice-retributive | index.html | 3725 |
| hume-moral | index.html | 2580 |
| plato-sophstate | index.html | 2098 |
| culture-cogsci | index.html | 1849 |
| gorampa | index.html | 1841 |
| logic-deontic | index.html | 1333 |
| embodied-cognition | index.html | 1000 |
| berlin | notes.html | 920 |
| rule-following | index.html | 899 |
| delusion | index.html | 858 |
| logic-deontic | notes.html | 822 |
| schopenhauer | index.html | 774 |
| autrecourt | index.html | 713 |
| meaning-holism | notes.html | 572 |
| ayn-rand | supplement.html | 417 |
| aristotle-psychology | active-mind.html | 275 |
| spencer | notes.html | 169 |
| ayn-rand | notes.html | 127 |
| history | index.html | 120 |
| aristotle-psychology | notes.html | 109 |
| ethics-ai | index.html | 97 |
| descartes | index.html | 95 |
| rule-following | notes.html | 94 |
| special-obligations | notes.html | 90 |
| plato-sophstate | notes.html | 65 |
| discrimination | index.html | 54 |
| justice-retributive | challenges.html | 43 |
| reasons-agent | notes.html | 36 |
| chinese-social-political | index.html | 20 |
| green | notes.html | 20 |
| logic-ancient | index.html | 20 |
| ayer | index.html | 18 |
| concepts | notes.html | 18 |
| feminist-bioethics | notes.html | 18 |
| reasons-internal-external | notes.html | 18 |
| shared-agency | notes.html | 18 |
| conscience | index.html | 16 |
| linguistics | whorfianism.html | 16 |
| organs-sale | index.html | 16 |
| progress | index.html | 16 |
| abortion | index.html | 14 |
| aristotle-psychology | method.html | 14 |
| dialectical-school | notes.html | 14 |
| epistemic-utility | char-ep-ut-cred.html | 14 |
| human-genome | index.html | 14 |
| informed-consent | index.html | 14 |
| neuroethics | index.html | 14 |
| phylogenetic-inference | index.html | 14 |
| phylogenetic-inference | notes.html | 14 |
| privacy | index.html | 14 |
| recursive-functions | ackermann-peter.html | 14 |
| recursive-functions | notes.html | 14 |
| cellular-automata | supplement.html | 12 |
| human-genome | notes.html | 12 |
| justep-intext | notes.html | 12 |
| logic-provability | notes.html | 12 |
| possibilism-actualism | index.html | 12 |
| publichealth-ethics | index.html | 12 |
| publichealth-ethics | notes.html | 12 |
| comte | index.html | 6 |
| self-knowledge | supplement.html | 4 |
| academic-freedom | notes.html | 2 |
| buber | index.html | 2 |
| cockburn | notes.html | 2 |
| it-moral-values | notes.html | 2 |

## 七、缺陷与修复（本阶段发现）

1. **`tools/fetch_all.py` 不可用**（2026-11-18 起）：`CONFIGS` 值已改为整数线程数，启动处仍按 `cfg[0]` 取数，直接 `TypeError`；worker 内 `_checkpoint(..., cfg)` 引用不存在的变量。已修，并加 4 项单测。
2. **`unchanged` 覆盖钉账**：`fetch_one` 的 unchanged 结果不含 `files`，原 worker 直接送 `upsert_baseline` 会把整条钉账替换成残记录（`files[].sha256` 丢失，ADR-0045 风险）。现改为不写盘、不动账、仍转换；`upsert_baseline` 增护栏拒收无 `files` 记录。
3. **2 件转换 `PermissionError`**：Windows 文件占用所致，补转成功；I2 复核归零。SOP 已写明“转换失败不阻塞抓取，须补转并复核 I2”。
4. **变化分类性能**：初版用 `difflib.SequenceMatcher` 对 80KB 可见文本，126 件超时；改为行级判据后 25 秒完成。

## 八、结论与后续

1. **上游确有新修订**：10 件 `substantive_revision`（11-21～24）＋55 件小幅文字变化；`text` 65 件构成建账面，其余 61 个磁盘变化文件（layout／rename-wave／binary／asset）不建账。
2. **补丁无需变动**：3 条全部有效，公共性 0，维持 `upstream-typo` 分类。
3. **转换保真未退化**：I2 1873/0；B3.1 集合零变化，说明上游换行重排与改名波纹未破坏装配闭合。
4. **下一步**：建账批次另立（按 specs/001 `compare.py` 逐件产出变更文件），本卡不建译任务；B3.2 池面刷新随本批提交。
5. **B3.2 新增 gap 40 件**：池重建后 pool 1811／gap 62／stale 0；相对旧基线新增 gap 40、修复 0。新增件全部来自本轮 `en` 变化（改名波纹的注释化链接、模板重排、正文修订），池规则无法吸收，清单见 `b32-new-gap.md`；待 053 线下批按四出口（勘误／补丁／转换器／例外）处置。属上游变化后的残差面重算，不是新缺陷。

## 九、收口复核（2026-11-25，独立复算）

证据：`phase12-review.md`。要点：

* 全部实质数字经独立复算成立（抓取 1873、账差 522、磁盘 126 文件／100 词条、分类 65／40／17／3／1、清单 65 件、I2 1873／0、B3.1 1663／210 集合零差、B3.2 新增 gap 40 修复 0 且 40 件全在变更集内）。
* 订正本文件两处口径：旧池 judge 标注“叙述值无凭证”；钉账资产改用抓取后口径（image 1474→1477、script 458）。
* SVG 归资产类结案（用户 2026-11-25 裁定：sha 变了随钉替换，不建账不过目）：`.svg` 并入 `binary`，`en_delta.py` 增 `--base REV` 复跑参数。
* 修复一处账实脱节：`logic-deontic` 重钉时 3 个旧图（`fig-box-b.svg`、`fig-square-b.svg`、`fig-vbox-a.svg`）被摘出 `files[]`，按 `registered_orphans` 口径恢复登记；`en_integrity --all` 硬发现由 4 降为 3（余项均既存）。
* 待落项：① 上游 2026-11-23 修订在 `aristotle-psychology/notes.html` 新引入双点错链 `index..html#ref-1`，按补丁 P-004 处置；② `en_integrity` 入门禁；③ `upsert_baseline` 改为并集保留。

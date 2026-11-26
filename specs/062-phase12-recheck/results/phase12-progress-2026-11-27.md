# 阶段 1.2 进度复核（2026-11-27，独立复算）

对象：阶段 1.2 收口（2026-11-25，提交 339c09dcf）及其后续处置项的当前完成度。方式：只读复算（现跑检查器、现读 JSON 与账），不采信报告自报值。工具探针 `script/tmp/check_12_tasks.py`（本地，不入库）。**复算补记（2026-11-27 晚）**：B3.1／B3.2 两项以全量独立重跑为准（`reassemble.py --all` 全库 1,873 件；`page_assemble.py --all` 全量 judge 复扫），不采信 05x 结果目录落盘值；下表现值即重跑值。

## 一、转换进度现值（对照 1.2 收口值）

| 指标 | 1.2 收口（11-25） | 现值（11-27 复算） | 演变 |
| --- | --- | --- | --- |
| I2 转换保真 | 1873 件，issue 0 | 1873 件，issue 0（复跑 `check_yuanwen_fidelity --gate`） | 持平 |
| 补丁池 | 3 条（P-001–003） | 5 条（P-001–005），strict 全绿 mismatch 0／admission 0／index 0／git 0／public 0 | +2（P-004 错链 11-25、P-005 结构错位 11-26） |
| B3.1 往返不动点 | 1663／210 | **1849／24**（全量重扫；失败集合与 `b31-attribution.json` 24 件同集，全为 bib-keys） | +186，0 转红 |
| B3.2 页面判定 | pool 1811／gap 62／stale 0 | **pool 1873／gap 0／stale 0**（全量 judge 独立复扫），池占页 52.17%（123,168,272／236,108,340 B） | gap 清零（053 第四十四～四十七批） |
| 钉账词条 | 1873 | 1873 | 持平 |
| 资产分类 | main 1873／supplement 467／notes 683／script 458／image 1477 | main 1873／supplement 468／notes 684／script 458／image 1477（`entries.json` files[] 现数） | +1／+1（saadya notes、aristotle-psychology suppl1 按 registered_orphans 补登） |
| yuanwen md | 2421 | 2421 | 持平 |

1.2 收口时点的“B3.2 新增 gap 40”已由 specs/053 第四十四～四十七批全部清零；B3.1 由 1663 → 1849（第五十至五十七批）。**剩余 24 件的定性已于 2026-11-27 重新取证并推翻旧结论**：旧记「bib-keys 24＝判据信息边界」不成立，主族实为书目区 `<dl class="sentag">` 的 `<dd>` 条目未进 `bib_entries`（C 第一遍发散文段、R 重建后第二遍建键，两遍键集不等；addams-jane 17 条、heidegger 107 条判例），第五十八批靶（`script/tmp/b31_keydiff.py` 键差普查）；另有 2 件续行小节首条的子族（watsuji-tetsuro／ibn-bajja）。

## 二、1.2 收口时的待落项

| 待落项 | 状态 | 凭证 |
| --- | --- | --- |
| ① aristotle-psychology 双点错链处置 | ✅ 已落地 | `baseline/en-patches/P-004.patch`（origin: upstream-typo，expect 1），入池且 strict 全绿 |
| ② `en_integrity` 入门禁 | ✅ 已落地 | `check_all --list-gates` 第 14 项 `en-integrity`（复算订正：原记第 15 项系误数） |
| ③ `upsert_baseline` 改并集保留 | ✅ 已落地 | `tools/fetch_entry.py:237-239` `merge_files(prev, rec)`，旧资产不再被整体替换摘钉 |
| ④ 补转自动重试、旧池 judge 凭证、B 族账本刷新（review R-5/R-6/R-8） | ✅ 已落地 | `phase12.py` convert_retry／`results/phase12-oldpool-judge.json`／SOP 步 6 `--rebuild-b3` |

## 三、建账批次进度（1.2 唯一未收口项）

1.2 建账清单 65 件 text（54 词条）的处置是“另批建账（compare.py 产出变更文件 → 建账置空待译，ADR-0050/0068）”。复算结果：**未执行**。

| 复算项 | 值 |
| --- | --- |
| text 行／词条 | 65／54 |
| compare 变更文件已产出 | 0（`specs/001-sep-sync-pipeline/compare/` 最新为 2026-11-20 批次，1.2 清单无对应文件） |
| 任务账 version_pin 仍旧钉（主文件 sha 已变而账未随钉） | 37 词条 |
| pin 恰与新钉一致 | 17 词条——其中 15 词条系 2026-11-25 账外补建（`wipe_missing_tasks.py`，建账时钉已新）、2 词条（cockburn／self-knowledge）变化仅在 notes／supplement 而主文件未变；**均非 1.2 建账动作** |

注意：version_pin 只在 `task_ops.create` 时写入（`tools/task_ops.py:188`），cleared 件上游修订后 pin 不自动前移；建账置空待译须走 compare 变更文件凭证的建账批次。10 件 `substantive_revision` 正式修订件（justice-retributive、hume-moral、plato-sophstate、culture-cogsci、gorampa、logic-deontic、delusion、embodied-cognition、rule-following、schopenhauer）在建账批次内优先——其中 plato-sophstate／logic-deontic／schopenhauer 恰为账外补建件（pin 已新），其余 7 件任务账仍旧钉。

## 四、结论

1. 阶段 1.2 本体（抓取→分类→补丁复核→进度→SOP→独立复核）闭环；收口时点的全部待落项已落地。
2. B3.2 新增 gap 40 已由 053 线全部收口；转换进度较 1.2 收口时点大幅演进（B3.1 +186、B3.2 gap 归零）。
3. **唯一未收口＝建账批次**：65 件 text／54 词条待建账置空待译（compare 变更文件未产出、37 词条任务账钉旧）。属独立批次工作，不在 1.2 卡内。

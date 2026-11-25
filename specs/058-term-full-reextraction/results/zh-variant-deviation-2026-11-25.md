# 登记形 vs 文本形偏离扫描（2026-11-25）

**目的**：登记册译法列常写「（亦作“X”）」。译文若通篇用 X 而不用主形，即为 D1 偏离（文本未采登记形）。本次把每个异形回中文语料计数，产出一张筛查表，供逐条回源研判——**不做机械替换**（规则禁止，且多数词各有语境）。

* 脚本：`bin/audit_zh_variants.py`
* 产物：`results/zh-variant-deviation-2026-11-25.tsv`（variant_count／main_count／key／main_zh／variant／top_files）
* 规模：带「亦作」的登记行 519；异形在语料中 ≥3 次者 187

## 一、读数须先定性的三类

1. **泛词假象**（多数）：`per se`（自身 2474）、`Causation`（因果 2267）、`nous`（理智 1553）、`presupposition`（前提 1288）——异形本身是常用词，计数含大量非术语用法，**不能据此判偏离**。
2. **真·术语双形并行**（学界两形皆通行，属 D2 而非错误）：`aesthetic experience` 审美经验 208／审美体验 228、`ontology` 本体论 1052／存在论 239、`intuition` 直观 734／直觉 1271、`Bedeutung` 意义 4228／意谓 452。
3. **真·文本未采登记形**（值得逐条回源看）：`schêma (Kant)` 主形图型 23／图式 411；`theōria` 静观 58／沉思 282；`construction` 构式 36／构造 817（构式是 construction grammar 的专形，泛用“构造”未必错）；`Bestimmung` 天职 6／规定 834；`explication` 阐释 151／阐明 441；`spread (intuitionism)` 展形 15／展开 559。

## 二、处置口径

* 类别 1、2 不动。
* 类别 3 逐条回 `en/`／`yuanwen/` 看原文用词与语境，再决定「改正文」还是「改登记形」；任何改动都走任务流程，不做批量替换。
* 本表只做筛查；`main_count` 与 `variant_count` 均含普通词用法，**判断前必须看 top_files 与原文句**。

## 三、附带发现

`Bedeutung` 行主形“意义”与 `significatio` 行异形“意谓”交叉，说明「意谓」一词在本库被两个德语／拉丁语行共用；这不是错误，但查重与译名统一时应留意三行（Bedeutung／significatio／meaning）的分工。

## 四、门禁

脚本只读语料与登记册，不写登记册；产物为 TSV，已入 `results/`。后续若把本扫描接进 `check_terms`，须先解决「泛词假象」的过滤（按词长与共现判别），否则误报会淹没真信号。

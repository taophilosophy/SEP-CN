# 收割批 6：中文语料频次审计（zh-corpus-audit）

* 日期：2026-11-25
* 手段：`specs/058-term-full-reextraction/bin/audit_zh_corpus.py`
* 输入：`tasks/term-pool.json`（status=new、type∈{term,phrase}、英文侧 freq≥35）∧ 登记册（`shu-yu-biao.md`＋`ren-ming-biao.md`，按 `norm_key` 排除已登记）
* 语料：`a/`–`z/` 全部中文译文，1880 文件、26 568 633 字节；Aho–Corasick 一次扫描，大小写不敏感，’→'
* 产物：`results/zh-corpus-audit-2026-11-25.tsv`（zh_count≥6，261 行）

候选 5474 个，命中 ≥6 的 261 行。判读口径与前五批一致：**先在中文侧看真用了多少**，再定性。

## 一、261 行定性

| 族 | 例 | 处置 |
| ---- | ---- | ---- |
| 书目／期刊串 | British Journal（402）、philosophical studies（296）、American philosophical（147）、collected works（90）、Complete Works（65）、Gesammelte Schriften、Philosophical Association、lecture notes、secondary literature | 噪声不登；唯 **secondary literature／primary source** 属文献学通名，本批登记（体例要用） |
| 人名残片（姓＋名分开出现） | van der（84）、van Inwagen（80）、van Benthem、van Dalen、von Wright、Dutilh Novaes、Van Norden、Pico della Mirandola、Anne Conway、Ibn Daud、Ibn Ezra、Frank Jackson、North Whitehead、Sanders Peirce | 逐一经人名表反查：全部已登记（人名表用姓先形 `Dalen, Dirk van` 等，故 `norm_key` 精确比对判为缺口＝假阳性） |
| 专名与论题短语 | Kant’s Theory、Aristotle’s Metaphysics、Concerning Human Understanding、Grundlagen der、contra gentiles、libero arbitrio、sur les、der Hoek | 题名残片，不登 |
| 泛词／时期语 | everyday life、late medieval、seventeenth century、contemporary debate、philosophical analysis、case study、modern period、applied mathematics、life sciences | 不登 |
| **真术语缺口** | 见下 | 登记 |

## 二、假阳性根因：合并键未被拆开

审计以整行键的 `norm_key` 比对，而登记册 2026-11-21 起流行「旧键并入」写法（`relevance logic`、`future contingent event / future contingents`、`moral sentiment`、`nonclassical logics`），并入形不在键串里就漏判。本批据此改用**按 `/` 拆形＋单复数变体**的二次筛查（242 行→真缺口 242 行，其中术语级 30 行），下列四形经核对已在册，不再重复登记：

* relevant logic → `relevance logic 相干逻辑`（旧键并入，行内已注明）
* future contingent（单数）→ `future contingent event / future contingents 未来偶然事件`
* moral sentiments（复数）→ `moral sentiment 道德情操`
* non-classical logics（带连字符）→ `nonclassical logics 非经典逻辑`

## 三、登记（30 行，`tasks/manifests/2026-11-25-058-batch58-terms.json`）

| 英文 | 主形 | 择形理由 |
| ---- | ---- | ---- |
| aesthetic appreciation | 审美欣赏 | 语料 41 次，无分流 |
| aesthetic properties | 审美属性 | 语料 78 次 |
| autonomous agent | 自主行动者 | 语料仅 3 次，取行动哲学与 AI 伦理通形 |
| communicative action | 交往行为（亦作“交往行动”） | 语料“交往行动”38／“交往行为”23，但书名《交往行为理论》已在册，主形从书名，异形体注内 |
| computing machine | 计算机器 | 图灵 1936 语境，语料 17 次，与“图灵机”分列 |
| conceptual change | 概念变化（亦作“概念转变”） | 语料 10／2，主形取多数 |
| constructive set theory | 构造集合论（亦作“构造性集合论”） | 语料作“构造集合论” |
| democratic theory | 民主理论 | 语料 17 次 |
| epistemic virtue | 认知德性 | 与 intellectual virtue 理智德性按域分列 |
| epsilon calculus | ε 演算 | 与 ε 记号（epsilon-notation）分列 |
| global governance | 全球治理 | 语料 5 次，学科通名 |
| intellectual history | 思想史 | 语料 80 次 |
| intellectual virtue | 理智德性 | 语料 11 次，与 moral virtue 对举 |
| language model | 语言模型 | 语料 15 次（＋大语言模型 10），池中无此键，故池不置 published |
| legal theory | 法律理论 | 语料 19 次 |
| literary work | 文学作品 | 语料 62 次 |
| mathematical object | 数学对象 | 语料 140 次 |
| mathematical structure | 数学结构 | 语料 23 次，与数学结构主义分列 |
| medical ethics | 医学伦理学（亦作“医学伦理”） | 学科全称作主形，语料短形作形体注内 |
| moral practice | 道德实践 | 语料 10 次 |
| natural beauty | 自然美 | 语料 37 次，与 artistic beauty 对举 |
| organ sale | 器官买卖 | 语料 49 次 |
| primary source | 原始文献（亦作“一手文献”） | 语料 49／3 |
| queer theory | 酷儿理论 | 语料 41 次 |
| research ethics | 研究伦理 | 语料 7 次，与医学伦理学分列 |
| scientific change | 科学变革（亦作“科学变迁”） | 语料各 1 次，取学科通形 |
| secondary literature | 二手文献 | 语料 93 次，文献节体例要用 |
| visual art | 视觉艺术 | 语料 21 次 |
| voluntary action | 自愿行为 | “意志行为”语料 17 次属 volition，不并 |
| Zeno’s paradox | 芝诺悖论 | 语料 11 次 |

落册：`term_flow` 干跑 30/0，实写 30；池 published=28；`check_terms` 硬错误 0（自洽 0）；告警 148 条（非英语术语缺原文，批前既有，未因本批增减）、人名缺项 781 条（既有待核账）。

## 四、联网检索凭证缺口

本会话内 bingweb 返 0 命中、duckduckgo／brave 连接超时（os error 10060）、exa 需重新授权、glm/deepseek 等无 API key，故 30 行的依据一律记为「学界通行译名（审定库无对口命中，2026-11-25）」，未写在线检索凭证。已核对**术语在线本地镜像**（`specs/008-terminology-campaign/results/queries/termonline-all`，24069 份）：30 词精确命中 0 条，仅 `relevant logic`（→相干逻辑，维基百科源）、`incompleteness theorem`（→哥德尔不完全性定理，自然辩证法名词 03.249）、`intrinsic property`（→内禀属性，物理学名词 09.1599）三条命中，而它们都已在册，本批不重复登记。通道恢复后须为「交往行为／概念变化／构造集合论」三处主形之争补在线凭证（存 D5 改判可能）。

## 五、遗留

1. 人名表 435 行译形仍为拉丁字母（ADR-0022「无通行汉名者保留英文」），其中 `Dalen, Dirk van`（语料 47 次）等高频者值得逐条查证是否已有通行汉名——需在线通道。
2. 合并键假阳性属审计工具的结构性偏差，`audit_zh_corpus.py` 下轮须改为拆 `/`＋单复数变体比对（本轮以一次性二次筛查代替）。
3. `van der`（84）、`Peter van`（13）一类跨词残片应加黑名单前缀过滤，否则每轮重复占据清单头部。

# q1 引文锁定判据表（cite_audit）

> 工序：`q1_cite_checked`，位次在 `s2.5_checked` 之后、`q2_logic_checked` 之前。
> 对象：译文全部引文——引块、行内引号引文、脚注引文、参考文献内的被引条目。
> 裁判：人审唯一裁决；机检只做完备性、字段完整性、守恒与形态核对。
> 依据：ISO 690:2021（引文数据保持原始语言与文字系统、关联信息 `[translit.: …]`／`[trans.: …]`、转写系统按 ISO 24229 登记）、GB/T 7714-2025 5.1（按信息资源本身语种著录）、ADR-0011（引文原文语言还原）、rules/07。

## 0 清单模型（cite-manifest.json）

每条引文一条记录，字段缺一即未完成：

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| `id` | string | `c-<slug>-<序号>`，全篇连续 |
| `loc` | string | 位置：`§2.B16`（节.段）或 `note-<key>` |
| `form` | enum | `block` 引块／`inline` 行内／`note` 脚注 |
| `lang` | string | BCP 47：`en`、`grc`、`la`、`de`、`fr`、`it`、`ar`、`fa`、`sa`、`bo`、`ja`、`zh`、`ru` |
| `original` | string | 该语言原文；英文原引文即 en 原文 |
| `english` | string | 英文翻译；en 引文填 `—` |
| `translator` | string | 英译来源：`published:<版本>`／`my`／`sep`（SEP 原文自带英译）／`—` |
| `register_system` | string | 转写系统代码：`iso-843`、`iso-233`、`iso-9`、`iso-3602`、`iast`、`wylie`、`pinyin-gbt16159`、`—` |
| `anchor` | string | 回溯锚点：`en/<slug>/index.html#<节>`、`[^key]`、书目键 |
| `hash` | string | `original`＋`english` 的 SHA-256 前 16 位 |
| `verdict` | enum | `pass`／`fail`／`waived`（豁免须写理由） |
| `reviewer` | string | 裁判标识；不得等于 draft actor |

## 1 判据

| 编号 | 判据 | 判定形态 | 标准依据 | 级别 | 处置 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| C-1 | 引文清单完备：文中每一处引文（引块、行内引号、脚注、参考文献被引条目）在清单有且仅有一条记录；清单条数与文中引文标记数一致 | 机检（标记抽取＋计数）＋人审补漏 | ISO 690:2021 引文可定位要求 | Critical | 缺条即 fail |
| C-2 | 字段完整：九字段齐全，`lang` 在允许集内，`form`／`verdict` 取值合法 | 机检 | 同上 | Critical | 缺字段即 fail |
| C-3 | 原文呈现：`lang≠en` 的引文，译文必须给出该语言的原文（引块内或脚注内）；确实无法可靠还原者，须有译注写明“原文未能还原，据英译转译” | 人审（逐条） | ADR-0011、ISO 690:2021 7.1.2.2 | Critical | 缺原文且无译注即 fail |
| C-4 | 英译呈现：`lang≠en` 的引文必须同时给出英文翻译，并注明来源（已刊译本／自译／SEP 原文自带）；中文译文据英文翻译转译，不得绕过英文直接自原文重译而不留痕 | 人审（逐条） | ISO 690:2021 关联信息；CMOS 11.12–11.14 同理 | Major | 缺英译或未注来源即 fail |
| C-5 | 转写规范：非拉丁文字按登记系统转写，`register_system` 与所用转写一致；不得混用两套转写（如梵语混用 IAST 与 Harvard-Kyoto） | 机检（字符域＋系统白名单）＋人审 | ISO 690:2021 引 ISO 24229 | Major | 混用即 fail |
| C-6 | 出处可回溯：`anchor` 指向的 en 源位置或书目键存在；禁止凭记忆补全引文、页码、年份 | 机检（锚点存在性）＋人审 | rules/07 禁幻觉引文 | Critical | 锚点不存在即 fail |
| C-7 | 引文守恒：`hash` 在 q2–q6 各出口核对，不得变动；引文内部文字与标点不得被语法、语域、计量、标点工序改动 | 机检 | 本建议书 §3.2 依赖 1 | Critical | hash 变动即硬失败 |
| C-8 | 中文／日文原典：中国典籍用通行中文原文与篇码（《论语》2.3、《孟子》6A.1）；日文引文用日文原文；不以英译回译 | 人审 | ADR-0011、rules/07 | Major | 以英译回译即 fail |

## 2 语种与转写对照（工具内置表）

| 语言 | 标签 | 转写系统 | 备注 |
| ---- | ---- | ---- | ---- |
| 古希腊语 | `grc` | `iso-843`（或学界惯用拉丁转写，须全篇统一） | 哲学条目高频；与 `el`（现代希腊语）区分 |
| 拉丁语 | `la` | 原文照录，不转写 | 保留 macron／ae 等 |
| 德语 | `de` | 原文照录 | 保留 ä ö ü ß |
| 法语 | `fr` | 原文照录 | 保留重音 |
| 意大利语 | `it` | 原文照录 | — |
| 阿拉伯语 | `ar` | `iso-233` | 须标转写系统 |
| 波斯语 | `fa` | `iso-233` 变体须注明 | — |
| 梵语 | `sa` | `iast` | 哲学／佛学条目高频 |
| 藏语 | `bo` | `wylie` | 与梵语区分 |
| 日语 | `ja` | `iso-3602` 或 Hepburn，二者择一 | 假名原文优先 |
| 汉语 | `zh` | `pinyin-gbt16159`（人名另按 GB/T 28039） | 典籍不转写，直接用汉字 |

## 3 引文块范式

非英语引文的标准形态（引块内）：

```
> “Il correttore di tipografia, piuttosto che curare che il libro a stampa
> riesca conforme al volere dell’autore, pensa a presentarlo con un aspetto
> grammaticale corretto e coerente.”
> （校订者并不操心印本是否合乎作者意愿，而是设法让它以语法正确、前后一致的面貌出现。）
> ——Migliorini & Baldelli 1984, 119，英译为本文作者所译。
```

要点：原文在前、英译在后（或反之，全篇统一）；括注英译；末注出处与译者；转写系统在 manifest 登记，不在正文堆叠标签（正文只在必要时给 `[转写：…]`）。

## 4 已知误报与豁免

| 情形 | 处理 |
| ---- | ---- |
| 英文引文内夹少量外语词（如 *das Man*） | 不作为独立引文条，随英文条登记 `lang=en`，括注即可 |
| 书名、术语原文斜体（*dharma*） | 不属引文，不入清单 |
| 参考文献照录条目 | 不入引文清单（书目另有 s1 与 check_academic 管辖），但其内部的非英语书名按 GB/T 7714-2025 5.1 保持原语种 |
| 译注中引述他人译法 | 入清单，`form=inline`，`translator` 记明出处 |

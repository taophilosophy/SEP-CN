# q1 引文锁定判据表（cite_audit）

> 工序：`q1_cite_checked`，位次在 `s2.5_checked` 之后、`q2_logic_checked` 之前。
> 对象：译文全部引文——引块、行内引号引文、脚注引文、参考文献内的被引条目。
> 裁判：人审唯一裁决；机检只做完备性、字段完整性、守恒与形态核对。
> 依据：ISO 690:2021（引文数据保持原始语言与文字系统、关联信息 `[translit.: …]`／`[trans.: …]`、转写系统按 ISO 24229 登记）、GB/T 7714-2025 5.1（按信息资源本身语种著录）、ADR-0011（引文原文语言还原）、rules/07。

## 0A 对象分层：引文级与术语级（不做分层则清单爆炸）

| 级 | 对象 | 量级（2026-11-25 摸底） | 归属 | 要求 |
| ---- | ---- | ---- | ---- | ---- |
| 一级 引文级 | 成句、成段的非英文引文（引块或行内引号内的整句） | 约 440 条候选／250＋词条 | q1 清单，逐条核销 | 原文＋英文双呈现（C-3、C-4） |
| 二级 术语级 | 单个或几个词的外语术语、人名、书名转写（多为期体或括注） | 约 1.28 万片段（含噪声）／700＋词条 | 术语轴 s2.4＋登记册 | 只要求首次出现括注原文与通行英译，不入引文清单 |
| 三级 书目级 | 参考文献条目内的非英文书名、期刊名 | 照录对象 | s1＋`check_academic` | 按 GB/T 7714-2025 5.1 保持原语种，不入引文清单 |

## 0B 上游现状（扫描凭证 `results/nonlatin-scan.json`）

| 语种 | 引文级候选 | 词条数 | 上游已给英文对译 | 未给 |
| ---- | ---- | ---- | ---- | ---- |
| 拉丁语 | 187 | 128 | 73（括注） | 114 |
| 德语 | 111 | 57 | 51（括注）＋2（明示） | 58 |
| 希腊语 | 78 | 37 | 25（括注）＋1（明示） | 52 |
| 法语 | 33 | 27 | 13 | 20 |
| 汉语／日文 | 26 | 10 | 14 | 12 |
| 意大利语／西班牙语 | 4 | 4 | 1 | 3 |

三条硬事实：

1. **上游自带的英文对译只占约 45%**，明示“my translation”一类全库仅 5 处——即“作者理解的英文”多数不在引号旁边，而在作者紧随引文的英文阐释段落里。
2. **形态不统一**：方括号 `[Concerning the Steppes and Deserts]` 与圆括号 `(multis modis)` 并存，中文译文须择一定为规范形（建议方括号，与圆括号承担语法插注分工）。
3. **重灾字头集中**：阿拉伯语—伊斯兰哲学（`ibn-gabirol` 21、`ikhwan-al-safa` 16）、德国哲学与美学（`aesthetics-18th-german` 14、`brentano` 14、`wilhelm-humboldt` 11）、印度与佛教（`kumaarila` 11、`twotruths-india`）、韩国与日本（`korean-philosophy` 13、`kyoto-school` 8）。阿拉伯语、梵语、藏语、日语的通行英译本远少于希腊拉丁德法，须单独立批。

## 0C “作者理解的英文翻译”的取得通道（C-4 的操作化）

用户要求引用非英文原文时给出“实际语言原文”与“作者理解的英文翻译”。关键问题：**作者的英文理解往往不写在引文旁，而写在其后的英文论述里**。因此按可核实的优先级取用，不得代作者编造英文：

| 通道 | `english_source` 取值 | 取得方法 | 证据要求 | 优先级 |
| ---- | ---- | ---- | ---- | ---- |
| 一 | `sep-inline` | SEP 原文引文旁已有英文对译 | 照录，记 anchor | 1 |
| 二 | `sep-paraphrase` | SEP 作者紧随引文的英文阐释句就是其理解；抽出该句并在 manifest 记 `anchor` 指向该句 | 必须逐字摘录作者原句，不得改写；中文译该句时不叠加解释 | 2 |
| 三 | `published` | 无作者英文理解，但该著作有通行英译本（如 Barnes 编《亚里士多德全集》、Cooper 编《柏拉图全集》、Cambridge 康德系列） | 查证到实书：书名、译者、版次、页码；禁凭记忆（rules/07 禁幻觉） | 3 |
| 四 | `editorial` | 前三者皆无，由本库给出英文转译 | manifest 标 `editorial`＋`to-verify`；中文侧译注声明“英文为本文译者所据原文转译，非 SEP 作者理解” | 4（末位） |

禁止形态：把 `editorial` 写成作者口吻；用模型生成英文而不标注；把通道三的通行译本冒充通道一或二。

## 0D 清单模型（cite-manifest.json）

每条引文一条记录，字段缺一即未完成：

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| `id` | string | `c-<slug>-<序号>`，全篇连续 |
| `loc` | string | 位置：`§2.B16`（节.段）或 `note-<key>` |
| `form` | enum | `block` 引块／`inline` 行内／`note` 脚注 |
| `lang` | string | BCP 47：`en`、`grc`、`la`、`de`、`fr`、`it`、`ar`、`fa`、`sa`、`bo`、`ja`、`zh`、`ru` |
| `original` | string | 该语言原文；英文原引文即 en 原文 |
| `english` | string | 英文翻译；en 引文填 `—` |
| `english_source` | enum | 取得通道：`sep-inline`／`sep-paraphrase`／`published`／`editorial`（见 0C）；en 引文填 `—` |
| `translator` | string | 英译责任：`sep`（作者自带）／`<译者名>`（通行译本）／`editorial`（本库转译）／`—` |
| `to_verify` | bool | `editorial` 通道置 `true`，进待核实清单 |
| `register_system` | string | 转写系统代码：`iso-843`、`iso-233`、`iso-9`、`iso-3602`、`iast`、`wylie`、`pinyin-gbt16159`、`—` |
| `anchor` | string | 回溯锚点：`en/<slug>/index.html#<节>`、`[^key]`、书目键 |
| `hash` | string | `original`＋`english` 的 SHA-256 前 16 位 |
| `verdict` | enum | `pass`／`fail`／`waived`（豁免须写理由） |
| `reviewer` | string | 裁判标识；不得等于 draft actor |

## 1 判据

| 编号 | 判据 | 判定形态 | 标准依据 | 级别 | 处置 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| C-1 | 引文清单完备：文中每一处引文（引块、行内引号、脚注、参考文献被引条目）在清单有且仅有一条记录；清单条数与文中引文标记数一致 | 机检（标记抽取＋计数）＋人审补漏 | ISO 690:2021 引文可定位要求 | Critical | 缺条即 fail |
| C-2 | 字段完整：十一字段齐全，`lang` 在允许集内，`form`／`verdict`／`english_source` 取值合法 | 机检 | 同上 | Critical | 缺字段即 fail |
| C-3 | 原文呈现：`lang≠en` 的成句引文（一级对象）必须给出该语言的原文（引块内或紧邻脚注）；确实无法可靠还原者，须有译注写明“原文未能还原，据英译转译”并标 `waived` | 人审（逐条） | ADR-0011、ISO 690:2021 7.1.2.2 | Critical | 缺原文且无译注即 fail |
| C-4 | 英文呈现：`lang≠en` 的成句引文必须给出英文，`english_source` 按 0C 四通道择一取值；通道二须逐字摘录作者英文阐释并记 anchor；通道四须标 `editorial`＋`to_verify` 并在译注声明；中文译文据英文转译，不得绕过英文直接自原文重译而不留痕 | 人审（逐条）＋机检（字段与取值） | ISO 690:2021 关联信息；CMOS 11.12–11.14 同理 | Critical | 缺英译、通道取值不实或未注来源即 fail |
| C-4b | 禁止冒充：`editorial` 英文不得写成作者口吻，不得使用未标注的模型生成英文，不得把通行译本标成 `sep-inline`／`sep-paraphrase` | 人审（抽查＋全量复核 `editorial` 项） | rules/07 禁幻觉引文 | Critical | 冒充即 Critical 一票否决 |
| C-4c | 术语级片段：二级对象只要求首次出现括注原文与通行英译，不入引文清单；同一术语全篇同形 | 机检（首现定位）＋人审 | ISO 704、rules/03 | Minor | 未括注即告警 |
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

## 3 承载分档与范式

三层内容（中文译文、原文、英文）不叠在一处，按引文长度分三档承载。全篇同一档内形态必须一致。

### 3.1 分档

| 档 | 判据 | 承载 | 例 |
| ---- | ---- | ---- | ---- |
| A 短语级 | 原文 ≤25 字、一个短语或短句 | 正文中文＋紧随括注原文＋方括号英译 | 作者说，校订者“只是设法让它以语法正确、前后一致的面貌出现”（“pensa a presentarlo con un aspetto grammaticale corretto e coerente”［takes care to present it correctly and consistently from a grammatical point of view］）。 |
| B 整句级 | 1–3 句 | 引块＝原文；块内末行方括号英译；中文译文置于引块前的引出句或引块后独立成段 | 见 3.2 |
| C 长段级 | >3 句 | 引块＝原文；英译入紧邻脚注；正文给中文译述＋关键句直译，脚注给英译全文 | 正文：“……作者在此把校订者的工作概括为语法层面的整齐化。”脚注：原文英译全文＋出处 |

### 3.2 范式（B 档）

```
> “Il correttore di tipografia, piuttosto che curare che il libro a stampa
> riesca conforme al volere dell’autore, pensa a presentarlo con un aspetto
> grammaticale corretto e coerente.”
> [The proofreader, rather than ensuring that the printed book complies with
> the author’s intent, takes care to present it as grammatically correct and
> consistent.]
> ——Migliorini & Baldelli 1984, 119；英译为本文作者所译。

中文译文另起一段：校订者并不操心印本是否合乎作者意愿，而是设法让它以语法正确、前后一致的面貌出现。
```

### 3.3 形态约定

* 英译统一用方括号 `[…]`；圆括号留给语法性插注与中文行文（ISO 690:2021 的关联信息亦用方括号）。
* 原文语言标记不写在正文（`lang` 在 manifest），仅当读者可能误判语种时于脚注首句点明（“原文为意大利语”）。
* 转写系统不堆在正文；需要时写 `[转写：…]`，系统代码登记在 manifest。
* 出处与译者注记：`——作者 年份, 页码；英译为……`；通道二写“英文据作者下文表述”，通道四写“英文为本文译者所据原文转译，非作者理解”。
* 中文译文不得只译英文而隐去原文的修辞特征（双关、韵律）；无法保留时用译注说明，不静默抹平。

## 4 已知误报与豁免

| 情形 | 处理 |
| ---- | ---- |
| 英文引文内夹少量外语词（如 *das Man*） | 不作为独立引文条，随英文条登记 `lang=en`，括注即可 |
| 书名、术语原文斜体（*dharma*、*Einfühlung*、al-Rāzī） | 二级对象，不入引文清单；按 C-4c 首现括注 |
| 参考文献照录条目 | 不入引文清单（书目另有 s1 与 check_academic 管辖），但其内部的非英语书名按 GB/T 7714-2025 5.1 保持原语种 |
| 译注中引述他人译法 | 入清单，`form=inline`，`translator` 记明出处 |
| 数学公式中的希腊字母、逻辑符号 | 不属引文；按 check_math 与 ADR-0049 处理 |

## 5 批次与成本

按语种可取得性分四批，不按字头：字头法会把同一语种的查证工作打散，无法复用译本资源。

| 批 | 语种／主题 | 代表词条 | 通道预期 | 备注 |
| ---- | ---- | ---- | ---- | ---- |
| B1 | 希腊语、拉丁语、德语、法语 | `aesthetics-18th-german`、`brentano`、`henry-ghent`、`diderot` | 通道二＋三为主 | 通行英译本充足，先做此批以校准口径 |
| B2 | 阿拉伯语、波斯语、希伯来语 | `ibn-gabirol`（21）、`ikhwan-al-safa`（16）、`abu-bakr-al-razi` | 通道二为主，通道四比例高 | 英译本稀缺，`editorial` 与 `to_verify` 会集中出现 |
| B3 | 梵语、藏语、巴利语 | `kumaarila`（11）、`twotruths-india`、`twotruths-tibet` | 通道二＋三 | 依 IAST／Wylie 转写；佛学条目须与术语轴联动 |
| B4 | 汉语、日语、韩语 | `korean-philosophy`（13）、`kyoto-school`（8） | 通道一＋二为主 | 汉字原文优先，拼音按 GB/T 16159／GB/T 28039 |

成本量级：一级对象约 440 条，每条查证与 manifest 登记 30–50 分钟，约 220–370 人时；加口径校准、四通道判定复核与待核实清单管理，约 300–450 人时。成本集中在 B2／B3 的通道四判定，须逐条留证。

质量指标：① `sep-inline`／`sep-paraphrase` 合计占比应 ≥50%（说明多数可从上游取得）；② 单件 `editorial` 超过 30% 即触发复核，判断是上游确实未给理解，还是我们漏读了作者阐释；③ `to_verify` 清单须在 r2 前清零或逐条说明。

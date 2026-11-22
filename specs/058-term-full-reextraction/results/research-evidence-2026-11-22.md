# 调研凭证：类似项目的术语提取与词表建设做法（2026-11-22）

> 用途：specs/058 的方法论依据。所有条目均于 2026-11-22 经代理（192.168.5.4:7890）实抓或经 OpenAlex／Wikipedia API 取得；失败的通道如实记录，不以推测代替。

## 1. 术语抽取的通用方法

**来源**：Wikipedia, “Terminology extraction”（https://en.wikipedia.org/wiki/Terminology_extraction，2026-11-22 经 API 获取）。
**要点**：术语抽取是信息抽取的子任务；方法分统计式、语言学式、混合式三类。统计式以词频、共现、术语度（termhood）为核心；语言学式利用词性、句法模式与词典；混合式结合两者。输出通常还需人工验证。

**来源**：Frantzi, K. & Ananiadou, S. 的 C-value／NC-value 方法谱系；OpenAlex 检索 “bilingual terminology extraction” 命中（2026-11-22）：
- Gaussier, E. (2001) *General considerations on bilingual terminology extraction*（DOI 10.1075/nlp.2.09gau，被引 88）。
- Macken, L. et al. (2013) *TExSIS: Bilingual terminology extraction from parallel corpora using chunk-based alignment*（DOI 10.1075/term.19.1.01mac，被引 84）。
- *Bilingual terminology extraction using multi-level termhood*（2012，DOI 10.1108/02640471211221395）。
- *Bilingual Terminology Extraction in Sketch Engine*（2015）。
**采纳**：本项目为单语原文＋人工译名登记，无平行语料，故取“termhood ＋ 来源广度 ＋ 嵌套抑制”的统计路线，辅以定义语境与词形规则；不采用对齐式双语抽取。

## 2. 词表的数据模型与交换格式

**来源**：Wikipedia, “TermBase eXchange”（https://en.wikipedia.org/wiki/TermBase_eXchange，2026-11-22）。
**要点**：TBX 是 ISO 30042:2019 术语数据交换标准，面向概念（concept-oriented），一个概念一条记录，可承载术语、词性、定义、语境、来源、状态等字段；同义词与多语种译名挂在同一概念下。

**来源**：Wikipedia, “Universal Terminology eXchange”（https://en.wikipedia.org/wiki/Universal_Terminology_eXchange，2026-11-22）。
**要点**：UTX 由 AAMT 制定，最小字段为源语言词条、目标语言词条、词性，用于机器翻译词表的快速交换。

**来源**：Wikipedia, “TermBase eXchange” 条目对 IATE 的说明（同上）。
**要点**：IATE 为欧盟机构间术语库，支持多语种、来源标注与校验流程。

**采纳**：
1. 一行一概念，同形不同义分行（与本仓库 `rules/03` 的“同形不同义分行”一致）。
2. 登记行保留“依据＋日期”（等价于 TBX 的 source/status 字段）。
3. 由于本项目登记册是 GitBook Markdown 表格，不引入 TBX/UTX 文件格式；但把其字段语义映射为：键｜原文｜译法｜首现｜依据｜裁定日期（术语），原文｜别名｜译法｜籍属｜生卒｜首现｜依据｜裁定日期（人名）。
4. 长词条（句级）登记为 `sentence` 型候选，不强行塞进术语行；只有确属固定译名的格言式表达才入册。

## 3. 类似翻译项目的组织方式

**来源**：Wikipedia, “Stanford Encyclopedia of Philosophy”（https://en.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy，2026-11-22）。
**要点**：SEP 由专家撰写、同行评审、持续修订；同一主题允许并存竞争性条目，因此术语用法存在条目间差异，不能假设全库完全统一。

**来源**：SEP 主站（https://plato.stanford.edu/，2026-11-22）与单篇页面（https://plato.stanford.edu/entries/abduction/）。**限制**：站内未检索到官方翻译项目页面（`/translations*` 均 404），故不以 SEP 官方翻译页作为方法依据；改以通用术语工程实践为准。此项为通道事实，不作推断。

**来源**：Bing／DuckDuckGo／Brave／Mojeek／百度检索（2026-11-22）均被反爬拦截（空壳、202 挑战或连接拒绝），未取得第三方中文 SEP 项目的可核验页面，故不引用此类内容。

**采纳**：
1. 逐篇提取而非全库一把抓，保留来源篇目，承认条目间术语差异。
2. 来源广度作为置信信号：多篇共现的概念优先登记；单篇孤例降档留池。
3. 不把“全库统一”当作硬目标；同形不同义按条目语境分行，沿用 ADR-0013 的撞形豁免。

## 4. 中文权威依据通道

**来源**：本仓库 `rules/03-terminology.md`、ADR-0012、ADR-0074；`tools/cnki_query.py`、`tools/termonline_token.py`。
**要点**：译名依据优先级为审定名词库（术语在线，2026-11-18 解禁重抓）→ 权威译本与学术出版通行译法 → 学界惯例；禁止维基百科；CNKI 翻译助手不新增查询。

**采纳**：登记批次先查术语在线（GB 标准库与审定名词库），命中者依据列写“审定名词库（…）；凭证 日期”；未命中且学界通行者写“学界通行（…）；凭证 日期”；无通行译名者保留英文原名。

## 5. 方法结论（写入 spec 的规则）

1. 提取：多路线＋术语性守卫＋折叠键去重＋来源广度。
2. 排序：按词首字母 A–Z，非拉丁与数字归 `#` 节；节内按折叠键排序。
3. 状态机：`new → published@日期 | held:理由 | rejected:理由`，沿用 specs/008 先例。
4. 登记：一行一概念；同形不同义分行；每条依据可回溯到来源＋日期。
5. 规模控制：全量入总表，分档登记；不把未裁定的低频长尾固化为登记行。

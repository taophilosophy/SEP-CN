# 词汇表复核报告（2026-10-27）

对 `qian-yan/ci-hui-biao.md` 词汇表的真实性与有效性做了全面复核：共修正 46 处，联网核查 24 项，并新增本地检查工具 `script/glossary_lint.py`。修正已随提交 d4f13ed4 入库；本报告记录方法、依据与遗留事项。配套文档见 [正反误用手册](zheng-fan-wu-yong-shou-ce.md) 与 [翻译工程方法](gong-cheng-fang-fa.md)。

## 结论摘要

* **真实性**：原表存在 22 处误译，其中 12 处属“正反误用”或张冠李戴级硬伤（如 Argument 译“悖论”、Philoponus 误挂 Philolaus 的汉译“菲洛劳斯”、Absolute idealism 译“新黑格尔主义”），全部按权威来源纠正并补备注。
* **有效性**：原表存在 8 处坏行（标题拆断、键残缺、尾逗号、异体字）、4 组完全重复行、多组键值冲突与中文碰撞。修正后 lint 0 问题；确属同指异名的 9 组碰撞与 3 组同键异译编入 lint 白名单留档。
* **增补**：从 git 提交信息挖掘出 5 条既有裁定（Chancellor 总务长、Philip the Chancellor 总务长菲利普、Constitution 构成、Nominalism 唯名论、anomalous monism 变异一元论）补录入表；持续任务登记于 `tasks/ci-hui-biao.json`。
* **避免的误改**：两处原表译名经核查后维持原状——“词项属性”（全国社科工作办 2024 年文章用“词项属性理论”）、“堆垛悖论”（华文哲学百科与中文维基均立此名）。

## 修正清单（按缺陷类型）

### 一、误译纠正（真实性缺陷）

| 英语 | 原译（废弃） | 新译 | 依据 |
| ---- | ---- | ---- | ---- |
| Argument | 悖论 | 论证 | 悖论是 paradox；argument 是论证。日常词“argument=争论”的正反误用 |
| Absolute idealism | 新黑格尔主义 | 绝对唯心论 | 黑格尔自称 absoluter Idealismus；新黑格尔主义（Neo-Hegelianism）指英国后继思潮 |
| Philoponus | 菲洛劳斯 | 斐洛波努斯 | 与 Philolaus（菲洛劳斯，毕达哥拉斯学派）同名混淆；中文维基作“费罗普勒斯” |
| Myths | 秘所思 | 神话 | “秘所思”系讹译 |
| thin | 瘦 | 薄（的） | 威廉姆斯厚/薄概念（thick/thin concepts） |
| development / biological development | 演化 | 发展；发育 | evolution 才是“演化”；生物学 development=发育 |
| Structural Realism | 结构现实主义 | 结构实在论 | 科学哲学通行译名；“结构现实主义”是国际关系理论（沃尔兹）译名 |
| Territorial Rights | 领土主权 | 领土权利 | rights=权利；领土主权是 territorial sovereignty |
| Territorial Justice | 领地正义 | 领土正义 | “领地”指庄园、领主领地 |
| general idea | 概述 | 一般观念 | 洛克、贝克莱语境；“概述”是日常义 |
| Ethics | 道德 | 伦理学 | 学科名与书名；《模糊性的道德》书名内随书名译“道德” |
| Warrant | 担保 | 保证 | 普兰丁格概念，中文学界通行“保证”（孙清海《哲学分析》2015 等） |
| Boolean algebra | 逻辑代数 | 布尔代数 | 与 Boole 布尔行保持一致；“逻辑代数”为旧称 |
| bald | 秃子 | 秃头 | 堆垛悖论标准示例谓词 |
| agent / agency | 行为体 | 行动者 / 能动性 | 伦理学与行动理论标准译名；“行为体”是国际关系术语 |
| awareness | 意识 | 觉知；觉察 | 与 consciousness（意识）相区别 |
| accommodation | 解释 | 顺应；调节 | 按语境：科学哲学指理论迁就既有数据 |
| constructive | 建构主义／构造主义 | 构造性的 | constructivism 才是名词“构造主义” |
| pragmatic theory | 实用主义 | 语用（的）；实用（的） | pragmatism 才是“实用主义” |
| Pragmatist | 实用主义 | 实用主义者 | 名词指人 |
| Alfred North Whitehead | 阿弗烈·诺夫·怀特海 | 阿尔弗雷德·诺思·怀特海 | 国家图书馆规范标目、中文维基均如此 |
| Diodorus Cronus | 卡里亚雅苏斯的狄奥多罗斯 | 狄奥多罗斯·克罗诺斯 | Cronus 是承自其师的绰号（“老顽固”），非地名；其出生地为卡里亚的雅索斯 |

### 二、坏行与格式修复（有效性缺陷）

| 问题 | 修复 |
| ---- | ---- |
| `Adieux: A Farewell\|Sartre to 告别的仪式`（标题拆断） | Adieux: A Farewell to Sartre｜告别的仪式（上海译文 2019，孙凯译） |
| `She Came\|Stay to 女宾`（标题拆断） | She Came to Stay｜女宾（上海译文，周以光译） |
| `Will\|Believe to 信念意志`（标题拆断） | The Will to Believe｜信仰的意志（通行中译；作概念短语亦译“信念的意志”） |
| `3rd Earl of\|第三代`（键残缺） | 3rd Earl of Shaftesbury｜第三代沙夫茨伯里伯爵 |
| `Shaftesbury Lord\|沙夫茨伯里伯爵`（键倒序） | Lord Shaftesbury｜沙夫茨伯里勋爵 |
| `Henry David Thoreau\|亨利·戴维·梭罗,`（尾逗号） | 去除标点 |
| `‘Abd al-Latif’`（带引号重复键） | 删除，并入 Abd al-Latif 行 |
| `Alexander of Aphrosias`（英文键拼写错误） | Alexander of Aphrodisias｜阿佛洛狄西亚的亚历山大 |
| 阿毘达磨（异体字“毘”） | 阿毗达磨 |

### 三、重复与冲突归并

* `Account|解释/原理`、`Account|解释/原理/理论`、`accounts|解释/原理/理论` 三行归并为一行（解释；说明；原理，按语境取义）。
* `constructive` 两行（建构主义／构造主义）归并为“构造性的”。
* `commentators`、`Pluralism` 大小写完全重复行各删一行。
* `Ammonius` 同键两译名保留（两名同名哲学家：赫尔米亚的阿莫尼俄斯即 Ammonius Hermiae；另一行为泛指，含 Ammonius Saccas）。
* `empirical` 两译（实证／经验的）保留：形容词与名词分工，且“实证”行引有专文出处（汤茂林、黄展，《地理研究》2020）。
* `Justification` 两译（证成／辩护）保留：当代知识论与传统语境并行的两种通行译法。

### 四、备注补源（可追溯性）

为 15 条通行译名补写来源备注，包括：堆垛悖论（又称连锁悖论、谷堆悖论、累积悖论）、Properties of Terms 词项属性（proprietates terminorum，含意谓、指代、联结、称呼、扩张、限制）、haecceity 此性（司各脱 haecceitas）、bundle theory 束理论（亦译捆束理论、丛束理论）、contractarianism／contractualism（自利契约论／非自利契约论，霍布斯线与康德—斯坎伦线）、akrasia 不能自制（廖申白译本）、Kalām 凯拉姆、Falsafa、Ḥikmah、Albertus Magnus 与大阿尔伯特同人异译、Theophrastus 异译等。

## 联网核查来源（24 项核查的主要出处）

* 中文维基百科：约翰·费罗普勒斯、艾尔伯图斯·麦格努斯、阿佛洛狄西亚的亚历山大、绝对唯心主义、阿尔弗雷德·诺思·怀特海、连锁悖论、共相问题、精诚兄弟会典、泰奥弗拉斯托斯、含糊
* SEP 词条：philoponus、diodorus-cronus、sorites-paradox、universals-medieval、medieval-terms、contractarianism、contractualism、ikhwan-al-safa、types-tokens、sortals、medieval-haecceity、alexander-aphrodisias
* IEP：Proper Functionalism（普兰丁格 warrant）
* 孙清海《论普兰丁格的“保证”思想》（《哲学分析》2015 年第 1 期）；《普兰丁格的“保证”学说与当代儒学创新》（《中山大学学报》2016 年第 3 期）
* 全国哲学社会科学工作办公室《中世纪逻辑及其现代性》（2024，用“词项属性理论”）
* 哲学中国网：张华夏《科学实在论和结构实在论》、魏洪钟《结构实在论中的实体之争》（结构实在论）
* 华文哲学百科《堆垛悖論》；长沙理工大学《含糊性及累积悖论研究》
* 《亚里士多德论 akrasia》（贵州师范学院学报 2015，akrasia 即“不能自制”）
* 豆瓣：告别的仪式（上海译文 2019）、女宾（上海译文）；西蒙娜·德·波伏瓦系列页
* 译言古登堡计划《信仰的意志》（The Will to Believe 中译）

## 有效性检查工具与白名单

`python script/glossary_lint.py`：检查重复键冲突、中文碰撞、坏行（标题拆断、键残缺倒序、尾标点、带引号键、异体字、未翻译行），当前 571 行数据 0 问题。已裁定例外编入脚本白名单（同指异名 9 组、同键异译 3 组），例外调整须先在复核报告中记录理由。

## 裁定沿革

* **Token**：2024-05-11 提交 43ea5ea2 裁定“令牌→个体”；2026-10-27 复核改裁“殊例”——“个体”与 Individual(s) 的中文碰撞正是原表有效性缺陷的根源之一。沿革只记此处，不进发布表。
* **Theophrastus**：登记簿（alcmaeon 词条）裁“特奥弗拉斯托斯”，词汇表作“泰奥弗拉斯特”，两者均为通行异译；发布表备注已注明，登记簿裁定在其词条范围内优先。

## 遗留事项与待办

持续任务“从 git 提交信息增补修订词汇表”登记于 `tasks/ci-hui-biao.json`，含：①找回 2024 年 13 条“词汇表”提交在 bb2793a0 标准化合并中可能丢失的行；②14 条全文型提交（信息即整篇旧译文）按词条回收术语；③登记簿与发布表的双向同步机制；④裁定沿革留痕。

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
| Aspect | 体态 | 体（体貌） | 语言学范畴，与 tense（时态）相对；“体态”易与 posture 混 |
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

`python script/glossary_lint.py`（v2）：检查重复键冲突、中文碰撞、坏行（标题拆断、键残缺倒序、尾标点、带引号键、异体字、未翻译行）与登记簿同步缺口，当前 594 行数据 0 问题。已裁定例外编入脚本白名单（同指异名 8 组、转写折叠变体 1 组、同键异译 3 组），例外调整须先在复核报告中记录理由。

## v2 复核强化与极端情况兼容（2026-10-27 第二轮）

检查工具升级至 v2，新覆盖的极端情况：utf-8 BOM 与 CRLF 换行；围栏代码块内的管道行；单元格内转义竖线 `\|` 的正确切分；表头与分隔行不计数；Unicode NFC 归一化与变音折叠（去附加符号、撇号变体归一），据以捕获近似重复键——如 Al-Fârâbî／al-Farabi 折叠后同为 alfarabi；隐形字符（零宽字符、软连字符、NBSP）、HTML 实体残留、全角字母数字、数据行列数与空键空值。

v2 首轮即抓出两处“报告已记、执行漏改”的行（Argument、Aspect——第一轮复核报告中列出但编辑未落地，本报告自身也被纳入复核），已补正；另暴露并修复了 v1 的分隔行误计与 `strip("|")` 吞空列两个工具缺陷。

新增**登记簿↔发布表同步检查**：登记簿 yi-zhe-shuo-ming.md 的全部裁定按 `/` 与 or 拆分后与发布表折叠键比对。本次暴露 26 条“已裁定未发布”缺口（阿尔克迈翁条 10 个希腊文术语、Token／type 的 type 侧、13 位希腊古典人名），已全部按登记簿译法发布，发布表现为 594 行。

## 别名与重名约定

针对人名、术语的别名与重名问题，按四类处置（工具规则与白名单已固化）：

* 同指异名（拼写变体 Burleigh/Burley、缩写 QFT/Quantum Field Theory、跨语同义 Wisdom/Ḥikmah、单复数 type/Types、Token/Tokens）→ 白名单放行，备注交叉指引；
* 同键多指（两名 Ammonius）→ 分行并列，备注注明各自所指；
* 同姓异人 → 泛指/简称行必须带消歧备注（lint 观照名单：albert、more、samuel、cohen、wilson、williams、sturm、bell、ammonius），已为 7 个裸姓氏行补写消歧注，如 Albert 行指向大阿尔伯特与萨克森的阿尔伯特两条专条；贝尔定理的 John Stewart Bell 与逻辑学家 John L. Bell 亦在册；
* 术语别名 → 备注记“又称”（堆垛悖论又称连锁悖论、谷堆悖论、累积悖论）。

## 学术规范专项走查（2026-10-27 第五轮）

按标准 v1.0 与正反误用手册的规范条目（R1 译名有据／R2 依据留痕／R3 键规范／R4 一致性／R5 人名体例／R6 书名出版译名／R7 正反误用／R8 格式）对 706 行再次全量走查。先经程序化漂移核对：他会话整表重写（目录重组连带）零译名值漂移，唯一变化为其按登记册对齐 Theophrastus→特奥弗拉斯托斯（合法归一）。人工走查修正 11 处一致性/字符问题：

* **人名通译统一**：Alfred Tarski 阿尔弗莱德→阿尔弗雷德·塔尔斯基；Francis Hutcheson 弗兰西斯→弗朗西斯·哈奇森（与 Francis Bacon 一致）；Franz Brentano 弗朗兹→弗朗茨·布伦塔诺；Anicius Manlius Severinus Boethius 全名“亚尼修·玛理乌斯·塞味利诺”非标准形→“阿尼修斯·曼利乌斯·塞维利努斯·波爱修斯”。
* **Beauvoir 全表统一**：波伏娃→波伏瓦（上海译文及学界通行形），含 Simone de Beauvoir 行；备注注明“亦作波伏娃”。
* **字符规范**：François-Marie d'Arouet 行分隔符“‧”（U+2027）误植→间隔号“·”。
* **译法变体分隔统一**：Conventionality、Simultaneity、property 三行的半宽斜杠→分号（与他行“；”风格一致）。
* **备注润色**：Peter Abelard 行措辞理顺。

会话间漂移说明：并行会话将旧版 guan-yu 页面迁入 `pending/` 目录重整，check_all 豁免清单随之更新（guan-yu 之外加 pending 目录）；期间他会话还按登记册对齐了 Theophrastus 译名并自行补充 4 条术语（856b7d21），双通道流程运转正常。

## 去重合并规则 v3（2026-10-27 第四轮）

词汇表规模达 707 行后，原有折叠去重不足以覆盖变体形态，glossary_lint 升级 v3，新增三层检测：**强折叠层**（fold2：属格 's 残留、英式/美式拼写、-isation 类后缀归一，白名单 FOLD2_SAME_OK 承接 bell theorem、skepticism、单复数等有意变体）、**词序倒置**（词多重集相同且折叠键不同才报）、**词缀包含一致性**（token 序列包含的行对，被包含键 ≥2 词，译名按斜杠分项后互不为子串且双方无消歧备注才报）。

首跑 22 条发现，三分处置：18 条为规则精化排除（Theory/Truth 类单 token 泛词的包含误报、斜杠别译的子串误报）；4 条真发现以**消歧备注/语境分流注**处置——Benjamin（本雅明 vs 本杰明·惠科特，入重名观照名单）、Continuum Hypothesis（连续统固定搭配 vs 泛指连续体）、identity theory（同一论 vs Identity 同一性）、Academic Skepticism（怀疑主义/怀疑论两译并存）。原则重申：**译名合并永远由人逐条裁定，工具只提示**。另修 Ralp Cudworth 键拼写笔误。

同期他会话上线 `tools/check_terms.py`（specs/002，CI 侧译法集合比对门禁），与本工具形成双门禁分工：其强在中文译法集合与登记册自洽，本工具强在英文键归一与结构检查；协作中发现并修复登记簿人名表缺裁定日期列（17 行补 2026-10-26）、Constitution 行括注破坏其解析器（重组为前置变体）两处接口问题。双门禁现均 0 告警。

## 全局逐个复核（2026-10-27 第三轮）

对 594 行逐行遍历（非仅 lint 报警行），每一行核对译名通行度、语境分流与书名出处，另对 5 个书名联网核查。结果：

* **真错误 2 处**：Sociobiology 旧译“生物社会学”系语序倒置，正为“社会生物学”；Latin West 由“西方拉丁世界”改为通行的“拉丁西方”。
* **书名联网核查 5 项**：Coming of Age 简中版为《老年》（上海译文 2025，孟玉秋译；台版《论老年》）；A Week on the Concord and Merrimack Rivers 通行中译《河上一周》（商务涵芬书坊、果麦；商务 2025 新译《两河一周》）；Noces《婚礼集》确认（郭宏安译本）；Djamila Boupacha 中文媒体通行“布帕查”（亦作“波巴查”），原表“布巴夏”罕用；Pyrrhus et Cinéas 无简中出版译本，补注说明。
* **备注补强 14 条**：Understanding（康德 Verstand 定译“知性”）、Rationality（合理性）、Representation（Vorstellung 语境译“表象”）、Truthlikeness（亦译“逼真性”）、vagueness（亦译“含糊”）、square of opposition（又称“对当方阵”）、Thrasymachus（商务译本作“色拉叙马霍斯”）、Timon（亦作“蒂蒙”）、al-Kindi（亦译“金迪”）、Hole Argument（亦译“空洞论证”）、Quantum-Bayesian（QBism 量子贝叶斯主义）、Underdetermination（亦译“不充分决定性”）、transcendentalism（指美国运动，康德语境译“先验”）、Bohmian（玻姆力学）。

此后词汇表进入稳态：新增术语一律走“登记→发布→复核”三步，本表仅在新词条翻译时增量维护。

## 裁定沿革

* **Token**：2024-05-11 提交 43ea5ea2 裁定“令牌→个体”；2026-10-27 复核改裁“殊例”——“个体”与 Individual(s) 的中文碰撞正是原表有效性缺陷的根源之一。沿革只记此处，不进发布表。
* **Theophrastus**：登记簿（alcmaeon 词条）裁“特奥弗拉斯托斯”，词汇表作“泰奥弗拉斯特”，两者均为通行异译；发布表备注已注明，登记簿裁定在其词条范围内优先。

## 遗留事项与待办

持续任务“从 git 提交信息增补修订词汇表”登记于 `tasks/ci-hui-biao.json`，含：①找回 2024 年 13 条“词汇表”提交在 bb2793a0 标准化合并中可能丢失的行；②14 条全文型提交（信息即整篇旧译文）按词条回收术语；③登记簿与发布表的双向同步机制；④裁定沿革留痕。

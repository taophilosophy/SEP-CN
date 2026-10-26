# SEP 分类目录核查建议书

**核查对象**：`mu-lu-s.md`（SEP 分类目录）与 `SUMMARY.md`（字母序总目录）
**核查日期**：2026-10-26
**官方比对基准**：https://plato.stanford.edu/contents.html （2026-10-26 抓取，主条目 1872 条、别名 654 条），以及核查中逐条抓取的官方条目页（plato.stanford.edu/entries/…）

## 核查方法（三轮复核）

1. **第一轮（逐条普查）**：将 `mu-lu-s.md` 全部 1817 条词条按 16 个哲学分区拆分，逐一核对【分类归属】与【中文标题翻译】。分类判断以官方条目页导言、人物生卒与学派为据；译名以通行汉译（中文维基百科、华文哲学百科、已出版中译本、术语数据库）为据。共报告约 355 项问题。
2. **第二轮（换源复核）**：由 4 个独立复核组分别对"分类""译名""结构/元数据"问题换用证据来源复核（官方页面 citation_author 元数据、不同词典与百科、分类成员统计）。裁定为"确认 / 修正 / 否决"三档：分类类 175 项（确认 152、修正 20、否决 3）、译名类 99 项（确认 73、修正 7、否决 19）、其他与结构类 60 项（确认 49、修正 8、否决 3）。
3. **第三轮（终审仲裁）**：对两轮结论冲突处直接取证裁决，并补查第二轮遗漏的 6 条。重要翻案包括：
   * `johann-sturm`：官方目录署名形式为 "Sturm, Johann"，但**条目正文实为 Johann Christoph Sturm（1635–1703，阿尔特多夫大学教授）**，故"移入唯理论"与"译名补'克里斯托夫'"两项建议均成立（第二轮曾据目录字面否决，系误判）。
   * `continental-rationalism`（大陆理性主义）：官方 contents 页未列，但条目页仍在线（HTTP 200），第一轮"软 404"的说法有误；该条目未纳入官方目录属 SEP 自身目录遗漏。
   * 雅可比条目"缺右括号"为批次文件截断造成的假阳性，`SUMMARY.md:1290` 实际完好，撤销该项。
   * 作者名单抽查 5 条（categories、epistemology、mysticism、aristotle-biology、francis-bacon）全部与官方 citation_author 一致，附录 B 名单可信。

**数据说明**：SEP 现行网站已取消公开的主题分类浏览页（旧 category.html 已 404，条目页无学科元数据），故"分类是否正确"的判定依据是：条目官方导言所述主题＋人物生卒年代＋学派归属，对照本项目分类名及其括注定义；"翻译是否正确"的判定依据是官方英文标题、作者与通行中文译法。web.archive.org 在当前网络不可达，未使用存档数据。

---

## 一、总体结论

1. **英文标题与作者体例总体健康**：SUMMARY 中 1582 条主条目的英文标题与官方完全一致（0 处偏差），610 条别名中 531 条与官方别名精确对应。主要滞后在**作者名单**（155 条需更新，见附录 B）。
2. **分类目录覆盖率不足**：`mu-lu-s.md` 收录 1817 条（1814 个唯一路径，含"前言""关于"两个项目分区共 10 页），`SUMMARY.md` 共 2616 条（除 README.md 与 mu-lu-s.md 两个项目文件外 2614 条内容词条），**800 条内容词条未纳入分类目录**（覆盖率约 69%），详见附录 A。
3. **分类错置真实存在且呈系统性**：确认需移动的词条约 **150 条**，集中在"功利主义混入实用主义""分析哲学兜底分类""真理理论误挂认识论正当性""认知科学被当作万能桶""待分类桶可清空"等几个成片区域；另有约 **15 项分类体系本身的问题**（类名名不副实、括注与成员不符、年代标注失准）。
4. **译名问题 80 余条确认**：多为非通行音译（如"兹米尔茨·特瓦尔多夫斯基""麦拉加学派"）与术语误配（如 dialogical logic 译"博弈语义"、names 译"名词"）；另有 25 项第一轮建议被复核否决，现行译名可接受，**请勿误改**（见第六节）。
5. **少量官方条目已更换作者或退休**：155 条作者名单过期（附录 B），至少 1 条对应官方条目已退休（time-experience，由 consciousness-temporal 取代且尚未翻译）。

---

## 二、结构性发现（与官方目录逐条比对，可直接核实）

以下各项由脚本对 `SUMMARY.md`、`mu-lu-s.md` 与官方 contents.html（2026-10-26）逐条比对得出，均属确定性差异：

### 2.1 覆盖率：800 条词条未纳入分类目录

`mu-lu-s.md` 收录 1817 条，缺失 800 条（按 SUMMARY 字母分区统计与全名单见**附录 A**）。建议按附录 A 逐批补录进对应分类。

### 2.2 mu-lu-s.md 与 SUMMARY.md 标题不一致（4 处）

| 文件路径 | SUMMARY.md 写法 | mu-lu-s.md 写法 | 建议 |
| --- | --- | --- | --- |
| `a/a-si-ka-long-de-an-ti-ku-s-antiochus-of-ascalon-james-allen.md` | 阿斯卡隆的安提库斯（"库斯"后多一空格） | 阿斯卡隆的安提库斯 | 删除多余空格（以 SUMMARY 为准，CI 会同步） |
| `d/disability/pi-pan-de-can-ji-li-lun-critical-disability-theory-melinda-c.-hall.md` | 批判的残疾理论 | 批判性残疾理论 | 统一为文件 H1"批判的残疾理论" |
| `f/wei-lai-ou-ran-shi-jian-.../zhong-shi-ji-de-wei-lai-ou-ran-shi-jian-li-lun-medieval-theories-of-simo-knuuttila.md` | 中世纪的未来偶然性理论 | 中世纪的未来偶然事件理论 | 统一（官方为 medieval theories of future contingents，建议"未来偶然命题/事件"择一并全书统一） |
| `i/innate-acquired.md` | 遗传性特征与获得性特征的区别 | 先天/后天的区分 | 两写法均未精确对应官方 The Distinction Between Innate and Acquired Characteristics；建议统一为"先天性特征与后天获得性特征的区别"（innate≠hereditary，"遗传性"易生歧义） |

### 2.3 mu-lu-s.md 重复收录（5 处）

| 路径 | 重复位置 | 处理 |
| --- | --- | --- |
| `s/schlegel.md` | 德国浪漫主义分类内 L369 与 L373 逐字符重复 | 删一条 |
| `d/disability/pi-pan-de-can-ji-li-lun-...md` | 社会正义分类内 L2149 与 L2156 重复（两处译名还不同） | 删一条，并按 2.2 统一译名 |
| `s/social-minimum.md` | mu-lu-s.md:2155 与 2158 连续重复 | 删一条 |
| `f/wei-lai-ou-ran-shi-jian-.../README.md` | 非经典逻辑分类内 L865 与 L873 重复，且两个中文标题不同（未来偶然性/未来偶然事件） | 删一条并统一译名 |
| `i/xian-tian-hou-tian-de-qu-fen-...md` | 康德哲学（L403）与生命科学哲学（L1677）跨分类双重收录 | 择一保留（建议生命科学哲学） |

### 2.4 SUMMARY 别名条目在官方现行目录已无对应（4 处）

官方 contents.html 的别名清单中已查不到以下条目，建议逐一点开官方原链接核实是否已被撤销，再决定去留：

* `*超距作用——见量子力学：量子力学中的超距作用 action at a distance — see quantum mechanics: action at a distance in`
* `*同意——见政治义务 consent — see political obligation`
* `*松果体——见勒内·笛卡尔：笛卡尔与松果体 pineal gland — see Descartes, René: and the pineal gland`
* `*递归——见递归（递归函数） recursion — see recursion`（README 记载曾询编委会确认为"梗"条目，若官方已删可加译注保留）

### 2.5 SUMMARY 主条目与官方目录对不上（核查后余 14 条，均属可解释情形）

自动比对未能精确匹配的 17 条中：12 条为项目自建页（README、前言、关于等，无需处理）；余下核查确认——

* **官方目录确实未收录但条目在线**：`continental-rationalism`（大陆理性主义）。SEP 官方 contents 页漏列此条，本地无需改动，可加译注说明。
* **官方条目已退休**：`time-experience`（对时间的体验和知觉，Robin Le Poidevin）——官方页面标注 "Document Retired, superseded by Temporal Consciousness"（`consciousness-temporal`，Vanessa Carbonell 一类新条目已存在）。建议：本地条目加"已退休"译注，并安排补译新条目。
* **多部分条目的子条目标题省略父词**（属项目既有惯例，保留亦可，但建议至少在 mu-lu-s 中可见完整语义）：`笛卡尔与松果体 and the pineal gland`、`宗教与道德 and morality`、`柏拉图的乌托邦 on utopia`、`对时间的体验和知觉 the experience and perception of`、`西方音乐哲学史：古代至 1800 history of western philosophy of, antiquity to 1800` 等。
* 其余（量子力学、图表 diagrams、女性主义对物化的观点、可证性逻辑、逻辑与本体论、科学解释、智慧）经逐一比对官方标题与作者均正确存在，未发现内容错误。

### 2.6 SUMMARY 作者名单与官方不一致：155 条

完整名单见**附录 B**。类型包括：新增合作者（如 abilities 现为 John Maier and Sophie Kikkert）、整条更换作者（如 discrimination 现为 Anthony Sangiuliano、nationalism 现为 David Miller）、作者顺序调整（如 morality-definition 现为 Joshua Gert and Bernard Gert）。项目体例要求作者与官方一致，建议按附录 B 批量更新（涉及文件名内嵌作者的还需同步改名与链接）。

### 2.7 匹配歧义待人工确认（19 条）

多为多部分条目的同名子条目（各哲学家"美学 aesthetics"、"ethics"、"medieval theories of"等）。经人工抽样核对（如 croce-aesthetics/collingwood-aesthetics 均为 Gary Kemp，官方 meta 标签证实），内容无误；清单见**附录 C**，仅供未来自动化比对参考。

---

## 三、分类修改建议（两轮复核确认，约 150 条）

以下每条均经三轮确认（第一轮报告→第二轮独立取证→第三轮仲裁）。"→"后为建议归入的分类。括注说明证据要点。

> **注意**：本节按"主题优先"的思路给出归属建议。**人物条目**（亚历山大、波爱修斯、根特的亨利、苏亚雷斯、博丹、莱因霍尔德、特瓦尔多夫斯基、卢卡谢维奇、塔尔斯基、雷斯涅夫斯基、伽利略、亥姆霍兹、布尔、格劳秀斯、奥斯丁、施图尔姆、冯特、费希纳、哈特利、普莱斯、皮科、伊本·达乌德、伊本·埃兹拉、黑尔、普里查德、罗斯、史蒂文森、奇泽姆、格莱斯、伯林、古德曼、刘易斯、维特根斯坦、唐纳德·卡里·威廉姆斯、布劳德、杜威、爱德华兹、克拉克、柯林斯等）在**第九节"哲学史/哲学理论两分原则"下另有改判方案**（人物原则上归哲学史部，不按主题散入理论部），实施前请先阅读第九节并定夺路线。主题条目的建议不受影响。

### 3.1 古代与中世纪

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 阿芙罗蒂西亚的亚历山大 Alexander of Aphrodisias | 晚期希腊哲学 > 伊壁鸠鲁学派 | 中期希腊哲学 > 亚里士多德及逍遥学派（SEP：逍遥学派注释家，2–3 世纪） |
| 波爱修斯 Boethius | 经院哲学 > 唯名论 | 教父哲学与早期经院哲学（100-700）（约 475–526） |
| 根特的亨利 Henry of Ghent | 教父哲学与早期经院哲学（100-700） | 经院哲学（1000——1350）（1217–1293） |
| 尚波的威廉 William of Champeaux | 经院哲学 > 唯名论 | 经院哲学 > 实在论（SEP：staunch defense of realism） |
| 戈麦斯·佩雷拉 Gómez Pereira | 经院哲学 > 唯名论 | 文艺复兴与早期近代哲学 1350-1600（1500–?） |
| 罗吉尔·培根 Roger Bacon | 经院哲学 > 唯名论 | 经院哲学（1000——1350）主分类（与普遍性问题无关） |
| 苏亚雷斯 Suárez | 经院哲学（1000——1350） | 文艺复兴与早期近代哲学 1350-1600（1548–1617，第二经院哲学） |
| 萨拉曼卡学派 School of Salamanca | 经院哲学（1000——1350） | 文艺复兴与早期近代哲学 1350-1600（16–17 世纪） |
| 让·博丹 Bodin | 文艺复兴 > 宗教改革运动 | 文艺复兴与早期近代哲学 1350-1600 主分类（主权理论家，与宗教改革无涉；不移政治哲学史以免与同代人拆散） |
| 埃里金纳 Eriugena | 教父哲学与早期经院哲学（100-700） | 保留但建议将分类年代上限延至约 900，或新增加洛林时代分类（约 800–877） |
| 中世纪哲学 Medieval Philosophy（通论） | 教父哲学与早期经院哲学（100-700） | 上提为中世纪区块总论，或新增"中世纪哲学通论" |
| 中世纪的类比理论 Medieval Theories of Analogy | 宗教学 > 基督教 | 经院哲学（1000——1350）（逻辑—神学—形而上学交叉，与"X in Christian thought"条目族不同） |
| 中世纪哲学的文学形式 Literary Forms of Medieval Philosophy | 文化哲学 | 中世纪哲学通论（新增）（覆盖整个中世纪） |
| 亚伯拉罕·伊本·达乌德 Ibn Daud | 区域哲学 > 伊斯兰哲学 | 区域哲学 > 犹太哲学（SEP：犹太哲学先驱） |
| 亚伯拉罕·伊本·埃兹拉 Ibn Ezra | 区域哲学 > 伊斯兰哲学 | 区域哲学 > 犹太哲学 |

### 3.2 启蒙运动与早期近代（1600–1750）

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 康帕内拉 Campanella | 启蒙时代的法国哲学【1600-1750】 | 文艺复兴与早期近代哲学 1350-1600（1568–1639，晚期文艺复兴，且非法国人） |
| 蒙田 Montaigne | 启蒙时代的法国哲学【1600-1750】 | 文艺复兴与早期近代哲学 1350-1600（卒 1592） |
| 人格主义 Personalism | 德国浪漫主义（耶拿浪漫主义） | 新增独立分类（20 世纪上半叶成形的流派，不属任何现有时期类） |
| 大陆理性主义 Continental Rationalism | 暂时无法分类--待分类 | 启蒙运动和早期现代哲学 > 唯理论 |
| 塞缪尔·克拉克 Samuel Clarke | 暂时无法分类--待分类 | 唯理论（1675–1729） |
| 安东尼·柯林斯 Anthony Collins | 暂时无法分类--待分类 | 经验论（1676–1729，英国自由思想者） |
| 杜博斯 Du Bos | 暂时无法分类--待分类 | 启蒙时代的法国哲学（1670–1742，美学家） |
| 爱德华兹 Jonathan Edwards | 暂时无法分类--待分类 | 启蒙运动和早期现代哲学 1600-1750（1703–1758） |
| 施图尔姆 Sturm, Johann | 暂时无法分类--待分类 | 唯理论（条目实为 Johann Christoph Sturm，1635–1703，见第三节末说明） |
| 文艺复兴时期的亚里士多德主义 Aristotelianism: in the Renaissance | 暂时无法分类--待分类 | 文艺复兴与早期近代哲学 1350-1600 |
| 普芬道夫的伦理学和政治哲学 Pufendorf: moral and political philosophy | 暂时无法分类--待分类 | 法哲学（自然法传统） |
| 约翰·奥斯丁 John Austin | 暂时无法分类--待分类 | 法哲学（分析法理学创始人） |
| 杜威/胡克/詹姆斯/皮尔士/米德/罗蒂/罗伊斯/桑塔亚纳/昌西·赖特等 | 现代西方哲学 > 功利主义 | 新增"实用主义"分类（见 3.4） |
| 莱因霍尔德 Reinhold | 现代西方哲学 > 新康德主义 | 启蒙运动和早期现代哲学 > 德国唯心论/德国观念论（1757–1823，康德早期普及者） |

### 3.3 现代西方哲学（1750–1900）

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 梅洛-庞蒂 Merleau-Ponty | 现代西方哲学 > 解释学 | 现象学（战后法国现象学代表） |
| 李凯尔特 Rickert | 现代西方哲学 > 新黑格尔主义 | 新康德主义（巴登学派） |
| 费英格 Vaihinger | 现代西方哲学 > 新黑格尔主义 | 新康德主义（SEP：Neo-Kantian philosopher） |
| 特瓦尔多夫斯基 Twardowski | 前期分析哲学 | 布伦塔诺学派（布伦塔诺学生、利沃夫-华沙学派创立者） |
| 华沙学派 Lvov-Warsaw School | 前期分析哲学 | 语言哲学与逻辑学 > 逻辑史 |
| 卢卡谢维奇 Łukasiewicz | 前期分析哲学 | 语言哲学与逻辑学 > 逻辑学家 |
| 塔尔斯基 Tarski（主条目） | 前期分析哲学 | 语言哲学与逻辑学 > 逻辑学家（人物条目与卢卡谢维奇、布尔同例） |
| 塔尔斯基的真理定义 Truth Definitions | 前期分析哲学 | 语言哲学与逻辑学 > 语义学 |
| 雷斯涅夫斯基 Leśniewski | 科学哲学 | 语言哲学与逻辑学 > 逻辑学家（华沙逻辑学派） |
| 伽利略 Galileo | 科学哲学 | 科学哲学 > 科学家（1564–1642） |
| 亥姆霍兹 Helmholtz | 科学哲学 | 科学哲学 > 科学家 |
| 确定物与可确定物 Determinates and Determinables | 前期分析哲学 | 形而上学 > 本体论 |
| 唐纳德·卡里·威廉姆斯 Williams, Donald Cary | 分析哲学（待进一步分类） | 形而上学 > 本体论（核心贡献为特普论） |
| 以赛亚·伯林 Berlin | 分析哲学（待进一步分类） | 政治哲学 > 自由主义与共和主义 |
| 黑尔 Hare | 分析哲学（待进一步分类） | 伦理学 > 元伦理学（规定主义） |
| 普里查德 Prichard | 分析哲学（待进一步分类） | 伦理学 > 元伦理学（牛津直觉主义） |
| 罗斯 W. D. Ross | 分析哲学（待进一步分类） | 伦理学 > 规范伦理学（《对与善》） |
| 史蒂文森 Stevenson | 分析哲学（待进一步分类） | 伦理学 > 元伦理学（情感主义） |
| 奇泽姆 Chisholm | 分析哲学（待进一步分类） | 认识论 |
| 格莱斯 Grice | 分析哲学（待进一步分类） | 语言哲学与逻辑学 > 语用学（会话含义） |
| 大卫·刘易斯 Lewis | 分析哲学（待进一步分类） | 形而上学 > 模态实在论（可能世界） |
| 古德曼 Goodman | 分析哲学（待进一步分类） | 美学 > 艺术哲学 |
| 维特根斯坦 Wittgenstein | 分析哲学（待进一步分类） | 语言哲学与逻辑学 > 逻辑学家 |
| 事态 States of Affairs | 分析哲学（待进一步分类） | 语义学 |
| 遵循规则与意向性 Rule-Following and Intentionality | 分析哲学（待进一步分类） | 语义学 |
| 私人语言 Private Language | 分析哲学（待进一步分类） | 语义学 |
| 逻辑形式 Logical Form | 分析哲学（待进一步分类） | 语义学 |
| 自然主义 Naturalism | 分析哲学（待进一步分类） | 形而上学（条目主体为本体论自然主义与物理主义；一轮建议元认识论过窄，第二轮修正） |
| 思维语言假说 Language of Thought | 分析哲学（待进一步分类） | 心理学与心灵哲学 > 认知科学 |
| 意向性 Intentionality 条目群（含古代意向性子条目） | 现象学 / 布伦塔诺学派 | 心理学与心灵哲学 > 心灵的特征（意向性）（古代意向性一轮建议归亚里士多德及逍遥学派，第二轮修正为随意向性条目群同归心灵的特征，避免同族拆散） |
| 本体论承诺 Ontological Commitment | 科学哲学 | 形而上学 > 本体论 |
| 蒯因的新基础 New Foundations | 科学哲学 | 语言哲学与逻辑学 > 非经典逻辑（集合论公理系统） |
| 基于行动的知觉理论 Action-Based Theories of Perception | 行动哲学 | 心理学与心灵哲学 > 知觉 |
| 行动的逻辑 Action (logic 子条目) | 行动哲学 | 语言哲学与逻辑学 > 非经典逻辑（一阶行动逻辑） |
| 斯宾塞 Spencer | 实证主义 | 新增"演化哲学与社会哲学"分类（低置信，或暂留并加注） |
| 拉姆齐的代际福利经济学 Ramsey: Intergenerational Welfare Economics | 前期分析哲学 | 经济哲学 > 经济学家（注意与父目录同组移动） |

### 3.4 马克思主义、社会学、经济、博弈、决策等

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 物理主义 Physicalism | 马克思主义与西方马克思主义 | 心理学与心灵哲学 > 物理主义 |
| 17 至 20 世纪的原子论 Atomism: 17th to 20th Century | 马克思主义与西方马克思主义 | 科学哲学 > 物理学哲学 |
| 唯心主义 Idealism | 马克思主义与西方马克思主义 | 形而上学（跨时期通论条目；一轮建议德国唯心论过窄，第二轮修正） |
| 科学知识的社会维度 Social Dimensions of Scientific Knowledge | 社会学哲学 | 科学哲学 > 科学方法论与科学知识论 |
| 团结 Solidarity | 社会学哲学 | 政治哲学 > 社会理论和公共哲学 |
| 社会生物学 Sociobiology | 社会学哲学 | 科学哲学 > 生命科学哲学 |
| 虚构主义 Fictionalism | 文化哲学 | 语言哲学与逻辑学 > 语义学 |
| 幽默哲学 Humor | 文化哲学 | 美学 |
| 商业伦理学 Business Ethics | 经济哲学 | 伦理学 > 应用伦理学 |
| 知识产权 Intellectual Property | 经济哲学 | 伦理学 > 应用伦理学 |
| 分析游戏的逻辑 / 逻辑与游戏 / 分析标准形式博弈中权力的逻辑（三条） | 博弈论 | 语言哲学与逻辑学 > 非经典逻辑（哲学逻辑条目族） |
| 陪审团定理 Jury Theorems | 决策理论 | 政治哲学 > 民主理论 |
| 实验哲学 Experimental Philosophy | 哲学咨询与实践 | 暂入分析哲学兜底类（待该类消解时一并分流） |
| 思想实验 Thought Experiments | 哲学咨询与实践 | 科学哲学 > 科学方法论与科学知识论 |
| 体育哲学 Philosophy of Sport | 暂时无法分类--待分类 | 文化哲学（低置信） |
| 中世纪的良心理论 Medieval Theories of Conscience | 暂时无法分类--待分类 | 伦理学 > 伦理学理论与伦理学家 |
| 中世纪情感理论 / 17 和 18 世纪的情感理论 | 暂时无法分类--待分类 | 心理学与心灵哲学 > 情感哲学 |
| 古代和中世纪的经验主义 / 理性主义与经验主义 | 暂时无法分类--待分类 | 认识论 |
| 17 世纪的意识理论 | 暂时无法分类--待分类 | 心理学与心灵哲学 > 关于意识的形而上学问题 |
| 罗森斯托克-胡絮 Rosenstock-Huessy | 暂时无法分类--待分类 | 社会学哲学（20 世纪社会哲学家） |
| 约翰·库克·威尔逊 Cook Wilson | 暂时无法分类--待分类 | 语言哲学与逻辑学 > 逻辑学家（牛津逻辑学教授） |
| 中世纪的实践理性 Medieval Theories of Practical Reason | 暂时无法分类--待分类 | 伦理学 > 伦理学理论与伦理学家 |
| 约克·冯·瓦滕堡 Yorck von Wartenburg | 暂时无法分类--待分类 | 现代西方哲学 > 解释学（与狄尔泰合作） |

### 3.5 语言哲学与逻辑学

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 溯因 Abduction | 语义学 | 认识论（解释性推理） |
| 认识论的语境主义 Contextualism: Epistemic | 语用学 | 认识论 |
| 内部言语 Inner Speech | 语用学 | 心理学与心灵哲学 > 认知科学 |
| 先天与语言 Innateness and Language | 语义学 | 心理学与心灵哲学 > 认知科学 |
| 分歧 Disagreement | 语义学 | 认识论 > 社会认识论 |
| 类比与类比推理 Analogy and Analogical Reasoning | 语义学 | 形式逻辑与非形式逻辑 |
| 归纳问题 Problem of Induction | 形式逻辑与非形式逻辑 | 认识论 |
| 偏好 Preferences | 非经典逻辑 | 决策理论 |
| 论证与论辩 Argument and Argumentation | 非经典逻辑 | 形式逻辑与非形式逻辑 |
| 可能性主义与实在主义辩论 Possibilism-Actualism Debate | 非经典逻辑 | 形而上学 > 模态实在论 |
| 严格指示词 Rigid Designators | 非经典逻辑 | 语义学 |
| 代数 Algebra | 非经典逻辑 | 科学哲学 > 数学哲学 |
| 斯科伦悖论 Skolem's Paradox | 非经典逻辑 | 形式逻辑与非形式逻辑（悖论） |
| 中世纪未来偶然性理论 / 中世纪义务理论 Obligationes | 非经典逻辑 / 经典逻辑与传统逻辑 | 逻辑史（两条） |
| 命题 Propositions（含单称命题、结构化命题） | 经典逻辑与传统逻辑 | 语义学 |
| 概念 Concepts | 语义学 | 心理学与心灵哲学 > 认知科学 |
| 格劳秀斯 Grotius | 逻辑学家 | 法哲学（自然法；一轮建议政治哲学，第二轮修正为法哲学） |
| 析取 Disjunction | 逻辑史 | 经典逻辑与传统逻辑 |
| λ 演算 Lambda Calculus | 科学哲学 > 科学家 | 语言哲学与逻辑学 > 逻辑史 |
| 丘奇类型论 Church's Type Theory | （关联项） | 与 3.4 段"库内译名统一"联动，见 5.10 |

### 3.6 法哲学与认识论

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 主权 Sovereignty | 法哲学 | 政治哲学 > 政治义务与合法性 |
| 报应正义 Retributive Justice | 法哲学 | 政治哲学 > 正义理论 |
| 自卫 Self-Defense | 法哲学 | 伦理学 > 应用伦理学 |
| 变化与不一致 Change and Inconsistency | 认识论 | 形而上学 > 身份与变化 |
| 社会认识论 Social Epistemology（总条目） | 认识论（父类） | 认识论 > 社会认识论 |
| 事实 Facts | 认识论 | 形而上学 > 本体论 |
| 道德认识论 Moral Epistemology | 认识论 > 元认识论 | 伦理学 > 元伦理学 |
| 真理 Truth（总条目） | 认识论 > 元认识论 | 语言哲学与逻辑学 > 语义学 |
| 真理融贯论 / 符合论 / 紧缩论 / 同一论 / 多元真理论 / 实用主义真理观 / 修正真理论（7 条） | 认识论 > 认识论正当性 | 语言哲学与逻辑学 > 语义学（其文件目录本身挂在真理条目下） |
| 似真性 Truthlikeness | 认识论 > 认识论正当性 | 语言哲学与逻辑学 > 语义学 |
| 知识的价值 Value of Knowledge | 认识论 > 社会认识论 | 认识论 > 元认识论 |
| 关于如何做某事的知识 Knowledge How | 认识论 > 社会认识论 | 认识论（父类） |
| 直觉主义类型论 Intuitionistic Type Theory | 认识论 > 认识论正当性 | 语言哲学与逻辑学 > 非经典逻辑 |
| 理解 Understanding | 认识论 > 认识论正当性 | 认识论（父类） |
| 外在主义与自我认识 Externalism and Self-Knowledge | 认识论 > 外在性 | 心理学与心灵哲学 > 外在主义与延展心灵 |
| 谬误 Fallacies | 认识论 > 合理性 | 形式逻辑与非形式逻辑 |
| 泛指概括 Generic Generalizations | 认识论 > 合理性 | 语言哲学与逻辑学 > 语义学 |
| 相对主义 Relativism | 认识论 > 合理性 | 形而上学 |
| 可靠主义认识论 Reliabilist Epistemology | 认识论 > 合理性 | 认识论 > 认识论正当性 |
| 简单性 Simplicity | 认识论 > 合理性 | 科学哲学 > 科学方法论与科学知识论 |

### 3.7 形而上学

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 无限 Infinity | 因果关系 | 科学哲学 > 数学哲学 |
| 特普 Tropes | 因果关系 | 本体论 |
| 现代物理学中的存在与变化 Being and Becoming in Modern Physics | 本体论 | 时间与空间哲学 |
| 上帝与其他终极存在 / 上帝和其他必然存在（2 条） | 哲学中的神秘传统 | 宗教学 > 神学（第二轮修正：不新增形而上学子类，入现有神学类） |
| 动物主义 Animalism | 科学哲学 > 生命科学哲学 | 形而上学 > 身份与变化（人格同一性理论） |
| 事件 Events | 出生哲学与死亡哲学 > 历史哲学 | 形而上学 > 本体论（第二轮修正；次选时间与空间哲学） |
| 历史哲学 History, Philosophy of | 出生哲学与死亡哲学 > 历史哲学 | 社会学哲学 |

### 3.8 心理学与心灵哲学

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 二元论 Dualism | 物理主义 | 关于意识的形而上学问题（二元论） |
| 进化心理学 Evolutionary Psychology | 认知科学 | 心理学与心灵哲学顶层（SEP：Philosophy of Psychology） |
| 利己主义 Egoism | 认知科学 | 伦理学 > 规范伦理学 |
| 情感 Emotion（总条目）/ 共情 Empathy | 认知科学 | 情感哲学 |
| 内省 Introspection | 情感哲学 | 心理学与心灵哲学顶层 |
| 认知封闭 Epistemic Closure / 认知悖论 Epistemic Paradoxes / 认知效用于认知规范 Epistemic Utility Arguments | 认知科学 | 认识论（三条） |
| 中世纪哲学中的心理表征 Mental Representation: in Medieval Philosophy | 认知科学 | 经院哲学（1000——1350） |
| 疼痛 Pain | 知觉 | 意识研究 |
| 感觉与料 Sense Data | 关于意识的形而上学问题 | 知觉 |
| 莫利纽克斯问题 Molyneux's Problem | 认知科学 | 知觉 |
| 狭义心理内容 / 非概念性心理内容 / 心理内容的目的论理论 / 心理表征（4 条） | 意识研究 / 认知科学 | 心灵的特征（意向性） |
| 泛心论 Panpsychism | 意识研究 | 关于意识的形而上学问题 |
| 副现象主义 Epiphenomenalism | 意识研究 | 心灵因果性 |
| 中立一元论 Neutral Monism | 物理主义 | 关于意识的形而上学问题 |
| 多重可实现性 Multiple Realizability | 认知科学 | 物理主义 |
| 心理主义 Psychologism | 心理学与心灵哲学顶层 | 语言哲学与逻辑学 > 逻辑史 |
| 能力 Abilities | 心理学与心灵哲学顶层 | 现代西方哲学 > 行动哲学（低置信） |
| 利他主义的经验主义研究（子条目） | 心理学与心灵哲学顶层 | 随父条目"利他主义"归置（父条目在伦理学 > 价值观哲学），避免同族分裂 |
| 冯特 / 费希纳 / 哈特利（3 条） | 伦理学 > 心理学家 | 心理学与心灵哲学 |
| 普莱斯 Price, Richard | 伦理学 > 心理学家 | 伦理学 > 道德心理学（道德感论） |

### 3.9 科学哲学

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 玻尔兹曼在统计物理学方面的研究 Boltzmann's Work in Statistical Physics | 科学家 | 物理学哲学 |
| 游戏、完全抽象和完全性 Games, Abstraction and Completeness | 信息和数字文化哲学 | 语义学（程序语言指称语义） |
| 科学中的计算机模拟 Simulations in Science | 信息和数字文化哲学 | 科学方法论与科学知识论 |
| 元胞自动机 Cellular Automata | 信息和数字文化哲学 | 物理学哲学（低置信；或随"计算机与人工智能哲学"拆分去向） |
| 微调 Fine-Tuning | 科学方法论与科学知识论 | 物理学哲学（宇宙学） |
| 菲奇的可知性悖论 Fitch's Paradox of Knowability | 科学认识论 | 认识论 |
| 亲知与摹状知识 Knowledge by Acquaintance vs. Description | 科学认识论 | 认识论 |
| 神创论 Creationism | 宗教学 > 神学 | 科学哲学 > 生命科学哲学（进化论相关；次选宗教学通论"宗教与科学"） |

### 3.10 中国、区域与宗教

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 18 世纪苏格兰哲学 Scottish Philosophy: 18th Century | 区域哲学 > 欧洲哲学 | 启蒙运动和早期现代哲学 > 苏格兰启蒙运动（1700-1800） |
| 19 世纪苏格兰哲学 Scottish Philosophy: 19th Century | 区域哲学 > 欧洲哲学 | **保留现置**（第二轮否决移动：与 18 世纪条目成对，无更贴切子类；如采纳上一条需连带决定此条去向） |
| 儒学中的性别 Gender in Confucian Philosophy | 女性哲学 > 性别与酷儿哲学 | 中国哲学 > 中国哲学通论 |
| 双重意识 Double-Consciousness | 伦理学 > 道德心理学 | 区域哲学 > 非裔哲学（Du Bois 概念） |
| 基督教传统中的情感 Emotions in the Christian Tradition | 宗教学 > 基督教 | **保留现置**（第二轮否决：与"X in Christian thought"条目族模式吻合） |

### 3.11 伦理学、性别与美学、政治哲学

| 词条 | 现分类 | 建议分类 |
| --- | --- | --- |
| 公共证成 Public Justification | 伦理学 > 社会正义 | 政治哲学 > 政治义务与合法性（第二轮修正；次选社会理论和公共哲学） |
| 实验伦理学 Experimental Moral Philosophy | 应用伦理学 | 道德心理学 |
| 决策能力 Decision-Making Capacity | 人权 | 科学哲学 > 医学人文学和医学哲学 > 生命医学伦理与公共政策（第二轮修正） |
| 恐怖主义 Terrorism | 社会正义 | 社会伦理学 |
| 可行能力 Capability Approach | 人权 | 政治哲学 > 正义理论（第二轮修正；分配正义理论） |
| 行动体 Agency（含共享行为体） | 人权 | 现代西方哲学 > 行动哲学 |
| 异化 Alienation | 人权 | 社会学哲学（第二轮修正；次选马克思主义与西方马克思主义） |
| 皮科·德拉·米兰多拉 Pico della Mirandola | 近代女性哲学家（1500-1750） | 文艺复兴与早期近代哲学 1350-1600（男性，1463–1494） |
| 孔多塞：女性主义史中的孔多塞 Condorcet: in the history of feminism | 现代女性哲学家（1750+） | 女性哲学 > 女性主义哲学（第二轮修正；男性启蒙思想家，条目属女性主义史系列） |
| 女性主义伦理学 / 女性主义道德心理学 / 女性主义生命伦理学（3 条） | 性哲学 | 女性主义哲学（与同系列女性主义法哲学、宗教哲学等并列） |
| 颜色 Color | 美学 | 心理学与心灵哲学 > 知觉（第二轮确认） |
| 肮脏之手问题 Dirty Hands | 政治哲学 > 民主理论 | 政治义务与合法性（政治伦理） |
| 身份政治 Identity Politics | 正义理论 | 政治理论（各种主义） |

---

## 四、分类体系本身的建议（约 20 项）

1. **功利主义（24 条）拆分**：其中实用主义者（皮尔士 3 条、詹姆斯、杜威 3 条、米德、罗蒂、罗伊斯、桑塔亚纳、胡克、昌西·赖特、实用主义总目等）至少 14 条，应新增"现代西方哲学 > 实用主义"分类并移入；功利主义保留边沁、戈德温、穆勒父子、西季威克等约 10 条。
2. **分析哲学（待进一步分类以消解掉本分类）（23 条）**：类名自我声明为临时兜底。按第三节 3.3 分流完毕后删除本类；实验哲学、思维语言假说等去向已列入上表。
3. **宗教学 > 证明论（5 条）改名"上帝存在的论证"**：五条实为宇宙论/本体论/目的论/道德/实用主义论证，"证明论"是 proof theory（逻辑学）的既定译名，名实严重错位。两个分区核查组独立得出同一结论。
4. **认识论 > 认识论正当性**：18 条中 8 条为真理理论（其文件路径本身挂在真理条目下），迁往语义学后仅留证成、怀疑论、证言等约 10 条。
5. **认识论 > 社会认识论**：现仅 2 条成员且均非社会认识论；将社会认识论总条目迁入，另两条按 3.6 分流。
6. **认识论 > 合理性**：7 条成员（谬误、泛指概括、直觉、相对主义、可靠主义、自我定位信念、简单性）中 5 条与合理性无关，建议整体解散并按 3.6 分流。
7. **认识论 > 外在性**：唯一成员为"外在主义与自我认识"，类名应改"外在主义"（externalism），或随成员迁入心灵哲学专类后撤销。
8. **心理学与心灵哲学 > 认知科学**：实际充当万能桶（进化心理学、利己主义、情感、认知封闭、心理表征等混入），建议按 3.8 逐条分流，类目仅保留认知科学本体条目。
9. **物理主义分类括注与成员不符**：括注列"行为主义"但行为主义条目在顶层（SEP 官方将 behaviorism 归 physicalism 组，建议移入）；二元论条目在物理主义类下而括注未列；建议将二元论移出（见 3.8）后核对括注。
10. **心灵的特征括注"意识大众心理学"改"民间心理学"**：与全库 folk psychology 译名一致。
11. **关于意识的形而上学问题括注**：末尾悬空逗号"幻象论，）"删除；括注成员与实际条目对齐。
12. **心灵因果性括注**：删去"外在主义与心灵因果"（已有专类）。
13. **伦理学 > 心理学家**：4 条按 3.8 处理后撤销该子类（与"科学家/逻辑学家/经济学家"命名范式不同质）。
14. **伦理学 > 价值观哲学括注**改"价值论、好生活、道德情感与德性"（现括注"道德情感、道德标准相关"覆盖不到 18 条中的多数）。
15. **科学哲学 > 信息和数字文化哲学（34 条）拆分**：约 20 余条为人工智能/可计算性类（图灵机、中文房间、邱奇-图灵论题、可计算性与复杂度、联结主义、框架问题等），建议拆出"计算机与人工智能哲学"；其余为信息哲学与网络伦理。
16. **科学实在论括注**（理论解释力、理论变化……）远窄于实际内容（含科学解释、科学发现、客观性、进步、革命、测量等），建议扩充或删去括注。
17. **启蒙运动和早期现代哲学 1600-1750 年代标注失准**：下辖康德哲学（卒 1804）、德国唯心论（黑格尔卒 1831）、苏格兰启蒙运动（1700-1800）、德国浪漫主义（1700-1800），建议顶层改"1600-1900"或上移相关子类。
18. **启蒙时代的法国哲学【1600-1750】名不副实**：13 条中蒙田、康帕内拉、梅森、伽桑狄、帕斯卡、培尔等约 6 条属文艺复兴/科学革命，建议改名"法国早期近代哲学（16 世纪末–1750）"或拆分。
19. **出生哲学与死亡哲学 > 历史哲学解散**：仅 2 条且均与主题无关（事件→本体论，历史哲学→社会学哲学，见 3.7）。
20. **政治哲学 > 解放哲学分流**：5 条中民族主义→政治理论，革命、分离→政治义务与合法性；仅解放哲学与拉丁美洲的自由主义保留。
21. **区域哲学 > 欧洲哲学改名"苏格兰哲学"**：仅 2 条且均为 Scottish Philosophy 系列条目。
22. **经院哲学 > 唯名论按立场重排**：10 条中尚波（实在论者）、波爱修斯（6 世纪）、佩雷拉（16 世纪）、罗吉尔·培根 4 条名实不符（见 3.1）。
23. **晚期希腊哲学 > 怀疑论学派括注**：括注中"阿尔凯阳劳和卡尼阿德"实属"老学园及学园怀疑主义"分类，括注只保留实际成员"皮浪和第蒙、塞克斯都·恩披里克"，并修正错别字（阿尔凯**阳**劳→阿尔凯**西**劳，恩披**单**柯→恩披**里**柯）。
24. **教父哲学与早期经院哲学（100-700）年代上限**：唯一超期条目为埃里金纳（约 800–877），建议上限延至约 900，或新增"加洛林时代哲学"。

---

## 五、译名修改建议（两轮复核确认，约 80 条）

### 5.1 人名音译

| 现译 | 建议 | 词条（slug） | 依据要点 |
| --- | --- | --- | --- |
| 麦拉加学派 | 辩证学派 | dialectical-school | 官方 Dialectical School；"麦加拉"（Megara）另为其相关学派名，两不相混 |
| 阿帕米亚的努美尼乌斯 | 阿帕梅亚的努梅尼乌斯 | numenius | Apamea 通行"阿帕梅亚" |
| 尼克尔·奥雷姆 | 尼科尔·奥雷姆 | oresme | 中文维基条目名"尼科爾·奧雷姆" |
| 拉曼·鲁尔 | 拉蒙·柳利 | llull-ramon | Ramon Llull 通行译名 |
| 约瑟夫·伊本·卡斯比 | 约瑟夫·卡斯皮 | kaspi-joseph | Kaspi 非"伊本"式姓名；通行"卡斯皮" |
| 弗朗西斯科·桑奇 | 弗朗西斯科·桑切斯 | sanches-francisco | Sanches 通行"桑切斯" |
| 雅各布·萨巴雷拉 | 贾科莫·萨巴雷拉 | zabarella-giacomo | Giacomo 通行"贾科莫" |
| 亚当·冯·沃德汉姆 | 亚当·德·沃德汉姆 | wodeham-adam-de | de 译"德"，"冯"对应德语 von |
| 亨利·莱格伍 | 亨利·雷吉乌斯 | regius-henricus | Regius 通行"雷吉乌斯" |
| 兹米尔茨·特瓦尔多夫斯基 | 卡济梅尔兹·塔多斯基 | twardowski-kazimierz | 现译截取自 Kazimierz 词中段，不成词；中文维基"卡济梅尔兹·塔多斯基" |
| 斯坦尼斯瓦夫·雷斯涅夫斯基 | 斯坦尼斯瓦夫·莱什涅夫斯基 | lesniewski-stanisaw | Leśniewski 通行"莱什涅夫斯基" |
| 扬-卢卡谢维奇 | 扬·武卡谢维奇（连字符改间隔号） | lukasiewicz-jan | 中文维基条目名"扬·武卡谢维奇" |
| 奥图·纽拉特 | 奥托·纽拉特 | neurath-otto | Otto 通行"奥托" |
| 查理·邓巴·布劳德 | 查理·邓巴·布罗德 | broad-charlie-dunbar | Broad 通行"布罗德" |
| 理查德·麦尔文·黑尔 | 理查德·默尔文·黑尔 | hare-richard-mervyn | Mervyn 通行"默尔文" |
| 威廉姆·斯坦利·杰文斯 | 威廉·斯坦利·杰文斯 | jevons-william-stanley | "威廉姆"为冗译 |
| 亚瑟·普赖尔 | 阿瑟·普赖尔 | prior-arthur | Arthur 通行"阿瑟" |
| 艾利亚·德尔·梅第戈 | 以利亚·德尔·梅第戈 | delmedigo-elijah | Elijah 通行"以利亚" |
| 格舒姆·索罗姆 | 格肖姆·朔勒姆 | scholem-gershom | Gershom Scholem 通行（中译本署名即"格肖姆·朔勒姆/索伦"） |
| 达马里斯·卡德沃斯·马沙姆 | 达玛里斯·库德沃斯·马沙姆 | masham-lady-damaris | 与术语表 Cudworth=库德沃斯 统一；Damaris 通作"达玛里斯" |
| 玛丽·艾斯泰尔 | 玛丽·阿斯特尔 | astell-mary | Mary Astell 通行"阿斯特尔" |
| 玛德琳·德·史居里 | 玛德莱娜·德·斯居代里 | scudry-madeleine-de | Scudéry 通行"斯居代里" |
| 赫尔曼·冯·海姆霍兹（关联） | （保持与术语表一致） | hermann-helmholtz | — |

### 5.2 术语与标题误译

| 现译 | 建议 | 词条（slug） | 依据要点 |
| --- | --- | --- | --- |
| 先验论证与先验知识 | 先验证成与先验知识 | apriori-justification-and-knowledge | justification=证成（术语表）；现译与 transcendental arguments（先验论证）撞名 |
| 休谟的宗教学 | 休谟论宗教 | hume-on-religion | 官方 Hume on Religion；"宗教学"对应 religious studies |
| 莱布尼茨的表面哲学 | 莱布尼茨的通俗哲学 | leibniz-exoteric-philosophy | exoteric 与 esoteric（秘传）相对 |
| 夏尔·路易·德·塞孔达，拉布雷德与孟德斯鸠男爵 | 夏尔·路易·德·塞贡达·拉布雷德与孟德斯鸠男爵 | montesquieu | Secondat 通行"塞贡达"；人名串中的全角逗号不合体例 |
| 古代哲学学述 | 古代哲学学说史 | doxography-of-ancient-philosophy | doxography 通行"学说史" |
| 1277 大谴责 | 1277 年巴黎谴责 | condemnation-of-1277 | 官方 condemnation of 1277；与文件名统一 |
| 总务长菲利普 | （保留，术语表一致） | philip-the-chancellor | 第二轮否决改动；如需更通行可作"菲利普校长"，由项目定夺 |
| 逻辑代数的发展 | 逻辑代数的传统 | algebra-of-logic-tradition | tradition=传统 |
| 语用（pragmatics 主条目） | 语用学 | pragmatics | 与学科名体例一致 |
| 范畴类型逻辑 | 类型语法 | typelogical-grammar | Typelogical Grammar 即类型语法 |
| 博弈语义（dialogical logic） | 对话逻辑 | logic-dialogical | dialogical logic ≠ 博弈语义（game-theoretic semantics） |
| 名词（names） | 专名 | names | 条目论 proper names |
| 恩斯的特的道义逻辑 | 恩斯特·马利的道义逻辑 | mally-deontic-logic | 现译把名"恩斯特"错作属格主语 |
| 用于分析标准形式博弈中权力的逻辑 | （同左） | logics-power-games | 现译"游戏中的权力推理"漏译 normal form 且"推理"应为"分析" |
| 变化与不一致 | （保留） | change-and-inconsistency | 第二轮否决："不一致"可接受 |
| 知识证成的融贯论理论 | 知识证成的融贯论 | justep-coherence | "融贯论理论"叠床架屋；同目录"基础主义理论"同步 |
| 直觉主义认识论 | 直觉主义类型论 | type-theory-intuitionistic | Type Theory=类型论，"认识论"完全错配 |
| 泛化 | 泛指概括 | generic-generalizations | generics 领域通行译名 |
| 后向因果关系 | 逆向因果关系 | causation-backwards | 与术语表 Retrocausality=逆因果关系 及文件名一致 |
| 基质主义 | 此性论 | haecceitism | 与术语表 haecceity=此性 一致；"基质"对应 substratum |
| 变异一元论 | （保留，术语表首选） | anomalous-monism | 术语表 anomalous monism=变异一元论（亦译异常一元论） |
| 感知的分离理论 | 感知的析取理论 | perception-disjunctive | disjunctive 固定译"析取" |
| 联想主义思想 | 联想主义的思维理论 | associationist-thought | 官方 Associationist Theories of Thought，漏译 theories |
| 取消式唯物主义 | 取消唯物主义 | eliminative-materialism | 与分类括注"取消主义"统一 |
| 意向（intention） | 意图 | intention | action 语境通行"意图"，避免与"意向性"混淆 |
| 科学中的机械论 | 科学中的机制 | science-mechanisms | mechanism in science=机制；项目日志已自记"需要重译" |
| 预测与解释 | 预测与迁就 | prediction-accommodation | accommodation≠explanation；术语表作"（理论）迁就" |
| 中文房间实验 | 中文房间论证 | chinese-room | argument=论证 |
| 菲奇的可知性悖论 | 费奇的可知性悖论 | fitchs-paradox | 华文哲学百科作"费奇" |
| 游戏、完全抽象和完全性 | 博弈、完全抽象与完全性 | games-abstraction | 数理语境 games=博弈；一轮建议的"完全完备性"叠用，第二轮修正 |
| 基因漂移 | 遗传漂变 | genetic-drift | 生物学标准中译；文件名已是 yi-chuan-piao-bian |
| 荷兰赌定理 | 荷兰赌论证 | dutch-book | arguments=论证（条目内区分 argument 与 theorem） |
| 生物演化理论 | 生物发育理论 | theories-biological-development | development=发育（术语表生物学语境注）；与同库"进化和发育"统一 |
| 质能守恒 | 质能等价 | equivalence-of-mass-and-energy | equivalence=等价；"守恒"是 conservation |
| 系统发生分析 | 系统发生推断 | phylogenetic-inference | inference=推断（统计推断） |
| EPR 悖论 | EPR 论证 | einstein-podolsky-rosen | 官方 the Einstein-Podolsky-Rosen argument（低置信：物理界惯称"EPR 悖论"，由项目定夺） |
| 概率与随机性 | 机会与随机性 | chance-randomness | chance≠probability，条目正是在区分二者 |
| 希尔伯特计划 | （保留） | hilbert-program | 中文维基条目名"希尔伯特计划"，第二轮否决改"纲领" |
| 中国哲学认识论 | 中国哲学中的认识论 | chinese-philosophy-epistemology | 与同组"中国哲学中的形而上学"等体例平行 |
| 中国伦理学 | 中国哲学中的伦理学 | chinese-philosophy-ethics | 同上；避免误读为"中国的伦理学" |
| 布尔戈斯的阿布纳 | 布尔戈斯的阿布内尔 | abner-of-burgos | 与术语表 Abner of Burgos=阿布内尔 统一（或改表，二选一） |
| 非洲哲学（Africana Philosophy） | 非裔哲学 | africana-philosophy | 官方 Africana 与 African 分立，现译撞名 |
| 现代非洲哲学 contemporary | 当代非裔哲学 | africana-contemporary | contemporary=当代；漏译 Africana |
| 阿坎哲学关于人格的看法 | 阿坎哲学中的人格 | akan-person | 官方 Akan Philosophy of the Person，"的看法"为增译 |
| 永恒（immutability） | 不变性 | immutability | 同分类 eternity 已译"永恒"；immutability 是"不变性" |
| 宇宙论证明 / 本体论证明 | 宇宙论论证 / 本体论论证 | cosmological-argument / ontological-arguments | argument=论证；与同分类"道德论证""目的论论证"统一 |
| 实用主义与上帝信仰 | 实用主义论证与上帝信仰 | pragmatic-belief-god | 漏译 arguments |
| 宗教与道德 | 西方哲学中的宗教与道德 (John Hare and Jennifer Herdt) | religion-morality | 漏译 in western philosophy；漏第二作者 |
| 道家/道教 | （保留） | daoism-chad-hansen | 第二轮否决：条目兼覆哲学与宗教两面 |
| 行为体（agency） | 能动性 | agency | 与术语表及文件名 neng-dong-xing 一致 |
| 规范伦理学括注"结果主义、道义论" | "后果主义、义务论" | 分类括注 | 与词条内译法及 SEP 原分类统一 |
| 自然美学 | 环境美学 | environmental-aesthetics | 环境美学为学科标准译名；nature aesthetics 才是"自然美学" |
| 生活美学 | 日常美学 | aesthetics-of-the-everyday | Saito 通行"日常美学"；"生活美学"另有所指 |
| 虚构小说（fiction） | 虚构 | fiction | fiction 不限于小说；子条目同步 |
| 欧陆哲学女性主义 | 欧陆女性主义哲学 | feminist-continental | 语序通顺且不省"哲学" |
| 18 世纪法国美学 | 18 世纪的法国美学 | aesthetics-french-18th | 与"18 世纪的英国美学"统一（德国美学条目一并加"的"） |
| 统治（domination） | 支配 | domination | Pettit non-domination 通行"无支配" |
| 共益物品 | 共同善 | common-good | 政治哲学通行"共同善"；文件名 gong-tong-li-yi 亦需联动 |
| 领土主权与领地正义 | 领土权利与领土正义 | territorial-rights-justice | 同时违反术语表 Territorial Rights=领土权利、Territorial Justice=领土正义 两条 |
| 社会契约论的当代研究方法 | 社会契约论的当代方法 | contractarianism-contemporary | approaches=方法，"研究"为增译；保留"论"以合术语表 social contract=社会契约论 |
| 工作和劳动的哲学研究方法 | 工作和劳动的哲学方法 | work-labor | approaches=方法 |
| 伦理学中的现实主义和可能性主义 | 统一 actualism 译法 | actualism-possibilism-ethics | 现一处"现实主义"一处"实在主义"，且均与 realism 混；第二轮建议"实存主义/可能性主义"，**需项目定夺后全书统一并补术语表** |
| 丘奇/邱奇 | 全书统一（推荐"丘奇"） | church-type-theory 等 | mu-lu-s 内"丘奇类型论/阿隆佐·邱奇/邱奇-图灵论题"三处两形并存；数理逻辑文献通行"丘奇-图灵论题"，中文维基作"邱奇"，**需项目定夺** |

### 5.3 标点与体例

* `西奥多·W ·阿多诺` → `西奥多·W·阿多诺`（"W"与间隔号之间多余空格；文件名 `duow` 为 `duo-w` 粘连）。
* `乔纳森‧爱德华兹`、`彼得‧约翰‧奥利维` → 间隔号 U+2027 改 U+00B7 `·`（全库仅此 2 处）。
* `印度的"二谛 "理论`、`西藏的"二谛 "理论` → 删除右引号前多余空格（两文件 H1 及 mu-lu-s.md 两行共 4 处）。
* 文件名拼音修正（低优先级，需同步链接）：`a/ke-luo-dun-deaer-ke-mai-weng-…`（de-a-er 粘连）→ `ke-luo-dun-de-a-er-ke-mai-weng-…`；`g/…qie-da-mo-er-…`（"伽"应 jia）→ `jia-da-mo-er`；`p/xuan-chuan-publicity-…`（"公开性"误拼"宣传"）→ `gong-kai-xing-publicity-…`；`a/xi-ao-duow-a-duo-nuo-…` → `xi-ao-duo-w-a-duo-nuo-…`。

---

## 六、被复核否决的第一轮建议（请勿按第一轮误改）

以下 25 项经第二轮以独立证据否决，**现行写法可接受**，保留现状：

1. 杨布里科斯（Iamblichus）——中文维基条目名即"杨布里科斯"。
2. 彼得罗·彭波那齐（Pomponazzi）——《世界哲学史》中译对照表即作"彭波那齐"。
3. 总务长菲利普——术语表两处登记一致（如需更通行可另议"菲利普校长"）。
4. 康德的道德哲学——官方标题 moral philosophy 直译准确，与术语表"伦理学=Ethics"分工不冲突。
5. 变化与不一致——"不一致"为 inconsistency 可接受译法。
6. 多的难题——形而上学文献常见表述。
7. 中世纪的超越理论——可读，与术语表不冲突。
8. 变异一元论——术语表首选译名。
9. 利他主义的经验主义研究——术语表 empirical approaches=经验主义研究。
10. 知觉辩护——术语表 Justification 并列登记"证成/辩护"，两行皆合规。
11. 亲知与摹状知识——与"摹状词"术语系统一致。
12. 希尔伯特计划——中文维基条目名。
13. 道家/道教——条目兼覆两面，与"宗教道教"子条目层级区分成立。
14. 弗朗切斯科·帕特里齐——Patrizi 通行即"帕特里齐"。
15. 遗传性特征与获得性特征的区别——SUMMARY 与 mu-lu-s 均有依据（但两文件写法不一致，见 2.2）。
16. 实证道德心理学/经验主义研究并存——术语表两行并列登记，属有意体例。
17. Justification 译法"证成/辩护"并存——术语表有意并列（第 291–292 行），非自相矛盾。
18. 威廉·马克西米利安·冯特——Maximilian 标准中译即"马克西米利安"。
19. 19 世纪苏格兰哲学留"欧洲哲学"——与 18 世纪条目成对，无更优子类。
20. 基督教传统中的情感留"宗教学 > 基督教"——与"X in Christian thought"条目族模式吻合。
21. 模态认识论留"元认识论"——本身即认识论分支。
22. 中世纪的此性理论英文标题——官方标题本就截短为 medieval theories of，无需补全。
23. 雅可比条目缺右括号——假阳性，仓库内括号完好。
24. 术语表 Philoponus/Structural Realism 条目——术语表本身正确（真错误在 SUMMARY 别名行，见第七节）。
25. 共益物品作者缺漏——官方与仓库一致（Julian Reiss），无缺漏。

---

## 七、术语表与别名行修正（第三轮确认）

1. **`SUMMARY.md:181`** `*菲洛劳斯——见菲洛劳斯 Philoponus — see Philoponus`：中文误作"菲洛劳斯"（毕达哥拉斯学派 Philolaus），应为"菲洛波诺斯/斐洛波努斯"（Philoponus）。术语表第 361–362 行已明确区分并警告勿混。另正文用"菲洛波诺斯"、术语表用"斐洛波努斯"，建议统一"菲/斐"之一。
2. **`SUMMARY.md:2179`** `*结构主义——结构现实主义 structural — see structural realism`：应作"结构实在论"（术语表第 475 行明确"结构现实主义"是国际关系理论译名，勿混）。
3. 术语表 `Sociobiology|生物社会学`（第 431 行）改"社会生物学"（E. O. Wilson 通行中译；词条正文已作"社会生物学"）。

## 八、遗留事项与局限

1. **官方目录未列但条目在线**：continental-rationalism（大陆理性主义）——SEP 自身目录遗漏，本地可加译注。
2. **官方条目退休**：time-experience 已由 consciousness-temporal（时间意识）取代，建议补译并加"已退休"注。
3. **两处需项目定夺的译名**：actualism 统一译法（建议"实存主义/可能性主义"或另定）；Church 统一"丘奇"或"邱奇"。
4. **文件名联动改名**：第五节 5.3 与 5.2 中涉及文件名的条目（共同善、公开性、伽达默尔、阿多诺、阿尔克迈翁、遗传漂变等）改名时需同步 SUMMARY、mu-lu-s 与全部引用链接，建议单独一批处理。
5. **分类建议落实顺序建议**：先做第四节分类体系调整（新增"实用主义""计算机与人工智能哲学"、改名"上帝存在的论证"等），再按第三节移动词条，最后按附录 A 补录缺失词条，避免二次返工。
6. 本建议书基于 2026-10-26 官方数据；SEP 条目持续更新，作者名单（附录 B）建议在实施时再刷新一次。

---

## 九、分类原则（哲学史／哲学理论两分）下的修订意见

**对分类原则的理解**：本目录采用两分法——

* **哲学史部（人物及其理论）**：收人物条目、学派与运动、时期通论，以及"康德的伦理学""罗素的逻辑原子主义"式人物专题；按时代—传统—学派组织（古代希腊→中世纪→文艺复兴→早期近代→现代西方→马克思主义；中国哲学与区域哲学同属此部）。
* **哲学理论部**：收主题条目（认识论、形而上学、语言哲学与逻辑学、心灵哲学、科学哲学、伦理学、美学、政治哲学……），按学科组织，不收人物。

若以此原则衡量，**第三节的建议需分两类对待**：

### 9.1 主题条目：第三节建议全部维持

第三节中凡主题条目（真理及七种真理理论、泛指概括、严格指示词、事态、遵循规则、私人语言、逻辑形式、思维语言假说、意向性、本体论承诺、确定物与可确定物、无限、特普、事件、动物主义、溯因、偏好、泛指概括、谬误、相对主义、异化、颜色、恐怖主义、可行能力、公共证成等）均应移入理论部对应学科——这与两分原则完全一致，无需改判。

### 9.2 人物条目：改判为"归哲学史部"，不按主题散入理论部

第三节中约 30 条人物建议是在"主题优先"思路下给出的；按两分原则应改判如下：

| 人物（现位置） | 第三节原建议（主题优先） | **两分原则下的建议** |
| --- | --- | --- |
| 黑尔、普里查德、罗斯、史蒂文森、布劳德、伯林、奇泽姆、古德曼、格莱斯、刘易斯、塞拉斯、唐纳德·卡里·威廉姆斯、约翰·安德森、塞缪尔·亚历山大、西尔万 | 分散到元伦理学、认识论、语用学、自由主义、美学、模态实在论等 | **全部移入"后期分析哲学"**（20 世纪分析哲学家；该类现仅 4 条，正好充实） |
| 维特根斯坦 | 语言哲学与逻辑学 > 逻辑学家 | 移入"前期分析哲学"（《逻辑哲学论》期）并加互见说明（或后期，由项目定夺） |
| 卢卡谢维奇、塔尔斯基、雷斯涅夫斯基、布尔、约翰·库克·威尔逊 | 逻辑学家／逻辑史／语义学 | 留在历史侧："前期分析哲学"（四人皆 19–20 世纪逻辑学家，与弗雷格、罗素同代）或保留"逻辑学家"人物册（见 9.3） |
| 特瓦尔多夫斯基 | 布伦塔诺学派 | 维持（布伦塔诺学派本就是历史侧学派类，与原则一致） |
| 伽利略、亥姆霍兹、亚历山大·冯·洪堡 | 科学哲学 > 科学家 | 严格两分下：伽利略→"文艺复兴与早期近代哲学 > 科学革命与自然哲学"；亥姆霍兹、洪堡→"现代西方哲学 1750-1900"；或保留"科学家"人物册（见 9.3） |
| 格劳秀斯 | 法哲学 | "启蒙运动和早期现代哲学 1600-1750"（17 世纪自然法人物；其逻辑学家归属无论何案均应撤销） |
| 约翰·奥斯丁（法学家） | 法哲学 | "现代西方哲学 1750-1900"（19 世纪）；或保留法哲学人物册 |
| 冯特、费希纳、哈特利、H. H. 普莱斯 | 心理学与心灵哲学／道德心理学 | 冯特（1832–1920）、费希纳（1801–1887）、哈特利（1705–1757）、普莱斯（1723–1791）按时代分归"现代西方哲学"与"启蒙运动和早期现代哲学"；或四人合设人物册 |
| 施图尔姆、克拉克、柯林斯、爱德华兹、杜博斯 | 唯理论／经验论／法国哲学／早期近代 | 维持（本就归哲学史部各时期，与原则一致） |
| 伊本·达乌德、伊本·埃兹拉 | 犹太哲学 | 维持（传统=史部） |
| 皮科、孔多塞条目 | 文艺复兴／女性主义哲学 | 维持 |

### 9.3 人物册（逻辑学家／科学家／经济学家／政治家／心理学家／神学家／神秘学家）的处置——两案并列，请定夺

现状：六个"人物册"嵌在理论部各学科之下，册内混入主题条目与错置人物：

* 逻辑学家（12）内含格劳秀斯（非逻辑学家）；λ 演算（主题）在科学家册；玻尔兹曼统计物理研究（专题）在科学家册；政治家册内含"原初状态""反思平衡"（罗尔斯子条目）；前期分析哲学内含摹状词、逻辑构造、罗素悖论、《数学原理》符号等主题条目。

**方案 A（严格两分，推荐）**：人物册逐步解散，人物按时代归哲学史部（见 9.2），主题条目移理论部；理论部内一律不设人物条目。优点：原则彻底、目录自洽；缺点：改动面大（约 50 条），图灵、哥德尔、邱奇等人物的时代归宿需逐一论证。

**方案 B（保留人物册，正名净化）**：承认"领域人物册"为两分法的例外约定，做三件事：①册内主题条目移走（λ 演算→逻辑史、玻尔兹曼研究→物理学哲学、原初状态与反思平衡→罗尔斯条目处、《数学原理》与牛顿的哲学→随人物）；②明显错置人物移走（格劳秀斯出逻辑学家册）；③册名统一标注人物属性（如"人物：逻辑学家"），并在编委会日志写明该约定。优点：改动小、领域聚集便于查阅；缺点：两分原则留有例外。

**无论何案均应做的**：以"分析哲学兜底类"的人物充实"后期分析哲学"（现仅 4 条），使兜底类得以删除；"前期分析哲学"内的主题条目（摹状词、逻辑构造、罗素悖论、确定物与可确定物、弗雷格定理和算术基础、《数学原理》中的符号等）按主题移入理论部（语义学、数学哲学、本体论），人物与人物专题留下。

### 9.4 配套建议

1. 在 README 或编委会日志中把"哲学史（人物及其理论）／哲学理论"两分原则成文化，并说明人物册的取舍约定，避免后续贡献者按不同直觉归档。
2. 跨传统主题条目定一条规则：传统内专题（如"儒学中的性别""中国哲学中的认识论"）归传统史部对应通论类；现代理论专题（如"性别与酷儿哲学"）归理论部。第三节 3.10 已按此执行。
3. 落实顺序：先删兜底类充实前后期分析哲学（人物就地分配）→ 再按第三节移动主题条目 → 按第四节调整分类体系 → 最后按附录 A 补录缺失的 800 条。

## 十、上游（SEP）同步规则与批准记录（2026-10-26 增补）

**批准记录**：本建议书经三轮核查与项目负责人全面批准。批准以"先与上游同步"为前提，已于 2026-10-26 履行：当日两次全新抓取官方 contents.html（含加随机参数的防缓存抓取），SHA256 与建议书所用快照完全一致（主条目 1872、别名 654、零漂移），即建议书的比对基准就是当前上游状态。

### 10.1 同步机制（已建）

| 组件 | 位置 | 说明 |
| --- | --- | --- |
| 检查脚本 | `.github/scripts/sep_sync_check.py` | 抓取官方目录并解析（主条目＋别名），与已提交基线比对，输出 `status.json` 与 `report.md`；`--write-baseline` 用于更新基线。只报告，不改动任何内容文件 |
| 基线快照 | `.github/sep-baseline/official-snapshot.json` | 批准时的上游状态（2026-10-26，主 1872＋别名 654）。每次人工落地变化后更新并随改动提交 |
| 定时工作流 | `.github/workflows/sep-sync-check.yml` | 每周一 18:30 UTC 自动运行（可手动触发）；发现漂移或异常时创建/更新 issue「SEP 上游变化同步报告」，附完整报告与受影响本地文件提示；不自动 commit/push |

### 10.2 同步规程（每周期）

1. 工作流检测到上游变化 → 自动开 issue（同一期间只更新同一 issue，不刷屏）。
2. **人工核对**变化类型：新条目（译名登记→翻译→加入 SUMMARY 与 mu-lu-s 对应分类）、作者变更（更新署名，文件名内嵌作者者需同步改名）、标题变更（改 SUMMARY 一处，H1 由 CI 同步）、撤下条目（**切勿自动删除**，先核实是否真被撤下；撤下条目保留并加译注，或按补译新条目处理）。
3. 落地后运行 `python .github/scripts/sep_sync_check.py --write-baseline` 更新基线，与改动一并提交。
4. 基线更新后的下一次运行应报 clean，否则说明仍有未处理漂移。

### 10.3 极端情况处置

| 情况 | 检测 | 处置 |
| --- | --- | --- |
| 抓取失败/超时/限流 | 脚本重试 3 次（退避），仍失败报 `fetch-error` | 只开 issue 提示，不改任何文件；人工重跑 workflow_dispatch |
| 官方页面改版导致解析失败 | 护栏：解析主条目 < 1500 即报 `parse-error` | 解析器需人工更新；期间不产生假漂移报告 |
| 条目退休（页面 404 但仍在目录，或目录撤下但页面仍在） | 目录比对＋人工点开核实 | 参照 time-experience 先例：保留本地条目加"已退休/由 X 取代"译注，安排补译新条目 |
| 别名条目消失（如 recursion、consent 等 4 例先例） | 别名比对 | 人工核实后决定去留，可加译注保留（如"递归"梗条目） |
| 官方目录重复 slug | 脚本列为 `duplicate_slugs` | 报告人工判断，不自动择一 |
| 变音符/HTML 实体差异造成的假作者变更 | 归一化（NFKD 去变音符、实体解码、and/逗号切分取集合）比较 | 若仍报变更即为真变更 |
| 大小写敏感 | Windows 磁盘不敏感而 Linux 构建敏感 | 改名时逐字符核对磁盘真实文件名，引用与磁盘完全一致 |
| 并发运行重叠 | workflow `concurrency` 组串行化 | 无需人工干预 |
| issue 刷屏 | 同名 issue 只更新不新建 | 长期未处理时可人工关闭旧 issue，新周期自动新建 |
| 主题条目在官方无分类元数据 | ——（SEP 现行网站无分类页） | 新条目的 mu-lu-s 归类由人工按本建议书第三、九节的原则判定 |

### 10.4 与建议书实施的关系

本建议书第三～九节的修改建议按 9.4 顺序实施（充实后期分析哲学→移动主题条目→调整分类体系→补录 800 条）；实施期间若同步工作流报告上游变化，优先处理漂移，避免在旧数据上继续落地。

### 10.5 实施进度（干执行记录）

**2026-10-27，项目负责人确认分类原则**：哲学史按"区域→时期→学派/组织/流派→人物→人物专题"层级；神学独立（基督教——注意与中世纪哲学区分、佛教、伊斯兰、犹太教），道教、中国佛教、藏传佛教等民族性宗教除外（留区域）；仅改目录本身，不动文件路径。

* **干执行一**（8cb7b4c9）：新增"西方哲学史"区域包裹（10 个时期 H1 降为 H2，学派 H2 降为 H3，与区域哲学史层级对齐）；新建"神学与宗教哲学"（神学教义通论／基督教／上帝存在的论证／神学家／神秘学家／佛教（印度佛教）／宗教哲学与宗教学通论），宗教学解散；中国佛教（含藏传佛教）与道教以"中国佛教与道教"归入中国哲学；心理学家四人（冯特、费希纳、哈特利、H. H. 普莱斯）归时期直属；清理空的嵌套实用主义与伦理学>心理学家标题。
* **干执行二**（f25d0108）：目录标题修复约 190 处（译名、标题统一、别名传播式替换）＋作者名单对齐官方 263 处，覆盖 SUMMARY.md 与 mu-lu-s.md，仅标题文本、不动路径。
* **干执行三**（9f989efe）：核查收尾——"二谛"引号前空格两文件各 2 处、科学实在论括注转义斜杠、markdownlint 块间空行；两目录文件 lint 清零，条目守恒 1814。
* **并行会话协同**：同期另一会话在同一分支实施了语义化路径改名、H3 细分（笛卡尔、逻辑实证主义、数理逻辑、量子力学、进化论、人工智能哲学等）与术语一致性门禁；本会话所有编辑均以标题/标题行定位、逐批原子提交，未触碰路径与并行会话文件。
* **尚待执行**：附录 A 的 800 条补录进分类目录；人物册（逻辑学家/科学家/经济学家/政治家）方案 A/B 的最终定夺与净化；需改文件名的译名（伽达默尔拼音、公开性、共同善等）单独一批；actualism 与 Church 译名的项目定夺。

以下附录由脚本自动生成（数据源：script/tmp/toc.json、official.json、match.json，2026-10-26）。

## 附录 A：未纳入分类目录的词条名单（800 条）

以下词条存在于 SUMMARY.md 但不在 mu-lu-s.md 中（已排除 README.md、mu-lu-s.md 两个项目文件；"前言""关于"两分区已在分类目录内）。按 SUMMARY 字母分区分组，仅列标题（作者略）。


**A（86 条）**

偶然属性——见本质属性与偶然属性 accidental properties — see essential vs. accidental properties、共同——见行为体：共享行为体 joint — see agency: shared、逻辑 ——见逻辑学：行动的逻辑 logic of — see logic: action、超距作用——见量子力学：量子力学中的超距作用 action at a distance — see quantum mechanics: action at a distance in、现实主义——见现实主义与可能性主义辩论 actualism — see possibilism-actualism debate、罗马的吉尔斯——见罗马的吉尔斯 Aegidius Romanus — see Giles of Rome、埃奈西德谟——见怀疑论：古代怀疑论 Aenesidemus — see skepticism: ancient、美学 aesthetics、门罗·C.比厄斯利的美学——见门罗·C.比厄斯利：比厄斯利的美学 Beardsley — see Beardsley, Monroe C.: aesthetics、柯林武德——见罗宾·乔治·柯林武德：柯林武德的美学 Collingwood — see Collingwood, Robin George: aesthetics、克罗齐——见贝内德托·克罗齐：克罗齐的美学 Croce — see Croce, Benedetto: aesthetics、文化挪用——见文化遗产伦理 cultural appropriation — see cultural heritage, ethics of、艺术的定义——见艺术的定义 definition of art — see art, definition of、杜威——见约翰·杜威：杜威的美学 Dewey — see Dewey, John: aesthetics、女性主义——见女性主义哲学介入：女性主义美学 feminist — see feminist philosophy, interventions: aesthetics、伽达默尔——见汉斯-格奥尔格·伽达默尔：伽达默尔的美学 Gadamer — see Gadamer, Hans-Georg: aesthetics、古德曼——见纳尔逊·古德曼：古德曼的美学 Goodman — see Goodman, Nelson: aesthetics、黑格尔——见格奥尔格·威廉·弗里德里希·黑格尔：黑格尔的美学 Hegel — see Hegel, Georg Wilhelm Friedrich: aesthetics、海德格尔——见马丁·海德格尔：海德格尔的美学 Heidegger — see Heidegger, Martin: aesthetics、休谟——见大卫·休谟：休谟的美学 Hume — see Hume, David: aesthetics、日本——见日本哲学：日本美学 Japanese — see Japanese Philosophy: aesthetics、柏拉图——见柏拉图：柏拉图的美学 Plato — see Plato: aesthetics、叔本华——见阿图尔·叔本华：叔本华的美学 Schopenhauer — see Schopenhauer, Arthur: aesthetics、维特根斯坦——见路德维希·维特根斯坦：维特根斯坦的美学 Wittgenstein — see Wittgenstein, Ludwig: aesthetics、美学价值——见美学的概念 aesthetic value — see aesthetic, concept of the、非洲哲学 African Philosophy、科学哲学中的基于主体的模型——见科学哲学中基于主体的模型 agent-based modeling in philosophy of science — see modeling in the philosophy of science, agent-based、行动者相关与行动者中立的理由——见行动的原因：行动者中立与行动者相关 agent-relative vs. agent-neutral reasons — see reasons for action: agent-neutral vs. agent-relative、不可知论与无神论——见无神论与不可知论 agnosticism and atheism — see atheism and agnosticism、阿格里帕——见怀疑论：古代怀疑论 Agrippa — see skepticism: ancient、阿坎哲学 Akan Philosophy、不自制——见意志薄弱 akrasia — see weakness of will、阿摩尼阿斯·萨卡斯——见普罗提诺 Ammonius Saccas — see Plotinus、类比 analogy、阿那克萨库——见皮浪 Anaxarchus — see Pyrrho、罗得岛的安德罗尼柯——见亚里士多德的评注者 Andronicus of Rhodes — see Aristotle, commentators on、动物 animal、道德反实在论——见道德反实在论 anti-realism, moral — see moral anti-realism、后验知识——见先验论证和先验知识 a posteriori knowledge — see a priori justification and knowledge、表象与实在 appearance vs. reality、知觉的认识论问题——见知觉：知觉的认识论问题 epistemological problems of perception — see perception: epistemological problems of、怀疑论——见怀疑论 skepticism — see skepticism、阿拉伯和伊斯兰哲学相关 Arabic and Islamic Philosophy, disciplines in、阿拉伯和伊斯兰哲学中的历史和方法论相关 Arabic and Islamic Philosophy, historical and methodological topics in、阿拉伯和伊斯兰哲学中的特色主题 Arabic and Islamic Philosophy, special topics in、伊本·凯姆那——见伊本·凯姆那 Ibn Kammūna — see Ibn Kammūna、精诚兄弟社——见精诚兄弟社 Ikhwân al-Safâ’ — see Ikhwân al-Safâ’、德性——见伦理学：古代伦理学 arete — see ethics: ancient、认知规范的论证 arguments for epistemic norms、认知效用——见关于认知规范的认知效用论证 epistemic utility — see epistemic utility arguments for epistemic norms、亚里士多德主义 Aristotelianism、亚里士多德的评注者——见亚里士多德的评注者 commentators on Aristotle — see Aristotle, commentators on、阿芙罗蒂西亚的亚历山大——见阿芙罗蒂西亚的亚历山大 Alexander of Aphrosias — see Alexander of Aphrodisias、赫尔米亚的阿莫尼俄斯——见赫尔米亚的阿莫尼俄斯 Ammonius — see Ammonius、大卫——见大卫 David — see David、埃利亚斯——见埃利亚斯 Elias — see Elias、奥林匹奥多罗斯——见奥林匹奥多罗斯 Olympiodorus — see Olympiodorus、菲洛劳斯——见菲洛劳斯 Philoponus — see Philoponus、辛普利修斯——见辛普利修斯 Simplicius — see Simplicius、关于亚里士多德的一般性主题 Aristotle, General Topics、亚里士多德的特色主题 Aristotle, Special Topics、弗朗索瓦-马里‧阿鲁埃——见伏尔泰 Arouet, François-Marie — see Voltaire、艺术 art、自动推理——见推理：自动推理 automated reasoning — see reasoning: automated、信念的形式化表述——见信念的形式化表述 belief representation — see belief, formal representations of、中文房间实验——见中文房间实验 Chinese room argument — see Chinese room argument、联结主义——见联结主义 connectionism — see connectionism、可辩驳推理——见推理：可辩驳推理 defeasible reasoning — see reasoning: defeasible、框架问题——见框架问题 frame problem — see frame problem、图灵测试——见图灵测试 Turing test — see Turing test、体态——见时态与体态 aspect — see tense and aspect、原子论 atomism、属性——见属性 attributes — see properties、听知觉——见知觉：听知觉 auditory perception — see perception: auditory、法律——见法律义务和权威 legal — see legal obligation and authority、自动推理——见推理：自动推理 automated reasoning — see reasoning: automated、自主权 autonomy、知情同意——见知情同意 and informed consent — see informed consent、伊本·鲁世德——见伊本·鲁世德（阿威罗伊） Averroes — see Ibn Rushd、自然哲学——见伊本·鲁世德的自然哲学 natural philosophy — see Ibn Rushd: natural philosophy、所罗门·伊本·盖比鲁勒——见所罗门·伊本·盖比鲁勒（阿维斯布隆） Avicebron — see Ibn Gabirol, Solomon、阿维森纳——见伊本·西那（阿维森纳） Avicenna — see Ibn Sina、逻辑学——见伊本·西那（阿维森纳）的逻辑学 logic — see Ibn Sina: logic、形而上学——见伊本·西那（阿维森纳）的形而上学 metaphysics — see Ibn Sina: metaphysics、自然哲学——见伊本·西那（阿维森纳）的自然哲学 natural philosophy — see Ibn Sina: natural philosophy、身体意识——见身体意识 awareness, bodily — see bodily awareness


**B（35 条）**

亚历山大·贝恩——见苏格兰哲学： 19 世纪苏格兰哲学 Bain, Alexander — see Scottish Philosophy: in the 19th century、门罗·C.比厄斯利 Beardsley, Monroe C、詹姆斯·比蒂——见苏格兰哲学： 18 世纪苏格兰哲学 Beattie, James — see Scottish Philosophy: in the 18th Century、存在——见存在 being — see existence、存在与变化 ——见时间 being and becoming — see time、现代物理学——见空间与时间：现代物理学中的存在与变化 in modern physics — see space and time: being and becoming in modern physics、自我定位——见自我定位信念 self-locating — see self-locating beliefs、生物多样性——见生态学：生物多样性 biodiversity — see ecology: biodiversity、生物演化 theories of、生物信息——见信息：生物信息 biological information — see information: biological、生物学 biology、保育——见保育生物学 conservation — see conservation biology、发育——见发育生物学 developmental — see developmental biology、分子——见分子生物学 molecular — see molecular biology、还原——见科学还原论：生物学中的还原论 reduction in — see reduction, scientific: in biology、目的论观念——见目的论：生物学中的目的论观念 teleological notions in — see teleology: teleological notions in biology、生物学哲学 biology, philosophy of、女性主义——见女性主义介入：女性主义生物学哲学 feminist — see feminist philosophy, interventions: philosophy of biology、休·布莱尔——见苏格兰哲学：18 世纪苏格兰哲学 Blair, Hugh — see Scottish Philosophy: in the 18th Century、身体——见实体 body — see substance、尼尔斯·玻尔 Bohr, Niels、逻辑代数 Boolean algebra、脑死亡——见死亡：死亡的定义 brain death — see death: definition of、缸中之脑——见怀疑论：怀疑论和内容外在主义 brains in a vat — see skepticism: and content externalism、托马斯·布朗——见苏格兰哲学：19 世纪苏格兰哲学 Brown, Thomas — see Scottish Philosophy: in the 19th century、佛教 Buddhism、禅宗（Chan）——见中国哲学：禅宗 Chan — see Chinese Philosophy: Chan Buddhism、印度佛教中的伦理学——见印度佛教中的伦理学 ethics in Indian Buddhism — see ethics: in Indian Buddhism、印度佛教哲学中的心灵——见印度佛教哲学中的心灵 mind in Indian Buddhist Philosophy — see mind: in Indian Buddhist Philosophy、天台宗——见中国哲学：天台宗 Tiantai — see Chinese Philosophy: Tiantai Buddhism、禅宗（Zen）——见日本哲学：日本禅宗哲学 Zen — see Japanese Philosophy: Zen Buddhism、华严宗——见中国哲学：华严宗 Buddhism: Huayan — see Chinese Philosophy: Huayan Buddhism、束理论——见实体 bundle theory — see substance、詹姆斯·伯内特（蒙博多勋爵）——见 18 世纪苏格兰哲学 Burnett, James \[Lord Monboddo\] — see Scottish Philosophy: in the 18th Century、约瑟夫·巴特勒 Butler, Joseph


**C（70 条）**

爱德华·凯尔德——见苏格兰哲学：19 世纪苏格兰哲学 Caird, Edward — see Scottish Philosophy: in the 19th century、卡利克勒斯——见柏拉图：卡利克勒斯和塞拉西马柯 Callicles — see Plato: Callicles and Thrasymachus、乔治·坎贝尔——见苏格兰哲学：18 世纪苏格兰哲学 Campbell, George — see Scottish Philosophy: in the 18th Century、格肖姆·卡迈克尔——见苏格兰哲学：18 世纪苏格兰哲学 Carmichael, Gershom — see Scottish Philosophy: in the 18th Century、决疑论——见推理：道德推理 casuistry — see reasoning: moral、因果决定论——见决定论：因果决定论 causal determinism — see determinism: causal、因果关系 causation、心理——见心理因果关系 mental — see mental causation、逆因果性——见量子力学：量子力学中的逆因果关系 retrocausality in quantum mechanics — see quantum mechanics: retrocausality、审查——见色情：色情与审查 censorship — see pornography: and censorship、其他条件不变律——见自然法则：其他条件不变律 ceteris paribus laws — see laws of nature: ceteris paribus、概率 chance、变化 change、易经：中国哲学——见中国哲学：中国易经哲学 change: Chinese philosophy of — see Chinese Philosophy: philosophy of change、智利 Chile、嵌合体、人类与非人类——见生物医学伦理学：人类与非人类嵌合体 chimeras, human/non-human — see ethics, biomedical: chimeras, human/non-human、中国儒学 Chinese Confucianism、中国伦理学——见中国哲学：中国伦理学 Chinese ethics — see Chinese Philosophy: ethics、中国哲学 Chinese Philosophy、与西方哲学相比——见比较哲学：中西哲学 Compared to Western Philosophy — see comparative philosophy: Chinese and Western、孔子——见孔子 Confucius — see Confucius、道家/道教——见道家/道教 Daoism (Taoism) — see Daoism、老子——见老子 Laozi — see Laozi、孟子——见孟子 Mencius — see Mencius、玄学——见玄学 Neo-Daoism — see Neo-Daoism、王阳明——见王阳明 Wang Yangming — see Wang Yangming、荀子——见荀子 Xunzi — see Xunzi、庄子——见庄子 Zhuang Zi — see Zhuangzi、朱熹——见朱熹 Zhu Xi — see Zhu Xi、社会选择——见社会选择理论 choice, social — see social choice theory、邱奇论题——见邱奇-图灵论题 Church’s Thesis — see Church-Turing Thesis、亚历山大的克莱门特——见古代哲学学述 Clement of Alexandria — see doxography of ancient philosophy、气候正义——见正义：气候正义 climate justice — see justice: climate、临床研究伦理——见生物医学伦理学：临床研究伦理 clinical research, ethics of — see ethics, biomedical: clinical research、认知 cognition、动物——见动物：动物认知 animal — see animal: cognition、共同原因原理——见汉斯·赖兴巴赫的共同原因原理 common cause principle — see Reichenbach, Hans: common cause principle、比较哲学 comparative philosophy、生物医学决策中的能力——见决策能力 competence, in biomedical decision-making — see decision-making capacity、复杂度 complexity、可计算性——见可计算性和复杂度 computability and — see computability and complexity、计算性——见计算复杂性理论 computational — see computational complexity theory、组合、模糊性——见关于多的难题 composition, the vagueness of — see many, problem of、计算 computation、计算语言学——见语言学：计算语言学 computational linguistics — see linguistics: computational、心灵计算理论——见心灵：心灵计算理论 computational theory of mind — see mind: computational theory of、计算机 computing、逻辑——见逻辑学：条件句的逻辑 logic of — see logic: conditionals、马里·让·安托万·尼古拉·德·卡里塔，孔多塞侯爵 Condorcet, Marie-Jean-Antoine-Nicolas de Caritat, Marquis de、Confucianism 儒学、日本——见日本哲学：日本儒学 Japanese — see Japanese Philosophy: Confucian、韩国——见韩国哲学：韩国儒学 Korean — see Korean Philosophy: Confucianism、孟子——见孟子 Mencius — see Mencius、新儒学——见中国儒学：新儒学 Modern Confucianism — see Chinese Confucianism: Modern Confucianism、宋明——见中国哲学：宋明理学 Song-Ming — see Chinese Philosophy: Song-Ming Confucianism、王阳明——见王阳明 Wang Yangming — see Wang Yangming、荀子——见荀子 Xunzi — see Xunzi、朱熹——见朱熹 Zhu Xi — see Zhu Xi、连接词 connectives、动物——见动物：动物意识 animal — see animal: consciousness、同意——见政治义务 consent — see political obligation、建构主义 constructivism、连续统假设——见集合论：连续统假设 continuum hypothesis — see set theory: continuum hypothesis、道德与约定区分——见道德与约定的区分 moral/conventional distinction — see moral/conventional distinction、宇宙学 cosmology、反事实条件句——见条件句：反事实 counterfactuals — see conditionals: counterfactual、对应体理论——见可能对象 counterpart theory — see possible objects、批判种族理论——见批判种族哲学 critical race theory — see critical philosophy of race、贝内德托·克罗齐 Croce, Benedetto、文化演化——见进化：文化演化 cultural evolution — see evolution: cultural


**D（50 条）**

老子——见老子 Laozi — see Laozi、玄学——见玄学 Neo-Daoism — see Neo-Daoism、庄子——见庄子 Zhuang Zi — see Zhuangzi、查尔斯·达尔文 Darwin, Charles、从《物种起源》到《人类的由来》——见进化：达尔文：从《物种起源》到《人类的由来》 from the Origin of Species to the Descent of Man — see evolution: from the Origin of Species to the Descent of Man、此在——见马丁·海德格尔 Dasein — see Heidegger, Martin、亚伯拉罕·伊本·达乌德——见亚伯拉罕·伊本·达乌德 Daud, Abraham Ibn — see Ibn Daud, Abraham、西蒙·德·波伏娃——见西蒙·德·波伏娃 de Beauvoir, Simone — see Beauvoir, Simone de、欺骗 deception、定义——见谎言与欺骗：谎言与欺骗的定义 definition of — see lying and deception: definition of、自我——见自我欺骗 self — see self-deception、期望效用的理性选择理论——见理性选择的规范理论：理性选择的规范理论：预期效用 expected utility theories of rational choice — see rational choice, normative: expected utility、非期望效用的理性选择理论——见理性选择的规范理论：理性选择的规范理论：预期效用的替代理论 non-expected-utility theories of rational choice — see rational choice, normative: rivals to expected utility、理查德·戴德金 Dedekind, Richard、科学的界定——见科学：科学与伪科学 demarcation of science — see science: and pseudo-science、演绎 demonstration、亚里士多德的理论——见亚里士多德的特色主题：亚里士多德的逻辑学 Aristotle’s theory of — see Aristotle, General Topics: logic、指示词——见指代词 demonstratives — see indexicals、直指——见指称 denotation — see reference、义务伦理学——见伦理学：义务伦理学 deontological ethics — see ethics: deontological、情感理论——见情感：17 世纪和 18 世纪的情感理论 theory of emotion — see emotion: 17th and 18th century theories of、设计论证——目的论：上帝存在的目的论论证 design, argument from — see teleology: teleological arguments for God’s existence、决定论 determinism、古代的理论——见自由：古代自由与决定论理论 ancient theories of — see freedom: ancient theories of、理论——见生物发育：生物发育的理论 theories of — see biological development: theories of、认识论——见数学中的视觉化思维：数学中的视觉思维认识论 epistemology of — see visual thinking in mathematics: epistemology of、黑格尔的辩证法——见格奥尔格·威廉·弗里德里希·黑格尔的辩证法 dialectics, Hegel’s — see Hegel, Georg Wilhelm Friedrich: dialectics、第欧根尼·拉尔修——见古代哲学学述 Diogenes Laertius — see doxography of ancient philosophy、亚略巴古的狄奥尼修斯——见伪狄奥尼修斯 Dionysius the Areopagite — see Pseudo-Dionysius the Areopagite、残疾 disability、女性主义视角——见女性主义哲学主题：女性主义对残疾的观点 feminist perspectives on — see feminist philosophy, topics: perspectives on disability、道德——见道德分歧 moral — see moral disagreement、疾病——见健康 disease — see health、双重论证——见智者 Dissoi Logoi — see Sophists, The、分配正义——见正义：分配正义 distributive justice — see justice: distributive、国际——见正义：全球分配正义 international — see justice: international distributive、多样性 diversity、宗教——见宗教多样性 religious — see religious diversity、神 divine、命令论——见神学意志主义 command theory — see voluntarism, theological、预知与自由意志——见自由意志：预知与自由意志 foreknowledge and free will — see free will: divine foreknowledge and、自由——见自由：神的自由 freedom — see freedom: divine、隐藏——见神的隐藏 hiddenness — see hiddenness of God、天意——见神意 providence — see providence, divine、启示——见神启 revelation — see revelation, divine、单纯——见简单性：神圣单纯性 simplicity — see simplicity: divine、婚姻和同居伴侣——见婚姻和同居伴侣 domestic partnership and marriage — see marriage and domestic partnership、詹姆斯·邓巴——见苏格兰哲学：18 世纪苏格兰哲学 Dunbar, James — see Scottish Philosophy: in the 18th Century、动态认知逻辑——见逻辑学——动态认知逻辑 dynamic epistemic logic — see logic: dynamic epistemic、动态语义——见语义：动态语义 dynamic semantics — see semantics: dynamic


**E（73 条）**

埃克哈特大师——见埃克哈特大师 Eckhart, Meister — see Meister Eckhart、生态遗传学——见遗传学：生态遗传学 ecological genetics — see genetics: ecological、保育生物学——见保育生物学 conservation biology — see conservation biology、经济学 economics、拉姆齐与代际福利经济学：见弗兰克·拉姆齐：拉姆齐与代际福利经济学 Ramsey and intergenerational welfare economics — see Ramsey, Frank: and intergenerational welfare economics、阿尔伯特·爱因斯坦 Einstein, Albert、空穴论证——见空间与时间：空穴论证 the hole argument — see space and time: the hole argument、早期中国哲学——见早期中国哲学中的情 in Early Chinese philosophy — see Chinese Philosophy: emotions in early Chinese Philosophy、虚构作品的回应——见虚构：虚构作品引起的情感反应 responses to fiction — see fiction: emotional responses to、经验主义研究 empirical approaches、利他主义——见利他主义：利他主义的经验主义研究 altruism — see altruism: empirical approaches、道德——见道德品质：道德品质的经验主义研究 character, moral — see character, moral: empirical approaches、规范认知心理学——见规范认知心理学 psychology of normative cognition — see normative cognition, psychology of、经验主义——见理性主义与经验主义 empiricism — see rationalism vs. empiricism、构建——见构建经验主义 constructive — see constructive empiricism、蕴含——见逻辑蕴涵 entailment — see logical consequence、熵 entropy、信息处理——见信息处理：信息加工与热力学熵 and information processing — see information processing: and thermodynamic entropy、认知基础关系——见认知基础关系 epistemic basing relation — see basing relation, epistemic、认识论上的自我怀疑——见认识论上的自我怀疑 epistemic self-doubt — see self-doubt, epistemic、语境主义——见认识的语境论 contextualism in — see contextualism, epistemic、女性主义——见女性主义哲学介入：女性主义认识论与科学哲学 feminist — see feminist philosophy, interventions: epistemology and philosophy of science、古典印度哲学——见古典印度哲学：古典印度哲学认识论 in classical Indian philosophy — see Indian Philosophy (Classical): epistemology、道德——见道德认识论 moral — see moral epistemology、道德先验主义——见道德认识论：道德认识论中的先验主义 moral, a priorism in — see moral epistemology: a priorism in、可靠主义——见可靠主义认识论 reliabilist — see reliabilist epistemology、社会女性主义——见女性主义哲学介入：女性主义社会认识论 social feminist — see feminist philosophy, interventions: social epistemology、实在本质——见约翰·洛克：约翰·洛克的实在本质 essence, real — see Locke, John: on real essence、本质属性——见本质属性与偶然属性 essentialism — see essential vs. accidental properties、伦理学 ethics、实在主义和可能性主义——见伦理学中的实在主义和可能性主义 actualism and possibilism — see actualism and possibilism in ethics、信念——见信念伦理 of belief — see belief, ethics of、中国——见中国哲学：中国伦理学 Chinese — see Chinese Philosophy: ethics、女性主义——见女性主义哲学介入：女性主义伦理学 feminist — see feminist philosophy, interventions: ethics、人格同一性——见人格同一性：人格同一性与伦理学 and personal identity — see personal identity: and ethics、社交网络——见社交网络的伦理 and social networking — see social networking and ethics、厚概念——见厚的伦理概念 thick concepts — see thick ethical concepts、功利主义——见结果主义 utilitarian — see consequentialism、非洲伦理学——见非洲哲学：非洲伦理学 ethics, African — see African Philosophy: ethics、应用伦理学 ethics, applied、信息技术伦理学的现象学方法——见信息技术：信息技术伦理学的现象学方法 phenomenological approaches to ethics and information technology — see information technology: phenomenological approaches to ethics and、生物医学伦理学 ethics, biomedical、预先指示和替代决策——见预先指示和替代决策 advance directives and substitute decision-making — see advance directives、克隆——见克隆 cloning — see cloning、决策能力——见决策能力 decision-making capacity — see decision-making capacity、残疾——见残疾：残疾的定义与模型 disability — see disability: definitions and models、疾病与健康的概念——见疾病与健康的概念 disease and health, concepts of — see health、人类卵子和精子的捐献和买卖——见人类卵子和精子的捐献与买卖 the donation and sale of human eggs and sperm — see donation and sale of human eggs and sperm、人体器官捐献——见人体器官捐献 the donation of human organs — see donation of human organs、人类增强——见人类增强 human enhancement — see human enhancement、知情同意——见知情同意 informed consent — see informed consent、怀孕、分娩和医学——见怀孕、分娩和医学 pregnancy, birth, and medicine — see pregnancy, birth, and medicine、公共卫生伦理——见公共卫生：公共卫生伦理 public health ethics — see public health: ethics、人体器官买卖——见人体器官买卖 the sale of human organs — see sale of human organs、幸福——见伦理学：古代伦理学 eudaimonia — see ethics: ancient、安乐死 euthanasia、科学——见确证 scientific — see confirmation、恶 evil、演化伦理学——见道德：道德与演化生物学 evolutionary ethics — see morality: and evolutionary biology、演化博奕论——见博弈论：演化博奕论 evolutionary game theory — see game theory: evolutionary、进化心理学——见心理学：进化心理学 evolutionary psychology — see psychology: evolutionary、美学——见美学：存在主义美学 aesthetics — see aesthetics: existentialist、审美体验——见审美体验 experience, aesthetic — see aesthetic experience、实验 experimentation、生物学——见生物学：实验生物学 in biology — see biology: experiment in、物理学——见物理学：实验物理学 in physics — see physics: experiment in、解释 explanation、数学——见数学相关：数学解释 mathematical — see mathematical: explanation、形而上学——见形而上学解释 metaphysics — see metaphysical explanation、科学——见科学实在论 scientific — see scientific realism、外在主义 externalism、外在性——见内在属性与外在属性 extrinsic — see intrinsic vs. extrinsic properties、亚伯拉罕·伊本·埃兹拉——见亚伯拉罕·伊本·埃兹拉 Ezra, Abraham Ibn — see Ibn Ezra, Abraham


**F（23 条）**

女性主义哲学方法 feminist philosophy, approaches、女性主义哲学介入 feminist philosophy, interventions、女性主义哲学主题 feminist philosophy, topics、亚当·弗格森——见苏格兰哲学：18 世纪苏格兰哲学 Ferguson, Adam — see Scottish Philosophy: in the 18th Century、詹姆斯·弗雷德里克·费里尔 Ferrier, James — see Scottish Philosophy: in the 19th century、数学哲学——见数学哲学：数学哲学中的虚构主义 in the philosophy of mathematics — see mathematics, philosophy of: fictionalism、金融、货币哲学——见货币与金融哲学 finance, philosophy of money and — see money and finance, philosophy of、民间心理学 folk psychology、神的预知——见自由意志：预知与自由意志 foreknowledge, divine — see free will: divine foreknowledge and、形式认识论——见形式认识论 formal epistemology — see epistemology, formal、形式主义 formalism、数学哲学——见数学哲学：数学哲学中的形式主义 in the philosophy of mathematics — see mathematics, philosophy of: formalism、信念的形式化表述——见信念的形式表述 formal representations of belief — see belief, formal representations of、形式（柏拉图）——见柏拉图：柏拉图的中期形而上学和认识论 Forms \[Platonic\] — see Plato: middle period metaphysics and epistemology、四维主义——见时间部分 four dimensionalism — see temporal parts、法兰克福学派——见批判理论 Frankfurt School — see critical theory、自由 freedom、积极和消极——见自由：积极自由和消极自由 positive and negative — see liberty: positive and negative、（非决定性）理论——见不相容论：自由意志的不相容主义（非决定性）理论 (nondeterministic) theories of — see incompatibilism: (nondeterministic) theories of free will、函项 function、生物——见目的论：生物学中的目的论概念 in biology — see teleology: teleological notions in biology、命题——见命题函项 propositional — see propositional function、递归——见递归函数 recursive — see recursive functions


**G（22 条）**

游戏 games、逻辑——见逻辑学：逻辑与游戏 logic and — see logic: and games、逻辑分析——见逻辑学：分析游戏的逻辑 logics for analyzing — see logic: for analyzing games、广义相对论 general relativity、几何学 geometry、亚历山大·杰拉德——见苏格兰哲学：18 世纪苏格兰哲学 Gerard, Alexander — see Scottish Philosophy: in the 18th Century、德国哲学 German Philosophy、证成——见知识证成：知识证成的基础主义理论 given, the — see justification, epistemic: foundationalist theories of、全球民主——见民主：全球民主 global democracy — see democracy: global、全球正义——见正义：全球正义 global justice — see justice: global、上帝 God、上帝存在的信仰论证 God, arguments for belief in、实用主义——见上帝存在信念的实用主义论证 pragmatic — see pragmatic arguments and belief in God、上帝存在的论证 God, arguments for the existence of、宇宙论——见宇宙论证明 cosmological — see cosmological argument、笛卡尔的本体论——见勒内·笛卡尔：笛卡尔的本体论证明 Descartes’ ontological — see Descartes, René: ontological argument、本体论——见本体论证明 ontological — see ontological arguments、目的论——见目的论：关于上帝存在的目的论论证 teleological — see teleology: teleological arguments for God’s existence、公共物品——见公共物品 goods, public — see public goods、语法 grammar、范畴——见语法：范畴类型逻辑 categorial — see grammar: typelogical、群体权利——见权利：群体权利 group rights — see rights: group


**H（21 条）**

此性——见实体 haecceity — see substance、威廉·哈密顿爵士——见苏格兰哲学：19 世纪苏格兰哲学 Hamilton, William — see Scottish Philosophy: in the 19th century、中国哲学的心——见中国哲学：中国哲学中的心 heart-mind, in Chinese Philosophy — see Chinese Philosophy: mind、基督教思想中的地狱与天堂——见基督教思想中的天堂与地狱 hell and heaven in Christian thought — see heaven and hell in Christian thought、遗传系统——见遗传系统 inheritance systems — see inheritance systems、大卫·希尔伯特 Hilbert, David、与弗雷格的争议——见戈特洛布·弗雷格：弗雷格-希尔伯特争论 controversy with Frege — see Frege, Gottlob: controversy with Hilbert、希庇亚斯——见智者 Hippias — see Sophists, The、情感学说——见情感：17 世纪和 18 世纪的情感理论 theory of emotion — see emotion: 17th and 18th century theories of、亨利·霍姆——见苏格兰哲学：18 世纪苏格兰哲学 Home, Henry \[Lord Kames\] — see Scottish Philosophy: in the 18th Century、人文主义 humanism、公民——见公民人文主义 civic — see civic humanism、人权——见权利：人权 human rights — see rights: human、人体试验 ——见生物医学伦理学：临床研究伦理 human test subjects — see ethics, biomedical: clinical research、康德关于因果关系的论述——见伊曼努尔·康德：康德和休谟论因果关系 and Kant on causality — see Kant, Immanuel: and Hume on causality、康德关于道德的论述——见伊曼努尔·康德：康德和休谟论道德 and Kant on morality — see Kant, Immanuel: and Hume on morality、情感理论——见情感：17 世纪和 18 世纪的情感理论 theory of emotion — see emotion: 17th and 18th century theories of、谦逊——见谦虚与谦逊 humility — see modesty and humility、弗兰西斯·哈奇森——见苏格兰哲学：18 世纪苏格兰哲学 Hutcheson, Francis — see Scottish Philosophy: in the 18th Century、情感理论——见情感：17 世纪和 18 世纪的情感理论 theory of emotion — see emotion: 17th and 18th century theories of、混合逻辑——见混合逻辑 hybrid logic — see logic: hybrid


**I（39 条）**

闪-托夫·伊本·法拉奎拉——见闪-托夫·伊本·法拉奎拉 Ibn Falaquera, Shem Tov — see Falaquera, Shem Tov Ibn、撒母耳·伊本·提波安——见撒母耳·伊本·提波安 Ibn Tibbon, Samuel — see Tibbon, Samuel Ibn、人格——人格同一性 personal — see personal identity、心灵同一理论——见心脑同一论 identity theory of mind — see mind/brain identity theory、法律与意识形态——见法律与意识形态 ideology, law and — see law: and ideology、心理意象——见心理意象 imagery, mental — see mental imagery、模仿游戏——见图灵测试 imitation game — see Turing test、永生——见死后生命 immortality — see afterlife、内隐偏见——见内隐偏见 implicit bias — see bias, implicit、不可通约性 incommensurability、价值——见价值：不可通约性价值 of values — see value: incommensurable、价值不可共量——见价值：价值不可共量 incomparable values — see value: incommensurable、不相容论 incompatibilism、印度哲学 Indian Philosophy、生物学个体——见生物学个体 individuals, biological — see biological individuals、归纳 induction、归纳逻辑——见逻辑学：归纳逻辑 inductive logic — see logic: inductive、不平等——见平等 inequality — see equality、惯性系统——见空间和时间：空间与时间：惯性参考系 inertial systems — see space and time: inertial frames、推断至最佳解释——见溯因 inference to the best explanation — see abduction、无限小——见连续性与无穷小 infinitesimals — see continuity and infinitesimals、非形式逻辑——见逻辑学：非形式逻辑 informal logic — see logic: informal、逻辑——见逻辑学：逻辑和信息 and logic — see logic: and information、量子纠缠——见量子理论：量子纠缠与信息 quantum entanglement and — see quantum theory: quantum entanglement and information、信息处理 information processing、信息技术 information technology、内在性——见实体 inherence — see substance、先天 innateness、工具理性——见理性：工具理性 instrumental rationality — see rationality: instrumental、意识——见意识：意识与意向性 consciousness and — see consciousness: and intentionality、行动的内因与外因——见行动的原因：行动的原因：内在与外在 internal vs. external reasons for action — see reasons for action: internal vs. external、互联网研究伦理——见伦理学互联网研究伦理 internet research ethics — see ethics: internet research、直觉主义 intuitionism、伦理学——见直觉主义伦理学 ethics — see moral intuitionism、数学哲学——见数学哲学：数学哲学中的直觉主义 in the philosophy of mathematics — see mathematics, philosophy of: intuitionism、直觉主义逻辑——见逻辑学：直觉主义逻辑 intuitionistic logic — see logic: intuitionistic、发展——见逻辑史：直觉主义逻辑的发展 development of — see logic, history of: intuitionistic logic、直觉类型论——见类型论：直觉类型论 intuitionistic type theory — see type theory: intuitionistic、感质倒转——见感质：感质倒转 inverted qualia — see qualia: inverted


**J（18 条）**

西田几多郎——见西田几多郎 Nishida Kitarō — see Nishida Kitarō、和辻哲郎——见和辻哲郎 Watsuji Tetsurō — see Watsuji Tetsurō、犹大·哈列维——见犹大·哈列维 Judah Halevi — see Halevi, Judah、判断 judgment、美学——见美学：审美判断 aesthetic — see aesthetics: aesthetic judgment、信念合并与判断聚合——见信念合并与判断聚合 judgment aggregation and belief merging — see belief merging and judgment aggregation、医疗保健的获取——见生物医学伦理学：医疗保健的公正与获取 and access to health care — see ethics, biomedical: justice and access to health care、厄运——见运气：正义与厄运 and bad luck — see luck: justice and bad luck、残疾——见残疾：残疾与正义 and disability — see disability: and justice、分配正义与实证道德心理学——见分配正义：分配正义与实证道德心理学 distributive justice and empirical moral psychology — see distributive justice: and empirical moral psychology、经济学——见规范经济学与经济正义 economic — see economics and economic justice、健康和不平等——见生物医学伦理学：正义、不平等和健康 inequality and health — see ethics, biomedical: justice, inequality, and health、领土——见领土主权与领地正义 territorial — see territorial rights and justice、知识证成 justification, epistemic、先验——见先验论证与知识 a priori — see a priori justification and knowledge、可靠主义——见可靠主义认识论 reliabilism — see reliabilist epistemology、传递——见辩护与担保的传递 transmission of — see transmission of justification and warrant、政治正当性 justification, political


**K（7 条）**

杀害或让其死亡——见造成伤害与允许伤害 killing vs. letting die — see doing vs. allowing harm、知识 knowledge、先验——见先验论证与知识 a priori — see a priori justification and knowledge、自我——见自我认识 self- — see self-knowledge、科亨-施佩克尔定理（KS 定理）——见量子力学：科亨-施佩克尔定理（KS 定理） Kochen-Specker theorem — see quantum mechanics: Kochen-Specker theorem、日本国学——见日本哲学：日本国学 Kokugaku (Native Japan Studies) School — see Japanese Philosophy: Kokugaku School、空海——见日本哲学：空海 Kūkai — see Japanese Philosophy: Kūkai


**L（37 条）**

大基数和确定性——见集合论：大基数和确定性 large cardinals and determinacy — see set theory: large cardinals and determinacy、认识论——见认识论：拉丁美洲的认识论 epistemology — see epistemology: in Latin America、女性主义——见女性主义哲学方法：拉丁美洲女性主义 feminism — see feminist philosophy, approaches: Latin American feminism、自由主义——见自由主义：拉丁美洲的自由主义 liberalism — see liberalism: in Latin America、生物学哲学——见生物学哲学：拉丁美洲的生物学哲学 philosophy of biology — see philosophy of biology: in Latin America、科学哲学——见科学哲学：拉丁美洲的科学哲学 philosophy of science — see philosophy of science: in Latin America、怀疑论——见怀疑论：拉丁美洲的怀疑论 skepticism — see skepticism: in Latin America、法律 law、限制——见法律的界限 limits of — see limits of law、自然——见自然法：自然法理论 nature of — see nature of law: natural law theories、规则——见法治与程序正义 rule of — see rule of law and procedural fairness、法哲学 legal philosophy、法律实证主义——见法律的本质：法律实证主义 legal positivism — see nature of law: legal positivism、法律惩罚——见法律惩罚 legal punishment — see punishment, legal、法律推理 legal reasoning、莱昂·埃布里奥——见犹大·莱昂·阿布拉瓦内尔 Leone Ebreo — see Abrabanel, Judah、自由女性主义——见女性主义哲学介入：自由主义女性主义 liberal feminism — see feminist philosophy, interventions: liberal feminism、自由 liberty、生活世界——见埃德蒙德·胡塞尔 lifeworld — see Husserl, Edmund、线性逻辑——见逻辑学：线性逻辑 linear logic — see logic: linear、语言学 linguistics、生前遗嘱——见预先指示和替代决策 living wills — see advance directives、逻辑学 logic、古典印度哲学——见古典印度哲学：古典印度哲学中的逻辑学 in classical Indian philosophy — see Indian Philosophy (Classical): logic、基于逻辑的人工智能——见人工智能：基于逻辑的人工智能 logic-based artificial intelligence — see artificial intelligence: logic-based、物质名词——见物质名词：物质名词的逻辑 of mass expressions — see mass expressions: logic of、自然演绎系统——见逻辑学中的自然演绎系统 natural deduction systems in — see natural deduction systems in logic、句子连接词——见连接词：形式逻辑中的句子连接词 sentence connectives in — see connectives: sentence connectives in formal logic、逻辑史 logic, history of、证明论——见证明论：证明论的发展 proof theory — see proof theory: development of、早期集合论——见集合论：集合论的早期发展 set theory, early — see set theory: early development、逻辑原子主义 logical atomism、维特根斯坦——见路德维希·维特根斯坦：维特根斯坦的逻辑原子主义 Wittgenstein’s — see Wittgenstein, Ludwig: logical atomism、代数命题逻辑——见逻辑学：代数命题逻辑 algebraic propositional logic — see logic: algebraic propositional、逻辑经验主义——见经验主义：逻辑经验主义 logical empiricism — see empiricism: logical、运气 luck、谎言与欺骗 lying and deception


**M（78 条）**

情感理论——见情感：17 世纪和 18 世纪的情感理论 theory of emotion — see emotion: 17th and 18th century theories of、质能守恒——见质能守恒 mass/energy equivalence — see equivalence of mass and energy、物质名词 mass expressions、唯物主义——见物理主义 materialism — see physicalism、数学相关 mathematical、风格——见风格：数学风格 style — see style: in mathematics、数学 mathematics、数学基础 mathematics, foundations of、戴德金的贡献——见理查德·戴德金：理查德·戴德金对数学基础的贡献 Dedekind’s contributions to — see Dedekind, Richard: contributions to the foundations of mathematics、希尔伯特计划——见大卫·希尔伯特：希尔伯特计划 Hilbert’s program — see Hilbert, David: program in the foundations of mathematics、康德——见伊曼努尔·康德：康德的数学哲学 Kant — see Kant, Immanuel: philosophy of mathematics、维特根斯坦——见路德维希·维特根斯坦：维特根斯坦的数学哲学 Wittgenstein — see Wittgenstein, Ludwig: philosophy of mathematics、意义 meaning、把人作为手段——见把人作为手段 means, treating persons as — see treating persons as means、测量 measurement、中国中医哲学——见中国哲学：中国哲学与中医 medicine: Chinese philosophy — see Chinese Philosophy: Chinese medicine、政治——见政治哲学：中世纪政治哲学 political — see political philosophy: medieval、中世纪理论 medieval theories of、类比——见中世纪的类比理论 analogy — see analogy: medieval theories of、范畴——见中世纪的范畴理论 categories — see categories: medieval theories of、因果——见中世纪的因果理论 causation — see causation: medieval theories of、良心——见中世纪的良心理论 conscience — see conscience: medieval theories of、结果——见中世纪结果理论 consequence — see consequence, medieval theories of、演绎——见中世纪的演绎理论 demonstration — see demonstration: medieval theories of、情感——见情感：中世纪情感理论 emotion — see emotion: medieval theories of、未来偶然事件——见未来偶然事件：中世纪的未来偶然事件理论 future contingents — see future contingents: medieval theories of、此性——见此性：中世纪的此性理论 haecceity — see haecceity: medieval theories of、心理表征——见心理表征：中世纪哲学中的心理表征 mental representation — see mental representation: in medieval philosophy、模态——见模态：中世纪的模态理论 modality — see modality: medieval theories of、义务——见中世纪的义务理论 obligationes — see obligationes, medieval theories of、实践理性——见中世纪的实践理性 practical reason — see practical reason: medieval theories of、词项属性——见词项：中世纪词项属性理论 properties of terms — see terms, properties of: medieval theories of、关系——见关系：中世纪关系理论 relations — see relations: medieval theories of、单称词项——见单称词项：中世纪的单称词项理论 singular terms — see singular terms: medieval theories of、三段论——见三段论：中世纪的三段论理论 syllogism — see syllogism: medieval theories of、超越——见中世纪的超越理论 transcendentals — see transcendentals, medieval theories of、心理内容 mental content、心灵外在主义——见心灵外在主义 externalism about the mind — see externalism about the mind、精神疾病——见精神障碍（精神疾病）mental illness — see mental disorder、位置——见位置与分体论 and location — see location and mereology、16 世纪的形而上学 metaphysics in the 16th century、弗朗西斯科·苏亚雷斯——见弗朗西斯科·苏亚雷斯 Francisco Suárez — see Suárez, Francisco、墨西哥 Mexico、心灵 mind、中国哲学——见中国哲学：中国哲学中的心 in Chinese Philosophy — see Chinese Philosophy: mind、模态认识论——见模态：模态认识论 modal epistemology — see modality: epistemology of、模态 modality、笛卡尔——见勒内·笛卡尔：笛卡尔的模态形而上学 Descartes and — see Descartes, René: modal metaphysics、不可能世界——见不可能世界 impossible worlds — see impossible worlds、莱布尼茨——见戈特弗里德·威廉·莱布尼茨：莱布尼茨的模态形而上学 Leibniz and — see Leibniz, Gottfried Wilhelm: modal metaphysics、模态虚构主义——见虚构主义：模态虚构主义 modal fictionalism — see fictionalism: modal、必要条件与充分条件——见必要条件与充分条件 necessary and sufficient conditions — see necessary and sufficient conditions、可能对象——见可能对象 possible objects — see possible objects、可能世界——见可能世界 possible worlds — see possible worlds、斯宾诺莎——见巴鲁赫·斯宾诺莎：斯宾诺莎的模态形而上学 Spinoza and — see Spinoza, Baruch: modal metaphysics、模态逻辑——见逻辑学：模态逻辑 modal logic — see logic: modal、现代起源——见逻辑史：现代模态逻辑的起源 modern origins — see logic, history of: modal logic、多模态逻辑的哲学方向——见多模态逻辑的哲学方向 philosophical aspects of multi-modal logic — see multi-modal logic, philosophical aspects of、墨家——见中国哲学：墨家 Mohism — see Chinese Philosophy: Mohism、墨经——见中国哲学：墨经 Mohist Canons — see Chinese Philosophy: Mohist Canons、异常——见变异一元论 anomalous — see anomalous monism、中立——见中立一元论 neutral — see neutral monism、道德品质——见道德品质 moral character — see character, moral、规范认知的心理学——见规范认知的心理学 moral cognition, psychology of — see normative cognition, psychology of、道德认知主义与非认知主义——见道德认知主义与非认知主义 moral cognitivism vs. non-cognitivism — see cognitivism vs. non-cognitivism, moral、道德普遍主义——见道德普遍主义：道德特殊主义与道德普遍主义 moral generalism — see moral particularism: and moral generalism、道德 morality、道德运气——见运气：道德运气 moral luck — see luck: moral、道德自然主义——见自然主义：道德自然主义 moral naturalism — see naturalism: moral、道德现象学——见现象学：道德现象学 moral phenomenology — see phenomenology: moral、道德心理学 moral psychology、道德推理——见推理：道德推理 moral reasoning — see reasoning: moral、道德地位 moral status、动物——见动物的道德地位 of animals — see animals: moral status of、动机 motivation、道德——道德动机 moral — see moral motivation、音乐 music、柏拉图的秘所思——见柏拉图：柏拉图的秘所思 myths, Plato’s — see Plato: myths


**N（24 条）**

日本国学——见日本哲学：日本国学 Native Japan Studies (Kokugaku) School — see Japanese Philosophy: Kokugaku School、认识论——见认识论：自然主义认识论 in epistemology — see epistemology: naturalism in、数学哲学——见数学哲学：数学哲学中的自然主义 in the philosophy of mathematics — see mathematics, philosophy of: naturalism、自然语言本体论——见自然语言本体论 natural language ontology — see ontology, natural language、自然法 natural law、伦理学传统——见伦理学：伦理学中的自然法传统 tradition in ethics — see ethics: natural law tradition、自然哲学 natural philosophy、新理正派——见早期现代印度的分析哲学 Navya-Nyāya — see Early Modern India, analytic philosophy in、必然存在 necessary beings、上帝——见上帝和其他必然存在 and God — see God: and other necessary beings、库萨的尼古拉——见库萨的尼古拉 Nicolas of Cusa — see Cusanus, Nicolaus、意向对象——见埃德蒙德·胡塞尔 noema — see Husserl, Edmund、唯名论 nominalism、数学哲学——见数学哲学：数学哲学中的唯名论 in the philosophy of mathematics — see mathematics, philosophy of: nominalism、道德非自然主义——见道德非自然主义 non-naturalism, moral — see moral non-naturalism、非概念性内容——见非概念性心智内容 nonconceptual content — see mental content: nonconceptual、正则形式博弈 normal form games、分析权力的逻辑——见逻辑学：博弈中的权力推理 logics for analyzing power in — see logic: for analyzing power in normal form games、规范性 normativity、逻辑——见逻辑的规范性地位 logic — see logic: normative status of、意义——见意义：意义和内容的规范性 meaning — see meaning: normativity of、元伦理学——见元伦理学中的规范性 metaethics — see metaethics, normativity in、合作规范——见社会规范 norms of cooperation — see social norms、罗伯特·诺齐克 Nozick, Robert


**O（9 条）**

客观性 objectivity、科学——见科学的客观性 scientific — see scientific objectivity、义务 obligation、法律——见法律义务与法律权威 legal — see legal obligation and authority、义务 obligations、本体论依赖——见本体论依赖 ontological dependence — see dependence, ontological、本体论 ontology、社会——见社会本体论 social — see social ontology、财产和所有权——见财产和所有权 ownership, property and — see property and ownership


**P（61 条）**

悖论 paradox、柯里——见柯里悖论 Curry’s — see Curry’s paradox、费奇的可知性悖论——见费奇的可知性悖论 Fitch’s paradox of knowability — see Fitch’s paradox of knowability、说谎者——见说谎者悖论 of the liar — see liar paradox、罗素悖论——见罗素悖论 Russell’s paradox — see Russell’s paradox、辛普森悖论——见辛普森悖论 Simpson’s paradox — see Simpson’s paradox、圣彼得堡悖论——见圣彼得堡悖论 St. Petersburg paradox — see St. Petersburg paradox、悬疑——见悬疑悖论 of suspense — see suspense, paradox of、芝诺悖论——见爱利亚的芝诺：芝诺悖论 Zeno’s paradoxes — see Zeno of Elea: Zeno’s paradoxes、认知——见认知悖论 epistemic — see epistemic paradoxes、部分/整体——见分体论 part/whole — see mereology、知觉 perception、基于行动的感知理论——见基于行动的感知理论 action-based theories — see action-based theories of perception、知觉学习——见知觉学习 perceptual learning — see learning, perceptual、持存——见时间部分 persistence — see temporal parts、人格 personhood、古典印度哲学——见古典印度哲学：古典印度哲学中的人格 in classical Indian Philosophy — see Indian Philosophy (Classical): personhood、人格——见人格同一性 persons — see personal identity、将人作为手段——见将人作为手段 persons, treating as means — see treating persons as means、现象意向性——见意向性：现象意向性 phenomenal intentionality — see intentionality: phenomenal、生物学哲学 philosophy of biology、科学哲学 philosophy of science、辩证学家斐洛——见麦拉加学派 Philo the Dialectician — see Dialectical School、物理学 physics、量子场论——见量子理论：量子场论 quantum field theory — see quantum theory: quantum field theory、自然与习俗——见智者 physis and nomos — see Sophists, The、松果体——见勒内·笛卡尔：笛卡尔与松果体 pineal gland — see Descartes, René: and the pineal gland、柏拉图主义 Platonism、数学哲学——见数学哲学：数学哲学中的柏拉图主义 in the philosophy of mathematics — see mathematics, philosophy of: Platonism、多元主义 pluralism、宗教——见宗教多元主义 religious — see religious diversity、形式的多样性——见最著名的一对 plurality of forms — see binarium famosissimum、以撒·波尔卡尔——见以撒·波尔卡尔 Polgar, Isaac — see Polqar, Isaac、政治哲学 political philosophy、政治现实主义 political realism、政治理论与宗教——见宗教：宗教与政治理论 political theory and religion — see religion: and political theory、群体遗传学——见遗传学：群体遗传学 population genetics — see genetics: population、色情 pornography、刺激贫乏论——见先天：先天与语言 poverty of the stimulus argument — see innateness: and language、默认——见语义和语用中的默认 defaults in — see defaults in semantics and pragmatics、祷告 prayer、低阶谓词演算——见逻辑学：经典逻辑 predicate calculus — see logic: classical、预测主义——见预测与解释 predictivism — see prediction versus accommodation、产前检测与产前筛查——见优生学 prenatal testing and screening — see eugenics、信息技术——见信息技术：隐私与信息技术 and information technology — see information technology: and privacy、医学——见生物医学伦理学：隐私与医疗 and medicine — see ethics, biomedical: privacy and medicine、不确定概率——见非精确概率 probabilities, indeterminate — see probabilities, imprecise、概率与逻辑——见逻辑学：逻辑与概率 probability and logic — see logic: and probability、程序正义——见法治与程序正义 procedural fairness — see rule of law and procedural fairness、生育——见为人父母和生育 procreation — see parenthood and procreation、普罗狄科——见智者 Prodicus — see Sophists, The、涌现——见涌现属性 emergent — see emergent properties、本质与偶然——见本质属性与偶然属性 essential vs. accidental — see essential vs. accidental properties、产权 property、命题逻辑——见逻辑学：命题逻辑 propositional logic — see logic: propositional、科学与伪科学——见科学：科学与伪科学 pseudo-science, science and — see science: and pseudo-science、灵魂——见古代的灵魂理论 psyche — see soul, ancient theories of、心理学 psychology、公共卫生 public health、塞缪尔·冯·普芬道夫 Pufendorf, Samuel Freiherr von、皮浪主义——见怀疑论：古代怀疑论 Pyrrhonism — see skepticism: ancient


**Q（6 条）**

清代哲学——见中国哲学：清代哲学 Qing philosophy — see Chinese Philosophy: Qing philosophy、贝尔定理——见贝尔定理 Bell’s Theorem — see Bell’s Theorem、量子理论 quantum theory、测量问题——见量子理论：量子理论的哲学问题 the measurement problem — see quantum theory: philosophical issues in、不确定性原理——见不确定性原理 uncertainty principle in — see Uncertainty Principle、不可或缺性论证——见数学哲学：数学哲学中的不可或缺性论证 indispensability argument — see mathematics, philosophy of: indispensability arguments in the


**R（35 条）**

批判种族哲学——见批判种族哲学 critical philosophy of — see critical philosophy of race、随机性 randomness、随机性与概率——见概率：概率与随机性 versus chance — see chance: versus randomness、理性选择的规范理论 rational choice, normative、理性 rationality、贝叶斯主义——见认识论：贝叶斯认识论 Bayesian — see epistemology: Bayesian、有限性——见有限理性 bounded — see bounded rationality、博弈论的认识论基础——见博弈论：博弈论的认识论基础 epistemic foundations of game theory — see game theory: epistemic foundations of、道德——道德实在论 moral — see moral realism、国际关系中的政治现实主义——见政治现实主义：国际关系中的政治现实主义 political, in international relations — see political realism: in international relations、科学——见科学实在论 scientific — see scientific realism、结构主义——结构现实主义 structural — see structural realism、推理 reasoning、类比——见类比与类推推理 by analogy — see analogy and analogical reasoning、行动的理由 reasons for action、递归——见递归（递归函数） recursion — see recursion、物理学——见物理学：物理学中的跨理论关系 in physics — see physics: intertheory relations in、道德——见道德相对主义 moral — see moral relativism、宗教 religion、女性主义哲学——见女性主义哲学介入：女性主义宗教哲学 feminist philosophy of — see feminist philosophy, interventions: philosophy of religion、自然——见自然神学与自然宗教 natural — see theology, natural and natural religion、科学表征——见科学表征 representation, scientific — see scientific representation、想象性抗拒——见想象性抗拒 resistance, imaginative — see imaginative resistance、责任 responsibility、应报正义——见正义：应报正义 retributive justice — see justice: retributive、公民——见公民权利 civil — see civil rights、法律——见法律权利 legal — see legal rights、领土——见领土权与领地正义 territorial — see territorial rights and justice、机器人学 robotics、伦理学——见人工智能：人工智能和机器人伦理 ethics of — see artificial intelligence: ethics of、角色义务：见义务：特殊义务 role obligations — see obligations: special、理查德·西尔万——见理查德·西尔万（Routley）Routley \[Sylvan\], Richard — see Sylvan, Richard、理查德·鲁弗斯——见诡辩家理查德 Rufus, Richard — see Richard the Sophister、规则后果主义——见结果主义：规则后果主义 rule consequentialism — see consequentialism: rule、逻辑原子主义——见逻辑原子主义：罗素的逻辑原子主义 logical atomism — see logical atomism: Russell’s


**S（51 条）**

怀疑论——见怀疑论 scepticism — see skepticism、科学 science、模型——科学模型 models in — see models in science、科学知识 scientific knowledge、理论变革——见实在论：科学实在论和理论变革 and theory change — see realism: and theory change in science、科学理论 scientific theories、不可通约性——见不可通约性：科学理论的不可通约性 incommensurability of — see incommensurability: of scientific theories、非充分决定性——见非充分决定性：科学理论的非充分决定性 underdetermination of — see underdetermination, of scientific theories、苏格兰哲学 Scottish Philosophy、约翰内斯·司各特·爱留根纳——见约翰内斯·司各特·爱留根纳 Scottus \[Scotus\] Eriugena \[Erigena\], John — see Eriugena, John Scottus、约翰·邓·司各脱——见约翰·邓·司各脱 Scotus, John Duns — see Duns Scotus, John、搜索引擎伦理——见伦理学：搜索引擎伦理 search engines and ethics — see ethics: search engines and、雷蒙·塞邦——见米歇尔·德·蒙田 Sebond, Raymond — see Montaigne, Michel de、早期现代哲学中的第一性质和第二性质——见早期现代哲学中的第一性质和第二性质 secondary qualities, in early modern philosophy — see primary and secondary qualities in early modern philosophy、自我 self、女性主义对自我的观点——见女性主义哲学主题：女性主义对自我的观点 feminist perspectives on the — see feminist philosophy, topics: perspectives on the self、认识——见自我认识 knowledge — see self-knowledge、外在主义——见外在主义：外在主义与自我认识 and externalism — see externalism: and self-knowledge、自尊——见自尊 self-respect — see respect、语义整体论——见意义整体论 semantic holism — see meaning holism、语义 semantics、默认——见语义和语用中的默认 defaults in — see defaults in semantics and pragmatics、符号学 semiotics、感性理论——见恰当态度的价值理论 sensibility theory — see fitting attitude theories of value、道德情感主义——见道德情感主义 sentimentalism, moral — see moral sentimentalism、情感理论——见情绪：17 世纪和 18 世纪的情绪理论 theory of emotion — see emotion: 17th and 18th century theories of、单称词项 singular terms、情境 situations、道德——道德怀疑论 moral — see moral skepticism、斯科伦悖论——见悖论：斯科伦悖论 Skolem’s paradox — see paradox: Skolem’s、亚当·斯密——见苏格兰哲学：18 世纪苏格兰哲学 Smith, Adam — see Scottish Philosophy: in the 18th Century、社会建构 social construction、社会契约论——见自利契约论 social contract — see contractarianism、社会认识论——见认识论：社会认识论 social epistemology — see epistemology: social、空间与时间 space and time、speech 言语、内部——内部言语 inner — see inner speech、斯宾诺莎 Spinoza、情感理论——见情绪：17 和 18 世纪的情感理论 theory of emotion — see emotion: 17th and 18th century theories of、统计物理学 statistical physics、干细胞研究的伦理问题——见生物医学伦理学：干细胞研究的伦理问题 stem cell research, ethics of — see ethics, biomedical: stem cell research、杜格尔·斯图尔特——见苏格兰哲学：18 世纪苏格兰哲学 Stewart, Dugald — see Scottish Philosophy: in the 18th Century、结构主义 structuralism、数学哲学：见数学哲学：数学哲学中的结构主义 in mathematics — see mathematics, philosophy of: structuralism、物理学——见物理学：物理学中的结构主义 in physics — see physics: structuralism in、风格 style、子结构逻辑 substructural logics — see logic: substructural、无行为能力者的代理人决策 surrogate decision-making for incompetent individuals — see advance directives、三段论 syllogism、对称性与对称性破缺——见物理学：对称性与对称性破缺 symmetry and symmetry breaking — see physics: symmetry and symmetry breaking、综合——见分析/综合的区别 synthetic — see analytic/synthetic distinction


**T（23 条）**

道家/道教——见道家/道教 Taoism — see Daoism、技术——见科学和技术 techne — see episteme and techne、目的论 teleology、心理内容的目的论——见心理内容：心理内容的目的论 teleological theories of mental content — see mental content: teleological theories of、时间意识——见意识：时间意识 temporal consciousness — see consciousness: temporal、词项属性 terms, properties of、证言 testimony、审美证言——见审美证言 testimony, aesthetic — see aesthetic testimony、有神论 theism、无神论与不可知论——见无神论与不可知论 atheism and agnosticism — see atheism and agnosticism、一神论——见一神论 monotheism — see monotheism、超泛神论——见超泛神论 panentheism — see panentheism、过程——见过程神学 process — see process theism、怀疑论——见怀疑论式有神论 skeptical — see skeptical theism、联想主义思想——见联想主义思想 thought, associationist theories of — see associationist theories of thought、塞拉西马柯——见柏拉图：卡利克勒斯和塞拉西马柯 Thrasymachus — see Plato: Callicles and Thrasymachus、现代物理学中的存在与变化——见时间与空间：现代物理学中的存在与变化 being and becoming in modern physics — see space and time: being and becoming in modern physics、康德——见伊曼努尔·康德：康德的先验论证 Kant — see Kant, Immanuel: transcendental arguments、女性主义对跨性别议题的观点——见女性主义哲学主题：女性主义对跨性别议题的观点 trans issues, feminist perspectives on — see feminist philosophy, topics: perspectives on trans issues、跨界同一性——见同一性：跨界同一性 transworld identity — see identity: transworld、塔尔斯基的真理定义——见阿尔弗莱德·塔尔斯基：塔尔斯基的真理定义 Tarski’s theory of truth — see Tarski, Alfred: truth definitions、乔治·特恩布尔——见苏格兰哲学：18 世纪苏格兰哲学 Turnbull, George — see Scottish Philosophy: in the 18th Century、建构主义——见类型论：直觉主义类型论 constructive — see type theory: intuitionistic


**U（8 条）**

终极存在 ultimates、上帝——见上帝：上帝与其他终极存在 and God — see God: and other ultimates、自然选择的单位与层次——见自然选择：选择的单位与层次 units and levels of natural selection — see natural selection: units and levels of、统一科学——见科学：统一科学 unity of science — see science: unity of、普遍的形质论——见最著名的一对 universal hylomorphism — see binarium famosissimum、普遍性——见属性 universals — see properties、功利主义——见结果主义 utilitarianism — see consequentialism、规则——见后果主义：规则后果主义 rule — see consequentialism: rule


**V（13 条）**

组合的模糊性——见多的难题 vagueness of composition — see many, problem of、有效性——见逻辑真理 validity — see logical truth、价值 value、知识——见知识价值 of knowledge — see knowledge, value of、无知之幕——见原初状态 veil of ignorance — see original position、内涵及物动词——见内涵及物动词 verbs, intensional transitive — see intensional transitive verbs、逼真性——见似真性 verisimilitude — see truthlikeness、德性 virtue、古代理论——见伦理学：古代伦理学 ancient theories of — see ethics: ancient、德性伦理学：见伦理学：德性伦理学 virtue ethics — see ethics: virtue、数学中的视觉思维 visual thinking in mathematics、维泰博的詹姆斯——见维泰博的詹姆斯 Viterbo, James of — see James of Viterbo、意志——见自由意志 volition — see free will


**W（9 条）**

辩护与担保的传递——见辩护与担保的传递 warrant, transmission of — see transmission of justification and warrant、福利经济学——见规范经济学与经济正义 welfare economics — see economics and economic justice、拉姆齐与代际——见弗兰克·拉姆齐：拉姆齐的代际福利经济学 intergenerational, and Ramsey — see Ramsey, Frank: and intergenerational welfare economics、本杰明·惠科特——见剑桥柏拉图学派 Whichcote, Benjamin — see Cambridge Platonists、奥卡姆的威廉——见奥卡姆的威廉 William of Ockham — see Ockham, William、词义——见意义：词义 word meaning — see meaning: of words、世界 worlds、不可能——见不可能世界 impossible — see impossible worlds、可能——见可能世界 possible — see possible worlds


**Z（2 条）**

恩斯特·策梅洛 Zermelo, Ernst、公理化集合论——见策梅洛的公理化集合论 axiomatization of set theory — see set theory: Zermelo’s axiomatization of

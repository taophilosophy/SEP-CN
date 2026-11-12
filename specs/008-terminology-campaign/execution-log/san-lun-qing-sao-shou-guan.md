# 执行记录：术语战役 · 三轮清扫收官（2026-11-12）

TL-main-20261112 续：凭证文件名缺陷修复、重复行归一与清扫收官。

## 2026-11-12 三轮清扫收官（TL-main-20261112 续）

### 一、三轮队列与通道机制

* 队列 `%TEMP%/az-term3.json` 586 项（二轮 27 个降级词＋并行会话 2026-11-11/12 新登记行＋历史残差），
  `--start 0` 全量跑完（断点 586/586），爬虫自愈降级多次全部恢复，末批补跑救回。
* **轮次同名碰撞坑根治**：批次文件名跨轮复用同名，旧守护按纯文件名记账致新一轮被当旧账跳过（三次实踩）；
  本地守护重写为「文件名+mtime」记账＋启动时刻过滤（`script/tl_ingest_watch.py`，本地草稿不入库），
  爬虫覆写同名即重入，处置过程已注记本卡「轮次同名碰撞坑」节。

### 二、三轮增量裁定（59 条，q–s 段，差集口径）

* 审计刷新（补亦作落册后复跑）：一致 1041 / 不一致 711 / 查无 4107 / 未查证 4118（登记册 9977 行，较二轮收官
  +157 行系并行会话新增；10 条亦作使一致 +10、不一致 −10）。裁定前审计：一致 1031 / 不一致 721 / 查无 4106 / 未查证 3962。
* **主译变更 0 条；登记补亦作 10 条**：
  * E-language「E-语言」亦作“外化语言”、I-language「I-语言」亦作“内化语言”（审定·语言学名词理论语言学核心术语；
    正文 12:0 / 22:0 沿字母对举体例）；
  * inverse-square law「反平方定律」亦作“平方反比定律”（审定·物理学；本词条 H1 与脚注一体的“反平方”体例，4:1）；
  * transfinite induction「超限归纳」亦作“超穷归纳法”（审定·数学集合论；正文 4:0）；
  * replicator「复制者」亦作“复制因子”（审定·遗传学/生化；与交互者对举体例）；
  * no-go theorem「不可行定理」亦作“止步定理”（审定·物理学粒子物理）；
  * genome-wide association study「全基因组关联研究」亦作“全基因组关联分析”（审定三库一致）；
  * center of oscillation「振动中心」亦作“摆动中心”（审定·物理学）；
  * lunar inequality「月球不等项」亦作“月行差”（审定·天文学）；
  * self-organization「自我组织」亦作“自组织”（审定·自然辩证法复杂系统科学哲学；康德 Selbstorganisation 语境沿自我组织）。
* **保留 49 条**，归类：
  * 假阳性/垃圾池/泛词：automatism（自动症 医学）、avyākṛta（TA克隆）、good will（多行不义必自毙 成语库）、
    karma（佛教业报义）（义通 泛词）、nondirectiveness、perspectivalism、perspective (RQM)、subjectivist（垃圾池）、
    the Requirement（党建文献）、theory of principle（理论与实际相结合原则）、variation (lunar)（磁月日变 地磁）、
    saṃkhyā（数目）（目/编目/吏目 汉字训释）、fixed stars（固定探头式星跟踪器）、active/passive euthanasia（有源的 fuzzy）、
    accounting price（码价核算制 图书发行）、mutual recognition（学分互认 教育认证）、motive force（质子动力 生化）、
    physical information（实物信息源 通信）、national-popular（民族的科学的大众的文化 政论）。
  * 同形异义/学科分域：desert（荒漠 沙）、chart（海图/表图 航海图学）、dimension（尺寸/量纲；本行矢量空间维数）、
    norm（规范/范数混列；本行矢量长度“模”）、configuration（构型 化学；本行利科“塑形”）、defect（疵点/缺陷；
    本行非欧几何“亏量”）、critical period（关键期 心理/生物；本行康德“批判时期”分期）、critical level（临界菌量/
    临界潮位 具体下位）、citizenship（公民权 侧重权利；本行公民身份）、sociability（社交能力/群集度；本行康德
    Geselligkeit 合群性）、guest worker（僮客 古语/外来劳工 近义泛称；本行史学术语客籍工人）、palliative care
    （审定“缓和照顾”（台）/“安宁疗护”；大陆临床“姑息治疗”与“缓和医疗”并通行，正文 9 处 3 词条）、
    objective idealism（审定“客观唯心主义”教科书形；本库观念论体例，dilthey 语境沿客观观念论）。
  * 上位/下位/全称/词形：classical genetics（遗传学 上位）、constant curvature（常曲率空间 下位）、
    constructive theory（学习的建构理论/函数构造论 假阳性）、Big Bang（[宇宙]大爆炸 方括号记法）、
    Jacobin（雅各宾派 全称形）、singularity (cosmological)（宇宙奇点 全称形）、projection postulate
    （冯·诺依曼投影公设 全称形）、elliptic/hyperbolic geometry（审定加“[学]”尾记法差）、capital-output ratio
    （资本产出率 词序/体例差）、hard problem（NP难问题 假阳性；反向命中“意识的难问题”佐证现译）、
    air-pump（抽气泵/空气压缩泵 工程下位；本行波义耳实验语境）、self-adjoint operator（自伴算子 数学形；
    本库物理语境“算符”）、redescription（再描述 vs 重新描述 词形差，利科体例）、fundamentalism（审定“基本教义主义/
    原教旨主义”；本行康德语境“基要主义者”学术通行形）。
* 「risk perception」由二轮补亦作行（风险认知）转一致，差集出列 1 条。

### 三、四轮清扫（191 项，a–t 段残差；2026-11-12）

* 队列 `%TEMP%/az-term4.json` 191 项（三轮降级 error＋并行会话新登记行），`--start 0` 全量 191/191 收官；
  守护按 mtime 记账，同名碰撞未再出现（轮次切换零手工）。
* 审计刷新（裁定前）：一致 1060 / 不一致 730 / 查无 4187 / 未查证 4031；**裁定后复跑：一致 1063 / 不一致 727**
  （3 条亦作各转一致一条）。登记册续增系并行会话持续入册。
* **主译变更 0 条；补亦作 3 条**：initial segment「初始片段」亦作“初始段”（审定·数学集合论）；
  interactor「交互者」亦作“互动子”（审定·自然辩证法生物学哲学；与 replicator“复制者”对举体例）；
  modern synthesis「现代综合」亦作“现代综合论”（审定·自然辩证法生物学哲学/古生物学；全库 b/e/g 段多处带引号短语沿短形）。
* **保留 16 条**：Robbins conjecture、fictionality、fictionality puzzle、idiolect（垃圾池命中）；
  charity（caritas 基督教汉译“爱德”，审定“慈善事业/施舍”异义）；construction（构式语法“构式”）；
  domain-general / domain-specific（认知科学对举；审定命中为“领域一般理论/领域特殊理论”全称）；
  impossibility theorem（审定命中均为“阿罗［不可能］定理”全称）；incompleteness theorems（登记行已并存
  词条名“不完备定理”与叙述“不完全性定理”）；inductive generalization（科学哲学通行“归纳概括”，审定“归纳泛化”为心理学义）；
  latus rectum（“通径”，审定“半通径”为 semi-latus rectum 下位）；melancholy（存在论状况“忧郁”，审定“沉郁”为文艺学义）；
  preparation（量子力学“制备”，审定“制剂/剂型”药学义）；restitution（格劳秀斯法学“返还”，审定“恢复/重建”异义）；
  transversality condition（最优控制/增长理论“横截条件”，审定“强横截条件/横截性条件”为数学变体）。

### 四、五轮清扫（56 项残差；2026-11-12）

* 队列 `%TEMP%/az-term5.json` 56 项（四轮降级 error＋新登记行），`--start 0` 全量 56/56 收官，末批补跑救回。
* 审计刷新：一致 1067 / 不一致 731 / 查无 4203 / 未查证 4007。
* **主译变更 0 条、补亦作 0 条，保留 4 条**：agonism（格劳秀斯伦理“对抗论”，审定“激动”药理学假阳性）、
  false-belief（“错误信念”，审定命中“错误信念任务”为测验下位，反向佐证）、imperfectivity（Thompson“不完全性”，垃圾池命中）、
  self-respect（利科 respect de soi“自我尊重”，审定“敬谦”假阳性）。

### 五、六轮清扫与术语表收敛（8 项；2026-11-12）

* 队列 `%TEMP%/az-term6.json` 8 项（单批），全部 ok；此后 `--emit --unverified --table term` 归零
  （除并行会话后续新登记行），术语表未查证队列至此清空。
* 审计刷新（裁定前）：一致 1067 / 不一致 732 / 查无 4202 / 未查证 4007；**裁定后：一致 1068 / 不一致 731**。
* **主译变更 1 条**：amniocentesis「羊膜穿刺术」→「羊膜腔穿刺术」（审定·医学名词四库一致；旧形降亦作；
  `g/genetics.md` 1 处看齐）。其余 7 项：查无 5（goal-directed agency、immortality of the soul、intention in action、
  poverty of stimulus、provability），一致 2（consistency、world-picture）。

### 六、凭证文件名希腊字母剥名缺陷与重复行归一（2026-11-12 收尾）

* **缺陷**：`cnki_query.safe_key` 只保留 `[a-z0-9\\u4e00-\\u9fff]`，希腊字母被剥——`ω-consistency` 与
  `consistency` 落同一文件名，后查者覆盖前查者凭证（实测 4 组：ω-consistency/consistency、ω-provability/provability、
  modal μ-calculus/modal calculus、ε-notation/notation）。更隐蔽的是审计会因此误判「一致」。
* **修复**：`safe_key` 增加希腊字母音译表（ω→omega、ε→epsilon、μ→mu 等，25 字母），`tools/cnki_query.py`
  已单独提交（19eb975e5）；四组凭证重查后分别落 `omega_consistency/omega_provability/epsilon_notation/modal_mu_calculus.json`，
  普通词 `consistency/provability` 回正。
* **重复行归一 2 组**（同义同译，且归一后文件名相撞）：`immortality (of the soul)` 与 `immortality of the soul` 合为后行；
  `world-picture` 与 `world picture` 合为后行（Weltbild 原文与维特根斯坦依据并入）。
* **多会话事故留痕**：共享克隆内并行会话的 `git checkout`/结构删除两次冲掉本会话未提交的暂存（暂存的重命名、
  工具补丁、登记册合并行）；教训重申——工具补丁与登记册改动须即刻单独提交，不留窗口。
* 收敛实测：`--emit --unverified --table term` 余 18 项，均为并行会话当日新登记行（genetics/teleosemantics 批次等），
  属正常增量而非缺陷。该 18 项随后三批补齐（informational content 降级后冷却补查、theoros 批末补跑救回），
  新增不一致 2 条均保留：functional reference（“功能指称”，审定命中“物联网功能参考结构”假阳性）、
  sender（“发送者”，审定“传送者/发话人”为通信/语言学变体；本行 teleosemantics 语境 sender/receiver 对举）。
  审计终态：一致 1075 / 不一致 732 / 查无 4207 / 未查证 4104（未查证余量＝并行会话持续新登记行）。

### 七、队列稳态续跑（2026-11-12 下午，56 项）

* 并行会话当日新登记行（含 ibn-taymiyya 阿拉伯语哲学词汇、hypothesis 批次等）56 项跑完；中途会话中断一次，
  自断点 32 续跑并手动补入中断前四批（新守护只摄取启动后文件，历史批次须 `--ingest` 补）。
* 审计刷新：一致 1079 / 不一致 738 / 查无 4301 / 未查证 4219。
* 新增不一致 4 条全保留：taʿṭīl「剥离」、taḥayyuz「空间延展」、taḥrīf「扭曲」、taṣawwur「概念化」——
  四条审定命中均为「TA克隆」垃圾池（模糊匹配污染），本行皆 ibn-taymiyya 首译的凯拉姆术语。

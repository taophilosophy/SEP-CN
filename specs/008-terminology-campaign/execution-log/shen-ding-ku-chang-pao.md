# 执行记录：术语战役 · 审定库长跑与二轮补查（2026-11-11）

TL-main-20261111 长跑续批与同日二轮补查增量裁定。

## 2026-11-11 审定库长跑续批与增量裁定（TL-main-20261111）

### 一、长跑状态

* 爬虫 `tools/tl_crawler.py` 自 offset 1804 续跑术语表未查证队列（`%TEMP%/az-term.json` 共 2772 项），
  `--no-warm --interval 10 --batch-gap 20`；`tl_ingest_watch.py` 同步落凭证，断点 `state/tl-crawl-state.json`。
* 在途凭证 87 份（s 区段 shingon–sifat）先行入库提交（`26064031c`），余下随跑随提。

### 二、增量裁定（11-10 → 11-11 新增不一致 25 条）

* 审计口径：`term_audit` → 8610 行（术语 4856 + 人名 3754）：一致 522 / 不一致 355 / 查无 1877 / 未查证 5856。
* 与 audit-2026-11-10 逐行比对，新增不一致 25 条（全部落在 s 区段），逐条判读：
  * **主译变更 1 条**：shifting balance theory「转换平衡理论」→「动态平衡说」（审定名词·遗传学名词，英文精确命中且学科语境正确；
    旧形降为亦作；正文 `e/ecological-genetics.md` 看齐）。
  * **保留 24 条**，归类：
    * 跨学科同名：second intention（体育）、secondary causes（军事）、semblance（石油）、shingon/mantra（音乐）、
      shu / shu shu（档案学「书」）、side condition（信息科技「伴随条件」）、situation（管理/语言学）、
      social model（行为医学）、social acts（Social Security Act，英文不符）、semantic compactness（社会学假阳性）。
    * 下位词/派生词：self-affirmation（自我肯定理论）、self-cultivation（教师修养/修齐治平）、self-interest（自为）、
      self-realization（自我实现人假设）、self-reliance（自主可控战略）、sensitivity/safety conditions（灵敏度/敏感性）。
    * 语境限定义项：signification（新闻学「意指」，本行取中世纪逻辑「意谓」）、sincerity（中华思想文化「诚」，
      本行为道德心理学子维度）、social software（Parikh 社会程序义≠社交软件）、size principle（生理学运动单位义）、
      self-knowledge（自然辩证法「自我知识」为知识论术语，conscience 语境取「自我认识」）、skilled action（教育「熟练动作」）。
* 裁定结论与凭证同日留档，登记册无其他改动。

### 三、门禁

* `check_terms` 硬错误 0（冲突 0 + 自洽 0）、词汇表滞后 0。
* `check_all` 9 项 8 绿；学术规范红为并行会话在途任务（`tasks/l/logic-substructural.json` 步骤 s2 缺语体核验），非本批改动。

### 四、第二批增量裁定（offset 2044–2076，8 条）

* 审计刷新：8624 行，一致 539 / 不一致 362 / 查无 1919 / 未查证 5804；新增不一致 8 条。
* **主译变更 1 条**：somatic mutation theory「体细胞突变论」→「体细胞突变学说」（审定名词·医学名词，英文精确且学科语境正确；
  旧形降为亦作；`c/cancer.md` 4 处看齐）。
* **保留 7 条**：species concept（审定命中为图书馆学「种概念」及下位「形态种概念」）、species（经院，维基垃圾命中）、
  spectator blame（社会学假阳性）、spirits / spiritus（天文学/药学/中医药异义）、Spirituals（音乐「灵歌」义≠方济各会「属灵派」）、
  sŏngjŏk tŭngji（维基垃圾命中）。

### 五、第三批增量裁定（offset 2076–2116，8 条）

* 审计刷新：一致 548 / 不一致 369 / 查无 1950 / 未查证 5757；新增不一致 8 条。
* **主译变更 1 条**：spontaneous generation「自然发生」→「自然发生说」（审定名词·动物学/微生物学名词，英文精确且学科语境正确；
  旧形降为亦作；`n/natphil-ren.md` 看齐）。
* **保留 7 条**：state of affairs / states of affairs（中国古代史「尚书省」假阳性）、state of war（战国时代假阳性）、
  startle response（下位「震惊条件反射实验」）、statistical learning（下位「统计学习理论」）、steering（航海「操舵」异义）、
  stem cell bank（下位「胚胎干细胞库」）。

### 六、第四批增量裁定（offset 2116–2172，8 条）

* 审计刷新：一致 556 / 不一致 376 / 查无 1990 / 未查证 5755；新增不一致 8 条。
* **主译变更 2 条**：strict finitism「严格有限主义」→「严格有穷论」（审定名词·自然辩证法名词；`i/intuitionism.md` 看齐）、
  subjective well-being「主观幸福」→「主观幸福感」（审定名词·心理学名词；`d/disability-care-rationing.md` 看齐）。
* **保留 5 条**：strategy-proof（「证明策略」假阳性）、strict implication（社会学假阳性）、subject-matter（经贸「标的物」异义）、
  subjunctive hypocrisy（假阳性）、subsistence（地理「自给」异义）。
* **待用户裁定 1 条（已裁定，见下节）**：Stoic——审定命中「斯多葛学派/斯多葛派」（自然辩证法·世界历史，en=Stoics），本库现行「斯多亚（斯多亚学派）」
  全库正文 372 处（斯多亚派 171/斯多亚主义 43/斯多亚学派 21），而词汇表 Stoicism 行已用「斯多葛主义」（两形并存约 1:15）。
  按 ADR-0012 档位应采审定形，但涉全库批量改名，上报裁定后另批执行。

### 七、全库统一斯多亚→斯多葛（用户裁定 2026-11-11）

* 裁定：采审定形「斯多葛（斯多葛学派）」，旧形降为亦作；登记行依据列改记审定名词库凭证 + 裁定日期。
* 工具 `script/stoa_rename_20261111.py`（本地草稿）：作用域=26 个字母目录 + `qian-yan/` + 根层五文档（`en/`、`yuanwen/`、
  `specs/`、`rules/` 等一律不动）；替换序=学派→主义→派→裸词；纪律=前置门（全量扫描发现任一脏文件即零写入）、
  幂等复跑 0 处、行数守恒、变更行仅允许「斯多亚↔斯多葛」字形差（norm 比对）、写回后作用域残余 0。
* 结果：49 个文件 394 处改形（含 `yi-zhe-shuo-ming.md` 14、`ren-ming-biao.md` 8、`qian-yan/ci-hui-biao.md` 3）；
  幂等复跑 0；残余仅登记行「亦作“斯多亚”」1 处（有意保留）。门禁：`check_terms` 硬错误 0/滞后 0，`check_all` 9/9 全绿。
* 并行事故留痕：首次 `--apply` 撞上并行会话交互式变基（`ren-ming-biao.md` UU），脚本旧版「边写边查脏」已写入 47 个文件；
  发现后按「写前确认干净」子集逐文件 `git checkout --` 撤回（47 个，含 CRLF 单文件），零内容损失；随后改脚本为
  **先全量扫描、脏则零写入**，并新增「rebase/merge 进行中拒绝执行」硬门。终次执行在变基收尾后完成。
  （改形内容后被并行会话「暂存」提交 `da5b57558` 收编，`git log -1 -- <文件>` 核实在库，按「收编即放行」处置。）

### 八、第五批增量裁定（offset 2308–2380，24 条）

* 审计刷新：一致 585 / 不一致 398 / 查无 2136 / 未查证 5643；新增不一致 24 条（全部 t–s 交界区段）。
* **主译变更 3 条**：
  * tautology「同义反复」→「重言式」（审定·数学/信息科技；逻辑学正条，正文 45 处本就用重言式，旧形降为亦作，仅改登记册——
    正文 7 处「同义反复」均为修辞义，不动）；
  * substitutional load「替换负荷」→「置换负荷」（审定·遗传学；`e/ecological-genetics.md` 看齐）；
  * time dilation「时间膨胀」→「时间延缓」（审定·物理学；`s/spacetime-convensimul.transport-clocks.md` 看齐）。
* **保留 21 条**，归类：
  * 跨学科同名/假阳性：substitution rule（化工「取代法则」）、substratum（农学/语言学）、superimposition（物理学「叠置」，
    本条佛学 samāropa「增益」）、surjection、survivals、synchronic、temporal reflection、The Elements、the First、the Good、
    theory of play（教育学「游戏理论」异义）、theory theory、test (program)、taḥlīl / taʾwīl / taʿārīf（维基垃圾命中）。
  * 义项不同／对举体例：taxonomy（本条作「分类系统」义，审定「分类学」为学科名）、technical object（与「认知物」对举，
    审定「技术客体」为通名，保留「技术物」）、surrogacy / surrogate（哲学科学模型义≠生殖医学「代孕」）。
  * 学科定名差异：substructural logic（审定·计算机作「亚结构逻辑」，逻辑学界通行「子结构逻辑」，本条出处 logic-linear）。

### 九、第六批增量裁定（offset 2380–2468，11 条）

* 审计刷新：一致 603 / 不一致 406 / 查无 2196 / 未查证 5557；新增不一致 11 条。
* **主译变更 1 条**：transient polymorphism「暂态多态性」→「过渡性多态性」（审定·遗传学；`e/ecological-genetics.md` 2 处看齐）。
* **保留 10 条**：timelike trajectory / tractability / Tractatus / Transcendental Deduction（社会学假阳性）、Topics（档案学「题目」异义）、
  Torah（社会学「律法」义，本库取音译「托拉」）、transcendentalism（本条 emerson 美国超验主义义，审定「先验主义」为康德/马克思主义义）、
  transcendentals（命中为形容词 transcendental）、trope / tropes（音乐「附加段」异义）。

### 十、第七批增量裁定（offset 2468–2516，4 条）

* 审计刷新：一致 610 / 不一致 409 / 查无 2236 / 未查证 5507；新增不一致 4 条，**全部保留现译**：
  type-form（风景园林「植被型」假阳性）、typology（本条圣经预表论义，审定「模式概念/类型学」异义）、
  units of selection（审定·自然辩证法「选择单位」为佐证；本条与词条标题「选择的单位与层次」一体，学界通行「选择的单位」，
  改形牵动 SUMMARY 标题，保留）、unity of opposites（审定命中为「对立统一规律」下位短语）。

### 十一、第八批增量裁定（offset 2516–2548，6 条）

* 审计刷新：一致 611 / 不一致 415 / 查无 2261 / 未查证 5475；新增不一致 6 条，**全部保留现译**：
  universal characteristic（铁道「万有特性」假阳性，本条 Leibniz 普遍文字）、universal relation（本条逻辑义「普适关系」，
  审定 CS「泛关系」为数据库义）、universal time（本条 Milne 宇宙学「普适时间」，审定天文「世界时」为时间标准异义）、
  universal validity（心理学「普遍效度」异义）、universals（航海形容词命中假阳性）、unwritten doctrines（社会学假阳性）。

### 十二、第九批增量裁定（offset 2548–2588，3 条）

* 审计刷新：一致 619 / 不一致 418 / 查无 2286 / 未查证 5494；新增不一致 3 条，**全部保留现译**：
  valence（本条情感「效价」义，审定化学「化合价」异义）、vega（航海恒星名命中假阳性）、venesection（社会学假阳性）。

### 十三、第十批增量裁定（offset 2588–2620，5 条）

* 审计刷新：一致 622 / 不一致 423 / 查无 2311 / 未查证 5474；新增不一致 5 条（vis viva 因两行同键重复计 2）。
* **登记补亦作 2 条（主译不变）**：virtue ethics「德性伦理学」、virtue theory「德性论」——审定名词库作「美德论」（自然辩证法/医学伦理学），
  但本库正文「德性伦理学」23 处、「德性论」15 处为主流学界形，「美德论」4 处并存；登记行补「亦作‘美德论’」并记审定凭证，
  既消 ripple 信号又不改通行形。
* **保留 2 条**：vis viva（命中「活力积分/活力方程」为派生公式下位词）、viśeṣa（维基垃圾命中）。

### 十四、第十一批增量裁定（offset 2620–2668，4 条）

* 审计刷新：一致 629 / 不一致 425 / 查无 2349 / 未查证 5427；新增不一致 4 条，**全部保留现译**：
  void space（船舶「浮力舱」/水利「孔隙」异义）、weak counterexample、weak foundationalism、weakly compact cardinal
  （后三条均社会学库假阳性命中）。

### 十五、第十二批增量裁定（offset 2668–2700，4 条）

* 审计刷新：一致 632 / 不一致 429 / 查无 2372 / 未查证 5397；新增不一致 4 条，**全部保留现译**：
  well-formed（审定作「合式[的]」，与现译仅方括号记法差异）、well-founded（命中「良基语义」下位词）、
  winning strategy（审定·计算机作「赢取策略」，逻辑/博戏文献通行「制胜策略」）、Wistar Institute（维基垃圾命中）。

### 十六、第十三批增量裁定（offset 2700–2732，1 条）

* 审计刷新：一致 639 / 不一致 430 / 查无 2395 / 未查证 5397；新增不一致 1 条，**保留现译**：
  world community「世界共同体」（审定·世界历史作「国际社会」World Community，本条政治哲学语境取通行直译）。

### 十七、第十四批增量裁定与本轮收官（offset 2732–2772，5 条）

* 审计刷新（本轮终态）：一致 643 / 不一致 435 / 查无 2425 / 未查证 5358（术语 4863 + 人名 3761，共 8624 行）；
  新增不一致 5 条，**全部保留现译**：ε-notation（审定命中为 μ/λ 记号平行词）、yi (arts)（六艺下位）、
  yielding（维基垃圾）、Zionism（本条朔勒姆历史语境用「锡安主义」，审定「犹太复国主义」为通名，登记行已注亦作）、
  zombie（生物物理「无魂人」/计算机「僵尸机」异义）。
* **本轮队列收官**：术语表未查证队列 2772 项全部跑完（offset 1804→2772 由本会话承接，前段 0–1803 已由前批完成）；
  凭证总量 3484 份（ok 3117 / empty 287 / error 80，错误率 2.3%）。**二轮 `--emit --unverified` 实测 1951 项**——
  除 error 外还包含队列重建/排序错位造成的漏查段（offsets 0–1803 并未真正落凭证），不能按 error 数估计二轮规模。
* 本轮累计增量裁定 14 批 122 条，主译变更 12 条（shifting balance theory、somatic mutation theory、spontaneous generation、
  strict finitism、subjective well-being、tautology、substitutional load、time dilation、transient polymorphism、
  Stoic/斯多亚→斯多葛全库统一、virtue ethics/virtue theory 补亦作）；其余 110 条保留并逐条留理由。
* 二轮补查队列同日起跑（1951 项，`%TEMP%/az-term2.json`，`--start 0 --batches 600 --no-warm --interval 10 --batch-gap 20`），
  断点续写 `state/tl-crawl-state.json`；ingest watcher 常驻，凭证随跑随提。

## 2026-11-11 二轮补查增量裁定（TL-main-20261111 续）

### 一、二轮第一批（offset 32–208，25 条，a 段重查）

* 审计刷新：一致 662 / 不一致 460 / 查无 2564 / 未查证 5193；新增不一致 25 条。
* **主译变更 2 条**：accidental generalization「偶然概括」→「偶适概括」（审定·自然辩证法；`s/scientific-explanation-20th.md` 2 处看齐）、
  anthropocentrism「人类中心论」→「人类中心主义」（审定·自然辩证法，且为正文多数形 5:3；3 处看齐）。
* **保留 23 条**，归类：
  * 通行形为主、审定形为地区/学科变体：agreeableness（海峡两岸「亲和性」，本库大陆通行「宜人性」）、
    authoritarian personality（审定「权威人格」，本库沿《权威主义人格》书名通行）、anti-intellectualism（本条 Ryle 谱系
    与「理智主义」对举）、anthropomorphism（宗教哲学「神人同形同性论」≠心理学「拟人论」）、
    act-utilitarianism（审定两库形不一：行动效用论/行为功利论，通行「行为功利主义」与规则功利主义对举）、
    arithmetical hierarchy（审定数学「算术分层」/计算机「算术层谱」两形并存，递归论通行「算术层级」）、
    absolute music（审定音乐「纯音乐」，美学「绝对音乐」）。
  * 跨学科同名/假阳性：a posteriori（最大后验/后验法）、abhāva（维基垃圾）、abstractionism、age of onset、
    analogy many-to-one、antecedent/consequent（本条逻辑「前件/后件」≠数学「前项」）、anticipation、appetite、
    argument from above/below、arousal theory（下位）、association relation、anti-theory、back-and-forth、
    bar induction、Barwise compactness theorem、affirmative action（审定为「肯定性行动计划」下位，通行「平权行动」）。

### 二、二轮第二批（offset 208–264，11 条，b/c 段补查）

* 审计刷新：一致 672 / 不一致 469 / 查无 2598 / 未查证 5169；新增不一致 11 条，**全部保留现译**：
  * 体例/通行形：belief contraction / expansion（AGM 正条用裸形「收缩/扩充」，与修正对举；审定「信念收缩/信念扩展」为复合形）、
    bisimulation（模态逻辑通行「互模拟」9 处，审定 CS「双模拟」）、cancer stem cell（肿瘤生物学通行「癌症干细胞」15 处；
    审定命中出自化工名词库）、Cartesian product（审定「笛卡儿积」与人名表主形「笛卡尔」不一致，保留「笛卡尔积」）。
  * 假阳性/下位：belief merging（审定「信念融合」，本库 31 处用「信念合并」）、Big Five（量表/模型下位词）、
    body politic（命中 body politics 异词）、cardinal（语言学/地理异义）、causal closure（审定「物理因果闭合」为限定短语）、
    bhūta（维基垃圾）。

### 三、二轮第三批（offset 264–328，12 条，c 段补查）

* 审计刷新：一致 680 / 不一致 481 / 查无 2630 / 未查证 5117；新增不一致 12 条。
* **主译变更 1 条**：communitarianism「共同体主义」→「社群主义」（审定·社会学/医学伦理学；正文原为 15:14 混用，
  `aesthetic-concept` / `african-ethics` / `kant-reason` / `korean-philosophy` 4 文件 15 处归一；
  撤销 2026-11-09「以别于共同体形态描述」的体例注，旧形降亦作）。
* **保留 11 条**：character（本条伦理学「品性」，审定医学「性格」异义）、chatbot（大数据「陪聊机器人」异形）、
  cell-of-origin（通信「原点小区」假阳性）、cheng（档案学「呈」异字）、chuch’e（维基垃圾）、circumscription（AI 逻辑
  「限定推理」，审定 CS「限定理论」为名词形；与国际法「限缩」分义）、classical conditioning（正文通行「经典条件作用」9:0，
  审定生理学「经典条件反射」）、collapse model（生物物理下位词）、communication rule（超矢列演算直译，审定新闻传播「沟通规则」异义）、
  competence（农学/医学遗传「感受态」异义）、competence（医疗与法律语境，维基垃圾）。

### 四、二轮第四批（offset 328–400，11 条，c 段补查）

* 审计刷新：一致 689 / 不一致 491 / 查无 2663 / 未查证 5065；新增不一致 11 条。
* **主译变更 2 条**：conceivability argument「可设想论证」→「可设想性论证」（审定·自然辩证法；`z/zombies.md` 17 行看齐）、
  constructive empiricism「建构经验主义」→「建构经验论」（审定·自然辩证法；`s/scientific-explanation-20th.md` 看齐）。
* **保留 9 条**：complement（生化「补体」异义）、computably enumerable（命中为复合词下位）、conceptual scheme（风景园林
  「方案设计」假阳性）、condensation（本条弗洛伊德「凝缩」≠物理「凝结」）、congruence（数学「同余式」异义）、
  conscientiousness（海峡两岸「严谨性」，大陆通行「尽责性」）、constellation（本雅明「星丛」≠天文「星座」）、
  continuity axiom（审定「连续公理」为 axiom of continuity 名词序，正文 24:0 通行「连续性公理」）、conversion（档案/化工异义）。

### 五、二轮第五批（offset 400–512，17 条，d 段补查）

* 审计刷新：一致 707 / 不一致 506 / 查无 2720 / 未查证 5171；新增不一致 17 条。
* **主译不变，登记补记 2 条**：degree of belief「置信度」补亦作“信念度”（审定·自然辩证法作“信念度”；正文 24:14 两形并用，
  取并记以消 ripple）、domain ontology「领域本体论」登记行注明审定作“领域本体”，因与 upper ontology“上层本体论”对举，
  沿用本词条体例。
* **保留 15 条**：coproduct（化工「联产品」异义）、corporations（本条社团主义「等级团体」义≠公司）、
  cosmogony（本条宇宙生成论≠天文「天体演化学」）、cost of natural selection（审定去“的”体例差异）、
  covering law model（审定「说明的覆盖律模型」为全称短语）、Cut rule（逻辑学界通行「切规则」，审定数学「截规则」）、
  deduction theorem（社会学假阳性）、default reasoning（海峡两岸「默认推理」，大陆通行「缺省推理」）、dereliction（假阳性）、
  dharma（维基垃圾）、dialectician（假阳性）、dictator game（假阳性）、disputation（维基命中「九十五条论纲」）、
  doctrinal paradox（假阳性）、downward causation（术语短形，审定「下向因果关系」为全称）。

### 六、二轮第六批（offset 512–608，12 条，e/f 段补查）

* 审计刷新：一致 722 / 不一致 517 / 查无 2775 / 未查证 5089；新增不一致 12 条。
* **主译变更 2 条**：
  * empirical adequacy「经验充足性」→「经验适当性」（审定·自然辩证法；van Fraassen 标准形；`s/scientific-explanation-20th.md` 2 处看齐）；
  * finitism「有限主义」→「有穷主义」（审定·自然辩证法；与已改的 strict finitism「严格有穷论」配套）。**连带题名同步**：
    `g/geometry-finitism.md` H1、`SUMMARY.md`、`mu-lu-s.md` 三处题名改「几何学中的有穷主义」；`qian-yan/ri-zhi-yu-bian-ji-gui-hua.md`
    2024 年旧编辑日志原件不动（历史记录）；`a/arabic-islamic-phil-math.md`、`h/hilbert-program.md`、`i/intuitionism.md` 正文/标题看齐。
* **保留 10 条**：emanation（放射医学「射气」异义）、empirical deduction（假阳性）、enactivism（假阳性）、endogenous / exogenous
  （动物学「内源/外源」词形差异）、explication（本条卡尔纳普「阐释」为技术术语，「阐明」是一般动词，不可互换）、
  expression（本条美学「表现」义）、extraversion（审定「外向」为词形差异，人格维度通行「外向性」）、facet（昆虫/电子异义）、
  filtration（农学/化工「过滤」异义）。

### 七、二轮第七批（offset 608–896，22 条，g–m 段补查）

* 审计刷新：一致 779 / 不一致 546 / 查无 2988 / 未查证 5160；自上一留档点（offset 608）以来新增不一致 22 条。
* **主译变更 3 条（+1 派生）**：
  * lexicographic order「词典序」→「字典序」（审定·数学名词；`b/belief-merging.md` 2 处、`l/logic-preference.md` 1 处、
    `r/ramsey-economics.md` 2 处看齐）；派生 leximax「词典最大算子」→「字典最大算子」（`b/belief-merging.md` 1 处），旧形均降亦作。
  * logical pluralism「逻辑多元论」→「逻辑多元主义」（审定·自然辩证法；词条题名与正文本就用「主义」6 处，登记行归正）；
  * logical monism「逻辑一元论」→「逻辑一元主义」（同一审定来源，配套对称改形；正文无旧形）。
* **保留 18 条**，归类：
  * 通行形为主/语境限定：folklore psychology（审定「民族心理学」为 Völkerpsychologie 异义，本库哲学心灵义「民间心理学」）、
    homogeneity（现象学语境「齐一性」，审定农学/生化「同质性/均一性」为他义，登记已注亦作）、
    indivisibility（语义学「不可分」词形，审定「不可分性」为名词形）、infectious agent（流行病学通行「传染因子」，
    审定免疫学「感染原」）、logical positivism（通行「逻辑实证主义」，审定「逻辑实证论」）、locative media（新媒体艺术「定位媒体」，
    审定新闻传播「定位媒介」）、Lexicographic 相关之外：Five-Factor Model（审定「人格五因素模型」为全称，正文「五因素模型」）。
  * 下位/全称短语：higher understanding（中华思想文化「下学上达」全称）、Huang-Lao（「黄老之术/黄老道」下位）、
    Lvov-Warsaw School（审定「华沙学派」短形）、impetus theory（资源科技「压力动力原理」异义）。
  * 跨学科同名/假阳性：guṇa（维基垃圾）、Han Shu（「蜀汉」假阳性）、historicity（地理「史实性」）、import（计算机「导入」/
    经贸「进口」）、incontinence（医学「失禁」）、independence constraint（化工 LICQ 复合词）、left-continuous（审定记法差异）、
    maieutic reflection（社会学假阳性）。

### 八、二轮第八批（offset 896–1192，43 条，g–p 段补查）

* 审计刷新：一致 818 / 不一致 586 / 查无 3198 / 未查证 4938；新增不一致 43 条。
* **主译变更 1 条**：paradigm shift「范式转移」→「范式转换」（审定·自然辩证法；正文两形 1:2，`k/kant-development.md` 看齐，旧形降亦作）。
* **保留 42 条**，归类：
  * 通行形为主／词形-标点差异：mark-recapture method（审定「标记重捕法」仅连字符差异）、multiple realizability（通行「多重可实现性」，
    审定「多重实现性」）、ordinal sum（模糊逻辑 t-范数通行「序和」，审定「序数和」为序数运算）、ordered pair（通行「有序对」，
    审定「序偶」）、model checking（通行「模型检验」，审定「模型检查/模型校验」）、non-coding RNA（空格体例差异）、
    multimodality（审定「多模态」名词形）、optogenetics（通行「光遗传学」，审定「光控遗传修饰技术」）、
    one-time pad（通行「一次性密码本」，审定「一次一密」）、mechanistic explanation（本库 explanation=解释，审定作「机制说明」）、
    natural magic（科学史通行「自然魔法」，审定「自然巫术」）、niche（本条干细胞生物学「干细胞龛」，审定「生态位」为生态学义）、
    nativism（本条与经验论相对「先天论」，审定语言学「天赋论」）、operational semantics（本条 Fine 术语直译「算子语义」，
    登记行已注明与 CS 分义）、oracle（本库 4:0 用「预言机」）、overdetermination（本条因果义「过度决定」，审定马克思主义「多元决定」）、
    optimality model（生物学哲学通行「最优性模型」，审定生态「最适模型」）、multifactorial disease（流行病学通行「多因子疾病」）、
    one-to-one correspondence、mark transmission。
  * 下位/全称短语：measure problem（「不变测度问题」）、moral norm（「医学道德规范」）、optimality 相关、organ failure（「多器官功能衰竭」）。
  * 跨学科同名/假阳性：manas（《玛纳斯》）、Metaphysical Deduction、ming (name)（日名/祭名）、moral character（人力资源「品德」）、
    moral/conventional distinction（「德性」）、natural place（资源科技「自然标志地」）、omnisubjectivity、On the Heavens（穹天/平天说）、
    opponent（奥运「对手」）、ordinary object（消毒学「普通物体表面」）、ordo doctrinae、organic state（材料科学）、
    parallelism（档案「排比」/机械「平行度」）、paraphrase（音乐「释义曲」）、microworld（物理「微观世界」）、
    minimax（本条算子名「最小最大算子」，审定「极小化极大」为数学通名）、microbiota（农学/生态「微生物区系」）。

### 九、二轮第九批（offset 1192–1360，19 条，o–p 段补查）

* 审计刷新：一致 844 / 不一致 604 / 查无 3317 / 未查证 4775；新增不一致 19 条，**全部保留现译**：
  * 下位/全称/词序差异：part-whole relation（审定「整体-部分关系」为反序词）、partial order（「偏序关系模型/完全偏序集」下位）、
    Peace of Augsburg（审定「奥格斯堡宗教和约」为全称）、perfect number（数学通行「完全数」，审定「完满数」）、
    pornography（「色情内容/书刊」下位）、portfolio analysis（「技术组合分析」下位）。
  * 跨学科同名/假阳性：partial support（地理信息系统「局部地址支持」）、participation（社会学「参与」，本条柏拉图「分有」）、
    physiognomy（植物学「外貌」/医学「容貌」）、Physics（亚里士多德书名≠学科名）、personal projects、phantasia（维基垃圾）、
    picturesque、pollae myŏnmok（维基垃圾）、positive/negative analogy（测绘「正片」/大气「阳」假阳性）、possible intellect、
    potentia coactiva、perfection（perfectio / Vollkommenheit 两行，社会学假阳性）。

### 十、二轮第十批（offset 1360–1528，21 条，p 段补查；2026-11-12 接力会话补裁）

* 前会话爬至 1528 中断，本批为其遗留账（audit-2026-11-11 604 → audit-2026-11-12 625 差集）。
* **主译不变，登记补亦作 3 条**：
  * potential infinity「潜无限」补亦作“潜无穷”（审定·自然辩证法数学哲学/数学数学基础两库一致作“潜无穷”；
    正文 2:0 通行“潜无限”，与实无限对举体例不动）；
  * predestination「预定」补亦作“预定论”（审定·宗教社会学；本词条正文 19:0 通行“预定”）；
  * propositional function「命题函项」补亦作“命题函数”（审定·数学模型论；罗素《数理哲学导论》中译传统不动）。
* **保留 18 条**，归类：
  * 方括号/记法差异：predicative（审定·数学数学基础作「直谓[的]」与现译仅记法差）、principle of least action
    （审定「最小作用[量]原理」）。
  * 下位/全称：primitive recursive（审定全为「原始递归集/函数/谓词」复合下位）、proper name（命中「专有名称权」法律下位）、
    precession of the equinoxes（审定「分点岁差」为全称形）。
  * 跨学科同名/假阳性：pramāṇa（认知凭据义）/pratyakṣa（感官知觉义）（命中「义通/感官分析」无效，jayaraasi 体例分工已注册）、
    precautionary principle（审定无正命中，「谨慎原则」非本学科语境；登记行已有“预警原则”亦作）、prescind / precision
    （precision 工程义假阳性）、prime mover（「原动机」工程假阳性）、principle of individuation（命中出自器官移植学，
    非本学科语境）、priority base（偏好逻辑专门译名「优先基」，审定 CS 异义）、projectivism/proof net（垃圾命中）、
    promotion（线性逻辑指数规则，审定「促销/晋升」异义）、proper function 两行（「本征函数/凸函数」异义；与普兰丁格行
    分域已注册）、prospect（地质「远景区」假阳性）。

### 十一、二轮第十一批＝收官批（offset 1528–1951，41 条，q–w 段；2026-11-12）

* 二轮队列 1951 项全部跑完（本会话自断点 1528 接力 423 项；爬虫自愈降级多次、批末补跑救回大部分 error 词；
  **27 词补跑后仍降级**—— propositional attitude、pudgala、quantum computation、quantum logic、redistribution game、
  reflective equilibrium、religious epistemology、rhythm、sabellianism、samkhya（数目）等，集中在会话间歇失效段，
  留三轮 `--unverified` 重查）。
* 审计终态：一致 930 / 不一致 663 / 查无 3734 / 未查证 4405（较基线 +38；差集口径新增不一致 41 条，
  另有 3 条基线键因并行会话登记册改动出列）。登记册总量 9602→9732（并行会话词条批次新增行）。
* **主译变更 0 条，全部保留现译**；risk perception「风险感知」补亦作“风险认知”（审定·心理学三库一致）。
* 保留归类：
  * 记法/连字符/破折号差异：Robertson-Walker metric（审定作半角连字符「罗伯逊-沃克度规」，库内全角破折号体例）、
    risk-benefit analysis（「风险-获益分析」获益/收益＋连字符记法差）。
  * 下位/复合/全称：quantum gate（审定「量子逻辑门/通用量子门」下位）、public key cryptography（审定「公钥密码」无学后缀）、
    word association（审定「字词联想测验」为测验名下位）、Republic (Plato)（命中带作者全称「柏拉图理想国」）、
    right to life（命中「生命健康权优先原则」下位）。
  * 跨学科同名/假阳性/垃圾命中：pseudo-process（「假绝热过程」气象假阳性）、public philosophy（「公共教育哲学」下位）、
    pure intellect / reductio / resurrection / satisfaction（集体消费理论等垃圾池命中）、quiddity（与 essence 并置时）
    （「时/时延」 fuzzy 垃圾）、Quodlibets（奥卡姆）（「诺姆/雷姆」垃圾）、real objects（「实物」异义）、
    reference class（「参见类目」图书情报假阳性）、Reflection Principle（命中「施瓦茨反射原理」为复分析，
    本行 van Fraassen 决策论反思原则）、repeater（「中继器/留级生」异义，本行 paradox-suspense 构词直译）、
    repertoire（「库/字汇」异义，本行 model-organisms 词条术语）、representation theorem（命中「格兰杰表述定理」
    计量经济学下位；注意同族 Stone representation theorem 行作「表示定理」，分域并存留档）、resiliency（「市场弹性」
    经济假阳性，本行 Skyrms 概率用语）、responder（「反应者」生化假阳性，本行独裁者博弈对举）、restriction
    （「限制/相克」泛词，本行中世纪逻辑限缩）、right of nature（「自然资源产权制度」异义）、rule of consequence
    （反兴奋剂垃圾命中）、safety barrier（「安全栅/新泽西护栏」工程异义）、samadhi（审定「禅定」为通名，
    本行空海语境佛教汉语传统「三昧」）、samudghāta（TA克隆垃圾）、sanction（「裁定/判罚」竞技假阳性）、
    scheme（「概形」代数几何假阳性，本行塔尔斯基语境图式）、self-attribution（审定「自我归因」心理学，
    本行康德统觉自我归赋体例）、world-unity（命中空，康德世界统一性通行）。
  * 通行形与审定变体并存：prospect theory（审定「展望理论」×4，学界卡尼曼语境通行「前景理论」，
    登记行已有亦作注）、rational reconstruction（审定「理性重建」，科学哲学界两形并用沿既有行）、
    rationality（审定「理性」泛词，本库与 reason「理性」分立取「合理性」）、recognition（审定「再认/识别」心理学，
    本行亚里士多德 Wiedererkennung 再认识）、recipient（审定「受体/受益人」，本行独裁者博弈受赠者）、
    quantum-related 下位不另计。
* **维基排查 4 行说明**：Conventuals 为已撤证留痕；Herbrand/Nelson/Takeuti 三行系当日并行会话新增人名行，
  依据列为“中文维基同/英文维基确认”之提及性措辞（非引证权威），留待该线自查润色，本批不动。
* 本批后二轮队列收官；error 残量 27 词待三轮 `--unverified` 重建清点。

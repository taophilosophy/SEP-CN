# specs/011 执行记录

## 2026-11-02 开工：预清理与收口

* 门禁三红清零：术语硬错 3（Bernard Williams 人名表「威廉斯」vs 词汇表「威廉姆斯」冲突、登记册 conditional independence 重复行、人名表 Wolterstorff 重复行）+ 分类目录 1（james-ward 穆勒目录「瓦德」）全部修复；Williams 定案译名同步弱势方 39+5 处（integrity 正文 39 处、词汇表/SUMMARY/mu-lu-s/词条标题 4 处）。提交 71e104ff。
* 信息非对称识别：i/information-biological.md 的 Williams 1992 = George C. Williams（进化生物学）、i/implicature-optimality-games.md 的 Asher/Sher/Williams = 语用学作者，均非 Bernard Williams，不改；两人未在 ren-ming-biao 登记 → 人名反向校对层补登记。
* 工作区收口：26 条 s3_checked/done 逐条提交（a5/b1/d1/h3/i17）；48 条在途中间态快照 + check_style 改进 + i 批 monitor 提交 641faf13。
* 剩余未跟踪 345 文件为临时装配/分块脚本（_tr_*.py、_asm_*.json、trans_p*.json、tasks/e/_tr_*.json 等）——不提交；移交清单待收口时统一裁定清理。
* 战役 spec 建档。下一步：机械层全跑。

## 2026-11-03 机械层全跑与 style 修复（三版迭代）

* 扫描器 `bin/mechanical_scan.py`：152 条有实质译文词条（A41/B14/C26/D14/E8/F1/G1/H16/I23/J6/K1/S1）全量 check_style/check_math/check_academic。首跑：style 55 条 1602 处（italic-cjk 823、bold-spacing 406、curly-quotes 272、no-html 59、cjk-spacing 42）、math 8、academic 16（全为在途尾节缺失，预期态豁免）。
* **v1 事故与止损**：italic 修复器 ITALIC_RE 在 `**X**（*Y*）` 粗斜相邻结构跨对错配，且产生文本重复（al-khunaji「通达其在，我们也无需通达其」），复验门只查三类残余查不出此类损坏 → rules/05 基线还原：ledger 逆向回滚 56 段 + 41 个纯修复产物文件整体 checkout 还原至 83fc857^；final_star_audit/final_dup_audit 双终审（星号 tokenizer + ≥8 字重复，对照 83fc857^）确证 18+2 行破坏全部回收。
* **v3 安全形态**：italic 降级——行内已有粗体（粗斜共存）一律不自动替换，挂人工；星号结构不平衡（畸形）行整行跳过；仅纯斜体行自动替换。43 条 514 处，终审破坏/重复双零。人工清单 305 行（coexist/畸形/混合连坐）落 style-fix-manual.jsonl。
* check_style 工具改进三项：①bold-spacing 遮蔽数学区间星号误配（$w^{**}$）；②curly-quotes 转写撇号遮蔽（词内双侧拉丁/边界起始两规则，汉字邻接豁免——法语 l'âme、希伯来 Shi'ur、阿拉伯 Ya'qub 不再误报）；③影响全库门禁口径，复跑无回归。
* copernicus 直角引号「」32 对+『』1 对转弯引号；impossible-worlds 混合型 4 处、africana 12 处人工定点。
* math 8 条（alberic-paris/boolalg-math/change/computability/heytesbury/hilbert-program/impossible-worlds/information-semantic）移交管线会话（数学转换域）。

## 2026-11-03 术语同步与人名反向校对

* `bin/term_verify.py` 二重验证：term_coverage 全量缺口 834 术语 + 44 人名 → EN 正文级确认（yuanwen 剔 References）+ zh 正文级变体确认（登记册行全串、按顿号／分号拆分）→ 558 条缺口落盘 term-verify.jsonl（证据链完整）。
* **人名反向校对 26→25 条逐条裁定**：
  - A 类真缺口（译文用字 vs 登记册裁定偏差）修弱势方 5 处共 41 替换：腓茨拉尔夫→菲茨拉尔夫（crathorn）、狄迪穆斯→迪迪穆斯×4 + 泰奥弗拉斯托斯→特奥弗拉斯托斯×34（doxography-ancient）、卡姆斯勋爵→凯姆斯勋爵（aesthetics-18th-german）、德雷特斯基→德雷斯基（information-semantic）。
  - B 类非缺口（现代学者保留英文体例，体例明文允许）：Quine×2、Baier、Lewontin、Wright、Levinson、Habermas、Cavell、Koyré、Hull、Gilligan、Smith、Earman、Norton、Adams、Mersenne、Wiggins 等——**登记册汉译行与体例的张力移交 008 裁定**（登记行去留/用途标注）。
  - C 类漏译疑点（zh 正文无汉译无 EN 残留而 yuanwen 正文有）：Habermas@aesthetics-critical-theory、侯奈因@al-kindi、Theophrastus@democritus、Van Helmont@elisabeth-bohemia、ibn-ezra、Wiggins@identity——移交镜像完整性流程逐条回源核对。
  - 新发现人名异译重复行：Jean Hampton（L77 让·汉普顿 2026-11-01 vs L316 琼·汉普顿 justice-virtue 2026-11-02 凭证优先）——留 316 行裁定待执行。
* 双词术语 93 条（done/s3/r1 范围）：抽样定性三类——拉丁术语保留原文（prima facie 体例张力）、译名偏差（条件句分析 vs 条件分析@abilities）、英文残留——裁定尺度属 008 术语战役职权（需查证流程），011 以 term-verify.jsonl 证据链移交，不越权批量改译。
* 单词术语 ~440 条：EN 词边界匹配对普通词（play/completion）误报率过高，工具方法局限登记，移交。

## 门禁终态

* check_all 7 项：6 绿 + 学术规范 1 红（529 处全部为 48 条在途词条尾节缺失 + 已知在途态，f–k 六批接管会话（ses-FGHIJK-main-1103）推进中）。
* 本战役范围（152 条复核对象）内：术语硬错 0、词汇表滞后 17（告警级移交）、分类目录 0、星号/重复破坏 0。

## 2026-11-03 待办全消化轮（用户裁定：不计成本、不移交）

* **术语三向全绿**：Hampton 异译重复行删旧留新；check_terms 词汇表解析补全（亦译/亦音译前缀+连排引号）与滞后口径收窄（只报词汇表缺）；词汇表 5 行补变体+Simplicius 冲突修弱势方。硬错 0 滞后 0。
* **math 8 条归档**：全部为 yuanwen 镜像 $ 平衡（009 已登记 T-math-macro-closure 家族，镜像须与转换器逐字符一致不可手改），011 记录引用不重复处理。
* **C 类漏译疑点 6 条回源核毕**：4 条异译对齐（泰奥弗拉斯托斯@democritus、维金斯@identity、赫尔蒙特@elisabeth-bohemia、胡奈因@al-kindi）+ ibn-ezra 埃兹拉→以斯拉 ×210；哈贝马斯=简形合法（term_verify 加名字段简形豁免）。
* **双词术语 53 对全量裁定**：译文对齐登记 214 处（意向行动×68/宗教信念×6/因果说明×8/特殊能力×17/小提琴家×35/先前·当前自我×102/传出副本×22/自由变元/差别原则等）+ 登记册 12 行补亦作与域注（条件句分析/能动理智/两种真理域注/存在论承诺/无限回溯/共通感觉/自相勿混域注/茶道/证成的真信念/理论德性/视觉知觉）+ 词汇表批量同步 8 行。
* **单词术语 64 对裁定**：term_coverage 变音符折叠误报根治（Nō→no 撞词 111 条清零，含变音符键用原文形态匹配）；核心词条组 5 对（3 拉丁豁免+2 语义落实）+99 对普通用法豁免——唯一对全量裁定完毕。
* **style v4**：italic 线性 tokenizer 根治正则回退跨对（v1/v2/v3 事故总根因：*Latin* 闭星错当开星吞整段中文，al-khunaji L54 复现实锤）；空格斜体对整对保留、** 块跳过；粗斜共存行放开自动处理；star_ok 列表项豁免。intensional 原始译文 61 行星号畸形修复至 4 行遗留（类型论记号结构性冲突）。
* **并行会话漂移处置**：mu-lu-s 四行英文标题错位对齐 SUMMARY（排除别名链行）；Norris 重复行去重；legrand 批新增登记行不混提。
* **遗留登记**：①intensional 4 行类型论记号+165 处逻辑式排版（重译域，需数学定界）；②人工深读 152 条未展开（机械层已全绿覆盖其外延）；③autrecourt 7 行/akan-person 3 行畸形（还原后即干净，已随还原批解决）。

## 2026-11-03 深读层启动（主会话直读，009 已覆盖 18 条去重后待读 141）

* 深读台账 `results/manual-deepread.jsonl` 建立；009 三层深读（1%+3%+5%，裸 slug 口径）覆盖去重后 141 条待读，清单 `results/deepread-todo.txt`。
* 已完成 8 条全 pass：abduction.peirce、abduction、abelard、abhidharma、abilities（实修：特定→特殊能力 7 处统一登记主形，粗体+括注阻隔形态教训）、abner-burgos、abortion、abrabanel。
* 深读协议：全文通读+结构连续性+术语人名抽检；上游笔误保真与 T-07 空壳 H3 为已知形态族不记缺陷；逐条 verdict 落台账、每批提交。

## 2026-11-04 主题词汇解析轮（用户建议：根据每篇文章主题重新解析词汇）

* `bin/topic_vocab.py` 三层解析器：L1 标题词（SUMMARY 英文题名去作者↔中文题名）、L2 正文斜体术语（yuanwen 剔尾 *term* 词频）、L3 登记落实。162 词条全量解析落 `results/topic-vocab/entries.jsonl`。
* **L1 标题词**：138 未登记三分（人名 34/概念词 41/题名短语 63）——真术语 33 条经 rowspec 落册（adaptationism 适应主义/haecceitism 此性论/frame problem 框架问题/personal identity 人格同一性/impossible worlds 不可能世界/ontological argument 本体论论证/华严宗/预先指示/动态选择等）；题名短语（The Ethics of Abortion 型）跳过（SUMMARY 已锁定定名不重复登记）。
* **人名 34 条**全部未登记（正文已用译名而人名表缺行）→ rowspec-persons 落册（SUMMARY 定名沿用格式，与 legrand 批先例一致）。
* **L2 斜体术语**：1685 未登记经著作名词典/拉丁短语/功能词三层过滤 → 真概念 8 条落册（cogito 我思/scientia/cognitio/pneuma 普纽玛/hegemonikon/modi significandi 意指样式/yin/yang）；其余确认为著作名照录体例与斜体强调误抓，不登记。
* **本轮净新增登记 75 条**（T 41 + P 34），term_flow 锚点格式教训（`| key |` 规范化、strip 顺序）入 rowspec 生成器。
* 深读层并行推进中（manual-deepread.jsonl 逐条台账）。

## 2026-11-04 深读滚动续

* 累计深读 15 条全 pass（+academic-freedom 2026 新发词条、action-perception 传出副本对齐态实证、action 意向行动对齐态实证、actualism-possibilism 实修版本行粗体违例+登记册补伦理学域注、adaptationism 因果说明对齐态实证、addams-jane）。
* 实修 2 项：abstract-objects 奎因→蒯因 7 处；actualism-possibilism 版本行 ** X ** 违例 1 处。
* 并行漂移随修 3 轮：mu-lu-s 四行全题化（mulu_sync.py 通用工具）；apperception 再生重复行去重并记双来源；Kant 人名重复行、Spinoza 词汇表冲突、leibniz-evil 登记重复 2 行（删旧并记来源）——**登记册/人名表重复行随并行会话新登记不断再生，每轮收口前 check_terms 必跑**。
* 主题词汇解析轮完成（独立节见上）。

## 2026-11-04 star_ok v2（交叉判据）与 v5 交叉纠正器

* star_ok 升级：①类型交叉即不健康（*X **Y** Z* 平衡但渲染必错乱形态，此前漏检）；②数学定界内星号剥离；③`***` 粗斜组独立 token（***版本行***）；④`(\*+)` 公式编号记号豁免；⑤转义星豁免；⑥列表项豁免。
* v5 交叉纠正器 cross_fix.py：括号书名/粗体截断等启发式规则，19 行修复。
* v2 判据全库重扫残留 63 行/25 文件（多为 mixed 挂人工行与逻辑式行的新交叉形态）——清单 cross-star-todo.txt，下批扩规则。
* 深读累计 15 条全 pass（新增 abstract-objects 实修奎因→蒯因 7 处、academic-freedom 2026 新发词条、action-perception/action/adaptationism/addams-jane/aesthetic-concept/actualism-possibilism 实修版本行+登记域注）。

## 2026-11-04 深读滚动续二 + 交叉星 v6

* 交叉星 v6：括号边界约束规则（（**X**）→（*X*）书名斜体、方括号、斜体闭多星）修 14 行；aesthetic-experience L311 手修两段（看作/悲伤的+是）；aesthetics-18th-french **标题作者括注截断**（SUMMARY 源头即坏——对照英文源修结构链三处）+L45 法语术语引号斜体 4 组。残留 ~40 行（intensional 类型论域 7 行+长尾）。
* 深读累计 17 条全 pass（+aesthetic-concept、aesthetics-18th-french 实修标题截断）。**新发现类型：SUMMARY 标题截断**（作者括注丢失半个括号）——结构事实源链（SUMMARY/mu-lu-s/H1）三处联动修复先例。

## 2026-11-04 标题截断批量修复轮（新缺陷类型：SUMMARY 作者括注截断）

* a/abelard 之外的发现链：aesthetics-18th-french H1 括注不配对 → 全库扫 SUMMARY 括号平衡 → **16 处标题截断实锤**（第一作者名+开括号丢失族）。
* 修复溯源：en/<slug>/index.html 的 citation_author meta（完整作者列表）+ yuanwen H1（完整英文题名主体）重建 `(全作者)` 括注；SUMMARY/mu-lu-s/词条 H1 三链同步；别名行与正式行分别处理。
* **事故与止损**：第一版脚本循环内反复读写 SUMMARY 致文件损坏（git checkout 恢复）→ 原子化改写；mu-lu-s 1856 处批量去噪未验证即提交引发分类目录红 → 回滚该改动、以 mulu_sync 16 行精确对齐收口。
* **教训**：①对单一事实源的批量写必须内存积累单次写回；②大规模格式变更（>千处）必须抽样验证后再提交；③SUMMARY 别名行（——见结构）与正式行的修复逻辑必须分流。

## 2026-11-04 mu-lu-s 噪声判定关闭

* 复核确认：mu-lu-s 的 `[*别名——见Y 词条题名]` 形态系收编 SUMMARY 别名行的历史合法形态（mu-lu-s 无转义符，与 SUMMARY 的 [\* 形态不同源），**无需去噪**——上一轮回滚正确，遗留项关闭。mulu_denoise.py 验证工具入库（0 命中即证明）。

## 2026-11-04 深读滚动续三 + mu-lu-s 噪声判定关闭

* mu-lu-s 的 [*别名——见Y 形态确认为历史合法形态（mulu_denoise.py 验证 0 命中），上轮回滚正确，遗留项关闭。
* 深读累计 17 条全 pass（+aesthetics-18th-german、aesthetics-18th-british——德意志/英吉利美学谱系质量上乘）。
* 深读实证结论（A 批 17 条样本）：40 路管线译文整体质量上乘；实修仅译名一致性小项（奎因→蒯因 7、特定→特殊 7、版本行 1）；结构/术语/引文体系零硬伤。

## 2026-11-04 术语地道性审查轮（用户要求：确保术语地道、符合传统）

* **核心根词审查**：48 个哲学基础术语对照中文学术传统（being/ontology/a priori/transzendental/Verstand/arete/phronesis/categorical imperative/thing-in-itself/the One 等）——已登记项全部地道（Dasein 此在、定言命令、eudaimonia 幸福与既有裁定同构）；**36 个基础根词从未入册**（being/category/substance/consciousness 等）→ 34 条按传统译法落册（一词多语境的主形+语境括注体例：understanding 知性（康德）／理解（日常）、mind 心灵／精神（Geist）、idea 理念／观念分域）。
* **可疑模式扫描**：形容词「的」尾（合理形态豁免）、人名音译无括注（惯例豁免）、**同键异译分立行**（真问题）——fold 归一（含连字符变体）扫描出 2 组合并：prima facie 初显的（亦作初步的，罗斯初定义务语境通译）、truth conducive 导向真理的；Motoori 重复行去重。
* **check_terms 工具盲区登记**：自洽检测只查整行重复，同键异译分立（初步的/初显的分立两行）不报——fold 归一检测待下轮工具化。
* 本轮净新增登记 34 条 + 合并 3 行。深读累计 17 条全 pass。

## 2026-11-04 作者括注体例归一轮（aesthetics-critical-theory 深读发现）

* 发现：SUMMARY/H1 作者括注存在 `姓, 名` 倒装形态 64 处（citation_author 原格式直录，与正装 `名 姓` 体例混用）。
* 修复：citation_author 溯源重建（名前姓后，多作者 SEP 格式 `A, B, and C`），SUMMARY/mu-lu-s/词条 H1 三链同步 64 条。
* 抽验：The Ethics of Abortion (Elizabeth Harman)、Implicature (Robert van Rooij and Michael Franke) ✓；剩余逗号形态为三作者分隔（合法豁免）。
* 双门禁绿。

## 2026-11-04 作者署名行体例归一（aesthetics-of-everyday 深读发现）

* 发现：词条内作者署名行（`*Last, First*`）倒装残留 5 处（aesthetics-18th-british/french、aesthetics-of-everyday、boethius-dacia、intuitionism-ethics）——与 87 条汉译正装署名行体例不一。
* 修复：citation_author 溯源正装化 5 处（*James Shelley* 等）；汉译登记（与 87 条汉译署名行统一）待后续批次——署名行的译名归属人名表域。
* slug 前缀坑第三次踩中（en/ 平铺结构 vs a/x.md 带前缀），工具函数统一记入。

## 2026-11-04 署名行汉译 + 深读续四

* 署名行汉译批次：6 作者人名表登记（詹姆斯·雪莱/詹妮弗·齐恩/雅克·莫里佐/斋藤百合子/斯滕·埃布森/马修·S. 贝德克）+ 5 署名行汉译括注体例（对齐 87 条汉译先例）。
* 深读累计 19 条全 pass（+aesthetics-existentialist 实修 H1/SUMMARY/mu-lu-s 英文题名补全 existentialist aesthetics、版本行空格——**H1 英文题名缺词**为截断族新变体）。

## 2026-11-05 ADR-0019 渲染域全库清零

* 发现链：aesthetics-race 深读 → 全库粗体内侧空格（`** X **` 渲染裸 **，ADR-0019 禁令）栈解析扫描 **398 处/23 文件**（actualism 100、leibniz 家族 214——并行会话管线标准形态）。
* 修复：栈定位重建修复器 scan_inner_space.py（扫描/修复双模；等长占位剥离终版——正则扫描跨对假阳性 1046→398、剥数学 offset 错位、跨数学星号误配三轮教训）；正则兜底 33 + 栈定位 207 + 手修 6 + 终修 3 = **全库清零**。check_render_artifacts 验证通过。
* 教训：正则无法解决星号形态学（跨对/交叉/数学邻接三重假阳性），栈解析唯一可靠；占位剥离必须等长保 offset。

## 2026-11-05 深读滚动续五

* 深读累计 22 条全 pass（+african-sage 全文通读蒯因对齐再实证、africana 850 行大部头三阶元哲学体系、akan-person 实修）。
* **截断族形态学扩展**：akan-person 的 H1 英文题名主体丢失（"of the person" 残段）——与 16 条作者括注丢失型不同的第二形态；yuanwen H1 重建法通用（对照 citation_author 补作者括注）。
* ADR-0019 渲染域清零已入账（独立节见上）。

## 2026-11-05 深读滚动续七

* 深读累计 28 条全 pass（+al-farabi-psych、al-khunaji、albalag、boethius-dacia、buddhism-huayan——A 批收口推进至 B 批）。
* check_terms 同键异译分立告警工具化入库；倒装括注 64 处+署名行体例归一；ADR-0019 渲染域 398→0（scan_inner_space.py 栈解析双模入库）。
* 体例归一轮：作者括注倒装正装化（SUMMARY/mu-lu-s/H1 三链）+署名行汉化（6 作者登记+5 行）。

## 2026-11-05 术语在线审定库复核轮（75 条概念术语）

* 批量爬虫 tl_crawler.mjs（断点续爬 JSONL 增量，7 段跑完 75 词，0 error）；凭证落盘 termonline-all（ok=73 empty=2）。
* 裁定（match=2 池污染过滤后取 en 精确相等命中 46 条）：
  - **✓一致 36 条**：being=存在、category=范畴、causality=因果性、consciousness=意识、idea=理念、necessity=必然性、ontology=本体论、perception=知觉、personal identity=人格同一性、evolution=进化、free will=自由意志 等——核心根词传统译法获审定库佐证（多数命中自然辩证法·科学哲学学科，语境正确）。
  - **跨学科同名 8 条保留现译**：frame problem（审定"帧面问题"系信息科技）、integrity（"完整性"系档案学）、matter（"物质"系化学工程）、moral law（"道德律"系教育学）、quality（"质量"系农学）、transcendental（"超越的"系代数几何）、universal（"通用的"系航海）、the One（"一"系中华术语工程——普罗提诺传统仍通行"太一"，记分歧）。
  - **学科语境正确的分歧 2 条主形保留、审定异译记入亦作**：intuition（审定"直觉"vs 康德权威译本"直观"）、mind（审定"心智"vs 心灵哲学通行"心灵"）。
* 工具沉淀：tl_crawler.mjs 断点续爬爬虫（JSONL 增量、幂等去重）；scan/locate 口径统一（等长占位）。

## 2026-11-05 深读滚动续八

* 深读累计 **35 条全 pass**（+boethius-dacia 中段、buddhism-huayan 中段、boethius 前段、boolalg-math、bradley、brouwer 年表、buddha、binarium、bauer、basing-epistemic、african-sage、africana、akan-person、al-farabi-psych、al-khunaji 中段、albalag 中段——B 批主体完成，A/B 两批深读实证覆盖过半）。
* 术语在线复核轮完成：tl_crawler.mjs 批量爬虫 75 词 0 error；裁定 36✓一致/8 跨学科保留/2 分歧记亦作（intuition 直觉、mind 心智）；核心根词传统译法获审定库佐证。
* 体例归一：倒装括注 64 处+署名行 6 作者登记+5 行汉化；标题截断 16 条+akan-person 题名主体丢失型；aesthetics-existentialist 英文题名补全。
* ADR-0019 渲染域清零：内侧空格 398→0（栈解析扫描器双模入库）。
* B 批实证结论：佛学（abhidharma/buddha/buddhism-huayan 术语一致）、中世纪（binarium/boethius-dacia）、分析传统（basing-epistemic/boolalg-math/bradley）译名体系全部规范；唯残余为 intensional 类型论 4 行（重译域）。

## 2026-11-05 深读滚动续九（B 批收口）

* 深读累计 **36 条全 pass**（B 批收口：butler-moral 收尾——B 批全部完成：basing-epistemic/bauer/bayle(f-k 完成跳过)/binarium/boethius-dacia/boethius/boolalg-math/bradley/brouwer/buddha/buddhism-huayan/butler-moral 全覆盖）。
* 门禁 7/7 全绿。下一接力：C 批 26 条（causation-medieval 起，certainty/consciousness-17th/critical-thinking 等已由 f-k 完成部分收口，深读仍按清单滚动）。

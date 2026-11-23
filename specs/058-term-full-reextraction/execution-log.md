# specs/058 执行记录

> 一段一节，按时间倒序追加。行内只记事实与凭证，不记进度叙事。

## 2026-11-22 会话（specs/058 启动）

* 开工核对：`git log` 基点 1d4767584；`git fetch` 后 origin/main 与本地一致（0 落后 0 领先）。工作区含其他会话在途改动 121 件（baseline patches、specs/001/053、tasks/term-pool.json 等），本规格不触碰。
* 误触发说明：本会话早先以 `--help` 调 `tools/term_harvest.py`（该工具无 --help），实际执行了一次全库增量收割：池 +103 候选、来源/频次随新语料漂移，状态零变更（与 HEAD 逐条比对，published/held/rejected 全部保持）。该产物保留（与全库重提目标一致），未回滚。
* 联网调研：见 `results/research-evidence-2026-11-22.md`。通道事实：DDG/Brave/Mojeek/Bing/百度均被反爬拦截；维基 API 与 OpenAlex/Crossref API 经代理 192.168.5.4:7890 可用；SEP 官网 `/translations*` 均 404，未找到官方翻译项目页面，不作为依据引用。
* 立项：`spec.md`（方向、口径、方法、验收）＋调研凭证。
* 提取器：`bin/reextract.py`（新增规格内高精度分型提取器，复用 `tools/term_harvest` 守卫常量，不另造判定）。
* 首轮全量（约 13:40）：2,998,178 键，保留 224,813，短语低频尾 2,774,365 不入总表。抽查发现三类缺陷：斜体噪声（et al/Figure/priori 残片）、机构与题名误判人名（Oxford University Press/Vienna Circle/Anomalous Monism）、合并后展示形取错类型。
* 修正：① NOISE_TERM 黑名单 26 词；② 人名路线 ORG_WORDS／DEMONYM／NONPERSON_TAIL 三重过滤＋尾词修剪；③ 展示形按类型优先级更新（person>work>term>sentence>foreign>topic>script）；④ 句级引语路线独立清洗（clean_sentence，2–300 字符，拒收标记与编号残片）；⑤ 产物收缩：原始档落 `script/tmp/candidates-full.json`（本地），入库档 `results/candidates.json.gz`（gzip 压缩，防 64MB JSON 进库）。
* 二轮全量（后台）：修正后重跑，产出 `results/az/A–Z/#.tsv` ＋ `results/summary.md` ＋ gz 索引。最终计数：语料 2418 篇，原始键 3,011,396，保留 260,526，低频短语尾 2,774,918 不入总表；类型：phrase 97,935／term 69,824／sentence 45,970／person 21,986／foreign 15,239／work 4,701／topic 3,113／cjk 1,256／arabic 468／greek 99。
* 状态刷新后：已登记 5,340／池内 54,402（new）＋ 2,162（其余裁定）／本轮新增 198,622（主要是句级长词条与池外低频项）。
* 总表格式改 TSV：Markdown 单字母文件超过 ADR-0004 的 1000 行/100 KB 阈值，`check_doc_size` 判红；改为每字母一份 TSV（生成物，数据表语义）＋ `az/README.md` 索引，复跑门禁转绿。
* 首批落册（batch1）：从评审表人工圈定 140 条高置信术语，经审定库 JWT 直连查证（112 条实查，111 ok／1 empty／28 已有凭证跳过）；人工逐条定译后，剔除合写键重复 3 条，实登记 102 条（22 条依据为审定名词库命中，80 条为教科书级标准术语 A 档直裁并注明审定库未采原因）。`term_flow` 干跑 102／0 跳过，实写后 `registry_azsort --apply` 守恒（术语表 7,103 行），`check_terms` 硬错误 0，`check_all` 17 项全绿。
* 产物：`tasks/manifests/2026-11-22-058-batch1.json`（裁定清单）、`results/curated-translations.tsv`（人工译法）、`results/rowspec-batch1.json`（机器清单）、`results/register-queue-{terms,persons,works}.json`（后续批次队列）。
* 开放项：
  1. 人名 21,986 条、著作 4,701 条只入总表，未落册；`register-queue-persons.json`／`register-queue-works.json` 已生成，需逐条核籍属/生卒与中译本，works 队列当前混入术语（feminist ethics／informal logic 类），下批须先分型。
  2. 本轮新增 198,622 条中，句级长词条 45,970 条多为引文，不属登记对象；其余按 T1/T2 逐批裁定。
  3. `candidates.json.gz`（8 MB，机器索引）未入库，保留在 `results/` 本地；全量 TSV 已入库。

## 2026-11-22 续：术语在线优先（用户裁定）

* 口径变更：登记一律先查审定名词库（allSearch），命中学科对口即采审定译名；查无或仅他义命中才走 A 档直裁，并写明原因。`termonline-standard` 实测为模糊检索（多词查询返回电力标准等无关命中），降为参考，不作优先通道。
* 首批依据复核：对 102 条逐条按“英文形一致或单复数变体＋学科对口”重扫凭证，14 条译名一致的命中升级依据为审定名词库（decision theory、moral beliefs、mental representations、field theory、artificial intelligence、cognitive processes、modal operators、moral values、inductive logic、machine learning、social structures、scientific progress、political economy、evolutionary biology），译名与日期不动。
* 首批未改采的审定异形命中及理由：perceptual experience 审定作“感性经验”（马克思主义语境，与知觉现象学非同概念）、moral agents 审定作“道德行为者”（语料通行“道德行动者”20 篇 vs 1 篇）、legal rights 审定作“法权”（马克思政治经济学义）、empirical research 审定作“经验性研究”（语料“经验研究”27 篇）、religious experience 审定作“宗教体验”（语料“宗教经验”10 篇）。
* 第二批：人工圈定 61 条，与总表求交得 59 条；全部先查审定库（48 条实查 ok、10 条已有凭证跳过）。按术语在线优先生成清单：5 条采审定译名（moral theories、number theory、empirical content、moral principle、logically equivalent→逻辑等值），54 条审定无对口命中后 A 档直裁。两条审定异形命中判定他义未采：physical theories→身体理论（自然辩证法·理论方法，身体义）、moral concepts→道德观念（医学伦理学，观念≠概念）。
* 落册：`term_flow` 干跑 59/0，实写 59；`registry_azsort --apply` 术语表 7161 行守恒；`check_terms` 硬错误 0。
* 当日累计：术语表新增 161 行（首批 102＋第二批 59），其中审定名词库依据 19 行。
* 第三批：人工圈定 52 条，全部先查审定库（44 实查 ok、8 已有凭证）。7 条采审定译名（译名与人工一致，含 Newtonian mechanics、ontological dependence、formal semantics 等），45 条审定无对口命中后 A 档直裁；无改采冲突。
* 著作名批次：7 部（Philosophical Investigations、Theory of Justice、Treatise of Human Nature、Principles of Philosophy、Politics、Laws、Summa theologiae），先查审定库——全部命中他义（公正／礼貌／水法规／外轮山等），判无对口条目；按 rules/03 §154 转权威译本档位登记：《哲学研究》《正义论》《人性论》《哲学原理》《政治学》《法律篇》《神学大全》。
* 落册：第三批 52＋著作 7，`term_flow` 干跑零跳过、实写 59；`registry_azsort` 术语表 7221 行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表新增 220 行（102＋59＋52＋7），审定名词库依据 40 行。
* 著作名第二批：26 部经典（Phenomenology of Spirit、Groundwork、City of God、Science of Logic、Word and Object、Languages of Art 等）。先逐部查审定库（26 部全部有凭证，命中均为他义：正商品／白皮病／字／艺术学科／冥想／下降／感觉 等），判无对口条目；按权威译本档位登记 26 行（去向见 `curated-works2.tsv` 的中译说明）。
* 人名队列诊断：修复人名合写键别名（“姓, 名 / 名 姓”双向、J. S. 缩写、van/von/della/ibn 粒子尾名），此前队列中的 Descartes、Husserl、Heidegger、Nietzsche、Mill、Kripke、Lewis、Marx 等经典人物实为已登记变体，不再重复入队。剩余真缺项以现代学者为主（Van Cleve、Della Rocca、Dutilh Novaes、Van Parijs、Van Gulick 等），按 ADR-0022 需逐条核籍属/生卒与通行汉名，留作专批。
* 落册：著作第二批 26 行；`registry_azsort` 术语表 7246 行守恒；`check_terms` 硬错误 0。
* 当日累计：术语表新增 246 行（102＋59＋52＋7＋26），审定名词库依据 40 行。
* 人名专批：合写键别名修正后再筛，确认真缺项 13 人：Isaiah Berlin、Simon Blackburn、Christine Korsgaard、Galen Strawson、Jonathan Dancy、Miranda Fricker、Joel Feinberg、Philippe Van Parijs、James Van Cleve、Michael Della Rocca、Catarina Dutilh Novaes、Ruth Barcan Marcus、Patrick Suppes。
* 取证：逐一查 Wikidata（经代理，限流退避；凭证 `results/people-wikidata-2026-11-22.tsv`），取 QID／生卒／国籍；Van Cleve、Della Rocca 无生卒数据，按“生卒未详”留空；Miranda Fricker 与已登记的 Elizabeth Fricker 为异人，分行登记。
* 落册：`term_flow` 干跑 13/0，实写 13；人名表 4558 行守恒；`check_terms` 硬错误 0。总表的状态判定同步支持人名合写键别名（`isaiah berlin` 等已标“已登记（人名表）”）。
* 当日累计：术语表 246 行；人名表 13 行。
* 人名第二批：再筛得 15 人：Tim van Gelder、Michiel van Lambalgen、Gideon Rosen、Stephen Darwall、Huw Price、Tommie Shelby、Jon Elster、Mark Schroeder、Brian Barry、Michael Tye、María Lugones、Russ Shafer-Landau、Paul Boghossian、Susan Wolf、Cecilia Martini Bonadeo。
* Anne Conway 在别名检查中被识别为已登记（“Conway, Lady Anne / 安妮·康威”），剔除；据此给人名别名加敬称剥离（lady/sir/saint/pope 等），防同类重收。
* 取证：Wikidata 逐人查（限流退避；凭证 `results/people-wikidata-2026-11-22-b2.tsv`）。Tim van Gelder 无生卒数据，留“—”；Mark Schroeder 首检命中篮球运动员，改查 Q93387536（1977–）。
* 落册：`term_flow` 干跑 15/0，实写 15；人名表 4573 数据行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表 246 行；人名表 28 行（13＋15）。
* 人名第三批：10 人：Julia Kristeva、Ludwig von Mises、Ernst Haeckel、公孙龙（Gongsun Long）、Ramon Llull、Ernst Mally、Philipp Frank、Patricia Hill Collins、Douglas Den Uyl、Stephen Davies。
* 取证：Wikidata 逐人查（限流退避；凭证 `results/people-wikidata-2026-11-22-b3.tsv`）。Stephen Davies 首检命中英国法官，改查 Q7609025（新西兰美学家，1950–）；公孙龙生卒取 Wikidata 前325／前250 约数，记“约前325–前250”。
* 落册：`term_flow` 干跑 10/0，实写 10；人名表 4583 数据行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表 246 行；人名表 38 行（13＋15＋10）。
* 著作名第三批：7 部：Port Royal Logic、Outlines of Pyrrhonism、Considerations on Representative Government、Lectures on Ethics、Book of Changes、Enquiry concerning Human Understanding、Thoughts Concerning Education。先查审定库（命中“图书／讲师／理解／教育思想”等他义），转权威译本登记：《波尔·罗亚尔逻辑》《皮浪主义纲要》《代议制政府》《伦理学讲座》《易经》《人类理解研究》《教育漫话》。
* 落册：`term_flow` 干跑 7/0，实写 7；`registry_azsort` 术语表 7254 行守恒；`check_terms` 硬错误 0。
* 当日累计：术语表 253 行（246＋7）；人名表 38 行。
* 人名第四批：14 人：Jean van Heijenoort、Robert Van Gulick、Lewis Carroll、James Clerk Maxwell、Quentin Skinner、David Enoch、Patricia Churchland、Larry Laudan、Jonardon Ganeri、George Bealer、H. L. A. Hart、Robin Le Poidevin、Felipe De Brigard、Mark van Roojen。
* 取证：Wikidata 逐人查（限流退避；凭证 `results/people-wikidata-2026-11-22-b4.tsv`）。Felipe De Brigard 无生卒数据，留“—”；Lewis Carroll 为作家兼逻辑学家（与已登记的 Noël Carroll 异人）；Patricia Churchland 与已登记的 Paul Churchland 异人分行。
* 落册：`term_flow` 干跑 14/0，实写 14；人名表 4597 数据行守恒；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 当日累计：术语表 253 行；人名表 52 行（13＋15＋10＋14）。

## 2026-11-23：人名表存量缺口回填

* 背景：specs/013 缺籍属/生卒告警 781 条（`specs/013-person-attribution/results/person-missing.txt`）。逐条筛名家可确证项。
* 回填 5 行：Aëtius（古希腊，约1–2世纪活动期，Q794615）、A.R. Anderson（美国，1925–1973，Q3268033）、David Lewis（美国，1941–2001，Q384522）、R. P. Wolff（美国，1933–2025，Q739540）、Timothy Williamson（英国，1955–，Q984380）。依据列追加“籍属/生卒联网查证：Wikidata Qxxx（2026-11-23 查，凭证 …）”，裁定日期不动。
* 弃用并留痕：Jon Williamson 的 Wikidata 条目 Q61951951 生卒为占位值 1900、职业仅 researcher，不可信；Paul Hoffman、Emma von Hartmann 查无条目。
* 证据：`results/people-wikidata-2026-11-23-backfill.tsv`。`registry_azsort` 守恒 4597；`check_terms` 硬错误 0。
* 门禁环境说明：本轮 `check_all` 本地红两项（单体文件大小、管线单元测试），根因均为 specs/057 会话未跟踪的新文件 s3u-audit.md（3343 行超限），不在本规格提交范围；已提交树不受影响，CI 为最终裁判。
* 当日累计：人名表存量回填 5 行（含 4 行补齐籍属/生卒、全部 5 行补凭证）。

## 2026-11-23：存量缺口自动回填（首批 200 条）

* 工具：`bin/backfill_auto.py`——逐条查 Wikidata，唯一学术候选且国籍/生卒可得者回填；多候选/无候选/数据全缺留痕不写。国籍优先 P27 映射，缺则按描述民族形容词回退（限定两条）；生卒取 P569/P570。
* 干跑暴露三类噪声并加守卫：① Wikidata 占位年 1900（Batterman、Brock 类）不给日期；② 生卒倒序（Epiphanius 600–501）不给；③ 同年占位（Albalag 1300–1300）不写。
* 人工排除 7 条撞名/存疑：Charles Mills（命中 18 世纪英国史家）、Audrey、Batterman, Robert、Brock, Gillian、Epiphanius、della Valle, Paolo、Balog, Katalin（首检为 1935–2005 匈牙利作家，存疑）。
* 实写 22 行（Abizadeh、Aldrich、Apollonius Cronus、Aristides、Axiothea、Barnes、Başkent、Boxer、Brady、Bridgeman、Buddhaghosa、Carugo、Chaerephon、Cintula、Costelloe、Cratylus、Dal Lago、De Giacomo、Della Rocca、Epimenides、Falk、Finsen）；其中 Buddhaghosa、Cratylus 两行人工把世纪改写为“约5世纪／约前5世纪（活动期）”，防止把世纪区间当生卒。
* 证据：`results/backfill-auto-2026-11-23.tsv`（227＋201 行，含两次运行全记录与排除理由）。
* `registry_azsort` 守恒 4597；`check_terms` 硬错误 0；`check_all` 17 项全绿。
* 事后更正（2026-11-23）：22 行依据列原引用 `people-wikidata-2026-11-23-auto.tsv`（不存在的文件名），实际凭证为 `backfill-auto-2026-11-23.tsv`；已批量改名（仅凭证文件名，译法/日期不动），脚本常量同步修正。`check_terms` 复跑硬错误 0。

## 2026-11-23：存量缺口自动回填（第二批 200–400）

* 工具：`bin/backfill_auto.py --start 200 --limit 200` 干跑 200 条，得 19 条“OK”（代理用 `127.0.0.1:7890`，192.168.5.4:7890 TLS 握手失败已弃），逐条核对 SEP 语境后仅 5 条身份确证：Gale, George（科学哲学家，Q133521156，补 1943–）、Gopal Sreenivasan（Q108581195，加拿大）、Hippobotus（Q2614752，希腊）、Kolodny, Niko（Q16403824，美国）、Lorki, Joshua（Q462009，西班牙／犹太改宗者，活动期 1400–1419）。
* 排除 14 条撞名/身份不符：Gerbrandy（描述计算机科学家、籍属记意大利）、Grant, Robert（美国法学家）、Green, Adam（歌手）、Hanson, William（土木工程师）、Hill, Thomas（作家）、Hippo（法国文学批评家）、Homer（美国物理学家，1942–2018）、Howard（单名物理学家）、Hyland, Martin（数学家且无生卒）、Iris（法律数据库）、John Pollock（英国史家）、Jonah（作家）、Klein, Peter（德国作家）、Ladner, Richard E.（生年 2000 为占位）。全部写入 EXCLUDE 并在证据 TSV 记理由。
* 定点写入脚本 `bin/backfill_batch2_manual.py`（只写上述 5 行，依据列追加 Wikidata 凭证）。
* `registry_azsort` 守恒 4597 行；`check_terms` 硬错误 0（人名缺项告警 781→775）；`check_all` 17 项全绿。

## 2026-11-23：著作名第五批（12 部）

* 选目来自全量总表 work 型高频未登记项，先经包含式查重排除已登记书名与概念行误拦：把查重脚本的包含式命中限定为「译法以《 开头的书名行」，并禁止连字符内切词（修正 Political Treatise 误撞 Theological-Political Treatise）。
* 逐部查审定库 allSearch（JWT 直连，12 部全有凭证）：命中均为他义——冥想、实践理性（概念非书名）、博物学传统、礼貌/论著、逻辑程序设计语言、期望寿命、可检验性（概念）、螺旋CT、穹天说、几何[学]、概率逻辑，判无对口条目。
* 转权威译本档登记 12 部：《第一哲学沉思集》《实践理性批判》《宇宙发展史概论》（全增嘏译）《政治论》（斯宾诺莎文集第2卷）《语言的逻辑句法》《普罗提诺传》《可检验性与意义》《黑皮肤，白面具》（张香筠译）《逻辑哲学论》《谈谈方法》（王太庆译）《几何基础》（江泽涵、朱鼎勋译）《概率的逻辑基础》。
* 译名联网核证（微信公号检索，2026-11-23）：谈谈方法（商务，王太庆）、宇宙发展史概论（全增嘏）、斯宾诺莎文集第2卷政治论、语言的逻辑句法（商务分析哲学名著译丛）、黑皮肤白面具（三联，张香筠）、几何基础（北大社，江泽涵/朱鼎勋）、普罗提诺生平（波菲利）。
* 落册：`term_flow` 干跑 12/0，实写 12；`registry_azsort` 术语表 7254→7266 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch9-works.json`。

## 2026-11-23：存量缺口自动回填（第三批 400–600）

* 干跑 200 条得 21 条“OK”，复核后实写 11 条、排除 10 条。
* 实写：Melissus（约前5世纪活动期）、Menedemus of Pyrrha（约前350–）、Metrodorus of Chios（约前4世纪活动期）、Michael Smith（澳大利亚，1954–，Q6828096，换条目）、Moltmann, Friederike（德国／法国）、Omori, Hitoshi（日本）、Paroush, Jacob（以色列，生年 2000 占位不写）、Phaedo of Elis（约前4世纪活动期）、Retoré, Christian（1964–）、Robert Adams（美国，1937–2024，Q5254926，换条目）、Roush, Sherrilyn（美国）。
* 换条目两例：Michael Smith 首检命中英国记者 Q6834471，改查 Q6828096（道德哲学家 Michael A. Smith）；Robert Adams 首检命中科幻小说家 Q7341356，改查 Q5254926（Robert Merrihew Adams）。
* 排除 10 条：MacLeod, Colin（籍属与多伦多大学心理学家不符）、McKay, Thomas（生物工程师）、Meskin, Aaron（生年与已知美学家不符）、Moran, Thomas（作家）、Murphy, Peter（作家兼法官）、Nishimura（仅姓氏）、Pease, Adam（计算机科学家）、Perry, John（罗德学者）、Radcliff（军人）、Richmond, Marsha（生年 1901 与当代科学史家不符）。全部入 EXCLUDE 并记证据。
* 纪年口径：描述只给世纪者记“约前N世纪（活动期）”，不冒充生卒；Wikidata 占位生年（2000）不写。
* 证据：`results/backfill-auto-2026-11-23.tsv` 追加 21 行。`registry_azsort` 守恒 4597；`check_terms` 硬错误 0，缺项告警 781→769。

## 2026-11-23：术语第四批（45 条）

* 选料改法：队列前列被泛搭配占据（health care、qua、let alone 等），改按「type=term＋术语后缀词表（theory/paradox/logic/principle…）＋未登记」直筛，得 574 条技术性候选。
* 逐条查审定库（50 条入队，全部有凭证）；命中对口者 11 条采审定形：自然主义谬误、会话含义（审定“会话隐含”记亦作）、商谈伦理、混沌理论、中文屋论证、合作原则、不确定性原理、恶性循环原则、行为功利主义（审定“行动效用论”记亦作）、丘奇论题、马赫原理；语境原理一条按审定形直采（语料无通行译法）。
* 语料计数佐证（篇目数）：子结构逻辑 16 vs 亚结构逻辑 1、会话含义 3 vs 会话隐含 1、行为功利主义 11 vs 行动效用论 5；中文屋论证 16、不确定性原理 13、弗雷格定理 8、斯科伦悖论 12、辛普森悖论 12。
* 四条跳过：substructural logics（与已登记 substructural logic／子结构逻辑 同概念复数形）、analogical arguments（同 analogical argument）、intellectual property rights（与 intellectual property／知识产权 同概念）、backwards induction（同 backward induction）；审定形“亚结构逻辑”与登记形“子结构逻辑”的差异留作 open item，待 rules/03 定性与裁决。
* 其余 34 条 A 档直裁（审定库仅命中泛词或他义）。
* 落册：`term_flow` 干跑 45/0，实写 45；`registry_azsort` 术语表 7266→7311 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch10-terms.json`。

## 2026-11-23：自动回填的偏移缺陷与修法

* 现象：第三批落册后再跑 `--start 600`，输出的 20 条与第三批复核名单重合。根因：`person-missing.txt` 由 `check_terms` 每次重生成（781→769 条），已补项退出后行序整体前移，用行号 `--start` 定位不等于“未处理者”。
* 修法：`backfill_auto.py` 增 `done_keys()`——读证据 TSV 第一列去重，`todo` 只取证据未记键，再按 `--start/--limit` 切片；重复查询归零，偏移不再依赖行序。
* 该轮干跑仅产生记录未写库（无 `--apply`），已在证据 TSV 留痕；后续批次按新逻辑重跑。

## 2026-11-23：存量缺口自动回填（第五批·剩余未查项）

* 按新去重逻辑（证据键）重跑，处理 181 条，得 30 条“OK”，复核后实写 10 条、排除 18 条、体例误判撤回 2 条。
* 实写：Shakespeare（英国，1564–1616）、Stephen Schiffer（美国，1940–）、Swartz, Norman（1939–）、Tartaglia（意大利，1499–1557）、Theocritus（约前3世纪活动期）、von Fintel, Kai（德国）、Weber, Zach（新西兰）、Wetzel, Linda（美国，1951–）、Wheeler, Michael（英国，1960–）、Schubert, Lenhart（美国）。
* 同名异人两例关键拦截：Sextus 行指莱布尼茨《神义论》里的塞克斯图斯·塔克文（恩披里柯已另行登记）、Zosimus 行指炼金术作家佐西摩斯而非拜占庭史家，均排除。
* 排除 18 条：Selig（诗人）、Shanahan（占位生年）、Simmons（生物力学家）、Skow／Uniacke（无生卒）、Solomon／Ubaldo／Wagener／Yin Xian（单名或描述过弱）、Squatrito（非哲学家）、Stanhope（代际不符）、Stephens（馆员）、Tian Pian（占位生年，行内已有凭证）、Turner（作曲家）、Weckert（占位生年）、Weinrich（身份存疑）。
* 方法事故与撤回：把 Van Cleve「美国／哲学」、van Gelder「澳大利亚／认知科学」误判为籍属污染并改写，核对全表发现「国籍／领域」是通行体例（1,041 行如此），已恢复原值；教训＝改存量字段前先量体例基线。
* 证据：`results/backfill-auto-2026-11-23.tsv` 追加 30 行。`registry_azsort` 守恒 4597；`check_terms` 硬错误 0，缺项告警 769→763。

## 2026-11-23：术语第五批（43 条）

* 自后缀筛结果第 61–120 位取 43 条，全部先查审定库（31 条实查 ok、12 条已有凭证）。
* 审定对口者 10 条：普通语义学、数学直觉、临摹性原则（亦作“拷贝原则”）、无类理论、约束理论、良序原则、玻尔对应原理（审定作“对应原理”）、实体实在论、批判理性主义、有效场理论（亦作“有效场论”）。
* 其余 33 条 A 档直裁；佛教概念 storehouse consciousness 按传统译名取“阿赖耶识（藏识）”（语料两形各 5 篇）。
* 译文语料计数：伯特兰悖论 2 篇（贝特朗悖论 0）、可知性悖论 11 篇、良序定理 3 篇（良序原则 0，哲学数学两义分列取原则）。
* 落册：`term_flow` 干跑 43/0，实写 43；`registry_azsort` 术语表 7311→7354 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch11-terms.json`。

## 2026-11-23：人名第五批（新增 5 人）

* 从重生成的人名队列里别名感知核查后确认真缺项 5 人：Iris Marion Young、Saunders Mac Lane、Frans van Eemeren、Francisco Miró Quesada、Abraham ibn Daud（Albertus Magnus＝已登记 Albert the Great、C. S. Peirce／P. F. Strawson／Anne Conway／Fichte 等均为别名变体）。
* 取证：Wikidata 逐人查（凭证 `results/people-wikidata-2026-11-23-b5.tsv`）。汉名按通行音译：艾丽斯·马里恩·扬、桑德斯·麦克莱恩、弗兰斯·范·埃默伦、弗朗西斯科·米罗·克萨达、亚伯拉罕·伊本·达乌德；籍属/生卒随行登记（美国 1949–2006／美国 1909–2005／荷兰 1946–／秘鲁 1918–2019／西班牙（安达卢斯）约1110–约1180）。
* 落册：`term_flow` 干跑 5/0，实写 5；`registry_azsort` 人名表 4597→4602 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch12-people.json`。

## 2026-11-23：术语第六批（42 条）＋人名第六批（3 人）＋差异裁定留证

* 术语第六批自后缀筛第 121–190 位取 42 条（跳过 foundational metaphysics、brute necessity 等义项不清者，以及 repository consciousness——与已登阿赖耶识同概念）。全部查审定库（33 实查、9 已有凭证），仅 2 条对口：信号检测理论、范畴论；其余 A 档直裁（切消定理、苏什科论题、贝里悖论、下行因果、个例-个例还原、移动聚光灯理论等）。
* 落册：`term_flow` 干跑 42/0，实写 42；`registry_azsort` 术语表 7354→7396 守恒；`check_terms` 硬错误 0。
* 人名第六批 3 人（逐人 Wikidata 取证，凭证 `results/people-wikidata-2026-11-23-b6.tsv`）：Andrew von Hirsch（安德烈亚斯·冯·赫希，英国（生于瑞士苏黎世），1934–2026，Q4759036）、Evelyn Fox Keller（伊夫林·福克斯·凯勒，美国，1936–2023，Q239131）、Leon van der Torre（无通行汉名保留原文，荷兰，1968–，Q23038082）。冯·赫希汉名经公众号文章核证，两种汉形并记（亦作“安德鲁·冯·赫希”）。
* 落册：`term_flow` 干跑 3/0，实写 3；`registry_azsort` 人名表 4602→4605 守恒；`check_terms` 硬错误 0。
* 差异裁定：审定形与登记形不一致的 6 例（substructural logic、conversational implicature、act utilitarianism、Copy Principle、Bohr’s correspondence principle、effective field theory）逐条定性并留证 `results/adjudication-2026-11-23-termonline-divergences.md`——均不构成 D1–D5，属“审定形与学界通行形并存”，主形取语料通行者、另一形以“亦作”入译法列，不另起行。

## 2026-11-23：著作名第六批（29 部）

* 自著作队列按修正后查重筛出 30 部真书名，逐部查审定库（16 部已有凭证、14 部新查），命中全为他义（唯象学、无穷、历史与社会课、论著、乌托邦、元素周期律、德目、回忆说、哲学王、寿命、非相干性、上议院、曙暮光、防御者、预测、政治经济学、必然性、情感分析、教育民主、恐惧、经验、向导、算术、四月提纲、全员参与、外伤史 等），判无对口条目。
* 译名联网核证（公众号检索）：《哲学家的矛盾》（安萨里）、《和平的保卫者》（马西利乌斯，商务）、《唯物主义史》（朗格，郭大力与李石岑合译）、《论人》（笛卡尔）、《法律要义》（霍布斯）、《普罗克洛生平》（马里努斯）。
* 弃收 1 部：De Genesi ad litteram（奥古斯丁）无通行汉名，学界多保留拉丁原名，按“查无 → 不臆造”暂不入册。
* 转权威译本登记 29 部：《知觉现象学》《总体与无限》《历史与阶级意识》《论人》《无政府、国家与乌托邦》《过程与实在》《法律要义》《德性论》《法权论》《论人类不平等的起源和基础》《差异与重复》《名哲言行录》《普罗克洛生平》《哲学家的矛盾》《商君书》《偶像的黄昏》《和平的保卫者》《经验与预测》《政治经济学原理》《命名与必然性》《道德情操论》《民主主义与教育》《恐惧与颤栗》《经验与自然》《迷途指津》《算术基础》《关于费尔巴哈的提纲》《万民法》《唯物主义史》。
* 落册：`term_flow` 干跑 29/0，实写 29；`registry_azsort` 术语表 7396→7425 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch14-works.json`。

## 2026-11-23：门禁环境说明（著作第六批收尾）

* 本地 `check_all` 16/17 绿，唯一红项「管线单元测试」失败用例 `test_abbrev_bare_name_still_dropped`；根因是并行会话（specs/053）对 `tools/yuanwen.py` 的在途未提交改动（工作区 M），不在本规格提交范围。
* 用 `git show HEAD:tools/yuanwen.py` 载入已提交版本复算：`build_cite_keys(['Descartes, René','Leibniz, G. W.'])` 返回 `[]`，与用例期望一致——已提交树不受影响，本规格不触碰该文件，推送后以 CI 为最终裁判。

## 2026-11-23：术语第七批（55 条）

* 自后缀筛第 191–260 位取 55 条，全部查审定库（38 实查、17 已有凭证），对口者 7 条：内部效度、溯祖理论、粒子数算符、计算树逻辑、归纳问题、代入量词、物理丘奇-图灵论题（审定只收基形“丘奇-图灵论题”，专名作主形并注）。
* 其余 48 条 A 档直裁：先验还原、定域实在论、非经典逻辑、混合表达主义、轻易知识、分子命题、序数逻辑、双重继承理论、后门准则、实用真理等。
* 落册：`term_flow` 干跑 55/0，实写 55；`registry_azsort` 术语表 7425→7480 守恒；`check_terms` 硬错误 0。清单 `tasks/manifests/2026-11-23-058-batch15-terms.json`。

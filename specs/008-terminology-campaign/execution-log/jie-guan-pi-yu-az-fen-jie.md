# 执行记录：术语战役 · 接管批与 A–Z 分节定型（2026-11-09）

TL-main-20261109 复核批与 TL-az-20261109 分节定型批。

## 2026-11-09 接管批（TL-main-20261109）：复核既有译名 + 同键异译合并 + 反向校对 + 依据链核验

**起点**：`check_terms` 硬错误 12（并行会话重复追加 10 行人名 + 2 行术语）、词汇表滞后 1（truth-maker）；术语在线匿名 `standardSearch` 实测可用（abduction/波义耳等返回 200）。

### 一、同键异译合并（19 组 → 0 组，主形按语料多数/SUMMARY 定名/审定口径）

| 键 | 合并为 | 判定依据 |
| ---- | ---- | ---- |
| abstractive cognition | 抽象认知（亦作“抽象认识”） | 语料 24 处/3 篇 vs 13 处/2 篇 |
| intuitive cognition | 直观认知（亦作“直观认识”） | 语料 47 处/4 篇 vs 20 处/7 篇 |
| divine ideas | 神圣理念（亦作“神圣观念”） | 神哲学通行；john-norris 用“观念”记涟漪待三校 |
| excommunication | 绝罚（亦作“开除教籍”） | 原行已含亦作，合并 marsilius-padua 出处 |
| positive law | 实在法（亦作“实定法”） | 语料 17 处/5 篇 vs 3 处/1 篇 |
| truth-maker | 真值制造者（亦作“真理制造者”） | 与 truthmaker theory 真值制造理论 同族；词汇表同步后滞后 0 |
| via moderna | 现代路线（亦作“近代之路”） | 两形各 1 篇，取字面直译 |
| imposition | 命名（词项施加；亦作“设定”） | 同一 impositio 概念两译，合并 |
| perfection | `perfection (Vollkommenheit)` 完善／`perfection (perfectio)` 完满性 | 沃尔夫—鲍姆嘉通 vs 笛卡尔—经院，**键加括注分义** |
| schêma | `schêma (Kant)` 图型（亦作“图式”） | 与英文 `schema` 行（GB 标准库 schema=图式）分列 |
| species | `species` 种／`species（经院认识论）` 种相 | telesio 行并入 crathorn 行（同义） |
| doxographical tradition / doxography | `doxographical tradition` 学说史传统 | 与 `doxography` 学说汇编 拆键 |
| ether; caloric | `ether` 以太／`caloric` 热质 | 合键拆分 |
| innate knowledge | 天赋知识 | 与 a priori knowledge 先天知识 分义（反校撤“先天知识”别形） |
| sophrosune | 节制（亦作“自制”“适度”） | 撤“明智”别形（与 phronesis 明智 撞车且语义不符） |

### 二、人名表同人异形合并（8 组）与同姓异人注记（3 处）

* 合并（主形按 SUMMARY 定名/语料/首登记）：`Mullā Ṣadrā`→穆拉·萨德拉（亦作“毛拉·萨德拉”）、`al-Nayrīzī`→奈里齐（亦作“纳里齐”）、`Boyle, Robert`→罗伯特·波义耳（亦作“玻意耳”，SUMMARY 定名）、`Eustachius a Sancto Paulo`→尤斯塔修斯（圣保罗的；亦作“欧斯塔基乌斯”）、`Heinrich Scholz`→海因里希·肖尔兹（亦作“肖尔茨”，SUMMARY 定名）、`Hintikka, Jaakko`→欣蒂卡（亦作 Hintikka，并修正年代列串位）、`Melissus`→麦里梭（亦作“墨利索斯”）、`Otto von Bismarck`→奥托·冯·俾斯麦（亦作“俾斯麦”）。
* 同姓异人注（不合并）：Bruce Bridgeman ↔ Percy Bridgman（均作“布里奇曼”）；Davidson, Maria ↔ Davidson, Donald（均作“戴维森”）；Robert Brandon（生物学哲学）↔ Robert Brandom（推论主义）——三者均为不同人，注记互指。

### 三、依据链核验（新工具，只报告）`script/evidence_audit3_20261109.py`

* 口径：只看凭证中「英文同词命中」，比对登记译法；四类异常 A 声称一致无有效命中 / B 声称一致译法不合 / C 声称查无却有异域同名 / D 凭证缺失。
* 结果：A=31、B=12、C=64、D=340、正常=564；清单 `results/evidence-anomalies-2026-11-09.tsv`。
* B/C 抽样均属既有裁定的跨域同名（aretê→刃脊、epoché→历元、connectionism→连接机制、mechanism→机构/机理 等），保留现译；D 多为键改名/浏览器通道凭证命名差异所致，留待对账批。
* 审计重跑：`term_audit` 5277 行 → 一致 261 / 不一致 104 / 查无 557 / 未查证 4355 / 维基 1（该 1 条为行内“已撤除维基引证”自述，误报）；104 条逐条复核无新真错，维持保留裁定。

### 四、并行会话数据事故拦截

* 并行合并脚本把 slug 写入「译法」列（7 行：Axiom of Choice、positive law、natural deduction、knowledge first、truth-maker、principle of bivalence、extension）→ `script/fix_slug_pollution_20261109.py` 修复（slug 移回「出处」、日期列复原），`check_terms` 滞后 2→0。
* 教训重申：合并脚本的列位映射必须小样验证；`cells[2]` 与 `cells[3]` 混淆是第二次出现。

### 五、术语在线查证（联网，>5s 节流，凭证入库）

* `--provider termonline-standard --force`：abstractive cognition、intuitive cognition、divine ideas、excommunication、imposition、perfection、positive law、schema、species、truth-maker、via moderna（ok 9 / empty 2）+ Boyle、Melissus、Bismarck、Mulla Sadra、Hintikka、Bridgman、Eustachius（全 empty）。
* 结论：GB 标准库对哲学词/人名基本查无（仅 schema=图式、species=种 有标准佐证），印证「标准库不作哲学否定证据」；审定库（termonline-all）需 token，本会话无 token，相关行依据维持既有凭证并如实标注。
* 门禁：`check_all` 7/7 全绿；`check_terms` 硬错误 0、滞后 0；原文缺 175、人名缺籍属/生卒 2352（生成物）。

## 2026-11-09 A–Z 分节定型与爬取程序化（TL-az-20261109）

### 一、两登记册 A–Z 分节（用户裁定：「只针对术语表、人名表」「各自单文件内 A–Z 分节」）

* 新工具 `tools/registry_azsort.py`：数据行按首字母分节重排（`## A`…`## Z` + 末节 `## #`），
  只重排行序、不改行内容；纪律=守恒门（数据行字节多重集相等，残余≠0 拒绝写回）、幂等
  （`<!-- az-sort:v1 -->` 标记，重跑逐字节相同）、原子写、默认要求工作区干净。
* 分节键：首列键剥离前置装饰符（《》、引号、括号、ʿ/ʾ）与变音符后的首个拉丁字母；
  希腊字母按转写首字母归档（ω→O、ε→E）；汉字/阿拉伯文/数字起首归 `#`。
* 结构副产物：人名表「登记格式说明」「待裁定」之后追加的 1189 行归位字母节；说明段文字原位保留；
  术语表 4 行历史表头/分隔行移除；术语表首次获得 H1 与体例说明。
* 首跑 3526+2802 行，周界 0；随后并行会话新增 57+43 行再跑一次，周界仍 0。提交 `2f3b394d`。
* 顺带解冲突：词汇表 `Paradox of Suspense` 补「亦作悬念悖论」（登记册正文形），`check_terms` 硬错误 0。
* 潜伏缺陷记录：术语表 `| term | — | 词项 | …` 一行首列撞 `HEADER_WORDS`，长期被解析器漏认
  （审计口径 3509 行，实际数据行 3510）；重排保留该行，但未改 `check_terms.is_data_row` 语义。

### 二、爬取程序化：`tools/tl_crawler.py`（用户裁定：「编写爬虫而不是模拟点击」）

* 分工：浏览器只承载登录态（persistent context + `state/tl-profile`），**请求全部由程序经
  `context.request` 发出**，无任何点击；`tl_browser_batch.py --ingest` 仍是唯一落凭证入口
  （批次 schema 不变）。
* 登录：`--login` 打开可见窗口人工登录一次（等待令牌最多 `--login-wait` 秒），profile 复用，
  之后 `--crawl` 可无头长跑；令牌每批从页面 localStorage 解密刷新。
* 节奏与容错：批内默认为 8s（硬约束 ≥5s）、批间 20s；连续 2 次降级 → 重新激活 + 退避 60s→300s，
  同词最多 3 试；降级绝不落盘为「查无」。
* 断点：`state/tl-crawl-state.json` 记 `next_offset`，`--start` 可覆盖。

### 三、限流与激活机制（两次校准，结论取代 2026-10-29 口径）

* 未激活时 `allSearch` 只回 3 库且全 0（降级）；`goto search?searchText=…` 让应用自己发一次检索后，
  同一令牌立刻 4 库齐全（408/106/18/31）。
* 首轮结论「瓶颈是激活、不是限流」**部分错误**：短时连发仍会降级。`--calibrate` 实测：
  6 秒间隔连发，**第 19 次起降级**（预算≈18 请求）；60 秒后单发恢复 ok。
* 整页激活代价高：一次 `goto` 搜索页本身触发应用十余个请求，等于吃掉大半预算。
  故稳态策略=常态不激活（`--no-warm`），仅降级后冷却 60 秒并激活一次。
* 稳态吞吐实测 2–3 词/分钟（12–20 秒间隔）；3068 项全量约需 18–20 小时，属长跑作业。
* 降级词一律不落凭证（error 状态），下轮 `--unverified` 自动重查——「宁可慢，不可假空」。

### 四、本批凭证（手工通道，offset 0–27）

* `Abhidharma` 真查无（4 库 0）；其余 26 项 ok，已 `--ingest` 落库（termonline-all）。
* 首次整批 8 词全降级（未激活）→ 全部作废未入库，符合「降级不落凭证」要求。

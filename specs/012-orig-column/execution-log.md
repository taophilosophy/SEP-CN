# 012 原文列 · 执行记录

计录原则：每批一段，写清**批次、条数、证据档位、剩余告警数**；证据不可得者单列「留队」。

## 2026-11-07 阶段 3B：逐词联网复核重做（提交 56d08558 / 8c869b12 / 5644c8eb / a8ddd565）

**方法（按同日裁定重做）**：每词一条检索，只采**来源页面显式给出的「罗马化 ↔ 原生文字」配对**——可用档位：Wikipedia 词头/译名表、Wiktionary 词条页头（如 `كَلَام • (kalām)`）、Tsadra Commons 词条表的「Devanagari Sanskrit Script / Devanagari」字段、wisdomlib **词典/词条页**（非其 `sanskrit/segments/` 转写器页，该页属机械转写，按裁定不采）。

| 批次 | 条数 | 源 | 说明 |
| ---- | ---- | ---- | ---- |
| 梵语一 | 17 行 | Wikipedia / Tsadra / wisdomlib | अनुमान·प्रत्यक्ष·संसार·स्वभाव·ईश्वर·मध्यमक·विज्ञान·योगाचार·चित्तमात्र·प्रमाण·अपोह·तथागतगर्भ·वैभाषिक·सौत्रान्तिक·प्रासङ्गिक·संधिनिर्मोचन·स्वातन्त्रिक |
| 梵语二 | 15 行 | 同上 | sphoṭa·apūrva·icchantika·cakravartin·abhidhamma·śāntarakṣita·nāgārjuna·candrakīrti·kumārajīva 等 |
| 梵语三 | 12 行 | 同上 | aṅgulimāla·mañjuśrī·dignāga·śrīharṣa·vimalakīrti·kumārila·tāranātha·śaṅkara·vipassanā 等 |
| 阿语一 | 5 行 | Wiktionary 阿语词条 | فلسفة·كلام·توحيد·شريعة·قياس |

**结果**：两表原文列现有**天城体 44 行、阿拉伯 5 行**；告警 190 → 142。

**未取到配对、留 `—` 待补（不得以映射补）**：`Śākyaśrībhadra`（en.wiki/Lotsawa House 均无天城体；wisdomlib concept 页亦无）。

**发现并修正的口径错误**：`kalām` 行原文列此前被填成罗马化 `kalām`（非原生文字），已改 `كلام`。**遗留工具缺口**：检查器不区分「原文＝罗马化自身」与「原文＝原生文字」，建议下批加告警（英文拉丁术语例外）。

**操作事故（已记录，未改写历史）**：本会话 `git commit --amend` 时 HEAD 已被并行会话推进，amend 误改了对方提交 `38cedecc`（j 批 jayaraasi p2）的信息为 012 文案；原信息可从 reflog/`git cat-file -p 38cedecc` 取回，因共享工作区脏（多会话未提交改动）放弃改写历史，特此留痕；该提交**树内容未受影响**。教训：共享工作区**禁用 amend**，提交前先 `git log --oneline -1` 确认 HEAD 是自己。

**会话副作用（同一并行会话机制）**：本会话未提交的 51 行映射批曾被对方 `git add -A` 式提交带走，故此后坚持**每批立即提交**。

## 2026-11-07 阶段 3A：希腊批（完成，提交 236cb76d）

**方法**：逐键联网检索（每键一条检索，取页面/词条显式给出的「转写 ↔ 希腊形」配对），39 行；单列见 map `state/orig_stage3_map.tsv`（不入库）。

## 2026-11-07 违规批次作废：梵语 IAST 映射批（51 行，已回退）

**用户裁定（同日）**：原文必须**逐词联网复核**，**禁止正推/逆推**（不得用 IAST/DIN 31635/Wylie 等映射表机械转换）。已写入 spec.md「裁定与假设」。

**处置**：以映射推演的 51 行（梵/巴利天城体 + 梵式人名）全部回退为 `—`（`script/_revert_orig_batch.py`，仅当第 2 列等于该批计划值才回退），告警 137 → 190；改逐词复核后重做。

**教训（工具层面，操作陷阱）**：

1. 并行会话可能在**其提交中带走本会话未提交的两登记册改动**（`git add -A` 式收口）——上一批 51 行就是这样进了 HEAD，导致 `git checkout -- <表>` 空跑；回退必须显式定位到「行 + 值」，不能靠 checkout。
2. 因此**每批回填后立即提交**，把提交粒度当作防串台边界。

## 2026-11-07 阶段 1：机械回填（完成，提交 6e5489de）

**方法**：`script/_fill_orig_stage1.py`（白名单制——2026-11-07 会话逐条人工复核 198 条 romanization 队列后编码）；写回幂等（只填「—」）。

* 修分类器换行分裂 bug（行界词对合并致 40 词漏填）；`Lüshi chunqiu`/`yì`/`hadé` 判 CJK 源词留阶段 2；韩式 MR 人名（ŏ/ŭ）与藏式 THL 人名单列。
* 检查器新增豁免 `ORIG_EDITORIAL_PAREN`：`competence（医疗与法律语境）`、`yielding（虚空）`＝英文术语+编者括注（democritus 虚空另立键 kenon），原文恒「—」。
* 回填 **211 行**（术语 139：拉丁/德/法原拼写 90+CJK 括注提取 21+西里尔 3+ω/ε 记号 3+括注原形 5；人名 72：正序 71+波兰人名 1）；头衔键 `Anne-Thésèse, Marquise de Lambert` 保留原形。
* 告警 544 → 333；check_all 7/7。

## 2026-11-07 阶段 2：语料取证（完成，提交 a4cd6000）

**方法**：`script/_fill_orig_stage2.py` 单遍大正则扫 `yuanwen/`（2428 文件）+中文词条，键 ±100 字符内共现原生文字 token 按语系过滤计票；`_fill_orig_stage2b.py` 定点探针补证；**每条映射人工核上下文后**经 `--apply` 写回。

* 回填 **113 行**（术语 82+人名 31）：中文典籍 22（道/氣/天/陰/陽/呂氏春秋/論語/孟子/墨子/莊子/老子/道德經/荀子/韓非子/易經/淮南子/史記/列子/管子/春秋/一心/義）+希腊 3（ἐπιστήμη/τέχνη/ἀταραξία，唯一镜像共现）+日本美学 50+韩佛 2（活句/死句、통불교）+日人名 15+韩人名 20（含谚文 백성욱）。
* 证据档位：镜像/词条共现（tier1）为主；**译法列括注**（如 物の哀れ/さびれる/無常/縁起/書院/見性）为登记册内部证据（tier1）；日本語同形词（武士道/型/甘味/国学者）记 tier3。
* 希腊键 ±400 放宽窗口仍无共现（镜像转写旁不带希腊字母）——余 34 条归阶段 3 外源。
* 留队（原生字形语料不可证，待阶段 3）：mono no aware 外的日韩余量 20（床の間/媚態/意地/切れ継ぎ/渋み/地味/派手/精舎/能/漢意/御国心/日本人論/大教宣布運動/鴨長明/谷崎潤一郎/西田幾多郎/韓元震/成渾/金一葉/眞興王）+ Sefer ha-Zohar + 希腊 34 + 梵/阿/藏全部。
* 告警 333 → 223；check_all 7/7。

## 2026-11-06 阶段 0：落表（完成）

**指令来源**：用户「术语表，人名表新增一列原文：如果术语非英语，必须同时增加原文。」；同日三项裁定（原生文字 / 键后第 2 列 / 先告警后分批）。

**结构变更**

* `yi-zhe-shuo-ming.md`：五列 → 六列，插入第 2 列「原文」，全行初始 `—`；数据行 1240 全部六列（`line.count('|')==7`）。
* `ren-ming-biao.md`：同上；数据行 1043 全部六列。
* 其余五列内容逐字节未改（迁移脚本按 `split('|')` 原位插列）。

**工具变更**（`tools/check_terms.py`）

* `parse_registry_full()`：六列标准解析（`term, orig, trans, first_seen, basis, date, lineno`），旧五/四列兼容（`orig=None`）；`>6 列` 记告警。
* `parse_registry()`：保留旧六元组签名，`term_audit.py` / `tl_browser_batch.py` 免改（复用解析）。
* 新增 `has_foreign_char` / `_key_variants` / `is_non_english` / `orig_missing` / `write_orig_missing`；`FOREIGN_WORDS` 小语种词表（拉丁惯用语/德/法/阿拉伯/梵巴/藏/日/朝/汉/俄）。
* 新告警「非英语术语缺原文」：**不计硬错误**；全库运行重写 `specs/008-terminology-campaign/results/orig-missing.txt`。

**回归**

| 检查 | 结果 |
| ---- | ---- |
| `check_terms.py`（全库） | 硬错误 0；告警 528（术语 354 + 人名 174） |
| `check_terms.py --docs l/logic-provability.md` | 通过，0 疑似缺译法 |
| `term_audit.py` | 正常出报告（2276 行：术语 1236 + 人名 1040） |
| `tl_browser_batch.py --emit` | 2357 项（2270 行）正常 |
| `check_all.py` | 7 项全绿 |

**队列分类**（528 条，按 `script/_fill_orig_stage1.py` 分类器）

| 类别 | 条数 | 阶段 |
| ---- | ---- | ---- |
| 罗马化待原生文字（拼音/罗马字/梵阿转写） | 198 | 1 选出可机械者，余 2/3 |
| 希腊语 | 37 | 2（语料 9260 字可证） |
| 印度-闪米特（梵/阿/波斯，含变音标记） | 70 | 3（语料仅 49+6 字，须外源） |
| 非拉丁人名 | 76 | 2（希腊/梵/谚文者）→3（阿/藏） |
| 其它非拉丁 | 2 | 2 |

**阶段 1 分类器已知误判（干跑发现，待修）**

* `dictum (Abelard)`：括注为人名消歧，原文应取主形 `dictum` → 已修为「括号首字母小写才取括注」。
* `Cheka / gulag / partinost`：西里尔源词，已内置映射（Чека / ГУЛАГ / партийность）。
* `yì`、`hadé`、`Lüshi chunqiu`：CJK 源词（义（義）/ 华丽 / 《吕氏春秋》），`FOREIGN_WORDS` 未覆盖 → 阶段 1 需 CJK 覆盖表排除或直接填。
* `naïve realism`、`Gödel’s theorem`、`Löwenheim-Skolem theorem`、`Müller-Lyer illusion`、`Łukasiewicz logic`、`Petőfi Circle`：含人名变音符的**英文术语/机构名**，填自身拼写即可消警（非原生文字问题）。

**语料可证性实测**（决定阶段 2/3 分流）

| 文字 | 字符数 | 文件数 |
| ---- | ---- | ---- |
| Greek | 9260 | 360 |
| Cyrillic | 998 | 20 |
| Hangul | 522 | 7 |
| Hebrew | 139 | 13 |
| Arabic | 49 | 3 |
| Devanagari | 6 | 1 |
| Tibetan | 0 | 0 |

**遗留**

1. `rules/03-terminology.md` 第 34 行「登记格式（两登记册统一，五列）」待改为六列并说明原文列（阶段 4 与条文开关同批落地，或提前单独改条文）。
2. 并行会话若按五列写表将致列错位——检查器有 `>6 列` 告警兜底，交接卡已列纪律。

## 2026-11-09 拉丁原拼写批（15 行，证据＝语料共现）

**方法**：`script/orig_latin_batch_20261109.py`——对「姓, 名」倒置的欧洲拉丁字母人名，构造自然序候选形式，在 `yuanwen/` 镜像与 A–Z 词条正文中检索**逐字共现**，命中方填；未命中留 `—`。

| 键 | 原文 | 证据（首三处） |
| ---- | ---- | ---- |
| Biard, Joël | Joël Biard | yuanwen/a/al-farabi-logic.md 等 |
| Bühler, Karl | Karl Bühler | yuanwen/f/feigl.md 等 |
| Delacroix, Eugène | Eugène Delacroix | yuanwen/m/mental-imagery.md |
| Hoernlé, Agnes Winifred | Agnes Winifred Hoernlé | yuanwen/l/langer.md; l/langer.md |
| Malraux, André | André Malraux | yuanwen/a/aesthetics-existentialist.md 等 |
| Möser, Justus | Justus Möser | yuanwen/a/august-rehberg.md |
| Müller, Adam | Adam Müller | yuanwen/a/august-rehberg.md; yuanwen/h/hamann.md |
| Schlözer, August Ludwig von | A.L. Schlözer | yuanwen/a/august-rehberg.md（源文作缩写形，照录） |
| Melon, Jean-François | Jean-François Melon | yuanwen/e/economics-early-modern.md 等 |
| Köhler, Wolfgang | Wolfgang Köhler | yuanwen/e/ehrenfels.md 等 |
| Viète, François | François Viète | yuanwen/d/descartes-mathematics.md 等 |
| Hoernlé, R.F.A. | R.F.A. Hoernlé | yuanwen/b/bosanquet.md; yuanwen/l/langer.md |
| Thomsen Thörnqvist, Christina | Christina Thomsen Thörnqvist | yuanwen/s/simon-faversham.md |
| LeMaître, Georges | Georges LeMaître | yuanwen/c/cosmology-30s.md |
| Lao Tzu | 老子 | yuanwen/c/chinese-legalism.md 等（汉字正形） |

* `Cinque (Joseph Cinqué)` 未填：语料仅见姓「Cinque」，全名「Joseph Cinqué」只见于键内括注——按「键列本体」档可采，但本批从严留待外源页核（记留队）。
* 告警 179 → 175（同期并行会话亦在补行，净额以 `check_terms` 输出为准）。

## 2026-11-09 多语种人工裁定批（26 行；自动初筛 → 人眼核对，拒误取）

**方法**：先以 `script/orig_foreign_batch_20261109.py` 自动初筛（en/ja 维基 API＋rigpawiki），
再从「同页片段」逐条人眼裁定；**只采页面显式给出的「罗马化 ↔ 原生文字」配对**（012 硬性裁定）。

**采信 26 行**（证据逐条落 `results/orig-evidence-2026-11-09.tsv`：键→原文→URL→片段）：

* 藏文 5（rigpawiki 页面正文 "Tib. X, wy, Wyl. Y" 形）：reliable cognition→ཚད་མ་（Tshad_ma）、appearing object→སྣང་ཡུལ་、Lorik→བློ་རིགས་、Collected topics→བསྡུས་གྲྭ་、doubt→ཐེ་ཚོམ་。
* 梵文 1：Śāntarakṣita→शान्तरक्षित（en.wiki 引导句 "Sanskrit: शान्तरक्षित; Tibetan: ཞི་བ་འཚོ"）。
* 日文 3：谷崎潤一郎、鴨長明、西田幾多郎（ja.wiki 条题正形＋en 引导句汉字）。
* 阿拉伯/波斯 17（en.wiki 引导句 "Arabic:/Persian: <全名>"，键内元素均在原字形内）：Jābir ibn Ḥayyān、al-Samawʾal、Ḥallāj、al-Bīrūnī、al-Nayrīzī、al-Shahrastānī、al-Sijzī、Sijistānī、Qūnawī、Jāmī、Ghazālī（父/弟两行）、Ibn al-Khaṭīb、ʿAbd al-Laṭīf、Ṭabāṭāʾī、Ḥāfiz、Iblīs。

**拒采（留队，记明理由）**：① 碎片式命中——ابو（仅父名助词）、رباعیات（《鲁拜集》书名）、لسان/محمد/صدر/تاج 等；② **错人**——al-Bukhārī 页面为 810–870 圣训学者，非键所指 Shams al-Dīn Muḥammad al-Bukhārī；③ 库尔德文转写（Shahrazurī شەمسەددین，非阿/波字形）；④ 仅姓氏页（Kirmānī/Kāshānī/Rāzī/Shīrāzī/Iṣfahānī/Lāhijī/Fanārī/Waliullāh/Taftazānī/Khayyam/Ibn Sabʿīn）——键含本名，填仅姓氏即失配。

**教训**：自动「邻近窗口」抽取对阿拉伯/日文误取率高（父名助词、书名、同姓他人），**必须人眼核片段**；这与 012「禁推演」同源——机器只能提供候选，裁定须留证据。

* 告警 180 → 164（同期并行会话仍在加行，净额以 check_terms 为准）；check_all 7/7 绿。

## 2026-11-13 本地配对实证 + 权威辞书联网查证批（12 行）

**方向声明**：用户三轮指令合观为“偿还两登记册告警；SEP 原文以本地 `en/` 与 `yuanwen/` 为准，不联网抓取；凡增补修订值必须联网查证且符合规范；批准推进”。本批目标为术语表「非英语缺原文」告警的净偿还；非目标为不改译法、不改正文、不改门禁口径。验收判据：每行原文列取自权威辞书显式排印的词头，依据列含书名／条目／查证日期，`check_terms` 硬错误 0 且原文告警下降，`check_all` 9 项全绿。

**第一步，本地配对实证（结论：零合格配对）**：`script/scan_orig_pairs.py`（本地草稿，只报告）扫 `en/**/index.html` 与 `yuanwen/**/*.md`，对 169 个缺原文键查「同项罗马化 ↔ 原生文字」共现。命中 14 键，逐条判读**全为假阳性**：汉字来自中文人名、典籍题名与书目（如 `en/korean-philosophy/index.html:227` 的“一心”、`:257` 的“圓測”），希腊字母来自逻辑符号 φ／Φ 与 ψ 记号，**没有一条构成术语与原生文字的显式配对**。报告落 `specs/008-terminology-campaign/results/orig-local-pairs-2026-11-13.tsv`。此结果复证 ADR-0030 的结构性结论：SEP 上游页面通篇用转写，不附原生文字，靠语料自足无法清偿该告警。

**第二步，联网查证权威辞书**：按 ADR-0030 第 2 级来源，取 Monier-Williams《梵英辞典》、Edgerton《佛教混合梵语辞典》、Böhtlingk–Roth《彼得堡大辞典》、Apte《实用梵英辞典》与《翻译名义大集》的天城体词头，经 wisdomlib DDSA 转录版、DILA 梵汉英佛学词典与 84000 译经词汇表交叉核对；维基系仅作词头线索，不作依据。**未用 IAST 等映射表正推或逆推**，所有天城体字形均读自辞书排印词头。逐行凭证见 `specs/008-terminology-campaign/results/orig-verify-2026-11-13.tsv`。

采信 12 行：`nirvāṇa`→निर्वाण、`Bodhisattva`→बोधिसत्त्व、`Mahāyāna`→महायान、`karma（佛教业报义）`→कर्म、`anātman`→अनात्मन्、`Prajñāpāramitā`→प्रज्ञापारमिता、`ālayavijñāna`→आलयविज्ञान、`śrāvaka`→श्रावक、`arhat`→अर्हत्、`skandha`→स्कन्ध、`dharmakāya`→धर्मकाय、`dharmatā`→धर्मता。词干／用例形异说（`karman` कर्मन् 对 कर्म、`arhant` अर्हन् 对 अर्हत्）、`bodhisatva` बोधिसत्व 异写、`skandha` स्कन्ध 与战神 `Skanda` स्कन्द 之辨，均逐条记入凭证备注，不混用。

**工具与护栏**：`specs/008-terminology-campaign/bin/apply_orig_column.py`（凭证驱动，支持 `--ledger` 续批）。按规则的批量改写护栏：按“键”精确定位、逐行身份追踪、只写第 2／5／6 列、覆盖式清除“原文列待考”、依据列含凭证名即跳过（幂等）、未匹配／多匹配／列数异常残余为 0 才允许写回。干跑残余 0 后写回 12 行，复跑全部判“已回填，跳过”。

**验收**：`check_terms.py` 原文告警 **169 → 157**（净偿还 12 条），硬错误 0；`check_all.py` 9 项全绿。

**遗留**：157 条以藏文 Wylie、阿拉伯／波斯术语、日文与希腊文为主，本地语料无配对，须逐批走权威工具书通道。按 ADR-0030 第 4 条，「工具书查无者」在依据列注明后保留 `—`，但 `check_terms` 告警口径不变，故该类告警在现行规则下不可全量归零；要么持续多轮逐行补证，要么由用户对「查无行的告警豁免」作规则层裁定（走 ADR）。

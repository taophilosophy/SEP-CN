# 013 人名籍属/生卒列 · 执行记录

## 2026-11-07 阶段 0：结构迁移（完成）

**指令来源**：用户「对于人物必须标注国籍或地区或民族或其他，生卒年或鼎盛年。新增此两列。」；随后补充「阿拉伯人名有的也有通俗中文译名，特别注意。」

**结构变更**

* `ren-ming-biao.md`：六列 → **八列**，在「译法」后插入「籍属」「生卒/鼎盛年」，全行初值 `—`。
* 首轮迁移 1609 行（`script/_add_person_cols.py`，幂等）；并行会话随后新增的六列行由重跑补齐 19 行；另修 1 行列数异常（`Parreut, John` 旧五列）。
* 术语表 `yi-zhe-shuo-ming.md` 保持六列不变。

**工具变更**（`tools/check_terms.py`）

* 新增 `parse_registry2_full()` 八列解析（返回含 nation/years 的九元组）；`parse_registry_full()` 改为投影回原七元组，**旧工具（term_audit / tl_browser_batch）零改动**。
* 六列旧行容忍（nation/years=None）；`>8 列` 告警。
* 新增 `person_missing()` / `write_person_missing()` 与告警「人名缺籍属/生卒」，清单落 `specs/013-person-attribution/results/person-missing.txt`（不计硬错误，阶段 3 再议升级）。

**回归**：`check_all` 7/7 全绿；`check_terms` 硬错误 0；队列 1626 条。

## 2026-11-07 阶段 1：首批回填（40 行）

**方法**：只回填**本会话已抓取过的同一来源页**（其信息框同时给出原文、生卒、地域），一次核销三列；证据行在 `state/person_fill.tsv`（不入库）。

* 阿拉伯系 25 行（含同人异键：Ghazālī 两形、Rāzī 两形、Ṭūsī 两形、Suhrawardī 两形、Mullā Ṣadrā 两形）。
* 梵语／佛教系 15 行；非历史人物（Mañjuśrī、Vimalakīrti）写「非历史人物（…）」＋「不适用」。

**同人核对（用户提醒落实）**：以通俗中文译名为锚点逐个确认「同一人」，再落键——

| 键 | 通俗译名 | 原文 | 判定 |
| ---- | ---- | ---- | ---- |
| Ibn Sīnā / Avicenna | 伊本·西那（阿维森纳） | ابن سينا | 拉丁名与阿拉伯名同指 ✓ |
| Abū Bakr al-Rāzī / Rhazes | 拉齐（医师哲学家） | أبو بكر الرازي | 勿与法赫尔丁·拉齐混 ✓（表内已注） |
| Fakhr al-Dīn al-Rāzī | 法赫尔丁·拉齐 | فخر الدين الرازي | 神学家，非医师 ✓ |
| Rūmī | 鲁米 | جلال الدين الرومي | 波斯苏非诗人 ✓ |
| al-Fārābī | 法拉比（阿尔·法拉比） | أبو نصر محمد الفارابي | ✓ |
| Mullā Ṣadrā | 毛拉·萨德拉／穆拉·萨德拉 | ملا صدرا | 两行同人 ✓ |

**纪律**：籍属取「地区／民族＋领域」而非单一国籍（古典人物国籍难断）；年代一律拉丁数字，与「原文」列分离。

**遗留**：队列 1586 条（主要为欧美近现代人物与日韩人名）。日／韩／藏人名的出生地与年代须逐条核页，不得据记忆填。

## 2026-11-09 反向校对批（同人异形合并 8 组 + 同姓异人注 3 处）

**指令**：用户「人名表再反向校对……必须联网核查，禁止虚构或推断」。

**方法**：新工具 `script/rev_classify_20261109.py`——取「同一中文译法 ↔ 多个不同原文键」组，按词元集合（NFD 折叠、去逗号、casefold）判「同人异形」与「疑似异人同译」：65 组同人异形、27 组待核。

**处置**

1. **同人异形合并 8 组**（主形按 SUMMARY 定名/语料/首登记，别名入「亦作」，出处并双来源）：
   `Mullā Ṣadrā`（SUMMARY 穆拉·萨德拉 ← 毛拉·萨德拉）、`al-Nayrīzī`（奈里齐 ← 纳里齐）、`Boyle, Robert`（SUMMARY 罗伯特·波义耳 ← 玻意耳）、`Eustachius a Sancto Paulo`（尤斯塔修斯 ← 欧斯塔基乌斯）、`Heinrich Scholz`（SUMMARY 海因里希·肖尔兹 ← 肖尔茨）、`Hintikka, Jaakko`（欣蒂卡 ← 保留英文形；并修年代列串位 `—；tarski-truth`）、`Melissus`（麦里梭 ← 墨利索斯）、`Otto von Bismarck`（全名 ← 俾斯麦）。
2. **同姓异人注 3 处**（不合并，互指以免读者混淆）：Bruce Bridgeman ↔ Percy Bridgman（皆译“布里奇曼”）、Davidson, Maria ↔ Davidson, Donald（皆译“戴维森”）、Robert Brandon（生物学哲学）↔ Robert Brandom（推论主义，**拼写不同、确为两人**，非笔误）。
3. **待核留队 2 处**：`Vidyānanda Pātrakesarisvāmin` 与 `Vidyānandin` 同译“毗提耶难陀”，登记行称“同一人异写”，学界另说为两人，须外源页核实后再定（本批未改）。
4. 65 组「姓, 名 ↔ 名 姓」双形式**保留**（键分别匹配书目形与正文形，属登记册设计内别名链，relation 审计 2026-10-31 已定「良性同义形」）。

**联网核查**：termonline-standard 对 al-Nayrīzī／Boyle／Melissus／Bismarck／Mulla Sadra／Hintikka／Bridgman／Eustachius 全部查无（人名不在标准库），故主形判定走 SUMMARY 定名与语料用形两档，逐条在案。

## 2026-11-13 凭证化批（并网硬编码行的合规化与纠错）

**方向声明**：用户三轮指令合观为“偿还术语表、人名表告警；SEP 原文 HTML 以本地 `en/` 与 `yuanwen/` 为准，不联网抓取；凡增补修订值必须联网查证且符合规范；批准按此推进”。目标是把无凭证的增补值逐行换成可回溯证据；非目标为不改译法、不改正文、不改门禁口径。验收判据：每行依据列含权威源与查证日期、`check_terms` 硬错误 0、`check_all` 9 项全绿、凭证入库。

**取证链**：一级为本地来源页（`en/<slug>/index.html`，逐条记行号与原文片段）；二级为联网权威工具书与国家图书馆规范标目——LC NAF、BnF、GND／德国数字图书馆、Britannica、SEP 官网与镜像、Springer《Encyclopedia of Renaissance Philosophy》、ODNB／Jackson Bibliography、《中国大百科全书》第三版网络版。维基系只作线索，不作依据。逐行凭证见 `results/verify-2026-11-13.tsv`（18 行，含权威源 URL、本地页行号、判定备注）。

**处置**：并行会话已入库的 `specs/008-terminology-campaign/bin/fill_person_meta.py` 以硬编码填了 17 行籍属／生卒，依据列仅写“据学界通行”，无凭证。本批不删该脚本，改为按凭证覆盖式写入 18 行（含 Fakhr 重复行合并留痕），清除无凭证措辞，逐行补权威源与查证日期。

**联网查证发现的 5 处错值，已更正**：

| 键 | 硬编码初值 | 更正与依据 |
| ---- | ---- | ---- |
| Allan Ramsay | 苏格兰，1686–1758 | 来源页 `en/scottish-18th/index.html:671` 指画家（与休谟、斯密共创 Select Society），Britannica 同名条目作 1713–1784；1686–1758 为其父诗人，属实体错配 |
| Hermeias | 埃及，c. 410–c. 450 | 生卒仅见维基系，禁作依据；按 ADR-0031 改 `fl. 5 世纪中叶`，籍属取 `en/ammonius/index.html:147,223–234` |
| Syrianus | 希腊（亚历山大里亚生，雅典卒），d. c. 437 | `en/syrianus/index.html:149,227,284` 明载生于亚历山大里亚、主要活动于雅典、约 437 年卒；籍属改埃及（亚历山大里亚），生年不可考只留卒年 |
| Nicolaus Taurellus | 德国，1547–1606 | `en/taurellus/index.html:147` 与 Springer 条目作生于蒙贝利亚尔（时属符腾堡，今法国杜省），籍属按出生地政权归属写明 |
| James Dunbar | 苏格兰，c. 1742–1798 | ODNB／Jackson Bibliography 标目作 1742–98，去 `c.`；精确月日仅见档案级来源，不入表 |

另：Jean Baudrillard 生日存在 7 月 27 日（LC NAF）与 29 日（Britannica）异说，年份无争议，异说留痕；William of Champeaux 卒年取本地 SEP 来源页 1122，工具书多作 1121，异说留痕不臆改；Charles Leslie Stevenson 卒年按《中国大百科全书》取 1979（中文文献有作 1978 者）。

**工具**：`bin/apply_person_meta.py`（凭证驱动，支持 `--ledger` 多批续跑）。护栏按 rules/05：只按“键”精确定位、逐行身份追踪、只写第 4／5／7／8 列、覆盖式清除旧措辞、依据列含本批凭证名即跳过（幂等）、未匹配／多匹配／列数异常残余为 0 才允许写回。干跑残余 0 后写回 18 行，复跑全部判“已回填，跳过”。

**门禁**：`check_terms.py` 硬错误 0；`check_all.py` 9 项全绿。

**规模事实**：本批是合规化而非净偿还——17 行在上一会话已被填入值，故不在缺项队列内；并行会话同期另补 2 行，队列由 3485 降至 3483。术语表另有 169 条“非英语缺原文”告警。按 ADR-0030／0031，工具书查无者须留 `—` 并注明，检查器告警口径不变，故两类告警在现行规则下不可全量归零；后续按批次偿还，需用户对“查无行的告警豁免”作规则层裁定（走 ADR），或持续多轮逐行补证。

## 2026-11-13 GND 规范标目批（A 段 46 行）

**方向声明**：用户指令「偿还术语表，人名表告警，联网查证」。本批目标为人名表「籍属／生卒」告警的净偿还；非目标为不改译法、不改正文、不改门禁口径；验收判据为每行依据列含权威源与查证日期、`check_terms` 硬错误 0、`check_all` 九项全绿、凭证入库。

**通道定型**：德国国家图书馆 GND 规范标目，经 lobid.org 检索接口读取（`https://lobid.org/gnd/search?q=…&filter=type:Person`，单条 `https://lobid.org/gnd/<id>`）。选此源的理由：ADR-0031 明列「各国国家图书馆规范标目」为第二级来源；GND 记录同时给出规范形、生卒日、出生／卒地、地域码与职业，可一次核销两列并支持同姓异人排除。逐条 5 秒间隔（rules/05 抓取礼貌），失败退避重试三次。

**取样与命中**：按登记册顺序取 A 段 110 行（缺项队列 Latin 键 3247 行之前段），命中 50 行（exact 36＋variant 14）、歧义 12 行、查无 48 行。逐行复核后采信 46 行；凭证 `results/verify-2026-11-13-gnd-a.tsv`（46 行，含 GND 号、规范形、职业与匹配方式）。

**逐行复核的拒采（5 行，避免实体错配）**：

| 键 | 抓取结果 | 拒采理由 |
| ---- | ---- | ---- |
| Abrabanel, Judah | Leo, Hebraeus（1460–1523） | 别名形误命中莱奥内·埃布雷奥（其子），非犹大·阿布拉瓦内尔 |
| Alan Macdonald | Pritchard, Alan（1955–） | 同姓异人，键所指非此人 |
| Albrecht Becker-Freyseng | 1907–，哲学家／语文学家 | 与键所指身份不合，实体存疑 |
| Albo, Joseph | Albo, Yosef（1365–1444） | 生年与学界通行 c. 1380 冲突，不采 |
| Andreas Rüdiger | Luft, Andreas Rüdiger（1972–，医生） | 同姓异人，键所指为 1673–1731 哲学家 |

**歧义行处置**：12 行同姓多值，仅对可凭生卒与身份唯一定位者人工选定 GND 号（John Quincy Adams 1767–1848、Joseph Addison 1672–1719、Adolf Reinach 1883–1917、Aijaz Ahmad 1941–2022）；其余（Wilhelm Ackermann、Alexander V、Larry Alexander、Archibald Alison、Amy Allen、Elizabeth Anderson、Guy Anderson、Michael Anderson）留队，待逐条另核。Archibald Alison 之父（1757–1839）与子（1792–1867）同姓名，须依首现词条定人后再落表。

**既有值冲突（不改他方数据）**：`Alvarado, José Tomás` 登记册已有「哥斯达黎加」，GND 地域码作 Chile；按 013 非目标（不改既有列）本批不覆盖，另立核对项。

**验收**：`check_terms.py` 人名缺项告警 **3328 → 3282**（净偿还 46 条），硬错误 0；`check_all.py` 九项全绿。**规模事实**：A 段 110 行命中率 45%（50/110），其中 5 行须拒采、12 行须另核；按此比率，余量 3282 行在 5 秒礼貌间隔下约需 60 小时持续作业，非单会话可清，须按批推进。

## 2026-11-13 GND 规范标目批（B 段 48 行）

**范围**：接 A 段（110 行）续取 120 行（Anselm of Canterbury 至 Bartolus of Sassoferrato）。命中 55 行（exact 40／variant 15）、歧义 14、查无 51。逐行复核采信 48 行，凭证 `results/verify-2026-11-13-gnd-b.tsv`。

**逐行复核的拒采（9 行）**：

| 键 | 抓取结果 | 拒采理由 |
| ---- | ---- | ---- |
| Antoine Le Grand | Arnauld, Antoine（1612–1694） | 同姓异人：勒格朗（1629–1699）与阿尔诺非一人 |
| Arthur Schopenhauer | Keller, Arthur S.（1891–） | 姓名检索错配；改为人工定位 gnd 118610465（1788–1860）后采信 |
| Ash, Michael | Ash, Michael R.（1961–，作者） | 职业不足以定人，身份存疑 |
| Ashton, Michael | 1968–，金融分析师 | 与键所指不合 |
| Ashkenazi, Shaul | 1470–1523，地域码「Land unbekannt」 | 无籍属可据，留队 |
| Auriol, Peter | Hill, Peter Murray（1908–1957，演员） | 同姓异人；奥里奥尔（c. 1280–1322）另论 |
| Barber, Alex | 2005–，儿童文学作者 | 生年与键所指学者不合 |
| Barrio, Eduardo | Matos Barrio, Eduardo（1904–1995，摄影师） | 同姓异人；键所指为当代逻辑学家 |
| Bartel, Christopher | 1987–，医生 | 同姓异人 |

**人工定位（7 行，专名检索被同名者挤占后按生卒与身份取号）**：Schopenhauer gnd 118610465、Francis Bacon 118505696、Jane Austen 118505173、Alexander Bain 116040793、John Austin 118505181、Susan B. Anthony 118645331、Ernest Barker 119237350——逐条取单条记录核验生卒、地域码与职业后落表。

**歧义留队（14 行）**：Susan B. Anthony（自动检索）、Anton Ulrich、Armstrong, David、Arnauld, Antoine、Arnold Ruge、Austen, Jane（自动检索）、Austin, John（自动检索）、Bacon, Francis（自动检索）、Bain, Alexander（自动检索）、Francke, August Hermann、Barker, Chris、Barker, Ernest（自动检索）、Barnes, Elizabeth、Barr, Michael——其中 7 条已由人工定位解决，其余 7 条待另核。

**存疑留队**：`Balme, David`（GND 地域码 USA，与常见英国说异，不落表）。

**验收**：`check_terms.py` 人名缺项告警 **3282 → 3234**（净偿还 48 条），硬错误 0；`check_all.py` 见收工记录。累计两批 A/B 段 94 行，命中率约 45%，拒采率约 6%（14/235 命中中 14 条实体错配）。

## 2026-11-14 GND C 段与歧义另核（52＋10 行）

**范围**：GND 续取 120 行（B 段之后），命中 63（exact 54／variant 9）、歧义 22、查无 35。逐行复核后采信 52 行；另有 A/B 段遗留的歧义与错配 13 人另源核实，采信 10 行。凭证 `results/verify-2026-11-14-gnd-c.tsv`、`results/verify-2026-11-14-alt.tsv`。

**C 段复核要点**：拒采 `Booker T. Washington`（GND 命中蓝调乐手 Bukka White，本名恰为 Booker T. Washington White，与十九世纪教育家非一人）；人工改正五处籍属口径：Batson 补国别（美国／心理学）、Bolyai 补匈牙利、Spinoza 取荷兰（GND 双值 Germany 为接受史著录）、Boethius of Dacia 补丹麦、Benedict XII 改神学（原以“外交”充学科）；`Blund, John` 生年 1185 与通行 c. 1175 异说留痕。`Bocheński` 两键同号并存待并档。

**另源核实**：Armstrong（澳大利亚，1926–2014）、Arnauld（法国，1612–1694）、Alison（苏格兰，1757–1839，与其子 1792–1867 别）、Amy Allen（美国，1970–）、Elizabeth Anderson（美国，1959–）、Michael Anderson（美国，1951–）、Ackermann（德国，1896–1962）、Alexander V（希腊／意大利，c. 1339–1410）、Larry Alexander（美国，1943–）、Balme（英国，1912–1989，ODNB；GND 地域码 USA 异说留痕）。查无：Barber、Bartel、Barrio。

**并发事故与处置**：本批写回期间另一会话连续执行合并与清理，两次抹去未提交的登记册改动与未跟踪凭证；已由 `script/_tmp/gnd-c.tsv` 重建 C 段凭证、按会话记录重建另源凭证，重放后即时提交。合并另带入 4 处空重复行（Apt、Benedict XII、Benedict XVI 等），按“同键同译、一有一无”删除空行，硬错误归零。

**验收**：`check_terms.py` 硬错误 0；人名缺项 3236 → 3187（含并行会话新增行与本次净偿还）；`check_all.py` 除并行会话在途的 `tasks/b/brouwer.json` 学术项外全绿。

## 2026-11-14 GND D 段（50 行）

**范围**：续取 120 行（Born 至 Cassirer），命中 57（exact 48／variant 9）、歧义 21、查无 42。采信 42 行，另对 8 位同姓多值名家人工定位后补入，共 50 行；凭证 `results/verify-2026-11-14-gnd-d.tsv`。

**拒采 4 行**：`Brutus, Marcus Junius`（GND 生日作公元前 8—前 4 年，与通行前 85—前 42 不合）、`Cai Yong`（命中现代同名者 Wang, Cai-Yong，1961–）、`Campbell, Dugald`（GND 仅作传教士，身份不合）、`Borrows, John`（GND 地域码 USA，与加拿大法学家身份冲突，留队）。无籍属可据而跳过者：Bos、Brady、Bunt、Burstall、Callus。

**人工定位 8 人**：Brentano 1838–1917（奥地利／德国）、Boyle 1627–1691（英国）、Cantor 1845–1918（丹麦／德国）、Burke 1729–1797（爱尔兰／英国）、Born 1882–1970（德国／英国）、Butler 1692–1752（英国）、Carlyle 1795–1881（英国）、Cardano 1501–1575（意大利）。

**口径校正**：Byron 取英国（GND 双值德国为出版史著录）、Cassirer 取德国／美国（GND 四值取首二会误置瑞典）。

**验收**：硬错误 0；人名缺项 3187 → 3137；凭证与登记册同批提交（16274f5e7），避免并行会话再次抹去未提交改动。

## 2026-11-14 GND E 段（42 行）

**范围**：续取 120 行（Catena 至 Cole），命中 62（exact 50／variant 12）、歧义 20、查无 49。逐行复核采信 42 行；凭证 `results/verify-2026-11-14-gnd-e.tsv`。

**口径校正**：Cather 取美国（GND 三值中英、捷为译本与出版著录）；Chakrabarty 取印度／美国（原序会成“美国／澳大利亚”）；Chan 取加拿大／新加坡；朝鲜两位学者（Chŏng Chedu、Chŏng Tojŏn）按时代取“朝鲜／儒学”，不用 GND 现代南北韩码。

**跳过**：无地域码者 Cohen, Ronnie／Cohen, Stewart；`Clairaut, Alexis` 与 `Clairaut, Alexis-Claude` 两键同人，均采同号（待并档）。

**留队的高价值歧义**：Darwin、Baudelaire、Chalmers、Charles Mills、Cicero、Thomasius、Samuel Clarke、Cayley、Clement V、Cohen, Joshua——均因同姓多值且尚无可据的单一记录，留待另源或指定首现词条后处理。

**验收**：硬错误 0；人名缺项 3137 → 3095；数据与凭证同批提交（eada9bf14）。

## 2026-11-14 GND F 段（47 行）

**范围**：续取 120 行（Cole 至 de Sitter），命中 55（exact 47／variant 8）、歧义 17、查无 44。采信 47 行；凭证 `results/verify-2026-11-14-gnd-f.tsv`。

**拒采 4 条实体错配**：`Costa, Paul`（命中 1672–1726 木雕家 Costa, Pau）、`Crupi, Vincenzo`（命中 1952 年文学研究者，与逻辑哲学家不合）、`Dana Scott`（命中 Spears, Dana Scott，非 1932 年生逻辑学家）、`David Hull`（命中 Holmes, David H.，1865–1918 古典学家）。

**口径校正**：Condillac 取“法国／哲学”（GND 三值含意大利、瑞士为游历与出版著录）；Columbus 取“意大利／西班牙”（按出生地与卒地次序）。

**跳过**：Cohen 类无地域码者（Cowie、Cullen），以及 17 位同姓多值者（含 Donald Davidson、Stephen Davies、Richard Dawkins、Daniel Bell、Robert Dahl）。

**验收**：硬错误 0；人名缺项 3095 → 3048；数据与凭证同批提交（a04185529）。

## 2026-11-14 GND G 段（56 行）

**范围**：续取 120 行（Dekker 至 Eliot），命中 67（exact 57／variant 10）、歧义 10、查无 42，采信 56（跳过无地域码者 11）。凭证 `results/verify-2026-11-14-gnd-g.tsv`。

**拒采 1 条**：`Edward Stillingfleet`（GND 命中 1802–1862 的同名者，键所指神学家为 1635–1699）。
**口径校正**：Descartes 取“法国／哲学”（GND 双值为游历著录）；Duns Scotus 取“英国／法国／神学”。
**留队歧义 10 人**：Dennett、Dewey、Dworkin、Edith Stein、Pierre Duhem、Dickie、Dietrich、Dodwell、Dorothea Veit、Edgar Bauer。

**验收**：硬错误 0；人名缺项 3048 → 2992，首次降到 3000 以下。凭证表头首次生成时有误，已重建并复核后再写回（e3907d0f2）。

## 2026-11-14 GND H 段（45 行）

**范围**：续取 120 行（Emanuel 至 Fraenkel），命中 61（exact 52／variant 9）、歧义 16、查无 47，采信 45（跳过无地域码 12）。凭证 `results/verify-2026-11-14-gnd-h.tsv`。

**口径校正 3 处**：Ernst Mayr 取“德国／美国／生物学”（GND 四值首二为印尼、巴新，系考察地而非籍属）；Erasmus 取“荷兰／人文主义”；Foucher de Careil 取“法国／哲学”。
**留队歧义 16 人**：Engel, Johann Jakob、Eno、Erdős、Meumann、Ernst Schröder、Euler、Evans, Gareth、Falk、Feigl、Ferguson、Feuerbach、Finch 两人、Flynn、Forster, Thomas、Foucault, Léon。

**验收**：硬错误 0；人名缺项 2992 → 2947。

## 2026-11-14 GND I 段（56 行）

**范围**：续取 120 行（Glisson 至 Gilbertus Porretanus），命中 61（exact 52／variant 9）、歧义 22、查无 36，采信 56。凭证 `results/verify-2026-11-14-gnd-i.tsv`。

**口径校正 1 处**：Hegel 取“德国／哲学”（GND 双值含瑞士，系著述出版与游历著录）。
**跳过**：Furlanus（无地域码）、George Boolos（GND 无地域码）等 6 人。
**留队歧义 22 人**：Engels、Ebert、Simmel、Gentile、Gentzen、Garber、Harvey Friedman、Friedmann、Georg Forster、Georg Ernst Stahl、Bilfinger、Washington、Froben 两人、Gale 两人等。

**验收**：硬错误 0；人名缺项 2947 → 2891。

## 2026-11-14 GND J 段（44 行）

**范围**：续取 120 行（Gillespie 至 Hallyn），命中 46（exact 39／variant 7）、歧义 25、查无 39，采信 44（跳过无地域码 10）。凭证 `results/verify-2026-11-14-gnd-j.tsv`。

**拒采 2 条**：`Gillespie, John H.`（GND 作 1858–1924，与键所指进化生物学家不合）、`Gunter, Carl`（GND 作 1885–1951，身份不合）。
**口径校正**：Gödel 取“奥地利／美国／逻辑学”；新增 Tibet→西藏 映射（Gorampa 条）。
**留队歧义 25 人**：Goldman、Gramsci、Goya、Grant 三人、Glymour 类无地域码者、Hájek、Hale、Guo Xiang、Guyer、Lukács 等。

**验收**：硬错误 0；人名缺项 2891 → 2847。

## 2026-11-14 GND K 段（41 行）

**范围**：续取 120 行（Halpern 至 Hisdal），命中 45（exact 41／variant 4）、歧义 23、查无 43，采信 41（跳过无地域码 9）。凭证 `results/verify-2026-11-14-gnd-k.tsv`。

**拒采 4 条**：`Hao Wang`（GND 作 1993 年生，与 1921–1995 的逻辑学家不合）、`He Yan`（现代同名者，非魏晋玄学家）、`Hermes Trismegistus`（GND 命中 1769–1834 同名者，传说人物无生卒）、`Heytesbury, William`（GND 作 1809 年生，与 14 世纪哲学家不合）。
**口径校正**：Han Yongun 取“朝鲜／佛教”；Hindemith 取“德国／美国／音乐”（GND 四值首二为瑞士、土耳其，系流亡地）。
**验收**：硬错误 0；人名缺项 2847 → 2806。

## 2026-11-14 GND L 段（46 行）

**范围**：续取 120 行（Hiż 至 Rohault），命中 48（exact 44／variant 4）、歧义 18、查无 48，采信 46。凭证 `results/verify-2026-11-14-gnd-l.tsv`。

**拒采 2 条**：`Hugo Grotius`（GND 命中 1810–1878 的同名者，键所指为 1583–1645）、`Huan Tan`（命中 1981 年生现代同名者，键所指为汉代桓谭）。
**口径校正**：Holbach 取“法国／哲学”、Höffe 取“德国／哲学”、Im Yunjidang 取“朝鲜／儒学”；新增阿拉伯、叙利亚、挪威地域映射。
**留队歧义 18 人**：Hu Shi、Husserl、Hutcheson、Huygens 两人、Jackson、Hooke、Horthy 等。

**验收**：硬错误 0；人名缺项 2806 → 2760。

## 2026-11-14 GND M 段（44 行）

**范围**：续取 120 行（Jäger 至 Kaegi），命中 48（exact 43／variant 5）、歧义 20、查无 51，采信 44（跳过无地域码 1）。凭证 `results/verify-2026-11-14-gnd-m.tsv`。

**拒采 4 条（年代明显不合）**：`Ji Yun`（GND 作 1992 年生，键所指为清人纪昀）、`Johann Heinrich Lambert`（GND 作 1801–1862，键所指为 1728–1777）、`John Pollock`（GND 作 1878–1963，键所指为 1940–2012）、`José Ortega`（GND 作 1921–1990，键所指为 Ortega y Gasset 1883–1955）。
**口径校正**：Gottsched 取“德国／文学与哲学”、Borges 取“阿根廷／文学”；新增特立尼达和多巴哥映射。
**留队歧义 20 人**：William James、Habermas、Joseph Priestley、Hutcheson 类、Joyce、Toland、John Sergeant、Jonathan Bennett 等。

**验收**：硬错误 0；人名缺项 2760 → 2716。

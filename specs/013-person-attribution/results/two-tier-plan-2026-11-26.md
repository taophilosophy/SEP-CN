# 人名缺籍属/生卒两档收口方案（2026-11-26，用户批准“随译定点＋两档”）

现况：`person-missing.txt` 780 行（术语会话同步 5,000 数据行），GND/Wikidata 已扫过
一轮；Wikidata 0.6 次/秒即 429，试点 10 行仅 1 候选——批量不值当的判断成立。

## 两档

| 档 | 范围 | 道路 | 判据 |
| ---- | ---- | ---- | ---- |
| A 古代／近代 | 卒年可考的历史人物 | GND（lobid 主道；DNB SRU 与 id.loc.gov 403 在案） | 严格姓＋名＋职业三重判据分诊；防线照旧：无逗号键且候选生年>1850 不自动采、fl.≥2020 不采、误采全量撤 |
| B 当代学者 | 查无确年的在世/晚近学者 | 不再批量；“查无留空”按 013 既有口径收口 | 随译定点：正文翻到谁、顺路核谁 |

## 本轮动作

1. **候选池采集（不出判定）**：`bin/gnd_batch_candidates.py` 把 780 行全量过 lobid
   精确名检索（每名 ≤3 命中、间隔 ≥5s、断点续跑），落
   `results/gnd-candidates-2026-11-26.tsv`；**只采集不写册**，判定走三重判据人工线。
2. **判定线**：A 档候选按防线分诊后，经 `bin/apply_person_meta.py` 写册（现工具），
   每批留凭证行号；B 档在 `person-missing.txt` 维持“查无”状态，不追加记录。
3. **随译定点**：正文翻译遇到的人名顺路核；核到的按 A 档判据入册。

## 不做

* 第三轮全量 Wikidata（限速与命中率双低）。
* 无候选自动写册（防线即是判据，GND 会错例在案）。

## 工具与格式（2026-11-26 定型）

* `bin/gnd_batch_candidates.py`：候选列四列制（键｜原文｜译法｜候选），候选列为
  `q=…; verdict=HIT/MISS/ERR; gndIdentifier=…; preferredName=…; dateOfBirth=…; dateOfDeath=…;
  countryOfActivity=…; professionOrOccupation=…; type=…`，多候选 ` || ` 分隔，制表符已清洗；
  限速按"相邻请求 ≥5s"计（同一次判定的两个查询形共享节流），断点 state 每 10 名落盘。
* `bin/gnd_triage.py`：判定线。R1（无逗号键且候选生年>1850 不自动采）、R2（floruit≥2020
  不自动采）、三重判据（姓＋名/首字母＋学界职业）全过且国别可映射 → auto；否则 review；
  无命中 → none。国别映射走德→中表（54 国在册），映射外（城市名等）进 review 人工。
  auto 档产 `gnd-auto-ledger-2026-11-26.tsv`（apply_person_meta 凭证格式），**写册前仍须
  人工过目**——GND 会错例防线只挡机器，不替代判定。

## 实测结论（2026-11-26 晚，172 名先头批）

GND（lobid）按「姓, 名」检索的**同名率极高**，自动档实测 **0/172**。三个判例：

| 键 | GND 首条命中 | 问题 |
| ---- | ---- | ---- |
| Blake, Michael | Schriftsteller 1945–2015 | 同名作家，非政治哲学家 |
| Collins, John | Musiker/Songwriter 1944 | 同名音乐人 |
| Crupi, Vincenzo | Literaturwissenschaftler 1952 | 同名文学研究者 |
| Baumgartner, Michael | 1996– | 生年过晚（R3 防线拦下） |

判定线上过的防线：R1（无逗号键＋生年>1850）、R2（floruit≥2020）、R3（生年≥1980，
SEP 作者群极少年份，疑同名）、同名多候选（size=3 命中里 2 条以上即判歧义）。
即使加上「唯一候选＋学界职业＋有年份」三重，前 172 名仍无一条落 auto。

Wikidata 侧同时复测：`wbsearchentities` 直接 429（unthrottling 需联系 WMF），
与既有「0.6 次/秒即 429」记录一致。

**结论**：人名元数据**不做批量自动回填**，两档方案维持——GND 只产**候选 dossier**
（`gnd-candidates-2026-11-26.tsv`，含生卒、职业、出生地，供人工消歧），A 档仍走人工判定；
B 档查无留空。

## 全量跑完的实测（2026-11-26 晚，780/780）

后台池跑满 780 名后重跑判定线（`gnd_triage.py`，候选池按键去重、后者胜）：

| 档位 | 条数 | 处置 |
| ---- | ---- | ---- |
| auto | 6 | 仅作待核条目（不直接写登记册）：Dorsey, Dale（1976–）、Kirmānī, Ḥamīd al-Dīn（963–1021）、Lopez-Escobar, Edgar（1937–）、McCrae, Robert（1949–）、Molema, S. M.（1892–1965）、Pelletier, Francis Jeffry（1944–） |
| review | 383 | 人工扫读 `gnd-review-short-2026-11-26.tsv`（已按姓名过滤＋年份／职业排序） |
| none | 391 | 查无可用候选，留空 |

即全量自动档也只有 **6/780（0.77%）**，且 6 条均为“人名一致＋学界职业＋年份合理”，
仍以人工复核为准。auto-ledger 只作凭证草稿。

人工复核抓到的反例已进防线：`Páez, Andrés` GND 记 Jurist，而 en/ 里 Paez 2022 是
美学／知识论作者，执业域不合即可能同名异人 → 降 review（`gnd_triage.SUSPECT`）。

## review 池逐条筛（2026-11-26 夜）

383 条 review 中“有生卒且有职业”的 102 条已逐条判（台账
`gnd-review-decisions-2026-11-26.tsv`）：

| 判定 | 条数 | 说明 |
| ---- | ---- | ---- |
| 采信候选 | 6 | Thijssen, Hans（buridan 注释）、Tuna, Emine Hande（词条作者）、Planer, Ronald J.（gene 引）、Hawkins, Jennifer S.（informed-consent 引）、Wülfer, Daniel、Rötenbeck, Georg Paul（johann-sturm 正文） |
| 存疑 | 1 | Páez, Andrés（GND 法学家 vs SEP 哲学作者） |
| 驳回 | 95 | 非学界职业 65（摄影师／作曲家／乐手／演员／医生／牧师…）；学界职业但语境不符 30（含 Charles Mills→Tiebout、MacLeod→遗传学家、Perry→神学家等同名案） |

采信四人已填生卒（`ren-ming-biao.md`，依据列记 GND 号与 en/ 行号）；Tuna、Planer 只有
`19XX` 段，生卒仍留空。其余 281 条 review 无年份或同名多候选，须回原条目语境另查，
不入本轮。

### 第二轮：en/ 正文括注补生卒（批 62）

缺生卒的 668 行按「首现 slug → 姓氏 → 其后 70 字内的 YYYY–YYYY」重扫，得 40 条候选；
逐条看上下文后只有 6 条可用，采信率 15%。陷阱三型（与人名线旧记一致）：

* 页码区间（111–120、384–401 等，占 31/40）；
* 他人年份（Brouwer 夫人旁的 1881–1966 属其夫；Sturm 之父旁的 1635–1703 属其子；
  Yi I 旁的 1681–1763 属 Yi Ik）；
* 书目年份与连字符截断（Hull 处原文作 1884–52，按 1884–1952 记并注上游截断）。

采信 6：Ernst Christoph Graf von Manteuffel 1676–1749、E. C. Tolman 1886–1959、
E. R. Guthrie 1886–1959、C. L. Hull 1884–1952、Park Chungbin 1891–1943、
Yi Hwang 1501–1570。依据列记 `en/<slug>/<file>:<line>`。

### 判定台账覆盖

`gnd-review-decisions-2026-11-26.tsv` 现覆盖全部 383 条 review：采信 6、存疑 1、未判 281、
驳回 95。未判者均为“无生卒或缺职业”，旁证列已记条目内是否有引证（有 236／无 45），
留待随译按语境定人。

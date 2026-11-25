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

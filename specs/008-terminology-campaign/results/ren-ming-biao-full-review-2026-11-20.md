# 人名表全量复核（4,655 行逐行）2026-11-20

用户指令：“无法匹配的逐个判断是否是满足要求的术语，人名。对人名表全量复核”。会话 TL-main-20261120。口径：ADR-0012（人名表拆分、现代学者保留英文）、ADR-0022（现代学者体例：有通行汉名者汉名＋首现括注）。

## 方法与覆盖

* 全表 4,655 行列型核验（8 列：原文｜别名｜译法｜籍属｜生卒｜首现｜依据｜裁定日期），按 200 行/批切 24 份审核表逐行通读（含译法、生卒、首现、依据四列语义）。
* 机器标记预筛：重复折叠键组、书名号嫌疑、保留英文形、维基依据、无首现、译法空、机构学派嫌疑（F1–F9）。
* 判层：**合格性**（是否人名/机构学派误入/重复/译名合规）全量判；**数据完备性**（籍属/生卒缺失）只记补正面，不挡合格。

## 结论一：非人名行 = 0

4,655 行全部为真实人名条目或**有体例依据的名义人物**：

* 虚构/示例人物（Alice、Bob、Eve、Cordelia、Cleanth 类、Penelope、Solange、Octavia 等）——正文例证所需，依据列均注明“示例人名/虚构人物首译”；
* 神祇/神话/圣经人物（Zeus、Iris、Thaumas、Heracles、Achilles、Moses、Paul、Solomon 等）——学术通行汉译；
* 集体笔名（Bourbaki）、学派创始人头衔称谓（Guru Nanak 等）——单条登记合规；
* 汉学家自取汉名（葛瑞汉、安乐哲、任博克、普鸣、森舸澜、叶山等）——本人通行名，依据列注明；
* 保留英文的现代学者（41 行）——ADR-0022 判据，全部有“无通行汉名”依据。
* 无机构/学派/书名误入（F9 零命中；书名号嫌疑为零）。

## 结论二：真问题三类（已修）

### A. 首现列“首现（slug）”包装（45 行）→ 剥壳
例：`首现（xenophanes）` → `xenophanes`。依据为新格式统一（首现列本体即 slug/书目标签）。

### B. 生卒列“—；slug…”杂质（44 行）→ 清为“—”
例：`—；logic-fuzzy`、`—；prophecy`。成因同上（列错位后回落）。

### C. 缺“别名”列致整行后移一格（19 行）→ 列序重排
`[原文, 别名, 译法, 籍属, 生卒, 首现, 依据, 日期]` ← `[原文, 别名, 译法, 依据, 籍属, 日期, 首现, 译法残留]` 修正；涉及 quine-nf 批 12 行与数理逻辑批 7 行（Aczel、Boffa、Kuratowski、Wiener、Rosser 等）。前置门：别名列须为空才改。

### D. 依据列 ADR 引用笔误（10 行）→ ADR-0021 改 ADR-0022
ADR-0021 为 LLM 初译协议，该批行原文写“ADR-0021”（实指人名体例），统一改准。

### E. 生卒误植（1 行）
`Gregory, Alex` 记 1915–1999，而依据列为“现代学者（能力缺失理论，2016+ 论文）”，矛盾 → 生卒置“—”待核。

## 结论三：同人重复行 59 组（删 61 行，4,655 → 4,594）

合并语义沿 11-13 先例：keeper 保留；absorbed 删除并记“2026-11-20 重复行合并（旧键 `X` 并入）”，首现/依据取并集，生卒/籍属补缺，译法异形入“亦作”。全组清单见 `ren-ming-review-merge-2026-11-20.json`。典型组：

| keeper（保留） | absorbed（并入） | 说明 |
| ---- | ---- | ---- |
| Hugo Grotius（胡果） | Hugo Grotius（雨果，已标废弃） | 废弃行收编 |
| Theodor W. Adorno（西奥多） | Theodor W. Adorno（特奥多尔，已标废弃） | 废弃行收编 |
| Laozi | Lao Tzu | 拼形两行 |
| Hu Shih | Hu Shi | 拼形两行 |
| Dignāga | Diṅnāga | 同人异写 |
| Dostoevsky | Dostoyevsky | 拼形 |
| Feng Youlan / Fung Yu-lan | — | 拼形 |
| Suhrawardī（al-qudat 首现） | Suhrawardi、Suhrawardī / al-Suhrawardī | 三行合一组 |
| Peter of Abano | Pietro d'Abano、Pietro of Abano | 三行合一组 |
| Nicholas of Autrecourt | Nicolas of Autrecourt | 拼形 |
| Justinian | Justinian the Great | 称谓两行 |
| al-Ṭūsī, Naṣīr al-Dīn | Ṭūsī, Naṣīr al-Dīn | 拼形 |
| Peter of Spain | Peter of Spain / Petrus Hispanus | 全名形 |
| Levi ben Gerson (Ralbag) | Gersonides | 同名异语形 |
| Cangrande / Caesalpino / Clemens of Alexandria / Genshin 类 | — | 见清单 |

未合并的“同译法不同人”（Wilkinson Martin/Stephen/T.M.、Davidson Donald/Maria、Helen of Troy/Helene、Menger Carl/Karl、Kohlberg/Kohlberg 类）**保持分立**——同姓/同名异人，合并即错。

## 结论四：审计信号变动说明（诚实账）

合并前 absorbed 行中 3 行带审计状态（Lao Tzu 不一致、Hu Shi 不一致、Peter of Spain / Petrus Hispanus 一致）；keeper 行均为查无。三对的 absorbed 凭证命中已并入 keeper 凭证（laozi +48、hu_shih +22、peter_of_spain +18，含并网注记），但 term_audit 的相关性过滤按 keeper 词元（Laozi / Hu Shih / Peter of Spain）判，含拉丁拼形变体（Lao Tzu 等）的命中不参与判态，故 keeper 仍为查无。

**四态变动即此三行：一致 2,004→2,003、不一致 948→946、查无 8,818→8,760（另 58 行为删除的查无/噪声行）**。判定不改写、不人工翻转；如需这三行状态，应以其变体形另立查证任务，不做假翻转。

## 结论五：数据完备性（独立战役，不在本次范围）

2,723 行缺籍属或生卒（check_terms 长期告警，清单 `specs/013-person-attribution/results/person-missing.txt`）。属补齐类战役（联网/工具书逐条补），与合格性判定无关；本次只记录存量。

## 验收

| 项 | 结果 |
| ---- | ---- |
| 逐行通读覆盖 | 4,655/4,655（24 批） |
| 非人名行 | 0 |
| 机械修复 | 45＋44＋19＋10＋1 行（manifest `ren-ming-review-mech-2026-11-20.json`） |
| 重复合并 | 59 组／删 61 行（manifest `ren-ming-review-merge-2026-11-20.json`） |
| check_terms | 硬错误 0 |
| term_audit | 未查证 0；四态变动全部有账（见结论四） |

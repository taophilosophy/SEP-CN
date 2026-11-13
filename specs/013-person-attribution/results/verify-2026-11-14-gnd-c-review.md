# GND 取证 C 段复核（2026-11-14）

## 一、批次概况

- 抓取：`script/_gnd_batch.py --limit 120 --out script/_tmp/gnd-c.tsv --sleep 5`，完成 120 条，此前 state 已处理 230 条（A／B 段）。
- 状态分布：exact 54／variant 9／ambiguous 22／nomatch 35（含 error 0）。
- 凭证草稿：`verify-2026-11-14-gnd-c.tsv` 共 60 行，其中 7 行系 `script/_manual_b.tsv` 人工行（与 B 批重复，见第四节），实新增 53 行。
- 复核方式：逐行比对 `gnd-c.tsv` 同键的规范形、生卒、地域码、职业、传记摘录，并以 `en/` 原文语境（人名出现处及参考文献条）核定所指是否为同一人，未抽样。

## 二、可疑行

| 键 | GND 号 | 可疑理由 | 建议 |
| --- | --- | --- | --- |
| Booker T. Washington | 134555651 | GND 规范形为 `White, Bukka`（1909–1977），职业作“作曲家、词作者、音乐家、歌手”，即蓝调乐手 Bukka White，其本名恰为 Booker T. Washington White。与《Alexander Crummell》所述十九世纪教育家（1856–1915）并非一人；职业亦与本表体例不合。 | 拒采 |
| Batson, C. Daniel | 139632115 | 地域码作 `Land unbekannt`，脚本遂以职业“心理学”充作籍属，成“心理学”而无国别；传记摘录载其在堪萨斯大学任职，为美国心理学家。籍属栏以学科冒充国别，属口径错误。 | 改人工定位（美国／心理学） |
| Bolyai, János | 119372886 | 地域码作 `Ungarn`，该值未列入 `_gnd_to_ledger.py` 的 AREA 映射，籍属仅余“数学”，无国别。 | 改人工定位（匈牙利／数学） |
| Baruch Spinoza | 118616242 | 地域码作 `Deutschland；Niederlande`，故生成“德国／荷兰”。斯宾诺莎生于阿姆斯特丹，终身为荷兰境内居民，德国一项疑为后世接受史之著录，非籍属。 | 改人工定位（荷兰）；若主代理裁定保留原样，须在备注说明 GND 双值之由来 |
| Boethius of Dacia | 119228599 | 地域码作 `Frankreich；Dänemark`，`Dänemark` 未映射而被弃，籍属只剩法国；传记明言“ursprünglich aus Dänemark，在巴黎授课”，GND 职业亦仅“语法学家”，与“达西亚的”之名相悖。 | 改人工定位（丹麦／法国） |
| Benedict XII | 118508903 | GND 职业作 `Diplomat；Bischof`，脚本取首项，遂成“法国／外交”。本笃十二世为教宗，按本表体例当系神学，不宜以“外交”充学科。 | 改人工定位（法国／神学） |
| Bocheński, Józef M. 与 Bochenski, I. M. | 119245426 | 两键指向同一 GND 号、同一人（1902–1995），草稿各生成一行，入册即成重复登记。 | 合并：择一为主行，另一键在备注注明异写，或两行并存但须标同一 GND 号 |
| Blund, John | 100948499 | 生年 1185 与通行所记约 1175 略异；GND 传记仅载 1232–1233 年当选坎特伯雷大主教而遭教宗否决，未载生年，故 1185 无独立佐证。 | 可采（生年建议注“c. 1175”） |

## 三、未入册而需裁定者

下列三键在抓取中已命中，但被脚本以“缺项”跳过，未进草稿。若仅补草稿而不改映射，将永久留队。

| 键 | GND 号 | 情况 | 建议 |
| --- | --- | --- | --- |
| Bolde, Samuel | 1055505644 | 规范形 `Bold, Samuel`（1649–1737），GND 无地域码、无职业，脚本判无籍属而跳过。《Lady Masham》原文所列洛克友人 Samuel Bolde 即此人，英国教士。 | 改人工定位（英国） |
| Betegh, Gábor | 140805044 | 地域码 `Ungarn` 未映射，判缺项跳过；传记载其任剑桥大学 Laurence 古代哲学讲席，匈牙利人。 | 改人工定位（匈牙利） |
| Bonnay, Denis | 1275024246 | 地域码 `Land unbekannt`，且 GND 无职业，判缺项跳过；《Logical Consequence》所引者为法国学者。 | 改人工定位（法国） |

## 四、草稿层面的口径问题（非人名错配，供主代理处置）

1. **日期不实**：`_gnd_to_ledger.py` 内 `DATE` 硬编码为 `2026-11-13`，本批实际抓取于 2026-11-14，故表头“2026-11-13 查”及 60 行正文的“2026-11-13 经 lobid.org 接口读取”均早记一日，与文件名 `verify-2026-11-14-gnd-c.tsv` 不符。入册前须改日期或改脚本常量。
2. **七行重复**：`_manual_b.tsv` 被无条件追加，故 `Arthur Schopenhauer`、`Bacon, Francis / Francis Bacon`、`Austen, Jane`、`Bain, Alexander / Alexander Bain`、`Austin, John / John Austin`、`Anthony, Susan B.`、`Barker, Ernest` 七行与 `verify-2026-11-13-gnd-b.tsv` 逐字段相同，本批实增 53 行。另 `Arthur Schopenhauer` 同时在 `REJECT` 集合中，与其经人工行重新入册相冲突，建议清理该名单。
3. **AREA 映射缺项**：`AREA` 未收 `Ungarn`、`Dänemark` 等值，且缺值被静默丢弃，既不报错也不回退，是本批“籍属无国别”与“整行被跳过”的共同成因。建议补映射后对 Bolyai、Boethius of Dacia、Betegh 三键重跑，并让未映射值显式报出。

## 五、结论

- 草稿 60 行＝新增 53 行＋重复 7 行。53 行中：可直接采信 46 行；须改籍属口径 5 行（Batson、Bolyai、Spinoza、Boethius of Dacia、Benedict XII），此 5 行改后即可入册；生年存疑但可采 1 行（Blund）；须拒采 1 行（Booker T. Washington）；Bocheński 两行须合并为一行（净减一行）。
- 另有 3 键已命中却未入草稿，须人工定位。
- 凭证 TSV 未作任何改动，待主代理裁定。

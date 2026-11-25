# 词条人名索引（重译就绪产物，2026-11-25）

**用途**：rv-01 除术语表外还要人名对照。人名表键是「姓, 名」倒序，直接拿键匹配英文正文会大面积漏；本产物先把键还原成正文里实际出现的形，再逐词条输出「人名 × 次数」。

* 工具：`bin/entry_person_index.py`
* 产物：`results/entry-person-index-2026-11-25.tsv.gz`（gzip 约 1.1 MB；解压 85,980 行；列：entry／count／name_key／zh）
* 语料：`yuanwen/*/*.md` 2,418 件（英文侧）
* 匹配形：①「名 姓」（`Kant, Immanuel / Immanuel Kant` → `Immanuel Kant`）；②裸姓（`Kant`、`Hume`——正文最常见）；③别名列的 ASCII 形。裸姓只从「姓, 名」键取，且排除 60 余个常见大写词（David／Young／Price…），防撞普通词。
* 校验：命中后验词边界，并验原文首字母大写（防 `kant` 类小写误配）。
* **变音符折叠**（2026-11-25 补）：键与正文都做长度保持的 NFKD 折叠（`Nāgārjuna`→`nagarjuna`、`Śāntarakṣita`→`santarakssita` 形），否则带变音符的非西方人名全部漏配。折叠后 Nāgārjuna 词条命中 122 次、Madhyamaka 词条 Candrakīrti 41／Nāgārjuna 30、jaina-philosophy 30 人（Mahāvīra／Dharmakīrti 等）。

## 规模

| 指标 | 值 |
| ---- | ---- |
| 词条文件 | 2,418 |
| 有命中词条 | 2,288 |
| 输出行 | 85,980 |
| 抽样 | Hume 词条 510 次休谟、Kant 词条 479 次康德、Aristotle 词条 436 次亚里士多德 |

## 限制与坑

1. **裸姓撞名**：同姓不同人只保留先入册者（Mill→John Stuart Mill），同姓两家需人工分辨；「David」「Thomas」一类教名作姓的行仍会带来噪声（词条内次数低，可忽略）。
2. **「Wisdom」「Truth」等作姓者曾撞佛典「Perfection of Wisdom」**，已入常见大写词表排除；同类词（Good、Being）一并排除，代价是同名人物漏配。
3. **不含著作名**：著作行在术语表（`shu-yu-biao`），已由 `entry-glossary` 覆盖。
4. **不含纯汉名行**：译法为汉字的非西方人名（大雄、诃梨跋陀罗等）在英文正文明以转写出现，本轮只按 ASCII 形匹配，转写形（Mahāvīra 等）需要人名表补别名后才能命中——这是下一轮的补捞点。
5. 次数是**原文出现次数**，不是译名应出现次数；同一人可能以代词出现。

## 门禁

只读人名表与 yuanwen；产物 gz 入库。重跑约 1 分 10 秒。

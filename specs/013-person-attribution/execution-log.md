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

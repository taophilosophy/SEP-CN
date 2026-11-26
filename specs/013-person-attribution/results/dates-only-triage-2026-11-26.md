# 44 条“有年份无职业”GND 候选的年代相容性复核（2026-11-26）

承接 `two-tier-plan-2026-11-26.md` 的 review 池收口：383 条 review 中，102 条“有生卒＋有职业”
已按三重判据逐条判；本轮处理 **44 条只有年份、GND 无职业** 的一档——职业缺位使三重判据失效，
改用**条目语境年代相容性**作第一道筛，再对可另指者回权威档核实。

## 判据

1. **语境年代**：取首现词条 `en/` 正文首现句（`script/tmp/gnd44/context.txt` 档案）。语境人物
   的时代、在世区间或所属学术脉络与候选生年不相容者，直接驳回。
2. **权威档交叉**：候选的 GND 号经 lobid 完整记录取 `sameAs`，再经 Wikidata（`wbgetentities`）
   取 `P569/P570/P27/P106`。**只认有职业或国籍的实体**——仅年精度、无职业国籍的 Wikidata 条目
   多为 GND 导入件（本轮 26 条对应实体的 8 条），不作独立佐证。
3. **同名改判**：候选同名但语境所指另有专档者，按专档补录在册（生卒＋籍属），候选记驳回。
4. 无职业旁证、年代亦无矛盾者不硬填，留空等随译定点（两档方案 B 档）。

## 判定分布（44 条，台账 `gnd-review-decisions-2026-11-26.tsv` 已逐条回写）

| 判定 | 条数 | 处置 |
| ---- | ---- | ---- |
| 采信候选 | 12 | 生年与在册一致，无新增（Allwein、Brady、Bunt、Burstall、Göller、Lawry、Longeway、Mikhail、Muyskens、Rosenfield、Stamos、Wohlfahrt） |
| 改判识别 | 4 | 候选同名，语境所指另有专档，已在册补录（Robertson、King、Klein、Clarke） |
| 同名驳回 | 16 | 语境年代或身份不可能（Baumgartner、Beurer、Callias、Falk、Fritsche、Homer、Hotho、Howard、Huang Xu、Johann Friedrich、Nellie、Noble、Radcliff、Regnier、Straub、Ubaldo） |
| 存疑 | 4 | Mehta（原值系同名误取，已置回“—”）、Stanhope、Stegmann、Farley |
| 未判 | 8 | 年份相容但无职业旁证（Michael、Ross、Schulz、Simmons、Stephens、White、Young、Müller） |

## 写册八行（`bin/patch_b65_dates_only_triage.py`，幂等）

| 键 | 改动 | 凭证 |
| ---- | ---- | ---- |
| Robertson, G. | 生卒 1842–1892、籍属 英国 | Mind 1 (1876) 书目行＋WD Q983704／GND 116576707 |
| King, Peter | 生卒 1669–1734、籍属 英国 | lady-masham“his nephew Peter King”＋WD Q7175194／GND 131343440 |
| Klein, Peter | 生卒 1940–、籍属 美国 | closure-epistemic Klein 1995＋WD Q7173507／GND 138894388 |
| Clarke, Edward | 生卒 1650–1710、籍属 英国 | lady-masham＋WD Q19039689（GND 1055230068 同档，生年记 1652 属异说） |
| Burstall, Rod M. | 籍属 英国 | WD Q7356136（国籍英国，生卒与在册一致） |
| Stamos, David | 籍属 加拿大 | WD Q5237896（国籍加拿大） |
| Mehta, Uday | 生卒 1933 → — | 原值取自同名 GND 1145908829；语境作者 Uday Singh Mehta（WD Q28868996／GND 12165687X，无年份） |
| Nellie | 依据注非人物 | necessary-sufficient 例子中的象名；候选 Ladd 1859–1922 驳回 |

## 复核发现的三个登记册缺陷

1. **Mehta 生卒实为同名误取**：在册“1933”与 colonialism 语境作者（1999 年专著）无关联，权威档
   对该作者无年份。已置回“—”。这是 GND 单源填值无职业旁证时的典型失败形态。
2. **Nellie 不是人物**：`necessary-sufficient` 词条以“如果 Nellie 是一头大象”作假设例子，
   Nellie 是象名。该行保留（键已入别名体系），依据列注记非人物、不填生卒。
3. **Stanhope 候选年代偏晚**：hume-aesthetics 语境为休谟 1776 年前的顾问，GND 候选
   1755–1815 是第五代切斯特菲尔德伯爵（WD Q1026379），与语境不合；另有 Philip Stanhope
   1732–1768（Q7184415）年代相容。两说未定，记存疑，不填。

## 方法学量测

* “只有年份”档的可用率：44 条中 12 条可采信（27%），4 条改判识别（9%），16 条驳回（36%），
  余 12 条存疑或未判——与 en/ 括注取生卒 15% 的产出率同量级，说明**年份单值本身不构成身份**。
* Wikidata 对应率 26/44（59%），但其中 8 条为 GND 导入件（仅年精度、无职业国籍），
  独立佐证率 18/44（41%）。判定一律以“有职业或国籍”的实体为凭，避免自证循环。
* 通道：lobid `gnd/<id>.json`（需 `Accept: application/json`，否则返回反爬页）；WD API
  `wbgetentities` 批量 ≤50 号（WDQS 端点限速 1 次/分，批量 VALUES 查询须留 70 秒重试窗口）；
  Wikipedia `pageprops` 仅用于取 Q 号（经代理，TLS 握手偶断须重试），**不作年份凭证**。

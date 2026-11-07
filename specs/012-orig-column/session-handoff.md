# 交接卡：012 原文列长期工程

> 新会话拿卡即开工。规则正文见 [spec.md](spec.md) 与 [contracts/orig-column.md](contracts/orig-column.md)；进度以本卡与 [execution-log.md](execution-log.md) 为准。

## 开工三件事

1. `git log --oneline -5` + `git status --short`（多会话并行，先核基点；两登记表为共享文件，注意他人未提交行）。
2. `python tools/check_terms.py | tail -3`——记下当前**告警数**（= 待补队列长度），与下卡「状态快照」对比。
3. `head -40 specs/008-terminology-campaign/results/orig-missing.txt`——取当前队列。

## 状态快照（2026-11-07 阶段 3B 中段）

| 项 | 值 |
| ---- | ---- |
| 当前阶段 | 阶段 3B（逐词联网复核），已做梵语 39 键、阿语 5 键 |
| 原文列已填 | 528 行（其中天城体 44、阿拉伯 5、希腊 39、日/韩/中/藏等阶段 2 批次） |
| 待补队列 | 142（`specs/008-.../results/orig-missing.txt`） |
| 门禁 | check_all 7/7；check_terms 硬错误 0 |

**⚠ 硬性裁定（2026-11-07，优先于本卡其余内容）**：原文必须**逐词联网复核**，原生字形须**读自来源页面**的显式配对；**禁止**用 IAST / DIN 31635 / Wylie / ISO 15919 等任何转写映射表正推或逆推。违者作废回退（见 execution-log 2026-11-07 违规批记录）。

## 可用的逐词配对源（实测有效）

* **Wiktionary 词条页**：`en.wiktionary.org/wiki/<原生文字>`，页头形如 `كَلَام • (kalām)`；巴利语词条有「Alternative scripts」表，直接给天城体（如 `vipassanā` → विपस्सना）。
* **Tsadra Commons** `commons.tsadra.org/index.php/<术语>`：表单字段「Devanagari Sanskrit Script」「In Tibetan Script」「Wylie Tibetan Transliteration」——**藏文批首选**（Wylie ↔ 藏文两向都在同页）。
* **wisdomlib 词典/词条页** `wisdomlib.org/definition/<词>`：词头即「罗马化 (天城体)」。
* **Wikipedia/Wiktionary 词头**（如 `Nāgārjuna (Sanskrit: नागार्जुन)`）。
* **不可采**：`wisdomlib.org/sanskrit/segments/...`（机械转写器页）、任何「转写对照表」页。

## 剩余 142 条分组（按语系领批）

| 组 | 条数 | 处理 | 状态 |
| ---- | ---- | ---- | ---- |
| 阿拉伯/波斯术语与人名 | ~65 | Wiktionary 阿语词条 / ar.wikipedia / EI 词条页 | 阿语已做 5（falsafa·kalām·tawḥīd·sharīʿa·qiyās） |
| 藏文 Wylie 术语与人名 | ~30 | Tsadra Commons「In Tibetan Script + Wylie」字段 | 未开始 |
| 日/韩留队（渋み·日本人論·韓元震 等） | ~20 | Wikipedia 日/韩语版词条 / Wiktionary | 未开始 |
| 梵语余量 | 12 | 同上方法 | 未开始（`Śākyaśrībhadra` 已判外源不可得） |
| 希伯来 | 1（Sefer ha-Zohar） | Wikipedia/Wiktionary 希伯来词条 | 未开始 |

## 批次队列（按序领取，领取后在此登记）

| 批次 | 阶段 | 范围 | 条数 | 状态 |
| ---- | ---- | ---- | ---- | ---- |
| B1 | 1 | 欧洲拉丁原拼写+西里尔+ω/ε | ~130 | ✅ 2026-11-07（211 行，6e5489de） |
| B2 | 1 | CJK 括注提取 | ~30 | ✅ 并入 B1（21 行） |
| B3 | 2 | 日/韩/中/希伯来（语料可证者） | ~90 | ✅ 2026-11-07（113 行，a4cd6000） |
| B4 | 3 | 希腊 39 | 39 | ✅ 2026-11-07（236cb76d） |
| B5 | 3 | 梵语 51 | 51 | 🟡 39/51（56d08558·8c869b12·5644c8eb）；余 12 |
| B6 | 3 | 阿拉伯/波斯 ~65 | ~65 | 🟡 5/65（a8ddd565） |
| B7 | 3 | 藏文 ~30 + 日韩留队 ~20 + 希伯来 1 | ~51 | ⬜ 未开始 |
| B8 | 4 | 告警清零 → 规则升硬错误 | — | 阻塞于 B5–B7 |

## 各阶段标准作业（要点，细则见 spec.md「标准作业」）

**阶段 1（机械）**
```bash
python -I script/_fill_orig_stage1.py           # 干跑：看分类与「可填」清单
python -I script/_fill_orig_stage1.py --write   # 实写（幂等，只填「—」行）
python tools/check_terms.py | tail -3           # 告警应下降
```
填前必须**人工过一遍干跑清单**：括号取形（`dictum (Abelard)` 取主形）、罗马化误判（`yì`/`hadé`/`Lüshi chunqiu` 属 CJK，须排除）。

**阶段 2（语料取证）**
1. 对每键在 `yuanwen/` 与中文词条正文检索（含去变音符、小写、词干变体）。
2. 取键邻域 ±80 字内的非拉丁 token（只取 token，不取整段）。
3. 脚本/行对照核实语义对应后填；证据写 `execution-log`：`键 → 原文 → 文件:行`。
4. 无共现证据 → 留「—」，记「留队 · 待阶段 3」。

**阶段 3（外部权威源）**
- 阿拉伯/波斯：术语在线（阿拉伯语词条）/权威工具书；不得凭转写反推字母。
- 梵/巴利天城体：权威辞书或学界标准转写映射表。
- 藏文：须专门核实 tsheg 与连写；无法核实即保留 `—` 并登记「外源不可得」。
- 希腊重音符：阶段 2 填后整批复核一次（重点：尖音符/气音符/下加点）。

**阶段 4（升级）**
- 按 contracts §6 四项条件逐条核；改 rules/03 条文 + check_terms 开关，同一提交内完成。

## 纪律

* **零编造**：说不出出处的原文一律不填；记忆推断不是证据。
* **只动第 2 列**：译法/依据/日期列不改（发现错另行立任务，不混入本工程）。
* **幂等 + 逐行身份**：按 (表, 键) 定位且只填 `—`，不做全局替换。
* **禁 heredoc 写中文**；脚本落 `script/`，`python -I` 运行。
* **提交**：只 `git add` 两登记表 + `specs/012-*` + `specs/008-*/results/orig-missing.txt`；中文一行信息注明批次与条数。

## 交接时必写

* 本卡「状态快照」的待补数与阶段；
* 本卡批次队列表的状态列（已领/完成）；
* `execution-log.md` 追加本批记录（条数、证据档位、剩余）。

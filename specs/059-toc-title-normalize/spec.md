# specs/059 — 目录条目标题体例规范化实施（甲类机械＋乙类补译，丙类裁定不归一）

- 编号：specs/059；立项日期：2026-11-25；状态：**已完成**（2026-11-25 单会话：写回 26 处→J1–J6 全过→派生面联动→判据入 ADR-0078；甲类 15＋乙类 11，丙类按用户裁定不实施）
- 承办：主会话（ADR-0034 主代理单干）
- 上位：`jian-yi-shu/mu-lu-tiaomu-ti-li-gui-fan-jian-yi-shu.md`（2026-11-25 建议书，本卡为其实施卡）、`rules/01`（SUMMARY／mu-lu-s 规则）、`rules/05`（批量改写纪律）、`rules/08` §9–12（卡钉基准、试金石、独立复算、返工归因）、ADR-0024／0041／0048／0057／0060／0062

## 1 意图复述（rules/08 §1）

用户 2026-11-25 裁定：**“与和不必强制归一化。甲乙丙全部批准，任何机械处理必须事后全量复核。”**

转述：批准 2026-11-25 建议书 §5 的甲类（机械可改 15 处）与乙类（别名行补中文连接 11 行）实施；丙类“与／和”连词**不作强制归一**（既不走案 A 也不走案 B 白名单，双轨并存为合法状态）；一切机械处理须做事后全量复核（独立复算，非自报）。

## 2 目标

1. 甲类 15 处符号层归一：U+2027→U+00B7（1）、`&ndash;`→`–`（1）、别名行“——见”前空格删（3）、“：见”→“——见”（4）、全角冒号后空格删（2）、分组行中英序归一（2）、mu-lu-s 标题 U+2013→一字线 U+2014 并补中西文空格（2）。
2. 乙类 11 行补中文连接：按“X——见Y”形态补 `——见<目标中文题>`；其中 L680 仅缺“见”字（机械插字）。
3. 事后全量复核（§5 J1–J6），凭证入 `results/`。
4. 判据回写 `rules/01`（走 ADR-0078）＋标准清单增补（GB/T 22466-2023、ISO 999:1996、《世界人名翻译大辞典》）。

## 3 非目标

- **丙类不归一**：标题内“与／和”双轨、以及 en “and”／“vs.” 的中文连词选择，一律不改（用户 2026-11-25 裁定）；不建白名单、不立机检。
- 不动条目行正文标题（甲乙类均只触及别名行／分组行／mu-lu-s 标题行，`check_mulu_s` 共有标题面零变更）。
- 不动 `en/`、`yuanwen/`、`yuanwen/SUMMARY-en.md`（ADR-0062 冻结；en 侧别名左段系上游照录面）。
- **不改别名行左侧英文段**：建议书 §5 曾疑 L2378 `Models in Science` 非上游索引式（catalog `label=models in`），经复核 ADR-0024 明文“左侧英文写目标词条完整标题”、`check_summary.alias_fragments` 口径为“与任一 baseline 标题或右侧索引名等价即放行”，判为**合规存量**，同族共 103 行，本轮不动（结案记录见 §6）。
- 不改分类归属与排序（specs/055–057 定案）、不改术语译法（specs/058 管辖）。

## 4 基准钉与约束

- 基准 HEAD：`5bc61de2d`；开工前 `sync_guard pull` 已判“本地与远端一致”，`SUMMARY.md`／`mu-lu-s.md` mtime 距开工 >1.5 h（并行会话已落定，无在途 M）。
- 行数基线（`recheck.py` 实测，`split('\\n')` 口径含尾空串）：SUMMARY 2,788、mu-lu-s 5,275（`wc -l` 2,787／5,274）；条目行 3,772（SUMMARY 1,872＋mu-lu-s 1,866＝3,738，另 34 行为并行会话 2026-11-25 新增条目）；别名行 638、分组行 182。
- 改前谓词基线（`results/before.json`）：P1=1、P2=1、P3=3、P4=4、P5=2、P6=2、P7=2、P8=11，合计 26 处。
- 写回前置门（rules/05）：脚本仅做**整行精确匹配替换**（`old_line` 唯一命中，命中 0 或 >1 即中止不写），逐行身份追踪 old→new，幂等（已应用则 changed 不含该项）。
- 目标态谓词：建议书 §5 谓词 1–7 ＋ 乙类 `缺连接=0、：见=0`。

## 5 验收判据（全部为二值可执行；事后全量复核＝用户硬要求）

| # | 判据 | 命令 | 期望 |
| ---- | ---- | ---- | ---- |
| J1 | 写回前置门通过 | `python specs/059-*/bin/apply.py` | `applied=26`、`residual=0`、无 abort |
| J2 | 幂等 | 同命令复跑 | `changed=0`（空 diff） |
| J3 | 行数守恒 | `wc -l SUMMARY.md mu-lu-s.md` | 2787／5274 不变 |
| J4 | 改动面受控 | `git diff --numstat -- SUMMARY.md mu-lu-s.md` | 仅两文件；改动行数＝26（±26），且逐行落 old→new 白名单 |
| J5 | 门禁 | `python tools/check_summary.py`、`python tools/check_mulu_s.py`、`python tools/check_all.py` | HARD ERRORS: 0／全绿 |
| J6 | **全量复扫（独立复算）** | `python -I specs/059-*/bin/recheck.py` | 七类谓词全 0 命中；与改前快照逐项对照，无新增违例、无误伤非目标行 |

- **作废条件**：①并行会话在我方窗口内改动两文件（mtime 或 diff 意外增长）→ 停手重新基点核对（R3）；②J1 出现命中≠1 的替换 → 禁止写回（残余不为 0 禁写回）；③J5 任一门禁红且非本卡引入 → 按 rules/06 竞态纪律先复跑定性；④J6 发现本卡引入的新缺陷 → `git revert` 本卡提交（一行回退）。

## 6 研判与结案记录（乙类逐行凭据）

- **680**：`* \*设计论证——目的论：上帝存在的目的论论证 …` 缺“见”字（“——目的论”应为“——见目的论”），机械插字，语义无损。
- **985**：上游 `label=Ferrier, James / href=Scottish Philosophy: in the 19th century`；同目标既有行 L271／L279 写法为「苏格兰哲学：19 世纪苏格兰哲学」，本行从同族写法（父簇：子条目），非新造译名。
- **715／1229／1808／1817／2247／2378／2516／2556／2562**：目标中文题直接取本库条目行既有译名（L1807 道德动机、L2006 人格同一性、L1816 道德实在论、L1825 道德怀疑论、L2549 结构实在论、L1770 科学模型、L1300 内部言语、L1570 子结构逻辑、L43 预先指示和替代决策），零新译名（不触发 ADR-0048 译法抉择查证义务）。
- **结案（L2378 左段）**：catalog `label="models in"` 与 SUMMARY 左段 `Models in Science` 不符一事，判为 ADR-0024 有意偏离（左侧＝目标完整标题），门禁口径亦放行；同族 103 行一并维持现状，建议书 §5 该行“须回源核对”项就此结案。
- **丙类**：不实施；建议书 §4 T2 由“应（两案呈裁）”改判为“可（语体择用，不设机检）”，已在 rules/01 新节按此措辞。

## 7 落地清单

1. `bin/apply.py`（写回）＋ `bin/recheck.py`（J6 独立复算）；凭证 `results/apply-report.json`、`results/recheck.txt`、`results/before-snapshot.txt`。
2. 写回 → J1–J6 → pathspec 提交（禁裸 commit，防并行树收编）。
3. ADR-0078 判据入 `rules/01`；rules/README 标准清单增补三行；建议书标注裁定与结案。

## 8 实施结果（2026-11-25 实测，凭证 results/）

| # | 判据 | 实测 | 结论 |
| ---- | ---- | ---- | ---- |
| J1 | 写回前置门 | `applied=26 skipped=0 abort=0` | 通过 |
| J2 | 幂等 | 复跑 `applied=0 skipped=26` | 通过（空 diff） |
| J3 | 行数守恒 | 2,787／5,274（`wc -l`） | 通过 |
| J4 | 改动面 | `git diff --numstat`：SUMMARY 24 行、mu-lu-s 2 行，共 26 行；逐行落在白名单 old→new | 通过 |
| J5 | 门禁 | `check_summary` HARD 0（除并行线在途项）、`check_mulu_s` HARD 0、`check_catalog_network --gate` G1–G5 全绿 | 通过（见 §9） |
| J6 | 独立复算 | P1–P8 全 0，`VERDICT: PASS`（`results/after.json`） | 通过 |

派生面联动（连锁必跑，否则 `catalog-net` 红）：

* `python tools/gen_en_summary.py` → `yuanwen/SUMMARY-en.md` 1 行（`&ndash;`→`–` 的 en 侧镜像；分组行序不影响 en 侧输出）。
* `python tools/check_catalog_network.py --build-mulu` → `baseline/mulu-map.json` 3 行（两处 mu-lu-s 标题＋时间戳）；随后 G1–G5 全绿。

## 9 外部红项（非本卡引入，不抢修）

实施完成时 `check_all` 唯一红项为「SUMMARY 结构审计」的 `H1 mismatch: v/vives.md`（SUMMARY 名“比韦斯”／H1 名“维夫斯”），系并行会话 5700c2b82（specs/058 vives 登记批）的提交面；`journal/v/vives.ndjson` 与 `v/vives.md` 当时在途 M，判定其正在该文件线上作业，按 rules/06 竞态纪律不抢修、不抢提交，报用户知悉。**终态**：并行会话随即把 H1 同步为“比韦斯”，`check_all` 二次复跑 17 项失败 0、全绿（首次红属在途半成品瞬态，符合“并行在途门禁假失败先复跑定性”判例）。本卡 26 处改动已随 5700c2b82 收编入库（`git show HEAD:SUMMARY.md` 特征串 4/4、`git show HEAD:mu-lu-s.md` 特征串 2/2）。

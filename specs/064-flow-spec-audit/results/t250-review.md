# T250 rv 全链证据：japanese-aesthetics

- 日期：2026-11-28
- 对象：`zh/j/japanese-aesthetics.md`
- 状态：`tr-04_checked → rv-01_checked → rv-02_checked → rv-03_checked → rv-04_checked → rv-05_checked → rv-06_checked → rv-07_checked → rv-08_checked → rv-09_checked`
- 依据：`rules/04` rv 链、ADR-0063（rv-01 三轴）、ADR-0079（rv-03–08 六轴）、ADR-0041（规范基线）

## 一、rv-01 术语与体例（三轴）

`check_terms --docs` 硬错误 0（自洽 0）；8 处“正文缺登记译法”告警按 D2→D1 逐处订正落地：

| 登记英文 | 登记译法 | 落地句 |
| ---- | ---- | ---- |
| bushidō | 武士道 | §8“武士及其生活方式（武士道，bushidō）” |
| chayoriai | 茶寄合 | §4“奢华的茶会（茶寄合，chayoriai）” |
| ikiji | 意地 | §8“勇敢的从容（意地，ikiji）” |
| sabireru | 荒废（さびれる） | §5“sabireru 意为‘荒废、变得荒凉’” |
| Charles Baudelaire | 夏尔·波德莱尔 | §8 首现 |
| Henry David Thoreau | 亨利·大卫·梭罗 | §9 首现 |
| Hideyoshi | 丰臣秀吉 | §4 首现 |
| Nishida Kitarō | 西田几多郎 | §7 首现 |

体例轴：`check_style` 0 issue；`check_pairs --gate` hard 0／out_of_scope 0（errata-apply、note-anchor 过）；勘误第二十一节 1 行承载=译注①在位；`check_prose` 0。

## 二、rv-02 全局两轴审计

- 译文轴：账本 120 段对齐 en 120 块；块类型仅第 114 段（学术工具）en 引块表↔zh 列表，属 ADR-0037 正典形态，非缺陷。
- 全局轴：H2 14/15（差 1 为译者注释末节，ADR-0065 允许）、H3 1/1；脚注定义 44/44（键集相同）、引用 8/8、图 33/33；6 件补充子文档链接全部可解析；年份集仅 zh 多 1920（en 作 1920s），无缺项。
- 密度：破折号 59 对（原文 43）逐处复核均承担插入/转折/解释；“一个”30 处均对应不定冠词或数量义；AI 套话抽查仅“首先/其次/最后/不仅/可以说”等常规连接，无空洞拔高。
- 机检：`check_math_zh` 0、`check_math` 0、`check_academic --strict` 无硬错误、`check_pairs --gate` 0、`check_style` 0。

## 三、rv-03 引文锁定

`cite_audit` 42 条（block 10／inline 32），清单 `state/axis/japanese-aesthetics.cite.json`：

| 裁定 | 条数 | 说明 |
| ---- | ---- | ---- |
| pass（ja） | 31 | 日文原著；`unavailable`／`sep-inline`，据 upstream 英文译出，不代造原文 |
| pass（en） | 5 | 英文原著；`na`／`self` |
| pass（de） | 2 | 德文原著；`unavailable`／`sep-inline`（含歌德/谢林/叔本华暗指） |
| waived | 4 | 术语级／题名片段：17 匍匐而入之处、18 荒废/变得荒凉、30 表演之优雅、32 无与伦比之魅力的花之艺（C-4c） |

anchor 全部指向 en 行；hash 42/42 守恒；`--gate` 0。

## 四、rv-04 逻辑一致性

`logic_audit` 376 散句骨架（trivial 304、logic_bearing 72）；72 条逐条裁定 `equivalent`，reviewer=trae-main。24 条算子配对候选逐条复核，均为英文 all/no/some/if 与中文语境对应或引文内词形造成的机械差（如 no two countries、all things），未发现量词强弱、否定辖域、条件方向、模态强度漂移；L-1／L-2 抽查未见命题增删与论元角色反转；`--gate` 0。

## 五、rv-05 语法

`grammar_audit` 22 条告警全为 G-19“待定形日源词”（物哀 11、幽玄 11），均系本词条主题术语用形，已在 `zh/shu-yu-biao.md` 登记且首现括注日文原文，非未定形生造词；按 G-17 术语用形与 G-19 防误判逐条裁定 waived（附 evidence）。G-1／G-5／G-7 三型 0；G-9–G-16 反欧化 0；`--gate` 0。

## 六、rv-06 语域

`register_audit` 10 节全部 R-1（说明性段落按 R-2），无 R-4／R-5 越界。唯一候选 R-d@165“是以”经核为“就是以……而动”的介词框架，非文言连词，判 false-positive。口语／方言／第二人称敬称 0；AI 腔抽查未见空洞拔高或公式化排比。`baseline/register-baseline.md` 尚未建立（全库缺口），按 `rules/02` 语体结论判与既有 done 件同档。`--gate` 0。

## 七、rv-07 计量

`measure_audit` items 0（无 SI 量值对；正文“60 厘米 × 60 厘米”“2 英尺”等中文名称照录源）；ranges 27 全篇 en dash 同形，参考文献照录段豁免；连接号统一归一体例战役（ADR-0041）未立项，不铺量改。issues 10 全为 M-4 误报（`ginkakuji2`、`ryoanji3`、`LSfathers2` 等图片文件名序号被当作“应上标”量值），逐条 false-positive。`--gate` 0。

## 八、rv-08 标点

`punct_audit` 28→0（sg-01 复核后 1 条引文内页码转 waived，见文末补记）：

- P-13 数值范围 27 处由 en dash 改为全库统一的一字线（正文生卒年、行内引证页码；书目定义照录段保留 en dash 12 处未改）。
- P-7 单句双冒号 1 处（“第二点观察是：……：茶道”）改为逗号。
- P-8／P-9／P-11／P-13／P-15／P-18／P-20 硬档 0；`check_style` 0、`check_quotes` 0、`check_prose` 0。

## 九、rv-09 体例终校

适用规范基线筛查：GB/T 15834-2011（标点）、GB/T 15835-2011（数字与计量）、CY/T 266-2023（编校质量）、GB 3100／3101（量和单位，照录源豁免）与 ADR-0041 偏离登记；未发现与项目基线冲突项。

尾序：参考文献＞学术工具＞其他网络资源＞相关词条＞脚注定义＞译者注释；H1 中英题＋作者、pubinfo 引块、编号 `N.` 均正典。

机检：`check_style` 0 issue；markdownlint-cli2 0 issue（单件 `--no-globs`）；`check_quotes` 0；`check_pairs --gate` hard 0／out_of_scope 0；`check_academic --strict` 无硬错误；`check_math_zh --strict` 硬 0；`check_terms` 硬 0；`check_images` 悬空 0；`check_prose` 0。

结构：341 行／13,513 汉字／120 段账本／44 脚注定义（唯一键 44）／8 引用／33 图／H2 15（含译者注释）／H3 1。

结论：rv 全链通过，状态 `rv-09_checked`；下一步 T251 sg 链。

## 十、sg-01 复核补记（2026-11-28）

- rv-08 将 §5 Tanizaki 引文内的页码 `11–12` 也归一为一字线，触动了 q1 引文 hash。sg-01 已恢复 en dash，`P-13@107` 转 waived（引文内页码照录）；rv-08 终态为 28→1 waived。
- §3 `See section 7, below, on cutting` 的“切”专节实为 §9，属上游第二处同页自相矛盾；已改“第 9 节”，入勘误第二十一节第二行。译者注释重排为① §3、② Acknowledgments。


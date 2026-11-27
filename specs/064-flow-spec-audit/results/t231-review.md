# T231 tr-02 全量：newton-principia

- 日期：2026-11-27
- 对象：`zh/n/newton-principia.md`（全件入库）；`tasks/n/newton-principia.ledger.yaml`（255 段）
- 源文：`en/n/newton-principia.md`（导论＋§1–§10＋尾节＋96 脚注定义）
- 版本钉：`pubinfo_date: Dec 20, 2007`；`archive_edition: Winter 2024`；`sha256: 05a4a2b2…6f38`
- 依据：`results/t157-decomposition.md` T231；`rules/04`、`rules/02`、`rules/03`

## 一、批次执行

| 批 | 范围 | 源字符 | 要点 |
| ---- | ---- | ---- | ---- |
| A | §2–§4 | 34,117 | 哥白尼附释三段、三个版本、定义与绝对空间 |
| B | §5–§6 | 34,301 | 运动定律、图 1（引块内）、图 2（引块内）、`quam proxime` |
| C | §7–§8 | 38,157 | 第二卷阻力与涡旋、第三卷引力推导与月球不等项、图 3（行内同行图注） |
| D | §9–§10＋尾节 | 20,276 | 十一项成就、方法论、参考文献／学术工具／其他网络资源／相关词条 |
| E | Notes | 24,928 | 59 条编号注逐条译；37 条书目键照录英文 |

- 全部五批逐段初译后统一做译后编辑（PE）：术语统一、长句断句、引文出处与图注格式统一、书目键保持原文。
- 样章（T230）13 段并入，账本合计 **255 段**，与 en 块数一一对应（257 块含 H1／pubinfo 等非账本块）。

## 二、规模与结构守恒

| 项 | en | zh | 判定 |
| ---- | ---- | ---- | ---- |
| 行数 | 539 | 537 | 差异为 pubinfo 与末尾空行，正文块数一致 |
| 汉字 | — | 35,900（目标 36,082，−0.5%） | 达标 |
| 块数（含 H1／pubinfo） | 257 | 257 | 一致 |
| 账本段 | 255 | 255 | 一致 |
| 脚注定义 | 96（59 编号注＋37 书目键） | 96 | 一致 |
| 脚注引用 | 62（59 编号注＋2 书目键＋1 字面 `[^key]`） | 62 | 一致 |
| 图片 | 3 | 3 | 一致；路径 `../../assets/newton-principia/figN.jpg` |
| 引块 | 23 | 23 | 一致 |
| 链接 | 12 | 12 | 一致 |
| H2／H3 | 15／2 | 15／2 | 一致 |

- 图 1、图 2 保留在引块内（含图注）；图 3 保留“行内图片＋同行图注”形态。
- 学术工具 5 行源表按既有体例改为 4 项列表（action／axiom-choice 同例），链接目标与文字一一对应。
- 引文出处 `[**P**, …]` 等按中文标点体例作 `（**P**, …）`，以过 `check_style` bold-spacing 门。

## 三、术语与人名

- 本件新增登记 17 条：T230 12 条（absolute motion、attraction、clockwork universe、contact mechanism、forces of nature、impulse、law of gravity、laws of motion、lunar apogee、mean motion、orbital mechanics、physical geodesy）＋T231 5 条（finite-difference method、line of apsides、Newtonian fluid、perfect fluid、rigid body）。
- 复用既有登记：tenacity 黏着性、viscosity 黏滞性、variation (lunar) 二均差、nutation 章动、line of nodes 交点线、apsidal angle 拱点角、latus rectum 通径、cycloidal／hypocycloidal pendulum 摆线摆／内摆线摆、conical pendulum 圆锥摆、impressed force 外加力、motive force 运动的力、quantity of motion 运动量、occult qualities 隐秘的质、impetus 冲力、celestial mechanics 天体力学、point-mass 质点等。
- 人名：Boulliau、Streete、Wing、Mercator、Horrocks、Halley、Hooke、Cassini、Ptolemy、Copernicus、Tycho、Leibniz、Cotes、Le Seur、Jacquier、Clairaut、d'Alembert、Euler、Bradley、Gassendi、Wallis、Hermann、Bernoulli、Duhem、Mach、Whewell 均按 `zh/ren-ming-biao.md` 既有行；Mersenne 作“马林·梅森”。

## 四、机检

| 检查 | 结果 |
| ---- | ---- |
| `check_style --docs` | 0 issue |
| `check_quotes --docs` | 0 处违例 |
| `check_math_zh --docs` | 0 条，硬错误 0 |
| `check_terms --docs` | 硬错误 0（“正文缺登记译法”告警留待 rv-01 逐条处理） |
| `check_academic --docs --strict` | 学术规范无硬错误（在途豁免 1） |
| `check_pairs --gate` | hard 0；out_of_scope 0 |

## 五、勘误（第十九节）

| 位置 | 上游原文 | 定性 | 参考读法 |
| ---- | ---- | ---- | ---- |
| §2（en L36） | `guest it to be Elliptical` | ①排印手误 | `guessed it to be Elliptical` |
| note-3（en L350） | `maris nostril` | ①排印手误（拉丁文） | `maris nostri` |
| note-9（en L362） | `Rudolphime Tables` | ①排印手误 | `Rudolphine Tables` |
| note-26（en L396） | `35, 2986` | ①排印手误（年份） | `35, 1986` |
| smith-2002（en L522） | `pp. 31-70..` | ①纯排版重复句点 | `pp. 31-70.` |

均为纯排版类，无需译者注释；中文书目键照录。

## 六、结论与移交

1. 全文 255 块与 en 一一对应；96 脚注定义、62 引用、3 图、23 引块、12 链接、15 H2／2 H3 守恒。
2. 35,900 汉字，达 T157 目标（36,082）的 99.5%。
3. `tr-02` 已推进至 `tr-02_checked`；可进入 T232（tr-03／tr-04）。
4. 移交：T232 一校逐节核销时优先复核长引文（哥白尼附释、总释、惠更斯与莱布尼茨引文）与 59 条编号注；rv-01 处理“正文缺登记译法”告警（Cohen-Whitman、人名简称等）。

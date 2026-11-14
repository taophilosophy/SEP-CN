# s2.4/s2.5 前置阶段试点实测评估报告（2026-11-15）

**试点面**（用户裁定：公式最多 5 件＋完全随机 10 件，均出自 s2.5_checked 回退池 198 件；抽样种子 20261115，`pilot-sample.json`）：

* **公式 Top-5**：logic-provability（358）、intuitionism（294）、epsilon-calculus（227）、boolalg-math（173）、diodorus-cronus（171）——公式计数口径＝zh 译文 `$$` 块＋行内 `$…$`（代码块豁免）。
* **随机 10**：august-rehberg、bayle、delmedigo、ehrenfels、intensional-trans-verbs、locke-on-medicine、obligationes、quantum-bayesian、redistribution、ricoeur。

## 一、机检批跑结果（六器×15 件）

| 检查器 | 结果 | 说明 |
| ---- | ---- | ---- |
| check_prose（含三则新规则） | **15 件全 0 告警** | 新规则（时态词/并列连词/成功地）零误报——好信号 |
| check_math_zh --strict | **15 件全 0 硬错误** | 358 公式重镇 strict 过——公式体例成熟 |
| check_terms --docs | **15 件全过** | 登记册自洽 |
| check_academic --strict | **15 件全过** | 学术规范 |
| check_style | **1 件重灾：intensional-trans-verbs 150 处**（bold 边界 130＋星标损坏 8＋引号序 2＋italic-cjk 2＋其它），其余 14 件 0 | **check_style 不在 check_all 十项内**——历史 done 件带违例潜伏，回炉才现形（流程发现 F-A） |
| check_tables_images（全库口径） | 15 处 table-en-prose，**试点 0 命中** | 工具无单文件模式（发现 F-M4，批处理口径已修正） |

## 二、实测修复（intensional-trans-verbs，150→0）

按 ADR-0019 源标签裁定逐处修复（en/intensional-trans-verbs/index.html 对表）：

* 星标损坏 4 类：`** x(y)**或** y(x)**`→`**x(y)** 或 **y(x)**`（源 `<strong>`）；`（iii）** xy*`→`（iii）*xy*`（源 `<em>`）；`***内涵***`→`**内涵** `（源 `<em>`＋中文禁斜体）；`**那***件羊毛毛衣`→`**那** 件羊毛毛衣`（源 `<em>that</em>` 加粗、woollen sweater 源无标签去斜体）。
* bold 边界空格 130 处（`**X**汉字`→空格，围栏/表格/照录节豁免）。
* 引号-西文邻接 3 处（`NP‘the…`→`NP ‘the…`，rules/02 引号空格条款）。
* 修后 check_style 0；mathzh/terms/acad 复跑 0。

## 三、密度统计与「一个」抽判（rules/04 s2.5 全局项实测）

* 破折号 7–105/件（ehrenfels 101、locke-on-medicine 105 为高位）；AI 词 0–12（ricoeur 12 待走查）；「一个」12–**249**/件（intensional-trans-verbs 249 最高）。
* **「一个」抽判**（intensional 249 处抽 10，seed 20261115）：强违规 4／边缘 2／保留 4——**违规率约 40%**，外推该词条约 100 个判定点。证实「一个」节制的偿还需求巨大且**必须逐例语义判定、不可机改**（ADR-0033 口径）——028 滚动批次的单件工作量主项。

## 四、s2.4 术语对照实测（工具两轮迭代）

* v1 直扫：表面「未登记率 ~95%」——两层噪音淹没（类型论记号 `(every(sweater))`＋照录书刊名）。
* v2（沉淀 `bin/s24-register-diff.py`）：记号过滤＋照录节豁免后，**真实未登记 4–12/件且集中于书刊名**（照录区不登记，ADR-0011）——真实待登记术语面小，s2.4 可执行。
* 附带真发现：`*$\omega$-一致的*`、`*PSPACE-完全的*` 类**中文/数学混合斜体**＝italic-cjk 违例候选（rules/02），转 s2.5/s3 处置清单。

## 五、流程缺陷与优化清单（试点核心产出）

| # | 发现 | 优化动作 | 状态 |
| ---- | ---- | ---- | ---- |
| O1 | check_style 不在 check_all，历史违例潜伏（150 处实证） | 建议 s25 门加挂 check_style（随 028 增项批次） | 待批 |
| O2 | cjk-spacing 不覆盖 引号↔西文 邻接（NP‘the 漏检且诱发引号误报） | check_style 扩展候选（rules/05 登记） | 待批 |
| O3 | 词内撇号遮蔽对 `P‘t`（NP 引导语）误报 | 以空格写法规避（本次）；checker 改进候选 | 登记候选 |
| O4 | check_tables_images 无单文件模式 | 批处理口径＝全库跑后按 slug 过滤 | 已修正 |
| O5 | s2.4 自动对照需双层过滤（记号＋照录节） | 工具沉淀 `bin/s24-register-diff.py` | 已完成 |
| O6 | 回退件 s2.5 凭证无步可记（revert 落位即 s2.5_checked） | 凭证随 s3 步 evidence 引用 028 凭证件 | 已实践 |
| O7 | 「一个」偿还工作量基准：约 40% 违规率×全库频次 | 028 滚动批次按字头推进、逐例判定；不做机改 | 已量化 |

## 六、诚实边界

* 本试点＝机检网全量＋增项实测＋1 件深度修复；**15 件的逐段三向人审未完成**（028 滚动主项），全部保留 s2.5_checked，未越权推进 s3。
* 试点凭证：pilot-sample.json、pilot-machines.json、pilot-tables-full.txt、pilot-density-terms.json、本报告。

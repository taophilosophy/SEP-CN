# 053 — EN 语料模板审计与勘误装配线

**版本** v1.4 ｜ **状态** P0 已执行、验收框架与形式化证明已登记（§7–§9）、P1–P4 待批批次 ｜ **日期** 2026-11-19 ｜ **权威** 用户“批准053”（四阶段方案审定）＋“三族分目、目录结构执行国标等”（ADR-0076）＋验收目标“英语 md 逆向装配回原 HTML、确保可重现性”及修正裁定“残差可在逆装配侧打补丁吸收，sha 一致可实现”（§7）＋编位裁定“纳入 B 系列、视为 B3”（§7）＋“复核后全面批准、具体方案进行形式化证明补遗、联网查询成熟方案”（§9） ｜ **承接** specs/047（B2，已批待实施）、ADR-0070 建议③④⑤、specs/044 B0–B3 保真基线族

## 0. 方向声明（rules/08）

- **目标**：①三族审计产物分目（模板契约 T／补丁 P／勘误装配 E，ADR-0076）；②实施 specs/047 结构反向核验（堵 I2 自证盲区）；③B0 判据增强五项＋例外登记册落地；④新发现定性分流续批；⑤译注挂载批次＋挂载台账（勘误 ID→词条→圈号锚点）。
- **非目标**：不翻译（ADR-0072 边界）、不改 en/ 任何字节（ADR-0062）、不打破规则所有权（判据增强归 specs/044、白名单登记口径归 specs/039、判定权三权分立 ADR-0063）、不引入 LaTeX 中转层（ADR-0063 §7 否决）。
- **验收判据**：①047 判定器对负向样本（构造丢一节/丢一脚注 md）必报；②全量跑账本闭合（new 缺陷皆有四出口之一去向）；③每条新发现登记出口，无“机检全绿＝已验证”表述（ADR-0070）；④译注台账建立后勘误表每件“译注队列”可对应词条内实际圈号锚点，errata-apply 轴全绿；⑤check_all 全绿、提交推送、`origin/main..main` 为空；⑥逆向装配 B3 判据（B3.1 往返不动点全量绿、B3.2 装配残差池 sha 全等 1,872/1,872、规则闭合率＋残差分型、补丁可逆性单测，§7）。

## 1. P0 三族分目（已完成，2026-11-19）

目录形态＝**baseline/ 三类目平铺**（ADR-0076，用户三方案预览选定）：

```
baseline/
├─ en-template/     # T：template-contract.md（正典）＋anomalies.json（空册）＋README
├─ en-patches/      # P：原位不动（三律＋命中计数硬校验不变）
└─ en-errata/       # E：en-errata.md（自 specs/001 results 收编）＋divergences.json（自 baseline 根收编）＋README；note-anchors.json（P4 建账）
```

标准依据（组合推导，建书 2026-11-17 结论＋2026-11-19 条款回核）：**无国标直接规定仓库目录结构**；GB/T 26162-2021（等同 ISO 15489-1:2016）分类方案按职能分 T/P/E 三类目；DA/T 22-2015 §3.2 整理五步（组件＝一补丁一文件/一账一文件、分类＝三职能类目、排列＝节序、编号＝P-00N 档号、编目＝README 卷内目录）＋§5.4.1 档号五原则；GB/T 18894-2016 规范存储结构与元数据关联（layout.json 七问字段）；IEEE 828 受控库 vs 工作区分界（机检工作产物留 specs/*/results/）。

已修复引用面：代码常量 2（`check_pairs.ERRATA_PATH`、`divergence.DIV_PATH`）＋docstring 4（fetch_entry/compare/baseline_audit/en_source_audit）＋活文档（AGENTS.md、rules/README 判例＋标准清单、rules/04、rules/06、specs/001 contracts/cli.md、specs/036、specs/001 spec.md 历史指针）。补丁文件头与 INDEX 的 `source: en-errata.md §N` 为相对节号引用，迁移后仍有效，不动（补丁 sha 钉在 INDEX）。

## 2. P1 结构反向核验（实施 specs/047，判官只读）——B2 已实施（2026-11-19）

- **已完成**：`specs/047-structural-reverse-check/bin/verify_structure.py`（v1.6）五维判定器＋全库首跑（1,872 件＝1,706 过／166 候选）＋负向 selftest 3/3＋补丁可逆性单测（A6，tools/tests/test_en_patch_reverse.py）。候选族分解与 W1–W6 登记见 047 execution-log（figures 64 真丢文候选、logical-constants −27 账差等）。
- **B3.1 已实施（2026-11-19）**：`bin/reassemble.py`（R 装配器，同源求值闭环）＋试金石 15 件 14 过＋全库首跑 **1,240 不动点／632 残差（规则闭合率 66.2%）**＋负向 selftest 绿。残差族与 W7–W12 登记见 execution-log.md（最大族＝文献分节作者键重建 W8 ≈396 件）。
- **待续（B3.2）**：残差池 `baseline/en-template/assembly-patches/`（一补丁一文件＋INDEX＋命中计数硬校验＋冻结）→ `unpatch(R(md))⊕pool ≡ H0` sha 全等验收线。
- 边界：与 ADR-0063 §7 LaTeX 否决不冲突（stdlib `html.parser`＋自有 md 解析，无派生层）。

## 3. P2 B0 判据增强＋例外登记册（归属 specs/044 后续，specs/053 消费）

ADR-0070 建议③五项：节号连续性、pubinfo↔archinfo 交叉、math_delim 位置配对（非仅计数）、孤立可疑字符（悬空 `\)`/`\[`/`\` 残迹）、引用闭包接入 en_integrity。
例外登记册＝`baseline/en-template/anomalies.json`（空册已建）：B0 增强后新报上游原生变异逐条人审定性入册（upstream-native/judged-ok/exempt），登记三字段（谁审/何时/审什么）；已知变异类清单见 `template-contract.md` §9。

## 4. P3 定性分流续批

新发现逐条四出口：文字层→勘误表续批＋`divergence.py register`（机器账）；格式层→补丁池（C1–C4 全过）；转换器缺陷→改 `tools/yuanwen.py` 全量重转（禁只改产物）；上游原生→anomalies.json 登记。预期产出校正：B0 全量已闭合（new=0），新发现主要来自 P1 结构轴与 P2 判据增强；**勘误续批为主、补丁增长为辅**（044 实测：模板失败几乎全是文字层）。

## 5. P4 译注挂载批次＋台账

- 对受勘误影响的已译词条（有正文面）按 ADR-0065 圈号锚点挂译注；建 `baseline/en-errata/note-anchors.json` 台账：勘误 ID→slug→圈号序号→凭证行。
- errata-apply 机检收口（check_pairs 体例轴）；勘误表每件“译注队列”字样销账。
- 未来词条由 s2.4 勘误轴自然承载（判据已接线），台账只管存量挂载状态。

## 6. 边界与并行

- 术语轴（specs/008/050）与进度主战场不在本 spec；与并行会话共树作业遵守逐文件 staging 纪律。
- 批次开工立卡钉基准、列作废条件；新手段先小样本试金石；自报完成须独立复算（rules/08 §9–12）。

## 7. 验收框架：逆向装配与 sha 一致性结论（用户 2026-11-19 验收目标）

**装配链定义**：`H0`＝原始网页钉（`en/<slug>/index.html`）；`H1`＝H0⊕补丁（转换输入视图）；`md`＝`C(H1)`（`tools/yuanwen.py` 确定性转换）；`R`＝**逆向装配器**（md⊕模板骨架→规范化 HTML，按 `baseline/en-template/template-contract.md` §6 映射逆写）；`Ĥ1`＝R(md)；`unpatch`＝补丁逆向（replace→find 逐条，命中计数逆校验）；`H0'`＝unpatch(R(md))⊕**装配残差池**。

**sha 一致性结论（v1.2 修正，登记用户裁定＋实证普查）**：

- **正向可重现性已成立**：钉→md 重放字节级确定（I2 全库免抖动重转零异常）——零信任要求的可重现性主形态。
- **反向 sha 全等可实现（修正 v1.1 的“不可达”结论）**：丢失面是**确定性的**，可由“模板骨架生成＋全局规则＋每件装配残差补丁池”三层吸收——架构与正向（钉＋en-patches）镜像对称。实证普查（1,872 件正文区间，只读）：骨架区（head/nav/footer）由生成器复现，非残差；正文注释 10,538 条全件皆有，主体为系统模板件（DO NOT MODIFY 行、Entry Contents、sep-man-icon 图标——规则可推导），真历史残差少数（frege-logic 数学记号注释 166 条为最大件）；正文实体 1,575,636 处（均值 ~842，单件最高 4,776）且**件内编码策略一致**（mereology/pufendorf 实测零字面弯引号全实体），可压成每件编码策略参数而非逐处 hunk；正文 img 8,969（系统图标＋真实图）。残差面＝每件策略参数＋结构怪癖（锚点分布 81.3%、属性形态）＋少数异类——补丁池小而结构化，比逐 hunk diff 小数个量级。
- **证据语义两分（关键裁定，防验收语义滑坡）**：
  - 池**冻结后**：`H0' ≡ H0` 全量 sha 相等＝**反向漂移检测器**，强度与 I2 对称（md 手改／转换器变更／补丁漂移任一显形）——这是验收线（B3.2）。
  - 池**即答案**：池内容源自 H0 差集，故 sha 相等**不构成**转换器“最初无损”的独立证据（用答案构造输出＝oracle 不可写）——转换器正确性由 B3.1 不动点＋B2 结构树〔047〕＋规则闭合率承载。两层互证、互不冒充。

**判据编位（v1.3，用户裁定“纳入 B 系列、视为 B3”；原 R1–R4 编号撤销——与状态机三审 R1–R3 撞号）**：

判据族＝specs/044 保真基线 B 系列（§1.3）：**B0 形式可解析 → B1 词元等值 → B2 结构等值〔specs/047〕→ B3 字节重建（本线）**，逆向保真强度单调递增。specs/043 的 B1–B3 为权责证明局部引理，另属命名域，引用写全称。

| 判据 | 定义 | 性质 |
| ---- | ---- | ---- |
| **B3.1 往返不动点（转换器正确性主判据）** | `C(Ĥ1) ≡ md` 字节级（＝I2 以 R(md) 代 en） | 全量机检；文本层丢失必显形 |
| **B3.2 装配全等（验收线）** | `unpatch(R(md))⊕pool ≡ H0` 全量 1,872/1,872；池＝`baseline/en-template/assembly-patches/`（一补丁一文件＋INDEX 生成物＋命中计数硬校验＋冻结，en-patches 同律） | 全量机检；语义＝反向漂移检测器＋灾难恢复重建资产 |
| 规则闭合率＋残差分型（建设期统计面，非谓词） | 固定规则集（模板骨架＋归一规则）下 sha 相等件数＝真验收指标；失败件 hunk 分型（实体策略／锚点分布／属性形态／历史注释／异类），异类逐条人审→anomalies.json 或转换器缺陷 | 机检＋人审分型（建池批次产物） |
| 补丁可逆性单测（池正本性质，非谓词） | 逐条补丁 `unpatch∘patch = id` 于上下文 fixture；逆向命中计数==expect | specs/039 工具族单测 |

**B3(s) ⟺ B3.1(s) ∧ B3.2(s)**（单件谓词合取，与 B0/B1 同构；定义登记于 specs/044 §1.3）。与既有判据的互补：I2 抓“未手改”（自证）、I3 抓词元多重集、B2 抓**结构层**、B3.1 抓**文本层**、B3.2 抓**全链漂移**（正反双向对称）。B3.1 与 B2 归 P1 批次（与 047 同批实现，共用 parser 契约）；B3.2 建池批次（普查→策略参数化→冻结）紧随 P1。

## 8. 全流程逆向验证总账（环节 × 逆向判据 × 现状）

| 环节 | 正向产物 | 逆向验证判据 | 现状 |
| ---- | ---- | ---- | ---- |
| 抓取/钉 | live → en/ 钉 | 钉重放三层口径（钉／抓取时／今日线上，重跑 drift_scan；实抓复证先例 bioethics-moral-reasoning） | 已有；季度重放制度化待登记 |
| 补丁池 | H0 → H1 | C2 准入（剥空白/剥标签 find≡replace）＋补丁可逆性单测 | C2/C4 已机检；单测缺 |
| 转换 | C(H1)=md | I2 重放等值、I3 词元流、B2 结构树〔047〕、B3.1 往返不动点 | I2/I3 已机检；B2/B3.1＝P1 |
| 中文译文 | zh md | 段落账本 parity 守恒门、check_pairs 七则 | 已机检（haecceitism/hamann 即判例） |
| 勘误承载 | errata→译注 | note-anchors 台账双向闭合（每勘误有落点、每锚点有勘误源） | P4 验收 |
| 术语 | 登记→正文落地 | check_terms 双向互查（登记必落地、落地必有登记） | 已机检 |
| 结构/站点 | SUMMARY→站点 | SUMMARY↔H1↔mu-lu-s 三向、yuanwen↔zh 镜像逐字符、render-audit CDP 探针 | 已机检 |
| 账务 | journal↔实际 | 账实不变量严格档、backfill witness↔批次账 | 已入 GATES |
| PDF（specs/035） | md → PDF | pdftotext 抽回词元流比对 md | 缺（低成本可选） |

## 9. 形式化证明补遗（B2/B3，v1.4，2026-11-19）

**性质**：续 specs/044 §2 公理族编号（A1–A3、T1–T4 已立）；本节只增补逆向族对象，不自造理论（§9.5 成熟方案对照）。

### 9.1 符号增补

- `Θ`：装配上下文＝模板骨架生成器＋全局归一规则集（固定，代码化于判官实现）。
- `R : md × Θ → Ĥ1`：逆向装配器（按 `baseline/en-template/template-contract.md` §6 映射逆写）。
- `P_s`：词条 s 的装配残差池（冻结集，每条补丁带准入谓词与命中计数）。
- `H0'(s) ≜ unpatch(R(md(s))) ⊕ P_s`。
- `τ_md, τ_h`：结构树（五维：分节序列／脚注引用↔定义配对序／图·表·公式块文档序／列表层级／引用条目数）。
- `token(·)`：词元流；`=_wl`：转换器白名单内的相等。

### 9.2 公理增补（续 A1–A3）

- **A4（装配确定性）**：`R` 是纯函数——同 md 同 Θ 必得同一 Ĥ1。
- **A5（池冻结与准入）**：建池批次完成后 `P_s` 只读；每条补丁须过**残差面准入谓词**——只含非文字层残差（实体编码策略／模板骨架／属性与锚点形态／HTML 注释），**正文文字层禁入**；命中计数硬校验，失配即硬失败（A2 同构；补丁 inverse 公理 `unpatch∘patch = id` 于上下文 fixture，单测钉死——Darcs patch theory 的 inverse，见 §9.5）。
- **L1（转换器词元守恒，经验引理）**：`token(md) =_wl tokens(H1 文本流)`——全库 I3 机检绿为凭证（specs/039 深档 47 件已逐件定性入白名单）。

### 9.3 判据形式定义

- `B2(s) ⟺ τ_md(s) ≡ τ_h(s)`（逐维相等；判官 specs/047 bin，判官只读）。
- `B3(s) ⟺ B3.1(s) ∧ B3.2(s)`：
  - **B3.1**：`C(R(md(s))) == md(s)`（字节级）；
  - **B3.2**：`sha256(H0'(s)) == sha256(H0(s))`。

### 9.4 定理增补（续 T1–T4）

**T5（B2 可判定）**：五维各为有限序列／多重集比较，`O(|md| + |H1|)`；树形维度可用有序树编辑距离（Zhang–Shasha 1989）量化差异（O(m²n²)，相似树近线性变体 RTED 存在）。

**T6（漂移覆盖完备性）**：A5＋冻结之下，四类漂移各有专属机检、检测面互异、并集覆盖全部漂移类：

| 漂移类 | 检测者 | 机理 |
| ---- | ---- | ---- |
| md 文字层手改 | B3.2（链路）＋I2（账面）双保险 | 池准入禁文字层（A5）⟹ 冻结池不含该文字 ⟹ 重建缺句 ⟹ sha 红；账册被重登时链路仍拦 |
| md 非文字层改动 | I2（钉账） | 池准入允许吸收 ⟹ B3.2 可能仍绿，由账面 pin 兜底（T7 衰减面实例） |
| H0 漂移 | divergence verify | sha 原始钉（ADR-0045，A3） |
| 池漂移 | 命中计数硬校验 | A5＋INDEX 生成物 |

证明：各行“机理”列即构造性论证；互异性由准入谓词的层位划分保证（文字层／非文字层／原始字节／池本体）。∎

**T7（验证力单调定理）**：B3.2 的验证强度是 `|P_s|` 的单调递减函数；`|P_s| = 0` 时退化为纯规则重建（最强验证）；`P_s` 承载全部丢失信息时验证力归零（同义反复）。故**规则闭合率＝B3.2 证据力的量化指标**，建池目标＝池最小化。
证明：B3.2 的证书内容＝“md 与 H0 的差异不超出 Θ∪P_s 所承载者”。`P_s` 增大 ⟹ 被假设而非被验证的信息增多 ⟹ 证书信息量单调下降；`P_s` 覆盖全部差异时 `(md, Θ, P_s)` 信息等价于 `H0`，等式成为构造性重言。∎（oracle 不可写的量化形态）

**T8（边界）**：Θ 的模板变异覆盖面不可自证（T3 同构）；B3 重建完备性受 `Θ ∪ P_s` 覆盖面限制；失败件走对账律四态（044 §6），`new` 类逐条四出口分流。

**对偶映射（理论定位）**：`(C, R)` 构成**收缩对**（retraction）：`C∘R = id_md`（B3.1）即双向变换 lens 的 **PutGet 律**（Foster–Greenwald–Moore–Pierce–Schmitt, TOPLAS 2007）——C 是有损 get，R 是其右逆；`B3.2` 是带**补集存储**（残差池）的 **GetPut 律**字节级实例——纯 lens 的 GetPut（`R(C(h)) = h`）因 C 有损而不成立，池恰好补齐 get 丢失的补集。此定位把本方案安放进已建立的 bx 理论，不自造公理。

### 9.5 成熟方案对照（联网调研 2026-11-19，全部实名可溯）

| 本方案构件 | 成熟方案 | 对应概念／律 |
| ---- | ---- | ---- |
| B3.1 `C∘R=id_md` | 双向变换 lens 理论（TOPLAS 2007 well-behaved lenses） | PutGet 律；收缩对 |
| `(R, P_s, unpatch)` 三元重建 | Darcs patch theory（Jacobson 逆半群形式化；Angiuli–Harper–Wilson HoTT 形式化） | 补丁 inverse＋commutation（`P_s ⊥ pats` 正交特例） |
| 逐件全量机检＋判官只读 | translation validation（Pnueli–Zuck 1998 起；Tristan–Leroy POPL 2008 验证验证器本身） | 验证每次运行而非翻译器整体；判官自身可证伪 |
| 钉＋INDEX＋池冻结 | OAIS fixity（ISO 14721／16363）＋BagIt（RFC 8493 complete-bag） | manifest 校验＝命中计数硬校验；sha 全等清单＝fixity 账 |
| R2 残差分型 | 有序树编辑距离（Zhang–Shasha 1989；RTED 后续） | hunk 最小编辑分类 |
| 负向证伪（verify_b0b1 `--selftest` 先例） | round-trip property testing（QuickCheck 家族 `decode∘encode=id`） | 最小反例收缩 |

### 9.6 与已登记档案标准的衔接

B3.2 的 sha 全等清单即 OAIS fixity 账的实现形态；与 ADR-0076 已登记的 GB/T 18894-2016（规范存储结构与元数据关联）、GB/T 26162-2021（分类方案）同族衔接。BagIt／RFC 8493 是 manifest 校验的成熟机制层参照——本项目以 en-patches／assembly-patches 的 INDEX＋命中计数承载同语义，**不引入 BagIt 文件格式本身**。

### 9.7 落点与负向证伪

- 判官：`specs/047.../bin/verify_structure.py`（B2）、specs/053 装配链（B3.1/B3.2）——P1／建池批次实现。
- 负向证伪（全部必报）：B2 构造丢一节／丢一脚注 md；B3.1 篡改 md 任意一字节；B3.2 动池任一条或动 md；补丁可逆 fixture 篡改上下文。
- 凭证产物：`results/structure-scan.json`、`results/assembly-diff-census.json`、sha 全等清单（1,872 行）。

## 10. B3.2 实施记（2026-11-19，ADR-0077）

**装配链**（四件套，全部落地并被本记的实测数字驱动）：

| 件 | 位置 | 语义 |
| ---- | ---- | ---- |
| 骨架模板 | `baseline/en-template/skeleton/` | 19 件冻结模板（headA 1／headmid 1／headrest 2／pre 5／postrest 10），槽位 `@S@`（slug）、`@CR@`（版权块）、`@SY@`（站点年） |
| 版式账 | `baseline/en-template/page-layout.json` | 逐词条字段（标题／作者／日期／版权年／作者主页 URL／邮箱）＋三处时代号 |
| 结构账 | `baseline/en-template/article-ledger.json` | hids／bib_seq／bib_groups／bib_indices／bib_ids／bib_tree／rel_links／acad_icons／tables／links／entities／greek／toc_block／wrap_width |
| 装配补集池 | `baseline/en-template/assembly-patches/<slug>.json` | 分段模型 m／u／r 三类补丁＋P1/P2/P3 硬谓词（`assembly_pool.py` v4） |

**实测（同轮，`results/page-scan.json`）**：

- **chrome 层：1,873／1,873 逐字节闭合**（head＋meta＋body 前导＋页脚＋版权块含邮箱混淆规则，零补集）。这是纯规则结果，证据力最强的一档。
- **页面级：规则 0／池 616（32.9%）／缺口 1,257**；池体积 3.88 MB／页 236 MB＝**1.64%**（T7 口径：规则闭合率约 98.4% 的字节由规则承载）。
- B3.1 未受影响：试金石 14／15（bayes-theorem 为既有残差）。

**缺口族（首差上下文归类，1,257 件）**：段落行内（`p`）约 58%、表格（`table`）约 10%、列表（`ul`，含嵌套）约 12%、引块 4%、定义列表（`dl`）3%、文献区小节标题错位（adorno 判例：H0 的 `h4` 小节题在 md 中被并入其他层）等。共同根因是 **C 转换层的结构改写**（嵌套列表→文献定义行、表格 thead/tbody 与空单元、松散列表 `<li><p>`、文献区小节题层级），非 B3.2 判定器缺陷。

**已固化的规则（本轮，均以判例驱动）**：星号开星放宽为“左紧且右非字母数字”（Düring 判例）；脚注引用回写 `<sup>[<a href="notes.html#note-N">N</a>]</sup>`（站点规范形）；外链补 `target="other"`（21,345:1,440 实测）；链接文字允许一级方括号（书目 `[X 1997 [2016] …]` 形）；参考文献区散文与 h3/h4 小节题原位发（18thGerman 判例）；`&nbsp;` 计入空白层；同形希腊宏按件出现序账（phi／varphi）。

**口径**：缺口件不入池（A5 残差面谓词拒绝文字层差异），保持红并在本记与 execution-log 逐族登记；池与账为冻结派生件，规则迭代后旧池显“陈旧”即重抽。

## 10.1 B3.2 第二批实施记（2026-11-20，区间补丁模型，续“必须100%闭合”）

**引擎升级**：对齐域从“u 单元键序列”改为 **raw 段键 difflib＋块内 ukey 流贪心合并**——段落分合、松散列表 `<li><p>`、`dl`、引块内 `p` 等边界错位不再整块拒录，块内文字键流（ukey 拼接）相等即生成一个区间 `u` 补丁（文字全部取自装配侧流、布局照目标重建，A5 谓词的区间形态）。补丁应用统一为**字符偏移降序**（旧实现 m/u 用字符偏移、r 用段索引混用，且 r 分支取不存在的 `p["n"]` 键）；空白与实体形态差由 `layout_items` 折进 mk/tx（`&thinsp;` 与空格按排版空白等值，A5 允许）；`--build` 写盘前先就地应用补丁核对逐字节再生（自洽门）。

**R／账新增规则（判例驱动）**：图片逆写（`![alt](../assets/…)` → `<img src alt />`，alt 占位隔离）；词内开星（`P*hilosophy of History and Action*`）与 `(*)` 记号星不开星／`[*‘Uyūn* 604f]` 照常开星；内部链接**文档序游标**定位（旧 nth 语义遇嵌套锚文重叠插入）；脚注引用形账 `note_forms` 全量记账＋游标消费（同一键既有规范 sup 又有 `footnote 14` 散文形）；相关条目 `rel_items` 含无链接纯文字项＋尾随竖线；表位形与 R 格位一一消费（空位占一个 cell 位）；`norm_md` 支持 URL 一级圆括号（`ERInt.2013(1(2)).pdf`）；账内定位失败按“前一索引＋1”兜底。

**实测（`results/page-scan.json`，第二轮为基线 `page-scan-all.json`）**：chrome 1,873／1,873 不变；页面级 **池 878（46.9%）／缺口 995**；池体积 49.07 MB／页 235.94 MB＝**20.80%**（T7：规则承载 79.2% 字节，大头是区间补丁的标签＋空白布局，如实同报）。缺口 995 全部为 `unaligned text units`（真文字差或合并至末尾仍不等），逐族处置转入后续批。B3.1 回归 **1,435/1,873（76.6%）**（＋195，无回退）。

**CI**：B3.2 判定（judge 只读）挂 `en-roundtrip.yml` ③′ 步，差集经 `roundtrip_drift.py --page/--page-baseline` 对 `page-scan-all.json` 判转差／转好／增删，并入同一 issue（`rules/05/ci-workflows.md`）。

## 10.2 B3.2 第三批实施记（2026-11-20，缺口族分流与前缀/表格结构）

**分流方法**：全 gap 首差普查（926 件 → star 308／text 300／digit 224／math 90／entity 4），逐族判例回源对读，只改有实证根因者。

**修复**：①星判定改“第一个紧闭星即决断”——右邻数字 ⇒ `(G*1)…(G*2)` 记号星对放弃、松左星 ⇒ 新开星放弃、否则按多词含空白／单词内全字母判 em；双星紧邻闭括号照常开（strong 包标点）；②嵌套引块 `> > ` 全剥；③related 段内逐子项扫描（H0 末两项间无 `|`）；④bib 区改用括号配平定位（`</div> ` 收口不齐致 bib_seq 全空的 adorno 判例）、`scan_bib` 增 table 块（`[RF]` 型条目表）、References 前瞻加 `\Z`；⑤表位形记 `[kind, colspan]` 并改按行分配（pipe 表按逻辑列展开、文字落点不可靠，aristotle-logic 判例）。

**实测**：池 **979（52.3%）／缺口 894**；池占页 **23.35%**；chrome 1,873/1,873 不变；judge 复扫 0 stale；B3.1 **1,452/1,873（77.5%）**。

## 10.3 B3.2 第四批实施记（2026-11-20，结构账顶层化与 H0 形态回补）

**方法**：gap 判例件逐件首差定位，只修落在账抽取形态或 R 逆写形态的根因；md 与 en 文字不一致者（logic-informal 的 `logic**s**` 在 H0 不存在等）记录不修，归同步线（specs/001 compare 漂移）。

**修复**：①账顶层化——`split_items` 只返顶层 li（旧裸 finditer 把嵌套子项当兄弟，`_tree_nodes` 递归双计，abelard 37 节点 vs 真 25＋4，分节与条目错位）；②`_render_bib` 的 items 提取改 `_flat_li`（嵌套感知、父先子后），`_match_close` depth 自 1 起算（复制件误写 0 → 返回兄弟开标签，隔条取 49/97）；③related 账逐项记 `sep`（H0 末两项间无 `|`），渲染按账发分隔符；④文献区 `<ol>` 全链支持（adorno 的编号清单整块被漏）；⑤bib 入口门与 `_bib_region` 同源（收口不齐件不再整块漏抽，adorno）；⑥账记 `bib_heads`（H0 标题 lv/text/id），渲染 h 项用 H0 规范文字——md 侧标题带中文加工后缀（`## References（引用注释）`，全库 1,878 件统一形态），且 seq 首项即 Bibliography 与预发重复须跳过；⑦R 引块内整段列表行生成 `<ol start>`/`<ul>`（bodin 的 `<ol type="I">` 判例）；⑧H0 缺闭合 `<li>`（anarchism 44 vs 101 判例）按兄弟边界截断；⑨`build_pool` 判 gap 时清旧池（否则 stale 长期误报）；⑩`plain`/`ukey` 剥 HTML 注释（bodin 的 `<!--<p>…</p>-->` 注释段，C 正确丢弃而等值判定把注释文字混入 B 侧）。

**实测**：池 **1,272（67.9%）／缺口 601／stale 0**（上轮 979／894）；池占页 **31.71%**（上轮 23.35%，T7 口径如实同报）；chrome 1,873/1,873 不变；B3.1 **1,452/1,873（77.5%）持平**（首轮曾因引块 ol `start≠1` 生成破坏不动点 10 件，改“序号非 1 退回 `<p>`”后集合级 0 退化 0 改善）。缺口 601 分类：star 257／md_extra 149／math 66／h0_extra 54／digit 35／text 33／ok? 5／entity 3。

## 10.4 B3.2 第五批实施记（2026-11-21，词内闭星修复）

**方法**：star 族 257 件再分诊（子模式普查：a_extra 172／shift 54／b_extra 31），a_extra 172 件经 replace 窗口标签判定 **172/172 全部 r_pair**（H0 对应处均有真 em）——星族主流是 R 配对错位，可修。判例回源（africana）：H0 `T<em>he Sociology…Chang</em>e` 为词中起排的 em，md `T*he…Chang*e` 词内开星＋**词内闭星**。

**修复**：`_intra_word_open` 决断条件改「第一个紧闭星右邻**非数字**」即进文字形态判定（旧判据只认右邻非字母数字，词内闭星 `Chang*e` 的右邻字母 `e` 漏判 → 整对星字面化）。右邻数字仍排除（`(G*1)…(G*2)` 记号星对，actualism 判例不回退）。

**实测**：池 **1,274（68.0%）／缺口 599／stale 0**（上轮 1,272／601）；池占页 **31.79%**；chrome 1,873/1,873 不变；B3.1 **1,452/1,873 持平、集合级 0 退化 0 改善**（词内闭星为纯增量规则：改前改后成功路径不变，仅失败路径转成功）。判例：africana 转池（269 补丁）。

## 10.5 B3.2 第六批实施记（2026-11-21，C 侧转义改造＋结构化强调，B3.1 +117）

**动因**：五批把 B3.1 停在 1,452，缺口大头 star 257／math 66 的根因在 **C 侧有损**——md 里字面 `*`／`$` 与强调定界符、数学定界符不可区分，R 只能靠形态试探去猜（此前三轮试探均未收敛）；嵌套强调（strong 套 em 679 处/77 件、em 套 strong 81/38、em 套 em 255/82）更是在旧四条单层正则下整块失配、外层被兜底剥壳静默丢失。

**C 侧改造**（`tools/yuanwen.py`，全量重转 1,873 件）：

- **文本层全转义**：`_esc_lit` 对标签外文字逐字转义 `\`→`\\`、`*`→`\*`、`$`→`\$`——md 字面字符 ↔ H0 字面字符单射，R 侧占位还原后 B3.1（C 再转义）与 B3.2（与 H0 逐字节一致）同时成立；
- **结构化强调**：`_emph_tags_to_md` 栈式单趟取代四条单层正则——同类相邻嵌套压平（CommonMark 无 em 套 em，保外层、内层标签归池）、异类嵌套照发（`**A *B* C**`）、星内侧空白外移（含 `&nbsp;`／U+2028）、缺闭合回删定界符、孤立闭标签忽略、跨 `<br>` 行（引块）不发表、相邻同类强调合并；
- **数学**：行内体字面 `$` 全转义（rationality `\(n \cdot $10{,}000\)` 判例）、显示体只转边缘（qm-consistent-histories `\text{ for $\alpha\neq\beta$ }` 是真嵌套）、空体 `\(\)` 不产 `$$`（propositional-function）、裸排环境先暂存后补 `$$`（epistemology-visual-thinking `\begin{align\*}` 判例）、希腊字母在斜体内不再自包星（tense-aspect／qm-retrocausality）。

**R 侧配套**（`bin/reassemble.py`）：`_star_parse` 改 run 逐星消费（整 run 全作开星优先，否则按 slot 最内层先闭，`*q***P**` 型相邻强调正确拆分）；撤 `_intra_word_open` 与全部形态试探；code 段占位（字面星不再入解析）；`\$`/`\*`/`\\`/`\#` 转义感知占位还原；数学改扫描式占位（显示体允许成对单美元）；`\(\d+\*+\)` 记号星占位撤除（吞掉合法闭星，histfem-condorcet `(1786*)` 判例）。

**检查器配套**：`check_yuanwen_fidelity.strip_math_ex` 增 `dollars=False`（html 侧裸 `$` 恒字面，全库实测 728 处/105 件皆币值，按数学跨度剥会让 `$0.75…$1` 吞掉中间正文）；作者行剔除限 count=1（图注整行 em 恢复后不再误删，berlin 判例）。

**实测**：B3.1 **1,452 → 1,569/1,873（83.8%）**，集合级 **0 退化**（转绿 117／转红 0，`script/tmp/b31_setcmp.py` 对照 `results/assembly-scan-all.json`）；B3.2 建池 **1,359（72.6%）／缺口 514／stale 0**（五批 1,274/599，+85 件转池）；池占页 **34.70%**（31.79%，T7 如实同报：池增大＝规则覆盖扩展＋嵌套标签入池，验证力相应下降）；chrome 1,873/1,873 不变；I2/I3 门禁 `--gate` 0 issue（1,873 全过），深比对软信号 305（math-asymmetric 252＋text-stream 53，均为审计档；2026-11-17 基线 322）。

## 10.6 B3.2 第七批实施记（2026-11-22，图注定界修正）

**方法**：第六批后 514 件缺口族普查（`script/tmp/b32_families2.py`）：star 204／md_extra 156／h0_extra 59／text 37／digit 34／math 19／entity 3／ok? 2。star 204 逐件首差定位发现主流是**图注标签**：H0 `<span class="figlabel">Figure 1:</span>`，C `figure_to_md` 注入 `*Figure 1:*` 定界星后再走 `inline_to_md`，被第六批的文本层全转义写成 `\*Figure 1:\*` 字面星——第六批语义改动波及了既有注入点。

**修复**：`figure_to_md` 注入点改为占位符（`\x17N\x17`），块渲染完成后还原为真定界星；md 侧回到 `*Figure 1:*`（真 em），R 侧 `_star_parse` 正常配对出 `<em>`，span 还原归 B3.2 格式层池。全量重转后 B3.1 **1,569 集合级 0 退化 0 改善**（与第六批基线逐件一致）。

**实测**：B3.2 建池 **1,483（79.2%）／缺口 390／stale 0**（第六批 1,359/514，+124 件转池）；池占页 **38.49%**（34.70%→38.49%，T7 如实同报）。缺口族分布（390）：md_extra（md 与 en 同步差，specs/001 线）／h0_extra（书目结构元素：`<ol>` 手排号、缩写键块、分节标题、表题——需账记列表形态，待批）／text／digit。

**教训**：①判据试错的终点是**语义层**——R 侧形态试探三轮不收敛，把字面/定界在 C 侧转义分离后问题整体消失，“先改产生方再改判下方”；②C 改动必须**全量重转**（1,873 件 sha 登记 entries.json 同步更新）并以 B3.1 集合级对照止损，本轮逐族修复净 +117、终态转红 0；③嵌套强调的正确表示不是更强的正则而是**栈**，md 扁平形态表达不了的结构（em 套 em、跨行 em）宁可压平/不发表并交池补，也不产歧义星流。

**附记（同批已回退的星歧义三轮）**：嵌套星对判据（歧义预模拟／括号收紧／贪心残留）三轮 B3.1 净退化 3→7 件均大于 B3.2 收益（+1），全部回退至 da27aa026——根因是 C 对嵌套 em 转不出外层星，H0 字面星残留与真嵌套在 md 扁平形态不可区分，登记专项（候选＝账记 em 嵌套结构或 yuanwen.py 转出嵌套标记）。
## 10.7 B3.2 第八批实施记（2026-11-22，链接题注守卫与公式形态账）

**缺陷一（links 账把内文引用挂到题注标签上，belief-merging 判例）**：H0 的 `Table 1` 可见出现序 0,2,3,4,5,6 全在正文，第 1 次是题注 span；游标法把首条链接挂到 C 注入的 `*Table 1:*` 题注行上。先试“全局出现序＝账 nth”精确匹配，全库实测池 **−9**（1,483→1,474，失池 17 件）——md 与 H0 出现次数不等时反而全错位，**已回退**。终法：保留文档序游标，加题注跳过守卫（md 侧 `*Xxx N:*` 题注行、锚文位于行首且后接 `:` 时不作为链接位）。

**缺陷二（裸排显示环境多出定界符）**：C 的 `wrap_naked_envs`（ADR-0049 决策 6）把裸 `\begin{align}` 包成 `$$…$$` 送渲染，md 里两种形态都成 `$$`；R 一律发 `\[…\]`，裸排件文字层多出定界符（belief-merging 判例）。新增结构账 **`math_forms`**（文档序 `br`／`naked`，全库 289 件有账），R 按游标还原：账记 `naked` 时只发环境体、不补定界符。

**实测**：池 **1,483→1,486（79.3%）／缺口 387／stale 0**；转池 4（axiom-choice／belief-merging／confirmation／decision-theory），失池 1（discourse-representation-theory，json 游标错位）；池占页 **38.59%**。B3.1 **1,569 不变**（链接账与公式账在 B3.1 判官路径下均为 None，R 行为恒等）。

**教训**：①“用账里的精确序号替换启发式”不是无条件改进——账 nth 与 md 出现次数不等时反而全盘错位（−9 实测），启发式＋局部守卫更稳；②转换层为了渲染而加的包裹（`wrap_naked_envs`）必须同时记进结构账，否则右逆无从还原。

## 10.8 B3.2 第九批实施记（2026-11-22，字面编号段落转义）

**缺陷（字面 `N.` 段落被 markdown 当有序列表，alyngton／kilvington 判例）**：H0 有 `<p>\n1. (Quantity) According…` 这类作者手打字面编号段落，全库 **224 处／35 件**（kilvington 35、alyngton 29、causation-law 16、rationality-historicist 15、fallacies 13）。md 行首 `N.` 被当列表项，右逆发 `<ol>` 吞掉数字，文字层缺 `1.`。

**终法**：C 侧 `_escape_leading_hash` 扩为块级行首双义转义——`#`（标题）已有，新增 `^(\d+)\.` → `\1\\.`（仅字符串开头，不涉软换行）；R 侧先占位 `\.`→`\x18`、收尾还原为 `.`，使 `1.` 以字面形式落回 `<p>`。

**实测**：B3.1 **1,569→1,585（+16，转红 0）**，转绿 16 件（alyngton／arnauld／causation-law／economics／fallacies／fatalism／kaspi-joseph／learning-formal／mind-indian-buddhism／nonexistent-objects／rationality-historicist／reference／teleological-arguments／tibbon／toleration／transcendental-arguments）；B3.2 池 **1,486→1,513（80.8%）／缺口 360／stale 0**，转池 27、失池 0，池占页 **39.50%**。

**教训**：行首结构义（标题、列表号、引用号）必须在 C 侧**全部**枚举转义——只做 `#` 时 `N.` 成漏网；转义点选“反斜杠＋原字符”（`N\.`）而非占位符，md 可读性与右逆可逆性兼得（占位符只用于星/美元等会被强调/数学解析吃掉的字符）。

## 10.9 B3.2 第十批实施记（2026-11-22，导航区逐字与书目定义表入账）

**缺陷一（导航区被折行器改写，alain-locke 判例）**：`toc_block` 本是账内逐字（见 `article_ledger` 注），但 `wrap_article` 把 toc 的 `<li>` 一并交 `wrap_html`：标签计入宽度使短项被折（`2.1\nValue-Feelings`），`split(" ")` 又把 H0 的双空格坍成单空格（`2.  Axiology`→`2. Axiology`）。两者都落在**文字段**上，`_sub_diff` 按段键对齐时整页文字流错位，报 `unaligned text units`。终法：`wrap_article` 与 `related-entries` 同构地切出 `<div id="toc">…</div>` 不折（配平守卫：区间内若现 `<div` 则不切）。顺带修 `wrap_html` 连续空格保真（H0 正文 439 件有词间双空格：空 token 已记 n−1 个空格，词前再补一个分隔符）。

**缺陷二（书目区定义表整块漏发，23 件全 gap）**：H0 文献区的缩写键块 `<dl class="sentag tag4em"><dt>[AOP]</dt><dd>…</dd>` 被 C 折成散文段落落进 md，而 `scan_bib` 的 `BI_START` 不含 `<dl>`，`bib_seq` 里就没有 dl 位——`_render_bib` 只按 seq 发射，md 那 16 个段落被整块丢弃（alain-locke：装配页从 `Abbreviations of Principal Works` 直接跳到 `Primary Literature`）。终法：账新增 **`bib_dl`**（`{"attrs": <dl 属性>, "pairs": [[dt_pidx, dd_pidx, dt_attrs, dd_attrs], …]}`，纯整数＋标签属性，**文字仍只从 md 段取**，合账注“禁含散文”）；`extract_bib_seq` 逐对用可见文等值在 References 散文序中定位（空 `<dt> </dt>` 不占位，contract-law 判例），配对不全则整块回落散文序逐件发 `p`（宁留结构差不丢文字）；`_render_bib` 按账发 `<dl>`/`<dt>`/`<dd>`。全库重抽账：变更 26 件，新增键只有 `bib_dl`。

**实测**：池 **1,513→1,529（81.6%）／缺口 344／stale 0**，转池 16（addams-jane／alain-locke／contract-law／japanese-philosophy／kant-conceptualism／kant-hume-morality／leibniz-evil／luxemburg／meister-eckhart／nietzsche-aesthetics／reid-ethics／rorty／scholem／srigupta／vasubandhu／wilhelm-wundt），失池 0；池占页 **39.65%**。B3.1 不受影响（本批只动 R/账）。

**残留族（本批定位，未修）**：①dl 的 dd 内嵌 `<ol>`（heidegger：`GA50` 项下 `1.… 2.…` 条目化，配对模型未覆盖）；②书目区首段说明文字被丢（leibniz-exoteric：`Note that all quotes from untranslated sources…`）；③书目区**整节**在 A 侧位置漂移（bruno：装配把 Bibliography 排在 Other Internet Resources 之后，H0 在前）；④交叉引用注 `see note 20` → md 空键 `[^note-]`（ratnakirti／boethius-dacia）；⑤dl 文字被 C 折进脚注定义、References 区无散文可配（leibniz-ethics／levinas：`[^csm-1985]: [**CSM I**] …` 一块多对）；⑥字符层漂移 `10−35`（U+2212）vs `10-35`（ibn-sina-natural，属 md/en 同步线）。

**教训**：①“账记逐字”的区间必须**整体退出**后续文本处理器——折行器作用于全页时，逐字承诺即作废，且破坏的是文字段对齐（后果是整页 gap，不是局部补丁）；②列表类结构（ol/ul/dl）在 C 侧一律降级为散文，右逆要还原就必须把“哪些散文属于该结构”记进账：账记**索引与属性**，文字仍归 md，才是单一事实源；③配对失败要**回落**而非硬发，宁可留格式层差不制造文字层缺失。

## 10.10 B3.2 第十一批实施记（2026-11-22，链接落位守卫组与账归一化转义还原）

**缺陷一（链接挂到标题上，bruno 判例）**：内文“见下文 Other Internet Resources 一节”的散文链接与标题同文，游标前置失配时链接被挂到 `<h2 id="Oth">` 上，标题 `txt` 带标签致 `REGION_HEADS` 认不出，整个 OIR 节并进 main-text。修法：标题行不消费链接（全库正文标题内 href 链接 0 件，跳过安全；`<a name>` 形不入账不受影响）。该族 133 件预检：97 pool→pool、3 gap→pool、0 退化。

**缺陷二（链接落进数学体／列表标记，infinity／trinity 判例）**：短锚文（`1`）在词界匹配后落进 `$…=1$`（右逆发 `\(…=1\)` 破坏公式）或有序列表 `1. ` 标记上（行首成 `[1](…)`，列表解析失效）。修法：候选位先过数学区间（`_math_spans`，与 `_scan_stash_math` 同判据）与列表标记区间守卫。

**缺陷三（锚文跨强调定界星，infinity 判例）**：锚文可见跨度可跨过闭星（`*interpretations* of probability` 取后半句），直接插入使 `<a>` 跨 `<em>` 边界。修法：跨度内定界星不配对时**就地**扩展（只认紧邻星，最多 4 步；不能就地配平则弃此候选，绝不向远处吞字），产出 `[*interpretations* of probability](…)`。同时撤除锚文 `replace("*", "\\*")` 旧法——字面星 C 侧已转义为 `\*`（第六批文本层全转义），旧法反把强调定界星打成字面星。

**缺陷四（账归一化不认 C 的转义，heidegger 判例）**：`norm_md` 只去星不去反斜杠，C 第六/九批起写入的 `1\.`、`(\*)` 在可见文等值上全部失配，书目 `dl` 配对失败回落散文。修法：`\*` 先占位、其余 `\x` 还原为字面字符（`\*` 占位须先于去星，否则字面星被当强调星删掉）。

**实测**：池 **1,529→1,567（83.7%）／缺口 306／stale 0**，转池 38、失池 0，池占页 **41.00%**；B3.1 1,585 持平（本批 R 改动只在 links 非空路径生效）。

**教训**：①链接落位守卫是**组合**而非单条——标题／数学／列表／强调四类位置互不包含，缺一即从别处漏出；②首版守卫单独上线时全库 −2（infinity／trinity 转红），按失池件逆向定位才见裸星与数学体两处真因——**净值为正不等于无损，失池件必须逐件定性**；③扩展必须“就地或弃”，远处吞字会把锚文语义搞坏（读者可见错误比 gap 更糟）。

## 10.11 B3.2 第十二批实施记（2026-11-22，行首列表标记转义与书目引块位次账）

**缺陷一（行首 `+ ` 被当无序列表，berkeley 判例）**：H0 引块首行 `+ Mind is a congeries…`，md `> + Mind …` 的 `+` 成列表标记，符号丢失且体例失真。修法：C 侧 `_escape_leading_hash` 增行首 `[-+] ` → `\-`／`\+`，R 侧 `\x19`／`\x1a` 占位还原（全库仅 1 件）。

**缺陷二（上游断锚成空键引用，ratnakirti 判例）**：H0 `<a href="notes.html#">note 20</a>` 空片段，C 生成 `[^note-]` 空键（无定义、右逆无从还原）。修法：空片段按纯文字照录（链接形态交池）。

**缺陷三（书目区内容引块整块丢失，20 件有账）**：`scan_bib` 的 `BI_START` 不含 `<blockquote>`，账无位次；R 的 References 区分支又把区内所有 `>` 行一律跳过（原意只是跳过 C 注入的“原文参考文献已转为脚注引用”固定注，已在区首消费）——H0 用引块排的版本条目（berkeley 的 `[W]`）两侧同丢。修法：账增 `bq` 位次（`["bq", n]`，只记位次不记文字），R 抽出 `_render_bq`（主循环与 References 区共用），区内内容引块按位次取 md 的 `>` 块发射。

**实测**：B3.1 **1,585→1,592（+7，转红 0）**（转绿 aquinas／hamann／hume-religion／justice-distributive／leibniz-mind／scheler／theophrastus）；受影响 21 件定点重建 → 池 **1,567→1,578（84.3%）／缺口 295／stale 0**，11 件 gap→pool（aquinas／berkeley／feminism-femhist／frege／hamann／hume-religion／justice-distributive／leibniz／leibniz-mind／scheler／theophrastus）、0 反退，池占页 **41.34%**。

**教训**：①“跳过某类行”的规则要写明**跳过谁**——按前缀一刀切（区内所有 `>`）会把同形的正文内容一并吞掉，正确判据是固定注的精确前缀；②同一渲染分支出现在两处时先抽函数再改（`_render_bq`），否则一处修、一处漏；③账记位次而非文字，R 侧按位次取 md 块，仍然是单一事实源。

## 11. 现状与下一步（开工卡，2026-11-22）

**验收线现状**（现查口径，勿引快照）：

| 判据 | 现状 | 取数命令 |
| ---- | ---- | ---- |
| B3.1 往返不动点 | **1,592/1,873（85.0%）**，集合级 0 退化（对 `results/assembly-scan-all.json`） | `python -B specs/053-en-template-audit/bin/reassemble.py --all --out <json>` |
| B3.2 页面装配 | **pool 1,578（84.3%）／gap 295／stale 0**，池占页 41.34% | `python -B specs/053-en-template-audit/bin/page_assemble.py --all --build` |
| I2/I3 转换保真 | `--gate` 0 issue（1,873 全过） | `python -B tools/check_yuanwen_fidelity.py --gate` |
| 全库门禁 | check_all 17 项全绿 | `python -B tools/check_all.py` |

**缺口 295 分族**（`script/tmp/b32_families2.py <scan-json>`，2026-11-22 现查）：md_extra 168／text 37／h0_extra 33／math 24／digit 21／ok? 6／star 4／entity 2。

- **md_extra**：md 有而 H0 无＝md 与 en 版本差／译注污染，属 specs/001 同步线（`compare` 漂移），**不修规则**。这是最大族，B3.2 分母的收敛上限由它决定。
- **书目区散文折叠进脚注定义**（leibniz-exoteric／ratnakirti／augustine 等）：C 把书目区 `<p>` 无作者年份散文也建成 `-nd` 伪键定义（首词成“作者名”，leibniz-exoteric 的键竟是 `note-nd`），而账侧 `defs` 列表排除 `note-` 前缀，`pd` 定位失败整段不发射。候选修法＝C 侧定案：书目区无年份散文直接落段（影响 ~265 件 579 段的定义改段落），须全量重转＋B3.1 止损。
- **text／digit／star／math 残余**：逐件定位用 `script/tmp/probe_align2.py <slug>`（打印拒录块首差）。

**已修复（第九至十二批）**：①字面编号段落转义（C `N\.`，B3.1 +16）；②toc 退出折行链＋双空格保真＋`bib_dl` 账；③链接落位守卫组（标题／数学体／列表标记／强调就地配平）＋`norm_md` 转义还原；④行首 `[-+] ` 转义＋空锚按文字＋书目引块 `bq` 位次账＋`_render_bq` 抽出。

**下一批入口**（按收益排序）：
1. **书目区散文定义化**（上述 C 侧定案）——同时解 md 里的 `[^x-nd]` 伪定义污染与 `pd` 定位失败族。
2. **dl 的 dd 内嵌 `<ol>`**（heidegger 已转池但 ibn-rushd 等仍有版次差）与 bruno／burke／analysis／nicolai-hartmann 等逐件定位。
3. **md_extra 173**：转 specs/001 同步线（`compare` 漂移清单核对），不属本线规则。

**流程提醒**：动 C 必全量重转（约 18 分钟）＋B3.1 集合级对照止损；动 R/账只重跑 B3.1（约 10 分钟）＋建池（约 20 分钟）＋judge 复扫（约 25 分钟）；**小改动可走定点重建＋judge 拼接**（受影响件集＝账 diff 的 slug 集＋md 变件，见 `script/tmp/splice_b12.py`）；基线只在收敛后人工更新并提交。

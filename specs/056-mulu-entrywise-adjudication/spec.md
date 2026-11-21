# specs/056 — mu-lu-s 逐条目分类研判（不计成本全量覆盖）

- 编号：specs/056；立项日期：2026-11-22；状态：**已完成**（2026-11-22 收官）
- 承办：主会话（ADR-0034 主代理单干）
- 上位：specs/055（六区体系定案维持）、ADR-0048（研判须联网查证留凭证——本战役证据基座为本地冻结镜像，边缘条目联网补查）、ADR-0039（批次卡钉与作废条件）、rules/08

## 意图复述（rules/08 §0）

用户 2026-11-22 指令："**逐条目研判不计成本**"（承接 mu-lu-s 分类定案维持之后的下一步）＝对 `mu-lu-s.md` 全部链接行（1873 正式词条＋10 导航行）**逐条研判分类归属**：每行核对现节是否为六区体系下最恰当归类，错位即修（MOVE），全量逐行留痕（台账），不限投入。

## 目标

1. 全量研判台账：1883 行逐行含 裁定（KEEP／MOVE／HOLD）＋依据＋凭证，分批 TSV 入 `results/`。
2. MOVE 修正在台账定案后一次性应用：mu-lu-s.md 行迁移、守恒 1883、门禁全绿、mulu-map 重建。
3. 真歧义条目（HOLD）集中呈报用户裁定，不静默处置。

## 非目标

不改六区树结构（2026-11-22 定案维持）；不改 SUMMARY.md／词条文件／en／yuanwen；不改节内排序模型与档位；不做术语/译名处置（并行会话 r 系管辖）。

## 证据基座（逐条）

1. 条目题名（中文＋英文原题，mu-lu-s 行内已有）；
2. **本地冻结镜像摘要**：`en/<slug>/index.html` 标题＋首段（零抓取、权威）；
3. SEP Related Entries 簇（本地页内）；
4. specs/010 PP 映射 TSV（咨询性锚，auto 规则噪音按 ADR-0048 不机械采信）；
5. 边缘条目联网补查（PhilPapers 页面／SEP 站内检索），凭证记入台账凭证列。

## 台账 schema（results/adjudication-b<N>.tsv，tab 分隔）

seq｜slug｜题名｜现节｜裁定｜新节｜依据｜凭证
- 裁定 ∈ {KEEP, MOVE, HOLD}；KEEP 时新节空；依据一句话；凭证 ∈ {题名自释, 本地摘要, 相关条目, PP映射, 联网查证}（可组合）。

## 卡钉与作废条件（ADR-0039）

- **卡钉**：链接集合守恒 1883 进=出、零重复零丢失；每行有裁定非空；check_mulu_s 六项全绿（含空节硬拦）；G1–G4 全绿；台账批次连续覆盖 1..1883 无缺号。
- **作废条件**：应用后守恒破坏无法机械修复；或 MOVE 目标节不存在（六区树外路径）——逐批校验，触发即回滚该批。
- **试金石**：批次 1 先行 60 条（含全部已知疑位样本），验证台账→应用闭环后再放量。

## 批次计划

按六区顺序分批（每批 ≈188 行，共 11 批）：b1 前言/关于/西史·古代，b2 西史·中世纪，b3 西史·文艺复兴＋近代前半，b4 西史·近代后半，b5 西史·现代，b6 传统区，b7 形上认识论，b8 价值理论，b9 科学逻辑数学，b10 收尾（1693–1880），b11 尾三行（1881–1883）。

## 执行结果（2026-11-22 收官）

- **覆盖**：b1–b11 连续覆盖 seq 1–1883 无缺号；**KEEP 1855／MOVE 28／HOLD 0**。逐条清单与分布见 `results/adjudication-summary.md`。
- **应用**：`bin/apply_moves.py` 一次性写回 mu-lu-s.md（整簇搬运＋幂等重放）；守恒 1883 进=1883 出。
- **门禁**：check_mulu_s 六项 0 硬错、catalog-net G1–G4 全绿（mulu-map 重建 rows=links=1883）、check_all 17 项全绿。
- **应用阶段反检**（详见 summary）：b1 slug 笔误 2 处已修；`skepticism` 由 KEEP 改判 MOVE（结构门禁反检出空节与错位双缺陷）。
- **卡钉达成**：全部满足；无 HOLD，无需呈报裁定项。
- 增量教训（已记 summary）：台账入库前须与文档序全量对账；应用器原生支持簇与幂等；结构判定交权威门禁、不重复实现。

## 追加批次 b12：概念属人物者归人物簇（2026-11-22 用户新裁定）

**指令**："概念属于人物的应归类到人物，有问题读取原文。"

**判定方法（三路定向扫描，漏报好于误报）**：
1. `en/<slug>/index.html` 标题英文所有格（129 条命中）；
2. mu-lu-s 中文侧"某某的…"结构（57 条命中，交叉验证）；
3. "Person on/in X" 模式（143 条，确认史区人物簇已完备）。
广谱"标题含人物姓氏"（488 条）因单名误配过多、多为"X in 领域"正确形态，按漏报好于误报不采。

**原文核实**：19 条候选逐条读 `en/` 首段（`results/` 凭证列记要点），全部确属对应人物学说条目。

**落地（`results/adjudication-b12.tsv`，17 行／19 行移动）**：
- `CLUS` 同节簇化（缩进 2、移入母条簇末尾）14 条：wittgenstein ×3、lewis-metaphysics、al-farabi ×4、ibn-rushd-natural、ibn-sina ×3、bolzano-logic、mally-deontic；
- `MOVECLUS` 跨节移入簇 3 条：type-theory-church（数理逻辑→逻辑史 church 簇）、goodman-aesthetics（艺术哲学→分析语言哲学 goodman 簇）、newton-stm＋随簇 2 子条（物理科学哲学→史区近代哲学 newton 簇）。

**刻意 KEEP 的例外**（人物条不在库、或为定理/悖论/问题类）：Butler、Adam Smith、Nozick、Croce、Beardsley、Shaaban Robert；Bell 定理、Skolem／Curry／Fitch 悖论、Gödel 不完备定理、Molyneux 问题、囚徒困境、Hilbert 纲领、Arrow 定理等——非人物学说条目，留学科节。`schema`／`practical-reason`／`dualism`／`personalism` 原文均为通题（已核实），b1–b11 搬出人物簇的裁定不变。

**验收**：守恒 1883；check_mulu_s 六项 0 硬错；G1–G4 全绿（mulu-map 重建）；check_all 17 项全绿。

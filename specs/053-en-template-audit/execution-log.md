# 053 执行账：EN 语料模板审计与勘误装配线

## 2026-11-19 P1 批次（B3.1 逆向装配器）——验收线 B3.1 首跑

**裁定与上下文**：用户“批准继续，加强复核”。B3.1＝`C(R(md)) ≡ md` 字节级不动点（收缩对右逆，specs/053 §9 定理框架；B3.2 的 sha 全等在池冻结后验收）。

**产物**：
- `bin/reassemble.py`（R 装配器，判官只读；同源求值——装配 HTML 交 yuanwen 生产函数原件闭环）。
- `results/assembly-trial.json`（试金石 15 件）＋`results/assembly-scan-all.json`（全库 1,872）。
- 负向 selftest：篡改 md 一段 → 不动点必破（绿）。

### 1. 试金石（15 件，含 leucippus 最小底稿／abelard 97 文献／补丁件 incommensurability）

14/15 通过；唯一残差 bayes-theorem（引块表 + 公式段，W7）。

### 2. 全库首跑与规则迭代（v1.0→v1.6，四轮全库）

| 轮 | 不动点 | 闭合率 | 本轮的修 |
| ---- | ---- | ---- | ---- |
| v1.0 | 1,058 | 56.5% | 首版（题头合成层/pubinfo/h1/文献 ul 原位/脚注链） |
| v1.1 | 1,085 | 58.0% | 希腊字母逆映射补反斜杠（`*ψ*`→`\(\psi\)`，C 侧 fullmatch 才识别） |
| v1.2 | 1,240 | **66.2%** | ①表题 `<caption>` 装配（`***X***` 紧贴表）②文献区散文段先于 ul（bib_entries 次序＝HTML 文档序）③数学占位先于 sub/sup（`$\pr_{t}$` 不被改写成 `<sub>`)④松散列表边界（项间空行＝列表边界） |

净增 +182 件。终态：**1,872＝1,240 不动点（66.2%）／632 残差／0 跳过**。

### 3. 残差分型（632，首差特征）

| 族 | 件数 | 例 | 定性 |
| ---- | ---- | ---- | ---- |
| 文献分节键（def-line±notes） | ~396 | adorno、addams-jane、comte | md 尾 defs 与 References 区 h3 分节无法对位；year-first 条目键依赖 section author → 键错位。→ W8 |
| 其余未归 | ~144 | aesthetic-judgment | 需逐件人审（多为键序/定义顺序） |
| math-inline／subsup | ~24 | causal-models | TeX 内空白/记号残留 |
| bold-italic（含乘法星邻接） | ~44 | anderson-john、altruism-biological | ` * ` 乘法星与强调星歧义。→ W10 |
| 引块表／notes 链 | ~13 | assertion、bayes-theorem | W7 |

### 4. W 登记（动工前现查）

- **W7** 引块表（`> | …`）与引块内 `<br>` 组合残差（bayes-theorem）。
- **W8** 文献分节作者键重建：R 需把 md 尾 defs 归位到 References 区 h3 分节；仅凭 md 无法判定分节边界 → 候选方案：转换器在 md 侧保留分节锚（如 def 行加注 section），或 B3.2 池按 slug 记录分节布局。**这是当前最大残差族。**
- **W9** 有序列表起始号（`<ol start=N>` 被 C 丢弃 → md 显示 1..N，但部分 md 自身带非 1 起始，如 alyngton `2.`）——需核 C 的 list_to_md 是否读 start。
- **W10** 乘法星邻接（`10 * Prob(...)` 的裸星与强调星配对歧义）。
- **W11** 图片 passthrough（md 中 `![…]` 与 `<img>` 混形）。
- **W12** 行内数学残留（`$…$` 内空白归一等）。

### 5. 加强复核四件套（ADR-0067）

1. **守恒**：装配 HTML 经 parse_entry 解析零异常＋B0 抽检（b0_mini）每件记录。
2. **同源**：求值用 `yuanwen.strip_closed_comments / protect_cross_block_math / render_blocks / extract_blocks_raw / build_cite_keys / link_citations / convert_notes / _drop_duplicate_h1 / restore_cross_block_math / apply_en_patches` 原件——R 只做 md→HTML 的右逆，不重实现转换语义（ADR-0073 同源对照）。
3. **负向**：`--selftest`（删段必破）。
4. **交集**：试金石含补丁件 incommensurability（求值视图 en⊕patches 全绿）。

### 6. 教训

①**判据迭代须全库复跑**：单件转绿不等于族转绿（caption 修复只影响 1 件；希腊反斜杠影响 ~400）。②**首差窗口取尾段会误导**（前缀/后缀修剪的展示窗口曾把我引向错误族）。③**慢≠死**：首轮全库 ~12 分钟被误判为挂死，加逐件计时后确认为正常耗时；stderr 须 flush（管道缓冲致日志空）。

## 2026-11-19 B3 运营化：EN 互转漂移巡检入 CI（用户“做成 GitHub ci，发现变动时提交变化 issue，每天定时三次”）

**产物**：`.github/workflows/en-roundtrip.yml`（每日三次 UTC 01/09/17）＋`tools/roundtrip_drift.py`（基线差集对比器）。

**语义（本轮裁定）**：B3.1 存已知残差（632/1872），故“变动”一律指**相对已提交基线扫描 `results/assembly-scan-all.json` 的差集**，不是“有失败”：③新残差（基线 ok→今 fail，需人审定四出口）／④转绿（基线 fail→今 ok，基线待更新）／⑤词条增删；另并入①en 钉漂移（divergence verify failures）与②I2 红灯（fidelity --gate）。基线更新仍是人工/本地会话动作（重跑 reassemble --all 并提交）。

**只读原则**（同 catalog-drift，specs/054 §3）：不写 baseline、不改 en//yuanwen/、不提交内容文件；有变动开/更新 issue（`en-roundtrip-drift`；巡检自身失败 `en-roundtrip-broken`），报告与全量扫描入运行工件。

**本地实测**：同件→changed=false；翻转一 ok→fail／一 fail→ok／删一条＋I2 红灯 → changed=true 且四族逐项报出（script/tmp 实测，产物未入库）。登记：`rules/05/ci-workflows.md` 工作流清单新增一行。

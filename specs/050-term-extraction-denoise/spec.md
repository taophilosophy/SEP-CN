# specs/050 术语提取降噪（标本兼治）

> 触发：2026-11-18 主理人发现「术语提取有问题——有的术语是多个单词构成，或直接是
> 1 句话/2 句话/多句话；而且有的不只是纯粹哲学领域词汇」。当日指令「标本兼治，不计成本」。

## 1. 病象（实证）

对 `tasks/term-pool.json`（75,594 条，其中 `new` 74,269 条）逐类抽样诊断为五类噪声：

| 类 | 例 | 根因 |
| ---- | ---- | ---- |
| 子句/句子片段 | `am in pain`、`Sullivan is eating burrito`、`Kant argues`、`Gödel published` | `clean_phrase` 只按 ≤4 词放行，未检系动词/助动词/报道动词 |
| 连字符残片 | `suárez- suárez-`、`Rawls rawls-`、`kuhn- kuhn-` | 词条名截断后残留连字符尾 |
| 外语混排残片 | `Künne chap`、`Gödel's inner model`、`disciple Kamalaśīla`、`structures dào` | 英语普通词与原文混排，未判「术语+英语词」残片 |
| 结构标题/节名 | `Introduction`、`Theory of Human Nature`、`catalog supplement` | topic 路把章节标题当术语 |
| 泛词/泛搭配 | `good`、`true`、`yes`、`takes place`、`too much`、`general theory` | 单字普通词与通用搭配未过滤 |
| LaTeX 残渣 | `mid cdot`、`rightarrow rightarrow` | 提取前未剔除 `$..$` 数学模式，反斜杠被词元正则剥掉后成普通词 |

## 2. 治法

### 2.1 治本（提取端，`tools/term_harvest.py`）

- `extract_slug` 增数学模式剔除（`$..$` / `$$..$$` / `\(..\)` / `\[..\]`），从源头消灭 LaTeX 残渣。
- 新增 `termhood_ok(raw, typ)` 守卫，在 `add()` 入池前拦截：数学残渣 / 子句片段
  （系动词、助动词、报道动词，刻意放行 `will`/`being`/`matter` 以保住 free will、
  human being、prime matter）/ 连字符与词干重复残片 / 单字泛词（含术语后缀豁免）/
  短语泛搭配（含白名单 `TERM_KEEP` 保住 natural kind、problem of evil 等）/
  结构标题（含 supplement）/ 跨句粘连 / cjk 虚词与句子级串 / 外语混排残片。
- 原则：只拦确定性/高置信非术语，语义待定者一律放行（机检为筛、人审为判，ADR-0070）。

### 2.2 治标（存量池，`tools/term_prescreen.py`）

- 对 `new` 候选复用同一套守卫常量（单一事实源），逐条分类并置
  `rejected:自动预筛-<类>`；`type=person` 跳过（人名走人名表 workflow）。
- 生成 `specs/008-terminology-campaign/results/prescreen-<日期>.json` 全量撤销清单。
- 首轮实绩：处理 65,985 条，判噪声 11,266 条（17.1%），保留 54,719 条。

### 2.3 口径（`tools/check_term_pool.py` + `check_all`）

两条不变量入 CI 门禁（键 `termpool`）：
- **I1 无回归**：`new` 候选不得违反 `termhood_ok`（防提取改动静默放回噪声）。
- **I2 可追溯**：每条 `rejected:自动预筛-*` 须在 manifest 撤销清单中（防绕过工具手塞裁定）。

## 3. 验收

- `tools/tests/test_term_harvest.py` 5 项 + `test_term_prescreen.py` 5 项全绿。
- `tools/check_term_pool.py --gate` 绿（I1=0、I2=0）。
- 误伤防护实测：natural kind / ontological commitment / problem of evil /
  identity of indiscernibles / true belief / florbian transfer 均保留。

## 4. 遗留（后续批，不阻塞本轮）

- 54,719 条保留候选中仍含书名（italic 路）、人名碎片（foreign 路）、部分泛搭配；
  这些「非原子术语」宜按目的地分流（书名→ADR-0011 书名登记；人名→人名表），
  属结构性分流课题，另立建议书，不在本轮强判（避免误杀真术语）。
- 本轮未跑 `term_harvest.py --refresh` 全库重提取：预筛已把同一套守卫套到存量池，
  与重提取对 `new` 的效果等价；`--refresh` 可在下一次常规重提取时顺带验证。

## 5. 全量重建（用户 2026-11-18「无需分流，全量现在进行」）

- 真实基底：隔离正式池跑空池（避开 `load_registered_keys` 读正式池把全部键当已登记的
  假象），修复后提取器全量产出 **60,173 条**；与旧 `new`（63,977 键）对比：共现 59,212 /
  基线新增 961 / **旧提取残渣退役 4,765**（跨句粘连等）。
- 重建（`script/tmp/rebuild_pool.py`）：裁定账 published 491 / held 28 / 人工 rejected 806 /
  自动预筛 11,266 全保留；旧 `new` 机器提议由基底替换（去裁定账重键）；池 **71,803 条**；
  退役清单 `results/rebuild-2026-11-18-retired.json`（全量 en/type/freq，可回滚）。
- 重建后对 `new` 再跑预筛：命中仅 1 条（Philosophical Papers Volume），证明守卫在提取端已拦净。
- 工具修正：`term_prescreen.py` 改**合并模式**（同日 manifest 并集，防覆盖历史裁定）；
  manifest 回填至 11,267 条。

## 6. 全量 A/B/C 分档提议（`tools/term_grade.py`）

机检为筛、人审为判（ADR-0070）：只给每条建议档位与理由，**不登记、不译名**。

| 档 | 条数 | 口径 |
| ---- | ---- | ---- |
| A 建议直裁 | 12,739 | -ism / 术语后缀（词干≥3，防 unity 类误判）/ foreign 纯原文（含 ASCII 德语名词经 GERMAN_SUFFIX 兜底） |
| B 需核 | 33,899 | 多词无后缀短语、多词引语、斜体多词、ascii 外语、希腊/汉/阿等 |
| C 挂起或驳 | 3,903 | topic 标题 / 单 Token 大写（书名刊名，ADR-0011）/ 高频全普通词 |
| P 转人名表 | 8,619 | type=person |

产物：`results/grade-2026-11-18.json`（逐条 en/type/freq/reason）+ `.md` 摘要。
已知噪声如实上报：P 档含 CAP_PAIR 误收（American Philosophy、Mario Bros 等）、
A 档含个别残片（Mathématique Paris Aug）——均列为待人工复核样例，不自动处置。

## 7. 登记册求差口径修复（用户 2026-11-18「批准并实测几份」）

- 发现：`term_harvest.load_registered_keys()` 池侧用 B 口径 `norm_key`（不折叠撇号），
  与登记册侧（`check_terms.norm_key` 实为 A 口径 `norm_key_quote`）不对称，致 ʿ/’/' 
  变体漏扣（如 ʿaql↔'aql、Bayes’ Theorem↔bayes' theorem、Ibn ʿArabī）。
- 修复：池侧建键与 `main()` 求差均改 A 口径（`norm_key_quote(key) in registered`）。
- 实测（重建后）：new 59,211→59,160；与两表 A 口径重合 **38→0（0.0000%）**；
  退役 44 条经逐一核验**全部为登记册撇号/归并变体**（0 条误杀）；
  测试 14/14 绿、门禁 I1/I2 绿、预筛 0 噪声。
- 结论：候选池与两登记册净重合度 0，扣除机制完全对齐 specs/033 口径纪律。

## 8. 双池合一（用户 2026-11-18「清理旧的，将二者合并」）

- 对象：`tasks/term-candidates.json`（2026-10-27 旧候选池，58 条）并入
  `tasks/term-pool.json`；旧池此后删除。
- 合并前核对：58 条中 **41 条键已在两登记册**（其中 published 36、held 5——
  held 5 条为历史漂移：actualism、bayesian confirmation theory、chinese/scottish/
  ancient philosophy，提请人工复核后走译法变更或豁免登记，不自动处置）；
  **17 条裁定状态未落地**（published 1 / held 11 / rejected 5），全部并入池账。
- 合并执行：A 口径去重（0 冲突），58 条全并入，note 注明来源与日期；
  池 71,752→71,810；meta.legacy_merged 记账。
- 清理与引用对齐：
  * `git rm --cached tasks/term-candidates.json` + 删文件（git 历史可溯）；
    合并副本存 `script/tmp/legacy-term-candidates-merged-20261118.json`。
  * `term_harvest.py`：LEGACY_POOL 常量改注释占位（不再读旧池），求差循环只读 POOL。
  * 活引用更新：`rules/03-terminology.md` 分档裁定节、`rules/reference/gong-cheng-fang-fa.md`、
    `specs/008-terminology-campaign/contracts/cli.md`——状态机归口一律改 `tasks/term-pool.json`。
- 验证：import OK；测试 14/14 绿；门禁 I1/I2 绿；17 条未落地裁定逐条抽验状态原样承接。

## 9. 遗留 5 条 held 豁免（用户 2026-11-18「豁免，你自己处理」）

- 对象：actualism / bayesian confirmation theory / chinese philosophy / scottish philosophy /
  ancient philosophy——合并带入 held，但键均已在术语登记册（L104 / L554 / L821 / L5065 / L268，
  2026-10-27~11-01 凭证在案），属池状态滞后于登记册的历史漂移。
- 处置（沿 specs/031 判读台账三出口·exempt 规范）：
  * 台账 `ledger-legacy-held-exempt.json`（5 行：d_class=n/a、exit=exempt、
    evidence 记豁免理由、source 记登记册行号与凭证、reviewer=ykla），
    `check_terms --check-ledger` 闭合校验 0 违例。
  * 池状态回写：held → `published@2026-11-18（豁免回写：登记册已收，specs/050 §9 …）`，
    5 条全命中；池分布变为 published 533 / held 39。
- 顺手修复：`check_terms.py` 与 `term_harvest.py` 各一处历史语法黏连
  （`passROOT=…` 致 NameError；本轮 check-ledger/gate 首次实跑暴露），已分离修正，
  全仓 grep 确认无同类残留。
- 验证：门禁 I1/I2 绿；测试 14/14 绿；5 条状态逐条抽验均为豁免回写形。





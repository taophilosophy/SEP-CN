# 065 机械化编目总表（T007 收口）

- 候选来源：`results/proof-candidates.tsv`（T001；28 件候选，5 个父词条）
- 三分类枚举（固定）：`已机械化`／`可对接`／`无从对接`
- 执行重映射（2026-11-28）：W1 原计划按 Gödel／模态／集合论族分工（T003–T006）；T001 实际候选池为认知逻辑／博弈论 13、Frege／Grundgesetze 10、基数／无限 1、量子语境性 3、确认论 1——按实际族执行，tasks.md 执行记录留痕。FFL 的 Gödel／Solovay 等成果仍为事实钉（spec §2.3）与未来扩展源，不入本表。

## 判定标准（T002 细化）

| 分类 | 判据 |
| ---- | ---- |
| 已机械化 | 命题本身（或直接等价形式）已有机器验证证明，可直接引用 |
| 可对接 | 存在机器化框架，命题可在其中陈述且关键定义齐备，但命题本身未证（引用须声明缺口） |
| 无从对接 | 未见相关机器化成果，或承载框架缺失（检索记录留痕；“未见”≠“不存在”） |

## 字段定义

| 字段 | 含义 | 硬约束 |
| ---- | ---- | ---- |
| slug | `en/` 补充页路径或词条 slug | 与 `proof-candidates.tsv` 一致 |
| 证据节 | 补充页内 Proof 节标题与行号 | 行号可复算 |
| 对接成果 | 机器验证成果名（如 AFP 条目、mathlib 声明、kscert） | 名称与官方页面一致；库名如实（ADR-0088／0089／0090） |
| 来源 URL | 成果官方页面或仓库 | 可直接访问；检索失败按 rules/05 显式记录最终状态 |
| 版本钉 | 仓库 commit／tag、论文版本或发布日期 | 不用浮动引用 |
| 分类 | 三分类之一 | 枚举外值即不合格 |
| 凭据 | 判定依据摘要（命题对应关系、覆盖范围、缺口） | 逐条可复核 |

## 总表（28 件，T007 收口）

| slug | 证据节 | 对接成果 | 来源 URL | 版本钉 | 分类 | 凭据 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| en/b/bayes-theorem.supplement.md | §Proof Sketch: 3.5 Lemma（L158）、3.6 Lemma（L173） | — | — | — | 无从对接 | 检索未见确认论量度机器化；mathlib 仅概率基座（条件概率），3.5／3.6 引理未形式化 |
| en/c/common-knowledge.proof2-04.md | §Proof of Proposition 2.4（L7） | AFP Epistemic Logic（From） | https://isa-afp.org/entries/Epistemic_Logic.html | 2018-10-29 首发；2021-04-15 扩充 T／KB／K4／S4／S5 | 可对接 | 多主体 Kripke 语义与 S5 完备性在案；划分模型与公共知识算子（K*_N／L*_N）未形式化，命题未证 |
| en/c/common-knowledge.proof2-05.md | §Proof of Proposition 2.5（L7） | AFP Epistemic Logic（From） | https://isa-afp.org/entries/Epistemic_Logic.html | 2018-10-29 首发；2021-04-15 扩充 T／KB／K4／S4／S5 | 可对接 | 多主体 Kripke 语义与 S5 完备性在案；划分模型与公共知识算子（K*_N／L*_N）未形式化，命题未证 |
| en/c/common-knowledge.proof2-08.md | §Proof of Proposition 2.8（L7） | AFP Epistemic Logic（From） | https://isa-afp.org/entries/Epistemic_Logic.html | 2018-10-29 首发；2021-04-15 扩充 T／KB／K4／S4／S5 | 可对接 | 多主体 Kripke 语义与 S5 完备性在案；划分模型与公共知识算子（K*_N／L*_N）未形式化，命题未证 |
| en/c/common-knowledge.proof2-11.md | §Proof of Proposition 2.11（L7） | — | — | — | 无从对接 | Cubitt–Sugden 共同理由信念；未见机器化；AFP 仅覆盖 Kripke 知识算子，博弈均衡定义缺 |
| en/c/common-knowledge.proof2-15.md | §Proof of Lemma 2.15（L7） | AFP Epistemic Logic（From） | https://isa-afp.org/entries/Epistemic_Logic.html | 2018-10-29 首发；2021-04-15 扩充 T／KB／K4／S4／S5 | 可对接 | 多主体 Kripke 语义与 S5 完备性在案；划分模型与公共知识算子（K*_N／L*_N）未形式化，命题未证 |
| en/c/common-knowledge.proof2-16.md | §Proof of Lemma 2.16（L7） | AFP Epistemic Logic（From） | https://isa-afp.org/entries/Epistemic_Logic.html | 2018-10-29 首发；2021-04-15 扩充 T／KB／K4／S4／S5 | 可对接 | 多主体 Kripke 语义与 S5 完备性在案；划分模型与公共知识算子（K*_N／L*_N）未形式化，命题未证 |
| en/c/common-knowledge.proof2-17.md | §Proof of Proposition 2.17（L7） | AFP Epistemic Logic（From） | https://isa-afp.org/entries/Epistemic_Logic.html | 2018-10-29 首发；2021-04-15 扩充 T／KB／K4／S4／S5 | 可对接 | 多主体 Kripke 语义与 S5 完备性在案；划分模型与公共知识算子（K*_N／L*_N）未形式化，命题未证 |
| en/c/common-knowledge.proof2-18.md | §Proof of Proposition 2.18（L7） | AFP Epistemic Logic（From） | https://isa-afp.org/entries/Epistemic_Logic.html | 2018-10-29 首发；2021-04-15 扩充 T／KB／K4／S4／S5 | 可对接 | 多主体 Kripke 语义与 S5 完备性在案；划分模型与公共知识算子（K*_N／L*_N）未形式化，命题未证 |
| en/c/common-knowledge.proof3-01.md | §Proof of Proposition 3.1（L7） | — | — | — | 无从对接 | Aumann 一致同意定理；未见机器化；AFP 仅覆盖 Kripke 知识算子，博弈均衡定义缺 |
| en/c/common-knowledge.proof3-04.md | §Proof of Proposition 3.4（L7） | — | — | — | 无从对接 | 贝叶斯理性与知识层级；未见机器化；AFP 仅覆盖 Kripke 知识算子，博弈均衡定义缺 |
| en/c/common-knowledge.proof3-07.md | §Proof of Proposition 3.7（L7） | — | — | — | 无从对接 | 内生相关均衡；未见机器化；AFP 仅覆盖 Kripke 知识算子，博弈均衡定义缺 |
| en/c/common-knowledge.proof3-11.md | §Proof of Proposition 3.11（L7） | — | — | — | 无从对接 | Aumann 相关均衡；未见机器化；AFP 仅覆盖 Kripke 知识算子，博弈均衡定义缺 |
| en/c/common-knowledge.proof3-12.md | §Proof of Proposition 3.12（L7） | — | — | — | 无从对接 | Bicchieri 逆向归纳；未见机器化；AFP 仅覆盖 Kripke 知识算子，博弈均衡定义缺 |
| en/f/frege-theorem.HerOnQN.md | §Proof that Q is Hereditary on the Natural Numbers（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.LemPred.md | §Proof of the Lemma on Predecessor$^{+}$（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.PredNoRefl.md | §Proof That No Number Ancestrally Precedes Itself（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.Q0.md | §Proof that 0 Falls Under Q（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.WAfact6.md | §Proof of Fact 6 Concerning the Weak Ancestral（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.proof4.md | §Proof of Lemma Concerning Zero（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.proof5.md | §Proof of Equinumerosity Lemma（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.proof6.md | §Proof of the General Principle of Induction（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.subproof1.md | §Proof of the Lemma for Hume's Principle（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/f/frege-theorem.subproof2.md | §Proof of Hume's Principle from Basic Law V—*Grundgesetze*-Style（L7） | — | — | — | 无从对接 | 两轮检索未见 Grundgesetze／Hume 原理推导的机器化（AFP／Lean／Isabelle／Coq）；命中均为哲学文献与证明论论文（未见≠不存在） |
| en/i/infinity.proofs.md | §Proofs of Theorems（L7） | mathlib4（Cardinal.mk_real／Cardinal.not_countable_real／Infinite.natEmbedding） | https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Cardinality.html | mathlib4 master 文档（2026-11-28 核）；月度工具链更新，引用须复钉 | 已机械化 | 命题1（Dedekind 无限→含 ℕ 大小子集）：Infinite.natEmbedding／Set.Infinite.natEmbedding＋Infinite.of_injective_to_set；命题2（正实数基数>正整数）：Cardinal.mk_real／Cardinal.not_countable_real |
| en/k/kochen-specker.proofvc1.md | §Proof of VC1（L7） | Meta ATLAS（atlas-lean）＋kscert | https://github.com/facebookresearch/atlas-lean/；https://github.com/shayaansiddique06/kscert | ATLAS v2（2026；arXiv:2605.29955）；kscert arXiv:2607.26413（2026-07-29） | 可对接 | KS 定理层面已有 Lean 形式化（Top-100 Quantum Theorems #59）；kscert 覆盖最小 KS 下界几何半边（291 行／180 图）；SEP 的 VC1／VC2／Step1 分步引理未见单独机械化（定理级覆盖、引理级缺口） |
| en/k/kochen-specker.proofvc2.md | §Proof of VC2（L7） | Meta ATLAS（atlas-lean）＋kscert | https://github.com/facebookresearch/atlas-lean/；https://github.com/shayaansiddique06/kscert | ATLAS v2（2026；arXiv:2605.29955）；kscert arXiv:2607.26413（2026-07-29） | 可对接 | KS 定理层面已有 Lean 形式化（Top-100 Quantum Theorems #59）；kscert 覆盖最小 KS 下界几何半边（291 行／180 图）；SEP 的 VC1／VC2／Step1 分步引理未见单独机械化（定理级覆盖、引理级缺口） |
| en/k/kochen-specker.step1.md | §Proof of Step 1（L7） | Meta ATLAS（atlas-lean）＋kscert | https://github.com/facebookresearch/atlas-lean/；https://github.com/shayaansiddique06/kscert | ATLAS v2（2026；arXiv:2605.29955）；kscert arXiv:2607.26413（2026-07-29） | 可对接 | KS 定理层面已有 Lean 形式化（Top-100 Quantum Theorems #59）；kscert 覆盖最小 KS 下界几何半边（291 行／180 图）；SEP 的 VC1／VC2／Step1 分步引理未见单独机械化（定理级覆盖、引理级缺口） |

## 收口记录（T007，2026-11-28）

- 行数复算：28 行 ≡ `proof-candidates.tsv` 候选 28 件（独立复算一致，28／28）。
- 分类分布：**已机械化 1**（infinity.proofs，对应 mathlib 两命题）、**可对接 10**（common-knowledge 7＋kochen-specker 3）、**无从对接 17**（common-knowledge 博弈论 6＋frege 10＋bayes 1）。
- 关键发现：显式 Proof 节候选池与 FFL 的 Gödel／Solovay 成果无交集——已机械化覆盖率仅 1／28；编目的主要价值在“可对接”10 件的框架声明与 17 件的缺口登记，而非直接引用。
- URL 抽核：AFP、mathlib docs、atlas-lean、kscert、arXiv 各抽 1 条可达（2026-11-28 检索通道）。
- 缺口登记：T008 译注对接前置不足——5 个父词条 `zh/` 均为仅 H1 骨架（nonblank=1），译者注释无承载；待翻译后执行。
- 判定边界：Frege 族“无从对接”为检索结论（未见≠不存在）；若后续出现机械化成果，按本表重开单行并在 tasks.md 追加任务。

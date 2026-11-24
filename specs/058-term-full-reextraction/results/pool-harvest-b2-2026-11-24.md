# 候选池收割第二小批（2026-11-24）：六词取中文定名凭证

来源：`tasks/term-pool.json` T1/T2 收割词。前批（`rowspec-batch58-harvest1.json`）已收停机问题、过去假设两条，本批续查其余候选，逐条联网取证。

## 一、登记（6 条）

1. **action model → 行动模型**
   西南大学逻辑与智能研究中心《西南大学—卑尔根大学逻辑工作坊》综述（2024-03-27/28）述卑尔根大学 Rustam Galimullin 报告 “Why Quantification in DEL is Fun”：
   “结合公开宣告逻辑与行动模型探讨这一领域的主要结果与开放问题”。
   与 Baltag–Moss–Solecki 的 action model 对应，取“行动模型”。
2. **Antidiscrimination Principle → 反歧视原则**
   刘征峰《从“反歧视原则”进入民事交易关系观察当代民法理念的革新》（中国社会科学院法学所·中国法学网，2017-04）题名与摘要均用“反歧视原则”；
   北京大学法学院学术书评（2018-04-11）述费斯（Owen Fiss）学说，明确将 antidiscrimination principle 译作“反歧视原则”，并与“反归类原则”“反屈从原则”并置。
3. **Critical Disability Theory → 批判残障理论**
   册内已有 `critical disability studies`＝“批判残障研究”，本行按同一构词取“批判残障理论”；
   《人权》2022 年第 5 期黄贺《论后人文主义残障观及其对残障权利事业的启示》作“批判性残障研究”（CDS，同域）；
   中文权威期刊未见“批判残障理论”定名，依 specs/058 A 档直裁，理由入册。
4. **Landauer's principle → 兰道尔原理**
   尹沛、朱慧涓《沃尔夫物理学奖与量子信息的发展》，《科技导报》2019 年第 21 期：“这个也被称为‘兰道尔原理’”。
   中国指挥与控制学会 CICC 科普栏目（2025-05-24）《兰道尔原理：连接信息与物理测量的桥梁》同。
5. **Nonidentity Problem → 非同一性问题**
   高景柱《论代际正义视域中的“非同一性问题”》（爱思想 147258），正文以帕菲特《理与人》述该名；
   王灵芝、周斌、郝明《帕菲特非同一性问题的再审视——以人类生殖系基因编辑为例》，《医学与哲学》2023 年第 18 期，英文题 A Reflection of Parfit's Non-identity Problem。
   **查重处置**：册内 2026-11-11 已有 `non-identity problem`（首见 repugnant-conclusion）同译名行，
   本篇 SEP 标题与正文均作 nonidentity（无连字符，57:16），故合并为键 `nonidentity problem`，
   保留原首见与 Parfit 1984 依据，并入本批双证，旧键删除（同概念异拼写合并）。
6. **plausibility model → 似真模型**
   同《西南大学—卑尔根大学逻辑工作坊》综述：Fernando R. Velazquez Quesada 报告题名
   “似真模型中的分布式相信”（Distributed Belief in Plausibility Models），中英题名明确配对。

## 二、未登记（3 条，证据不足）

| 候选 | 检索结论 |
| ---- | ---- |
| base theory | 语境分散（公理化真理论、逆数学、复杂性、测量科学），中文分别作“基础理论”“基础系统”，无单一权威定名；不登记，避免一词多义强行归一 |
| Modal Criterion | 中文使真者文献用“使真者必然主义”（truthmaker necessitarianism），未见 Modal Criterion 的对口定名；本义为事实判准中的模态条件，不登记 |
| intended model | 中文模型论教材（林作铨讲义等）作“标准模型/规范模型”，维基百科作“预期模型”但不可作依据；无权威中文定名，不登记 |

## 三、落册

- 术语表：8,264 → 8,269（插入 6，同概念合并删 1）。
- 池：published 6（action model、Antidiscrimination Principle、Critical Disability Theory、Landauer's principle、Nonidentity Problem、plausibility model）。
- 凭证：本文件、`rowspec-batch58-harvest2.json`；`python tools/check_all.py` 全绿。

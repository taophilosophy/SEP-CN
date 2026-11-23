# 质量复核：主形重复与落地率（2026-11-23）

对象：specs/058 当日登记的 835 条术语（21 份当日清单合计，去除表外行）。

## 一、中文主形碰撞扫描

全术语表按「译法主形」（去括注、去书名号）归组，主形对应两个以上不同英文键的共 **154 组**。其中大部分是同概念跨传统/跨转写的合法并存（如「无我」对应 anātman 与 nairātmya、「德性」对应 aretê 与 virtue、「范畴」对应 category 与 tattva）。

**其中 22 组是当日新行与既有行同概念异拼写**，属重复登记：

- 已合并 20 组（新行删去，旧行键追加合写别名并留痕）：
  act utilitarianism→act-utilitarianism、storehouse consciousness→ālayavijñāna、Bertrand's Paradox→Bertrand paradox、Black Skin, White Masks→Black Skin White Masks、Book of Lord Shang→Shangjunshu、Defender of Peace→Defensor Pacis、Discourse on the Method→Discourse on Method、discourse representation structures→…structure (DRS)、effortless action→wuwei、received opinions→endoxa、four beginnings→si duan、free play→free play (of cognitive faculties)、Guide for the Perplexed→Guide of the Perplexed、inductive principle→induction principle、Liar's paradox→Liar Paradox、Lives of the Philosophers→Lives of Eminent Philosophers、living forces→vis viva、Political Treatise→Tractatus Politicus、somatic markers→somatic marker、wu xing→wuxing。
- 辨析后保留 2 组（同形不同义，按 rules/03 分行）：
  - 可靠认知：一般知识论意义（reliable cognition）与藏传量论意义（tshad ma）；
  - 统计相关性：一般用法与 Salmon 的 SR 模型（statistical relevance (SR) model）。

合并后术语表数据行 8,089 → 8,069，`check_terms` 硬错误 0，`registry_azsort` 守恒。

## 二、落地率

当日 835 条术语中，主形在 2,021 篇中文译文中出现的 **364 条（43.6%）**；其余 471 条为前瞻性登记（英文语料出现、中文译文尚未用到或尚未译出），不构成缺陷。

抽查若干未落地项，均属登记形与语料用法并行而非误登：

- 丘奇论题（Church's thesis）— 语料通行的是「丘奇—图灵论题」（另一概念，已单独登记）；
- 帕累托原则 — 语料多为「帕累托条件／帕累托最优」；
- 良序原则 — 语料多为「良序定理」；
- 恶性循环原则 — 语料多为「恶性循环论证」；
- 概率因果性 — 语料作「概率因果关系」，属 causality 与 causal relation 两概念分列，保留。

## 三、防线

`tools/term_flow.py` 增「中文主形已存在」告警（只告警不拦截，同形不同义仍需人工按 rules/03 判定）；当日合成用例（新英文键配「五行」）正确触发。全量单元测试 578 项通过。

## 四、遗留

- 154 组主形碰撞中剩余的跨传统并存组未逐一裁定，属登记层既有格局，非本线引入。
- 合并动作改写了 20 行既有行的键与依据列，已在依据列留「2026-11-23 合并同日重复登记形」痕迹；如需回溯，可按该串检索。

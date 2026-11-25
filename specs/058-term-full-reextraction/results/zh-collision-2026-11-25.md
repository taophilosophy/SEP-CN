# 术语表中文主形撞形线（批 30–31，2026-11-25）

## 一、为什么查

登记册里不同英文键落成同一中文主形是常态：同形不同义、同概念异语都按 rules/03、ADR-0048 分行。真正的隐患是**没有裁定痕迹的撞形**——既不并键，也不写“同形不同义／撞形豁免”，重译时就等于在两个英文键之间随机取值。批 15 的 Löwenheim–Skolem 与批 25 的 humors／humours 都是这一类漏网。

## 二、判据与工具

`bin/audit_zh_collisions.py`（只读，幂等）。取译法列“（”前为中文主形，分三步：

1. **保留书名号**。剥掉《》会把概念形“万民法”与书名形“《万民法》”判成撞形，实测多组假阳性，故概念形与书名形不互撞。
2. **排除体例标签**。“拉丁原文保留”“保留原文”是体例行标签，几十行共用同一标签，不参与判定。
3. **裁定痕迹双重判据**：依据列带“同形不同义／同形异义／同概念异语／撞形豁免／按域分用／按原文分列”等标记词，或译法列带非“亦作”的括注（域、语种、作者），任一命中即算已裁定。

首扫（标记只认依据列）得 164 组撞形、55 组有行无标记；补上“译法括注”判据后降到 28 组；再去掉书名号误判为 21 组。逐组研判后归零。

## 三、九组同概念异形并键（批 30）

keeper 取排序靠前行，键写“A / B”，依据栏记旧键与旧首现：

| 并入键 | 被并键 | 理由 |
| ---- | ---- | ---- |
| cognitive ability / cognitive capacities | cognitive capacities | 同一概念，单复数异形 |
| maker's knowledge (tradition) / maker's knowledge | maker’s knowledge | 同一传统，直／弯撇号与括注差异（批 25 拼写折叠没扫到：字母不同，不是变音符） |
| mental states / psychological states | psychological states | 同一心理状态范畴，两种英文写法 |
| Nyāya-sūtra / Nyāyasūtra (Gautama) | Nyāyasūtra (Gautama) | 同一经，连字符与括注差异；并键后带 Devanagari 原文，缺原文告警 −1 |
| Occam’s razor / Ockham’s razor | Ockham’s razor | 同一原理，两种拼写（同上，字母差异非变音符） |
| Peripatetic / Peripatetics | Peripatetics | 学派名，单复数 |
| significatio / signification | signification | 中世纪语义学同一术语，拉丁形与英语形 |
| sublunar world / sublunary world | sublunary world | 同一宇宙论区域，形容词两形 |
| Lutheran / Lutheranism | Lutheranism | 宗派名，形容词与名词形 |

数据行 9,014 → 9,005；去重后“非英语术语缺原文”告警 148 → 147。

## 四、三十九行加括注消歧（批 30 十四行、批 31 二十五行）

只加“（…）”，主形一字不改，因此不属译法改定，属撞形登记。要点：

* 同形异语：烦恼（耆那）／烦恼（佛教）；全知（神学）；真理（truth 通义）／真理（阿拉伯哲学）；实（名实论）／实（事物）；情感（维韦斯 affectiones）；宗派（古代学派组织）；出离（印度宗教）；邪见（虚妄性）；或然论（耆那）；视角（耆那 naya）／视角（罗韦利关系量子力学）。
* 同域异义：选择理论（决策论）／选择理论（进化论）；期望值（物理）／期望值（决策论）；法哲学（黑格尔 Rechtsphilosophie）；数论（数学）；可解释性（模型内部）；道德价值（价值观义）／道德价值（康德语境）；正当性（行为正当）；请求权（允诺 claim）；质点（物理）。
* 书名撞车：《光学》（伊本·海赛姆）／《光学》（笛卡尔）；《数学原理》（罗素 1903 单卷）／Principia Mathematica《数学原理》（怀特海、罗素合著）；《论第一哲学》（“第一哲学”通名，非专书）／《论第一哲学》（肯迪著作）。
* 情感主义：sentimentalism 加“（道德情感主义传统…）”，与 emotivism 元伦理学情感主义分列。

## 五、结果与遗留

* 145 组撞形全部带裁定痕迹，无标记组 0；全量清单 `results/zh-collision-all-2026-11-25.tsv`（313 行），残余清单 `results/zh-collision-residue-2026-11-25.tsv` 为空表头即达标态。
* 门禁：`check_terms` 硬错误 0，缺原文 147、缺籍属/生卒 781；`check_all` 19 项全绿。
* 遗留：`《论第一哲学》` 两行只靠括注区分作者，若日后新增同题著作，须先查本清单再登记；`Causation` 作词条主题名与 `causal relation` 的题名分工仍归 SUMMARY 管辖，登记册只登记概念形。

## 六、“亦作”与独立行撞车（批 32）

撞形线收口后再加一道：译法列“亦作“X””里的异形，是否已经有独立行。扫得 27 处，逐处研判：

* 三处属同概念两行，并键：
  * degree of belief / degrees of belief（置信度，亦作信念度；审定作“信念度”，形式认识论两形并用）；
  * correspondence theory / correspondence theory of truth（符合论，亦作真理符合论；题名依 SUMMARY 作“真理符合论”，概念形仍用短形）；
  * Chinese Room / Chinese Room argument（中文屋，亦作中文屋论证、中文房间）。
* 其余 24 处是跨域或跨概念，不动：直觉／直观（康德传统 vs 伦理学语境）、智者／《智者篇》、广延／外延、理智／努斯、明智／实践智慧、图型／图式、伦理生活／伦理、空性／空、等数／等势、命名／设定等，每行依据已各自说明分列理由。
* 另清一处键残留：`rubūbiyya / rabbāniyya` 的别名列已被 2026-11-21 的 FLAG 裁定拆出（rabbāniyya 另立行作“养育性”），本键与原文列同步去掉残留并列形，只留 rubūbiyya／ربوبية。

数据行 9,005 → 9,002；撞形无标记组仍为 0（并键后新出现的符合论／conformality theory 一组已补“同形不同义”标记）。

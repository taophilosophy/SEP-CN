# 收割批 9：-ism 家族（2026-11-25）

候选池 `type=ism` 的 new 条目 632，其中登记册缺 629；按「拆 `/`＋单复数」初筛降到 581，再按强归一（去连字符／空格／大小写）复核，61 条语料高频者里 **4 条是伪缺口、4 条属同概念异拼写**，真正登记 54 条。

## 一、伪缺口与同概念异拼写（8 条并入既有行，不重登）

| 拟登键 | 册中已有键 | 处置 |
| ---- | ---- | ---- |
| Antisemitism | `anti-Semitism` | 键并入 |
| four-dimensionalism | `Four Dimensionalism` | 键并入 |
| noncognitivism | `non-cognitivism` | 键并入 |
| rule-consequentialism | `Rule Consequentialism` | 键并入 |
| Prioritarianism | `prioritarian` | 键并入（学说名与形容词一概念） |
| non-realism | `irrealism` | 键并入（同译“非实在论”） |
| Relationism | `relationalism(space and time)` | 键并入（同译“关系论”） |
| Relationalism | `relationalism (RQM)` | 键并入（同译“关系主义”） |

**结构性教训**：`register_lib.norm_key` 只做大小写与撇号归一，不统一连字符、空格与括注，所以 `non-cognitivism`／`noncognitivism`、`Rule Consequentialism`／`rule-consequentialism` 在键比对里是两个键。批 6–8 的缺口清单同样带有这一层偏差（假阳性偏多）。**下轮审计须先做强归一**（`[^a-z0-9]+` 全删）再判缺口；本轮以一次性复核补上。

## 二、登记（54 条）

高频段：primitivism 175、Personalism 159、descriptivism 122、retributivism 106、act-consequentialism 97、Constitutionalism 92、moralism 87、eternalism 86、emotivism 78、predictivism 77、Animalism 76、Totalitarianism 74、supervaluationism 70、pancomputationalism 70、normativism 69、interpretivism 68、separatism 66、preservationism 66、Meinongianism 66、generalism 63、Hinduism 62、frequentism 56、morphism 55、constructionism 54、Infinitism 51、noncognitivism（并入）、substantivalism 49、Emergentism 49、Adverbialism 47、Neo-Daoism 45、secularism 43、Textualism 42、Humeanism 40、irrationalism 38、extensionalism 38、dimensionalism 38、Trinitarianism 38、experimentalism 38、behaviourism（异形并入 behaviorism）、Eurocentrism 35、reductivism 34、Russellianism 34、poststructuralism 33、classicism 32、Copernicanism 32、supernaturalism 30、proceduralism 30、anti-psychologism 30、traditionalism 26、purposivism 25、paralogism 25、constitutivism 25、ecofeminism 23、sufficientarianism 20、immaterialism 22、non-realism（并入）、non-reductionism 32。

择形要点：

* **按域加限定语**（同中文形而英文词不同，靠括注分域）：eternalism 永恒论（时间哲学）／presentism 现在主义；Animalism 动物论（心灵哲学）／animalism 的泛生命义；Adverbialism 副词论（知觉哲学）；Relationism 关系论（时空）／Relationalism 关系主义（RQM）；substantivalism 实体论（时空）／substance 实体；generalism 通则主义（伦理学）／particularism 特殊主义；constitutivism 构成主义（伦理学）／constructivism 构成主义（艺术史）。
* **同族对齐**：boxed 与已登记行的译形保持一致——rule-/act-consequentialism 对 consequentialism 后果论；non-reductionism 对 anti-reductionism 反还原论；emotivism 对 sentimentalism（同为“情感主义”，故 emotivism 译形加“（伦理学）”限定，避免两行主形全同）。
* **不登**：dynamism、centralism、antagonism、catechism、cannibalism、empathy-altruism、purposivism 之外的零用量 -ism 名；`paralogism` 登（康德谬误推理为实术语），`morphism` 登（范畴论态射）。

## 三、落册与门禁

* 清单：`tasks/manifests/2026-11-25-058-batch61-terms.json`（54 行；8 条并入行单列在清单元数据外，见 §1）
* `term_flow` 干跑 54/0，实写 54；池 published=53
* 键并入 8 行：`shu-yu-biao.md` diff +62／−8；数据行 8,706→8,760（+54），`registry_azsort` 守恒
* `check_terms` 硬错误 0（自洽 0）；告警仍 148／781 两条既有账
* 唯一主形告警 emotivism／sentimentalism 已按 §2 加限定语，属故意并行

## 四、凭证

在线通道当日仍全不通，依据记「学界通行」。批 9 涉及大量「学派名 vs 主义名」的英文词形差，**术语在线镜像 0 命中**，故最需补凭证者为 `eternalism／presentism`、`Relationism／substantivalism`、`generalism／particularism` 三组——它们的中文主形在学界尚有两种流布（如 eternalism 亦作“永恒主义”、Relationism 亦作“关系主义”），通道恢复后应查权威译本与工具书再定。

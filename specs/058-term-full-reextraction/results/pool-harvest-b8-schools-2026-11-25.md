# 收割批 8：学派与思潮名缺口（2026-11-25）

批 7 之后，按同一「拆形＋单复数」口径抽 72 个学派／思潮名逐个复核，缺 23，其中语料有实际用量的 13 个登记入册。这一族与学科名同理：池的短语规则抓不到「专名式 -ism」，但译文里它们是高频标签，且直接决定「相关词条」与正文的学派归属表述。

## 一、抽样与缺口

* 抽样 72：希腊化学派、中世纪诸派、近代诸主义、当代诸转向、非西方诸派。
* 已登记 49（Stoicism、Epicureanism、Neoplatonism、Ockhamism、Cārvāka、Nyāya、Yogācāra 等）。
* 缺 23，`low_count` 为英文形在中文语料中的出现次数（含书目串，仅作量级参考）：

| 英文 | 主形 | 语料 | 处置 |
| ---- | ---- | ---- | ---- |
| Thomism | 托马斯主义 | 41 | 登记 |
| Analytic Philosophy | 分析哲学 | 48 | 登记 |
| Cambridge Platonism | 剑桥柏拉图主义 | 31 | 登记 |
| Psychoanalysis | 精神分析（亦作“精神分析学”） | 14 | 登记 |
| Renaissance Humanism | 文艺复兴人文主义 | 8 | 登记（与 humanism 人文主义分行） |
| Deism | 自然神论 | 7 | 登记 |
| Vedānta | 吠檀多（亦作“吠檀多派”） | 7 | 登记，原文列补 वेदान्त |
| Sāṃkhya | 数论（印度哲学派） | 3 | 登记，原文列补 सांख्य，与 number theory 数论（数学义）按域分用 |
| Avicennism | 阿维森纳主义 | 3 | 登记（与 Averroism 阿威罗伊主义配对） |
| Cynicism | 犬儒主义 | 2 | 登记 |
| Incompatibilism | 不相容论 | 2 | 登记（与 compatibilism 相容论对举） |
| Daoism | 道家（宗教义作“道教”） | 16＋5 | 登记，一词两义按域分义 |
| Scotism | 司各脱主义 | 2 | 登记 |
| Māturīdism／Cyrenaicism／Suárezianism／Ordinary Language Philosophy／Counter-Enlightenment／Corpuscularianism／Process Theology／Liberation Theology／Feminist Theology／Jansenism／Neopositivism | — | 0–1 | 不登记（语料无实量，留待出现再立） |

Sophism（169）不入册：语料对应的是 274 次「诡辩」（论证类型），学派义已由 `sophists 智者` 承载。

## 二、落册与门禁

* 清单：`tasks/manifests/2026-11-25-058-batch60-terms.json`
* `term_flow` 25→13 行干跑 13/0，实写 13；池 published=8
* diff 仅 +13 行（无重排）；`check_terms` 硬错误 0（自洽 0）
* 告警 148 条不变：Sāṃkhya／Vedānta 已按 jaina 批次的梵文原文惯例补 Devanagari，未新增缺原文告警
* 唯一中文主形撞形告警（Sāṃkhya／number theory 同为「数论」）系故意分域，依据栏已写明按域分用

## 三、凭证

同批 6、7：在线通道全不通，依据记「学界通行（中文语料 N 次）」，未造在线凭证。通道恢复后 `Daoism` 一朝两义的按域分用最需复核（学界亦有用「道学」统称者，本库暂不取）。

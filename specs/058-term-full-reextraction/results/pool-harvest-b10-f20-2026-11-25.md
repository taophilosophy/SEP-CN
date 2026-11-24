# 收割批 10：f20 带（池频次 20–35）＋区域／分期哲学名（2026-11-25）

用 v2 审计（强归一 + 残片黑名单，`bin/audit_zh_corpus2.py`）把池频次下限从 35 降到 20，候选 13,001，中文侧 ≥6 命中 271 行。这个带里书目串与跨词残片占比更高（`British Journal` 402、`American philosophical` 147、`Quaestiones super` 79），定性命中真缺口 36 条，另并键 3 条。

## 一、主发现：区域与分期哲学名同样整族缺位

与批 7 的学科名、批 8 的学派名同源：**哲学史的「分区—分期」标签未进册**。中文语料用量很大：中世纪 818、近代早期 77、经院哲学 81、伊斯兰哲学 64、印度哲学 59、希腊哲学 52、非洲哲学 34、阿拉伯哲学 26、日本哲学 10、拜占庭哲学 6、拉丁美洲哲学 6、拉丁哲学 4、波斯哲学 3、韩国哲学 3。

择形与分列：

| 英文 | 主形 | 处理 |
| ---- | ---- | ---- |
| Middle Ages | 中世纪 | 分期通名 |
| Late Middle Ages | 中世纪晚期 | 与 medieval 中世纪哲学（批 7）分列 |
| early modern philosophy | 近代早期哲学（亦作“早期近代哲学”） | 语料 近代早期 77／早期近代 53，主形取前者 |
| scholastic philosophy | 经院哲学 | **并入** `Scholasticism / scholastic philosophy`（同译形，不重登） |
| islamic philosophy | 伊斯兰哲学 | 与 arabic philosophy 阿拉伯哲学按原文分列 |
| arabic philosophy | 阿拉伯哲学 | 同上 |
| indian philosophy | 印度哲学 | 与 Mīmāṃsā／Nyāya 等派名成族 |
| african philosophy | 非洲哲学 | 与 sage philosophy 智者哲学（非洲语境）区分 |
| greek philosophy | 希腊哲学 | |
| byzantine philosophy | 拜占庭哲学 | |
| latin philosophy | 拉丁哲学 | 与 latin american philosophy 拉丁美洲哲学分列 |
| japanese philosophy／korean philosophy／persian philosophy | 日本哲学／韩国哲学／波斯哲学 | 语料 3–10，入册备用 |

另并两键：`Presocratic / Presocratic philosophers`、`intellectual property / intellectual property rights`。

## 二、专题术语 36 条

* 逻辑史：medieval logic 中世纪逻辑、Arabic logic 阿拉伯逻辑学（与 medieval logic 分列）、disputed questions 论辩问题（原文列补 *quaestiones disputatae*；与 dialectical question 论辩问题分域并列）。
* 宗教哲学：divine omniscience 神的全知、divine knowledge 神的知识（与 omniscience 全知、God 神的知识用法分层）、political theology 政治神学。
* 伦理学：effective altruism 有效利他主义、Kantian ethics 康德伦理学（与 Kantianism 康德主义分列）、moral foundations 道德基础。
* 美学：philosophical aesthetics 哲学美学、modern aesthetics 现代美学、aesthetic engagement 审美参与（亦作“审美介入”）。
* 其他：intentional act 意向行为、reflective knowledge 反思知识、intellectual powers 理智能力、German romanticism 德国浪漫主义、ideology critique 意识形态批判、mass culture 大众文化、literary theory 文学理论、infinite universe 无限宇宙、background independence 背景独立性、animal signals 动物信号。

## 三、落册与门禁

* 清单：`tasks/manifests/2026-11-25-058-batch62-terms.json`（36 行）
* `term_flow` 36/0；池 published=28；`shu-yu-biao.md` diff +38／−2（36 新行＋键并入），数据行 8,760→8,796（+36），`registry_azsort` 守恒
* `check_terms` 硬错误 0（自洽 0）；告警 148／781 两条既有账不变
* 唯一主形告警 disputed questions／dialectical question 已加限定语，属按域并列

## 四、剩余清单判读

271 行中未登的 235 行按族归并：书目串（British Journal、Quaestiones super、Gesammelte Schriften、Language Semantics 等）、人名残片（Pico della、Ibn Daud、Kemp Smith、Dutilh Novaes、Vander Laan、Tov Ibn Falaquera、Martini Bonadeo）、题名残片（Kant’s Theory、Aristotle’s Metaphysics、Concerning Human Understanding、Pure Theory、Principia philosophiae）、分期语与泛词（fourteenth century、everyday life、human knowledge、philosophical analysis、moral practice 已登）。三类都不宜入册；若后续要处理，应走「题名行（书名）＋人名行」的既有通道，而不是术语表。

## 五、凭证

在线通道当日仍全不通；依据记「通名（中文语料 N 次）」。区域／分期名属**描述性标签**，学界用形分歧小，风险主要在 `early modern` 一族的「近代早期 vs 早期近代」——待通道恢复后查权威哲学史译本再定主形。

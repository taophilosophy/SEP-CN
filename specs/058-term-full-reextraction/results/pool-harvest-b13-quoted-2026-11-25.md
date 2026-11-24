# 收割批 13：引号片段审计（2026-11-25）

池 `type=quoted`、登记册缺、频次 ≥12 的候选 969 条。引号片段与斜体不同：多半是正文里被引号括起的**概念词**（"principles"、"vital force"），也有强调用法（"knows"、"better"）。逐条看前 60，定出 13 条登记、2 条并入。

## 一、登记 13 条

| 英文 | 主形 | 依据 |
| ---- | ---- | ---- |
| vital force | 生命力 | 生命哲学与康德目的论（与 mechanism 机械论对举）；语料 13 |
| evil genius | 恶魔（笛卡尔 evil genius；与 demon 恶魔按原文分列） | 第一沉思 *genium malignum*；语料“恶魔”24 |
| open question argument | 开放问题论证 | 元伦理学（摩尔）；英文侧 106 |
| mind-body problem | 心身问题 | 心灵哲学；语料“心身问题”与“身心问题”各 1（两形并存） |
| fine art | 美的艺术（亦作“美术”） | 美学（Kant 美的艺术）；语料 美术 32／美的艺术 19 |
| specious present | 显似现在（亦作“似是而非的现在”） | 时间哲学（詹姆斯）；语料“显似”62 |
| divine names | 神名 | 伪狄奥尼修斯《神名论》语境 |
| rational egoism | 理性利己主义 | 与 psychological egoism 心理利己主义对举；语料“理性利己”66 |
| legal validity | 法律效力 | 法哲学；语料 25 |
| reasonable person | 理性人 | 与已登记 reasonable person standard 理性人标准分列 |
| eternal law | 永恒法 | 阿奎那法哲学（自然法、人法并列）；语料 4 |
| proximate cause | 近因 | 与 remote cause 远因、ultimate cause 终极因对举；语料 4 |
| equal respect | 平等尊重 | 与 equal concern 平等关切对举；语料 3 |
| experimental philosopher | 实验哲学家 | 与 armchair philosopher 扶手椅哲学家对举；语料 18 |

## 二、并入 2 条

* `aesthetic judgment / aesthetic judgments` ＋ `aesthetic judgement(s)`（英式拼写；语料“审美判断”241 次，原只有美式键）
* `inductive inference` ＋ `inductive reasoning`（同译“归纳推理”，审定名词库行在前）

## 三、不登的噪声

单数泛词（principles、elements、facts、rules、states、worlds）、强调性引号（knows、believe、seeing、better、normal、private）、形容词（socially constructed、causal、conceptual）、专名残片（red apple、blue、horse、star）、学科内过窄者（omni-theism、architectural objects、event horizon、supreme emergency——语料 0 次）。

## 四、门禁

* 清单 `tasks/manifests/2026-11-25-058-batch64-terms.json`（13 行）；`term_flow` 13/0，池 published=12
* `shu-yu-biao.md` diff +15／−2，数据行 8,806→8,819，`registry_azsort` 守恒
* `check_terms` 硬错误 0（自洽 0）；告警 148／781 不变
* 唯一主形告警 evil genius／demon 已按原文分列并在译法括注

## 五、凭证

在线通道仍不通，依据记「通名（语料 N 次）」。`specious present`（显似现在 vs 似现现在）、`fine art`（美的艺术 vs 美术）两处主形在学界均有流布，待通道恢复后复核。

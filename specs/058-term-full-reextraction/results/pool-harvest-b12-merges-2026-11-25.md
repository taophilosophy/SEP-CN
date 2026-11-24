# 收割批 12：同概念异拼写合并（2026-11-25）

批 9 暴露 `norm_key` 不统一连字符／空格／大小写的问题后，反向做了一次全库扫描：对**键为纯 ASCII**的术语行做强归一（`[^a-z0-9]+` 全删），同强键多行即成候选；非 ASCII 键（阿拉伯转写、IAST）不参与，因为强归一后 `aʿdād`／`ḥadd` 都会塌成 `add`。

扫描结果：8,867 行术语，ASCII 同强键组 20 组。逐组研判后**合并 7 组**，其余 13 组属「同概念不同范围」或「按域分行」，维持不动。

## 一、合并 7 组（每组合并后保留一行、删一行）

| 合并后键 | 主形 | 被并键（旧首现） | 判读 |
| ---- | ---- | ---- | ---- |
| air pump / air-pump | 空气泵（亦作“抽气机”） | air-pump（hobbes-science） | 语料 空气泵 6／抽气机 1；《利维坦与空气泵》通行题名取“空气泵” |
| Discourse on Method / Discourse on the Method | 《谈谈方法》（亦作《方法谈》） | Discourse on the Method（《方法谈》，works 批 11-24 新立） | 王太庆译本作《谈谈方法》，语料两形并用；同日重复登记，合并 |
| money pump / money-pump | 抽钱机（亦作“货币泵”） | money-pump（repugnant-conclusion） | 语料只作“抽钱机”（1 次），“货币泵”零见 |
| Port Royal Logic / Port-Royal Logic | 《波尔·罗亚尔逻辑》（国内亦称“王港逻辑”） | Port-Royal Logic（journal） | 连接号异形；两行同书 |
| truth-maker / truth maker | 使真者（亦作“真值制造者”） | truth maker（语料回收） | 语料 真值制造者 30／使真者 22；主形维持登记册既有技术形，异形入注 |
| syncategorematic word / syncategorema | 非范畴词（亦作“助范畴词”） | syncategorematic word（richard-sophister，原译“非范畴词”与保留行“助范畴词”撞概念） | 语料 非范畴词 48／助范畴词 22；合并为主形＋异形 |
| Presocratic / Presocratic philosophers / pre-Socratic | 前苏格拉底（的） | pre-Socratic（johann-sturm） | 连字符异形，同一学派名 |

配合 `j/johann-sturm.md` 正文 1 处「抽气机」改为「空气泵」（该文件为本会话试金石成果，r2_reviewed；改后 check_style strict / check_academic strict / check_math / check_terms --docs 全绿）。

## 二、维持不动的 13 组（附判据）

* **按域分行（D5）**：categorematic 形容词「范畴的」／名词行「范畴词」；dialectician 经院语境「辩证论者」与 peter-damian 术语对「辩证法家」；ideal proposition／mental proposition 的布尔丹「心灵命题」与诺里斯术语对「心理命题／理想命题」；participation「分有」与 analogy 术语对「模仿类比／分有类比」。
* **同概念不同范围**：soundness「可靠性」／arithmetical completeness/soundness「算术完全性／算术可靠性」；completeness「完全性」／modal soundness/completeness「模态可靠性／模态完全性」；final cause「目的因」／efficient/final cause「动力因／目的因」；divination「占卜」／necromancy/geomancy/divination 三词并列行；geomancy 同理；intrinsic「内在」／intrinsic-extrinsic preference「内在偏好／外在偏好」；spiritual matter「精神质料」／spiritual matter＋corporeal matter 对举行；type「类型」／Token-type 对举行。
* 这些行的既有依据栏已写明分域理由（多带 2026-11-21 FLAG 裁定），本轮不推翻。

## 三、另一份清单：同中文主形多键 159 组

`cognition／cognitio／jñāna` 同译「认知」、`definition／lakṣaṇa／taʿārīf／ḥadd` 同译「定义」、`entity／dravya／jawhar／substance` 同译「实体」……这类是**多语并行**的既有设计（同一概念在不同源语下各自立键，译形相同），不是重复；另有 3 组是「拉丁原文保留」「保留原文」的显式占位形。159 组**一律不合并**，但清单值得入库，供日后 `check_terms` 扩展「同形异语」白名单时使用。

## 四、门禁

* `shu-yu-biao.md` diff +7／−14（7 行改写＋7 行删除），数据行 8,813→8,806，`registry_azsort` 守恒
* `check_terms` 硬错误 0（自洽 0）；告警仍 148／781
* `j/johann-sturm.md` 定点四检全绿

## 五、遗留

1. 扫描脚本未入库，下轮固化 `bin/audit_strong_dup.py`（ASCII-only 键、译法冲突高亮）。
2. 同中文主形 159 组应落一份白名单（`specs/058/results/zh-homograph-allowlist.tsv`），否则每次撞形告警都要人工重判。
3. 译法冲突型重复（air pump 抽气机／空气泵）今后应由 `term_flow` 的「中文主形已存在」告警升级为**拦截**——本批 air pump（sturm 批新登「抽气机」）与 Discourse（works 批 11-24 再登《方法谈》）两处，都是同一概念二次登记、且未按告警回查既有行才出现的译形分裂。

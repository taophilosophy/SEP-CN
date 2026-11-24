# q2 逻辑一致性判据表（logic_audit）

> 工序：`q2_logic_checked`，位次在 `q1_cite_checked` 之后、`q3_grammar_checked` 之前。
> 对象：每个命题单元（以句为基本单位，复句按分句登记）的谓词-论元骨架与逻辑算子。
> 裁判：人审唯一裁决；LLM 只可产候选句对，不得作为通过证据。
> 命名纪律：本工序的“逻辑形式化”不得占用“公理”一词；`rules/axioms.json` 的 P1–P28 是管线公理，与此不同层。
> 依据：CY/T 266-2023 表 1 第 1-11 类“逻辑性、语法性差错”（句式杂糅、歧义、前后矛盾、不合事理、语句不通、表意不明，每处计 2 个差错）；ISO 24617-8:2016（DR-core 篇章关系）、ISO 24617-12:2025（QuantML 量化标注）；rules/02 语言质量表。

## 0 骨架模型（logic-skeleton.jsonl）

每句一条 JSON 记录：

```json
{"id":"p012","loc":"§2.B16","src":"All swans are white, but some birds are not.",
 "zh":"所有天鹅都是白的，但有些鸟不是。",
 "props":[
   {"pred":"white","args":[{"role":"theme","var":"x","quant":"all","restrict":"swan"}],"polarity":"+","modality":null},
   {"pred":"bird","args":[{"role":"theme","var":"y","quant":"some"}],"polarity":"+","modality":null},
   {"pred":"white","args":[{"role":"theme","var":"y"}],"polarity":"-","modality":null}],
 "discourse":"contrast","mapping":"1:1","verdict":"equivalent","reviewer":"<id>"}
```

字段：`props` 每项含谓词、论元（角色／变量／量化／限定）、极性、模态；`discourse` 取 DR-core 核心关系；`mapping` 记录源汉句对应（合句 `2:1`、拆句 `1:2`）；`verdict` 取 `equivalent`／`weakened`／`strengthened`／`drifted`／`unformalized`。

## 1 判据

| 编号 | 判据 | 判定形态 | 依据 | 级别 | 处置 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| L-1 | 命题数守恒：译句命题数等于源句命题数；合句、拆句须在 `mapping` 记录，不得增删命题 | 机检粗对齐（句数／分句数）＋人审 | ISO 24617-12 量化结构 | Critical | 增删命题即 fail |
| L-2 | 论元角色不变：施事、受事、工具、处所不得反转；主动↔被动改写须保持角色对应 | 人审 | 框架语义（ISO 24617-4 语义角色） | Critical | 角色反转即 fail |
| L-3 | 量词辖域：`all／every／any／no／some` 与“所有／每个／任何／没有／有些”一一对应；禁止 some→all、all→most、no→not all 的强弱漂移 | 机检配对初筛＋人审 | ISO 24617-12 | Critical | 强弱漂移即 fail |
| L-4 | 否定辖域：否定词位置与辖域一致；“并非所有 A 是 B”≠“所有 A 不是 B”；“没有 A 是 B”≠“有些 A 不是 B” | 机检配对初筛＋人审 | 同上 | Critical | 辖域错即 fail |
| L-5 | 条件方向：`if P then Q` 不得译成“Q 因为 P”；`unless` 不得译成“如果”；充分条件与必要条件不得互换 | 机检配对初筛＋人审 | 同上 | Critical | 方向反转即 fail |
| L-6 | 模态强度：`must／should／may／can` 对应“必须／应当／可以／能够”，不得升格或降格；`ought` 与 `must` 区分 | 机检配对初筛＋人审 | 同上 | Major | 升降格即 fail |
| L-7 | 命题态度：`believes／claims／argues／denies` 的主语与态度对象不变；不得把“X 主张 P”压成“P” | 人审 | 语义角色＋态度谓词 | Critical | 压平态度即 fail |
| L-8 | 预设与断言：定指摹状词的预设不得改写成断言；“X 停止做 P”不得译成“X 不再做 P 且 X 曾做 P”式的明示化增义 | 人审 | 预设理论 | Major | 预设断言化即 fail |
| L-9 | 并列同质：`and／or` 连接的成分须同范畴、同层级；否定与假设场景的列举用顿号不用“或”（承 rules/02 并列连词节制） | 机检（连词两侧词性粗判）＋人审 | ISO 24617-8 篇章关系 | Major | 跨范畴并列即 fail |
| L-10 | 指代链：代词与零形式的先行词唯一、可回指、在同句或近句内确定；不得出现两个候选先行词 | 人审（逐句登记） | rules/02 指代显化 | Major | 歧义指代即 fail |
| L-11 | 时间与体：过去／现在／完成／进行与时间副词一致；不得因删“曾／已”造成时点漂移，也不得保留冗余时态词（承 rules/02 时态词节制） | 人审 | 同上 | Major | 时点漂移即 fail |
| L-12 | 病句逻辑类：歧义、前后矛盾、不合事理、语句不通、表意不明——出现即判 Critical，不得带入 q3 | 人审 | CY/T 266-2023 表 1 第 1-11 类 | Critical | 一票否决 |

## 2 机检配对表（初筛，不作裁判）

| 源算子 | 允许译法 | 危险译法（出候选） |
| ---- | ---- | ---- |
| all／every | 所有、每个、一切 | 大多、多数、往往 |
| some | 有些、某些、有的 | 所有、都 |
| no／none | 没有、无一、都不 | 有些……不 |
| not all | 并非所有、不是所有 | 所有……不 |
| any | 任何、任一 | 所有（在否定／条件语境外的替换） |
| if … then | 如果……就、若……则 | 因为……所以 |
| unless | 除非、除非……否则 | 如果……不 |
| only if | 只有……才 | 如果……就 |
| must | 必须、务必 | 应该、可以 |
| should／ought | 应当、应该 | 必须 |
| may／can | 可以、可能、能够 | 必须、一定会 |
| believes | 相信、认为 | 知道（知识蕴含为更强） |
| knows | 知道、认识到 | 相信 |
| before／after | 在……之前／之后 | 因果倒置表述 |

## 3 “公理化”的操作边界

1. 只登记可判项：谓词、论元角色、量化、极性、模态、条件、态度、篇章关系。情感色彩、修辞效果不登记。
2. 不可判项标 `unformalized` 并转人审，不得用打分掩盖。
3. 骨架文件只读产出（由 draft 之外的会话生成与核对）；禁止把骨架回写成译文修改指令——修改须人审逐处执行（承 rules/05 禁机械替换）。
4. 逻辑骨架金样本（`baseline/logic-baseline.jsonl`）只作对照基准，不作自动判定模型；样本变更走 ADR。

## 4 与其他工序的分工

| 问题 | 归属 |
| ---- | ---- |
| 命题内容错、漏、增（准确性） | s1 一校 |
| 命题之间的逻辑关系（因果、转折、让步、条件） | q2（句级）＋R2（段落与跨节） |
| 句子不合语法（成分残缺、杂糅） | q3 |
| 用词不合语域（口语、文言） | q4 |
| 术语译名错 | s2.4 |
| 数字、单位、量值错 | q5 |

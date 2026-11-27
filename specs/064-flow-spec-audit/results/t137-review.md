# T137 rv-02 全局一致性记录（2026-11-27）

- 对象：`h/habermas.md`（38,150 汉字）／`tasks/h/habermas.ledger.yaml`（239 段）
- 两轴：译文轴（zh↔en 逐段）＋全局轴（结构、脚注、书目、术语、密度、语体）
- 状态：**完成**（T137 勾选；状态推进 `rv-02_checked`）

## 1 译文轴（逐段）

| 项 | 结果 |
| ---- | ---- |
| 账本段落 | 239 段；source 与 yuanwen 对应；239/239 step2 落文 |
| `scan_zh_vs_yuanwen` | `sections_zh 13／sections_yw 12`（多出 `## 脚注`，ADR-0065 正典形态） |
| `para_mismatch` | 2 处，均为 §2.1 三根支柱编号列表：源为单列表块，中文按段分行；内容逐项对应，非漏译 |
| `untranslated` | 8 个纯标签块：`**(1)**`／`**(2)**`／`**b.**`／`**c.**`／`**(3)**`／`**(D)**`／`**(U)**`／`**(D)**`；属格式行，非未译散文 |
| `ratio_flags` | 0 |
| `tail_missing` | 0 |

逐段抽核（§1–§7）见 T134 记录；T136 已处理术语混形。

## 2 全局轴

### 2.1 结构、脚注、书目

| 项 | 结果 |
| ---- | ---- |
| 尾节 | 参考文献 > 学术工具 > 其他网络资源 > 相关词条 > 脚注；`check_pairs` tail-order 0 |
| 脚注标记 | zh **156**／yw **156**；only_zh 0／only_yw 0；本轮补回 Fraser `[^fraser-1992]` 1 处 |
| 脚注定义 | zh **254**／yw **254**；only_zh 0／only_yw 0 |
| 书目 | 254 条定义照录；无重复键（`check_pairs` bib-duplicate 0） |
| 标题 | H2/H3 点号式；13 个 H2＝源 12＋`## 脚注`；无跳级（check_pairs heading-number 0） |

### 2.2 术语

- `check_terms --docs h/habermas.md`：硬错误 0；仅 `Müller-Doohm` 引用组拉丁名 1 条告警，按引用照录豁免。
- `civil society (Habermas)`＝公民社会、`legitimacy (Habermas)`＝合法性已在 T136 登记；正文统一。

### 2.3 密度与语体

| 指标 | 数值 | 判读 |
| ---- | ---- | ---- |
| 破折号 `——` | 47（约 1.23／千字） | 抽查 25 处均为插入、转折、解释；无连续堆叠或替代冒号/括号的滥用 |
| 量词“一个” | 72（约 1.89／千字） | 多为真实数量或种类（一个社会、一个句子、一个言语行为）；未见系统性填充“一个”，不批量删 |
| AI 高频词 | 层面 16、机制 12、维度 4、复杂 8；未见“彰显／赋能／梳理／勾勒” | 密度不异常；`层面` 多为“制度层面／规范层面”实义 |
| 语体 | 现代汉语学术书面语；无文言仿古、无官样套话 | 通读 §1.2、§3.3、§4.4、§7.2 抽样，结论成立 |

### 2.4 同源盲区

本会话同时承担 tr-02／tr-03／tr-04／rv-01／rv-02，无独立 actor。按 rules/04 单会话补偿：全局密度统计＋冷置回读抽样；结论记入本文件。若后续有独立审校，应优先复核 §3 商谈伦理与 §4 法哲学。

## 3 机检汇总

| 检查 | 结果 |
| ---- | ---- |
| `check_pairs h/habermas.md` | 0 issue |
| `check_style`／`check_quotes` | 0 issue／0 违例 |
| `check_academic --strict` | 无硬错误 |
| `check_math_zh`／`check_math habermas` | 0 条／formulas 0，missing 0，unbalanced 0 |
| `check_tables_images --gate` | 全库 1882 文件 0 处；habermas 无表图问题 |
| `scan_zh_vs_yuanwen` | 见 §1 |
| `check_all` | 23/23 全绿 |

## 4 结论

T137 两轴完成：译文轴 239 段守恒、标记/定义 156/254 全等、无漏译硬证据；全局轴尾节、书目、术语、密度与语体均通过；单会话盲区已按全局密度＋冷读补偿留痕。证据见本文件与 `state/t137-scan2.jsonl`。

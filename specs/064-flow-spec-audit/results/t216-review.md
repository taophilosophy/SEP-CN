# T216 证据：action tr-02 样章（§1–§2）

- 日期：2026-11-27
- 任务：T216（T155 拆站第 2 项）；范围 `en/a/action.md` 起首至 §2.4 末（源 L1–L66），不含 §3 及以后与尾节
- 条目：`a/action`；版本钉 `Jan 11, 2023／Fall 2026／81716c8b…2189`
- 方案：`results/t155-decomposition.md`
- 产出：`zh/a/action.md`（193 行／5,776 汉字；正文 5,774 汉字）；`tasks/a/action.ledger.yaml`（31 段）

## 一、结构守恒（与 en §0–§2 对齐）

| 项 | en | zh 样章 | 结论 |
| ---- | ---- | ---- | ---- |
| 非空块 | 33 | 33 | 一致 |
| 标题 | 7（H1 1＋H2 2＋H3 4） | 7（同构） | 一致 |
| 引块 | 4 | 4（另有 pubinfo 引块 1，属体例模板） | 一致 |
| 脚注标记 | 75 | 75 | 顺序与多重集均一致（逐键比对） |
| 脚注定义 | 62＋`roth-2017`（`note-1` 内引用）＝63 | 63 | 逐条与 en 定义逐字一致（空白归一后 0 差异） |
| LaTeX 公式 | 0（§1–§2 无 `$` 定界符；`S₁`／`Sₙ` 为 Unicode 下标） | 0 | 一致，无增删 |
| 链接 | 0 | 0 | 一致（25 处链接均在尾节，归 T217） |
| 列表 | 0 | 0 | 一致（4 个列表项在 §3 以后，归 T217） |
| 引用块内容 | 戴维森 2 段、一般形式 1 段、Setiya 1 段 | 4 段全译 | 一致 |

块类型序列（去掉 H1／pubinfo 后 31 段）英中逐段同型：`PPPHPPPPHPHPPHPPHPPHPQPQPQPQPPP`。

## 二、机检

| 检查器 | 结果 | 说明 |
| ---- | ---- | ---- |
| `check_style.py` | 0 issue | 弯引号、引号空格、加粗空格、中西文空格、中文斜体均无告警 |
| `check_quotes.py` | 0 处 | 无直角引号／直引号 |
| `check_math_zh.py` | 0 文件有问题，硬错误 0 | §1–§2 无公式 |
| `check_terms.py --docs` | 硬错误 0；本文件疑似缺译法 0 | 13 条新登记术语均已在正文落地 |
| `check_academic.py --docs --strict` | OK，硬错误 0 | 非存根词条 1／在途豁免 1 |
| `check_pairs.py` | 4 条 | 均为样章范围缺口，见下 |
| `check_prose.py` | 16 条 | long-sentence 11／de-chain 4／weak-verb 1；归 T218 tr-04 处置 |

`check_pairs` 的 4 条缺口：

1. `cite-authoryear`：正文“Wu 2016”在 en 书目有对应条目，样章书目未含（该条在 References 尾节）。
2. `count-vs-source`：节标题 7 vs 31（样章只含 §1–§2）。
3. `count-vs-source`：书目 63 vs 314（样章只含样本所引脚注定义）。
4. `tail-order`：尾节缺失（参考文献、学术工具、其他网络资源、相关词条），归 T217。

以上均为 T216 既定范围，不是缺陷；T217 全量后应清零。

## 三、术语登记（先登记后用）

在 `zh/shu-yu-biao.md` 新增 13 行（`registry_azsort.py --apply` 归位；人名表重排副作用已还原，无改动）：

| 键 | 译法 | 依据 |
| ---- | ---- | ---- |
| causalism | 因果论 | 学界通行；与“非因果论”对举 |
| causal theory of action | 行动因果论（亦作“行动的因果理论”） | 学界通行；戴维森行动哲学 |
| standard story of action | 行动的标准故事 | Velleman 1992 命名 |
| accordion effect | 手风琴效应 | 构词直译（Feinberg 1965）；中文哲学文献检索无对口固定译名 |
| causal deviance | 因果偏离 | 与已登记 `deviant causal chain`＝偏离的因果链 同族 |
| primary deviance | 原发偏离 | 与 secondary deviance 对举 |
| secondary deviance | 继发偏离 | 同上 |
| agent causation (philosophy of action) | 行动者因果性 | 与 `agent causality` 同概念；中文文献有“行动者因果性理论”用例；与中世纪 `agent causation / exemplar causation` 同形异义分立（撞形豁免） |
| extended action | 延展行动 | 学界惯例（布拉特曼）；构词直译 |
| action individuation | 行动个体化 | 学界通行（戴维森论题） |
| intentional explanation | 意向解释 | 学界惯例；与“合理化解释”同族 |
| rationalization (action) | 合理化 | 戴维森行动理论通行 |
| sustaining cause | 维持性原因 | 构词直译；与“先行原因”对举 |

联网凭证（2026-11-27，Tavily）：

- 《理由、原因与行动》，全国哲学社会科学工作办公室：<http://www.nopss.gov.cn/n/2013/0423/c362294-21249685.html>（戴维森“合理化解释是一类因果解释”、reason 与 cause 关系；中文文献亦用“基本理由”指 primary reason，本库从登记册作“首要理由”）。
- 徐向东《论行动者因果性理论的不连贯性》：<http://hksh.site/macaufilosofia/2006/xuxiangdong.pdf>（“行动者因果性”学界用例）。
- “延展行动”“手风琴效应”“因果偏离”检索未获中文哲学文献固定译名，按构词直译登记；“手风琴效应”为 Feinberg 1965 的比喻命名（原文自带说明）。

已登记并直接沿用：`action`＝行动、`intentional action`＝意向行动、`primary reason`＝首要理由、`practical knowledge`＝实践知识、`basic action`＝基本行动、`proximate cause`＝近因、`logical connection argument`＝逻辑关联论证、`deviant causal chain`＝偏离的因果链、`teleological explanation`＝目的论说明、`omission`＝遗漏、`constitutive aim`＝构成性目的。

## 四、源文瑕疵观察（转 T217／勘误轮）

样章翻译中发现 3 处 T215 机检未覆盖的上游瑕疵，均按零信任照录，尚未改勘误表：

| 位置 | 上游原文 | 观察 |
| ---- | ---- | ---- |
| §1 第 3 段（en L18） | `Mele. 2010` | 排印手误，疑为 `Mele 2010` |
| 脚注 `note-2`（en L475） | `a primary reason the explains the action` | 疑为 `that explains` |
| 脚注 `davidson-1970b`（en L188） | `P*hilosophy of History and Action*` | 斜体标记错位，疑为 `*Philosophy of History and Action*` |

T217 建尾节与译注时一并定性：纯排版者只入勘误表，文字缺陷者按 ADR-0076 加译者注释。

## 五、结论

T216 满足验收：样章块类、标题、引块、脚注标记与定义、公式与链接均与 en 样本守恒；13 条术语先登记后用；定点机检无硬错误。样章范围缺口 4 条留待 T217 全量收口。

下一步：T217 全量（§3–§8＋尾节＋320 脚注，分 3 批 checkpoint），建全量账本并补 `project_spec`／`pe`，完成后 `advance --step tr-02`。

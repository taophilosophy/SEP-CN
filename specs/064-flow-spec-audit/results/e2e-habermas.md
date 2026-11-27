# E2E 试金石：h/habermas

- 任务：`tasks/h/habermas.json`｜kind retranslate｜state **cleared**（正文 86 字节＝仅 H1）
- 版本钉：pubinfo 2023-09-15／archive Spring 2026／sha256 `8f15af6e…be32`
- 源文件：`en/habermas/index.html`（单文件，无 notes.html）
- 体量（060 §5.4 记录）：105,946 字符／37,025 汉字；247 脚注、37 个三级标题
- 起跑：2026-11-26

## 22 节点覆盖表（另列非节点动作）

> 旧版称“22 站记录”但只有 18 行，且把置空／发布混入节点。现按 pipeline 的 22 个节点逐行；非节点动作另表。状态只允许：已执行、复用待核、未执行、N/A（附理由）。不得用“通过”代替证据。

| # | 节点 | 阶段 | 状态 | 证据／说明 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | ex-01 抓取与版本钉 | 1.2.1 | 复用待核 | `en/habermas/index.html` 与 pin 已存在；尚未在本次记录中重放校验 |
| 2 | ex-02 转 Markdown | 1.2.2 | 复用待核 | `yuanwen` 存在；须补 I2／补丁命中凭证 |
| 3 | ex-03 保真校验 | 1.2.3 | 复用待核 | 须给 `check_yuanwen_fidelity` 结果与时间 |
| 4 | ex-04 源审计 | 1.3.3 | **部分执行** | 机器面 hard=0／warn=5；候选人工定性未完；见下 |
| 5 | ex-05 格式闭合 | 1.3.4 | 未执行 | 本次未记录；不得由 rv-09 代替段内闭合 |
| 6 | tr-01 预处理 | 2.1 | **样章已执行** | T132：术语/勘误注入见 `tasks/h/habermas.ledger.yaml` 与 `results/c-group-evidence.md` |
| 7 | tr-02 初译 | 2.2 | **样章完成** | T132：§1–§2 样章约 2,350 汉字；T133 全量未启动 |
| 8 | tr-03 一校 | 2.3 | 未执行 | — |
| 9 | tr-04 二校 | 2.4 | 未执行 | — |
| 10 | tr-05 段内格式 | 2.5 | 未执行 | — |
| 11 | rv-01 术语与勘误 | 3.1 | 未执行 | — |
| 12 | rv-02 全局一致性 | 3.2 | 未执行 | — |
| 13 | rv-03 引文 | 3.3 | 未执行 | — |
| 14 | rv-04 逻辑 | 3.4 | 未执行 | — |
| 15 | rv-05 语法 | 3.5 | 未执行 | — |
| 16 | rv-06 语域 | 3.6 | 未执行 | — |
| 17 | rv-07 计量 | 3.7 | 未执行 | — |
| 18 | rv-08 标点 | 3.8 | 未执行 | — |
| 19 | rv-09 体例终校 | 3.9 | 未执行 | — |
| 20 | sg-01 初审 | 4.1 | 未执行 | — |
| 21 | sg-02 复审 | 4.2 | 未执行 | — |
| 22 | sg-03 终审 | 4.3 | 未执行 | 须用户另行 `--mandate` |

**非节点动作**

| 动作 | 状态 | 证据 |
| ---- | ---- | ---- |
| 置空（cleared） | 已执行 | 状态为 cleared；正文 86 字节＝仅 H1；ADR-0081 全库置空为历史事实 |
| 发布 | 未执行 | 终审前不得发布 |

> 结论：本件只完成 ex-04 的机器扫描，**不是 22 站完成，也不是全流程通过**。源侧前置节点若复用，须补原时点、版本钉与结果位置；否则按未执行处理。

## ex-04 站明细

### 机器面

| 检查 | 结果 |
| ---- | ---- |
| `en_integrity habermas` | `problems: []`（零问题）；凭证 `results/e2e-habermas-en-integrity.json` |
| `en_source_audit habermas` | `hard: []`；`warn: 5`；`info: 0`；凭证 `results/e2e-habermas-source-audit.json` |
| 计数 | entry_links 15、external_links 12、math_inline 0、math_display 0、tables 2、headings 49 |

### warn 五项（typo 候选，待定性）

| # | kind | token | 定性初判 | 依据 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | word_digit_eq | `sum2023` | **误报** | `archives/sum2023/` 是存档 URL 片段，非正文文字 |
| 2 | doubled_word | `Discourse … Discourse` | **待核** | 疑为三级标题（3.1 Discourse）与正文首词相接，非真重复；需看原文 |
| 3 | digit_for_letter | `80s` | **误报** | “the late 80s and early 90s” 属规范年代缩写（GB/T 15835） |
| 4 | digit_for_letter | `90s` | **误报** | 同上 |
| 5 | punct_run | `,,` | **疑似真 typo** | `Ritus”,, translated` 双逗号，需回原文确认 |

**误报率初判**：5 项中 3 项确定误报（60%），1 项待核，1 项疑似真错。这是判据质量问题，不是本件质量问题。

## 本件 findings

| # | 发现 | 类型 | 阻断 | 证据 |
| ---- | ---- | ---- | ---- | ---- |
| F1 | `en/habermas/` 仅 `index.html`，无 notes.html；而 060 §5.4 记该件 247 脚注——脚注内嵌于同页，非缺件 | 观察 | 否 | `ls en/habermas/` |
| F2 | `en_source_audit` 的 typo 候选误报率高（3/5 确定误报），URL 存档片段与年代缩写是系统性误报源 | **判据缺陷** | 否 | 本表 warn 五项 |
| F3 | **ex-04 的“人工定性”环节无成文豁免清单**：URL 片段、年代缩写、标题接正文三类常见误报未成文 | 文档缺口（G13） | 否 | **2026-11-26 已落 `rules/11` §5.3 A–E；本件尚未逐条按清单复核，故 T130 仍未完成** |
| F4 | 报告中“22 站”与实际执行面不完全对应：仅 18 行，缺 ex-01／02／03／05、tr-01、tr-05 | 表述缺陷 | 否 | **已改为 22 节点表＋非节点动作；旧“22 站完成”结论撤销** |

## 下一站的前置

tr-02 初译涉及 37,025 汉字的正文与 247 条脚注，单轮无法完成。需按节分批：先完成 §1–§2 作为样章，验证账本与写作口径，再全量推进。**在批次划分与样章验收前，不进入 tr-02。**

## T130 人工定性（2026-11-27，用户已批准）

> 依据：`rules/11-source-side.md` §5.3 A–E 类；候选取自 `results/e2e-habermas-source-audit.json`（`slug: habermas`，`checked_at 2026-11-25T21:38:53Z`，hard 0／warn 5／info 0）。回源对象 `en/habermas/index.html`（只读），行号为该文件行号。

### 三段摘要

1. **候选总数：5**（warn 5；hard 0、info 0，与 JSON 一致）。
2. **豁免类计数**：A（存档与 URL 片段）1、B（年代与数字缩写）2、C（标题接正文）1、D（标点连串）1、E（外链失效）0。其中 A/B/C 共 4 项按 §5.3 豁免、不计缺陷；D 类不豁免，属真候选。
3. **逐条定性结论**：真候选 **1**（`,,`，D 类，回原文确认系排印手误）；误报 **4**（A 1＋B 2＋C 1）；待核 **0**。本表 5 候选内缺陷计数净增 1 条（文字层）；另经用户 2026-11-27 批准补录 `Empitical` 1 条（不计入 5 候选）。两条均按 ADR-0062 走全局勘误表＋中文译注，`en/` 零改动。

### 逐条定性表

| # | 候选 | 类 | 定性 | 依据 | 处置 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | `sum2023`（`word_digit_eq`） | A 存档与 URL 片段 | **误报** | HTML L4867：`&lt;<a href="https://plato.stanford.edu/archives/sum2023/entries/habermas/">https://plato.stanford.edu/archives/sum2023/entries/habermas/</a>&gt;`（Other Internet Resources，L4860 起；同句另有 `(Summer 2023 Edition)`，L4865–4866）。`sum2023` 为存档路径片段，非正文文字 | 豁免，不入勘误表；记录“命中 A 类、判为误报” |
| 2 | `Discourse … Discourse`（`doubled_word`） | C 标题接正文 | **误报** | HTML L1577 `<h3 id="Disc">3.1 Discourse</h3>`，L1579–1580 `<p>` 换段后正文首句 `Discourse is not a synonym for language or speech.`。重复关系来自“标题末词＋正文首词”，非正文重复。JSON token 原文含换行：`Discourse \n\n \nDiscourse`；ctx 为 `… 3.1 Discourse \n\n \nDiscourse is not a synonym for language or speech` | 豁免（回原文确认后判误报）；建议 `en_source_audit` 后续屏蔽“标题末词＝段落首词”形态 |
| 3 | `80s`（`digit_for_letter`） | B 年代与数字缩写 | **误报** | HTML L2120：`researched the book in the late 80s and early 90s, political theory`（§4 首段，L2116 起） | 豁免（GB/T 15835 年代缩写规范用法）；不入勘误表 |
| 4 | `90s`（`digit_for_letter`） | B 年代与数字缩写 | **误报** | 同上句 HTML L2120（同一短语 `the late 80s and early 90s`） | 豁免，同上 |
| 5 | `,,`（`punct_run`） | D 标点连串 | **真候选（真 typo）** | HTML L4199–4201：`<li>chapter 3, &ldquo;Eine Hypothese zum gattungsgeschichtlichen Sinn` / `des Ritus&rdquo;,, translated as &ldquo;A Hypothesis concerning the` / `Evolutionary Meaning of Rites&rdquo;, 43&ndash;56.</li>`（Bibliography › Works by Habermas，L3561 起；父条 2012 [2017] 见 L4192–4195）。`&rdquo;` 后紧接两个逗号，而姊妹子条 chapter 4 作 `&rdquo;, translated as`（L4203–4205，单逗号），chapter 6 作 `&rdquo; translated as`（L4208–4209，无逗号） | **真 typo**：入全局勘误表＋中文译注；`en/` 不改（ADR-0062），`yuanwen/h/habermas.md` L823 照录双逗号；建议勘误行要素见下 |

### 第 5 条勘误行（已写入 `baseline/en-errata/en-errata.md` 第十三节；另附 `Empitical` 条）

按 `baseline/en-errata/en-errata.md` §“入表格式（第八节起）”七列：

| slug | 位置 | 上游原文 | 缺陷定性 | 参考读法 | 中文承载 | 凭证 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| habermas | Bibliography › Works by Habermas（`#WorkHabe`，L3561）› 2012 [2017]《Nachmetaphysisches Denken II》条子项 chapter 3（HTML L4199–4201；yuanwen `h/habermas.md` L823，脚注键 `eine-nd-3`） | `des Ritus”,, translated as` | ①（排印手误） | `des Ritus”, translated as`（单逗号） | 该脚注条目按单逗号呈现；译注落同条句内，形如 `（译注：上游原文此处作双逗号“”,,”，系排印之误。）`，具体措辞由 tr-04／rv-01 定 | 同页姊妹子条 chapter 4（L4203–4205）、chapter 6（L4208–4209）均无连串逗号；`en/` 冻结不改，`yuanwen` 忠实照录 |

### 附带发现（不计入本表 5 候选）

* HTML L4179–4181 `Theory on Empitical Research` 疑为 `Empirical` 之误（①排印手误），`en_source_audit` 未产出该候选（拼写类不在其检出范围）。已按用户 2026-11-27 批准另立勘误条，见 `baseline/en-errata/en-errata.md` 第十三节；本表 5 行仍与 JSON warn 一一对应，不因该观察改动计数。

状态：T130 已完成（2026-11-27 用户全部批准：5 候选定性、`,,` 入表、`Empitical` 另立勘误条）

用户批准：2026-11-27（本轮指令“全部批准后继续B组”）

# 收割批 7：学科与分支名缺口（2026-11-25）

批 6 的审计暴露一个结构性现象：**学科名整族未登记**。术语表此前收的是词条内的专门术语，而 `philosophy of mind`、`philosophy of science` 这类分支学科名散见于正文与「相关词条」栏，既未进候选池（池按词频与短语规则生成），也未人工补登。本批逐条以「登记册拆形＋单复数复核」确认缺位，再以中文语料频次择形。

## 一、缺口与择形

| 英文 | 主形 | 中文语料 | 备注 |
| ---- | ---- | ---- | ---- |
| philosophy of science | 科学哲学 | 163 | |
| philosophy of mathematics | 数学哲学 | 152 | |
| philosophy of religion | 宗教哲学 | 96 | |
| philosophy of mind | 心灵哲学 | 94（心智哲学 2） | 异体入注 |
| philosophy of language | 语言哲学 | 79 | |
| philosophy of biology | 生物学哲学 | 93 | |
| philosophy of law | 法哲学 | 41 | 与 `philosophy of right`（黑格尔语境）同译形，按原文词分列 |
| philosophy of history | 历史哲学 | 40 | |
| philosophy of logic | 逻辑哲学 | 28 | 不取「哲学逻辑」：语料仅 1 次，且 `philosophical logic` 的 83 次多为 *Journal of Philosophical Logic*／*Handbook of Philosophical Logic* 刊名书名 |
| philosophy of physics | 物理学哲学 | 11 | |
| philosophy of action | 行动哲学 | 18 | |
| metaethics | 元伦理学 | 51（元伦理） | |
| normative ethics | 规范伦理学 | 22 | |
| applied ethics | 应用伦理学 | 11 | |
| bioethics | 生命伦理学 | 41（生命伦理） | 与医学伦理学分列 |
| social philosophy | 社会哲学 | 35 | |
| political theory | 政治理论 | 105 | 与 political philosophy 政治哲学行分列，按原文用词取形 |
| political science | 政治学 | 82 | 与书名行《政治学》（Politics）不冲突 |
| jewish philosophy | 犹太哲学 | 107 | |
| feminist philosophy | 女性主义哲学 | 31 | 「女性主义」本库统一形 |
| medieval philosophy | 中世纪哲学 | 79 | |
| modern philosophy | 近代哲学（亦作“现代哲学”） | 32／58 | 主形从本库分期惯例 |
| contemporary philosophy | 当代哲学 | 58 | |
| history of philosophy | 哲学史 | 231 | |
| theoretical computer science | 理论计算机科学 | 5 | |

## 二、落册与门禁

* 清单：`tasks/manifests/2026-11-25-058-batch59-terms.json`
* `term_flow` 干跑 25/0，实写 25；池 published=13
* `registry_azsort --apply` 写回后与现状 diff 仅 +25 行（无重排），数据行 8,668→8,693，守恒
* `check_terms` 硬错误 0（自洽 0）；告警仍为 148／781 两条既有账，未因本批变动
* 告警两条已核对非撞形：`philosophy of law`／`philosophy of right` 同中文形而原文词不同，按原文词分列；`political science` 与 `Politics` 之别是书名号剥离造成的假撞形

## 三、为什么池没抓到这一族

候选池生成规则偏「术语」（名词短语、词频、共现），学科名多为「of 结构」的轻短语，且大量出现于参考文献与「相关词条」栏，被当作书目噪声或泛词过滤。**改法**：在 `bin/reextract.py` 的短语判定里为 `philosophy of X`／`X ethics`／`X philosophy` 三类加白名单通道，下一轮重扫时把学科名单独成表，与术语表分开维护（学科名桩位稳定，长期不动）。

## 四、凭证

同批 6：术语在线本地镜像精确命中 0 条，在线通道当日全不通（bingweb 0 命中、duckduckgo／brave 10060、exa 待授权、glm 无 key）；依据记「学科通名（中文语料 N 次）」，未造在线检索凭证。通道恢复后须为 `philosophy of logic 逻辑哲学`／`modern philosophy 近代哲学` 两处主形之争补凭证。

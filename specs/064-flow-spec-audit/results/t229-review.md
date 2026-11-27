# T229 ex-04 源审计：newton-principia

- 日期：2026-11-27
- 对象：`en/n/newton-principia.md`（165,995 B／538 行）；`html/newton-principia/index.html`、`notes.html`、`fig1–3.jpg`
- 版本钉：`pubinfo_date: Dec 20, 2007`；`archive_edition: Winter 2024`；`sha256: 05a4a2b2…6f38`
- 依据：`rules/11-source-side.md` §2–§5、`results/t157-decomposition.md`、`rules/04` 状态机

## 一、机检面

| 项 | 命令 | 结果 |
| ---- | ---- | ---- |
| 英文镜像完整性 | `en_integrity.py newton-principia` | audited 1、clean 1、hard 0；mathjax 0、math_inline 0、math_asset 0 |
| 源审计 | `en_source_audit.py newton-principia` | hard 0、warn 3、info 0；counts：entry_links 9／external_links 11／math_inline 0／math_display 0／tables 1／headings 21 |
| 公式 | `check_math.py --docs en/n/newton-principia.md` | checked 0、formulas 0、missing 0、unbalanced 0 |
| 资产闭包 | `fetch_audit.py newton-principia` | complete 1／assets 4／missing 0／fixed 0 |

## 二、候选定性（三段式）

**候选总数**：3（全部为 warn；hard 0、info 0）。

**豁免类计数**：A–E 类 0；结构类 false-positive 2。

**逐条结论**：

| # | 候选 | 定性 | 依据 |
| ---- | ---- | ---- | ---- |
| 1 | `heading_skip`（h2→h4） | **false-positive** | HTML 中 4 处 `<h4>` 均为页面模板（Browse／About／Support SEP／Mirror Sites，index.html L3217–3252），非正文；正文标题为 H1→H2→H3 连续。不计缺陷。 |
| 2 | `orphan_note`（note-1…note-40 截断清单） | **false-positive（工具口径）** | 上游锚点写作 `<a href="notes.html#1" name="note-1">1</a>`（index.html L269 起），href 片段为数字 `#1`，审计按 `#note-1` 匹配失败；en 镜像 59/59 编号注引用闭合（见 §三）。不计缺陷。 |
| 3 | `typo_candidate`：`pp. 31-70..` | **真候选（D 类标点连串）** | 位于文献 `smith-2002`（en L522；html index L3084）。属条目末重复句点，定性①纯排版；参考读法 `pp. 31-70.`；入勘误第十九节，中文书目照录，无需译注。 |

## 三、脚注键闭合

- 定义合计 **96**＝编号注 **59**（`note-1`–`note-59`）＋文献键 **37**。
- 编号注：59 条定义／59 处引用，逐键闭合，无悬空、无缺定义。
- 文献键：37 条定义；正文实际引用 2 条（`stein-1967`、`aiton-1972`）；其余 35 条为书目条目（References 节说明“完整条目见文末脚注定义”），按设计无文内引用。
- `[^key]`（References 引块内，en L320）为说明性文字中的字面示例，非引用标记。
- 特殊注：`note-2`／`note-3` 讨论 Cohen-Whitman 英译的译名取舍并引拉丁原文，T231 须保留拉丁原句与引号形态。

## 四、图资产闭包

| 文件 | 基线 SHA-256（前 8 位） | 实测 | 闭包 |
| ---- | ---- | ---- | ---- |
| `html/newton-principia/index.html` | 05a4a2b2 | 一致 | 主文件 |
| `html/newton-principia/notes.html` | 31a11a86 | 一致 | 注文件 |
| `fig1.jpg` | 3be9c808 | 一致 | 引块内（en L130） |
| `fig2.jpg` | d44f4cf0 | 一致 | 引块内（en L174） |
| `fig3.jpg` | 64a58bf2 | 一致 | 行内＋同行图注（en L254） |

- 根 `assets/newton-principia/` 三图在位（18,566／20,634／57,108 B），与 html 同名同尺寸；`fetch_audit` 闭包 complete、缺件 0。
- 译文引用路径拟为 `../../assets/newton-principia/figN.jpg`（zh/n/ 相对根 assets）。

## 五、版本钉与 pubinfo

- `index.html` SHA-256＝`05a4a2b2ef2bbca8eda188bc2bc705767bb7183f6132cfc05adfa316a3ee6f38`，与 `tasks/n/newton-principia.json` 及 `baseline/entries.json` 一致。
- `baseline/entries.json`：`first_published: Dec 20, 2007`；`substantive_revision: null`；`archive_edition: Winter 2024`；`latest_change_type: minor correction`。
- HTML `pubinfo` 仅“First published Thu Dec 20, 2007”，无实质修订行；中文 pubinfo 拟作 `> *首次发表于 2007 年 12 月 20 日。*`（无修订日期）。

## 六、14 类构件复核

| # | 构件类 | 计数 | 与拆站方案一致 |
| ---- | ---- | ---- | ---- |
| 1 | H2 | 15 | 一致 |
| 2 | H3+ | 2（空节） | 一致 |
| 3 | 脚注定义 | 96（59＋37） | 一致 |
| 4 | 链接 | 12（9 文本＋3 图） | 一致 |
| 5 | 图片 | 3 | 一致 |
| 6 | 表格块 | 1（5 行／4 内容行） | 一致 |
| 7 | 引块 | 23 块／36 行 | 一致 |
| 8 | 列表项 | 3 | 一致 |
| 9 | 嵌套列表 | 0 | 一致 |
| 10 | 行内公式 | 0 | 一致 |
| 11 | display 公式 | 0 | 一致 |
| 12 | LaTeX 环境 | 0 | 一致 |
| 13 | 代码块 | 0 | 一致 |
| 14 | 加粗 | 58 | 一致 |

命中 9／14，与 `t157-decomposition.md` §二一致；译文不得新增构件。

## 七、G13 结论

- 2 条结构告警均为 false-positive，不属 A–E 类，无需建豁免清单。
- 1 条 typo 候选属 D 类，按真候选处理：入 `baseline/en-errata/en-errata.md` 第十九节（纯排版，无需译注）。
- 无静默跳过；所有候选均在本表有逐条结论。

## 八、结论与移交

1. hard 0；3 条 warn 全部定性；脚注 96 定义闭合；3 图资产齐备；版本钉一致；14 类计数与拆站方案一致。
2. 可进入 T230（tr-02 样章：导论＋§1，13,010 源字符）。
3. 移交事项：T231 注意 `note-2`／`note-3` 译名说明与拉丁原文、35 条书目键照录；T233 q1 引文轴覆盖 23 引块与 2 条文献键引用。

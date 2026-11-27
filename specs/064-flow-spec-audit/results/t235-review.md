# T235 ex-04 源审计：logic-dynamic

- 日期：2026-11-27
- 对象：`en/l/logic-dynamic.md`（64,581 B／575 行）；`html/logic-dynamic/`（index.html、local.js、model1/2.png）
- 版本钉：`pubinfo_date: Feb 16, 2023`；`archive_edition: Fall 2023`；`sha256: bb7c36ae…5cf9`
- 依据：`rules/11-source-side.md` §2–§5、`results/t158-decomposition.md`

## 一、机检面

| 项 | 命令 | 结果 |
| ---- | ---- | ---- |
| 英文镜像完整性 | `en_integrity.py logic-dynamic` | clean 1／hard 0；MathJax 1、math_inline 1 |
| 源审计 | `en_source_audit.py logic-dynamic` | hard 0、warn 5（typo_candidate 5）；counts：entry 6／external 10／math_inline 666／math_display 4／tables 5／headings 20 |
| 资产闭包 | `fetch_audit.py logic-dynamic` | complete 1／assets 3／missing 0 |
| 公式口径 | 逐段计数 | en markdown 行内 `$…$` 604、display 4 对；HTML 数学跨度 666／4 |

## 二、候选定性（三段式）

**候选总数**：5（全部 `typo_candidate`；hard 0、info 0）。

**豁免类计数**：A–E 类 0；结构／工具口径 false-positive 4；真候选 1。

**逐条结论**：

| # | 候选 | 定性 | 依据 |
| ---- | ---- | ---- | ---- |
| 1–4 | `sat   sat` ×4 | **false-positive** | HTML 列表 `<li>\(M,x\) sat \(p\)</li>` 等相邻短项在剥离数学后连成 “sat sat”；非正文重复词。 |
| 5 | `and   and` | **真候选（①语法／排印）** | §4.3（en L364）“where A0=p and π0=π and proved that…” 第二处 `and` 后缺主语，参考读法 `and they proved that`；中文译作“并证明了”，语义自足；入勘误第二十节。 |

## 三、脚注键闭合

- 定义 55；真实文内引用 0；`[^key]`（References 说明行）为字面示例，非引用。
- 55 条均为书目键定义（54 条正文未引 + 1 条对应 `[^key]` 说明所指），按设计无文内引用；条目结构与 newton-principia 同类。
- References 说明称“文内作者-年份引用组后附 `[^key]` 标记”，但正文未实际出现标记；属上游书目转换形态，登记备查，不改 `en/`。

## 四、图资产闭包

| 文件 | 基线 SHA-256（前 8 位） | 实测 | 备注 |
| ---- | ---- | ---- | ---- |
| `index.html` | bb7c36ae | 一致 | 主文件；版本钉 |
| `model1.png` | a53bc073 | 一致 | §2.1 图 1（32,056 B） |
| `model2.png` | 19690701 | 一致 | §2.1 图 2（76,763 B） |
| `local.js` | 875f6d9b | 一致 | 仅 `\ldquo`／`\rdquo` 两宏 |

- 根 `en/assets/logic-dynamic/` 两图在位；`fetch_audit` 闭包 complete、缺件 0。
- 译文引用路径拟为 `../../assets/logic-dynamic/modelN.png`。

## 五、版本钉与 pubinfo

- `index.html` SHA-256＝`bb7c36ae9f82ba0c7e5bc8c15382ff1572a79e9e3f394bfbff59677efdb35cf9`，与任务及 `baseline/entries.json` 一致。
- `first_published: Feb 1, 2007`；`substantive_revision: Feb 16, 2023`；`archive_edition: Fall 2023`。
- 中文 pubinfo 拟作 `> *首次发表于 2007 年 2 月 1 日；实质修订于 2023 年 2 月 16 日。*`

## 六、14 类构件复核

| # | 构件类 | 计数 | 与拆站方案一致 |
| ---- | ---- | ---- | ---- |
| 1 | H2 | 9 | 一致 |
| 2 | H3+ | 10 | 一致 |
| 3 | 脚注定义 | 55 | 一致 |
| 4 | 链接 | 33（含图 2） | 一致 |
| 5 | 图片 | 2 | 一致 |
| 6 | 表格块 | 5 块／40 行 | 一致 |
| 7 | 引块 | 6 行 | 一致 |
| 8 | 列表项 | 44 | 一致 |
| 9 | 嵌套列表 | 0 | 拆站“待复核”→实测 0 |
| 10 | 行内公式 | 604（audit 666） | 口径差异见 §一 |
| 11 | display 公式 | 4 对 | 一致 |
| 12 | LaTeX 环境 | 0 | 一致 |
| 13 | 代码块 | 0 | 一致 |
| 14 | 加粗 | 16 | 一致 |

命中 12／14；无嵌套列表、LaTeX 环境与代码块。

## 七、G13 结论

- 4 条 `sat sat` 为工具口径 false-positive，不属 A–E 类，无需建清单。
- 1 条 `and and` 为真候选，按①语法／排印处理，入勘误第二十节。
- 无静默跳过。

## 八、结论与移交

1. hard 0；5 条 warn 全部定性；55 脚注定义闭合；2 图资产齐备；版本钉一致。
2. 可进入 T236（tr-02 样章：§1＋§2.1）。
3. 移交：T236 注意 `\ldquo`／`\rdquo` 宏与两幅模型图；T237–T239 公式密度高，逐批跑 `check_math_zh`；T240 处理 55 条书目键与 Academic Tools 表。

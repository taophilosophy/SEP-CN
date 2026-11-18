# SEP 词条 HTML 模板契约（正典）

**地位**：本文是 SEP 词条 HTML 模板契约的**唯一正典**（ADR-0076，specs/053 P0 汇编）。来源：specs/001 spec.md 顶部“网站结构事实基础”（2026-10-26 九词条抽样，历史记录保留原文）＋ `tools/parser.py` 契约 ＋ specs/044 B0 十谓词 ＋ specs/039 结构实测基线（2026-11-16 全库扫描）。修订走 ADR。

**求值视图**：一切“模板是否符合契约”的判定都在 `en ⊕ baseline/en-patches/`（转换输入）上求值——补丁修的正是使 HTML 可解析的格式层缺陷，在原始字节上判会把已热修缺陷误报为失败（specs/044 §1.0，ADR-0073 同源对照条）。

## 1. 词条包形态

- `en/<slug>/index.html`：词条正文页（顶层平铺 slug 目录，无字母层）。
- `en/<slug>/notes.html`：脚注正文独立文件；404 为正常缺省形态。
- 补充材料：词条目录下任意命名 `.html`（如 set-theory 的 `basic-set-theory.html`）。
- 图片：`<div class="figure">` 内 `<img src="imageN.jpg">`，词条目录相对路径文件。
- 数学宏：`en/<slug>/local.js`（MathJax 2.7.2 全 TeX 源码，零 MathML）。
- 引用闭包由 `tools/en_integrity.py` 全命名空间解析（包完整性面，不并入模板契约判定）。

## 2. 正文结构契约

| 元素 | 契约 |
| ---- | ---- |
| 正文界定 | `<!-- BEGIN ARTICLE HTML -->` 与 `<!-- END ARTICLE HTML -->` 注释 |
| 版本元数据 | `<div id="pubinfo"><em>First published …; substantive revision …</em></div>`（旧模板条目 pubinfo 形态存在变异，见 §9） |
| 题名元数据 | `<meta name="citation_title">` |
| 分节 | `<h2><a id="锚">N. 标题</a></h2>`（h2/h3/h4 嵌套，节号 `N[.M[.K]]`），与 `<div id="toc">` 一一对应 |
| 结尾 | 固定 Related Entries；作者/版权在 `<div id="article-copyright">` |

## 3. 数学

- 行内 `\(...\)`、行间 `\[…\]`；少量 `$$..$$` 与 LaTeX 环境；MathJax 客户端渲染。
- MathJax **不支持嵌套定界符**（`\text{…\(…\)` 类嵌套为上游文字层缺陷，勘误表 §十 三族先例）。

## 4. 表格与图

- 表格常嵌于 `<blockquote><table>` 内承载编号定义/公式。
- 图注 `<span class="figlabel">Figure N</span>`；部分图注 "reprinted with permission"。

## 5. 脚注

正文引用形如 `<sup>[<a href="notes.html#N">N</a>]</sup>`，与 `notes.html` 内定义一一对应。

## 6. 转换映射（md 契约，convert 纯函数 A1）

| HTML | md（yuanwen） |
| ---- | ---- |
| 节 `N. 标题` | `## N. 标题`（点号式与原文一致） |
| 脚注 | `[^note-N]` 定义行（脚注恒末位） |
| 图片 | `../assets/<slug>/` |
| citation meta / 参考文献 | 转脚注定义（`build_cite_keys`，无姓氏路径 `fallback_author` 兜底） |
| 同文重复 H1（旧模板 citation_title 无条件前置） | `_drop_duplicate_h1` 留首删余 |
| 上游字面 `#` | `\#` 转义（md 语义保护） |

## 7. B0 十谓词（模板一致性判据，判官 `specs/044-b0b1-baseline/bin/b0_scan_all.py`）

| 谓词 | 判据 |
| ---- | ---- |
| `marker` | BEGIN/END 注释均命中 |
| `pubinfo` | First published 出版信息可解析 |
| `title` | citation_title 命中 |
| `section` | 至少一个带节号 h2 分节 |
| `no_truncation` | 含 `</html>`（无截断） |
| `no_error_page` | 页头无错误/风控页标记 |
| `math_delim` | `\(`/`\)` 与 `\[/\]` 各自配对 |
| `math_brace` | 公式内 TeX 花括号平衡 |
| `table_row` | 每个 `<table>` 含 `<tr>` |
| `img_src` | 每个 `<img>` 有 `src` |

**B0 机检盲区**（判形式可解析，不判内容对，ADR-0070 附录）：节号跳号/层级错乱、pubinfo↔archinfo 不一致、定界符位置配对（计数不查位置）、td/th 失衡与 colspan 错、标记之间正文截断。增强判据归 specs/053 P2（ADR-0070 建议③）。

## 8. 例外登记（anomalies.json）

- 判据“至少一个 h2”“锚 id 唯一”等存在上游原生变异；凡判为**上游原生非缺陷**的变异，逐条人审登记 `anomalies.json`（字段：id/class/description/slugs 或 count/evidence/judged_by/judged_at/judgement），**豁免＝已人审后豁免，非免检**（ADR-0070 建议④）。
- 边界（T3，不可自证）：本契约能证明“已登记结构元素无一落空”，不能证明“没有第 11 种模板变异”——相对完备边界（specs/044 §2.3）。

## 9. 已知上游原生变异类（待 P2 逐条定性入册）

1. 尾节锚点 id 仅 81.3%（上游自身不规范）。
2. 正文标题 id 94.8% 全库唯一；作者自由文本不可枚举、深度不可预设。
3. 旧模板条目 pubinfo 形态变异。
4. 无尾节主件 551 件全为带点子文档（supplement/bibN/vita/figdesc 天然无尾节，勿计违规）。
5. h2→h4 跳档（bauer 先例，SEP 原生结构豁免）。

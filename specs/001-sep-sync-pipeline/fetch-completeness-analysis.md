# HTML 抓取内容与结构完整性分析 — 2026-10-27

用户指令："HTML 抓取的内容、结构是否完整，包含图片，公式，css 等？分析网站结构并将其记录优化分析。" 数据源：en/ 实测抽样（capitalism 153KB / abduction 93KB / logic-classical 135KB / bayes-theorem 91KB）+ 全库计数。

## 一、SEP 网站结构（实测）

一个词条页 = 站点框架 + 词条内容两部分；本管线**只抓词条内容**：

| 层 | 内容 | 是否抓取 | 理由 |
|---|---|---|---|
| 站点框架 | 9 个 CSS `<link>`、MathJax JS/字体、symbols/ 站内框架图（logo 5 个/页）、导航 chrome | **不抓**（有意设计） | 转换只需要词条正文；样式由本地 VitePress 提供 |
| 词条正文 | index.html（BEGIN/END ARTICLE 注释界定，153KB 量级） | ✅ | 转换源 |
| pubinfo / article-copyright | 版本事实 + 版权 meta | ✅（在 index.html 内） | 版本钉来源 |
| div#toc | 目录 | ✅（在 index.html 内） | 节结构参照 |
| 脚注 | notes.html（词条目录下独立文件，存在性因词条而异，404 为正常缺省） | ✅ 存在即抓 | 624/1872 词条有 |
| 补充材料 | 词条目录下任意命名 .html | ✅ 存在即抓 | 421 个 |
| 词条图片 | `<div class="figure">` 内 `<img src="imageN.jpg">`（词条目录相对路径） | ✅ 按引用抓 | action-perception fig1-3.png 等在位 |
| 公式 | 行内 `\(...\)`、行间 `\[…\]` 文本（MathJax 源码，无 MathML） | ✅ 原样保留 | logic-classical 单页 1545 处行内公式；check_math 门禁保证转换保真 |
| 表格 | `<table>`（bayes-theorem 25 个） | ✅ | — |

## 二、完整性结论

* **对转换管线而言：完整。** 转换所需四类物（正文 HTML、脚注、补充材料、图片）按引用齐备；全库计数 index 1726 / notes 624 / 补充材料 421，缺件即"缺省件"显式登记（404 非错误）。
* **对"离线高保真存档"而言：不完整。** CSS/MathJax/字体/symbols 未抓——当前设计下不需要；若未来要"浏览器直接打开即原貌"的学术存档，需补抓（见建议 2）。
* **待验证缺口已闭环（2026-10-27 干执行）**：tools/fetch_audit.py 全库审计——引用闭包迭代至不动点（第 1 轮补 457、第 2 轮补 29、第 3 轮起 fixed=0），累计补齐 **486 个资产**（多为 notes/补充材料内引用的图片与文件），0 缺省件、0 可补抓、0 错误；1724/1724 词条包资产完整。

## 三、优化建议（不计成本）

1. **抓取完整性主动闭环（tools/fetch_audit.py，已实现并全库收敛）**：对每个 en/<slug>/ 校验"index.html + notes.html + 补充材料内引用的全部词条资产在包内"，缺件自动补抓并更新 baseline——把现行的"缺省件登记"升级为"主动补齐 + 验收"。
2. **高保真存档模式（可选开关）**：抓全站 CSS + MathJax + 字体 + symbols 到 `en/_site/`，使 en/<slug>/ 成为浏览器直接可开的完整离线快照；SEP 内容 CC BY-NC-SA，私有存档注明来源与许可。成本：一次性抓 9 CSS + 字体 + 每页 5 symbols（体积小）。
3. **WARC/MHTML 存档级格式（长期）**：对每词条生成单文件 WARC（含全部依赖），作为学术存档的法定完整性形态（可配合 Web Archive 团队工具链验证）。
4. **语义元数据深化**：index.html 内 citation_* meta 已用于版本钉；可补抓 JSON-LD/引文导出（BibTeX via /citez endpoints）供学术工具节与引用管理。
5. **抓取调度**：cron 定期 `fetch_catalog` + `compare` 全量比对，漂移自动进更新队列（与 specs/004 路线第 6 条合并执行）。

## 四、复审

* 复审日期：2027-01-21（随存档季抓取轮复核本表计数）。

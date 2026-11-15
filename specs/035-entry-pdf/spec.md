# specs/035-entry-pdf: 词条 Friends 版式仿排 PDF 管线

## 背景与目标

SEP 官方 Friends of the SEP Society PDF 是独立排版产物（pdfTeX/Times+CM、双宽栏横排、
季度版页脚），与网页 HTML 同源不同线（原版结构解剖见 execution-log 2026-11-15 首段）。
本规格把「词条中文 md → pandoc → typst → Friends 风格 PDF」固化为可复用工具：

- `bin/entry_pdf.py <slug>`：一条命令出 PDF（封面信息栏+题栏+目录树、双栏正文、
  页眉页脚、引块、栏底脚注、悬挂缩进书目）。
- `bin/entry_pdf_template.typ`：版式模板（占位符填充）。

## 非目标

- 不逐字节复刻原版（原版 LaTeX 类私有；本仿排为 Typst 独立实现）。
- 不做 Letter/A4/单栏半页变体、不做目录页码、不做批量并行排版。
- 不改词条 md 本体；产物不入库（默认 `script/tmp/entry-pdf/`）。

## 契约（用法）

```sh
uv run --with typst --with pymupdf python specs/035-entry-pdf/bin/entry_pdf.py <slug> \
  [--edition "2025 年夏季版"] [--out DIR] [--no-preview]
```

- slug 解析：先 `<letter>/<slug>.md`，回 `tasks/<letter>/<slug>.json` 的 `zh_doc` 登记。
- 输入体例依赖（与组装约定一致）：H1 `中英题 (作者)`；pubinfo 行（首次发表于/实质性修订）；
  参考文献＝脚注定义承载（行内 `[^key]` 引用 → 真脚注；`[^key]:` 定义 → 书目段落）；
  「原文参考文献已转为脚注引用」底稿注记剥离。
- 依赖：pandoc(PATH)、typst/pymupdf（uv 注入）。字体自举经 `gh release download`
  至 `script/tmp/sep-pdf/fonts/`（霞鹜文楷屏幕阅读版 + 主仓 Medium，本地缓存不入库）；
  SEP 标志单请求抓取转黑。
- 退出码：0 成功；1 输入/解析错；2 依赖或自举失败；3 编译失败。失败显式化，禁止静默跳过。

## 排版要点（与原版对照）

| 原版特征 | 仿排实现 |
| ---- | ---- |
| A4/Letter 双宽栏横排 | `#columns(2, gutter: 1.8cm)` + `page(flipped)` |
| 页脚 verso 页码+刊名 / recto 季度版 | `binding: auto` 奇偶切换 |
| 页眉 词条题（小型大写）\| 作者 | 字距替代小型大写（Times 无 smcp） |
| 封面 左信息栏+标志+版权块 \| 右题栏+目录树 | 同构复刻 |
| 中文正文（本项目扩展） | 霞鹜文楷屏幕阅读版；段首缩进 2 字符（`all: true`）；段距 1.35em |
| 中文强调/标题 | 主仓 Medium 字重（无 Bold/Italic 字面，typst 不合成假粗斜体） |

已知偏差：无小型大写字母真字形；目录树无页码；中文标题字重为 Medium（500）非粗体。

## 验收判据

1. 换 slug 可复现（试金石：`descartes-ontological`）。
2. 目视：封面无溢出、正文段首缩进、引块/脚注/书目版式正确。
3. PDF 内嵌字体恰为 LXGWWenKaiScreen + LXGWWenKai-Medium + Times 系（无 KaiTi 回退——
   Screen 版族名 typst 只认英文 `LXGW WenKai Screen`，中文名会静默回退，见 execution-log）。

## Assumptions（用户裁定登记）

- 2026-11-15：中文正文用霞鹜文楷屏幕阅读版（用户指定「雾霞文楷屏幕阅读版本」）。
- 2026-11-15：删除仿排声明框（版权块保留）。
- 2026-11-15：中文排版优化：段首缩进两字符、加大段间距。
- 2026-11-15：选条方式为 done 池真随机（本体论修正池 2 条抽中 descartes-ontological）。

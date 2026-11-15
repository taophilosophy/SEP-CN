# specs/035 执行记录

## 2026-11-15 首日：原版解剖 → 仿排复现 → 字体替换 → 排版优化 → 固化

**原版解剖**（对 plato/leibniz 服务链路的实证，样张 `turing-machine-sample.pdf`）：
- 服务器：plato/leibniz 为斯坦福自管 nginx 静态主机（171.67.193.20/23，单 A 记录无 CDN）；
  Friends PDF 走 leibniz 会员门户，公开样张可下。
- PDF 内部：`Producer=pdfTeX-1.40.24 (TeX Live 2022)`；每页为 `\includegraphics`
  双层叠加（`wrapper.pdf` 页框 + `complete.pdf` 正文 + `SEPthinker.pdf` 标志，
  `PTEX.FileName` 留痕）；23 字体全内嵌（Times 正文 + CM 标题）；35 页零位图——
  官方说明「generated from the HTML source using professional typographic software」，
  季度 Archive 后重生成。

**仿排复现**（script/tmp 试金石 → 本规格）：
- 路线：md 变换 → pandoc(-t typst) → Typst 模板填充 → 编译 → pymupdf 渲染目视迭代。
- 坑 1（typst 0.15 API 演进）：`two-sided`→`binding: auto`；`column-gutter`/`gutter`
  从 `page()` 移除，改 `#columns(2, gutter:…)`；`query()` 须入 `context`。
- 坑 2（字体族名）：霞鹜文楷屏幕阅读版 name 表含中英两条 family 记录，typst 只匹配
  首条英文 `LXGW WenKai Screen`；用中文名会静默回退 KaiTi/Libertinus——靠
  `page.get_fonts()` 内嵌字体核验抓出。
- 坑 3（假粗斜体）：该家族无 Bold/Italic 字面且 typst 不合成；中文强调/标题改主仓
  `霞鶩文楷` Medium（500），拉丁照旧 Times 真粗斜体。
- 结构特判（descartes-ontological）：参考文献＝脚注定义承载（项目转脚注约定）——
  行内 `[^key]` 8 处 → 真脚注；`[^key]:` 49 条 → 书目段落（悬挂缩进）；底稿注记
  「原文参考文献已转为脚注引用」剥离不排。
- pubinfo 核对（零信任）：zh 行「首次发表于 2001 年 6 月 18 日；2025 年 5 月 5 日
  实质修订」与 en 源 `First published Mon Jun 18, 2001; substantive revision Mon
  May 5, 2025` 一致。首日曾误报「zh 与 en 冲突」，系把 abortion 条目日期行误安，
  当轮已撤回。

**字体替换**（用户裁定）：宋体+楷体 → 霞鹜文楷屏幕阅读版（正文）+ 主仓 Medium（强调/
标题）。仿排声明框删除，版权块保留。

**排版优化**（用户裁定）：段首缩进 2 字符（`first-line-indent: (amount: 2em, all: true)`，
封面右栏与参考文献节显式豁免——书目走悬挂缩进）；段间距 1.0em→1.35em；行距 0.92→0.96em。

**固化**：script/tmp 一次性脚本泛化为 `bin/entry_pdf.py <slug>`（slug 自动解析
zh_doc、字体/标志自举、退出码显式化），模板随之参数化（`%%EDITION%% %%ENTRY_URL%%`）。
试金石 `descartes-ontological` 全流程复跑通过，内嵌字体核验 =
LXGWWenKaiScreen + LXGWWenKai-Medium + Times×2，无 KaiTi。

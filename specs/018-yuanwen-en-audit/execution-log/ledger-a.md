# 018 台账 — a 批

格式：每词条一节。核=逐段人眼比对（协议见 ../spec.md）；修=yuanwen 侧修复；译=中文译文同步。
「系统行为（不改）」= 转换器设计约定（specs/001 契约 + 018 实证确认），非缺陷。

## abduction（正式，任务 done 口径见 tasks/a/abduction.json）

- 源：en/abduction/index.html（1924 行；正文 h1 至 Related Entries 止）↔ yuanwen/a/abduction.md（439 行）
- 逐段核：preamble 4 段✓；§1 4 段✓；§1.1 5 段+2 引块✗（F1）；§1.2 6 段+1 引块✓；§2 15 段+ABD1/2/3（dt/dd→加粗行）✓（F2×2）；§3/3.1/3.2 12 段✓（F2×1）；§4 11 段✓；书目 121 条逐一比对（html `<li>` ↔ md 脚注定义，计数 121:121，内容含 URL/doi 逐条一致）✓（F4×1）；Academic Tools 4 行表✓；OIR✓；Related Entries 8 条✓；作者行=citation_author meta✓；notes 无脚注（无 notes.html）✓
- 发现（4 类 6 处，均已定性非机械替换）：
  - F1 引块 `<br />` 三行图式被并行成单行（§1.1 三段论图式、佛兰德归纳图式）
  - F2 em 标签内空格剥失致粘字：`*abductive*ones`、`*that**H*`、`*supposes*that`
  - F4 `<b>CP</b>` 加粗丢失（书目 Peirce 条）
- 修复：先人工修 6 处（yuanwen 侧）+ 译文同步 3 处（a/abduction.md 行27/33 引块拆行、行357 [**CP**]）；随后按用户指令（spec A4）修进转换器并重转——重转产物与人工修复预期逐行一致，人工修复被重转产物覆盖等价替代
- 系统行为（实证确认，不改）：跨词条链接转纯文本（同一目录补充材料链接转本地 md 链接）；TOC 丢弃（导航非内容）；Bibliography→文末脚注定义+文内引用组附 [^key]（按引用组匹配追加，键按首作者-年份）；`<sub>1</sub>`→Unicode ₁、字母下标→`_{*n*}`；`<dl class="sentag">`→`**ABD1**` 独立行+dd 段
- 结论：发现 3 类系统性缺陷（F1/F2/F4）+1 例（F4 即 b 标签类），已全部修入转换器（tools/yuanwen.py，单测 6 例）并全量重转；译文已同步。
- 重转回归（2026-11-13）：1872 词条 × 2421 文件全量重转，0 失败；归一化差异扫描 1839 未变 / 134 BR / 447 SPACE-STAR / 1 OTHER（=SUMMARY.md 按根 SUMMARY 刷新，合法）/ 0 文件增删。
  - 扫描期间发现第 4 类：`&nbsp;`（`\xa0`）是诗行与书信缩进正文内容，`<br>` 拆分时若用 `\s*` 连带吞掉即丢缩进（aesthetic-experience 诗行、physics-experiment 书信署名等 15 例）→ 已改为只吞 ASCII 空白并补单测。
- 并行会话冲突留痕：本会话译文修正曾于并行批量改写中被覆盖回滚一次，提交前已复查并重新落盘；`a/abduction.md` 现含 3 处同步修正（行27/34 引块拆行、行361 [**CP**]）。

## abelard（正式；译文 a/abelard.md 存在）

- 源：en/abelard/index.html（2278 行）↔ yuanwen/a/abelard.md（463 行）
- 逐段核：preamble 1 段✓；§1/1.1（7 段）✓；§1.2（13 段 + 7 个书目式项目列表，圆点列表逐项对位）✓；§2（8 段）✓；§3（5 段）✓；§4（11 段 + 2 引块）✓；§5（9 段）✓；§6（12 段 + 1 引块）✓；§7（9 段 + 1 引块）✓；书目 **97 条逐一比对**（拉丁原始文献 29 含 LI 四子条、英译 13、二手文献 55；html `<li>` 与 md 脚注定义 97:97，条目文字含 URL/在线链接一致）✓；Academic Tools 4 行✓；OIR 8 条✓；Related Entries 8 条同序✓；作者行=citation_author 双作者✓
- 源文瑕疵忠实保留（不作「修正」，零信任口径）：§2 “in separation form the body”（源 html 同误，form←from）；§4 “the fact that that we can”（源同）；§2 行内 “Abelard‘s” 误用左单引（源 `&lsquo;` 同）
- 系统行为（实证确认，不改）：Bibliography→「References（引用注释）」+ 条目全量转文末脚注定义；三个文献子标题（Primary texts in Latin / English translation / Selected Secondary）在 md 中成为空壳，因条目已移入脚注定义，**顺序仍按原三分组排列**（29/13/55），信息不丢；中文侧 a/abelard.md 同形态（3 空壳 + 97 定义），两侧一致
- 结论：本轮转换后 **零缺陷**；BR/em/b 三类历史缺陷在本词条未复现（验证转换器修复生效）。译文无需同步改动。

## abilities（正式；译文 a/abilities.md 存在）

- 源：en/abilities/index.html（2247 行）↔ yuanwen/a/abilities.md（516 行）
- 逐段核：preamble 2 段✓；§1（1 段）✓；§1.1（5 段）✓；§1.2（4 段）✓；§1.3（6 段）✓；§2（1 段）✓；§2.1（6 段）✓；§2.2（5 段）✓；§3（1 段）✓；§3.1（7 段 + (CA) dt/dd）✓；§3.2（8 段 + 2 引块）✓；§3.3（6 段 + 2 引块）✓；§3.4（9 段 + 4 引块 + (CD)）✓；§4（1 段）✓；§4.1（7 段 + (MA)/(CA_modal)）✓；§4.2（7 段）✓；§4.3（6 段 + (1)/(2) 公式 dt/dd + 1 引块）✓；§4.4（6 段）✓；§5（1 段）✓；§5.1（8 段 + 1 引块）✓；§5.2（5 段）✓；Acknowledgments✓；书目 79 条逐条✓；Academic Tools 4 行✓；OIR✓；Related Entries 8 条✓
- 结构细节验证：`<strong>T</strong>`/`<strong>K</strong>`（模态逻辑系统名）已按 F3 修复转 `**T**`/`**K**` ✓（修复前会丢加粗）；`(CA_modal)` 的 `<sub>` 转 `_{modal}` ✓；`&nbsp;` 无；引块单行内容转 `>` 单行 ✓
- 源文内部不一致忠实保留：正文「Martin (1994)」vs 书目「Martin, C.B., 1996」（源 html 同）；「theory of abilitiy」拼误（源同）；「Norman,and Wikler」「Glick, Ephraim. 2012」标点缺漏（源同）
- 结论：零转换缺陷；译文无需同步。

<!-- 接力指针：下一词条 abner-burgos（yuanwen/a/abner-burgos.md；en/abner-burgos/index.html） -->

## abhidharma（正式；译文 a/abhidharma.md 存在）

- 源：en/abhidharma/index.html（2048 行）↔ yuanwen/a/abhidharma.md（354 行 → 重转后同）
- 逐段核：preamble 2 段✓；§1（5 段）✓；§1.1（4 段）✓；§1.2（4 段）✓；§2（8 段）✓；§3（8 段）✓；§4（6 段）✓；§5（6 段）✓；§6（10 段）✓；书目 **78 条**（Primary 27 + Secondary 51，另说明段 1）逐条比对✓；脚注 `[^note-1..17]` ↔ 定义 17 条✓（含 [^note-5] 内嵌引块）；Academic Tools✓；OIR 两小节 4 链接✓；Related Entries 14 条✓；作者行✓
- 新发现系统缺陷（已修入转换器，单测 27 项全绿，全量重转）：
  - F6 年份大写后缀键退化：`1992A/2004B/1918B` 旧正则因尾 `\b` 与后缀大写冲突，**整条年份匹配失败**，退而匹配条目正文内的页引年份（如 1918B 条被命名 `brouwer-1975`），键名与条目错位；全库 18 处/5 文件键名错位。修法：后缀扩 `[a-eA-E]` + lower。
  - F7 notes.html 页标题泄漏：`## Notes to <Entry>` 与转换器 `## Notes（原文脚注）` 双标题（全库 692 处）→ 页首 500 字符内 Notes 标题剥除。
- 重转回归（第 3 轮全量）：OTHER 3 例全部定性——SUMMARY.md 刷新（合法）、a/abhidharma（+1 标记：`Gethin 1992b` 现正确命中年份键）、i/intuitionistic-logic-development（−2 标记：旧版三个 `brouwer-1975*` 幻键中两个指向 1918B/1919A，现归位）
- 系统行为（实证确认，不改）：书目说明段转 `[^pali-nd]` 脚注定义（内容保全）；正文 `[^note-N]` 与 `[^key]` 混排正常



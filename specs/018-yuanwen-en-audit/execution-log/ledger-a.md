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
- 结论：发现 3 类系统性缺陷（F1/F2/F4）+1 例（F4 即 b 标签类），已全部修入转换器（tools/yuanwen.py，单测 5 例）并全量重转；译文已同步。

<!-- 接力指针：下一词条 abelard（yuanwen/a/abelard.md，96KB；en/abelard/index.html 116KB） -->

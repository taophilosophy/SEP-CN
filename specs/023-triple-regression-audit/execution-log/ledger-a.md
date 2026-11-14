# 023 ledger-a — 逐词条双轴台账

协议见 `../spec.md`。每词条一节：镜像轴（en↔yuanwen）＋译文轴（zh↔en/yuanwen）逐行走查记录；接力指针在文末注释行。018 已核 10 条（abduction…abu-bakr-al-razi）镜像轴结论沿用（spec A5），其译文轴在本台账照常审。

## academic-freedom（正式；译文 a/academic-freedom.md；任务 done）

- 源：en/academic-freedom/index.html（2622 行；正文 §1–6 行 142–1785；Bibliography 130 li；OIR 13；Related 9；notes.html 1 注）↔ yuanwen/a/academic-freedom.md（537 行）↔ 译文（537 行；作者 Levy, Jacob T.）
- 机械对账：标记 yw 64/zh 64（`[^key]` 为 References 说明行字面文档串）；defs 两侧 131＝130 书目＋note-1，键集全等；照录区归一化 diff 仅 note-1 有别（内容注译中文，体例 ④）；尾节四件套齐（学术工具 4 行 bullet、OIR 13、相关词条 9 中译、致谢、译注行）；未引用 defs 两侧同集（83 键）。
- 镜像轴逐段走查（§1–6 全部、四尾节、note-1）：无缺段、无凭空多出；引用组标记逐组核对；源文瑕疵照源保留 3 处实证——`universities<em>.</em>`→`*.*`（preamble）、`classroom<em>&rdquo; Keyishian…</em>`→引号入斜体（§3.4）、`6<strong>.1.</strong>`→`6**.1.**`（§3.5）、vozar 条 `Revolution<em>: Libertas…</em>`→星从冒号起（书目）、medeiros 条 `&rdquo;…&ldquo;` 反向引号（书目）、weber 条 `<em>The Vocation</em>, <em>Lectures</em>` 双斜体（书目）——均逐字对位 en。
- 译文轴逐行走查（zh 1–203 全正文＋204–236 全尾节＋照录区抽查）：内容保真无缺漏；s3 批遗留的高频缺陷（组装重复行、双语 defs、中英混杂）均无；术语与人名处理规范（内容无关性/情境无关性、拒予平台、洪堡/杜威/佩蒂特等）。
- **发现与处置**：
  1. en 源头勘误 3 处（ADR-0038 类①，已登记 en-errata.md 并改正、重转）：`akedemische Freiheit`→`akademische`（德语正字）；`David Owewn`→`Owen`（Hackett 2004 合编者实名）；`Enyidi Zsolt, 2018`→`Enyedi, Zsolt, 2018`（已核实 doi:10.1017/S1537592718002165）。译文侧：zh 正文 akademische 原本已正（s3 批译者已修），zh 照录区两处同步改正（Enyedi、Owen）。
  2. 【观察，不动】`[^whittington-2022]` 挂于引证组 `(Whittington 2018b, Ben-Porath 2022, Eisgruber 2025)`——键匹配式在逗号组内跨条配中（组内含 "Whittington…2022" 字面即中）。yw/zh 两侧一致、检查器全绿；属转换器既定行为（ADR-0038 逗号容许的代价面），改动匹配式须另立证据周期（A4 语义）。
  3. 【豁免】zh §3.4 将 en 斜体引号尾（`…classroom<em>&rdquo;</em>`）正读为引号闭合后再接文献——翻译级标点规整，内容无损。
  4. 【观察，语体归 015】en 1940 声明 "special obligations" 与 1915 "peculiar obligation" zh 均作"特殊义务"，区分未显。
- 定点门禁：check_academic --strict OK；check_style --strict 0。
- 结论：镜像轴零转换缺陷（3 处 en 勘误后）；译文轴零缺陷；3 处勘误已三层落位。

<!-- 接力指针：下一词条 action（queue #13，done，562 行）；队列全序见 specs/023-triple-regression-audit/results/queue.md，禁止跳条 -->

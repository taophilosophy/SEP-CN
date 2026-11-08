# T–Z 批战役开工记录（2026-11-07，会话 TZ-main-20261107）

**范围**：t/u/v/w/x/y/z 七批共 **139 条**（71+4+15+38+3+2+6），约 200 万英文词；`campaign.py claim --force` 改账至本会话，**S 批仍属 SZ-main-20261107**。
**方法**：主会话直译（2026-11-07 用户裁定，不用子代理）＋ ADR-0021 段落账本（`script/lq.py`）＋ `script/lq_fill.py` 块级填充。

## 1. 体量盘点（`script/size_tz.py`，本地件）

| 项目 | 计数 |
| --- | --- |
| 条目 | 139（最小 timon-phlius 4978 词；最大 weyl 61631 词 / 1013 段） |
| 总词数 | 2,001,810 |
| 含补充材料 | trinity(4) / truthlikeness(6) / truth-values(4) / two-dimensional-semantics(4) / time-travel-phys(3) / transmission-justification-warrant(3) / value-theory(3) / turing-machine(2) / thick-ethical-concepts(2) / weyl(2) |
| 含图 | 15 条 |
| 现制 References（引用注释） | zeno-elea / twardowski / zhuangzi / voting-methods（另有 timon-phlius、truth-coherence 实为同形态，见下） |
| 公式密集（≥300 定界符） | truth-revision 1196 / type-theory-intuitionistic 556 / type-theory 428 / truth-axiomatic 327 / time-machine 306 / truth-pluralist 266 |
| 罗马化线索≥8（ADR-0011 中国文献还原） | xunzi / zhuangzi / zhu-xi / wang-yangming / thomas-kuhn / trans / twotruths-tibet 等 7 条 |

## 2. 已完成（s3_checked，待复审波 r1–r3）

| 词条 | 段数 | 形态 | 备注 |
| --- | --- | --- | --- |
| t/timon-phlius | 26+1 | 现制 References（15 条定义照录，正文 marker 仅 long-1978） | 术语登记 28 行；相关词条 3 项无 SUMMARY 行（Academy, Plato's / Cynics / Megaric School），经 `baseline/catalog.json` 实证不在本库目录，保留中文译名待挂链 |
| t/truth-coherence | 47+1 | 现制 References（21 条定义） | 术语登记 21 行；源文自身不一致两处照源直译（Candlish 2006 vs candlish-2021；Knight 2025 vs knight-2024） |
| w/william-sherwood | 56+1 | 现制 References（29 条定义）+ 1 图（指代树状图，本地化 `../yuanwen/assets/`）+ 2 个拉丁诗句引块 + 表格（格/式） | 术语登记 25 行；相关词条 2 项手工归位（obligationes → 中世纪的义务理论；Peter of Spain → 西班牙的彼得（彼得·希斯帕努斯）的逻辑）；兰伯特正形对齐 SUMMARY（欧塞尔的兰伯特） |
| w/wisdom | 54+2+1 | 现制 References（20 条定义）+ 5 个编号定义块 + 1 条真脚注（note-1） | 术语登记 18 行；相关词条 1 项手工归位（coherentist justification → 知识证成的融贯论）；源尾笔记脚手架（#### / ## Notes to Wisdom）节数差 1 属转换器约定 |
| x/xenophanes | 50+1 | 现制 References（29 条定义）+ 11 处残篇/转述引块 | 术语登记 24 行；prose 16→0 全实修；Xenophanes 主形按 SUMMARY 定为「克塞诺芬尼（亦作色诺芬尼）」并同步词汇表；相关词条 3 项（Anaximander/Anaximenes/Thales）无 SUMMARY 条目，改中文名待挂链 |
| w/william-jevons | 38 | 现制 References（56 条定义照录，正文 marker 16）+ 1 引块表格（三律符号表）+ 7 子弹推理形式清单 | 术语登记 36 行/人名 13 行（bisect 插入、先查后登）；prose 14→1（实修 13，豁免 1 为 Black & Könekamp 引文）；相关词条 De Morgan 无 SUMMARY 行改登记册正形待挂链；**产物（md/json/ledger）与登记行被并行会话提交收编（b1546bb9/ff4504ce/2500e112），内容逐项核实无损后确认入库，本会话免重复提交** |
| t/telesio | 28 | 现制 References（100 条拉丁/意/西语著录全照录，正文 marker 12）+ 2 引块（《论物性》卷五长引）+ 13 项相关词条全自动映射 | 术语登记 16 行/人名 11 行（bisect 先查后登；hegemonikon 同键异译依先登优先并入既有「灵魂的主导部分」行，正文改从正形）；prose 29→6（实修 23，豁免 6 全在引文块/引语内）；正文依批规用登记册正形「特莱西奥」，H1 沿用 SUMMARY「特勒肖」入 §4 归一清单；登记行已被并行提交收编入 HEAD，产物另提交 |
| t/theology-aristotle | 50 | 现制 References（60 条拉丁/阿拉伯/意语著录全照录，正文 marker 53）+ 4 引块（序言/太一比较/两种无知/隐德来希）+ 阿拉伯文术语汉译并列（fayd/anniyya faqat/ṣifāt/kalima/al-lays 等） | 术语登记 21 行/人名 11 行（现代学者循 israeli 先例保留拉丁引用组）；prose 25→0 全实修无豁免；相关词条 7 项全自动映射；登记行已被并行提交收编入 HEAD |

各条均为：`lq.py check` HARD=0；节标题/标记键/定义键集/段落四维对账齐；`check_style --strict` 0 issue；`check_academic --strict` 0 硬错误；`check_math` 0；`check_all` 七项全绿。

## 3. 门禁与登记册修复（跨会话事项）

1. **Alain Locke 冲突**：`qian-yan/ci-hui-biao.md` 滞后于 `ren-ming-biao.md` 归一形（阿兰·勒罗伊·洛克），已对齐（commit 02735ed）。
2. **Leibniz 重复行**：并行会话 scholz 批次在 `ren-ming-biao.md` 增行与既有 lady-masham 行同键同译，触发 `check_terms` 自洽硬门；已合并留痕（首现列作「lady-masham；亦见 scholz」）。
3. **term_flow.py 行体例偏差**：`build_row` 产出 5 列行，而两张登记表实际为 6 列（第二列「原文」占位 `—`），且 `note` 以「学界惯例（…）」开头时被二次包裹为「学界惯例（学界惯例（…））」。本批 49 行已按表体例重排；**建议后续修订 `tools/term_flow.py` 的 `build_row`**（未改动工具，留待规则层裁定）。
4. **Henry David Thoreau 冲突**：`ren-ming-biao.md`（亨利·大卫·梭罗，japanese-aesthetics）与 `qian-yan/ci-hui-biao.md`（亨利·戴维·梭罗）异形，依 ADR-0012 词汇表对齐登记册正形（telesio 批顺带收口）。
5. **Mulla Sadra 重复行**：illumination 批新行与 al-qudat 全形行同键触发 `check_terms` 自洽硬门；已按 Leibniz 先例合并（保留全 metadata 行，首现注记「亦见 illumination」），telesio 批顺带收口。
6. **Philip the Chancellor 冲突**：conscience 批人名表「菲利普校长」与词汇表旧行「总务长菲利普」异形，依 ADR-0012 词汇表对齐（theology-aristotle 批顺带收口；总务长语义保留于备注列）。

## 4. SUMMARY 与登记册异形（移交 011 归一）

正文一律用 `ren-ming-biao.md` 正形；SUMMARY 标题侧仍为旧形，待归一战役统一（改 SUMMARY 须联动 `mu-lu-s.md`）：

| 名 | 登记册正形 | SUMMARY 现形 |
| --- | --- | --- |
| ~~Xenophanes~~ | 克塞诺芬尼（亦作色诺芬尼）—**2026-11-07 已对齐 SUMMARY** | 克塞诺芬尼 |
| Zeno of Elea | 埃利亚的芝诺 | 爱利亚的芝诺 |
| Sextus Empiricus | 塞克斯都·恩披里柯 | 塞克斯都·恩披里克 |
| Anaxagoras | 阿那克萨戈拉 | 阿那克萨哥拉 |
| Telesio | 特莱西奥 | 特勒肖（正文依批规用登记册正形，H1 取 SUMMARY 题铃；词汇表两形并存待并） |

## 5. 下一步（按体量序）

truth-coherence 之后：william-sherwood → wisdom → xenophanes → william-jevons → telesio → theology-aristotle → **已完成**；续排 xenocrates(6652) → vives(6811) → vico(6846) …；公式密集件单独排程（先跑 `check_math`）；`xunzi/zhuangzi/zhu-xi/wang-yangming` 四条中国哲学件按 ADR-0011 走中国文献还原。
**复审波**：s3 完成后冷置回读再走 r1–r3（单会话作业须在 evidence 记明冷置），不复查旧错。

## 6. 实跑中新增的可复用经验

1. **单引号包裹拉丁字母触发 curly-quotes**：`‘a’`/‘Festino’ 会被规则当作转写撇号部分遮蔽，留下孤立的 ’ 报「右引号先于左引号」。写法：字母/单词名一律用双引号 `“a”`，或改用斜体 `*Festino*`；不嵌在双引号内即可。
2. **图注与图片路径**：源 `../assets/<slug>/x.jpg` 在 zh 侧必须改 `../yuanwen/assets/<slug>/x.jpg`（模板 §3.6 裁定）；长英文 alt（树状图）整段译出留在 `![]()` 内。
3. **块内嵌套引文**（`> > Barbara celarent…`）与编号定义块（`> *S* is wise iff` + `> 1. …`）可整块作一段入账本，行内换行照写，守恒门不受影响。
4. **节数差 1 的两种合法来源**：源尾 `## Notes（原文脚注）`/`####`/`## Notes to Wisdom` 脚手架（wisdom）；源端空标题（timon-phlius 的 `## References（引用注释）` 下空子节保留）。对账时先看尾部三元组再判缺陷。
5. **相关词条自动映射落空的处置顺序**：先查 `SUMMARY.md` 是否有对应 slug（有则手工改成 SUMMARY 定名）；无 slug 再查 `baseline/catalog.json`（不在目录者保留中文译名待挂链）。

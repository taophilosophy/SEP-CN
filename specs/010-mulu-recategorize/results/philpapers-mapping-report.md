# specs/010 PhilPapers 全量映射分析报告（2026-11-01）

产物：`philpapers-mapping.tsv`（1881 条 × 7 列：slug/标题/现节/PP大类/PP子类/来源/备注）
方法：三层规则引擎（区级断代与区域映射 → ### 子节级细化 → 标题关键词兜底[仅同类内生效]）+ 全量 auto-kw 140 条逐条终审。
覆盖：**1881/1881（100%）**，其中 auto-rule 1732、auto-kw 140、nav 9（前言/关于导航条目）；待人工 0。

## 一、映射分布（PP 七大类 × 34 子类）

| PP 大类 | 条数 | 子类分布 |
| --- | --- | --- |
| History of Western Philosophy | 597 | 20th 182 · 17th/18th 147 · Med&Renaiss 101 · Ancient 90 · 19th 54 · 19th/20th(马克思主义) 17 · （含女性两时期节 70） |
| Metaphysics and Epistemology | 333 | Metaphysics 106 · Language 87 · Mind 69 · Religion 61 · Epistemology 50 · M&E Misc 13 · Action 7 |
| Science, Logic, and Mathematics | 313 | Logic 110 · General PoS 61 · Biology 60 · Physical 46 · Cognitive Sci 36 · Math 30 · Computing 30 · Social Sci 21 |
| Value Theory | 314 | Social&Political 105 · Normative 78 · Aesthetics 35 · Meta-Ethics 31 · Applied 28 · Law 21 · Gender/Race/Sex 16 |
| Philosophical Traditions | 165 | Asian 86 · Traditions Misc 68（犹太 28+伊斯兰 40 级） · African/Africana 6 · Americas 5 |
| Philosophy, Misc | 15 | Misc 15（教育 6+文化 3+生死 3+其他） |
| nav | 9 | 站点导航 |

## 二、结构对照结论

1. **总骨架与 PhilPapers 七大类同构可映射**，且本项目在三个方向比 PhilPapers 更细：西史断代 6 子类+女性两时期专题节；区域哲学 9 节（中国/日/韩/印度 vs PhilPapers 单一 Asian；犹太/伊斯兰单列）；科学哲学按部门科学 8 子节。
2. **PhilPapers 有而我们无独立节**：Continental Philosophy（欧陆按哲学史优先散布西史人物簇，自洽不补）；Philosophy of Action（已于 R8 补设伦理学区 ### 节）。
3. **我们有而 PhilPapers 无对应子类**（归并策略）：教育/文化/生死/技术哲学 → PhilPapers Misc 或 General PoS；化学/医学 → Physical/Applied。
4. **PhilPapers 官方组织方式**（contents.html 字母序+人物/主题嵌套簇）与本项目人物挂靠结构同构，1741 条 auto-rule 中嵌套分支词条随主词条类目 ✓。

## 三、终审修正记录

* 首版关键词兜底跨大类误判 33 例（如法哲学节"证据的法律概念"被"证据"拽到 Epistemology、美学节"悲剧悖论"被"悖论"拽到 Logic、政治节"爱国主义"被"爱"拽到 Mind）→ 修正优先级：**关键词仅在节默认同类内细化，跨大类一律守节上下文**，修正后 auto-kw 173→140，140 条逐条终审通过。
* 边缘多归属词条（PhilPapers 自身双类）：legal rights（Law/Social&Political）、voting（Normative/Social&Political）、rational choice（Decision/Epistemology）——按节上下文取用，登记不改。

## 四、过程发现与修补

* **通论区"## 语言哲学与逻辑学"标题缺失**（二轮 R1-R6 重跑时引入，### 子节直接挂 # 下、层级跳级）：本轮补回一行，check_mulu_s 五项恢复全绿。
* 映射引擎初版 TSV 双写事故（Edit 残留致 if-m 段重复）→ 门禁语义对账（唯一 slug 1882 vs 行数 3754）拦截修复。

# 执行日志：009 目录与镜像归一性复核

## 2026-10-29 建档

* 用户指令："建立任务书复核 summary、mu-lu-s、yuanwen、en 文件夹内容，格式、结构的归一性"。任务书落 `spec.md`，状态 Created（待开工）。
* 开工底数实测（写入 spec 范围栏）：baseline 1878；SUMMARY 2649 链接；mu-lu-s 1888 链接；yuanwen 2427 md（gitignore，仅 6 个演示条目入库）；en/ 1880 目录（1878 词条包 + `_catalog`/`_manual`）。
* 集合预检：en/ 1878 词条包对 baseline **零缺包**；SUMMARY 与 yuanwen/SUMMARY 链接数相等（2649）。
* 已知发现基线自 007 承接（457 脚注悬空 / 46 未换行收尾 / 5 pm-notation 表格 / 232 math warn / spacetime-holearg 在途），复审维持原状不计新失败。
* 并行会话注意：mu-lu-s.md、yuanwen/SUMMARY.md、tools/yuanwen.py 等在途 staged 编辑；本战役纯本地复核，冲突处只登记归属不裁改。

## 2026-10-29 用户裁定：禁止机械复核

* 用户指令："禁止机械复核，必须确保格式的转译一致性"。已登记进 spec「约束与用户裁定」并新增「格式转译一致性」专节。
* 要点：检查器全绿（check_markdown/check_math/重转换字节一致）降级为必要非充分；重转换零漂移只证转换器确定性，不证转译正确性。
* 落地：转译规则目录 T-01…T-09（自 convert_entry 构件面归纳：区块/行内/数学/表格/列表/图/引文键/脚注补充材料/目录镜像），每条规则三级结论——形态唯一性（全库扫描）、语义保真（≥5 例人工抽样，记录词条名与比对结论）、zh 镜像兼容（结构锚点）。
* 产物新增：`bin/transpile_scan.py`（形态分布扫描器）、`results/transpile-rules.md`（规则目录与裁定）；验收标准插入为第 2 条（零未裁决项）。

## 2026-10-29 用户指令：1% 抽样逐段审阅

* 用户指令："随机抽取1%的html yuanwen en进行逐段审阅"。已登记进 spec（约束与用户裁定 / 工具 / 产物 / 验收第 6 条）。
* 方案：baseline 1878 × 1% = ceil → **19 条**；`bin/para_review.py` 复用 convert_entry 的切块路径（HEAD/TAIL_RE + extract_blocks_raw）对 `en/<slug>/index.html` 与 `yuanwen/<letter>/<slug>.md` 做全段对齐（文本骨架归一：公式→⟦M⟧、脚注引用键与文献标记剔除、md 语法剥离）；分歧段 100% 人工复核，无分歧段每条抽检 ≥3 段（最长段/含公式段/含表格或链接段）。种子 20261029 落 sampling.json，可复现。

## 2026-10-29 用户改令：全量逐段复核（长线战役）

* 用户指令："改为全量逐段复核，建立长线任务书"。1% 抽样方案作废；spec 增「全量逐段复核（长线战役）」节：A–Z 字母批、review-log.jsonl 断点、多会话字母批认领、零写入被审对象。
* 全量形状直方图即 T-01…T-09 形态唯一性扫描本体，独立 transpile_scan.py 取消并入。
* 验收第 6 条改写为全量口径：1878/1878 凭证、分歧段零未裁决、抽检 ≥3 段/条留痕。

## 2026-10-29 用户补充：确保 SUMMARY 正确

* 用户指令："新增：确保summary 正确"。登记为战役硬门槛四查：条目集=baseline、路径在盘、标题链三元组全量逐条核对（para_review 采集）、转义规则+既有门禁全绿。
* 落地：para_review.py 逐条读 SUMMARY 条目文字、zh H1、yuanwen H1，三元组比对结果入 review-log 与 <slug>.json；标题链不一致处走分歧段人工裁定。

## 2026-10-29 对齐器语义裁定（para_review.py 冒烟定标）

* 冒烟词条：abduction、pm-notation、quine（各含 dl/数学/表格/bib 小节等形态）。定标后 abduction、pm-notation 全清，quine 仅剩可归类项。
* 归一化裁定：比值阈值 **0.95**；公式定界内容双侧归一 ⟦M⟧；上下标双侧归一 ⟦S⟧/⟦P⟧（Unicode 原生字符经 SUB_MAP/SUP_MAP 反向识别，T-02 记号保真另由重转换字节复核覆盖）；pubinfo（First published…）双侧保留配对；作者行（全斜体行）双侧剔除；标题比较去强调标记（`*Principia Mathematica*` 斜体保真不算分歧）。
* 剔除对称：html `bib-container` ↔ md `References（引用注释）`节（标题+其后 h3 小节+体例说明，遇下一 h2 即止）双侧剔除——T-07 设计转换（文献全量转脚注），其保真由 baseline cite 计数与 007 重转换字节复核覆盖，不逐段比对。
* **整组合并判据**：连续非匹配区段整组比值 ≥0.95 → 记 merged 形态注记（preamble/列表/dl 的 1↔N 拆合块是转译形态，非内容分歧，T-01）；<0.95 才逐块 flag。
* 标题链判据修正：SUMMARY 条目文字 = zh H1（中文侧硬）；yuanwen H1（去强调）= html 标题（英文侧硬）；SUMMARY 用「姓, 名」引文格式系设计使然，与 html 原题词序差异不算错。
* 冒烟已知真发现：bib 段 h3 小节在 md 侧随 References 节渲染（quine 型）——已归入 References 段剔除范围，非正文泄漏。

## 2026-10-29 跑批期发现与对齐器迭代（第二轮）

* **真发现 R1（全库清点）**：30 个词条 yuanwen md 存在**重复 H1**——词条包 html 文章首块为图片（figure 先于 h1）时，convert_entry 兜底前置标题与正文渲染的 H1 叠加，且图片位于标题之前。清单 `results/para-review/dup-h1-scan.json`（anderson-john、frege、russell、descartes 等 30 条）。移交镜像责任会话（修复方向：兜底前置仅在渲染输出无 H1 时触发，图片块移至标题后），本战役零写入不改被审文件。
* **对齐器迭代 2**：①SUMMARY 解析支持嵌套方括号链接文字与数字开头目录（1878 标题全命中，重启前 4 条 title 误报归零）；②References 文献节剔除规则修正——注释性文献节（addams-jane 型：h3/h4 小节与条目段落混排）整段剔除，**遇 h2 正文节才回到正文**；③html 侧 `|` 剥离（Related Entries 管道分隔符，与 md 表格管道剥离对称）。
* 跑批策略：全量首轮以定稿前代码在跑（进度 151/1878）；完成后仅对 flagged 词条 `--force` 定点重跑（吸收迭代 2/3 修复），ok 词条证据不受影响。

## 2026-10-29 主代理 1% 人工深读完成（19/19）

* 用户裁定落地："主代理必须同时随机抽1%条目逐个逐段人工复核，禁止机械"——种子 20261029 抽 19 条，主代理逐段通读（18 条 md 全文 + science-mechanisms 正文全读/defs 抽检），逐条裁定落 `manual-1pct.jsonl`，汇总裁定落 `para-review-summary.md`。
* **反机械层价值实证**：人工层捕获机械层两类系统性盲区——R2 链接丢失（对齐器忽略链接语法）与上游笔误/形态（骨架比对天然吸收）；用户"机械复核会遗漏真实情况"的判断成立。
* **真发现**：R1 重复 H1 人工实证（james）；R3 键张冠李戴（hooks→holtug）；R4 键退化家族（名当姓/首词键/前缀截断/非 ASCII 不一致）；R5 挂键率悬殊 0–363（baseline 实证）；M2 裸美元 3 处；M3 零宽字符（建议 02-style 增补检查项）。
* **R6 改判**：图表标签双现系上游 figlabel+figcaption 双文本结构、转换保真（science-mechanisms 完整形态对照），非转换缺陷。
* 全部修复责任移交镜像/管线会话，本战役零写入不改被审文件。

## 2026-10-30 用户指令：再抽 5% 人工深读

* 用户指令："再次抽查随机5%"。同协议加抽 94 条（种子 20261030），主代理逐段通读，结论落 `manual-5pct.jsonl`；与 1% 层累计 6% 人工覆盖。全量跑批同期推进（1590/1878）。

## 2026-10-30 5% 人工深读完成（94/94）

* 完成：种子 20261030 抽样 94 条全部主代理逐段通读完毕（本日续接 22 条：bradley-regress→atonement），逐条裁定落 `manual-5pct.jsonl`（102 条记录=94 抽样全覆+8 条前会话跨词条普查补充；94 条零缺失零重复），每条即读即记即 pathspec 提交。
* 裁定分布：pass 80 / fail 22（前阶段 fail 多指「发现待移交」标记、其 verdict 正文均为完整性描述；本日新增 22 条中 21 pass，仅 williams-dc 记 fail）。
* **最高优先级移交项（镜像忠实性破坏）**：williams-dc 原 Primary literature 节 20 条作者著作在 yuanwen 整节静默丢失（空 H3 后零 def 零残留）；duhem 表格书目完整幸存、bergson 题名开头条目成功转 def，三方对照锁定丢失机制=悬挂列表年份开头无作者条目被转译跳过。
* SUMMARY 正确性门实体发现 1 例：identity-ethics SUMMARY L1996 作者滞后（仍署 Shoemaker，2025-06-30 新版实为 Dufner）。
* 锚定率谱系实证（作者-年份锚定率跨条目 0%–91%）：spacetime-holearg 0%、logic-ai 4%、bergson 6% ↔ egalitarianism 91%、bodily-awareness 81%、identity-ethics 78%——转译批次行为不一致的量化证据；另录「目录区零锚/讨论区有锚」斑块分布与六类系统性锚定盲区（survey 组/裸名/多年份组/变音名/作者改名/forthcoming-nd）。
* 同姓同年与姓前缀误挂大爆发：Cohen 交叉互染、Wallace/Wall、Gadsby、Lush、Isaacs、Chalmers、Eliasmith 一引三 def、Rumelhart 一引四 def——同姓同年 def 对为误挂磁铁，Read&Thakkar/Leibovitz/Palmira/Dais/Coelho/Dewhurst/Silver 等年份拼写失配族。
* 上游误拼与形态实锤密度极高（全部逐条回原 HTML 计数定性、镜像忠实）：august-rehberg 16 处、physics-experiment 13 连（larue-nd "DATE" 占位符、nelson-1994-2 重复 def、Simon S. 讹名、双 Einstein 损形）、computational-mind 14 连（Krishevsky 缺 z、grice Ways of Words、maley 卷页双错）、atonement 正文 "(LINK)" 字面占位符、identity-ethics "is reflects" 语法错、sextus-empiricus C34 强调句号等——修复责任在上游会话，本战役零写入。
* 新转译形态家族（移交镜像会话）：em 边缘空格双侧破强调、span.smaller 推荐标注丢失（13 处）、表格内嵌 ul 压平、dl-dt 转四星、sup→^{} 与 sub→*{} 字面残留、正文与 def 反向引号区、References 压扁变体四型（空 H3/四连空/双层双说明行/叙述压 def 汤）、附录注编号列表与主注 def 双制、跨节重列重复 def 五对、多卷本拆孤儿 def（vol-nd）、=*{defn} 下标残留。
* 5% 层与 1% 层累计人工覆盖 113 条（6%）；全部修复责任移交镜像/管线会话，本战役零写入不改被审文件。

## 2026-10-31 遗留问题修复期：T-em-lang-drop 落地（用户授权写入）

* 用户指令："先解决遗留问题并思考纠正到软件工程理论"——本战役首次获授权对镜像写入（此前零写入仅记录）。修复对象：T-em-lang-drop（43 页 / 33 词条 / 12 语种 `<em lang>` 外语术语斜体丢失，全语种普查 1,143 实例）。
* **生成器 v2（计数对账法）** `bin/fix_em_lang.py`：放弃 v1 逐处上下文锚定（HTML↔Markdown 格式差使锚点失配率 54%，弃），改为 (文件,术语) 粒度计数对账：en 侧 lang-em 计数 vs yw 侧词界命中分类（精确星已足额/短语斜体内/自由命中），自由命中全量补 `*`。
* **对账规则**：满足前置（精确星数≥en 计数→跳过）；赤字桥接（`自由数 ≤ en−星数 ≤ 自由数+短语斜体数`→包全部自由命中）；其余 fail-closed 挂起。真相交覆盖（同起点前缀/同终点后缀/内部，srigupta 复合 em 案例）。
* **事故与根治**：首轮挂起集未冻结，次轮对挂起术语重评致超额包裹 126 处（Instauratio magna 4→19）；按 rules/05 批量改写纪律外科剥星 114 处还原，再以**冻结挂起集**（em-lang-deferred.txt 持久化、永不复评）+ 满足前置达成三轮不动点（补插 0、门2 残余 0、超额 0）。
* **终态**：自动补插 858 处（37 文件）；挂起 69 术语清单化移交人工逐处锚定（`results/para-review/em-lang-deferred.txt`）；门禁 7 项全绿。提交 a212c0ee。
* **SUMMARY 题名截断修复（第二遗留项）**：disability-care-rationing 与 disability-justice 两行丢失 `disability` 前缀（SUMMARY.md/mu-lu-s.md/yuanwen-SUMMARY 五处），对照 en h1 补回。提交 44bd34f7。
* **剩余移交**：T-math-macro-closure（465 包 local.js 宏 vs 站点 MathTypesetter.vue 无宏定义——该文件并行会话在改，009 不得触碰）；T-supplement-drop（epistemic-utility/maths-inacc.html、ergodic-hierarchy/appendix.html 未转换）。

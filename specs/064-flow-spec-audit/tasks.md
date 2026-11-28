# 任务清单：064 全流程全要素审计与规范化

- 输入：`specs/064-flow-spec-audit/spec.md`（rev 21）、`plan.md`、`results/axioms-v3.md`、`results/axioms-tasks.md`、`results/test-coverage.md`、`results/target-workflow.md`、`results/exploration-2026-11-27.md`
- 状态：**94 项已验证（T131、T168、T169、T130、T020–T024、T132、T133、T134、T135、T136、T137、T185、T186、T187、T188、T189、T190、T139、T191、T192、T141、T193、T194、T195、T143、T196、T197、T198、T199、T200、T201、T145、T146、T147、T148、T149、T150、T151、T152、T153、T202、T203、T204、T205、T206、T207、T208、T209、T210、T211、T212、T213、T214、T215、T216、T217、T218、T219、T220、T221、T222、T223、T224、T225、T226、T227、T228、T229、T230、T231、T232、T233、T234、T235、T236、T237、T238、T239、T240、T241、T242、T243、T244、T245、T246、T247、T248、T249、T250、T251）；0 项部分执行；74 项未开始；0 项撤销**。合计 **168 个编号（全部有效）**；habermas 已 `done`；logic-preference **已 `done`**；environmental-aesthetics **已 `done`**；imprecise-probabilities **已 `done`**（T209–T214；sg-03 经用户 2026-11-27 授权签字）；W1 三件＋W2 首件全部 `done`（action 于 2026-11-27 经用户 sg-03 授权签字置 `done`）；**S16 临时布局迁移 T202–T208 已完成**；W2 T155 已拆为 T215–T220 并全部完成（action `done`）；T156 已拆为 T221–T228（方案 `results/t156-decomposition.md`），**T221–T228 全部完成，axiom-choice 于 2026-11-27 经用户 sg-03 授权签字置 `done`**；T157 已拆为 T229–T234（方案 `results/t157-decomposition.md`，6 项待执行）；T159 已拆为 T244–T251（方案 `results/t159-decomposition.md`，T244–T251 全部完成、`japanese-aesthetics` 已 `done`；容器行不勾）。2026-11-26 全部批准十项建议＋流程 v2；2026-11-27 全部批准探索建议书 EP-01–09；2026-11-27 迁移轨 S0＋S3–S9 共 37 项全部批准实施（R0–R7）；A／B 组与 C 组 T132–T137 已完成，其余维持“已批准、待执行”
- **删除记录（rev21）**：S1 登记表 7 项、S11 案 B 5 项、S-1 案 B 复核 1 项已从本书**直接删除**，不保留 `[撤销]` 行；精确清单见 spec §11 rev21／§15（本文件不再引用已删 T 号）
- 新增落点：**T166（G4 测试）、T167（G6＋G8 ADR）、T168（G24／G25 治理）、T169（标准回写）、T170–T175（S14 学术翻译出版流程 v2）、T176–T184（S15 探索批准项 EP-01–09）**；**T168／T169 已于 2026-11-27 完成**，其余均为“已批准、待执行”
- **执行排程**：`results/schedule.md`（W0–W7、W0b、G0–G5、11 件逐件表；探索批准项 E0–E5）是唯一排程源；本清单只定义工作项，不复制波次。**a／b 组已完成；C 组 T132–T137 完成，habermas 全链完成并 `done`；logic-preference ex-04、T143 样章、T196（§3）、T197（§4）、T198（§5）、T199（§6）、T200（§7–§8）、T201（收口）、T145（tr-03／tr-04）、T146（rv-01／rv-02／rv-09）、T147（rv-03–08 六轴）、T148（sg-01／sg-02）完成并至 `sg-02_checked`；sg-03 待用户 mandate；environmental-aesthetics T149 ex-04、T150 样章、T151 全量、T152 校次与六轴、T153 sg 链完成并 `done`；S16 临时布局迁移 T202–T208 全部完成并收口**。
- **组界 tag**：a–k 每组开始／结束各打一枚 `batch/064-<组>-start|end`；规则见 `results/schedule.md` §8。未打 start 不开工，未打 end 不收口；tag 不替代 evidence。
- 形式约束：`results/axioms-tasks.md` 的 TA1–TA8／TH1–TH8 是本清单的结构验收面；任何修改须复跑其中的只读检查（编号、分区、验收、依赖、状态、工作包分层）
- **编号纪律**：本文件的 `S-1／S0–S15`（S1、S11 已删除，实际 15 个分区）是**任务分区**；spec §8 与 plan §7 的路线包写作 `WP-*`。`WP-S1`（标准回写）不是登记表契约
- **语言偏好**：spec §13.1 的 LPR-1–5（2026-11-26 批准）是 S4–S9 的选型依据——长期稳定调用（四问全满足）优先 Rust 且须多并发多线程，其余默认 Python，其他语言不引入新门；S-1／S0–S3／S10–S15 不改变语言分工
- 格式：`[ID] [P?] [阶段] 描述（含文件路径与验收）`；`[P]`＝不同文件、无依赖，可并行
- **粒度规则**：S-1 的 `T142–T161`、S12 的 `T166`、S14 的 `T170–T175`、S15 的 `T176–T184` 是工作包，不是可直接执行的原子任务；开工前须按 T130–T141 的“件×站段”模板拆为原子任务（从下一可用号顺序分配，不预写占位号）。T140 的 sg-01／sg-02、T141 的 sg-03 及任何 sg-03 行均须单列并检查 mandate。工作包不得整体勾选
- **门禁编号**：不预写“第 N 项”；以 `check_all.py --list-gates` 实际输出为准
- **ADR 编号**：不预占；实施前重读 `rules/adr/` 尾部取实际最大号

## 阶段 S-1 端到端试金石（2026-11-26 批准；**11 件全跑，已解冻待执行**；按件按段拆任务）

> 名单引用 `specs/060` §5.4；按 22 节点跑（案 B 已裁定不实施），用现有 Python 链。一件一段一任务、各自收口；上表未勾满不进入下一段。产出 findings 回填 spec §18.4。
> 优先级：先 habermas 走完，再 logic-preference，再 environmental-aesthetics；第二／三梯队每件单列一个任务，按轴启用。

### habermas（第一梯队 1/3）

- [x] T130 [S-1] ex-04 源审计——**机器面完成**（hard=0／warn 5，`results/e2e-habermas*.json`）；**已完成**（2026-11-27 用户批准：5 候选定性＋`,,` 入表＋`Empitical` 另立勘误条）；证据 `results/e2e-habermas.md`、`baseline/en-errata/en-errata.md` 第十三节；验收：记录含“候选总数／豁免类计数／逐条定性结论”三段，5 个候选均有处置且与 JSON 对应
- [x] T131 [S-1] G13 豁免清单落地（`rules/11-source-side.md` §5.3）——**已完成**（2026-11-26）；验收：A–E 五类清单在位、规则地图登记 11、规范登记册一致性门通过（局部判据；全库其他红线不得反向否定本任务）；配套 ADR 留待治理轮
- [x] T132 [S-1] tr-02 样章（§1–§2，约 3,000 字）：验证段落账本、step1／step2、术语注入——**已完成**（2026-11-27；账本 `tasks/h/habermas.ledger.yaml` 16 段；样章 `h/habermas.md` 约 2,350 汉字；证据 `results/c-group-evidence.md`）；验收：账本守恒、样章可读、候选逐条定性
- [x] T133 [S-1] tr-02 全量（余下各节，分 4–6 批 checkpoint）——**已完成**（2026-11-27；5 个批次由子代理产出、主代理合并；全文 38,150 汉字；账本 239 段、step2 全部落文；复核补漏 §1.1 P4 与 §1.2 交往权力段；证据 `results/c-group-evidence.md`）；验收：全文入库、账本段落数守恒
- [x] T134 [S-1] tr-03 一校（对照英文源逐节核销）——**已完成（首轮）**（2026-11-27：239 段守恒、全文机检全绿、残留外文 0；逐节锚点抽核无硬错误；术语/源缺陷挂 T136；证据 `results/t134-review.md`）；验收：对照记录；残留外文 0
- [x] T135 [S-1] tr-04 二校（语体、反欧化）——**已完成**（2026-11-27；`check_prose` 153→139，13 处改写、139 条逐条豁免留痕；`check_style` 0 issue；证据 `results/t135-review.md`）；验收：`check_prose` 告警清零或逐条豁免
- [x] T136 [S-1] rv-01 术语与勘误（术语轴＋体例轴＋勘误轴）——**已完成**（2026-11-27；新增 civil society (Habermas)=公民社会、legitimacy (Habermas)=合法性；正文统一；check_terms 硬 0；check_pairs/check_style 0；勘误两条照录区一致；证据 `results/t136-review.md`）；验收：三段 evidence
- [x] T137 [S-1] rv-02 全局一致性（两轴比较校对）——**已完成**（2026-11-27；239 段守恒；脚注 156/156、定义 254/254；密度与语体留痕；`check_pairs`/`check_style`/`check_academic --strict` 0；证据 `results/t137-review.md`）；验收：两轴记录＋机检输出
- [ ] T138 [S-1] **[工作包]** rv-03–08 六轴（q1 引文→q2 逻辑→q3 语法→q4 语域→q5 计量→q6 标点，顺序固定）——**六个原子任务 T185–T190 均已完成**（方案 `results/t138-decomposition.md`；轴定义按 `rules/04` ADR-0079）；本行只作容器，**不得整体勾选**（完成由子项派生）；验收：T185–T190 全部完成且各轴凭据落 `state/axis/` 与 `results/t185–t190-review.md`
- [x] T185 [S-1] rv-03 q1 引文锁定：成句直引清单、原著语种与原文可得性（na/present/verifiable/unavailable）、hash 锁定——`cite_audit --init/--gate`；判据 `specs/060-six-axis-quality-gates/checklists/q1-cite.md` C-1/C-2/C-3/C-4/C-6/C-7；**已完成**（2026-11-27：补引块抽取工具缺口；167 候选＝28 引块＋139 行内，pass 39、waived 128、pending 0；`--gate`/`--check-hash` 0；发现 F2 承载形态、F3 德语原文缺口；证据 `results/t185-review.md`、`state/axis/habermas.cite.json`）；验收：清单完备、字段合法、anchor 非空、verdict 无 pending、hash 守恒
- [x] T186 [S-1] rv-04 q2 逻辑一致性：谓词-论元骨架、量化与辖域、条件方向、模态——`logic_audit`（只产候选）；判据 `q2-logic.md`；**已完成**（2026-11-27：907 散句／235 承载句／30 算子候选；28 误报逐条定性、2 处 L-6 模态修正（L526、L544）；235 条全部有裁决、0 pending；`--gate` 0、q1 hash 不变；G1 全文形式化缺口登记；证据 `results/t186-review.md`、`state/axis/habermas.logic.jsonl`）；验收：候选逐条定性、无未处置告警（前置 T185）
- [x] T187 [S-1] rv-05 q3 语法：句法合法性、反欧化、和制汉语——`grammar_audit`（吸收 `check_prose`）；判据 `q3-grammar.md`；**已完成**（2026-11-27：140 条 issue＝G-11 105／G-10 32／G-9 2／G-7 1；139 条 waived（沿用 T135 逐条口径，2 条补录）＋1 条 false-positive；0 pending；G-1／G-5 为 0、和制汉语无命中；`--gate` 0；H1 第一层未全量重审已登记；证据 `results/t187-review.md`、`state/axis/habermas.grammar.json`）；验收：告警清零或逐条豁免（前置 T186）
- [x] T188 [S-1] rv-06 q4 语域：五档标尺、档位漂移、语气——`register_audit`（只产候选）；判据 `q4-register.md`；**已完成**（2026-11-27：7 节全部 R-1、无 R-4／R-5 越界；8 条文言候选全部 false-positive（“是＋以……”子串误报）；R-e／R-f 无命中；0 pending；`--gate` 0；修正工具节内相对行号→全文绝对行号（新增单测 1/1）；I1 样章基准缺失登记，须 sg-03 前处置；证据 `results/t188-review.md`、`state/axis/habermas.register.json`）；验收：档位漂移逐条定性、无未处置告警（前置 T187）
- [x] T189 [S-1] rv-07 q5 计量：量值-单位、数字形态、换算——`measure_audit`；判据 `q5-measure.md`；**已完成**（2026-11-27：量值条目 0（本件无物理单位/货币）；170 处数值范围＝164 引文页码（en-dash 照录豁免）＋6 正文范围（一字线统一）；唯一 M-6 聚合告警定性 false-positive；日期/年代形态一致；修正工具误把引用键 1992a 当量值（新增单测 4/4）；`--gate` 0；J1 本件量值面为空已登记；证据 `results/t189-review.md`、`state/axis/habermas.measure.json`）；验收：硬错误 0、告警逐条处置（前置 T188）
- [x] T190 [S-1] rv-08 q6 标点：GB/T 15834 十七种标点、邻接与禁则——`punct_audit`（吸收 `check_style` 标点项）；判据 `q6-punct.md`；**已完成**（2026-11-27：168 条 issue＝P-13 164（引文页码，waived）＋P-7 4（引文 locator 冒号，false-positive）；P-8／P-18 工具误报修复、P-20 12 处清零；正文改 12 处引文定位符标点＋1 处双冒号；工具修正加单测 4/4；`--gate` 0；K1 P-19 渲染层未验已登记；证据 `results/t190-review.md`、`state/axis/habermas.punct.json`）；验收：告警清零或逐条豁免（前置 T189）
- [x] T139 [S-1] rv-09 体例终校——**已完成**（2026-11-27：`check_style`／`check_pairs`／`check_quotes` 0；`check_academic --strict` 硬 0；`check_math_zh`／`check_math` 0；`check_terms` 硬 0（Müller-Doohm 沿用 T136 豁免）；H1／pubinfo／尾序／编号／勘误承载一致；未改文；F2／F3／I1／K1 转 sg 链前处置；证据 `results/t139-review.md`）；验收：`check_style` 0 issue（前置 T190）
- [ ] T140 [S-1] **[工作包]** sg-01／sg-02（初审＋复审）——**已拆为 T191–T192，两项均已完成**；本行只作容器，**不得整体勾选**；验收：T191／T192 均完成且记录落 `results/`
- [x] T191 [S-1] sg-01 初审（Verity）：抽 3–5 段，以哲学专业本科生为假设读者，判可读性、术语习惯、背景提示、语体一致——**已完成**（2026-11-27：抽 §1.2／§2.2／§3.3／§4.3／§7.2 五段，四维均通过；V1 引块断句转 F2、V2 次属反公共领域转 rv-01；未改文；证据 `results/t191-sg01.md`）；验收：适切性记录含抽样段、四维结论、签字（前置 T139）
- [x] T192 [S-1] sg-02 复审（Coherence）：全文逻辑链、指代、跨节呼应、段落衔接——**已完成**（2026-11-27：七节逻辑链完整；199 句代词起首抽 32 组无歧义；跨节呼应一致；C1“第三个显著特征”Minor 观察、C2 转 F2；问题单无 Critical／Major；未改文；证据 `results/t192-sg02.md`）；验收：复核记录＋问题单（前置 T191）
- [x] T141 [S-1] sg-03 终审（需用户显式指定 `--mandate`）——**已完成**（2026-11-27：用户以 `user` 身份签署；`--mandate` 记录已补全；CI `check_all` 23/23；交付清单完整、pin 有效；F2／F3／I1／K1 按授权结案；状态 `sg-03_checked` → `done`；证据 `results/t141-final.md`）；验收：CI 全绿＋签字

### logic-preference（第一梯队 2/3；工作包，须按站段拆分）

- [ ] T142 [S-1] **[工作包]** ex-04 源审计——**已拆为 T193–T195，三项均完成**（方案 `results/t142-decomposition.md`）；本行只作容器，**不得整体勾选**；验收：T193–T195 完成且证据落 `results/`
- [x] T193 [S-1] ex-04 机检面：`en_integrity`＋`en_source_audit`；统计行内公式（实测 417；原 362 为旧口径）、节集合、表格／图片、文献条目；记录 hard／warn 与抓取最终状态——**已完成**（2026-11-27：en 完整性 clean；源审计 hard 0（修 `\\[` 误计后；原误报 45/43）＋warn 5；check_math 429／missing 0；四项计数：公式 417／43、H2 12／H3 16、表 1／图 2、脚注定义 67；证据 `results/t193-ex04-machine.md`＋三份 JSON）；验收：四项计数齐全、hard 0 或逐条登记、无静默跳过（前置 T142）
- [x] T194 [S-1] ex-04 人工定性：候选逐条回源，按 Critical／Major／Minor 定性；区分文字缺陷（全局勘误表）与格式问题（补丁池）；三段式汇总——**已完成**（2026-11-27：H1 math_delim 为 `\\[1em]` 误计（已修 en_source_audit，hard 0）；W1 页脚 h4、W2 win2022、W3–W5 引用键、U1 `$1` 货币误判均为 false-positive；无 Critical／Major，不建勘误／补丁；D1 任务书 362→实测 417 已回写 T143；证据 `results/t194-ex04-human.md`）；验收：候选总数／豁免类计数／逐条结论齐全（前置 T193）
- [x] T195 [S-1] G13 豁免清单（按需）：A–E 类源侧候选按 `rules/11-source-side.md` §5.3 建清单；无候选则记录“无需建清单”——**已完成**（2026-11-27：typo 候选 4＝A 类 1（win2022）＋非 A–E 误报 3（2013a,b）；B／C／D／E 均 0；无真候选，**无需建清单**；证据 `results/t195-g13.md`）；验收：清单在位或理由与检查范围留痕（前置 T194）
- [x] T143 [S-1] tr-02 样章（§1–§2）——**已完成**（2026-11-27：`l/logic-preference.md` 159 行／3,107 汉字；源样章 125 个公式（14 display＋82 `$`＋29 `\(`）数学结构 125/125，定界符配对；2 处公式内英文连接语按 C8 译为中文；check_style／check_math_zh／check_quotes 0，check_terms 硬 0，check_academic 在途无硬错误；check_pairs 2 条样章范围缺口；证据 `results/t143-review.md`）；验收：公式定界符与 **417 处**行内公式样本无损（样章实测 125 个）
- [ ] T144 [S-1] **[工作包]** tr-02 全量——**已拆为 T196–T201**（方案 `results/t144-decomposition.md`）；**T196–T201 六项均完成，容器按 TA7 不勾选**；本行只作容器，**不得整体勾选**；验收：T196–T201 完成且全文入库
- [x] T196 [S-1] tr-02 全量批 1：§3 语义进路（3.1 雷舍尔-范达伦、3.2 可能世界偏好、3.3 偏好提升）——**已完成**（2026-11-27：§3 入库，文件 327 行／5,077 汉字；源 §3 公式 81（7 display＋74 行内）覆盖 81/81；SEP 宏展开 `⟦⟧`／`:=`；C8 连接语译中文；check_style／check_quotes 0、check_math_zh 仅 1 条 C10 提醒、check_terms 硬 0；证据 `results/t196-review.md`）；验收：§3 公式逐条保留、段落账本（前置 T143）
- [x] T197 [S-1] tr-02 全量批 2：§4 基于理由的偏好（内在/外在、双层结构）——**已完成**（2026-11-27：§4 入库，文件 438 行／7,276 汉字；源 §4 公式 53（5 display＋48 行内）覆盖 53/53；check_style／check_quotes 0、check_math_zh 仅 1 条 C10 提醒、check_terms 硬 0；证据 `results/t197-review.md`）；验收：§4 公式与术语一致（前置 T196）
- [x] T198 [S-1] tr-02 全量批 3：§5 偏好改变（5.1–5.3）——**已完成**（2026-11-27：§5 入库，文件 577 行／9,859 汉字；源 §5 公式 51（10 display＋41 行内）覆盖 51/51，2 处引号符号按渲染等价改写并留痕；check_style／check_quotes 0、check_math_zh 仅 1 条 C10 提醒、check_terms 硬 0；证据 `results/t198-review.md`）；验收：§5 公式与动态逻辑术语一致（前置 T197）
- [x] T199 [S-1] tr-02 全量批 4：§6 其他条件不变偏好与 CP-nets（6.1–6.2）——**已完成**（2026-11-27：§6 入库，文件 669 行／11,429 汉字；源 §6 公式 73（3 display＋70 行内）覆盖 73/73；check_style／check_quotes 0、check_math_zh 仅 C10 提醒、check_terms 硬 0；证据 `results/t199-review.md`）；验收：§6 公式与 CP-net 术语一致（前置 T198）
- [x] T200 [S-1] tr-02 全量批 5：§7 研究领域交叉＋§8 结论——**已完成**（2026-11-27：§7–§8 入库，文件 731 行／13,136 汉字；源 §7–§8 公式 7（2 display＋5 行内）覆盖 7/7；新增脚注定义 10 条、全文 43 条无重复无悬空；check_style／check_quotes 0、check_math_zh 仅既有 C10 提醒、check_terms 硬 0；证据 `results/t200-review.md`）；验收：§7–§8 入库、无漏段（前置 T199）
- [x] T201 [S-1] tr-02 全量收口：尾节四件套＋脚注定义、全量账本、project_spec／pe 字段、全文公式与门禁——**已完成**（2026-11-27：全文 798 行／13,283 汉字；尾节四件套按序入库；脚注定义 67/67；账本 301 段（300 body＋1 oir）step2 与正文 300/300 块一致；project_spec 六项＋llm-pe/full 字段补齐；`advance --step tr-02` 通过、状态 `tr-02_checked`；check_pairs 0 issue、check_all 23/23；证据 `results/t201-review.md`）；验收：全文入库、账本守恒、`advance --step tr-02` 通过（前置 T200）
- [x] T145 [S-1] 校次链 tr-03／tr-04——**已完成**（2026-11-27：tr-03 账本 301 段守恒、机检全绿、残留外文 0、逐节锚点无硬错误（`results/t145-tr03.md`）；tr-04 check_prose 12→0、12 处逐条改写无豁免、账本重建（`results/t145-tr04.md`）；两站均 `check_all` 23/23；状态推进 `tr-03_checked → tr-04_checked`）；验收：同 T134／T135
- [x] T146 [S-1] rv-01／rv-02／rv-09——**已完成**（2026-11-27：rv-01 三轴完成、术语登记主形“其他条件不变偏好”、§6.1 符号疑误入勘误表第十四节并由译者注释①承载（`results/t146-rv01.md`）；rv-02 两轴复检 301 段守恒、密度与冷置回读留痕（`results/t146-rv02.md`）；rv-09 体例终校通过（`results/t146-rv09.md`）；状态 `rv-02_checked → rv-09_checked`）；验收：同 T136／T137／T139
- [x] T147 [S-1] 六轴 rv-03–08——**已完成**（2026-11-27：rv-03 引文 30 候选（pass 6／waived 24、pending 0）；rv-04 逻辑 460 句、承载 128、2 处 L-6 修正；rv-05 语法 0 告警；rv-06 语域 8 节均 R-1；rv-07 计量量值 0、候选全误报；rv-08 标点 P-7 2 处已修；六轴 `--gate` 均 0，证据 `results/t147-rv03.md`–`t147-rv08.md`）；验收：各轴凭证
- [x] T148 [S-1] sg 链——**已完成（sg-01／sg-02／sg-03）**（2026-11-27：sg-01 初审四维通过、无 Critical／Major（`results/t148-sg01.md`）；sg-02 复审逻辑链与指代一致、问题单无 Critical／Major（`results/t148-sg02.md`）；sg-03 经用户 2026-11-27 授权签字、交付清单与 version_pin 核验通过（`results/t148-sg03.md`）；状态至 `done`）；验收：sg-01／sg-02 分列；sg-03 另核 mandate

### environmental-aesthetics（第一梯队 3/3；工作包，须按站段拆分）

- [x] T149 [S-1] ex-04 源审计（重点：369 条文献条目）——**已完成**（2026-11-27：`en_integrity` clean 1/1、资产缺件 0；`en_source_audit` hard 0、warn 2（win2016／sum2024 为存档 URL 段，false-positive）；脚注定义 369、标记 489（不同键 341）、标题 24、表 1、图 0、公式 0；无 Critical／Major；证据 `results/t149-review.md`）；验收：书目计数
- [x] T150 [S-1] tr-02 样章（§1–§2）——**已完成**（2026-11-27：`zh/e/environmental-aesthetics.md` §1–§2＋导论入库，480 行／8,125 汉字；193 个不同脚注键全部闭合、443 处标记；无公式；check_style／check_quotes／check_math_zh 0、check_terms 硬 0、check_academic 在途无硬错误；check_pairs 仅样章范围缺口；证据 `results/t150-review.md`）；验收：文献键位与脚注配对
- [x] T151 [S-1] tr-02 全量——**已完成**（2026-11-27：全文 961 行／15,007 汉字；96 正文块与 en 96 块一致；369 条脚注定义、489 处标记（341 键）；尾节四件套＋致谢；账本 98 段（96 body＋2 oir）守恒；check_pairs 0 issue、check_style／check_quotes／check_math_zh 0、check_terms 硬 0、check_academic --strict 无硬错误、check_all 23/23；证据 `results/t151-review.md`）；验收：全文入库
- [x] T152 [S-1] 校次链与 rv 链（重点 q1 引文）——**已完成**（2026-11-27：tr-03 98 段守恒、tr-04 `check_prose` 19→2（2 豁免）；rv-01 六组术语按册统一、22 人名 D5 豁免；rv-02 密度与冷置回读；rv-03 引文 18 候选（pass 9／waived 9）；rv-04 380 句、候选 15 全 equivalent；rv-05 语法 2 豁免；rv-06 4 节 R-1；rv-07 计量 0；rv-08 标点 3 条处置；rv-09 体例终校通过；状态至 `rv-09_checked`；证据 `results/t152-tr03/tr04/rv01–rv09.md`）；验收：引文 hash 锁定
- [x] T153 [S-1] sg 链——**已完成**（2026-11-27：sg-01 初审四维通过、无 Critical／Major（`results/t153-sg01.md`）；sg-02 复审逻辑链与跨节呼应一致、无 Critical／Major（`results/t153-sg02.md`）；sg-03 经用户 2026-11-27 授权签字、交付清单与 version_pin 核验通过（`results/t153-sg03.md`）；状态至 `done`）；验收：同 T141；分节点执行

### 第二梯队（工作包；核心 3 件至 sg-02 后启用，执行前须拆站段）

- [ ] T154 [S-1] **[工作包]** `i/imprecise-probabilities`（14 类构件命中 12 类）全流程——**已拆为 T209–T214**（方案 `results/t154-decomposition.md`；14 类清单与实测计数见方案 §二）；**T209–T214 全部完成，本件已 `done`**；本行只作容器，**不得整体勾选**（完成由子项派生）；验收：T209–T214 全部完成且本件 `done`，14 类构件无丢失
- [x] T209 [S-1] ex-04 源审计：`en_integrity`＋`en_source_audit`＋`check_math`；10 条 warn 与 6 条 unbalanced 逐条回源定性；复核 14 类构件计数；189 脚注键闭合、2 图资产在位；G13 按需——**已完成**（2026-11-27：en_integrity clean 1/1；en_source_audit hard 0／warn 10；check_math 370、missing 0、unbalanced 6；16 条候选全部 false-positive，无 Critical／Major，不建勘误与补丁；构件 12/14；脚注 189 键闭合、图 2、表 1；G13 无需建清单；证据 `results/t209-review.md`）；验收：候选总数／豁免类计数／逐条结论三段齐全，hard 0 或逐条登记，无静默跳过
- [x] T210 [S-1] tr-02 样章（§1–§1.2，14,244 源字符）：术语表与重要区分；76 行内公式＋1 display、35 脚注引用、1 引块、13 列表项——**已完成**（2026-11-27：32/32 块对应、2,862 汉字；76＋1 公式逐式无缺失，8 处孤立 Ω 按 ADR-0049 转 `*Ω*`；33 脚注键闭合、无悬空；check_style／check_quotes／check_math_zh 0、check_terms 硬 0、check_academic --strict 无硬错误；check_pairs 余 3 条样章范围缺口；术语表畸形条目已修正；两份补充材料 H1 存根已建；证据 `results/t210-review.md`）；验收：公式与构件按 14 类清单无损；样章块数与 en 对应（账本随 T211 全量收口）
- [x] T211 [S-1] tr-02 全量：§2–§4＋尾节四件套＋189 脚注定义；分 3 批 checkpoint（§2／§3／§4＋尾节）；全量账本与 `project_spec`／`pe` 字段——**已完成**（2026-11-27：764 行／18,478 汉字；165/165 块对应；账本 169 段（165 body＋4 oir）step1=step2；189 脚注定义／179 引用闭合；图 2、表 1、display 4 完整；公式差额 11 处归因；上游缺陷 2 处入勘误第十五节并加译者注释①②；check_pairs／check_style／check_quotes／check_math_zh 0、check_terms 硬 0、check_academic --strict 无硬错误、check_all 23/23；证据 `results/t211-review.md`）；验收：全文入库、189 脚注闭合、4 display＋366 行内公式与 2 图 1 表无损、账本守恒、`advance --step tr-02` 通过
- [x] T212 [S-1] 校次链 tr-03／tr-04：一校逐节核销、二校语体与反欧化——**已完成**（2026-11-27：tr-03 账本 169 段守恒、165/165 块对应、189 脚注闭合、残留外文 0；tr-04 `check_prose` 33→7，26 处实改，余 7 条全为直接引文（Joyce／Kaplan／Levi／Walley）逐条豁免；两站 check_all 23/23；证据 `results/t212-review.md`）；验收：账本守恒、残留外文 0、两站 `check_all` 全绿
- [x] T213 [S-1] rv 链：rv-01 三轴→rv-02 全局一致性→rv-03–08 六轴→rv-09 体例终校——**已完成**（2026-11-27：rv-01 术语／体例／勘误三轴通过；rv-02 169 段守恒、冷置回读五段一致；rv-03 引文 40 候选＝13 引块 pass＋27 行内 waived，`--gate`／`--check-hash` 0；rv-04 676 句／242 承载全部 equivalent、43 算子候选复核；rv-05 语法 8 告警＝7 引文 waived＋1 G-7 误报；rv-06 四节均 R-1、`弄错`→`判断有误`；rv-07 量值 0、数值面一致；rv-08 标点 15→10，5 处 P-7 实改、10 条豁免；rv-09 体例终校全绿，check_all 23/23；证据 `results/t213-rv01`–`t213-rv09.md`）；验收：各轴凭据落 `state/axis/`、`--gate` 0 或逐条豁免
- [x] T214 [S-1] sg 链：sg-01 初审、sg-02 复审、sg-03 终审（须用户 `--mandate`）——**已完成**（2026-11-27：sg-01 抽五段、四维通过、无 Critical／Major（`results/t214-sg01.md`）；sg-02 四节逻辑链完整、指代与跨节呼应一致、无 Critical／Major（`results/t214-sg02.md`）；sg-03 经用户 2026-11-27 授权签字，交付清单与 version_pin 核验通过（`results/t214-sg03.md`）；状态至 `done`）；验收：sg-01／sg-02 无 Critical／Major；sg-03 另核 mandate
- [ ] T155 [S-1] **[工作包]** `a/action`（长文＋引文双密集）全流程——**已拆为 T215–T220**（方案 `results/t155-decomposition.md`）；本行只作容器，**不得整体勾选**（T215–T220 均已完成，action 2026-11-27 `done`；容器按 TA7 保持未勾）；验收：T215–T220 全部完成且本件 `done`
- [x] T215 [S-1] ex-04 源审计：`en_integrity`＋`en_source_audit`＋`check_math`；warn／unbalanced 逐条回源；320 脚注键闭合；14 类构件复核；G13 按需——**已完成**（2026-11-27：en_integrity clean 1/1；en_source_audit hard 0／warn 19；check_math 8、missing 0、unbalanced 0；19 条候选＝12 false-positive＋7 纯排版缺陷（入勘误第十六节，只入表不加译注）；构件 10/14；脚注 320 键闭合、引用 381 处；G13 无需建清单；证据 `results/t215-review.md`）；验收：三段式汇总、hard 0 或逐条登记、无静默跳过
- [x] T216 [S-1] tr-02 样章（§1–§2，22,450 源字符）：行动问题＋因果论（2.1–2.4）；样章账本——**已完成**（2026-11-27：`zh/a/action.md` 193 行／5,776 汉字；`tasks/a/action.ledger.yaml` 31 段；块类、7 标题、4 引块、75 脚注标记顺序一致、63 条定义逐字一致；13 条术语先登记后用；check_style／check_quotes／check_math_zh 0，check_terms 硬 0，check_academic --strict 0；check_pairs 4 条样章范围缺口留 T217；证据 `results/t216-review.md`）——验收：公式与构件无损、块数与 en 对应、术语先登记后用
- [x] T217 [S-1] tr-02 全量：§3–§8＋尾节＋320 脚注；分 3 批 checkpoint（§3–§4／§5–§6／§7–§8＋尾节）；全量账本与 `project_spec`／`pe` 字段——**已完成**（2026-11-27：五个子代理分五批翻译、主代理复核合稿；`zh/a/action.md` 1,109 行／29,238 汉字；230 块对应、375 脚注标记等序、320 定义逐字一致；`tasks/a/action.ledger.yaml` 219 段；`project_spec`／`pe` 已补；check_style／check_quotes／check_math_zh 0，check_terms 硬 0，check_academic --strict 0，check_all 23/23；check_pairs 仅 6 条原文 note 计数口径差；check_prose 101 条留 T218；证据 `results/t217-review.md`）；状态 `ex-04_checked → tr-02_checked`——验收：全文入库、320 脚注闭合、7 行内＋1 display 公式与 12 引块/4 列表/25 链接完整、账本守恒、`advance --step tr-02` 通过
- [x] T218 [S-1] 校次链 tr-03／tr-04：一校逐节核销、二校语体与反欧化——**已完成**（2026-11-27：两个子代理分段一校，Critical 1／Major 9 全部落地、Minor 23 采纳 18；tr-04 将 check_prose 101→8，93 条 FIX 落地、8 条按表豁免（直接引文 5、机检误报 3）；结构 230 块、375 标记、320 定义守恒；check_style／quotes／math_zh／terms／academic 硬错误 0；证据 `results/t218-tr03.md`、`results/t218-tr04.md`）；状态 `tr-02_checked → tr-04_checked`——验收：账本守恒、残留外文 0、两站 `check_all` 全绿
- [x] T219 [S-1] rv 链：rv-01 三轴→rv-02→rv-03–08 六轴→rv-09——**已完成**（2026-11-27：rv-01 术语硬 0／体例 gate 0／勘误第十七节 8 条＋译注①；rv-02 两轴比较与账本重建；q1 64 条 pass 20／waived 44、q2 304 条 equivalent、q3 9 条豁免、q4 8 节 R-1＋1 处改词、q5 量值 1 条误识别、q6 18 条 17 豁免；六轴 gate 均 0；rv-09 体例终校 0；证据 `results/t219-rv02.md`–`t219-rv09.md`）；状态 `rv-02_checked → rv-09_checked`——验收：各轴凭据落 `state/axis/`、`--gate` 0 或逐条豁免
- [x] T220 [S-1] sg 链：sg-01／sg-02／sg-03（须用户 `--mandate`）——**已完成**（2026-11-27：sg-01 抽 5 段四维评估、sg-02 全篇逻辑链＋20 组指代＋10 处跨节；两轮均发现 §3 首段否定辖域 Critical 1，已并回单句；Major 5 已改；Minor 采纳 8／保留 4；sg-03 经用户 2026-11-27 AskUserQuestion“授权并签字”执行，交付清单完整、六轴 gate 0、check_all 23/23、320 脚注闭合；证据 `results/t220-sg01.md`、`t220-sg02.md`、`t220-sg03.md`）；状态 `sg-01_checked → sg-02_checked → sg-03_checked → done`——验收：sg-01／sg-02 无 Critical／Major；sg-03 未授权则止于 `sg-02_checked`
- [ ] T156 [S-1] **[工作包]** `a/axiom-choice`（517 行内公式＋16 display＋4 表）全流程——**已拆为 T221–T228**（方案 `results/t156-decomposition.md`）；本行只作容器，**不得整体勾选**（T221–T228 全部完成，本件已 `done`）；验收：公式与表无损；T221–T228 全部完成且本件 `done`
- [x] T221 [S-1] ex-04 源审计：`en_integrity`＋`en_source_audit`＋`check_math`；111 脚注键闭合；14 类构件复核——**已完成**（2026-11-27：en_integrity clean 1/1；en_source_audit hard 0、warn 3（orphan_note 1 聚合＋doubled_word 2，均 false-positive）；check_math 547、missing 0、unbalanced 2（`$0 \ne 1$` 的 `\ne` 被误当换行）；111 定义闭合；14 类命中 12/14；证据 `results/t221-review.md`）；状态 `cleared → ex-04_checked`——验收：三段式汇总、hard 0 或逐条登记、无静默跳过
- [x] T222 [S-1] tr-02 样章（§1，10,500 源字符，68 行内＋2 display＋1 表）——**已完成**（2026-11-27：`zh/a/axiom-choice.md` 30 块、68 行内／2 display／11 行表、22 标记、23 脚注；账本 30 段；SEP 宏全展开；check_style／quotes／math_zh 0、terms 硬 0、academic 0；check_pairs 3 条样章缺口；证据 `results/t222-review.md`）——验收：公式与表无损、块数与 en 对应、术语先登记后用
- [x] T223 [S-1] tr-02 批 1（§2–§3，14,913 源字符，226 行内＋2 display＋1 表）——**已完成**（2026-11-27：26 块、15 标记、2 display、7 行表；行内 226→227 为 en L86 定界符错位的正确拆读并登记勘误第十八节；`\sI` 脚注残留已展开；账本 56 段；check_style／quotes／math_zh 0、terms 硬 0、academic 0；证据 `results/t223-review.md`）——验收：§2–§3 入库、公式配对、账本守恒
- [x] T224 [S-1] tr-02 批 2（§4–§5，19,201 源字符，179 行内＋12 display＋1 表＋补充文档链接）——**已完成**（2026-11-27：90 块、22 标记、12 display、12 行表；行内 179→178 为孤立 `$\mu$` 按 ADR-0049 转文字；en L86 定界符错位与 L243 游离 `^{,}` 入勘误第十八节；账本 146 段；check_style／quotes／math_zh 0、terms 硬 0、academic 0；证据 `results/t224-review.md`）——验收：§4–§5 入库、display 与表无损
- [x] T225 [S-1] tr-02 批 3（尾节＋111 脚注＋补充文档注记）——**已完成**（2026-11-27：602 行／9,143 汉字；159 块、60 标记、473 行内、16 display、4 表块、111 定义、7 条补充注记；补译导论段；补充文档链接改上游页；check_pairs 0、style／quotes／math_zh 0、terms 硬 0、academic 0；账本 148 段；证据 `results/t225-review.md`）；状态 `ex-04_checked → tr-02_checked`——验收：尾节合体例、111 脚注闭合、7 条补充注记照译
- [x] T226 [S-1] tr-03／tr-04 校次——**已完成**（2026-11-27：两个子代理分段一校，Critical 0／Major 4 全部落地（两处定义主宾倒置、note-3/5 引块、note-21 压行），Minor 11 采纳 8；tr-04 check_prose 23→6（6 条数学定义句 de-chain 逐条豁免）；勘误第十八节 6 条＋译注①；check_style／quotes／math_zh／terms／academic／pairs 硬 0；证据 `results/t226-tr03.md`、`t226-tr04.md`）；状态 `tr-02_checked → tr-04_checked`——验收：账本守恒、残留外文 0、检查器全绿
- [x] T227 [S-1] rv 链：rv-01→rv-02→rv-03–08→rv-09——**已完成**（2026-11-27：rv-01 术语硬 0／体例 gate 0／勘误第十八节 6 条＋译注①；rv-02 两轴比较；q1 11 条 pass 10／waived 1、q2 274 条 equivalent、q3 6 条 de-chain 豁免、q4 5 节 R-1、q5 无物理量值、q6 3 条年份改一字线；六轴 gate 0；rv-09 体例终校 0；证据 `results/t227-rv03.md`–`t227-rv09.md`）；状态 `rv-02_checked → rv-09_checked`——验收：各轴凭据落 `state/axis/`、`--gate` 0 或逐条豁免
- [x] T228 [S-1] sg 链：sg-01／sg-02／sg-03（sg-03 须用户 `--mandate`）——**已完成**（2026-11-27：sg-01 抽 5 段，Critical 2 已改（f≤g 每一处、词数例译注②），Major 6 已改 5（选择子括注、R 公式勘误＋译注③、LST 条件句、真类注、族统一），Minor 采纳 9；sg-02 通读＋22 组指代＋9 处跨节，Major 1（§2 “后者”）已改；sg-03 经用户 2026-11-27 答复“批准终审。复核后继续”授权签字，`--mandate` 已记录；602 行／9,143 汉字、159 块、60 标记、111 定义，check_all 23/23、check_pairs 0、六轴 gate 0；证据 `results/t228-sg01.md`、`t228-sg02.md`、`t228-sg03.md`）；状态 `sg-02_checked → sg-03_checked → done`——验收：sg-01／sg-02 无 Critical／Major；sg-03 用户授权且 CI 全绿
- [ ] T157 [S-1] **[工作包]** `n/newton-principia`（36,082 汉字＋3 图）全流程——**已拆为 T229–T234**（方案 `results/t157-decomposition.md`）；本行只作容器，**不得整体勾选**（T229–T234 全部完成，本件已 `done`）；验收：图与版式无损；T229–T234 全部完成且本件 `done`
- [x] T229 [S-1] ex-04 源审计：`en_integrity`＋`en_source_audit`＋`check_math`；96 脚注键（59 编号注＋37 书目键）闭合；3 图资产闭包；14 类构件复核；3 条 warn 逐条定性——**已完成**（2026-11-27：en_integrity clean 1/1；en_source_audit hard 0／warn 3，heading_skip 为页面模板 h4、orphan_note 为 notes.html 数字锚点口径、`pp. 31-70..` 为 D 类真候选入勘误第十九节；check_math 0 公式；59 编号注 59/59 闭合、35 条书目键按设计无文内引用；3 图哈希同基线、fetch_audit 缺件 0；版本钉一致；证据 `results/t229-review.md`）；状态 `cleared → ex-04_checked`——验收：三段式汇总、hard 0 或逐条登记、图资产在位、无静默跳过
- [x] T230 [S-1] tr-02 样章（导论＋§1，13,010 源字符，3 脚注引用、3 引块）——**已完成**（2026-11-27：13 块与 en 一一对应；3 条 `note-*` 引用、3 引块完整；登记术语 12 条先登记后用（absolute motion、attraction、clockwork universe、contact mechanism、forces of nature、impulse、law/laws of motion、lunar apogee、mean motion、orbital mechanics、physical geodesy）；check_style／quotes／math_zh 0，terms 硬 0，academic 无硬错误，check_pairs hard 0（样章范围 1 条 out_of_scope）；账本 `tasks/n/newton-principia.ledger.yaml` 13 段；证据 `results/t230-review.md`）——验收：构件无损、块数与 en 对应、术语先登记后用
- [x] T231 [S-1] tr-02 全量（§2–§10＋尾节＋96 脚注定义；5 批：§2–§4／§5–§6／§7–§8／§9–§10＋尾节／Notes）——**已完成**（2026-11-27，五批逐段译后编辑 PE：255 段账本与 en 块一一对应；35,900 汉字（目标 36,082）；96 脚注定义（59 编号注译＋37 书目键照录）、62 引用、3 图、23 引块、12 链接、15 H2／2 H3 守恒；学术工具表按体例转 4 项列表；新增术语 5 条（finite-difference method、line of apsides、Newtonian fluid、perfect fluid、rigid body）；勘误第十九节 5 条；check_style／quotes／math_zh 0、check_pairs hard 0／out_of_scope 0、terms 硬 0、academic 无硬错误；证据 `results/t231-review.md`）；状态 `ex-04_checked → tr-02_checked`——验收：全文入库、96 定义闭合、3 图 1 表 23 引块完整、账本守恒
- [x] T232 [S-1] tr-03／tr-04 校次——**已完成**（2026-11-27：tr-03 块配对 255/255、96 脚注键集合一致、20 项数字年代抽核、10 处重点段落回源，修正 3 项（太阳地平视差、残留星号、生硬表述），无 Critical／Major；tr-04 `check_prose` 184→156，weak-verb 17→0、passive-bei 11→3（引文）、plural-men 1→0，long-sentence 78／de-chain 75 逐条豁免留痕；check_style／quotes 0、terms 硬 0；证据 `results/t232-tr03.md`、`t232-tr04.md`）；状态 `tr-02_checked → tr-04_checked`——验收：账本守恒、残留外文 0（书目与拉丁引文除外）、检查器全绿
- [x] T233 [S-1] rv 链：rv-01→rv-02→rv-03–08（六轴）→rv-09——**已完成**（2026-11-27：rv-01 术语硬 0（5 条告警定性）／体例 hard 0／勘误第十九节 5 条；rv-02 冷置回读 255 段／96 定义；q1 89 条均 waived（block anchor 21）、q2 708 句／249 承载均 equivalent、q3 157 条 waived、q4 10 节 R-1、q5 5 量值 pass＋2 M-4 false-positive、q6 P-13 7 处改一字线＋P-7 拆句＋P-5 4 条 false-positive；六轴 gate 全 0；rv-09 `check_style`／`quotes`／`math_zh` 0、`pairs` hard 0、`terms` 硬 0、`academic` 无硬错误；证据 `results/t233-rv01.md`–`t233-rv09.md`）；状态 `tr-04_checked → rv-09_checked`——验收：各轴凭据落 `state/axis/`、`--gate` 0 或逐条豁免
- [x] T234 [S-1] sg 链：sg-01／sg-02／sg-03（sg-03 须用户 `--mandate`）——**已完成**（2026-11-27：sg-01 抽 §2／§5／§8／§9／§10 五段，四维 B+／A−／B+／A−，无 Critical／Major，m1／m2 已采纳；sg-02 全文通读＋20 组指代＋4 组前者／后者＋10 处跨节引用，无 Critical／Major／Minor；sg-03 经用户 2026-11-27“批准终审”授权签字，537 行／35,900 汉字、255 段、96 定义、3 图，check_all 23/23、六轴 gate 全 0；证据 `results/t234-sg01.md`、`t234-sg02.md`、`t234-sg03.md`）；状态 `sg-02_checked → sg-03_checked → done`——验收：sg-01／sg-02 无 Critical／Major；sg-03 用户授权且 CI 全绿

### 第三梯队（工作包；单项极值，按轴专项启用，执行前须拆站段）

- [ ] T158 [S-1] **[工作包]** `l/logic-dynamic`（行内公式 602 处）——**已拆为 T235–T243**（方案 `results/t158-decomposition.md`）；本行只作容器，**不得整体勾选**；验收：公式定界符全配对；T235–T243 全部完成且本件 `done`
- [x] T235 [S-1] ex-04 源审计：`en_integrity`＋`en_source_audit`＋`fetch_audit`；5 条 typo 候选定性；604／666 公式口径核对；55 脚注键与 54 条书目口径；2 图资产——**已完成**（2026-11-27：en_integrity clean 1/1；en_source_audit hard 0／warn 5，4 条 sat sat 为列表剥离数学误报、1 条 and and 真候选入勘误第二十节；fetch_audit 缺件 0；55 定义 0 真实引用、54 书目键；2 图哈希同基线；版本钉一致；证据 `results/t235-review.md`）；状态 `cleared → ex-04_checked`——验收：三段式汇总、hard 0 或逐条登记、图资产在位
- [x] T236 [S-1] tr-02 样章（§1＋§2.1，14,810 源字符，256 行内公式＋2 图）——**已完成**（2026-11-27/28：2 个子代理分段译导论＋§1 与 §2＋§2.1，主代理合并 PE；实入库 16,153 源字符、44 块、259 公式（含宏展开）、7 个列表块、2 图；登记术语 22 条（4 处撞形处置）；check_style／quotes／math_zh 0、terms 硬 0、academic 无硬错误、check_pairs hard 0（样章 out_of_scope 1）；账本 44 段；证据 `results/t236-review.md`）——验收：公式与图无损、块数与 en 对应、术语先登记后用
- [x] T237 [S-1] tr-02 批 1（§2.2–§2.3，10,518 源字符，123 公式）——**已完成**（2026-11-28：单子代理翻译、主代理核验；56 块、123 公式逐块多重集一致、2 张推演表各 6 行；check_style／quotes／math_zh 0、terms 硬 0、academic 无硬错误、check_pairs hard 0（out_of_scope 1）；账本 100 段；证据 `results/t237-review.md`）——验收：公式配对、推演表完整、账本守恒
- [x] T238 [S-1] tr-02 批 2（§3，12,761 源字符，106 公式＋4 display＋4 表块）——**已完成**（2026-11-28：单子代理翻译、主代理核验；41 块、106 公式、4 display（8 个 `$$`）、2 张推演表（7／14 行）；修正 C2 定界符空白 1 处并入勘误；check_style／quotes／math_zh 0、terms 硬 0、academic 无硬错误、check_pairs hard 0（out_of_scope 1）；账本 141 段；证据 `results/t238-review.md`）——验收：display 与规则表逐行完整、账本守恒
- [x] T239 [S-1] tr-02 批 3（§4，12,272 源字符，116 公式）——**已完成**（2026-11-28：单子代理翻译、主代理核验；45 块、116 处公式（`$\mu$`／`$\Delta$` 按 ADR-0049 转文字、1 处 C8 公式连接语中文化）、4 条列表、5 个变体专名；check_style／quotes／math_zh 0、terms 硬 0、academic 无硬错误、check_pairs hard 0（out_of_scope 1）；账本 186 段；证据 `results/t239-review.md`）——验收：四个变体定义与公式无损、账本守恒
- [x] T240 [S-1] tr-02 批 4（§5＋尾节＋55 脚注定义）——**已完成**（2026-11-28：主代理全量入库；573 行／9,702 汉字、251 块／251 段账本、602 行内公式、4 display 对、55 脚注定义、2 图；check_style／quotes／math_zh 0、terms 硬 0、academic 无硬错误、check_pairs hard 0／out_of_scope 0；证据 `results/t240-review.md`，已推进 `tr-02_checked`）——验收：尾节合体例、55 脚注闭合、书目键照录
- [x] T241 [S-1] tr-03／tr-04 校次——**已完成**（2026-11-28：一校逐节对照 en，Critical 0／Major 1（“对合的分配性”误译）／Minor 6，上游括号误植入勘误；二校 `check_prose` 13→0 无豁免，语体结论现代汉语学术书面语；两站证据 `results/t241-tr03.md`、`results/t241-tr04.md`，已推进 `tr-04_checked`）——验收：账本守恒、残留外文 0（书目与公式除外）、检查器全绿
- [x] T242 [S-1] rv 链：rv-01→rv-02→rv-03–08→rv-09——**已完成**（2026-11-28：rv-01 术语 D1 两处修复、体例/勘误全绿；rv-02 全篇复核与结构对账 0 问题；rv-03 十处括注全部 waived；rv-04 104 句逻辑承载全部 equivalent；rv-05 语法 0；rv-06 语域 5 节 R-1；rv-07/08 假阳性已裁定、P-7 已修；rv-09 体例终校全绿；凭据 `state/axis/`，汇总 `results/t242-review.md`）——验收：各轴凭据落 `state/axis/`、`--gate` 0 或逐条豁免
- [x] T243 [S-1] sg 链：sg-01／sg-02／sg-03（sg-03 须用户 `--mandate`）——**已完成**（2026-11-28：sg-01 自审 Minor 3 处已修、语体结论；sg-02 逐句回核问题单 0；sg-03 经用户授权签字（mandate 已记）；`logic-dynamic` 置 `done`；证据 `results/t243-sg01.md`、`t243-sg02.md`、`t243-sg03.md`）——验收：sg-01／sg-02 无 Critical／Major；未授权则止于 `sg-02_checked`
- [ ] T159 [S-1] **[工作包]** `j/japanese-aesthetics`（图 33 幅）——**已拆为 T244–T251**（方案 `results/t159-decomposition.md`）；本行只作容器，**不得整体勾选**；T244–T251 全部完成、本件 `done`，容器保持未勾；验收：图注与 alt 齐备；T244–T251 全部完成且本件 `done`
- [x] T244 [S-1] ex-04＋tr-01＋tr-02 样章（导论＋§1–§2，约 7,540 字符；0 图／0 公式）——**已完成**（2026-11-28：en_integrity clean 1/1、en_source_audit hard 0／warn 0、fetch_audit 72 资产缺件 0；33 图闭包、44 脚注定义；tr-01 术语摘录并新增 5 行（六艺／《源氏物语》／《平家物语》／《徒然草》／沙罗）、无勘误注入；样章 16 段账本、1,607 汉字、2 引块、1 脚注；check_style／quotes／math_zh／terms 0、academic 无硬错误、pairs hard 0（out_of_scope 1）；证据 `results/t244-review.md`；状态 `cleared → ex-04_checked`）——验收：源审计 hard 0；33 图与 alt 清单在案；术语先登记后用；样章块数与 en 对应
- [x] T245 [S-1] tr-02 批 1（§3–§4，15,955 字符，3 图）——**已完成**（2026-11-28：新增 27 块、账本 43 段、全件 5,089 汉字；3 图 alt 改“银阁寺缩略图 1/2/3”；新增 9 条术语登记；check_style／quotes／math_zh／terms 0、academic 无硬错误、pairs hard 0（out_of_scope 1，含 ginkakuji 子文档链接待 T248）；prose 19 条留 T249；证据 `results/t245-review.md`）——验收：图注与 alt 中文齐备；账本守恒
- [x] T246 [S-1] tr-02 批 2（§5–§7，19,477 字符，5 图）——**已完成**（2026-11-28：新增 38 块、账本 81 段、全件 9,362 汉字；5 图 alt 中文化；新增 5 条术语与 3 条脚注定义；check_style／quotes／math_zh／terms 0、academic 无硬错误、pairs hard 0（out_of_scope 1，dangling-link 3 待 T248）；prose 33 条留 T249；证据 `results/t246-review.md`）——验收：图注与 alt 中文齐备；账本守恒
- [x] T247 [S-1] tr-02 批 3（§8–§10，18,746 字符，25 图）——**已完成**（2026-11-28：新增 29 块、账本 110 段、全件 13,233 汉字；25 图 alt 中文化；新增 4 条术语与 3 条脚注定义；俳句两列表保留；check_style／quotes／math_zh／terms 0、academic 无硬错误、pairs hard 0（out_of_scope 1，dangling-link 6 待 T248）；prose 48 条留 T249；证据 `results/t247-review.md`）——验收：25 图注与 alt 中文齐备；账本守恒
- [x] T248 [S-1] tr-02 批 4（尾节＋Acknowledgments＋44 脚注＋6 补充子文档）——**已完成**（2026-11-28：尾节与致谢入库、44 脚注与 en 逐字一致、6 件子文档新建并复制 33 幅大图至 assets（33→66）、dangling 0；账本 120 段、13,509 汉字；check_style／quotes／math_zh／terms 0、academic 无硬错误、pairs 0、check_all 23/23；致谢“Section 7”记 tr-03 勘误候选；证据 `results/t248-review.md`；状态 `ex-04_checked → tr-02_checked`）——验收：尾节合体例；44 脚注闭合；补充链接可解析
- [x] T249 [S-1] tr-03／tr-04 校次——**已完成**（2026-11-28：tr-03 逐节对照 en，Critical 0／Major 0／Minor 1（致谢 Section 7 实为 §10，已改正入勘误第二十一节并加译者注释①）；tr-04 `check_prose` 48→0（long-sentence 8、de-chain 36、weak-verb 3、passive-bei 1），全部改写无豁免；尾序修正（译者注释移至脚注定义之后末节）；check_style／quotes／math_zh／terms 0、academic 无硬错误、pairs hard 0、images 悬空 0；账本 120 段守恒；证据 `results/t249-tr03.md`、`results/t249-tr04.md`）——验收：账本守恒、残留外文 0（书目与日文引文除外）、检查器全绿
- [x] T250 [S-1] rv 链：rv-01→rv-02→rv-03–08→rv-09——**已完成**（2026-11-28：rv-01 术语 8 处 D2→D1 落地、体例三轴 0；rv-02 120 段对齐＋全局计数；rv-03 42 条引文（38 pass／4 waived）；rv-04 376 骨架（72 裁定 equivalent、24 候选无漂移）；rv-05 22 条 G-19 主题术语 waived；rv-06 10 节 R-1、1 条 R-d 误报；rv-07 0 量值对、10 条 M-4 误报；rv-08 标点 28→0（27 处 en dash→一字线、1 处双冒号）；rv-09 全量机检＋markdownlint 0；证据 `results/t250-review.md`、`state/axis/japanese-aesthetics.*`）——验收：各轴凭据落 `state/axis/`、`--gate` 0 或逐条豁免
- [x] T251 [S-1] sg 链：sg-01／sg-02／sg-03（sg-03 须用户 `--mandate`）——**已完成**（2026-11-28：sg-01 四维自审，Minor 3 已处理（措辞、§3 跨节引用 §7→§9 入勘误第二十一节＋译者注释①、引文页码恢复 en dash），Critical／Major 0，语体结论；sg-02 逐段抽核 24 块＋全量数字／引文／指代／跨节核对，问题单 0；sg-03 经用户本会话授权，终稿结构／版本钉／CI／交付清单全过，`japanese-aesthetics` 置 `done`；证据 `results/t251-sg01.md`、`t251-sg02.md`、`t251-sg03.md`）——验收：sg-01／sg-02 无 Critical／Major；sg-03 mandate 已记
- [ ] T160 [S-1] **[工作包]** `k/kokugaku-school`（表 48 行）——**已拆为 T252–T260**（方案 `results/t160-decomposition.md`）；本行只作容器，**不得整体勾选**；验收：表格结构完整；T252–T260 全部完成且本件 `done`
- [x] T252 [S-1] ex-04＋tr-01＋tr-02 样章（§1–§2，8,791 字符／1,341 词，0 表）——**已完成**（2026-11-28：en_integrity clean 1/1、en_source_audit hard 0／warn 2 均假阳性、fetch_audit 资产 0；51 脚注定义、6 表 47 行、0 图 0 公式；新发现 3 类文字缺陷入 en-errata 第二十二节；新增 11 条术语、Keichū 译名简体化；样章 22 段账本、2,413 汉字；check_style／quotes 0、terms 硬 0、academic 无硬错误、pairs 4 条样章预期缺口；证据 `results/t252-review.md`；状态 `cleared → ex-04_checked`）——验收：源审计 hard 0、warn 逐条定性；术语先登记后用；样章块数与 en 对应
- [x] T253 [S-1] tr-02 批 1（§3，12,362 字符，2 张和歌表）——**已完成**（2026-11-28：新增 2,801 汉字、账本 51 段、全件 5,214 汉字；两张和歌表按源逐行对译，表前加 `表 1`／`表 2`，右列罗马字照录；新增 13 条术语；check_style／quotes 0、terms 硬 0、academic 无硬错误、pairs 4 条样章预期缺口；证据 `results/t253-review.md`）——验收：两表结构完整、表号与单元格中文；账本守恒
- [x] T254 [S-1] tr-02 批 2（§4.1–§4.2，12,079 字符，0 表）——**已完成**（2026-11-28：新增约 2,550 汉字、账本 79 段、全件 7,764 汉字；6 引块；新增 16 条术语（含《灵能真柱》《新鬼神论》《古道大意》等）；check_style／quotes 0、terms 硬 0、academic 无硬错误；证据 `results/t254-review.md`）——验收：人名生卒照源；账本守恒
- [x] T255 [S-1] tr-02 批 3（§4.3–§4.5，11,179 字符，4 张和歌表）——**已完成**（2026-11-28：新增约 2,321 汉字、账本 106 段、全件 10,085 汉字；4 表和歌逐行对译；松平义建（1800—1862）②落地、荷田春满节题①锚点；`## 译者注释` ①②；新增 15 条术语＋4 条人名；check_style 0、terms 硬 0、academic 无硬错误、pairs 3 条收口预期缺口；证据 `results/t255-review.md`）——验收：4 表结构完整；勘误行承载在位；账本守恒
- [x] T256 [S-1] tr-02 批 4（§5–§6＋尾节＋51 脚注定义）——**已完成**（2026-11-28：译后编辑全量入库；全文 431 行／12,515 汉字、账本 181 段；51 定义键集与 en 相同、5 处 marker 闭合；尾序 参考文献＞原始文献＞二手文献＞学术工具＞其他网络资源＞相关词条＞脚注定义＞译者注释；新增 10 条术语；check_style／quotes 0、terms 硬 0、pairs 0、academic 无硬错误、check_all 23/23；证据 `results/t256-review.md`；状态 `ex-04_checked → tr-02_checked`）——验收：尾节合体例；51 定义与 en 逐字一致；账本守恒
- [x] T257 [S-1] tr-03／tr-04 校次——**已完成**（2026-11-28：tr-03 181 段对齐、25 段数字差异逐段判读、30 余人名与登记册核对，Critical／Major／Minor 0；tr-04 `check_prose` 36→7（29 条改写、7 条逐条豁免），语体结论现代汉语学术书面语；check_style／quotes 0、terms 硬 0、pairs 0、academic 无硬错误；证据 `results/t257-tr03.md`、`t257-tr04.md`、`t257-prose.json`；状态 `tr-02_checked → tr-04_checked`）——验收：账本守恒；残留外文 0（书目与日文引文除外）；检查器全绿
- [x] T258 [S-1] rv-01 三轴（术语＋体例＋勘误）——**已完成**（2026-11-28：术语硬 0／告警 0；Keichū 简体化 D2、Matsudaira 订正 D2、Sanjō 终态 D5、Ōkuni 跨历留痕 D5；体例 check_style／quotes 0、pairs --gate 0；勘误 4 行承载①②，errata-apply／note-anchor 0；证据 `results/t258-rv01.md`；状态 `tr-04_checked → rv-01_checked`）——验收：`check_terms` 硬 0；体例 hard 0；勘误 1 行承载可验
- [x] T259 [S-1] rv-02＋rv-03–08＋rv-09——**已完成**（2026-11-28：rv-02 181 段对齐、H3/H4/表/定义/引用 12/4/6/51/5 全对齐、H2 11 含译者注释；q1 17 条全 pass、q2 303 句 37 条 equivalent、q3 10→9 处置、q4 六节 R-1、q5 2 量值 pass＋37 范围、q6 1 条页码豁免；六轴 gate 全 0；rv-09 check_style／quotes 0、pairs 0、terms 硬 0、academic 无硬错误；证据 `results/t259-review.md`、`state/axis/kokugaku-school.*`；状态 `rv-01_checked → rv-09_checked`）——验收：各轴凭据落 `state/axis/`；`--gate` 0 或逐条豁免；`check_all` 全绿
- [ ] T260 [S-1] sg 链：sg-01／sg-02／sg-03（sg-03 须用户 `--mandate`）——验收：sg-01／sg-02 无 Critical／Major；未授权则止于 `sg-02_checked`
- [ ] T161 [S-1] `d/digital-art`（唯一代码块）——验收：代码块闭合；拆后方可执行

### 汇总与回填（全部条目完成后）

- [ ] T162 [S-1] 汇总 `results/e2e-findings.md`（G26+；G13–G14 为既有，标阻断／非阻断）——验收：与各件记录逐条对应；不得把工作包当完成
- [ ] T164 [S-1] **stage_of 联调**：逐站核对阶段派生（063 CT3／CT8 候选）——**前置：T102；排程 W6**；验收：差异有解释并回写 063，不改实现迁就模型
- [ ] T165 [S-1] 回填 spec：findings → G 清单 → 后续工作包顺序——验收：spec §2.7／§18.4 更新，状态与证据一致

## 阶段 S0 契约测试框架（迁移的必要证据之一，非充分）

- [ ] T001 [P] [S0] 建 `tools/golden/` 与 `run_golden.py` 骨架：按 `meta.json` 的 `compare_mode` 选择 byte／canonical-json／artifacts；仅声明 byte-contract 的输出逐字节——验收：假 tool 正反例各一，且 JSON 键序变化不应误红。
- [ ] T002 [P] [S0] 定 `expected.json`／`meta.json` 格式（compare_mode、exit_code、result schema、artifacts、commit、tool_version、platform、dynamic_fields）——验收：schema 文档写入 `tools/golden/README.md`。
- [ ] T003 [S0] 录制模式 `run_golden.py --record <tool>`（跑现行 Python 版并落 expected）——验收：`check_doc_size` 录制成功且回放通过。
- [ ] T004 [S0] 实现 canonical-json 比对（键序、换行、显式动态字段；浮点容差须由 schema 指定，不擅自容忍）——验收：同输入两次结果相等，注入时间戳不误红。

## 阶段 S2 清理检查点（2026-11-26 rev17 解冻；W0b 并行卫生轨，不阻塞 G0）

> 登记表部分已随 G23 裁定撤销；本节只保留 `clean --check`、缓存扫描、`.gitignore` 与 CI 步骤评估，不建第二本账。

- [x] T020 [S2] 扩展 `tools/clean.py` 契约：`--check` 默认 0；`--strict` 仅对保护件缺失／越界风险退 1；**不消费登记表（G23 不建）**——**已完成**（2026-11-27；`tools/tests/test_clean.py` 8/8；证据 `results/b-group-evidence.md`；验收：上述 8/8 通过；`clean.py --check` 默认 0、`--strict` 仅保护件缺失／越界退 1）。
- [x] T021 [S2] 扫描面扩至 `target/`、`.ruff_cache`、`.mypy_cache`、`.pytest_cache`、`.vitepress/cache|dist`——**已完成**（2026-11-27；占位目录实测 91→97 项识别；另纳入 `.screenshots/`；验收：占位目录样测试识别 91→97；`.screenshots/` 在扫描面内）。
- [x] T022 [S2] 评估 `check_all.py` GATES 增“缓存与临时物”——**已完成（接入）**（2026-11-27；key `clean`；`--list-gates` 现 23 项；硬命中 0；验收：`--list-gates` 含 `clean` 且总数 23；硬命中 0）。
- [x] T023 [P] [S2] `.gitignore` 审计补齐（`target/`、`__pycache__/`、`*.pyc`、`.vitepress/cache`、`.vitepress/dist`）——**已完成**（2026-11-27；另补 `/.screenshots/`；`git check-ignore` 全命中；验收：五类路径 `git check-ignore` 全命中）。
- [x] T024 [P] [S2] 评估 `checks.yml` 是否需独立 `clean --check` 步骤；若 GATES 已覆盖则不重复——**已完成**（2026-11-27；矩阵自动跟随，不新增步骤；rules/05 已同步；验收：无重复步骤；矩阵自动跟随；`rules/05` 已同步）。

## 阶段 S3 Python 现代化（受控变更，非零风险）

- [ ] T030 [P] [S3] 建 `pyproject.toml` 草案（requires-python `>=3.15`；区分 runtime／dev／optional；`cryptography`、`playwright` 列为可选）——验收：`uv sync` 在临时环境成功，且不改运行时行为。
- [ ] T031 [P] [S3] `ruff format` 按目录分批（先 lib 层），每批单独提交——验收：该目录 diff 仅格式；`check_all` 全绿；禁止全库一次格式化。
- [ ] T032 [S3] `ruff check --select E,F,W,I` 先出基线清单，再逐目录清零或逐条豁免——验收：每次收窄均有记录，不以总豁免刷绿。
- [ ] T033 [S3] `mypy` 从 `tools/{common,naming_lib,register_lib,axis_lib}.py` 起步，先宽松后 strict——验收：四模块零错误且无未说明 `type: ignore`；其余列逐步清单。
- [ ] T034 [P] [S3] `uv.lock` 影子 CI 验证后再切换；保留 `python` 直跑回退——验收：本地与 CI 解释器版本一致，失败可一键切回。

## 阶段 S4 Rust 骨架

> 本节是 spec §13.1 LPR-2 的落地起点：每个迁移项须先证其属“长期稳定调用”（LPR-1 四问全满足），再交并发设计说明（线程模型、上界、背压、失败语义、确定性）；规则本身不构成迁移授权（LPR-5）。

- [ ] T040 [S4] `sep-core/` Cargo 工程（`rust-toolchain.toml` 钉 1.100、`#![forbid(unsafe_code)]`、clap 子命令骨架、tokio multi-thread＋rayon 线程池骨架）——验收：`cargo build --release` 出单二进制；两类运行时均可启动；并发设计说明模板入 `sep-core/README.md`（线程模型、并行粒度、上界、背压、失败语义、确定性）。
- [ ] T041 [S4] 统一输出层（`--json` 结构化、0／1／2／3 退出语义、stderr 诊断）——验收：与 Python 版适配映射表一致（黄金测试可验）；不得把告警并入失败码。
- [ ] T042 [S4] 在 `.github/workflows/checks.yml` 或经批准的新工作流增 Rust 构建与 `cargo test`；Linux CI、Windows 本地分别验收——验收：两平台各产 artifact；工作流变更同步 rules/05。
- [ ] T043 [P] [S4] `cargo-deny` 配置（许可证白名单、禁 yanked）——验收：`cargo deny check` 通过。

## 阶段 S5 B1 迁移（试金石批）

- [ ] T050 [S5] 迁移 `check_doc_size` → `sep check doc-size`——验收：黄金测试通过。
- [ ] T051 [S5] 迁移 `check_junk` → `sep check junk`——验收：同上。
- [ ] T052 [S5] 迁移 `check_quotes` → `sep check quotes`——验收：同上；含 Unicode 弯引号／直角引号用例。
- [ ] T053 [S5] 迁移 `clean` → `sep clean`（与 S2 的 Python 版并存）——验收：同上。
- [ ] T054 [S5] check_all 编排切换：四项改调 `sep`（保留 Python 回退开关）——验收：全库门禁输出与切换前一致。

## 阶段 S6 B2 结构校验

- [ ] T060 [S6] 迁移 `check_stages` → `sep check stages`（保留 S1–S7；063 新增谓词以 `ST1–ST9` 命名，064 承载谓词以 `ST10–ST14` 命名）——验收：黄金测试＋反例试金石；不得把 `S1–S7` 与阶段号混写。
- [ ] T061 [S6] 迁移 `check_catalog_network`（G1–G5）——验收：黄金测试（用最新快照）。
- [ ] T062 [S6] 迁移 `check_pairs`——验收：黄金测试。
- [ ] T063 [S6] 迁移 `check_summary`——验收：黄金测试。
- [ ] T064 [S6] 迁移 `check_taskfile_invariant`——验收：黄金测试。
- [ ] T065 [S6] `sep check --all` 并行编排（I/O 型用 tokio，CPU 型再评 rayon）——验收：固定平台与输入，报告 P50／P95／峰值内存及与 Python 基线的比值；**不预设 30 s**。

## 阶段 S7 B3 并发抓取

- [ ] T070 [S7] 迁移 `fetch_all`（tokio multi-thread，`--config A|B`，unchanged 不写盘不动钉）——验收：黄金测试＋1873 件 dry-run 计数一致。
- [ ] T071 [S7] 逐级压测并发（从现行 16 路起，按站点响应与退避调整；不以 128 为预设目标）——验收：请求速率受控、429／封禁风险有记录、逐请求留痕完整、可一键降并发。
- [ ] T072 [S7] 迁移 `fetch`／`fetch_entry`／`fetch_catalog`／`fetch_audit`——验收：各自黄金测试。
- [ ] T073 [S7] 迁移 `catalog_drift`——验收：黄金测试（四方差集）。
- [ ] T074 [S7] `sep fetch --only <slug>` 定点重抓——验收：单件重抓后 en/ 与钉一致。

## 阶段 S8 正则审计与 B4

- [ ] T080 [S8] 正则语义审计脚本：对 A 级工具列不可直译模式（反向引用／lookaround／条件组）——验收：输出清单与逐条处置（改写／留 Python）。
- [ ] T081 [S8] 迁移 `check_yuanwen_fidelity`（I2 字节＋I3 词元流）——验收：黄金测试；全库 1873 件零差异。
- [ ] T082 [S8] 迁移 `check_style`——验收：黄金测试；告警集合与 Python 版完全一致（不是数量，是集合）。
- [ ] T083 [S8] 迁移 `check_academic`——验收：同上。

## 阶段 S9 B5（正则风险最高，最后）

- [ ] T090 [S9] 迁移 `cite_audit`／`grammar_audit`／`measure_audit`／`punct_audit`——验收：各黄金测试。
- [ ] T091 [S9] 迁移 `check_terms`／`check_math_zh`——验收：同上。
- [ ] T092 [S9] 迁移 `en_source_audit`／`en_integrity`——验收：同上。
- [ ] T093 [S9] 六轴 q 链编排（`sep audit --axis`）——验收：q1–q6 串行与并行的**告警集合与退出语义**一致；非确定性排序须在 schema 中规范化。

## 阶段 S10 063 阶段轨实施（独立支线；**2026-11-26 批准：搁置至 E2E 完成**）

- [ ] T100 [S10] `rules/naming.json` 升 `sep-naming/v2`（stages 60／campaigns 6／marks 8／state_stage_map 19）——验收：schema 校验通过。
- [ ] T101 [S10] `check_stages` 新增 `ST1–ST9`（063 设计；ST9 判据归属）；064 另拟 `ST10–ST14`（AX15–AX19；AX20 复用既有 S2）——验收：命名不与既有 S1–S7 冲突；反例试金石至少三例必红。
- [ ] T102 [S10] 新增 `tools/stage_of.py`（派生视图，只读）——验收：1873 件均有输出；`--all` 分布与 tasks.state 聚合一致；对无状态节点输出 `derived_from`，不伪造状态。
- [ ] T103 [S10] 阶段轨 ADR（号实施时取，不预占）——验收：ADR 索引更新；`check_stages` S7 命名词表自洽。
- [ ] T104 [S10] specs/062 头注＋sop 映射行——验收：仅两行，不改正文；若 063 设计未批准则不加“已实施”措辞。

## 阶段 S12 测试补齐（G4，2026-11-26 立项）

- [ ] T166 [S12] **[工作包]** 测试补齐（按 `results/test-coverage.md` 的 **9 项缺口**：tr-03 check_pairs 全规则、rv-02 check_tables_images 与 check_math_zh 全规则、rv-03–08 六轴、ex-05 格式闭合）：执行前按项拆原子任务，每判据至少一正例一负例，六轴另加边界与 Unicode 样本；sg-01–03 为人工/聚合，写 N/A 理由——验收：`tools/tests/` 全绿；失败样本可稳定复现；不得以“检查器全绿”替代单测；工作包不得整体勾选。

## 阶段 S13 规范与治理补强（2026-11-26 立项）

- [ ] T167 [S13] G6＋G8 合并 ADR：文档形态判据（何时必须 spec＋plan＋tasks）与规则作用域（scope 由登记派生，不逐条手写）——验收：ADR 通过；`rules/09` 更新；至少一正例一反例可机检。
- [x] T168 [S13] 治理旧口径修复：`AGENTS.md` 5 秒→ADR-0069；`rules/README.md` P1–P28→P1–P33；`rules/naming.json` authority 12207:2017→2026——**已完成**（2026-11-27；证据 `results/a-group-evidence.md`）；验收：三处一致；无残留旧口径；不改历史 ADR。
- [x] T169 [S13] 标准回写：29148:2018、15289:2019、26514:2022 的官方结论与 12207:2026／25010:2023 备注写入 `rules/standards.json` 与 `rules/10`——**已完成**（2026-11-27；`verify_standards` 4/4 PASS；证据 `results/a-group-evidence.md`）；验收：`verify_standards` 通过；061 只作历史引用，不复制版本结论。

## 阶段 S14 学术翻译出版流程 v2（2026-11-26 批准并入 064；工作包，未拆）

> 依据 `results/target-workflow.md` 与 spec §21。22 节点保留、不重编号。T170–T175 均为工作包，执行前须拆原子任务；不得整体勾选。细粒度检查点见 `results/s14-checkpoints.md`（CP-S14-01–36；非 T 号；全部未启动）。

- [ ] T170 [S14] **[工作包]** 目标态与标准 crosswalk（`results/target-workflow.md`；spec §21）：标准状态、条款锚点、现状—目标差距、P0–P7 生命周期、角色/产物/闸门——执行前按标准族/阶段拆原子任务；验收：每项标准给“现行／在研／草案”状态与条款锚点；P0–P7 每阶段有角色、产物、闸门。
- [ ] T171 [S14] **[工作包]** 项目规范（ISO 11669）＋角色与独立性：`project_spec` 三类参数、缺项不得进 `tr-02`；RACI、competence 记录、译者≠双语审校≠复审≠终审硬门；取消 V01 同人偏离——执行前拆 schema/门禁/正反例；验收：`project_spec` 字段完整；独立性机检正例一反例各一；缺受众/用途/QA 等级/PE 级别/风险等级者拒进 `tr-02`。
- [ ] T172 [S14] **[工作包]** 概念术语库 TBX＋机器/LLM full PE 治理：TBX 概念条目（定义、学科域、来源、状态）；风险分级矩阵；模型/提示/参数登记；禁止 raw/light PE 出版；禁止模型生成引文——执行前拆术语/机器两线；验收：TBX 结构校验与迁移样本；风险矩阵正反例；模型登记字段完整。
- [ ] T173 [S14] **[工作包]** ISO 5060 质量评估＋学术出版编校：7 类错误、Critical/Major/Minor、抽样、评分卡、评估者校准；copyedit、page proofs、索引、图表、注释、参考文献、出版信息与译者署名——执行前拆评估/出版两线；验收：评分卡与抽样方案；校准记录；编校清单与样本。
- [ ] T174 [S14] **[工作包]** 记录/归档/度量＋AI 治理＋发布后：ISO 15489/GB/T 26162 归档包与留存；ISO/IEC 15939 指标基线；ISO/IEC 42001/23894 风险、影响、模型变更回归、保密；发布后勘误/反馈/上游更新/抽审——执行前拆三线；验收：归档包清单、指标基线表、AI 风险登记、发布后流程与样本。
- [ ] T175 [S14] **[工作包]** 规则与卡同步清单＋11 件试金石按 v2 新门复跑：rules/04、005、060、061、063、standards.json 的差异表逐项有落点；11 件 pilot 记录含项目规范、角色、TBX、full PE、ISO 5060、编校——执行前拆同步/试点两线；验收：差异表无悬空；pilot 记录逐件可复核；只出清单/记录，不改任务状态。

## 阶段 S15 探索批准项（2026-11-27 用户全部批准；工作包，未拆）

> 依据 `results/exploration-2026-11-27.md`（独立建议书，EP-01–09）。T176–T184 均为工作包，执行前须拆原子任务；不得整体勾选；全部“已批准、待执行”。

- [ ] T176 [S15] **[工作包]** EP-01 标准动态监测：建标准状态监测表（17100 Ed.2、18587:2026 DIS→发布、25058 AWI、999 Ed.3、8000-2 DIS）；触发条件与重评动作——执行前拆监测/触发两线；验收：每项标准有触发条件、责任人、证据位；18587 发布即登记重评。
- [ ] T177 [S15] **[工作包]** EP-02 术语库深化：TBX schema 对齐 ISO 26162-1/-2/-4＋GB/T 13725；抽取研究结论（ACM 2026/SAGE 2025）入候选流程；数据质量维度（ISO 8000/25012）——执行前拆 schema/迁移/校验三线；验收：样本往返；校验含数据质量；两表仍为生成视图。
- [ ] T178 [S15] **[工作包]** EP-03 知识组织观察：SKOS/25964/LMF/TMF 差异登记；概念关系表达评估；不迁移——执行前拆登记/评估两线；验收：差异表＋不迁移理由。
- [ ] T179 [S15] **[工作包]** EP-04 评分卡与校准：ISO 5060＋MQM 2.0（Linear Calibrated/Multi-Range 二选一记录理由）；抽样方案；双评校准——执行前拆评分/抽样/校准三线；验收：评分卡版本化；校准记录；SQC 候选评估。
- [ ] T180 [S15] **[工作包]** EP-05 QE 分流试点：CometKiwi/XCOMET 在试金石件产分流候选；与人工结论对照；LLM-judge 只产候选不得裁判——执行前拆分流/对照两线；验收：对照报告；误分流率与成本数据；判据所有权不变。
- [ ] T181 [S15] **[工作包]** EP-06 PE 工时度量：按“错误类型×方向”分层记录 PE 时间；编辑距离仅辅助——验收：分层基线表；无“编辑距离＝省力”表述。
- [ ] T182 [S15] **[工作包]** EP-07 AI 治理增强：ISO/IEC 42005:2025 影响评估三阶段表；5338 生命周期位（数据/模型/更新/退役）；25058 度量来源；42006 生态事实——执行前拆评估/生命周期/度量三线；验收：风险＋影响表；模型变更回归。
- [ ] T183 [S15] **[工作包]** EP-08 学术元数据与无障碍：词条页 `citation_*`（标题/作者/日期/源 URL）；GB/T 37668 四原则抽样（告警档）；ISO 999 索引低优先观察——执行前拆元数据/无障碍/索引三线；验收：元数据注入清单；无障碍抽样报告。
- [ ] T184 [S15] **[工作包]** EP-09 交换与供应链观察：XLIFF 2.2/ISO 21720/TMX/SRX 差异登记；SBOM（SPDX 3.0/CycloneDX 1.7）＋SLSA v1.0 写入 WP-R1 契约草案——验收：差异表；契约草案含 SBOM/SLSA 条款。

## 阶段 S16 临时布局迁移（2026-11-27 用户裁定；双写验证；含中文目录；SUMMARY 迁入 zh/；HTML 侧改名 html/；URL 新前缀；历史文本＋.vitepress＋壳仓一并改写）

> 依据 `results/layout-migration-plan.md`。目标：`en/` 与 `yuanwen/` 互换目录名，随后把 HTML 侧 `yuanwen/` 改名 `html/`；`a–z`、`1`、`fang-fa-lun`、`guan-yu`、`jian-yi-shu`、`qian-yan` 归入新建 `zh/`；`SUMMARY.md` 迁入 `zh/SUMMARY.md`；站点接受 `/zh/…`、`/en/…` 新前缀；同步工具链、日志、记忆、文档、任务书、specs、`.vitepress` 与壳仓 `taophilosophy.github.io`。T202–T208 为原子步骤，顺序不可跳；开始／结束各打 `batch/064-migrate-start|end`。

- [x] T202 [S16] 起点登记（免备份）：按用户 2026-11-27 裁定不设 `state/layout-backup`，以 Git 历史为唯一回退；记录起始 commit、`git status`、待迁目录清单与回退命令；壳仓 HEAD 与路径引用现状留档——验收：起始 commit 与回退命令可复核、工作区干净；证据 `results/t202-review.md`
- [x] T203 [S16] 双写 en／yuanwen＋站点常量：以旧 `yuanwen/` 生成新 `en/`（Markdown 镜像，含 `SUMMARY.md`、`SUMMARY-en.md`、`.gitbook.yaml`、`assets/`），以旧 `en/` 生成新 `yuanwen/`（原始 HTML，后改名 `html/`）；复制 `SUMMARY.md` 为 `zh/SUMMARY.md`；旧目录由 Git 跟踪；同步 `axis_lib`、`fetch_entry`、`yuanwen.py`、`en_*` 等工具常量；改 `.vitepress/config.mts` 的分片、SUMMARY 路径、配对、侧栏、srcExclude、locales、watch、导航，改 `prepare-gitstamps.mjs` 排除项与 `VersionPin.vue` 镜像判定——验收：只读门禁与抽样路径解析通过；证据 `results/t203-review.md`（前置 T202）
- [x] T204 [S16] 根目录归集 `zh/`＋壳仓：移动 27 个字母目录＋4 个中文目录＋`mu-lu-s.md`、`shu-yu-biao.md`、`ren-ming-biao.md`、`PROGRESS.md`、`RELEASE-NOTES.md` 到 `zh/`，删除 `开源翻译.md`；改写 `zh/SUMMARY.md`、`zh/mu-lu-s.md` 与根级说明页链接；更新 `rules/layout.json`、`check_*` 扫描根、`tasks/**/*.json` 的 `zh_doc`；同步 `.vitepress/README.md` 与壳仓 `README.md`，复核 `deploy.yml` 路径不需改——验收：`SUMMARY` 无失效链接、任务 `zh_doc` 全解析、壳仓说明与新布局一致；证据 `results/t204-review.md`（前置 T203）
- [x] T205 [S16] 历史文本改写：`rules/` 现行规则、`README`／`AGENTS`、`.vitepress/README.md`、壳仓 `README.md`、`specs/001` 契约、`specs/005` 交班卡与 `specs/064` 计划/任务书中的旧路径与 `en`／`yuanwen` 语义一并改写（HTML 侧现名 `html/`）；`rules/adr/` 按只追加约束保留原文；生成旧→新口径说明；不改写 Git 历史——验收：现行规则与任务书路径扫描无旧语义、ADR 仍可追溯；证据 `results/t205-review.md`（前置 T204）
- [x] T206 [S16] 全量验证：`check_all` 23/23、`unittest discover`、VitePress 分片构建（`ad`，四片合并交 CI）、壳仓 `bun run build`、`/zh/…` 与 `/en/…` 页面与死链检查、GitBook 两份配置可解析、11 件抽样三路径解析；修复残余——验收：门禁全绿、站点与壳仓构建通过、抽样通过；证据 `results/t206-review.md`（前置 T205）
- [x] T207 [S16] 收口：确认无误后提交并推送本仓与壳仓（壳仓只含壳侧改动）；更新 `zh/PROGRESS.md`、`schedule.md`、`axioms-tasks.md`；打 `batch/064-migrate-end`——验收：两仓工作区干净、远端同步；证据 `results/t207-review.md`（前置 T206）
- [x] T208 [S16] 原始 HTML 目录 `yuanwen/`→`html/`（收口后追加）：`git mv` 保留历史；同步 `tools/`、`baseline/entries.json` 4960 条 `files[].path`、5 个补丁与 INDEX、`.vitepress` 的 `srcExclude`／`watch`／`prepare-gitstamps`、`rules/layout.json`、规则/说明/specs/壳仓与单测夹具——验收：`check_all` 23/23、单测全绿、`SEP_SHARD=ad` 构建无死链、`/zh/` 与 `/en/` 产物在位；证据 `results/html-rename-2026-11-27.md`（前置 T207）

## 非本卡工作项与交接（不计入 W／114）

> 本表**不定义 T 号**，不计入 114 个编号，也不改变 S-1／S0–S15 的分区计数。G4／G6／G8／G23／G24／G25 已分别转为 T166–T169 或关闭，不再列此。

| 事项 | 现状 | 去向／触发 |
| ---- | ---- | ---- |
| G14 `en_source_audit` 抽样 | 单件 5 样本，不可外推 | 待 E2E 数据后定 |
| G16 061 标准矩阵机制 | 已加评估快照头注 | 机制改动另批 |

## 依赖与并行总览

```
WP-D0 文档重审（rev 10–17）
├─ WP-D1 关联卡纠偏
│  └─ WP-D2 已裁定 A：保留 22 节点（相关任务已删除）
├─ WP-E1 T130 人工定性 → 22 节点证据 → WP-E2 至 sg-02 → WP-E3 汇总回填（T164 排 W6）→ sg-03 另授权
├─ WP-S1 标准回写（已批准，T169 待执行）
├─ WP-C1 清理检查点（S2 解冻，W0b 并行；登记表不建）
├─ WP-T 学术翻译出版流程 v2（T170–T175，W7）
├─ WP-EP 探索批准项（T176–T184，E0–E5）
└─ WP-A1 Python 现代化 → WP-R1 单工具迁移证据（另批）

S0 测试框架 → S4 Rust 骨架 → S5 → S6 → S7／S8 → S9（均须独立立项）
S10 阶段轨（搁置至 E2E 后）
S12 测试补齐（T166）；S13 规范治理（T167–T169）；S14 流程 v2（T170–T175）；S15 探索批准项（T176–T184）
```

## 验收门（每个工作包收口）

1. 该包内原子任务全部完成且证据可复核；工作包不得整体勾选。
2. 对应契约／黄金／性质测试通过；若声称迁移等价，差异清单为空且抽核有记录。
3. 若新增长期物，先确认其不属于既有事实源；登记表未批准时不强求入表。
4. 提交只含相关文件；提交信息说明状态；推送后 `git log origin/main..main` 为空。
5. 任何“已证明／已相容／已完成”必须指向 verified 证据，不得以检查器全绿替代。

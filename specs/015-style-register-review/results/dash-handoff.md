# specs/015 破折号专项线交接卡

更新：2026-11-12（pc6）。本卡只记**破折号防滥用线**；语体线（verdicts.jsonl／置空重译）另有其记录，两线互不代管。

## 已完成

1. **枚举工具**：`bin/dash_scan.py`——全库 done 词条正文破折号用量枚举（排除引块／代码块／References 照录区），输出 `results/dash-scan.jsonl`，按密度排序；只作复核优先级，不作判定（spec.md 判定口径 7）。
2. **高密度段判定**：`per_1k ≥ 6/千字` 共 51 条全部语义复核，50 条结论入库 `results/dash-verdicts.jsonl`（james-ward 已在语体 verdicts 有 `dash=ok` 记录，不重复）；50 条均判 `abused`、`action=fix`。
3. **规则落地**：`rules/02`“破折号滥用的修复方式”——修复以含破折号的原句为单位、回英文源句（`yuanwen/`）**整句重新翻译**，禁止符号层机械替换（用户 2026-11-10 裁定）。
4. **样板修复**：`m/mathematics-inconsistent.md` 完成——22 段 58 处破折号句全部整句回源重译，残余 0；`check_prose` 回落 s2 豁免基线 8 条（无新增）；`check_style`／`check_academic --strict` 过。复核记录见 dash-verdicts 末条。
5. **机械替换回溯审计（2026-11-12，用户裁定「存在机械替换情况，禁止，必须重译」）**：新工具 `bin/mech_audit.py` 对全部已收口条目的修复 commit 逐行做 diff 分类（pure＝去标点逐字同＝纯符号替换；conn＝相似度≥0.95 且增删≤4 字＝连接词级补丁；susp＝0.85–0.95＝须人工判读），产出 `results/mech-spots.json`。首轮覆盖 17 条收口词条、438 处候选＋20 处 susp，**逐处回 `yuanwen/` 源句比对后实修 29 处、9 条词条判定零实修**（明细见 dash-verdicts 2026-11-12 各条）。查出的硬伤示例：kepler 诸行星「并不规则」↔源文 moved irregularly（语义翻转）、mathematics-inconsistent「特例微积分」连读（删对破折号）、al-farabi「哲学家—先知—统治者」被擅改为「兼……兼」（合规连接号误改，已回滚）。结论：符号层替换集中在 early 批次，且多数恰与源句结构对应（such as→括注、that is→即）；**「相似度高」不等于违规，必须回源定性**。

**并行会话收编造成的审计噪声（2026-11-12/13，luxemburg）**：他会话会把本会话在途改动并入自己的混合提交（luxemburg 被 85b804909、8d666e62e 两次收编，提交信息皆「！」，禁 amend 无法追改）。此后 `mech_audit` 会为每个被改段落生成整段配对候选（本库一行即一整段），pure/conn/susp 数量随之放大。判读口径：**只看 `cur_lineno` 是否仍定位**——pure 未定位＝旧文本已被后续整句重译覆盖（luxemburg 7 处即此情形，无需再改）；pure 仍定位＝纯符号替换未消，必改（luxemburg L95 已由 accceb9cf 整句重译）；conn/susp 未定位可略，定位者回源判「保持」并写进 verdicts evidence。

**工具加固（2026-11-13）**：`mech_audit.py` 增加「该行破折号数须有增减」过滤，剔除顿号化等全局标点提交造成的 pure 洪流（lakatos 曾虚高 68 条）；CLOSED 清单补入 leibniz-mind／lakatos／luxemburg。

**有账本词条的回溯方法（lakatos／leibniz-mind 实战）**：`tasks/<letter>/<slug>.ledger.yaml` 的 `segments[].source` 是唯一可靠中英对齐源——不必再猜段落对应。流程：① `mech_audit` 取 located 候选；② 按「文档序 md 正文行 ↔ 段」或相似度把候选落到 seg id；③ 以 `source` 重译该句；④ **同步改 md 与该段 `step2`**（否则 compose 会回灌旧文；注意 step1 是历史草稿，不得改，替换须限定在 step2 块内）；⑤ 幂等脚本断言唯一命中。lakatos 据此重译 84 段/117 句（cc6bbb436、2e45226df、40d242126），leibniz-mind 重译 52 句（1b14b50dc），两者复扫均归零（leibniz-mind 余 1 处工具区链接，豁免）。**教训：前一版 lakatos“224 处整句重译”里约八成实为符号替换，被 mech_audit 抓到，已全部重做；凡自称“整句重译”者，必须过 mech_audit 的 located 检查才算数。**

## 续做队列（按 dash-scan 密度降序）

lambert-auxerre→dai-zhen→…→kilvington→leibniz-mind→lakatos→luxemburg **等 20 条已收口且通过机械替换回溯审计**（见 dash-verdicts `action=none`）。leibniz-evil（2026-11-13，144→4）、lorenzo-valla（2026-11-14，116→0）、karl-reinhold（2026-11-14，98→3：引文 2+书名 1 豁免）已收口（见 dash-verdicts `action=none`）。**下一条：ockham（156，7.65）**，其后 duhem（98，7.60）→ 18thGerman-preKant（139，7.44）→ kochen-specker（118，7.26）→ abrabanel（78，7.26）→ …（余 32 条全清单见 dash-verdicts.jsonl `action=fix`，动手前以 dash_scan.py 最新复扫为准）。

**lorenzo-valla 收口要点（2026-11-14）**：① 账本 step2 落后于 md 时（他线已做术语收口而账本未跟上，本例 斯多亚→斯多葛、解释学→诠释学），先整块对齐落后段再上重译对，否则按 md 文本写的 old 串在账本必 MISS；② 首轮 85 句重译后 mech_audit 仍判 8 处 pure（段内只动了符号、词面未变）——按裁定必须二次整句重译（改词序措辞），pure 未定位后才算收口；③ 重译可能引入 de-chain（的-三连或单句≥6 个的），prose 须回归改前基线，超出即再调句法。

**并行安全（2026-11-12 血泪）**：本仓库多会话共用一个工作区，他会话的「门禁清障／rebase autostash」会**清空未提交改动**（lakatos 一次 224 处改动被整篇回滚、无 git 对象可恢复）。因此：① 一条词条**改完立即 `git add` + commit**，不要攒着；② 大批量替换写成幂等脚本（`script/_<slug>_dash_fix.py`，每对 old/new 断言唯一命中、已应用则跳过）一次跑完再核；③ 动手前 `stat` 目标文件 mtime，若数分钟内在变，先等其落定。

**leibniz-mind 收口样例（2026-11-12）**：94 处逐一按源句重写（`such as`→「如」、`that is`→「也就是说」、同位语→括注或「即」、并列→句分或「：」领起），复扫归零；改后须留意 `check_style` 的 bold-spacing（删破折号后加粗两侧失去「允许紧贴」的豁免，须补半角空格）。

**注意事项**：

* 语体线已置空重译的词条（classical／mixed，任务已出 done 队列）自动移出本线，重译时按新规则写即可——动手前以 `dash_scan.py` 最新复扫为准，判定记录以 dash-verdicts 为准。
* 修复一律整句回 `yuanwen/<letter>/<slug>.md` 英文源重译；成对插入语（真正插入、转折）可保留，引文内、书名内破折号豁免不动；单破折号作连接号（如「哲学家—先知—统治者」）合规，**不得改成「兼」「与」**（2026-11-12 al-farabi 回滚先例）。
* 重译后必跑：`check_prose <file>`（对照任务 s2 evidence 豁免基线，不许新增）、`check_style.py --docs <file>`、`check_academic.py --docs <file> --strict`，再 `dash_scan.py` 复扫该条归零确认。
* **收口前必跑** `python specs/015-style-register-review/bin/mech_audit.py <slug>`，对 pure/conn/susp 三类候选逐处回源定性；pure 必改，conn／susp 视源句结构判「保持」或「重译」，结论写进 verdicts 的 evidence。一次性本地草稿不得留在 `script/`。
* 完成后向 dash-verdicts.jsonl 追加 `{dash:"ok", action:"none"}` 记录（追加式流水，不改旧行）。

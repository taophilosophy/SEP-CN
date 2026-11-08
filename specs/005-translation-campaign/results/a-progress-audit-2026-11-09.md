# A 批词条翻译进度对账（2026-11-09）

**会话**：A3-main-20261109（接管 A 批翻译，主会话直译，不用子代理） | **工具**：`script/audit_a_progress.py`（四源只读核对＋状态分布）、`script/audit_a_full.py`（门禁复跑＋队列规模测算）、`script/gate_a2.py`（逐件门禁计数）——均为本地草稿区，不入库。

## 方法

对 `SUMMARY.md` 中 a 字母目录的正式词条（别名 `/— see/` 与占位母词条不计）逐条核对四源：`SUMMARY.md` 条目集合、`tasks/a/<slug>.json` 状态机（state/steps/version_pin/blockers）、`a/<slug>.md` 正文、`yuanwen/a/<slug>.md` 与 `baseline/entries.json`；并核对 `tasks/a/*.ledger.yaml` 组稿账本、`assets/` 图片发布侧、`check_academic/check_style/check_prose/check_math/check_images/check_summary` 现行门禁。

内容维度按状态机口径判定：`cleared` 须为 H1 桩、`drafted` 起须有实译正文；另比对 done 件的六道链条完整性、版本钉与基线哈希、补充材料/脚注覆盖。

## 实测数字（与 `campaign.py status a` 实时推导一致）

| 指标 | 数值 |
|---|---|
| 正式词条 | 160 |
| 已建基线 | 160 |
| 英文镜像 | 160 |
| 已建任务 | 160（全 retranslate，无 update 件、无 NO-TASK） |
| done | 54 |
| cleared（H1 桩，待全量重译） | 19 |
| pending（H1 桩，待 clear 后重译） | 87 |
| 未译合计 | 106 |

**状态分布**：done 54 / cleared 19 / pending 87 = 160。

**进度**：done 54/160（33.8%，全局口径 222/1879 = 11.8%）；done 正文合计 849,729 汉字，单件 5,657（albert-saxony）–63,397（aesthetics-18th-german），中位约 1.35 万字。未译 106 条源文合计 11,741,043 字符（约 180 万英文词）。

**账本（`specs/005-translation-campaign/ledger.json` 批次 a）**：phase=translate、计数以实时推导为准；对账前记「实况 done 54/160；批内 13 条 rework-open」——本次核对**与此前记账逐项相符**（13 件 rework-open 已实点，见下）。

## 一致性核对（零偏差项）

1. **状态机↔正文**：done 54 件全部有实译正文且末轮含 `done` 步；cleared 19 件全为 H1 桩（与 `HEAD` 内容逐字节一致，**清空未损任何译文**——它们本就是未译占位桩）；pending 87 件全为 H1 桩。无「done 缺正文」「cleared 却含正文」「正文成篇却状态 pending」。
2. **版本钉**：160 件 `version_pin.sha256` 与 `baseline/entries.json` 当前主文件哈希全等，**上游漂移 0**（无需建 update 任务）。
3. **补充材料/脚注**：`kind=notes` 的 15 件其脚注正文已由转换器内联为主文 `[^note-N]` 定义（如 abhidharma 17 条、abstract-objects 24 条），不另立中文页；`kind=supplement` 的 abduction 有 `a/abduction.peirce.md` 且已随 11-08 返工收口；三件 XML/PNG 资产（action-perception 3、actualism-possibilism-ethics 1、arabic-islamic-phil-math 3）按 `assets/<slug>/` 惯例落位（其中 3 件缺件已修，见下）。
4. **目录层**：`check_summary.py` H1 与 SUMMARY 不一致 0、别名片段 0、硬错误 0；`check_mulu_s.py` 未报 A 批问题。
5. **组稿账本**：`tasks/a/*.ledger.yaml` 0 份 —— A 批无段落账本体系（判例：11-06 B 批对账「无账本勿补造」）；**本轮起新译按 ADR-0021 建账本**（段落 id/source/step1/step2 双版），旧件不补造。

## 偏差发现与纠正

### 1. 已修：arabic-islamic-phil-math 三图发布侧缺件（内容缺陷）

done 正文 L56/L64/L72 引用 `../assets/arabic-islamic-phil-math/Fig-{1,2,3}.svg`，`assets/` 下无该目录（`check_images.py` 悬空 5 条中占 3；镜像侧 `yuanwen/assets/<slug>/` 反而齐备）。已从不可变基线 `en/arabic-islamic-phil-math/` 原样复制三件到 `assets/arabic-islamic-phil-math/`，**SHA-256 逐件与源一致**（`D46B60DD…` / `160B1B53…` / `90D5905A…`）。复跑 `check_images.py`：md 2097｜可解析 79｜**悬空 5→2**（余二件属 i 批 imprecise-probabilities，不在 A 范围）。正文未改（alt `described in the previous paragraph` 系上游 alt 照译，与镜像 L57/L65/L73 一致，非缺陷）。任务记录已追加 `reconcile-fix` 步留证，状态保持 done。

### 2. 已同步：PROGRESS.md 过期、批次认领转手

* `PROGRESS.md` 生成时间为 2026-11-08 14:38 UTC（全局 done 219），与现查 222 及 L/M/N/P/Q 等字母的在途推进不符——已 `tools/progress.py` 重生成纳入。
* 批次 a 认领由 `A2-main-20261108` 转 `A3-main-20261109`（用户 2026-11-09 裁定「现在由你负责翻译 A」），`campaign.py claim a --force` 已落账；phase 保持 translate（与事实相符，不作虚假推进）。
* 收编前任遗留的未提交凭证：`tasks/a/ancient-soul.json` 已于 2026-11-08T14:34:20Z 过基线门禁 clear（`state=cleared`，正文为 H1 桩、与 HEAD 一致），但未随 A2 提交落库——本次一并提交，故 cleared 计数 19 的口径含 ancient-soul（与前任账本「下一目标 ancient-soul」相符）。

### 3. 未消化（如实登记，非本对账改写项）

* **体例门禁漂移 64 条 / 10 件**（现行 `check_style.py`）：bold-spacing 34、italic-cjk 19、curly-quotes 11。成因是 ADR-0019（`**` 内侧禁空格，10-30 裁定）与 10-29「中文强调不用斜体」裁定**晚于**这些词条 done；分布：actualism-possibilism-ethics 22、akan-person 20、aesthetic-experience 6、al-khunaji 5、africana 3、al-kindi 2、albalag 2、abraham-daud 2、aesthetic-concept 1、aesthetics-18th-french 1。其中 actualism-possibilism-ethics、abraham-daud 两件已在 QA 返工队列（`qa-rework-dispatch-2026-11-05.md` 序 5/13），其余 8 件待返工线或批次语言批次消化。**done 计数不变**（计数口径是六道链条，非门禁现值）。
* **欧化告警 3,406 条 / 52 件**（`check_prose.py --strict`，告警级非硬错，ADR-0020）：long-sentence 1,326、de-chain 1,601、passive-bei 241、weak-verb 187、as-one 21、plural-men 21、exists-there 8、dang-shihou 1；告警清零仅 abduction、analogy-medieval 两件。大件如 africana 511、aesthetics-18th-german 414、aesthetic-experience 151、aesthetic-concept 147。按「不复查旧错」与返工线既定口径，归 13 件返工队列＋批次语言批次，不在本对账逐条改。
* **QA 返工队列 13 件**（state 保持 done，末步 `rework-open`）：abduction、abelard、abhidharma、abilities、abner-burgos、abortion、abrabanel、abstract-objects、academic-freedom、actualism-possibilism-ethics、advance-directives、abu-bakr-al-razi、abraham-daud（action、action-perception 两件已于 11-08 收口 `rework-close`）。
* **并行会话在途件**：`a/academic-freedom.md`、`a/addams-jane.md` 工作区有未提交语言润色（疑 011 译文审阅线），**本会话未动、未提交**，避免抢改。
* **check_math 误报一件（工具侧）**：alberic-paris 报 `unbalanced` 1，实为镜像行含 `"$2+2=4$"`，检查器货币豁免正则 `\$\d[\d,.]*` 先吞掉 `$2` 留下孤立 `$`；该报告为告警级（退出码只由 missing 驱动），缺失 0。中文侧同式 `$2+2=4$` 经 `.vitepress/math-plugin.mjs` 数字分支可正确配对渲染。处置：登记工具侧修正，不改进文。
* **术语门禁全局红（非 A 批所致）**：`check_all` 术语一致性项 12 条自洽硬错为 `yi-zhe-shuo-ming.md` / `ren-ming-biao.md` 的重复行（substantial form、Revelation、Moerbeke 等 10 组），经核**HEAD 已存在**，属 008/013 战役范围；A 批 54 件 `check_academic --strict` 全 0 硬错误、`check_terms --docs` 无本批词条级冲突。

## 作业队列（未译 106 条，按 `yuanwen` 字符数升序，先短后长）

**已 cleared 19 件**（基线门禁已过，可直接 draft）：african-ethics、aesthetic-judgment、al-din-al-razi、ancient-soul、al-farabi-soc-rel、afterlife、al-baghdadi、alain-locke、aesthetic-testimony、africana-contemporary、al-ghazali、aesthetics-19th-romantic、al-farabi-logic、agency、aesthetics-cogsci、adorno、affirmative-action、agent-modeling-philscience、al-farabi-metaphysics。

**pending 87 件**（须先 `task_ops.py clear`＋建账本再 draft），头 10（源文章符）：alexander 54,460 / aristotle-noncontradiction 56,892 / algebra-logic-tradition 59,705 / altruism-biological 63,712 / anscombe 68,029 / arabic-islamic-essence 69,141 / axiom-choice 69,713 / aristotle-mathematics 71,739 / arcesilaus 72,181 / analysis 72,715。

后续会话按此顺序推进：每件走 `create/clear → draft（段落账本 step1/step2 双版）→ s1→s2→s3→r1→r2→r3 → done`，收口处在本报告追加一行实况。

## 结论

A 批 phase=translate 与事实相符；160 条四源零缺项（基线/镜像/任务/正文/版本钉/目录层），done 54 计数真实（均为实译正文＋六道齐全），清空桩无损译内容。对账中实修 1 处内容缺陷（三图缺件）、同步 2 项记录（PROGRESS.md 重生成、认领转手），并登记 4 类未消化项（体例漂移 64 条、欧化告警 3,406 条、返工队列 13 件、并行在途 2 件）与 1 件工具误报。剩余 106 条未译由 A3-main-20261109 按上表队列推进。

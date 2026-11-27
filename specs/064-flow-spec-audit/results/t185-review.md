# T185 评审记录：rv-03 q1 引文锁定（habermas）

- 任务：T185（T138 六轴第一轴）；日期：2026-11-27；actor：trae-main
- 依据：`rules/04` §六轴（ADR-0079）、`specs/060-six-axis-quality-gates/checklists/q1-cite.md`
- 写域：`h/habermas.md`（未改正文）；清单：`state/axis/habermas.cite.json`（运行态）

## 1 机检面与工具缺口

`cite_audit` 原实现只抽弯引号（`axis_lib.quotes`），**不识别 `>` 引块**；而 q1 判据表明确把引块列为对象。本轮先补工具再锁定：

- `tools/cite_audit.py`：新增 `blockquote_spans`（跳过 pubinfo、照录说明、引用信息表）与 `build_items`（引块＋引块外行内引号，按行号排序连续编号；引块内层引号不重复计数）。
- `tools/tests/test_cite_audit.py`：4 项单测（引块抽取、pubinfo/说明跳过、多行引块、内层不重复、行序编号），4/4 通过。

## 2 清单总账

| 项 | 数 |
| ---- | ---- |
| 引文级候选 | 167 |
| 其中引块 | 28 |
| 其中行内弯引号 | 139 |
| 裁定 pass（锁定） | 39（28 引块＋11 行内成句/原文） |
| 裁定 waived（术语／短语级，C-4c 移交 rv-01） | 128 |
| verdict=pending | 0 |
| anchor 为空 | 0 |

`pass` 的原著语种与可得性：德语 `unavailable` 37、德语 `present` 1（`das Gute im Gerechten`）、英语 `na` 1（《创世记》引文，按 SEP 英文句处置）。

## 3 引块对应（28 块，中英逐块 1:1）

| 中文行 | 源文行 | 源文括注 | 锚点 |
| ---- | ---- | ---- | ---- |
| L13 | L14 | (1992a: interview 3, 79) | #BiogIntr |
| L27 | L28 | (1964 [1974: 53]) | #PublSphe |
| L63 | L64 | (2001a: chapter 5, 85) | #HabeMatuSociTheoTheoCommActi |
| L98 | L97 | (1986b [1998b chapter 3: 232]) | #HabePragTheoMean |
| L126 | L125 | (1981 [1984a: 285–6, 288]; 1981 [1998b chapter 2: 118]; Celikates & Jaeggi 2009 [2017: 263–4]) | #TheoSociActi |
| L130 | L129 | (1981 [1984a: 87–88]) | #TheoSociActi |
| L140 | L139 | (1984b [2001d: 85]) | #UnavThes |
| L144 | L143 | (1982: 237) | #UnavThes |
| L148 | L147 | (Fultner 2019; Habermas 1999a [2003a: 85–86; 17–18]) | #UnavThes |
| L172 | L171 | 无括注（承接上文） | #HabeSociOnto |
| L188 | L187 | (1981 [1987: 178]) | #Syst |
| L194 | L193 | (1981 [1987: 196]) | #Syst |
| L214 | L213 | (1981 [1987: 196]) | #Colo |
| L220 | L219 | (1981 [1987: 186]) | #Colo |
| L309 | L308 | (1996a essay 1: 60 [1998a: 42 translation amended]) | #PrinDiscEthiTheiJust |
| L319 | L318 | (1983 [1990: 67], Habermas quoting McCarthy 1978: 326) | #UKantCateImpe |
| L359 | L358 | (1992b [1996b: 287]) | #DiscTheoLawDemoBetwFactNorm |
| L371 | L370 | (1992b [1996b: 408 187]) | #TwoTracTheoDemo |
| L383 | L382 | (1992b [1996b: 122]) | #CoOrigThes |
| L391 | L390 | (1992b [1996b: 110]) | #PrinDemo |
| L431 | L430 | (1976b [1998b: 40]) | #RatiReco |
| L470 | L469 | (2009 chapter 7: 112) | #ConsPatrCosmInteLaw |
| L484 | L483 | (1992h: 241) | #ConsPatr |
| L516 | L515 | (2012 chapter 6 [2017: 143]) | #ReliPost |
| L530 | L529 | (2008c [2010: 17]) | #JeruAtheReliFaitPhilReas |
| L538 | L537 | (2012 chapter 4 [2017: 63]) | #PostDeliDemo |
| L542 | L541 | (2005b chapter 5 [2008a: 127]) | #PostDeliDemo |
| L558 | L557 | (2005b chapter 5 [2008a: 130–1]) | #PostDeliDemo |

对照结论：29 个 `>` 块中 1 个为照录说明（L566），已排除；其余 28 块与源文 28 个引块顺序一致、逐块对应，无缺块、无增块。抽核 L13、L126、L309、L516、L558 五块，中译与英文语义一致。

## 4 行内 pass 条目（11 条）

| 行 | 中文引文 | 原著／状态 | 英文来源 | 锚点 |
| ---- | ---- | ---- | ---- | ---- |
| L17 | 在法兰克福学派那里，批判理论——根本没有这样一种东西……没有一套连贯的学说 | de／unavailable | Critical Theory, at Frankfurt School—there was no such thing … no coherent doctrine | #BiogIntr |
| L84 | 当我们知道是什么使一个言语行为可被接受，我们就理解了这个言语行为 | de／unavailable | We understand a speech-act when we know what makes it acceptable | #HabePragTheoMean |
| L118 | 所有参与者都追求以言行事意图、且只追求以言行事意图的语言中介行动 | de／unavailable | linguistically mediated actions in which all participants pursue illocutionary aims and only illocutionary aims | #TheoSociActi |
| L186 | 在资本主义社会里，市场是对合作性语境加以无规范调节的最重要范例 | de／unavailable | In capitalist societies the market is the most important example of a norm-free regulation of cooperative contexts | #Syst |
| L202 | 工具性行动和策略性行动 **寄生于** 交往行为、反之则不然 | de／unavailable | instrumental and strategic action are “parasitic” on communicative action, but not vice versa | #RelaLifeSyst |
| L232 | 不是一种元理论，而是一种社会理论的开端，这种社会理论关心的是验证自身的批判标准 | de／unavailable | not a meta-theory but the beginning of a social theory concerned to validate its own critical standards | #NormGrou |
| L251 | 一种反思性的、以同意为取向的行动形式，它……置于后者的上层 | de／unavailable | reflective form of agreement-oriented action that …sit on top of the latter | #Disc |
| L327 | （对我或对我们来说）什么是好生活？ | de／unavailable | What is the good life (for me, or for us)? | #RetuHabeKantMoraDist |
| L329 | das Gute im Gerechten | de／present | the remnant of the good at the core of the right | #RetuHabeKantMoraDist |
| L560 | 上帝照着自己的形象造人 | en／na | God created man in his own image | #PostDeliDemo |
| L560 | 经 *ex utero* 受精的配子具有人权主体的地位 | de／unavailable | a gamete fertilized *ex utero* has the status of a subject of human rights | #PostDeliDemo |

## 5 豁免（128 条）

以下条目为术语或短语级片段（C-4c），q1 不裁决，统一 `verdict=waived` 并移交 rv-01 术语轴；其 hash 仍登记，防止后续漂移。编号：

```
c-habermas-002, 003, 004, 007, 008, 009, 010, 011, 012, 013
c-habermas-016, 017, 018, 019, 020, 022, 024, 025, 026, 027
c-habermas-033, 034, 035, 036, 038, 039, 040, 041, 042, 043
c-habermas-045, 047, 049, 050, 051, 052, 053, 055, 056, 059
c-habermas-060, 061, 062, 063, 064, 066, 067, 068, 069, 070
c-habermas-071, 073, 074, 075, 076, 077, 078, 079, 080, 081
c-habermas-082, 083, 084, 085, 087, 088, 090, 091, 092, 093
c-habermas-095, 096, 098, 099, 100, 101, 102, 103, 104, 105
c-habermas-106, 107, 109, 110, 111, 112, 113, 115, 116, 117
c-habermas-120, 121, 122, 123, 124, 125, 126, 127, 128, 129
c-habermas-131, 132, 133, 134, 135, 136, 137, 138, 140, 141
c-habermas-142, 144, 145, 146, 147, 148, 149, 150, 152, 153
c-habermas-154, 156, 159, 160, 162, 163, 164, 165
```

（编号省略共同前缀 `c-habermas-`。）

## 6 机检凭证

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| 清单初始化 | `python tools/cite_audit.py h/habermas.md --init --json` | 167 条（28 引块＋139 行内） |
| q1 门禁 | `python tools/cite_audit.py h/habermas.md --gate --json` | problems 0，退出码 0 |
| hash 守恒 | `python tools/cite_audit.py h/habermas.md --check-hash --json` | problems 0，退出码 0 |
| 新增单测 | `python -m unittest tools.tests.test_cite_audit -v` | 4/4 OK |
| 全量门禁 | `python tools/check_all.py` | 23/23 全绿 |

## 7 发现与限制（不静默）

- **F1 工具缺口已修**：原 `cite_audit` 不抽引块，q1 的“引块”对象会漏检；本轮补 `blockquote_spans`/`build_items` 并加单测。该修复对后续各件同样生效。
- **F2 承载形态待裁定**：28 个引块现为中文译文，英文原文记入清单；判据表 §6 B 的规范形是“引块＝英文引文，中文译文另起一段”。本轮按“锁定不改写”执行，未重构 28 块；是否回炉改载体形态需用户裁定（改动会牵动账本 step2 与下游 q2–q6）。
- **F3 德语原文缺口**：37 条 pass 条目原著为德语，按补裁“现代著作也逐条查原文”应核德语定本；仓库无德语底本，本会话未逐条联网查证，故保守标 `unavailable`、保留英文、不代造。`unavailable` 占比超过判据表 §8 的 50% 复核线；复核结论：非漏查，属底本缺位，建议在 sg-03 前设 B1 原文补证批。
- **F4 复核独立性**：reviewer 与 tr-02 draft actor 同为 `trae-main`，属既定单会话偏离（与 T136／T137 同）；已在 evidence 记录，不外推为独立性合规。

## 8 结论

q1 引文锁定完成到清单层：167 条候选全登记、39 条 pass、128 条按 C-4c 豁免移交 rv-01、0 pending、0 空锚点；`--gate` 与 `--check-hash` 均 0。F2／F3 作为待决发现挂入后续（sg-03 前必须处置），不阻塞 q1 状态推进。下一步 T186（rv-04 q2 逻辑）。

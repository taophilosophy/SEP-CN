# 交接卡：术语战役（specs/008）——新会话拿卡即开工

> 立法：ADR-0012（弃维基/优先知网/人名表拆分）。宪法 IV 流程先行：本卡是唯一开工入口。
> 硬约束：礼貌抓取 ≥5s；核验器只报告不修改；先登记后使用；凭证全部入库。
> **ZCode 技能**：本流程已封装为项目级技能 `termonline-batch`（`.zcode/skills/termonline-batch/SKILL.md`）——新会话说“术语跑批 / 查证下一批 / 审定库查证”即自动按 S.O.P. 执行，无需读本卡全文。

## 开工三件事

开工前先按 `rules/08-intent-first.md` 写方向声明：本批查证范围、目标/非目标与完成判据；范围含糊先问不猜。

1. `python tools/check_all.py`（应全绿）+ `git log --oneline -5` 核基点；
2. `python tools/term_audit.py`——看当前四态分布与未查证清单（报告在 `specs/008-terminology-campaign/results/`）；
3. 按下表认领下一批（认领记录写在本文件“执行认领”节，commit 留痕）。

## 状态基线（2026-10-31 多语种战役收官）

| 资产 | 状态 |
| ---- | ---- |
| 登记册两表 | yi-zhe-shuo-ming.md ~475 行 + ren-ming-biao.md ~73 行（多语种战役累计落册 ~210 行） |
| 候选池 | 75594 条：已裁定 ~1130（published ~330 / held 28 / rejected ~770）、new 余量=中低频长尾（随词条翻译核定，不再整批跑） |
| 提取器 | term_harvest 多语种版（topic/六种原文文字/foreign 重分类），动态增量：词条入库后 `--refresh` 或按字母批次补提 |
| 查证通道 | 审定库浏览器通道主力（S.O.P. 见 contracts/browser-channel.md）+ standard/youdao 辅助档；**激活机制=搜索页导航**（首页 reload 不激活） |
| 门禁 | check_terms 三表+落地核销两层语义（变体感知/涟漪信号）+ check_all 七项 |
| 技能 | termonline-batch（ZCode 项目级）：说「术语跑批/查证下一批」即按 S.O.P. 执行 |
| held | 28 条（来源未译，裁决点=词条翻译时；probabilism/taṣdīq 等已结清 4） |
| 系统批处理收官结论 | foreign ≥18 / phrase ≥40 / topic 高频 / person ≥15 / greek 原文 各段扫完；低频长尾整批跑收益递减（40-60 段实证泛词主导） |

## 常态流程（系统批处理收官后）

1. **词条翻译期**：新词条 intake/translate 时，`python tools/check_terms.py --docs <词条>` 核销正文术语与登记册一致性；池内该词条来源的 new 候选就地核定（A/C 分档）。
2. **登记变更**：主译变更 → Edit 两登记册（五列，禁维基）→ ci-hui-biao 看齐 → `--docs` 复核涟漪（主译待对齐信号）→ 正文看齐。
3. **增量提取**：新词条入库后 `python tools/term_harvest.py --refresh`（或 --letter）补提候选。
4. **多会话**：认领照旧写本卡「执行认领」节；批次工具与节奏全部固化在 termonline-batch 技能。

## 状态基线·历史存档（B0-第六轮，2026-10-28/29）

| 资产 | 状态 |
| ---- | ---- |
| term-pool.json 全库候选池 | 61997 条/26MB（2426 件逐篇遍历；phrase18990/italic25049/person8295/quoted8803/ism860） |
| 查证凭证 termonline-standard | 两登记册 234 键全量（含 ADR-0013 新增 43 键），凭证 235 份入库 |
| 查证凭证 youdao-aux（P0 换站） | **双通道投产**：有道词典 286 份凭证（ok 157/命中 684 条，按学科分组，供裁定辅助与多义区分；辅助参考档不作依据）；审计终态 一致126/不一致31/查无128 |
| P0 未通通道（插件位保留） | CNKI 翻译助手（TLS 反爬）/ zgbk（mtoken 签名）/ ncpssd（会话参数，机制已破译在执行记录）；~~审定库 token~~ **已通（浏览器通道，第六轮）** |
| 审定名词库浏览器通道（主力） | **已投产（2026-10-29 第六轮）**：S.O.P. 见 contracts/browser-channel.md；登记册全量 306 行查证完毕（334 查询项凭证入库）；配方=页面内 fetch + JWT 头 + credentials + 每批 reload 激活 + 批间冷却 4 分钟（限流窗口约 5 分钟） |
| 审阅报告 | audit-2026-10-29.md/json（最新）：**一致 154 / 不一致 30 / 查无 122 / 未查证 0，维基 0**（306 行全覆盖；30 行不一致均为保留裁定，理由见 execution-log 第六轮） |
| ADR-0013 阿拉伯伊斯兰加强批 | 已落地（7d39e70f）：提取器阿位专名路由+变音符折叠，人名种子 24 行、术语种子 19 行，词汇表 9 处归并互见；arabic 候选 822 条待逐条裁定 |
| 池首轮裁定 + P2 回填 | 已执行（bfa9c568，用户批准待办）：A 档 34 条直裁登记、B 16 held、C 16 rejected（manifest tasks/manifests/2026-10-28-pool-adjudication.json）；P2 依据回填 169 行实证两态；发布词汇表 +36 行。**池余量：A/B/C 三档已覆盖高频段，中频段（phrase freq 50-300、person 5-50、arabic <20）待后续批次裁定** |
| CNKI 翻译助手 / 审定名词库 | **通道未通**（TLS 反爬 / 需登录 token），provider 位保留 |

## 标准作业（每批次循环）

```bash
# 1) 查证（自动续跑；--force 重查）
python tools/cnki_query.py --from-registry            # 登记册增量行（standard/youdao 辅助档）
python tools/tl_browser_batch.py --emit --out <tmp>/tl-batch.json   # 审定库主力通道（见 contracts/browser-channel.md）
#    浏览器跑批 → --ingest 落凭证 → term_audit（节奏：每批 8 词+批间冷却 4 分钟）
python tools/cnki_query.py --pool                     # 候选池 new 条目（大，按字母分批见下）
python tools/cnki_query.py --terms <词...>            # 定点
# 2) 审阅
python tools/term_audit.py                            # 报告落 specs/008/results/
# 3) 裁定后登记（先登记后使用；依据列写来源+日期，禁维基）
#    → Edit yi-zhe-shuo-ming.md / ren-ming-biao.md（五列；变更不删旧行）
#    → qian-yan/ci-hui-biao.md 同步（修弱势方向登记册看齐）
# 4) 门禁
python tools/check_terms.py && python tools/check_all.py
```

候选池裁定批次建议：按 freq 降序扫 `tasks/term-pool.json`（jq/python 过滤 status=new），
A 档（通用哲学术语）直裁登记，B 档（存疑）走查证，C 档（泛词）标 rejected:理由。

## 待办优先级

1. **P0 通道攻坚**：① termonline 审定名词库 token（需手机注册账号，或用户授权提供 token——
   axios 拦截器头 `X-Access-Token`，接入后开 `termonline-all` provider）；② CNKI 翻译助手
   （真实浏览器通道：ZCode browser-use 或人工导出 cookie，破解内部 AJAX 端点后接 `cnki-dict`）。
   两者接通前，查证以 standardSearch 为主、依据列如实标注档位。
2. **P1 池裁定**：A 档术语分批登记（首推 -ism 860 条与 phrase 高频段，都是骨架术语）。
3. **P1 人名表扩充**：池 person 型 8295 条按 freq 降序裁定（注意体例：现代学者保留英文；
   古典/中世纪人名有通行译名者登记汉译；书名型误入 person 的移 phrase）。
4. **P2 存量依据回填**：登记册「待知网复核（008 战役）」行随查证逐条替换为实源。

## 纪律（多会话并行）

* 只 stage 自己改的文件；写完即 commit（共享暂存区事故先例）；提交后 `git log --oneline -2 -- <文件>` 核实归属。
* 认领批次时先读本节「执行认领」，避免撞车；认领格式：`- [日期/会话] 批次名（范围）`。
* 查证失败（error）不得臆造；unverified 行留给通道修复后 --force 重查。

## 执行认领

* [2026-10-28 / B0 会话] B0 全批：立法+拆分+工具链+全库首跑+登记册首轮查证+首轮审阅报告
* [2026-10-28 / Qoder 会话] P0 浏览器通道攻坚（CNKI dict + 审定库 token，用户弹窗登录）+ 不一致 31 条裁定 + ism/person/phrase 批量直裁（用户授权，manifest 留痕，held 兜底）
* [2026-10-29 / 第六轮会话] 审定库浏览器通道定型（contracts/browser-channel.md）+ 登记册全量 334 项扫批（34+3 批）+ 比对口径升级（亦作/书名号/注记变体）+ 首轮审定裁定 9 行主译变更（贝叶斯法则/大弃赌论证/最佳说明推理等，ci-hui-biao 同步）+ 终审计 154/30/122/0
* [2026-10-29 / 第七轮会话] P2 依据回填结算（164 行）+ 池 A 档首批 27 词（phrase 中频段 top，浏览器通道查证+直裁登记+池状态更新+manifest）
* [2026-11-02 / 轮替批次会话] A9 轮替批：person 池 rank 410+ 查遗续批 + 术语侧词条核心术语回填（relations ④ 队列首批），浏览器通道查证 + term_flow 落册

## 执行认领 2026-11-05（specs/011 联动批次）

* **会话**：011 复核主会话（claude/GLM 主代理）
* **范围**：011 主题词汇/传统审查新登记 75 条概念术语的审定库复核（specs/011/results/rowspec-*.json 的 T 表项；人名 34 条按 SOP 跳过）
* **清单**：$TEMP/tl-batch-011c.json（75 条，10 批）
* **状态**：浏览器跑批开始


## 执行认领

| 日期 | 会话 | 批次范围 | 状态 |
| ---- | ---- | ---- | ---- |
| 2026-11-06 | LQ-main-20261106 | 未查证术语队列 offset 0–22（23 词 4 批）+ 23–42（15 词 3 批，antitupia 查无） | ok=38 empty=1 落凭证（aa54205f+本轮）；审计裁定 72 条不一致全数判读（保留现译，3 行补亦作）；队列余术语 552+人名 777 待续，接力 offset 43 |
| 2026-11-08 | TERM-rev-20261108 | 11-08 未查证队列全量重建（术语 1665+人名 1632，A–Z 战役新落册行为主体）术语侧从头走批；人名侧反向校对（中文名查审定库验证通行形）；非英语原文列补填（回 en/ 原始 HTML+联网）；Conventuals 维基违例行修正 | 在途；02:37 提交 40f970d4（012 队列清理 A 批）后中断 |
| 2026-11-08 | TL-main-20261108（接管 TERM-rev） | 同范围续作：浏览器通道自未查证净队列 offset 0 走批（audit-2026-11-08 净队列 3297 行已构队 %TEMP%/tl-queue.json）；74 条不一致全数裁定；Conventuals 维基行联网复核；012 原文列队列穿插回填 | 前段完成（16 项凭证），余下由下行接管 |
| 2026-11-08 | TL-main-20261108b（接管 TL-main-20261108） | 同范围续作：净队列 3190 项自 offset 16 续跑（驱动队列 %TEMP%/tl-drive.json：术语正查 1578 + 人名中文名反查 1567 + 人名保留英文正查 45）；反向校对语义=中文名查审定库验通行形（命中 en 侧词元集合与英文名相等，审计四态自动成立）；不一致裁定 + ci-hui-biao 同步 + 012 原文列回填穿插 | 前段完成（24 项凭证，offset 0–23 至 agent_model）；余下由下行接管 |
| 2026-11-08 | TL-main-20261108c（接管 b） | 自 offset 24 续跑净队列（余 3166）；74 条不一致裁定 + Conventuals 维基行修正 + ci-hui-biao 同步 + 012 原文列回填穿插；每 4–5 批提交凭证 | 进行中（改判：offset 24 起由下行接管） |
| 2026-11-08 | TL-main-20261108d（接管 c） | 同范围续作：净队列 offset 24–63 共 5 批 40 词；84 条不一致全数判读留档（零主译变更）；重复行合并 7 组（Philip/Clement/Schiller/Schleiermacher/Maritain/ʿAyn al-Quḍāt/nominalism/Epistemic Closure）+ social contract 冲突归一，词汇表滞后归零；Conventuals 撤维基引证；012 原文列 +36 行（拉丁 18/日 11/朝鲜 4/阿语 3） | 本批完成；接力 offset 64。**门禁实况**：check_terms 硬错误 0、滞后 0；check_all 的 SUMMARY 结构审计红（220 条 orphan 全为元文档目录 .zcode/.specify/rules/fang-fa-lun 等，非术语资产，属仓库级卫生项） |

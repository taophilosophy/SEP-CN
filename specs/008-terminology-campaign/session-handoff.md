# 交接卡：术语战役（specs/008）——新会话拿卡即开工

> 立法：ADR-0012（弃维基/优先知网/人名表拆分）。宪法 IV 流程先行：本卡是唯一开工入口。
> 硬约束：礼貌抓取 ≥5s；核验器只报告不修改；先登记后使用；凭证全部入库。

## 开工三件事

1. `python tools/check_all.py`（应全绿）+ `git log --oneline -5` 核基点；
2. `python tools/term_audit.py`——看当前四态分布与未查证清单（报告在 `specs/008-terminology-campaign/results/`）；
3. 按下表认领下一批（认领记录写在本文件「执行认领」节，commit 留痕）。

## 状态基线（2026-10-28 B0 收工）

| 资产 | 状态 |
| ---- | ---- |
| ADR-0012 + rules/03 + ren-ming-biao.md 拆分 | 已入库（16b325ac），154 术语 + 19 人名五列 |
| check_terms 三表门禁 | 已挂 check_all，全绿 |
| term-pool.json 全库候选池 | 61997 条/26MB（2426 件逐篇遍历；phrase18990/italic25049/person8295/quoted8803/ism860） |
| 查证凭证 termonline-standard | 两登记册 234 键全量（含 ADR-0013 新增 43 键），凭证 235 份入库 |
| 查证凭证 youdao-aux（P0 换站） | **双通道投产**：有道词典 286 份凭证（ok 157/命中 684 条，按学科分组，供裁定辅助与多义区分；辅助参考档不作依据）；审计终态 一致126/不一致31/查无128 |
| P0 未通通道（插件位保留） | 审定名词库 token（X-Access-Token）/ CNKI 翻译助手（TLS 反爬）/ zgbk（mtoken 签名）/ ncpssd（会话参数，机制已破译在执行记录） |
| 审阅报告 | audit-2026-10-28.md/json：四态 + 维基排查（终态 一致2/不一致4/查无228/维基0） |
| ADR-0013 阿拉伯伊斯兰加强批 | 已落地（7d39e70f）：提取器阿位专名路由+变音符折叠，人名种子 24 行、术语种子 19 行，词汇表 9 处归并互见；arabic 候选 822 条待逐条裁定 |
| 池首轮裁定 + P2 回填 | 已执行（bfa9c568，用户批准待办）：A 档 34 条直裁登记、B 16 held、C 16 rejected（manifest tasks/manifests/2026-10-28-pool-adjudication.json）；P2 依据回填 169 行实证两态；发布词汇表 +36 行。**池余量：A/B/C 三档已覆盖高频段，中频段（phrase freq 50-300、person 5-50、arabic <20）待后续批次裁定** |
| CNKI 翻译助手 / 审定名词库 | **通道未通**（TLS 反爬 / 需登录 token），provider 位保留 |

## 标准作业（每批次循环）

```bash
# 1) 查证（自动续跑；--force 重查）
python tools/cnki_query.py --from-registry            # 登记册增量行
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

- [2026-10-28 / B0 会话] B0 全批：立法+拆分+工具链+全库首跑+登记册首轮查证+首轮审阅报告
- [2026-10-28 / Qoder 会话] P0 浏览器通道攻坚（CNKI dict + 审定库 token，用户弹窗登录）+ 不一致 31 条裁定 + ism/person/phrase 批量直裁（用户授权，manifest 留痕，held 兜底）

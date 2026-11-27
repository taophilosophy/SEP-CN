# T139 评审记录：rv-09 体例终校（habermas）

- 任务：T139（rv-09，六轴后终校）；日期：2026-11-27；actor：trae-main
- 依据：`rules/04` 状态机与 s2.4 三轴、ADR-0063/0065；`rules/05` 检查器地图
- 写域：`h/habermas.md`（本轮无改文）

## 1 定点检查

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| 体例硬门 | `python tools/check_style.py h/habermas.md` | 1 文件，0 issue |
| 配对／尾节／勘误承载 | `python tools/check_pairs.py h/habermas.md` | 1 文件，0 issue |
| 引号总检 | `python tools/check_quotes.py h/habermas.md` | 0 违例 |
| 学术规范（严格档） | `python tools/check_academic.py --docs h/habermas.md --strict` | 无硬错误（在途豁免 1） |
| 公式体例 | `python tools/check_math_zh.py h/habermas.md` | 0 问题 |
| 公式保真 | `python tools/check_math.py habermas` | 0 公式（本件无公式） |
| 术语定点 | `python tools/check_terms.py --docs h/habermas.md` | 硬错误 0；Müller-Doohm 引用组告警沿用 T136 豁免 |

## 2 结构与体例核对

| 项 | 实测 | 判定 |
| ---- | ---- | ---- |
| H1 | `# 于尔根·哈贝马斯 Jürgen Habermas (James Gordon Finlayson and Dafydd Huw Rees)` | 中英题＋作者括号，合规 |
| pubinfo | `> *首次发表于 2023 年 9 月 15 日。*` | 引块形，与 `baseline/entries.json` 一致 |
| 节集合 | 1–7 正文七节＋参考文献／学术工具／其他网络资源／相关词条／脚注 | 与 T137 记录一致（13 节，脚注为规范末节） |
| 尾序 | 参考文献 → 学术工具 → 其他网络资源 → 相关词条 → 脚注 | canonical，`脚注` 末位 |
| 勘误承载 | `baseline/en-errata` 第十三节两条照录；译文侧按 T136 结论 | 一致 |
| 编号 | 正文节 `N.` 点号式；脚注定义连续 | 合规 |

## 3 与六轴的关系

- rv-09 只判结构与交付格式，不重做 q1–q6。六轴（T185–T190）已于 2026-11-27 全部完成，状态 `rv-08_checked`。
- 本轮未改正文；q1 引文 hash、q2–q6 各门禁均不变（T190 收口时已复跑为 0）。
- s2.4 三轴（术语＋体例＋勘误）已在 T136（rv-01）完成；rv-09 为终校复核，不新增术语或勘误。

## 4 遗留项（转 T140／sg 链，不在 rv-09 处置）

| 编号 | 事项 | 去向 |
| ---- | ---- | ---- |
| F2 | 28 个引块为中文译文；q1 判据表 §6 B 规范形为英文引文＋中文另段 | sg-03 前需用户裁定 |
| F3 | 37 条 pass 引文原著为德语，现标 `unavailable`，未补原文 | 建议 sg-03 前设原文补证批 |
| I1 | `baseline/register-baseline.md` 缺失，R-g 未比对 | 用户裁定 3–5 段后补建 |
| K1 | P-19 渲染层未验（无已构建页面） | 站点构建／CI 渲染扫描 |
| G1／H1／J1 | q2 候选级、q3 第一层未逐句、q5 本件量值面为空 | 已在各轴评审记录登记 |

## 5 机检凭证汇总

`check_style` 0｜`check_pairs` 0｜`check_quotes` 0｜`check_academic --strict` 硬 0｜`check_math_zh` 0｜`check_math` 0｜`check_terms` 硬 0｜`check_all.py` 23/23 全绿。

## 6 结论

rv-09 体例终校通过：体例、配对、引号、学术规范、公式、术语六项定点检查均无硬错误；H1／pubinfo／尾序／编号／勘误承载与既有记录一致；本轮无改文。遗留项 F2／F3／I1／K1 与 G1／H1／J1 均已在案，转 sg 链前处置。下一步 T140（sg-01／sg-02 工作包，须拆两节点）。

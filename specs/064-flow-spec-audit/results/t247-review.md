# T247 证据：japanese-aesthetics tr-02 批 3（§8–§10）

- 日期：2026-11-28
- 任务：T247（T159 拆站第 4 项）；状态保持 `ex-04_checked`
- 范围：§8 意气（8 块）＋§9 切（8 块）＋§10 小津（10 块），源文 18,746 字符，25 图

## 一、术语与脚注

- 新增登记 4 条（2026-11-28）：《“意气”的结构》（The Structure of “Iki”）、《晚春》（Late Spring）、《东京物语》（Tokyo Story）、龙安寺（Ryōanji）。
- 其余意气、媚态、意地、断念、甘味、涩味、华丽、素雅、下品、上品、武士道、花道、切、切续、切字、俳句、枯山水、山水、临济、缘起、枯等均用既有登记形。
- 新增脚注定义 3 条：`berthier-2000`、`parkes-1997`、`parkes-2007`，与文内 marker 一一对应。
- 登记册 `The Structure of “Iki”` 原文列改作“いきの構造”（去日文直角引号，过 `check_quotes` 全库总检）。

## 二、译文与结构

- 新增 29 块，账本 81 → 110 段；全件 240 行／13,233 汉字。
- 图 25 幅全部入库并中文化 alt：龙安寺 0–9（10）、晚春 1–9（9）、东京物语 1–6（6）；路径 `../../assets/japanese-aesthetics/`。
- 芭蕉俳句保留两列引块表（原文／中译）；能剧步态、切字、小津切法等段落逐句照译。
- 6 个大图链接（ginkakuji、ginkakuji-kinkakuji、splashed-ink、ryoanji、late-spring、tokyo-story）目标待 T248 建子文档；`check_pairs` 记 dangling-link 6（样章 out_of_scope，预期）。

## 三、机检

`check_style` 0；`check_quotes` 0（全库总检）；`check_math_zh` 硬错误 0；`check_terms` 硬错误 0；`check_academic --strict` 无硬错误；`check_pairs` hard_in_scope 0／out_of_scope 1（dangling-link 6、节数／书目／尾节为样章预期）；`check_prose` 48 条（de-chain 36、long-sentence 8、passive-bei 1、weak-verb 3），留 T249 处理。

结论：T247 通过；33 图全部入库且 alt 中文，账本守恒。

# T246 证据：japanese-aesthetics tr-02 批 2（§5–§7）

- 日期：2026-11-28
- 任务：T246（T159 拆站第 3 项）；状态保持 `ex-04_checked`
- 范围：§5 寂（19 块）＋§6 幽玄（7 块）＋§7 幽玄与山水画（12 块），源文 19,477 字符，5 图

## 一、术语与脚注

- 新增登记 5 条（2026-11-28）：金阁寺（Kinkakuji）、《金阁寺》（The Temple of the Golden Pavilion）、《炎上》（Enjo）、《破墨山水》（Haboku Sansui）、龙脉（dragon’s veins）。
- 其余寂、侘、幽玄、能剧、型、艺道、唐绘、大和绘、道释画、临济、无为、弓道、柔道、书道、华道、茶道、破墨、泼墨等均用既有登记形。
- 新增脚注定义 3 条：`ghilardi-2015`、`jullien-2009`、`lippit-2012`，与文内 marker 一一对应。

## 二、译文与结构

- 新增 38 块，账本 43 → 81 段；全件 175 行／9,362 汉字。
- 图 5 幅：银阁寺 4/5、金阁寺 1/2、泼墨山水 1；alt 均中文，路径 `../../assets/japanese-aesthetics/`。
- 俳句引块保留三行形态；谷崎、世阿弥、Ghilardi、Jullien、Lippit 引文逐段照译。
- 三个大图链接（ginkakuji、ginkakuji-kinkakuji、splashed-ink）目标待 T248 建子文档；`check_pairs` 记 dangling-link 3（样章 out_of_scope，预期）。

## 三、机检

`check_style` 0；`check_quotes` 0；`check_math_zh` 硬错误 0；`check_terms` 硬错误 0；`check_academic --strict` 无硬错误；`check_pairs` hard_in_scope 0／out_of_scope 1（dangling-link 3、节数／书目／尾节为样章预期）；`check_prose` 33 条（de-chain 25、long-sentence 5、passive-bei 1、weak-verb 2），留 T249 处理。

结论：T246 通过；5 图 alt 已中文化，账本守恒。

# T245 证据：japanese-aesthetics tr-02 批 1（§3–§4）

- 日期：2026-11-28
- 任务：T245（T159 拆站第 2 项）；状态保持 `ex-04_checked`（tr-02 样章批次，不单独推进）
- 范围：§3 侘（15 块）＋§4 利休的茶道（13 块），源文 15,955 字符，3 图

## 一、术语

新增登记 9 条（2026-11-28）：《南方录》（Nampōroku）、《禅茶录》（Zencharoku）、斗茶（tōcha）、茶寄合（chayoriai）、银阁寺（Ginkakuji）、待庵（Tai-an）、茶入（tea caddy）、无偶像的（aniconic）、《阴翳礼赞》（In Praise of Shadows）。其余侘、寂、侘茶、书院、草庵、名物、躙口、刀挂、数寄屋、乐烧、挂轴、切腹等均用既有登记形。

## 二、译文与结构

- 新增 27 块，账本 16 → 43 段；全件 91 行／5,089 汉字。
- 图 3 幅：`ginkakuji1/2/3-thumb.jpg`，alt 均改为“银阁寺缩略图 1/2/3”，路径 `../../assets/japanese-aesthetics/`。
- 引块 5 处（《禅茶录》、谷崎《阴翳礼赞》、谷崎续引、兼好、《南方录》等）逐段照译；日文术语首现括注原文。
- 大图链接 `japanese-aesthetics.ginkakuji.md` 目标待 T248 建子文档；当前 `check_pairs` 记 dangling-link 1（样章 out_of_scope，预期）。

## 三、机检

`check_style` 0；`check_quotes` 0；`check_math_zh` 硬错误 0；`check_terms` 硬错误 0；`check_academic --strict` 无硬错误；`check_pairs` hard_in_scope 0／out_of_scope 1（dangling-link 1、节数／书目／尾节为样章预期）；`check_prose` 19 条（de-chain 14、long-sentence 5），留 T249 tr-04 处理。

结论：T245 通过；3 图 alt 已中文化，账本守恒。

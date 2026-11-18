# 047 执行账

## 2026-11-19 P1 批次：B2 判定器实施＋全库首跑（specs/053 承接，用户“批准继续”）

**产物**：`bin/verify_structure.py`（v1.6，判官只读）＋`results/structure-scan.json`（1,872 件全库）＋`tools/tests/test_en_patch_reverse.py`（A6 补丁可逆单测，3 项绿）。

**判据实现口径**（试金石 11 词条迭代 v1.0→v1.6 校准）：

- 五维：分节（原文正则扫描，非 parse_entry 块——div 内嵌 h2 不开块）/ 脚注（notes.html 三代锚形态：`name=`、`div#note-N`、`a#note-N`；配对序归一 `note-` 前缀；总账 deficit 硬判、surplus 登记面）/ 图（资产图 src 基名序，站点框架图互斥）＋公式块（\[..\] 与直书 $$ 三形计数）硬判；表（复杂表以原样 HTML 嵌入 md 单元格的 passthrough 契约形，口径未定）与列表（ol→块引/表格渲染语义未定）advisory。
- 归一化：标题两侧同用（剥 `<a name>` 锚＋实体解码＋数学定界符/花括号＋上下标转 ASCII）；md 脚注键正则放宽至非 ASCII（`[^hübsch-1883]` 实证——phil-bio 46“缺口”纯系测量假象，specs/039 教训⑨再证）。
- 负向证伪 selftest 3/3：丢节／丢脚注／丢数学块（数学案动态选取干净底稿）必报。

**全库首跑（v1.6）**：1,872 件＝过 1,218（v1.5 中间态）→**终态 1,706 过／166 候选**。

| 族 | 件数 | 定性 |
| ---- | ---- | ---- |
| figures（md 图片缺失） | 64 | **真丢文候选**（action-perception 3 图全丢实证——md 无图片行且无原样 HTML），转 P3 人审定性 |
| math（显示公式三形账） | 53 | SEP 直书 `$$` 第三形＋拆分形，口径待 W4 |
| sections | 33 | 数学进标题残差（augustine h4 'Spanish' delete、条目排序 replace） |
| footnotes pairing/ids | 21＋17 | notes 锚形态个案 |
| footnotes ledger deficit | 3 | **leibniz-ethics −2／logical-constants −27／possible-worlds −2**——真丢文候选（logical-constants 27 条文献账差为人审重点） |
| footnotes ledger surplus | ~493 | 拆条/子注合法族（T7 验证力衰减面，白名单登记后转 informational） |

**W 登记**（本批遗留，动工前现查）：

- W1 列表维：ol→块引/表格渲染语义未定性（v1 降 advisory）。
- W2 表维：复杂表 passthrough（md 单元格内嵌原样 `<table>`，altruism-empirical 13↔7 实证）口径未定性（v1 降 advisory）。
- W3 figures 族 64 件：逐件定性（转换器缺陷 vs 上游原生 vs 补丁面）。
- W4 显示公式三形（`\[..\]`／直书 `$$`／单 `$` align 裁定形）的账面口径。
- W5 surplus 白名单：拆条/子注登记后 ledger surplus 转 informational 的生效机制。
- W6 logical-constants 等 3 件 deficit 的人审定性（勘误表／转换器缺陷分流）。

**教训**：①判据正则必须含非 ASCII 键（变音符书目键）；②标题归一化必须两侧同源（单侧剥锚导致 910 假红——测量不对称实证）；③对账律有效：46“缺口”在正则修正后消失，避免了一次假发现进勘误表。

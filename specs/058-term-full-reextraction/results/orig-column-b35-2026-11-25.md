# 原文列欠账处置与白名单括注归一（批 35，2026-11-25）

## 一、发现：白名单被括号形态打败

`check_terms` 的“非英语术语缺原文”白名单 `ORIG_EDITORIAL_PAREN` 按**全角**括注登记（`anarchy（国际关系）`），登记册里同一行却写作**半角**（`anarchy(国际关系)`），字符串不相等，白名单等于没生效。此类共 7 条仍在告警：anarchy、chimera、competence、Great Learning、proper function、token、yielding。

处置：比对时先把全角括号归一成半角（`_paren_norm`），白名单再命中。另补一条 `On First Philosophy (al-Kindi)`（英文题名＋作者括注，与“第一哲学”通名分行）。**147 → 139**。

## 二、补录：法/德/拉丁语原题八行

原文列语义是“源语言书写形式”。这八条键本身就是源语言原题（拉丁字母书写，中间没有转写层），原文列却留“—”，属误留：

Le Monde、Le Système du Monde、Œuvres théologiques、Pensées diverses sur la comète、Réflexions critiques、Traité de l’Esprit de l’Homme、Was heißt: sich im Denken orientiren?、corvée。

处置：原文列填键形并在依据列留痕。**139 → 131**。

## 三、剩余 131 条的文字族分布

| 族 | 条数 | 可否离线补 |
| ---- | ---- | ---- |
| IAST 梵／巴利转写 | 106 | 不可，须原生天城体等，只能走 ADR-0030 ② 级工具书配对 |
| 其他（含英文基本词＋藏文 Wylie 括注、混合键） | 13 | 部分可，藏文原形仍须工具书 |
| 阿拉伯／波斯转写 | 5 | 不可 |
| 日文罗马字 | 4 | 不可（需假名／汉字原形） |
| 希腊转写 | 2 | 不可 |
| 韩文罗马字 | 1 | 不可 |

对梵、藏、阿、日、韩、希这些行，原文列不能靠推演填（`rules/03` 第 42 条明令禁止用 IAST／DIN 31635／Wylie 映射正推逆推）。可行的只有两条路：工具书逐条配对，或像人名表一样开“查无留 —”的豁免口——后者是规则变更，须走 ADR，本批不动。

## 四、门禁

`check_terms` 硬错误 0；“非英语术语缺原文”147 → 131；`check_all` 21 项全绿。

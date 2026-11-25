# 收割批 25：拼写折叠查重（2026-11-25）

对纯 ASCII 键做「变音符折叠＋英美拼写归一」（judgement→judgment、behaviour→behavior、colour→color、-isation→-ization、defence→defense、practice 系、mediaeval→medieval、aesthetic→esthetic 等）后重扫，得 38 组同折叠键。

逐组研判结果：

* **真重复 1 组**：`humors`（vives，2026-11-25 入册）／`humours`（locke-on-medicine，2026-11-05）同译“体液”，已合并为 `humors / humours`。
* 其余 37 组均为**按域并列**：同一拼写在不同语境分义（`dharma` 佛教法／胜论功德／耆那运动媒介；`karma` 业／胜论运动；`pradhāna` 系；`species` 种／经院种相；`token` 殊例／令牌；`proper function` 专有功能／普兰担格恰当功能；`chimera` 客迈拉／嵌合体；`competence` 胜任度／行为能力 等），或组合行与单项行并存（`analogy of imitation / participation` 与 `participation`）。
* 这一类与 2026-11-21 的 FLAG 裁定同向：**按域分义不合并**，只保证各行译法括注写明分域理由。

结论：拼写层已基本收敛，除本组外无新合并对象。

门禁：数据行 −1（合并删除一行），`check_terms` 硬错误 0。

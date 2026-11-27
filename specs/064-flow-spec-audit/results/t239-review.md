# T239 tr-02 批 3：logic-dynamic（§4）

- 日期：2026-11-28
- 对象：`zh/l/logic-dynamic.md` 追加 §4
- 源范围：`en/l/logic-dynamic.md` L350–441，12,272 字符
- 账本：`tasks/l/logic-dynamic.ledger.yaml` 141→186 段
- 子代理：1 个（累计 5/5，额度用尽）

## 一、结构与公式

| 项 | 源 | 译 | 判定 |
| ---- | ---- | ---- | ---- |
| 块数 | 45 | 45 | 一致 |
| 行内公式 | 116 | 116 处数学内容 | 3 处按体例转写（见下），无丢失 |
| 列表 | 4 项（$W$／$R(\pi)$／$uR(\pi)$／$V(p)$） | 4 | 一致 |
| 标题 | `## 4.`／`### 4.1`–`4.4` | `## 4. 若干变体`／`### 4.1 无测试的 PDL`／`### 4.2 带逆的 PDL`／`### 4.3 带重复与循环的 PDL`／`### 4.4 带交的 PDL` | 一致 |
| display 公式 | 0 | 0 | — |

体例转写（非内容丢失）：
- `$\mu$`→`*μ*`、`$\Delta$`→`*Δ*`：ADR-0049 孤立希腊字母转文字。
- 列表公式内 `j \text{ and } i \text{ integers}`→`j \text{ 与 } i \text{ 为整数}`：C8 公式内英文连接语译中文。

## 二、术语与人名

- 变体名首次出现均给中文名＋缩写：带逆的 PDL（CPDL）、带 $\infty$ 谓词的 PDL（LPDL）、带强循环谓词的 PDL（SLPDL）、带交的 PDL（IPDL）、带交与逆的 PDL（ICPDL）；RPDL 沿用 §3.3“带重复的 PDL（RPDL）”。
- 复用：variants 变体、expressive power 表达力、filtration 滤化、Fischer–Ladner 闭包、strong loop 强循环、intersection 交、concurrency 并发、upper／lower bound 上界／下界、triply／double exponential time 三重／双指数时间、exponential space 指数空间、word problem 字问题、Game Logic 博弈逻辑、dynamic epistemic logic 动态认知逻辑、differential dynamic logic 微分动态逻辑、hybrid systems 混合系统、algorithmic logic 算法逻辑、temporal logics 时态逻辑、finite／small model property 有穷／小模型性质。
- 人名：Harel 作“戴维·哈雷尔”；Parikh 首现“罗希特·帕里克”、其后“帕里克”；其余按登记册保留英文原名（Berman、Paterson、Streett、Kozen、Vardi、Stockmeyer、Emerson、Jutla、Sherman、Danecki、Göller、Lohrey、Lutz、Lange、Massacci、Balbiani、Vakarelov、Peleg、Goldblatt、Van Eijck、Stokhof、Van Ditmarsch、Van Der Hoek、Kooi、Platzer、Mirkowska、Salwicki、Schneider、Pratt、Fischer、Ladner）。

## 三、机检

| 检查 | 结果 |
| ---- | ---- |
| `check_style` | 0 issue |
| `check_quotes` | 0 处违例 |
| `check_math_zh` | 0 个文件有问题、硬错误 0（修正 C10 2 处、C8 1 处） |
| `check_terms` | 硬错误 0（43 条告警为后续节术语与形态变体） |
| `check_academic --strict` | 无硬错误（在途豁免 1） |
| `check_pairs --gate` | hard 0；out_of_scope 1（中途阶段） |

## 四、结论

§4 入库：45 块、116 处公式（3 处体例转写）、4 条列表、五个变体专名齐备。可进入 T240（§5＋尾节＋55 脚注定义）。

# 020 镜像侧缺陷清单（移交 018 转换器战役）

> **处置回执（2026-11-14，018 会话 2）**：本清单四类已全部处置——嵌套表降级与整表丢失为真缺陷已修（li/dd 缩进真表 + 嵌套表消毒 HTML 透传）；findlay 断行、图片未引用 13 件为**误报结案**（上游注释行/PDF 专版/学术工具图标，详见 018 台账「020 移交缺陷分诊结论」节）；mereology 拆块为观察项（notes 表计入 + 配对伪影，行内容逐条在镜像核实）。复跑对账全部配平。

2026-11-13 全库扫描（604 词条，`script/t020_cmp.py` + `script/t020_img.py`，en html ↔ `yuanwen/` 镜像逐表逐图）。以下均为**镜像（转换器产出）**缺陷，非译文缺陷；转换器归 018 战役维护（其会话正在改 `tools/yuanwen.py`），本战役只登记不抢修。

## 1. 嵌套表降级（16 件，128 处）

转换器把 en 的嵌套 `<table>` 降级为字面文本 `（嵌套表：\| … \|）`——中文注释混入英文镜像、转义管道以原文显示、表格结构丢失。译文侧无此形态（0 件），说明译文已人工修正或该词条未译。

| 词条 | 降级处数 | 译文状态 |
| ---- | ---- | ---- |
| altruism-empirical | 6 | pending |
| consciousness-representational | 2 | pending |
| future-contingents | 1 | pending |
| information-entropy | 15 | pending |
| logic-connexive | 11 | — |
| lukasiewicz | 5 | — |
| mally-deontic | 2 | — |
| medieval-syllogism | 7 | — |
| nonwellfounded-set-theory | 6 | — |
| pm-notation | 1 | — |
| presupposition | 6 | — |
| proof-theory-development | 11 | — |
| pythagoras | 1 | — |
| reasoning-automated | 35 | pending |
| typelogical-grammar | 14 | — |
| zeno-elea | 2 | done（译文手修正确） |

## 2. 整表丢失（8 件）

en 表数 > 镜像表数，且非嵌套降级致因：

| 词条 | en 表 | 镜像表 | 备注 |
| ---- | ---- | ---- | ---- |
| logic-dialogical | 48 | 29 | 对话博弈表大量丢失 |
| ibn-sina-logic | 16 | 10 | |
| situations-semantics | 10 | 4 | |
| lambda-calculus | 6 | 5 | |
| logic-conditionals | 10 | 9 | |
| logic-deontic | 9 | 8 | |
| pascal-wager | 6 | 5 | |
| sign-language-semantics | 2 | 0 | 译文 cleared（空） |

## 3. 表内断行（1 件）

* `findlay`：en 缩写表 16 行，镜像仅 10 行，缺 H、K、LU、PP、PW 等 6 行（引注键在镜像里不可查）。

## 4. 图片未引用（13 件）

en 正文 `<img>` 在镜像无对应引用（资产多数已在仓，属转换器丢 `<img>`）：

biology-developmental、biology-individual、bruno、computational-linguistics、computational-philosophy、ecological-genetics（en 引 `figure1.gif`，仓内存为 `.svg`，命名不一致）、frege-logic、generalized-quantifiers、large-cardinals-determinacy、legal-probabilism、location-mereology、sign-language-semantics、word-meaning。

## 5. 单表被拆为多块（1 件，观察项）

`mereology`：en 87 张表，镜像 95 个表块——单表在转换中被空行拆散。渲染可用，语义上每块成为独立表，随 018 全文逐段复核一并定夺。

## 复现方式

```sh
python tools/check_tables_images.py --yuanwen          # 结构项（当前 0 处）
python script/t020_cmp.py <slug>...                     # 三面行级对账
python script/t020_img.py <slug>...                     # 三面图片对账
```

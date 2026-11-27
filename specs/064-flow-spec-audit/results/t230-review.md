# T230 tr-02 样章：newton-principia（导论＋§1）

- 日期：2026-11-27
- 对象：`zh/n/newton-principia.md`（新建正文；H1 存根保留，补 pubinfo）
- 源样章：`en/n/newton-principia.md` 导论（L6）＋§1（L8–L30），13,010 字符
- 账本：`tasks/n/newton-principia.ledger.yaml`（13 段：1 导论＋1 标题＋8 段＋3 引块）
- 依据：`results/t157-decomposition.md` T230；`rules/04`、`rules/02`、`rules/03`

## 一、入库范围与结构

| 项 | 源（en） | 译（zh） | 判定 |
| ---- | ---- | ---- | ---- |
| 块数 | 13（导论 1／H2 1／正文段 8／引块 3） | 13 | 一致 |
| 脚注引用 | `note-1`、`note-2`、`note-3` | 同名 3 处 | 一致（定义待 T231 Notes） |
| 引块 | 3（第一版序言、第一卷第十一节末、总释） | 3 | 一致 |
| 公式 | 0 | 0 | 一致 |
| 图片 | 0（样章范围） | 0 | 一致 |
| 链接 | 0（样章范围） | 0 | 一致 |
| 标题 | `## 1. Overview: The Importance of the Work` | `## 1. 概述：这部著作的重要性` | 一致 |
| pubinfo | `First published Thu Dec 20, 2007`，无修订行 | `> *首次发表于 2007 年 12 月 20 日。*` | 一致 |

## 二、术语登记（先登记后用）

经 `term_flow.py` 落册 12 条（`zh/shu-yu-biao.md`，2026-11-27）：

| 原文 | 译法 |
| ---- | ---- |
| absolute motion | 绝对运动 |
| attraction | 吸引 |
| clockwork universe | 钟表宇宙 |
| contact mechanism | 接触机制 |
| forces of nature | 自然力 |
| impulse | 推动（与 impetus 冲力分列） |
| law of gravity | 引力定律 |
| laws of motion | 运动定律 |
| lunar apogee | 月球远地点 |
| mean motion | 平均运动 |
| orbital mechanics | 轨道力学 |
| physical geodesy | 物理大地测量学 |

- 复用既有登记：absolute space／time、centripetal force、inertia、universal gravitation、exact science、experimental philosophy、occult qualities、impetus、sublunar world、action at a distance、vortex、general relativity、special relativity 等。
- 人名复用：Newton、Einstein、Galileo、Huygens、Aristotle、Euclid、Descartes、Laplace、Kepler 均在 `zh/ren-ming-biao.md` 有行。

## 三、译后编辑（PE）记录

- 全部 13 段经主会话直译后逐段 PE；`step1`＝初译，`step2`＝定稿（本样章两者相同或仅标点/空格级差异）。
- 关键处理：
  1. 书名：首次 `《自然哲学的数学原理》`，其后 `《原理》`；《哲学原理》《几何原本》照通行译名。
  2. 世纪上标（20ᵗʰ／18ᵗʰ／19ᵗʰ）转“20 世纪”等中文体例。
  3. 引文出处 `[**P**, 382]` 等按中文标点体例作 `（**P**, 382）`，以过 `check_style` bold-spacing 门；`note-*` 标记原样保留。
  4. `impulse` 取“推动”并以括注保留原文，避免与 `impetus`（冲力）撞形。
  5. `*the* exemplar` 的冠词强调在中文以 `**典范**` 承载；`*every*` 作 `**每一处**`。
  6. 长句拆分：导论首段与 §1 第 3 段按汉语节奏断句，未增删命题内容。

## 四、机检

| 检查 | 结果 |
| ---- | ---- |
| `check_style --docs zh/n/newton-principia.md` | 0 issue |
| `check_quotes --docs` | 0 处违例 |
| `check_math_zh --docs` | 0 文件有问题、硬错误 0 |
| `check_terms --docs` | 硬 0（71 条“缺译法”为样章未覆盖的后续段，告警） |
| `check_academic --docs --strict` | 学术规范无硬错误（在途豁免 1） |
| `check_pairs zh/n/newton-principia.md --gate` | hard 0；out_of_scope_warn 1（样章阶段缺尾节/脚注定义，符合预期） |

## 五、结论与移交

1. 样章 13 块与源一一对应，3 条编号注引用就位，3 引块边界完整，无公式/图/表新增。
2. 术语 12 条先登记后用；人名全部复用既有行。
3. 可进入 T231（全量：§2–§10＋尾节＋96 脚注定义，5 批 checkpoint）。
4. 移交：T231 批次 A 起按本样章口径沿用术语与引文格式；Notes 批须译 59 条编号注、照录 35 条书目键，并保留 note-2／note-3 的拉丁原文。

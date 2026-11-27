# T143 评审记录：tr-02 样章 §1–§2（logic-preference）

- 任务：T143；日期：2026-11-27；actor：trae-main
- 条目：`l/logic-preference`；样章文件 `l/logic-preference.md`（159 行、3,107 汉字、17 KB）
- 范围：H1＋pubinfo＋导言＋§1 引言＋§2 句法进路（2.1、2.2）＋所用脚注定义
- 状态：任务仍 `ex-04_checked`；样章不推进 tr-02 状态，T144 全量后统一推进

## 1 公式覆盖（T143 核心验收）

| 项 | 源文 §1–§2 | 译文 | 判定 |
| ---- | ---- | ---- | ---- |
| display 公式块 | 14 | 14 | 全保留 |
| `$…$` 行内公式 | 82 | 82 | 全保留 |
| `\(…\)` 行内公式 | 29 | 29 | 全保留 |
| 合计 | 125 | 125 | 数学结构 125/125 |

- 定界符：`$$` 成对 14/14；`\(` 29／`\)` 29；无未闭合。
- 两处公式内英文连接语按 `check_math_zh` C8 译为中文：`\textrm{ and}`→`\textrm{ 与}`、`\textrm{such that }`→`\textrm{使得 }`；数学结构不变。
- 其余公式（含 `align`／`gather`、`\tag`、`\textrm` 标签）逐字保留。

## 2 检查器

| 检查 | 命令 | 结果 |
| ---- | ---- | ---- |
| 体例 | `check_style.py l/logic-preference.md` | 0 issue |
| 公式体例 | `check_math_zh.py l/logic-preference.md` | 0 硬错误 |
| 引号 | `check_quotes.py l/logic-preference.md` | 0 违例 |
| 学术规范 | `check_academic.py --docs ... --strict` | 无硬错误（在途豁免 1） |
| 术语 | `check_terms.py --docs ...` | 硬错误 0 |
| 配对 | `check_pairs.py l/logic-preference.md` | 2 条样章已知缺口（见 §3） |

## 3 样章已知缺口（转 T144）

- `count-vs-source`：译文 96 个公式 vs 全条目 358（`check_pairs` 口径）；样章只含 §1–§2，缺 §3–§8，属范围缺口，不是漏译。
- `tail-order`：缺参考文献／学术工具／其他网络资源／相关词条；样章未建尾节，T144 全量补齐。
- 未建全量账本 `tasks/l/logic-preference.ledger.yaml`；T144 按 §1–§8 建段（含 step1／step2）。
- 任务 JSON 尚无 `project_spec`／`pe` 字段；T144 进 tr-02 前补（`task_ops` 机检）。
- 新造标签“P-表达式／A-公式／B-公式”为文内定义；T144 术语轴决定是否登记。

## 4 术语

核心术语均取登记册既有行：偏好逻辑、内在偏好／外在偏好、其他条件不变、CP 网（条件偏好网络）、偏好提升、可能世界语义学、偏序、等价关系、肯定前件、传递性、放大、偏好改变。样章未新增登记项。

## 5 结论

样章 §1–§2 完成：3,107 汉字；125 个公式数学结构全保留，定界符配对；体例、公式体例、引号、学术规范、术语均无硬错误。样章范围缺口（尾节、全量账本、project_spec／pe、417 全量公式）已登记，交 T144。下一步 T144（tr-02 全量，分 4–6 批）。

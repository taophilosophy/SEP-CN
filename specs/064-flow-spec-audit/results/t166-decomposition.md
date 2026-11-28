# T166 拆解：测试补齐（G4，9 项缺口）

- 日期：2026-11-28
- 依据：`tasks.md` T166、`results/test-coverage.md` §2（9 项缺口）、`rules/11-source-side.md` §6
- 原则：T166 只作容器，**不得整体勾选**；拆为 10 个原子任务（T272–T281），每判据至少一正例一负例；六轴另加边界与 Unicode 样本

## 原子任务

| 任务 | 缺口 | 落点 | 验收 |
| ---- | ---- | ---- | ---- |
| **T272** | tr-03 `check_pairs` 全规则 | `tools/tests/test_check_pairs_rules.py`：pubinfo-form、bracket-pair、cite-authoryear、bib-duplicate、count-vs-source、dangling-link、ellipsis-form | 正反例各一；`unittest` 通过 |
| **T273** | rv-02 `check_tables_images` | `tools/tests/test_check_tables_images.py`：table-cols／table-no-sep／academic-table／table-fullwidth／table-compact／alt-lang／img-base／img-resolve | 每规则正反例；图片正例用临时文件解析 |
| **T274** | rv-02 `check_math_zh` 全规则 | `tools/tests/test_check_math_zh.py`：C1–C10 至少各一例（C10 告警级）、Unicode 零宽字符 | 规则码命中与干净样本不误报 |
| **T275** | rv-03 `cite_audit` | `test_axis_gap_cases.py`：干净样本（无引文）、行内＋引块边界、Unicode 引号 | 正反例与边界 |
| **T276** | rv-04 `logic_audit` | 同上：all／some／if 算子行、无算子 trivial、Unicode | 正反例 |
| **T277** | rv-05 `grammar_audit` | 同上：关联词错配正例、干净句、Unicode | 正反例 |
| **T278** | rv-06 `register_audit` | 同上：R-f 正例、R-1 干净段、Unicode | 正反例 |
| **T279** | rv-07 `measure_audit` | 同上：M-2 正例、引文键不误报、Unicode | 正反例 |
| **T280** | rv-08 `punct_audit` | 同上：P-8／P-11 正例、撇号与段间换行反例、Unicode | 正反例 |
| **T281** | ex-05 格式闭合八项 | 新增 `tools/check_format_closure.py`＋`test_format_closure.py`：标题跳级、表对齐、代码围栏、公式定界符、实体转义、行尾空白、连续空行、末换行 | 八项各有正反例；零差异写 pass |

## 执行顺序

```
T272 → T273 → T274 → T275 → T276 → T277 → T278 → T279 → T280 → T281
```

- 全部完成后统一复跑 `python -m unittest discover -s tools/tests` 与 `check_all`；T166 容器保持未勾选，完成由 T272–T281 派生。
- 不以“检查器全绿”替代单测；失败样本须可稳定复现。

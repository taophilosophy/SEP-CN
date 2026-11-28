# T166 证据：测试补齐（T272–T281）

- 日期：2026-11-28
- 任务：T166 工作包；原子任务 T272–T281 全部完成
- 结果：`python -m unittest discover -s tools/tests` **807 tests OK (skipped=2)**；`check_all` 23/23（提交前复跑）

## 一、新增测试

| 任务 | 文件 | 用例 | 覆盖 |
| ---- | ---- | ---- | ---- |
| T272 | `tools/tests/test_check_pairs_rules.py` | 16 | pubinfo-form／bracket-pair／ellipsis-form／dangling-link／cite-authoryear／bib-duplicate／count-vs-source／h1-form，各正反例 |
| T273 | `tools/tests/test_check_tables_images.py` | 15 | table-cols／table-no-sep／table-fullwidth／table-compact／academic-table／table-en-prose／alt-lang／img-base／img-resolve，各正反例 |
| T274 | `tools/tests/test_check_math_zh.py` | 12 | C1–C10 各至少一例＋围栏豁免＋干净样本 |
| T275–T280 | `tools/tests/test_axis_gap_cases.py` | 18 | 六轴：干净样本、正例、反例、Unicode／边界 |
| T281 | `tools/check_format_closure.py`＋`tools/tests/test_format_closure.py` | 17 | 标题跳级、表对齐、代码围栏、公式定界符、实体转义、行尾空白、连续空行、末换行，八项各正反例 |

## 二、工具缺陷（测试驱动修复）

| 工具 | 缺陷 | 修复 | 回归 |
| ---- | ---- | ---- | ---- |
| `check_math_zh` | C9 散文 `\(` 因 `continue` 先于判定而永不触发 | 把 C9 判定移到 `continue` 前 | `test_c9_prose_paren_math` |
| `check_math_zh` | C6／C7 不排除围栏代码，代码块内 `$` 误报 | C6／C7 增加 `in_ranges(i, ranges)` 豁免 | `test_fenced_code_exempt` |

## 三、验收对照

- 每判据至少一正例一负例：上述五文件逐类覆盖；六轴另加 Unicode（全角数字、零宽字符、不换行空格、Unicode 引号）。
- 失败样本可稳定复现：所有反例以临时文件构造，断言规则码；无网络／随机依赖。
- 不以“检查器全绿”替代单测：本证据以 unittest 计数与用例名为凭；`check_all` 仅作聚合复核。
- `sg-01`–`sg-03` 仍为人工／聚合，按 `test-coverage.md` 记 N/A，不补单测。

## 四、备注

- 新增 `check_format_closure.py` 为 ex-05 的可测实现，暂不入门禁清单；是否升为门禁由 T166 后续治理决定。
- T166 容器不整体勾选，完成由 T272–T281 派生。

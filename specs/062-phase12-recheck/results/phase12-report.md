# 阶段 1.2 报告：HTML 重抓·基线更新·补丁复核·转换进度

生成时间：2026-11-25T03:49:45Z

## 一、抓取与差集

| 项 | 值 |
| --- | --- |
| 抓取 | 执行 |
| 变化件 | 522 |
| 新增件 | 0 |
| 移除件 | 0 |

变化清单（前 50）：`abilities`、`abortion`、`abstract-objects`、`academic-freedom`、`action`、`actualism-possibilism-ethics`、`aesthetic-concept`、`aesthetic-experience`、`agent-modeling-philscience`、`al-khunaji`、`alberic-paris`、`algebra`、`algebra-logic-tradition`、`anaphora`、`animalism`、`apriori`、`arabic-islamic-phil-math`、`aristotle-logic`、`aristotle-psychology`、`arrows-theorem`、`art-ontology-history`、`artificial-intelligence`、`autrecourt`、`axiom-choice`、`ayer`、`ayn-rand`、`beauty`、`benjamin`、`berlin`、`bodin`、`bohr-correspondence`、`bolzano`、`bolzano-logic`、`boolalg-math`、`boole`、`bosanquet`、`bounded-rationality`、`boyle`、`branching-time`、`brentano`、`brouwer`、`buber`、`carnap`、`category-mistakes`、`category-theory`、`causal-explanation-science`、`causal-models`、`causation-backwards`、`causation-mani`、`causation-metaphysics`

## 二、补丁复核（必要性／有效性／一致性）

| 补丁 | 词条 | 出处 | 命中/expect | 判定 |
| --- | --- | --- | --- | --- |
| P-001 | incommensurability | upstream-typo | 1/1 | **有效** |
| P-002 | lakatos | upstream-typo | 1/1 | **有效** |
| P-003 | yorck | upstream-typo | 1/1 | **有效** |

一致性：INDEX／C2 准入／`git apply --check` 见 `check_en_patches` 汇总 {"schema": "sep-cn-en-patches-dir/1", "patches": 3, "checked": 3, "mismatch": 0, "admission_bad": 0, "index_bad": 0, "git_check_bad": 0, "public_candidates": 0}。

## 三、转换进度

| 指标 | 值 |
| --- | --- |
| I2 转换保真 | 1873 件，issue 0 |
| 钉账词条 | 1873 |
| yuanwen md | 2421 |
| B3.1 装配 | {'ok': 1663, 'fail': 210, 'total': 1873} |
| B3.2 页面 | {'counts': {'rule': 0, 'pool': 1851, 'gap': 22, 'stale': 0}, 'total': 1873} |
| 资产分类 | {'main': 1873, 'supplement': 467, 'notes': 683, 'script': 458, 'image': 1474} |

## 四、判据

* 有效＝命中数等于 expect；已修复＝命中 0 且 replace 已存在（可退役）；失配＝其余（转换层会硬失败）。
* 补丁必要性以“上游是否修复”为准；一致性由 INDEX／C2／git apply 三面承载。

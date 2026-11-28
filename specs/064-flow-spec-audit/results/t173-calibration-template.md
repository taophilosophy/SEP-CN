# T173 评估者资格与校准模板（CP-S14-23）

- 日期：2026-11-28
- 依据：ISO 5060:2024 §4；`rules/evaluator-registry.json`；`rules/qa-scorecard.json`
- 状态：**模板；阈值待 pilot 基线测量后设定（threshold_status=pending_pilot）**

## 1 资格表

| 角色 | 必填能力 | 独立性 | 校准 |
| ---- | ---- | ---- | ---- |
| evaluator | qualification／experience／domain／training | 不得是译者 | 双评 |
| arbiter | 同上 | 不得是 evaluator A 或 B | 第三人仲裁 |

个人资格记录沿用 `tasks/<letter>/<slug>.json` 的 `competences[actor]`（T171／ADR-0093），四项缺一不可。

## 2 双评记录字段

| 字段 | 说明 |
| ---- | ---- |
| slug | 被评词条 |
| scorecard_version | `rules/qa-scorecard.json` 的 version |
| evaluator_a／b | 两位评估者 actor，须不同且均非译者 |
| scores | 两人按同一评分卡逐项计分 |
| agreement | 一致率（percent agreement）或评分差 |
| arbiter | 不一致时的第三人；无争议填 `—` |
| conclusion | 采信分数与理由 |
| date | 评审计分日期 |

## 3 校准程序

1. 两位评估者独立评同一抽样，不互看结果。
2. 计算一致率；不一致项由第三人仲裁，仲裁结论写入 conclusion。
3. pilot 先测基线一致率，再设阈值；阈值未定前不得宣称“校准通过”。
4. 评估者不得评自己参与翻译或审校的件；终审评估者另受 sg-03 分离约束。

## 4 记录位置

实际记录入 `results/qa/<slug>-<date>.json`（与评分卡证据同址）；本文件只定模板，不伪造校准数据。

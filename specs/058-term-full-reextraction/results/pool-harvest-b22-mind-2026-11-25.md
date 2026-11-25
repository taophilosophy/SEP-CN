# 收割批 22：心灵哲学与认知科学族（2026-11-25）

抽查 78 个名，真缺 14 条（另 1 条因变音符误判，见 §3）。

## 登记 14 条

| 英文 | 主形 | 语料 | 说明 |
| ---- | ---- | ---- | ---- |
| pain | 疼痛 | —（“痛”字高频，含痛苦等复合） | 心灵哲学与伦理学 |
| mental imagery | 心理意象 | 33 | 与 imagery 意象（美学）分列 |
| unity of consciousness | 意识统一性 | 14 | |
| perceptual content | 知觉内容 | 12 | 与非概念内容对举 |
| affordance | 可供性 | 8 | 吉布森 |
| mental files | 心理档案 | 8 | recency 理论 |
| metacognition | 元认知 | 6 | |
| higher-order thought | 高阶思想 | 5 | HOT |
| predictive processing | 预测加工 | 4 | 预测编码框架 |
| zombie argument | 僵尸论证 | 3 | 查默斯 |
| type identity | 类型同一 | 3 | 与殊型同一对举 |
| token identity | 殊型同一 | 2 | 同上 |
| privileged access | 特权通道 | 1 | |
| first-person authority | 第一人称权威 | 1 | |

## 2. 不登

easy problem／multiple draft model／4E cognition／situated cognition／self-model／binding problem（语料 0）；imagery 意象（美学泛用 210 次，与心理意象分列）；free agency（2 次，暂由 agency 能动性行承载）。

## 3. 变音符教训（已修工具）

`naïve realism` 在册，键带 ï；判缺脚本把 ï 剥成空，得 `naveralism` ≠ `naiverealism`，于是误报缺口，dry-run 时才被「键已存在」拦下。处置：`bin/audit_zh_corpus2.py` 的 `strong()` 加 NFKD 去组合符折叠；该行键补无变音符别名 `naïve realism / naive realism`。此前批 6 的 `Sāṃkhya`、`Vedānta` 一类若用同一函数也会受此影响，故修正放在函数层而非个案层。

## 4. 门禁

* 清单 `tasks/manifests/2026-11-25-058-batch73-terms.json`（15 行，naive realism 跳过）
* 实写 14；池 published=8；数据行 8,918→8,932
* `registry_azsort` 守恒；`check_terms` 硬错误 0；告警 148／781 不变

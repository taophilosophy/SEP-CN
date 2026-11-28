# T175 pilot 记录模板（CP-S14-34）

- 日期：2026-11-28
- 用途：11 件 pilot 逐件记录；只记录，不据此扩量
- 原则：逐件可复核；失败样本可复现；不以“跑完”替代质量

## 1 记录字段

| 字段 | 必填 | 说明 |
| ---- | ---- | ---- |
| slug | 是 | 词条标识 |
| e2e_task | 是 | 对应 E2E 任务号 |
| project_spec_ref | 是 | 任务 JSON 路径；16 字段摘要 |
| model_id | 是 | `baseline/model-registry.json` 的 id |
| roles | 是 | translator／bilingual reviser／review／final／domain／proofreader actor |
| competences | 是 | 每个审校 actor 的四字段记录位置 |
| tbx_concepts | 是 | 本件使用的概念 ID 或“无新概念” |
| pe_level | 是 | full／n/a；full PE 证据位置 |
| qa_sample | 是 | `qa_sample.py` 输出路径 |
| scorecard_version | 是 | `rules/qa-scorecard.json` 的 version |
| score | 是 | 分数、Critical／Major／Minor 计数 |
| editing | 是 | 八项编校逐项状态 |
| archive_manifest | 是 | 归档 manifest 路径 |
| boundary | 是 | 内部／公开；pilot 一律内部 |
| failures | 否 | 失败样本：命令、输入哈希、期望／实际 |
| conclusion | 是 | 通过／不通过／待补 |

## 2 记录骨架

```json
{
  "slug": "<slug>",
  "e2e_task": "Txxx",
  "project_spec_ref": "tasks/<letter>/<slug>.json#project_spec",
  "model_id": "deepseek-v4.1-flash",
  "roles": {"translator": "", "bilingual_reviser": "", "review": "", "final": "", "domain": "", "proofreader": ""},
  "competences": "tasks/<letter>/<slug>.json#competences",
  "tbx_concepts": [],
  "pe_level": "full",
  "qa_sample": "results/qa/<slug>-sample.json",
  "scorecard_version": "2026-11-28",
  "score": {"value": null, "critical": null, "major": null, "minor": null},
  "editing": {"copyedit": "pending", "proofs": "pending", "index": "pending", "figures": "pending", "notes": "pending", "references": "pending", "pubinfo": "pending", "attribution": "pending"},
  "archive_manifest": "results/archive/<slug>.json",
  "boundary": "internal",
  "failures": [],
  "conclusion": "pending"
}
```

## 3 失败样本要求

失败样本须给：命令／脚本、输入文件与 SHA-256、环境（模型／版本）、期望结果、实际结果、最小复现步骤、影响范围。无失败样本不等于通过；`failures` 为空须在 conclusion 说明“未发现失败”的证据范围。

# T175 G5 检查单（CP-S14-35）

- 日期：2026-11-28
- 判据：T170–T175 完成、11 件 pilot 基线、规则卡差异表；三项齐全才可扩量
- 当前结论：**G5 未通过；不得扩量**

| 项 | 判据 | 当前状态 | 证据 |
| ---- | ---- | ---- | ---- |
| 1. T170–T175 | 六个工作包全部收口 | **是**（T170–T174 已完成；T175＝T313–T317 本批收口） | `tasks.md`、`t170-review.md` … `t175-review.md` |
| 2. 11 件 pilot 基线 | 11 件均过 P0–P6 并有记录与基线 | **部分**（P0／P1／P2／P4 完成；P3 sg-01 全量初审 11/11 由 glm-main 完成、留痕逐件可复核；sg-02 复审须第三 actor，P5／P6 未执行） | `results/pilot/README.md`、`results/pilot/sg01-*.md`、`t175-pilot-plan.md` |
| 3. 规则卡差异表 | 六源均有差异、落点、优先级，无悬空 | **是**（6 源 18 项；P1 5 项已同步） | `t175-rule-sync.md` |

## 未过原因与放行条件

1. 11 件 pilot 未全过 P0–P6：P0 规范、P1 源、P2 PE、P4 抽样计划已完成；P3 sg-01 已由独立 actor `glm-main`（GLM-5.3-Flash）按用户裁定"禁止抽审查，全量"完成全量初审（2026-11-28，11/11，逐件证据 `results/pilot/sg01-<slug>.md`，competences 已经 CLI 登记）；按 ADR-0093 sg-02 须异于 `trae-main` 与 `glm-main`，须用户指定第三 actor 后执行；P5 编校与 P6 发布预演未执行。
2. **P1 差异已同步（2026-11-28）**：rules/04 评分卡与 P5–P7 指针、rules/05 工具表、`check_v2.py` 入 `check_all`、specs/061 缺口状态均已有落点与证据；P1 待办为 0。
3. 基线未测：`rules/metrics-baseline.json` 仍 `pending_pilot`；须先测基线，再设阈值。

**放行规则**：第 1–3 项全部满足且证据可复核，G5 才可改“通过”；当前第 1 项仅部分、第 3 项未满足，未过期间不得以“E2E 已完成”或“check_all 全绿”替代，不得扩量。

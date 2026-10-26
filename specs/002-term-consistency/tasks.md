# Tasks: 术语一致性检查器

**Input**: [plan.md](./plan.md)

## 1. 实现

* [ ] T001 实现 `tools/check_terms.py`：两表解析（FR-001）、键规范化（D1）、冲突检测（FR-002/D2）、登记册自洽性校验（User Story 2）、报告输出与退出码（FR-003）
* [ ] T002 实现 `--docs <路径>...` 定点核销模式（User Story 3）：登记册“首现”驱动，仅报告不阻断

## 2. 测试

* [ ] T003 unittest：fixtures 覆盖——无冲突、互斥冲突、子集滞后、合法多译法并存、废弃链断链、重复行、缺列行、解析失败行、希腊文斜体原词

## 3. 接线与登记

* [ ] T004 接入 `.github/workflows/checks.yml`（冲突与违例为门禁）；登记 `tools/README.md` 与 `rules/05-ci-and-tools.md`
* [ ] T005 对全库两表跑一轮基线：当前冲突清单人工裁决入库（修正弱势一方），完成后 PROGRESS/演示日志留痕

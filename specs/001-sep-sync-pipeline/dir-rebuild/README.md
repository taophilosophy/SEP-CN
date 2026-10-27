# 目录重建（ADR-0005）英文侧执行记录 — 2026-10-27

用户裁决：中文译文按 a–z 平铺、`yuanwen/` 英文库逐字符镜像、别名/递归不列入、只建空目录与仅含 H1 的 .md、先同步规则再同步目录、英文侧先行。规则登记见 `rules/adr/0005-目录重建.md`、`rules/01-repository-structure.md`、spec Assumptions。**本轮只做英文侧（yuanwen/），SUMMARY.md / mu-lu-s.md / 中文侧未动**（SUMMARY 有并行会话在途改动）。

## 数据流

`SUMMARY.md`（唯一数据源）→ `tools/rebuild_dir.py packages`（四级取证推 slug：官方快照 > 单段路径 > yuanwen 库内 > baseline 标题）→ 工作包 `packages/group-0[1-4].json` → 4 个并行子代理补建骨架 → 结果 `results/group-0[1-4].json` → `python tools/rebuild_dir.py verify`。

## 结果

* SUMMARY 解析 2662 条：别名 620（不列入）、项目页 41（不列入）、正式条目 1791、复核 188、重复合并 22。
* 正式条目 1791 = 库内已有 1640 + 本轮新建骨架 **147**（子代理落盘 149，复核修正删除 2 个孤儿：`k/korean-buddhism.md`、`i/indian-philosophy.md`，SUMMARY 无对应正式条目，系导航枢纽误判）。镜像覆盖率 1784/1791 = **99.6%**。
* 新建文件全部通过单行 H1 校验（`# <english>` + LF，UTF-8 无 BOM）；slug 大小写逐字符保留（如 `physics-Rpcc`）。
* git：`yuanwen/` 8 个跟踪文件的 M 状态前后比对一致（并行会话在途改动），本轮零触碰、零覆盖、零 git 写操作；新骨架文件因 `/yuanwen` gitignore 不入库（ADR-0003）。

## 镜像缺口（missing.json，7 条）

* 2 条孤儿已删（korean-buddhism、indian-philosophy）。
* 5 条工作包派生 slug 被子代理以快照/作者证据否定，正典文件已存在：`and-morality`→`r/religion-morality.md`、`animals-moral-status-of`→`m/moral-animal.md`、`logic-normative-status-of`→`l/logic-normative.md`、`music-philosophy-of`→`m/music.md`、`the-experience-and-perception-of`（疑 time-experience-perception，无本地证据，未落盘）。**中文侧建目录时须改用正典 slug。**

## extras（508 条，报告不清理）

库内有文件但当前 SUMMARY 未收录：SEP 补充材料（`*.xxx.md` 点号族）、SUMMARY 缺载的正式条目（如 `a/abortion.md`——快照有而 SUMMARY 无）、历史遗留。留待上游同步管线（spec 001 US-2 目录 diff）裁决。

## 需人工裁决（188 条，明细见 results/*.json 与 all-items.json `action=review`）

* **derived-nav 144**：无作者且快照无此条的节点。已知快照不完整（缺 `wisdom`、`aesthetics`、`morality`、`knowledge`、`perception`、`religion` 等真实独立条目），其中必混有真条目，**不可据"快照无"判定不存在**；子代理已救回 4 条（wisdom、feminism-objectification、logic-provability、social-procedures）。
* **同名候选 needs_review 28 + conflict 16**：同名子词条（各集群的 ethics/aesthetics 等）与同 slug 冲突行，多数已由子代理按集群上下文裁定为 skip-existing。
* 非SEP条目混入 SUMMARY 约 10 条（`tools/tests/fixtures/`、`fang-fa-lun/`、`jian-yi-shu/`、项目首页等），建议另行从 SUMMARY 清理。

## 4 个 slug 待上游核对（已建骨架，疑与 SEP 实际 slug 不符）

`o/on-utopia.md`（疑 plato-on-utopia）、`a/and-the-pineal-gland.md`（疑 descartes-pineal-gland）、`a/action-at-a-distance-in.md`（疑 qm-action-at-a-distance 或同族）、`h/health-well-being-personal-relationships.md`（疑已撤并）。快照与 baseline 均无对照，抓取时 404 即可确认并改名。

## 复现

```
python tools/rebuild_dir.py packages   # 从当前 SUMMARY 重新生成包与清单
python tools/rebuild_dir.py verify     # 镜像缺口/extras/跟踪文件核对
```

## 时点注记（重要）

本轮包生成所依据的 SUMMARY 工作副本（2026-10-27，含 1700+ 字母目录链接与 pending/ 项目页，2662 条）在英文侧构建期间已被并行会话整体重写（当前工作副本又回到旧结构形态，2652 条）。英文侧镜像锚定的是**构建时快照**，完整输入留档于 `all-items.json` 与 `packages/*.json`。**中文侧动工前必须对"当时"的 SUMMARY 重新跑 `packages`**，并先与并行会话确认 SUMMARY 的目标形态；本 README 的 missing/extras 数字只对快照负责。

> 注：ADR-0005/0007/0008/0009 执行记录已统一为 [specs/001-sep-sync-pipeline/execution-log.md](../execution-log.md)（本目录仅存目录重建专项凭证：包/结果/清单）。

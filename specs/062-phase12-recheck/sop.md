# SOP：阶段 1.1（目录四方互转）与阶段 1.2（HTML 重抓·基线·补丁复核）

两类阶段的固定作业。命令可照抄复跑；退出码 0 为全绿。

## 阶段 1.1 — 目录抓取与四方互转

**对象**：上游 `contents.html`（钉存）、`baseline/catalog.json`、`yuanwen/SUMMARY-en.md`、`SUMMARY.md`、`mu-lu-s.md` 及支撑账（`catalog-skeleton.json`、`catalog-residual.json`、`mulu-map.json`）。

**一键**：

```bash
python specs/062-phase12-recheck/bin/phase11.py            # 联网抓目录 + 全链复核
python specs/062-phase12-recheck/bin/phase11.py --offline  # 不联网，用最新钉存重放
```

内部顺序固定：

1. `tools/fetch_catalog.py`：落 `en/_catalog/<ts>-contents.html`，重建 `baseline/catalog.json`，输出 added／removed／renamed／alias_changed。
2. `tools/summary_sync.py report`：裁决表（add／remove／mapped）。
3. `tools/catalog_drift.py --latest`：四方差集（10 项＋挂起集）。
4. `tools/rebuild_catalog.py --check`：目录域 B3.2 装配 sha 全等。
5. `tools/check_catalog_network.py --gate`：G1–G5 五向重放。
6. `tools/gen_en_summary.py --check`：英文 TOC 镜像最新。
7. `tools/check_mulu_s.py`：mu-lu-s 六项（空节硬拦）。
8. `tools/sync_official_snapshot.py --check`：官方快照三处一致。

**通过判据**：四差集为空（或逐条解释并建账）；G1–G5 全绿；装配 sha 全等；mulu 0 硬错。**漂移处置**：ADD／REMOVE／RENAME 走 `summary_sync` → 人工裁定 → `apply-*` → 重建池 → 复跑 G1–G5。

**证据**：`results/phase11-run.json`、`results/phase11-drift.{json,md}`。

## 阶段 1.2 — HTML 重抓、基线更新、补丁复核、进度报告

**一键**：

```bash
python specs/062-phase12-recheck/bin/phase12.py --fetch --config A
python specs/062-phase12-recheck/bin/phase12.py --no-fetch          # 只复核出报告
# 可选：--no-convert / --limit N / --only slug...
```

流程：

1. **抓取前快照**：`baseline/entries.json` 复制到 `results/entries-before.json`。
2. **全量重抓**：`tools/fetch_all.py --config A`（16 路）。上游未变件走 `unchanged`：不写盘、不动钉账（ADR-0045），仍执行转换；有未搬运分歧且上游已变时自动拒抓。
3. **差集**：按 `slug → {path: sha256}` 比较前后，输出 changed／added／removed。
4. **补丁复核**（三判定）：
   * 有效＝命中数等于 `expect`（补丁仍必要且可用）；
   * 已修复＝命中 0 且 replace 已存在（上游已修，补丁可退役，走 ADR-0085 升档流程第 3、4 步）；
   * 失配＝其余（上游漂移或补丁失效，转换层硬失败，须人工裁定）。
   一致性由 `check_en_patches --strict` 的 INDEX／C2 准入／`git apply --check` 三面承载。
5. **I2 转换保真**：`check_yuanwen_fidelity --gate`（md ≡ convert(H1)）。
6. **进度**：钉账词条、资产分类、yuanwen 文件数、B3.1／B3.2 基线计数（读现成 JSON，不重跑）。

**通过判据**：补丁 `mismatch=0`、`admission_bad=0`、`index_bad=0`；I2 issue 0。差集非空不自动判失败——逐条给出出口（建账、补丁、勘误、例外）。

**失败处理**：抓取失败逐件登记（禁静默跳过）；补丁失配先回 `en/` 核对上游仍是原文，再决定退役／改写／登记例外。

**证据**：`results/phase12-run.json`、`results/phase12-report.md`、`results/entries-before.json`。

## 与既有线的分工

* 目录域判据归 specs/054（G1–G5），正文域归 specs/053（B3.1／B3.2）；本 SOP 只做编排与报告，不新立判据。
* 上游漂移转译任务：本 SOP 只出清单与建议，建账走 specs/001 `compare.py`。
* 抓取节律：ADR-0069 已废除强制间隔；用户 2026-11-25 再次确认不限速。重试退避、逐请求留痕、禁静默跳过三条不变。

## 频次与收口

* 阶段 1.1：目录变动或每周一次；阶段 1.2：月一次或上游批量修订后。
* 收口：两报告入库、`check_all` 全绿（除他人在途红项并注明归因）、提交即推。

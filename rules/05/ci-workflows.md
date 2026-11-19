# CI 工作流清单与运行时基线

## CI 工作流清单（`.github/workflows/`）

| 工作流 | 行为 | 触发 |
| ---- | ---- | ---- |
| `checks.yml` | 仓库一致性门禁**矩阵**（ADR-0061）：`plan` 作业跑 `tools/check_all.py --list-gates`（`GATES` 是唯一事实源），展开成每门禁一作业——`check_summary.py`（结构审计＋H1 一致性硬门禁，ADR-0024）＋`check_layout.py`（`rules/layout.json` 单一源，L1–L4，ADR-0067）＋`check_mulu_s.py`＋`check_doc_size.py`（ADR-0004）＋`check_junk.py`（垃圾/产物入库＋根目录白名单，ADR-0023）＋`check_images.py --gate`（图片引用完整性，rules/01）＋`check_terms.py`＋`check_quotes.py`＋`check_academic.py`（rules/07）＋`check_math_zh.py --strict`＋`divergence.py verify`（原始物分歧账，ADR-0045）＋`check_yuanwen_fidelity.py --gate`（转换保真 I2/I3，ADR-0063）＋`check_catalog_network.py --gate`（目录四方重放网络，specs/054）＋管线单元测试；`fail-fast: false`，红灯作业名即门禁名，失败日志与图片报告入运行工件 | push / 手动 |
| `format.yml` | markdownlint／autocorrect／md-padding 三工具**矩阵**（ADR-0061）：手动触发各自 `--fix` 并各开一条 PR（合并前人工核 diff；禁机械替换译文，见 [batch-rewrite.md](batch-rewrite.md)）；PR 触发只读 markdownlint（告警级，权威配置根 `.markdownlint-cli2.jsonc`）。禁改区排除 `en/`、`yuanwen/`、两本登记册、`SUMMARY.md`、测试夹具、站点产物 | pull_request / 手动 |
| `links.yml` | lychee 链接检查；范围单点由 `.github/lychee.toml` 的 `exclude_path` 决定（原文 `en/`、镜像 `yuanwen/`、草稿/运行态/构建产物/夹具不查）。**报告口径（2026-11-16）**：检出死链开 issue，作业本身不硬拦（`fail: true` + `continue-on-error`，以保留真实退出码供 issue 步骤消费；`fail: false` 会加 `--no-fail` 使退出码恒 0、永不开 issue）。日志 `verbose` 保持 `warn`——`trace` 会把每条已检链接写进 job summary，实测 1.7 MB 超 GitHub 1 MB 上限 | 定时（每月 15 日 18:00 UTC）+ 手动 + repository_dispatch |
| `catalog-drift.yml` | **每日三次**（UTC 01/09/17 点＝北京 09:00/17:00/次日 01:00）抓上游 `contents.html`，与本地三账（`baseline/catalog.json`／`SUMMARY.md`／`mu-lu-s.md`）四方对比，并做 B3.2 装配核验（specs/054）；上游有 NEW/REVISED 条目时并入 `new.html`＋`archinfo.cgi` 变更检测。**只读只报告**：不写 baseline、不改 SUMMARY/mu-lu-s、不提交内容文件；有漂移或变更时开/更新 issue（`sep-upstream-sync`，抓取/解析失败另标 `sep-sync-broken`），报告入运行工件。网络抓取在 CI 的唯一例外（单次 contents.html ＋ new.html ＋ ≤40 条 archinfo，ADR-0069 无最小间隔） | 定时（每日三次）+ 手动 |
| `en-roundtrip.yml` | **每日三次**（UTC 01/09/17 点＝北京 09:00/17:00/次日 01:00）核验“本地 HTML（`en/`）↔ 英文 markdown（`yuanwen/`）”双向互转：①`divergence.py verify`（en 钉）②`check_yuanwen_fidelity.py --gate`（I2 正向重放，约 1 分钟）③`specs/053 bin/reassemble.py --all`（B3.1 逆向装配往返不动点，约 12–20 分钟）。**变动口径＝相对已提交基线 `specs/053-en-template-audit/results/assembly-scan-all.json` 的差集**（新增残差／转绿／词条增删／钉漂移／I2 红灯），不是“有失败”——B3.1 存已知残差约 632 件。**只读只报告**：不写 baseline、不改 en//yuanwen/、不提交内容文件；有变动开/更新 issue（`en-roundtrip-drift`，巡检自身失败另标 `en-roundtrip-broken`），报告与全量扫描入运行工件；对比器 `tools/roundtrip_drift.py` | 定时（每日三次）+ 手动 |
| `Auto-Assign.yml` | issue/PR 自动分配 | issues / pull_request / 手动 |
| `create-pdf.yml` | 手动导出本项目中文 PDF/EPUB（gitbook-pdf-export 工具只读使用；可按首字母分批，全量约 2500 词条页；首字母过滤按 `## <字母>` 小节走，无链接的占位母行/别名行随节去留）；Python 3.15；产物仅上传运行工件，**不写 tag/Release/外部仓库**（2026-11-04 重写 D20；2026-11-16 适配，ADR-0061） | workflow_dispatch |
| `render-artifact-audit.yml` | 手动按 `SEP_SHARD` **四片矩阵**构建（`bun --bun x`，ADR-0014/0055）后逐片跑 `check_render_artifacts.py` 扫渲染残留（裸 `**`、字面 `[^`、链接残留、`@@M` 哨兵），有残留即红；报告入运行工件（2026-11-05 接线，ADR-0019；2026-11-16 矩阵化，ADR-0061） | workflow_dispatch |

* 不要新增与上述约定冲突的本地规则；需要新检查时先改 `tools/check_all.py` 的 `GATES`（CI 矩阵自动跟随）并在此登记。
* CI 红灯定位：打开 `checks.yml` 里红色的矩阵作业（作业名即门禁名），按其 `run` 命令在本地复现（如 `python tools/check_summary.py`）；各工具退出码语义见其 docstring，不按文字推断。门禁清单与本地 `check_all.py` 同源，不存在“CI 多查一项”。
* lint 配置统一在根目录 `.markdownlint-cli2.jsonc`（规则、纳入范围、按文件豁免），这是唯一一份（`.github/.markdownlint.json` 等价副本与 `.github/.autocorrectrc` 已于 2026-11-16 退役，ADR-0061）；autocorrect 配置为根 `.autocorrectrc`；`yuanwen/`（原文照录）与 `.zcode/`（本地工具）不参与 lint。
* 各工作流在文件顶部声明**最小 `permissions:`**（2026-11-15 按 CodeQL `actions/missing-workflow-permissions` 全量补齐）：只读校验类 `contents: read`；以 issue 反馈结果的加 `issues: write`；自动修复后开 PR 的加 `contents: write` + `pull-requests: write`。新增工作流照此就地声明，不依赖仓库默认权限。
* 修改工作流须同步更新本表（变更管理见 [06-governance.md](../06-governance.md)）。

## 运行时基线（2026-11-10 起，ADR-0032）

* **Python ≥ 3.15**（本地验证 3.15.2；`tools/` 仅标准库，`check_all` 全部门禁与单元测试全绿，项数以 `--list-gates` 为准）。
* **Node ≥ 26**（本地验证 26.13.0；Vite 8 要求 `^20.19 || >=22.12`，Node 26 满足；站点命令仍走 bun，见 ADR-0014）。
* **bun ≥ 1.4**（本地 1.4.4；`engines`/`packageManager` 钉在构建壳 `taophilosophy.github.io/package.json`，ADR-0055）。
* PDF 导出线（`create-pdf.yml`）用 Python 3.15（2026-11-16 用户裁定：随仓基线统一；原“暂留 3.13、待 weasyprint 上游支持”注记作废，ADR-0061）。
* **SBOM 登记**（S07，ADR-0071）：软件物料清单 `specs/046-standards-compliance/results/sbom.json` 登记依赖与版本，可溯源；本仓 `tools/` 零第三方 Python 依赖（纯标准库），前端依赖属壳仓 `taophilosophy.github.io`（ADR-0055）。

**B3.2 页面级判定（本地，未入 CI）**：`python -B specs/053-en-template-audit/bin/page_assemble.py --all`（只读判官：rule／pool／gap／stale 四态，产物 `specs/053-en-template-audit/results/page-scan.json`）；建池 `--build`（唯一写者，写 `baseline/en-template/assembly-patches/`）。口径见 ADR-0077：补集池只承载格式层（P1 文字等值／P2 哈希命中／P3 全覆盖），缺口件不入池保持红。全库约 10 分钟（0.18 s/件＋慢件）。CI 接入待下一批（差集口径同 en-roundtrip）。

# 源审计前置与存量补课（specs/036）

**版本** v1.0 ｜ **状态** 机制生效（存量批次待批启动）｜ **日期** 2026-11-15 ｜ **权威** ADR-0052 ｜ **工具** `tools/en_source_audit.py`、`tools/en_integrity.py`、`task_ops.py source-audit`

## 1. 目的

落实 ADR-0052：把 s2.5 的源侧核查（镜像轴）前移到零信任前置阶段，并新增 **HTML 本体格式与内容核查**（typo、死链、图片、公式、表格、交叉引用、注释、段落），使"翻译依据可信"从版本钉升级为版本钉＋源本体可信。本 spec 承接其存量回补：**已译出与正在翻译的词条必须补做一遍**。

**非目标**：不重译已 done 词条（除非审计暴露译文缺陷，走 ADR-0040 三层落位）；不改正文语义（勘误限于 ADR-0038 四类）；不把镜像轴在 s2.5 重复跑（已移至 s0）。

## 2. 对象与口径

| 集合 | 2026-11-15 盘点 | 处置 |
| ---- | ---- | ---- |
| 在途 `s2.5_checked`（specs/028 回退件） | 194 | **补课**：`task_ops.py source-audit` 追加 s0 记录（状态不迁移）；进 s3 的门禁已挂（无 s0 历史不放行）；镜像轴证据按 specs/028 作业面复用/续做 |
| done 存量 | 219 | **ADR-0053（2026-11-15）改口径**：原"台账制补课（不改状态机）"作废，一律 `revert-state` 回炉重走（specs/028 承接），s0 经任务内 `source-audit` 补课；台账制 `makeup-*.jsonl` 不再新增 |
| pending / cleared | 621 / 162 | 走管线自然入口：`advance --step s0` 时机检自动跑，无批量补课需要 |

勘误引发的存量影响按 ADR-0038 后果条款偿还（中文成品以重转后 yuanwen 为对照基准）；发现的内容类缺陷（漏译、错译）转该件 s2.5/s3 口径，`changes:` 登记。

## 3. s0 检查项定义（与工具一一对应）

* **HTML 本体核查**（`en/<slug>/index.html`，canon）：页面真实性与截断；typo 候选（词内数字/等号混入、重复词、异常标点串、数字替换字母、`pp.` 缺空格——启发式只产候选，人按 ADR-0038 四类定性）；页内锚点配对（硬）；站内词条链接对 `baseline/entries.json` 目录（硬）；包内资产存在性（硬，图片与链接目标）；`\(…\)`/`[…\]` 定界符配对与 TeX 花括号平衡（硬）；`\unicode`/`\char` 已知渲染问题族（告警，ADR-0049）；表格无行/配平（硬）；嵌套表（信息）；note/fn 孤儿定义（告警）；空段落与标题跳档（告警）；外链盘点（`--net` 活体检查：缓存＋≥5s 礼貌间隔＋退避；死链只登记不修）。
* **镜像轴保真**（yuanwen↔en）：specs/018 协议逐段人审＋书目逐条计数比对；机检辅助 specs/018 `regression_scan.py`。在途 s2.5_checked 件镜像轴随 specs/028 作业面继续，勿双跑。
* **处置出口**：ADR-0038 四类→`specs/001-sep-sync-pipeline/results/en-errata.md` 先行登记→就地勘误→`yuanwen.py` 重转→分歧账登记（`divergence.py register`）；死链/待考→本 spec `results/` 裁定表登记，不改正文；typo 误报→裁定表记录成因，同类 ≥3 处回修工具（specs/030 §4.7 先例）。

## 4. 执行规则

1. **按字头 A–Z 分批并行**（ADR-0043 决策 8 / ADR-0047 同构）；每批四步闭环：**扫描 → 裁定 → 修复 → 复算**，三份凭证：
   * `results/scan-<letter>-<date>.json`：`en_source_audit.py --out` 原始输出（复算基准）；
   * `results/adjudication-<letter>.md`：逐处裁定表（勘误四类／登记待考／豁免／工具误报）；
   * `results/makeup-<letter>.jsonl`：逐行 `{slug, mode: makeup|done-campaign, s0_recorded, mirror_evidence, findings}`。
2. **done 补课不进状态机**：以 `results/makeup-<letter>.jsonl` 台账为凭证（specs/023 先例）；在途件用 `source-audit` 子命令留任务内凭证。
3. **勘误与重转逐条独立**：每缺陷一处勘误＋重转＋回归扫描 OTHER=0（ADR-0038 决策 10、ADR-0040 修复路径），禁止跨条目批量套改；并行会话活跃期重转遵守 rules/06 多机并行条款。
4. **批次收口判据**：该字头 done＋在途集合中，`en_source_audit` 硬错 0、告警全部定性（勘误/登记/豁免）、镜像轴证据在案。
5. **门禁关系**：s0 机检硬错进 `advance` 门（新件即在管线内强制）；本 spec 批量补课本身为告警级，不进 `check_all`/CI；s3 门禁（历史须有 s0）已在 `task_ops` 落地。
6. **死链活检**：离线盘点先行；`--net` 全库活检单独成批（URL 去重缓存后估计规模可控），批次启动待用户批准，期间不阻塞其他作业。

## 5. 与状态机的关系

* `s0_source_checked` 为正式状态（ADR-0052）：retranslate 在 cleared 与 drafted 之间，update 在 pending 与 s1 之间；`advance --step s0` 自动挂 `en_integrity`＋`en_source_audit`；进 s3 前历史须有 s0 记录。
* `source-audit` 子命令仅供在途/done 补课：追加 s0 步、状态不迁移；pending/cleared 拒绝（走正常 advance）；重复补课拒绝。
* revert-state 语义不变（仍仅 `--to s2.5_checked`）。

## 6. Assumptions（用户裁定登记）

* 2026-11-15 用户裁定：s2.5 源侧核查前置到零信任前置阶段；HTML 本体核查（typo/死链/图片/公式/表格/交叉引用/注释/段落）必须首先做；已译出与正在翻译的必须补做一遍。
* s2.5 的译文轴＋全局对账＋密度统计＋语体审阅**不前移**（依赖已译内容，留在 s2.5）。
* 存量批次启动与 `--net` 活检批次启动均待用户批准；未启动期间除 s3 门禁外不作为在途件阻塞。
* 2026-11-15 用户裁定（ADR-0053）：全量 done 回炉重走 s0/s2.4/s2.5，§2 的 done 台账线作废；先行批字头 a＋1 已批准执行（specs/028 清单驱动）。

## 7. 收口与结案

全部 26 字头批次收口（§4.4 判据）且 `en_source_audit --all` 硬错 0 时，本 spec 转结案；此后 s0 为常规管线环节（rules/04 源审计前置环节节），本 spec 保留为存量补课凭证与工具语义登记处。

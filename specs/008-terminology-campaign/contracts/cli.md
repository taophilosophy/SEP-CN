# 契约：specs/008 术语战役工具职责权属

延续 specs/001 contracts/cli.md 的职责权属体例。三个新工具 + 既有 check_terms 扩展，全部归 008 战役会话负责。

| 工具 | 职责 | 输入 | 输出 | 权属边界 |
| ---- | ---- | ---- | ---- | -------- |
| `tools/term_harvest.py` | 逐篇遍历 yuanwen/ 全库提取术语/人名候选，与已登记条目求差，幂等可续跑 | `--letter <x>` 单字母批；默认全库 | `tasks/term-pool.json`（candidates: en/freq/type/suggest/status/sources） | 只写候选池，**不碰**两登记册与词汇表 |
| `tools/cnki_query.py` | 译名查证（provider 插件：termonline-standard 可用；cnki-dict/审定库待通道），≥5s 礼貌节流、退避重试、断点续跑 | `--from-registry`（两登记册全量）/ `--pool` / `--terms <词>...` / `--provider <名>` / `--resume` | `specs/008-terminology-campaign/results/queries/<provider>/<规范键>.json`（含请求时间与原始响应） | 只写 results/ 凭证；**不修改**任何登记册 |
| `tools/term_audit.py` | 两登记册逐条审阅驱动：关联查证凭证，四态判定（一致/不一致/查无/未查证），产出报告 | `--out <目录>`（默认 specs/008/results/） | `audit-<日期>.md` + `audit-<日期>.json` | **只报告不修改**；修正走裁定 → 登记 → 门禁 |
| `tools/check_terms.py`（既有，008 扩展） | 三表一致性门禁：登记册+人名表+词汇表冲突/自洽/缺依据告警 | 默认三表；测试可注入 `--registry/--registry2/--glossary` | 人类可读报告，退出码 | 只读，不改数据文件 |

## 数据权属

* `tasks/term-pool.json` —— 候选池（状态机 published/held/rejected 沿用 term-candidates.json 先例；term-candidates.json 保留为历史批次记录，新批次一律进 term-pool.json）。
* `specs/008-terminology-campaign/results/` —— 查证凭证与审阅报告（入库，可追溯）。
* `yi-zhe-shuo-ming.md` / `ren-ming-biao.md` —— 登记册，只经裁定流程修改（会话 Edit + 中文一行提交）。
* `qian-yan/ci-hui-biao.md` —— 发布视图，修弱势方向登记册看齐。

## 门禁接线

`tools/check_all.py` 已含 check_terms（三表模式）；audit/harvest/cnki_query 不进门禁（网络依赖），由战役批次自行驱动并在 execution-log.md 留凭证。

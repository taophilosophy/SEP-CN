# 契约：specs/008 术语战役工具职责权属

延续 specs/001 contracts/cli.md 的职责权属体例。三个新工具 + 既有 check_terms 扩展，全部归 008 战役会话负责。

| 工具 | 职责 | 输入 | 输出 | 权属边界 |
| ---- | ---- | ---- | ---- | -------- |
| `tools/term_harvest.py` | 逐篇遍历 yuanwen/ 全库提取术语/人名候选，与已登记条目求差，幂等可续跑 | `--letter <x>` 单字母批；默认全库 | `tasks/term-pool.json`（candidates: en/freq/type/suggest/status/sources） | 只写候选池，**不碰**两登记册（ADR-0036：词汇表已并网删除） |
| `tools/cnki_query.py` | 译名查证（provider 插件：termonline-standard 可用；cnki-dict/审定库待通道），≥5s 礼貌节流、退避重试、断点续跑 | `--from-registry`（两登记册全量）/ `--pool` / `--terms <词>...` / `--provider <名>` / `--resume` | `specs/008-terminology-campaign/results/queries/<provider>/<规范键>.json`（含请求时间与原始响应） | 只写 results/ 凭证；**不修改**任何登记册 |
| `tools/term_audit.py` | 两登记册逐条审阅驱动：关联查证凭证，四态判定（一致/不一致/查无/未查证），产出报告 | `--out <目录>`（默认 specs/008/results/） | `audit-<日期>.md` + `audit-<日期>.json` | **只报告不修改**；修正走裁定 → 登记 → 门禁 |
| `tools/check_terms.py`（既有，008 扩展） | 两登记册一致性门禁：自洽/缺依据告警（ADR-0036 词汇表腿移除） | 默认两表；测试可注入 `--registry/--registry2` | 人类可读报告，退出码 | 只读，不改数据文件 |

## 数据权属

* `tasks/term-pool.json` —— 候选池（状态机 published/held/rejected 沿用原 term-candidates.json 先例；**2026-11-18 起原 `tasks/term-candidates.json` 已全量并入本池并删除**，见 specs/050 §8；新批次一律进 term-pool.json）。
* `specs/008-terminology-campaign/results/` —— 查证凭证与审阅报告（入库，可追溯）。
* `shu-yu-biao.md` / `ren-ming-biao.md` —— 登记册，只经裁定流程修改（会话 Edit + 中文一行提交；前者 ADR-0036 改名，原 `yi-zhe-shuo-ming.md`）。
* `qian-yan/ci-hui-biao.md` —— 发布视图（**已并网删除，ADR-0036**；历史凭证见 git 历史）。

## 门禁接线

`tools/check_all.py` 已含 check_terms（两表模式，ADR-0036）；audit/harvest/cnki_query 不进门禁（网络依赖），由战役批次自行驱动并在 execution-log/ 留凭证。

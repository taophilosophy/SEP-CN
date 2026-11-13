# 执行记录：术语战役

术语战役（specs/008）的机制记录与批次凭证。原为单文件 `execution-log.md`（850 行、102,862 字节），2026-11-12 越过 ADR-0004 的 100 KB 阈值，按该 ADR 拆为同名文件夹：本页保留标题、索引与拆分说明，各轮次正文按阶段归入下列四份子文件，正文逐字未改。

| 阶段 | 时间 | 轮次 | 文件 |
| ---- | ---- | ---- | ---- |
| 通道考古与九轮扫批 | 2026-10-28 – 10-30 | B0 批次至第九轮 | [di-yi-zhi-di-jiu-lun.md](di-yi-zhi-di-jiu-lun.md) |
| 接管批与 A–Z 分节定型 | 2026-11-09 | TL-main-20261109、TL-az-20261109 | [jie-guan-pi-yu-az-fen-jie.md](jie-guan-pi-yu-az-fen-jie.md) |
| 审定库长跑与二轮补查 | 2026-11-11 | TL-main-20261111 正批与续批 | [shen-ding-ku-chang-pao.md](shen-ding-ku-chang-pao.md) |
| 三轮清扫收官 | 2026-11-12 | TL-main-20261112 续 | [san-lun-qing-sao-shou-guan.md](san-lun-qing-sao-shou-guan.md) |
| 词汇表并网收官 | 2026-11-13 | ADR-0036 结构收口 + 412 行分流 | [ci-hui-bing-wang-shou-guan.md](ci-hui-bing-wang-shou-guan.md) |
| 人名表分段长跑 | 2026-11-13 起 | TL-main-20261113 首段 0–200 | [ren-ming-biao-fen-duan.md](ren-ming-biao-fen-duan.md) |
| 两册去重 | 2026-11-13 | 人名 156 组 / 术语 22 组纯变体 | [liang-ce-qu-zhong.md](liang-ce-qu-zhong.md) |

* 拆分依据：ADR-0004（单体文件治理）；门禁 `tools/check_doc_size.py` 实拦，拆分后各文件均在阈值内。
* 历史追溯：`git log --follow specs/008-terminology-campaign/execution-log/index.md` 可追至拆分前的单文件历史。
* 后续批次：新轮次另起子文件并在上表登记，不回写本页正文。

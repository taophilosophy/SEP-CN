# 执行记录：术语战役

## B0 批次（2026-10-28，本会话）

### 通道考古（译名查证基础设施实测）

| 通道 | 结果 | 结论 |
| ---- | ---- | ---- |
| 术语在线 `api.termonline.cn/main-serve/business/tm/tmWord/standardSearch` | **匿名可用**（参数 `term&match=2&sources=&pubYears=&pageSize=20&pageNo=1`，返回标准文件术语库 GB 条目：cn/en/standardCode/standardName） | cnki_query 默认 provider，已投产 |
| 术语在线 `tmWord/allSearch`（审定名词库/台湾库/其他库聚合） | 匿名恒回空（`totalRecords=0`，含已知存在的词实测）；axios 拦截器 `X-Access-Token`（getToken，仅手机/微信/账密登录发放，无访客通道） | **禁用，待 token 通道**；spec FR-005 插件位保留 |
| CNKI 翻译助手 dict.cnki.net | curl/urllib/subagent-WebFetch：TLS 指纹反爬断连或空壳 SPA（结果 AJAX 加载）；内部 API 端点未破解 | **禁用，待浏览器通道**；spec FR-005 插件位保留 |
| 判定基准数据点（浏览器实测） | termonline 网页端搜索「溯因推理」→ 349 条结果，审定库含：溯因推理=abductive reasoning（计算机科学技术名词 2018，又称反绎推理）；溯因=abduction（自然辩证法名词 2024，科学哲学_归纳，定义在案） | 审定名词库确实覆盖哲学，token 通道接通后价值最高 |

### 立法（ADR-0012，commit 16b325ac）

* 译名依据优先级三档（知网系 → 权威译本 → 学界惯例；**禁维基**）入 rules/03。
* `ren-ming-biao.md` 人名表拆分（154 术语 + 19 人名五列迁移），check_terms 扩三表校验 + 缺依据告警，140 单测全绿。

### 逐篇遍历（commit 02653da5）

* `tools/term_harvest.py` 全库首跑：**2426 件**（yuanwen/ 全镜像），五路提取（斜体/引语/-ism/高频短语/人名序列）。
* 迭代修复三现：① 尾部站点节（References/Academic Tools 等）不裁剪 → 39 万候选充水（Oxford/Cambridge/DOI 噪声）→ 裁剪后收敛；② 全量跑合并语义错误（旧条目残留）→ 改整池重建；③ 停用词更新后必须 `--refresh`（单篇缓存嵌入旧停用词，实测 'criticism'/'see Section' 残留假象）。
* 终态：**61997 候选 / 26MB**（phrase 18990 / italic 25049 / person 8295 / quoted 8803 / ism 860），低频尾部留存 harvest-cache（本地 gitignore，随词条翻译核定）。
* 池顶样例（ phrase ≥1000）：possible worlds、mental states、human nature、possible world、twentieth century、natural selection——真术语密度合格；泛词（human beings/criticism 类）由裁定档驳回。

### 查证与审阅（本次运行，2026-10-28）

* `cnki_query.py --from-registry`：两登记册 **192 键**（154 术语 + 19 人名 + 并行会话 fc48ce23 新增文献译名 19 条）× termonline-standard 全量查证，5s 节流，凭证 192 份入库（ok 77 / empty 115）。
* 迭代修复两轮：① 首轮凭证 `cn=None` —— standardVO.tmWordList 字段名实为 `cnName`/`enName`（与 allSearch 不同），作废重查；② 审计命中相关性过滤（GB 库 match=2 模糊匹配噪声）：初版词元重叠 ≥1 放进大量噪声（Bell→号钟/钟罩），收紧为「查询词元全集 ⊆ 命中 EN 词元（剥尾 s）」后不一致 75→5→4。
* **终态四态分布：一致 2 / 不一致 4 / 查无 186 / 未查证 0；维基排查 0**。
* 不一致明细（待裁定，已列于 audit-2026-10-28.md）：connectionism（联结主义 vs 连接机制）、mechanism（机械论 vs 机制）、quantum theory（量子理论 vs 量子复杂性理论）、Plato（柏拉图 vs 柏拉图度，人名表）——多为 GB 标准库学科错位，哲学现行译法均为学界通行，倾向保留并标注「学界惯例」档依据。
* **结论**：GB 标准库哲学覆盖率低（查无 186/192）属预期，其证据价值限于工程类术语；审定名词库（termonline 网页实测确有 abduction→溯因/溯因推理 词条）与 CNKI 翻译助手两条主力通道仍待接通（P0）。

## 教训（复用）

1. 本会话 ZCode 的 DeferredToolCall/浏览器/MCP 通道整体损坏（校验器 "name missing" 缺陷）——网络工作全走 Bash+子代理，子代理自带 WebFetch 可过部分 WAF。
2. heredoc 内嵌 Python 补丁再次失败（assert 未命中静默 no-op / 转义损坏）——一律 Edit 工具改码，脚本补丁必须 assert 验证。
3. 提取器阈值/停用词每次改动后，已缓存的单篇结果不会自动失效——`--refresh` 强制重提，否则看到的是旧词表的假象。

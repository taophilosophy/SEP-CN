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

## 阿拉伯伊斯兰加强批（ADR-0013，2026-10-28 第二轮）

用户裁定：加强伊斯兰阿拉伯人名、术语的识别、区分、翻译。

### 识别（提取器升级）

* 词元正则扩展拉丁扩展区（\u00C0-\u024F、\u1E00-\u1EFF）与 ʾ ʿ（\u02BE-\u02BF）首字符；新增**阿位专名路由**：含定冠词同化形（al-/ad-/as-/…，含 al-Dīn 型冠词连字词与 Al-Fârâbî 型连字符词）、谱系词（ibn/bin）、尊称（abu/abū/umm/abd/dhū）颗粒的专名序列 → type=arabic。
* 键规范化升级为**变音符折叠**（NFD 剥组合记号后 casefold）：Al-Fârâbî / al-Farabi / Abū Naṣr al-Fārābī 归并同键；check_terms.norm_key 同步，三表比对折叠归一。
* 全库 `--refresh` 重提两轮（首轮 arabic 727 → 补 ʿʾ 后 **822**）：Ibn Gabirol 567、Ibn Taymiyya 423、Ibn Daud 312、ʿAyn al-Quḍāt 187、Kashf al-Asrār 112、Fakhr al-Dīn al-Rāzī 94、Naṣīr al-Dīn al-Ṭūsī、Tahāfut al-tahāfut 等完整形全部入池；此前 ASCII 截断假候选（Fakhr al-D、al-K tib、Ikhw al-Saf）清零。

### 区分与翻译（登记与词汇表修正，commit 7d39e70f）

* **人名表种子区 24 行**：拉丁通行名/阿拉伯本名同人归并（Ibn Sīnā/Avicenna → 伊本·西那（阿维森纳）等）；**父子语序区分**（Ḥunayn ibn Isḥāq 侯奈因·本·伊斯哈格父 ↔ Isḥāq ibn Ḥunayn 伊沙克·本·侯奈因子）；**同姓区分**（Abū Bakr al-Rāzī 拉齐 ↔ Fakhr al-Dīn al-Rāzī 法赫尔丁·拉齐）。
* **术语表种子区 19 行**：kalām 凯拉姆；伊斯兰教义学、falsafa 法尔萨法；哲学、ishrāq 照明、tawḥīd 认主独一、Muʿtazila 穆尔太齐赖派、Ikhwān al-Ṣafāʾ 精诚兄弟会及四部经典书名。
* **词汇表 9 处修正**：al-Farabi/Al-Fârâbî 归并且**主译裁定变更**（阿里·法拉比 → 法拉比，学界通行，旧形注记保留）；Avicenna↔Ibn Sina、Averroes↔Ibn Rushd、Avempace↔Ibn Bâjja 两通行名互见；al-Razi 行补"医师哲学家，勿与法赫尔丁·拉齐相混"。
* 知网系查证：新键 43 条全部凭证在案（GB 标准库人物/宗教术语覆盖率低，empty 属预期，依据档位如实标注"学界通行/权威工具书"）。

### 教训

1. 阿位专名识别的关键不是"找出大写词"而是**颗粒词法**（al-/ibn/abd/ʿAbd 的正字形态变体全谱），且变音符必须在词元层支持（折叠只解决归并，不解决截断）。
2. published 词汇表的旧译法（阿里·法拉比）来源大概率是"al-"冠词直音译——裁定变更时旧形必须保留在注记里（可追溯）。
3. 主译变更（阿里·法拉比→法拉比）属登记册裁定，词汇表修弱势向登记册看齐——check_terms 冲突 0 即证明归一完成。

## 教训（复用，B0 批次）


1. 本会话 ZCode 的 DeferredToolCall/浏览器/MCP 通道整体损坏（校验器 "name missing" 缺陷）——网络工作全走 Bash+子代理，子代理自带 WebFetch 可过部分 WAF。
2. heredoc 内嵌 Python 补丁再次失败（assert 未命中静默 no-op / 转义损坏）——一律 Edit 工具改码，脚本补丁必须 assert 验证。
3. 提取器阈值/停用词每次改动后，已缓存的单篇结果不会自动失效——`--refresh` 强制重提，否则看到的是旧词表的假象。

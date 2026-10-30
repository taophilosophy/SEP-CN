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

## 池首轮裁定与 P2 回填批（2026-10-28 第三轮，用户批准待办）

* **P1 池裁定**（commit bfa9c568）：A 档 34 条直裁登记（-ism 骨架 15：mysticism/compatibilism/reliabilism/existentialism 等；亚氏著作与《数学原理》4；模态/心哲骨架短语 9：可能世界/模态逻辑/心理状态等；人名 5：托马斯·阿奎那/大卫·休谟/威廉·詹姆斯/艾因·库扎特/阿卜杜·贾巴尔）；B 档 16 held（书名待核/全名待核/语境分流，理由逐条入池）；C 档 16 rejected（泛词/截断/现代学者保留英文体例）。manifest：tasks/manifests/2026-10-28-pool-adjudication.json。
* **工具修复**：`load_registered_keys` 补归并行**变体拆分**（「主形 / 他形」逐变体作键，Ibn Gabirol 型种子变体此前漏排除）；裁定脚本 B/C 键过折叠（abū ḥātim ≠ abu hatim 首轮漏配 6 条）。
* **P2 依据回填**：169 行「待知网复核（008 战役）」按凭证替换为实证依据两态（查证无收录/查证在案 + 待主力通道复核）。
* **发布词汇表同步**：36 行字母序插入（含 4 处书名号口径修正对齐登记册《》形）；check_terms 冲突 0、七门禁全绿。
* **P0 通道**：本会话 ZCode DeferredToolCall 校验器持续损坏（浏览器/WebFetch 全不可用），CNKI 浏览器攻坚与审定库 token 接入留待新会话或用户供 token（axios 头 `X-Access-Token`）。
* **登记册修复（commit 3e6b8275）**：bfa9c568 曾把 30 行插错节（append_rows 无节边界）且回填脚本 `strip('|')` 丢行首尾竖线（191→71 行表格形态破坏）——从 7d39e70f 恢复重做三处修复：append_rows 节边界、行首尾竖线复原、依据列定位 cells[3]（首轮误写裁定日期列）。**教训：表格行重组脚本必须先小样验证再全量；strip 系操作后必须显式复原定界符。**
* **终态**：A 档新键凭证补齐（累计 270 份，含归并行整键 possible_worlds_possible_world），审计 一致 2 / 不一致 5 / 查无 262 / 未查证 0 / 维基 0；七门禁全绿。




## P0 换站批（2026-10-28 第四轮，用户裁定"p0换其他网站"）

* **探测矩阵**：中国大百科全书 www.zgbk.com（可达但 content-protect/mtoken 请求签名，SSR 壳无结果，内部 API 未破）；国家哲社文献中心 www.ncpssd.org（可达，搜索机制已破译——`POST /searchHandler/search` + base64 Lucene 串 `(IKVT="X" OR IKPYTE="X" ...)`，但站点自带查询串亦回 0，需会话参数，留待浏览器通道）；必应词典（重定向无数据）。
* **有道词典打通并投产**：`dict.youdao.com/result?word=X&lang=en` 匿名可用（SSR，按学科分组释义）。接入 `youdao-aux` provider（**辅助参考档**：不作依据，供裁定辅助与多义区分——abduction 逻辑学义=溯因推理、法学义=诱拐罪，正是"区分"所需）。
* **全量批查**：两登记册 285 键 × youdao-aux，凭证 **286 份**入库（ok 157 / empty 129，命中释义 684 条）——覆盖率 55%，远超 GB 标准库。
* **审计修复**：相关性过滤对直接查词通道（hit 无 en 字段）放行——四态从 查无262 改善为 **一致 126 / 不一致 31 / 查无 128**（维基 0）。不一致 31 条待裁定清单见 audit-2026-10-28.md。
* 通道现状：termonline-standard（档①）+ youdao-aux（辅助档）双通道投产；审定库 token / CNKI 浏览器 / zgbk / ncpssd 四通道插件位保留。

## P0 审定名词库通道破译（2026-10-28 第五轮，浏览器捕获）

**结论：termonline-all（审定名词库）通道已从「待 token」转为「可用」，AES 解密 + X-Access-Token 明文 JWT 已破译。CNKI 通道仍待浏览器。**

* **关键坑（B0 误判根因）**：B0 曾判「allSearch 匿名恒空 totalRecords=0，需 token」——实测确认**匿名确实恒空**（200 但 totalRecords=0），但**带有效 token 即返回真实数据**，故非「禁用」而是「需 token」。真正拦路的是 token 的**加密存储**：localStorage 的 `TERMONLINE__PRODUCTION__3.1.7__TOKEN__` 是 **AES-CBC-PKCS7 密文**（非明文），B0 直接读该值发请求 → 服务端 `getUserSectionInfoByToken` 校验密文 → 401「token非法无效」。
* **破译链路**（bundle `index-9a01f905.js` 静态还原 + 浏览器实测验证）：
  1. `createStorage$1` 用 `hasEncrypt=true`，`AesEncryption` 用 **AES-CBC + PKCS7**；
  2. `cacheCipher = {key:"_11111000001111@", iv:"@11111000001001_"}`（均 16 字节 UTF-8，iv 非 base64）；
  3. 解密 localStorage 密文 → `JSON {value: <明文JWT>, time, expire}`，取 `.value`；
  4. 请求头 `X-Access-Token: <明文JWT>`（无 scheme；拦截器 `requestInterceptors` 注入，`withToken:true` 才注入）。
* **端点在案**：`GET /main-serve/business/tm/tmWord/allSearch?term=<词>&match=2&sources=&pubYears=&pageSize=20&pageNo=1&baseId=1`（baseId=1 必填；`tmDatabase/listFront` 返回 4 库：id 0=审定公布/1=海峡两岸/2=其他来源/6=预公布）。
* **响应结构**：`result.searchResult[]` 每库 `{result:{totalRecords, tmWordList[], yearStats, sourceStats, typeStats}, id}`；词条字段 `cn/en/source/subjectName/subjectFullName/publishYear/definition/bbh/wordNumber/alsoName/aliasName`。**哲学覆盖率高**：实测「溯因推理」349 条，自然辩证法名词 16 条（溯因=abduction 2024、质料因=material cause 2024、三因学说等），GB 标准库（standardSearch）查无 186 的哲学词在审定库全在案。
* **实现方式**：provider 需（a）本地 AES-CBC 解密 localStorage 密文 → 明文 token；（b）token 有效期校验（JWT `exp`）；（c）带 `X-Access-Token` 头请求。**token 不落盘**：解密逻辑写进 `cnki_query.py`，token 来源经 `--token-env TERMONLINE_TOKEN` 环境变量或 `--token-file` 传入（用户浏览器 localStorage 密文导出），避免明文入库。
* **教训**：①「匿名恒空」≠「需登录」二象性——需区分「200+空」（无凭证被静默降级）与「401」（凭证错误）；②SPA token 存储常为**加密**，直接读 localStorage 拿到的是密文，必须还原站点 `cacheCipher` 后解密；③浏览器 evaluate 里 fetch 测试会被**已 patch 的 fetch/XHR** 干扰（返回 clone 消费原响应致空）——复现请求须用干净上下文（navigate 后未 patch 的 window）。
2. heredoc 内嵌 Python 补丁再次失败（assert 未命中静默 no-op / 转义损坏）——一律 Edit 工具改码，脚本补丁必须 assert 验证。
3. 提取器阈值/停用词每次改动后，已缓存的单篇结果不会自动失效——`--refresh` 强制重提，否则看到的是旧词表的假象。

## 浏览器通道全量扫批与首轮审定裁定（2026-10-29 第六轮）

**用户通道开通（浏览器登录）后的全量执行日。审定库（termonline-all）升为查证主力，登记册全量 306 行完成浏览器通道查证，9 行按审定名词完成主译裁定变更。**

### 鉴权机制实测修正（取代第五轮结论）

* 第五轮「X-Access-Token 明文 JWT 即可」**不完整**：Python 直连（urllib）带同一 JWT 仍被静默降级（200 + 全库 0，与匿名不可区分）。请求头捕获（钩 setRequestHeader）证实应用确实发送同值 JWT，但真正不可复现的是**真实浏览器上下文**；cookie 会话为短 TTL（约半小时级），不能只靠 cookie。
* **瞬时限流形态**：连续快速请求（5s 节奏连发 12 发）触发全库 0 降级，冷却 5 分钟恢复；**页面加载（goto/reload）可立即激活窗口**，窗口内 10s 节奏 ≥5 发全部正常。运行配方定型：每批 reload → 每词重读 localStorage 密文 → node 侧解密（`crypto.createDecipheriv`，AES-128-CBC，cacheCipher）→ evaluate 注入 → `credentials:"include"` + JWT 头 → 批间冷却 4 分钟。
* 响应形态判别：正常=4 库且总数>0；**降级=3 库全 0**（限流/无凭据），ingest 前把降级改记 error，防止误判「查无」。API 库 id 为 32 位十六进制串（…0006→6），须 int(id,16) 折算后查库名（cnki_query._tl_all_parse 同处修正）。
* **全量执行**：登记册 286 行（emit 313 查询项，归并行拆变体）34 批 + 并行会话中途新登记 20 行补扫 3 批，共 334 项全部落凭证（`results/queries/termonline-all/`，154 份新凭证入库）。
* node REPL 教训：① fetch 循环不能写在 node 侧（内核无 fetch，「fetch is not defined」）——必须在 `tab.playwright.evaluate` 内；② evaluate 传字符串函数体不会被调用（返回 {}）——传函数对象 + arg；③ 全量结果由 node 直写 %TEMP% 文件、只回批摘要，避免 30+ 批原始 JSON 撑爆上下文。

### 比对口径升级（check_terms）

* `translations()`：吸收注记 亦作"X" 变体（半/全角引号）与《书名号》主形——绝对唯心主义/《数学原理》类假「不一致」消除。
* `parse_glossary()`：词汇表第 3 列注记只提取 亦作"X" 形态并入比对（整列并入会把「学界通行」等叙述当译法，实测 143 假滞后，已收窄）。滞后告警 20 → 9（低于战役前 11）。
* 单测 143 全绿；硬错误 0、冲突 0。

### 首轮审定裁定（9 行主译变更，依据=审定名词库·自然辩证法/经济学名词，凭证 2026-10-29）

| 原文 | 旧主译 | 新主译 |
| ---- | ---- | ---- |
| bayes rule | 贝叶斯规则 | 贝叶斯法则 |
| bayesian confirmation theory | 贝叶斯确证理论 | 贝叶斯验证理论 |
| common cause principle | 共因原则 | 共因原理 |
| consequentialism | 后果主义 | 后果论 |
| Dutch book (argument) | 荷兰赌（论证） | 大弃赌论证 |
| empirical equivalence | 经验等价 | 经验等价性 |
| empirically equivalent | 经验等价 | 经验等价的 |
| Inference to the Best Explanation | 最佳解释推理 | 最佳说明推理 |
| underdetermination | 非充分决定性 | 不完全决定 |

* 全部旧主译降为 亦作（可追溯）；ci-hui-biao 弱势方向 11 行同步看齐。
* 保留不改的「不一致」（依据不足或 sense 不符，共 30 行）：youdao-aux 辅助档按规则不作变更依据（Anaximenes/Theophrastus/Xenophanes 等人名异译）；审定库命中为跨学科同名（mechanism 机构/机理、warrant 认股权证、imposition 组版、integral wholes 整数、dictum 集体消费理论等）； narrowing-term 命中（confirmation theory 对贝叶斯验证理论）。
* anomalous monism 经比对口径升级后转「一致」（登记册 亦作 已含审定形 异常一元论）。
* 审计终态：**一致 154 / 不一致 30 / 查无 122 / 未查证 0，维基 0**（306 行全覆盖，含并行会话新增 20 行）。

### 待办（下一会话接手）

1. **池批次**：term-pool 中频段（phrase 50-300、person 5-50、arabic <20）按本契约跑批裁定（`--emit --pool`，词条级批次节奏同本文档）。
2. **高噪声词精确补查**：match=2 对含 "ibn"/"the" 等词的查询命中巨型模糊池（Ibn Bājja/Ḥayy ibn Yaqẓān 同回 4498/987/419/610），主译裁定前需 match=1 精确补查定向核销。
3. **cnki-dict 浏览器通道**：同法可在 dict.cnki.net 页面内试内部 AJAX（本会话未再攻，插件位保留）。
4. 登记册 irrealism 行落在伊斯兰节（并行会话编辑错节），下批登记时归位。

## 批准待办全执行（2026-10-29/30 第七、八轮：P2 结算 + 池 A 档两批 + C 档专项 + match=1 补查）

用户「批准所有建议」后的连续执行。四项建议全部落地：

### P2 依据回填结算（第七轮，commit 0e3feaa9）

两登记册 **164 行**「待主力通道复核」后缀按终审计四态结算为实证文本（一致/查无/在案三形，驱动=audit-2026-10-29.json，干跑零告警）；irrealism 行错节归位主术语区。

### 池 A 档首批（phrase 150-300，27 词，commit bb0eFF63）

emit 定制清单 + 浏览器通道 4 批查证 → 采审定 12（心理内容/科学解释/数理逻辑/模型论/量子态/希尔伯特空间/概率论/知情同意/意向状态/本体论承诺/佩亚诺算术/因果说明复合词佐证）+ 学界惯例 15（动力因/差别原则/定言命令/社会正义等，跨域审定不采：医学域"意识性体验"、地理域"社会公正"）→ 三表同步 27 行；池状态 published@2026-10-29 + 垃圾 3 条 rejected；manifest tasks/manifests/2026-10-29-pool-a1.json。

### C 档泛词专项（45 条，无网络）

中频段明确泛词/残片/引文框架词批量 rejected:C档泛词专项（理由逐条入池）。

### match=1 精确补查（37 项+ASCII 变体，第八轮）

**结论性发现：审定库不收录伊斯兰哲学人名/书名**——al-Fārābī/Ibn Sīnā/Tahāfut 等全部键（变音符、ASCII 两种拼写）match=1 精确查询均为认证空（4 库形），此前 match=2 的巨型命中确认为纯模糊池噪声。相关登记行依据=学界通行+审定库精确查无；凭证 note 带 match=1 标记（ingest 已支持 match 字段）。教训：match=2 的「巨型同名结果集」行不能当在案证据，match=1 空才是可采信的查无。

### 池 A 档二批（phrase 100-150 + person 高频，22 词，2026-10-30）

术语 15（采审定 4：相空间/囚徒困境/空集/人类能动性；学界惯例 11：先天知识/认知不义/概括原则等）+ 人名 7（洛克/康德/司各脱/恩披里柯/罗尔斯/弗雷格/杜威，学界通行汉译+审定精确查无）+ Del Medigo held（全名语境待核）；三表同步（登记册+15、人名表+7、词汇表+22）；manifest tasks/manifests/2026-10-30-pool-a2.json。

### 审计终态（2026-10-30）

**一致 171 / 不一致 34 / 查无 149，维基 0（354 行全覆盖）**。34 条不一致全部为有记录的保留裁定：辅助档不作依据（Pietism 等）、跨学科同名（warrant 认股权证等）、审定命中为下位词/复合词（confirmation theory、causal explanation）、部分证据（epistemology of belief）、跨域审定不采（conscious experience）。check_terms 硬错误 0、冲突 0、滞后 9；check_all 七项全绿。

### 下一批待办

1. phrase 50-100 段与 person 中频段继续 A/C 分档（节奏与工具已固化，见技能 termonline-batch）；
2. person 池中大量**书名/概念误入 person 型**（Principia Ethica、Twin Earth、Frankfurt School 等）需重新分型后再裁定；
3. person 池现代学者按体例批量 rejected（保留英文）。

## 多语种智能提取升级与 foreign 首批（2026-10-30 第九轮，用户裁定"动态提取/不一定是英语/还有阿拉伯语"）

### 提取器升级（term_harvest.py 六路→多路）

* **主题词路线（type=topic）**：H1 题名 + 章节标题关键短语；专用清洗 clean_topic（剥首尾停用词而非拒收——clean_phrase 的「首词停用词即拒」会杀死 "The Basic Idea" 型标题）；TOPIC_GENERIC 排除 Introduction/References 等框架词。与既有候选同键时类型合并（topic 最弱，phrase/italic 优先）。
* **原文文字路线**：阿拉伯（含波斯扩展）/希腊/希伯来/西里尔/天城体/汉字六种字母序列；单字母守卫（希腊数学变量 φ/α 非术语，除汉字外 ≥2 字符）。语料实测：希腊 339 篇、希伯来 12、阿拉伯 3（罗马化 route 仍是主力 784 新键）、西里尔 18、汉字引文（理 49/仁 38/道 26）。
* **罗马化外语重分类（type=foreign）**：斜体/引语候选含非 ASCII 拉丁扩展、德语名词后缀（-heit/-keit/-ung/-schaft/-tät/-isch）或经典词小词典（Dasein/Lebenswelt/logos/phronêsis 等 40 词，可扩充）→ foreign。
* **池账本语义修复（数据事故拦截）**：原 fresh 循环的 registered 差集作用于全部键，而池自身是 registered 源之一——第二次全量跑会把整个旧账裁掉（实测 62828→12930）。修复：全量跑=账本语义，旧池条目一律保留，registered 只挡「新键入池」；恢复池后重跑=75594（62828+12766 新）。
* 语料扫描方法论：先扫码点分布定路线规模（CJK 2425 篇全是 yuanwen 转换器的「References（引用注释）」脚手架，尾部裁剪已切；真引文汉字是少数）。

### foreign 首批 19 词（三批浏览器通道查证 + 直裁）

采审定 3（logos 逻各斯·自然辩证法、naïve realism 朴素实在论·科学哲学、polis 城邦·世界历史）+ 缩略形佐证 1（Löwenheim-Skolem→勒文海姆–斯科伦定理，亦作 L-S定理）+ 学界惯例 15（中哲拼音转写 Dao/qi/rén/yì/tian——拼音与汉字对应、希腊 technê/epistêmê/nous/phronêsis/eudaimonia、佛教 dharma/svabhāva、德语 Bildung、哥德尔数、《百科全书》）；held 3（ilāhiyyāt/wujūd/pathê 语境待核）；rejected 4。三表同步 18 行；manifest tasks/manifests/2026-10-30-foreign-a1.json。

### 落地复核（同日，用户裁定"复核术语落地情况"）

`check_terms --docs` 九个非存根词条核销：9 处告警判定为 ①登记变更后正文涟漪（abduction 用旧主译 最佳解释推理×5/贝叶斯确证理论×4/经验等价×2/荷兰赌论证×1；spacetime-holearg 规范自由×2）②正文合理变体未登记（不充分决定性、荷兰赌论证→已补进亦作）③首现标记宽泛（IWE/total evidence 未在正文出现，良性）。**checkers 落地核销语义升级**：两层报告（任一变体出现=落地；主形未出现=「主译待对齐（涟漪）」信号，且仅 亦作 行触发涟漪——译作 行是并立形不算）；translations() 补 译作"X" 与 "X""Y" 连排引号支持、「（思想的）副词论」型前缀括注 head 提取修复。涟漪正文修订属三校/变更流程，不在核验器代改。

### 涟漪对齐执行（2026-10-31，commit 7f06c647）

正文对齐直接编辑（证据链=登记册裁定行+本日志，不走 update 任务——变更文件契约属上游漂移，术语对齐非上游变更）：abduction.md 最佳说明推理×5、贝叶斯验证理论×4（含节标题）、经验等价性概念×1（行 57 的「经验等价的」为 empirically equivalent 登记形与谓词用法，保留）、动态大弃赌论证×1、不完全决定论证×2（行 433 相关词条标签属该词条自身题名，不动）；spacetime-holearg.md 规范自由度×6（含 10.3 节标题与链接文字）。核销终态：**9 文档仅剩 1 处良性告警**（total evidence 未在正文出现）。check_academic --strict 两文档通过。

### foreign A2 批（2026-10-31，榜 20-60 名，19 词直裁）

**本批亮点：审定库·哲学域直接命中 3 个佛教术语**——śūnyatā=空、vijñāna=识、tathāgatagarbha=如来藏（哲学名词审定覆盖梵语佛教术语的实证）。学界惯例 16：Dasein 此在（陈嘉映译本）、Geist 精神、epoché 悬搁、theōria 静观、puruṣa 神我、différance 延异（德里达定译）、Bedeutung 意义（王路"意谓"并存注记）、saṃsāra 轮回、aretê 德性、īśvara 自在天、哥德尔句/哥德尔定理/卢卡西维茨逻辑 + 书名《几何学》《吕氏春秋》《鲁拜集》。held 3（希伯来/韩/日罗马字冷僻书名）；rejected 12（残片/复数形/单字拼音歧义）。三表同步 17 行（nous 于 A1 已登记不重复）；manifest tasks/manifests/2026-10-31-foreign-a2.json。check_all 七项全绿（009 会话已自行修复其尺寸违规与 abortion 任务记录）。

### foreign A3 批（2026-10-31，榜 60-105 名，18 词查证 15 词直裁）

审定·心理学域直接命中 1：Müller-Lyer illusion=米勒-莱尔错觉。学界惯例 14：aisthêsis 感知、arché 本原（始基）、kinêsis 运动、anumāna 比量、pratyakṣa 现量、schêma 图型（康德）、Sittlichkeit 伦理（黑格尔）、Vorstellung 表象、waḥdat al-wujūd 存在单一论（伊本·阿拉比）、mutakallimūn 凯拉姆学者、Mīmāṃsā 弥曼差、Löb's theorem 勒布定理 + 书名《反杜林论》《哲学思想录》。held 8（印度量论截断与阿位逻辑术语 taṣdīq"断定"候选等语境待核）；rejected 18（介词残片/单字拼音/已登记行变体）。三表同步 15 行；manifest tasks/manifests/2026-10-31-foreign-a3.json。check_all 七项全绿。

**foreign 榜高频段（freq ≥18）至此扫完**：三批累计 56 词查证、50 行落册；余量转入中低频长尾（harvest-cache 留存，随词条翻译核定）。

### topic 专项（2026-10-31，4743 条清洗 + 7 词登记）

topic 型（标题词）专项：**7 个真术语查证登记**——Metaphysics 形而上学（946 篇标题在案）、biodiversity 生物多样性、Epistemology 认识论、Freedom 自由、Causation 因果关系（审定"因果关系"）、Rule Consequentialism 规则后果论（随后果论行）、Epistemic Closure 认知封闭；**结构性/自明标题词批量清洗 502 条**（Life and Works/Biographical Sketch/supplement 类 + Life/History/Language 等自明单词）；多词专名余 ~4200 条保持 new 随词条核定。manifest tasks/manifests/2026-10-31-topic-a1.json。教训：脚本干跑应无副作用——topic_a1.py 的池写盘未受 dry 开关保护，幸而目标态幂等。

### person 池专项（2026-10-31，重分型 33 + 拒登 8 + 15 词登记）

person 型 8711 条的 top 段约半数为**误分型真术语**（书名/机构/概念被 person 路径捕获）。三步处理：① 33 条重归 phrase（法兰克福学派/批判理论/孪生地球/说谎者悖论/中文屋/《哲学研究》/《人类理解论》等）；② 8 条拒登（Book III/Part III 编号残片、Maynard Smith 现代学者体例、Sherlock Holmes/Clark Kent 虚构人物、North America 地理词、John Duns 已登记行变体、Civil War 语境歧义）；③ **15 词查证登记**——审定直接命中 4（批判理论·自然辩证法、法兰克福学派·新闻传播学、中文屋论证·自然辩证法、狭义相对论·物理学）+ 学界惯例 11（自然权利/天赋人权并立、主动理智、圣灵、说谎者悖论、必然真理、公共证成、净土、孪生地球 + 人物霍布斯/普特南/惠施）。三表同步 15 行（登记册 +12、人名表 +3、词汇表 +15）；manifest tasks/manifests/2026-10-31-person-a1.json。check_all 七项全绿。

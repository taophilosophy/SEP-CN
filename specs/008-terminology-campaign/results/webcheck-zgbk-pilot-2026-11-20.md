# 查无联网查证·zgbk 脚本道投产与试金石批 2026-11-20

## 通道破译（档②主力道，无需浏览器）

中国大百科全书第三版网络版（zgbk.com）签名机制全链破译并脚本化（`script/tmp/zgbk_fetch.py`）：

1. SSR 页内嵌会话串 `var token = "<32位hex>"`（页载即发，非 cookie）；
2. AJAX 签名头 `token: hex_md5(会话串 + '/ecph 后路径')`（mtoken.js 实证）；
3. 请求须携带页面会话 cookie（JSESSIONID 等）＋Referer，缺一即 401；
4. 搜索端点 `POST /ecph/api/search`（form：conditions JSON［accuracy 1=精准/0=模糊、field=title、logic］＋pageIndex＋pageSize＋siteID），返回条目 title（含 font 高亮）/summary/subjectName/wikiType；另有 `/ecph/api/suggest`（标题联想）。
   此前 2026-10-28 探测记录“内部 API 未破”就此收口。

## 试金石批（60 词，与 OpenAlex 道同队列）

* 抓取 ok 60／error 0，5.1s/词（≥5s 节奏）；命中 7，**7/7 全部条目直证、语境正确（100%）**。
* 裁定：**KEEP 7**（abhāva→无体量、Abhidhamma/Abhidharma→阿毗达磨、Abhidharmamahāvibhāṣā→大毗婆沙论、abilities→能力、Academy（Plato's）→学园〔条目"学园派"释义明指柏拉图学园〕、acknowledgement (Anerkennung)→承认〔"黑格尔哲学的一个基本概念"〕）——全部档②（权威工具书条目直证，ADR-0012 顶档）；余 53 NOSOURCE（本道无条目，留 OpenAlex／后续段）。
* 凭证落库：新增 4 件，3 件追加出处进既有 OpenAlex 凭证（append 语义，双道并网不覆盖）。
* 四态：一致 2,000→2,004、查无 8,822→8,818（追加件此前已翻转）。

## 校准

* zgbk 道证据质量为全档最高（条目＋定义原文引证），命中即 KEEP，几乎无假命中（条目库本身即权威语境）。
* 命中率与词性相关：试金石段为书名/专名密集区（A 字头英文书名多无条目），哲学术语段预期显著上升。
* 道口定盘：**zgbk 脚本道＝主力（档②，无配额硬顶，守 ≥5s 节奏）**；OpenAlex＝补充道（档③，独立 key $1/日）；ncpssd（档③）机制在案待复探。
* OpenAlex 接独立 key（librebsd@163.com，`.secrets/openalex-api-key.json`）后重跑 200 词零 429，累计 ok 278 词、117 词有命中待裁定（raws b1–b16 在 script/tmp/webcheck-raw/，断点 next=279/batch=17）。

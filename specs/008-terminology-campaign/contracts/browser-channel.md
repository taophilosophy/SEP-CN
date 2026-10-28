# 契约：术语在线「审定名词库」浏览器通道标准流程（S.O.P.）

> specs/008 第六轮（2026-10-28）确立。取代第五轮「仅 X-Access-Token 头即可」的结论。
> 适用：`cnki_query.py` 的 `termonline-all` 数据源实际经本通道执行；`tl_browser_batch.py` 承担批次与落盘。

## 鉴权事实（实测修正）

1. 审定库 `allSearch` 的有效凭据是**登录会话**：应用前端经 axios 拦截器发送
   `X-Access-Token: <明文 JWT>`（localStorage `TERMONLINE__PRODUCTION__3.1.7__TOKEN__`
   的 AES-CBC-PKCS7 密文解出，`tools/termonline_token.py` 同款 cacheCipher）。
2. **Python 直连（urllib）带同一 JWT 头仍被静默降级为「200 + 全库 0」**——真实浏览器
   上下文不可省。cookie 会话短 TTL（约半小时级），不能只靠 cookie。
3. 稳定配方＝**页面内 fetch + X-Access-Token 头 + `credentials:"include"` + 相邻请求 ≥5s**。
4. 响应形态判别：正常=4 库（审定公布/海峡两岸/其他来源/预公布）且总数>0；
   **降级=3 库全 0**（限流或无凭据，与匿名不可区分）。连续快速请求会触发瞬时限流，
   停 1-2 分钟或经 UI 正常检索一次即恢复。
5. JWT 明文不落盘不入库：node 侧 `crypto.createDecipheriv("aes-128-cbc",
   "_11111000001111@", "@11111000001001_")` 解密后经 evaluate 参数注入页面。

## 标准作业（每批次循环）

```text
1) 产清单：python tools/tl_browser_batch.py --emit --out <tmp>/tl-batch.json [--pool]
   （登记册全量；归并行「主形 / 他形」拆变体，行键保留整行）
2) 浏览器跑批（ZCode browser-use，每批 ≤12 词）：
   - node 读 <tmp>/tl-batch.json 切片 → 逐词 evaluate(fetch allSearch, credentials+token)
   - 批内相邻请求 sleep ≥5000ms；结果写 <tmp>/tl-batch-<offset>.json（row_key 已标注）
   - 批摘要（词:状态:各库总数）入会话即可，全量 JSON 不过上下文
3) 落凭证：python tools/tl_browser_batch.py --ingest <tmp>/tl-batch-<N>.json --map <tmp>/tl-batch.json
   （按 row_key 归并变体 → specs/008/results/queries/termonline-all/<safe_key>.json，
     schema 与 cnki_query 一致；raw 留空，note 记各库 totalRecords）
4) 审计：python tools/term_audit.py（四态刷新，报告落 specs/008/results/）
5) 裁定登记：只报告不修改；修正走裁定 → Edit 两登记册（五列，禁维基）→ ci-hui-biao 看齐
6) 门禁：python tools/check_terms.py && python tools/check_all.py；提交（中文一行信息）
```

## 护栏

* 礼貌抓取：批内 ≥5s；批间自然间隔；单批 ≤12 词；遇「3 库全 0」形态先判限流
  （停 60-120s 重试该批），再判会话失效。
* 会话失效处置：浏览器打开 https://www.termonline.cn/ ，由**用户人工登录**
  （手机号+验证码/密码）；登录后 localStorage 密文即可复用，无需导出。
* 核验器只报告不修改；凭证 JSON 一律 `*.tmp + os.replace` 原子写；error 不臆造。
* 池批次（--pool）词量大，按字母/频次分片跑，节奏同上。

## 通道对比（2026-10-28 终态）

| 通道 | 凭据 | 状态 |
| ---- | ---- | ---- |
| termonline-standard（standardSearch） | 匿名 | 可用（GB 标准库，哲学覆盖低） |
| termonline-all（allSearch，本契约） | 浏览器登录会话 | **可用（主力，哲学覆盖高）** |
| youdao-aux | 匿名 | 可用（辅助参考档，不作依据） |
| cnki-dict | TLS 反爬未破 | 插件位保留 |
| zgbk / ncpssd | 签名/会话参数 | 插件位保留（机制存 execution-log） |

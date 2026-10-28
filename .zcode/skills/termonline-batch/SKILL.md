---
name: termonline-batch
description: SEP-CN 术语在线「审定名词库」批量查证全流程——浏览器通道跑批、凭证落盘、四态审计、译名裁定登记与门禁提交。当用户说「术语跑批」「查证下一批」「审定库查证」「术语在线查证」「008 术语战役」「池裁定」「术语批次」或要求继续 specs/008 术语战役时用本技能。
---

# 术语在线审定库·批量查证全流程（specs/008）

**适用**：D:\SEP-CN 仓库。法律依据：ADR-0012（译名依据优先级=知网系权威源→权威译本→学界惯例，**禁维基**）。
**权威文档**（冲突时以此为准）：`specs/008-terminology-campaign/contracts/browser-channel.md`（S.O.P.）、`specs/008-terminology-campaign/session-handoff.md`（认领与状态）、`specs/008-terminology-campaign/execution-log.md`（机制记录）。

## 0. 开工三件事

1. `git pull --rebase` + `git log --oneline -3`（并行会话多，先核基点）；
2. 在 `session-handoff.md`「执行认领」节登记本批次认领（格式见卡内说明）；
3. 核对工具在位：`tools/tl_browser_batch.py`、`tools/term_audit.py`、`tools/check_terms.py`。

## 1. 通道原理（30 秒读懂）

审定库 `allSearch` 的有效凭据是**真实浏览器上下文**：应用前端发送 `X-Access-Token`（localStorage `TERMONLINE__PRODUCTION__3.1.7__TOKEN__` 的 AES-CBC-PKCS7 密文解出的 JWT），且请求必须发自真实页面（Python 直连带同值 JWT 会被静默降级为全库 0）。cookie 会话短 TTL（约半小时），不可单独依赖。

**响应形态判别（贯穿全程）**：
- 正常 = 4 个库且总数不全为 0（或 4 库真查无）；
- **降级 = 3 库全 0**（限流/会话未激活）——绝不可落凭证当「查无」。

## 2. 标准批次循环（每批 8 词）

### 2.1 产清单

```bash
python tools/tl_browser_batch.py --emit --out "$TEMP/tl-batch.json"          # 登记册全量（增量无需担心，ingest 幂等覆盖）
python tools/tl_browser_batch.py --emit --pool --out "$TEMP/tl-pool.json"    # 候选池 new 条目（大，按需切片）
```

### 2.2 浏览器跑批

先加载 `browser-use:control-browser` 技能，打开 `https://www.termonline.cn/`（已有登录态则直接用；**无登录态→请用户人工登录**，不要索要密码/token）。

**每批执行下面的模板**（只需改 `OFFSET`/`SIZE`/两个文件路径；每批前必 reload；批内相邻请求 sleep ≥10000ms）：

```js
// 前置：browser-use bootstrap + browser.tabs.list() 找 termonline 标签页 + tabs.get 绑定
await tab.reload();
await tab.playwright.waitForLoadState({ state: "domcontentloaded" });
await tab.playwright.waitForTimeout(8000);
const fs = await import("node:fs");
const { createDecipheriv } = await import("node:crypto");
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const batch = JSON.parse(fs.readFileSync("C:/Users/<用户>/AppData/Local/Temp/tl-batch.json", "utf8"));
const offset = 0, SIZE = 8;                       // ← 每批改这里
const items = batch.items.slice(offset, offset + SIZE);
const out = [], summary = [];
for (const it of items) {
  const cipher = await tab.playwright.evaluate(() => localStorage.getItem("TERMONLINE__PRODUCTION__3.1.7__TOKEN__"));
  const d = createDecipheriv("aes-128-cbc", "_11111000001111@", "@11111000001001_");
  const jwt = JSON.parse(d.update(cipher, "base64", "utf8") + d.final("utf8")).value;
  const r = await tab.playwright.evaluate(async (args) => {
    const [term, token] = args;
    const url = "https://api.termonline.cn/main-serve/business/tm/tmWord/allSearch?term=" + encodeURIComponent(term) + "&match=2&sources=&pubYears=&pageSize=20&pageNo=1&baseId=1";
    try {
      const resp = await fetch(url, { headers: { "X-Access-Token": token }, credentials: "include" });
      const j = await resp.json();
      const srs = (j.result && j.result.searchResult) || [];
      const totals = srs.map(s => s.result.totalRecords);
      const ok = totals.some(x => x > 0);
      return { term, status: ok ? "ok" : (srs.length >= 4 ? "empty" : "error"),
        error: ok || srs.length >= 4 ? null : "degraded shape (3-db all-zero)",
        dbs: srs.map(s => ({ db: s.id, total: (s.result && s.result.totalRecords) || 0,
          words: (((s.result && s.result.tmWordList) || [])).slice(0, 12).map(w => ({
            cn: w.cn, en: w.en, source: w.source, wordNumber: w.wordNumber,
            subjectFullName: w.subjectFullName, subjectName: w.subjectName,
            publishYear: w.publishYear, definition: (w.definition || "").slice(0, 100) })) })) };
    } catch (e) { return { term, status: "error", dbs: [], error: String(e) }; }
  }, [it.display, jwt]);
  r.row_key = it.row_key;
  out.push(r);
  summary.push(it.display + " : " + r.status + " : " + (r.dbs || []).map(x => x.total).join("/"));
  await sleep(10000);
}
fs.writeFileSync("C:/Users/<用户>/AppData/Local/Temp/tl-batch-<OFFSET>.json", JSON.stringify({ results: out }, null, 1));
nodeRepl.write("batch offset=" + offset + " n=" + out.length + "\n" + summary.join("\n"));
```

### 2.3 限流处置

- 摘要出现整批 `0/0/0`（3 库形）→ **立即停**，等 5 分钟后 reload 重试该批；连续两次降级则再等 10 分钟。
- 单条 `error` → 记下词，冷却后重跑该批（ingest 幂等覆盖，无需特殊处理）。
- 节奏红线：批内 ≥10s、批间 ≥4 分钟、单批 ≤8 词。**宁可慢，不可假空**。

### 2.4 落凭证 + 审计

```bash
python tools/tl_browser_batch.py --ingest "$TEMP/tl-batch-<OFFSET>.json" --map "$TEMP/tl-batch.json"
python tools/term_audit.py     # 四态报告落 specs/008/results/audit-<日期>.md/json
```

每 4-5 批提交一次凭证（`git add specs/008-terminology-campaign/results/ && git commit`，中文一行信息）。

## 3. 裁定登记（审计报告出来后）

原则（ADR-0012）：**只采「termonline-all（审定库）」且学科语境（subjectFullName/定义）正确的命中**做主译变更；
- youdao-aux 辅助档**不作变更依据**（人名音译差异一律保留现译）；
- 跨学科同名（warrant→认股权证、mechanism→机构、imposition→组版等）保留原译；
- 审定命中是下位词（如 confirmation theory 对「贝叶斯验证理论」）不改，只在日志记一笔；
- match=2 模糊池污染词（含 ibn/the 的查询返回巨型同名结果集）需 `match=1` 精确补查后再裁定。

变更操作：Edit `yi-zhe-shuo-ming.md` / `ren-ming-biao.md`（五列：新主译 + 旧形降为「亦作"…"」+ 依据列写「审定名词库（termonline-all·库名，日期 浏览器通道凭证）」+ 裁定日期）→ `qian-yan/ci-hui-biao.md` 弱势方向同步看齐 → 门禁 → 提交。

## 4. 门禁与提交

```bash
python tools/check_terms.py && python tools/check_all.py     # 必须全绿
git add <只挑本批次相关文件> && git commit -m "008 审定库跑批…（中文一行）"
```

## 5. 坑清单（前人踩实，复用勿重推）

1. **fetch 必须写在 `tab.playwright.evaluate` 函数体内**——node REPL 内核没有 fetch（报 `fetch is not defined`）。
2. **evaluate 必须传函数对象 + arg 参数**——传字符串函数体不会被调用（静默返回 `{}`）。
3. **JWT 明文不落盘不入库不入日志**——node 侧 `crypto` 解密后经 evaluate 参数注入页面即用即弃；密文缓存文件只放 %TEMP%。
4. **批次原始 JSON 由 node 直写 %TEMP% 文件、nodeRepl 只回批摘要**——几十批的原始 JSON 会撑爆会话上下文。
5. **API 库 id 是 32 位十六进制串**（…0006），落凭证前经 `tl_browser_batch._db_name` 折算（int(id,16)）查库名。
6. **降级形态绝不 ingest**（工具会把降级记 error，但摘要里要先人工盯一眼）。
7. 写登记册/词汇表一律用 Edit/Write 工具，**禁 bash heredoc**（中文与转义会被损坏）。
8. 只 stage 本批次相关文件；提交后 `git log --oneline -2 -- <文件>` 核实未被并行会话卷入。

// specs/011 术语在线批量爬虫（浏览器内 fetch 版，断点续爬）
// 用法（node_repl 内）：import { runBatch } from "<本文件 URL>";
//   await runBatch(tab, offset, n)  → 跑 [offset, offset+n) 词，JSONL 增量落盘
import fs from "node:fs";

const TEMPO = process.env.TEMP || "C:/Users/ykla/AppData/Local/Temp";
const LIST = TEMPO + "/tl-batch-011c.json";
const OUTJ = TEMPO + "/tl-batch-011-results.jsonl";
const TOKEN_KEY = "TERMONLINE__PRODUCTION__3.1.7__TOKEN__";

export function loadList() {
  return JSON.parse(fs.readFileSync(LIST, "utf8")).items;
}

export function doneTerms() {
  if (!fs.existsSync(OUTJ)) return new Set();
  const s = new Set();
  for (const l of fs.readFileSync(OUTJ, "utf8").split("\n")) {
    if (!l.trim()) continue;
    try { s.add(JSON.parse(l).term); } catch {}
  }
  return s;
}

export function nextOffset(items, done) {
  for (let i = 0; i < items.length; i++) {
    if (!done.has(items[i].display)) return i;
  }
  return items.length;
}

export async function getToken(tab) {
  const cipher = await tab.playwright.evaluate(
    () => localStorage.getItem("TERMONLINE__PRODUCTION__3.1.7__TOKEN__"),
  );
  const { createDecipheriv } = await import("node:crypto");
  const d = createDecipheriv("aes-128-cbc", "_11111000001111@", "@11111000001001_");
  return JSON.parse(d.update(cipher, "base64", "utf8") + d.final("utf8")).value;
}

export async function fetchOne(tab, jwt, term) {
  return tab.playwright.evaluate(async (args) => {
    const [term, token] = args;
    const url = "https://api.termonline.cn/main-serve/business/tm/tmWord/allSearch?term="
      + encodeURIComponent(term) + "&match=2&sources=&pubYears=&pageSize=20&pageNo=1&baseId=1";
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
  }, [term, jwt]);
}

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// tab 由调用方绑定后传入（node_repl 每次调用是新内核，tab 在调用内取得后传入本函数）
export async function runBatch(tab, offset, n) {
  const items = loadList();
  const done = doneTerms();
  const slice = [];
  let i = offset;
  while (i < items.length && slice.length < n) {
    if (!done.has(items[i].display)) slice.push(items[i]);
    i++;
  }
  const jwt = await getToken(tab);
  const out = [], summary = [];
  for (const it of slice) {
    const r = await fetchOne(tab, jwt, it.display);
    r.row_key = it.row_key;
    out.push(r);
    fs.appendFileSync(OUTJ, JSON.stringify(r) + "\n");
    summary.push(it.display + " : " + r.status + " : " + (r.dbs || []).map(x => x.total).join("/"));
    await sleep(10000);
  }
  return { ran: out.length, nextOffset: i, remaining: items.length - i, summary };
}

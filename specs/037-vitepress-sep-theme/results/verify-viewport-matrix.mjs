// 多档视口适配矩阵验证（specs/037 2026-11-24）。用户清单：
// 1080p / 1.5×（缩放屏）/ 2K / 2.5× / 4K / 带鱼屏 / iPad 全系。
// DPR 与系统缩放的本质是 CSS 视口缩水，故直接按 CSS 视口量测：
//   1080p@1.0=1920、1080p@1.5=1280、2K@1.0=2560、2K@1.5=1707、
//   4K@2.5=1536、4K@1.0=3840、带鱼 3440/5120、
//   iPad Pro 13 横 1366 / Pro 11 横 1194 / Pro 13 竖 1024 / Pro 11 竖 834 / mini 竖 744。
// 断言：正文列宽落档（1200 封顶 / 窄视口回退正文区）＋正文列左缘 ≥ 侧栏让位宽
// （不与 fixed 侧栏重叠）＋iPad 竖屏走移动布局满宽。
// 前置：Chrome headless --remote-debugging-port=9222；构建产物已在 dist-ad。
// 用法：bun verify-viewport-matrix.mjs

const { spawn } = await import('node:child_process')
const fs = await import('node:fs')

const REPO = 'C:/Users/ykla/Documents/SEP-CN'
const cssFile = fs.readdirSync(`${REPO}/.vitepress/dist-ad/assets`).find((f) => f.startsWith('style'))

const prev = spawn('bun', ['--bun', 'x', 'vitepress', 'preview', REPO, '--port', '4199'], {
  cwd: REPO,
  env: { ...process.env, SEP_SHARD: 'ad' },
  stdio: 'ignore',
  shell: true,
})
process.on('exit', () => { try { prev.kill() } catch {} })

let ok0 = false
for (let i = 0; i < 30 && !ok0; i++) {
  try { if ((await fetch(`http://localhost:4199/assets/${cssFile}`)).status === 200) ok0 = true } catch {}
  if (!ok0) await new Promise((r) => setTimeout(r, 1000))
}
if (!ok0) { console.log('[FAIL] preview CSS 不可达'); process.exit(1) }

const list = await (await fetch('http://127.0.0.1:9222/json/list')).json()
const page = list.find((t) => t.type === 'page')
if (!page) { console.log('[FAIL] no page target'); process.exit(1) }
const ws = new WebSocket(page.webSocketDebuggerUrl)
let id = 0
const pending = new Map()
ws.addEventListener('message', (ev) => {
  const msg = JSON.parse(ev.data)
  if (msg.id && pending.has(msg.id)) {
    const { res, rej } = pending.get(msg.id)
    pending.delete(msg.id)
    msg.error ? rej(new Error(JSON.stringify(msg.error))) : res(msg.result)
  }
})
const send = (method, params = {}) =>
  new Promise((res, rej) => {
    const i = ++id
    pending.set(i, { res, rej })
    ws.send(JSON.stringify({ id: i, method, params }))
  })
await new Promise((r) => ws.addEventListener('open', r, { once: true }))
await send('Page.enable')
await send('Runtime.enable')

const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
let fails = 0
function ok(cond, label) {
  console.log((cond ? '[OK ] ' : '[FAIL] ') + label)
  if (!cond) fails++
}
async function evaluate(expr) {
  const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true })
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || 'evaluate error')
  return r.result.value
}
let VW = 1920, VH = 1080
async function viewport(w, h) {
  VW = w; VH = h
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false })
}
async function goto(url) {
  await send('Page.navigate', { url })
  await sleep(2500)
  await send('Emulation.setDeviceMetricsOverride', { width: VW, height: VH, deviceScaleFactor: 1, mobile: false })
  await sleep(800)
  for (let i = 0; i < 40; i++) {
    if (await evaluate('globalThis.__VITEPRESS__ === true')) break
    await sleep(200)
  }
  await sleep(400)
}
const RECT = `JSON.stringify((() => {
  const d = document.querySelector('.VPDoc .vp-doc')
  if (!d) return { w: -1, l: -1 }
  const r = d.getBoundingClientRect()
  return { w: Math.round(r.width), l: Math.round(r.left) }
})())`

const BASE = 'http://localhost:4199'
await goto(BASE + '/a/abduction')

/** w=视口宽；doc=期望正文列（[min,max] 或 'mobile'）；side=期望侧栏让位宽 */
const CASES = [
  { w: 1920, h: 1080, name: '1080p@1.0', doc: [1200, 1200], side: 272 },
  { w: 1280, h: 720, name: '1080p@1.5（缩放屏）', doc: [600, 900], side: 224 },
  { w: 1707, h: 960, name: '2K@1.5（缩放屏，≥1500 归大屏档）', doc: [900, 1240], side: 272 },
  { w: 2560, h: 1440, name: '2K@1.0', doc: [1200, 1200], side: 272 },
  { w: 1536, h: 864, name: '4K@2.5（缩放屏，≥1500 归大屏档）', doc: [800, 1160], side: 272 },
  { w: 3840, h: 2160, name: '4K@1.0', doc: [1200, 1200], side: 272 },
  { w: 3440, h: 1440, name: '带鱼屏 3440×1440', doc: [1200, 1200], side: 272 },
  { w: 5120, h: 1440, name: '超宽带鱼 5120×1440', doc: [1200, 1200], side: 272 },
  { w: 1366, h: 1024, name: 'iPad Pro 13 横（1200–1499 档）', doc: [650, 1000], side: 224 },
  { w: 1194, h: 834, name: 'iPad Pro 11 横', doc: [550, 900], side: 192 },
  { w: 1024, h: 1366, name: 'iPad Pro 13 竖', doc: [500, 820], side: 192 },
  { w: 834, h: 1194, name: 'iPad Pro 11 竖（≤959 移动布局）', doc: 'mobile', side: null },
  { w: 744, h: 1133, name: 'iPad mini 竖（移动布局）', doc: 'mobile', side: null },
]

for (const c of CASES) {
  await viewport(c.w, c.h)
  const r = JSON.parse(await evaluate(RECT))
  const left = await evaluate(`Math.round(document.querySelector('.VPContent').getBoundingClientRect().left)`)
  const pl = await evaluate(`Math.round(parseFloat(getComputedStyle(document.querySelector('.VPContent')).paddingLeft))`)
  if (c.doc === 'mobile') {
    ok(r.w >= c.w - 160, `${c.name}：正文列 ${r.w}（移动布局满宽 ≈ 视口−内边距，移动端总内距实测约 146px）`)
    ok(pl === 0, `${c.name}：VPContent 左让位 ${pl}（移动布局应为 0）`)
  } else {
    ok(r.w >= c.doc[0] && r.w <= c.doc[1], `${c.name}：正文列 ${r.w}（期望 ${c.doc[0]}–${c.doc[1]}）`)
    ok(r.l >= c.side, `${c.name}：正文列左缘 ${r.l} ≥ 侧栏让位 ${c.side}（不重叠）`)
    ok(pl === c.side, `${c.name}：VPContent padding-left ${pl}（期望 ${c.side}＝sidebar-width 档位）`)
  }
}

// —— 双语对照态不回归（1920 与 1194 各一轮） ——
await viewport(1920, 1080)
await goto(BASE + '/a/abduction?bili=1&layout=side&show=compare')
const side1920 = await evaluate(`Math.round(document.querySelector('.bili-doc > .vp-doc')?.getBoundingClientRect().width ?? -1)`)
ok(side1920 >= 650 && side1920 <= 730, `side 对照 1920 英文列 ${side1920}（不回归）`)
await viewport(1194, 834)
await goto(BASE + '/a/abduction?bili=1&layout=side&show=compare')
const side1194 = await evaluate(`Math.round(document.querySelector('.bili-doc > .vp-doc')?.getBoundingClientRect().width ?? -1)`)
ok(side1194 >= 300, `side 对照 1194（iPad 横）英文列 ${side1194}（半屏内可用）`)

console.log(fails ? `\n== ${fails} 项失败 ==` : '\n== 全部通过 ==')
try { prev.kill() } catch {}
process.exit(fails ? 1 : 0)

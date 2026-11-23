// 正文列加宽全链路验证（specs/037 2026-11-24）：单脚本内 spawn preview→
// 等 CSS→CDP 量测→杀 preview，规避 shell 后台任务的生命周期陷阱
// （后台化吞 cwd、任务清理连坐 preview、sirv 快照旧清单）。
// 前置：Chrome headless --remote-debugging-port=9222；构建产物已在 dist-ad。
// 用法：bun verify-width-full.mjs

const { spawn } = await import('node:child_process')
const fs = await import('node:fs')

const REPO = 'C:/Users/ykla/Documents/SEP-CN'
const cssFile = fs.readdirSync(`${REPO}/.vitepress/dist-ad/assets`).find((f) => f.startsWith('style'))
console.log('css file:', cssFile)

// —— spawn preview（SEP_SHARD=ad → config.outDir = dist-ad） ——
const prev = spawn('bun', ['--bun', 'x', 'vitepress', 'preview', REPO, '--port', '4199'], {
  cwd: REPO,
  env: { ...process.env, SEP_SHARD: 'ad' },
  stdio: 'ignore',
  shell: true,
})
process.on('exit', () => { try { prev.kill() } catch {} })

// 等 CSS 200（≤30s）
let ready = false
for (let i = 0; i < 30 && !ready; i++) {
  try {
    const r = await fetch(`http://localhost:4199/assets/${cssFile}`)
    if (r.status === 200) ready = true
  } catch {}
  if (!ok) await new Promise((r) => setTimeout(r, 1000))
}
if (!ok) { console.log('[FAIL] preview CSS 不可达'); process.exit(1) }
console.log('preview ready')

// —— CDP ——
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
let VW = 1920, VH = 900
async function viewport(w, h) {
  VW = w; VH = h
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: false })
}
async function goto(url) {
  await send('Page.navigate', { url })
  await sleep(2500)
  // specs/038 已知坑：导航后重发 override（MathJax 词条页钳制视口）
  await send('Emulation.setDeviceMetricsOverride', { width: VW, height: VH, deviceScaleFactor: 1, mobile: false })
  await sleep(800)
  // hydration 完成标志（app mount 前置设置）
  for (let i = 0; i < 40; i++) {
    if (await evaluate('globalThis.__VITEPRESS__ === true')) break
    await sleep(200)
  }
  await sleep(400)
}
const zhDocW = `Math.round(document.querySelector('.VPDoc .vp-doc')?.getBoundingClientRect().width ?? -1)`

// —— 普通态 ——
await viewport(1920, 900)
await goto('http://localhost:4199/a/abduction')
let w = await evaluate(zhDocW)
ok(w === 1200, `普通 1920×900 正文列 ${w}（期望 1200＝封顶）`)
w = await evaluate(`Math.round(document.querySelector('.VPDoc .content-container')?.getBoundingClientRect().width ?? -1)`)
ok(w === 1200, `普通 1920 content-container ${w}（期望 1200）`)

await viewport(1366, 768)
w = await evaluate(zhDocW)
// 1366 视口正文区物理宽 ≈ 视口−侧栏 272−aside 288−padding 64 ≈ 742 < 75vw＝1024，
// max-width 不撑破父容器——自然回退到正文区宽度（CSS 注释预写的行为）
ok(w >= 650 && w < 1024, `普通 1366×768 正文列 ${w}（75vw 装不下，自然回退到正文区宽度）`)

await viewport(2560, 1200)
w = await evaluate(zhDocW)
ok(w === 1200, `普通 2560×1200 正文列 ${w}（期望 1200＝封顶）`)

await viewport(390, 844)
w = await evaluate(zhDocW)
ok(w > 300, `手机 390×844 正文列 ${w}（满宽＝视口−内边距，>300）`)

// —— 双语态 ——
await viewport(1920, 900)
await goto('http://localhost:4199/a/abduction?bili=1&layout=side&show=compare')
w = await evaluate(zhDocW)
ok(w >= 650 && w <= 730, `side 对照 1920 中文列 ${w}（两栏同基准 37.5vw≈720，栏内 75%）`)
const enW = await evaluate(`Math.round(document.querySelector('.bili-doc > .vp-doc')?.getBoundingClientRect().width ?? -1)`)
ok(enW >= 650 && enW <= 730, `side 对照 1920 英文列 ${enW}（与中文对齐）`)

await goto('http://localhost:4199/a/abduction?bili=1&show=en')
const enFull = await evaluate(`Math.round(document.querySelector('.bili-doc > .vp-doc')?.getBoundingClientRect().width ?? -1)`)
ok(enFull === 1200, `仅英文 1920 英文列 ${enFull}（期望 1200＝封顶）`)

await goto('http://localhost:4199/a/abduction?bili=1&layout=stack&show=compare')
w = await evaluate(zhDocW)
ok(w === 1200, `stack 对照 1920 中文列 ${w}（期望 1200）`)

await goto('http://localhost:4199/a/abduction?bili=1&layout=inter&show=compare')
w = await evaluate(zhDocW)
ok(w === 1200, `交错态 1920 中文列 ${w}（期望 1200）`)

// —— 非词条页（非 has-aside 分支） ——
// 分片构建无 index.html（CI 才 cp README→index），用 mu-lu-s 代表非词条页
await viewport(1920, 900)
await goto('http://localhost:4199/mu-lu-s')
w = await evaluate(`Math.round(document.querySelector('.VPDoc .vp-doc')?.getBoundingClientRect().width ?? -1)`)
ok(w === 1200, `mu-lu-s（非词条页）1920 正文列 ${w}（期望 1200＝封顶）`)

console.log(fails ? `\n== ${fails} 项失败 ==` : '\n== 全部通过 ==')
try { prev.kill() } catch {}
process.exit(fails ? 1 : 0)

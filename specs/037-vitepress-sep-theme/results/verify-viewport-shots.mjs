// 极端视口截图留证（specs/037 2026-11-24）：spawn preview→CDP 逐视口截图→kill。
// 前置：Chrome headless --remote-debugging-port=9222；构建产物已在 dist-ad。
// 用法：bun verify-viewport-shots.mjs

const { spawn } = await import('node:child_process')
const fs = await import('node:fs')

const REPO = 'C:/Users/ykla/Documents/SEP-CN'
const OUT = `${REPO}/specs/037-vitepress-sep-theme/results`
const cssFile = fs.readdirSync(`${REPO}/.vitepress/dist-ad/assets`).find((f) => f.startsWith('style'))

const prev = spawn('bun', ['--bun', 'x', 'vitepress', 'preview', REPO, '--port', '4199'], {
  cwd: REPO,
  env: { ...process.env, SEP_SHARD: 'ad' },
  stdio: 'ignore',
  shell: true,
})
process.on('exit', () => { try { prev.kill() } catch {} })
let ready = false
for (let i = 0; i < 30 && !ready; i++) {
  try { if ((await fetch(`http://localhost:4199/assets/${cssFile}`)).status === 200) ready = true } catch {}
  if (!ready) await new Promise((r) => setTimeout(r, 1000))
}
if (!ready) { console.log('[FAIL] preview CSS 不可达'); process.exit(1) }

const list = await (await fetch('http://127.0.0.1:9222/json/list')).json()
const page = list.find((t) => t.type === 'page')
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
const evaluate = async (e) =>
  (await send('Runtime.evaluate', { expression: e, returnByValue: true })).result?.value

// 留证统一用浅色（羊皮纸）：headless Chrome 跟随 Windows 深色偏好，
// 首轮四张全截成深色。VitePress 显式偏好的存储键是 vitepress-theme-appearance。
await send('Emulation.setEmulatedMedia', {
  features: [{ name: 'prefers-color-scheme', value: 'light' }],
})
await send('Page.navigate', { url: 'http://localhost:4199/a/abduction' })
await sleep(1500)
await evaluate("localStorage.setItem('vitepress-theme-appearance', 'light')")

const SHOTS = [
  { w: 1280, h: 900, url: '/a/abduction', name: 'shot-viewport-1280-1080p-150pct.png' },
  { w: 1920, h: 1080, url: '/a/abduction', name: 'shot-viewport-1920.png' },
  { w: 3440, h: 1440, url: '/a/abduction', name: 'shot-viewport-3440-ultrawide.png' },
  { w: 1366, h: 1024, url: '/a/abduction', name: 'shot-viewport-1366-ipad-pro-13-landscape.png' },
]
for (const s of SHOTS) {
  await send('Emulation.setDeviceMetricsOverride', { width: s.w, height: s.h, deviceScaleFactor: 1, mobile: false })
  await send('Page.navigate', { url: 'http://localhost:4199' + s.url })
  await sleep(2500)
  await send('Emulation.setDeviceMetricsOverride', { width: s.w, height: s.h, deviceScaleFactor: 1, mobile: false })
  for (let i = 0; i < 40; i++) {
    if (await evaluate('globalThis.__VITEPRESS__ === true')) break
    await sleep(200)
  }
  // 兜底：若仍落深色（存储键写入晚于本次加载），直接摘 .dark 类
  if (await evaluate("document.documentElement.classList.contains('dark')")) {
    await evaluate("document.documentElement.classList.remove('dark')")
  }
  await sleep(600)
  const dark = await evaluate("document.documentElement.classList.contains('dark')")
  const shot = await send('Page.captureScreenshot', { format: 'png' })
  fs.writeFileSync(`${OUT}/${s.name}`, Buffer.from(shot.data, 'base64'))
  console.log('saved', s.name, 'dark=' + dark)
}
try { prev.kill() } catch {}
// WebSocket 常连会吊住事件循环（首轮跑完四张后脚本不退出），显式收尾
try { ws.close() } catch {}
process.exit(0)

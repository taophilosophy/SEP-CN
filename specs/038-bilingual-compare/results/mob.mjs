// CDP 移动端真机视口截图/量测（Chrome headless 的 --window-size 有 526px 最小宽度，
// 真机 390 只能靠 Emulation.setDeviceMetricsOverride）。用法：
//   node mob.mjs <url> <out.png> [w] [h] [evalFile]
const url = process.argv[2]
const out = process.argv[3]
const W = +(process.argv[4] || 390)
const H = +(process.argv[5] || 844)
const evalFile = process.argv[6]
const MOBILE = process.argv[7] !== 'desktop'
const fs = await import('node:fs/promises')

const list = await (await fetch('http://127.0.0.1:9222/json/list')).json()
const page = list.find((t) => t.type === 'page')
if (!page) throw new Error('no page target')
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
await send('Emulation.setDeviceMetricsOverride', {
  width: W,
  height: H,
  deviceScaleFactor: 2,
  mobile: MOBILE,
})
await send('Page.navigate', { url })
// 等 load + 面板/英文载入（固定等待，够长即可）
await new Promise((r) => setTimeout(r, 9000))
if (evalFile) {
  const expr = await fs.readFile(evalFile, 'utf8')
  const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })
  console.log(JSON.stringify(r.result?.value ?? r, null, 1))
}
const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false })
await fs.writeFile(out, Buffer.from(shot.data, 'base64'))
console.log('saved', out)
ws.close()

// 语言切换器浏览器端验证（specs/037 2026-11-23）。前置：
//   ① preview 服务：bun --bun x vitepress preview <repo> --outDir .vitepress/dist-ad --port 4199
//   ② Chrome headless：--remote-debugging-port=9222
// 用法：bun verify-langswitch-browser.mjs <desktop|mobile>
// 桌面：配对页 flyout 可见→点 English→SPA 导航 /yuanwen/a/abduction（无整页刷新）→
//       lang=en→回程 /a/abduction；无配对页 /mu-lu-s 切换器 display:none。
// 移动：390×844 打开 nav screen，Translations 手风琴在无配对页隐藏。

const MODE = process.argv[2] || 'desktop'
const BASE = 'http://localhost:4199'

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
const W = MODE === 'desktop' ? 1440 : 390
const H = MODE === 'desktop' ? 900 : 844
// CDP mobile:true 会被 MathJax 钳制（specs/038 血泪），一律 mobile:false＋导航后重发 override
await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 2, mobile: false })

const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
let fails = 0
function ok(cond, label) {
  console.log((cond ? '[OK ] ' : '[FAIL] ') + label)
  if (!cond) fails++
}

async function evaluate(expr) {
  const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || 'evaluate error')
  return r.result.value
}
async function goto(pathname) {
  await send('Page.navigate', { url: BASE + pathname })
  await sleep(1200)
  // 等 hydration 完成（app div 有内容且 flyout 挂载）
  for (let i = 0; i < 40; i++) {
    if (await evaluate("!!document.querySelector('.VPNavBarTranslations')")) break
    await sleep(200)
  }
  // hydration 真完成标志（S() 开头置 __VITEPRESS__）：SSR DOM 立即有元素，
  // 直接 click 会落在无监听阶段（冷加载首页 >1.5s 实测）
  for (let i = 0; i < 50; i++) {
    if (await evaluate('globalThis.__VITEPRESS__ === true')) break
    await sleep(200)
  }
  await sleep(300)
}

if (MODE === 'desktop') {
  // ① 中文配对页：flyout 可见 + SSR href 正确
  await goto('/a/abduction')
  const vis = await evaluate(`(() => {
    const el = document.querySelector('.VPNavBarTranslations')
    if (!el) return { mounted: false }
    const r = el.getBoundingClientRect(), s = getComputedStyle(el)
    return { mounted: true, display: s.display, w: r.width, h: r.height }
  })()`)
  ok(vis.mounted && vis.display !== 'none' && vis.w > 0, `配对页切换器可见（display=${vis.display} w=${vis.w}）`)
  const href = await evaluate(`document.querySelector('.VPNavBarTranslations a[hreflang="en"]')?.getAttribute('href')`)
  ok(href === '/yuanwen/a/abduction', `SSR/hydration href = ${href}`)

  // ② 点击 English → SPA 导航（window 标记存活 ⇒ 无整页刷新）
  await evaluate('window.__NAVTEST__ = 1')
  await evaluate(`document.querySelector('.VPNavBarTranslations a[hreflang="en"]').click()`)
  let arrived = false
  for (let i = 0; i < 30; i++) {
    const p = await evaluate('location.pathname')
    if (p === '/yuanwen/a/abduction') { arrived = true; break }
    await sleep(200)
  }
  ok(arrived, '点击 English 后到达 /yuanwen/a/abduction')
  const spa = await evaluate('window.__NAVTEST__')
  ok(spa === 1, 'window 标记存活 ⇒ SPA 导航（无整页刷新）')
  ok((await evaluate('document.documentElement.lang')) === 'en', '客户端 html lang = en')

  // ③ 英文页回程
  const back = await evaluate(`document.querySelector('.VPNavBarTranslations a[hreflang="zh-CN"]')?.getAttribute('href')`)
  ok(back === '/a/abduction', `英文页回程 href = ${back}`)
  await evaluate('window.__NAVTEST__ = 1')
  await evaluate(`document.querySelector('.VPNavBarTranslations a[hreflang="zh-CN"]').click()`)
  let backArrived = false
  for (let i = 0; i < 30; i++) {
    if ((await evaluate('location.pathname')) === '/a/abduction') { backArrived = true; break }
    await sleep(200)
  }
  ok(backArrived && (await evaluate('window.__NAVTEST__')) === 1, '回程 SPA 导航到 /a/abduction')

  // ④ 无配对页：切换器 DOM 存在但 display:none
  await goto('/mu-lu-s')
  const hid = await evaluate(`(() => {
    const el = document.querySelector('.VPNavBarTranslations')
    if (!el) return { mounted: false }
    const r = el.getBoundingClientRect(), s = getComputedStyle(el)
    return { mounted: true, display: s.display, w: r.width, cls: document.querySelector('.Layout')?.className }
  })()`)
  ok(hid.mounted && hid.display === 'none' && hid.w === 0, `无配对页切换器隐藏（display=${hid.display} w=${hid.w}）`)
  ok(String(hid.cls).includes('no-langswitch-page'), 'Layout 根含 no-langswitch-page')
} else {
  // 移动端：无配对页开 nav screen（窄屏 VPNavBar 仍可达，入口 hamburger）
  await goto('/mu-lu-s')
  await sleep(1500)
  await evaluate(`[...document.querySelectorAll('.VPNavBarHamburger')].filter(b => b.getBoundingClientRect().width > 0)[0]?.click()`)
  await sleep(900)
  const m = await evaluate(`(() => {
    const acc = document.querySelector('.VPNavScreenTranslations')
    if (!acc) return { mounted: false }
    const s = getComputedStyle(acc)
    return { mounted: true, display: s.display, screenOpen: !!document.querySelector('.VPNavScreen') }
  })()`)
  ok(m.mounted && m.screenOpen, `nav screen 已打开且手风琴挂载（open=${m.screenOpen}）`)
  ok(m.display === 'none', `无配对页移动端手风琴隐藏（display=${m.display}）`)

  // 配对页手风琴应可见
  await goto('/a/abduction')
  await evaluate(`[...document.querySelectorAll('.VPNavBarHamburger')].filter(b => b.getBoundingClientRect().width > 0)[0]?.click()`)
  await sleep(900)
  const m2 = await evaluate(`(() => {
    const acc = document.querySelector('.VPNavScreenTranslations')
    if (!acc) return { mounted: false }
    const r = acc.getBoundingClientRect(), s = getComputedStyle(acc)
    return { mounted: true, display: s.display, h: r.height }
  })()`)
  ok(m2.mounted && m2.display !== 'none' && m2.h > 0, `配对页移动端手风琴可见（h=${m2.h}）`)
}

console.log(fails ? `\n== ${fails} 项失败 ==` : '\n== 全部通过 ==')
process.exit(fails ? 1 : 0)

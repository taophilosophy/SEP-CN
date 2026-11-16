// 主题全量矩阵探针（2026-11-16）：视口 × 页面 × 对照三态 × 暗色，收 DOM 度量与关键截图。
// 复用 specs/038/results/mob.mjs 的 CDP 法（Chrome headless --window-size 最小 526px，
// 真机视口一律 Emulation.setDeviceMetricsOverride）。
//   node full-matrix.mjs <out.json> [shotPrefix]
const OUT = process.argv[2] || 'full-matrix.json'
const SHOT_DIR = 'C:/Users/ykla/Documents/SEP-CN/specs/038-bilingual-compare/results'
const fs = await import('node:fs/promises')
await fs.mkdir(SHOT_DIR, { recursive: true })

// 每视口新开一个标签页：模拟状态按 target 隔离，避免上一个视口的窗口状态
// 把小视口钳制成 524（Chrome 157 实测，复用同一 target 会污染）
async function newTab() {
  const r = await fetch('http://127.0.0.1:9222/json/new?url=about:blank', { method: 'PUT' })
  return r.json()
}
const closeTab = (id) => fetch(`http://127.0.0.1:9222/json/close/${id}`)

let ws, id = 0, pending = new Map()
function onMsg(ev) {
  const msg = JSON.parse(ev.data)
  if (msg.id && pending.has(msg.id)) {
    const { res, rej } = pending.get(msg.id)
    pending.delete(msg.id)
    msg.error ? rej(new Error(JSON.stringify(msg.error))) : res(msg.result)
  }
}
const send = (method, params = {}) =>
  new Promise((res, rej) => {
    const i = ++id
    pending.set(i, { res, rej })
    ws.send(JSON.stringify({ id: i, method, params }))
  })
async function attach(tab) {
  ws = new WebSocket(tab.webSocketDebuggerUrl)
  ws.addEventListener('message', onMsg)
  await new Promise((r) => ws.addEventListener('open', r, { once: true }))
  id = 0
  pending = new Map()
  await send('Page.enable')
  await send('Runtime.enable')
}

const rect = (el) => {
  if (!el) return null
  const b = el.getBoundingClientRect()
  return [Math.round(b.x), Math.round(b.y), Math.round(b.width), Math.round(b.height)]
}
const vis = (el) => !!el && !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)

// 页内度量：结构存在性/坐标/溢出/字号/触达尺寸
const METRICS = `(() => {
  const out = {}
  const q = (s, r) => (r || document).querySelector(s)
  const rect = (el) => { if (!el) return null; const b = el.getBoundingClientRect(); return [Math.round(b.x), Math.round(b.y), Math.round(b.width), Math.round(b.height)] }
  const vis = (el) => !!el && !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
  out.vw = innerWidth; out.vh = innerHeight; out.dpr = devicePixelRatio
  out.hOverflow = document.documentElement.scrollWidth - innerWidth
  // 导航
  const nav = q('.VPNavBar'); const lnav = q('.VPLocalNav')
  out.nav = vis(nav) ? { rect: rect(nav) } : null
  out.localNav = vis(lnav) ? { rect: rect(lnav) } : null
  out.navTitle = { vis: vis(q('.VPNavBarTitle .title, .VPLocalNav .message')) }
  out.search = { vis: vis(q('.VPNavBarSearch')) }
  out.hamburger = { vis: vis(q('.VPNavBarHamburger, .VPLocalNav .menu')), rect: rect(q('.VPNavBarHamburger, .VPLocalNav .menu')) }
  out.sidebar = { vis: vis(q('.VPSidebar')), rect: rect(q('.VPSidebar')) }
  const aside = q('.vp-doc + aside, .VPContentDoc aside, aside')
  out.aside = vis(aside) ? { rect: rect(aside) } : null
  // 正文（对照态下 zh 根仍是 .vp-doc；bili-doc 只存在于英文面板内）
  const cc = q('.content-container') || q('.VPContent')
  out.contentContainer = rect(cc)
  const zhVp = q('.content-container .vp-doc')
  out.zhDoc = rect(zhVp)
  out.h1 = (q('h1') || {}).textContent?.trim().slice(0, 40) || null
  const p = q('.vp-doc p')
  out.zhFontPx = p ? getComputedStyle(p).fontSize : null
  // 数学（本站包裹为 span.math-tex > mjx-container；块级公式 mjx-container[display="true"]）
  const mjxD = q('mjx-container[display="true"]') || q('.math-display')
  if (mjxD) {
    const fs1 = getComputedStyle(mjxD).fontSize
    out.math = { rect: rect(mjxD), fontSize: fs1, innerW: Math.round(mjxD.scrollWidth), clipW: Math.round(mjxD.clientWidth), overflow: mjxD.scrollWidth - mjxD.clientWidth }
  }
  const mjxAny = q('mjx-container')
  out.mathInlineFs = mjxAny ? getComputedStyle(mjxAny).fontSize : null
  // 表格与代码块溢出（容器内滚动是合法形态，全页溢出才是 bug）
  const tw = [...document.querySelectorAll('.vp-doc table')].slice(0, 3).map(t => {
    const wrap = t.parentElement
    return { sw: wrap.scrollWidth, cw: wrap.clientWidth, need: wrap.scrollWidth > wrap.clientWidth + 1, pageOverflow: t.getBoundingClientRect().right > innerWidth + 1 }
  })
  if (tw.length) out.tables = tw
  const pres = [...document.querySelectorAll('.vp-doc pre')].slice(0, 4).map(p2 => ({ need: p2.scrollWidth > p2.clientWidth + 1, pageOverflow: p2.getBoundingClientRect().right > innerWidth + 1 }))
  if (pres.length) out.preBlocks = pres
  // 对照
  out.bodyClass = document.body.className
  const zhDoc = [...document.querySelectorAll('.bili-doc')].find(d => !d.closest('.bili-panel'))
  out.zhDoc = rect(zhDoc)
  const panel = q('.bili-panel')
  out.panel = vis(panel) ? { rect: rect(panel) } : null
  if (panel) {
    const enDoc = q('.bili-doc', panel)
    out.enDoc = rect(enDoc)
    out.enDocW = enDoc ? Math.round(enDoc.getBoundingClientRect().width) : 0
    out.enFontPx = enDoc ? getComputedStyle(enDoc).fontSize : null
    const bar = q('.bili-bar', panel)
    out.bar = rect(bar)
    out.barH = bar ? Math.round(bar.getBoundingClientRect().height) : 0
    out.barVar = getComputedStyle(document.body).getPropertyValue('--bili-bar-h').trim()
    out.barBtnMin = Math.min(...[...panel.querySelectorAll('.bili-bar button, .bili-bar .bili-act')].map(b => Math.min(b.getBoundingClientRect().width, b.getBoundingClientRect().height)))
    out.barBtns = [...panel.querySelectorAll('.bili-bar button')].length
    out.progress = (q('.bili-progress', panel) || {}).textContent || null
  }
  // 交错块
  const eb = document.querySelectorAll('.bili-en-block')
  if (eb.length) out.enBlocks = eb.length
  const lbl = q('.bili-en-label')
  out.enLabel = vis(lbl) ? { rect: rect(lbl) } : null
  // 入口按钮（对照开启时应隐藏；关闭时桌面在导航槽位、窄屏是 Teleport 浮窗）
  const tw2 = q('.bili-toggle-wrap')
  out.entry = vis(tw2) ? { rect: rect(tw2), fixed: getComputedStyle(tw2).position } : null
  // 页脚
  const foot = q('footer, .VPFooter')
  out.footer = vis(foot) ? { rect: rect(foot) } : null
  out.dark = document.documentElement.classList.contains('dark')
  const vpwd = q('.VPContent, main')
  out.bg = getComputedStyle(document.body).backgroundColor
  return out
})()`

const VIEWPORTS = [
  // 桌面：720p / 1080p / 2K@150%（2560 物理） / 2K 原生 / 4K 原生
  { k: '1280x720', w: 1280, h: 720, dpr: 1, mobile: false },
  { k: '1920x1080', w: 1920, h: 1080, dpr: 1, mobile: false },
  { k: '1707x960', w: 1707, h: 960, dpr: 1.25, mobile: false }, // 2K@150% 缩放的 CSS 视口
  { k: '2560x1440', w: 2560, h: 1440, dpr: 1, mobile: false },
  { k: '3840x2160', w: 3840, h: 2160, dpr: 1, mobile: false },
  // iPad（最新款）：mini 7.9/A17 Pro、Air 11、Pro 13 竖横
  { k: 'ipad-mini-p', w: 744, h: 1133, dpr: 2, mobile: false },
  { k: 'ipad-air-p', w: 820, h: 1180, dpr: 2, mobile: false },
  { k: 'ipad-pro13-p', w: 1032, h: 1376, dpr: 2, mobile: false },
  { k: 'ipad-pro13-l', w: 1376, h: 1032, dpr: 2, mobile: false },
  { k: 'ipad-air-l', w: 1180, h: 820, dpr: 2, mobile: false },
  // iPhone（最新款）＋SE
  { k: 'iphone-se', w: 375, h: 667, dpr: 2, mobile: false },
  { k: 'iphone-15', w: 393, h: 852, dpr: 3, mobile: false },
  { k: 'iphone-16pro', w: 402, h: 874, dpr: 3, mobile: false },
  { k: 'iphone-16promax', w: 440, h: 956, dpr: 3, mobile: false },
  // 小米/安卓旗舰（CSS 视口按 1080p 物理 × 2.75-3 DPR 近似）
  { k: 'android-360', w: 360, h: 800, dpr: 3, mobile: false },
  { k: 'xiaomi-15', w: 393, h: 873, dpr: 3, mobile: false },
  { k: 'xiaomi-ultra', w: 412, h: 915, dpr: 3, mobile: false },
  { k: 'android-430', w: 430, h: 932, dpr: 3, mobile: false },
  { k: 'phone-landscape', w: 852, h: 393, dpr: 3, mobile: false },
]

const BASE = 'http://127.0.0.1:81'
const WAIT = 3800 // dev 预热后单页载入
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
let curV = VIEWPORTS[0]

const results = { captured: new Date().toISOString(), viewports: {} }
const isNarrow = (v) => v.w <= 959
const shotSteps = new Set([
  '1280x720|compare', '1920x1080|compare', '2560x1440|compare', '3840x2160|compare',
  'ipad-pro13-p|compare', 'ipad-air-p|compare', 'ipad-mini-p|compare',
  'iphone-15|compare', 'iphone-15|inter', 'iphone-16promax|compare',
  'xiaomi-15|compare', 'android-360|compare', 'phone-landscape|compare',
  '3840x2160|zh', 'iphone-16promax|zh', 'xiaomi-15|zh',
  'iphone-15|dark-zh', 'iphone-15|dark-compare', '1280x720|dark-zh', '3840x2160|dark-compare',
  'iphone-16promax|enpage', '1280x720|axiom',
])

async function nav(url) {
  await send('Page.navigate', { url })
  await sleep(WAIT)
  // 导航会重置模拟视口（Chrome 157 实测 innerWidth 落回钳制值），载入后必须重发一次
  await send('Emulation.setDeviceMetricsOverride', { width: curV.w, height: curV.h, deviceScaleFactor: curV.dpr, mobile: curV.mobile })
  await sleep(700)
}
async function evalMetrics() {
  const r = await send('Runtime.evaluate', { expression: METRICS, returnByValue: true })
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.text)
  return r.result.value
}
async function shot(name) {
  // 合成 KeyboardEvent 的 isTrusted=false，Escape 处理器不认；Esc 一律走 CDP 派发
  const s = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false })
  await fs.writeFile(`${SHOT_DIR}/matrix-${name}.png`, Buffer.from(s.data, 'base64'))
}
async function escKey() {
  await send('Input.dispatchKeyEvent', { type: 'keyDown', key: 'Escape', code: 'Escape', windowsVirtualKeyCode: 27, nativeVirtualKeyCode: 27 })
  await send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'Escape', code: 'Escape', windowsVirtualKeyCode: 27, nativeVirtualKeyCode: 27 })
}

for (const v of VIEWPORTS) {
  curV = v
  const R = results.viewports[v.k] = { ...v }
  const tab = await newTab()
  await attach(tab)
  await send('Emulation.setDeviceMetricsOverride', { width: v.w, height: v.h, deviceScaleFactor: v.dpr, mobile: false })
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'light' }] })
  const narrow = isNarrow(v)

  const steps = []
  steps.push(['zh', `${BASE}/a/abstract-objects?bili=0`])
  if (v.w <= 1280) steps.push(['axiom', `${BASE}/a/axiom-choice?bili=0`])
  steps.push(['compare', `${BASE}/a/abstract-objects?bili=1&layout=side&show=compare`])
  steps.push(['inter', `${BASE}/a/abstract-objects?bili=1&layout=inter&show=compare`])
  if (['1280x720', '1920x1080', '3840x2160', 'iphone-15', 'xiaomi-15', 'ipad-pro13-p'].includes(v.k))
    steps.push(['enonly', `${BASE}/a/abstract-objects?bili=1&layout=side&show=en`])
  steps.push(['enpage', `${BASE}/yuanwen/a/abstract-objects`])
  if (['1280x720', '1920x1080', 'iphone-15', 'xiaomi-15', '3840x2160'].includes(v.k)) {
    steps.push(['dark-zh', `${BASE}/a/abstract-objects?bili=0`, true])
    if (v.k !== '1280x720' && v.k !== '1920x1080') steps.push(['dark-compare', `${BASE}/a/abstract-objects?bili=1&layout=side&show=compare`, true])
  }

  for (const [name, url, dark] of steps) {
    try {
      if (dark) await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'dark' }] })
      await nav(url)
      let m = await evalMetrics()
      m.step = name
      m.narrowExpected = narrow
      // Esc 残留检查：compare 态派发 Escape 后 body 类与正文宽度应复原
      if (name === 'compare') {
        await escKey()
        await sleep(600)
        const m2 = await evalMetrics()
        m.escBodyClass = m2.bodyClass
        m.escZhDoc = m2.zhDoc
        m.escPanel = m2.panel
        // Esc 之后重开对照，恢复面板给后续截图；esc 快照回贴到最终 m
        const esc = { escBodyClass: m.escBodyClass, escZhDoc: m.escZhDoc, escPanel: m.escPanel }
        await nav(`${BASE}/a/abstract-objects?bili=1&layout=side&show=compare`)
        m = await evalMetrics()
        Object.assign(m, esc)
        m.step = name
        m.narrowExpected = narrow
      }
      if (dark) await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'light' }] })
      R[name] = m // 先落盘，截图失败不丢度量
      if (shotSteps.has(`${v.k}|${name}`)) {
        try { await shot(`${v.k}-${name}`) } catch (e) { m.shotError = String(e) }
      }
      console.log(v.k, name, 'hOver=', m.hOverflow, 'panel=', m.panel ? 'open' : '-', 'esc=', m.escBodyClass ?? '')
    } catch (e) {
      R[name] = { error: String(e) }
      console.log(v.k, name, 'ERROR', String(e).slice(0, 120))
    }
  }
  await closeTab(tab.id)
}

await fs.writeFile(OUT, JSON.stringify(results, null, 1))
console.log('written', OUT)
ws.close()

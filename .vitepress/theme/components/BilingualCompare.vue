<script setup lang="ts">
// 中英比较界面（specs/038）：同页双栏（默认）＋段间交错精读，三态通用。
// 2026-11-16 重做：去 iframe（原 postMessage 跨窗口同步），英文原文 fetch 后注入
// 同页容器；视觉语汇取自 5000yan 文言/白话对照（英文侧=浅底附注块）。
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useData, withBase } from 'vitepress'
import {
  activeBlock,
  annotateBlocks,
  biliBlocks,
  blockByKey,
  clearSentenceMarks,
  clickableBlock,
  containingBlock,
  highlightSentence,
  interleavePlan,
  mapPoint,
  markActive,
  offsetInElement,
  pointEl,
  sentenceIndexAt,
} from '../bili-paragraph'
import { ensureMathJax } from '../mathjax-loader'

type Layout = 'side' | 'stack' | 'inter'
type Show = 'compare' | 'zh' | 'en'

const { page } = useData()
const enPath = computed(() => page.value.frontmatter?.enPath as string | undefined)
const hasLS = typeof localStorage !== 'undefined'

const panel = ref<HTMLElement | null>(null)
const host = ref<HTMLElement | null>(null)
const loading = ref(false)
const failed = ref(false)

// ---------------------------------------------------------------- 持久化 --
function ls(key: string, fallback: string): string {
  return hasLS ? localStorage.getItem(key) ?? fallback : fallback
}

const open = ref(false)
const layout = ref<Layout>((ls('bili-layout', 'side') as Layout) || 'side')
const show = ref<Show>((ls('bili-show', 'compare') as Show) || 'compare')
const sync = ref(true)
const hideSidebar = ref(hasLS && localStorage.getItem('hide-sidebar') === '1')
// 用户显式开/关后本会话不再自动恢复（dev 下 page 数据异步到达，enPath 稍后就位）
const userTouched = ref(false)

watch(
  [enPath],
  () => {
    if (!hasLS) return
    if (!userTouched.value) open.value = localStorage.getItem('bili-open') === '1' && !!enPath.value
  },
  { immediate: true, flush: 'post' },
)

// 链接参数覆盖（便于分享对照链接与自动化验收）：?bili=0|1&layout=side|stack|inter&show=compare|zh|en
// presence 即接管，且不回写 localStorage（不污染读者自己的偏好）
const paramMode = ref(false)
function applyUrlParams() {
  if (typeof location === 'undefined') return
  const q = new URLSearchParams(location.search)
  if (!q.has('bili') && !q.has('layout') && !q.has('show')) return
  paramMode.value = true
  userTouched.value = true // 阻止 enPath 到达时的 localStorage 恢复覆盖链接参数
  if (q.has('bili')) open.value = q.get('bili') !== '0'
  const l = q.get('layout') as Layout | null
  if (l && ['side', 'stack', 'inter'].includes(l)) layout.value = l
  const s = q.get('show') as Show | null
  if (s && ['compare', 'zh', 'en'].includes(s)) show.value = s
}

onMounted(() => {
  sync.value = localStorage.getItem('bili-sync') !== '0'
  applyUrlParams()
  refreshClasses()
})

watch(open, (v) => {
  userTouched.value = true
  if (hasLS && !paramMode.value) localStorage.setItem('bili-open', v ? '1' : '0')
})
watch(layout, (v) => {
  if (hasLS && !paramMode.value) localStorage.setItem('bili-layout', v)
})
watch(show, (v) => {
  if (hasLS && !paramMode.value) localStorage.setItem('bili-show', v)
})
watch(sync, (v) => {
  if (hasLS) localStorage.setItem('bili-sync', v ? '1' : '0')
})
watch(hideSidebar, (v) => {
  if (hasLS) localStorage.setItem('hide-sidebar', v ? '1' : '0')
})

// 底部工具条形态：交错永远底栏；双栏在「仅中文」时也收成底栏（正文恢复全宽）
const bottomBar = computed(() => layout.value === 'inter' || show.value === 'zh')

/** body 上的状态类集中刷新（布局、三态、底栏、侧栏隐藏）。
    布局/三态类必须以「对照真的开着」为前提：这些类直接驱动 vp-compat.css
    里的中文栏让位规则，关闭面板后若残留 bili-side，正文会一直缩在左半屏
    （2026-11-16 Esc 走查实测）。hide-sidebar 独立于面板，不受此限。 */
function refreshClasses() {
  const on = open.value && !!enPath.value
  const b = document.body
  b.classList.toggle('bili-mode', on)
  b.classList.toggle('bili-side', on && layout.value === 'side')
  b.classList.toggle('bili-stack', on && layout.value === 'stack')
  b.classList.toggle('bili-inter', on && layout.value === 'inter')
  b.classList.toggle('bili-show-compare', on && show.value === 'compare')
  b.classList.toggle('bili-show-zh', on && show.value === 'zh')
  b.classList.toggle('bili-show-en', on && show.value === 'en')
  b.classList.toggle('bili-bottombar', on && bottomBar.value)
  b.classList.toggle('hide-sidebar', hideSidebar.value)
}
watch([open, layout, show, bottomBar, enPath], () => refreshClasses(), { flush: 'post' })

// ------------------------------------------------------------ 英文文档载入 --
let enDoc: HTMLElement | null = null // fetch 到的 .vp-doc（脱离文档，作为交错模式的克隆源）
let loadedFor = ''
let pending: AbortController | null = null

const enPageUrl = computed(() => {
  if (!enPath.value || typeof location === 'undefined') return ''
  return new URL(withBase(enPath.value), location.href).href
})

function rewriteEnDoc(root: HTMLElement, pageUrl: string) {
  root.querySelectorAll('script, style, link, noscript').forEach((n) => n.remove())
  // id 加 en- 前缀：中文页与原文页的脚注/锚点 id 可能同名，同页共存必须隔离
  root.querySelectorAll<HTMLElement>('[id]').forEach((el) => {
    el.id = 'en-' + el.id
  })
  root.querySelectorAll<HTMLAnchorElement>('a[href]').forEach((a) => {
    const href = a.getAttribute('href') || ''
    if (href.startsWith('#')) {
      a.setAttribute('href', '#en-' + href.slice(1))
    } else if (/^(https?:|mailto:|tel:)/i.test(href)) {
      a.target = '_blank'
      a.rel = 'noopener'
    } else {
      const u = new URL(href, pageUrl)
      a.setAttribute('href', u.pathname + u.search + u.hash)
    }
  })
  root.querySelectorAll<HTMLImageElement>('img[src]').forEach((img) => {
    const src = img.getAttribute('src') || ''
    if (/^(https?:|data:)/i.test(src)) return
    img.setAttribute('src', new URL(src, pageUrl).pathname)
  })
  annotateBlocks(root)
}

function typeset(el: HTMLElement) {
  if (!el.querySelector('.math-tex')) return
  ensureMathJax()
    .then((MJ) => {
      try {
        MJ.typesetClear?.([el])
      } catch {
        /* 清除失败忽略 */
      }
      return MJ.typesetPromise([el])
    })
    .catch(() => {})
}

/** dev 兜底：dev server 不预渲染页面（HTML 由 SPA 现渲染），fetch 只能拿到外壳，
    取不到 .vp-doc。改用同源隐藏 iframe 让英文页自行渲染后再取正文；构建态有
    静态 HTML，走 fetch 成功即不产生 iframe。 */
function loadViaIframe(url: string): Promise<HTMLElement> {
  return new Promise((resolve, reject) => {
    const frame = document.createElement('iframe')
    frame.setAttribute('aria-hidden', 'true')
    frame.style.cssText =
      'position:fixed;left:-9999px;top:0;width:1200px;height:900px;border:0;opacity:0;pointer-events:none'
    const finish = (fn: () => void) => {
      frame.remove()
      fn()
    }
    frame.addEventListener('load', () => {
      let tries = 0
      const poll = () => {
        const el = frame.contentDocument?.querySelector<HTMLElement>('.vp-doc')
        if (el) return finish(() => resolve(document.importNode(el, true) as HTMLElement))
        if (++tries > 120) return finish(() => reject(new Error('no .vp-doc')))
        setTimeout(poll, 100)
      }
      poll()
    })
    frame.addEventListener('error', () => finish(() => reject(new Error('iframe error'))))
    frame.src = url
    document.body.appendChild(frame)
  })
}

async function loadEn() {
  if (!enPath.value || loadedFor === page.value.relativePath) return
  loading.value = true
  failed.value = false
  pending?.abort()
  pending = new AbortController()
  const rel0 = page.value.relativePath
  try {
    let doc: HTMLElement | null = null
    try {
      const res = await fetch(enPageUrl.value, { signal: pending.signal })
      if (res.ok) {
        const parsed = new DOMParser().parseFromString(await res.text(), 'text/html')
        doc = parsed.querySelector<HTMLElement>('.vp-doc')
      }
    } catch (e: any) {
      if (e?.name === 'AbortError') throw e
    }
    if (!doc) doc = await loadViaIframe(enPageUrl.value)
    if (rel0 !== page.value.relativePath) return // 期间已切换词条
    rewriteEnDoc(doc, enPageUrl.value)
    enDoc = doc
    loadedFor = page.value.relativePath
    mountEnDoc()
    if (layout.value === 'inter') buildInterleave()
  } catch (e: any) {
    if (e?.name === 'AbortError') return
    failed.value = true
  } finally {
    loading.value = false
  }
}

/** 双栏模式：把英文 .vp-doc 挂进滚动容器 */
function mountEnDoc() {
  if (!host.value || !enDoc) return
  host.value.replaceChildren(enDoc)
  host.value.scrollTop = 0
  typeset(host.value)
  refreshEnPct()
  followZh(true)
}

// ------------------------------------------------------------ 段间交错构建 --
let interleaved: HTMLElement[] = []
let zhMarked: HTMLElement[] = []

function clearInterleave() {
  interleaved.forEach((n) => n.remove())
  interleaved = []
  zhMarked.forEach((n) => n.classList.remove('bili-zh-block'))
  zhMarked = []
}

function buildInterleave() {
  clearInterleave()
  const zhRoot = document.querySelector<HTMLElement>('.vp-doc')
  if (!zhRoot || !enDoc) return
  // 中文块打标（「仅英文」态据此隐藏中文侧）
  zhMarked = biliBlocks(zhRoot)
  zhMarked.forEach((n) => n.classList.add('bili-zh-block'))
  zhRoot.classList.add('bili-interleaved')

  for (const item of interleavePlan(zhRoot, enDoc)) {
    if (!item.after.isConnected) continue
    const wrap = document.createElement('div')
    wrap.className = 'bili-en-block' + (item.section ? ' bili-en-section' : '')
    wrap.setAttribute('data-bili-h', String(item.h))
    wrap.setAttribute('lang', 'en')
    if (item.section) {
      const label = document.createElement('div')
      label.className = 'bili-en-label'
      label.textContent = 'English · 对应区段'
      wrap.appendChild(label)
    }
    for (const node of item.en) wrap.appendChild(node.cloneNode(true))
    item.after.insertAdjacentElement('afterend', wrap)
    interleaved.push(wrap)
    typeset(wrap)
  }
}

watch([layout, show, open], () => {
  refreshClasses()
  if (!open.value || layout.value !== 'inter') {
    clearInterleave()
    return
  }
  if (enDoc) buildInterleave()
})

watch(
  () => page.value.relativePath,
  () => {
    // 路由切换：丢弃旧原文，按需重取（open 状态保持，符合「跟随上次选择」）
    clearInterleave()
    enDoc = null
    loadedFor = ''
    host.value?.replaceChildren()
    if (open.value && enPath.value) loadEn()
  },
  { flush: 'post' },
)

watch(
  [open, enPath],
  () => {
    if (!open.value || !enPath.value) {
      clearInterleave()
      return
    }
    loadEn()
  },
  { flush: 'post' },
)

// ---------------------------------------------------------------- 双向同步 --
// 中文为主：中文滚动驱动英文跟随；英文滚动只更新高亮与进度（双向互驱会振荡，
// 2026-10-31 实测裁定沿用）。三态与交错模式下不对英文栏做滚动驱动。
let lastKey = ''
let driveUntil = 0
let lastDrive = 0

function keyOf(pt: { h: number; b: number } | null): string {
  return pt ? pt.h + ':' + pt.b : ''
}

function scrollEnTo(h: number, b: number, soft: boolean) {
  if (!host.value || !enDoc) return
  const el = blockByKey(enDoc, h, b) || pointEl(enDoc, h, b)
  if (!el) return
  const delta = el.getBoundingClientRect().top - host.value.getBoundingClientRect().top
  const top = Math.max(0, host.value.scrollTop + delta - 24)
  host.value.scrollTo({ top, behavior: soft ? 'smooth' : 'auto' })
}

function followZh(force = false) {
  if (!open.value || layout.value === 'inter' || show.value === 'zh') return
  if (!force && (!sync.value || !enDoc || !host.value)) return
  const zhRoot = document.querySelector<HTMLElement>('.vp-doc')
  if (!zhRoot) return
  const el = activeBlock(zhRoot)
  if (!el) return
  markActive(zhRoot, el)
  const pt = mapPoint(zhRoot, el)
  if (!pt) return
  const key = keyOf(pt)
  if (key === lastKey || Date.now() < driveUntil) return
  lastKey = key
  driveUntil = Date.now() + 900
  scrollEnTo(pt.h, pt.b, true)
  markEnActive(pt.h, pt.b)
}

function markEnActive(h: number, b: number) {
  if (!enDoc) return
  const el = blockByKey(enDoc, h, b)
  if (el) markActive(enDoc, el)
}

/** 英文栏滚动 → 中文高亮与英文进度（不驱动中文滚动） */
function onHostScroll() {
  refreshEnPct()
  if (!open.value || layout.value === 'inter' || show.value === 'zh' || !enDoc || !host.value) return
  const zhRoot = document.querySelector<HTMLElement>('.vp-doc')
  if (!zhRoot) return
  const block = activeInContainer(enDoc, host.value)
  if (!block) return
  const h = Number(block.dataset.biliH ?? -1)
  const b = Number(block.dataset.biliB ?? 0)
  const el = pointEl(zhRoot, h, b)
  if (el) markActive(zhRoot, el)
}

/** 容器内当前阅读块（视口上 1/3 基准线，跳过零尺寸块） */
function activeInContainer(doc: Element, box: HTMLElement): HTMLElement | null {
  const line = box.getBoundingClientRect().top + box.clientHeight * 0.33
  let cur: HTMLElement | null = null
  for (const el of biliBlocks(doc)) {
    const r = el.getBoundingClientRect()
    if (r.width === 0 && r.height === 0) continue
    if (r.top <= line && r.bottom >= line) return el
    if (r.top < line) cur = el
  }
  return cur
}

const zhPct = ref(0)
const enPct = ref(0)
function refreshPct() {
  const max = document.documentElement.scrollHeight - window.innerHeight
  zhPct.value = max > 0 ? Math.min(100, Math.round((window.scrollY / max) * 100)) : 0
}
function refreshEnPct() {
  const h = host.value
  if (!h) return
  const max = h.scrollHeight - h.clientHeight
  enPct.value = max > 0 ? Math.min(100, Math.round((h.scrollTop / max) * 100)) : 0
}

// 滚动位置记忆（per-page，中文侧）
let saveTimer: ReturnType<typeof setTimeout> | undefined
function saveScroll() {
  clearTimeout(saveTimer)
  saveTimer = setTimeout(() => {
    if (hasLS && page.value.relativePath) {
      try {
        localStorage.setItem('bili-scroll:' + page.value.relativePath, String(Math.round(window.scrollY)))
      } catch {
        /* 存储满等异常静默 */
      }
    }
  }, 800)
}

let lastPolledY = -1
function onWinScroll() {
  const now = Date.now()
  if (now - lastDrive < 120) return
  lastDrive = now
  refreshPct()
  saveScroll()
  followZh()
}

// ------------------------------------------------- 点击 / 选中 / 键盘（沿用） --
function onDocClick(e: MouseEvent) {
  if (!open.value) return
  const target = clickableBlock(e)
  if (!target) return
  const zhRoot = document.querySelector<HTMLElement>('.vp-doc')
  if (!zhRoot) return
  const pt = mapPoint(zhRoot, target)
  if (!pt) return
  lastKey = keyOf(pt)
  markActive(zhRoot, target)
  driveUntil = Date.now() + 1200
  if (layout.value !== 'inter' && show.value !== 'zh') {
    scrollEnTo(pt.h, pt.b, true)
    markEnActive(pt.h, pt.b)
  }
  // 点击处句子 → 双侧句级高亮
  const caret = (document as any).caretRangeFromPoint?.(e.clientX, e.clientY)
  if (caret && target.contains(caret.startContainer)) {
    const si = sentenceIndexAt(target.textContent || '', offsetInElement(target, caret))
    highlightSentence(target, si, 'bili-sent-zh')
    if (layout.value !== 'inter' && show.value !== 'zh' && enDoc) {
      const enEl = blockByKey(enDoc, pt.h, pt.b)
      if (enEl) highlightSentence(enEl, si, 'bili-sent-en')
    }
  }
}

function onHostClick(e: MouseEvent) {
  if (!open.value || !enDoc || !host.value) return
  const box = host.value
  const t = e.target as HTMLElement
  if (t.closest('a, button, select, input, label, sup')) return
  const block = t.closest<HTMLElement>('p, h2, h3, h4, li, blockquote, pre, table, dl')
  if (!block || !box.contains(block)) return
  const h = Number(block.dataset.biliH ?? -1)
  const b = Number(block.dataset.biliB ?? 0)
  const zhRoot = document.querySelector<HTMLElement>('.vp-doc')
  if (!zhRoot) return
  const el = pointEl(zhRoot, h, b)
  if (!el) return
  lastKey = keyOf(mapPoint(zhRoot, el))
  markActive(zhRoot, el)
  driveUntil = Date.now() + 1200
  const y = el.getBoundingClientRect().top + window.scrollY - 88
  window.scrollTo({ top: Math.max(y, 0), behavior: 'smooth' })
}

let selTimer: ReturnType<typeof setTimeout> | undefined
function onSelectionChange() {
  clearTimeout(selTimer)
  selTimer = setTimeout(() => {
    if (!open.value || !enDoc) return
    const zhRoot = document.querySelector<HTMLElement>('.vp-doc')
    const sel = window.getSelection()
    if (!zhRoot || !sel || sel.isCollapsed || !sel.anchorNode || !zhRoot.contains(sel.anchorNode)) {
      if (zhRoot) clearSentenceMarks(zhRoot, 'bili-sent-zh')
      if (enDoc) clearSentenceMarks(enDoc, 'bili-sent-en')
      return
    }
    const para = containingBlock(zhRoot, sel.anchorNode)
    if (!para) return
    const si = sentenceIndexAt(para.textContent || '', offsetInElement(para, sel.getRangeAt(0)))
    highlightSentence(para, si, 'bili-sent-zh')
    const pt = mapPoint(zhRoot, para)
    if (!pt) return
    const enEl = blockByKey(enDoc, pt.h, pt.b)
    if (enEl) highlightSentence(enEl, si, 'bili-sent-en')
  }, 300)
}

function moveActive(delta: number) {
  if (!open.value) return
  const zhRoot = document.querySelector<HTMLElement>('.vp-doc')
  if (!zhRoot) return
  const blocks = biliBlocks(zhRoot)
  if (!blocks.length) return
  const keys = blocks.map((b) => keyOf(mapPoint(zhRoot, b)))
  let idx = keys.indexOf(lastKey)
  if (idx < 0) idx = delta > 0 ? -1 : 0
  const el = blocks[Math.min(Math.max(idx + delta, 0), blocks.length - 1)]
  const pt = mapPoint(zhRoot, el)
  lastKey = keyOf(pt)
  markActive(zhRoot, el)
  driveUntil = Date.now() + 1200
  const y = el.getBoundingClientRect().top + window.scrollY - 88
  window.scrollTo({ top: Math.max(y, 0), behavior: 'smooth' })
  if (layout.value !== 'inter' && show.value !== 'zh' && pt) {
    scrollEnTo(pt.h, pt.b, true)
    markEnActive(pt.h, pt.b)
  }
}

function onKeydown(e: KeyboardEvent) {
  const t = e.target as HTMLElement
  if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return
  if (e.metaKey || e.ctrlKey) return
  if (e.key === 'Escape' && open.value) {
    open.value = false
    return
  }
  if (!open.value) return
  if (e.key === 'j' || (e.altKey && e.key === 'ArrowDown')) {
    e.preventDefault()
    moveActive(1)
  } else if (e.key === 'k' || (e.altKey && e.key === 'ArrowUp')) {
    e.preventDefault()
    moveActive(-1)
  }
}

function cycleLayout() {
  layout.value = layout.value === 'side' ? 'stack' : layout.value === 'stack' ? 'inter' : 'side'
}

function close() {
  open.value = false
}

const layoutLabel = computed(() =>
  layout.value === 'side' ? '⇔ 左右' : layout.value === 'stack' ? '↕ 上下' : '⇕ 交错',
)

onMounted(() => {
  window.addEventListener('scroll', onWinScroll, { passive: true })
  // 原生 scroll 事件在部分宿主环境不派发（2026-10-31 IAB 实测），轮询兜底
  setInterval(() => {
    const y = Math.round(window.scrollY)
    if (y !== lastPolledY) {
      lastPolledY = y
      onWinScroll()
    }
  }, 400)
  document.addEventListener('click', onDocClick)
  document.addEventListener('selectionchange', onSelectionChange)
  document.addEventListener('keydown', onKeydown)
  if (open.value && enPath.value) loadEn()
  if (hasLS && page.value.relativePath) {
    const saved = Number(localStorage.getItem('bili-scroll:' + page.value.relativePath) || '0')
    if (saved > 50) window.scrollTo({ top: saved })
  }
})

onBeforeUnmount(() => {
  pending?.abort()
  window.removeEventListener('scroll', onWinScroll)
  document.removeEventListener('click', onDocClick)
  document.removeEventListener('selectionchange', onSelectionChange)
  document.removeEventListener('keydown', onKeydown)
  clearInterleave()
  clearTimeout(selTimer)
  clearTimeout(saveTimer)
  const b = document.body
  b.classList.remove(
    'bili-mode', 'bili-side', 'bili-stack', 'bili-inter', 'bili-show-compare',
    'bili-show-zh', 'bili-show-en', 'bili-bottombar',
  )
})
</script>

<template>
  <div v-if="enPath" class="bili-toggle-wrap">
    <button class="bili-btn" :class="{ on: hideSidebar }" title="隐藏/显示左侧目录（桌面端）" @click="hideSidebar = !hideSidebar">
      ⇤ 目录
    </button>
    <button class="bili-btn" :class="{ on: open }" title="双语对照：中文与 SEP 英文原文" @click="open = !open">
      ⇔ 对照原文
    </button>
  </div>

  <Teleport to="body">
    <div v-if="open && enPath" ref="panel" class="bili-panel">
      <div class="bili-bar">
        <span class="bili-bar-title">English · SEP 原文</span>

        <div class="bili-tabs" role="group" aria-label="双语显示模式">
          <button :class="{ on: show === 'compare' }" title="中英对照" @click="show = 'compare'">对照</button>
          <button :class="{ on: show === 'zh' }" title="只显示中文" @click="show = 'zh'">仅中文</button>
          <button :class="{ on: show === 'en' }" title="只显示英文原文" @click="show = 'en'">仅英文</button>
        </div>

        <span class="bili-progress" title="双语阅读进度">
          中 {{ zhPct }}%<template v-if="layout !== 'inter' && show !== 'zh'"> · 英 {{ enPct }}%</template>
        </span>
        <button class="bili-act" :title="`当前：${layoutLabel}，点击切换`" @click="cycleLayout">
          {{ layoutLabel }}
        </button>
        <label v-if="layout !== 'inter' && show !== 'zh'" class="bili-sync">
          <input v-model="sync" type="checkbox" />段落同步
        </label>
        <a class="bili-act" :href="withBase(enPath!)" target="_blank" rel="noopener">新窗口</a>
        <button class="bili-act" @click="close">关闭</button>
      </div>

      <div
        v-show="layout !== 'inter' && show !== 'zh'"
        ref="host"
        class="bili-doc"
        @scroll.passive="onHostScroll"
        @click="onHostClick"
      >
        <p v-if="loading" class="bili-hint">正在载入英文原文…</p>
        <p v-else-if="failed" class="bili-hint">
          英文原文载入失败。<a :href="withBase(enPath!)" target="_blank" rel="noopener">在新窗口打开</a>
        </p>
      </div>
    </div>
  </Teleport>
</template>

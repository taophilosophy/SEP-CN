<script setup lang="ts">
import { onBeforeUnmount, onMounted, watch } from 'vue'
import { useData } from 'vitepress'
import {
  activeBlock,
  clearSentenceMarks,
  clickableBlock,
  containingBlock,
  highlightSentence,
  mapPoint,
  markActive,
  offsetInElement,
  pointEl,
  sentenceIndexAt,
} from '../bili-paragraph'
import { ensureMathJax } from '../mathjax-loader'

const { page } = useData()
let timer: ReturnType<typeof setTimeout> | undefined

let retries = 0

function typeset(el: HTMLElement) {
  if (!el.querySelector('.math-tex')) return // 无公式页面零开销
  ensureMathJax()
    .then((MJ) => {
      try {
        MJ.typesetClear?.([el])
      } catch {
        /* 忽略清除失败 */
      }
      return MJ.typesetPromise([el])
    })
    .catch(() => {})
}

// -------------------------------------------- 公式复制按钮（复制 TeX 原文） --
// 公式原文本就保留在 .math-tex 的文本里（math-plugin rawMathHtml），
// 无需 data-tex；排版前后均可复制。
function enhanceMathCopy(el: HTMLElement) {
  for (const span of el.querySelectorAll<HTMLElement>('.math-tex')) {
    if (span.querySelector('.math-copy')) continue
    const tex = (span.textContent || '').trim()
    if (tex.length < 3) continue
    const btn = document.createElement('button')
    btn.type = 'button'
    btn.className = 'math-copy'
    btn.textContent = '复制'
    btn.setAttribute('aria-label', '复制公式 TeX 原文')
    btn.addEventListener('click', (ev) => {
      ev.stopPropagation() // 不触发段落对照跳转
      navigator.clipboard
        ?.writeText(tex)
        .then(() => {
          btn.textContent = '✓ 已复制'
          setTimeout(() => {
            btn.textContent = '复制'
          }, 1200)
        })
        .catch(() => {})
    })
    span.appendChild(btn)
  }
}

function schedule(delay = 120) {
  clearTimeout(timer)
  retries = 0
  timer = setTimeout(attempt, delay)
}

// dev 下正文由路由异步加载且分两步：.vp-doc 外壳先挂载、md 模块内容
// （含 .math-tex）稍后到达——看到外壳后继续短重试直至公式哨兵出现或达上限
// （无公式页多空转几秒的 DOM 查询，开销可忽略）
function attempt() {
  const el = document.querySelector('.vp-doc') as HTMLElement | null
  if (!el || (!el.querySelector('.math-tex') && retries < 35)) {
    if (retries++ < 35) timer = setTimeout(attempt, 300)
    return
  }
  typeset(el)
  enhanceMathCopy(el)
}

watch(() => page.value.relativePath, () => schedule())

onMounted(() => schedule(60))
onBeforeUnmount(() => clearTimeout(timer))

// ---------------------------------------- iframe 内：段落跟随（子侧） --
// SSR（vitepress build）下没有 window，须先判存在
const w = (typeof window !== 'undefined' ? window : undefined) as any
const inIframe = !!w && w.parent !== w

if (inIframe && !w.__biliIframeSync) {
  w.__biliIframeSync = true
  let lockedUntil = 0
  let lastKey = ''

  // 英文侧滚动 → 当前段变化 → 回传父页(时间节流,理由同父侧)
  let lastTick = 0
  window.addEventListener('scroll', () => {
    if (Date.now() < lockedUntil) return
    const now = Date.now()
    if (now - lastTick < 120) return
    lastTick = now
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const el = activeBlock(doc)
    if (!el) return
    markActive(doc, el)
    const pt = mapPoint(doc, el)
    if (!pt) return
    const key = pt.h + ':' + pt.b
    if (key === lastKey) return
    lastKey = key
    const max = document.documentElement.scrollHeight - window.innerHeight
    const enPct = max > 0 ? Math.min(100, Math.round((window.scrollY / max) * 100)) : 0
    window.parent.postMessage({ type: 'bili:active-back', h: pt.h, b: pt.b, enPct }, '*')
  }, { passive: true })

  // 接收中文侧驱动：soft=滚动跟随（无闪烁），硬=点击跳转（带闪烁）
  window.addEventListener('message', (e: MessageEvent) => {
    if (e.source !== window.parent || e.data?.type !== 'bili:goto') return
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const el = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (!el) return
    lockedUntil = Date.now() + 900
    lastKey = e.data.h + ':' + e.data.b
    markActive(doc, el)
    el.scrollIntoView({ block: 'start', behavior: 'smooth' })
    if (!e.data.soft) {
      el.classList.add('bili-flash')
      setTimeout(() => el.classList.remove('bili-flash'), 1600)
    }
  })

  document.addEventListener('click', (ev: MouseEvent) => {
    const target = clickableBlock(ev)
    if (!target) return
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const pt = mapPoint(doc, target)
    if (pt) {
      lastKey = pt.h + ':' + pt.b
      markActive(doc, target)
      window.parent.postMessage({ type: 'bili:goto-back', h: pt.h, b: pt.b }, '*')
    }
  })

  // 布局模式同步:父侧切换左右/上下时同步 html 类(等宽/居中排版切换)
  const applyLayout = () => {
    document.documentElement.classList.toggle(
      'bili-side',
      localStorage.getItem('bili-layout') !== 'stack',
    )
  }
  applyLayout()
  window.addEventListener('message', (e: MessageEvent) => {
    if (e.source !== window.parent || e.data?.type !== 'bili:layout') return
    if (e.data.layout) localStorage.setItem('bili-layout', e.data.layout)
    applyLayout()
  })

  // 原生 scroll 事件可能不派发(同父侧),轮询兜底
  let lastPolledY = -1
  setInterval(() => {
    const y = Math.round(window.scrollY)
    if (y === lastPolledY) return
    lastPolledY = y
    if (Date.now() < lockedUntil) return
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const el = activeBlock(doc)
    if (!el) return
    markActive(doc, el)
    const pt = mapPoint(doc, el)
    if (!pt) return
    const key = pt.h + ':' + pt.b
    if (key === lastKey) return
    lastKey = key
    const max = document.documentElement.scrollHeight - window.innerHeight
    const enPct = max > 0 ? Math.min(100, Math.round((window.scrollY / max) * 100)) : 0
    window.parent.postMessage({ type: 'bili:active-back', h: pt.h, b: pt.b, enPct }, '*')
  }, 400)

  // 选中文本 → 中文侧同序句高亮（2026-10-31；selectionchange 300ms 去抖）
  let selTimer: ReturnType<typeof setTimeout> | undefined
  document.addEventListener('selectionchange', () => {
    if (selTimer) clearTimeout(selTimer)
    selTimer = setTimeout(() => {
      const doc = document.querySelector('.vp-doc')
      if (!doc) return
      const sel = window.getSelection()
      if (!sel || sel.isCollapsed || !sel.anchorNode || !doc.contains(sel.anchorNode)) {
        window.parent.postMessage({ type: 'bili:sent-back', h: -1, b: 0, si: -1 }, '*')
        clearSentenceMarks(doc, 'bili-sent-en')
        return
      }
      const para = containingBlock(doc, sel.anchorNode)
      if (!para) return
      const si = sentenceIndexAt(para.textContent || '', offsetInElement(para, sel.getRangeAt(0)))
      const pt = mapPoint(doc, para)
      if (!pt) return
      highlightSentence(para, si, 'bili-sent-en')
      window.parent.postMessage({ type: 'bili:sent-back', h: pt.h, b: pt.b, si }, '*')
    }, 300)
  })

  // 接收中文侧选中驱动：对侧同序句高亮 / 清除
  window.addEventListener('message', (e: MessageEvent) => {
    if (e.source !== window.parent || e.data?.type !== 'bili:sent') return
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const para = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (!para) return
    if ((e.data.si ?? -1) < 0) {
      clearSentenceMarks(para, 'bili-sent-en')
      return
    }
    highlightSentence(para, e.data.si, 'bili-sent-en')
  })
}
</script>

<template>
  <span style="display: none" aria-hidden="true"></span>
</template>

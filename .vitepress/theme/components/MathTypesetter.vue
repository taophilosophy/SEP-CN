<script setup lang="ts">
import { onBeforeUnmount, onMounted, watch } from 'vue'
import { useData } from 'vitepress'
import { clickableBlock, mapPoint, pointEl } from '../bili-paragraph'
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

// ---------------------------------------- iframe 内：滚动同步（子侧） --
// SSR（vitepress build）下没有 window，须先判存在
const w = (typeof window !== 'undefined' ? window : undefined) as any
const inIframe = !!w && w.parent !== w

if (inIframe && !w.__biliIframeSync) {
  w.__biliIframeSync = true
  let lockedUntil = 0
  let raf = 0

  window.addEventListener('scroll', () => {
    if (Date.now() < lockedUntil || raf) return
    raf = requestAnimationFrame(() => {
      raf = 0
      const max = document.documentElement.scrollHeight - window.innerHeight
      window.parent.postMessage(
        { type: 'bili:scroll', ratio: max > 0 ? window.scrollY / max : 0 },
        '*',
      )
    })
  }, { passive: true })

  window.addEventListener('message', (e: MessageEvent) => {
    if (e.source !== window.parent || e.data?.type !== 'bili:scroll') return
    const max = document.documentElement.scrollHeight - window.innerHeight
    lockedUntil = Date.now() + 120
    window.scrollTo(0, (e.data.ratio ?? 0) * Math.max(max, 0))
  })

  // 段落级对照（2026-10-30 #4，子侧）：接收中文栏的段落坐标并滚动对位；
  // 英文栏内点击段落则把坐标回传父页（bili:goto-back）
  window.addEventListener('message', (e: MessageEvent) => {
    if (e.source !== window.parent || e.data?.type !== 'bili:goto') return
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const el = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (!el) return
    lockedUntil = Date.now() + 2500
    el.scrollIntoView({ block: 'start', behavior: 'smooth' })
    el.classList.add('bili-flash')
    setTimeout(() => el.classList.remove('bili-flash'), 1600)
  })

  document.addEventListener('click', (ev: MouseEvent) => {
    const target = clickableBlock(ev)
    if (!target) return
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const pt = mapPoint(doc, target)
    if (pt) window.parent.postMessage({ type: 'bili:goto-back', h: pt.h, b: pt.b }, '*')
  })
}
</script>

<template>
  <span style="display: none" aria-hidden="true"></span>
</template>

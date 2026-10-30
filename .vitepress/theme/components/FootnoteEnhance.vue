<script setup lang="ts">
import { nextTick, onBeforeUnmount, onMounted, watch } from 'vue'
import { useData } from 'vitepress'
import 'littlefoot/dist/littlefoot.css'
import { ensureMathJax } from '../mathjax-loader'

// 脚注悬浮预览（2026-10-30 #5）：现成方案 littlefoot.js——
// [^n] 引注变为悬停/点击弹出气泡，不再跳页打断阅读。
// SPA 路由切换时先卸载旧实例，再对新页面重建。
const { page } = useData()
let inst: { unmount: () => void } | null = null
let retries = 0
let timer: ReturnType<typeof setTimeout> | undefined

// dev 下正文由路由异步加载，onMounted 时 .vp-doc 可能尚不存在——
// 与 MathTypesetter 同款重试，直至脚注引用出现（无脚注页面重试上限后静默放弃）
function schedule(delay = 120) {
  clearTimeout(timer)
  timer = setTimeout(attempt, delay)
}

async function attempt() {
  if (inst) {
    try {
      inst.unmount()
    } catch {
      /* 页面已更替时忽略 */
    }
    inst = null
  }
  await nextTick()
  if (typeof document === 'undefined') return
  // 无脚注引用的页面不初始化（2.0 的脚注 href 形如 #footnote1）
  if (!document.querySelector('.vp-doc .footnote-ref a[href^="#footnote"]')) {
    if (retries++ < 25) timer = setTimeout(attempt, 300)
    return
  }
  // vite 依赖预打包会把 littlefoot 双重包裹（default 里再套 {default, littlefoot}），
  // rollup 构建产物则直接是函数——做兼容解包（2026-10-30 实测）
  const mod = (await import('littlefoot')) as any
  const lf =
    typeof mod === 'function'
      ? mod
      : typeof mod?.default === 'function'
        ? mod.default
        : mod?.default?.default
  if (typeof lf !== 'function') return
  inst = lf({
    activateOnHover: true,
    dismissOnUnhover: true,
    hoverDelay: 200,
    scope: '.vp-doc',
    // 弹层克隆的是未排版的原始 .math-tex（littlefoot 隐藏的底部脚注区
    // 不参与 MathJax 排版，见 2026-10-30 实测）——弹层激活后对其单独排版，
    // 无公式页面顺便按需触发 MathJax 加载
    activateCallback: (popover: HTMLElement) => {
      if (!popover.querySelector('.math-tex')) return
      ensureMathJax()
        .then((MJ) => MJ.typesetPromise([popover]))
        .catch(() => {})
    },
  })
}

watch(() => page.value.relativePath, () => {
  retries = 0
  schedule()
})
onMounted(() => {
  retries = 0
  schedule(60)
})
onBeforeUnmount(() => {
  clearTimeout(timer)
  inst?.unmount()
})
</script>

<template>
  <span hidden aria-hidden="true"></span>
</template>

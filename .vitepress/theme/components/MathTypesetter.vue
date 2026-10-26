<script setup lang="ts">
import { onBeforeUnmount, onMounted, watch } from 'vue'
import { useData } from 'vitepress'

const { page } = useData()
let timer: ReturnType<typeof setTimeout> | undefined

let retries = 0

function typeset() {
  const MJ = (window as any).MathJax
  // MathJax 脚本 defer 加载，未就绪时稍后重试（有上限，脚本缺失时静默放弃）
  if (!MJ?.typesetPromise) {
    if (retries++ < 25) timer = setTimeout(typeset, 300)
    return
  }
  const el = document.querySelector('.vp-doc') as HTMLElement | null
  if (!el || !el.querySelector('.math-tex')) return
  try {
    MJ.typesetClear?.([el])
  } catch {
    /* 忽略清除失败 */
  }
  MJ.typesetPromise([el]).catch(() => {})
}

function schedule(delay = 120) {
  clearTimeout(timer)
  timer = setTimeout(typeset, delay)
}

watch(() => page.value.relativePath, () => schedule())

onMounted(() => schedule(60))
onBeforeUnmount(() => clearTimeout(timer))

// ---------------------------------------- iframe 内：滚动同步（子侧） --
const w = window as any
const inIframe = typeof window !== 'undefined' && window.parent !== window

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
}
</script>

<template>
  <span style="display: none" aria-hidden="true"></span>
</template>

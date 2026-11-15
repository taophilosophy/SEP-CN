<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, watch } from 'vue'
import { useData } from 'vitepress'

// SEP 版式题区（specs/037）：作者行 + 斜体 pubinfo + EDEBE9 横幅，按 SEP 词条
// “标题 → pubinfo → 横幅 → 正文”的顺序插到 .vp-doc 首个 h1 之后。
// VitePress 2.0-alpha 没有“标题后”槽位（doc-top 是 aside 上方全宽位），
// 故采用 FootnoteEnhance 同款 DOM 手术模式；无 srcMeta 的页面不渲染。
// pubinfo 文案保持 SEP 原文措辞逐字一致（上游自身元数据，可回溯核对）。
const { page } = useData()
const m = computed<any>(() => page.value.frontmatter?.srcMeta)

let el: HTMLElement | null = null
let retries = 0
let timer: ReturnType<typeof setTimeout> | undefined

function cleanup() {
  el?.remove()
  el = null
}

async function attempt() {
  cleanup()
  if (!m.value) return
  await nextTick()
  if (typeof document === 'undefined') return
  const doc = document.querySelector('.vp-doc')
  const h1 = doc?.querySelector('h1')
  if (!doc || !h1) {
    if (retries++ < 25) timer = setTimeout(attempt, 300)
    return
  }
  const wrap = document.createElement('div')
  const meta = document.createElement('div')
  meta.className = 'entry-meta'
  const authors = (m.value.authors || []) as string[]
  if (authors.length) {
    const line = document.createElement('div')
    line.className = 'entry-authors'
    line.textContent = authors.join(', ')
    meta.appendChild(line)
  }
  const parts: string[] = []
  if (m.value.firstPublished) parts.push(`First published ${m.value.firstPublished}`)
  if (m.value.substantiveRevision) parts.push(`substantive revision ${m.value.substantiveRevision}`)
  if (parts.length) {
    const pub = document.createElement('div')
    pub.className = 'entry-pubinfo'
    pub.textContent = parts.join('; ')
    meta.appendChild(pub)
  }
  if (meta.childElementCount) wrap.appendChild(meta)
  // 对照模式（iframe 内）横幅是噪音：in-iframe CSS 已隐藏 .entry-banner，
  // 元信息（SEP 同款 pubinfo）保留在标题下，镜像页因此更像原站。
  const banner = document.createElement('div')
  banner.className = 'entry-banner'
  banner.append('开放获取 · 本站为《斯坦福哲学百科全书》简体中文译本，支持与')
  const a = document.createElement('a')
  a.href = String(m.value.sourceUrl || 'https://plato.stanford.edu/')
  a.target = '_blank'
  a.rel = 'noopener'
  a.textContent = '英文原文'
  banner.appendChild(a)
  banner.append('对照阅读')
  wrap.appendChild(banner)
  h1.after(wrap)
  el = wrap
}

watch(
  () => page.value.relativePath,
  () => {
    retries = 0
    cleanup()
    schedule()
  },
)

watch(m, () => {
  retries = 0
  cleanup()
  schedule()
})

function schedule(delay = 120) {
  clearTimeout(timer)
  timer = setTimeout(attempt, delay)
}

onMounted(() => {
  retries = 0
  schedule(60)
})

onBeforeUnmount(() => {
  clearTimeout(timer)
  cleanup()
})
</script>

<template>
  <span hidden aria-hidden="true"></span>
</template>

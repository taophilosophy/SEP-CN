<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useData, withBase } from 'vitepress'
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

const { page } = useData()
const enPath = computed(() => page.value.frontmatter?.enPath as string | undefined)

const open = ref(false)
const sync = ref(true)
const frame = ref<HTMLIFrameElement | null>(null)
// 用户显式开/关后，本会话内不再自动恢复（dev 下 page 数据异步到达，
// 挂载时 enPath 未定——自动恢复必须响应 enPath 到达事件，2026-10-31 修复）
const userTouched = ref(false)

watch(
  [enPath],
  () => {
    if (!userTouched.value) {
      open.value = localStorage.getItem('bili-open') === '1' && !!enPath.value
    }
  },
  { immediate: true, flush: 'post' },
)

onMounted(() => {
  sync.value = localStorage.getItem('bili-sync') !== '0'
})

watch([enPath, open], applyState, { flush: 'post' })
function applyState() {
  document.body.classList.toggle('bili-mode', open.value && !!enPath.value)
  document.body.classList.toggle('bili-stack', layout.value === 'stack')
  document.body.classList.toggle('hide-sidebar', hideSidebar.value)
}

watch(open, (v) => {
  userTouched.value = true
  localStorage.setItem('bili-open', v ? '1' : '0')
})

// 布局模式：side=左右并排 | stack=上下堆叠（2026-10-31 新增，持久化）
const layout = ref<'side' | 'stack'>(
  localStorage.getItem('bili-layout') === 'stack' ? 'stack' : 'side',
)
watch(
  layout,
  (v) => {
    localStorage.setItem('bili-layout', v)
    applyState()
  },
  { flush: 'post' },
)

// 左侧目录隐藏开关（2026-10-31：独立于对照模式，桌面对比/沉浸阅读用，持久化）
const hideSidebar = ref(localStorage.getItem('hide-sidebar') === '1')
watch(
  hideSidebar,
  (v) => {
    localStorage.setItem('hide-sidebar', v ? '1' : '0')
    applyState()
  },
  { flush: 'post' },
)

function toggleHideSidebar() {
  hideSidebar.value = !hideSidebar.value
}

// 选中文本 → 对侧同序句高亮（选中变化 300ms 去抖后驱动）
let selTimer: ReturnType<typeof setTimeout> | undefined
function onSelectionChange() {
  if (selTimer) clearTimeout(selTimer)
  selTimer = setTimeout(() => {
    if (!open.value || !sync.value || !frame.value?.contentWindow) return
    const sel = window.getSelection()
    const doc = document.querySelector('.vp-doc')
    if (!doc || !sel || sel.isCollapsed || !sel.anchorNode || !doc.contains(sel.anchorNode)) {
      frame.value?.contentWindow?.postMessage({ type: 'bili:sent', h: -1, b: 0, si: -1 }, '*')
      const el = document.querySelector('.vp-doc')
      if (el) clearSentenceMarks(el, 'bili-sent-zh')
      return
    }
    const para = containingBlock(doc, sel.anchorNode)
    if (!para) return
    const range = sel.getRangeAt(0)
    const si = sentenceIndexAt(para.textContent || '', offsetInElement(para, range))
    const pt = mapPoint(doc, para)
    if (!pt) return
    highlightSentence(para, si, 'bili-sent-zh')
    frame.value.contentWindow!.postMessage({ type: 'bili:sent', h: pt.h, b: pt.b, si }, '*')
  }, 300)
}
watch(sync, (v) => localStorage.setItem('bili-sync', v ? '1' : '0'))

const frameSrc = computed(() => (enPath.value ? withBase(enPath.value) + '?embed=1' : ''))

// ------------------------------------------ 段落级双向跟随（2026-10-30 #4 升级） --
// 比例同步退役：以「当前阅读段」(标题区段 h + 区段内块序 b)为单位双向驱动，
// 键相同即止（断回环）、驱动锁防抖；「滚动同步」开关 = 是否进行双向跟随。
let lastKey = ''
let driveUntil = 0
let rafPending = false

function keyOf(pt: { h: number; b: number } | null): string {
  return pt ? pt.h + ':' + pt.b : ''
}

// 中文侧滚动 → 当前段变化 → 英文栏跟随（软跳：平滑、无闪烁）
function followZh() {
  if (!open.value || !sync.value || !frame.value?.contentWindow) return
  const doc = document.querySelector('.vp-doc')
  if (!doc) return
  const el = activeBlock(doc)
  if (!el) return
  markActive(doc, el)
  const pt = mapPoint(doc, el)
  if (!pt) return
  const key = keyOf(pt)
  if (key === lastKey || Date.now() < driveUntil) return
  lastKey = key
  driveUntil = Date.now() + 900
  frame.value.contentWindow!.postMessage({ type: 'bili:goto', h: pt.h, b: pt.b, soft: 1 }, '*')
}

function onWinScroll() {
  if (!open.value || !sync.value || rafPending) return
  rafPending = true
  requestAnimationFrame(() => {
    rafPending = false
    followZh()
  })
}

function onMessage(e: MessageEvent) {
  if (e.source !== frame.value?.contentWindow || !sync.value || !open.value) return
  const doc = document.querySelector('.vp-doc')
  if (!doc) return
  if (e.data?.type === 'bili:sent-back') {
    // 英文侧选中 → 中文侧同序句高亮
    const el = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (!el) return
    if ((e.data.si ?? -1) < 0) {
      clearSentenceMarks(el, 'bili-sent-zh')
      return
    }
    highlightSentence(el, e.data.si, 'bili-sent-zh')
  } else if (e.data?.type === 'bili:active-back') {
    // 英文侧滚动跟随：中文侧滚到对应段（键相同/驱动锁内仅更新高亮）
    const el = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (!el) return
    markActive(doc, el)
    const pt = mapPoint(doc, el)
    const key = keyOf(pt)
    if (key === lastKey || Date.now() < driveUntil) return
    lastKey = key
    driveUntil = Date.now() + 900
    const y = el.getBoundingClientRect().top + window.scrollY - 88
    window.scrollTo({ top: Math.max(y, 0), behavior: 'smooth' })
  } else if (e.data?.type === 'bili:goto-back') {
    // 段落点击回跳（硬跳）
    const el = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (!el) return
    const pt = mapPoint(doc, el)
    lastKey = keyOf(pt)
    markActive(doc, el)
    driveUntil = Date.now() + 1200
    const y = el.getBoundingClientRect().top + window.scrollY - 88
    window.scrollTo({ top: Math.max(y, 0), behavior: 'smooth' })
  }
}

// 段落级跳转：点击中文段落 → 英文栏滚到对应段（硬跳+闪烁）
function onDocClick(e: MouseEvent) {
  if (!open.value || !sync.value || !frame.value?.contentWindow) return
  const target = clickableBlock(e)
  if (!target) return
  const doc = document.querySelector('.vp-doc')
  if (!doc) return
  const pt = mapPoint(doc, target)
  if (!pt) return
  lastKey = keyOf(pt)
  markActive(doc, target)
  driveUntil = Date.now() + 1200
  frame.value.contentWindow!.postMessage({ type: 'bili:goto', h: pt.h, b: pt.b }, '*')
}

function onFrameLoad() {
  // 新原文载入后立即对齐当前阅读段
  followZh()
}

onMounted(() => {
  window.addEventListener('scroll', onWinScroll, { passive: true })
  window.addEventListener('message', onMessage)
  document.addEventListener('click', onDocClick)
  document.addEventListener('selectionchange', onSelectionChange)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onWinScroll)
  window.removeEventListener('message', onMessage)
  document.removeEventListener('click', onDocClick)
  document.removeEventListener('selectionchange', onSelectionChange)
  if (selTimer) clearTimeout(selTimer)
})
</script>

<template>
  <div v-if="enPath" class="bili-toggle-wrap">
    <button
      class="bili-btn"
      :class="{ on: hideSidebar }"
      title="隐藏/显示左侧目录（桌面端）"
      @click="toggleHideSidebar"
    >
      ⇤ 目录
    </button>
    <button
      class="bili-btn"
      :class="{ on: open }"
      title="并排显示本条目的英文原文"
      @click="open = !open"
    >
      ⇔ 对照原文
    </button>
  </div>

  <Teleport to="body">
    <div v-if="open && enPath && frameSrc" class="bili-panel">
      <div class="bili-bar">
        <span class="bili-bar-title">English · SEP 原文</span>
        <button class="bili-act" title="切换左右/上下布局" @click="layout = layout === 'side' ? 'stack' : 'side'">
          {{ layout === 'side' ? '↕ 上下' : '⇔ 左右' }}
        </button>
        <label class="bili-sync"><input v-model="sync" type="checkbox" />段落同步</label>
        <a class="bili-act" :href="withBase(enPath!)" target="_blank" rel="noopener">新窗口</a>
        <button class="bili-act" @click="open = false">关闭</button>
      </div>
      <iframe ref="frame" class="bili-frame" :src="frameSrc" title="英文原文" @load="onFrameLoad" />
    </div>
  </Teleport>
</template>

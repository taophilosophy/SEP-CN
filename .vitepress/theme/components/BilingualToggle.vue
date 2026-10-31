<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useData, withBase } from 'vitepress'
import {
  activeBlock,
  BILI_BLOCKS,
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
const hasLS = typeof localStorage !== 'undefined'

watch(
  [enPath],
  () => {
    if (typeof localStorage === 'undefined') return // SSR（build 渲染页）无 localStorage
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
  if (typeof localStorage !== 'undefined') {
    localStorage.setItem('bili-open', v ? '1' : '0')
  }
})

// 布局模式：side=左右并排 | stack=上下堆叠（2026-10-31 新增，持久化）
const layout = ref<'side' | 'stack'>(
  hasLS && localStorage.getItem('bili-layout') === 'stack' ? 'stack' : 'side',
)
watch(
  layout,
  (v) => {
    if (hasLS) localStorage.setItem('bili-layout', v)
    applyState()
    frame.value?.contentWindow?.postMessage({ type: 'bili:layout', layout: v }, '*')
  },
  { flush: 'post' },
)

// 左侧目录隐藏开关（2026-10-31：独立于对照模式，桌面对比/沉浸阅读用，持久化）
const hideSidebar = ref(hasLS && localStorage.getItem('hide-sidebar') === '1')
watch(
  hideSidebar,
  (v) => {
    if (hasLS) localStorage.setItem('hide-sidebar', v ? '1' : '0')
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
let lastPolledY = -1

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

let lastDrive = 0
function onWinScroll() {
  // 时间节流而非 rAF:rAF 在后台 tab 被节流为 0,双屏对照场景下用户
  // 在另一窗口滚动时跟随会全卡(2026-10-31 实测)
  const now = Date.now()
  if (now - lastDrive < 120) return
  lastDrive = now
  refreshPct()
  saveScroll()
  followZh()
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
    // 英文侧滚动 → 仅同步高亮与进度,不驱动中文滚动:双向同时驱动会因两侧
    // 块数/译序差异振荡收敛到错位平衡(TransRead/SnapVerbo 均为单向滚动跟随
    // +点击双向;2026-10-31 实测振荡后改单向主从,中文为主)
    if (typeof e.data.enPct === 'number') enPct.value = e.data.enPct
    const el = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (el) markActive(doc, el)
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

// 段落级跳转：点击中文段落 → 英文栏滚到对应段 + 双侧句级高亮（一击两得，
// SnapVerbo/Yalango 范式：tap a sentence to highlight it in both languages）
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
  // 点击处的句子 → 双侧句级高亮（caretRangeFromPoint 取点击字符位）
  const caret = document.caretRangeFromPoint
    ? (document as any).caretRangeFromPoint(e.clientX, e.clientY)
    : null
  if (caret && target.contains(caret.startContainer)) {
    const si = sentenceIndexAt(
      target.textContent || '',
      offsetInElement(target, caret),
    )
    highlightSentence(target, si, 'bili-sent-zh')
    frame.value
      .contentWindow!.postMessage({ type: 'bili:sent', h: pt.h, b: pt.b, si }, '*')
  }
}

// ------------------------------------------------ 键盘导航（Yalango/CAT 范式） --
// j / Alt+↓ = 下一阅读段；k / Alt+↑ = 上一段；Esc = 关闭对照面板
function moveActive(delta: number) {
  if (!open.value || !sync.value || !frame.value?.contentWindow) return
  const doc = document.querySelector('.vp-doc')
  if (!doc) return
  const blocks = [...doc.querySelectorAll<HTMLElement>(BILI_BLOCKS)]
  if (!blocks.length) return
  const keys = blocks.map((b) => keyOf(mapPoint(doc, b)))
  let idx = keys.indexOf(lastKey)
  if (idx < 0) idx = delta > 0 ? -1 : 0
  const next = Math.min(Math.max(idx + delta, 0), blocks.length - 1)
  const el = blocks[next]
  const pt = mapPoint(doc, el)
  lastKey = keyOf(pt)
  markActive(doc, el)
  driveUntil = Date.now() + 1200
  const y = el.getBoundingClientRect().top + window.scrollY - 88
  window.scrollTo({ top: Math.max(y, 0), behavior: 'smooth' })
  frame.value.contentWindow!.postMessage({ type: 'bili:goto', h: pt.h, b: pt.b }, '*')
}

function onKeydown(e: KeyboardEvent) {
  const t = e.target as HTMLElement
  if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return
  if (e.metaKey || e.ctrlKey) return
  if (e.key === 'Escape' && open.value) {
    open.value = false
    return
  }
  if (!open.value || !sync.value) return
  if (e.key === 'j' || (e.altKey && e.key === 'ArrowDown')) {
    e.preventDefault()
    moveActive(1)
  } else if (e.key === 'k' || (e.altKey && e.key === 'ArrowUp')) {
    e.preventDefault()
    moveActive(-1)
  }
}

// 进度百分比（Yalango 范式：面板条常显双语阅读进度）
const zhPct = ref(0)
const enPct = ref(0)

function refreshPct() {
  const max = document.documentElement.scrollHeight - window.innerHeight
  zhPct.value = max > 0 ? Math.min(100, Math.round((window.scrollY / max) * 100)) : 0
}

// 滚动位置记忆：per-page 持久化，重开对照自动回到上次阅读位
let saveTimer: ReturnType<typeof setTimeout> | undefined
function saveScroll() {
  if (saveTimer) clearTimeout(saveTimer)
  saveTimer = setTimeout(() => {
    if (hasLS && page.value.relativePath) {
      try {
        localStorage.setItem(
          'bili-scroll:' + page.value.relativePath,
          String(Math.round(window.scrollY)),
        )
      } catch {
        /* 存储满等异常静默 */
      }
    }
  }, 800)
}

function onFrameLoad() {
  // 新原文载入后：同步布局模式,恢复上次阅读位（per-page 记忆），再对齐当前段
  frame.value?.contentWindow?.postMessage(
    { type: 'bili:layout', layout: layout.value },
    '*',
  )
  if (hasLS && page.value.relativePath) {
    const saved = Number(localStorage.getItem('bili-scroll:' + page.value.relativePath) || '0')
    if (saved > 50) window.scrollTo({ top: saved })
  }
  refreshPct()
  followZh()
}

onMounted(() => {
  window.addEventListener('scroll', onWinScroll, { passive: true })
  // 原生 scroll 事件在部分宿主环境不派发(2026-10-31 IAB 实测:scrollTop
  // 变化而事件 0 次)——轮询兜底,双通道并用
  setInterval(() => {
    const y = Math.round(window.scrollY)
    if (y !== lastPolledY) {
      lastPolledY = y
      onWinScroll()
    }
  }, 400)
  window.addEventListener('message', onMessage)
  document.addEventListener('click', onDocClick)
  document.addEventListener('selectionchange', onSelectionChange)
  document.addEventListener('keydown', onKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onWinScroll)
  window.removeEventListener('message', onMessage)
  document.removeEventListener('click', onDocClick)
  document.removeEventListener('selectionchange', onSelectionChange)
  document.removeEventListener('keydown', onKeydown)
  if (selTimer) clearTimeout(selTimer)
  if (saveTimer) clearTimeout(saveTimer)
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
        <span class="bili-progress" title="双语阅读进度">中 {{ zhPct }}% · 英 {{ enPct }}%</span>
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

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useData, withBase } from 'vitepress'
import { clickableBlock, mapPoint, pointEl } from '../bili-paragraph'

const { page } = useData()
const enPath = computed(() => page.value.frontmatter?.enPath as string | undefined)

const open = ref(false)
const sync = ref(true)
const frame = ref<HTMLIFrameElement | null>(null)

onMounted(() => {
  open.value = localStorage.getItem('bili-open') === '1' && !!enPath.value
  sync.value = localStorage.getItem('bili-sync') !== '0'
})

watch([enPath, open], applyState, { flush: 'post' })
function applyState() {
  document.body.classList.toggle('bili-mode', open.value && !!enPath.value)
}

watch(open, (v) => localStorage.setItem('bili-open', v ? '1' : '0'))
watch(sync, (v) => localStorage.setItem('bili-sync', v ? '1' : '0'))

const frameSrc = computed(() => (enPath.value ? withBase(enPath.value) + '?embed=1' : ''))

// -------------------------------------------------------- 父侧滚动同步 --
let lockedUntil = 0

function frameRatio() {
  const f = frame.value
  if (!f?.contentWindow) return
  const max = document.documentElement.scrollHeight - window.innerHeight
  f.contentWindow.postMessage(
    { type: 'bili:scroll', ratio: max > 0 ? window.scrollY / max : 0 },
    '*',
  )
}

function onWinScroll() {
  if (!sync.value || !open.value || Date.now() < lockedUntil) return
  frameRatio()
}

function onMessage(e: MessageEvent) {
  // 只接受当前原文 iframe 发来的消息
  if (e.source !== frame.value?.contentWindow || !sync.value || !open.value) return
  if (e.data?.type === 'bili:scroll') {
    const max = document.documentElement.scrollHeight - window.innerHeight
    lockedUntil = Date.now() + 120
    window.scrollTo(0, (e.data.ratio ?? 0) * Math.max(max, 0))
  } else if (e.data?.type === 'bili:goto-back') {
    // 段落级回跳：读者在英文栏点击某段，中文侧滚到对应段落
    const doc = document.querySelector('.vp-doc')
    if (!doc) return
    const el = pointEl(doc, e.data.h ?? -1, e.data.b ?? 0)
    if (!el) return
    lockedUntil = Date.now() + 2500
    const y = el.getBoundingClientRect().top + window.scrollY - 72
    window.scrollTo({ top: Math.max(y, 0), behavior: 'smooth' })
  }
}

// 段落级跳转（2026-10-30 #4）：对照模式下点击中文段落/标题/列表项，
// 英文栏滚到对应段落（以标题区段+区段内块序为坐标，见 bili-paragraph.ts）
function onDocClick(e: MouseEvent) {
  if (!open.value || !sync.value || !frame.value?.contentWindow) return
  const target = clickableBlock(e)
  if (!target) return
  const doc = document.querySelector('.vp-doc')
  if (!doc) return
  const pt = mapPoint(doc, target)
  if (!pt) return
  frame.value.contentWindow!.postMessage({ type: 'bili:goto', h: pt.h, b: pt.b }, '*')
  lockedUntil = Date.now() + 2500
}

function onFrameLoad() {
  // 新原文载入后立即对齐到当前中文页的滚动位置
  if (sync.value) frameRatio()
}

onMounted(() => {
  window.addEventListener('scroll', onWinScroll, { passive: true })
  window.addEventListener('message', onMessage)
  document.addEventListener('click', onDocClick)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onWinScroll)
  window.removeEventListener('message', onMessage)
  document.removeEventListener('click', onDocClick)
})
</script>

<template>
  <div v-if="enPath" class="bili-toggle-wrap">
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
        <label class="bili-sync"><input v-model="sync" type="checkbox" />滚动同步</label>
        <a class="bili-act" :href="withBase(enPath!)" target="_blank" rel="noopener">新窗口</a>
        <button class="bili-act" @click="open = false">关闭</button>
      </div>
      <iframe ref="frame" class="bili-frame" :src="frameSrc" title="英文原文" @load="onFrameLoad" />
    </div>
  </Teleport>
</template>

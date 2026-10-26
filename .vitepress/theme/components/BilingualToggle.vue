<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { useData, withBase } from 'vitepress'

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
  if (e.data?.type !== 'bili:scroll' || !sync.value || !open.value) return
  const max = document.documentElement.scrollHeight - window.innerHeight
  lockedUntil = Date.now() + 120
  window.scrollTo(0, (e.data.ratio ?? 0) * Math.max(max, 0))
}

function onFrameLoad() {
  // 新原文载入后立即对齐到当前中文页的滚动位置
  if (sync.value) frameRatio()
}

onMounted(() => {
  window.addEventListener('scroll', onWinScroll, { passive: true })
  window.addEventListener('message', onMessage)
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

<script setup lang="ts">
import { computed } from 'vue'
import { useData } from 'vitepress'

// 译文版本钉（零信任/可追溯的读者可见化，2026-10-30 #2）：
// 数据来自 baseline/entries.json（抓取管线单一事实源），由 config.mts 的
// transformPageData 按页面路径注入 frontmatter.srcMeta，此处只做展示。
const { page } = useData()
const m = computed<any>(() => page.value.frontmatter?.srcMeta)
const isMirror = computed(() => String(page.value.relativePath).startsWith('yuanwen/'))
const short = computed(() => (m.value?.sha256 ? String(m.value.sha256).slice(0, 12) : ''))
</script>

<template>
  <div v-if="m" class="src-pin">
    <template v-if="isMirror">
      <span>SEP 英文原文镜像（{{ m.edition }} 版抓取）</span>
    </template>
    <template v-else>
      <span>
        译自 <a :href="m.sourceUrl" target="_blank" rel="noopener">SEP 英文原文</a>（{{ m.edition }} 版）
      </span>
      <span v-if="m.firstPublished">首发 {{ m.firstPublished }}</span>
      <span v-if="m.substantiveRevision">实质修订 {{ m.substantiveRevision }}</span>
    </template>
    <span v-if="short" class="src-pin-sha" title="抓取源 HTML 的 SHA-256，全文可回溯核验">
      SHA-256 {{ short }}…
    </span>
  </div>
</template>

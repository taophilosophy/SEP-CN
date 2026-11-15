<script setup lang="ts">
import { withBase } from 'vitepress'
import VersionPin from './VersionPin.vue'

// SEP 版式页脚（specs/037）：菜单块分栏 + 版本钉（迁入）+ 版权行。
// 链接只收站点真实路由与外部实名资源，不造占位链接。
</script>

<template>
  <footer class="sep-footer">
    <div class="sep-footer-inner">
      <div class="menu">
        <div class="menu-block">
          <h4>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M3 6.5 9 4l6 2.5L21 4v13l-6 2.5L9 17l-6 2.5z" /><path d="M9 4v13M15 6.5v13" /></svg>
            站点
          </h4>
          <ul>
            <li><a :href="withBase('/')">首页</a></li>
            <li><a :href="withBase('/mu-lu-s')">分类目录</a></li>
          </ul>
        </div>
        <div class="menu-block">
          <h4>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z" /><path d="M20 17v4H6.5a2.5 2.5 0 0 1 0-4" /></svg>
            词汇与体例
          </h4>
          <ul>
            <li><a :href="withBase('/qian-yan/ci-hui-biao')">词汇表</a></li>
            <li><a :href="withBase('/shu-yu-biao')">术语对照</a></li>
          </ul>
        </div>
        <div class="menu-block">
          <h4>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9" /><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18" /></svg>
            外部
          </h4>
          <ul>
            <li><a href="https://plato.stanford.edu/" target="_blank" rel="noopener">SEP 英文原站</a></li>
            <li><a href="https://github.com/taophilosophy/SEP-CN" target="_blank" rel="noopener">GitHub 仓库</a></li>
          </ul>
        </div>
      </div>
      <VersionPin />
      <div class="credits">
        <p>《斯坦福哲学百科全书》简体中文翻译项目 · 支持与英文原文对照阅读</p>
        <p>Copyright © 2024 ykla · 以 BSD-2-Clause 许可证发布</p>
      </div>
    </div>
  </footer>
</template>

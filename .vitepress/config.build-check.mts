import { mergeConfig, defineConfig } from 'vitepress'
import base from './config.mts'

// 构建验证专用隔离配置（2026-10-30）：与 dev 并行运行时互不踩
// .vitepress/cache（dev 持有缓存目录，build 直接复用会互相破坏）。
// 产物仍出 .vitepress/dist（dev 不写该目录，无冲突）。
export default mergeConfig(base, defineConfig({
  cacheDir: '.vitepress/cache-build',
  // 2026-10-30 实验 A:footnote 引用在 build 产物字面化而 dev 正常,
  // 头号假说是 markdown 缓存与 footnote 插件 env 依赖不兼容——关缓存对照
  markdown: { cache: false },
}))

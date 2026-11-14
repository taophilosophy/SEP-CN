// 把 MathJax 的 tex-svg 组件复制到 public/mathjax/，站点完全离线加载。
// （specs/024：MathJax 4.1.3 起组件文件在包根，v3 的 es5/ 目录已取消。）
// public/mathjax/ 已被 .gitignore 排除，克隆后运行 `bun run dev` 会自动重建。
import { copyFileSync, existsSync, mkdirSync } from 'node:fs'
import path from 'node:path'

const src = path.join(process.cwd(), 'node_modules', 'mathjax', 'tex-svg.js')
const destDir = path.join(process.cwd(), 'public', 'mathjax')

if (!existsSync(src)) {
  console.error('[prepare-assets] 未找到 node_modules/mathjax/tex-svg.js，请先 bun install')
  process.exit(1)
}
mkdirSync(destDir, { recursive: true })
copyFileSync(src, path.join(destDir, 'tex-svg.js'))
console.log('[prepare-assets] mathjax/tex-svg.js → public/mathjax/tex-svg.js')

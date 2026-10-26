// 把 MathJax 3 的 tex-svg 组件复制到 public/mathjax/，站点完全离线加载。
// public/mathjax/ 已被 .gitignore 排除，克隆后运行 `bun run dev` 会自动重建。
import { copyFileSync, existsSync, mkdirSync } from 'node:fs'
import path from 'node:path'

const src = path.join(process.cwd(), 'node_modules', 'mathjax', 'es5', 'tex-svg.js')
const destDir = path.join(process.cwd(), 'public', 'mathjax')

if (!existsSync(src)) {
  console.error('[prepare-assets] 未找到 node_modules/mathjax/es5/tex-svg.js，请先 bun install')
  process.exit(1)
}
mkdirSync(destDir, { recursive: true })
copyFileSync(src, path.join(destDir, 'tex-svg.js'))
console.log('[prepare-assets] mathjax/es5/tex-svg.js → public/mathjax/tex-svg.js')

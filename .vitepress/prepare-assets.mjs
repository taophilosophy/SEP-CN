// 把 MathJax 的 tex-svg 组件复制到 public/mathjax/，站点完全离线加载。
// （specs/024：MathJax 4.1.3 起组件文件在包根，v3 的 es5/ 目录已取消。）
// public/mathjax/ 已被 .gitignore 排除，构建前自动重建。
//
// 依赖可以装在内容仓根，也可以装在上一层构建壳（ADR-0055：壳为构建入口，
// 依赖统一装在壳根）。因此两个路径都与 cwd 解耦：
//   src  —— 自本文件所在目录起按 Node 解析顺序逐级向上找 node_modules/mathjax；
//   dest —— 固定写回内容仓（本文件的上级目录）的 public/mathjax/。
import { copyFileSync, existsSync, mkdirSync } from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const here = path.dirname(fileURLToPath(import.meta.url))
const repoRoot = path.resolve(here, '..')
const REL = ['node_modules', 'mathjax', 'tex-svg.js']

function resolveUp(rel) {
  for (let dir = here; ; dir = path.dirname(dir)) {
    const candidate = path.join(dir, ...rel)
    if (existsSync(candidate)) return candidate
    if (path.dirname(dir) === dir) return null
  }
}

const src = resolveUp(REL)
if (!src) {
  console.error(
    '[prepare-assets] 找不到 node_modules/mathjax/tex-svg.js（已从 ' +
      here +
      ' 逐级向上查找）；请在内容仓根或上层构建壳运行 bun install',
  )
  process.exit(1)
}

const destDir = path.join(repoRoot, 'public', 'mathjax')
mkdirSync(destDir, { recursive: true })
copyFileSync(src, path.join(destDir, 'tex-svg.js'))
console.log(`[prepare-assets] ${src} → ${path.join(destDir, 'tex-svg.js')}`)

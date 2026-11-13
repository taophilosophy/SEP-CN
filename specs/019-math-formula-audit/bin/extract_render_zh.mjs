// 019 译文/yuanwen 侧公式抽取（渲染真值口径）。
//
// 直接调用站点 .vitepress/math-plugin.mjs 的 protectMath（渲染时真正参与
// 配对的同一正则，含货币守卫与围栏豁免），解出 @@MJ…@@ 哨兵里的公式原文。
// 这样抽取集 ≡ 站点实际送 MathJax 的集合，可渲染性判定零口径漂移。
// 另统计 \(…\) 残留（站上不渲染，属格式违规发现项）。
//
// 用法: node extract_render_zh.mjs zh|yw
//   zh → 扫 <repo>/<letter>/*.md；yw → 扫 <repo>/yuanwen/<letter>/*.md
// 产: results/render-<mode>.jsonl  每行 {f,i,k,x}（k: inline|display|paren）
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { protectMath } from '../../../.vitepress/math-plugin.mjs'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.resolve(HERE, '..', '..', '..')
const mode = process.argv[2] || 'zh'
const root = mode === 'yw' ? path.join(REPO, 'yuanwen') : REPO
const outPath = path.join(HERE, '..', 'results', `render-${mode}.jsonl`)
fs.mkdirSync(path.dirname(outPath), { recursive: true })

const SENTINEL = /@@MJ([A-Za-z0-9_-]+)@@/g
const PAREN = /\\\(([^]*?)\\\)/g
let idx = 0
const out = fs.createWriteStream(outPath)

for (const letter of fs.readdirSync(root).sort()) {
  const dir = path.join(root, letter)
  if (!(letter.length === 1 && /[a-z]/.test(letter)) || !fs.statSync(dir).isDirectory()) continue
  for (const name of fs.readdirSync(dir).sort()) {
    if (!name.endsWith('.md')) continue
    const rel = `${letter}/${name}`
    const src = fs.readFileSync(path.join(dir, name), 'utf8')
    const prot = protectMath(src)
    let i = 0
    for (const m of prot.matchAll(SENTINEL)) {
      const latex = Buffer.from(m[1], 'base64url').toString('utf8')
      const kind = latex.startsWith('$$') ? 'display' : 'inline'
      out.write(JSON.stringify({ f: rel, i: i++, k: kind, x: latex }) + '\n')
    }
    for (const m of src.matchAll(PAREN)) {
      out.write(JSON.stringify({ f: rel, i: -1, k: 'paren', x: m[0] }) + '\n')
    }
    idx++
  }
}
out.end(() => console.log('files:', idx, '→', outPath))

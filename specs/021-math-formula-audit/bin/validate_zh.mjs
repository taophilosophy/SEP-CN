// 021 译文侧可渲染性验证（逐文件归因）。
// 读 render-zh.jsonl，用 mathjax-full（严格：无 noundefined/noerrors）逐条编译，
// 失败项按文件聚合，输出 results/zh-render-fail.jsonl 与汇总。
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createRequire } from 'node:module'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.resolve(HERE, '..', '..', '..')
const RESULTS = path.join(HERE, '..', 'results')
const require2 = createRequire(path.join(REPO, 'state', 'mathval', 'package.json'))

const { liteAdaptor } = require2('mathjax-full/js/adaptors/liteAdaptor.js')
const { RegisterHTMLHandler } = require2('mathjax-full/js/handlers/html.js')
const { mathjax } = require2('mathjax-full/js/mathjax.js')
const { TeX } = require2('mathjax-full/js/input/tex.js')
const { SVG } = require2('mathjax-full/js/output/svg.js')
const { AllPackages } = require2('mathjax-full/js/input/tex/AllPackages.js')

const adaptor = liteAdaptor({ fontSize: 16 })
RegisterHTMLHandler(adaptor)
const STRICT = AllPackages.filter((p) => p !== 'noundefined' && p !== 'noerrors')
const tex = new TeX({ packages: STRICT, formatError: (_j, e) => { throw e } })
const svg = new SVG({ fontCache: 'none' })
const doc = mathjax.document('', { InputJax: tex, OutputJax: svg })

function compile(kind, latex) {
  let body = latex
  if (kind === 'display') {
    if (body.startsWith('$$') && body.endsWith('$$')) body = body.slice(2, -2)
    else if (body.startsWith('\\[') && body.endsWith('\\]')) body = body.slice(2, -2)
  } else {
    if (body.startsWith('\\(') && body.endsWith('\\)')) body = body.slice(2, -2)
    else if (body.startsWith('$') && body.endsWith('$')) body = body.slice(1, -1)
  }
  try {
    doc.convert(body, { end: { input: true }, display: kind === 'display' })
    return null
  } catch (e) {
    return String((e && e.message) || e).slice(0, 200)
  }
}

const lines = fs.readFileSync(path.join(RESULTS, 'render-zh.jsonl'), 'utf8').split('\n')
const out = fs.createWriteStream(path.join(RESULTS, 'zh-render-fail.jsonl'))
const byFile = new Map()
const seen = new Set()
let total = 0
let fails = 0
for (const line of lines) {
  if (!line) continue
  const r = JSON.parse(line)
  if (r.k === 'paren') continue
  total++
  const key = r.k + '\x00' + r.x
  if (seen.has(key)) continue
  seen.add(key)
  const err = compile(r.k, r.x)
  if (err) {
    fails++
    byFile.set(r.f, (byFile.get(r.f) || 0) + 1)
    out.write(JSON.stringify({ f: r.f, i: r.i, k: r.k, x: r.x.slice(0, 300), err }) + '\n')
  }
}
out.end(() => {
  const top = [...byFile.entries()].sort((a, b) => b[1] - a[1])
  console.log(JSON.stringify({ total, unique_fails: fails, files: byFile.size }, null, 1))
  for (const [f, n] of top.slice(0, 20)) console.log(n, f)
})

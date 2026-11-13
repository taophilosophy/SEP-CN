// 021 en/ 侧可渲染性验证：按各词条 local.js 宏表注入后逐条编译。
// SEP 页在 SEP 站点由 MathJax v2 + 该词条宏表渲染；本验证以 v3 等价口径
// 判定「上游语义下是否可渲染」，失败项即上游/快照级缺陷。
// 输入 en-formulas.jsonl（快照）与 macro-table.json；输出 results/en-render-fail.jsonl
import fs from 'node:fs'
import path from 'node:path'
import { createRequire } from 'node:module'
import { fileURLToPath } from 'node:url'

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
const macroTable = JSON.parse(fs.readFileSync(path.join(RESULTS, 'macro-table.json'), 'utf8'))
const svg = new SVG({ fontCache: 'none' })

// 每个词条一套 TeX（宏表不同）；缓存
const docs = new Map()
function docFor(slug) {
  if (docs.has(slug)) return docs.get(slug)
  const spec = macroTable[slug] || {}
  const macros = {}
  for (const [k, v] of Object.entries(spec)) {
    macros[k] = v.n ? [v.tmpl, v.n] : v.tmpl
  }
  const tex = new TeX({ packages: STRICT, macros, formatError: (_j, e) => { throw e } })
  const d = mathjax.document('', { InputJax: tex, OutputJax: svg })
  docs.set(slug, d)
  return d
}

function bodyOf(kind, latex) {
  let b = latex
  if (kind === 'display') {
    if (b.startsWith('$$') && b.endsWith('$$')) return b.slice(2, -2)
    if (b.startsWith('\\[') && b.endsWith('\\]')) return b.slice(2, -2)
  } else {
    if (b.startsWith('\\(') && b.endsWith('\\)')) return b.slice(2, -2)
    if (b.startsWith('$') && b.endsWith('$')) return b.slice(1, -1)
  }
  return b
}

const rows = fs.readFileSync(path.join(RESULTS, 'en-formulas.jsonl'), 'utf8')
  .split('\n').filter(Boolean).map((l) => JSON.parse(l))
const out = fs.createWriteStream(path.join(RESULTS, 'en-render-fail.jsonl'))
const bySlug = new Map()
const perSlug = new Map()
let total = 0
let fails = 0
const uniqueFail = new Set()
for (const r of rows) {
  const slug = r.f.split('/')[0]
  perSlug.set(slug, (perSlug.get(slug) || 0) + 1)
  const key = slug + '\x00' + r.k + '\x00' + r.x
  if (uniqueFail.has(key)) continue
  total++
  const body = bodyOf(r.k, r.x)
  try {
    docFor(slug).convert(body, { end: { input: true }, display: r.k === 'display' })
  } catch (e) {
    uniqueFail.add(key)
    fails++
    bySlug.set(slug, (bySlug.get(slug) || 0) + 1)
    out.write(JSON.stringify({ f: r.f, i: r.i, k: r.k, x: r.x.slice(0, 300),
      err: String((e && e.message) || e).slice(0, 200) }) + '\n')
  }
}
out.end(() => {
  console.log(JSON.stringify({ slugs: perSlug.size, formulas: rows.length,
    unique_checked: total, unique_fails: fails, slugs_with_fails: bySlug.size }, null, 1))
  for (const [s, n] of [...bySlug.entries()].sort((a, b) => b[1] - a[1]).slice(0, 15)) console.log(n, s)
})

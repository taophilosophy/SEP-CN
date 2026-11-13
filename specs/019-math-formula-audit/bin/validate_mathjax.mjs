// 019 可渲染性全量验证：mathjax-full 逐条编译（站点 tex-svg 同源 TeX 引擎）。
//
// 输入: results/{en-formulas,render-zh,render-yw}.jsonl（每行 {f,i,k,x}）
// 去重后按 (kind, latex) 编译；formatError 抛错 → 硬错误逐条记录。
// AllPackages 严格口径（未定义宏/真语法错都算失败；noundefined 的红字
// 兜底在站点上仍是视觉缺陷，故不引入）。
// 输出: results/verdicts.jsonl 每行 {k,x,ok,err}（x 为唯一公式串）
//
// 用法: node validate_mathjax.mjs
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
// 严格口径：去掉 noundefined（未定义宏红字仍是站点视觉缺陷）与 noerrors
const STRICT = AllPackages.filter((p) => p !== 'noundefined' && p !== 'noerrors')
const tex = new TeX({ packages: STRICT, formatError: (_jax, err) => { throw err } })
const svg = new SVG({ fontCache: 'none' })
const doc = mathjax.document('', { InputJax: tex, OutputJax: svg })

// 站点配置：inline \( \) 与 $ $，display \[ \] 与 $$ $$
const INPUTS = {
  inline: [['\\(', '\\)'], ['$', '$']],
  display: [['\\[', '\\]'], ['$$', '$$']],
}

function compile(kind, latex) {
  // 抽取产物都带定界符（en: \(\)/\[\]/$$；zh/yw: $/$$），剥壳后编译
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
    return { ok: true }
  } catch (e) {
    return { ok: false, err: String(e && e.message || e).slice(0, 300) }
  }
}

// 1) 读三个来源，去重 (kind, latex)
const unique = new Map()
for (const name of ['en-formulas', 'render-zh', 'render-yw']) {
  const p = path.join(RESULTS, `${name}.jsonl`)
  if (!fs.existsSync(p)) continue
  const lines = fs.readFileSync(p, 'utf8').split('\n')
  for (const line of lines) {
    if (!line) continue
    try {
      const r = JSON.parse(line)
      if (r.k === 'paren') continue
      const key = r.k + '\x00' + r.x
      if (!unique.has(key)) unique.set(key, { k: r.k, x: r.x })
    } catch { /* 跳过坏行，汇总时报 */ }
  }
}
console.error('unique formulas:', unique.size)

// 2) 逐条编译
const out = fs.createWriteStream(path.join(RESULTS, 'verdicts.jsonl'))
let n = 0
for (const { k, x } of unique.values()) {
  const v = compile(k, x)
  out.write(JSON.stringify({ k, x, ok: v.ok, err: v.err || null }) + '\n')
  if (++n % 5000 === 0) console.error('compiled', n)
}
out.end(() => console.error('done', n))

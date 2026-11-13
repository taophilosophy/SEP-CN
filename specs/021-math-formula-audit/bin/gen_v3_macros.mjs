// 021 生成 tools/data/mathjax3-macros.json：SEP 宏名中 v3 标准包即可编译者
// （这些名字在译文里保留也照样渲染；其余 SEP 宏名残留即红字，门禁须拦）。
import fs from 'node:fs'
import path from 'node:path'
import { createRequire } from 'node:module'
import { fileURLToPath } from 'node:url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.resolve(HERE, '..', '..', '..')
const require2 = createRequire(path.join(REPO, 'state', 'mathval', 'package.json'))
const { liteAdaptor } = require2('mathjax-full/js/adaptors/liteAdaptor.js')
const { RegisterHTMLHandler } = require2('mathjax-full/js/handlers/html.js')
const { mathjax } = require2('mathjax-full/js/mathjax.js')
const { TeX } = require2('mathjax-full/js/input/tex.js')
const { SVG } = require2('mathjax-full/js/output/svg.js')
const { AllPackages } = require2('mathjax-full/js/input/tex/AllPackages.js')

RegisterHTMLHandler(liteAdaptor())
const STRICT = AllPackages.filter((p) => p !== 'noundefined' && p !== 'noerrors')
 const tex = new TeX({ packages: STRICT, formatError: (_j, e) => { throw e } })
const doc = mathjax.document('', { InputJax: tex, OutputJax: new SVG({ fontCache: 'none' }) })

const table = JSON.parse(fs.readFileSync(path.join(HERE, '..', 'results', 'macro-table.json'), 'utf8'))
const names = new Set()
for (const spec of Object.values(table)) for (const k of Object.keys(spec)) names.add(k)

const ok = []
const need = []
for (const name of [...names].sort()) {
  let out = ''
  try {
    out = doc.convert(`\\${name}`, { end: { input: true }, display: false })
  } catch (e) {
    need.push(name)
    continue
  }
  // 未定义宏在 AllPackages 下走 noundefined 红字（merror），据此判失败
  if (/merror|Undefined control sequence/.test(out)) need.push(name)
  else ok.push(name)
}
const dest = path.join(REPO, 'tools', 'data', 'mathjax3-macros.json')
fs.writeFileSync(dest, JSON.stringify({ standard: ok, needs_expansion: need }, null, 1) + '\n')
console.log('names:', names.size, 'standard:', ok.length, 'needs_expansion:', need.length)
console.log('needs sample:', need.slice(0, 20).join(' '))

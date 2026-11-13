// 021 最小复现：定位 MathJax v3 对 反引号/撇号 的崩溃触发条件
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

const adaptor = liteAdaptor({ fontSize: 16 })
RegisterHTMLHandler(adaptor)
const tex = new TeX({ packages: AllPackages, formatError: (_j, e) => { throw e } })
const doc = mathjax.document('', { InputJax: tex, OutputJax: new SVG({ fontCache: 'none' }) })

const samples = [
  '`v',
  '`v' + "'",
  'a`b',
  '\\sigma(`v)',
  '\\sigma(`v{\\text{’}})',
  '`\\text{four}',
  '`\\text{four}{\\text{’}}',
  '{\\text{’}}',
  'a{\\text{’}}',
  '`a{\\text{’}}',
  '\\llbracket `a ]\\rrbracket',
]
for (const s of samples) {
  try {
    doc.convert(s, { end: { input: true }, display: false })
    console.log('OK  ', JSON.stringify(s))
  } catch (e) {
    console.log('FAIL', JSON.stringify(s), '→', String(e.message || e).slice(0, 70))
  }
}

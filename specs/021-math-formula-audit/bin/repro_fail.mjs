// 021 复现：编译 zh-render-fail.jsonl 中剩余失败项（原样串）
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

const adaptor = liteAdaptor({ fontSize: 16 })
RegisterHTMLHandler(adaptor)
const tex = new TeX({ packages: AllPackages, formatError: (_j, e) => { throw e } })
const doc = mathjax.document('', { InputJax: tex, OutputJax: new SVG({ fontCache: 'none' }) })

const rows = fs.readFileSync(path.join(HERE, '..', 'results', 'zh-render-fail.jsonl'), 'utf8')
  .split('\n').filter(Boolean).map((l) => JSON.parse(l))
for (const r of rows) {
  const tryIt = (s) => {
    try { doc.convert(s, { end: { input: true }, display: r.k === 'display' }); return 'OK' }
    catch (e) { return 'FAIL ' + String(e.message || e).slice(0, 60) }
  }
  let body = r.x
  if (body.startsWith('$')) body = body.replace(/^\$+/, '').replace(/\$+$/, '')
  console.log(r.f, r.i, tryIt(body))
  // 二分定位：逐字符去掉前半，看何时转 OK
  let lo = 0, hi = body.length
  if (tryIt(body).startsWith('FAIL')) {
    for (let cut = 1; cut < Math.min(body.length, 40); cut++) {
      const v = tryIt(body.slice(cut))
      if (v === 'OK') { console.log('   去掉前', cut, '字符后 OK；前段=', JSON.stringify(body.slice(0, cut))); break }
    }
  }
}

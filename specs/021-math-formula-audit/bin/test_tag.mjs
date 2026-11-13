// 021 验证：tag 内容与 text 内 $ 数学在 v3 的编译表现
import path from 'node:path'
import { createRequire } from 'node:module'

const req = createRequire(path.join(process.cwd(), 'state/mathval/package.json'))
const { liteAdaptor } = req('mathjax-full/js/adaptors/liteAdaptor.js')
const { RegisterHTMLHandler } = req('mathjax-full/js/handlers/html.js')
const { mathjax } = req('mathjax-full/js/mathjax.js')
const { TeX } = req('mathjax-full/js/input/tex.js')
const { SVG } = req('mathjax-full/js/output/svg.js')
const { AllPackages } = req('mathjax-full/js/input/tex/AllPackages.js')

RegisterHTMLHandler(liteAdaptor())
const tex = new TeX({
  packages: AllPackages.filter((p) => p !== 'noundefined' && p !== 'noerrors'),
  formatError: (_j, e) => { throw e },
})
const doc = mathjax.document('', { InputJax: tex, OutputJax: new SVG({ fontCache: 'none' }) })

const cases = [
  String.raw`\tag{\({\bf KS}\)} \exists \alpha`,
  String.raw`\tag{{\bf KS}} \exists \alpha`,
  String.raw`\tag{KS} \exists \alpha`,
  String.raw`\tag{\(\Pi^0_1\)} A`,
  String.raw`\tag{\(\Pi^0_1\)}`,
  String.raw`\text{if $x$ is a rational number}`,
  String.raw`\textrm{($>$-asymmetry)}`,
  String.raw`\text{from $A$ and $(A \rightarrow B)$ infer $B$}`,
]
for (const s of cases) {
  try {
    doc.convert(s, { end: { input: true }, display: true })
    console.log('OK  ', s)
  } catch (e) {
    console.log('FAIL', s, '→', String(e.message).slice(0, 60))
  }
}

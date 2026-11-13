// 019 决定性实测：MathJax v2（SEP 所用版本）对 \amp \lamp \osim 等宏的真实反应。
// 用 v2 的 node 组件（MathJax 2.7 支持 require，配置 TeX-MML-AM_CHTML 同 SEP）。
const path = require('node:path')
const { MathJax } = require('/c/Users/ykla/Documents/SEP-CN/state/mathval/node_modules/mathjax/MathJax.js')

const samples = [
  'a \\amp b',
  'A \\lamp B',
  'a \\osim b',
  '\\bs A',
  '\\rO(A)',
  '\\sfx{S}',
  'x \\amp y',
]

MathJax.Hub.Config({
  tex2jax: { inlineMath: [['\\(', '\\)']] },
  jax: ['input/TeX', 'output/SVG'],
  SVG: { scale: 100, font: 'STIX-Web', linebreaks: { automatic: true } },
  showProcessingMessages: false,
  messageStyle: 'none',
})

MathJax.Hub.Register.StartupHook('End', () => {
  for (const s of samples) {
    try {
      const node = MathJax.Hub.getAllJax()
      const script = MathJax.HTML.Element('script', { type: 'math/tex' }, [s])
      const jax = MathJax.Hub.getJaxFor(MathJax.Hub.queue.pending ? null : null)
      // 走 Queue：把公式塞进一个临时元素再排版
      const el = MathJax.HTML.Element('span', {}, ['\\(', s, '\\)'])
      document.body.appendChild(el)
      MathJax.Hub.Queue(['Typeset', MathJax.Hub, el])
      MathJax.Hub.Queue(() => {
        const out = el.innerHTML
        const bad = /merror|Undefined control sequence|Math input error/.test(out)
        console.log(JSON.stringify({ s, bad, snippet: out.slice(0, 80) }))
      })
    } catch (e) {
      console.log(JSON.stringify({ s, bad: true, err: String(e) }))
    }
  }
})

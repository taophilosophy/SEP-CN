// 021 定位器：找出被 protectMath 判为公式、但内容可疑（含中文/超长）的段。
// 用法: node find_suspect_spans.mjs <letter/slug.md>
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { protectMath } from '../../../.vitepress/math-plugin.mjs'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.resolve(HERE, '..', '..', '..')
const rel = process.argv[2]
const src = fs.readFileSync(path.join(REPO, rel), 'utf8')
const prot = protectMath(src)
const SENTINEL = /@@MJ([A-Za-z0-9_-]+)@@/g
let n = 0
for (const m of prot.matchAll(SENTINEL)) {
  const latex = Buffer.from(m[1], 'base64url').toString('utf8')
  const cjk = (latex.match(/[\u4e00-\u9fff]/g) || []).length
  if (cjk > 2 || latex.length > 400) {
    const before = prot.slice(Math.max(0, m.index - 90), m.index).replace(/@@MJ[A-Za-z0-9_-]+@@/g, '«…»')
    console.log(`#${n} len=${latex.length} cjk=${cjk}`)
    console.log('  before:', JSON.stringify(before.slice(-90)))
    console.log('  span  :', JSON.stringify(latex.slice(0, 200)))
  }
  n++
}
console.log('total spans:', n)

// 021 D6 精确化：用站点 protectMath 之后的残余 $ 判定不成对（渲染真值口径）。
// protectMath 会把参与配对的公式换成哨兵；剩下的裸 $ 就是站上可见的未配对 $。
// 产 results/d6-unpaired.jsonl（每行 {f,count,samples}）
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { protectMath } from '../../../.vitepress/math-plugin.mjs'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const REPO = path.resolve(HERE, '..', '..', '..')
const out = fs.createWriteStream(path.join(HERE, '..', 'results', 'd6-unpaired.jsonl'))
let files = 0

for (const letter of fs.readdirSync(REPO).sort()) {
  const dir = path.join(REPO, letter)
  if (!(letter.length === 1 && /[a-z]/.test(letter)) || !fs.statSync(dir).isDirectory()) continue
  for (const name of fs.readdirSync(dir).sort()) {
    if (!name.endsWith('.md')) continue
    const src = fs.readFileSync(path.join(dir, name), 'utf8')
    const prot = protectMath(src)
    const leftover = []
    for (const [i, line] of prot.split('\n').entries()) {
      const stripped = line.replace(/@@MJ[A-Za-z0-9_-]+@@/g, '')
      if (stripped.includes('$')) leftover.push([i + 1, stripped.slice(0, 120)])
    }
    if (leftover.length) {
      files++
      out.write(JSON.stringify({ f: `${letter}/${name}`, count: leftover.length,
        samples: leftover.slice(0, 5) }) + '\n')
    }
  }
}
out.end(() => console.log('files with leftover $:', files))

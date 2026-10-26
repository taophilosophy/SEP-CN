// 从抓下的 book.bsdcn.org HTML 中提取 GitBook 主题色（一次性脚本，用完即删）
import fs from 'node:fs'

const html = fs.readFileSync(
  process.env.TEMP.replace(/\\/g, '/') + '/bsdcn.html',
  'utf8',
)

// 1) 常见 GitBook 新版变量名
const varNames = [
  '--ts-color-primary',
  '--primary-color',
  '--color-primary',
  '--ts-color-accent',
  '--site-primary',
  'primaryColor',
  '--ts-var-color',
]
for (const v of varNames) {
  const re = new RegExp(`${v.replace(/-/g, '\\-')}[^,;"}]*`, 'g')
  const hits = [...html.matchAll(re)].slice(0, 6)
  for (const h of hits) console.log(v, '→', h[0].slice(0, 120))
}

// 2) RSC 载荷里出现的 hex 颜色及其上下文
const hexRe = /#([0-9a-fA-F]{6})\b/g
const ctx = new Map()
let m
while ((m = hexRe.exec(html))) {
  const start = Math.max(0, m.index - 80)
  const around = html.slice(start, m.index + 8).replace(/\s+/g, ' ')
  ctx.set(m[0].toLowerCase(), (ctx.get(m[0].toLowerCase()) || 0) + 1)
  if ((ctx.get(m[0].toLowerCase()) || 0) <= 2) console.log('HEX', m[0], '…', around.slice(-140))
}

// 3) 明暗模式标记
for (const kw of ['prefers-color-scheme', 'darkMode', '"dark"', 'lightMode']) {
  const i = html.indexOf(kw)
  if (i >= 0) console.log('KW', kw, '…', html.slice(Math.max(0, i - 100), i + 160).replace(/\s+/g, ' '))
}

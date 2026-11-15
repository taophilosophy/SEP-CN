// 合并分片构建产物（CI 并行，见 config.mts 的 SEP_SHARD 说明）。
//
// 用法：bun .vitepress/merge-shards.mjs [shardDir...]
//   默认 dist-af dist-gm dist-ns dist-tz（相对 .vitepress/），合并写入 .vitepress/dist。
//
// 做四件事：
//   1. 把各片产物叠加进 dist（哈希文件名不冲突；同名文件以先到者为准）；
//   2. hashmap.json 取并集——客户端路由在本片哈希表缺项时会回退 fetch
//      /hashmap.json 重试（vitepress/dist/client/app/router.js），并集后跨片跳转正常；
//   3. sitemap.xml 把各片的 <url> 条目拼回一份（各片 hostname 相同，格式一致）；
//   4. 对整份 dist 跑一次 pagefind（分片时 config 里不挂插件，参数与插件保持一致：
//      --exclude-selectors "div.aside, a.header-anchor"）。
import { cpSync, existsSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from 'node:fs'
import path from 'node:path'
import { execSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

const vpDir = path.dirname(fileURLToPath(import.meta.url))
const outDir = path.join(vpDir, 'dist')

const args = process.argv.slice(2)
// 显式参数按 cwd（仓库根）解析——CI 传的是 docs/.vitepress/shards/dist-*；
// 无参数时用 .vitepress/ 下的默认分片目录（本地调试）。
const shardDirs = args.length
  ? args.map((s) => (path.isAbsolute(s) ? s : path.resolve(process.cwd(), s)))
  : ['dist-ad', 'dist-ek', 'dist-lp', 'dist-qz'].map((s) => path.join(vpDir, s))

const existing = shardDirs.filter((d) => existsSync(path.join(d, 'hashmap.json')))
if (!existing.length) {
  console.error('[merge-shards] 没有可合并的分片产物：' + shardDirs.join(', '))
  process.exit(1)
}

rmSync(outDir, { recursive: true, force: true })
for (const dir of existing) {
  cpSync(dir, outDir, { recursive: true, force: true })
  console.log(`[merge-shards] + ${path.basename(dir)}`)
}

// ---- hashmap 并集 ----
const hashMap = {}
for (const dir of existing) {
  Object.assign(hashMap, JSON.parse(readFileSync(path.join(dir, 'hashmap.json'), 'utf8')))
}
writeFileSync(path.join(outDir, 'hashmap.json'), JSON.stringify(hashMap))
console.log(`[merge-shards] hashmap ${Object.keys(hashMap).length} 条`)

// ---- sitemap 拼接 ----
const urlRe = /<url>[\s\S]*?<\/url>/g
const seen = new Set()
const urls = []
for (const dir of existing) {
  const file = path.join(dir, 'sitemap.xml')
  if (!existsSync(file)) continue
  for (const m of readFileSync(file, 'utf8').match(urlRe) ?? []) {
    if (seen.has(m)) continue
    seen.add(m)
    urls.push(m)
  }
}
if (urls.length) {
  const header =
    '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" ' +
    'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" ' +
    'xmlns:xhtml="http://www.w3.org/1999/xhtml" ' +
    'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" ' +
    'xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">'
  writeFileSync(path.join(outDir, 'sitemap.xml'), header + urls.join('') + '</urlset>')
  console.log(`[merge-shards] sitemap ${urls.length} 条`)
}

// ---- pagefind：合并后统一索引一次 ----
console.log('[merge-shards] pagefind …')
execSync(
  `bunx pagefind --site "${outDir}" --exclude-selectors "div.aside, a.header-anchor"`,
  { stdio: 'inherit' },
)

// ---- 统计 ----
function countHtml(dir) {
  let n = 0
  for (const name of readdirSync(dir)) {
    const p = path.join(dir, name)
    if (statSync(p).isDirectory()) n += countHtml(p)
    else if (name.endsWith('.html')) n++
  }
  return n
}
console.log(`[merge-shards] dist ${countHtml(outDir)} 个页面 → ${outDir}`)

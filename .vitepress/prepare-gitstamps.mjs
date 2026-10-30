// git 时间戳预计算（B1，2026-10-30）
//
// 内置 lastUpdated 会在构建时逐页查询 git 历史（2400+ 页显著拖慢构建）。
// 这里一次全量 `git log --format=%ct --name-only` 生成 路径→最后提交时间(ms)
// 映射写入 .vitepress/git-stamps.json，config.mts 在 transformPageData 注入
// pageData.lastUpdated。文件是派生物，不入库。
import { execSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')

// 与站点无关的大目录不进映射，压体积（yuanwen/ 与字母目录是站点页面，保留）
const EXCLUDE = [
  'en/',
  'node_modules/',
  'baseline/',
  'state/',
  'tasks/',
  'specs/',
  'tools/',
  'script/',
  'rules/',
]

const out = execSync('git log --format=%ct --name-only', {
  cwd: repoRoot,
  maxBuffer: 1 << 28,
}).toString()

// log 按时间倒序：路径首次出现即最后一次提交
const stamps = {}
let ts = 0
for (const line of out.split(/\r?\n/)) {
  if (/^\d{9,}$/.test(line)) {
    ts = Number(line) * 1000
    continue
  }
  if (!line || !ts) continue
  if (line.startsWith('.')) continue
  if (EXCLUDE.some((p) => line.startsWith(p))) continue
  const p = line.replace(/\\/g, '/')
  if (!stamps[p]) stamps[p] = ts
}

fs.writeFileSync(
  path.join(repoRoot, '.vitepress', 'git-stamps.json'),
  JSON.stringify(stamps),
)
console.log(`[prepare-gitstamps] ${Object.keys(stamps).length} paths`)

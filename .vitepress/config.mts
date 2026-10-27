import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { mathPlugin } from './math-plugin.mjs'

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')

// ------------------------------------------------------------- SUMMARY 解析 --

type Item = { kind: 'section' | 'item'; title: string; href?: string; depth: number }

function parseSummary(file: string): Item[] {
  const out: Item[] = []
  if (!fs.existsSync(file)) return out
  const text = fs.readFileSync(file, 'utf8')
  for (const line of text.split(/\r?\n/)) {
    if (/^##\s+/.test(line)) {
      out.push({ kind: 'section', title: line.replace(/^##\s+/, '').trim(), depth: 0 })
      continue
    }
    const m = /^(\s*)\*\s+\[(.+?)\]\((\S+?)\)\s*$/.exec(line)
    if (m) {
      out.push({
        kind: 'item',
        title: m[2],
        href: m[3].replace(/^\.\//, ''),
        depth: Math.floor(m[1].replace(/\t/g, '  ').length / 2),
      })
    }
  }
  return out
}

/** SUMMARY 标题里的 markdown 转义（如 \[Abailard\]）还原为纯文本 */
function cleanTitle(t: string): string {
  return t.replace(/\\([\\`*_{}[\]()#+.!-])/g, '$1').trim()
}

function sidebarLink(href: string): string {
  if (/^https?:\/\//.test(href)) return href
  if (href === 'README.md') return '/'
  return '/' + href
}

type VpItem = { text: string; link?: string; collapsed?: boolean; items?: VpItem[] }

function toTree(items: Item[]): VpItem[] {
  const root: VpItem[] = []
  const stack: { depth: number; node: VpItem }[] = []
  for (const it of items) {
    if (it.kind !== 'item' || !it.href) continue
    const node: VpItem = { text: cleanTitle(it.title), link: sidebarLink(it.href) }
    while (stack.length && stack[stack.length - 1].depth >= it.depth) stack.pop()
    if (stack.length) {
      const parent = stack[stack.length - 1].node
      ;(parent.items ||= []).push(node)
    } else {
      root.push(node)
    }
    stack.push({ depth: it.depth, node })
  }
  const markCollapsed = (nodes: VpItem[]) => {
    for (const n of nodes)
      if (n.items?.length) {
        n.collapsed = true
        markCollapsed(n.items)
      }
  }
  markCollapsed(root)
  return root
}

function buildSidebar(items: Item[]): (VpItem | { text: string; collapsed: boolean; items: VpItem[] })[] {
  const result: any[] = []
  let current: { text: string; items: Item[] } | null = null
  const flush = () => {
    if (current) {
      result.push({ text: current.text, collapsed: true, items: toTree(current.items) })
      current = null
    }
  }
  for (const it of items) {
    if (it.kind === 'section') {
      flush()
      current = { text: cleanTitle(it.title), items: [] }
    } else {
      ;(current ? current.items : []).push(it)
      if (!current) {
        // 第一个 ## 之前的顶层条目（首页、分类目录）直接平铺
        if (it.kind === 'item' && it.href) result.push({ text: cleanTitle(it.title), link: sidebarLink(it.href) })
      }
    }
  }
  flush()
  return result
}

const zhItems = parseSummary(path.join(repoRoot, 'SUMMARY.md'))
const enItems = parseSummary(path.join(repoRoot, 'yuanwen', 'SUMMARY.md'))

// ------------------------------------------------------- 中英页面配对（按序对齐）--

const zhToEn: Record<string, string> = {}
const enToZh: Record<string, string> = {}
const enGroups: Record<string, VpItem[]> = {}
const flatZh = zhItems.filter((i) => i.kind === 'item' && i.href)
const flatEn = enItems.filter((i) => i.kind === 'item' && i.href)
for (let i = 0; i < Math.min(flatZh.length, flatEn.length); i++) {
  const zh = flatZh[i]
  const en = flatEn[i]
  if (zh.title !== en.title) continue // 结构漂移保护：标题不一致就不配对
  if (!/^yuanwen\/.+\.md$/.test(en.href!)) continue
  zhToEn[zh.href!] = en.href!
  enToZh[en.href!] = zh.href!
  const letter = en.href!.split('/')[1] || '其他'
  ;(enGroups[letter] ||= []).push({ text: cleanTitle(zh.title), link: '/' + en.href! })
}

const enSidebar: any[] = Object.keys(enGroups)
  .sort()
  .map((letter) => ({ text: letter.toUpperCase(), collapsed: true, items: enGroups[letter] }))

// ------------------------------------------------------------------- 数学配置 --

const mathjaxConfig = {
  tex: {
    inlineMath: [
      ['\\(', '\\)'],
      ['$', '$'],
    ],
    displayMath: [
      ['\\[', '\\]'],
      ['$$', '$$'],
    ],
  },
  svg: { fontCache: 'global' },
  options: { enableMenu: false },
  startup: { typeset: false }, // 由主题组件在路由变化后手动排版（SPA）
}

export default defineConfig({
  lang: 'zh-CN',
  title: 'SEP 简体中文版',
  description: '斯坦福哲学百科全书（SEP）简体中文翻译项目，与英文原文对照阅读',
  ignoreDeadLinks: true,
  // 非站点目录（治理/管线/原始物）不作为页面参与构建
  srcExclude: [
    'en/**',
    'specs/**',
    '.specify/**',
    'tools/**',
    'tasks/**',
    'baseline/**',
    'script/**',
    'state/**',
    'rules/**',
    '.github/**',
    '.zcode/**',
    'AGENTS.md',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'yuanwen/SUMMARY.md',
  ],
  head: [
    ['link', { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    ['script', {}, `window.MathJax = ${JSON.stringify(mathjaxConfig)}`],
    ['script', { src: '/mathjax/tex-svg.js', defer: '' }],
    // 嵌入双语对照 iframe 中的页面隐藏站点框架
    ['script', {}, `if(window.parent!==window){document.documentElement.classList.add('in-iframe')}`],
  ],
  markdown: {
    config(md) {
      md.use(mathPlugin)
    },
  },
  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'SEP 简体中文版',
    nav: [
      { text: '首页', link: '/' },
      { text: '分类目录', link: '/mu-lu-s' },
      { text: '词汇表', link: '/qian-yan/ci-hui-biao' },
      { text: '术语对照', link: '/yi-zhe-shuo-ming' },
    ],
    sidebar: {
      '/yuanwen/': enSidebar,
      '/': buildSidebar(zhItems),
    },
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    socialLinks: [{ icon: 'github', link: 'https://github.com/taophilosophy/SEP-CN' }],
    footer: {
      message: '《斯坦福哲学百科全书》简体中文翻译项目 · 支持与英文原文对照阅读',
      copyright: 'Copyright © 2024 ykla · 以 BSD-2-Clause 许可证发布',
    },
    search: {
      provider: 'local',
      options: {
        miniSearch: {
          // 原文库很大（2300+ 页、正文约 240MB），完整索引会超出 V8 字符串上限
          // （"Invalid string length"），浏览器端也不可用。自管分节：
          // 剥离公式哨兵、单节 4KB、单页 16KB 上限，把索引压到可服务体积。
          *_splitIntoSections(file, html) {
            const headingRegex = /<h(\d*).*?>(.*?<a.*? href="#.*?".*?>.*?<\/a>)<\/h\1>/gi
            const headingContentRegex = /(.*)<a.*? href="#(.*?)".*?>.*?<\/a>/i
            const clearTags = (s) =>
              s.replace(/<[^>]*>/g, '').replace(/@@M[A-Z][A-Za-z0-9_-]+@@/g, ' ')
            const PAGE_CAP = 3500
            const SECTION_CAP = 1500
            let total = 0
            const parts = html.split(headingRegex)
            parts.shift()
            let parentTitles = []
            for (let i = 0; i < parts.length; i += 3) {
              const level = parseInt(parts[i]) - 1
              const m = headingContentRegex.exec(parts[i + 1] || '')
              const title = (m?.[1] ?? '').replace(/<[^>]*>/g, '').trim()
              const content = parts[i + 2]
              if (!title || !content) continue
              const text = clearTags(content)
              if (!text) continue
              const titles = parentTitles.slice(0, level)
              titles[level] = title
              if (total >= PAGE_CAP) break
              const kept = text.slice(0, Math.max(0, Math.min(SECTION_CAP, PAGE_CAP - total)))
              total += kept.length
              yield { anchor: m?.[2] ?? '', titles, text: kept }
              if (level === 0) parentTitles = [title]
              else parentTitles[level] = title
            }
            // 无标题页面（如目录页）整体作为一节，保证条目标题可被搜到
            if (!parts.length) {
              const text = clearTags(html).slice(0, Math.max(0, PAGE_CAP - total))
              if (text) yield { anchor: '', titles: [], text }
            }
          },
        },
        locales: {
          root: {
            translations: {
              button: { buttonText: '搜索词条', buttonAriaLabel: '搜索词条' },
              modal: {
                noResultsText: '未找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' },
              },
            },
          },
        },
      },
    },
  },
  transformPageData(pageData) {
    const rel = pageData.relativePath.replace(/\\/g, '/')
    const en = zhToEn[rel]
    if (en) pageData.frontmatter.enPath = '/' + en.replace(/\.md$/, '')
    const zh = enToZh[rel]
    if (zh) pageData.frontmatter.zhPath = '/' + zh.replace(/\.md$/, '')
  },
  vite: {
    plugins: [
      {
        name: 'sep-readme-index-fallback',
        // VitePress 2.0 alpha 的 dev 端只按 /index.md 解析页面，
        // 本仓库沿用 GitBook 的 README.md 作为首页/目录首页（build 端能正确映射）。
        // 这里把 dev 请求里的 index.md 改写为 README.md（存在时），保持两端一致。
        configureServer(server) {
          server.middlewares.use((req, _res, next) => {
            if (req.url) {
              const [pathname, query] = req.url.split('?')
              if (/(^|\/)index\.md$/.test(pathname)) {
                const candidate = decodeURI(pathname).replace(/index\.md$/, 'README.md')
                if (!candidate.includes('..') && fs.existsSync(path.join(repoRoot, candidate))) {
                  req.url = candidate + (query ? '?' + query : '')
                }
              }
            }
            next()
          })
        },
      },
    ],
    server: {
      host: '0.0.0.0',
      port: 81,
      strictPort: true,
      watch: {
        // 本仓库所在盘的 ReadDirectoryChangesW 会报 UNKNOWN 错误，改用轮询监听
        usePolling: true,
        interval: 600,
        // 仓库里与站点无关的大目录不监听，降低轮询开销
        ignored: [
          '**/.git/**',
          '**/en/**',
          '**/tools/**',
          '**/state/**',
          '**/tasks/**',
          '**/baseline/**',
          '**/specs/**',
          '**/script/**',
          '**/node_modules/**',
        ],
      },
    },
  },
})

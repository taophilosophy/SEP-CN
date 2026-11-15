import { defineConfig } from 'vitepress'
import { searchForWorkspaceRoot } from 'vite'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { mathPlugin } from './math-plugin.mjs'
import { chineseSearchOptimize, pagefindPlugin } from 'vitepress-plugin-pagefind'

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
// 构建时用 pagefind 做离线全文搜索（索引分块，2400+ 页可控）；
// dev 下没有 pagefind 产物，保留内置 MiniSearch（PAGE_CAP 限流版）
const isBuild = process.argv.includes('build')

// ------------------------------------------------------- 分片构建（CI 并行）--
// SEP_SHARD=ad|ek|lp|qz：四片按字母区间均衡切分（2026-11-16 实测内容页：
// a–d 1164、e–k 1050、l–p 1196、q–z 915，中英两侧合并计；各片另出 404 一页），
// 每片产物写 .vitepress/dist-<shard>，由 .vitepress/merge-shards.mjs 合并 dist、
// 并集 hashmap.json、拼 sitemap 并跑一次 pagefind。
// **死链检查在分片模式照常开启**：跨片链接在本片的 pages 里必然“缺失”，但只
// 要它指向的是本站真实存在的页面就豁免（collectSitePages 扫全仓生成页面集，
// 与构建无关）。页面在全站都不存在时依旧硬失败——检查强度与全量构建一致。
// 根级页面与 1/、qian-yan 等非字母目录只进第一片（ad），其 yuanwen/ 英文镜像同片。
const SHARD_LETTERS: Record<string, string> = {
  ad: 'abcd',
  ek: 'efghijk',
  lp: 'lmnop',
  qz: 'qrstuvwxyz',
}
const ROOT_SHARD_LETTERS = SHARD_LETTERS.ad
const shard = (process.env.SEP_SHARD || '').toLowerCase()
const shardLetters = SHARD_LETTERS[shard]
const isShard = Boolean(shardLetters)
const ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
// 非字母目录（1/ 是 Kant 前德国哲学等的既有落位）——与同名字母目录一样成对处理，
// 中文与 yuanwen/ 英文镜像必须同片，否则某片只有译文没有原文、双语切换指向未构建页。
const NON_LETTER_DIRS = ['1', 'qian-yan', 'guan-yu', 'jian-yi-shu', 'fang-fa-lun']
const isRootShard = shardLetters === ROOT_SHARD_LETTERS
const shardExclude: string[] = isShard
  ? [
      // 非本片字母的词条目录与英文镜像
      ...ALL_LETTERS.split('')
        .filter((l) => !shardLetters!.includes(l))
        .flatMap((l) => [`${l}/**`, `yuanwen/${l}/**`]),
      // 根级页面（README、mu-lu-s、两本登记册、SUMMARY 等）与非字母目录只进首片
      // （ad）；英文侧根级页面（yuanwen/README.md）同理，保持中英同片。
      ...(isRootShard
        ? []
        : [
            '*.md',
            'yuanwen/README.md',
            ...NON_LETTER_DIRS.flatMap((d) => [`${d}/**`, `yuanwen/${d}/**`]),
          ]),
    ]
  : []

// ------------------------------------------------ 版本钉登记册（baseline） --
// baseline/entries.json 是抓取管线登记的单一事实源：slug → source_url /
// pubinfo（首发、实质修订）/ archive_edition（存档版名）/ 源 SHA-256 /
// 中英文档路径。配置加载期读入，transformPageData 按页面路径注入
// frontmatter.srcMeta，主题组件（VersionPin）据此在页脚展示版本钉（#2）。
type SrcMeta = {
  slug: string
  sourceUrl: string
  firstPublished?: string
  substantiveRevision?: string
  edition?: string
  sha256: string
  authors?: string[]
}
const srcByDoc: Record<string, SrcMeta> = {}
try {
  const entriesRaw = JSON.parse(
    fs.readFileSync(path.join(repoRoot, 'baseline', 'entries.json'), 'utf8'),
  ) as { entries?: Record<string, any> }
  for (const e of Object.values(entriesRaw.entries ?? {})) {
    if (!e?.slug) continue
    const meta: SrcMeta = {
      slug: e.slug,
      sourceUrl: e.source_url,
      firstPublished: e.pubinfo?.first_published,
      substantiveRevision: e.pubinfo?.substantive_revision,
      edition: e.archive_edition,
      sha256: e.files?.find((f: any) => f.kind === 'main')?.sha256 || '',
      authors: e.authors || [],
    }
    if (e.zh_doc) srcByDoc[e.zh_doc] = meta
    if (e.yuanwen?.md) srcByDoc[e.yuanwen.md] = meta
  }
} catch {
  // 登记册缺失时静默降级：页面不显示版本钉，不影响构建
}

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
      continue
    }
    // 无链接行（集群占位母行 `* \*分类名`，ADR-0057；别名词条行 `* \*X——见Y`，ADR-0060）
    // 不指向文件：SUMMARY 保留这层层级与索引信息供 GitBook 与结构审计使用，侧栏不渲染
    // 这类行，故此处不产出条目。一旦重新指向文件（README.md 或目标词条），GitBook 会因
    // 「一文件多页」拒绝导入。
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
// yuanwen/SUMMARY.md 的条目 href 相对 yuanwen/ 目录（../ 开头的导航行指向仓库外），
// 统一改写为仓库根相对路径。此前未做此改写时 zhToEn 配对恒为空：对照按钮从不
// 渲染、英文侧栏字母分组取错、链接指到中文页（2026-10-30 实测发现并修复）
for (const it of enItems) {
  if (it.kind === 'item' && it.href && !it.href.startsWith('../') && !/^https?:/.test(it.href)) {
    it.href = 'yuanwen/' + it.href
  }
}

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

// ------------------------------------------------ 侧栏按字母分键（A1） --
// VitePress 按前缀最长匹配取侧栏：词条页只内联本字母条目树（页重 1.2MB→约
// 300KB），非词条页（/、mu-lu-s 等）仍走 '/' 全树。2026-10-30 用户拍板。
const catLink = { text: '分类目录', link: '/mu-lu-s' }

const zhSidebarByLetter: Record<string, any[]> = {}
const byLetter: Record<string, Item[]> = {}
{
  for (const it of zhItems) {
    if (it.kind !== 'item' || !it.href) continue
    const seg = it.href.split('/')[0]
    if (!/^[a-z0-9]$/.test(seg)) continue // 单字符字母/数字桶；qian-yan 等目录页走 slim 索引
    ;(byLetter[seg] ||= []).push(it)
  }
  for (const seg of Object.keys(byLetter).sort()) {
    zhSidebarByLetter[`/${seg}/`] = [
      catLink,
      { text: seg.toUpperCase(), collapsed: true, items: toTree(byLetter[seg]) },
    ]
  }
}

// ------------------------------------------ 非词条页侧栏瘦身（内存/移动端） --
// 全树侧栏在移动端折算 ~2 万 DOM 节点（实测 mu-lu-s 21507 节点），
// 是非词条页内存与渲染的大头。2026-10-30 裁定：非词条页一律 slim——
// 顶部导航行 + 分类目录 + 26 字母首链；多页目录（qian-yan 等）另列自身页面。
// 顶行仅取站首页一行。集群占位母行（`* \*美学 aesthetics`）自 2026-11-15 起是无链接
// 分组行（ADR-0057：GitBook 一文件一页，182 行同指 README.md 会拒绝导入），parseSummary
// 不再为它们产出 href，故此处只可能命中站首页一行；分类目录入口由 catLink 提供，
// 不再单列 mu-lu-s 行以免重复。
const topRows = zhItems
  .filter((i) => i.kind === 'item' && i.href === 'README.md')
  .map((i) => ({ text: cleanTitle(i.title), link: sidebarLink(i.href!) }))

const slimIndexSidebar: any[] = [
  ...topRows,
  catLink,
  ...Object.keys(byLetter)
    .sort()
    .map((seg) => ({
      text: seg.toUpperCase(),
      link: '/' + byLetter[seg][0].href!.replace(/\.md$/, ''),
    })),
]

const dirSidebars: Record<string, any[]> = {}
for (const seg of ['qian-yan', 'guan-yu', 'jian-yi-shu']) {
  const own = zhItems.filter((i) => i.kind === 'item' && i.href?.startsWith(seg + '/'))
  dirSidebars[`/${seg}/`] = [
    catLink,
    ...own.map((i) => ({ text: cleanTitle(i.title), link: sidebarLink(i.href!) })),
  ]
}

const enSidebarByLetter: Record<string, any[]> = {}
for (const letter of Object.keys(enGroups).sort()) {
  enSidebarByLetter[`/yuanwen/${letter}/`] = [
    catLink,
    { text: letter.toUpperCase(), collapsed: true, items: enGroups[letter] },
  ]
}

// ---------------------------------------------- git 时间戳预计算（B1） --
// prepare-gitstamps.mjs 一次全量 git log 生成 路径→最后提交时间(ms) 映射，
// transformPageData 据此注入 pageData.lastUpdated——内置 lastUpdated 的
// 逐页 git 查询（2400+ 页）取消，构建显著提速。缺文件时仅页脚不显示时间。
let gitStamps: Record<string, number> = {}
try {
  gitStamps = JSON.parse(
    fs.readFileSync(path.join(repoRoot, '.vitepress', 'git-stamps.json'), 'utf8'),
  ) as Record<string, number>
} catch {
  gitStamps = {}
}

// SEP 补充材料中文译文尚未落地的页面键（与台账同名，见下方 ignoreDeadLinks 注释）。
// 2026-11-13 全库扫描：31 个目标、49 处引用；英文源与原文镜像齐备，缺的只是译文。
const pendingSupplementPages = [
  'ancient-soul.supplement',
  'axiom-choice.choice-and-type-theory',
  'brouwer.strongcounterex',
  'brouwer.weakcounterex',
  'descartes-works.history',
  'imprecise-probabilities.supplement-formal',
  'imprecise-probabilities.supplement-historical',
  'intrinsic-extrinsic.grounding-theories',
  'intrinsic-extrinsic.non-disjunctive',
  'intrinsic-extrinsic.relational-theory',
  'japanese-aesthetics.ginkakuji',
  'japanese-aesthetics.ginkakuji-kinkakuji',
  'japanese-aesthetics.late-spring',
  'japanese-aesthetics.ryoanji',
  'japanese-aesthetics.splashed-ink',
  'japanese-aesthetics.tokyo-story',
  'kant-judgment.supplement1',
  'kant-judgment.supplement2',
  'kant-judgment.supplement3',
  'kant-judgment.supplement4',
  'kant-judgment.supplement5',
  'kochen-specker.proofvc1',
  'logic-fuzzy.readings-by-topic',
  'logic-relevance.logic-b-dj-dk',
  'logic-relevance.logice',
  'logic-relevance.logicnr',
  'logic-relevance.logicr',
  'logic-relevance.logics',
  'spacetime-holearg.active-passive',
  'spacetime-holearg.gauge',
  'spacetime-holearg.leibniz-equivalence',
]

// 站点页面范围的基础清单（srcExclude 的非分片部分）。分片构建的排除面另见上方
// shardExclude：这里只描述“哪些文件不是站点页面”，与分片无关，故分片模式的死链
// 判定可以直接复用它扫全仓（见 collectSitePages）。
const siteExclude = [
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
  '.qoder/**',
  'AGENTS.md',
  'CONTRIBUTING.md',
  'CODE_OF_CONDUCT.md',
  'yuanwen/SUMMARY.md',
  'yuanwen/SUMMARY-en.md',
]

// 分片模式的死链检查（2026-11-16 用户裁定：必须打开）。
// 分片的 pages 只含本片页面，跨片链接在本片必然“缺失”；这里按与构建相同的排除
// 规则扫全仓 md 得到“全站页面集”，凡指向其中任一页面的链接豁免，全站都不存在的
// 链接照旧按死链硬失败——检查强度与全量构建一致。只扫文件系统、不产出页面。
const sitePages: Set<string> = (() => {
  if (!isShard) return new Set<string>()
  const skipDirs = new Set(['.git', 'node_modules', 'public'])
  const skipFileRels = new Set(siteExclude.filter((e) => !e.endsWith('/**')))
  const skipDirRels = new Set(siteExclude.filter((e) => e.endsWith('/**')).map((e) => e.slice(0, -3)))
  const pages = new Set<string>()
  const walk = (dir: string) => {
    for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
      if (ent.isDirectory()) {
        const rel = path.relative(repoRoot, path.join(dir, ent.name)).split(path.sep).join('/')
        if (skipDirs.has(ent.name) || skipDirRels.has(rel) || ent.name.startsWith('.')) continue
        walk(path.join(dir, ent.name))
      } else if (ent.name.endsWith('.md')) {
        const rel = path.relative(repoRoot, path.join(dir, ent.name)).split(path.sep).join('/')
        if (!skipFileRels.has(rel)) pages.add(rel.replace(/\.md$/, ''))
      }
    }
  }
  walk(repoRoot)
  return pages
})()

// 与 VitePress 内部同口径解析链接（去查询串/锚点与 .md、.html 后缀，目录补 index，
// 相对链接按引用文件所在目录解析），再查全站页面集。
function isExistingSitePage(url: string, fileOrig: string): boolean {
  if (!isShard) return false
  const clean = url.replace(/[?#].*$/, '').replace(/\.(html|md)$/, '')
  const withIndex = clean.endsWith('/') ? `${clean}index` : clean
  const resolved = withIndex.startsWith('/')
    ? withIndex.slice(1)
    : path.relative(repoRoot, path.resolve(path.dirname(fileOrig), withIndex))
  return sitePages.has(resolved.split(path.sep).join('/'))
}

export default defineConfig({
  lang: 'zh-CN',
  title: 'SEP 中文版',
  description: '斯坦福哲学百科全书（SEP）简体中文翻译项目，与英文原文对照阅读',
  // 死链检查：2026-11-13 关闭全局豁免（原为全局放行 true）。
  // VitePress 把死链记为构建硬失败（renderStart 抛错），故下列数组仅登记已核实的存量缺口，
  // 任何新增死链都会阻断构建。台账：
  // specs/005-translation-campaign/results/supplement-translation-gap-2026-11-13.md
  // 收敛规则：每落地一个 <letter>/<slug>.<x>.md 译文，即从 pendingSupplementPages 删除对应一条；
  // 清空后删除本配置项，恢复零豁免。
  // VitePress shouldIgnoreDeadLink 传入的 url 带 ./ 前缀且已去 .md 后缀，故统一加前缀。
  // 分片构建下跨片链接必然“缺失”：靠数组末尾的 isExistingSitePage 豁免指向全站
  // 真实页面的链接，全站都不存在的链接仍判死链（见上方说明）。
  ignoreDeadLinks: [
    ...pendingSupplementPages.map((s) => `./${s}`),
    // 英文原文镜像中的受限量词记号被 markdown-it 误判为链接；ADR-0007 要求原文逐字符一致，不改源。
    './Unmarried(*x*,*w*)',
    './Unmarried',
    './*Gx*',
    './f',
    isExistingSitePage,
  ],
  // 2026-10-29 逐项选定：URL 去 .html；词条页标签加站名后缀；显示更新时间。
  // 注意：2.0 的 titleTemplate 占位符是 :title（%s 是 1.x 语法，会原样出现在标签页标题里）。
  // lastUpdated 不用内置逐页 git 查询（B1）：关闭后由 transformPageData 注入
  // git-stamps.json 预计算值，主题页脚照常显示（VPDocFooter 只看 page.lastUpdated）。
  cleanUrls: true,
  // 分片构建各写自己的产物目录，避免并行任务互踩（见上方 SEP_SHARD 说明）
  ...(isShard ? { outDir: `.vitepress/dist-${shard}` } : {}),
  titleTemplate: ':title · SEP 中文版',
  // sitemap：2026-10-29 定启用；本站部署在 taophilosophy.github.io 的站点根（base '/'），
  // hostname 与之对齐（2026-11-16 实测部署地址）。分片构建各片自产 sitemap，合并时拼回一份。
  sitemap: { hostname: 'https://taophilosophy.github.io/' },
  // 非站点目录（治理/管线/原始物）不作为页面参与构建
  srcExclude: [
    ...siteExclude,
    // 分片构建的排除面（SEP_SHARD 未设时为空）
    ...shardExclude,
  ],
  head: [
    ['link', { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    // 嵌入双语对照 iframe 中的页面隐藏站点框架
    ['script', {}, `if(window.parent!==window){document.documentElement.classList.add('in-iframe')}`],
    // 构建端：pagefind 命中词在目标页面上高亮（#8；dev 无 pagefind 产物不注入）
    // ① 等插件把 pagefind 挂上 window 后设置 highlightParam，使结果 URL 带 ?bili_hl=词条
    // ② 每页引入官方高亮脚本，按同名参数回显命中词
    ...(isBuild
      ? [
          [
            'script',
            {},
            `(function(){var n=0;(function p(){var f=window.__pagefind__;if(f&&f.options){f.options({highlightParam:'bili_hl'}).catch(function(){})}else if(++n<120){setTimeout(p,500)}})()})()`,
          ],
          [
            'script',
            { type: 'module' },
            `import('/pagefind/pagefind-highlight.js').then(function(){new PagefindHighlight({highlightParam:'bili_hl'})}).catch(function(){})`,
          ],
        ]
      : []),
  ],
  markdown: {
    // 关闭 markdown 编译缓存（ADR-0019，2026-10-31 实验证实）：缓存与
    // footnote 插件的 env 依赖不兼容——脚注引用在 build 产物字面化
    // （1911 页 2312 处），cache:false 后同源页面 footnote 正常渲染
    //（rationality 镜像 0→153）。构建耗时无显著差异（636-685s）。
    cache: false,
    // 关闭内置 @mdit/plugin-attrs：全库以 ^{…}/_{…} 作上下标约定、正文含
    // 大量字面 {…}（如 ^{−1}），attrs 会把尾随花括号吞成 HTML 属性——轻则
    // 上下标文本静默丢失（u(a_{1}) 渲染成 u(a），重则非法属性名（−½）炸掉
    // Vue 模板编译，kochen-specker 等页整页构建失败（2026-10-28 复核裁定）。
    attrs: false,
    // 图片原生懒加载（A3）：SEP 词条图多且大（实测词条页 img 无 loading 属性）
    image: { lazyLoad: true },
    config(md) {
      md.use(mathPlugin)
      // 行内代码全局 v-pre（vuejs/vitepress#3724 的做法）：
      // 代码内的 {{ }} 与标签不再被 Vue 当模板处理
      const defaultCodeInline = md.renderer.rules.code_inline!
      md.renderer.rules.code_inline = (tokens, idx, options, env, self) => {
        tokens[idx].attrSet('v-pre', '')
        return defaultCodeInline(tokens, idx, options, env, self)
      }
      // 参考文献就地全量渲染（2026-10-31 裁定：词条保持底稿形态不动，站点层补显示）。
      // 内置 footnoteTail（vendored markdown-it-footnote）只渲染被正文引用过的脚注
      // 定义，未被引用的定义组被静默丢弃——abduction 125 条定义仅 48 条被正文引用，
      // 77 条不出现在页面任何位置，致“## 参考文献”下观感为空（ADR-0017 实测证据）。
      // 本规则注册于 footnoteTail 之前（ruler.after 后注册者先跑）：把全部
      // footnote_reference_open/close 定义组按文件顺序转成完整列表，插回首个定义组
      // 原位（即标题之下）；定义组本体原样保留，由 footnoteTail 照旧剔除并在文末
      // 生成仅含被引用条目的脚注区——回跳锚与 littlefoot 气泡内容源均不受影响。
      // 自定义 token 类型与类名和脚注体系隔离，避开 littlefoot 对脚注容器的
      // 清空删除逻辑；li 加 v-pre（定义行含字面 {{ 的实例如
      // yuanwen/z/zermelo-set-theory note-29），杜绝新渲染内容触发 Vue 插值。
      md.core.ruler.after('inline', 'refsInPlace', (state) => {
        const { tokens, Token } = state
        const groups: { start: number; end: number; tokens: typeof tokens }[] = []
        let open = -1
        for (let i = 0; i < tokens.length; i++) {
          const type = tokens[i].type
          if (type === 'footnote_reference_open') {
            open = i
          } else if (type === 'footnote_reference_close' && open >= 0) {
            groups.push({ start: open, end: i, tokens: tokens.slice(open + 1, i) })
            open = -1
          }
        }
        if (groups.length === 0) return
        const list = [new Token('refs_list_open', 'ol', 1)]
        for (const g of groups) {
          list.push(
            new Token('refs_item_open', 'li', 1),
            ...g.tokens,
            new Token('refs_item_close', 'li', -1),
          )
        }
        list.push(new Token('refs_list_close', 'ol', -1))
        tokens.splice(groups[0].start, 0, ...list)
      })
      md.renderer.rules.refs_list_open = () => '<ol class="refs-full-list">\n'
      md.renderer.rules.refs_list_close = () => '</ol>\n'
      md.renderer.rules.refs_item_open = () => '<li v-pre>\n'
      md.renderer.rules.refs_item_close = () => '</li>\n'
    },
  },
  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'SEP 中文版',
    nav: [
      { text: '首页', link: '/' },
      { text: '分类目录', link: '/mu-lu-s' },
      { text: '词汇表', link: '/qian-yan/ci-hui-biao' },
      { text: '术语对照', link: '/shu-yu-biao' },
    ],
    sidebar: {
      '/yuanwen/': enSidebar,
      ...enSidebarByLetter,
      '/': slimIndexSidebar,
      ...zhSidebarByLetter,
      ...dirSidebars,
    },
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    // 2026-10-29 逐项选定：编辑此页 + 剩余界面文案补全中文 + 外链图标
    editLink: {
      pattern: 'https://github.com/taophilosophy/SEP-CN/edit/main/:path',
      text: '编辑此页',
    },
    lastUpdated: {
      text: '最后更新于',
    },
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    langMenuLabel: '切换语言',
    navMenuLabel: '菜单',
    mobileMenuLabel: '导航',
    extraMenuLabel: '更多',
    skipToContentLabel: '跳到正文',
    externalLinkIcon: true,
    socialLinks: [{ icon: 'github', link: 'https://github.com/taophilosophy/SEP-CN' }],
    // 全站页脚由 SepFooter（SEP 版式菜单块）承担，不再用默认 VPFooter（specs/037）
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
    // 本地预览时壳仓的 docs/ 是目录联接（taophilosophy.github.io/docs → 本仓），
    // Vite 按真实路径解析后 relativePath 会变成 ../../SEP-CN/a/x.md，直接查表则
    // 配对与版本钉全部落空（enPath 缺失 → 对照入口不出现，dev 实测踩坑）。
    // 这里按仓库根还原成仓内相对路径；构建态（docs 为真实目录）走原值，不受影响。
    let rel = pageData.relativePath.replace(/\\/g, '/')
    if (rel.startsWith('../')) {
      // relativePath 以 VitePress root（壳仓 docs）为基准，故只能按文本归一：
      // 去掉前导 ../ 段后，若首段正是本仓目录名（SEP-CN）再剥一层。
      const segs = rel.split('/')
      while (segs.length && (segs[0] === '..' || segs[0] === '.')) segs.shift()
      const base = path.basename(repoRoot)
      if (segs[0] === base) segs.shift()
      rel = segs.join('/')
    }
    const src = srcByDoc[rel]
    if (src) pageData.frontmatter.srcMeta = src
    const stamp = gitStamps[rel]
    if (stamp) pageData.lastUpdated = stamp
    const en = zhToEn[rel]
    if (en) pageData.frontmatter.enPath = '/' + en.replace(/\.md$/, '')
    const zh = enToZh[rel]
    if (zh) pageData.frontmatter.zhPath = '/' + zh.replace(/\.md$/, '')
  },
  vite: {
    build: {
      // 分块告警阈值（2026-11-16 实测，Vite 8/rolldown 按未压缩体积比较，默认 500）：
      // 依赖块远在阈值内——framework 111 KB、theme 101 KB、littlefoot 7 KB；
      // 超限的全是「数据体积」块，且没有可拆的机制：
      //   chunks/metadata 1.2 MB（__VP_HASH_MAP__ 4325 条路由哈希 + 站点数据，
      //     VitePress 2.0 起 metaChunk 默认开启，页面元数据已按页拆出，剩下的
      //     哈希表是全局前置数据，无配置项可再拆）；
      //   chunks/assets 1.0 MB（全站图片 URL 映射，gzip 453 KB，随图片数线性增长）；
      //   单页登记册/超长词条模块（shu-yu-biao 1.3 MB、ren-ming-biao 1.2 MB 等，
      //     属单页内容本身）。
      // manualChunks/rolldownOptions.codeSplitting 只能重排依赖，对这四类无效，
      // 故按数据面上限放行告警；低于此值的块仍会正常告警。
      chunkSizeWarningLimit: 1600,
    },
    plugins: [
      // 分片构建不跑 pagefind：合并后在 merge-shards.mjs 里对整份 dist 跑一次
      ...(isBuild && !isShard
        ? [
            pagefindPlugin({
              customSearchQuery: chineseSearchOptimize,
            }),
          ]
        : []),
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
      // 本地预览内容仓工作树时常用目录联接（壳 docs/ → 本仓）。Vite 把 root 解析到
      // 真实路径后，默认 serving allow 只含壳目录，页面模块一律 403；这里把内容仓
      // 真实根与壳的 workspace 根一并放行（仅 dev 生效，不影响 build）。
      fs: {
        allow: [repoRoot, searchForWorkspaceRoot(process.cwd())],
      },
      watch: {
        // 本仓库所在盘的 ReadDirectoryChangesW 会报 UNKNOWN 错误，改用轮询监听；
        // 2026-10-30（#9）粒度放宽 600→1500ms，降常驻 CPU 占用，热更新延迟上限 1.5s
        usePolling: true,
        interval: 1500,
        // 仓库里与站点无关的大目录不监听，降低轮询开销；
        // build 产物/隔离缓存不监听——否则 build 期间每写一页就触发 dev 全页刷新（2026-10-30）
        ignored: [
          '**/.git/**',
          '**/.vitepress/dist/**',
          '**/.vitepress/cache-build/**',
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

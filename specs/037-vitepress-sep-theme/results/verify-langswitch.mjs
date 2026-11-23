// 语言切换器静态验证（specs/037 2026-11-23）：bun specs/037-vitepress-sep-theme/results/verify-langswitch.mjs
// 断言 config.mts 的 locales/i18nRouting 改动满足验收判据（不用起构建）。
import cfg from '../../../.vitepress/config.mts'

let fails = 0
function ok(cond, label) {
  if (cond) console.log('[OK ] ' + label)
  else {
    fails++
    console.log('[FAIL] ' + label)
  }
}

// 1. siteConfig.locales：root 中文 + yuanwen 英文（键不带前导斜杠，见 config 注释）
ok(cfg.locales?.root?.lang === 'zh-CN', "locales.root.lang === 'zh-CN'")
ok(cfg.locales?.root?.label === '简体中文', "locales.root.label === '简体中文'")
ok(cfg.locales?.yuanwen?.lang === 'en', "locales.yuanwen.lang === 'en'")
ok(cfg.locales?.yuanwen?.label === 'English', "locales.yuanwen.label === 'English'")

// 2. i18nRouting 函数：配对直达 / 无配对回落 locale 首页
const ir = cfg.themeConfig?.i18nRouting
ok(typeof ir === 'function', 'themeConfig.i18nRouting 是函数')
const mkData = (fm) => ({ page: { value: { frontmatter: fm } } })
ok(ir(mkData({ enPath: '/yuanwen/a/abelard' }), {}, 'yuanwen') === '/yuanwen/a/abelard',
  '中文配对页 → enPath')
ok(ir(mkData({ zhPath: '/a/abelard' }), {}, 'root') === '/a/abelard', '英文配对页 → zhPath')
ok(ir(mkData({}), {}, 'yuanwen') === '/yuanwen/', '中文无配对 → /yuanwen/ 首页兜底')
ok(ir(mkData({}), {}, 'root') === '/', '英文无配对 → / 兜底')
ok(ir(mkData({ enPath: '/yuanwen/z/zermelo-set-theory' }), {}, 'yuanwen') === '/yuanwen/z/zermelo-set-theory',
  'enPath 直达（z 字母页样例）')

// 3. 浅合并语义防丢：根级 themeConfig 关键配置仍在（en locale 只覆盖给出的键）
ok(cfg.themeConfig?.search?.provider === 'local', '根级 search 仍在（en locale 不覆盖）')
ok(Array.isArray(cfg.themeConfig?.nav) && cfg.themeConfig.nav.length === 4, '根级 nav 4 项仍在')
ok(cfg.locales.yuanwen.themeConfig?.outline?.level?.join() === '2,3',
  'en locale outline.level 连子键一起重给（浅合并不丢 [2,3]）')
ok(cfg.themeConfig?.sidebar?.['/yuanwen/'] !== undefined, '根级 sidebar 的 /yuanwen/ 键仍在')

// 4. 搜索 UI 中文文案（themeConfig.search.options.locales.root.translations）未被动
ok(cfg.themeConfig?.search?.options?.locales?.root?.translations?.button?.buttonText === '搜索词条',
  '搜索框中文文案（search.options.locales.root）未动')

// 5. 无配对页隐藏机制的挂钩存在（源码文本断言）
const { readFileSync } = await import('node:fs')
const cfgSrc = readFileSync(new URL('../../../.vitepress/config.mts', import.meta.url), 'utf8')
const css = readFileSync(new URL('../../../.vitepress/theme/vp-compat.css', import.meta.url), 'utf8')
ok(cfgSrc.includes("pageData.frontmatter.pageClass = 'no-langswitch-page'") && cfgSrc.includes('!en && !zh'),
  'transformPageData 给无配对页注入 pageClass（构建期，SSR 即输出）')
ok(css.includes('.no-langswitch-page .VPNavTranslations') && css.includes('.no-langswitch-page .VPNavScreenTranslations'),
  'vp-compat.css 藏桌面 flyout 与移动端手风琴两处')
const { existsSync } = await import('node:fs')
ok(!existsSync(new URL('../../../.vitepress/theme/components/LangSwitchGuard.vue', import.meta.url)),
  '客户端 watch 方案（LangSwitchGuard.vue）已被 pageClass 方案取代并删除')

console.log(fails ? `\n== ${fails} 项失败 ==` : '\n== 全部通过 ==')
process.exit(fails ? 1 : 0)

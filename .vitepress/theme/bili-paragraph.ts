// ---------------------------------------------------------- 段落级对照映射 --
// 双语对照「以段落为单位」的定位算法：中英页面同源（yuanwen 镜像与译文
// 均由同一 SEP 源 HTML 派生），标题序与各区段内块序天然对齐；译文增删段
// 造成的漂移只在当前区段内生效，失配时按序号钳制到最近块，不会越界。

export const BILI_HEADS = 'h2, h3'
export const BILI_BLOCKS =
  'p, h2, h3, h4, li, blockquote, pre, table, dl, .math-display'

/** 把目标块换算成 (标题序 h, 区段内块序 b) 坐标；h=-1 表示首标题之前的导语区 */
export function mapPoint(doc: Element, target: Element): { h: number; b: number } | null {
  const heads = Array.from(doc.querySelectorAll(BILI_HEADS))
  const all = Array.from(doc.querySelectorAll(BILI_BLOCKS))
  const ti = all.indexOf(target)
  if (ti < 0) return null
  let h = -1
  for (let i = ti - 1; i >= 0; i--) {
    if ((all[i] as HTMLElement).matches(BILI_HEADS)) {
      h = heads.indexOf(all[i])
      break
    }
  }
  const secStart = h >= 0 ? all.indexOf(heads[h]) + 1 : 0
  return { h, b: ti - secStart }
}

/** 由坐标还原对侧页面的对应块；越界时钳制到区段尾块/标题 */
export function pointEl(doc: Element, h: number, b: number): HTMLElement | null {
  const heads = Array.from(doc.querySelectorAll(BILI_HEADS))
  const all = Array.from(doc.querySelectorAll(BILI_BLOCKS))
  const hd = h >= 0 && h < heads.length ? (heads[h] as HTMLElement) : null
  const secStart = hd ? all.indexOf(hd) + 1 : 0
  const next = hd && h + 1 < heads.length ? all.indexOf(heads[h + 1]) : all.length
  const sec = all.slice(Math.min(secStart, all.length), Math.max(secStart, next))
  return (sec[b] as HTMLElement) || hd || null
}

/** 点击目标是否应触发段落跳转（链接/表单/脚注按钮除外，选中文本时不触发） */
export function clickableBlock(e: MouseEvent): HTMLElement | null {
  const t = e.target as HTMLElement
  if (e.defaultPrevented) return null
  if (
    t.closest(
      'a, button, input, textarea, select, label, sup, .littlefoot__button, .littlefoot__popover',
    )
  )
    return null
  const sel = window.getSelection()
  if (sel && String(sel).length) return null
  const doc = document.querySelector('.vp-doc')
  const target = t.closest(BILI_BLOCKS) as HTMLElement | null
  return doc && target && doc.contains(target) ? target : null
}

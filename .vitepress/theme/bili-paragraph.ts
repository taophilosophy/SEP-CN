// ---------------------------------------------------------- 段落级对照映射 --
// 双语对照「以段落为单位」的定位算法：中英页面同源（yuanwen 镜像与译文
// 均由同一 SEP 源 HTML 派生），标题序与各区段内块序天然对齐；译文增删段
// 造成的漂移只在当前区段内生效，失配时按序号钳制到最近块，不会越界。

export const BILI_HEADS = 'h2, h3'
export const BILI_BLOCKS =
  'p, h2, h3, h4, li, blockquote, pre, table, dl, .math-display'

/** 正文块集合（排除交错模式注入的英文块：它们也在 .vp-doc 内，会把块序算歪） */
export function biliBlocks(root: Element): HTMLElement[] {
  return Array.from(root.querySelectorAll<HTMLElement>(BILI_BLOCKS)).filter(
    (el) => !el.closest('.bili-en-block'),
  )
}

/** 把目标块换算成 (标题序 h, 区段内块序 b) 坐标；h=-1 表示首标题之前的导语区 */
export function mapPoint(doc: Element, target: Element): { h: number; b: number } | null {
  const heads = Array.from(doc.querySelectorAll(BILI_HEADS))
  const all = biliBlocks(doc)
  const ti = all.indexOf(target)
  if (ti < 0) return null
  let h = -1
  for (let i = ti - 1; i >= 0; i--) {
    if ((all[i] as HTMLElement).matches(BILI_HEADS)) {
      h = heads.indexOf(all[i])
      break
    }
  }
  const secStart = h >= 0 ? all.indexOf(heads[h] as HTMLElement) + 1 : 0
  return { h, b: ti - secStart }
}

/** 由坐标还原对侧页面的对应块；越界时钳制到区段尾块/标题 */
export function pointEl(doc: Element, h: number, b: number): HTMLElement | null {
  const heads = Array.from(doc.querySelectorAll(BILI_HEADS))
  const all = biliBlocks(doc)
  const hd = h >= 0 && h < heads.length ? (heads[h] as HTMLElement) : null
  const secStart = hd ? all.indexOf(hd) + 1 : 0
  const next = hd && h + 1 < heads.length ? all.indexOf(heads[h + 1] as HTMLElement) : all.length
  const sec = all.slice(Math.min(secStart, all.length), Math.max(secStart, next))
  return (sec[b] as HTMLElement) || hd || null
}

// ------------------------------------------ 区段切分与交错配对（specs/038） --
// 同页对照需要把两侧正文切成「标题区段 + 区内块序」，与 mapPoint 同口径；
// 交错模式下按区段配对，块数差异过大的区段（参考文献、延伸阅读等）整段并列。

export type Section = { head: HTMLElement | null; blocks: HTMLElement[] }

/** 按 BILI_HEADS 切区段；首元素 head=null 为导语区（对应 h=-1） */
export function docSections(doc: Element): Section[] {
  const out: Section[] = []
  let cur: Section = { head: null, blocks: [] }
  for (const el of biliBlocks(doc)) {
    if (el.matches(BILI_HEADS)) {
      out.push(cur)
      cur = { head: el, blocks: [] }
    } else {
      cur.blocks.push(el)
    }
  }
  out.push(cur)
  return out
}

/** 给文档内每个块标注 data-bili-h / data-bili-b（注入的英文文档一次性做，供 O(1) 查表） */
export function annotateBlocks(doc: Element): void {
  const all = biliBlocks(doc)
  const heads = Array.from(doc.querySelectorAll(BILI_HEADS))
  let h = -1
  let secStart = 0
  all.forEach((el, ti) => {
    if (el.matches(BILI_HEADS)) {
      h = heads.indexOf(el)
      secStart = ti + 1
      el.setAttribute('data-bili-h', String(h))
      el.setAttribute('data-bili-b', '-1')
      return
    }
    el.setAttribute('data-bili-h', String(h))
    el.setAttribute('data-bili-b', String(ti - secStart))
  })
}

/** 按 (h, b) 取已标注的块 */
export function blockByKey(doc: Element, h: number, b: number): HTMLElement | null {
  return doc.querySelector<HTMLElement>(`[data-bili-h="${h}"][data-bili-b="${b}"]`)
}

/** 一条交错插入指令：把 en 块组插到 zh 块的紧后面（section=true 表示整段并列） */
export type Insertion = { after: HTMLElement; en: HTMLElement[]; h: number; section: boolean }

/** 生成交错配对计划（纯函数，不改 DOM；克隆与插入由组件执行） */
export function interleavePlan(zh: Element, en: Element): Insertion[] {
  const zs = docSections(zh)
  const es = docSections(en)
  const plan: Insertion[] = []
  for (let i = 0; i < zs.length; i++) {
    const z = zs[i]
    const e = es[i]
    const zb = z.head ? [z.head, ...z.blocks] : z.blocks
    const eb = e ? (e.head ? [e.head, ...e.blocks] : e.blocks) : []
    if (!zb.length || !eb.length) continue
    const ratio = Math.min(zb.length, eb.length) / Math.max(zb.length, eb.length)
    // 退化：块数差异过大（参考文献 251 li 对 2 块之类）→ 整段并列，避免碎块配对
    if (ratio < 0.5 || Math.abs(zb.length - eb.length) > 8) {
      plan.push({ after: zb[zb.length - 1], en: eb, h: i - 1, section: true })
      continue
    }
    const k = Math.min(zb.length, eb.length)
    for (let j = 0; j < k; j++) plan.push({ after: zb[j], en: [eb[j]], h: i - 1, section: false })
    if (eb.length > zb.length) {
      plan.push({ after: zb[zb.length - 1], en: eb.slice(zb.length), h: i - 1, section: false })
    }
  }
  return plan
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

/** 当前阅读段：视口上 1/3 基准线所穿过的块（滚动跟随高亮/双向驱动用）。
    零尺寸块（littlefoot 隐藏的脚注定义区等 display:none 子树，rect 恒为
    0,0 且 top<line 恒真）必须跳过——否则兜底分支永远选中它们（实测踩坑） */
export function activeBlock(doc: Element): HTMLElement | null {
  const blocks = biliBlocks(doc)
  if (!blocks.length) return null
  const line = window.innerHeight * 0.33
  let cur: HTMLElement | null = null
  for (const b of blocks) {
    const r = b.getBoundingClientRect()
    if (r.width === 0 && r.height === 0) continue
    if (r.top <= line && r.bottom >= line) return b
    if (r.top < line) cur = b
  }
  return cur
}

/** 双侧当前段高亮：唯一保留 .bili-active */
export function markActive(doc: Element, el: HTMLElement | null): void {
  doc.querySelectorAll('.bili-active').forEach((x) => {
    if (x !== el) x.classList.remove('bili-active')
  })
  if (el) el.classList.add('bili-active')
}

// ------------------------------------------ 句子级选中高亮（2026-10-31） --

/** 按中英终止符切句，返回各句在全文中的 [start, end) 偏移 */
export function sentenceSpans(text: string): Array<[number, number]> {
  const spans: Array<[number, number]> = []
  const re = /[。！？!?]|\.(?=\s|$)/g
  let start = 0
  let m: RegExpExecArray | null
  while ((m = re.exec(text))) {
    spans.push([start, m.index + m[0].length])
    start = m.index + m[0].length
  }
  if (start < text.length) spans.push([start, text.length])
  return spans.filter(([a, b]) => b > a)
}

/** 字符偏移所在句序号（超出按末句） */
export function sentenceIndexAt(text: string, offset: number): number {
  const spans = sentenceSpans(text)
  for (let i = 0; i < spans.length; i++) {
    if (offset >= spans[i][0] && offset < spans[i][1]) return i
  }
  return Math.max(0, spans.length - 1)
}

/** 选区所在的内容块：包含 node 的最内层 BILI_BLOCKS 成员（不能按
    '.vp-doc > *' 最近父解析——转换器会包 DIV 层，直接子非内容块，实测踩坑） */
export function containingBlock(doc: Element, node: Node): HTMLElement | null {
  let best: HTMLElement | null = null
  for (const b of biliBlocks(doc)) {
    if (b.contains(node) && (!best || best.contains(b))) best = b
  }
  return best
}

/** 选区起点在元素全文中的字符偏移 */
export function offsetInElement(el: Element, range: Range): number {
  const r = document.createRange()
  r.selectNodeContents(el)
  try {
    r.setEnd(range.startContainer, range.startOffset)
  } catch {
    return 0
  }
  return r.toString().length
}

/** 清除元素内指定类名的句子高亮（解包 mark 并合并文本节点） */
export function clearSentenceMarks(el: Element, cls: string): void {
  el.querySelectorAll('mark.' + cls).forEach((m) => {
    const p = m.parentNode!
    while (m.firstChild) p.insertBefore(m.firstChild, m)
    m.remove()
    p.normalize()
  })
}

/** 高亮元素内第 si 句：逐文本节点切片包裹 mark（句子跨元素时拆多片） */
export function highlightSentence(el: Element, si: number, cls: string): void {
  clearSentenceMarks(el, cls)
  const text = el.textContent || ''
  const spans = sentenceSpans(text)
  if (si < 0 || si >= spans.length) return
  const [a, b] = spans[si]
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT)
  const nodes: Array<{ node: Text; start: number; end: number }> = []
  let off = 0
  let n: Node | null
  while ((n = walker.nextNode())) {
    const len = n.textContent!.length
    nodes.push({ node: n as Text, start: off, end: off + len })
    off += len
  }
  for (const { node, start, end } of nodes) {
    if (end <= a || start >= b) continue
    const s = Math.max(a, start) - start
    const e = Math.min(b, end) - start
    const range = document.createRange()
    range.setStart(node, s)
    range.setEnd(node, e)
    const mark = document.createElement('mark')
    mark.className = cls
    try {
      range.surroundContents(mark)
    } catch {
      /* 片段跨边界等异常时放弃该片 */
    }
  }
}


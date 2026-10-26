// 数学定界符保护插件（markdown-it）
//
// 站内公式存在两种写法：yuanwen/ 英文词条用 $…$ 行内与 $$…$$ 块级（tools/yuanwen.py
// 原样保留），已译词条用 \(…\) 行内与 \[…\] 块级。若直接交给 markdown 解析，
// 反斜杠与下划线等会被吞掉，因此这里在解析前把公式整体抽换成 base64 哨兵
// （markdown 不会碰的纯 ASCII），渲染前再还原成带 v-pre 的 <span>/<div>，
// 最后由客户端 MathJax（tex-svg，见 config.mts 的 head）扫描渲染。
// 围栏代码块与行内代码里的定界符不做替换。

const SENTINEL_RE = /@@M([IBJ])([A-Za-z0-9_-]+)@@/

function encodeB64(str) {
  return Buffer.from(str, 'utf8').toString('base64url')
}

function decodeB64(str) {
  return Buffer.from(str, 'base64url').toString('utf8')
}

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

function inlineHtml(tex) {
  return `<span v-pre class="math-tex">\\(${escapeHtml(tex)}\\)</span>`
}

function displayHtml(tex) {
  return `<div v-pre class="math-tex math-display">\\[${escapeHtml(tex)}\\]</div>`
}

/** $/$$ 公式原文连同定界符原样保留，由 MathJax 按 $ 定界符排版 */
function rawMathHtml(raw) {
  return `<span v-pre class="math-tex">${escapeHtml(raw)}</span>`
}

/** 源文进入 markdown 解析前：围栏/行内代码以外的公式抽换为哨兵 */
export function protectMath(src) {
  // 守卫必须編进正则（而非事后拒绝）：事后拒绝会让扫描跳过已消费的定界符，
  // 货币符号 "$150,000" 与后续公式错配时会连锁打乱整篇的 $ 配对。
  // 单 $ 分两支：
  //  A) 数字开头（货币嫌疑）：右定界符必须紧随内容、其后不允许紧跟数字（"$150,000" 不参与配对）
  //  B) 非数字开头：右定界符前后允许空格（原子译稿有 "$ \alpha S' = {…} $" 写法）
  const re =
    /(```|~~~)[^\n]*\n[\s\S]*?\n\1[^\n]*(?=\n|$)|(```|~~~)[^\n]*\n[\s\S]*$|`[^`\n]*`|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|(?<!\\)\$\$([\s\S]+?)\$\$|(?<!\\)\$((?:[ \t]+\\)?\d(?:(?:\\\$|[^\n$]|\n(?![ \t]*\n))*[^\s$])?)\$(?!\d)|(?<!\\)\$(?!\d)((?:[ \t]+\\)?(?:\\\$|[^\s$])(?:(?:\\\$|[^\n$]|\n(?![ \t]*\n))*[^\s$])?)[ \t]*\$/g
  const out = src.replace(
    re,
    (all, fenceClosed, fenceOpen, blockTex, inlineTex, ddTex, dTexA, dTexB) => {
      if (fenceClosed || fenceOpen) return all // 围栏代码块原样保留
      if (all.startsWith('`')) return all // 行内代码原样保留
      if (blockTex !== undefined) return `\n\n@@MB${encodeB64(blockTex)}@@\n\n`
      if (inlineTex !== undefined) return `@@MI${encodeB64(inlineTex)}@@`
      if (ddTex !== undefined) return `@@MJ${encodeB64(`$$${ddTex}$$`)}@@`
      const single = dTexA !== undefined ? dTexA : dTexB
      return `@@MJ${encodeB64(`$${single}$`)}@@`
    },
  )
  // 数学之外的裸 {{ 会被 Vue 当模板插值（轻则文本消失、重则编译报错），须屏蔽。
  // 代码块内用零宽空格（实体在代码里会被 markdown 再转义成可见的 &#123;），
  // 其余文本用等效实体（显示与复制均不受影响）。
  return out
    .replace(/(`[^`\n]*`|(```|~~~)[^\n]*\n[\s\S]*?\n\2)/g, (c) => c.replace(/\{\{/g, '{\u200b{'))
    .replace(/\{\{/g, '&#123;{')
}

/** 渲染前把哨兵还原为最终 HTML */
function restoreMath(state) {
  for (const tok of state.tokens) {
    // 块级公式独占段落 → 整段还原为 html_block，避免 <div> 落入 <p>
    if (tok.type === 'paragraph') {
      const m = tok.content.trim().match(/^@@MB([A-Za-z0-9_-]+)@@$/)
      if (m) {
        tok.type = 'html_block'
        tok.tag = ''
        tok.content = displayHtml(decodeB64(m[1]))
        tok.children = null
        continue
      }
    }
    if (tok.type === 'inline' && Array.isArray(tok.children)) {
      const children = []
      for (const child of tok.children) {
        if (child.type === 'text' && SENTINEL_RE.test(child.content)) {
          let rest = child.content
          let m
          while ((m = SENTINEL_RE.exec(rest))) {
            if (m.index > 0) children.push(textToken(state, rest.slice(0, m.index)))
            const tex = decodeB64(m[2])
            const html =
              m[1] === 'I'
                ? inlineHtml(tex)
                : m[1] === 'J'
                  ? rawMathHtml(tex)
                  : `<span v-pre class="math-tex">\\[${escapeHtml(tex)}\\]</span>`
            children.push(htmlToken(state, html))
            rest = rest.slice(m.index + m[0].length)
          }
          if (rest) children.push(textToken(state, rest))
        } else {
          children.push(child)
        }
      }
      tok.children = children
    }
  }
}

function textToken(state, content) {
  const t = new state.Token('text', '', 0)
  t.content = content
  return t
}

function htmlToken(state, content) {
  const t = new state.Token('html_inline', '', 0)
  t.content = content
  return t
}

export function mathPlugin(md) {
  const originalParse = md.parse.bind(md)
  md.parse = function (src, env) {
    return originalParse(protectMath(src), env)
  }
  md.core.ruler.push('sep_math_restore', restoreMath)
}

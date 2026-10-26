// 数学定界符保护插件（markdown-it）
//
// yuanwen/ 英文词条使用 \(…\) 行内公式与 \[…\] 块级公式（tools/yuanwen.py 原样保留）。
// 若直接交给 markdown 解析，反斜杠与下划线等会被吞掉，因此这里在解析前把公式整体
// 抽换成 base64 哨兵（markdown 不会碰的纯 ASCII），渲染前再还原成带 v-pre 的
// <span>/<div>，最后由客户端 MathJax（tex-svg，见 config.mts 的 head）扫描渲染。
// ``` 围栏代码块内的 \( \[ 不做替换。

const FENCE_MARKS = ['```', '~~~']
const SENTINEL_RE = /@@M([IB])([A-Za-z0-9_-]+)@@/

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

/** 源文进入 markdown 解析前：围栏代码块以外的 \(…\)、\[…\] 抽换为哨兵 */
function protectMath(src) {
  const lines = src.split(/\r?\n/)
  const out = []
  let fence = null
  for (const line of lines) {
    if (fence) {
      out.push(line)
      if (line.trim().startsWith(fence)) fence = null
      continue
    }
    const trimmed = line.trim()
    const mark = FENCE_MARKS.find((m) => trimmed.startsWith(m))
    if (mark) {
      fence = mark
      out.push(line)
      continue
    }
    out.push(
      line
        .replace(/\\\[([\s\S]+?)\\\]/g, (_, tex) => `\n\n@@MB${encodeB64(tex)}@@\n\n`)
        .replace(/\\\(([\s\S]+?)\\\)/g, (_, tex) => `@@MI${encodeB64(tex)}@@`),
    )
  }
  return out.join('\n')
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
            children.push(
              m[1] === 'I'
                ? htmlToken(state, inlineHtml(tex))
                : htmlToken(state, `<span v-pre class="math-tex">\\[${escapeHtml(tex)}\\]</span>`),
            )
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

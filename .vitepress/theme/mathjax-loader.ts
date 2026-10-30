// MathJax 按需加载器（2026-10-30 A2）
// 单例：首个需要排版的组件触发注入，配置须在 tex-svg.js 执行前就位
// （MathJax 启动时读取 window.MathJax）。MathTypesetter 与 FootnoteEnhance 共用。
import { mathjaxConfig } from './math-jax-config'

let mjLoading: Promise<any> | null = null

export function ensureMathJax(): Promise<any> {
  const w = window as any
  if (w.MathJax?.typesetPromise) return Promise.resolve(w.MathJax)
  if (!mjLoading) {
    mjLoading = new Promise((resolve, reject) => {
      w.MathJax = { ...mathjaxConfig }
      const s = document.createElement('script')
      s.src = '/mathjax/tex-svg.js'
      s.onload = () => {
        // startup.promise 的解析值并非 MathJax 对象（实测 undefined），
        // 轮询全局 typesetPromise 就绪为准
        let n = 0
        const poll = () => {
          if (w.MathJax?.typesetPromise) return resolve(w.MathJax)
          if (++n < 40) return setTimeout(poll, 200)
          reject(new Error('MathJax 初始化超时'))
        }
        poll()
      }
      s.onerror = () => reject(new Error('MathJax 脚本加载失败'))
      document.head.appendChild(s)
    }).catch((e) => {
      mjLoading = null
      throw e
    })
  }
  return mjLoading
}

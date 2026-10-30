// MathJax 全局配置（2026-10-30 A2：由 config head 预载改为按需加载——
// MathTypesetter 在页面首次出现 .math-tex 时先写入 window.MathJax 再拉
// /mathjax/tex-svg.js，无公式页面零开销）。
// enableMenu 重开原生右键菜单（Show Math As → TeX/MathML），作为复制按钮之外的备用入口。
export const mathjaxConfig = {
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
  options: { enableMenu: true },
  startup: { typeset: false }, // 由 MathTypesetter 在路由变化后手动排版（SPA）
}

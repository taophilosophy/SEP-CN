import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import BilingualToggle from './components/BilingualToggle.vue'
import FootnoteEnhance from './components/FootnoteEnhance.vue'
import MathTypesetter from './components/MathTypesetter.vue'
import VersionPin from './components/VersionPin.vue'
import './custom.css'

// 离线字体：正文用霞鹜文楷屏幕阅读版（LXGW WenKai Screen），
// 代码用内嵌英文等宽字形的霞鹜文楷等宽（LXGW WenKai Mono）；
// 标题的粗体来自 LXGW WenKai Bold（屏幕阅读版只有 400 一档字重）。
import 'lxgw-wenkai-screen-webfont/lxgwwenkaiscreen.css'
import 'lxgw-wenkai-webfont/lxgwwenkai-bold.css'
import 'lxgw-wenkai-webfont/lxgwwenkaimono-regular.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'nav-bar-content-after': () => h(BilingualToggle),
      'doc-top': () => h(MathTypesetter),
      'doc-footer-before': () => h(VersionPin),
      'layout-bottom': () => h(FootnoteEnhance),
    })
  },
}

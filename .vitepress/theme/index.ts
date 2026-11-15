import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import BilingualToggle from './components/BilingualToggle.vue'
import EntryMatter from './components/EntryMatter.vue'
import FootnoteEnhance from './components/FootnoteEnhance.vue'
import MathTypesetter from './components/MathTypesetter.vue'
import SepFooter from './components/SepFooter.vue'
import './custom.css'
import './sep-theme.css'
// 兼容桥接层最后加载：全站唯一引用 VitePress 内部类名的文件（specs/037）
import './vp-compat.css'

// 离线字体：正文用霞鹜文楷屏幕阅读版（LXGW WenKai Screen），
// 代码用内嵌英文等宽字形的霞鹜文楷等宽（LXGW WenKai Mono）；
// 标题的粗体来自 LXGW WenKai Bold（屏幕阅读版只有 400 一档字重）。
import 'lxgw-wenkai-screen-webfont/lxgwwenkaiscreen.css'
import 'lxgw-wenkai-webfont/lxgwwenkai-bold.css'
import 'lxgw-wenkai-webfont/lxgwwenkaimono-regular.css'

// SEP 版式主题（specs/037）：槽位组件 + CSS 换皮，交互沿用默认主题。
// 版本钉不再挂 doc-footer-before，已迁入 SepFooter 页脚块。
export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'nav-bar-content-after': () => h(BilingualToggle),
      'doc-top': () => [h(MathTypesetter), h(EntryMatter)],
      'doc-bottom': () => h(SepFooter),
      'layout-bottom': () => h(FootnoteEnhance),
    })
  },
}

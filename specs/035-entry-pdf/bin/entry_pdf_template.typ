// ===== SEP Friends 版式仿排 ·《斯坦福哲学百科全书》简体中文翻译项目 =====
// 占位符(由 bin/entry_pdf.py 填充;文档注释内不得出现 %%..%% 记号,防 replace 误吞):
//   ZH_TITLE / EN_TITLE / AUTHOR / PUBINFO / EDITION / ENTRY_URL / INTRO / BODY
// 字体方案(specs/035 Assumptions):正文=霞鹜文楷屏幕阅读版;强调/标题=主仓 Medium;
//   该家族无 Bold/Italic 字面且 typst 不合成假粗斜体,故中文强调一律走 Medium。
#let zhserif = ("Times New Roman", "LXGW WenKai Screen")
#let zhmed = ("Times New Roman", "霞鶩文楷")

#let tocshow = context {
  for h in query(heading) {
    if h.level == 2 [ #block(spacing: 0.55em)[#text(size: 9.2pt)[• #h.body]] ]
    else if h.level == 3 [ #pad(left: 1.4em)[#block(spacing: 0.45em)[#text(size: 9.2pt)[◦ #h.body]]] ]
  }
}

#set page(
  paper: "a4", flipped: true, binding: auto,
  margin: (top: 2.0cm, bottom: 2.5cm, inside: 2.0cm, outside: 2.0cm),
  header: context {
    let n = counter(page).get().first()
    if n > 1 [
      #grid(columns: (1fr, 1fr),
        align(left, text(size: 8pt, tracking: 0.14em, font: zhserif)[%%ZH_TITLE%%]),
        align(right, text(size: 8pt, tracking: 0.1em, font: zhserif)[%%AUTHOR%%]),
      )
      #v(0.5em)
    ]
  },
  footer: context {
    let n = counter(page).get().first()
    if n > 1 {
      if calc.odd(n) [
        #grid(columns: (1fr, 1.4fr, 1fr),
          [],
          align(center, text(size: 8pt, tracking: 0.12em, font: zhserif)[%%EDITION%% · 简体中文翻译]),
          align(right, text(size: 8.8pt)[#n]),
        )
      ] else [
        #grid(columns: (1fr, 1.4fr, 1fr),
          align(left, text(size: 8.8pt)[#n]),
          align(center, text(size: 8pt, tracking: 0.12em, font: zhserif)[斯坦福哲学百科全书]),
          [],
        )
      ]
    }
  },
)

// 中文排版(specs/035):段首缩进两字符(含标题后段),段间距加大
#set text(font: zhserif, size: 9.5pt, lang: "zh", region: "cn")
#set par(justify: true, leading: 0.96em, spacing: 1.35em, hanging-indent: 0em,
  first-line-indent: (amount: 2em, all: true))
#set heading(numbering: none)
#show heading: it => {
  v(0.8em, weak: true) + block(above: 0.9em, below: 0.5em, it)
}
#show heading.where(level: 2): set text(size: 11pt, font: zhmed, weight: 700)
#show heading.where(level: 3): set text(size: 10pt, font: zhmed, weight: 700)
#show emph: set text(font: zhmed)
#show strong: set text(font: zhmed, weight: 700)
#show quote: set block(inset: (left: 1.1em, right: 0.6em), spacing: 0.9em)
#show quote: set text(size: 9pt)
#show footnote: set text(size: 7.8pt)
#show list: set list(indent: 1.1em, spacing: 0.7em)
#show enum: set enum(indent: 1.1em, spacing: 0.7em)
#show link: set text(fill: rgb("#1a4d8f"))

// ===================== 封面(第 1 页,左信息栏/右题栏) =====================
#grid(
  columns: (1fr, 1fr), gutter: 1.8cm,
  align: (center + top, left + top),
  [
    #set par(leading: 0.75em, spacing: 0.5em, first-line-indent: 0em)
    #v(0.3em)
    #text(size: 9pt)[词条 PDF 版本]
    #v(0.1em)
    #text(size: 10.5pt, weight: "bold")[%%ZH_TITLE%%]
    #v(0.3em)
    #text(size: 7.6pt)[#link("%%ENTRY_URL%%")[%%ENTRY_URL%%]]
    #v(0.4em)
    #text(size: 8.5pt)[取自《斯坦福哲学百科全书》\ %%EDITION%%]
    #v(0.7em)
    #text(size: 11.5pt, tracking: 0.16em)[斯坦福哲学百科全书]
    #v(0.2em)
    #text(size: 9pt, tracking: 0.2em)[STANFORD \u{2009}ENCYCLOPEDIA \u{2009}OF \u{2009}PHILOSOPHY]
    #v(0.8em)
    #image("sepman-black.png", height: 1.9cm)
    #v(0.8em)
    #set par(leading: 0.7em)
    #text(size: 8.3pt)[
      原版主编：Edward N. Zalta 与 Uri Nodelman \
      副主编：Colin Allen、Hannah Kim、Paul Oppenheimer \
      编辑委员会：plato.stanford.edu/board.html \
      美国国会图书馆刊号：ISSN 1095-5054
    ]
    #set par(leading: 0.8em)
    #text(size: 7.6pt)[
      斯坦福哲学百科全书 \
      版权 © 2025 by the publisher \
      The Metaphysics Research Lab \
      Department of Philosophy \
      Stanford University, CA 94305 \
      #line(length: 34%, stroke: 0.3pt) \
      %%EN_TITLE%% \
      版权 © 2025 by the author %%AUTHOR%% \
      All rights reserved.
    ]
  ],
  [
    #set par(leading: 0.85em, spacing: 0.8em, first-line-indent: 0em)
    #v(0.3em)
    #text(size: 16pt, weight: "bold")[%%ZH_TITLE%%]
    #v(0.15em)
    #emph[#text(size: 11pt)[%%EN_TITLE%%]]
    #v(0.6em)
    #emph[#text(size: 9pt)[%%PUBINFO%%]]
    #v(0.9em)
    %%INTRO%%
    #v(0.9em)
    #tocshow
  ]
)
#pagebreak()

// ===================== 正文 =====================
#columns(2, gutter: 1.8cm)[
%%BODY%%
]

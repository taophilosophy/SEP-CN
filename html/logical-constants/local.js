window.MathJax = {
    TeX: {
      equationNumbers: { autoNumber: "all" },
      TagSide: "left",
      TagIndent: "0em",
      Macros: {
            refp: ["(\\ref{#1})", 1],
            dq: ["{\\text{“}#1\\text{”}}", 1],
            cq: ["{\\ulcorner #1 \\urcorner}", 1],
            and: "\\,\\&\\,",
      }
    }
};

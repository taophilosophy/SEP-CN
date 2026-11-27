window.MathJax = {
    TeX: {
        TagSide: "left",
        TagIndent: "0em",
        Macros: {
	    amp: "\\mathbin{\\&}",
	    lpar: "\\mathrel{\\unicode{x214b}}",
	    limp: "\\mathbin{-\\hspace{-0.70mm}\\circ}",
	    bang: "\\mathop{!}",
	    quest: "\\mathop{?}",
	    one:  "\\mathbf{1}",
	    zero: "\\mathbf{0}",
	    ot: "\\otimes",
            Up: ["{#1};{#2} \\Uparrow {#3}",3],
            Down: ["{#1};{#2} \\Downarrow {#3}",3],
	    lvdash: ["\\mathbin{|\\hspace{-0.70mm}\\raise 2mm {\\scriptstyle\\underline{\\,#1\\,}}}\\;", 1]
	}
    }
};

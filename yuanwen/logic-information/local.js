window.MathJax = {
    TeX: {
        TagSide: "left",
        TagIndent: "0em",
        Macros: {
	    amp: "\\mathbin{\\&}",
            bfrac: ["{^{#1}\\unicode{x2044}_{#2}}",2],
	    frasl: "\\unicode{x2044}",
	    Diamond: "\\unicode{x2B26}",
	    dproves: "\\mathbin{\\rvert\\!{\\sim}}",
	    notdproves: "\\mathop{\\mathrel{\\rlap{\\hskip .2em/}}\\rvert\\!{\\sim}}",
	    llangle: "\\langle\\!\\langle",
	    rrangle: "\\rangle\\!\\rangle",
	    llbracket: "[\\![",
	    rrbracket: "]\\!]"
	}
    }
};

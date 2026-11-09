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
	    llbracket: "[\\![",
	    rrbracket: "]\\!]",
	    TC: "\\mathord{\\textit{TC}}",
	    MOD: "\\mathord{\\textit{MOD}}",
	    EXT: "\\mathord{\\textit{EXT}}"
	}
    }
};

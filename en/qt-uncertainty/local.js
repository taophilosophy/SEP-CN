window.MathJax = {
    TeX: {
        TagSide: "left",
        TagIndent: "0em",
        Macros: {
	    amp: "\\mathbin{\\&}",
	    bA: "\\boldsymbol{A}",
	    bB: "\\boldsymbol{B}",
	    bP: "\\boldsymbol{P}",
	    bQ: "\\boldsymbol{Q}",
	    abs: ["{\\lvert #1 \\rvert}",1],
	    braket: ["{\\langle #1 {\\mid} #2 \\rangle}",2],
	    expval: ["{\\langle #1 \\rangle}",1],
	    expvalexp: ["{\\langle #2 {\\mid} #1 {\\mid} #2 \\rangle}",2],
	    ket: ["{\\lvert #1 \\rangle}",1]
	}
    }
};

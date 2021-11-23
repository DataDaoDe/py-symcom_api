from sympy.parsing.latex import parse_latex
from sympy import latex

def from_latex(latex_formula: str):
    return parse_latex(latex_formula)

def to_latex(expression):
    return latex(expression)
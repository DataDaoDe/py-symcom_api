from sympy.parsing.latex import parse_latex
from sympy import Derivative, latex

def from_latex(latex_formula: str):
    return parse_latex(latex_formula)

def to_latex(expression):
    return latex(expression)

def take_derivative(formula: str, nth_derivative: int):
    dx_expression = Derivative(formula)
    result = None

    idx = 0
    while idx < nth_derivative:
        result = dx_expression.doit()

        if result.is_number and result.is_zero:
            break
        
        dx_expression = Derivative(result)

        idx += 1

    return result
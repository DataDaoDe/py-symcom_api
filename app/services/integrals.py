from sympy import Integral, symbols, UnevaluatedExpr, Add

def find_integral_of(
    formula: str
):
    int_expr = Integral(formula)
    c = symbols("C", real=True, constant=True)

    # todo: figure out a cleaner way to do this
    result = UnevaluatedExpr(Add(int_expr.doit(), UnevaluatedExpr(c)))

    return result


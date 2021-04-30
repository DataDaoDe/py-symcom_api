from sympy import Derivative

def find_nth_derivative_of(
    formula: str,
    nth_derivative: int
):
    dx_expression = Derivative(formula)

    # todo: decide how to handle derivatives < 0

    if nth_derivative < 1:
        return dx_expression.doit()

    result = None
    idx = 0

    while idx < nth_derivative:
        result = dx_expression.doit()

        if result.is_number and result.is_zero:
            break
        
        dx_expression = Derivative(result)

        idx += 1

    return result


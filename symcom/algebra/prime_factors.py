from typing import Dict, List, Tuple, Any, NamedTuple
from functools import reduce
from sympy.ntheory import factorint


class RenderedStepResult(NamedTuple):
    step_words: str
    step_latex: str

def get_prime_factors(n: int) -> List[Tuple[int, int]]:
    result = factorint(n)
    factors = sorted(zip(result.keys(), result.values()), key=lambda t: t[0])
    return factors

def get_steps(factors: List[Tuple[int, int]]) -> List[Dict[str, Any]]:
    steps = []
    total = reduce(lambda a, b: a * b, [x[0]**x[1] for x in factors])

    for factor in factors:
        base = factor[0]
        for p in range(0, factor[1]):
            steps.append({'total' : total, 'factor' : base, 'division_result' : total // base })
            total = total // base

    return steps

def render_steps(factors: List[Tuple[int, int]], steps: List[Dict[str, Any]]) -> List[RenderedStepResult]:
    rendered_results = []

    for step in steps:
        step_words = f"{step['total']} divides by {step['factor']} resulting in {step['division_result']}"
        step_latex = f"{step['total']} = {step['factor']}\\cdot {step['division_result']}"
        step_result = RenderedStepResult(step_words=step_words, step_latex=step_latex)

        rendered_results.append(step_result)

    # add summary step
    just_factors = ', '.join( list(map(lambda x: str(x[0]), factors)) )
    just_factors += ' are all the prime numbers, therefore no further factorization is possible.'

    rendered_results.append(RenderedStepResult(step_words=just_factors, step_latex=None))

    return rendered_results
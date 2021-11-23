from typing import List, Tuple
from functools import reduce
from sympy.ntheory import factorint

def get_prime_factors(n: int) -> List[Tuple[int, int]]:
    result = factorint(n)
    factors = sorted(zip(result.keys(), result.values()), key=lambda t: t[0])
    return factors

def get_steps(factors: List[Tuple[int, int]]) -> List[str]:
    steps = []
    total = reduce(lambda a, b: a * b, [x[0]**x[1] for x in factors])

    for factor in factors:
        base = factor[0]
        for p in range(0, factor[1]):
            steps.append({'total' : total, 'factor' : base, 'division_result' : total // base })
            total = total // base

    return steps
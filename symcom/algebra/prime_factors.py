from typing import List, Tuple
from functools import reduce
from sympy.ntheory import factorint

def get_prime_factors(n: int) -> List[Tuple[int, int]]:
    result = factorint(n)
    factors = list(zip(result.keys(), result.values()))
    return factors

def get_steps(factors: List[Tuple[int, int]]) -> List[str]:
    steps = []
    total = reduce(lambda a, b: a * b, [x[0]**x[1] for x in factors])

    for factor in factors:
        base = factor[0]
        for p in range(0, factor[1]):
            print(base, p)
            steps.append({'total' : total, 'base' : base, 'div' : total // base })
            total = total // base

    return steps
from symcom.algebra import prime_factors as pf
from symcom.latex import from_latex
from unittest import TestCase

def test_get_prime_factors():
    factors = pf.get_prime_factors(45)
    
    assert len(factors) == 2, "45 has two distinct prime factors"
    
    assert list(map(lambda x: x[0], factors)) == [3, 5], "45 has prime factors 3 and 5"
    assert factors[0][0] == 3, "The first prime factor is 3"
    assert factors[0][1] == 2, "3 factors 2 times"
    assert factors[1][0] == 5, "The second prime factor is 5"
    assert factors[1][1] == 1, "5 factors once"


def test_get_steps():
    factors = pf.get_prime_factors(180)
    
    steps = pf.get_steps(factors)

    assert steps[0] == {'total' : 180, 'factor' : 2, 'division_result' : 90}
    assert steps[1] == {'total' : 90, 'factor' : 2, 'division_result' : 45}
    assert steps[2] == {'total' : 45, 'factor' : 3, 'division_result' : 15}
    assert steps[3] == {'total' : 15, 'factor' : 3, 'division_result' : 5}
    assert steps[4] == {'total' : 5, 'factor' : 5, 'division_result' : 1}


def test_render_steps():
    factors = pf.get_prime_factors(45)
    steps = pf.get_steps(factors)
    r = pf.render_steps(factors, steps)

    assert r[0].step_words == "45 divides by 3 resulting in 15"
    assert from_latex(r[0].step_latex), "evaluates latex expression w/out error"

    assert r[1].step_words == "15 divides by 3 resulting in 5"
    assert from_latex(r[1].step_latex), "evaluates latex expression w/out error"

    assert r[2].step_words == "5 divides by 5 resulting in 1"
    assert from_latex(r[2].step_latex), "evaluates latex expression w/out error"

    assert r[3].step_words == "3, 5 are all the prime numbers, therefore no further factorization is possible."
    assert r[3].step_latex == None, "There is no expression data for the final summary step."
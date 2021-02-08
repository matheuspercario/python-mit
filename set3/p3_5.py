# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 8th, 2021
# ============================================================================
from math import exp


def sqrt_func(x):
    return x ** 0.5


def poly_3(x):
    return (3 * x ** 3) + (x ** 2) + (4 * x) + 10


def approx_derivative(f, x, delta=1e-6):
    return (f(x + delta) - f(x - delta)) / (2 * delta)


def approx_derivative_2(f, delta=1e-6):
    def inner_derivative(x):
        return (f(x + delta) - f(x - delta)) / (2 * delta)
    return inner_derivative


# print(approx_derivative(sqrt_func, 1))
# print(approx_derivative(sqrt_func, 2))
# print(approx_derivative(sqrt_func, 3))
# print(approx_derivative(poly_3, 5))


# f_prime = approx_derivative_2(sqrt_func)
# print(f_prime(1))
# print(f_prime(2))
# print(f_prime(3))

# f_prime = approx_derivative_2(poly_3)
# print(f_prime(5))

def approx_integral(f, lo, hi, num_regions):

    # step
    d_x = (hi - lo) / num_regions

    # terms to sum
    terms = [f(x) for x in [(lo + i * d_x) for i in range(1, num_regions)]]

    # variables
    f0 = f(lo)
    f_sum = sum(terms)
    fn = f(hi)

    return d_x * (f_sum + ((f0 + fn) / 2))


# print(approx_integral(exp, 0, 1, 10))
# print(approx_integral(lambda x: 2 * exp(x), 5, 7, 10))

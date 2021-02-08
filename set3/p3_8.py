# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 7th, 2021
# ============================================================================

def f_1(a):
    return 2 * a


def f_2(b):
    return 3 * b


def composite_result(f, g, x):
    return f(g(x))


def composite(f, g):
    def inner_func(x):
        return f(g(x))
    return inner_func


# print(composite_result(f_1, f_2, 5))

# composite_f1_2 = composite(f_1, f_2)
# print(composite_f1_2(5))

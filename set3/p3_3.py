# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 8th, 2021
# ============================================================================
import math


def dictmap(d, f):
    for key, value in d.items():
        d[key] = f(value)


# d1 = {'a': 452, 'pi': 3.14, 'test': 5612}
# print(d1)
# dictmap(d1, math.cos)
# print(d1)

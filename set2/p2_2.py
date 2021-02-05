# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 4th, 2021
# ============================================================================


import doctest
from math import sqrt


def prime(x: int):
    """Verifica se o número é primo ou não

    Args:
        x (int): Número fornecido pelo usuário.

    Returns:
        [bool]: True se é primo e False caso contrário.

    >>> prime(0)
    False
    >>> prime(1)
    False
    >>> prime(2)
    True
    >>> prime(29)
    True
    >>> prime(27)
    False
    >>> prime(641)
    True
    """
    # Definido pelo enunciado
    if x in (0, 1):
        return False

    # Se for 2 é primo
    elif x == 2:
        return True

    # Se for par paramos aqui
    elif x % 2 == 0:
        return False

    else:
        r_q = round(sqrt(x))  # Raiz quadrada de X
        # Percorrendo todos números ímpares até a raiz quadrada de X
        for i in range(3, r_q + 1, 2):
            if x % i == 0:
                return False
        return True


doctest.testmod()

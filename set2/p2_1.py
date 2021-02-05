# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 4th, 2021
# ============================================================================


import doctest
from math import sqrt


def square(x):
    """Calcula o quadrado do número informado.
    Args:
        x ([int], [float]): valor dado pelo usuário.

    Returns:
        [[int], [float]]: quadrado do numero informado pelo usuário.

    # Testes
    >>> square(5)
    25
    >>> square(4.5)
    20.25
    """
    return x ** 2


def fourth_power(x):
    """Calcula a quarta potência de um numero.

    Args:
        x ([int], [float]): Valor fornecido pelo usuário.

    Returns:
        [[int], [float]]: a quarta potência do numero informado pelo usuário.

    >>> fourth_power(2)
    16
    >>> fourth_power(5)
    625
    >>> fourth_power(235.4)
    3070618301.1856003
    """
    return square(square(x))


def perfect_square(x):
    """Verifica se um número é quadrado perfeito ou não.

    Args:
        x (int, float): Número fornecido pelo usuário.  

    Returns:
        [bool]: True se for quadrado perfeito e False caso contrário.

    >>> perfect_square(36)
    True
    >>> perfect_square(132)
    False
    """
    # Validar apenas positivos
    if x >= 0:
        result = sqrt(x)
        if result - round(result) == 0.0:
            return True
        else:
            return False

    
doctest.testmod()

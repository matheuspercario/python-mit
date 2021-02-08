# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 7th, 2021
# ============================================================================

def hailstone_iterative_sequence(a_0):
    """Calcula (iterativamente) a sequência conhecida como "números de granizo" (hailstone sequence) ou "números maravilhosos". A Conjectura de Collatz afirma que, independentemente do valor de a[0], a sequência sempre atingirá um valor k tal que a[k]=1.  

    Args:
        a_0 (int): Valor inicial, a partir de onde a sequêcia de números maravilhosos se iniciará.

    Returns:
        list: Lista com números maravilhosos a partir de 'a_0'.
    """
    a = [a_0]
    k = 0

    while True:
        # Condição de parada -> a[k] == 1
        if a[k] == 1:
            return a
        # Decisão para próximo passo da sequência (par ou ímpar)
        elif a[k] % 2 == 0:
            a.append(a[k] // 2)
        else:
            a.append(3 * a[k] + 1)

        k += 1


def hailstone_sequence(a_0: int):
    """Calcula (recursivamente) a sequência conhecida como "números de granizo" (hailstone sequence) ou "números maravilhosos". A Conjectura de Collatz afirma que, independentemente do valor de a[0], a sequência sempre atingirá um valor k tal que a[k]=1.

    Args:
        a_0 (int): Número inicial, de onde a sequência iniciará.

    Returns:
        list: Lista dos números maravilhosos.
    """
    # Condição de parada -> a_0 == 1
    if a_0 == 1:
        return [a_0]
    # Decisão para próximo passo da sequência (par ou ímpar)
    elif a_0 % 2 == 0:
        # return é o número atual mais o hailstone do próximo par
        return [a_0] + hailstone_sequence(a_0 // 2)
    else:
        # return é o número atual mais o hailstone do próximo ímpar
        return [a_0] + hailstone_sequence(3 * a_0 + 1)


# print(hailstone_iterative_sequence(5))
# print(hailstone_sequence(5))

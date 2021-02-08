# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 7th, 2021
# ============================================================================

def hailstone_sequence(a_0):
    """Calcula a sequência conhecida como "números de granizo" (hailstone sequence) ou "números maravilhosos". A Conjectura de Collatz afirma que, independentemente do valor de a[0], a sequência sempre atingirá um valor k tal que a[k]=1.  

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
        if a[k] % 2 == 0:
            a.append(a[k] // 2)
        else:
            a.append(3 * a[k] + 1)

        k += 1


def hailstone_sequence_rec(a_0):
    pass

# PYTHON - MIT - UNICAMP
# =============================================================================
# Created By   : Matheus Percário Bruder
# Created Date : February 4th, 2021
# ============================================================================


def ndoors(n: int):
    """Define quais portas estarão abertas após 'n' passagens. Todas iniciam trancadas.

    Args:
        n (int): Número de portas.

    Returns:
        list: Portas ques estarão aberta apos 'n' passagens.

    >>> 100
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    >>> 10
    [1, 4, 9]
    """
    # Criar lista para portas (1 - 100)
    doors = [i for i in range(1, n + 1)]

    # Criar lista para status (1: aberta | 0: fechada)
    status = [0 for i in doors]

    # Apenas portas abertas
    only_open = []

    # Percorer todas portas alterando valores
    for m in doors:
        for index, k in enumerate(doors):
            # Alterar os valores das portas cujo resto da divisao k e m seja zero
            if k % m == 0:
                # Se aberta, feche
                if status[index]:
                    status[index] = 0
                # Se fechada, abra
                else:
                    status[index] = 1

        # Representação visual de todas portas
        # for d, s in zip(doors, status):
        #     print(f"{d:^10} | {s:^3} --")

    # Retornar somente portas abertas
    for d, s in zip(doors, status):
        if s == 1:
            only_open.append(d)

    return only_open


print(ndoors(100))
